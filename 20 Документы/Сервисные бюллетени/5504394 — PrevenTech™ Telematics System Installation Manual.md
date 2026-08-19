---
aliases:
  - "Руководство по установке телематики PrevenTech™"
type: "Сервисный бюллетень"
doc: "5504394"
title_en: "PrevenTech™ Telematics System Installation Manual"
title_ru: "Руководство по установке телематики PrevenTech™"
released: "2018-05-04"
modified: "2020-12-16"
group: "17 - Miscellaneous"
engines:
  - "33239746"
  - "33239899"
  - "41349633"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSK19"
figures: 20
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/5504394.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/bulletin/5504394.pdf"
tags:
  - "документ/бюллетень"
  - "двигатель/K38/K50"
  - "двигатель/QSK19"
  - "перевод/машинный"
  - "тема/miscellaneous"
---

# PrevenTech™ Telematics System Installation Manual
**Руководство по установке телематики PrevenTech™**

> [!abstract] Сервисный бюллетень · `5504394`
> **Раздел Cummins:** 17 - Miscellaneous
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60, QSK19
> **Даты:** выпущен 2018-05-04 · изменён 2020-12-16
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/5504394.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/bulletin/5504394.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Руководство по установке телематики PrevenTech™

**Таблица содержимого**

- Системный и аппаратный обзор
- Установка
- Инструкции по установке: Телематическое оборудование PrevenTechTM
- Аппендикс А: Спецификации Telematics Box Hardware
- Аппендикс Б: Примеры установки
- APPENDIX C: WIFI передача

**Обзор систем и оборудования**

В данном руководстве подробно описывается установка телематической системы PrevenTechTM. Хотя были предприняты усилия для того, чтобы сделать это руководство как можно более всеобъемлющим, установки должны быть адаптированы к конкретной модели применения/оборудования.

Набор PrevenTechTM содержит следующее оборудование:

1. Телематическая коробка PrevenTechTM
2. Сотовая/GPS/Bluetooth антенна
3. Главная проводка
4. Антенна монтажное оборудование

Набор PrevenTechTM не содержит всего оборудования, необходимого для установки. SIM-карты и проводов подключения ** должны быть приобретены отдельно.

![[19r99430.png]]

Рисунок 1 PrevenTechTM Kit Hardware.

Экологические и физические требования к эксплуатации и хранению:

| Таблица 1, Требования к эксплуатации и хранению |  |
|---|---|
| Операция "Температурный диапазон" | -5°C до +70°C \[23°F до 158 ̊F \] |
| Диапазон температур хранения | -30°C до +85°C \[ 86°F до 185 ̊F \] |
| влажность | До 95% - неконденсируемые |

**Предустановочные этапы**

Перед тем, как выводить аппаратное обеспечение PrevenTechTM на сайт клиента, необходимо выполнить проверку стенда, чтобы убедиться, что система функциональна и закупленная SIM-карта совместима с системой.

1. Зарегистрируйтесь, связавшись с командой CPS по адресу connectedsol.support@cummins.com. В поле PrevenTechTM, предоставьте идентификационные номера и IMEI. Также необходимы серийный номер двигателя (ESN), калибровка ECM, рейтинг hp, OEM / модель оборудования, номер блока, местоположение / минный сайт и информация о SIM-карте.

![[17r00286.png]]

Рисунок 2, Идентификационная этикетка на нижней части коробки PrevenTechTM.

2. Удалите крышку телематической коробки и убедитесь, что выключены выключатели (в направлении к подвесному положению или в «правильном», если разъём проводов упряжки находится в верхней части). Эти переключатели являются внутренними резисторами, которые не нужны.

![[19r99441.png]]

Рисунок 3, Интерьер коробки PrevenTechTM. Выделено месторасположение Dip Switch.

3. Закупите 3G GSM SIM-карту (стандартный размер 2FF) или обратно совместимую 4G LTE SIM-карту. Обратите внимание, что коробка ** не** работает с использованием карты 4G или карты, настроенной на сеть CDMA. Убедитесь, что в этом районе достаточно 3G-покрытия. При активации карты требуется номер IMEI на этикетке коробки. Рекомендовать зарегистрировать клиента и оборудование и активировать доступ к www.preventech.cummins.com. Если клиент имеет **не** заказанные SIM-карты с активным планом данных, используйте совместимую SIM-карту с активированным планом данных для проверки работоспособности.

4. Установите SIM-карту с вырезанной вкладкой на внешней стороне

![[17r00287.png]]

Рисунок 4, Интерьер коробки PrevenTechTM с установленной SIM-картой.

![[17r00977.png]]

Рисунок 5, расположение батареи часов

5. Подключите антенну к телематической коробке и поместите в повышенное положение, чтобы получить сотовый сигнал.

6. Подключите проводку к коробке. Подключение VINPUT приводит к источнику питания 12/24 В и GND приводит к отрицательному соединению. Примените силу. Через 5 минут зеленый свет должен быть устойчивым. Красный свет должен быть мигающим (2 секунды выключения - от 0 до 5 секунд Включения). Если красный свет устойчив, это означает, что нет связи сотовой связи. Если это происходит, обратитесь к приложению А для устранения неполадок.

7. Определить стратегию соединения автобусов J1939. Существует несколько способов подключения к двигателю J1939 CAN Bus. Эта стратегия определит, какое периферийное оборудование необходимо заказать.

- Вариант 1: Автобус OEM J1939 CAN Bus

![[17r00288.png]]

Рисунок 6, CAN Bus Node

- Вариант 2: Расширьте магистраль двигателя до телематической коробки проводов.

![[17r00289.png]]

Рисунок 7, Расширение проводной узлы

8. Общее оборудование для установки не включено в комплект. элементы, необходимые для выполнения полной установки, которые не включены в комплект. Эти элементы будут варьироваться в зависимости от типа приложения / модели.

