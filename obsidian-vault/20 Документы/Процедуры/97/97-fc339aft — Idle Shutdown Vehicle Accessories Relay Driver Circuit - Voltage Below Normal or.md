---
type: "Процедура"
doc: "97-fc339aft"
title_en: "Idle Shutdown Vehicle Accessories Relay Driver Circuit - Voltage Below Normal or Shorted to Low Source"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc339aft.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc339aft.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
  - "перевод/машинный"
---

# Idle Shutdown Vehicle Accessories Relay Driver Circuit - Voltage Below Normal or Shorted to Low Source

> [!abstract] Процедура · `97-fc339aft`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-10-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc339aft.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc339aft.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 339 (Послепродажное и OEM)

### Idle Shutdown Vehicle Accessories Relay Driver Circuit - напряжение ниже нормального или короткое до низкого

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 339 P(P): СПН: ФМИ: Лампа: СТО: | Idle Shutdown Vehicle Accessories Relay Driver Circuit - напряжение ниже нормального или короткое до низкого источника. Менее 6 VDC, обнаруженных на выходной цепи реле зажигания шины, когда высокое напряжение ожидалось модулем управления холостым ходом ICONTM. | Система ICONTM будет отключена. Включено только обязательное отключение. Двигатель можно запускать нормально. Постоянная мощность будет находиться в цепи зажигания переключателя зажигания. |

![[19802960.png]]

### Описание цепи

Реле зажигания управляет цепями зажигания, питающими элементы управления кондиционированием отопления / воздуха и другое оборудование, подключенное к реле 1 зажигания и реле 2 шины зажигания. Эти реле управляются положительным (+) сигналом реле зажигания от контакта 4 разъема ICONTM B. Вышеупомянутая схема может варьироваться, например, разъем или штифты, в зависимости от марки или модели транспортного средства. Установки OEM могут обеспечить взаимодействие между модулем управления холостым ходом и другими устройствами ICONTM.

### Расположение компонента

Реле шины зажигания обычно расположено под приборной панелью внутри кабины транспортного средства. Модуль ICONTM может быть расположен в другом месте в зависимости от применения транспортного средства.

### Практические замечания

Этот дефект обычно указывает на короткое замыкание на землю или открытую цепь от модуля управления ICONTM холостого хода B разъема контакта 4, реле зажигания положительное (+). Реле зажигания положительное (+) (контакт 4) выводит 12 VDC для открытия реле шины зажигания 1 и 2, когда система ICONTM приводит в действие транспортное средство и должна отключить питание, идущее к кабине. Реле 1 и 2 зажигания обычно закрываются, когда не применяется питание.

Система ICONTM может отображать только текущий активный код неисправности. Если одновременно активируется более одного кода неисправности, система ICON выдает наиболее приоритетную ошибку. После того, как ошибка была исправлена, будет выброшена следующая активная ошибка.

**Примечание: **Электронная система ICONTM может отображать более одного активного и неактивного кода неисправности одновременно.

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
>

**Для уменьшения возможности повреждения нового модуля управления бездействия ICONTM необходимо изучить все другие коды активных неисправностей до замены модуля управления бездействия ICONTM**.

> [!warning] ОСТОРОЖНО
>

