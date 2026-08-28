---
aliases:
  - "Жгут проводов двигателя"
type: "Процедура"
doc: "87-019-043"
title_en: "Engine Wiring Harness"
title_ru: "Жгут проводов двигателя"
modified: "2018-08-09"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 49
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-043.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-043.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Engine Wiring Harness
**Жгут проводов двигателя**

> [!abstract] Процедура · `87-019-043`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2018-08-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-043.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-043.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Промышленные двигатели QST30 используют три отдельных жгута для управления двигателем и некоторыми операциями транспортного средства:

1. Левобережная электропроводка (primary)
2. Правобережная проводка двигателя (вторичный)
3. SAE J1939 - магистральная проводка.

![[nobox.png]]

Замените проводную упряжку, если есть открытая цепь или короткое замыкание, обнаруженное под защитным покрытием корпуса проводной упряжки.

![[19400386.png]]

### Проверка

Запустите двигатель и бегите на низком холостом ходу. При запуске двигателя вырезать левый берег, удалив разъём проводов RP39 из левобережной проводов. Если двигатель умирает, правый берег работает неправильно, так как двигатель должен работать на одном банке при низком холостом ходу.

Повторите вышеупомянутый тест, вырезав правый берег, удалив разъём RP39 из правого берег провода. Если двигатель умирает, левый берег работает неправильно, так как двигатель должен работать на одном банке при низком холостом ходу.

Если двигатель работает на низком холостом ходу во время обоих вышеупомянутых испытаний, любые проблемы с двигателем являются уникальными для конкретных цилиндров, а не для одного полного банка.

![[19a00338.png]]

Если один банк идентифицирован как **не** функционирующий, начните с проверки того, что модуль управления двигателем (ECM) получает выключатель и замок зажигания.[[99-019-064 — Key Switch Power Supply Circuit|См. процедуру 019-064 в разделе 19.]]См. процедуру 019-087 в разделе 19.

Убедитесь, что клапан отключения топлива Bosch® EHAB работает правильно.[[87-019-050 — Fuel Shutoff Valve|См. процедуру 019-050 в разделе 19.]]. Проверьте наличие любых электронных кодов неисправностей, указывающих на закрытую или застрявшую заправочную стойку. Устранение неполадок любыми активными кодами неисправностей соответственно.

![[19a00338.png]]

### Снятие

Левый берег

> [!note] Примечание
> Левобережная проводка двигателя - это основная проводка двигателя.

Отсоедините проводку двигателя от датчика давления охлаждающей жидкости (если он присутствует).

Удалите зажимы ремней жгутов проводов.

![[19801065.png]]

Отключите датчик температуры охлаждающей жидкости и датчик уровня охлаждающей жидкости.

![[19a00334.png]]

Разрежьте галстуки на кронштейне корпуса термостата, трубке послеохладителя и топливной трубке.

![[19801067.png]]

Отключите датчик температуры впускного коллектора.

![[19a00247.png]]

Отсоедините два 6-контактных или один 9-контактный разъем (разъемы) шины данных CAN от кронштейна поддержки проводов, удалив болты.

![[19a00273.png]]

Отключите датчик давления масла.

![[19a00254.png]]

Отключите датчик давления окружающего воздуха и датчик давления впускного коллектора.

![[19a00335.png]]

Отключите разъем топливного насоса.

![[19a00274.png]]

Отключите EHAB (запорный клапан топлива).

![[19a00249.png]]

Отключите датчик скорости двигателя.

![[19a00245.png]]

Отсоедините блок двигателя от блока.

![[19400393.png]]

Отключите 21-контактные и 31-контактные разъёмы.

![[19a00258.png]]

Отсоедините 21-контактный первичный/вторичный проводной упряжь отсоедините разъем.

![[19a00276.png]]

Используйте 4-мм \[5/32-в\] шестигранный головной гаечный ключ для отключения разъема электропроводки двигателя DeutschTM от ECM.

![[19900781.png]]

Правый Банк

> [!note] Примечание
> Правобережная проводка двигателя - это вторичная проводка двигателя.

Удалите зажимы ремней жгутов проводов.

![[19801065.png]]

Отключите датчик температуры впускного коллектора.

![[19a00277.png]]

Отключите датчик положения двигателя.

![[19a00261.png]]

Отключите топливный насос.

![[19a00338.png]]

Отключите EHAB (запорный клапан топлива).

![[19a00339.png]]

Отсоедините блок двигателя от блока.

![[19400393.png]]

Используйте 4-мм \[5/32-в\] шестигранный головной гаечный ключ для отключения разъема электропроводки двигателя DeutschTM от ECM.

![[19900787.png]]

### Установка

Левый берег

> [!note] Примечание
> Левобережная проводка двигателя - это основная проводка двигателя.

