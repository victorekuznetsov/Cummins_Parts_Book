---
type: "Процедура"
doc: "10-011-056"
title_en: "Exhaust System Diagnostics"
modified: "2023-08-04"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
manuals:
  - "3666239"
figures: 12
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-011-056.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-011-056.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSX15"
  - "группа/10"
  - "перевод/машинный"
---

# Exhaust System Diagnostics

> [!abstract] Процедура · `10-011-056`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Входит в руководства:** [[3666239 — Signature™, ISX, and QSX15 Service Manual|3666239]]
> **Секции:** Section 11 - Exhaust System - Group 11
> **Даты:** изменён 2023-08-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-011-056.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-011-056.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Следующая процедура содержит шаги по устранению неполадок и информацию о системе послеоперационного лечения.

![[nobox.png]]

Утечки в выхлопной системе могут вызвать запах выхлопных газов или белый дым.

Проверьте выхлопные трубы на наличие утечек, трещин и свободных соединений. См. процедуру 010-024 в разделе 10.

Затягивать выхлопные зажимы, если это необходимо. См. спецификации OEM и правильное момент затяжки.

Может потребоваться выполнить стационарную (припаркованную) регенерацию для обнаружения утечек выхлопных газов.[[101-014-013 — Aftertreatment Testing|См. процедуру 014-013 в разделе 14.]]

![[10d00395.png]]

Температура окружающей среды влияет на продолжительность времени, необходимого для выполнения стационарной (припаркованной) регенерации, поскольку двигатель должен работать усерднее, чтобы увеличить температуру выхлопных газов до соответствующих уровней при низких температурах окружающей среды.

При низких температурах окружающей среды (приблизительно -18 ° C \[ 0° F \] или холоднее) стационарная (припаркованная) регенерация может занять больше времени. При чрезвычайно низких температурах окружающей среды стационарная (припаркованная) регенерация может быть неполной.

В этих случаях может потребоваться подогреть двигатель до рабочей температуры перед началом стационарной (припаркованной) регенерации или переместить транспортное средство в место с более высокими температурами окружающей среды.

![[nobox.png]]

Изготовитель транспортного средства имеет возможность установки двух переключателей, которые контролируют функцию последующей обработки: Стартовый выключатель и разрешительный выключатель.

Стартовый переключатель (называемый Diesel Particulate Filter Regeneration Start Switch в электронном сервисном оборудовании INSITETM) используется для запуска стационарной (припаркованной) регенерации. Производитель транспортного средства может также ссылаться на этот переключатель как на "стационарный переключатель регенерации", "стартовый переключатель" или "припаркованный переключатель регенерации".

Переключатель разрешения (называемый Diesel Particulate Filter Permit Switch в электронном сервисном оборудовании INSITETM) используется для того, чтобы оператор мог отключить активную регенерацию, если это необходимо. Производитель транспортного средства может также ссылаться на этот переключатель как на "переключатель ингибирования", "переключатель остановки" или "переключатель отключения".

Стартовый переключатель может быть жестко подключен к ECM или мультиплексирован по сравнению с мультиплексированием J1939.

Если стартовый переключатель является проводным, он разделяет значок ECM с диагностическим переключателем. Когда переключатель включен, а двигатель выключен, ECM интерпретирует этот сигнал как диагностический переключатель. Когда переключатель включен и двигатель работает, ECM интерпретирует этот сигнал как стартовый переключатель.

Если стартовый выключатель имеет мультиплекс J1939, сигнал для этого выключателя передается по шине данных J1939 CAN.

Сигнал J1939-мультиплексного стартового переключателя имеет приоритет над сигналом жесткого стартового переключателя, поэтому, если стартовый переключатель включен по сравнению с J1939, проводной сигнал игнорируется двигателем ECM.

Настройка по умолчанию для стартового переключателя отключена. Если стартовый выключатель включен в инструмент электронного обслуживания INSITETM, но выключатель не установлен (либо в жесткой проводах J1939-multiplexed), статус переключателя останется выключенным.

