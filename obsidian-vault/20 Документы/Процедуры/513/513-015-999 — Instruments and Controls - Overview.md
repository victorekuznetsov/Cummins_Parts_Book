---
type: "Процедура"
doc: "513-015-999"
title_en: "Instruments and Controls - Overview"
modified: "2025-06-05"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "5411480"
figures: 13
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-015-999.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-015-999.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
  - "перевод/машинный"
---

# Instruments and Controls - Overview

> [!abstract] Процедура · `513-015-999`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section 15 - Instruments and Controls - Group 15
> **Даты:** изменён 2025-06-05
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-015-999.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-015-999.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Система Marine C Command Connect и C Command Connect Premier Panel System используется для мониторинга различных датчиков судна, основных эксплуатационных характеристик двигателя, а также для управления функциями запуска и остановки двигателя. Дисплей способен принимать информацию о двигателе, генераторной установке и передаче от модуля управления двигателем (ECM) через шину данных CAN 2000 Общества автомобильных инженеров (SAE) J1939 или Национальной морской электронной ассоциации (NMEA). Штурмовой дисплей принимает информацию о датчике судна и датчике передачи NEMA 2000 от дисплея клиентского интерфейса (CIB). Панельная система C Command Connect и Connect Premier состоит из следующих компонентов, которые могут быть или не быть предоставлены Cummins Inc.:

- Интерфейс двигателя, проводка жгута (Cummins Inc.) **только**
- CIB (с дисплеем ED-4 или без него) (Cummins Inc.) **только**
- Дисплей (Cummins Inc.) Производитель оригинального оборудования (OEM)
- Усилитель привода для проводов (Cummins Inc. или OEM-поставлено
- Вода в топливном датчике удлинителя проводов жгута (Cummins Inc. или OEM-поставлено
- Основная удлинительная проводка жгута и Tee (Cummins Inc.) или OEM-поставлено
- Шлем проводов жгут (включает CAN шины разъем) (Cummins Inc.) или OEM-поставлено
- Система включает переключатель (Cummins Inc.). или OEM-поставлено
- Старт-коммутатор (Cummins Inc.) или OEM-поставлено
- Стоп-коммутатор (Cummins Inc.) или OEM-поставлено
- Start/Stop Switch, однократный быстрый нажатие (PS103) (Cummins Inc.) или OEM-поставлено
- Внешний сигнальный рог (Cummins Inc.) или OEM-поставлено
- Dimmer (OEM поставляется только)
- Узлы для электропроводки дроссельной заслонки (Cummins Inc.) или OEM-поставлено
- Трансмиссионное оборудование для датчика давления и температуры масла адаптер проводов жгута, если оно оборудовано. (Cummins Inc. или OEM-поставлено
- OEM интерфейс проводов жгут (Cummins Inc.) или OEM-поставлено
- OEM датчик проводов жгут (Cummins Inc.) или OEM-поставлено
- Дисплей адаптера проводов жгута (Cummins Inc.). или OEM-поставлено. **Примечание:** Система управления морскими средствами связи и подключением премьер-панелей требует, чтобы OEM-производители использовали Cummins Inc. Разработана CIB и интерфейсная проводка двигателя. Остальные компоненты системы (дисплеи, датчики, например) и проводные ремни могут быть спроектированы и закуплены OEM-производителем, если компоненты соответствуют техническим рекомендациям Cummins® и проходят оценку качества установки.

Ограничения проводов:

Система C Command Connect и Connect Premier использует несколько проводных ремней. Основа J1939 имеет конечные резисторы на каждом конце, обычно один за самым дальним рулевым рычагом и один на двигателе.

- Интерфейс двигателя проводка жгут: интерфейс проводов ремня для двигателя CIB, дроссельной заслонки и мощности ECM
- Привод приложения проводка жгут (PS102): проводка сетки подключения для системы включить, температура выхлопа, нейтральная безопасность, и трансмиссии передачи масла охладитель давления и температуры датчик
- Привод приложения жгут проводов (PS103): проводка жгутов проводов для подключения системы, температура выхлопа, нейтральный датчик безопасности
- Вода в топливном датчике удлинитель проводов ремня: проводка жгут соединяет OEM интерфейс проводов жгут к воде в датчике топлива
- OEM интерфейс проводов жгут: Упряжка проводов соединяется с CIB для воды в топливе, дроссельной заслонки, подавления пожара, проверки бездействия и нейтральных сигналов безопасности. Эта проводка может иметь либо стандартные разъёмы проводов, либо терминальную полосу.
- OEM датчик проводов жгут: Упряжка проводов соединяет CIB с OEM-датчиками по терминальной полосе.
- Основная удлинительная проводка: wiring harness соединяет CIB с рулевой проводкой (s)
- Основная проводка удлинителя TEE: Расширение соединения для дополнительной проводов руля.
- Шлем проводов жгут: Упряжка проводов соединяется с основным удлинителем проводов для подключения к адаптеру дисплея, упряжке проводов, переключателям (система включает, запускает и останавливает), внешнему сигнальному рогу и 3-контактному разъему J1939 с конечным резистором (если это конец шины данных CAN).
- Дисплей адаптера проводов жгута: Упряжка для проводов соединяет рулевую упряжку с дисплеем (дисплеями), затемнитель, если он оборудован, и NMEA 2000, если он оборудован. Эта проводка может быть либо стандартной, продвинутой, либо двухмоторной конструкцией.
- Адаптер для дроссельной проводов: Подключение к системе дросселя
- Трансмиссионное оборудование для датчика давления и температуры масла, адаптер проводов, если он оборудован: Адаптерная проводка жгута, подключенная к приводу приложения жгута для подключения к датчикам, обычно расположенным в морской зубчатой масляной кулере.

Коннектор шины данных:

Диагностический разъем 9 контактов расположен на двигателе рядом с ECM. Если оборудование будет установлено, то диагностический разъем 9-контактный может быть также расположен у руля судна. Cummins Inc. Сегодня производится много двигателей, которые управляются электронным способом. Эти двигатели имеют особые диагностические требования из-за ECM в системе. Для взаимодействия с этими ECM были разработаны инструменты электронного обслуживания, такие как инструмент электронного обслуживания INSITETM. INSITETM - это инструментальная система для электронных сервисов, которая взаимодействует с электронными двигателями с помощью шины данных CAN. Шина данных CAN обеспечивает физическое средство для передачи и сортировки электронных сигналов. Шина данных CAN состоит из специальной электронной схемы и электропроводки. Точки подключения для электронных сервисных инструментов также являются частью шины данных CAN. Ссылки на данные определяются стандартами, написанными SAE. Cummins Inc. Использует два таких стандарта для электронных средств обслуживания. Один из них представляет собой комбинацию SAE J1587/SAE J1708, а другой - SAE J1939. Двигатели могут поддерживать один или оба из этих стандартов шины данных CAN.

Рекомендуемый разъем шины данных CAN для двигателей Cummins® представляет собой разъем 9 pin DeutschTM. Этот разъем может обеспечивать связь SAE J1587/SAE J1708 и SAE J1939 и напряжение батареи. Ниже приведены вырезы для 9-контактного разъема:

| Пин | сигнал |
|---|---|
| А. | Напряжение батареи 1 Возвращение |
| B | Напряжение батареи 1 Поставка |
| C | SAE J1939 CAN Data Bus Поставка данных |
| D | SAE J1939 Возвращение данных |
| Е | SAE J1939 CAN шина данных Shield |
| F | Не используется* |
| GGG | Не используется* |
| Hе | Не используется* |
| Я | Не используется* |

![[19400739.png]]

CIB:

Существует две конфигурации CIB.

1. Связь команд
2. C Command Connect Premier (англ.)русск.

![[15e00014.png]]

CIB расположен в машинном отделении и получает данные о двигателе от ECM через 31-контактный разъем.

Двигатель получает команды запуска и остановки через CIB. CIB также может получать OEM-данные от различных датчиков судов.

CIB содержит следующее:

1. Включатель запуска и остановки двигателя
2. Дисплей ED-4 (Подключение Premier **только**)
3. Выключатели
4. Положительная связь с аккумулятором
5. Политетрафторэтилен (ПТФЭ) герметичный мембранный вентиляционный отверстий
6. Отрицательное соединение батареи Lug
7. J1939 3-контактное соединение
8. Основное расширение проводов жгутового соединения
9. Подключение к OEM-датчику (Connect Premier option **only**)
10. Подключение NMEA 2000 (подключение Premier **только**)
11. OEM интерфейс проводка жгут соединение
12. Интерфейс двигателя подключает жгут.

Не показано*:

- Печатная плата (PCB) (внутренний CIB)
- Реле (внутренний CIB).

![[15e00015.png]]

CIB Circuit Protection:

CIB содержит выключатели (1) для защиты системы от перенапряжения. Выключатели доступны на боковой CIB.

Печатная плата CIB (PCB) имеет автоматические предохранители для следующего. Эти предохранители **не** пригодны для использования.

- Нейтральная безопасность
- Аксессуарное реле
- Отключение
- Автоматическая/ручная схема переключения
- XDRG (сенсорная площадка).

Используйте следующее для информации о выключателе. См. процедуру 018-021 в разделе V.

![[15e00016.png]]

CIB J1939 CAN шина передачи данных

Соединение J1939 3 pin (1) на CIB обычно используется OEM для доступа к информации шины данных CAN.

![[15e00017.png]]

CIB NMEA 2000 CAN шина данных

Соединение NMEA 2000 (1) на CIB обычно используется OEM для доступа к информации шины данных CAN.

![[15e00018.png]]

CIB Engine Start/Stop Switch:

Переключатель (1) запуска/остановки двигателя позволяет непосредственно запускать и останавливать двигатель от CIB.

![[15e00019.png]]

CIB PCB и реле:

Печатная плата содержит переключатели для установки напряжения, которые должны **не **перемещаться.

Реле, подключенные к печатной плате, используются для начального локаута, отключения и вспомогательного реле.

Печатная плата и реле **не** пригодны для использования.

![[15e00020.png]]

CIB ED-4 Дисплей:

Дисплей ED-4 (1) соединен с ECM через шину данных SAE J1939 CAN. На дисплее будут указаны параметры работы двигателя и коды неисправностей. Дисплей является шлюзом для передачи информации о ECM двигателя в NMEA 2000.

При установке на CIB дисплей требует уникальной загрузки программного обеспечения для системы панели C Command Connect Premier и не является общим с другими системами управления Cummins®.

Имя и версия программного обеспечения дисплея отображаются на экране после включения переключателя системы, и его можно найти на экране меню «О нас».

Дисплей поставляется с предустановленным программным обеспечением и обновляется. Используйте следующую процедуру для получения информации о программном обеспечении.[[513-015-107 — Display Software|См. процедуру 015-107 в разделе 15.]]

При установке на CIB файл личности судна дисплея должен быть обновлен для каждой заявки на судно при первоначальной установке OEM или, если он будет заменен, во время мероприятия обслуживания.

Используйте следующую процедуру для получения информации о файлах личности судна.[[513-015-044 — Managing Vessel Personalities|См. процедуру 015-044 в разделе 15.]]

![[15e00021.png]]

Компоненты шлема:

- Системный активируем Switch
- Стартовый коммутатор (PS102)
- Stop Switch (PS102)
- Переключатель «Пуск/Стоп» (PS103)
- Диммер:
- Внешний сигнал тревоги:

Дисплей ED-4 (Helm Mounted):

Дисплей обычно подключается к ECM через шину данных SAE J1939 CAN. На дисплее будут указаны параметры работы двигателя и коды неисправностей. Дисплей является шлюзом для передачи информации о ECM двигателя в NMEA 2000. При установке у руля дисплею требуется уникальная программная нагрузка для системы C Command Connect и Connect Premier Panel System и он **не** не является общим для других систем управления Cummins®.

Имя и версия программного обеспечения дисплея отображаются на экране ED-4 после включения переключателя системы, и его можно найти на экране меню «О нас».

Дисплей поставляется с предустановленным программным обеспечением и обновляется. Используйте следующую процедуру для получения информации о программном обеспечении.[[513-015-107 — Display Software|См. процедуру 015-107 в разделе 15.]]

При установке у руля файл личности судна дисплея должен быть обновлен для каждой заявки на судно при первоначальной установке OEM или, если он будет заменен, во время мероприятия обслуживания.

Используйте следующую процедуру для получения информации о файлах личности судна.[[513-015-044 — Managing Vessel Personalities|См. процедуру 015-044 в разделе 15.]]

![[15e00022.png]]

Дисплей ED-5 или ED-7 (Helm Mounted):

Дисплей представляет собой блок сенсорного экрана и обычно подключается к ECM через шину данных SAE J1939 CAN. На дисплее будут указаны параметры работы двигателя и коды неисправностей. Дисплей является шлюзом для передачи информации о ECM двигателя в NMEA 2000.

Имя и версия программного обеспечения отображения отображаются на экране ED-5 / ED-7 после включения переключателя системы, и его можно найти на экране меню «О».

Дисплей поставляется с предустановленным программным обеспечением и файлом личности сосуда дисплея и при необходимости обновляется полем. Используйте следующую процедуру для получения информации о программном обеспечении.[[513-015-107 — Display Software|См. процедуру 015-107 в разделе 15.]]

При установке у руля файл личности судна предварительно загруженного дисплея должен быть выбран для каждой заявки судна при первоначальной установке OEM или, если он будет заменен, во время события обслуживания.

Используйте следующую процедуру для получения информации о файлах личности судна.[[513-015-044 — Managing Vessel Personalities|См. процедуру 015-044 в разделе 15.]]

![[00e00312.png]]

Удаленный клавиатура (Helm Mounted):

Опциональная удаленная клавиатура подключена к дисплею ED-5 / ED-7 через шину данных SAE J1939 CAN. Удалённая клавиатура позволяет легко управлять функцией сенсорного экрана дисплея с помощью клавиш на панели.

![[00e00313.png]]

MFD (Multifunction Display) (Многофункциональный дисплей):

MFD соединен с двигателем ECM через шину данных J1939 или NMEA 2000 CAN.

В МФД будут указаны параметры работы двигателя и информация о неисправности.

MFD обычно не поставляется Cummins Inc. См. информацию об услугах производителя оборудования для обновления услуг или программного обеспечения.

![[15d00958.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The Marine C Command Connect and C Command Connect Premier Panel System is used to monitor various vessel sensors, basic engine operating characteristics, and to control engine start and stop functions. The display is capable of receiving engine, generator set, and transmission information from the engine control module (ECM) via Society of Automotive Engineers (SAE) J1939 or National Marine Electronics Association (NMEA) 2000 data link. The helm display receives vessel and transmission sensor NEMA 2000 information from the customer interface box (CIB) display. The C Command Connect and Connect Premier panel system is comprised of the following components, which may or may **not** be supplied by Cummins Inc.:
>
> - Engine interface wiring harness (Cummins Inc. supplied **only**)
> - CIB (with or without ED-4 display) (Cummins Inc. supplied **only**)
> - Display (Cummins Inc. or original equipment manufacturer (OEM)-supplied)
> - Drive application wiring harness (Cummins Inc. or OEM-supplied)
> - Water in fuel sensor extension wiring harness (Cummins Inc. or OEM-supplied)
> - Main extension wiring harness and Tee (Cummins Inc. or OEM-supplied)
> - Helm wiring harness (includes data link connector) (Cummins Inc. or OEM-supplied)
> - System enable switch (Cummins Inc. or OEM-supplied)
> - Start switch (Cummins Inc. or OEM-supplied)
> - Stop switch (Cummins Inc. or OEM-supplied)
> - Start / Stop Switch, single quick press (PS103) (Cummins Inc. or OEM-supplied)
> - External alarm horn (Cummins Inc. or OEM-supplied)
> - Dimmer (OEM supplied **only**)
> - Throttle adapter wiring harness (Cummins Inc. or OEM-supplied)
> - Transmission gear oil pressure and temperature sensor adapter wiring harness, if equipped. (Cummins Inc. or OEM-supplied)
> - OEM interface wiring harness (Cummins Inc. or OEM-supplied)
> - OEM sensor wiring harness (Cummins Inc. or OEM-supplied)
> - Display adapter wiring harness (Cummins Inc. or OEM-supplied). **Note:** The Marine C Command Connect and Connect Premier Panel System requires the OEM to use a Cummins Inc. designed CIB and engine interface harness. The remaining system components (displays, sensors, e.g.) and wiring harnesses can be designed and procured by the OEM as long as the components meet the Cummins® application engineering guidelines and pass installation quality assessment.
>
> Wiring Harnesses:
>
> The C Command Connect and Connect Premier system uses multiple wiring harnesses. The J1939 backbone has terminating resistors on each end, typically one behind the farthest helm dash and one on the engine.
>
> - Engine interface wiring harness: Harness interface for the engine CIB, throttle, and ECM power
> - Drive application wiring harness (PS102): Harness connections for system enable, exhaust temperature, neutral safety, and transmission gear oil cooler pressure and temperature sensor
> - Drive application wiring harness (PS103): Harness connections for system enable, exhaust temperature, neutral safety sensor
> - Water in fuel sensor extension wiring harness: Harness connects the OEM interface wiring harness to the water in fuel sensor
> - OEM interface wiring harness: Harness connects to CIB for water in fuel, throttle, fire suppression, idle validation, and neutral safety signals. This harness can either have standard wiring connectors or a terminal strip.
> - OEM sensor wiring harness: Harness connects CIB to OEM sensors by terminal strip.
> - Main extension wiring harness: Harness connects CIB to the helm wiring harness(s)
> - Main extension wiring harness tee: Extension connection for additional helm wiring harness.
> - Helm wiring harness: Harness connects to main extension wiring harness for connection to the display adapter wiring harness, switches (system enable, start, and stop), external alarm horn, and J1939 3-pin connector with terminating resistor (if it is the end of the datalink).
> - Display adapter wiring harness: Harness connects the helm wiring harness to the display(s), dimmer, if equipped, and NMEA 2000, if equipped. This harness can be either a standard, advanced, or twin engine wiring harness design.
> - Throttle adapter wiring harness: Connection to the throttle system
> - Transmission gear oil pressure and temperature sensor adapter wiring harness, if equipped: Adapter harness connected to the drive application wiring harness for connection to the sensors typically located in the marine gear oil cooler.
>
> Data Link Connector:
>
> The 9 pin diagnostic connector is located on the engine near the ECM. If equipped, the 9 pin diagnostic connector could also be located at the helm of the vessel. Cummins Inc. produces many engines today that are electronically controlled. These engines have special diagnostic requirements because of the ECM in the system. To interface with these ECMs, electronic service tools have been developed, such as INSITE™ electronic service tool. INSITE™ electronic service tool interfaces with the electronic engines by means of a data link. A data link provides a physical means for transmitting and sorting electronic signals. A data link consists of special electronic circuitry and electrical harnesses. Connection points for electronic service tools are also part of the data link. Data links are defined by standards written by the SAE. Cummins Inc. uses two such standards for electronic service tools. One is a combination of SAE J1587/SAE J1708 and the other is SAE J1939. Engines can support one or both of these data link standards.
>
> The recommended data link connector for Cummins® engines is a 9 pin Deutsch™ connector. This connector can supply SAE J1587/SAE J1708 and SAE J1939 communications and battery voltage. The following are pin-outs for the 9 pin connector:
>
> | Pin | Signal |
> |---|---|
> | A | Battery Voltage 1 Return |
> | B | Battery Voltage 1 Supply |
> | C | SAE J1939 Data Link Supply |
> | D | SAE J1939 Data Link Return |
> | E | SAE J1939 Data Link Shield |
> | F | **Not** Used |
> | G | **Not** Used |
> | H | **Not** Used |
> | I | **Not** Used |
>
> CIB:
>
> There are two configurations of the CIB.
>
> 1. C Command Connect
> 2. C Command Connect Premier.
>
> The CIB is located in the engine room and receives engine data from the ECM through a 31 pin connector.
>
> The engine receives start and stop commands through the CIB. The CIB can also receive OEM data from various vessel sensors.
>
> The CIB contains the following:
>
> 1. Engine start and stop switch
> 2. ED-4 display (Connect Premier option **only**)
> 3. Circuit breakers
> 4. Battery positive connection lug
> 5. Polytetrafluoroethylene (PTFE) sealed membrane vent
> 6. Battery negative connection lug
> 7. J1939 3-pin connection
> 8. Main extension wiring harness connection
> 9. OEM sensor wiring harness connection (Connect Premier option **only**)
> 10. NMEA 2000 connection (Connect Premier option **only**)
> 11. OEM interface wiring harness connection
> 12. Engine interface wiring harness connection.
>
> **Not** shown:
>
> - Printed circuit board (PCB) (internal to CIB)
> - Relays (internal to CIB).
>
> CIB Circuit Protection:
>
> The CIB contains circuit breakers (1) to protect the system from over voltage. The circuit breakers are accessible on the side CIB.
>
> The CIB printed circuit board (PCB) has auto-resetting fuses for the following. These fuses are **not** serviceable.
>
> - Neutral safety
> - Accessory relay
> - Shutdown
> - Auto/manual switching circuit
> - XDRG (sensor ground).
>
> Use the following for circuit breaker information. Refer to Procedure 018-021 in section V.
>
> CIB J1939 Data Link Connection:
>
> The J1939 3 pin connection (1) on the CIB is typically used by the OEM to access data link information.
>
> CIB NMEA 2000 Data Link Connection:
>
> The NMEA 2000 connection (1) on the CIB is typically used by the OEM to access datalink information.
>
> CIB Engine Start/Stop Switch:
>
> The engine start/stop switch (1) allows direct engine start and stop from the CIB.
>
> CIB PCB and Relays:
>
> The printed circuit board contain switches for voltage setup that should **not** be moved.
>
> The relays connected to the printed circuit board are used for starter lockout, shutdown, and accessory relay.
>
> The printed circuit board and relays are **not** serviceable.
>
> CIB ED-4 Display:
>
> The ED-4 display (1) is connected with the ECM through a SAE J1939 data link. The display will indicate engine operating parameters and fault codes. The display is the gateway for relaying engine ECM information to NMEA 2000.
>
> When mounted at the CIB, the display requires a unique software load for the C Command Connect Premier Panel System and is **not** common with other Cummins® controls systems.
>
> The display software name and version is displayed on the screen after the system enable switch is turned ON and it can be found in the “About” menu screen.
>
> The display comes preloaded with software and is updateable. Use the following procedure for information on software. [[513-015-107 — Display Software|Refer to Procedure 015-107 in Section 15.]]
>
> When mounted at the CIB, the display's vessel personality file will need to be updated for each vessel application at initial install by the OEM or, if replaced, during a service event.
>
> Use the following procedure for information on vessel personality files. [[513-015-044 — Managing Vessel Personalities|Refer to Procedure 015-044 in Section 15.]]
>
> Helm Components:
>
> - System Enable Switch
> - Start Switch (PS102)
> - Stop Switch (PS102)
> - Start / Stop Switch (PS103)
> - Dimmer:
> - External Alarm Horn:
>
> ED-4 Display (Helm Mounted):
>
> The display is typically connected to the ECM through a SAE J1939 data link. The display will indicate engine operating parameters and fault codes. The display is the gateway for relaying engine ECM information to NMEA 2000. When mounted at the helm, the display requires a unique software load for the C Command Connect and Connect Premier Panel System and is **not** common with other Cummins® controls systems.
>
> The display software name and version is displayed on the ED-4 screen after the system enable switch is turned ON and it can be found in the “About” menu screen.
>
> The display comes preloaded with software and is updateable. Use the following procedure for information on software. [[513-015-107 — Display Software|Refer to Procedure 015-107 in Section 15.]]
>
> When mounted at the helm, the display's vessel personality file will need to be updated for each vessel application at initial install by the OEM or, if replaced, during a service event.
>
> Use the following procedure for information on vessel personality files. [[513-015-044 — Managing Vessel Personalities|Refer to Procedure 015-044 in Section 15.]]
>
> ED-5 or ED-7 Display (Helm Mounted):
>
> The display is a touch screen unit and is typically connected to the ECM through a SAE J1939 data link. The display will indicate engine operating parameters and fault codes. The display is the gateway for relaying engine ECM information to NMEA 2000.
>
> The display software name and version is displayed on the ED-5 / ED-7 screen after the system enable switch is turned ON and it can be found in the “About” menu screen.
>
> The display comes preloaded with software and display's vessel personality file and is field updateable if required. Use the following procedure for information on software. [[513-015-107 — Display Software|Refer to Procedure 015-107 in Section 15.]]
>
> When mounted at the helm, the preloaded display's vessel personality file will need to be selected for each vessel application at initial install by the OEM or, if replaced, during a service event.
>
> Use the following procedure for information on vessel personality files. [[513-015-044 — Managing Vessel Personalities|Refer to Procedure 015-044 in Section 15.]]
>
> Remote Keypad (Helm Mounted):
>
> The optional remote keypad is connected to the ED-5 / ED-7 display through a SAE J1939 data link. The remote keypad enables to easily control touchscreen function of the display using the keys on the pad.
>
> MFD (Multifunction Display) (Helm-Mounted):
>
> The MFD is connected with the engine ECM through a J1939 or NMEA 2000 data link.
>
> The MFD will indicate engine operating parameters and fault information.
>
> The MFD is typically **not** supplied by Cummins Inc. See equipment manufacturer service information for service or software updates.