Подключите датчик давления охлаждающей жидкости (если он присутствует).

Установите зажимы ремней жгутов проводов.

![[19801065.png]]

Подключите датчик температуры охлаждающей жидкости.

Подключите датчик уровня охлаждающей жидкости.

![[19a00334.png]]

Установите галстуки на кронштейн корпуса термостата, трубку послеохладителя и топливную трубку.

![[19801067.png]]

Подключите датчик температуры впускного коллектора.

![[19a00247.png]]

Подключите два 6-контактных или один 9-контактный разъем (разъемы) шины данных CAN к кронштейну поддержки проводов и установите болты.

![[19a00273.png]]

Подключите датчик давления масла.

![[19a00254.png]]

Подключите датчик давления окружающего воздуха и датчик давления впускного коллектора.

![[19a00335.png]]

Подключите топливный насос.

![[19a00274.png]]

Подключите EHAB (запорный клапан топлива).

![[19a00249.png]]

Подключите датчик скорости двигателя.

![[19a00245.png]]

Подключите блок двигателя к блоку.

![[19400393.png]]

Подключите 21-контактные и 31-контактные разъёмы.

Подключите 12-контактный разъем монитора двигателя.

![[19a00275.png]]

Используйте 4-мм \[5/32-в\] шестигранный головной гаечный ключ для подключения разъема электропроводки двигателя DeutschTM к ECM.

![[19900781.png]]

Правый Банк

> [!note] Примечание
> Правобережная проводка двигателя - это вторичная проводка двигателя.

Установите зажимы ремней жгутов проводов.

![[19801065.png]]

Подключите датчик температуры впускного коллектора.

![[19a00277.png]]

Подключите датчик положения двигателя.

![[19a00261.png]]

Подключите датчик давления впускного коллектора.

![[19a00278.png]]

Подключите топливный насос.

![[19a00338.png]]

Подключите EHAB (запорный клапан топлива).

![[19a00339.png]]

Подключите блок двигателя к блоку.

![[19400393.png]]

Подключите 21-контактный первичный/вторичный проводной упряжь отсоедините разъем.

![[19a00276.png]]

Используйте 4-мм \[5/32-в\] шестигранный головной гаечный ключ для подключения разъема электропроводки двигателя DeutschTM к ECM.

![[19900787.png]]

### Проверка сопротивления

> [!warning] ОСТОРОЖНО
> Не используйте щупы или испытательные щупы, кроме Части № 3822758. Разъём будет повреждён. Лиды должны плотно помещаться в разъеме без расширения штифтов в разъеме.

Отключите разъемы ECM правого и левого берега.

![[19900515.png]]

Измерьте сопротивление от положения стойки общего провода к наземному проводу на правом берегу провода двигателя упряжка разъема ECM. См. схему проводов для идентификации контакта с разъемом.

Измерьте сопротивление от положения стойки общего провода к наземному проводу на левобережной проводах двигателя упряжка разъема ECM. См. схему проводов для идентификации контакта с разъемом.

> [!note] Примечание
> Сопротивление левого берега не должно проверяться на жгуте проводов двигателя, номер детали 4975508.

Сопротивление должно быть между 2134 и 2266 Ом.

Если значение сопротивления проводов между контактами разъёма жгута проводов находится в пределах спецификации, обратитесь к коду неисправности или процедурам устранения неполадок на основе симптомов.

Если значение сопротивления проводов упряжке соответствует **не** спецификации, замените резистор и проверьте значение сопротивления снова.

Если сопротивление жгута проводов по-прежнему соответствует спецификации **не**, замените жгут проводов.