Положение стартового переключателя можно контролировать с помощью инструментария электронного сервиса INSITETM на экране монитора данных / блогера.

По умолчанию настройка для переключения разрешения является недоступной.

Если выключатель разрешений включен с помощью электронного инструментария обслуживания INSITETM, но выключатель не установлен (либо проводной, либо мультиплексированный J1939), статус выключателя останется выключенным.

Если транспортное средство эксплуатируется в течение длительного периода времени с выключателем разрешения, могут возникнуть коды неисправностей для вышеуказанных нормальных уровней нагрузки на сажу фильтра для дизельных твердых частиц после обработки (коды неисправности 1921, 1922 и 2639).

Если после обработки дизельный фильтр сажи с твердыми частицами достигает умеренно тяжелого уровня (код по умолчанию 2639), и выключатель разрешения отключен, ECM также регистрирует код по умолчанию 2777.

Если переключатель разрешения мультиплексирован и, следовательно, ENABLED в разделе «Особенности и параметры» J1939 в инструменте электронного обслуживания INSITETM, он должен быть включен в разделе «Особенности и параметры после обработки» в инструменте электронного обслуживания INSITETM. Если это не так, то регенерация будет подавлена.

Переключатель разрешения может быть жестко подключен к ECM **только **в калибровках аварийного транспортного средства. Для всех других неаварийных калибровок переключатель разрешения может быть только J1939-мультиплексированным по шине данных J1939 CAN.

В случае аварийных калибровок транспортных средств, когда разрешительный выключатель жестко подключен, разрешительный выключатель заменяет выключатель типа губернатора.

Сигнал переключателя с мультиплексным разрешением J1939 имеет приоритет над сигналом переключателя с жестким приводом, поэтому, если переключатель с разрешением включен по сравнению с J1939, сигнал с жестким приводом игнорируется двигателем ECM.

Положение переключателя разрешения можно контролировать с помощью инструментария электронного сервиса INSITETM на экране монитора данных / блогера:

- Когда переключатель разрешений включен, активная регенерация разрешена.
- Когда выключатель разрешения отключен, активная регенерация не допускается.

![[11d00294.png]]

Если датчики температуры выхлопных газов после обработки **не подключены должным образом или если проводка в электропроводке между двигателем и после обработки **не** верна, двигатель может испытывать частые DPF лампы освещения или стационарные (припаркованные) регенерации, которые не завершены**.

Проверить разъемы датчика температуры после обработки выхлопных газов, чтобы убедиться, что они подключены к правильному разъему на проводах системы после обработки. Два датчика температуры имеют идентичные разъёмы проводов. Поскольку датчики имеют одинаковый номер детали, можно установить проводные разъёмы жгута на неправильный датчик.

Для проверки правильного расположения датчиков используйте инструмент электронного обслуживания INSITETM для мониторинга следующих параметров с включенным ключом зажигания, но с работающим двигателем **не**.

- После обработки катализатора окисления дизельного топлива впускной датчик температуры сигнала напряжения (V)
- После обработки дизельного фильтра для впуска температуры датчик сигнала напряжения (V)
- После обработки дизельного фильтра твердых частиц выходной датчик температуры сигнала напряжения (V).

Отключите каждый из датчиков температуры выхлопных газов после обработки, по одному за раз.

Если напряжение изменяется, когда датчик отключен, разъём проводов подключается к правильному датчику.

Если напряжение не изменяется, когда датчик отключен, переключите местоположение разъема на другой датчик температуры, отключите его и проверьте изменение напряжения.

Неправильно собранная проводка после обработки может быть проверена путем отключения каждого из датчиков температуры выхлопных газов после обработки.

**только **метод проверки для неправильной сборки проводов после обработки жгута является проверка проводов жгута разъемы для правильной установки штифта. См. схему проводов двигателя для идентификации контакта разъема и местоположения.

![[19c01217.png]]