- Зип-связь
- Владельцы предохранителей
- 5-амперный предохранитель
- Различные электрические терминалы / сплайсы прикладов
- Гландские орехи
- Дополнительный провод 18AWG (если необходимо расширение проводов)

** Процедуры установки**

1. J1939 Public CAN Bus 3-Pin Connection (недоступная ссылка)

- Двигатели и оборудование могут иметь несколько сетей CAN в своей архитектуре. Рядовой. Идентификация общественного автобуса J1939 CAN необходима до установки телематического ящика PrevenTechTM. Чтобы проверить правильность выбранного CAN Bus, свяжитесь с OEM-оборудованием. В качестве альтернативы, проверьте непрерывность между выбранным 3-контактным разъемом и 9-контактным сервисным разъемом.

2. Проверить сопротивление автобуса J1939 CAN путем измерения между положительным и отрицательным терминалом на 9-пиновом разъеме службы (Pins C и D на рисунке ниже). Если измерение сопротивления составляет 120 Ом, в основу должен быть добавлен дополнительный конечный резистор ***. Если измерение сопротивления составляет менее 60 Ом, то резистор *** должен быть удален.

![[19r99427.png]]

Рисунок 8, контактная схема разъема

Установите телематическую коробку PrevenTechTM

- Место установки должно соответствовать следующим критериям окружающей среды:
- Монтажная телематическая коробка с использованием монтажного оборудования.

4. Connect Wiring Harness (соединение)

- В проводной упряжке PrevenTechTM имеется несколько проводов, которые не используются в существующей конфигурации. Составьте следующие соединения:

![[17r00851.png]]

Рисунок 9, Ветка жгута проводов Harness

> [!note] Примечание
> Удалите штифт K4 на телематической коробке, используя длинный носовой маленький плоскогубец и медленно с твердым захватом, перемещая его в направлении вверх и вниз, пока он не сломается. Это предотвращает ошибки связи из-за внутренней проблемы проводов с использованием проводов DO (цифровые выходы).

![[17r00852.png]]

Рисунок 10, Телематическая коробка 48 Pin Connector Layout

- Подключите проводку к телематической коробке PrevenTechTM, вставив разъем, а затем вращая рычаг в заблокированное положение.

![[19r99431.png]]

Рисунок 11, Подключение проводов PrevenTechTM к телематической коробке PrevenTechTM

5. Установить антенну

- Антенна GSM/GPS/WIFI должна быть установлена снаружи оборудования, с прямой прямой видимости на небо.
- Установка не менее 40 см от оператора оборудования
- Рассмотрите стратегию маршрутизации и близость к телематической коробке PrevenTechTM
- Маршрутные антенные разъемы через прокладку, скобки и удерживающий гай.
- Обеспечить безопасность кронштейна и крепления с использованием двух U-болтов.
- Маршрутные антенные разъемы подключаются к телематическому ящику PrevenTechTM и сопоставляют разъемы с правильным портом на коробке. Примечание: Разъем антенны с надписью «WIFI» ** должен быть подключен к разъему телематической коробки с надписью «BT».

![[17r00291.png]]

Рисунок 12, Узлы для проводов антенны, подключенные к телематической коробке и горе антенны на внешней стороне приложения.

- Создайте облегчение напряжения, разрешив по меньшей мере 1 фут кабеля между антенными портами и размещением рельефа напряжения.
- Безопасная проводка по маршруту с использованием P-Clips или Zip-связей. Избыточная проводка упряжки должна быть аккуратно свернута и закреплена, чтобы предотвратить вмешательство с другими компонентами.

6. Примените мощность и через 5 минут убедитесь, что светодиодные фонари включены в соответствии со следующими таблицами. Если светодиоды не дают надлежащего указания, обратитесь к приложению А для устранения неполадок.

- Включится примерно через 30 секунд, когда питание будет подано. Если оборудование принимает кадры через порт CAN0, светодиод будет мигать на высокой скорости, указывающей на передачу.

| ** Зеленый индикатор светодиодов - CAN Operation** |  |
|---|---|
| ** Государство** | ** Указание** |
| Не останавливайся. | Система инициализированная |
| мигающий | Данные передаются по CAN0 |
| Остановиться | Операционная система не инициализируется |

- Красный светодиод используется для обозначения состояния связи устройства. В течение первых 5 минут с момента питания устройства светодиод будет выключен. Если телематическая коробка не обеспечивает связь через 5 минут, светодиод будет постоянно светиться. В отличие от этого, если 3G / GSM соединение стабильно в течение 5 минут, светодиод будет мигать каждые 2 секунды.

| ** Красный светодиодный индикатор - сетевое подключение** |  |
|---|---|
| ** Государство** | ** Указание** |
| Устойчиво (через 5 минут) | Нет 3G/GSM-связи |
| Вспышка (2 секунды OFF - от 0 до 5 секунд ON) | Стабильная связь 3G/GSM |
| Остановиться | Только первые 5 минут после включения |

7. После проверки регистрации оборудования используйте панель приборов PrevenTech для проверки местоположения GPS и активации связи. Если связь не может быть установлена, выполните шаги по устранению неполадок или свяжитесь с Cummins CARE.

Аппендикс А: устранение неполадок

ШАГ 1A. Проверьте видимость неисправного оборудования на приборной панели PrevenTechTM

| ** Условия: ** В то время как оборудование включено |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Войдите на панель инструментов PrevenTechTM, https://preventech.cummins.com; Проверьте панель инструментов для работы | Видно ли оборудование на приборной панели? *Да** | **2A** |
| Видно ли оборудование на приборной панели? **Нет** | **1B** |  |

ШАГ 1B. Проверка видимости другого оборудования на приборной панели PrevenTechTM

| ** Условия: ** В то время как оборудование включено |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверить приборную панель на предмет видимости другого оборудования | Видно ли другое оборудование на приборной панели? **Давайте не будем мешать с Dashboard | **2A** |
| Видно ли другое оборудование на приборной панели? **Нет** | ** Контакт: ** Региональная поддержка PrevenTechTM Контакт или care.cummins.com |  |

