---
aliases:
  - "Блок останова интерфейсной коробки заказчика"
type: "Процедура"
doc: "116-015-122"
title_en: "Customer Interface Box Shutdown Unit"
title_ru: "Блок останова интерфейсной коробки заказчика"
modified: "2026-04-14"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021617"
figures: 12
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-015-122.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-015-122.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# Customer Interface Box Shutdown Unit
**Блок останова интерфейсной коробки заказчика**

> [!abstract] Процедура · `116-015-122`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section 15 - Instruments and Controls - Group 15
> **Даты:** изменён 2026-04-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-015-122.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-015-122.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Диаграмма компонентов

![[15c01538.png]]

Схема компонентов компонента блоков отключения клиентского интерфейса Box Shutdown Unit

1. SDU 410 (контроль безопасности)
2. Огни с индикаторами состояния
3. 5.2.3 Индикатор выключения
4. 5.2.1 Неисправные индикаторные лампы
5. **Кнопка «Признание**»
6. **Кнопка «Более скоростной тест**»

### Выбор сервисного инструмента

#### Рекомендованный сервисный инструмент Cummins®

- Контактный очиститель, номер детали 3824510 или эквивалент

#### Дополнительные сервисные позиции

- Никаких дополнительных предметов обслуживания не требуется.

### Общие сведения

SDU 410 расположен в окне клиентского интерфейса (CIB) и обеспечивает защиту двигателя, выключая двигатель, если превышены критические пороговые значения параметров.

**Индикатор лампы**

Огни с индикаторами состояния описываются в следующей таблице.

| 410 Статусные индикаторы лампы |  |  |
|---|---|---|
| Имя лампы | Штат лампы | Описание статуса |
| Власть | Над | Напряжение питания SDU 410 выше 23 VDC. |
|  | мигающий | Напряжение питания SDU 410 ниже 23 VDC. |
| Крэнк Катофф | Над | Скорость двигателя выше установленного порога, чтобы указать на завершение проворачивания. |
| бегать | Над | Скорость двигателя выше установленного порога, чтобы указать, что двигатель работает. |
| Тачо 1 | Над | Скорость двигателя выше 5 оборотов в минуту измеряется датчиком скорости двигателя, подключенным к каналу. |
|  | мигающий | Неисправность схемы обнаружена на канале. |
| Тату 2 | Над | Скорость двигателя выше 5 оборотов в минуту измеряется датчиком скорости двигателя, подключенным к каналу. |
|  | мигающий | Неисправность схемы обнаружена на канале. |
| Отключение Override | Над | Отключение преобладает над активным. |
| жужжание | Над | SDU 410 активирует звуковой сигнал тревоги. |
| КОМ 1 | мигающий | Активная связь между SDU 410 и DCU 410E. |
| COM 2 | мигающий | Активная связь между SDU 410 и другим устройством по каналу RS-485 Modbus. |
| COM 3 | мигающий | Активная связь между SDU 410 и другим устройством по каналу Ethernet. |

Красные индикаторные лампы выключения описаны в следующей таблице. Мгновенная лампа указывает, что состояние не было признано оператором.

| SDU 410 индикатор выключения ламп (красный) |  |
|---|---|
| Имя лампы | Описание Shutdown |
| Коммутатор 1 - 8 | Выключение двигателя, вызванное цепью с подсветкой лампы. |
| Отключение | Отключение двигателя под управлением SDU 410. Освещение в дополнение к лампе переключения или лампе переключения скоростей, указывающей причину отключения. |
| сверхскоростной | Отключение двигателя из-за превышения скорости. Если быстро мигает, то тест на скорость активен. См. раздел Тест в этой процедуре. |

Огни с индикатором неисправности янтаря описаны в следующей таблице. Мгновенная лампа указывает, что состояние не было признано оператором.

| SDU 410 Fault Indicator Lamps (Янтарные лампы) |  |
|---|---|
| Имя лампы | Описание ошибки |
| Коммутатор 1 - 8 | Неисправность коммутатора. |
| Отключаемая катушка | Неисправность цепи катушки отключения. |
| Отключение Override | Отключение перекрывает сбой в цепи. |