При выполнении стационарной (припаркованной) регенерации, следите за температурой выхлопных газов в последующей обработке, чтобы определить, почему стационарная (припаркованная) регенерация будет **не** завершена.

Возможные причины стационарной (припаркованной) регенерации, которая не будет завершена, включают:

- Неправильно собранная электропроводка после обработки
- Высокое сопротивление датчика температуры выхлопных газов обратной цепи
- После обработки датчики температуры выхлопных газов, установленные в неправильном месте
- Заглушенный после обработки дизельный катализатор окисления
- Неисправный турбокомпрессор.

Нормальная стационарная (припаркованная) регенерация будет следовать показанному шаблону.

- Линия разреза предназначена для датчика температуры впускного отверстия дизельного катализатора окисления после обработки.
- Пунктирная линия предназначена для датчика температуры впускного отверстия дизельного фильтра твердых частиц после обработки.
- Твердая линия предназначена для датчика температуры выходного отверстия дизельного фильтра твердых частиц после обработки.

Когда начинается стационарная (припаркованная) регенерация (1), все три температуры должны быть примерно одинаковыми и должны увеличиваться с одинаковой скоростью.

В этом примере проводка к датчикам температуры после обработки представляется правильной, поскольку все они считывают примерно одну и ту же температуру в начале стационарной (припаркованной) регенерации и увеличиваются с одинаковой скоростью.

После обработки инъекции начинаются, когда все три температуры достигают приблизительно 288 ° C [550° F ] (2).

После начала инъекций после обработки температура впускного катализатора дизельного окисления может незначительно изменяться, но обычно остается между 260 и 399 ° C [500 и 750 ° F ].

После обработки дизельный фильтр твердых частиц температура входа и выхода увеличится примерно до 482-649 ° C [от 900 до 1200° F ]. Температура может изменяться во время стационарной (припаркованной) регенерации, поскольку количество топлива, впрыскиваемого во время послеоперационной инъекции, изменяется для поддержания постоянной температуры.

После обработки дизельный фильтр твердых частиц температуры входа и выхода останутся при этой температуре в течение всего периода стационарной (припаркованной) регенерации.

![[11d00299.png]]

Этот график иллюстрирует стационарную (припаркованную) регенерацию, где блокируется вход катализатора окисления дизельного топлива после обработки.

- Линия разреза предназначена для датчика температуры впускного отверстия дизельного катализатора окисления после обработки.
- Пунктирная линия предназначена для датчика температуры впускного отверстия дизельного фильтра твердых частиц после обработки.
- Твердая линия предназначена для датчика температуры выходного отверстия дизельного фильтра твердых частиц после обработки.

В этом состоянии скорость двигателя увеличится до стационарной (припаркованной) скорости регенерации от 1000 до 1400 об/мин.

Повышение температуры после обработки до температуры после обработки может занять больше времени, чем обычно, если вход в катализатор окисления дизельного топлива после обработки подключен, ограничивая часть потока выхлопных газов.

После того, как после обработки начинается впрыск (2), после обработки дизельного фильтра твердых частиц температура входа и выхода будет сильно отличаться из-за заглубленного после обработки дизельного катализатора окисления, не способного окислять впрыскиваемое топливо. После обработки дизельный фильтр твердых частиц имеет некоторую способность окислять впрыскиваемое топливо, но может **не** поддерживать это состояние, не повреждая фильтрующий материал с течением времени. Возможно, что белый дым будет присутствовать из выхлопной трубы автомобиля во время этого состояния.

В этом примере проводка к датчикам температуры после обработки представляется правильной, поскольку все они считывают примерно одну и ту же температуру в начале стационарной (припаркованной) регенерации и увеличиваются с одинаковой скоростью.

Возможная причина этого состояния - заглушенный после обработки дизельный катализатор окисления.[[101-011-049-tr — Aftertreatment Diesel Oxidation Catalyst|См. процедуру 011-049 (катализатор окисления дизельного топлива после обработки) в разделе 11 для проверки катализатора окисления дизельного топлива после обработки.]]

