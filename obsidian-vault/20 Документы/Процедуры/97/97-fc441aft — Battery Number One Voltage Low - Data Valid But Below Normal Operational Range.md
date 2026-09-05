---
type: "Процедура"
doc: "97-fc441aft"
title_en: "Battery Number One Voltage Low - Data Valid But Below Normal Operational Range - Moderately Severe Level"
modified: "2004-10-15"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc441aft.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc441aft.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
  - "перевод/машинный"
---

# Battery Number One Voltage Low - Data Valid But Below Normal Operational Range - Moderately Severe Level

> [!abstract] Процедура · `97-fc441aft`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-10-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc441aft.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc441aft.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 441 (Послепродажное и OEM)

### Низкий уровень напряжения батареи номер один - данные действительны, но ниже нормального операционного диапазона - умеренно тяжелый уровень

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 441 PID(P): СПН: ФМИ: Лампа: СТО: | Батарея номер один напряжение низкое - данные действительны, но ниже нормального операционного диапазона - умеренно тяжелый уровень. Напряжение батареи ниже нормального рабочего уровня. | Система ICONTM будет отключена. Включено только обязательное отключение. Двигатель запускается нормально. |

![[19803819.png]]

### Описание цепи

Модуль управления ICONTM idle получает непереключенный вход батареи через электропроводку двигателя ICONTM. В непереключенном проводе батареи есть один 5-амперный встроенный предохранитель для защиты провода жгута проводов двигателя ICONTM. Провода возврата аккумулятора соединены непосредственно с отрицательной (-) позицией аккумулятора. Вышеупомянутая схема может варьироваться, например, разъем или штифты, в зависимости от марки или модели транспортного средства. Установки OEM могут обеспечить взаимодействие между модулем управления холостым ходом и другими устройствами ICONTM.

### Расположение компонента

Модуль управления ICONTM холостым ходом подключается непосредственно к батареям через электропроводку двигателя ICONTM. Эта прямая линия обеспечивает постоянный источник питания для модуля управления ICONTM. См. руководство OEM для определения местоположения батареи. Модуль ICONTM может быть расположен в другом месте в зависимости от применения транспортного средства.

### Практические замечания

Непереключенные провода питания и возврата батареи должны быть непосредственно подключены к батарее для правильной работы системы ICONTM. Во время запуска системы ICONTM этот сбой может быть зарегистрирован во время проворачивания двигателя, если есть неисправное наземное соединение.

Эта неисправность будет зарегистрирована, если напряжение батареи падает ниже 9 VDC в системе 12 VDC. Это эквивалентно очень низкому напряжению батареи на электронном модуле управления двигателем (ECM).

Проведите испытание системы зарядки аккумулятора, как описано в Процедуре[[97-210-001 — Installation Procedure|210-001]]Руководство по установке, чтобы проверить, что батарея будет иметь достаточное напряжение для правильной работы системы ICONTM.

Система ICONTM может отображать только текущий активный код неисправности. Если одновременно активируется более одного кода неисправности, система ICONTM выдает наиболее приоритетную ошибку. После того, как ошибка была исправлена, будет выброшена следующая активная ошибка.

**Примечание: **Электронная система ICONTM может отображать более одного активного и неактивного кода неисправности одновременно.

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
>

**Для уменьшения возможности повреждения штифта и проводов жгута проводов используйте при проведении измерений следующий испытательный щуп: Номер детали 3822758 - пробный щуп типа пробоотвода Deutsch/AMP/Metri-Pack**

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте батареи и систему зарядки. |  |
|  | **ШАГ 1А.** Проверьте аккумуляторы и генератор. | Нет поврежденных соединений |
| ШАГ 2. | Проверьте статус ошибки. |  |
|  | **STEP 2A.** Используйте функцию вспышки неисправности или инструмент электронного сервиса ICONTM для считывания кодов неисправностей. | Код 441 неактивный |
| ШАГ 3. | Очистите код ошибки. |  |
|  | **STEP 3A.** Отключить код ошибки. | Код 441 неисправности обезврежен |

### ШАГ 1. Проверьте батареи и систему зарядки.

#### ШАГ 1A. Проверьте батареи и генератор переменного тока.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Для двигателей M11, обратитесь к процедуре 013-001, процедуре 013-007 и процедуре 013-009 в базовом руководстве по устранению неполадок и ремонту двигателя, в бюллетене 3666139. Для двигателей N14 обратитесь к процедуре 013-001, процедуре 013-007 и процедуре 013-009 в руководстве по устранению неполадок и ремонту базового двигателя, в бюллетене 3666142. Для двигателей ISM, обратитесь к процедуре 013-001, процедуре 013-007 и процедуре 013-009 в базовом руководстве по устранению неполадок и ремонту двигателя, в бюллетене [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. Для двигателей Signature и ISX обратитесь к процедуре 013-001, процедуре 013-007 и процедуре 013-009 в руководстве по устранению неполадок и ремонту базового двигателя, в бюллетене [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. | Более 12 VDC | 2А |
| Устранение неполадок любых других кодов неисправностей. | 3А |  |

