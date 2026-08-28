#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Перевод документов QuickServe на русский.

Три слоя, по убыванию качества:

1. Память переводов (ru_memory.json) — выверенные вручную формулировки
   для самых частых фраз: предупреждения, шаги, заголовки разделов.
2. Правила — моменты затяжки, ссылки на процедуры, пункты регламента ТО,
   номера деталей: переводятся детерминированно, без участия модели.
3. Офлайн-модель en→ru (Argos/OPUS, CTranslate2) с «наведением» на
   правильную терминологию: часть выражений переписывается в источнике
   на однозначный английский, а в готовом русском тексте правятся
   характерные ошибки модели (все падежные формы).

Разметка Markdown, номера деталей, ссылки и иллюстрации не переводятся:
структура строки разбирается, переводится только текст.
"""
import collections
import glob
import html
import json
import os
import re
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from common import BUILD          # kb_build/ — общее состояние сборки
SCRIPTS = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(BUILD, "_cache")        # английские тексты (build_docs.py)
OUT = os.path.join(BUILD, "_cache_ru")       # русские тексты (их читают write_docs и web_data)
CATS = ("procedures", "tsb", "bulletin", "sti", "install_inst", "outlines")

# --------------------------------------------------------------- источник
# однозначные формулировки, которые модель переводит правильно
EN_REWRITE = [
    (r"\bengine harness\b", "engine wiring harness"),
    (r"\bOEM harness\b", "OEM wiring harness"),
    (r"\bharness connector\b", "wiring harness connector"),
    (r"\bpin (\d+)", r"contact \1"),
    (r"\bpins (\d+)", r"contacts \1"),
    (r"\bconnector pin\b", "connector contact"),
    (r"\bconnector pins\b", "connector contacts"),
    (r"\bsignal pin\b", "signal contact"),
    (r"\bsupply pin\b", "supply contact"),
    (r"\breturn pin\b", "return contact"),
    (r"\bdamaged pins\b", "damaged contacts"),
    (r"\bbent pins\b", "bent contacts"),
    (r"\bcapscrews?\b", "bolts"),
    (r"\bcap screws?\b", "bolts"),
    (r"\bRefer to Procedure\b", "See procedure"),
    (r"\bRefer to\b", "See"),
    (r"\bin Section (\w+)", r"in section \1"),
    (r"\bvalve clearance\b", "valve gap"),
    (r"\bintake clearance\b", "intake valve gap"),
    (r"\bexhaust clearance\b", "exhaust valve gap"),
    (r"\bend play\b", "axial clearance"),
    (r"\bdrive belt tension\b", "tension of the drive belt"),
    (r"\blet it idle\b", "run it at idle speed"),
    (r"\bidle the engine\b", "run the engine at idle speed"),
    (r"\bvalve cover\b", "valve cover assembly"),
    (r"\brocker lever\b", "valve rocker arm"),
    (r"\brocker arm\b", "valve rocker arm"),
    (r"\bcrankcase blowby\b", "crankcase gas blowby"),
    (r"\bengine timing pin\b", "crankshaft locking pin"),
    (r"\btiming pin\b", "crankshaft locking pin"),
    (r"\bbarring gear\b", "engine turning gear"),
    (r"\bkeyswitch\b", "ignition switch"),
    (r"\bkey switch\b", "ignition switch"),
    (r"\bwater pump weep hole\b", "water pump drain hole"),
    (r"\bshop talk\b", "practical note"),
    (r"\bmust be within specification\b", "must be within the specified limits"),
    (r"\bwithin specification\b", "within the specified limits"),
    (r"\bout of specification\b", "outside the specified limits"),
    (r"\bservice tool\b", "service tooling"),
    (r"\bhand tools\b", "hand tooling"),
    (r"\bsteam clean\b", "clean with steam"),
    (r"\bair filter\b", "air cleaner filter"),
    (r"\bfuel filter head\b", "fuel filter mounting head"),
    (r"\bdipstick\b", "oil level gauge"),
    (r"\bpressure cap\b", "radiator pressure cap"),
    (r"\bpetcock\b", "drain valve"),
    (r"\bdraincock\b", "drain valve"),
    (r"\bwastegate\b", "turbine bypass valve"),
    (r"\bgland nut\b", "packing nut"),
    (r"\bjam nut\b", "locknut"),
    (r"\binjectors?\b", "fuel injector"),
    (r"\bgauge\b", "measuring gauge"),
    (r"\bshop air\b", "compressed air supply"),
    (r"\bbore\b", "cylinder bore"),
    (r"\bset screws?\b", "locking screws"),
    (r"\bcompartment\b", "engine compartment"),
    (r"\bpress fitted\b", "pressed onto"),
    (r"\bpress-fitted\b", "pressed onto"),
    (r"\bkey movement\b", "woodruff key movement"),
    (r"\bcharging alternator\b", "alternator"),
    (r"\bbilge\b", "vessel bilge"),
    # --- правки по итогам разбора первого прогона -----------------------
    (r"(?<!compressed )\bair ?lines?\b", "compressed air line"),
    (r"\btest leads?\b", "test probe"),
    (r"\b(red|black|positive|negative|meter) leads?\b", r"\1 probe"),
    (r"\blead wires?\b", "wire"),
    (r"\bcalibration bench\b", "calibration test stand"),
    (r"\bbench calibration\b", "test stand calibration"),
    (r"\bbench harness\b", "test stand wiring harness"),
    (r"\bbench test\b", "test stand check"),
    (r"\bon a bench\b", "on a workbench"),
    (r"\bbenches\b", "test stands"),
    (r"\bbench\b", "test stand"),
    (r"\bcrossheads\b", "valve bridges"),
    (r"\bcrosshead\b", "valve bridge"),
    (r"\bcam shafts\b", "camshafts"),
    (r"\bcam shaft\b", "camshaft"),
    (r"\bcam followers\b", "tappets"),
    (r"\bcam follower\b", "tappet"),
    (r"\bhousings\b", "casings"),
    (r"\bhousing\b", "casing"),
    (r"\bthreads\b", "threading"),
    (r"\bthread ?locker\b", "threadlocking adhesive"),
    (r"\bmale union\b", "externally threaded fitting"),
    (r"\bfemale union\b", "internally threaded fitting"),
    (r"\bmale connector\b", "plug connector"),
    (r"\bfemale connector\b", "socket connector"),
    (r"\bmale Deutsch\b", "plug-type Deutsch"),
    (r"\bfemale Deutsch\b", "socket-type Deutsch"),
    (r"\bmale terminal\b", "plug terminal"),
    (r"\bfemale terminal\b", "socket terminal"),
    (r"\bblind hole puller\b", "puller for blind holes"),
    (r"\btearing the harness down\b", "disassembling the wiring harness"),
    (r"\btear down the\b", "disassemble the"),
    (r"\bpins ([A-Z]) and ([A-Z])\b", r"contacts \1 and \2"),
    (r"\bpins ([A-Z]), ([A-Z])\b", r"contacts \1, \2"),
    (r"\bpin ([A-Z])\b", r"contact \1"),
    (r"\bbetween the pins\b", "between the contacts"),
    (r"\bthrough the pins\b", "through the contacts"),
    (r"\bpin-to-pin\b", "contact-to-contact"),
    (r"\bdata link\b", "CAN data bus"),
    (r"\bdatalink\b", "CAN data bus"),
    (r"\bbackshell\b", "connector shell"),
    (r"\bbreakout\b", "harness branch"),
    (r"\bP-Clip\b", "P-clamp"),
    (r"\bwire loom\b", "wire sleeve"),
    (r"\bloom\b", "wire sleeve"),
    # bare harness -> wiring harness (после всех частных правил)
    (r"(?<!wiring )\bharness(es)?\b", r"wiring harness\1"),
    (r"\bwiring wiring harness\b", "wiring harness"),
]

# ------------------------------------------------------------ русский текст
# характерные ошибки модели: все падежные формы неверного слова -> верное
NOUN_FIX = {
    "инжектор": "форсунка", "инжектора": "форсунки", "инжектору": "форсунке",
    "инжектором": "форсункой", "инжекторе": "форсунке", "инжекторы": "форсунки",
    "инжекторов": "форсунок", "инжекторам": "форсункам", "инжекторами": "форсунками",
    "инжекторах": "форсунках", "инжекторе.": "форсунке.",
    "сковорода": "поддон", "сковороды": "поддона", "сковороде": "поддоне",
    "сковороду": "поддон", "сковородой": "поддоном",
    "клиренс": "зазор", "клиренса": "зазора", "клиренсу": "зазору",
    "клиренсом": "зазором", "клиренсе": "зазоре",
    "просвет": "зазор", "просвета": "зазора", "просвете": "зазоре",
    "просветом": "зазором",
    "шланг-хомут": "хомут шланга",
    "соединитель": "разъём", "соединителя": "разъёма", "соединителю": "разъёму",
    "соединителем": "разъёмом", "соединителе": "разъёме", "соединители": "разъёмы",
    "соединителей": "разъёмов", "соединителям": "разъёмам", "соединителями": "разъёмами",
    "соединителях": "разъёмах",
    "проводки": "проводов", "проводке": "проводах",
    "рокера": "коромысла", "рокер": "коромысло", "рокеру": "коромыслу",
    "рокером": "коромыслом", "рокере": "коромысле",
    "болтовое": "болтовое",
    "порядок": "процедура", "порядка": "процедуры",
    "картридж": "картридж",
    "прокладку": "прокладку",
    # --- второй разбор ------------------------------------------------
    "тягач": "съёмник", "тягача": "съёмника", "тягачу": "съёмнику",
    "тягачом": "съёмником", "тягаче": "съёмнике", "тягачи": "съёмники",
    "тягачей": "съёмников", "тягачам": "съёмникам", "тягачами": "съёмниками",
    "тягачах": "съёмниках",
    "сковородок": "поддон", "сковородки": "поддона", "сковородке": "поддоне",
    "сковородку": "поддон", "сковородком": "поддоном", "сковородка": "поддон",
    "клиренсы": "зазоры", "клиренсов": "зазоров", "клиренсам": "зазорам",
    "клиренсами": "зазорами", "клиренсах": "зазорах",
    "скамейка": "стенд", "скамейки": "стенда", "скамейке": "стенде",
    "скамейку": "стенд", "скамейкой": "стендом", "скамеек": "стендов",
    "скамья": "стенд", "скамье": "стенде", "скамью": "стенд",
    "зонд": "щуп", "зонда": "щупа", "зонду": "щупу", "зондом": "щупом",
    "зонде": "щупе", "зонды": "щупы", "зондов": "щупов",
    "жилье": "корпус", "жилья": "корпуса", "жилью": "корпусу",
    "жильем": "корпусом", "жильём": "корпусом", "жилища": "корпуса",
    "камшафт": "распредвал", "камшафта": "распредвала", "камшафту": "распредвалу",
    "камшафтом": "распредвалом", "камшафте": "распредвале", "камшафты": "распредвалы",
    "камшафтов": "распредвалов",
    "рокеры": "коромысла", "рокеров": "коромысел", "рокерам": "коромыслам",
    "рокерами": "коромыслами", "рокерах": "коромыслах",
    "нить": "резьба", "нити": "резьбы", "нитей": "резьб", "нитью": "резьбой",
    "нитям": "резьбам", "нитями": "резьбами", "нитях": "резьбах",
    "кроссхед": "мостик", "кроссхеда": "мостика", "кроссхеды": "мостики",
    "кроссхедов": "мостиков", "кроссхедами": "мостиками",
}

# замена корня с сохранением окончания: прилагательные и однотипные основы
STEM_FIX = [
    ("инжекторн", "форсуночн"),
    ("камшафтн", "распредвальн"),
    ("рокерн", "коромысленн"),
    ("тестов", "измерительн"),
]

# прилагательные с иным типом основы — только полными формами
ADJ_FIX = {}
for bad, good in (("мужск", "штырев"), ("женск", "гнездов"), ("сокетн", "гнездов")):
    for a, b in (("ый", "ой"), ("ий", "ой"), ("ой", "ой"), ("ого", "ого"), ("ому", "ому"),
                 ("им", "ым"), ("ым", "ым"), ("ом", "ом"), ("ая", "ая"),
                 ("ую", "ую"), ("ой", "ой"), ("ие", "ые"), ("ые", "ые"),
                 ("их", "ых"), ("ых", "ых"), ("ими", "ыми"), ("ыми", "ыми")):
        ADJ_FIX.setdefault(bad + a, good + b)

# замены по словосочетаниям (без учёта падежа — только точные совпадения)
PHRASE_FIX = [
    ("значение крутящего момента", "момент затяжки"),
    ("крутящий момент затяжки", "момент затяжки"),
    ("напряжение ремня", "натяжение ремня"),
    ("напряжение приводного ремня", "натяжение приводного ремня"),
    ("верхний мертвый центр", "верхняя мёртвая точка"),
    ("верхней мертвой точки", "верхней мёртвой точки"),
    ("верхнего мертвого центра", "верхней мёртвой точки"),
    ("мертвая точка", "мёртвая точка"),
    ("мертвой точки", "мёртвой точки"),
    ("сопло инжектора", "распылитель форсунки"),
    ("сопла инжектора", "распылителя форсунки"),
    ("топливный инжектор", "форсунка"),
    ("топливного инжектора", "форсунки"),
    ("смазочного масла", "моторного масла"),
    ("смазочное масло", "моторное масло"),
    ("смазочным маслом", "моторным маслом"),
    ("масляная сковорода", "масляный поддон"),
    ("жгута проводки", "жгута проводов"),
    ("жгут проводки", "жгут проводов"),
    ("ремня двигателя", "жгута проводов двигателя"),
    ("ремень двигателя", "жгут проводов двигателя"),
    ("часть №", "номер детали"),
    ("часть No", "номер детали"),
    ("номер части", "номер детали"),
    ("Часть №", "Номер детали"),
    ("раннего предупреждения", "предварительного уведомления"),
    ("Раннее предупреждение", "Предварительное уведомление"),
    ("сервисный инструментарий", "сервисный инструмент"),
    ("инструментарий", "инструмент"),
    ("клапанного рокера", "коромысла клапана"),
    ("клапанный рокер", "коромысло клапана"),
    ("рычаге рокера", "коромысле клапана"),
    ("рычага клапанного рокера", "коромысла клапана"),
    ("указатель уровня масла", "маслоизмерительный щуп"),
    ("турбинный байпасный клапан", "перепускной клапан турбины"),
    ("байпасный клапан турбины", "перепускной клапан турбины"),
    ("блокирующий штифт коленчатого вала", "фиксатор ВМТ"),
    ("стопорный штифт коленчатого вала", "фиксатор ВМТ"),
    ("замок зажигания в положение", "замок зажигания в положение"),
    ("выключатель зажигания", "замок зажигания"),
    ("зажигания выключатель", "замок зажигания"),
    ("газовый прорыв картера", "прорыв газов в картер"),
    ("прорыв газа картера", "прорыв газов в картер"),
    ("двигательный поворотный механизм", "валоповоротное устройство"),
    ("поворотная передача двигателя", "валоповоротное устройство"),
    # --- правки по итогам разбора первого прогона -----------------------
    ("испытательный стенд калибровки", "стенд калибровки"),
    ("сжатая воздушная линия", "линия сжатого воздуха"),
    ("сжатой воздушной линии", "линии сжатого воздуха"),
    ("линию сжатого воздуха", "линию сжатого воздуха"),
    ("вилочный разъём", "штыревой разъём"),
    ("разъём-вилка", "штыревой разъём"),
    ("разъём-розетка", "гнездовой разъём"),
    ("гнездовой соединитель", "гнездовой разъём"),
    ("оболочка разъёма", "корпус разъёма"),
    ("оболочку разъёма", "корпус разъёма"),
    ("ветвь жгута", "ответвление жгута"),
    ("ветви жгута", "ответвления жгута"),
    ("шина данных CAN", "шина данных CAN"),
    ("CAN-шина данных", "шина данных CAN"),
    ("проволочная втулка", "защитная оплётка"),
    ("проволочной втулки", "защитной оплётки"),
    ("проволочную втулку", "защитную оплётку"),
    ("съёмник для глухих отверстий", "съёмник для глухих отверстий"),
    ("наружная резьбовая арматура", "штуцер с наружной резьбой"),
    ("наружного резьбового фитинга", "штуцера с наружной резьбой"),
    ("наружный резьбовой фитинг", "штуцер с наружной резьбой"),
    ("внутренний резьбовой фитинг", "штуцер с внутренней резьбой"),
    ("Печать, пыль", "Уплотнение пылезащитное"),
    ("Печать, масло", "Уплотнение масляное"),
    ("Печать, вода", "Уплотнение водяное"),
    ("гарантийное заявление", "положение о гарантии"),
    ("Гарантийное заявление", "Положение о гарантии"),
    ("Резолюция", "Решение"),
    ("резолюция", "решение"),
    ("Обоснование", "Обоснование"),
    ("рабочий стол", "верстак"),
    ("рабочем столе", "верстаке"),
    # --- второй разбор ------------------------------------------------
    ("смазочный масляный поддон", "масляный поддон"),
    ("смазочного масляного поддона", "масляного поддона"),
    ("масляной сковородки", "масляного поддона"),
    ("масляная сковородка", "масляный поддон"),
    ("масляную сковородку", "масляный поддон"),
    ("соединительных стержней", "шатунов"),
    ("соединительные стержни", "шатуны"),
    ("соединительный стержень", "шатун"),
    ("соединительного стержня", "шатуна"),
    ("соединительном стержне", "шатуне"),
    ("соединительным стержнем", "шатуном"),
    ("поршневых соединительных стержней", "шатунов"),
    ("мужской адаптер шланга", "штуцер шланга с наружной резьбой"),
    ("мужского адаптера шланга", "штуцера шланга с наружной резьбой"),
    ("мужскому адаптеру шланга", "штуцеру шланга с наружной резьбой"),
    ("мужской адаптер трубы", "штуцер трубы с наружной резьбой"),
    ("мужской адаптер", "штуцер с наружной резьбой"),
    ("мужского адаптера", "штуцера с наружной резьбой"),
    ("мужскому адаптеру", "штуцеру с наружной резьбой"),
    ("женский адаптер", "штуцер с внутренней резьбой"),
    ("мужской союз", "штуцер с наружной резьбой"),
    ("смазочный масляный сковородок", "масляный поддон"),
    ("смазочного масляного сковородка", "масляного поддона"),
    ("тест-свинец", "измерительный щуп"),
    ("ремень безопасности проводов", "жгут проводов"),
    ("ремня безопасности проводов", "жгута проводов"),
    ("ремень безопасности", "жгут проводов"),
    ("ремня безопасности", "жгута проводов"),
    ("ремню безопасности", "жгуту проводов"),
    ("ремнём безопасности", "жгутом проводов"),
    ("ремнем безопасности", "жгутом проводов"),
    ("ремне безопасности", "жгуте проводов"),
    ("ремни безопасности", "жгуты проводов"),
    ("ремней безопасности", "жгутов проводов"),
    ("жгут проводов проводов", "жгут проводов"),
    ("жгута проводов проводов", "жгута проводов"),
    ("ремень поддержки жгута проводов", "кронштейн крепления жгута"),
    ("сокетный экипаж", "гнездовая головка"),
    ("нитевидного шкафчика", "фиксатора резьбы"),
    ("нитевидный шкафчик", "фиксатор резьбы"),
    ("нитевидный клей", "фиксатор резьбы"),
    ("нитевидного клея", "фиксатора резьбы"),
    ("нитевидным клеем", "фиксатором резьбы"),
    ("стрейдлокера", "фиксатора резьбы"),
    ("рокерные розетки", "гнёзда коромысел"),
    ("рокерных розеток", "гнёзд коромысел"),
    ("рычаги рокеров", "коромысла"),
    ("рычагов рокеров", "коромысел"),
    ("валы рокеров", "валики коромысел"),
    ("камеры-последователи", "толкатели"),
    ("камерам-последователям", "толкателям"),
    ("камер-последователей", "толкателей"),
    ("камеры-последователя", "толкателя"),
    ("Авиакомпания Starboard", "Starboard"),
    ("Авиакомпания", "Воздух"),
    ("КЕС", "CES"),
    ("охлаждающего агента", "охлаждающей жидкости"),
    ("охлаждающий агент", "охлаждающая жидкость"),
    ("охлаждающим агентом", "охлаждающей жидкостью"),
    ("охлаждающих веществ", "охлаждающих жидкостей"),
    ("охлаждающие вещества", "охлаждающие жидкости"),
    ("охлаждающего вещества", "охлаждающей жидкости"),
    ("охлаждающего оборудования", "охлаждающей жидкости"),
    ("сокетный штандарт", "гнездовая головка"),
    ("тестовый свинец", "измерительный щуп"),
    ("внешне резьбовый", "с наружной резьбой"),
    ("топливных инжекторных отверстий", "распылительных отверстий форсунок"),
    ("инжекторных отверстий", "распылительных отверстий форсунки"),
    ("инжекторных распылительных отверстий", "распылительных отверстий форсунки"),
    ("инжекторным удерживающим болтом", "болтом крепления форсунки"),
    ("соединительный съёмник", "съёмник муфты"),
    ("съёмник сцепления", "съёмник муфты"),
    ("измерительный зонд", "измерительный щуп"),
    ("испытательный щуп", "измерительный щуп"),
    ("дренажную вилку", "сливную пробку"),
    ("дренажную пробку", "сливную пробку"),
    ("дренажная пробка", "сливная пробка"),
    ("указанных пределах", "пределах спецификации"),
    ("указанные пределы", "пределы спецификации"),
    ("в пределах указанных пределов", "в пределах спецификации"),
    ("сливной кран", "сливной клапан"),
    ("уплотнительное кольцо O", "уплотнительное кольцо"),
    ("О-образное кольцо", "уплотнительное кольцо"),
    ("o-кольцо", "уплотнительное кольцо"),
    ("охлаждающего вещества", "охлаждающей жидкости"),
    ("охлаждающее вещество", "охлаждающая жидкость"),
    ("хладагент двигателя", "охлаждающая жидкость"),
    ("сжатого воздушного", "сжатого воздуха"),
    ("защитный кожух вентилятора", "диффузор вентилятора"),
    ("инъекционная инспекция", "проверка форсунок"),
    ("инъекционный", "форсуночный"),
    ("инъекционная", "форсуночная"),
    ("инъекционного", "форсуночного"),
    ("измерительный калибр", "калибр"),
    ("измерительного калибра", "калибра"),
    ("измерительным калибром", "калибром"),
    ("Гауге", "калибр"),
    ("гауге", "калибр"),
    (" пси", " psi"),
    ("Torque Wrench", "динамометрический ключ"),
    ("гаечного ключа плунжера", "плунжера динамометрического ключа"),
    ("воздушный привод Valve", "пневматический клапан"),
    ("Valve", "клапан"),
    ("Маффлер", "глушитель"),
    ("маффлер", "глушитель"),
    ("колея", "калибр"),
    ("Колея", "Калибр"),
    ("в запоре", "в отверстии"),
    ("наклеивания плунжеров", "заклинивания плунжеров"),
    ("поставке воздуха магазина", "магистрали сжатого воздуха"),
    ("поставку воздуха", "подачу воздуха"),
    ("чтения", "показаний"),
    ("наблюдайте за чтением", "снимите показания"),
    ("количество крутящего момента", "момент"),
    ("цилиндровое отверстие", "отверстие цилиндра"),
    ("двигательного отсека", "моторного отсека"),
    ("трюма судна", "трюма"),
    ("тестовый провод", "измерительный провод"),
    ("тестовые провода", "измерительные провода"),
    ("тестовых проводов", "измерительных проводов"),
    ("блокирующие винты", "установочные винты"),
    ("заклинившийся", "заклинивший"),
    ("сервисное инструментальное обеспечение", "сервисный инструмент"),
    ("инструментальное обеспечение", "инструмент"),
    ("измерительный прибор", "калибр"),
    ("измерительного прибора", "калибра"),
    ("измерительным прибором", "калибром"),
    ("измерительные приборы", "калибры"),
    ("Топливный форсунка", "Форсунка"),
    ("топливный форсунка", "форсунка"),
    ("топливный форсунки", "форсунки"),
    ("топливная форсунка", "форсунка"),
    ("топливной форсунки", "форсунки"),
    ("собранного форсунки", "собранной форсунки"),
    ("собранный форсунка", "собранная форсунка"),
    ("на помехи плунжеров", "на заклинивание плунжеров"),
    ("генератора зарядки", "генератора"),
    ("зарядного генератора", "генератора"),
    ("генератор зарядки", "генератор"),
    ("движение ключа", "перемещение шпонки"),
    ("движения ключа", "перемещения шпонки"),
    ("шкив был нажат на вал", "шкив был напрессован на вал"),
    ("нажат на вал", "напрессован на вал"),
    ("гарантийное заявление", "положение о гарантии"),
    ("Гарантийное заявление", "Положение о гарантии"),
    ("анонсировано введение", "объявлено о введении"),
    ("только для промышленности", "только промышленное исполнение"),
]

# вежливая форма повелительного наклонения
IMPERATIVE = {
    "Проверь": "Проверьте", "Сними": "Снимите", "Установи": "Установите",
    "Затяни": "Затяните", "Ослабь": "Ослабьте", "Измерь": "Измерьте",
    "Очисти": "Очистите", "Замени": "Замените", "Отрегулируй": "Отрегулируйте",
    "Убедись": "Убедитесь", "Отключи": "Отключите", "Подключи": "Подключите",
    "Отсоедини": "Отсоедините", "Присоедини": "Присоедините", "Смажь": "Смажьте",
    "Запусти": "Запустите", "Останови": "Остановите", "Слей": "Слейте",
    "Залей": "Залейте", "Осмотри": "Осмотрите", "Сравни": "Сравните",
    "Запиши": "Запишите", "Повтори": "Повторите", "Выполни": "Выполните",
    "Используй": "Используйте", "Нажми": "Нажмите", "Поверни": "Поверните",
    "Вставь": "Вставьте", "Вынь": "Выньте", "Утилизируй": "Утилизируйте",
    "Продуй": "Продуйте", "Просуши": "Просушите", "Заменяй": "Заменяйте",
    "Держи": "Держите", "Следи": "Следите", "Не используй": "Не используйте",
    "Не снимай": "Не снимайте", "Не допускай": "Не допускайте",
}

UNIT_FIX = [
    (r"\bн[·•\-]?м\b", "Н·м"), (r"\bN[·•]m\b", "Н·м"), (r"\bn[·•]m\b", "Н·м"),
    (r"\bft-lb\b", "фунт-фут"), (r"\bin-lb\b", "фунт-дюйм"), (r"\bin-oz\b", "унция-дюйм"),
    (r"\blb-ft\b", "фунт-фут"), (r"\bft\.lb\b", "фунт-фут"),
    (r"\bдюйм\b", "дюйм"), (r"\bмм\b", "мм"),
    (r"\bОм\b", "Ом"), (r"\bohms?\b", "Ом"), (r"\bkOhms?\b", "кОм"),
]

PROTECT = re.compile(
    r"(!\[\[[^\]]+\]\]|`[^`]+`|https?://\S+|\b\d{6,8}\b|\b[A-Z]{2,}\d{2,}[A-Z0-9\-]*\b)")
WIKI = re.compile(r"\[\[([^\]\|]+)(\\?\|)([^\]]*)\]\]")
SENT = re.compile(r"(?<=[.!?:])\s+")
# разделитель ячеек таблицы: экранированный \| внутри wiki-ссылки не режем
CELL = re.compile(r"(?<!\\)\|")
# markdown-ссылка: адрес не трогаем, подпись переводим (если это не сам адрес)
MDLINK = re.compile(r"(?<!\!)\[([^\[\]]*)\]\(([^()\s]+)\)")
TOKEN = re.compile(r"\[\[([^\]\|]+)(\\?\|)([^\]]*)\]\]"
                   r"|(?<!\!)\[([^\[\]]*)\]\(([^()\s]+)\)"
                   r"|(!?\[\[[^\]\|]+\]\])")


class Engine:
    """Офлайн-перевод en->ru пакетами."""

    def __init__(self):
        import ctranslate2
        import sentencepiece as spm
        pkg = glob.glob("/root/.local/share/argos-translate/packages/translate-en_ru*/")[0]
        self.sp = spm.SentencePieceProcessor(pkg + "sentencepiece.model")
        self.tr = ctranslate2.Translator(pkg + "model", device="cpu",
                                         intra_threads=4, compute_type="int8")

    def batch(self, texts):
        toks = [self.sp.encode(t, out_type=str) for t in texts]
        res = self.tr.translate_batch(toks, beam_size=1, max_batch_size=8192,
                                      batch_type="tokens")
        return [self.sp.decode(r.hypotheses[0]) for r in res]


# ------------------------------------------------------------------ правила
TORQUE = re.compile(r"^([\d.,]+)\s*n[·•]m\s*\[\s*([\d.,]+)\s*(ft-lb|in-lb|in-oz)\s*\]$", re.I)
STEP = re.compile(r"^STEP\s+([0-9]+[A-Za-z]?(?:-[0-9]+)?)\.?$", re.I)
REFPROC = re.compile(r"^Refer to Procedure ([\w\-]+) in Section ([\w\-]+)\.?$", re.I)
CHECKITEM = re.compile(r"^(.+?)\s+-\s+(Check|Clean|Drain|Replace|Inspect|Adjust|Lubricate|Test)$", re.I)
ACTION_RU = {"check": "проверить", "clean": "очистить", "drain": "слить",
             "replace": "заменить", "inspect": "осмотреть", "adjust": "отрегулировать",
             "lubricate": "смазать", "test": "проверить"}
UNIT_RU = {"ft-lb": "фунт-фут", "in-lb": "фунт-дюйм", "in-oz": "унция-дюйм"}


def rule_translate(text, memory, comp_ru):
    """Детерминированный перевод типовых строк. None — если правило не подошло."""
    t = text.strip()
    if t in memory:
        return memory[t]
    low = t.lower()
    if low in memory:
        return memory[low]
    bare = t.strip(" .:;")
    if bare and bare.lower() in memory:
        return memory[bare.lower()] + t[len(bare):]
    m = STEP.match(t)
    if m:
        return "ШАГ " + m.group(1).upper() + "."
    m = TORQUE.match(t)
    if m:
        return f"{m.group(1)} Н·м [{m.group(2)} {UNIT_RU.get(m.group(3).lower(), m.group(3))}]"
    m = REFPROC.match(t)
    if m:
        return f"См. процедуру {m.group(1)} в разделе {m.group(2)}."
    m = CHECKITEM.match(t)
    if m:
        comp = comp_ru.get(m.group(1).strip().lower())
        if comp:
            return f"{comp} — {ACTION_RU[m.group(2).lower()]}"
    if re.fullmatch(r"[\d\W]+", t):
        return t
    return None


def post_edit(ru):
    ru = ru.replace("\u00ad", "").replace("\u200b", "")
    for a, b in PHRASE_FIX:
        if a in ru:
            ru = ru.replace(a, b)
        au = a[0].upper() + a[1:]
        if au != a and au in ru:
            ru = ru.replace(au, b[0].upper() + b[1:])
    words = dict(NOUN_FIX)
    words.update(ADJ_FIX)
    ru = re.sub(r"\b(" + "|".join(map(re.escape, words)) + r")\b",
                lambda m: words[m.group(1)], ru)
    ru = re.sub(r"\b(" + "|".join(w[0].upper() + w[1:] for w in words) + r")\b",
                lambda m: (lambda v: v[0].upper() + v[1:])(
                    words[m.group(1)[0].lower() + m.group(1)[1:]]), ru)
    for bad, good in STEM_FIX:
        ru = re.sub(r"\b" + bad + r"([а-яё]*)",
                    lambda m: good + m.group(1), ru)
        ru = re.sub(r"\b" + bad[0].upper() + bad[1:] + r"([а-яё]*)",
                    lambda m: good[0].upper() + good[1:] + m.group(1), ru)
    for a, b in IMPERATIVE.items():
        ru = re.sub(r"(?<![\w])" + re.escape(a) + r"(?=[\s,.:;!?])", b, ru)
    for pat, rep in UNIT_FIX:
        ru = re.sub(pat, rep, ru)
    ru = ru.replace(" No ", " № ").replace("№ детали", "номер детали")
    ru = re.sub(r"\s+([,.;:])", r"\1", ru)
    ru = re.sub(r"\(\s+", "(", ru).replace(" )", ")")
    return ru.strip()


def pre_edit(en):
    en = en.replace("\u00ad", "").replace("\u200b", "")
    for pat, rep in EN_REWRITE:
        en = re.sub(pat, rep, en, flags=re.I if pat.islower() else 0)
    return en


# ---------------------------------------------------------- разбор markdown
def split_line(line):
    """(префикс, переводимый текст, суффикс-функция сборки)."""
    s = line.rstrip("\n")
    if not s.strip():
        return None
    if s.lstrip().startswith("!["):
        return None
    m = re.match(r"^(\s*(?:[-*]|\d+\.)\s+)(.*)$", s)
    if m:
        return (m.group(1), m.group(2), "")
    m = re.match(r"^(#{1,6}\s+)(.*)$", s)
    if m:
        return (m.group(1), m.group(2), "")
    m = re.match(r"^(>\s*(?:\[!\w+\][+-]?\s*)?)(.*)$", s)
    if m and m.group(2).strip():
        return (m.group(1), m.group(2), "")
    if s.strip().startswith("|"):
        return None          # таблицы разбираются по ячейкам отдельно
    if s.strip() in ("---", "***"):
        return None
    return ("", s, "")


def segments_of(md):
    """Все переводимые куски текста файла: (тип, координата, текст)."""
    out = []
    for i, line in enumerate(md.split("\n")):
        if line.strip().startswith("|"):
            cells = CELL.split(line.strip().strip("|"))
            for j, c in enumerate(cells):
                c = c.strip()
                if c and not re.fullmatch(r":?-{2,}:?", c):
                    out.append(("cell", (i, j), c))
            continue
        p = split_line(line)
        if not p:
            continue
        out.append(("line", i, p[1]))
    return out


def translatable(text):
    """Разбирает строку на части: переводимый текст и защищённые куски."""
    parts = []
    pos = 0
    for m in TOKEN.finditer(text):
        parts.append(("t", text[pos:m.start()]))
        if m.group(6) is not None:
            # ссылка без подписи: имя заметки переводить нельзя
            parts.append(("keep", m.group(6)))
        elif m.group(1) is not None:
            parts.append(("wiki", (m.group(1), m.group(2))))
            parts.append(("t", m.group(3)))
            parts.append(("wikiend", ""))
        else:
            label, url = m.group(4), m.group(5)
            if label.strip() and not re.match(r"^\s*(https?://|www\.|mailto:)", label):
                parts.append(("mdopen", ""))
                parts.append(("t", label))
                parts.append(("mdclose", url))
            else:
                parts.append(("keep", "[" + label + "](" + url + ")"))
        pos = m.end()
    parts.append(("t", text[pos:]))
    return parts


def dict_path(name):
    """Словарь терминологии: рядом со скриптами или в состоянии сборки."""
    for base in (SCRIPTS, BUILD):
        p = os.path.join(base, name)
        if os.path.exists(p):
            return p
    return ""


def build_memory():
    """Память переводов: выверенные фразы + названия документов и деталей."""
    mem = {}
    for fn in ("ru_docs.json", "ru_parts.json", "ru_memory.json"):
        path = dict_path(fn)
        if not path:
            continue
        for k, v in json.load(open(path, encoding="utf-8")).items():
            k = (k or "").strip()
            if k and v:
                mem[k] = v
                mem.setdefault(k.lower(), v)
                bare = k.strip("*").strip()
                if bare and bare != k:
                    mem.setdefault(bare, v.strip("*").strip())
                    mem.setdefault(bare.lower(), v.strip("*").strip())
    return mem


def build_component_ru():
    """Названия узлов для пунктов регламента: «Water Pump - Check»."""
    comp = {}
    for fn in ("ru_docs.json", "ru_parts.json", "ru_glossary.json"):
        path = dict_path(fn)
        if not path:
            continue
        for k, v in json.load(open(path, encoding="utf-8")).items():
            if k and v:
                comp[k.strip().lower()] = v
    return comp


def translate_text(text, resolve):
    """Собирает перевод строки: ссылки и защищённые куски сохраняются."""
    out = []
    for kind, val in translatable(text):
        if kind == "wiki":
            out.append("[[" + val[0] + val[1])
            continue
        if kind == "wikiend":
            out.append("]]")
            continue
        if kind == "mdopen":
            out.append("[")
            continue
        if kind == "mdclose":
            out.append("](" + val + ")")
            continue
        if kind == "keep":
            out.append(val)
            continue
        if not val.strip():
            out.append(val)
            continue
        pieces = []
        for sent in SENT.split(val):
            if not sent.strip():
                continue
            pieces.append(resolve(sent.strip()))
        out.append(" ".join(pieces))
    return "".join(out)


def main():
    t0 = time.time()
    only = sys.argv[1] if len(sys.argv) > 1 else None
    memory = build_memory()
    comp_ru = build_component_ru()
    mt_path = os.path.join(BUILD, "_mt_cache.json")
    mt_cache = json.load(open(mt_path, encoding="utf-8")) if os.path.exists(mt_path) else {}

    force = "--force" in sys.argv
    files = []
    for cat in CATS:
        if only and only != "--force" and cat != only:
            continue
        for f in sorted(glob.glob(os.path.join(CACHE, cat, "*.md"))):
            # уже переведённые документы не трогаем: перевод — долгий прогон,
            # а готовые тексты уже выверены (см. fix_translation_marks.py)
            if not force and os.path.exists(os.path.join(OUT, cat, os.path.basename(f))):
                continue
            files.append(f)
    print(f"файлов к переводу: {len(files)}"
          + ("" if force else " (уже переведённые пропущены)"), flush=True)
    if not files:
        print("нечего переводить"); return

    # ------------------------------------------------- что нужно перевести
    need = set()
    parsed = {}
    for path in files:
        md = open(path, encoding="utf-8").read()
        segs = segments_of(md)
        parsed[path] = (md, segs)
        for _kind, _coord, text in segs:
            for k, val in translatable(text):
                if k != "t" or not val.strip():
                    continue
                for sent in SENT.split(val):
                    sent = sent.strip()
                    if not sent:
                        continue
                    if rule_translate(sent, memory, comp_ru) is not None:
                        continue
                    pre = pre_edit(sent)
                    if pre not in mt_cache:
                        need.add(pre)
    print(f"уникальных предложений для модели: {len(need)} "
          f"(в кэше уже {len(mt_cache)})", flush=True)

    # ----------------------------------------------------------- перевод
    if need:
        eng = Engine()
        todo = sorted(need, key=len)
        step = 1500
        done = 0
        for i in range(0, len(todo), step):
            chunk = todo[i:i + step]
            try:
                res = eng.batch(chunk)
            except Exception as exc:                     # noqa: BLE001
                print("сбой пакета:", exc, flush=True)
                res = chunk
            for en, ru in zip(chunk, res):
                mt_cache[en] = ru
            done += len(chunk)
            if done % 6000 < step:
                el = time.time() - t0
                print(f"  переведено {done}/{len(todo)}, {el:.0f} c, "
                      f"{done/max(el,1):.0f} предл/с", flush=True)
                json.dump(mt_cache, open(mt_path, "w", encoding="utf-8"),
                          ensure_ascii=False)
        json.dump(mt_cache, open(mt_path, "w", encoding="utf-8"), ensure_ascii=False)

    # -------------------------------------------------------- сборка файлов
    def resolve(sent):
        r = rule_translate(sent, memory, comp_ru)
        if r is not None:
            return r
        raw = mt_cache.get(pre_edit(sent))
        return post_edit(raw) if raw else sent

    written = 0
    for path, (md, segs) in parsed.items():
        lines = md.split("\n")
        cells = collections.defaultdict(dict)
        for kind, coord, text in segs:
            ru = translate_text(text, resolve)
            if kind == "line":
                orig = lines[coord]
                p = split_line(orig)
                lines[coord] = (p[0] if p else "") + ru
            else:
                cells[coord[0]][coord[1]] = ru
        for i, cmap in cells.items():
            row = lines[i].strip()
            keep_l = "| " if row.startswith("|") else ""
            parts = CELL.split(row.strip().strip("|"))
            for j, v in cmap.items():
                if j < len(parts):
                    parts[j] = " " + v + " "
            lines[i] = "|" + "|".join(parts) + "|" if keep_l else "|".join(parts)
        cat = os.path.basename(os.path.dirname(path))
        dst = os.path.join(OUT, cat, os.path.basename(path))
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        open(dst, "w", encoding="utf-8").write("\n".join(lines))
        written += 1
        if written % 400 == 0:
            print(f"  собрано {written}/{len(parsed)}", flush=True)

    print(f"готово: {written} документов, кэш перевода {len(mt_cache)} фраз, "
          f"{time.time()-t0:.0f} c")


if __name__ == "__main__":
    main()
