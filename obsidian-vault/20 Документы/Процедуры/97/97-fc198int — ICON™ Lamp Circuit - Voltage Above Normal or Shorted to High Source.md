---
type: "Процедура"
doc: "97-fc198int"
title_en: "ICON™ Lamp Circuit - Voltage Above Normal or Shorted to High Source"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc198int.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc198int.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
  - "перевод/машинный"
---

# ICON™ Lamp Circuit - Voltage Above Normal or Shorted to High Source

> [!abstract] Процедура · `97-fc198int`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc198int.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc198int.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 198 (интегрированный)

### ICONTM Lamp Circuit - напряжение выше нормального или короткое до высокого источника

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 198 PID(P): S122, 3 SPN: 612 FMI: 3 лампы: Желтая СТО: | ICONTM Lamp Circuit - напряжение выше нормального или короткое до высокого источника. Высокое напряжение, обнаруженное на цепи лампы ICONTM, когда низкое напряжение ожидалось электронным модулем управления двигателем (ECM). | не позволит активировать ICONTM, однако, если ICONTM активирован и код ошибки 198 активируется, ICONTM будет отключен. |

![[19803214.png]]

### Описание цепи

Схема лампы ICONTM освещает лампу ICONTM, чтобы указать, когда система ICONTM активна. Кроме того, на этой лампе будут высвечиваться коды неисправностей ICONTM. Схема лампы требует определенного времени вспышки (включения/выключения). Если напряжение включения/выключения некорректно, система ICONTM будет отключена. Схема лампы должна быть функциональной для включения ICONTM.

### Расположение компонента

Лампа ICONTM расположена в кабине автомобиля на приборной панели.

### Практические замечания

Эта неисправность указывает на короткое замыкание к напряжению батареи. Лампа ICONTM будет **только **выдавать активные коды неисправностей.

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
>

**Для уменьшения возможности повреждения штифта и проводов жгута проводов используйте при проведении измерений следующий испытательный щуп: Номер детали 3822917 - пробный щуп типа гнезда Deutsch/AMP/Metri-Pack Номер детали 3822758 - пробный щуп типа пробки Deutsch/AMP/Metri-Pack.**

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Прочитайте все коды ошибок. |  |
|  | **ШАГ 1А.** Прочитайте коды неисправностей с помощью инструментария электронного обслуживания INSITETM или выключите лампу ICONTM для кодов неисправностей ICONTM. | Код ошибки 198 неактивен |
| ШАГ 2. | Проверьте контакты подключения OEM-мотора и разъема ECM двигателя. |  |
|  | **STEP 2A.** Проверить электропроводку OEM-мотора и разъем ECM двигателя на наличие поврежденных контактов. | Никаких поврежденных контактов |
|  | **ШАГ 2В.** Проверьте короткое замыкание на аккумуляторе. | Менее 0,5 VDC |
|  | **STEP 2C.** Проверьте короткое замыкание от пин-кодов до пин-кодов. | Более 100 тыс. ом |
| ШАГ 3. | Проверьте лампу ICONTM. |  |
|  | **ШАГ 3А.** Проверьте разъем лампы ICONTM на наличие поврежденных контактов. | Никаких поврежденных контактов |
| ШАГ 4. | Очистите код ошибки. |  |
|  | **STEP 4A.** Отключить код ошибки. | Код ошибки 198 неактивен |

### ШАГ 1. Прочитайте все коды ошибок.

#### ШАГ 1A. Прочитайте коды неисправностей с помощью инструментария электронного обслуживания INSITETM или выключите лампу ICONTM для кодов неисправностей ICONTM.

| **Условия:** Включить переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Прочитайте коды неисправностей с помощью инструментария электронного обслуживания INSITETM или выключите лампу ICONTM. | Код ошибки 198 неактивен | 4А |
| Код ошибки 198 активный | 2А |  |

### ШАГ 2. Проверьте контакты подключения OEM-мотора и разъема ECM двигателя.

#### ШАГ 2A. Осмотрите упряжку для проводов двигателя OEM и разъем ECM двигателя для поврежденных контактов.

