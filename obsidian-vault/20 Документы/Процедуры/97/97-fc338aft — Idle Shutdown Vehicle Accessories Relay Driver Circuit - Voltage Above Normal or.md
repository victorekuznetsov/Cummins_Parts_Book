---
type: "Процедура"
doc: "97-fc338aft"
title_en: "Idle Shutdown Vehicle Accessories Relay Driver Circuit - Voltage Above Normal or Shorted to High Source"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc338aft.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc338aft.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
  - "перевод/машинный"
---

# Idle Shutdown Vehicle Accessories Relay Driver Circuit - Voltage Above Normal or Shorted to High Source

> [!abstract] Процедура · `97-fc338aft`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-10-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc338aft.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc338aft.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 338 (Послепродажное и OEM)

### Idle Shutdown Vehicle Accessories Relay Driver Circuit - напряжение выше нормального или короткое до высокого источника

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 338 P(P): СПН: ФМИ: Лампа: СТО: | Idle Shutdown Vehicle Accessories Relay Driver Circuit - напряжение выше нормального или короткое до высокого источника. Высокое напряжение, обнаруженное на выходной цепи шины зажигания (положительное (+) реле зажигания), когда низкое напряжение ожидалось модулем управления холостым зажиганием ICONTM. | Система ICONTM будет отключена. Включено только обязательное отключение. Двигатель можно запускать нормально. Нет питания в цепи зажигания переключателя зажигания. |

![[19802960.png]]

### Описание цепи

Реле зажигания управляет цепями зажигания, питающими элементы управления кондиционированием отопления / воздуха и другое оборудование, подключенное к реле 1 зажигания и реле 2 шины зажигания. Эти выходные реле управляются положительным (+) сигналом реле зажигания от контакта 4 коннектора B модуля управления холостым зажиганием ICONTM. Некоторые OEM-установки, возможно, не будут иметь вторую реле шины зажигания. Вышеупомянутая схема может варьироваться, например, разъем или штифты, в зависимости от марки или модели транспортного средства. Установки OEM могут обеспечить взаимодействие между модулем управления холостым ходом и другими устройствами ICONTM.

### Расположение компонента

Реле шины зажигания обычно расположено под приборной панелью внутри кабины транспортного средства.

Модуль ICONTM может быть расположен в другом месте в зависимости от применения транспортного средства.

### Практические замечания

Этот недостаток обычно указывает на короткое замыкание от коннектора 4 коннектора B модуля управления холостого хода ICONTM (ретранслятор зажигания положительный (+)) выход к напряжению батареи. Реле зажигания положительное (+) (контакт 4) выводит 12 VDC для открытия реле шины зажигания 1 и 2, когда система ICONTM приводит в действие транспортное средство и нуждается в отключении питания, идущего к кабинным схемам. Реле 1 и 2 зажигания обычно закрываются, когда не применяется питание.

Система ICONTM может отображать только текущий активный код неисправности. Если одновременно активируется более одного отказа, система ICONTM выдает наиболее приоритетный недостаток. После того, как ошибка была исправлена, будет выброшена следующая активная ошибка.

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
|  | **STEP 1A.** Используйте функцию вспышки неисправности или инструмент электронного сервиса ICONTM для считывания кодов неисправностей. | Код 338 неактивен |
| ШАГ 2. | Проверьте реле шины зажигания. |  |
|  | **ШАГ 2А.** Проверить контакты ретранслятора шины зажигания. | Никаких поврежденных контактов |
|  | **STEP 2B.** Проверьте сопротивление катушки реле зажигания шины. | 70-100 Ом |
|  | **STEP 2C** Проверьте короткое замыкание в реле шины зажигания. | Более 100 тыс. ом |
| ШАГ 3. | Проверьте проводные ремни ICONTM. |  |
|  | **STEP 3A.** Проверить контакты разъема модуля управления ICONTM с проводкой двигателя, кабины и проводов ICONTM. | Никаких поврежденных контактов |
|  | **STEP 3B.** Проверьте полную проводку ремня для короткого замыкания от пин-кодов до пин-кодов. | Более 100 тыс. ом |
|  | **STEP 3B-1.** Определите, является ли система ICONTM послепродажным или OEM-производителем. | Система ICONTM является системой Aftermarket. |
|  | **STEP 3B-2.** Проверьте электропроводку кабины на короткое замыкание от пин-кодов до пин-кодов. | Более 100 тыс. ом |
|  | **STEP 3C.** Проверьте полную проводку ремня для короткого замыкания к батарее. | Менее 0,5 VDC |
|  | **STEP 3C-1.** Определите, является ли система ICONTM послепродажным или OEM-производителем. | Система ICONTM является системой Aftermarket. |
|  | **STEP 3C-2.** Проверьте электропроводку кабины на короткое замыкание к батарее. | Менее 0,5 VDC |
| ШАГ 4. | Очистите код ошибки. |  |
|  | **STEP 4A.** Отключить код ошибки. | Код 338 неисправности обезврежен |

