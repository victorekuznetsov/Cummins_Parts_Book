---
type: "Процедура"
doc: "97-fc338int"
title_en: "Idle Shutdown Vehicle Accessories Relay Driver Circuit - Voltage Above Normal or Shortedd to High Source"
modified: "2004-09-28"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
  - "80141463"
  - "80248213"
families:
  - "QSM11"
  - "QSX15"
manuals:
  - "3666415"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc338int.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc338int.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
  - "перевод/машинный"
---

# Idle Shutdown Vehicle Accessories Relay Driver Circuit - Voltage Above Normal or Shortedd to High Source

> [!abstract] Процедура · `97-fc338int`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc338int.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc338int.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 338 (интегрированный)

### Idle Shutdown Vehicle Accessories Relay Driver Circuit - напряжение выше нормального или сокращенное до высокого источника

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 338 P(P): S087, 3 SPN: 1267 FMI: 3 лампы: Желтая СТО: | Idle Shutdown Vehicle Accessories Relay Driver Circuit - напряжение выше нормального или сокращенное до высокого источника. Высокое напряжение, обнаруженное на выходной цепи шины зажигания, реле зажигания положительное (+), когда система ICONTM ожидала низкого напряжения. | Система ICONTM будет отключена. Включено только обязательное отключение. Двигатель можно запускать нормально. Нет питания в цепи зажигания переключателя зажигания. |

![[19803215.png]]

### Описание цепи

Реле зажигания управляет цепями зажигания, питающими элементы управления кондиционированием отопления / воздуха и другое оборудование, подключенное к реле (реле) шины зажигания (необязательное второе реле может быть установлено для дополнительных аксессуаров). Это реле(ы) управляется (управляются) реле зажигания положительным (+) сигналом от электронного модуля управления двигателем (ECM) OEM 50-контактного разъема 35.

### Расположение компонента

Реле шины зажигания расположено под приборной панелью внутри кабины транспортного средства.

### Практические замечания

Этот недостаток обычно указывает на короткое замыкание от положительного (+) выхода зажигания реле напряжения батареи. Реле зажигания положительный (+) выводит 12 VDC, чтобы открыть реле (реле) шины зажигания, когда система ICONTM приводит в действие транспортное средство и должна отключить питание, идущее к кабинным схемам. Реле (ретрансляторы) шины зажигания обычно закрывается, когда не применяется питание.

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
>

**Для уменьшения возможности повреждения нового двигателя ECM необходимо изучить все другие коды активных неисправностей перед заменой двигателя ECM. Чтобы не повредить контакты и жгут, при измерениях пользуйтесь следующими измерительными проводами: Номер детали 3822917 - пробный щуп типа гнезда Deutsch/AMP/Metri-Pack Номер детали 3822758 - пробный щуп типа пробки Deutsch/AMP/Metri-Pack.**

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Прочитайте все коды ошибок. |  |
|  | **ШАГ 1А.** Прочитайте коды неисправностей с помощью инструментария электронного обслуживания INSITETM или выключите светильник ICONTM. | Код 338 неактивен |
| ШАГ 2. | Выполните испытание реле зажигания шины с помощью электронного инструментария обслуживания INSITETM. |  |
|  | **STEP 2A.** Проведите испытание реле шины зажигания с помощью электронного инструментария INSITETM. | Вентиляторы приборной панели выключаются |
| ШАГ 3. | Осмотрите разъем переборки OEM-проводов, разъем ECM-проводов OEM-двигателя. |  |
|  | **STEP 3A.** Проверить контакты разъема проводов OEM-мотора. | Никаких поврежденных контактов |
|  | **ШАГ 3В.** Проверить короткое замыкание от пин-кодов до пин-кодов. | Более 100 тыс. ом |
| ШАГ 4. | Проверьте реле шины зажигания. |  |
|  | **STEP 4A.** Проверьте контакты ретранслятора шины зажигания. | Никаких поврежденных контактов |
|  | **STEP 4B.** Проверьте сопротивление релейной катушки зажигания шины. | См. руководство по устранению неполадок и ремонту OEM для спецификаций |
|  | **STEP 4C.** Проверьте короткое замыкание аккумулятора на реле шины зажигания. | Менее 1,5 VDC |
| ШАГ 5. | Очистите код ошибки. |  |
|  | **STEP 5A.** Отключить код ошибки. | Код 338 неактивен; Вентиляторы панели управления отключены |

### ШАГ 1. Прочитайте все коды ошибок.

#### ШАГ 1A. Прочитайте коды неисправностей с помощью инструментария электронного обслуживания INSITETM или выключите лампу ICONTM.