![[11d00300.png]]

Этот график иллюстрирует стационарную (припаркованную) регенерацию, когда двигатель может **не** наращивать достаточно тепла для запуска после обработки.

- Линия разреза предназначена для датчика температуры впускного отверстия дизельного катализатора окисления после обработки.
- Пунктирная линия предназначена для датчика температуры впускного отверстия дизельного фильтра твердых частиц после обработки.
- Твердая линия предназначена для датчика температуры выходного отверстия дизельного фильтра твердых частиц после обработки.

Скорость двигателя, вероятно, увеличится до стационарной (припаркованной) скорости регенерации от 1000 до 1400 об/мин, но поскольку температуры после обработки увеличиваются недостаточно для начала послеоперационного впрыска, стационарная (припаркованная) регенерация будет **не** завершена.

Возможные причины этого вопроса включают:

- Высокое сопротивление в цепи возврата датчика температуры выхлопных газов. Используйте следующую процедуру в руководстве по устранению неполадок и ремонту электронных систем управления ISX CM871 и ISM CM876, Bulletin 4021560.[[99-019-360 — Resistance Measurement Using a Multimeter|См. процедуру 019-360 в разделе 19.]]
- Неисправный турбокомпрессор. Используйте следующую процедуру, чтобы проверить, что оборудование для сектора турбокомпрессоров имеет полный ход.[[10-010-134 — Variable Geometry Turbocharger Actuator, Electric|См. процедуру 010-134 в разделе 10.]]
- Низкая температура окружающей среды. Переместите автомобиль в место с более высокими температурами окружающей среды.

![[11d00301.png]]

Этот график иллюстрирует стационарную (припаркованную) регенерацию, когда проводка к датчикам температуры после обработки неверна.

- Линия разреза предназначена для датчика температуры впускного отверстия дизельного катализатора окисления после обработки.
- Пунктирная линия предназначена для датчика температуры впускного отверстия дизельного фильтра твердых частиц после обработки.
- Твердая линия предназначена для датчика температуры выходного отверстия дизельного фильтра твердых частиц после обработки.

В этом состоянии скорость двигателя увеличится до стационарной (припаркованной) скорости регенерации от 1000 до 1400 об/мин.

После обработки впрыск **не **происходит в этом состоянии, потому что после обработки дизельного катализатора окисления температура входа не достигает необходимой температуры. Поскольку после обработки инъекции **не происходит, температуры после обработки должны **не читать по-разному.

Возможной причиной этого состояния является неправильно собранная проводка после обработки жгута. См. раздел проводов датчика температуры выхлопных газов после обработки этой процедуры.

![[11d00302.png]]

Этот график иллюстрирует стационарную (припаркованную) регенерацию, где разъемы к датчику температуры впускного катализатора окисления дизельного топлива после обработки и датчику температуры впускного фильтра дизельных твердых частиц после обработки обращены вспять.

- Линия разреза предназначена для датчика температуры впускного отверстия дизельного катализатора окисления после обработки.
- Пунктирная линия предназначена для датчика температуры впускного отверстия дизельного фильтра твердых частиц после обработки.
- Твердая линия предназначена для датчика температуры выходного отверстия дизельного фильтра твердых частиц после обработки.

В этом состоянии скорость двигателя увеличится до стационарной скорости регенерации от 1000 до 1400 об/мин.

После лечения инъекции могут произойти в этом состоянии (2). Однако после обработки дизельного катализатора окисления температура впуска увеличивается после начала инъекции после обработки, в то время как после обработки дизельного фильтра твердых частиц температура впуска остается постоянной.

Возможная причина этого состояния заключается в том, что разъемы к датчику температуры впускного катализатора окисления дизельного топлива после обработки и датчику температуры впускного фильтра дизельных твердых частиц после обработки обращены вспять. См. раздел проводов датчика температуры выхлопных газов после обработки этой процедуры.

![[11d00303.png]]