### ШАГ 1. Считайте коды неисправностей.

#### ШАГ 1A. Используйте функцию вспышки неисправности или инструмент электронного сервиса ICONTM для считывания кодов неисправностей.

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите электронный сервис ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Используйте сервисную оснастку для проверки реле шины зажигания. Инициировать кнопку Ignition Bus Relay Test с включенным переключателем зажигания и определить, будет ли реле выключать вентиляторы. | Код 338 неактивен. Неактивные или прерывистые коды ошибок, процедура[[99-019-362 — Inactive or Intermittent Fault Code\|019-362]]. | 4А |
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
| Измерить сопротивление от контакта 85 до контакта 86 реле (реле). См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | 70-100 Ом | 2C |
| Заменить реле(ы). См. процедуру[[97-019-301 — Ignition Bus Relay 1 and 2\|019-301]]. | 4А |  |

#### ШАГ 2C. Проверьте короткое замыкание в реле шины зажигания.

| **Условия:** Выключите замок зажигания. Отсоедините реле (ретрансляторы) шины зажигания от электропроводки кабины. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление от контакта 85 реле (реле) шины зажигания до контактов 30, 87 и 87А реле (реле). См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 100 тыс. ом | 3А |
| Заменить реле(ы). См. процедуру[[97-019-301 — Ignition Bus Relay 1 and 2\|019-301]]. | 4А |  |

### ШАГ 3. Проверьте проводные ремни ICONTM.

#### ШАГ 3A. Осмотрите контакты разъема проводов двигателя ICONTM, проводов кабины и коннектора модуля управления ICONTM.

| **Условия:** Выключите замок зажигания. Отсоедините разъем B модуля управления ICONTM от модуля управления ICONTM. Отключите любые другие разъемы для системы ICONTM, чтобы проверить контакты разъема. Отсоедините проводку кабины от реле (реле) шины зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Корродированные штифты Бент или сломанные штифты Отталкивание назад или расширенные штифты Проводная изоляция Повреждение Влажность в или на разъем Пропавшие или поврежденные соединительные штифты Коннекторная оболочка разбитая Грязь или мусор в или на разъемных контактах. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 3B |
| Ремонт поврежденных контактов. Промывайте грязь, мусор или влагу от контактов разъема с помощью электрического контактного очистителя, Номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт ремня электропроводки двигателя ICONTM. См. процедуру 019-206 или 019-207. Заменить электропроводку двигателя ICONTM. См. процедуру 019-043. Ремонт проводов такси. См. процедуру 019-211 или 019-207. Замените проводку кабины. См. процедуру 019-305. Заменить модуль управления ICONTM idle. См. процедуру 019-358. По мере необходимости ремонтировать или заменять электропроводку OEM. | 4А |  |

#### ШАГ 3B. Проверьте полную проводку ремня для короткого замыкания от пин-кодов до пин-кодов.

| **Условия:** Выключите замок зажигания. Отсоедините разъем B модуля управления ICONTM от модуля управления ICONTM. Отсоедините реле (ретрансляторы) шины зажигания от электропроводки кабины. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта 4 в неработающем модуле управления ICONTM B проводов жгута разъёма ко всем другим штифтам в разъеме. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 100 тыс. ом | 3C |
|  | 3В-1-1 |  |

#### ШАГ 3B-1. Определите, является ли система ICONTM послепродажным или OEM-производителем.

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

#### ШАГ 3C. Проверьте полную проводку ремня для короткого замыкания к батарее.

