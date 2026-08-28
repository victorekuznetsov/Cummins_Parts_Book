---
aliases:
  - "Регулировка клапанного механизма (OBC)"
type: "Процедура"
doc: "20-003-006-om"
title_en: "Overhead Set (OBC)"
title_ru: "Регулировка клапанного механизма (OBC)"
modified: "2017-11-10"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "3666120"
parts:
  - "3090007"
figures: 24
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-003-006-om.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/20-003-006-om.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/20"
  - "перевод/машинный"
---

# Overhead Set (OBC)
**Регулировка клапанного механизма (OBC)**

> [!abstract] Процедура · `20-003-006-om`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[3666120 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Operation and Maintenance Manual|3666120]]
> **Секции:** Section 7 - Maintenance Procedures at 1500 Hours or 1 Year
> **Даты:** изменён 2017-11-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-003-006-om.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/20-003-006-om.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

с форсункой механического управления

Клапаны и форсунка **должны быть правильно отрегулированы для эффективного функционирования двигателя. Регулировка клапана и форсунки **должна выполняться с использованием значений, перечисленных в этой процедуре.

Cummins Inc. Было установлено, что двигатели в большинстве применений **не **испытывают значительный износ клапана / форсунки. Рекомендуется регулировка клапана и форсунки производится только *, когда форсунка снят или когда другие ремонтные работы нарушают работу клапанного поезда.

Если регулировка клапана и форсунки проверяется во время устранения неполадок или до рекомендуемого интервала технического обслуживания, регулировка не требуется, если измерения находятся в пределах пределов перепроверки.

![[03400025.png]]

с форсункой электронного управления

Клапаны **должны быть правильно отрегулированы для эффективного функционирования двигателя. Корректировка клапана **должна выполняться с использованием значений, перечисленных в этой процедуре.

Для двигателей с топливным форсункой с электронным приводом периодическая регулировка клапана **не требуется. Рекомендуется регулировать клапаны **только при снятии топливного форсунка.

![[03400145.png]]

### Подготовительные операции

с форсункой механического управления

- Удалите крышку рычага клапанного клапана и все связанные с ним компоненты.[[20-003-011-om — Rocker Lever Cover|См. процедуру 003-011 в разделе A.]]

с форсункой электронного управления

> [!danger] ОПАСНО
> При работе с пароочистителем надевайте защитные очки или щиток и защитную одежду. Горячий пар может привести к травмам.

> [!danger] ОПАСНО
> В зависимости от обстоятельств, дизельное топливо является легковоспламеняющимся. При осмотре или выполнении обслуживания или ремонта топливной системы, чтобы уменьшить вероятность пожара и в результате серьезных травм, смерти или повреждения имущества, никогда не курите и не допускайте искр или пламени (например, пилотные огни, электрические выключатели или сварочное оборудование) в рабочей зоне.

> [!danger] ОПАСНО
> Давление топлива в линии достаточно, чтобы проникнуть в кожу и нанести серьезный вред здоровью. Носите перчатки и защитную одежду.

> [!danger] ОПАСНО
> Давление в топливной системе высокого давления никогда не должно измеряться с помощью механического калибра. Возможны значения давления топлива более 1724 бар \[25 000 psi\]. При высоком давлении механическая измерительная манометрия может выйти из строя, вызывая утечку топлива высокого давления, что приводит к травмам и имущественному ущербу.

> [!danger] ОПАСНО
> При очистке растворителями, кислотами и щелочными составами соблюдайте указания их изготовителя. Работайте в защитных очках и защитной одежде, чтобы снизить риск травмы.

> [!danger] ОПАСНО
> При работе со сжатым воздухом применяйте защиту глаз и лица. Разлетающиеся частицы и грязь могут привести к травме.

> [!warning] ОСТОРОЖНО
> При отсоединении и снятии топливных магистралей, замене фильтров и прокачке системы не допускайте пролива и слива топлива в трюм. Не бросайте фильтрующие элементы в трюм. Топливо и топливные фильтры утилизируйте по местным природоохранным требованиям.

> [!warning] ОСТОРОЖНО
> Очень небольшое количество грязи и мусора может быть очень вредным для топливного форсунка и колбочек сидений на топливных форсунках высокого давления. Для поддержания топливных соединений в чистоте во время удаления и установки требуется дополнительная осторожность.

- Очистите все фитинги и компоненты паром или растворителем перед удалением из двигателя.
- Подключите электронный сервисный инструмент INSITETM и проверьте, что давление топлива снизилось, контролируя давление топлива.
- Удалите линию подачи топливного форсунка и линии подачи.[[20-006-051-om — Injector Supply Lines (High Pressure)|См. процедуру 006-051 в разделе A.]]
- Снимите крышку рычага клапанного клапана.[[20-003-011-om — Rocker Lever Cover|См. процедуру 003-011 в разделе A.]]

