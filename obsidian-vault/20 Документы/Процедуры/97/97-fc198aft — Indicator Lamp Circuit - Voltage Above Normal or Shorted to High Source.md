---
type: "Процедура"
doc: "97-fc198aft"
title_en: "Indicator Lamp Circuit - Voltage Above Normal or Shorted to High Source"
modified: "2004-10-04"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc198aft.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc198aft.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
  - "перевод/машинный"
---

# Indicator Lamp Circuit - Voltage Above Normal or Shorted to High Source

> [!abstract] Процедура · `97-fc198aft`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-10-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc198aft.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc198aft.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 198 (Послепродажное и OEM)

### Циркута лампы индикатора - напряжение выше нормального или короткое к высокому источнику

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 198 PID(P): СПН: ФМИ: Лампа: СТО: | Циркулятор лампы индикатора - напряжение выше нормального или короткое к высокому источнику. Высокое напряжение, обнаруженное на лампе ICONTM или светодиодной цепи, когда низкое напряжение ожидалось модулем управления ICONTM. | Система ICONTM будет отключена. Включено только обязательное отключение. |

![[19802947.png]]

### Описание цепи

Лампа ICONTM или светодиодная схема включает лампу ICONTM, чтобы указать, когда система ICONTM активна. Кроме того, на этой лампе будут высвечиваться коды неисправностей ICONTM. Лампа или светодиодная схема требуют определенного времени вспышки (включения / выключения). Если напряжение включения/выключения некорректно, система ICONTM будет отключена. Лампа или светодиодная схема должны быть функциональными для включения системы ICONTM. Вышеупомянутая схема может варьироваться, например, разъем или штифты, в зависимости от марки или модели транспортного средства. Установки OEM могут обеспечить взаимодействие между модулем управления холостым ходом и другими устройствами ICONTM.

### Расположение компонента

Лампа ICONTM или светодиод обычно расположены в кабине автомобиля на панели приборов.

Модуль ICONTM может быть расположен в другом месте в зависимости от применения транспортного средства.

### Практические замечания

Эта неисправность указывает на короткое замыкание к напряжению батареи.

Система ICONTM может отображать только текущий активный код неисправности. Если одновременно активируется более одного кода неисправности, система ICONTM выдает наиболее приоритетную ошибку. После того, как ошибка была исправлена, будет выброшена следующая активная ошибка.

**Примечание: **Электронная система ICONTM может отображать более одного активного и неактивного кода неисправности одновременно.

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
>

**Для уменьшения возможности повреждения штифта и проводов жгута проводов используйте при проведении измерений следующий испытательный щуп: Номер детали 3822758 - пробный щуп типа пробоотвода Deutsch/AMP/Metri-Pack Номер детали 3822917 - пробный щуп типа разъема Deutsch/AMP/Metri-Pack.**

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Считайте коды неисправностей. |  |
|  | **STEP 1A.** Используйте функцию вспышки неисправности или инструмент электронного сервиса ICONTM для считывания кодов неисправностей. | Код ошибки 198 неактивен |
| ШАГ 2. | Проверьте лампу ICONTM. |  |
|  | **ШАГ 2А.** Проверьте разъем лампы ICONTM на наличие поврежденных контактов. | Никаких поврежденных контактов |
|  | **STEP 2B.** Проверьте короткое замыкание на аккумуляторе. | Менее 0,5 VDC |
| ШАГ 3. | Проверьте проводные ремни ICONTM. |  |
|  | **STEP 3A.** Проверить контакты разъема модуля управления ICONTM с проводкой двигателя, кабины и проводов ICONTM. | Никаких поврежденных контактов |
|  | **STEP 3B.** Проверьте полную проводку ремня для короткого замыкания от пин-кодов до пин-кодов. | Более 100 тыс. ом |
|  | **STEP 3B-1.** Определите, является ли система ICONTM послепродажным или OEM-производителем. | Система ICONTM является системой Aftermarket. |
|  | **STEP 3B-2.** Проверьте электропроводку кабины на короткое замыкание от пин-кодов до пин-кодов. | Более 100 тыс. ом |
|  | **STEP 3C.** Проверьте полную проводку ремня для короткого замыкания к батарее. | Менее 0,5 VDC |
|  | **STEP 3C-1.** Определите, является ли система ICONTM послепродажным или OEM-производителем. | Система ICONTM является системой Aftermarket. |
|  | **STEP 3C-2.** Проверьте электропроводку кабины на короткое замыкание к батарее. | Менее 0,5 VDC |
| ШАГ 4. | Очистите код ошибки. |  |
|  | **STEP 4A.** Отключить код ошибки. | Код ошибки 198 обезврежен |