| **Условия:** Отсоединить разъем B модуля управления ICONTM от модуля управления ICONTM. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте напряжение от контакта 4 модуля управления ICONTM холостого хода B проводов ремня разъема к заземлению блока двигателя. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для многометровых методов использования, обратитесь к процедуре[[99-019-359 — Multimeter Usage\|019-359]]. | Менее 0,5 VDC Заменить модуль управления ICONTM. См. процедуру[[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Ремонт завершён |
|  | 3С-1-1 |  |

#### ШАГ 3C-1. Определите, является ли система ICONTM послепродажным или OEM-производителем.

| **Условия: **Ни одно |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| См. процедуру[[97-209-017 — ICON™ Idle Control System\|209-017]]. | Система ICONTM является системой Aftermarket. | 3С-2 |
| Проверьте штифт OEM-проводов, чтобы зажать батарею в цепи ретрансляции шины зажигания. | 4А |  |

#### ШАГ 3C-2. Проверьте электропроводку кабины для короткого замыкания к батарее.

| **Условия:** Включить переключатель зажигания. Отключите 14-контактный проходной разъем. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте напряжение от контакта F 14-контактной проводов кабины, стороны проводов кабины, до заземления блока двигателя. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для многометровых методов использования, обратитесь к процедуре[[99-019-359 — Multimeter Usage\|019-359]]. | Менее 0,5 VDC ремонт или замена ICONTM проводка двигателя ремень репарации двигателя ICONTM ремень проводов двигателя. См. процедуру 019-206 или 019-207. Заменить электропроводку двигателя ICONTM. См. процедуру 019-043. | 4А |
| Ремонт или замена кабины ICONTM ремень проводов кабины. См. процедуру 019-207. Замените проводку кабины. См. процедуру 019-305. | 4А |  |

### ШАГ 4. Очистите код ошибки.

#### ШАГ 4A. Отключите код неисправности.

| **Условия: **Соединить все компоненты. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Цикл переключателя зажигания для проверки кода неисправности неактивен. | Код 338 неисправности обезврежен | Ремонт завершён |
| Устранение неполадок с оставшимися активными кодами неисправностей. | Соответствующие диаграммы устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 338 (Aftermarket and OEM)
>
> ### Idle Shutdown Vehicle Accessories Relay Driver Circuit - Voltage Above Normal or Shorted to High Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 338 PID(P): SPN: FMI: Lamp: SRT: | Idle Shutdown Vehicle Accessories Relay Driver Circuit - Voltage Above Normal or Shorted to High Source. High voltage detected at the ignition bus relay output circuit (ignition relay positive (+)) when low voltage was expected by the ICON™ idle control module. | The ICON™ system will be disabled. **Only** mandatory shutdown will be enabled. Engine can be started normally. No power to the keyswitch ignition circuit. |
>
> ### Circuit Description
>
> The ignition bus relay controls ignition circuits powering the heating/air conditioning controls and other equipment connected to the ignition bus relay 1 and ignition bus relay 2. These outputting relays are controlled by the ignition relay positive (+) signal from the ICON™ idle control module B connector pin 4. Some OEM installations will possibly **not** have the second ignition bus relay. The above circuit diagram can vary, such as connector or pins, depending on the vehicle make or model. OEM installations can possibly provide the harnessing between the idle control module and other ICON™ devices.
>
> ### Component Location
>
> The ignition bus relay is typically located under the dash inside the vehicle cab.
>
> The ICON™ module can be located in a different location depending on the vehicle application.
>
> ### Shoptalk
>
> This fault typically indicates a short circuit from the ICON™ idle control module B connector pin 4 (ignition relay positive (+)) output to battery voltage. Ignition relay positive (+) (pin 4) outputs 12 VDC to open the ignition bus 1 and 2 relays when the ICON™ system has powered the vehicle down and needs to disconnect power going to the cab circuits. The ignition bus 1 and 2 relays are normally closed when no power is applied.
>
> The ICON™ system can display **only** the present active fault code. If more than one fault is active at the same time, the ICON™ system flashes out the highest priority fault. After the fault has been corrected then the next active fault will be flashed out.
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
> |  | **STEP 1A.** Use the fault flashout feature or the ICON™ electronic service tool to read the fault codes. | Fault Code 338 inactive |
> | STEP 2. | Check the ignition bus relay. |  |
> |  | **STEP 2A.** Inspect the ignition bus relay connector pins. | No damaged pins |
> |  | **STEP 2B.** Check the ignition bus relay coil resistance. | 70 to 100 ohms |
> |  | **STEP 2C.** Check for a short circuit in the ignition bus relay. | More than 100k ohms |
> | STEP 3. | Check the ICON™ harnesses. |  |
> |  | **STEP 3A.** Inspect the ICON™ engine harness, cab harness, and ICON™ idle control module connector pins. | No damaged pins |
> |  | **STEP 3B.** Check the complete harness for a short circuit from pin to pin. | More than 100k ohms |
> |  | **STEP 3B-1.** Identify whether the ICON™ system is an Aftermarket or an OEM. | ICON™ system is Aftermarket |
> |  | **STEP 3B-2.** Check the cab harness for a short circuit from pin to pin. | More than 100k ohms |
> |  | **STEP 3C.** Check the complete harness for a short circuit to the battery. | Less than 0.5 VDC |
> |  | **STEP 3C-1.** Identify whether the ICON™ system is an Aftermarket or an OEM. | ICON™ system is Aftermarket |
> |  | **STEP 3C-2.** Check the cab harness for a short circuit to the battery. | Less than 0.5 VDC |
> | STEP 4. | Clear the fault code. |  |
> |  | **STEP 4A.** Disable the fault code. | Fault Code 338 cleared |
>
> ### STEP 1. Read the fault codes.
>
> #### STEP 1A. Use the fault flashout feature or the ICON™ electronic service tool to read the fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect the ICON™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Use the service tool to check the ignition bus relay. Initiate the Ignition Bus Relay Test button with the keyswitch ON and determine if the relay will turn the fans OFF. | Fault Code 338 inactive. Refer to Inactive or Intermittent Fault Codes, Procedure [[99-019-362 — Inactive or Intermittent Fault Code\|019-362]]. | 4A |
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
> | Measure the resistance from pin 85 to pin 86 of the relay(s). Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | 70 to 100 ohms | 2C |
> | Replace the relay(s). Refer to Procedure [[97-019-301 — Ignition Bus Relay 1 and 2\|019-301]]. | 4A |  |
>
> #### STEP 2C. Check for a short circuit in the ignition bus relay.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ignition bus relay(s) from the cab harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 85 of the ignition bus relay(s) to pins 30, 87, and 87A of the relay(s). Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 3A |
> | Replace the relay(s). Refer to Procedure [[97-019-301 — Ignition Bus Relay 1 and 2\|019-301]]. | 4A |  |
>
> ### STEP 3. Check the ICON™ harnesses.
>
> #### STEP 3A. Inspect the ICON™ engine harness, cab harness, and ICON™ idle control module connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module B connector from the ICON™ idle control module. Disconnect any other connectors for the ICON™ system in order to check the connector pins. Disconnect the cab harness from the ignition bus relay(s). |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 3B |
> | Repair the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair the cab harness. Refer to Procedure 019-211 or 019-207. Replace the cab harness. Refer to Procedure 019-305. Replace the ICON™ idle control module. Refer to Procedure 019-358. Repair or replace the OEM wiring harness as necessary. | 4A |  |
>
> #### STEP 3B. Check the complete harness for a short circuit from pin to pin.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module B connector from the ICON™ idle control module. Disconnect the ignition bus relay(s) from the cab harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 4 in the ICON™ idle control module B harness connector to all other pins in the connector. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 3C |
> |  | 3B-1 |  |
>
> #### STEP 3B-1. Identify whether the ICON™ system is an Aftermarket or an OEM.
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
> #### STEP 3C. Check the complete harness for a short circuit to the battery.
>
> | **Conditions:** Disconnect the ICON™ idle control module B connector from the ICON™ idle control module. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the voltage from pin 4 of the ICON™ idle control module B harness connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For multimeter usage techniques, refer to Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | Less than 0.5 VDC Replace the ICON™ idle control module. Refer to Procedure [[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Repair Complete |
> |  | 3C-1 |  |
>
> #### STEP 3C-1. Identify whether the ICON™ system is an Aftermarket or an OEM.
>
> | **Conditions:** None |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Refer to Procedure [[97-209-017 — ICON™ Idle Control System\|209-017]]. | ICON™ system is Aftermarket | 3C-2 |
> | Check the OEM wiring harness pin to pin for a short to battery in the ignition bus relay circuit. | 4A |  |
>
> #### STEP 3C-2. Check the cab harness for a short circuit to the battery.
>
> | **Conditions:** Turn keyswitch ON. Disconnect the 14-pin pass-through connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the voltage from pin F of the 14-pin cab harness, cab harness side, to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For multimeter usage techniques, refer to Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | Less than 0.5 VDC Repair or replace the ICON™ engine harness Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. | 4A |
> | Repair or replace the ICON™ cab harness Repair the cab harness. Refer to Procedure 019-207. Replace the cab harness. Refer to Procedure 019-305. | 4A |  |
>
> ### STEP 4. Clear the fault code.
>
> #### STEP 4A. Disable the fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Cycle the keyswitch to verify the fault code is inactive. | Fault Code 338 cleared | Repair complete |
> | Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