### ШАГ 2. Проверьте статус ошибки.

#### ШАГ 2A. Используйте функцию вспышки неисправности или инструмент электронного сервиса ICONTM для считывания кодов неисправностей.

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите электронный сервис ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
|  | Код 441 неактивный | 3А |
| Код 441 активного отказа Заменить модуль управления ICONTM холостым ходом. См. процедуру[[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Ремонт завершён |  |

### ШАГ 3. Очистите код ошибки.

#### ШАГ 3A. Отключите код неисправности.

| **Условия: **Соединить все компоненты. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Цикл переключателя зажигания для проверки кода неисправности неактивен. | Код 441 неисправности обезврежен | Ремонт завершён |
| Устранение неполадок с оставшимися активными кодами неисправностей. | Соответствующие диаграммы устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 441 (Aftermarket and OEM)
>
> ### Battery Number One Voltage Low - Data Valid But Below Normal Operational Range - Moderately Severe Level
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 441 PID(P): SPN: FMI: Lamp: SRT: | Battery Number One Voltage Low - Data Valid But Below Normal Operational Range - Moderately Severe Level. Battery voltage below normal operating level. | The ICON™ system will be disabled. **Only** mandatory shutdown will be enabled. Engine will start normally. |
>
> ### Circuit Description
>
> The ICON™ idle control module receives unswitched battery input through the ICON™ engine harness. There is one 5-amp in-line fuse in the unswitched battery wire to protect the ICON™ engine harness wire. The battery return wires are connected directly to the negative (-) battery post. The above circuit diagram can vary, such as connector or pins, depending on the vehicle make or model. OEM installations can possibly provide the harnessing between the idle control module and other ICON™ devices.
>
> ### Component Location
>
> The ICON™ idle control module is connected directly to the batteries through the ICON™ engine harness. This direct link provides a constant power supply for the ICON™ idle control module. Refer to the OEM manual for the battery location. The ICON™ module can be located in a different location depending on the vehicle application.
>
> ### Shoptalk
>
> The unswitched battery supply and return wires **must** be directly connected to the battery for the ICON™ system to function properly. During the ICON™ system start, this fault can be logged during engine cranking if there is a faulty ground connection.
>
> This fault will be logged if the battery voltage falls below 9 VDC on a 12 VDC system. This is equivalent to a very low battery voltage on the engine electronic control module (ECM).
>
> Perform a battery charging system test as described in Procedure [[97-210-001 — Installation Procedure|210-001]], Installation Guidelines, to verify the battery will have adequate voltage for the ICON™ system to function properly.
>
> The ICON™ system can display **only** the present active fault code. If more than one fault code is active at the same time, the ICON™ system flashes out the highest priority fault. After the fault has been corrected then the next active fault will be flashed out.
>
> **Note:** The ICON™ electronic service tool can display more than one active and or inactive fault codes at the same time.
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
>
> **To reduce the possibility of pin and harness damage, use the following test lead when taking a measurement: Part Number 3822758 - male Deutsch/AMP/Metri-Pack test lead.**
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the batteries and charging system. |  |
> |  | **STEP 1A.** Check the batteries and alternator. | No damaged connections |
> | STEP 2. | Check the fault status. |  |
> |  | **STEP 2A.** Use the fault flashout feature or the ICON™ electronic service tool to read the fault codes. | Fault Code 441 inactive |
> | STEP 3. | Clear the fault code. |  |
> |  | **STEP 3A.** Disable the fault code. | Fault Code 441 cleared |
>
> ### STEP 1. Check the batteries and charging system.
>
> #### STEP 1A. Check the batteries and alternator.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | For M11 engines, refer to Procedure 013-001, Procedure 013-007, and Procedure 013-009 in the base engine Troubleshooting and Repair Manual, Bulletin 3666139. For N14 engines, refer to Procedure 013-001, Procedure 013-007, and Procedure 013-009 in the base engine Troubleshooting and Repair Manual, Bulletin 3666142. For ISM engines, refer to Procedure 013-001, Procedure 013-007, and Procedure 013-009 in the base engine Troubleshooting and Repair Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. For Signature and ISX engines, refer to Procedure 013-001, Procedure 013-007, and Procedure 013-009 in the base engine Troubleshooting and Repair Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. | More than 12 VDC | 2A |
> | Troubleshoot any other fault codes. | 3A |  |
>
> ### STEP 2. Check the fault status.
>
> #### STEP 2A. Use the fault flashout feature or the ICON™ electronic service tool to read the fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect the ICON™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> |  | Fault Code 441 inactive | 3A |
> | Fault Code 441 active Replace the ICON™ idle control module. Refer to Procedure [[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Repair Complete |  |
>
> ### STEP 3. Clear the fault code.
>
> #### STEP 3A. Disable the fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Cycle the keyswitch to verify the fault code is inactive. | Fault Code 441 cleared | Repair complete |
> | Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