Если выключение двигателя вызвано SDU 410, кнопка **Признание** на SDU 410 * должна быть нажата до запуска двигателя.

Звуковой сигнал тревоги будет звучать при выключении или неисправности ламп. Сигнал тревоги может быть настроен на автоматическое выключение через 5 секунд или на включение до нажатия кнопки **Признание** на SDU 410.

**Заткнись, переопределись**

Переопределение отключения может быть включено с помощью DCU 410E или дополнительного коммутатора, предоставляемого клиентом, подключенного к CIB. При включении переопределения отключения некоторые выключения защиты двигателя SDU 410 отключаются в зависимости от конфигурации. Защита от превышения скорости двигателя может быть отключена **не**.

**Тест на скорость**

Тест на сверхскоростную скорость используется во время устранения неполадок или сертификационных испытаний оборудования. Порог скорости двигателя будет временно снижен до нормального диапазона работы двигателя, чтобы вызвать отключение двигателя. Красная лампа быстро мигает, когда активен тест на скорость. См. раздел Тестирование этой процедуры.

**SDU 410 Switch Channels**

SDU 410 принимает входные данные от восьми обычно открытых коммутаторов. Когда выключатель закроется, канал SDU 410 будет активирован, и произойдет отключение двигателя. Шесть каналов определены Cummins Inc. Остальные каналы доступны для дополнительных переключателей оборудования, если они оборудованы. См. сервисную документацию изготовителя оборудования. Для каждого канала могут быть настроены следующие настройки:

- **On Run Only** - Канал контролируется только при работе двигателя.
- **Shutdown Override Disabled** - Канал вызовет остановку двигателя независимо от статуса перекрытия остановки.
- **Включить Зависимость от скорости** - Канал контролируется только*, когда скорость двигателя выше установленного порога.
- **Задержка** - время до отключения после обнаружения состояния.

В следующей таблице описан каждый канал SDU 410.

| SDU 410 - каналы коммутации входных сигналов |  |
|---|---|
| переключатель | Каналы по описанию |
| 1 | Высокотемпературная система охлаждения охлаждающая температура |
| 2 | Высокотемпературная система охлаждения охлаждающего давления |
| 3 | Низкое давление моторного масла |
| 4 | Высокое давление моторного масла |
| 5 | Дистанционный аварийный выключатель |
| 6 | Факультативный переключатель оборудования |
| 7 | Аварийный выключатель остановки CIB |
| 8 | Факультативный переключатель оборудования |

Все компоненты, обработанные в этой процедуре, весят менее 23 кг [50 фунтов].

### Проверка

> [!note] Примечание
> Порог превышения скорости двигателя будет временно снижен до нормального диапазона работы двигателя, чтобы вызвать отключение двигателя с сообщениями о неисправности скорости двигателя.

Откройте дверь CIB.[[116-015-023 — Customer Interface Box|См. процедуру 015-023 в разделе 15.]]

Пройдите тест на скорость.

- Подтвердите, что на DCU 410E нет активных сообщений об ошибках.
- Работа двигателя при следующих условиях:
- Нажмите кнопку «» на SDU 410 в течение 2 секунд.
- Красная лампа SDU 410 будет быстро мигать при активном тестировании скорости.

Тест на скорость автоматически прекращается после:

- Отключение двигателя из-за превышения скорости
- Пять минут без остановки двигателя.

Если тест не увенчался успехом, см. соответствующие деревья устранения неполадок в разделе ТТ.

![[15200528.png]]

Ручно остановить тест на скорость.

- Нажмите кнопку «Испытание на скорости» на SDU 410 в течение 2 секунд.
- Красная лампа SDU 410 перестанет мигать, чтобы указать, что испытание на сверхскоростной скорости завершено.

![[15200529.png]]

### Подготовительные операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Отключите батареи и источники питания. См. сервисную документацию изготовителя оборудования.
- Откройте дверь CIB.[[116-015-023 — Customer Interface Box|См. процедуру 015-023 в разделе 15.]]
- Удалите крышки трубопровода, если это необходимо.[[116-015-137 — Electrical Panel Conduit Box Cover(s)|См. процедуру 015-137 в разделе 15.]]