### Регулировка

с форсункой механического управления

> [!note] Примечание
> Вал заграждения устройства поворачивается примерно за два оборота до того, как двигатель начинает поворачиваться. Запрещающее устройство будет **не** поворачивать двигатель в противоположном направлении от нормального вращения.

Нажмите вал и поверните запирающее устройство **против часовой стрелки** до тех пор, пока отметка «А» на шкиве не будет выровнена с отметкой, которая отливается в босса для дополнительного уплотнения привода на передней крышке передач.

Определите цилиндр в позиции для набора клапанов.

| клапан установила марку | Проверьте положение клапан |
|---|---|
| А. | 1, 6 |
| B | 2, 5 |
| C | 3, 4 |

![[01400086.png]]

Если клапанные клапанные качалки были удалены, используйте этот шаг для определения цилиндра, который должен быть установлен.

Смазать регулировочную винтовую резьбу чистым моторным маслом перед внесением регулировок клапана и форсунки.

Все регулирующие винты **должны быть свободны на всех цилиндрах, а толкатели **должны оставаться в выравнивании.

Выполните этот шаг на обоих цилиндрах, чтобы проверить.

Держите оба рычага качения против клапанных мостиков. Поверните регулирующие винты, пока они не коснутся толкателей. Поверните каштаны, пока они не коснутся рычагов.

Толкательные стержни будут иметь такую же высоту над верхней частью корпуса рычага качения клапанного клапана на цилиндре, готовом к регулировке клапана.

![[03400001.png]]

Если рычаги коромысла были удалены **не**, поверните рычаги коромысла клапана на двух цилиндрах, о которых идет речь. Используйте диаграмму и выберите правильный цилиндр для настройки.

![[03400025.png]]

Используйте диаграмму для определения клапана и форсунки, который готов к настройке.

Настройка может начинаться на любом отметке клапана.

В примере, предположим, что знак A выровнен, а высоты толкателя указывают на то, что один клапан на цилиндре № 1 полностью открыт, а оба клапана на цилиндре № 6 полностью закрыты. На диаграмме также показано, что клапаны на цилиндре № 2 и форсунка на цилиндре 3 готовы к регулировке.

После регулировки заблокируйте двигатель на знак B. Настройка клапанов на цилиндре № 4 и регулировка форсунки на цилиндре № 6.

![[06400001.png]]

| Корректировка клапана (Initial Set) |  |  |  |
|---|---|---|---|
| Справочная точка | мм |  | в |
| А. | 0.81 | выхлоп | 0.032 |
| B | 0.36 | принимать | 0.014 |

![[06400003.png]]

Убедитесь, что клапанный мост прочно установлен на кончиках стеблей клапана.

Убедитесь, что калибр для щупальца находится под центром шара и розетки, или розетка может качать или наклоняться, что приводит к неправильной регулировке. Чтобы избежать ложных показаний, держите поворотную ногу плоской, чтобы избежать связывания при проверке ресницы.

Используйте инструментальную часть 3824901. Выберите калибр для правильной спецификации ресниц клапана. Вставить калибр между розеткой клапанного клапана и клапанным мостиком.

![[03400018.png]]

Ниже описаны два различных метода установления зазора клапанной ресницы. Можно использовать любой метод. Метод крутящего момента гаечный ключ оказался самым * последовательным.

#### Метод крутящего момента:

- Используйте служебную оснастку, номер детали 3376592, дюймовый гаечный ключ, чтобы затянуть регулирующий винт до.68 Н•м \[6 фунт-дюйм\] крутящего момента против калибра для считывания.

#### Метод чувств:

- Используйте нут драйвера и поверните регулировочный винт **только** до тех пор, пока рычаг не коснется датчика измерения щупальца.

![[03400023.png]]

Убедитесь, что части находятся в выравнивании. Затяните регулирующий винт и выдавите масло из клапанного поезда.

Устраните регулировочный винт, по крайней мере, один полный оборот.

Вставить датчик измерения между клапанным клапаном, на котором расположена розетка, и клапанным мостиком.

Используйте крутящий момент, номер детали 3376592, и затяните регулировочный винт.

> [!tip] Момент затяжки
> 0.68 Н·м [6 фунт-дюйм]

Удалите измеритель щупальца.

![[03400023.png]]

Винт регулировки **не должен** поворачиваться, когда затягивается локон. Крутящий момент локона может быть применен с или без адаптера гаечного ключа, номер детали 3163196.