Регенерация, которая будет **не** полной, может быть вызвана неисправностями в EGR, турбокомпрессорных системах с изменяемой геометрией или заправкой топливом. Эти неисправности не позволяют после обработки достичь необходимой температуры для впрыска топлива после обработки.

При выполнении стационарной (припаркованной) регенерации, проконтролируйте следующие параметры, чтобы определить, почему стационарная (припаркованная) регенерация будет **не** завершена:

- Дифференциальное давление EGR
- Измерение позиции клапана EGR (Percent Open)
- Давление выхлопных газов
- Давление во впускном коллекторе
- Процентная нагрузка
- Измерение положения турбокомпрессора (закрыто на процент)
- Скорость турбокомпрессора

![[nobox.png]]

Во время стационарной (припаркованной) регенерации это типичные значения для здоровой системы.

| Параметр | Измерение |
|---|---|
| Дифференциальное давление EGR | Менее 2 кПа[0,6 in-Hg] |
| Измерение позиции клапана EGR (Percent Open) | Менее двух процентов |
| Давление выхлопных газов | 350-520 кПа[103-154 in-Hg] |
| Давление во впускном коллекторе | 18 - 122 кПа[5 - 36 in-Hg] |
| Процентная нагрузка | Менее 12% |
| Измерение положения турбокомпрессора (закрыто на процент) | 87-96 процентов |
| Скорость турбокомпрессора | От 30 000 до 52 000 об/мин |

> [!note] Примечание
> Процентная нагрузка может колебаться, когда вентилятор двигателя циклически включается и выключается.