**Для уменьшения возможности повреждения штифта и проводов жгута проводов используйте при проведении измерений следующий испытательный щуп: Номер детали 3822758 - пробный щуп типа пробоотвода Deutsch/AMP/Metri-Pack Номер детали 3822917 - пробный щуп типа разъема Deutsch/AMP/Metri-Pack.**

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Считайте коды неисправностей. |  |
|  | **STEP 1A.** Прочитайте коды неисправностей с помощью инструментария электронного сервиса ICONTM или с помощью функции вспышки неисправностей. | Код 339 неактивен |
| ШАГ 2. | Проверьте реле шины зажигания. |  |
|  | **ШАГ 2А.** Осмотрите штифты реле (бусов) зажигания. | Никаких поврежденных контактов |
|  | **STEP 2B.** Проверьте сопротивление катушки реле зажигания шины. | 70-100 Ом |
| ШАГ 3. | Проверьте проводные ремни ICONTM. |  |
|  | **STEP 3A.** Проверить контакты разъема модуля управления ICONTM с проводкой двигателя, кабины и проводов ICONTM. | Никаких поврежденных контактов |
|  | **STEP 3B.** Проверьте полную проводку ремня для короткого замыкания от пин-кодов до пин-кодов. | Более 100 тыс. ом |
|  | **STEP 3B-1.** Определите, является ли система ICONTM послепродажным обслуживанием. | Система ICONTM является системой Aftermarket. |
|  | **STEP 3B-2.** Проверьте электропроводку кабины на короткое замыкание от пин-кодов до пин-кодов. | Более 100 тыс. ом |
|  | **STEP 3C.** Проверьте полную проводку ремня для короткого замыкания на землю. | Более 100 тыс. ом |
|  | **STEP 3C-1.** Определите, является ли система ICONTM послепродажным обслуживанием. | Система ICONTM является системой Aftermarket. |
|  | **STEP 3C-2.** Проверьте электропроводку кабины на короткое замыкание на землю. | Более 100 тыс. ом |
| ШАГ 4. | Очистите код ошибки. |  |
|  | **STEP 4A.** Отключить код ошибки. | Код 339 ошибки удален |

### ШАГ 1. Считайте коды неисправностей.

#### ШАГ 1A. Прочитайте коды неисправностей с помощью инструментария электронного сервиса ICONTM или с помощью функции вспышки неисправностей.

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите электронный сервис ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте реле шины зажигания с помощью служебной оснастки. Включив переключатель зажигания, инициируйте кнопку Ignition Bus Relay Test и определите, отключит ли реле вентиляторы. | Код 339 неактивен. Неактивные или прерывистые коды ошибок, процедура[[99-019-362 — Inactive or Intermittent Fault Code\|019-362]]. | 4А |
|  | 2А |  |

### ШАГ 2. Проверьте реле шины зажигания.

#### ШАГ 2A. Осмотрите буксиры реле (бусов) зажигания.

| **Условия:** Выключите замок зажигания. Отсоедините реле (ретрансляторы) шины зажигания от электропроводки кабины. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Корродированные штифты Бент или сломанные штифты Отталкивание назад или расширенные штифты Проводная изоляция Повреждение Влажность в или на разъем Пропавшие или поврежденные соединительные штифты Коннекторная оболочка разбитая Грязь или мусор в или на разъемных контактах. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 2В |
| Заменить реле(ы). Смывать грязь, мусор или влагу с реле с помощью электрического контактного очистителя, номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Заменить реле (ретрансляторы) шины зажигания. См. процедуру 019-301. | 4А |  |

#### ШАГ 2B. Проверьте сопротивление реле зажигания шины.

| **Условия:** Выключите замок зажигания. Отсоедините реле (ретрансляторы) шины зажигания от электропроводки кабины. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление от контакта 85 до контакта 86 реле (реле). См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | 70-100 Ом | 3А |
| Заменить реле(ы). См. процедуру[[97-019-301 — Ignition Bus Relay 1 and 2\|019-301]]. | 4А |  |

### ШАГ 3. Проверьте проводные ремни ICONTM.

#### ШАГ 3A. Осмотрите контакты разъема проводов двигателя ICONTM, проводов кабины и коннектора модуля управления ICONTM.

| **Условия:** Выключите замок зажигания. Отсоедините разъем B модуля управления ICONTM от модуля управления ICONTM. Отсоедините 14-контактный проходной разъем на брандмауэре автомобиля. Отсоедините реле (ретрансляторы) шины зажигания от электропроводки кабины. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Корродированные штифты Бент или сломанные штифты Отталкивание назад или расширенные штифты Проводная изоляция Повреждение Влажность в или на разъем Пропавшие или поврежденные соединительные штифты Коннекторная оболочка разбитая Грязь или мусор в или на разъемных контактах. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 3B |
| Ремонт поврежденных контактов Смывать грязь, мусор или влагу из контактов разъема с помощью электрического контактного очистителя, Номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт ремня электропроводки двигателя ICONTM. См. процедуру 019-206 или 019-207. Заменить электропроводку двигателя ICONTM. См. процедуру 019-043. Ремонт проводов такси. См. процедуру 019-205 или 019-207. Замените проводку кабины. См. процедуру 019-305. Заменить модуль управления ICONTM idle. См. процедуру 019-358. По мере необходимости ремонтировать или заменять электропроводку OEM. | 4А |  |

