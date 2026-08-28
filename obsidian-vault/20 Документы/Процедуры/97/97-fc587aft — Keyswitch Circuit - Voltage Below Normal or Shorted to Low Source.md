---
type: "Процедура"
doc: "97-fc587aft"
title_en: "Keyswitch Circuit - Voltage Below Normal or Shorted to Low Source"
modified: "2007-01-26"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc587aft.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc587aft.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
  - "перевод/машинный"
---

# Keyswitch Circuit - Voltage Below Normal or Shorted to Low Source

> [!abstract] Процедура · `97-fc587aft`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2007-01-26
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc587aft.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc587aft.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 587 (Послепродажное обслуживание и OEM)

### Замок зажигания - напряжение ниже нормального или короткое до низкого источника

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 587 PID(P): СПН: ФМИ: Лампа: СТО: | Замок зажигания - напряжение ниже нормального или короткое до низкого источника. Низкое напряжение, обнаруженное в выходной цепи переключателя зажигания модуля управления холостым ходом ICONTM, когда высокое напряжение ожидалось модулем управления холостым ходом ICONTM. | Система ICONTM будет отключена. Обязательная остановка также может быть отключена. Двигатель будет **не** нормально запускать. Двигатель отключится. |

![[19c01536.png]]

### Описание цепи

Выводная схема переключателя зажигания обеспечивает входной сигнал переключателя зажигания для модуля управления двигателем и реле пускового устройства. Вышеупомянутая схема может варьироваться, например, разъем или штифты, в зависимости от марки или модели транспортного средства. Установки OEM могут обеспечить взаимодействие между модулем управления холостым ходом и другими устройствами ICONTM.

### Расположение компонента

Сигнал переключателя зажигания соединяется с контактом 26 разъема привода на ремне электропроводки двигателя для двигателей CELECTTM Plus и контактом 39 для электронного модуля управления CM870 и CM875 (ECM) и контактом 38 разъема OEM для двигателей ISM, ISX и Signature. Он также подключается к контакту 85 стартового реле. Это предполагает наличие входного напряжения переключателя зажигания от переключателя зажигания до контакта 7 модуля управления неработающим ICONTM разъем А.

Модуль ICONTM может быть расположен в другом месте в зависимости от применения транспортного средства.

### Практические замечания

Эта неисправность обычно указывает на короткое замыкание на землю. Двигатель может быть не в состоянии запуститься.

Система ICONTM может отображать только текущий активный код неисправности. Если одновременно активируется более одного кода неисправности, система ICON выдает наиболее приоритетную ошибку. После того, как ошибка была исправлена, будет выброшена следующая активная ошибка.

**Примечание: **Электронная система ICONTM может отображать более одного активного и неактивного кода неисправности одновременно.

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
>

**Для уменьшения возможности повреждения штифта и проводов жгута проводов используйте при проведении измерений следующий испытательный щуп: Номер детали 3822758 - пробный щуп типа пробоотвода Deutsch/AMP/Metri-Pack Номер детали 3822917 - пробный щуп типа разъема Deutsch/AMP/Metri-Pack.**

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Считайте коды неисправностей. |  |
|  | **STEP 1A.** Используйте функцию вспышки неисправности или инструмент электронного сервиса ICONTM для считывания кодов неисправностей. | Код ошибки 587 активный |
| ШАГ 2. | Проверьте модуль управления ICONTM. |  |
|  | **STEP 2A.** Проверить коннекторы соединительного устройства двигателя ICONTM и коннектора модуля управления ICONTM. | Никаких поврежденных контактов |
|  | **STEP 2B.** Проверьте выход модуля управления холостым ходом ICONTM. | Больше 10 VDC |
| ШАГ 3. | Проверьте электропроводку ICONTM. |  |
|  | **ШАГ 3А.** Проверьте короткое замыкание на землю. | Более 100 тыс. ом |
|  | **STEP 3A-1.** Проверьте двигатель ECM. | Неисправность становится неактивной |
| ШАГ 4. | Очистите код ошибки. |  |
|  | **STEP 4A.** Отключить код ошибки. | Код ошибки 587 обезврежен |

### ШАГ 1. Считайте коды неисправностей.

#### ШАГ 1A. Используйте функцию вспышки неисправности или инструмент электронного сервиса ICONTM для считывания кодов неисправностей.

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите электронный сервис ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Используйте функцию вспышки неисправности или инструмент электронного сервиса ICONTM для считывания кодов неисправностей. | Код ошибки 587 активен. | 2А |
| Неактивные или прерывистые коды ошибок, процедура[[99-019-362 — Inactive or Intermittent Fault Code\|019-362]]. | 4А |  |

### ШАГ 2. Проверьте модуль управления ICONTM.

#### ШАГ 2A. Проверьте контакты разъема модуля управления ICONTM.

