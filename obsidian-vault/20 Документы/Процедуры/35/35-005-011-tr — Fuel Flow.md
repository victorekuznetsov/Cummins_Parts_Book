---
type: "Процедура"
doc: "35-005-011-tr"
title_en: "Fuel Flow"
modified: "2009-02-12"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
figures: 8
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-005-011-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-005-011-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/35"
  - "перевод/машинный"
---

# Fuel Flow

> [!abstract] Процедура · `35-005-011-tr`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 5 - Fuel System - Group 05
> **Даты:** изменён 2009-02-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-005-011-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-005-011-tr.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Первичная проверка

Освободите топливный поток в запорном клапане, пока двигатель работает. Если топливо не выходит из соединения, насос должен быть заправлен.

![[fp8hoka.png]]

### Испытание на давление

Минимальное давление в коленке

Подключите датчик измерения давления к быстрому отключению топливного насоса.

Начните сворачивать двигатель и наблюдайте за сворачивающимся давлением топлива.

| Минимальное давление на топливо |  |  |  |
|---|---|---|---|
|  | каша |  | пси |
| CELECTTM или CELECTTM Plus | 172 | Мин | 25 |
| НТС | 34 | Мин | 5 |

Если давление топлива ниже спецификации, убедитесь, что есть подачу топлива к насосу и что он **не **ограничен.[[35-006-020-tr — Fuel Inlet Restriction|См. процедуру 006-020 в разделе 6.]]При необходимости заправьте топливный насос.[[35-005-016-tr — Fuel Pump|См. процедуру 005-016 в разделе 5.]]

![[fp8gadb.png]]

Минимальное рабочее давление

Подключите датчик измерения давления от 0 до 2068 кПа \[0 до 300 psi\] к быстрому отключению, установленному на топливный насос.

![[fp8gadb.png]]

| Минимальное давление топлива |  |  |  |
|---|---|---|---|
|  | каша |  | пси |
| Во время чеканки | 172 | Мин | 25 |
| 1200 об/мин | 827 | Мин | 120 |
| Оправленный rpm | 1034—1241 | Мин | 150-180 |

![[oi101v09.png]]

### Тест на утечку

Установите 457 мм \[18 в \] куска прозрачной трубки на всасывающей стороне зубчатого насоса или головки крепления топливного фильтра. Tygon R-3603 является правильным размером для использования со стандартными швейными фитингами StratoflexTM № 10.

Добавьте 457 мм \[18 в \] куска прозрачной трубы к существующей линии всасывания топлива. Не заменяйте любую часть всасывающей линии, чтобы установить 457 мм [18 в] куска прозрачной трубки.

![[05200040.png]]

Запустите двигатель и позвольте воздуху очищаться от прозрачной трубы. Воздушные пузырьки могут **не** появляться.

Выключите двигатель и наблюдайте за прозрачной трубкой.

Как правило, в прозрачной трубке появится воздушное пространство, которое вытягивается из верхней части топливного фильтра.

![[05200041.png]]

Наблюдайте за топливом в прозрачной трубе. Он перестанет двигаться в течение 1 минуты, если система не будет работать. Если топливо продолжает двигаться в сторону топливного бака, в системе происходит утечка.

Обратите внимание, с какого направления пузырьки воздуха попадают в прозрачную трубку. Если они поступают со стороны топливного бака, утечка находится в охлаждающей пластине, фитингах, топливной линии или топливном баке.

![[05200042.png]]

Если топливо не двигалось сразу, то пусть автомобиль сидит около 1 часа. Если нет движения топлива, система запечатана и не вызовет тяжелую работу из-за отвода всасывающих линий.

Удалите чистую трубку и соедините всасывающую линию обратно с ее исходным соединением.

![[05200042.png]]


> [!quote]- Original (English) · английский оригинал
> ### Initial Check
>
> Loosen the fuel line at the shutoff valve while the engine is cranking. If fuel does **not** come out of the connection, the pump **must** be primed.
>
> ### Pressure Test
>
> Minimum Cranking Pressure
>
> Connect a pressure gauge to the quick disconnect fitting of the fuel pump.
>
> Start cranking the engine, and observe the cranking fuel pressure.
>
> | Minimum Cranking Fuel Pressure |  |  |  |
> |---|---|---|---|
> |  | kpa |  | psi |
> | CELECT™ or CELECT™ Plus | 172 | MIN | 25 |
> | STC | 34 | MIN | 5 |
>
> If the fuel pressure is below the specification, check to be sure there is a fuel supply to the pump and that it is **not** restricted. [[35-006-020-tr — Fuel Inlet Restriction|Refer to Procedure 006-020 in Section 6.]] Prime the fuel pump if necessary. [[35-005-016-tr — Fuel Pump|Refer to Procedure 005-016 in Section 5.]]
>
> Minimum Operating Pressure
>
> Connect a 0 to 2068 kPa \[0 to 300 psi\] pressure gauge to the quick disconnect fitting to the fuel pump.
>
> | Minimum Fuel Pressure |  |  |  |
> |---|---|---|---|
> |  | kpa |  | psi |
> | During Cranking | 172 | MIN | 25 |
> | 1200 rpm | 827 | MIN | 120 |
> | Goverened rpm | 1034 to 1241 | MIN | 150 to 180 |
>
> ### Leak Test
>
> Install a 457 mm \[18 in\] piece of clear tubing on the suction side of the gear pump or the fuel filter head. Tygon™ R-3603 is the correct size for use with standard Stratoflex™ Number 10 hose fittings.
>
> Add the 457 mm \[18 in\] piece of clear tubing to the existing fuel suction line. Do **not** replace any portion of the suction line to install the 457 mm \[18 in\] piece of clear tubing.
>
> Start the engine and allow the air to purge from the clear tubing. Air bubbles can **not** appear.
>
> Shut off the engine, and observe the clear tubing.
>
> Generally, an air space will appear in the clear tubing that is drawn from the top of the fuel filter.
>
> Observe the fuel in the clear tubing. It will stop moving within 1 minute if the system is leak free. If the fuel continues to move toward the fuel tank, there is a leak in the system.
>
> Observe from which direction air bubbles are coming into the clear tubing. If they are coming from the fuel tank side, the leak is in the cooling plate, fittings, fuel line, or fuel tank.
>
> If the fuel did **not** move immediately, let the vehicle sit for about 1 hour. If there is no movement of the fuel, the system is sealed and will **not** cause a hard start due to drainback of the suction lines.
>
> Remove the clear tubing, and connect the suction line back to its original connection.