#### ШАГ 3B. Проверьте полную проводку ремня для короткого замыкания от пин-кодов до пин-кодов.

| **Условия:** Выключите замок зажигания. Отсоедините разъемы ICONTM Idle Control Module A и B от модуля ICONTM idle Control. Отсоедините реле (ретрансляторы) шины зажигания от электропроводки кабины. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление контакта 4 в неработающем модуле управления ICONTM B проводов жгута разъёма со всеми другими штифтами в A и B проводов жгута разъема. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 100 тыс. ом | 3C |
|  | 3В-1-1 |  |

#### ШАГ 3B-1. Определите, является ли система ICONTM послепродажным обслуживанием.

| **Условия: **Ни одно |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| См. процедуру[[97-209-017 — ICON™ Idle Control System\|209-017]]. | Система ICONTM является системой Aftermarket. | 3В-2-2 |
| Проверьте штифт OEM-проводов, чтобы зажать короткое время в цепи реле шины зажигания. | 4А |  |

#### ШАГ 3B-2. Проверьте электропроводку кабины для короткого замыкания от пин-кодов до пин-кодов.

| **Условия:** Выключите замок зажигания. Отключите 14-контактный проходной разъем. Отсоедините реле (ретрансляторы) шины зажигания от электропроводки кабины. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта F 14-контактной кабины проводов ремня, кабины проводов ремня, ко всем другим штифтам в разъеме. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 100 000 Ом Ремонт или замена ремня электропроводки двигателя ICONTM Ремонт ремня электропроводки двигателя ICONTM. См. процедуру 019-206 или 019-207. Заменить электропроводку двигателя ICONTM. См. процедуру 019-043. | 4А |
| Ремонт или замена кабины ICONTM ремень проводов кабины. См. процедуру 019-207. Замените проводку кабины. См. процедуру 019-305. | 4А |  |

#### ШАГ 3C. Проверьте полную проводку ремня для короткого замыкания на землю.