| **Условия:** Выключите замок зажигания. Отсоедините разъем B модуля управления ICONTM от модуля управления ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить контакты разъема модуля управления ICONTM для холостого хода на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема разъема разъема или разъема изоляции Поврежденный разъем блокировки вкладки. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 2В |
| Ремонт поврежденных контактов. Промывайте грязь, мусор или влагу от контактов разъема с помощью электрического контактного очистителя, Номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт ремня электропроводки двигателя ICONTM. См. процедуру 019-206 или 019-207. Заменить электропроводку двигателя ICONTM. См. процедуру 019-043. По мере необходимости ремонтировать или заменять электропроводку OEM. | 4А |  |

#### ШАГ 2B. Проверьте выход модуля управления ICONTM.

| **Условия:** Включить переключатель зажигания. Отсоедините разъем B модуля управления ICONTM от модуля управления ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить напряжение при контакте 5 неработающего модуля управления ICONTM B с заземлением блока двигателя. См. схему проводов или схему схемы для идентификации контакта с разъемом. Для методов использования мультиметра, обратитесь к использованию мультиметра, процедура[[99-019-359 — Multimeter Usage\|019-359]]. | Больше 10 VDC | 3А |
| Заменить модуль управления ICONTM idle. См. процедуру[[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Ремонт завершён |  |

### ШАГ 3. Проверьте электропроводку ICONTM.

#### ШАГ 3A. Проверьте, чтобы короткое время приземлиться в электропроводке ICONTM.

| **Условия:** Выключите замок зажигания. Отсоедините разъем B модуля управления ICONTM от модуля управления ICONTM. Отключите разъемы ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта 5 разъема OEM-проводов ICONTM Aftermarket к заземлению блока двигателя. См. схему проводов или схему схемы для идентификации контакта с разъемом. Для методов использования мультиметра, обратитесь к использованию мультиметра, процедура[[99-019-359 — Multimeter Usage\|019-359]]. | Больше 100k Ом | 3А-1-1 |
| Ремонт ремня электропроводки двигателя ICONTM. См. процедуру 019-206 или 019-207. Заменить электропроводку двигателя ICONTM. См. процедуру 019-043. По мере необходимости ремонтировать или заменять электропроводку OEM. | 4А |  |

#### ШАГ 3A-1. Проверьте состояние кода неисправности двигателя.

| **Условия:** Включить переключатель зажигания. Подключите электронный сервис ICONTM. Отключите разъемы ECM двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте статус ошибки. Выключите замок зажигания на 30 секунд. Включите зажигание. Проверьте статус кода ошибки. | Неисправность становится неактивной, устраняет неисправности кодов двигателя ECM. См. Troubleshooting and Repair Manual, CELECTTM Plus, Bulletin 3666130, or Troubleshooting and Repair Manual, Electronic Control System, ISM, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], or Troubleshooting and Repair Manual, Electronic Control System, Signature and ISX, Bulletin 3666259, or Troubleshooting and Repair Manual, Electronic Control System, CM870 ISM, Bulletin 4021381, or Troubleshooting and Repair Manual, Electronic Control System, CM875 ISM, Bulletin 4021477. | 4А |
| Заменить модуль управления ICONTM idle. См. процедуру[[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Ремонт завершён |  |

### ШАГ 4. Очистите код ошибки.

#### ШАГ 4A. Отключите код неисправности.

| **Условия: **Соединить все компоненты. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Очистите код неактивной ошибки. Цикл переключателя зажигания для проверки кода неисправности неактивен. | Код ошибки 587 обезврежен | Ремонт завершён |
| Устранение неполадок с оставшимися активными кодами неисправностей. | Соответствующие диаграммы устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 587 (Aftermarket and OEM)
>
> ### Keyswitch Circuit - Voltage Below Normal or Shorted to Low Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 587 PID(P): SPN: FMI: Lamp: SRT: | Keyswitch Circuit - Voltage Below Normal or Shorted to Low Source. Low voltage detected at the keyswitch output circuit of the ICON™ idle control module when high voltage was expected by the ICON™ idle control module. | The ICON™ system will be disabled. Mandatory shutdown can also be disabled. Engine will **not** start normally. Engine will shutdown. |
>
> ### Circuit Description
>
> The keyswitch output circuit provides the keyswitch input signal for the engine control module and starter relay. The above circuit diagram can vary, such as connector or pins, depending on the vehicle make or model. OEM installations can possibly provide the harnessing between the idle control module and other ICON™ devices.
>
> ### Component Location
>
> The keyswitch signal connects to pin 26 of the actuator connector on the engine harness for CELECT™ Plus engines, and pin 39 for the CM870 and CM875 electronic control module (ECMs), and pin 38 of the OEM connector for ISM, ISX, and Signature engines. It also connects to pin 85 of the starter relay. This assumes the keyswitch input voltage from the keyswitch to pin 7 of the ICON™ idle control module A connector is present.
>
> The ICON™ module can be located in a different location depending on the vehicle application.
>
> ### Shoptalk
>
> This fault typically indicates a short circuit to ground. The engine will possibly **not** be able to start.
>
> The ICON™ system can display **only** the present active fault code. If more than one fault code is active at the same time, the ICON system flashes out the highest priority fault. After the fault has been corrected then the next active fault will be flashed out.
>
> **Note:** The ICON™ electronic service tool can display more than one active and or inactive fault codes at the same time.
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
>
> **To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch/AMP/Metri-Pack test lead Part Number 3822917 - female Deutsch/AMP/Metri-Pack test lead.**
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Read the fault codes. |  |
> |  | **STEP 1A.** Use the fault flashout feature or the ICON™ electronic service tool to read the fault codes. | Fault Code 587 active |
> | STEP 2. | Check the ICON™ idle control module. |  |
> |  | **STEP 2A.** Inspect the ICON™ engine harness and ICON™ idle control module connector pins. | No damaged pins |
> |  | **STEP 2B.** Check the output of the ICON™ idle control module. | Greater than 10 VDC |
> | STEP 3. | Check the ICON™ harness. |  |
> |  | **STEP 3A.** Check for a short circuit to ground. | More than 100k ohms |
> |  | **STEP 3A-1.** Check the engine ECM. | Fault becomes inactive |
> | STEP 4. | Clear the fault code. |  |
> |  | **STEP 4A.** Disable the fault code. | Fault Code 587 cleared |
>
> ### STEP 1. Read the fault codes.
>
> #### STEP 1A. Use the fault flashout feature or the ICON™ electronic service tool to read the fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect the ICON™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Use the fault flashout feature or the ICON™ electronic service tool to read the fault codes. | Fault Code 587 active. | 2A |
> | Refer to Inactive or Intermittent Fault Codes, Procedure [[99-019-362 — Inactive or Intermittent Fault Code\|019-362]]. | 4A |  |
>
> ### STEP 2. Check the ICON™ idle control module.
>
> #### STEP 2A. Check the ICON™ idle control module connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module B connector from the ICON™ idle control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the ICON™ idle control module connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris on or in the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 2B |
> | Repair the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair or replace the OEM wiring harness as necessary. | 4A |  |
>
> #### STEP 2B. Check the output of the ICON™ idle control module.
>
> | **Conditions:** Turn keyswitch ON. Disconnect the ICON™ idle control module B connector from the ICON™ idle control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the voltage at pin 5 of the ICON™ idle control module B connector to engine block ground. Refer to the wiring diagram or the circuit diagram for connector pin identification. For multimeter usage techniques, refer to Multimeter Usage, Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | Greater than 10 VDC | 3A |
> | Replace the ICON™ idle control module. Refer to Procedure [[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Repair complete |  |
>
> ### STEP 3. Check the ICON™ harness.
>
> #### STEP 3A. Check for a short to ground in the ICON™ harness.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module B connector from the ICON™ idle control module. Disconnect the ECM connectors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 5 of the ICON™ Aftermarket OEM harness connector to engine block ground. Refer to the wiring diagram or the circuit diagram for connector pin identification. For multimeter usage techniques, refer to Multimeter Usage, Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | Greater than 100k ohms | 3A-1 |
> | Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair or replace the OEM wiring harness as necessary. | 4A |  |
>
> #### STEP 3A-1. Check the engine fault code status.
>
> | **Conditions:** Turn keyswitch ON. Connect the ICON™ electronic service tool. Disconnect the engine ECM connectors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the fault status. Turn keyswitch OFF for 30 seconds. Turn keyswitch ON. Check the fault code status. | Fault becomes inactive Troubleshoot the engine ECM fault codes. Refer to Troubleshooting and Repair Manual, CELECT™ Plus, Bulletin 3666130, or Troubleshooting and Repair Manual, Electronic Control System, ISM, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], or Troubleshooting and Repair Manual, Electronic Control System, Signature and ISX, Bulletin 3666259, or Troubleshooting and Repair Manual, Electronic Control System, CM870 ISM, Bulletin 4021381, or Troubleshooting and Repair Manual, Electronic Control System, CM870 Signature and ISX, Bulletin 4021334, or Troubleshooting and Repair Manual, Electronic Control System, CM875 ISM, Bulletin 4021477. | 4A |
> | Replace the ICON™ idle control module. Refer to Procedure [[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Repair complete |  |
>
> ### STEP 4. Clear the fault code.
>
> #### STEP 4A. Disable the fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Clear the inactive fault code. Cycle the keyswitch to verify the fault code is inactive. | Fault Code 587 cleared | Repair complete |
> | Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