Затяните локон.

| Момент затяжки |  |
|---|---|
| **Регулировка номера части винта** | 168306 |
| С адаптером | 48 Н•м[35 фунт-фут] |
| Без адаптера | 60 Н•м[44 фут-лб] |
| **Регулировка номера части винта** | [[3090007]] |
| С адаптером | 84 Н•м[62 фут-лб] |
| Без адаптера | 105 Н•м[77 фунт-фут] |

Попробуйте вставить датчик измерения щупальца, который составляет 0,03 мм \[0,001 в\] толще. Стрелка клапана **не** правильна, когда более толстый калибр подойдет.

Повторите процесс настройки, пока не будет получена правильная ресница.

![[03400018.png]]

Используйте крутящий момент гаечного ключа, чтобы затянуть топливный форсунок клапана качели рычага регулирования винта. Если винт болтается во время установки, отремонтируйте винт и рычаг по мере необходимости.

Убедитесь, что части находятся в выравнивании. Затянуть регулировочный винт и выжать масло из топливного форсунка. Это начальная регулировка для предварительной загрузки форсунки.

> [!tip] Момент затяжки
> 28 Н·м [248 фунт-дюйм]

Устраните регулировочный винт, по крайней мере, одну революцию.

Закрутите регулировочный винт снова до конечной настройки.

> [!tip] Момент затяжки
> 19 Н·м [168 фунт-дюйм]

Зубной ключ должен быть откалиброван, иметь разрешение 0,28 Н•м \[2,5 фунт-дюйм\] и иметь диапазон от 17 до 23 Н•м \[150 до 200 фунт-дюйм\].

![[03400019.png]]

Держите винт регулировки в этом положении. Регулирующий винт **не должен** поворачиваться, когда затягивается локон.

Закрепить шприц на следующие значения:

Для способа крутящего момента (с адаптером) используйте адаптер гаечного ключа крутящего момента, часть номер ST-669.

| Момент затяжки |  |
|---|---|
| **Регулировка номера части винта** | 168306 |
| С адаптером | 48 Н•м[35 фунт-фут] |
| Без адаптера | 60 Н•м[44 фут-лб] |
| **Регулировка номера части винта** | [[3090007]] |
| С адаптером | 84 Н•м[62 фут-лб] |
| Без адаптера | 105 Н•м[77 фунт-фут] |

![[03400020.png]]

с форсункой электронного управления

> [!warning] ОСТОРОЖНО
> Чтобы уменьшить вероятность повреждения двигателя, используйте защитную крышку головки цилиндра, чтобы предотвратить попадание инструментов в полость крана.

Установите защитную крышку головки цилиндра, номер детали 4918282, в отверстие проточной трубки.

![[22400276.png]]

Вал заграждения устройства поворачивается примерно за два оборота до того, как двигатель начинает поворачиваться. Запрещающее устройство будет **не** поворачивать двигатель в противоположном направлении от нормального вращения.

![[01400081.png]]

TDC представляет собой Top Dead Center для цилиндров 1 или 6. Эта отметка будет использоваться для установки клапанов на двигатели с электронным топливным форсункой. Это позволит установить все клапаны в двух положениях. Игнорируйте знаки A, B и C при использовании этой процедуры.

Вставьте вал и поверните запирающее устройство, пока отметка TDC на шкиве не выровняется с отметкой, которая отливается в босса для дополнительного уплотнения привода на передней крышке передач.

![[03400172.png]]

Количество резьбы, видимой над корректирующим гайкой, будет **не** одинаковым. На винте регулирования впуска будет больше резьбы, чем на винте регулирования выхлопных газов.

Если клапанные клапанные качалки были удалены, используйте этот шаг для определения цилиндра, который должен быть установлен.

Все регулирующие винты **должны быть свободны на всех цилиндрах, а толкатели **должны оставаться в выравнивании.

Выполните этот шаг на обоих цилиндрах, чтобы проверить.

Держите оба рычага качения против клапанных мостиков. Поверните регулирующие винты, пока они не коснутся толкателей. Поверните каштаны, пока они не коснутся рычагов.

Толкательные стержни будут иметь ту же высоту над верхней частью корпуса рычага качения клапана на клапанах, которые должны быть свободными.

![[03400163.png]]

Если оба рычага цилиндра № 1 свободны, переходите к следующему шагу. Если рычаги цилиндра No1 не рыхли, поверните коленчатый вал на 360 градусов и переходите к следующему шагу.

Если цилиндр № 1 находится на TDC, и оба рычага коромысла свободны, ресница клапана (накладной комплект) может быть проверена на следующих рычагах коромысла:

