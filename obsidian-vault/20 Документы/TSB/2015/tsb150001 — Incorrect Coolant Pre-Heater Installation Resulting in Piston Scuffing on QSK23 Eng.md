---
type: "TSB"
doc: "tsb150001"
title_en: "Incorrect Coolant Pre-Heater Installation Resulting in Piston Scuffing on QSK23 Engines"
released: "2015-01-21"
modified: "2015-01-21"
engines:
  - "85017333"
families:
  - "QSK23"
figures: 5
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2015/tsb150001.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb150001.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QSK23"
  - "год/2015"
  - "перевод/машинный"
---

# Incorrect Coolant Pre-Heater Installation Resulting in Piston Scuffing on QSK23 Engines

> [!abstract] TSB · `tsb150001`
> **Двигатели:** [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23
> **Даты:** выпущен 2015-01-21 · изменён 2015-01-21
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2015/tsb150001.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb150001.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Неправильная установка предварительного нагревателя охлаждающей жидкости, приводящая к поршневой скаффингу на двигателях QSK23

### Суть проблемы

Преднагреватель охлаждающей жидкости **не** был правильно подключен к двигателю для правильного нагрева охлаждающей жидкости. Это приводит к тому, что двигатель **не** правильно нагревается перед использованием при номинальной скорости и нагрузке. Это может привести к потрепанному поршню (поршням).

### Подтверждение

На рисунках 1-4 ниже показана потасовка поршня в центре линии, которая возникла в результате правильного нагрева двигателя **не** перед использованием на номинальной скорости и нагрузке.

![[08r00135.png]]

Рисунок 1 Противоударная сторона Piston Scuff на цилиндрическом гильзе

![[08r00136.png]]

Рисунок 2, Thrust Side Piston Scuff на цилиндрическом гильзе

![[08r00137.png]]

Рисунок 3, Анти-Трастная сторона Piston Scuff

![[08r00138.png]]

Рисунок 4, Thrust Side Piston Scuff

Проверьте впускные и выпускные соединения охлаждающей жидкости перед нагреванием. Впуск охлаждающей жидкости перед нагреванием **должен быть подключен к впускному соединению (2 или 3). Отвод охлаждающей жидкости для предварительного нагрева **должен быть соединен с крышкой блока цилиндров на стороне выхлопа двигателя (1). См. рисунок 5.

> [!note] Примечание
> Пластина крышки блока цилиндров может потребоваться изменить, чтобы добавить место соединения розетки охлаждающей жидкости перед нагревателем.

![[08r00139.png]]

Рисунок 5, порты подключения охлаждающего предварительного нагревателя

Для получения информации о потоке охлаждающей жидкости используйте следующую процедуру в руководстве по устранению неполадок и ремонту QSK23, Bulletin [[4021375 — QSK23 Troubleshooting and Repair Manual\|4021375]].[[89-200-003 — Flow Diagram, Cooling System|См. процедуру 200-003 в разделе F.]]

### Решение

Если впускные и выпускные соединения охлаждающей жидкости перед нагреванием неверны, исправьте их на рисунке 5 выше. Это обеспечит надлежащую работу охлаждающей жидкости перед нагреванием и нагреванием двигателя.

В дополнение к предварительному нагревателю охлаждающей жидкости, есть другие методы работы в холодную погоду, которые следует учитывать:

- Убедитесь, что температура охлаждающей жидкости составляет 10 ° C \[50 ° F \], а температура масла -4 ° C \[25 ° F \], прежде чем выключать двигатель с низкой холостой работы.
- Используйте правильный смазочный масло для текущих условий окружающей среды. Используйте следующую процедуру в руководстве для владельцев QSK23, в бюллетене [[4915552 — QSK23 Owners Manual\|4915552]].[[102-018-003 — Lubricating Oil Recommendations and Specifications|См. процедуру 018-003 в разделе V.]]
- Для QSK23, используемого в экскаваторах Hitachi EX1200, калибровка модуля управления двигателем (ECM) должна быть D50098 ревизией 02 или выше. Эта калибровка задержит увеличение скорости бездействия в холодных условиях окружающей среды.

Для получения дополнительной информации о холодной погоде. См. Service Bulletin, Operation of Diesel Engines in Cold Climates, Bulletin.[[3379009 — Operation of Diesel Engines in Cold Climates|3379009]].

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## Incorrect Coolant Pre-Heater Installation Resulting in Piston Scuffing on QSK23 Engines
>
> ### Core Issue
>
> The coolant pre-heater has **not** been correctly connected to the engine for proper heating of the coolant. This results in the engine **not** being warmed properly prior to use at rated speed and load. This can lead to a scuffed piston(s).
>
> ### Confirmation
>
> Figures 1 through 4 below show center line piston scuffing that resulted from an engine **not** being warmed properly prior to use at rated speed and load.
>
> Figure 1, Anti-Thrust Side Piston Scuff on Cylinder Liner
>
> Figure 2, Thrust Side Piston Scuff on Cylinder Liner
>
> Figure 3, Anti-Thrust Side Piston Scuff
>
> Figure 4, Thrust Side Piston Scuff
>
> Check the coolant pre-heater coolant inlet and outlet connections. The coolant pre-heater coolant inlet **must** be connected to the water inlet connection (2 or 3). The coolant pre-heater outlet **must** be connected to the cylinder block cover plate on the exhaust side of the engine (1). See Figure 5.
>
> **Note · Примечание**
> The cylinder block cover plate may need to be modified to add a coolant pre-heater outlet connection location.
>
> Figure 5, Coolant Pre-Heater Connection Ports
>
> For coolant flow information, use the following procedure in the QSK23 Troubleshooting and Repair Manual, Bulletin [[4021375 — QSK23 Troubleshooting and Repair Manual\|4021375]]. [[89-200-003 — Flow Diagram, Cooling System|Refer to Procedure 200-003 in Section F.]]
>
> ### Resolution
>
> If the coolant pre-heater coolant inlet and outlet connections are incorrect, correct them per Figure 5 above. This will ensure proper coolant pre-heater operation and heating of the engine.
>
> In addition to a coolant pre-heater, there are other cold weather operating techniques to consider:
>
> - Ensure the coolant temperature is 10°C \[ 50°F \] and the oil temperature is -4°C \[ 25°F \] before taking the engine off of low idle.
> - Use the correct grade of lubricating oil for the current ambient conditions. Use the following procedure in the QSK23 Owners Manual, Bulletin [[4915552 — QSK23 Owners Manual\|4915552]]. [[102-018-003 — Lubricating Oil Recommendations and Specifications|Refer to Procedure 018-003 in Section V.]]
> - For QSK23 used in Hitachi EX1200 excavators, the engine control module (ECM) calibration **must** be D50098 revision 02 or higher. This calibration will delay idle increase speed in cold ambient conditions.
>
> For additional cold weather operation information. Refer to Service Bulletin, Operation of Diesel Engines in Cold Climates, Bulletin [[3379009 — Operation of Diesel Engines in Cold Climates|3379009]].
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Document History