| **Условия:** Включить переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Прочитайте коды неисправностей с помощью инструментария электронного обслуживания INSITETM или выключите лампу ICONTM. | Код 338 неактивен | 2А |
| Код ошибки 338 Active | 2А |  |

### ШАГ 2. Выполните испытание реле зажигания шины с помощью электронного инструментария обслуживания INSITETM.

#### ШАГ 2A. Выполните испытание реле зажигания шины с помощью электронного инструментария обслуживания INSITETM.

| **Условия:** Включить переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| См. процедуру 019-305. | Dashboard/blowers выключается | 5а |
| Dashboard/blowers do **not** | 3А |  |

### ШАГ 3. Осмотрите разъем переборки OEM-проводов, разъем ECM-проводов OEM-двигателя.

#### ШАГ 3A. Проверьте контакты разъема OEM-моторной проводов.

| **Условия:** Выключите замок зажигания. Отсоедините проводку OEM на переборке. Отсоедините электропроводку OEM к двигателю ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Корродированные штифты Бент или сломанные штифты Отталкивание назад или расширенные штифты Проводная изоляция Повреждение Влажность в или на разъем Пропавшие или поврежденные соединительные штифты Коннекторная оболочка разбитая Грязь или мусор в или на разъемных контактах. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 4А |
| Ремонт поврежденных контактов. Промывайте грязь, мусор и влагу от контактов разъема с помощью электрического контактного очистителя, Номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт или замена OEM проводов жгута. См. сервисное руководство изготовителя машины. Заменить двигатель ECM. См. процедуру 019-031 в руководстве по устранению и устранению неполадок, CELECTTM Plus, руководство по устранению и устранению неполадок или процедуру 019-031 в руководстве по устранению и устранению неполадок, электронную систему управления, ISM, в руководстве по устранению и устранению неполадок, или процедуру 019-031 в руководстве по устранению и устранению неполадок, электронную систему управления, 019-031 в руководстве по устранению и устранению неполадок, электронную систему управления, CM870 ISM, руководство по устранению и устранению неполадок или процедуру 019-031 в руководстве по устранению и устранению неполадок, в руководстве по электронной системе управления, в руководстве по устранению и устранению неполадок, в руководстве по электронной системе управления, в руководстве по устранению и устранению неполадок, в руководстве по электронной системе управления, в руководстве по устранению и устранению непола | 5а |  |

#### ШАГ 3B. Проверьте короткое замыкание от пин-кодов до пин-кодов.

| **Условия:** Выключите замок зажигания. Отсоедините реле (ретрансляторы) шины зажигания от электропроводки OEM. Отсоедините разъем OEM-проводов от двигателя ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта 35 разъёма OEM-проводов с другими штифтами в разъеме. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 100 тыс. ом | 4А |
| Ремонт или замена OEM проводов жгута. См. сервисное руководство изготовителя машины. | 5а |  |

### ШАГ 4. Проверьте реле шины зажигания.

#### ШАГ 4A. Проверьте контакты ретранслятора зажигания шины.

| **Условия:** Выключите замок зажигания. Отсоедините проводку OEM от реле шины зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Корродированные штифты Бент или сломанные штифты Отталкивание назад или расширенные штифты Проводная изоляция Повреждение Влажность в или на разъем Пропавшие или поврежденные соединительные штифты Коннекторная оболочка разбитая Грязь или мусор в или на разъемных контактах. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 4B |
| Ремонт поврежденных контактов, замена реле зажигания шины. Промывайте грязь, мусор и влагу от контактов разъема с помощью электрического контактного очистителя, Номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт или замена OEM проводов жгута. См. сервисное руководство изготовителя машины. Заменить двигатель ECM. См. процедуру 019-031 в руководстве по устранению и устранению неполадок, CELECTTM Plus, руководство по устранению и устранению неполадок или процедуру 019-031 в руководстве по устранению и устранению неполадок, электронную систему управления, ISM, в руководстве по устранению и устранению неполадок, или процедуру 019-031 в руководстве по устранению и устранению неполадок, электронную систему управления, 019-031 в руководстве по устранению и устранению неполадок, электронную систему управления, CM870 ISM, руководство по устранению и устранению неполадок или процедуру 019-031 в руководстве по устранению и устранению неполадок, в руководстве по электронной системе управления, в руководстве по устранению и устранению неполадок, в руководстве по электронной системе управления, в руководстве по устранению и устранению неполадок, в руководстве по электронной системе управления, в руководстве по устранению и устранению непола | 5а |  |

#### ШАГ 4B. Проверьте сопротивление реле зажигания шины.