- E = выхлоп
- I = прием

1I, 1E, 2I, 3E, 4I и 5E

![[03400236.png]]

| Корректировка клапана (Initial Set) |  |
|---|---|
| Выхлоп (А) | Взятие (B) |
| 0,69 мм \[0,027 in\] | 0,36 мм \[0,014 в\] |

| клапан Recheck лимиты |  |  |  |
|---|---|---|---|
|  | мм |  | в |
| Впускной клапан | 0.280 | Мин | 0.011 |
|  | 0.430 | Макс | 0.017 |
| Выпускной клапан | 0.610 | Мин | 0.027 |
|  | 0.762 | Макс | 0.030 |

![[03400147.png]]

Используйте сервисное оборудование, Номер детали 3163171 (впуск) или Номер детали 3163172 (выхлоп). Выберите калибр для правильной спецификации ресниц клапана. Вставить калибр между розеткой клапанного клапана и клапанным мостиком.

Убедитесь, что клапанный мост прочно установлен на кончиках стеблей клапана.

Убедитесь, что калибр для щупальца находится под центром шара и розетки, или розетка может качать или наклоняться, что приводит к неправильной регулировке. Чтобы избежать ложных показаний, держите поворотную ногу плоской, чтобы избежать связывания при проверке ресницы.

![[03400164.png]]

Ниже описаны два различных метода установления зазора клапана:

- Метод крутящего момента - Используйте номер детали 3376592, крутящий момент дюйма, чтобы затянуть регулирующий винт до 0,68 Н•м \[6 фунт-дюйм\] крутящего момента против измерителя щупальца.
- Способ ощущений - Используйте отвертку и включите регулирующий винт **только**, пока рычаг не коснется измерителя щупальца.

Можно использовать любой метод. Метод крутящего момента оказался наиболее последовательным.

![[03400165.png]]

Для установки клапанов с использованием метода гаечного ключа крутящего момента выполните следующие шаги:

Убедитесь, что части находятся в выравнивании. Затяните регулирующий винт и выдавите масло из клапанного поезда.

Устраните регулировочный винт, по крайней мере, одну революцию.

Вставить датчик измерения щупальца между розеткой рычага клапанного клапана и клапанным мостиком.

Используйте крутящий момент, номер детали 3376592, и затяните регулирующий винт.

Удалите калибр для щупальца.

> [!tip] Момент затяжки
> 0.68 Н·м [6 фунт-дюйм]

![[03400164.png]]

Чтобы установить клапаны с помощью метода ощупывания, выполните следующие шаги:

Винт регулировки **не должен** поворачиваться, когда затягивается локон. Крутящий момент локона может быть применен с или без адаптера гаечного ключа, номер детали 3163196.

Затяните локон.

Регулирующий винт **не должен** поворачиваться, когда затягивается локон.

Для способа крутящего момента (с адаптером) используйте адаптер гаечного ключа крутящего момента, часть номер ST-669.

| Момент затяжки |  |
|---|---|
| **Регулировка номера части винта** | 168306 |
| С адаптером | 48 Н•м[35 фунт-фут] |
| Без адаптера | 60 Н•м[44 фут-лб] |
| **Регулировка номера части винта** | [[3090007]] |
| С адаптером | 84 Н•м[62 фут-лб] |
| Без адаптера | 105 Н•м[77 фунт-фут] |

Попробуйте вставить датчик измерения щупальца, который составляет 0,03 мм \[0,001 в\] толще. Стрелка клапана **не** правильна, когда более толстый калибр подойдет.

Повторите процесс корректировки до получения надлежащего разрешения.

Используйте инструмент барринга для вращения коленчатого вала на 360 градусов. Используйте предыдущие шаги и спецификации для установки клапанной ресницы на следующих рычагах качения:

- E = выхлоп
- I = прием

2Е, 3I, 4Е, 5I, 6I, 6E.

Если измерения выходят за заданные пределы, установите клапанную ресницу.

> [!missing]- Иллюстрация `03400175.png` не извлечена — смотрите PDF-оригинал документа

Удалите защитную крышку головки цилиндра, номер детали 4918282, из отверстия в проточной трубе.

![[22400276.png]]

### Завершающие операции

с форсункой механического управления

- Установите крышку коромысел.[[20-003-011-tr — Rocker Lever Cover|См. процедуру 003-011 в разделе 3.]]
- Установите крышку коромысел.[[20-003-011-om — Rocker Lever Cover|См. процедуру 003-011 в разделе A.]]
- Запустите двигатель и проверьте на отсутствие утечек.

с форсункой электронного управления