ШАГ 2. Определить состояние светодиодов

ШАГ 2A. Зеленый светодиод мигает

| **Условия: ** В то время как оборудование включено **Примечание: ** через 30 секунд после подачи питания; Телематический блок PrevenTechTM зеленый светодиод начнет мигать на высокой скорости при приеме кадров через телематическое соединение PrevenTechTM J1939 |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверить зеленый LED | Зеленый светодиод мигает? **Данные передаются на телематическом окне PrevenTechTM J1939; окне телематики PrevenTechTM должно быть подключено к движку J1939, эталонный шаг **5A** | **2C** |
| Зеленый светодиод мигает? **Нет** | **2B** |  |

ШАГ 2B. Зеленый светодиод устойчивый

| ** Условия: ** В то время как оборудование включено |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверить зеленый LED | Зеленый светодиод устойчив? **Давайте заметим: ** Операционная система инициализирована | **5А** |
| Зеленый светодиод устойчив? **Примечание: ** Операционная система не инициализирована | **3A** |  |

ШАГ 2C. Красный светодиод мигает

| ** Условия: ** В то время как оборудование включено |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверить красный светодиод | Красный светодиод мигает? **Давайте примечание:** Стабильное 3G/GSM соединение | **Проверить информацию о конфигурации панели управления Контакт: ** Региональный контакт поддержки PrevenTechTM или care.cummins.com |
| Красный светодиод мигает? **Нет** | **2D** |  |

ШАГ 2D. Красный светодиод устойчивый

| **Условия:** При включении оборудования **Примечание:** Красный светодиод выключается в течение первых 5 минут после подачи питания в телематическую коробку PrevenTechTM |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверить красный светодиод | Красный светодиод устойчив? **Давайте примечание: ** Нет 3G/GSM-подключения | **6А** |
| Красный светодиод устойчив? **Нет** | **3A** |  |

ШАГ 3. Определить состояние электроснабжения

> [!note] Примечание
> Телематическая коробка внутренней картриджной батареи PrevenTechTM будет удерживать заряд в течение периода времени после того, как внешняя мощность будет удалена, и будет функционировать по назначению; при устранении неполадок внешнего источника питания отсоедините телематическую коробку внутренней картриджной батареи PrevenTechTM. При необходимости обратитесь к шагу 4 для обнаружения неисправности внутренней батареи телематического блока PrevenTechTM, т.е. Вариация времени печати данных на панели инструментов PrevenTechTM.

ШАГ 3A. Состояние предохранителя

| ** Условия: ** В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверить встроенный предохранитель | Запал открыт? ** Да, ремонт: ** Заменить предохранитель | ** Ремонт завершен** |
| Запал открыт? **Нет** | **3B** |  |

ШАГ 3B. Электропитание, зажигание и состояние проволочного провода шасси

| ** Условия: ** В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Тщательно проверьте состояние основной проводов жгута проводов Справочное приложение H выше. | Являются ли подачу электроэнергии, зажигание и наземные провода шасси в хорошем состоянии без повреждений, т.е. Никаких слез? *Да** | **3C** |
| Являются ли провода питания, зажигания и заземления шасси в хорошем состоянии без повреждений? **NoRepair:** Заменить телематическую коробку PrevenTechTM главной проводкой | ** Ремонт завершен** |  |

ШАГ 3C. Электропитание, зажигание и наземные соединения шасси

| ** Условия: ** В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Тщательно проверьте основные проводные соединения жгута | Подключены ли провода питания, зажигания и наземные провода шасси? *Да** | **3D** |
| Подключены ли провода питания, зажигания и наземные провода шасси? **NoRepair:** Подключите провод(ы), которые не подключены | ** Ремонт завершен** |  |

ШАГ 3D. Главная проводка подключения жгута к телематической коробке PrevenTechTM

| ** Условия: ** В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверить подключение основной проводов к телематической коробке PrevenTechTM. Справка ** Шаг 5** в Инструкции по установке: Телематическое оборудование PrevenTechTM выше. | Является ли основная проводка надежно подключенной к телематической коробке PrevenTechTM? *Да** | **3E** |
| Является ли основная проводка надежно подключенной к телематической коробке PrevenTechTM? **NoRepair:** Подключите и надежно заблокируйте основную проводку | ** Ремонт завершен** |  |

ШАГ 3E. Состояние питания, подаваемого на материнскую плату

| **Условия:** При подаче питания в телематическую коробку PrevenTechTM |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Откройте коробку PrevenTechTM и проверьте порт локальной сети на материнской плате, ссылочная фигура 39 выше | Включен ли порт LAN? *Да** | **3F** |
| Включен ли порт LAN? **NoRepair:** Заменить телематическую коробку PrevenTechTM | ** Ремонт завершен** |  |

ШАГ 3F. Состояние внутренней проводов LED(s)

| **Условия:** При подаче питания в телематическую коробку PrevenTechTM |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверить внутреннюю проводку светодиодов, ссылочная фигура 39 выше | Есть ли в них (или в них) светодиоды? **NoRepair:** Заменить телематическую коробку PrevenTechTM | ** Ремонт завершен** |

ШАГ 4. Внутренняя батарея PrevenTechTM

ШАГ 4A. Внутренние часы (круглые) аккумуляторные

| ** Условия: ** В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте штампы времени данных панели приборов Справочная фигура 5 выше. | Есть ли неопределенность в штампе данных / часах реального времени? **Примечание:** Удалите круглую батарею с помощью тонкой плоской отвертки и замените, проверьте приборную панель PrevenTechTM на функциональность | ** Ремонт завершен** |

ШАГ 5. Оборудование J1939 Connection

ШАГ 5A. Проверить оборудование и телематическую коробку PrevenTechTM J1939