### Снятие

> [!warning] ОСТОРОЖНО
> Тег проводов и установить в исходном месте. Электрические повреждения могут возникнуть, если провода установлены в неправильном месте.

Тег электрических разъемов с местоположением на SDU 410.

Удалите электрические разъемы.

![[15200530.png]]

Удалить SDU 410.

- Нажмите SDU 410.
- Поверните дно SDU 410 с монтажного рельса.

![[15200531.png]]

### Разборка

> [!warning] ОСТОРОЖНО
> Тег проводов и установить в исходном месте. Электрические повреждения могут возникнуть, если провода установлены в неправильном месте.

Удалите провода из электрических разъемов.

- Отметьте каждый провод с местоположением терминала.
- Терминал Лоосена. Используйте отвертку.
- Удалите провод из терминала.

![[15200551.png]]

### Очистка и проверка при повторном использовании

> [!danger] ОПАСНО
> При очистке растворителями, кислотами и щелочными составами соблюдайте указания их изготовителя. Работайте в защитных очках и защитной одежде, чтобы снизить риск травмы.

Чистый SDU 410. Используйте чистую, без винта ткань.

Чистые электрические разъемы. Используйте контактный очиститель, Номер детали 3824510 или эквивалент.

![[15200533.png]]

Проверить SDU 410.

Заменить, если:

- Разбитый
- Повреждены терминалы
- В противном случае поврежден.

![[15200534.png]]

Проверяйте каждый электрический разъем.

Заменить, если:

- Разбитый
- Повреждены терминалы
- В противном случае поврежден.

Проверьте провода.[[116-015-138 — Customer Interface Box Electrical Wires|См. процедуру 015-138 в разделе 15.]]

![[15200554.png]]

### Сборка

> [!warning] ОСТОРОЖНО
> Установите провода в исходном месте. Электрические повреждения могут возникнуть, если провода установлены в неправильном месте.

Установите провода в электрические разъемы.

- Вставьте провода в правильное место.
- Уплотнить терминалы.
- Легко нажмите на каждый провод, чтобы убедиться, что он правильно подключен.

![[15200551.png]]

### Установка

Установите SDU 410.

- Поместите верхнюю часть SDU 410 на монтажной рельсовой магистрали.
- Нажмите SDU 410. Поверните дно SDU 410 на крепежный рельс, как показано.

![[15200536.png]]

> [!warning] ОСТОРОЖНО
> Установите провода в исходном месте. Электрические повреждения могут возникнуть, если провода установлены в неправильном месте.

Установите электрические разъемы на SDU 410.

![[15200530.png]]

### Завершающие операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Установите крышки коробки.[[116-015-137 — Electrical Panel Conduit Box Cover(s)|См. процедуру 015-137 в разделе 15.]]
- Закрой дверь.[[116-015-023 — Customer Interface Box|См. процедуру 015-023 в разделе 15.]]
- Подключите батареи и источники питания. См. сервисную документацию изготовителя оборудования.