![[nobox.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The following procedure contains troubleshooting steps and information regarding the aftertreatment system.
>
> Leaks in the exhaust system can cause exhaust odor or white smoke.
>
> Inspect the exhaust piping for leaks, cracks, and loose connections. Refer to Procedure 010-024 in Section 10.
>
> Tighten the exhaust clamps, if necessary. Refer to the OEM specifications and the correct torque value.
>
> It may be necessary to perform a stationary (parked) regeneration to locate exhaust leaks. [[101-014-013 — Aftertreatment Testing|Refer to Procedure 014-013 in Section 14.]]
>
> The ambient temperature affects the length of time it will take to perform a stationary (parked) regeneration because the engine must work harder to increase the exhaust temperatures to the appropriate levels in cold ambient temperatures.
>
> In cold ambient temperatures (approximately -18°C \[ 0°F \] or colder), stationary (parked) regeneration may take longer to complete. In extremely cold ambient temperatures, stationary (parked) regeneration may **not** complete.
>
> In these cases, it may be necessary to warm the engine to operating temperature before starting the stationary (parked) regeneration, or to move the vehicle to a location with higher ambient temperatures.
>
> The vehicle manufacturer has the option of installing two switches that control aftertreatment function: the start switch and the permit switch.
>
> The start switch (called the Diesel Particulate Filter Regeneration Start Switch in INSITE™ electronic service tool) is used to start a stationary (parked) regeneration. The vehicle manufacturer may also reference this switch as a "stationary regeneration switch," "start switch," or "parked regeneration switch".
>
> The permit switch (called the Diesel Particulate Filter Permit Switch in INSITE™ electronic service tool) is used to allow the operator to disable active regeneration, if necessary. The vehicle manufacturer may also reference this switch as an "inhibit switch," "stop switch," or "disable switch".
>
> The start switch can be hardwired to the ECM, or it can be multiplexed over J1939 multiplexing.
>
> If the start switch is hardwired, it shares an ECM pin with the diagnostic switch. When the switch is turned ON and the engine is OFF, the ECM interprets this signal as the diagnostic switch. When the switch is turned ON and the engine is running, the ECM interprets this signal as the start switch.
>
> If the start switch is J1939-multiplexed, the signal for this switch is broadcast over the J1939 data link.
>
> A J1939-multiplexed start switch signal has priority over a hardwired start switch signal, therefore if the start switch is enabled over J1939, the hardwired signal is ignored by the engine ECM.
>
> The default setting for the start switch is OFF. If the start switch is enabled to INSITE™ electronic service tool, but no switch is installed (either hardwired of J1939-multiplexed), the switch status will remain OFF.
>
> The position of the start switch can be monitored with INSITE™ electronic service tool in the data monitor/logger screen.
>
> The default setting for the permit switch is ENABLED.
>
> If the permit switch is enabled with INSITE™ electronic service tool, but no switch is installed (either hardwired or J1939 multiplexed), the switch status will remain OFF.
>
> If the vehicle is operated for an extended period of time with the permit switch OFF, fault codes for the above normal levels of aftertreatment diesel particulate filter soot load may result (Fault Codes 1921, 1922, and 2639).
>
> If the aftertreatment diesel particulate filter soot load reaches the moderately severe level (Fault Code 2639), and the permit switch is OFF, the ECM will also log a Fault Code 2777.
>
> If the permit switch is multiplexed, and therefore ENABLED, in the J1939 section of Features and Parameters in INSITE™ electronic service tool, it **must** also be enabled in the aftertreatment section of Features and Parameters in INSITE™ electronic service tool. If is is **not**, regeneration will be inhibited.
>
> The permit switch can be hardwired to the ECM **only** in emergency vehicle calibrations. For all other non-emergency calibrations, the permit switch can **only** be J1939-multiplexed over the J1939 data link.
>
> In emergency vehicle calibrations where the permit switch is hardwired, the permit switch replaces the governor type switch.
>
> A J1939-multiplexed permit switch signal has priority over a hardwired start switch signal, so if the permit switch is enabled over J1939, the hardwired signal is ignored by the engine ECM.
>
> The position of the permit switch can be monitored with INSITE™ electronic service tool in the data monitor/logger screen:
>
> - When the permit switch is ON, active regeneration is allowed.
> - When the permit switch is OFF, active regeneration is **not** allowed.
>
> If the aftertreatment exhaust gas temperature sensors are **not** connected properly, or if the wiring in the harness between the engine and aftertreatment is **not** correct, the engine may experience frequent DPF lamp illuminations, or stationary (parked) regenerations that do **not** complete.
>
> Inspect the exhaust aftertreatment temperature sensor connectors to verify they are connected to the correct connector on the aftertreatment system wiring harness. Two of the temperature sensors have identical wiring harness connectors. Because the sensors are the same part number, it is possible to install the wiring harness connectors to the wrong sensor.
>
> To verify the correct sensor locations, use INSITE™ electronic service tool to monitor the following parameters with the ignition key ON, but with the engine **not** running.
>
> - Aftertreatment Diesel Oxidation Catalyst Inlet Temperature Sensor Signal Voltage (V)
> - Aftertreatment Diesel Particulate Filter Inlet Temperature Sensor Signal Voltage (V)
> - Aftertreatment Diesel Particulate Filter Outlet Temperature Sensor Signal Voltage (V).
>
> Unplug each of the aftertreatment exhaust gas temperature sensors, one at a time.
>
> If the voltage changes when the sensor is unplugged, the wiring harness connector is connected to the correct sensor.
>
> If the voltage does **not** change when the sensor is unplugged, switch the connector location to the other temperature sensor, unplug it, and check for a voltage change.
>
> An incorrectly assembled aftertreatment wiring harness can **not** be checked by unplugging each of the aftertreatment exhaust gas temperature sensors.
>
> The **only** method to check for a misassembled aftertreatment wiring harness is to check the wiring harness connectors for correct pin installation. Refer to the engine wiring diagram for connector pin identification and location.
>
> When performing a stationary (parked) regeneration, monitor the exhaust temperatures in the aftertreatment to determine why a stationary (parked) regeneration will **not** complete.
>
> Possible causes for stationary (parked) regenerations that will **not** complete include:
>
> - Misassembled aftertreatment wiring harness
> - High resistance in exhaust gas temperature sensor return circuit
> - Aftertreatment exhaust gas temperature sensors installed in the wrong location
> - A plugged aftertreatment diesel oxidation catalyst
> - A malfunctioning turbocharger.
>
> A normal stationary (parked) regeneration will follow the pattern shown.
>
> - The dashed line is for the aftertreatment diesel oxidation catalyst inlet temperature sensor.
> - The dotted line is for the aftertreatment diesel particulate filter inlet temperature sensor.
> - The solid line is for the aftertreatment diesel particulate filter outlet temperature sensor.
>
> When the stationary (parked) regeneration begins (1), all three temperatures should be approximately the same, and should increase at the same rate.
>
> The wiring to the aftertreatment temperature sensors appears to be correct in this example because they all read approximately the same temperature at the beginning of the stationary (parked) regeneration and increase at the same rate.
>
> Aftertreatment injection begins when all three temperatures reach approximately 288°C \[ 550°F \] (2).
>
> Once aftertreatment injection begins, the aftertreatment diesel oxidation catalyst inlet temperature may vary slightly, but will typically remain between 260 and 399°C \[ 500 and 750°F \].
>
> The aftertreatment diesel particulate filter inlet and outlet temperatures will increase to approximately 482 to 649°C \[ 900 to 1200°F \]. The temperatures may vary during the stationary (parked) regeneration as the amount of fuel injected during aftertreatment injection is changed to maintain a constant temperature.
>
> The aftertreatment diesel particulate filter inlet and outlet temperatures will remain at this temperature for the duration of the stationary (parked) regeneration.
>
> This graph illustrates a stationary (parked) regeneration where the inlet of the aftertreatment diesel oxidation catalyst is blocked.
>
> - The dashed line is for the aftertreatment diesel oxidation catalyst inlet temperature sensor.
> - The dotted line is for the aftertreatment diesel particulate filter inlet temperature sensor.
> - The solid line is for the aftertreatment diesel particulate filter outlet temperature sensor.
>
> In this condition, the engine speed will increase to the stationary (parked) regeneration speed of 1000 to 1400 rpm.
>
> Raising the aftertreatment temperature to the aftertreatment injection temperature may take longer to complete than normal if the inlet to the aftertreatment diesel oxidation catalyst is plugged, restricting some of the exhaust flow.
>
> Once aftertreatment injection begins (2), the aftertreatment diesel particulate filter inlet and outlet temperatures will differ greatly due to the plugged aftertreatment diesel oxidation catalyst being unable to oxidize the injected fuel. The aftertreatment diesel particulate filter has some capability to oxidize the injected fuel, but can **not** maintain this condition without damaging the filter material over time. It is possible that white smoke would be present from the vehicle tailpipe during this condition.
>
> The wiring to the aftertreatment temperature sensors appears to be correct in this example because they all read approximately the same temperature at the beginning of the stationary (parked) regeneration and they increase at the same rate.
>
> The possible cause of this condition is a plugged aftertreatment diesel oxidation catalyst. [[101-011-049-tr — Aftertreatment Diesel Oxidation Catalyst|Refer to Procedure 011-049 (Aftertreatment Diesel Oxidation Catalyst) in Section 11 to inspect the aftertreatment diesel oxidation catalyst.]]
>
> This graph illustrates a stationary (parked) regeneration where the engine can **not** build enough heat to start aftertreatment injection.
>
> - The dashed line is for the aftertreatment diesel oxidation catalyst inlet temperature sensor.
> - The dotted line is for the aftertreatment diesel particulate filter inlet temperature sensor.
> - The solid line is for the aftertreatment diesel particulate filter outlet temperature sensor.
>
> The engine speed will likely increase to the stationary (parked) regeneration speed of 1000 to 1400 rpm, but because the aftertreatment temperatures do **not** increase enough to start aftertreatment injection, the stationary (parked) regeneration will **not** complete.
>
> Possible causes of this issue include:
>
> - High resistance in the exhaust gas temperature sensor return circuit. Use the following procedure in the ISX CM871 and ISM CM876 Electronic Control System Troubleshooting and Repair Manual, Bulletin 4021560. [[99-019-360 — Resistance Measurement Using a Multimeter|Refer to Procedure 019-360 in Section 19.]]
> - A malfunctioning turbocharger. Use the following procedure to verify the turbocharger sector gear has full travel. [[10-010-134 — Variable Geometry Turbocharger Actuator, Electric|Refer to Procedure 010-134 in Section 10.]]
> - Low ambient temperatures. Move the vehicle to a location with higher ambient temperatures.
>
> This graph illustrates a stationary (parked) regeneration where the wiring to the aftertreatment temperature sensors is incorrect.
>
> - The dashed line is for the aftertreatment diesel oxidation catalyst inlet temperature sensor.
> - The dotted line is for the aftertreatment diesel particulate filter inlet temperature sensor.
> - The solid line is for the aftertreatment diesel particulate filter outlet temperature sensor.
>
> In this condition, the engine speed will increase to the stationary (parked) regeneration speed of 1000 to 1400 rpm.
>
> Aftertreatment injection will **not** occur in this condition because the aftertreatment diesel oxidation catalyst inlet temperature does **not** reach the required temperature. Because aftertreatment injection is **not** occurring, the aftertreatment temperatures should **not** read differently.
>
> The possible cause of this condition is an incorrectly assembled aftertreatment wiring harness. See the aftertreatment exhaust gas temperature sensor wiring section of this procedure.
>
> This graph illustrates a stationary (parked) regeneration where the connectors to the aftertreatment diesel oxidation catalyst inlet temperature sensor and the aftertreatment diesel particulate filter outlet temperature sensor are reversed.
>
> - The dashed line is for the aftertreatment diesel oxidation catalyst inlet temperature sensor.
> - The dotted line is for the aftertreatment diesel particulate filter inlet temperature sensor.
> - The solid line is for the aftertreatment diesel particulate filter outlet temperature sensor.
>
> In this condition, the engine speed will increase to the stationary regeneration speed of 1000 to 1400 rpm.
>
> Aftertreatment injection may occur in this condition (2). However, the aftertreatment diesel oxidation catalyst inlet temperature increases after aftertreatment injection begins, while the aftertreatment diesel particulate filter outlet temperature remains constant.
>
> The possible cause of this condition is that the connectors to the aftertreatment diesel oxidation catalyst inlet temperature sensor and the aftertreatment diesel particulate filter outlet temperature sensor are reversed. See the aftertreatment exhaust gas temperature sensor wiring section of this procedure.
>
> A regeneration that will **not** complete can be caused by malfunctions in the EGR, variable geometry turbocharger systems, or fueling. These malfunctions do **not** allow the aftertreatment to reach the necessary temperatures for aftertreatment fuel injection.
>
> When performing a stationary (parked) regeneration, monitor the following parameters to determine why a stationary (parked) regeneration will **not** complete:
>
> - EGR Differential Pressure
> - EGR Valve Position Measured (Percent Open)
> - Exhaust Gas Pressure
> - Intake Manifold Pressure
> - Percent Load
> - Turbocharger Actuator Position Measured (Percent Closed)
> - Turbocharger Speed
>
> During a stationary (parked) regeneration, these are the typical values for a healthy system.
>
> | Parameter | Measurement |
> |---|---|
> | EGR Differential Pressure | Less than 2 kPa \[ 0.6 in-Hg \] |
> | EGR Valve Position Measured (Percent Open) | Less than two percent |
> | Exhaust Gas Pressure | 350 to 520 kPa \[ 103 to 154 in-Hg \] |
> | Intake Manifold Pressure | 18 to 122 kPa \[ 5 to 36 in-Hg \] |
> | Percent Load | Less than 12 percent |
> | Turbocharger Actuator Position Measured (Percent Closed) | 87 to 96 percent |
> | Turbocharger Speed | 30,000 to 52,000 rpm |
>
> **Note · Примечание**
> The percent load can fluctuate when the engine fan cycles ON and OFF.
