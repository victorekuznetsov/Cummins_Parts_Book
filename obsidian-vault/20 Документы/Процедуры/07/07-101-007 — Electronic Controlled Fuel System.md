---
aliases:
  - "Топливная система с электронным управлением"
type: "Процедура"
doc: "07-101-007"
title_en: "Electronic Controlled Fuel System"
title_ru: "Топливная система с электронным управлением"
modified: "2003-12-01"
engines:
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "4021442"
figures: 20
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-101-007.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-101-007.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
  - "перевод/машинный"
---

# Electronic Controlled Fuel System
**Топливная система с электронным управлением**

> [!abstract] Процедура · `07-101-007`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section F - Familiarization
> **Даты:** изменён 2003-12-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-101-007.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-101-007.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Секвенирование лампы неисправности

Общие сведения

Лампы NGINE FAULT AND MAINTENANCE подсвечиваются при включении переключателя зажигания в положение ON.

Через 2 секунды красная лампа STOP ENGINE выключится. После дополнительной 1⁄2 секунды лампа янтарной CHECK ENGINE выключается. После дополнительной 1⁄2 секунды лампа Amber ENGINE MAINT выключается.

Лампы будут выключены до тех пор, пока не будет обнаружена неисправность.

> [!note] Примечание
> Это функция самотестирования лампы и лампы.

> [!note] Примечание
> Названия и цвета ламп могут варьироваться в зависимости от производителя судна, если используются панели, не относящиеся к Cummins.

![[15200041.png]]

Осведомление о неисправности и системе технического обслуживания двигателя

На следующей диаграмме представлены различные лампы и их работа.

| Особенность | Сообщение оператора | Операция с лампой |  |  |
|---|---|---|---|---|
| Проверьте двигатель | Остановите двигатель | Двигатель. |  |  |
| Дисплей лампы | Испытание лампы на включение | А потом выключайся. | А потом выключайся. | А потом выключайся. |
| диагностика | Вспышка кода ошибки | Flash Once / код | Флэш код кода |  |
| Защита двигателя | Проблема системы |  | Медленная вспышка |  |
| Монитор технического обслуживания | Интервал истек |  |  | 3x5 быстрая вспышка |
| Монитор технического обслуживания | Интервальный покой |  |  | 3x5 быстрая вспышка |
| диагностика | Нефатальная системная ошибка | На постоянной |  |  |
| диагностика | Фатальная системная ошибка |  | На постоянной |  |
| диагностика | Необходимые технические средства |  |  | На постоянной |

Если лампа STOP или CHECK ENG включается при работе двигателя, это означает, что был записан код неисправности. Лампа будет работать до тех пор, пока существует ошибка. Тяжесть неисправности определит, какая лампа подсвечивается.

### Диагностические коды ошибок

Остановить лампу двигателя

Светильник STOP ENGINE — это красный светильник. Эта лампа указывает на то, что двигатель должен быть выключен до того, как произойдет постоянное повреждение двигателя.

> [!note] Примечание
> Двигатель должен быть выключен, как только он может быть безопасно выключен. Двигатель не должен работать до тех пор, пока не будет исправлена неисправность.

Эта лампа также используется для вспышки номера кода неисправности в режиме диагностики.

![[15200042.png]]

Проверить лампу двигателя

Лампа CHECK ENGINE включается во время нефатальной системной ошибки. Двигатель все еще может работать, но ошибка должна быть исправлена как можно скорее.

> [!note] Примечание
> В режиме диагностики лампа CHECK ENGINE завершает трехзначный код неисправности.

![[15200043.png]]

Лампа технического обслуживания двигателя

Лампа ENGINE MAINT включается, когда требуется техническое обслуживание двигателя.

![[15200044.png]]

Ждать, когда зажгут лампу

Лампа WAIT TO START используется только на двигателях с системой впускного воздушного нагревателя, таких как двигатели серии C.

![[15200051.png]]

Диагностика двигателя

Когда зажигается неисправная или поддерживающая лампа, выключатель диагностики двигателя позволяет оператору просматривать коды неисправностей. Сосуд справа от переключателя предназначен для подключения компьютера техника, используя либо INSITETM, либо сервисную инструментальную поддержку EchekTM.

Активные коды неисправностей можно просматривать с помощью предупреждающей лампы стоп-двигателя, как описано ниже.

![[13200054.png]]

Чтобы просмотреть коды неисправностей:

1. Двигатель должен быть выключен (не работает).
2. Переключатель зажигания **должен** находиться в положении Включения.
3. Переключатель ENG DIAG (1) должен быть в положении ON.

![[15200045.png]]

Светильники CHECK ENGINE и STOP ENGINE мигают, если есть какие-либо коды неисправностей для отображения.

Если не будет отображаться код ошибки, лампы CHECK ENGINE и STOP ENGINE будут оставаться зажженными.

![[15200046.png]]

Если есть коды неисправностей, которые должны быть отображены, лампа проверочного двигателя мигает на мгновение. Затем стоп-сигнал двигателя мигает первой, второй и третьей цифрами кода неисправности.