| **Условия:** Выключите замок зажигания. Отсоедините разъем B модуля управления ICONTM от модуля управления ICONTM. Отсоедините реле (ретрансляторы) шины зажигания от электропроводки кабины. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление от контакта 4 неработающего модуля управления ICONTM B проводов ремня разъема к заземлению блока двигателя. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 100k Ом Заменить модуль управления ICONTM. См. процедуру[[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Ремонт завершён |
|  | 3С-1-1 |  |

#### ШАГ 3C-1. Определите, является ли система ICONTM послепродажным обслуживанием.

| **Условия: **Ни одно |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| См. процедуру[[97-209-017 — ICON™ Idle Control System\|209-017]]. | Система ICONTM является системой Aftermarket. | 3С-2 |
| Проверьте штифт OEM-проводов, чтобы зажать короткий к земле в цепи реле зажигания шины. | 4А |  |

#### ШАГ 3C-2. Проверьте электропроводку кабины для короткого замыкания на землю.

| **Условия:** Выключите замок зажигания. Отключите 14-контактный проходной разъем. Отсоедините реле (ретрансляторы) шины зажигания от электропроводки кабины. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта F 14-контактного разъёма кабины, стороны кабины, к заземлению блока двигателя. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 100 000 Ом Ремонт или замена ремня электропроводки двигателя ICONTM Ремонт ремня электропроводки двигателя ICONTM. См. процедуру 019-206 или 019-207. Заменить электропроводку двигателя ICONTM. См. процедуру 019-043. | 4А |
| Ремонт или замена кабины ICONTM ремень проводов кабины. См. процедуру 019-207. Замените проводку кабины. См. процедуру 019-305. | 4А |  |

### ШАГ 4. Очистите код ошибки.

#### ШАГ 4A. Отключите код неисправности.

| **Условия: **Соединить все компоненты. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Цикл переключателя зажигания для проверки кода неисправности неактивен. | Код 339 ошибки удален | Ремонт завершён |
| Устранение неполадок с оставшимися активными кодами неисправностей. | Соответствующие диаграммы устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 339 (Aftermarket and OEM)
>
> ### Idle Shutdown Vehicle Accessories Relay Driver Circuit - Voltage Below Normal or Shorted to Low Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 339 PID(P): SPN: FMI: Lamp: SRT: | Idle Shutdown Vehicle Accessories Relay Driver Circuit - Voltage Below Normal or Shorted to Low Source. Less than 6 VDC detected at the ignition bus relay output circuit when high voltage was expected by the ICON™ idle control module. | The ICON™ system will be disabled. **Only** mandatory shutdown will be enabled. Engine can be started normally. Constant power will be at the keyswitch ignition circuit. |
>
> ### Circuit Description
>
> The ignition bus relay controls ignition circuits powering the heating/air conditioning controls and other equipment connected to the ignition bus relay 1 and ignition bus relay 2. These relays are controlled by the ignition relay positive (+) signal from the ICON™ B connector pin 4. The above circuit diagram can vary, such as connector or pins, depending on the vehicle make or model. OEM installations can possibly provide the harnessing between the idle control module and other ICON™ devices.
>
> ### Component Location
>
> The ignition bus relay is typically located under the dash inside the vehicle cab. The ICON™ module can be located in a different location depending on the vehicle application.
>
> ### Shoptalk
>
> This fault typically indicates a short circuit to ground or an open circuit from the ICON™ idle control module B connector pin 4, ignition relay positive (+). Ignition relay positive (+) (pin 4) outputs 12 VDC to open the ignition bus 1 and 2 relays when the ICON™ system has powered down the vehicle and needs to disconnect power going to the cab circuit. The ignition bus 1 and 2 relays are normally closed when no power is applied.
>
> The ICON™ system can display **only** the present active fault code. If more than one fault code is active at the same time, the ICON system flashes out the highest priority fault. After the fault has been corrected then the next active fault will be flashed out.
>
> **Note:** The ICON™ electronic service tool can display more than one active and or inactive fault codes at the same time.
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
>
> **To reduce the possibility of damaging a new ICON™ idle control module, all other active fault codes must be investigated prior to replacing the ICON™ idle control module.**
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
> |  | **STEP 1A.** Read the fault codes with the ICON™ electronic service tool or by using the fault flashout feature. | Fault Code 339 inactive |
> | STEP 2. | Check the ignition bus relay. |  |
> |  | **STEP 2A.** Inspect the ignition bus relay(s) pins. | No damaged pins |
> |  | **STEP 2B.** Check the ignition bus relay coil resistance. | 70 to 100 ohms |
> | STEP 3. | Check the ICON™ harnesses. |  |
> |  | **STEP 3A.** Inspect the ICON™ engine harness, cab harness, and ICON™ idle control module connector pins. | No damaged pins |
> |  | **STEP 3B.** Check the complete harness for a short circuit from pin to pin. | More than 100k ohms |
> |  | **STEP 3B-1.** Identify whether the ICON™ system is an Aftermarket. | ICON™ system is Aftermarket |
> |  | **STEP 3B-2.** Check the cab harness for a short circuit from pin to pin. | More than 100k ohms |
> |  | **STEP 3C.** Check the complete harness for a short circuit to ground. | More than 100k ohms |
> |  | **STEP 3C-1.** Identify whether the ICON™ system is an Aftermarket. | ICON™ system is Aftermarket |
> |  | **STEP 3C-2.** Check the cab harness for a short circuit to ground. | More than 100k ohms |
> | STEP 4. | Clear the fault code. |  |
> |  | **STEP 4A.** Disable the fault code. | Fault Code 339 cleared |
>
> ### STEP 1. Read the fault codes.
>
> #### STEP 1A. Read the fault codes with the ICON™ electronic service tool or by using the fault flashout feature.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect the ICON™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the ignition bus relay with the service tool. With the keyswitch ON, initiate the Ignition Bus Relay Test button and determine if the relay will turn the fans OFF. | Fault Code 339 inactive. Refer to Inactive or Intermittent Fault Codes, Procedure [[99-019-362 — Inactive or Intermittent Fault Code\|019-362]]. | 4A |
> |  | 2A |  |
>
> ### STEP 2. Check the ignition bus relay.
>
> #### STEP 2A. Inspect the ignition bus relay(s) pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ignition bus relay(s) from the cab harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 2B |
> | Replace the relay(s). Flush the dirt, debris, or moisture from the relay pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Replace the ignition bus relay(s). Refer to Procedure 019-301. | 4A |  |
>
> #### STEP 2B. Check the ignition bus relay coil resistance.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ignition bus relay(s) from the cab harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 85 to pin 86 of the relay(s). Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | 70 to 100 ohms | 3A |
> | Replace the relay(s). Refer to Procedure [[97-019-301 — Ignition Bus Relay 1 and 2\|019-301]]. | 4A |  |
>
> ### STEP 3. Check the ICON™ harnesses.
>
> #### STEP 3A. Inspect the ICON™ engine harness, cab harness, and ICON™ idle control module connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module B connector from the ICON™ idle control module. Disconnect the 14-pin pass-through connector at the vehicle firewall. Disconnect the ignition bus relay(s) from the cab harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 3B |
> | Repair the damaged pins Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair the cab harness. Refer to Procedure 019-205 or 019-207. Replace the cab harness. Refer to Procedure 019-305. Replace the ICON™ idle control module. Refer to Procedure 019-358. Repair or replace the OEM wiring harness as necessary. | 4A |  |
>
> #### STEP 3B. Check the complete harness for a short circuit from pin to pin.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module A and B connectors from the ICON™ idle control module. Disconnect the ignition bus relay(s) from the cab harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 4 in the ICON™ idle control module B harness connector to all other pins in the A and B harness connectors. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 3C |
> |  | 3B-1 |  |
>
> #### STEP 3B-1. Identify whether the ICON™ system is an Aftermarket.
>
> | **Conditions:** None |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Refer to Procedure [[97-209-017 — ICON™ Idle Control System\|209-017]]. | ICON™ system is Aftermarket | 3B-2 |
> | Check the OEM wiring harness pin to pin for a short in the ignition bus relay circuit. | 4A |  |
>
> #### STEP 3B-2. Check the cab harness for a short circuit from pin to pin.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the 14-pin pass-through connector. Disconnect the ignition bus relay(s) from the cab harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin F of the 14-pin cab harness, cab harness side, to all other pins in the connector. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms Repair or replace the ICON™ engine harness Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. | 4A |
> | Repair or replace the ICON™ cab harness Repair the cab harness. Refer to Procedure 019-207. Replace the cab harness. Refer to Procedure 019-305. | 4A |  |
>
> #### STEP 3C. Check the complete harness for a short circuit to ground.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module B connector from the ICON™ idle control module. Disconnect the ignition bus relay(s) from the cab harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 4 of the ICON™ idle control module B harness connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms Replace the ICON™ idle control module. Refer to Procedure [[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Repair Complete |
> |  | 3C-1 |  |
>
> #### STEP 3C-1. Identify whether the ICON™ system is an Aftermarket.
>
> | **Conditions:** None |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Refer to Procedure [[97-209-017 — ICON™ Idle Control System\|209-017]]. | ICON™ system is Aftermarket | 3C-2 |
> | Check the OEM wiring harness pin to pin for a short to ground in the ignition bus relay circuit. | 4A |  |
>
> #### STEP 3C-2. Check the cab harness for a short circuit to ground.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the 14-pin pass-through connector. Disconnect the ignition bus relay(s) from the cab harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin F of the 14-pin cab harness connector, cab harness side, to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms Repair or replace the ICON™ engine harness Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. | 4A |
> | Repair or replace the ICON™ cab harness Repair the cab harness. Refer to Procedure 019-207. Replace the cab harness. Refer to Procedure 019-305. | 4A |  |
>
> ### STEP 4. Clear the fault code.
>
> #### STEP 4A. Disable the fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Cycle the keyswitch to verify the fault code is inactive. | Fault Code 339 cleared | Repair complete |
> | Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