| **Условия:** Выключите замок зажигания. Отсоедините разъем OEM-моторной проводов от двигателя ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Корродированные штифты Бент или сломанные штифты Отталкивание назад или расширенные штифты Проводная изоляция Повреждение Влажность в или на разъем Пропавшие или поврежденные соединительные штифты Коннекторная оболочка разбитая Грязь или мусор в или на разъемных контактах. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 2В |
| Ремонт поврежденных контактов. Смывать грязь, мусор и влагу с контактов разъема с помощью электрического контактного очистителя, номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт или замена ремня электропроводки двигателя. См. процедуру 019-043 в руководстве по устранению и устранению неполадок, CELECT Plus Engines, Bulletin 3666084 или процедуру 019-043 в руководстве по устранению и устранению неполадок, электронную систему управления, ISM, в руководстве по устранению и устранению неполадок, или процедуру 019-031 в руководстве по устранению и устранению неполадок, электронную систему управления, систему 3666259 или процедуру 019-043 в руководстве по устранению и устранению неполадок, электронную систему управления, CM870 ISM, в руководстве по устранению и устранению неполадок или процедуру 019-043 в руководстве по устранению и устранению неполадок, в руководстве по электронной системе управления, в руководстве по устранению и устранению неполадок, в руководстве по электронной системе управления, в руководстве по устранению и устранению неполадок, в руководстве по электронной системе управления, в руководстве по устранению и устран Ремонт или замена OEM проводов жгута. См. сервисное руководство изготовителя машины. | 4А |  |

#### ШАГ 2B. Проверьте короткое замыкание на аккумуляторе.

| **Условия:** Отсоедините разъем электропроводки OEM-мотора от двигателя ECM. Удалите лампу из держателя лампы ICONTM. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте напряжение от контакта 4 в разъёме проводов OEM-двигателя на разъеме ECM двигателя на землю. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. | Менее 0,5 VDC | 2C |
| Ремонт или замена OEM-моторной проводов. См. сервисное руководство изготовителя машины. | 4А |  |

#### ШАГ 2C. Проверьте короткое замыкание от пин-кодов до пин-кодов.

| **Условия:** Выключите замок зажигания. Отсоедините разъем OEM-моторной проводов от двигателя ECM. Удалите лампу из держателя лампы ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта 4 в разъёме ремня электропроводки OEM-двигателя на ECM-двигателе ко всем другим штифтам в разъеме. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 100 тыс. ом | 3А |
| Ремонт или замена OEM проводов жгута. См. сервисное руководство изготовителя машины. | 4А |  |

### ШАГ 3. Проверьте лампу ICONTM.

#### ШАГ 3A. Проверьте разъем лампы ICONTM на наличие поврежденных контактов.

| **Условия:** Выключите замок зажигания. Отсоедините разъем лампы ICONTM от электропроводки OEM-кабины. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Корродированные штифты Бент или сломанные штифты Отталкивание назад или расширенные штифты Проводная изоляция Повреждение Влажность в или на разъем Пропавшие или поврежденные соединительные штифты Коннекторная оболочка разбитая Грязь или мусор в или на разъемных контактах. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 4А |
| Ремонт поврежденных контактов Смой грязь, мусор и влагу из контактов разъема с помощью электрического контактного очистителя, Номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт контактов разъема лампы. См. Процедуры 019-202 или 019-206. | 4А |  |

### ШАГ 4. Очистите код ошибки.

#### ШАГ 4A. Отключите код неисправности.

