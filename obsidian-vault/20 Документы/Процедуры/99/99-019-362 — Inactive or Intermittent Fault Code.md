---
aliases:
  - "Неактивный или перемежающийся код неисправности"
type: "Процедура"
doc: "99-019-362"
title_en: "Inactive or Intermittent Fault Code"
title_ru: "Неактивный или перемежающийся код неисправности"
modified: "2022-02-23"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "35354607"
  - "35373113"
  - "37269910"
  - "37280605"
  - "37292556"
  - "37295879"
  - "41343322"
  - "41370103"
  - "71156161"
  - "80141463"
  - "80248213"
  - "85017333"
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
  - "K19"
  - "NT/NTA855 · ISM/QSM11"
  - "QSK23"
  - "QSK60"
  - "QSM11"
  - "QST30"
  - "QSX15"
manuals:
  - "3666070"
  - "3666113"
  - "3666184"
  - "3666214"
  - "3666266"
  - "3666410"
  - "3666415"
  - "4021419"
  - "4021442"
  - "4021674"
figures: 12
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-362.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-362.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "двигатель/K19"
  - "двигатель/NT/NTA855"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "двигатель/QSM11"
  - "двигатель/QST30"
  - "двигатель/QSX15"
  - "группа/99"
  - "перевод/машинный"
---

# Inactive or Intermittent Fault Code
**Неактивный или перемежающийся код неисправности**