| **Условия:** Выключите замок зажигания. Отсоедините проводку OEM от реле шины зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление от контакта 85 релейной катушки зажигания до контакта 86. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | См. руководство по устранению неполадок и ремонту OEM для спецификаций | 4C |
| Заменить реле шины зажигания. См. руководство изготовителя машины по диагностике и ремонту. | 5а |  |

#### ШАГ 4C. Проверьте короткое замыкание к батарее на реле шины зажигания.

| **Условия:** Отсоединить реле (ретрансляторы) шины зажигания от электропроводки OEM. Подключите OEM-проводку к двигателю ECM. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление от контакта 85 реле (реле) шины зажигания до контактов 30, 87 и 87А реле (реле). См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 100 тыс. ом | 5а |
| См. сервисное руководство изготовителя машины. | 5а |  |

### ШАГ 5. Очистите код ошибки.

#### ШАГ 5A. Отключите код неисправности.

| **Условия: **Соединить все компоненты. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверка кода 338 неактивна с использованием инструментария электронного обслуживания INSITETM. Выполните испытание реле зажигания шины с использованием инструментария электронного обслуживания INSITETM. Стирайте неактивные коды неисправностей с помощью инструментария электронного обслуживания INSITETM. | Код 338 неактивен; Вентиляторы панели управления отключены | Ремонт завершён |
| Вернитесь к шагам устранения неполадок или свяжитесь с ближайшим авторизованным ремонтным центром Cummins, если все шаги были завершены и перепроверены. Устранение неполадок с оставшимися активными кодами неисправностей. | Соответствующие диаграммы устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 338 (Integrated)
>
> ### Idle Shutdown Vehicle Accessories Relay Driver Circuit - Voltage Above Normal or Shortedd to High Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 338 PID(P): S087, 3 SPN: 1267 FMI: 3 Lamp: Yellow SRT: | Idle Shutdown Vehicle Accessories Relay Driver Circuit - Voltage Above Normal or Shortedd to High Source. High voltage detected at the ignition bus relay output circuit, ignition relay positive (+), when low voltage was expected by the ICON™ system. | The ICON™ system will be disabled. **Only** mandatory shutdown will be enabled. Engine can be started normally. No power to the keyswitch ignition circuit. |
>
> ### Circuit Description
>
> The ignition bus relay controls ignition circuits powering the heating/air conditioning controls and other equipment connected to the ignition bus relay(s) (optional second relay can be installed for additional accessories). This relay(s) is controlled by ignition relay positive (+) signal from the engine electronic control module (ECM) OEM 50-pin connector pin 35.
>
> ### Component Location
>
> The ignition bus relay is located under the dash inside the vehicle cab.
>
> ### Shoptalk
>
> This fault typically indicates a short circuit from the ignition relay positive (+) output of battery voltage. Ignition relay positive (+) pin outputs 12 VDC to open the ignition bus relay(s) when the ICON™ system has powered the vehicle down and needs to disconnect power going to the cab circuits. The ignition bus relay(s) is normally closed when no power is applied.
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
>
> **To reduce the possibility of damaging a new engine ECM, all other active fault codes must be investigated prior to replacing the engine ECM. To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822917 - female Deutsch/AMP/Metri-Pack test lead Part Number 3822758 - male Deutsch/AMP/Metri-Pack test lead.**
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Read all fault codes. |  |
> |  | **STEP 1A.** Read fault codes with INSITE™ electronic service tool or flash out with ICON™ lamp. | Fault Code 338 inactive |
> | STEP 2. | Perform the ignition bus relay test with INSITE™ electronic service tool. |  |
> |  | **STEP 2A.** Perform the ignition bus relay test with INSITE™ electronic service tool. | Dashboard blowers turn off |
> | STEP 3. | Inspect the OEM harness bulkhead connector, OEM engine harness ECM connector. |  |
> |  | **STEP 3A.** Inspect the OEM engine harness connector pins. | No damaged pins |
> |  | **STEP 3B.** Check for a short circuit from pin to pin. | More than 100k ohms |
> | STEP 4. | Check the ignition bus relay. |  |
> |  | **STEP 4A.** Check the ignition bus relay connector pins. | No damaged pins |
> |  | **STEP 4B.** Check the ignition bus relay coil resistance. | Refer to the OEM troubleshooting and repair manual for specifications |
> |  | **STEP 4C.** Check for a short circuit to the battery at ignition bus relay. | Less than 1.5 VDC |
> | STEP 5. | Clear the fault code. |  |
> |  | **STEP 5A.** Disable the fault code. | Fault Code 338 inactive; Dashboard blowers turned off |
>
> ### STEP 1. Read all fault codes.
>
> #### STEP 1A. Read fault codes with INSITE™ electronic service tool or flash out with ICON™ lamp.
>
> | **Conditions:** Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Read the fault codes with INSITE™ electronic service tool or flash out ICON™ lamp. | Fault Code 338 inactive | 2A |
> | Fault Code 338 active | 2A |  |
>
> ### STEP 2. Perform the ignition bus relay test with INSITE™ electronic service tool.
>
> #### STEP 2A. Perform the ignition bus relay test with INSITE™ electronic service tool.
>
> | **Conditions:** Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Refer to Procedure 019-305. | Dashboard/blowers turn off | 5A |
> | Dashboard/blowers do **not** turn off | 3A |  |
>
> ### STEP 3. Inspect the OEM harness bulkhead connector, OEM engine harness ECM connector.
>
> #### STEP 3A. Inspect the OEM engine harness connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness at the bulkhead. Disconnect the OEM harness to the engine ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 4A |
> | Repair the damaged pins. Flush the dirt, debris, and moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair or replace the OEM wiring harness. Refer to the OEM service manual. Replace the engine ECM. Refer to Procedure 019-031 in Troubleshooting and Repair Manual, CELECT™ Plus, Bulletin 3666130, or Procedure 019-031 in Troubleshooting and Repair Manual, Electronic Control System, ISM, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], or Procedure 019-031 in Troubleshooting and Repair Manual, Electronic Control System, Signature and ISX, Bulletin 3666259, or Procedure 019-031 in Troubleshooting and Repair Manual, Electronic Control System, CM870 ISM, Bulletin 4021381, or Procedure 019-031 in Troubleshooting and Repair Manual, Electronic Control System, CM870 Signature and ISX, Bulletin 4021334, or Procedure 019-031 in Troubleshooting and Repair Manual, Electronic Control System, CM875 ISM, Bulletin 4021477. | 5A |  |
>
> #### STEP 3B. Check for a short circuit from pin to pin.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ignition bus relay(s) from the OEM harness. Disconnect the OEM harness connector from the engine ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 35 of the OEM harness connector to all other pins in the connector. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 4A |
> | Repair or replace the OEM wiring harness. Refer to the OEM service manual. | 5A |  |
>
> ### STEP 4. Check the ignition bus relay.
>
> #### STEP 4A. Check the ignition bus relay connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ignition bus relay. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 4B |
> | Repair the damaged pins, replace ignition bus relay. Flush the dirt, debris, and moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair or replace the OEM wiring harness. Refer to the OEM service manual. Replace the engine ECM. Refer to Procedure 019-031 in Troubleshooting and Repair Manual, CELECT™ Plus, Bulletin 3666130, or Procedure 019-031 in Troubleshooting and Repair Manual, Electronic Control System, ISM, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], or Procedure 019-031 in Troubleshooting and Repair Manual, Electronic Control System, Signature and ISX, Bulletin 3666259, or Procedure 019-031 in Troubleshooting and Repair Manual, Electronic Control System, CM870 ISM, Bulletin 4021381, or Procedure 019-031 in Troubleshooting and Repair Manual, Electronic Control System, CM870 Signature and ISX, Bulletin 4021334, or Procedure 019-031 in Troubleshooting and Repair Manual, Electronic Control System, CM875 ISM, Bulletin 4021477. | 5A |  |
>
> #### STEP 4B. Check the ignition bus relay coil resistance.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ignition bus relay. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 85 of the ignition relay coil to pin 86. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Refer to the OEM troubleshooting and repair manual for specifications | 4C |
> | Replace the ignition bus relay. Refer to the OEM troubleshooting and repair manual. | 5A |  |
>
> #### STEP 4C. Check for a short circuit to the battery at ignition bus relay.
>
> | **Conditions:** Disconnect the ignition bus relay(s) from the OEM harness. Connect the OEM harness to the engine ECM. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 85 of the ignition bus relay(s) to pins 30, 87, and 87A of the relay(s). Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 5A |
> | Refer to the OEM service manual. | 5A |  |
>
> ### STEP 5. Clear the fault code.
>
> #### STEP 5A. Disable the fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify Fault Code 338 is inactive using INSITE™ electronic service tool. Perform ignition bus relay test using INSITE™ electronic service tool. Erase the inactive fault codes using INSITE™ electronic service tool. | Fault Code 338 inactive; Dashboard blowers turned off | Repair complete |
> | Return to the troubleshooting steps, or contact the nearest Cummins Authorized Repair Location if all the steps have been completed and rechecked. Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