| ** Условия: ** В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверить связь телематического ящика PrevenTechTM J1939 с оборудованием | Подключен ли кабель телематики PrevenTechTM J1939 к общедоступному соединению данных оборудования J1939? *Да** | **5C** |
| Подключен ли кабель телематики PrevenTechTM J1939 к общедоступному соединению данных оборудования J1939? **Нет** | **5B** |  |

ШАГ 5B. Оборудование J1939 Public Connection

| ** Условия: ** В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Измерить непрерывность от 9-контактного сервисного разъема до 3-контактного разъема Deutsch | Подтверждена ли преемственность? **Давайте отремонтируем:** Подключите телематическую коробку PrevenTechTM J1939 к общедоступным данным J1939 | ** Ремонт завершен** |
| Подтверждена ли преемственность? **Примечание:** Повторяйте этот шаг до тех пор, пока не будет установлено общественное соединение J1939 | ** Повторить шаг** |  |

ШАГ 5C. Измерить сопротивление оборудования

| ** Условия: ** В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Отключите соединение J1939; с помощью оборудования J1939 или 9 Pin сервисный разъем измеряет сопротивление оборудования, ссылочная фигура 1 выше. | Является ли измеренное сопротивление 60 Ом? *Да** | **5E** |
| Является ли измеренное сопротивление 60 Ом? **Нет** | **5D** |  |

ШАГ 5D. Осмотр резисторов магистральных терминалов J1939

| ** Условия: ** В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверить резисторы терминала связи J1939; измерить сопротивление. Справочная фигура 7 и фигура 26 выше. Примечание: Только два 120 Ом резистора, необходимых параллельно на магистрали для достижения общего сопротивления 60 Ом | Является ли измеренное сопротивление в каждом резисторе 120 Ом? *Да** | **5E** |
| Является ли измеренное сопротивление в каждом резисторе 120 Ом? **NoRepair:** Откажитесь от резистора (резисторов) и замените его (их) | ** Ремонт завершен** |  |

ШАГ 5E. Измерение сопротивления телематической коробки PrevenTechTM

| ** Условия: ** В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Измерить сопротивление на соединении PrevenTechTM J1939, ссылочная фигура 1 выше. | Является ли измеренное сопротивление приблизительно 50 К-Ом? **Нет** | **5F** |
| Является ли измеренное сопротивление приблизительно 50 К-Ом? ** Да, примечание: ** Нет проблемы телематического сопротивления PrevenTechTM | ** Ремонт завершен** |  |

ШАГ 5F. Телематическая коррекция сопротивления коробки PrevenTechTM

| ** Условия: ** В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Измерить сопротивление на соединении PrevenTechTM 1939, ссылочная фигура 1 выше. | Является ли измеренное сопротивление приблизительно 0 Ом? ** Дата выхода ** Короткое в коробке **Ремонт: ** Заменить телематическую коробку PrevenTechTM | ** Ремонт завершен** |
| Является ли измеренное сопротивление приблизительно 120 Ом? ** Да, ремонт: ** Убедитесь, что переключатели внутреннего сопротивления находятся справа от батареи. Справка ** Шаг 13** в Инструкции по установке: Телематическое оборудование PrevenTechTM выше. | ** Ремонт завершен** |  |

ШАГ 6. Передача данных на приборную панель PrevenTechTM

ШАГ 6A. Антенны соединения

| ** Условия: ** В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверить антенные соединения в телематическом блоке PrevenTechTM, ссылочный шаг 11 в Инструкции по установке: Телематическое оборудование PrevenTechTM Telematics | Являются ли провода антенн надежно и правильно соединены с телематическим блоком PrevenTechTM? *Да** | **6B** |
| Являются ли провода антенн надежно и правильно соединены с телематическим блоком PrevenTechTM? **NoRepair:** Правильно подсоедините антенные провода к правильным портам и надежно подключитесь. | ** Ремонт завершен** |  |

ШАГ 6B. Состояние антенных проводов

| ** Условия: ** В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверить провода между телематическим ящиком PrevenTechTM и антенным круглым передатчиком, ссылочный шаг 11 в Инструкции по установке: Телематическое оборудование PrevenTechTM Telematics | Повреждаются один или несколько антенных проводов, т.е. абразивный канал, круглое повреждение передатчика? **ДаРемонт:** Заменить и направить антенны в телематическую коробку PrevenTechTM | ** Ремонт завершен** |
| Повреждаются один или несколько антенных проводов, т.е. абразивный канал, круглое повреждение передатчика? **Нет** | **6C** |  |

ШАГ 6C. Статус SIM-карты

| ** Условия: ** В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Удалите SIM-карту Справочная фигура 14 выше. | Являются ли контакты SIM-карты и телематической коробки PrevenTechTM грязными или скучными? **YesRepair:** Очистите все контакты, переустановите SIM-карту и проверьте передачу данных | ** Ремонт завершен** |
| Являются ли контакты SIM-карты и телематической коробки PrevenTechTM грязными или скучными? **Нет** | **6D** |  |

ШАГ 6D. Данные SIM-карты

| **Условия: ** В то время как оборудование отключено **Примечание: ** Рассмотрите возможность использования мобильного телефона, совместимого с SIM-картой, того же сетевого провайдера для проверки функциональности данных; если передача данных установлена, может потребоваться замена телематического блока PrevenTechTM |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверка использования данных у сетевого провайдера | Достигнут ли максимальные пределы плана? **Да** Может рассмотреть возможность обновления до более высокого плана данных | ** Ремонт завершен** |
| Достигнут ли максимальные пределы плана? **NoRepair:** Коррумпированная SIM-карта; получить другую SIM-карту и перенастроить коробку PrevenTechTM Telematics | ** Ремонт завершен** |  |

** Добавление В: Примеры установки**