### ШАГ 1. Считайте коды неисправностей.

#### ШАГ 1A. Используйте функцию вспышки неисправности или инструмент электронного сервиса ICONTM для считывания кодов неисправностей.

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите электронный сервис ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
|  | Код ошибки 198 неактивен. Неактивные или прерывистые коды ошибок, процедура[[99-019-362 — Inactive or Intermittent Fault Code\|019-362]]. | 4А |
|  | 2А |  |

### ШАГ 2. Проверьте лампу ICONTM.

#### ШАГ 2A. Проверьте разъем лампы ICONTM на наличие поврежденных контактов.

| **Условия:** Выключите замок зажигания. Подключите электронный сервис ICONTM для подтверждения состояния неисправности. Отсоедините разъем лампы ICONTM от электропроводки кабины. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Корродированные штифты Бент или сломанные штифты Отталкивание назад или расширенные штифты Проводная изоляция Повреждение Влажность в или на разъем Пропавшие или поврежденные соединительные штифты Коннекторная оболочка разбитая Грязь или мусор в или на разъемных контактах. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 2В |
| Ремонт поврежденных контактов. Промывайте грязь, мусор или влагу от контактов разъема с помощью электрического контактного очистителя, Номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт контактов разъема лампы. См. Процедуры 019-202 или 019-206. По мере необходимости ремонтировать или заменять электропроводку OEM. | 4А |  |

#### ШАГ 2B. Проверьте короткое замыкание на аккумулятор.

| **Условия:** Выключите замок зажигания. Подключите электронный сервис ICONTM для подтверждения состояния неисправности. Отсоедините разъем лампы ICONTM от электропроводки кабины. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте напряжение от контакта А контактов разъема лампы ICONTM с заземлением блока двигателя. Измерьте напряжение от контакта B контактов разъема лампы ICONTM с заземлением блока двигателя. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для методов использования мультиметра, обратитесь к использованию мультиметра, процедура[[99-019-359 — Multimeter Usage\|019-359]]. | Менее 0,5 VDC | 3А |
| Ремонт или замена лампы ICONTM. См. процедуру[[99-019-046 — Fault Lamp\|019-046]]. | 4А |  |

### ШАГ 3. Проверьте проводные ремни ICONTM.

#### ШАГ 3A. Осмотрите контакты разъема проводов двигателя ICONTM, проводов кабины и коннектора модуля управления ICONTM.

| **Условия:** Выключите замок зажигания. Отсоедините разъемы ICONTM Idle Control Module A и B от модуля ICONTM idle Control. Отключите все разъёмы между лампой и модулем ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Корродированные штифты Бент или сломанные штифты Отталкивание назад или расширенные штифты Проводная изоляция Повреждение Влажность в или на разъем Пропавшие или поврежденные соединительные штифты Коннекторная оболочка разбитая Грязь или мусор в или на разъемных контактах. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 3B |
| Ремонт поврежденных контактов. Промывайте грязь, мусор или влагу от контактов разъема с помощью электрического контактного очистителя, Номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт ремня электропроводки двигателя ICONTM. См. процедуру 019-206 или 019-207. Заменить электропроводку двигателя ICONTM. См. процедуру 019-043. Ремонт проводов такси. См. процедуру 019-207. Замените проводку кабины. См. процедуру 019-305. По мере необходимости ремонтировать или заменять электропроводку OEM. | 4А |  |

#### ШАГ 3B. Проверьте полную проводку ремня для короткого замыкания от пин-кодов до пин-кодов.