> [!danger] ОПАСНО
> В зависимости от обстоятельств, дизельное топливо является легковоспламеняющимся. При осмотре или выполнении обслуживания или ремонта топливной системы, чтобы уменьшить вероятность пожара и в результате серьезных травм, смерти или повреждения имущества, никогда не курите и не допускайте искр или пламени (например, пилотные огни, электрические выключатели или сварочное оборудование) в рабочей зоне.

> [!danger] ОПАСНО
> Давление топлива в линии достаточно, чтобы проникнуть в кожу и нанести серьезный вред здоровью. Носите перчатки и защитную одежду.

> [!danger] ОПАСНО
> Давление в топливной системе высокого давления никогда не должно измеряться с помощью механического калибра. Возможны значения давления топлива более 1724 бар \[25 000 psi\]. Если используется механическая измерительная приборная панель, она может выйти из строя, вызывая утечку топлива под высоким давлением, которая может привести к травмам и имущественному ущербу.

> [!warning] ОСТОРОЖНО
> Очень небольшое количество грязи и мусора может быть очень вредным для топливного форсунка и колбочек сидений на топливных форсунках высокого давления. Для поддержания топливных соединений в чистоте во время удаления и установки требуется дополнительная осторожность.

- Установите крышку рычага клапанного клапана.[[20-003-011-tr — Rocker Lever Cover|См. процедуру 003-011 в разделе 3.]]
- Установите крышку рычага клапанного клапана.[[20-003-011-om — Rocker Lever Cover|См. процедуру 003-011 в разделе A.]]
- Установите новую линию подачи топливного форсунка и линии подачи между топливным форсуном.[[20-006-051-tr — Injector Supply Lines (High Pressure)|См. процедуру 006-051 в разделе 6.]]
- Установите новую линию подачи топливного форсунка и линии подачи между топливным форсуном.[[20-006-051-om — Injector Supply Lines (High Pressure)|См. процедуру 006-051 в разделе A.]]
- Запустите двигатель и проверьте на отсутствие утечек.

## Детали, упомянутые в документе

| Артикул | Наименование | Русское название |
|---|---|---|
| [[3090007]] | ROCKER LEVER ADJUSTING SCREW | Регулировочный винт коромысла |

> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> with Mechanically Actuated Injector
>
> The valves and injectors **must** be correctly adjusted for the engine to operate efficiently. Valve and injector adjustment **must** be performed using the values listed in this procedure.
>
> Cummins Inc. has found that engines in most applications will **not** experience significant valve/injector train wear. It is recommended valve and injector adjustment is performed **only** when the injectors are removed or when other repairs disturb the valve train.
>
> If valve and injector adjustment is checked during troubleshooting or before the recommended maintenance interval, adjustment is **not** required if measurements are within the recheck limits.
>
> with Electronically Actuated Injector
>
> The valves **must** be correctly adjusted for the engine to operate efficiently. Valve adjustment **must** be performed using the values listed in this procedure.
>
> For engines with electronically actuated injectors, periodic valve adjustment is **not** required. It is recommended that the valves be adjusted **only** when an injector is removed.
>
> ### Preparatory Steps
>
> with Mechanically Actuated Injector
>
> - Remove the rocker lever cover and all related components. [[20-003-011-om — Rocker Lever Cover|Refer to Procedure 003-011 in Section A.]]
>
> with Electronically Actuated Injector
>
> **WARNING · Опасно**
> When using a steam cleaner, wear safety glasses or a face shield, as well as protective clothing. Hot steam can cause personal injury.
>
> **WARNING · Опасно**
> Depending on the circumstance, diesel fuel is flammable. When inspecting or performing service or repairs on the fuel system, to reduce the possibility of fire and resulting severe personal injury, death, or property damage, never smoke or allow sparks or flames (such as pilot lights, electrical switches, or welding equipment) in the work area.
>
> **WARNING · Опасно**
> The pressure of the fuel in the line is sufficient to penetrate the skin and cause serious personal injury. Wear gloves and protective clothing.
>
> **WARNING · Опасно**
> Pressure within the high-pressure fuel system must never be measured using a mechanical gauge. Fuel pressure values of over 1724 bar \[25,000 psi\] are possible. Under high-pressure, a mechanical gauge can fail causing a high-pressure fuel leak resulting in personal injury and property damage.
>
> **WARNING · Опасно**
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.
>
> **WARNING · Опасно**
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.
>
> **CAUTION · Осторожно**
> Do not spill or drain fuel into the bilge area when disconnecting or removing fuel lines, replacing filters, and priming the fuel system. Do not drop or throw filter elements into the bilge area. The fuel and fuel filters must be disposed of in accordance with local environmental regulations.
>
> **CAUTION · Осторожно**
> A very small amount of dirt and debris can be very harmful to the injectors and the cone seats on the injector high-pressure supply connections. Extra care is required to keep the fuel connections clean during removal and installation.
>
> - Clean all fittings and components with steam or solvent before removal from the engine.
> - Connect INSITE™ electronic service tool and verify that the fuel pressure has bled down by monitoring the fuel pressure.
> - Remove the injector supply line and supply lines. [[20-006-051-om — Injector Supply Lines (High Pressure)|Refer to Procedure 006-051 in Section A.]]
> - Remove rocker lever cover. [[20-003-011-om — Rocker Lever Cover|Refer to Procedure 003-011 in Section A.]]
>
> ### Adjust
>
> with Mechanically Actuated Injector
>
> **Note · Примечание**
> The barring device shaft turns approximately two revolutions before the engine begins to turn. The barring device will **not** turn the engine opposite the direction of normal rotation.
>
> Push the shaft in and turn the barring device **counterclockwise** until the "A" mark on the pulley is aligned with the mark that is cast into the boss for the accessory drive seal on the front gear cover.
>
> Determine the Cylinder in Position for Valve Set.
>
> | Valve Set Mark | Check Valve Position |
> |---|---|
> | A | 1, 6 |
> | B | 2, 5 |
> | C | 3, 4 |
>
> If the rocker lever assemblies have been removed, use this step to determine the cylinder to be set.
>
> Lubricate the adjusting screw threads with clean engine oil prior to making valve and injector adjustments.
>
> All adjusting screws **must** be loose on all cylinders, and the push rods **must** remain in alignment.
>
> Perform this step on both cylinders to be checked.
>
> Hold both rocker levers against the crossheads. Turn the adjusting screws until they touch the push rods. Turn the locknuts until they touch the levers.
>
> The push rods will be the same height above the top of the rocker lever housing on the cylinder ready for valve adjustment.
>
> If the rocker levers have **not** been removed, wiggle the valve rocker levers on the two cylinders in question. Use the chart and select the correct cylinder for adjustment.
>
> Use the chart to determine the valve and injector that is ready to adjust.
>
> Adjustment can begin on any valve set mark.
>
> In the example, assume the A mark is aligned and the push rod heights indicate that one valve on cylinder number 1 is fully opened and both valves on cylinder number 6 are fully closed. The chart also shows that the valves on cylinder number 2 and the injector on cylinder 3 are ready to adjust.
>
> After the adjustment, bar the engine to the B set mark. Adjust the valves on cylinder number 4 and adjust the injector on cylinder number 6.
>
> | Valve Adjustment (Initial Set) |  |  |  |
> |---|---|---|---|
> | Reference Point | mm |  | in |
> | A | 0.81 | Exhaust | 0.032 |
> | B | 0.36 | Intake | 0.014 |
>
> Make certain the crosshead is firmly in place on the valve stem tips.
>
> Make certain the feeler gauge is under the center of the ball and socket, or the socket can rock or tip, resulting in an incorrect adjustment. To avoid false readings, hold the swivel foot flat to avoid binding while checking the lash.
>
> Use service tool Part Number 3824901. Select a feeler gauge for the correct valve lash specification. Insert the gauge between the rocker lever socket and the crosshead.
>
> Two different methods for establishing valve lash clearance are described below. Either method can be used. The torque wrench method has proven to be the **most** consistent.
>
> #### Torque Wrench Method:
>
> - Use service tool, Part Number 3376592, inch-pound torque wrench, to tighten the adjusting screw to.68 N•m \[6 in-lb\] torque against the feeler gauge.
>
> #### Feel Method:
>
> - Use a nut driver and turn the adjusting screw **only** until the lever touches the feeler gauge.
>
> Be certain the parts are in alignment. Tighten the adjusting screw and squeeze the oil out of the valve train.
>
> Loosen the adjusting screw at least one full revolution.
>
> Insert a feeler gauge between the rocker lever socket and the crosshead.
>
> Use torque wrench, Part Number 3376592, and tighten the adjustment screw.
>
> **Момент затяжки · Torque Value**
> 0.68 n•m [6 in-lb]
>
> Remove feeler gauge.
>
> The adjustment screw **must not** turn when the locknut is tightened. Locknut torque can be applied with or without a torque wrench adapter, Part Number 3163196.
>
> Tighten the locknut.
>
> | Torque Value |  |
> |---|---|
> | **Adjustment Screw Part Number** | 168306 |
> | With Adapter | 48 N•m \[35 ft-lb\] |
> | Without Adapter | 60 N•m \[44 ft-lb\] |
> | **Adjustment Screw Part Number** | [[3090007]] |
> | With Adapter | 84 N•m \[62 ft-lb\] |
> | Without Adapter | 105 N•m \[77 ft-lb\] |
>
> Attempt to insert a feeler gauge that is 0.03 mm \[0.001 in\] thicker. The valve lash is **not** correct when the thicker gauge will fit.
>
> Repeat the adjustment process until the proper lash is obtained.
>
> Use a torque wrench to tighten the injector rocker lever adjusting screw. If the screw chatters during setting, repair the screw and lever as required.
>
> Be certain the parts are in alignment. Tighten the adjusting screw and squeeze the oil out of the injector train. This is an initial adjustment to preload the injector.
>
> **Момент затяжки · Torque Value**
> 28 n•m [248 in-lb]
>
> Loosen the adjusting screw at least one revolution.
>
> Tighten the adjusting screw again to the final setting.
>
> **Момент затяжки · Torque Value**
> 19 n•m [168 in-lb]
>
> The torque wrench **must** be calibrated, have a resolution of 0.28 N•m \[2.5 in-lb\], and have a range of 17 to 23 N•m \[150 to 200 in-lb\].
>
> Hold the adjusting screw in this position. The adjusting screw **must not** turn when the locknut is tightened.
>
> Tighten the locknut to the following values:
>
> For the torque method (with adapter), use torque wrench adapter, Part Number ST-669.
>
> | Torque Value |  |
> |---|---|
> | **Adjustment Screw Part Number** | 168306 |
> | With Adapter | 48 N•m \[35 ft-lb\] |
> | Without Adapter | 60 N•m \[44 ft-lb\] |
> | **Adjustment Screw Part Number** | [[3090007]] |
> | With Adapter | 84 N•m \[62 ft-lb\] |
> | Without Adapter | 105 N•m \[77 ft-lb\] |
>
> with Electronically Actuated Injector
>
> **CAUTION · Осторожно**
> To reduce the possibility of engine damage, use a cylinder head protective cover to prevent tools from falling into the cam follower cavity.
>
> Install the cylinder head protective cover, Part Number 4918282, into the push tube hole.
>
> The barring device shaft turns approximately two revolutions before the engine begins to turn. The barring device will **not** turn the engine opposite the direction of normal rotation.
>
> TDC represents Top Dead Center for cylinders 1 or 6. This mark will be used to set the valves on engines with electronically actuated injectors. This will allow all valves to be set in two positions. Ignore the A, B, and C marks while using this procedure.
>
> Push the shaft in and turn the barring device until the TDC mark on the pulley is aligned with the mark that is cast into the boss for the accessory drive seal on the front gear cover.
>
> The number of threads visible above the adjusting nut will **not** be the same. There will be more threads visible on the intake adjusting screw than on the exhaust adjusting screw.
>
> If the rocker lever assemblies have been removed, use this step to determine the cylinder to be set.
>
> All adjusting screws **must** be loose on all cylinders, and the push rods **must** remain in alignment.
>
> Perform this step on both cylinders to be checked.
>
> Hold both rocker levers against the crossheads. Turn the adjusting screws until they touch the push rods. Turn the locknuts until they touch the levers.
>
> The push rods will be the same height above the top of the rocker lever housing on the valves that should be loose.
>
> If both number 1 cylinder rocker levers are loose, proceed to the next step. If the number 1 cylinder rocker levers are **not** loose, rotate the crankshaft 360 degrees and proceed to the next step.
>
> If the number 1 cylinder is at TDC and both rocker levers are loose, the valve lash (overhead set) can be checked on the following rocker levers:
>
> - E = exhaust
> - I = intake
>
> 1I, 1E, 2I, 3E, 4I, and 5E
>
> | Valve Adjustment (Initial Set) |  |
> |---|---|
> | Exhaust (A) | Intake (B) |
> | 0.69 mm \[0.027 in\] | 0.36 mm \[0.014 in\] |
>
> | Valve Recheck Limits |  |  |  |
> |---|---|---|---|
> |  | mm |  | in |
> | Intake Valve | 0.280 | MIN | 0.011 |
> |  | 0.430 | MAX | 0.017 |
> | Exhaust Valve | 0.610 | MIN | 0.027 |
> |  | 0.762 | MAX | 0.030 |
>
> Use service tool, Part Number 3163171 (intake) or Part Number 3163172 (exhaust). Select a feeler gauge for the correct valve lash specification. Insert the gauge between the rocker lever socket and the crosshead.
>
> Make certain the crosshead is firmly in place on the valve stem tips.
>
> Make certain the feeler gauge is under the center of the ball and socket, or the socket can rock or tip, resulting in an incorrect adjustment. To avoid false readings, hold the swivel foot flat to avoid binding while checking the lash.
>
> Two different methods for establishing valve lash clearance are described below:
>
> - Torque Wrench Method - Use Part Number 3376592, inch-pound torque wrench, to tighten the adjusting screw to 0.68 N•m \[6 in-lb\] torque against the feeler gauge.
> - Feel Method - Use a screwdriver and turn the adjusting screw **only** until the lever touches the feeler gauge.
>
> Either method can be used. The torque wrench method has proven to be the most consistent.
>
> To set the valves using the torque wrench method, complete the following steps:
>
> Be certain the parts are in alignment. Tighten the adjusting screw and squeeze the oil out of the valve train.
>
> Loosen the adjusting screw at least one revolution.
>
> Insert the feeler gauge between the rocker lever socket and the crosshead.
>
> Use torque wrench, Part Number 3376592, and tighten the adjusting screw.
>
> Remove the feeler gauge.
>
> **Момент затяжки · Torque Value**
> 0.68 n•m [6 in-lb]
>
> To set the valves using the feel method, complete the following steps:
>
> The adjustment screw **must not** turn when the locknut is tightened. Locknut torque can be applied with or without a torque wrench adapter, Part Number 3163196.
>
> Tighten the locknut.
>
> The adjusting screw **must not** turn when the locknut is tightened.
>
> For the torque method (with adapter), use torque wrench adapter, Part Number ST-669.
>
> | Torque Value |  |
> |---|---|
> | **Adjustment Screw Part Number** | 168306 |
> | With Adapter | 48 N•m \[35 ft-lb\] |
> | Without Adapter | 60 N•m \[44 ft-lb\] |
> | **Adjustment Screw Part Number** | [[3090007]] |
> | With Adapter | 84 N•m \[62 ft-lb\] |
> | Without Adapter | 105 N•m \[77 ft-lb\] |
>
> Attempt to insert a feeler gauge that is 0.03 mm \[0.001 in\] thicker. The valve lash is **not** correct when the thicker gauge will fit.
>
> Repeat the adjustment process until the proper clearance is obtained.
>
> Use the barring tool to rotate the crankshaft 360 degrees. Use the previous steps and specifications to set the valve lash on the following rocker levers:
>
> - E = exhaust
> - I = intake
>
> 2E, 3I, 4E, 5I, 6I, 6E.
>
> If the measurements are out of specification, set the valve lash.
>
> Remove the cylinder head protective cover, Part Number 4918282, from the push tube hole.
>
> ### Finishing Steps
>
> with Mechanically Actuated Injector
>
> - Install the rocker lever cover. [[20-003-011-tr — Rocker Lever Cover|Refer to Procedure 003-011 in Section 3.]]
> - Install the rocker lever cover. [[20-003-011-om — Rocker Lever Cover|Refer to Procedure 003-011 in Section A.]]
> - Operate the engine and check for leaks.
>
> with Electronically Actuated Injector
>
> **WARNING · Опасно**
> Depending on the circumstance, diesel fuel is flammable. When inspecting or performing service or repairs on the fuel system, to reduce the possibility of fire and resulting severe personal injury, death, or property damage, never smoke or allow sparks or flames (such as pilot lights, electrical switches, or welding equipment) in the work area.
>
> **WARNING · Опасно**
> The pressure of the fuel in the line is sufficient to penetrate the skin and cause serious personal injury. Wear gloves and protective clothing.
>
> **WARNING · Опасно**
> Pressure within the high-pressure fuel system must never be measured using a mechanical gauge. Fuel pressure values of over 1724 bar \[25,000 psi\] are possible. If a mechanical gauge is used it can fail, causing a high-pressure fuel leak which can cause personal injury and property damage.
>
> **CAUTION · Осторожно**
> A very small amount of dirt and debris can be very harmful to the injectors and the cone seats on the injector high-pressure supply connections. Extra care is required to keep the fuel connections clean during removal and installation.
>
> - Install rocker lever cover. [[20-003-011-tr — Rocker Lever Cover|Refer to Procedure 003-011 in Section 3.]]
> - Install rocker lever cover. [[20-003-011-om — Rocker Lever Cover|Refer to Procedure 003-011 in Section A.]]
> - Install new injector supply line and supply lines between injectors. [[20-006-051-tr — Injector Supply Lines (High Pressure)|Refer to Procedure 006-051 in Section 6.]]
> - Install new injector supply line and supply lines between injectors. [[20-006-051-om — Injector Supply Lines (High Pressure)|Refer to Procedure 006-051 in Section A.]]
> - Operate the engine and check for leaks.