Следующие фотографии документируют некоторые установки, проводимые в различных приложениях. Они предназначены только для справки. Каждая установка требует оценки, чтобы определить, какая стратегия подходит для этого конкретного устройства.

![[17r00292.png]]

Рисунок 13 Подключение к J1939 CAN Bus с помощью Гендерного Переключателя и Y Коннектора

![[17r00293.png]]

Рисунок 14, Пример установки телематических коробок

** Добавление C: WIFI трансляция**

В зависимости от местоположения объекта, блоки могут иметь либо телематическую коробку с внешним портом Ethernet, либо внутренний порт Ethernet.

Если будет установлено, что телематическая коробка имеет внутренний порт Ethernet, то для ее обнаружения необходимо пробурить небольшое отверстие над соединением с надписью «B».

![[17r00853.png]]

Рисунок 15, Телематическая коробка PrevenTechTM с внутренним портом Ethernet

Программное обеспечение должно быть обновлено для обоих типов телематических коробок PrevenTechTM, когда устройство может общаться в Интернете.

Полезность конфигурации EMD:

- EMD - это загружаемая программа конфигурации, которая должна настроить ячеистую сеть на телематическое устройство.
- Выполните следующие действия, чтобы загрузить программу:

Подключите компьютер к устройству с помощью адаптера модема USB-RS-232 и доступного подключения RS-232 на устройстве проводов жгута.

![[17r00854.png]]

Рисунок 16, Устройства проводов жгута RS-232 Соединение

Запустите утилиту конфигурации EMD и дождитесь появления диалогового окна с просьбой использовать последовательный порт для связи с устройством, по умолчанию устройство будет обмениваться данными со скоростью 115200 б/с. Выберите подходящий и нажмите кнопку OK.

![[17r00855.png]]

Рисунок 17, окно EMD Configuration Utility Window

Всплывает окно с просьбой дать пароль. Введите правильный пароль и нажмите OK.

> [!note] Примечание
> Пароль устройства **должен** быть получен путем обращения в команду PrevenTechTM.

![[17r00856.png]]

Рисунок 18, окно ввода пароля устройства

Информация DNS-сервера, необходимая от ИТ-отдела клиента, отошла на устройства связи.

- Режим: Переключитесь на ручной
- IP-адрес:
- Сетевая маска:
- Ворота:
- DNS1:
- DNS2:

В разделе вкладки Сеть введите информацию, собранную в соответствующих местах, и нажмите «Применить».

![[17r00857.png]]

Рисунок 19, окно сетевой конфигурации

Установочные соображения:

- В зависимости от участка шахты, если в текущем блоке POE-коммутатора нет доступных портов Ethernet, может потребоваться новая POE-коммутаторная коробка для интеграции сетчатой сети.
- Кабель RJ45 - RJ45 CAT6 Ethernet проходит от устройства к коммутатору POE.
- M12 (8-pin) - RJ45 CAT6 будет запущен из коммутатора POE в сетевой модем.

![[17r00858.png]]