Пример:

Код ошибки 432

4 вспышки, пауза

3 вспышки, пауза

2 вспышки

> [!note] Примечание
> Проверка лампы двигателя будет мигать между каждым кодом неисправности.

Рисунок повторяется до тех пор, пока не будет устранена ошибка или выключен выключатель.

![[15200047.png]]

Чтобы просмотреть следующий код неисправности, нажмите RPM ± переключатель (4) в направлении плюс (+).

Для просмотра предыдущего кода неисправности нажмите RPM ± переключатель (4) в направлении минус (-).

![[15200048.png]]

Звуковой сигнал тревоги (8) звучит в любое время, когда подсвечиваются предупреждающие или предупреждающие символы.

![[13200066.png]]

Кнопка (6) будильника временно заглушит звуковую сигнализацию.

> [!note] Примечание
> Сигнал тревоги будет заглушен на 2 минуты. Пока существует условие неисправности, сигнализация будет «обходить» каждые 2 минуты, чтобы напомнить оператору, что неисправность существует.

![[13200066.png]]

Кнопка будильника (6) также используется для проверки предупреждающих и предупреждающих знаков (1) и датчиков.

Для проверки датчиков и знаковых ламп нажмите кнопку (6) тишины сигнализации при включении выключателя зажигания. Сигнализация будет включаться в течение 5 секунд, и в течение 25 секунд все символы будут освещаться, а иглы измерительной приборной стрелки будут перемещаться из самого низкого положения в самое высокое положение и обратно в самое низкое положение.

> [!note] Примечание
> Вольтметр **не** покажет системный тест.

![[13200066.png]]

### Система мониторинга двигателя

Общие сведения

Символы индикатора (1) предоставляют дополнительную информацию о типе неисправности, обнаруженной ЭКМ. Отдельные символы будут мигать во время состояния неисправности.

> [!note] Примечание
> Нажатие кнопки (6) отмены сигнализации при включении переключателя зажигания осветит символы для самотестирования.

![[13200088.png]]

Низкое давление масла в двигателе

Лампа (7) низкого давления масла двигателя включается, когда давление масла двигателя ниже спецификации. См. раздел V руководства по эксплуатации и техническому обслуживанию для спецификаций давления масла.

![[13200079.png]]

Высокий уровень поглощения Manifold Temperature

Температурная лампа (1) с высоким впускным коллектором включается, когда температура впускного коллектора превышает спецификацию.

![[13200073.png]]

Вода в топливе

Лампа (3) для подачи воды в топливо взаимодействует с дополнительным датчиком подачи воды в топливо в первичном топливном фильтре. Он появляется, когда в топливном фильтре есть вода. Данная функция не доступна в настоящее время.

![[13200075.png]]

Высокая температура охлаждения

Температурная лампа (4) с высокой температурой охлаждающей жидкости включается, когда температура охлаждающей жидкости двигателя выше спецификации.

![[13200076.png]]

Низкое напряжение батареи

> [!note] Примечание
> Эта лампа напряжения **только **применяется для морских применений.

Лампа (6) низкого напряжения батареи включается, когда напряжение батареи ниже спецификации.

![[13200078.png]]

### Сквозные разрушители

Электронно управляемый морской двигатель оснащен двумя выключателями, расположенными на стороне ECM двигателя.

5-амперный выключатель (1) используется для питания с коммутацией клавиш на ECM, а 10-амперный выключатель (2) используется для питания с неключевым переключением на панель. Панель выключателя также содержит 40-контактный OEM-разъем (3).

![[13200057.png]]