| **Условия:** Выключите замок зажигания. Отсоедините разъемы ICONTM Idle Control Module A и B от модуля ICONTM idle Control. Отсоедините разъем лампы ICONTM от электропроводки кабины. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта 5 в неработающем модуле управления ICONTM Разъем проводов жгута ко всем другим штифтам в разъеме. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 100 тыс. ом | 3C |
|  | 3В-1-1 |  |

#### ШАГ 3B-1. Определите, является ли система ICONTM послепродажным или OEM-производителем.

| **Условия: **Ни одно |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| См. процедуру[[97-209-017 — ICON™ Idle Control System\|209-017]]. | Система ICONTM является системой Aftermarket. | 3В-2-2 |
| Проверьте штифт OEM-проводов, чтобы зажать короткий в выходной цепи лампы. | 4А |  |

#### ШАГ 3B-2. Проверьте электропроводку кабины для короткого замыкания от пин-кодов до пин-кодов.

| **Условия: **Отсоедините 14-контактный разъем. Отключите лампу ICONTM или светодиод. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта J в 14-контактном проходном разъеме, кабинной проводах с упряжкой, ко всем другим штифтам, кроме контакта K в разъеме, кабинной проводах с упряжкой. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 100 тыс. омов Ремонт или замена ремня электропроводки двигателя ICONTM. Ремонт ремня электропроводки двигателя ICONTM. См. процедуру 019-206 или 019-207. Заменить электропроводку двигателя ICONTM. См. процедуру 019-043. | 4А |
| Ремонт или замена кабины ICONTM ремень проводов кабины. См. процедуру 019-207. Замените проводку кабины. См. процедуру 019-305. | 4А |  |

#### ШАГ 3C. Проверьте полную проводку ремня для короткого замыкания к батарее.