> [!quote]- Original (English) · английский оригинал
> ### Component Diagram
>
> Customer Interface Box Shutdown Unit Component Diagram
>
> 1. SDU 410 (safety control)
> 2. Status indicator lamps
> 3. Shutdown indicator lamps
> 4. Fault indicator lamps
> 5. **Acknowledge** button
> 6. **Overspeed Test** button
>
> ### Select Service Tools
>
> #### Recommended Cummins® Service Tools
>
> - Contact cleaner, Part Number 3824510, or equivalent
>
> #### Additional Service Items
>
> - No additional service items required.
>
> ### General Information
>
> The SDU 410 is located within the customer interface box (CIB) and provides engine protection by shutting down engine if critical parameter thresholds are exceeded.
>
> **Indicator Lamps**
>
> Status indicator lamps are described in the following table.
>
> | SDU 410 Status Indicator Lamps |  |  |
> |---|---|---|
> | Lamp Name | Lamp State | Status Description |
> | Power | On | Power supply voltage to SDU 410 above 23 VDC. |
> |  | Flashing | Power supply voltage to SDU 410 below 23 VDC. |
> | Crank Cutoff | On | Engine speed above set threshold to indicate cranking complete. |
> | Running | On | Engine speed above set threshold to indicate engine is running. |
> | Tacho 1 | On | Engine speed above 5 rpm measured by engine speed sensor connected to channel. |
> |  | Flashing | Circuit fault detected on channel. |
> | Tacho 2 | On | Engine speed above 5 rpm measured by engine speed sensor connected to channel. |
> |  | Flashing | Circuit fault detected on channel. |
> | Shutdown Override | On | Shutdown override active. |
> | Buzzer | On | SDU 410 audible alarm active. |
> | COM 1 | Flashing | Active communication between SDU 410 and DCU 410E. |
> | COM 2 | Flashing | Active communication between SDU 410 and another device on RS-485 Modbus channel. |
> | COM 3 | Flashing | Active communication between SDU 410 and another device on Ethernet channel. |
>
> Red shutdown indicator lamps are described in the following table. A flashing lamp indicates the condition has **not** been acknowledged by the operator.
>
> | SDU 410 Shutdown Indicator Lamps (Red) |  |
> |---|---|
> | Lamp Name | Shutdown Description |
> | Switch 1 - 8 | Engine shutdown caused by circuit with lamp illuminated. |
> | Shutdown | Engine shutdown commanded by SDU 410. Illuminates in addition to switch lamp or overspeed lamp indicating cause of shutdown. |
> | Overspeed | Engine shutdown due to overspeed. If rapidly flashing, Overspeed Test is active. See Test section in this procedure. |
>
> Amber fault indicator lamps are described in the following table. A flashing lamp indicates the condition has **not** been acknowledged by the operator.
>
> | SDU 410 Fault Indicator Lamps (Amber) |  |
> |---|---|
> | Lamp Name | Fault Description |
> | Switch 1 - 8 | Switch circuit fault. |
> | Shutdown Coil | Shutdown coil circuit fault. |
> | Shutdown Override | Shutdown override circuit fault. |
>
> If engine shutdown is caused by the SDU 410, the **Acknowledge** button on the SDU 410 **must** be pressed before the engine can be started.
>
> An audible alarm will sound when shutdown or fault lamps are illuminated. The alarm can be configured to turn off automatically after 5 seconds or remain on until the **Acknowledge** button is pressed on the SDU 410.
>
> **Shutdown Override**
>
> Shutdown override can be enabled using the DCU 410E or an optional customer-provided switch connected to the CIB. When shutdown override is enabled, some SDU 410 engine protection shutdowns are disabled depending on configuration. Engine overspeed protection can **not** be disabled.
>
> **Overspeed Test**
>
> Overspeed Test is used during troubleshooting or equipment certification testing. The engine overspeed threshold will be temporarily lowered to within the normal engine operating range to cause engine shutdown. The red overspeed lamp will flash rapidly when Overspeed Test is active. See Test section of this procedure.
>
> **SDU 410 Switch Channels**
>
> The SDU 410 receives input from up to eight normally open switches. When a switch closes, that SDU 410 channel will be activated and engine shutdown will occur. Six of the channels are defined by Cummins Inc. The remaining channels are available for additional equipment switches, if equipped. See equipment manufacturer service information. The following settings can be configured for each channel:
>
> - **On Run Only** - Channel monitored **only** when engine is running.
> - **Shutdown Override Disabled** - Channel will cause engine shutdown regardless of shutdown override status.
> - **Enable Speed Dependency** - Channel monitored **only** when engine speed is above set threshold.
> - **Delay** - Time before shutdown is commanded after condition is detected.
>
> The following table describes each SDU 410 channel.
>
> | SDU 410 Input Switch Channels |  |
> |---|---|
> | Switch | Channel Description |
> | 1 | High temperature cooling system coolant temperature |
> | 2 | High temperature cooling system coolant pressure |
> | 3 | Low speed lubricating oil pressure |
> | 4 | High speed lubricating oil pressure |
> | 5 | Remote emergency stop switch |
> | 6 | Optional equipment switch |
> | 7 | Emergency stop switch on CIB |
> | 8 | Optional equipment switch |
>
> All components handled in this procedure weigh less than 23 kg \[ 50 lb \].
>
> ### Test
>
> **Note · Примечание**
> Engine overspeed threshold will be temporarily lowered to within normal engine operating range to cause engine shutdown with engine overspeed fault messages.
>
> Open CIB door. [[116-015-023 — Customer Interface Box|Refer to Procedure 015-023 in Section 15.]]
>
> Perform Overspeed Test.
>
> - Confirm there are no active fault messages on DCU 410E.
> - Operate engine at following conditions:
> - Hold **Overspeed Test** button on SDU 410 for 2 seconds.
> - SDU 410 overspeed red lamp will flash rapidly when Overspeed Test is active.
>
> Overspeed Test will terminate automatically after:
>
> - Engine shutdown due to overspeed
> - Five minutes without engine shutdown.
>
> If test is **not** successful, see appropriate troubleshooting trees in Section TT.
>
> Manually stop Overspeed Test.
>
> - Hold Overspeed Test button on SDU 410 for 2 seconds.
> - SDU 410 overspeed red lamp will stop flashing to indicate Overspeed Test terminated.
>
> ### Preparatory Steps
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Disconnect batteries and power supplies. See equipment manufacturer service information.
> - Open CIB door. [[116-015-023 — Customer Interface Box|Refer to Procedure 015-023 in Section 15.]]
> - Remove conduit box covers, as necessary. [[116-015-137 — Electrical Panel Conduit Box Cover(s)|Refer to Procedure 015-137 in Section 15.]]
>
> ### Remove
>
> **CAUTION · Осторожно**
> Tag wires and install in original location. Electrical damage can occur if wires are installed in incorrect location.
>
> Tag electrical connectors with location on SDU 410.
>
> Remove electrical connectors.
>
> Remove SDU 410.
>
> - Push SDU 410 down.
> - Rotate bottom of SDU 410 off of mounting rail.
>
> ### Disassemble
>
> **CAUTION · Осторожно**
> Tag wires and install in original location. Electrical damage can occur if wires are installed in incorrect location.
>
> Remove wires from electrical connectors.
>
> - Tag each wire with terminal location.
> - Loosen terminal. Use screwdriver.
> - Remove wire from terminal.
>
> ### Clean and Inspect for Reuse
>
> **WARNING · Опасно**
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.
>
> Clean SDU 410. Use clean, lint-free cloth.
>
> Clean electrical connectors. Use contact cleaner, Part Number 3824510, or equivalent.
>
> Inspect SDU 410.
>
> Replace if:
>
> - Cracked
> - Terminals damaged
> - Otherwise damaged.
>
> Inspect each electrical connector.
>
> Replace if:
>
> - Cracked
> - Terminals damaged
> - Otherwise damaged.
>
> Inspect wires. [[116-015-138 — Customer Interface Box Electrical Wires|Refer to Procedure 015-138 in Section 15.]]
>
> ### Assemble
>
> **CAUTION · Осторожно**
> Install wires in original location. Electrical damage can occur if wires are installed in incorrect location.
>
> Install wires in electrical connectors.
>
> - Insert wires in correct location.
> - Tighten terminals.
> - Lightly pull on each wire to make sure it is properly connected.
>
> ### Install
>
> Install SDU 410.
>
> - Place top of SDU 410 on mounting rail.
> - Push SDU 410 down. Rotate bottom of SDU 410 onto mounting rail, as shown.
>
> **CAUTION · Осторожно**
> Install wires in original location. Electrical damage can occur if wires are installed in incorrect location.
>
> Install electrical connectors on SDU 410.
>
> ### Finishing Steps
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Install conduit box covers. [[116-015-137 — Electrical Panel Conduit Box Cover(s)|Refer to Procedure 015-137 in Section 15.]]
> - Close CIB door. [[116-015-023 — Customer Interface Box|Refer to Procedure 015-023 in Section 15.]]
> - Connect batteries and power supplies. See equipment manufacturer service information.