> [!abstract] Процедура · `99-019-362`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]], [[85017333 — QSK23 CM500 CPL 2858|85017333]], [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3, K19, NT/NTA855 · ISM/QSM11, QSK23, QSK60, QSM11, QST30, QSX15
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]], [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]], [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]], [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]], [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]], [[3666410 — QSK45 and QSK60 CENSE™ Electronic Control System Troubleshooting and Repair Manual|3666410]], [[3666415 — ICON Idle Control System Master Repair Manual|3666415]], [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]], [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]], [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section 19 - Electronic Engine Controls · Section 19 - Electronic Engine Controls - Group 19 · Section 19 — Electronic Engine Controls — Group 19
> **Даты:** изменён 2022-02-23
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-362.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-362.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Эта процедура предназначена для устранения неисправностей электрических цепей, которые являются прерывистыми и в настоящее время неактивны. Эта процедура также может быть использована для устранения неполадок с высоким количеством неактивных кодов ошибок, связанных с цепью.

Если присутствует несколько кодов неисправностей, используйте схему проводов для проверки общих поставок датчиков и наземных цепей, которые могут быть разделены между датчиками, исполнительными механизмами и переключателями. Датчики давления могут иметь общую 5-вольтовую подачу и наземную цепь. Датчики температуры и исполнительные механизмы могут иметь общую схему. Если источник питания датчика или наземная схема имеют прерывистое соединение, коды неисправностей, связанные со всеми датчиками, могут быть активными или иметь большое количество неактивных кодов неисправностей.

Если условия для запуска кода сбоя существуют, а затем условия больше не присутствуют, создается неактивный код сбоя. Когда условия являются прерывистыми, может быть несколько неактивных подсчетов для данного кода неисправности. Если количество неактивных чисел превышает 10, код неисправности должен быть расшифрован как активный код неисправности. Приоритет в устранении неполадок следует отдавать кодам неисправностей, которые связаны с производительностью двигателя.

### Первичная проверка

Опросите оператора и определите условия работы двигателя, когда происходит неисправность, и какие симптомы возникают, когда неисправность активна.

Определить, были ли какие-либо недавние ремонтные работы или техническое обслуживание, которые могут быть связаны с прерывистым состоянием.

Просмотрите раздел «практическая записка» дерева устранения неисправностей кода неисправности. Практическая записка даст дополнительную информацию по устранению неполадок и перечислит возможные причины кода неисправности.

Проверить правильность калибровки электронного модуля управления (ECM). Проверьте историю калибровочных изменений, найденную на QuickServe® Online, для применимых исправлений для калибровки ECM. При необходимости перенастройте ECM. См. процедуру 019-032 Код калибровки модуля управления двигателем.

![[19800902.png]]

Отключите датчик или привод, связанный с прерывистым состоянием.

Осмотрите электропроводку и разъём на предмет:

- Свободный разъем (мягко вытягивайте провода на задней части разъемов)
- Корродированные булавки
- Сломанные или сломанные булавки
- Отодвинутые назад или расширенные булавки
- Влажность внутри или на разъемах
- Грязь или мусор в контактах разъема или на них
- Пропавшие или поврежденные соединительные уплотнения
- Повреждение изоляции провода
- Скорлупа разбита
- Поврежденный разъем вкладки блокировки
- Пин-ношение (близкий визуальный осмотр)
- Ржавый, окрашенный, разъединенный или свободный грунт.

Тщательно проверьте проводку между предполагаемым компонентом и соединением ECM. Проверьте правильное облегчение напряжения на проводах.

Темный порошок, найденный внутри разъема, может быть признаком трения штифта. Очистите контакты штифта и переподключите разъем.

![[19400450.png]]

Отсоедините разъём жгута проводов от ECM. Проверить разъем ECM на предмет:

- Свободный разъем (мягко вытягивайте провода на задней части разъемов)
- Корродированные булавки
- Сломанные или сломанные булавки
- Отодвинутые назад или расширенные булавки
- Влажность внутри или на разъемах
- Грязь или мусор в контактах разъема или на них
- Пропавшие или поврежденные соединительные уплотнения
- Повреждение изоляции провода
- Скорлупа разбита
- Поврежденный разъем вкладки блокировки
- Пин-ношение (близкий визуальный осмотр)
- Ржавый, окрашенный, разъединенный или свободный грунт.

![[19400450.png]]

Чистый разъем (разъемы) любых компонентов, связанных с кодом неисправности. Используйте инструмент Cummins®, номер детали 3823290, контактный очиститель QD® или эквивалент.

Очистить все коды ошибок.

![[19801316.png]]

Скриншоты Shake Test

Подключите рекомендуемый инструмент или эквивалент электронного сервиса Cummins® и откройте функцию Data Monitor/Logger.

Мониторинг напряжения сигнала датчика для соответствующего датчика или компонента.

Контролировать фактическое значение датчика или компонента.

![[19800902.png]]

Начиная с рассматриваемого компонента и возвращаясь через проводную упряжку к ECM, осторожно скручивайте, изгибайте и тяните за каждое соединение и между соединениями в проводной упряжке.

При выполнении проводов жгута Shake Test, датчик сигнала напряжения, что электронные сервисные инструменты дисплеи должны оставаться устойчивыми. Типичное значение должно быть от 0,5 до 5,12 вольт.

> [!note] Примечание
> Эта процедура также может быть использована для проверки свободных или поврежденных проводов для переключателей. Статус коммутатора можно контролировать с помощью электронного инструментария обслуживания. Ищите изменения переключателей при выполнении теста на встряхивание проводов.

![[19803637.png]]

Если код неисправности активен, неактивные счета увеличиваются, напряжение сигнала датчика колеблется или изменяется состояние переключателя, в этом конкретном месте есть свободное соединение или поврежденный провод. Осмотрите штифты на соответствующих разъемах.[[99-019-361 — Component Connector and Pin Inspection|См. процедуру 019-361]].

> [!note] Примечание
> ECM** не** мгновенно изменит статус переключателей и неисправностей. Приблизительно 10-15 секунд следует использовать для мягкого скручивания электропроводки и просмотра изменений считывания с ECM. Мониторинг слишком большого количества параметров одновременно с помощью электронного инструментария замедлит скорость обновления на экране. Сохраняйте количество параметров, отслеживаемых с помощью электронного инструментария обслуживания, до минимума, чтобы увеличить скорость обновления.

![[19800902.png]]

Запускай двигатель.

Мониторинг напряжения сигнала датчика для соответствующего датчика. Также отслеживайте фактическое значение датчика или компонента.

При выполнении проводов жгута Shake Test, датчик сигнала напряжения, что электронные сервисные инструменты дисплеи должны оставаться устойчивыми. Типичное значение должно быть от 0,5 до 5,12 вольт.

Теперь осторожно изгибайте, скручивайте и тяните соединения и между соединениями в проводной упряжке при мониторинге напряжения сигнала датчика.

Если напряжение сигнала датчика колеблется во время испытания, то в этом конкретном месте имеется свободное соединение или поврежденный провод. Проверьте контакты на соответствующих разъемах. Ремонт или замена по мере необходимости.[[99-019-361 — Component Connector and Pin Inspection|См. процедуру 019-361]].

![[nobox.png]]

Проверка наземной цепи

Проверьте наличие плохой батареи и шасси. Твердо тяните наземные провода или кабели, проверяя наличие свободных соединений. Проверьте следующие основания, чтобы убедиться, что они безопасны, чисты и на неокрашенной поверхности:

- Замок блокирует двигатель.
- Основания для шасси
- Основания ECM.
- Отрицательный (-) пост.
- Стартовый негативный (-) пост.

При выполнении этого шага проверьте, активируется ли код ошибки или увеличивается количество неактивных чисел. Если это произойдет, в этом месте есть слабое соединение или поврежденный провод. Отсоедините, чистые заземляющие кабели и заземляющие поверхности, затем снова подключитесь. Ремонт или замена заземляющих кабелей или проводов при необходимости.

![[19803636.png]]

Используйте мультиметр для измерения сопротивления.[[99-019-359 — Multimeter Usage|См. процедуру 019-359]].

Измерить сопротивление от отрицательной (-) позиции батареи до:

- ECM-оболочка (чистая, неокрашенная поверхность).
- Блок двигателя (чистая, неокрашенная поверхность).
- Стартовый негативный (-) пост.
- Отрицательный (-) пост.
- Основания шасси.

Все значения сопротивления должны быть меньше 1 Ом. Если значения сопротивления превышают 1 Ом, чистые заземляющие кабели и заземляющие поверхности, то пересоединяйтесь. Ремонт или замена заземляющих кабелей или проводов при необходимости.

![[19803635.png]]

### Проверка напряжения

Этот тест **должен** выполняться с помощью датчика или привода, подключенного к проводной ремне.

С датчиком или приводом, отключенным от проводной ремни, измеряйте напряжение на разъеме ремни электропитания двигателя компонента.

Подключите датчик или привод к проводной ремне и измерьте напряжение со всеми подключенными компонентами. Используйте проводку жгута ветвяного кабеля или заднюю зондацию разъема с мультиметровыми выводами при выполнении этой проверки.

Напряжение на компонент должно быть в пределах 0,5 вольт от первоначального измеренного напряжения. Если напряжение падает более чем на 0,5 вольта, проверьте наличие прерывистых соединений, прорезных проводов или коррозионных реле между приводом и ECM.

![[19c00095.png]]

### Проверка точности сенсора

Когда цепь датчика закорочена высоко или закорочена низко, значение датчика будет заблокировано до значения по умолчанию, когда код неисправности активен. Значение по умолчанию обычно устанавливается на значение, которое находится в пределах стандартного диапазона работы датчика. При мониторинге значений датчика с помощью инструментария службы будет казаться, что датчик считывает правильное значение, даже когда код неисправности активен.

Имейте в виду, когда устранение неполадок коды неисправности прерывистой цепи, что значение, отображаемое с помощью инструмента обслуживания может быть по умолчанию считывание датчика. Всегда используйте датчик измерения напряжения сигнала при устранении неполадок прерывистых схем коды неисправности.

Если необходимо дальнейшее исследование, используйте функцию Data Monitor/Logger в инструменте электронного сервиса для мониторинга входов и выходов работающего двигателя и для захвата данных в файл журнала. Функция регистратора данных в инструменте электронного обслуживания позволит собирать информацию во время прерывистого события и может быть рассмотрена позже.

![[19800902.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> This procedure is designed to troubleshoot electrical circuit faults that are intermittent and are currently inactive. This procedure can also be used to troubleshoot high inactive counts of circuit related fault codes.
>
> If multiple fault codes are present, use a wiring diagram to check for common sensor supplies and ground circuits that may be shared between sensors, actuators, and switches. Pressure sensors may share a common 5 volt supply and ground circuit. Temperature sensors and actuators may share a common ground circuit. If either a sensor supply or a ground circuit has an intermittent connection, fault codes related to all the sensors may be active or have high counts of inactive fault codes.
>
> If the conditions for a fault code to trigger exist and then the conditions are no longer present, an inactive fault code is created. When conditions are intermittent, there may be multiple inactive counts for a given fault code. If there are more than 10 inactive counts, the fault code should be troubleshot as an active fault code. Troubleshooting priority should be given to fault codes that are associated engine performance.
>
> ### Initial Check
>
> Interview the operator and determine the engine operating conditions when the fault occurs and what symptoms occur when the fault is active.
>
> Determine if there have been any recent service repairs or maintenance performed that may be related to the intermittent condition.
>
> Review the “Shop Talk” section of the fault code troubleshooting tree. Shop Talk will give additional troubleshooting information and will list possible causes for the fault code.
>
> Verify the electronic control module (ECM) calibration is correct. Check the calibration revision history found on QuickServe® Online for applicable fixes for the ECM calibration. If necessary, recalibrate the ECM. See procedure 019-032 Engine Control Module Calibration Code.
>
> Disconnect the sensor or actuator related to the intermittent condition.
>
> Inspect the wiring harness and connector for the following:
>
> - Loose connector (gently pull the wires at the back of the connectors)
> - Corroded pins
> - Bent or broken pins
> - Pushed back or expanded pins
> - Moisture in or on the connectors
> - Dirt or debris in, or on, the connector pins
> - Missing or damaged connector seals
> - Wire insulation damage
> - Connector shell broken
> - Damaged locking tab connector
> - Pin wear (close visual inspection)
> - Rusty, painted, corroded, or loose grounds.
>
> Thoroughly inspect the wiring harness between the suspected component and ECM connection. Check for the proper strain relief on the wiring harness.
>
> A dark powder found inside the connector may be a sign of pin fretting. Clean the pin contacts and reconnect the connector.
>
> Disconnect the wiring harness connector from the ECM. Inspect the ECM connector for the following:
>
> - Loose connector (gently pull the wires at the back of the connectors)
> - Corroded pins
> - Bent or broken pins
> - Pushed back or expanded pins
> - Moisture in or on the connectors
> - Dirt or debris in, or on, the connector pins
> - Missing or damaged connector seals
> - Wire insulation damage
> - Connector shell broken
> - Damaged locking tab connector
> - Pin wear (close visual inspection)
> - Rusty, painted, corroded, or loose grounds.
>
> Clean connector(s) of any components related to the fault code. Use Cummins® service tool, Part Number 3823290, QD® contact cleaner or equivalent.
>
> Clear all fault codes.
>
> Harness Shake Test
>
> Connect a recommended Cummins® electronic service tool or equivalent and open the Data Monitor/Logger feature.
>
> Monitor the sensor signal voltage for the appropriate sensor or component.
>
> Monitor the actual value of the sensor or component.
>
> Beginning at the component in question and working back through the harness to the ECM, gently twist, bend and pull at each connection and in between connections in the harness.
>
> While performing the Harness Shake Test, the sensor signal voltage that the electronic service tool displays should remain steady. A typical reading should be between 0.5 and 5.12 volts.
>
> **Note · Примечание**
> This procedure can also be used to check for loose or damaged wires for switches. Switch status can be monitored with an electronic service tool. Look for switch changes when performing the Harness Shake Test.
>
> If the fault code goes active, inactive counts increase, the sensor signal voltage fluctuates, or the switch status changes, there is a loose connection or damaged wire at that specific location. Inspect the pins at the corresponding connectors. [[99-019-361 — Component Connector and Pin Inspection|Refer to Procedure 019-361]].
>
> **Note · Примечание**
> The ECM will **not** change the status of switches and faults instantaneously. Approximately 10 to 15 seconds should be used to gently twist the harness and see a reading change from the ECM. Monitoring too many parameters at one time with an electronic service tool will slow down the update rate on the screen. Keep the number of parameters monitored with the electronic service tool to minimum to increase the update rate.
>
> Start the engine.
>
> Monitor the sensor signal voltage for the appropriate sensor. Also monitor the actual value of the sensor or component.
>
> While performing the Harness Shake Test, the sensor signal voltage that the electronic service tool displays should remain steady. A typical reading should be between 0.5 and 5.12 volts.
>
> Now gently bend, twist, and pull the connections and in between connections in the harness while monitoring the sensor signal voltage.
>
> If the sensor signal voltage fluctuates during the test, then there is a loose connection or damaged wire at that specific location. Inspect the pins at the connectors in question. Repair or replace as necessary. [[99-019-361 — Component Connector and Pin Inspection|Refer to Procedure 019-361]].
>
> Ground Circuit Check
>
> Check for poor battery and chassis grounds. Firmly pull on ground wires or cables checking for loose connections. Check the following grounds making sure they are secure, clean, and on a non-painted surface:
>
> - Engine block grounds.
> - Chassis grounds
> - ECM grounds.
> - Alternator negative (-) post.
> - Starter negative (-) post.
>
> While performing this step, check to see if the fault code goes active, or if inactive counts increase. If this happens, there is a loose connection or damaged wire at that location. Disconnect, clean grounding cables and grounding surfaces, then reconnect. Repair or replace grounding cables or wires if necessary.
>
> Use a multimeter to measure resistance. [[99-019-359 — Multimeter Usage|Refer to Procedure 019-359]].
>
> Measure resistance from the battery negative (-) post to:
>
> - ECM casing (clean, non-painted surface).
> - Engine block (clean, non-painted surface).
> - Starter negative (-) post.
> - Alternator negative (-) post.
> - Chassis grounds.
>
> All resistance values should measure less than 1 ohm. If resistance values exceed 1 ohm, clean grounding cables and grounding surfaces, then reconnect. Repair or replace grounding cables or wires if necessary.
>
> ### Voltage Check
>
> This test **must** be performed with the sensor or actuator connected to the wiring harness.
>
> With the sensor or actuator disconnected from the wiring harness, measure the voltage at the engine harness connector of the component.
>
> Connect the sensor or actuator to the wiring harness and measure the voltage with all the components connected. Use a breakout cable or back-probe the connector with the multimeter leads when performing this check.
>
> The voltage to the component should be within 0.5 volts of the original voltage measured. If the voltage drops more than 0.5 volts, check for intermittent connections, cut wires, or corroded relay connections between the actuator and the ECM.
>
> ### Sensor Accuracy Check
>
> When a sensor circuit is shorted high or shorted low, the sensor value will be locked to a default value when the fault code is active. The default value will usually be set to a value that is within the standard operating range of the sensor. When monitoring the sensor values with a service tool it will appear as if the sensor is reading a correct value even when the fault code is active.
>
> Be aware when troubleshooting intermittent circuit fault codes that the value displayed with a service tool could be a default sensor reading. Always use the sensor signal voltage measurement when troubleshooting intermittent circuit fault codes.
>
> If further investigation is necessary, use the Data Monitor/Logger feature in an electronic service tool to monitor the inputs and outputs of a running engine and to capture data to a log file. The data logger feature in an electronic service tool will allow for information to be captured during the intermittent event and can reviewed at a later time.