![[19c01215.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The QST30 Industrial engines use three separate wiring harnesses to control the engine and some of the vehicle operations:
>
> 1. Left bank engine harness (primary)
> 2. Right bank engine harness (secondary)
> 3. SAE J1939 backbone harness.
>
> Replace a harness if there is an open circuit or a short circuit found under the protective covering of the harness body.
>
> ### Test
>
> Start the engine and run at low idle. With the engine running, cut out the left bank by removing the RP39 harness connector from the left bank harness. If the engine dies, the right bank is **not** operating correctly, as the engine should run on one bank at low idle.
>
> Repeat the above test cutting out the right bank by removing the RP39 harness connector from the right bank harness. If the engine dies, the left bank is **not** operating correctly, as the engine should run on one bank at low idle.
>
> If the engine runs at low idle during both of the above tests, any engine problems are unique to specific cylinders, **not** one complete bank.
>
> If one bank is identified as **not** functioning, begin by verifying that the engine control module (ECM) is receiving unswitched and keyswitch power. [[99-019-064 — Key Switch Power Supply Circuit|Refer to Procedure 019-064 in Section 19.]] Refer to Procedure 019-087 in Section 19.
>
> Verify that the Bosch® EHAB fuel shutoff valve is functioning correctly. [[87-019-050 — Fuel Shutoff Valve|Refer to Procedure 019-050 in Section 19]]. Check for any electronic fault codes indicating a closed or stuck fueling rack. Troubleshoot any active fault codes accordingly.
>
> ### Remove
>
> Left Bank
>
> **Note · Примечание**
> The left bank engine harness is the primary engine harness.
>
> Disconnect the engine harness from the coolant pressure sensor (if present).
>
> Remove the engine harness clamps.
>
> Disconnect the coolant temperature sensor and the coolant level sensor.
>
> Cut the ties on the thermostat housing bracket, aftercooler tube, and fuel tube.
>
> Disconnect the intake manifold temperature sensor.
>
> Disconnect the two 6-pin or one 9-pin data link connector(s) from the harness support bracket by removing the capscrews.
>
> Disconnect the oil pressure sensor.
>
> Disconnect the ambient air pressure sensor and intake manifold pressure sensor.
>
> Disconnect the fuel pump connector.
>
> Disconnect the EHAB (fuel shutoff valve).
>
> Disconnect the engine speed sensor.
>
> Disconnect the engine block ground from the block.
>
> Disconnect the 21-pin and 31-pin connectors.
>
> Disconnect the 21-pin primary/secondary harness disconnect connector.
>
> Use a 4-mm \[5/32-in\] hex head wrench to disconnect the engine harness Deutsch™ connector from the ECM.
>
> Right Bank
>
> **Note · Примечание**
> The right bank engine harness is the secondary engine harness.
>
> Remove the engine harness clamps.
>
> Disconnect the intake manifold temperature sensor.
>
> Disconnect the engine position sensor.
>
> Disconnect the fuel pump.
>
> Disconnect the EHAB (fuel shutoff valve).
>
> Disconnect the engine block ground from the block.
>
> Use a 4-mm \[5/32-in\] hex head wrench to disconnect the engine harness Deutsch™ connector from the ECM.
>
> ### Install
>
> Left Bank
>
> **Note · Примечание**
> The left bank engine harness is the primary engine harness.
>
> Connect the coolant pressure sensor (if present).
>
> Install the engine harness clamps.
>
> Connect the coolant temperature sensor.
>
> Connect the coolant level sensor.
>
> Install ties on the thermostat housing bracket, aftercooler tube, and fuel tube.
>
> Connect the intake manifold temperature sensor.
>
> Connect the two 6-pin or one 9-pin data link connector(s) to the harness support bracket and install the capscrews.
>
> Connect the oil pressure sensor.
>
> Connect the ambient air pressure sensor and the intake manifold pressure sensor.
>
> Connect the fuel pump.
>
> Connect the EHAB (fuel shutoff valve).
>
> Connect the engine speed sensor.
>
> Connect the engine block ground to the block.
>
> Connect the 21-pin and 31-pin connectors.
>
> Connect the 12-pin advance engine monitor connector.
>
> Use a 4-mm \[5/32-in\] hex head wrench to connect the engine harness Deutsch™ connector to the ECM.
>
> Right Bank
>
> **Note · Примечание**
> The right bank engine harness is the secondary engine harness.
>
> Install the engine harness clamps.
>
> Connect the intake manifold temperature sensor.
>
> Connect the engine position sensor.
>
> Connect the intake manifold pressure sensor.
>
> Connect the fuel pump.
>
> Connect the EHAB (fuel shutoff valve).
>
> Connect the engine block ground to the block.
>
> Connect the 21-pin primary/secondary harness disconnect connector.
>
> Use a 4-mm \[5/32-in\] hex head wrench to connect the engine harness Deutsch™ connector to the ECM.
>
> ### Resistance Check
>
> **CAUTION · Осторожно**
> Do not use probes or test leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins in the connector.
>
> Disconnect the right bank and left bank ECM connectors.
>
> Measure the resistance from the rack position common wire to the ground wire on the right bank engine harness ECM connector. Refer to the wiring diagram for connector pin identification.
>
> Measure the resistance from the rack position common wire to the ground wire on the left bank engine harness ECM connector. Refer to the wiring diagram for connector pin identification.
>
> **Note · Примечание**
> Left bank resistance does **not** need to be checked on engine wiring harness, Part Number 4975508.
>
> The resistance **must** be between 2134 and 2266 ohms.
>
> If the harness resistance value between the harness connector pins is within the specification, consult the fault code or symptom based troubleshooting procedures.
>
> If the harness resistance value does **not** meet the specification, replace the resistor and check the resistance value again.
>
> If the harness resistance still does **not** meet specification, replace the harness.