> [!quote]- Original (English) · английский оригинал
> ### Fault Lamp Sequencing
>
> General Information
>
> The ENGINE FAULT AND MAINTENANCE lamps are illuminated when the keyswitch is turned to the ON position.
>
> After 2 seconds, the red STOP ENGINE lamp will turn off. After an additional ½ of a second, the amber CHECK ENGINE lamp will turn off. After an additional ½ of a second, the amber ENGINE MAINT lamp will turn off.
>
> The lamps will remain off until a fault is detected.
>
> **Note · Примечание**
> This is a self-test feature of the lamp wiring and lamps.
>
> **Note · Примечание**
> The names and colors of the lamps can vary with vessel manufacturer if non-Cummins panels are used.
>
> Engine Fault and Maintenance System Familiarization
>
> The following chart summarizes the different lamps and their operation.
>
> | Feature | Operator Message | Lamp Operation |  |  |
> |---|---|---|---|---|
> | Check Engine | Stop Engine | Engine Maint. |  |  |
> | Lamp Display | Power-up lamp test | On then off | On then off | On then off |
> | Diagnostics | Fault code flash-out | Flash once/code | Flash code number |  |
> | Engine Protection | System problem |  | Slow flash |  |
> | Maintenance Monitor | Interval expired |  |  | 3x5 fast flash |
> | Maintenance Monitor | Interval rest |  |  | 3x5 fast flash |
> | Diagnostics | Nonfatal system error | On steady |  |  |
> | Diagnostics | Fatal system error |  | On steady |  |
> | Diagnostics | Maintenance required |  |  | On steady |
>
> If the STOP or CHECK ENG lamp comes on when the engine is running, it means a fault code has been recorded. The lamp will remain on as long as the fault exists. The severity of the fault will determine which lamp is illuminated.
>
> ### Diagnostic Fault Codes
>
> Stop Engine Lamp
>
> The STOP ENGINE lamp is a red lamp. This lamp indicates that the engine needs to be shut down before permanent damage occurs to the engine.
>
> **Note · Примечание**
> The engine **must** be shut off as soon as it can be shut off safely. The engine **must not** be run until the fault is corrected.
>
> This lamp is also used to flash out the fault code number in the diagnostics mode.
>
> Check Engine Lamp
>
> The CHECK ENGINE lamp comes on during a nonfatal system error. The engine can still be run, but the fault **must** be corrected as soon as possible.
>
> **Note · Примечание**
> In the diagnostics mode, the CHECK ENGINE lamp completes the three-digit fault code.
>
> Engine Maintenance Lamp
>
> The ENGINE MAINT lamp comes on when engine maintenance is required.
>
> Wait to Start Lamp
>
> The WAIT TO START lamp is **only** used on engines with an intake air heater system such as C Series engines.
>
> Engine Diagnostics
>
> When a fault or maintenance lamp is lit, the engine diagnostics switch allows the operator to view the fault codes. The receptacle to the right of the switch is for the technician's computer connection, using either INSITE™ or Echek™ service tool.
>
> Active fault codes can be viewed using the stop engine warning lamp as described below.
>
> To view the fault codes:
>
> 1. The engine **must** be shut off (**not** running).
> 2. The keyswitch **must** be in the ON position.
> 3. The ENG DIAG switch (1) **must** be in the ON position.
>
> The CHECK ENGINE and STOP ENGINE lamps flash if there are any fault codes to display.
>
> If there are no fault codes to display, the CHECK ENGINE and STOP ENGINE lamps will remain lit.
>
> If there are fault codes to be displayed, the check engine lamp will flash momentarily. Then the stop engine lamp will flash the first, second, and third digits of the fault code.
>
> Example:
>
> Fault Code 432
>
> 4 flashes, pause
>
> 3 flashes, pause
>
> 2 flashes
>
> **Note · Примечание**
> The check engine lamp will flash between each fault code.
>
> The pattern repeats itself until the fault is cleared or the switch is turned off.
>
> To view the next fault code, press the RPM ± switch (4) in the plus (+) direction.
>
> To view the previous fault code, press the RPM ± switch (4) in the minus (-) direction.
>
> The audible alarm (8) sounds anytime the warning or caution symbols are illuminated.
>
> The alarm silence button (6) will temporarily silence the audible alarm.
>
> **Note · Примечание**
> The alarm will be silenced for up to 2 minutes. As long as the fault condition exists, the alarm will “chirp” every 2 minutes to remind the operator that a fault exists.
>
> The alarm silence button (6) is also used to test the warning and caution symbol lamps (1) and the gauges.
>
> To test the gauges and symbol lamps, press the alarm silence button (6) while turning on the keyswitch. The alarm will come on for 5 seconds and for 25 seconds all symbols will illuminate and the gauge needles will move from the lowest position to the highest position and back to the lowest position.
>
> **Note · Примечание**
> The voltmeter will **not** display a system test.
>
> ### Engine Monitoring System
>
> General Information
>
> The indicator symbols (1) provide additional information on the type of fault that the ECM has detected. The individual symbols will flash during a fault condition.
>
> **Note · Примечание**
> Pressing the alarm cancel button (6) when the keyswitch is turned on will illuminate the symbols for a self-test.
>
> Low Engine Oil Pressure
>
> The low engine oil pressure lamp (7) comes on when the engine oil pressure is below specification. Refer to Section V of the operation and maintenance manual for the oil pressure specifications.
>
> High Intake Manifold Temperature
>
> The high intake manifold temperature lamp (1) comes on when the intake manifold temperature is above specification.
>
> Water in Fuel
>
> The water-in-fuel lamp (3) interfaces with the optional water-in-fuel sensor in the primary fuel filter. It comes on when there is water in the fuel filter. This feature is **not** presently available.
>
> High Coolant Temperature
>
> The high coolant temperature lamp (4) comes on when the engine coolant temperature is above specification.
>
> Low Battery Voltage
>
> **Note · Примечание**
> This voltage lamp **only** applies to marine applications.
>
> The low battery voltage lamp (6) comes on when the battery voltage is below specification.
>
> ### Circuit Breakers
>
> The electronically controlled marine engine is equipped with two circuit breakers located on the ECM side of the engine.
>
> A 5-amp circuit breaker (1) is used for keyswitched power to the ECM and a 10-amp circuit breaker (2) is used for non-keyswitched power to the panel. The circuit breaker panel also houses a 40-pin OEM connector (3).