| **Условия: **Соединить все компоненты. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Убедитесь, что код 198 неактивен. Стирайте неактивные коды неисправностей с помощью инструментария электронного обслуживания INSITETM. | Код ошибки 198 неактивен | Ремонт завершён |
| Вернитесь к шагам устранения неполадок или свяжитесь с ближайшим авторизованным ремонтным центром Cummins, если все шаги были завершены и перепроверены. Устранение неполадок с оставшимися активными кодами неисправностей. | Соответствующие диаграммы устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 198 (Integrated)
>
> ### ICON™ Lamp Circuit - Voltage Above Normal or Shorted to High Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 198 PID(P): S122, 3 SPN: 612 FMI: 3 Lamp: Yellow SRT: | ICON™ Lamp Circuit - Voltage Above Normal or Shorted to High Source. High voltage detected at the ICON™ lamp circuit when low voltage was expected by the engine electronic control module (ECM). | Will **not** allow ICON™ to activate, however if ICON™ is engaged and fault code 198 becomes active, ICON™ will **not** be disabled. |
>
> ### Circuit Description
>
> The ICON™ lamp circuit illuminates the ICON™ lamp to indicate when the ICON™ system is active. In addition, ICON™ fault codes will be flashed out on this lamp. The lamp circuit requires a specific flash timing (on/off timing). If the on/off voltage is incorrect, the ICON™ system will be disabled. The lamp circuit **must** be functional to enable ICON™.
>
> ### Component Location
>
> The ICON™ lamp is located in the vehicle cab on the dash panel.
>
> ### Shoptalk
>
> This fault indicates a short circuit to battery voltage. The ICON™ lamp will **only** flash out the active fault codes.
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
>
> **To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822917 - female Deutsch/AMP/Metri-Pack test lead Part Number 3822758 - male Deutsch/AMP/Metri-Pack test lead.**
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Read all fault codes. |  |
> |  | **STEP 1A.** Read the fault codes with INSITE™ electronic service tool or flash out ICON™ lamp for ICON™ fault codes. | Fault Code 198 inactive |
> | STEP 2. | Check the OEM engine wiring harness and engine ECM connector pins. |  |
> |  | **STEP 2A.** Inspect the OEM engine wiring harness and engine ECM connector for damaged pins. | No damaged pins |
> |  | **STEP 2B.** Check for a short circuit to the battery. | Less than 0.5 VDC |
> |  | **STEP 2C.** Check for a short circuit from pin to pin. | More than 100k ohms |
> | STEP 3. | Check the ICON™ lamp. |  |
> |  | **STEP 3A.** Check the ICON™ lamp connector for damaged pins. | No damaged pins |
> | STEP 4. | Clear the fault code. |  |
> |  | **STEP 4A.** Disable the fault code. | Fault Code 198 inactive |
>
> ### STEP 1. Read all fault codes.
>
> #### STEP 1A. Read the fault codes with INSITE™ electronic service tool or flash out ICON™ lamp for ICON™ fault codes.
>
> | **Conditions:** Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Read the fault codes using INSITE™ electronic service tool or flash out ICON™ lamp. | Fault Code 198 inactive | 4A |
> | Fault Code 198 active | 2A |  |
>
> ### STEP 2. Check the OEM engine wiring harness and engine ECM connector pins.
>
> #### STEP 2A. Inspect the OEM engine wiring harness and engine ECM connector for damaged pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM engine wiring harness connector from the engine ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 2B |
> | Repair the damaged pins. Flush the dirt, debris, and moisture from the connector pins using the electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair or replace the engine harness. Refer to Procedure 019-043 in Troubleshooting and Repair Manual, CELECT Plus Engines, Bulletin 3666084, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, ISM, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], or Procedure 019-031 in Troubleshooting and Repair Manual, Electronic Control System, Signature and ISX, Bulletin 3666259, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM870 ISM, Bulletin 4021381, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM870 Signature and ISX, Bulletin 4021334, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM875 ISM, Bulletin 4021477. Repair or replace the OEM harness. Refer to the OEM service manual. | 4A |  |
>
> #### STEP 2B. Check for a short circuit to the battery.
>
> | **Conditions:** Disconnect the OEM engine wiring harness connector from the engine ECM. Remove the bulb from the ICON™ lamp holder. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the voltage from pin 4 in the OEM engine wiring harness connector at the engine ECM to ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. | Less than 0.5 VDC | 2C |
> | Repair or replace the OEM engine wiring harness. Refer to the OEM service manual. | 4A |  |
>
> #### STEP 2C. Check for a short circuit from pin to pin.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM engine wiring harness connector from the engine ECM. Remove the bulb from the ICON™ lamp holder. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 4 in the OEM engine wiring harness connector at the engine ECM to all other pins in the connector. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 3A |
> | Repair or replace the OEM wiring harness. Refer to the OEM service manual. | 4A |  |
>
> ### STEP 3. Check the ICON™ lamp.
>
> #### STEP 3A. Check the ICON™ lamp connector for damaged pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ lamp connector from the OEM cab harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 4A |
> | Repair the damaged pins Flush the dirt, debris, and moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the lamp connector pins. Refer to Procedures 019-202 or 019-206. | 4A |  |
>
> ### STEP 4. Clear the fault code.
>
> #### STEP 4A. Disable the fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify that Fault Code 198 is inactive. Erase the inactive fault codes using INSITE™ electronic service tool. | Fault Code 198 inactive | Repair complete |
> | Return to the troubleshooting steps, or contact the nearest Cummins Authorized Repair Location if all the steps have been completed and rechecked. Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