| **Условия:** Отсоединить разъемы ICONTM Idle Control Module A и B от модуля ICONTM idle Control. Примечание: Все остальные компоненты должны быть подключены. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить напряжение от контакта 5 модуля управления ICONTM холостого хода A проводов жгута разъёма с блоком двигателя земли. Измерить напряжение от контакта 6 модуля управления ICONTM холостого хода A разъёма проводной упряжки с заземлением блока двигателя. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для методов использования мультиметра, обратитесь к использованию мультиметра, процедура[[99-019-359 — Multimeter Usage\|019-359]]. | Менее 0,5 VDC Заменить модуль управления ICONTM. См. процедуру[[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Ремонт завершён |
|  | 3С-1-1 |  |

#### ШАГ 3C-1. Определите, является ли система ICONTM послепродажным или OEM-производителем.

| **Условия: **Ни одно |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| См. процедуру[[97-209-017 — ICON™ Idle Control System\|209-017]]. | Система ICONTM является системой Aftermarket. | 3С-2 |
| Проверьте OEM-проводку для короткого замыкания к батарее в выходной цепи лампы. | 4А |  |

#### ШАГ 3C-2. Проверьте электропроводку кабины для короткого замыкания к батарее.

| **Условия: **Отсоедините 14-контактный разъем. Примечание: Все остальные компоненты должны быть подключены. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте напряжение от контакта J в 14-контактном проходном разъеме, стороне проводов кабины, к заземлению блока двигателя. Измерьте напряжение от контакта D в 14-контактном проходном разъеме, стороне проводов кабины, до заземления блока двигателя. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для методов использования мультиметра, обратитесь к использованию мультиметра, процедура[[99-019-359 — Multimeter Usage\|019-359]]. | Ремонт или замена ремня электропроводки двигателя ICONTM менее 0,5 VDC. Ремонт ремня электропроводки двигателя ICONTM. См. процедуру 019-206 или 019-207. Заменить электропроводку двигателя ICONTM. См. процедуру 019-043. | 4А |
| Ремонт или замена кабины ICONTM ремень проводов кабины. См. процедуру 019-207. Замените проводку кабины. См. процедуру 019-305. | 4А |  |

### ШАГ 4. Очистите код ошибки.

#### ШАГ 4A. Отключите код неисправности.

| **Условия: **Соединить все компоненты. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Цикл переключателя зажигания для проверки кода неисправности неактивен. | Код ошибки 198 обезврежен | Ремонт завершён |
| Устранение неполадок с оставшимися активными кодами неисправностей. | Соответствующие диаграммы устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 198 (Aftermarket and OEM)
>
> ### Indicator Lamp Circuit - Voltage Above Normal or Shorted to High Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 198 PID(P): SPN: FMI: Lamp: SRT: | Indicator Lamp Circuit - Voltage Above Normal or Shorted to High Source. High voltage detected at the ICON™ lamp or LED circuit when low voltage was expected by the ICON™ idle control module. | The ICON™ system will be disabled. **Only** mandatory shutdown will be enabled. |
>
> ### Circuit Description
>
> The ICON™ lamp or LED circuit turns on the ICON™ lamp to indicate when the ICON™ system is active. In addition, ICON™ fault codes will be flashed out on this lamp. The lamp or LED circuit requires a specific flash timing (on/off timing). If the on/off voltage is incorrect, the ICON™ system will be disabled. The lamp or LED circuit **must** be functional to enable the ICON™ system. The above circuit diagram can vary, such as connector or pins, depending on the vehicle make or model. OEM installations can possibly provide the harnessing between the idle control module and other ICON™ devices.
>
> ### Component Location
>
> The ICON™ lamp or LED is typically located in the vehicle cab on the dash panel.
>
> The ICON™ module can be located in a different location depending on the vehicle application.
>
> ### Shoptalk
>
> This fault indicates a short circuit to battery voltage.
>
> The ICON™ system can display **only** the present active fault code. If more than one fault code is active at the same time, the ICON™ system flashes out the highest priority fault. After the fault has been corrected then the next active fault will be flashed out.
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
> |  | **STEP 1A.** Use the fault flashout feature or the ICON™ electronic service tool to read the fault codes. | Fault Code 198 inactive |
> | STEP 2. | Check the ICON™ lamp. |  |
> |  | **STEP 2A.** Check the ICON™ lamp connector for damaged pins. | No damaged pins |
> |  | **STEP 2B.** Check for a short circuit to battery. | Less than 0.5 VDC |
> | STEP 3. | Check the ICON™ harnesses. |  |
> |  | **STEP 3A.** Inspect the ICON™ engine harness, cab harness, and ICON™ idle control module connector pins. | No damaged pins |
> |  | **STEP 3B.** Check the complete harness for a short circuit from pin to pin. | More than 100k ohms |
> |  | **STEP 3B-1.** Identify whether the ICON™ system is an Aftermarket or an OEM. | ICON™ system is Aftermarket |
> |  | **STEP 3B-2.** Check the cab harness for a short circuit from pin to pin. | More than 100k ohms |
> |  | **STEP 3C.** Check the complete harness for a short circuit to the battery. | Less than 0.5 VDC |
> |  | **STEP 3C-1.** Identify whether the ICON™ system is an Aftermarket or an OEM. | ICON™ system is Aftermarket |
> |  | **STEP 3C-2.** Check the cab harness for a short circuit to the battery. | Less than 0.5 VDC |
> | STEP 4. | Clear the fault code. |  |
> |  | **STEP 4A.** Disable the fault code. | Fault Code 198 cleared |
>
> ### STEP 1. Read the fault codes.
>
> #### STEP 1A. Use the fault flashout feature or the ICON™ electronic service tool to read the fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect the ICON™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> |  | Fault Code 198 inactive. Refer to Inactive or Intermittent Fault Codes, Procedure [[99-019-362 — Inactive or Intermittent Fault Code\|019-362]]. | 4A |
> |  | 2A |  |
>
> ### STEP 2. Check the ICON™ lamp.
>
> #### STEP 2A. Check the ICON™ lamp connector for damaged pins.
>
> | **Conditions:** Turn keyswitch OFF. Connect the ICON™ electronic service tool to confirm the fault status. Disconnect the ICON™ lamp connector from the cab harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 2B |
> | Repair the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the lamp connector pins. Refer to Procedures 019-202 or 019-206. Repair or replace the OEM wiring harness as necessary. | 4A |  |
>
> #### STEP 2B. Check for a short circuit to battery.
>
> | **Conditions:** Turn keyswitch OFF. Connect the ICON™ electronic service tool to confirm the fault status. Disconnect the ICON™ lamp connector from the cab harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the voltage from pin A of the ICON™ lamp connector pins to engine block ground. Measure the voltage from pin B of the ICON™ lamp connector pins to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For multimeter usage techniques, refer to Multimeter Usage, Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | Less than 0.5 VDC | 3A |
> | Repair or replace the ICON™ lamp assembly. Refer to Procedure [[99-019-046 — Fault Lamp\|019-046]]. | 4A |  |
>
> ### STEP 3. Check the ICON™ harnesses.
>
> #### STEP 3A. Inspect the ICON™ engine harness, cab harness, and ICON™ idle control module connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module A and B connectors from the ICON™ idle control module. Disconnect all connectors between the lamp and ICON™ module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 3B |
> | Repair the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair the cab harness. Refer to Procedure 019-207. Replace the cab harness. Refer to Procedure 019-305. Repair or replace the OEM wiring harness as necessary. | 4A |  |
>
> #### STEP 3B. Check the complete harness for a short circuit from pin to pin.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module A and B connectors from the ICON™ idle control module. Disconnect the ICON™ lamp connector from the cab harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 5 in the ICON™ idle control module A harness connector to all other pins in the connector. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 3C |
> |  | 3B-1 |  |
>
> #### STEP 3B-1. Identify whether the ICON™ system is an Aftermarket or an OEM.
>
> | **Conditions:** None |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Refer to Procedure [[97-209-017 — ICON™ Idle Control System\|209-017]]. | ICON™ system is Aftermarket | 3B-2 |
> | Check the OEM wiring harness pin to pin for a short in the lamp output circuit. | 4A |  |
>
> #### STEP 3B-2. Check the cab harness for a short circuit from pin to pin.
>
> | **Conditions:** Disconnect the 14-pin connector. Disconnect the ICON™ lamp or LED. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin J in the 14-pin pass-through connector, cab harness side, to all other pins except pin K in the connector, cab harness side. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms Repair or replace the ICON™ engine harness. Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. | 4A |
> | Repair or replace the ICON™ cab harness Repair the cab harness. Refer to Procedure 019-207. Replace the cab harness. Refer to Procedure 019-305. | 4A |  |
>
> #### STEP 3C. Check the complete harness for a short circuit to the battery.
>
> | **Conditions:** Disconnect the ICON™ idle control module A and B connectors from the ICON™ idle control module. NOTE: All other components must be connected. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the voltage from pin 5 of the ICON™ idle control module A harness connector to engine block ground. Measure the voltage from pin 6 of the ICON™ idle control module A harness connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For multimeter usage techniques, refer to Multimeter Usage, Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | Less than 0.5 VDC Replace the ICON™ idle control module. Refer to Procedure [[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Repair Complete |
> |  | 3C-1 |  |
>
> #### STEP 3C-1. Identify whether the ICON™ system is an Aftermarket or an OEM.
>
> | **Conditions:** None |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Refer to Procedure [[97-209-017 — ICON™ Idle Control System\|209-017]]. | ICON™ system is Aftermarket | 3C-2 |
> | Check the OEM wiring harness for a short circuit to battery in the lamp output circuit. | 4A |  |
>
> #### STEP 3C-2. Check the cab harness for a short circuit to the battery.
>
> | **Conditions:** Disconnect the 14-pin connector. NOTE: All other components must be connected. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the voltage from pin J in the 14-pin pass-through connector, cab harness side, to engine block ground. Measure the voltage from pin D in the 14-pin pass-through connector, cab harness side, to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For multimeter usage techniques, refer to Multimeter Usage, Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | Less than 0.5 VDC Repair or replace the ICON™ engine harness. Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. | 4A |
> | Repair or replace the ICON™ cab harness Repair the cab harness. Refer to Procedure 019-207. Replace the cab harness. Refer to Procedure 019-305. | 4A |  |
>
> ### STEP 4. Clear the fault code.
>
> #### STEP 4A. Disable the fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Cycle the keyswitch to verify the fault code is inactive. | Fault Code 198 cleared | Repair complete |
> | Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