Рисунок 20, пример установки POE/Modem

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## PrevenTech™ Telematics System Installation Manual
>
> **Table of Contents**
>
> - System and Hardware Overview
> - Installation
> - Installation Instructions: PrevenTech™ Telematics Hardware
> - APPENDIX A: Telematics Box Hardware Specifications
> - APPENDIX B: Installation Examples
> - APPENDIX C:WIFI Transmission
>
> **System and Hardware Overview**
>
> This instruction manual details the installation of the PrevenTech™ telematics system. While efforts have been made to make this manual as comprehensive as possible, installations must be tailored to the particular application/equipment model.
>
> The PrevenTech™ Kit contains the following hardware:
>
> 1. PrevenTech™ telematics box
> 2. Cellular/GPS/Bluetooth antenna
> 3. Main wiring harness
> 4. Antenna mounting hardware
>
> The PrevenTech™ kit does not contain all the hardware needed for the installation. SIM cards and connection wiring harnesses **must** be purchased separately.
>
> Figure 1, PrevenTech™ Kit Hardware.
>
> Environmental and Physical Requirements Operation and Storage Requirements:
>
> | Table 1, Operation and Storage Requirements |  |
> |---|---|
> | Circuitry Operation Temperature Range | -5°C to +70°C \[ 23 °F to 158 ˚F \] |
> | Storage Temperature Range | -30°C to +85°C \[ 86 °F to 185 ˚F \] |
> | Humidity | Up to 95 % - non-condensing |
>
> **Pre-Installation Steps**
>
> Prior to taking the PrevenTech™ hardware to the customer site, a bench test must be performed to verify that the system is functional and the procured SIM card is compatible with the system.
>
> 1. Register box by contacting CPS team at connectedsol.support@cummins.com. On the PrevenTech™ box, provide ID and IMEI numbers. Also, needed are the engine serial number (ESN), ECM calibration, hp rating, equipment OEM/model, unit number, location/mine site, and SIM card information.
>
> Figure 2, Identification label on Bottom of PrevenTech™ Box.
>
> 2. Remove telematics box cover and verify that dip switches are switched off (towards outboard position or to the “right” if the harness connector is at the top). These switches are internal resistors that are **not** needed.
>
> Figure 3, Interior of PrevenTech™ Box. Dip Switch Location Highlighted.
>
> 3. Procure 3G GSM SIM card (Standard 2FF size) or backward compatible 4G LTE SIM card. Note that the box will **not** work using a 4G card or a card that is configured to the CDMA network. Verify that there is adequate 3G coverage in the area. When activating the card, the IMEI number on the box label is required. Recommend that the customer and equipment is registered and access to www.preventech.cummins.com is activated. If the customer has **not** ordered SIM cards with active data plan, use a compatible SIM card with activated data plan for operational validation.
>
> 4. Install SIM card with notched tab on the outer side
>
> Figure 4, Interior of PrevenTech™ Box With SIM Card Installed.
>
> Figure 5, Clock Battery Location
>
> 5. Connect Antenna to Telematics box and place in an elevated position to get cellular signal.
>
> 6. Connect wiring harness to box. Connect VINPUT lead to 12/24V power source and GND lead to negative connection. Apply power. After 5 minutes, the Green Light should be Steady On. The Red Light should be Flashing (2 seconds OFF – 0 to 5 seconds ON). If the Red light is Steady On, it means that there is No cell connectivity. If this occurs, reference Appendix A for troubleshooting.
>
> 7. Determine J1939 CAN Bus connection strategy. There are a couple different methods to connect to the engine J1939 CAN Bus. This strategy chosen will determine what Peripheral Hardware needs to be ordered.
>
> - Option 1: Node off OEM J1939 CAN Bus
>
> Figure 6, CAN Bus Node
>
> - Option 2: Extend Engine Backbone to Telematics Box Harness.
>
> Figure 7, Extension Wiring Harness
>
> 8. General installation hardware is not included in the kit. items required to perform complete installation that are not included in the kit. These items will vary depending on application/model type.
>
> - Zip ties
> - Fuse holders
> - 5 amp fuse
> - Various electrical terminals/butt splices
> - Gland Nuts
> - Additional 18AWG Wire (If extension of wiring harness leads needed)
>
> **Installation Procedures**
>
> 1. Select J1939 Public CAN Bus 3-Pin Connection
>
> - It is possible for engines and equipment to have multiple CAN networks within their architecture – Public vs. Private. Identifying the Public J1939 CAN Bus is essential prior to installation of the PrevenTech™ telematics box. To verify the correct CAN Bus has been selected, contact the equipment OEM. Alternatively, check continuity between the selected 3-pin connector and the 9-Pin service connector.
>
> 2. Verify J1939 CAN Bus resistance by measuring between Positive and Negative terminal on the 9-Pin service connector (Pins C and D in picture below). If resistance measurement is 120 ohms, an additional terminating resistor **must** be added to the backbone. If the resistance measurement is less than 60 ohms, then a resistor **must** be removed.
>
> Figure 8, Connector Pin Diagram
>
> Install PrevenTech™ Telematics Box
>
> - Installation location must meet the following environment criteria:
> - Mount telematics box using mounting hardware.
>
> 4. Connect Wiring Harness
>
> - The PrevenTech™ wiring harness has several wires that are not utilized in the existing configuration. Make the following connections:
>
> Figure 9, Wiring Harness Breakout
>
> **Note · Примечание**
> Remove pin K4 on telematics box using a long nose small plier and slowly with a firm grip moving it in an up and down direction until it breaks. This prevents communication errors due to an internal harness miswiring issue of DO (Digital Outputs) wires.
>
> Figure 10, Telematics Box 48 Pin Connector Layout
>
> - Connect wiring harness to PrevenTech™ Telematics Box by inserting connector and then rotating lever into locked position.
>
> Figure 11, PrevenTech™ Wiring Harness Connection to PrevenTech™ Telematics Box
>
> 5. Install Antenna
>
> - GSM / GPS / WIFI antenna must be installed on the outside of the equipment, with direct line of sight to the sky.
> - Installed at least 40 cm from equipment operator
> - Consider wiring harness routing strategy and proximity to PrevenTech™ Telematics Box
> - Route antenna connectors through gasket, bracket, and retaining nut.
> - Secure to bracket and mount using two U-bolts provided.
> - Route antenna connectors to PrevenTech™ telematics box and match the connectors to the correct port on the box. Note: Antenna connector labeled “WIFI” **must** be connected to telematics box connector labeled “BT”.
>
> Figure 12, Antenna Harness Connected to Telematics Box and Antenna Mount on Exterior Of Application.
>
> - Create a strain relief by allowing at least 1 foot of cabling between the antennae ports and the placement of the strain relief.
> - Secure wiring harness along route using P-Clips or zip ties. Excess wiring harness should be neatly coiled up and secured to prevent from interfering with other components.
>
> 6. Apply power and after 5 mins verify that LED lights are on in accordance with the following tables. If LEDs do not give proper indication, reference Appendix A for troubleshooting steps.
>
> - Will turn on after approximately 30 seconds as the power has been supplied. If the equipment is receiving frames through the CAN0 port, the LED will flash at high speed indicating transmission.
>
> | **Green LED Indicator – CAN Operation** |  |
> |---|---|
> | **State** | **Indication** |
> | Steady on | Operating system initialized |
> | Flashing | Data is being transmitted on CAN0 |
> | Off | Operating system not initialized |
>
> - The red LED is used to indicate the communication status of the device. During the first 5 minutes since the device has been powered, the LED will be off. If the telematics box has not achieved connectivity after 5 minutes, the LED will light up steadily. In contrast, if 3G / GSM connectivity is stable for 5 minutes, the LED will flash every 2 seconds.
>
> | **Red LED Indicator – Network Connection** |  |
> |---|---|
> | **State** | **Indication** |
> | Steady on (after 5 minutes) | No 3G/GSM connectivity |
> | Flashing (2 seconds OFF – 0 to 5 seconds ON) | Stable 3G/GSM connectivity |
> | Off | Only first 5 minutes after powered on |
>
> 7. After equipment registration is verified, use the PrevenTech dashboard to verify GPS location and communication is active. If communication cannot be established, perform troubleshooting steps or contact Cummins CARE.
>
> APPENDIX A: Troubleshooting
>
> STEP 1A. Check for faulty equipment visibility on PrevenTech™ dashboard
>
> | **Conditions:** While equipment is on |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Log on to PrevenTech™ dashboard, https://preventech.cummins.com; Check dashboard for operation | Is equipment in question visible on dashboard? **Yes** | **2A** |
> | Is equipment in question visible on dashboard? **No** | **1B** |  |
>
> STEP 1B. Check for visibility of other equipment on PrevenTech™ dashboard
>
> | **Conditions:** While equipment is On |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check dashboard for visibility of other equipment | Is other equipment visible on dashboard? **YesNote:** Not an issue with dashboard | **2A** |
> | Is other equipment visible on dashboard? **No** | **Contact:** PrevenTech™ Regional Support Contact or care.cummins.com |  |
>
> STEP 2. Identify state of LEDs
>
> STEP 2A. Green LED flashing
>
> | **Conditions:** While equipment is on **Note:** 30 seconds after power is supplied; PrevenTech™ telematics box green LED will start to flash at high speed when receiving frames through PrevenTech™ telematics J1939 connection |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect green LED | Is green LED flashing? **YesNote:** Data is being transmitted on PrevenTech™ telematics box J1939 connection; PrevenTech™ telematics box should be connected to engine's J1939 connection, reference step **5A** | **2C** |
> | Is green LED flashing? **No** | **2B** |  |
>
> STEP 2B. Green LED steady on
>
> | **Conditions:** While equipment is on |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect green LED | Is green LED steady on? **YesNote:** Operating System initialized | **5A** |
> | Is green LED steady on? **NoNote:** Operating System not initialized | **3A** |  |
>
> STEP 2C. Red LED flashing
>
> | **Conditions:** While equipment is on |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect red LED | Is red LED flashing? **YesNote:** Stable 3G/GSM connectivity | **Check dashboard configuration informationContact:** PrevenTech™ Regional Support Contact or care.cummins.com |
> | Is red LED flashing? **No** | **2D** |  |
>
> STEP 2D. Red LED steady on
>
> | **Conditions:** While equipment is on **Note:** Red LED will be off for the first 5 minutes after power has been supplied to PrevenTech™ telematics box |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect red LED | Is red LED steady on? **YesNote:** No 3G/GSM connectivity | **6A** |
> | Is red LED steady on? **No** | **3A** |  |
>
> STEP 3. Identify state of power supply
>
> **Note · Примечание**
> PrevenTech™ telematics box internal cartridge battery will hold charge for period time after external power has been removed and will function as intended; when troubleshooting the external power supply, disconnect PrevenTech™ telematics box internal cartridge battery. If needed refer to Step 4 for PrevenTech™ telematics box internal battery fault finding, i.e. data time stamp variation on PrevenTech™ dashboard.
>
> STEP 3A. Fuse condition
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect inline fuse | Is fuse open? **YesRepair:** Replace fuse | **Repair Complete** |
> | Is fuse open? **No** | **3B** |  |
>
> STEP 3B. Power supply, ignition, and chassis ground wire condition
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Carefully inspect main harness wiring condition Reference Appendix H above. | Are power supply, ignition, and chassis ground wires in good condition with no damage, i.e. no tears? **Yes** | **3C** |
> | Are power supply, ignition, and chassis ground wires in good condition with no damage? **NoRepair:** Replace PrevenTech™ telematics box main harness | **Repair Complete** |  |
>
> STEP 3C. Power supply, ignition, and chassis ground connections
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Carefully inspect main harness connections | Are power supply, ignition, and chassis ground wires connected? **Yes** | **3D** |
> | Are power supply, ignition, and chassis ground wires connected? **NoRepair:** Connect wire(s) that are not connected | **Repair Complete** |  |
>
> STEP 3D. Main harness connection to PrevenTech™ telematics box
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect main harness connection to PrevenTech™ telematics box. Reference **Step 5** in Installation Instructions: PrevenTech™ Telematics Hardware above. | Is the main harness connected securely to PrevenTech™ telematics box? **Yes** | **3E** |
> | Is the main harness connected securely to PrevenTech™ telematics box? **NoRepair:** Connect and securely lock main harness | **Repair Complete** |  |
>
> STEP 3E. Condition of power supplied to motherboard
>
> | **Conditions:** While power is supplied to PrevenTech™ telematics box |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Open PrevenTech™ box and inspect LAN port on motherboard, reference Figure 39 above | Is LAN port light on? **Yes** | **3F** |
> | Is LAN port light on? **NoRepair:** Replace PrevenTech™ telematics box | **Repair Complete** |  |
>
> STEP 3F. Condition of LED(s) internal wiring
>
> | **Conditions:** While power is supplied to PrevenTech™ telematics box |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect LED(s) internal wiring, reference Figure 39 above | Are LED(s) on? **NoRepair:** Replace PrevenTech™ telematics box | **Repair complete** |
>
> STEP 4. PrevenTech™ internal battery conditions
>
> STEP 4A. Internal clock (round) battery condition
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check dashboard data time stamps Reference Figure 5 above. | Is there ambiguity in the data time stamp/real time clock? **YesNote:** Remove round battery using a thin flathead screwdriver and replace, check PrevenTech™ dashboard for functionality | **RepairComplete** |
>
> STEP 5. Equipment J1939 connections
>
> STEP 5A. Inspect equipment and PrevenTech™ telematics box J1939 connection
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect PrevenTech™ Telematics box J1939 connection with equipment | Is PrevenTech™ telematics box J1939 plug connected to equipment's J1939 public data connection? **Yes** | **5C** |
> | Is PrevenTech™ telematics box J1939 plug connected to equipment's J1939 public data connection? **No** | **5B** |  |
>
> STEP 5B. Equipment J1939 Public Connection
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure continuity from 9-pin service connector to 3-pin Deutsch connector | Was continuity confirmed? **YesRepair:** Connect PrevenTech™ telematics box J1939 connection to public data J1939 connection on equipment | **Repair Complete** |
> | Was continuity confirmed? **NoNote:** Repeat this step until equipment J1939 public connection is located | **Repeat Step** |  |
>
> STEP 5C. Measure equipment resistance
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disconnect the J1939 connection; using the equipment J1939 or 9 Pin service connector measure the equipment resistance, reference Figure 1 above. | Is the measured resistance 60 Ohms? **Yes** | **5E** |
> | Is the measured resistance 60 Ohms? **No** | **5D** |  |
>
> STEP 5D. Inspect J1939 backbone terminal resistors
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect J1939 connection terminal resistors; measure resistance. Reference Figure 7 and Figure 26 above. Note: ONLY two 120 Ohms resistors needed in parallel on backbone to achieve a total resistance of 60 Ohms | Is the measured resistance in each resistor 120 Ohms? **Yes** | **5E** |
> | Is the measured resistance in each resistor 120 Ohms? **NoRepair:** Discard and replace resistor(s) | **Repair Complete** |  |
>
> STEP 5E. Measure PrevenTech™ telematics box resistance
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure resistance on PrevenTech™ J1939 connection, reference Figure 1 above. | Is the measured resistance approximately 50 K-Ohms? **No** | **5F** |
> | Is the measured resistance approximately 50 K-Ohms? **YesNote:** No PrevenTech™ telematics resistance issue | **Repair Complete** |  |
>
> STEP 5F. PrevenTech™ telematics box resistance correction
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure resistance on PrevenTech™ 1939 connection, reference Figure 1 above. | Is the measured resistance approximately 0 Ohms? **YesNote:** Short in box **Repair:** Replace PrevenTech™ telematics box | **Repair Complete** |
> | Is the measured resistance approximately 120 Ohms? **YesRepair:** Ensure internal resistance dip switches are all to the right of the battery. Reference **Step 13** in Installation Instructions: PrevenTech™ Telematics Hardware above. | **Repair Complete** |  |
>
> STEP 6. Data transmission to PrevenTech™ dashboard
>
> STEP 6A. Antennae connections
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect antennae connections on PrevenTech™ telematics box, reference Step 11 in Installation Instructions: PrevenTech™ Telematics Hardware above | Are the antennae wires connect securely and correct to PrevenTech™ telematics box? **Yes** | **6B** |
> | Are the antennae wires connect securely and correct to PrevenTech™ telematics box? **NoRepair:** Correctly wire the antennae wires to the correct ports and securely connect. | **Repair Complete** |  |
>
> STEP 6B. Condition of antennae wires
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect wires between PrevenTech™ telematics box and antennae round transmitter, reference Step 11 in Installation Instructions: PrevenTech™ Telematics Hardware above | Are one or more antennae wires damaged, i.e. abrasion to conduit, round transmitter physical damage? **YesRepair:** Replace and route antennae to PrevenTech™ Telematics box | **Repair Complete** |
> | Are one or more antennae wires damaged, i.e. abrasion to conduit, round transmitter physical damage? **No** | **6C** |  |
>
> STEP 6C. SIM card status
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Remove SIM card Reference Figure 14 above. | Are SIM card and PrevenTech™ telematics box motherboard contacts dirty or dull? **YesRepair:** Clean all contacts, reinstall SIM, and check for data transmission | **Repair Complete** |
> | Are SIM card and PrevenTech™ telematics box motherboard contacts dirty or dull? **No** | **6D** |  |
>
> STEP 6D. SIM card data
>
> | **Conditions:** While equipment is off **Note:** Consider using a mobile phone compatible with SIM card, same network provider, to check data functionality; if data transmission is established, replacement of PrevenTech™ telematics box may be necessary |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check data usage with network provider | Has data plan maximum limit been reached? **YesRepair** May consider upgrading to a higher data plan | **Repair Complete** |
> | Has data plan maximum limit been reached? **NoRepair:** Corrupt SIM card; obtain another SIM card and re-configure PrevenTech™ Telematics box | **Repair Complete** |  |
>
> **Appendix B: Installation Examples**
>
> The following pictures document some of the installations conducted on various applications. These are for reference only. Each installation requires evaluation to determine what the correct strategy is for that particular unit.
>
> Figure 13, Connecting into J1939 CAN Bus using Gender Changer and Y Connector
>
> Figure 14, Telematics Box Installation Example
>
> **Appendix C: WIFI Transmission**
>
> Depending on site location, units may have either a telematics box with an external ethernet port of an internal ethernet port.
>
> If it is determined that telematics box has an internal ethernet port, a small hole will need to be drilled above connection labeled “B” for it to be exposed.
>
> Figure 15, PrevenTech™ Telematics Box with Internal Ethernet Port
>
> Firmware needs to be updated for both PrevenTech™ telematics box types once device can communicate online.
>
> EMD Configuration Utility:
>
> - EMD is a downloadable configuration program needs to configure mesh network to telematics device.
> - Follow the steps below to download the program:
>
> Connect computer to device using a USB to RS-232 modem adapter and available RS-232 connection on device harness.
>
> Figure 16, Device Harness RS-232 Connection
>
> Launch EMD configuration utility and wait until dialog box appears asking for a serial port to use for communication with device, by default device will communicate at 115200 bps. Select appropriate and click OK button.
>
> Figure 17, EMD Configuration Utility Window
>
> A window pops up asking for a device password. Input correct password and click OK.
>
> **Note · Примечание**
> Password of the device **must** be obtained by contacting PrevenTech™ team.
>
> Figure 18, Device Password Input Window
>
> DNS Server information required from customer's IT departed to link devices.
>
> - Mode: Switch to Manual
> - IP Address:
> - Network Mask:
> - Gateway:
> - DNS1:
> - DNS2:
>
> Under the Network tab, input information gathered in appropriate locations and click Apply.
>
> Figure 19, Network Configuration Window
>
> Installation Considerations:
>
> - Depending on the mine site, if the unit's current POE switch box does not have any available Ethernet ports, a new POE switch box may be needed to include the mesh network integration.
> - A RJ45 – RJ45 CAT6 Ethernet cable runs from the device to the POE switch box.
> - A M12 (8-pin) – RJ45 CAT6 will be run from the POE switch box to the mesh network modem.
>
> Figure 20, POE/Modem Installation Example
>
> ### Document History
