---
type: "Процедура"
doc: "97-fc767aft"
title_en: "Starter Interlock Safety Circuit - Voltage Below Normal or Shorted to Low Source"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc767aft.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc767aft.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
  - "перевод/машинный"
---

# Starter Interlock Safety Circuit - Voltage Below Normal or Shorted to Low Source

> [!abstract] Процедура · `97-fc767aft`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-10-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc767aft.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc767aft.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 767 (Послепродажное и OEM)

### Стартовая цепь безопасности блокировки - напряжение ниже нормального или короткое до низкого источника

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 767 PID(P): СПН: ФМИ: Лампа: СТО: | Стартовая цепь безопасности блокировки - напряжение ниже нормального или короткое до низкого источника. Менее 6-VDC импульса, обнаруженного на выходных цепях блокировки лампы, когда высокое напряжение ожидалось от модуля управления холостым режимом ICONTM. | Система ICONTM будет отключена. Включено только обязательное отключение. Двигатель запускается нормально. |

![[19803824.png]]

### Описание цепи

Вводная и выходная цепи блокировки обеспечивают питание лампы ICONTM и переключателей блокировки. Вышеупомянутая схема может варьироваться, например, разъем или штифты, в зависимости от марки или модели транспортного средства. Установки OEM могут обеспечить взаимодействие между модулем управления холостым ходом и другими устройствами ICONTM.

### Расположение компонента

Лампа ICONTM обычно расположена в кабине автомобиля на панели приборов. Переключатель стояночного тормоза обычно расположен за тире на линии сжатого воздуха стояночного тормоза. Выключатель наклона капота обычно расположен на капоте позади левого корпуса фар. Переключатель нейтрального положения расположен на верхней крышке трансмиссии вблизи переключения передач.

Модуль ICONTM может быть расположен в другом месте в зависимости от применения транспортного средства.

### Практические замечания

Эта ошибка указывает на короткое замыкание на землю. Эта схема выводит импульсно-модулируемое напряжение шириной импульса (PWM) при контакте 5 с коннектором A коннектора модуля управления ICONTM.

Система ICONTM может отображать только текущий активный код неисправности. Если одновременно активируется более одного кода неисправности, система ICONTM выдает наиболее приоритетную ошибку. После того, как ошибка была исправлена, будет выброшена следующая активная ошибка.

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
|  | **STEP 1A.** Используйте функцию вспышки неисправности или инструмент электронного сервиса ICONTM для считывания кодов неисправностей. | Код ошибки 767 |
| ШАГ 2. | Проверьте модуль управления ICONTM. |  |
|  | **STEP 2A.** Проверьте модуль управления ICONTM бездействия Разъем А для поврежденных контактов. | Никаких поврежденных контактов |
|  | **ШАГ 2В.** Проверьте переключатель наклона капота для короткого замыкания на землю. | Более 100 тыс. ом |
|  | **STEP 2C** Проверьте компоненты ICONTM на короткое замыкание на землю. | Более 100 тыс. ом |
| ШАГ 3. | Определите систему ICONTM. |  |
|  | **STEP 3A.** Определите, является ли система ICONTM послепродажным или OEM-производителем. | Система ICONTM является системой Aftermarket. |
| ШАГ 4. | Проверьте электропроводку двигателя ICONTM. |  |
|  | **STEP 4A.** Проверить контактные контакты 14-контактного разъема с помощью проводов двигателя ICONTM. | Никаких поврежденных контактов |
|  | **STEP 4B.** Проверьте упряжку для электропроводки двигателя ICONTM на короткое время до земли. | Более 100 тыс. ом |
| ШАГ 5. | Проверьте электропроводку ICONTM. |  |
|  | **STEP 5A.** Проверить кабину проводов ICONTM с помощью 14 контактов разъёма штифта. | Никаких поврежденных контактов |
|  | **STEP 5B.** Проверьте электропроводку кабины и переключатели для короткого замыкания на землю. | Более 100 тыс. ом |
|  | **STEP 5C** Проверьте лампу ICONTM на короткое замыкание на землю. | Более 100 тыс. ом |
|  | **STEP 5D.** Проверьте выключатель стояночного тормоза ICONTM на короткое замыкание на землю. | Более 100 тыс. ом |
| ШАГ 6. | Проверьте компоненты блокировки ICONTM. |  |
|  | **STEP 6A.** Проверьте нейтральный переключатель положения ICONTM. | Более 100 тыс. ом |
| ШАГ 7. | Очистите код ошибки. |  |
|  | **STEP 7A.** Отключить код ошибки. | Код ошибки 767 обезврежен |

### ШАГ 1. Считайте коды неисправностей.

#### ШАГ 1A. Используйте функцию вспышки неисправности или инструмент электронного сервиса ICONTM для считывания кодов неисправностей.

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите электронный сервис ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
|  | Код ошибки 767 активен. | 2А |
| Неактивные или прерывистые коды ошибок, процедура[[99-019-362 — Inactive or Intermittent Fault Code\|019-362]]. | 7А |  |

### ШАГ 2. Проверьте модуль управления ICONTM.

#### ШАГ 2A. Проверьте модуль управления ICONTM для неработающих контактов Разъем А для поврежденных контактов.

| **Условия:** Выключите замок зажигания. Отсоедините разъем модуля управления ICONTM Idle A от модуля управления ICONTM idle. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Корродированные штифты Бент или сломанные штифты Отталкивание назад или расширенные штифты Проводная изоляция Повреждение Влажность в или на разъем Пропавшие или поврежденные соединительные штифты Коннекторная оболочка разбитая Грязь или мусор в или на разъемных контактах. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 2В |
| Ремонт поврежденных контактов Смывать грязь, мусор или влагу из контактов разъема с помощью электрического контактного очистителя, Номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт ремня электропроводки двигателя ICONTM. См. процедуру 019-206 или 019-207. Заменить электропроводку двигателя ICONTM. См. процедуру 019-043. По мере необходимости ремонтировать или заменять электропроводку OEM. | 7А |  |

#### ШАГ 2B. Проверьте выключатель наклона капота для короткого замыкания на землю.

| **Условия:** Выключите замок зажигания. Отключите переключатель наклона капота ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление от контакта В переключателя наклона ICONTM к заземлению блока двигателя. Измерить сопротивление от контакта А переключателя наклона ICONTM к заземлению блока двигателя. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 100 тыс. ом | 2C |
| Замените выключатель наклона капота. См. процедуру[[97-019-298 — Hood Tilt Switch\|019-298]]. | 7А |  |

#### ШАГ 2C. Проверьте компоненты ICONTM для короткого замыкания на землю.

| **Условия:** Выключите замок зажигания. Отсоедините разъемы ICONTM Idle Control Module A и B от модуля ICONTM idle Control. Установите стояночный тормоз. Поставьте автомобиль на нейтральный уровень. Закройте выключатель наклона капота или обойдите выключатель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление от контакта 5 в ICONTM холостого модуля управления проводка ремня разъема к блоку двигателя земли. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 100k Ом Заменить модуль управления ICONTM. См. процедуру[[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Ремонт завершён |
|  | 3А |  |

### ШАГ 3. Определите систему ICONTM.

#### ШАГ 3A. Определите, является ли система ICONTM послепродажным или OEM-производителем.

| **Условия: **Ни одно |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| См. процедуру[[97-209-017 — ICON™ Idle Control System\|209-017]]. | Система ICONTM является системой Aftermarket. | 4А |
| Проверьте OEM-проводку для короткого замыкания на землю в выходной цепи лампы. | 7А |  |

### ШАГ 4. Проверьте электропроводку двигателя ICONTM.

#### ШАГ 4A. Осмотрите контакты 14-контактного разъема с помощью проводов двигателя ICONTM.

| **Условия:** Выключите замок зажигания. Отсоедините 14-контактный проходной разъем на переборке транспортного средства. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Корродированные штифты Бент или сломанные штифты Отталкивание назад или расширенные штифты Проводная изоляция Повреждение Влажность в или на разъем Пропавшие или поврежденные соединительные штифты Коннекторная оболочка разбитая Грязь или мусор в или на разъемных контактах. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 4B |
| Ремонт поврежденных контактов Смывать грязь, мусор или влагу из контактов разъема с помощью электрического контактного очистителя, Номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт ремня электропроводки двигателя ICONTM. См. процедуру 019-206 или 019-207. Заменить электропроводку двигателя ICONTM. См. процедуру 019-043. | 7А |  |

#### ШАГ 4B. Проверьте упряжку для проводов двигателя ICONTM для короткого приземления.

| **Условия:** Выключите замок зажигания. Отсоедините модуль управления ICONTM от модуля управления ICONTM. Отсоедините 14-контактный проходной разъем на переборке транспортного средства. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление от контакта 5 в ICONTM холостого модуля управления проводка ремня разъема к блоку двигателя земли. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 100 тыс. ом | 5а |
| Заменить электропроводку двигателя ICONTM. См. процедуру[[97-019-043 — Engine Wiring Harness\|019-043]]. | 7А |  |

### ШАГ 5. Проверьте электропроводку ICONTM.

#### ШАГ 5A. Осмотрите контактные линзы кабины ICONTM 14 контактов разъема.

| **Условия:** Выключите замок зажигания. Отсоедините 14-контактный проходной разъем на переборке транспортного средства. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Корродированные штифты Бент или сломанные штифты Отталкивание назад или расширенные штифты Проводная изоляция Повреждение Влажность в или на разъем Пропавшие или поврежденные соединительные штифты Коннекторная оболочка разбитая Грязь или мусор в или на разъемных контактах. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 5В |
| Ремонт поврежденных контактов Смывать грязь, мусор или влагу из контактов разъема с помощью электрического контактного очистителя, Номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт проводов такси. См. процедуру 019-207 Заменить проводку кабины. См. процедуру 019-305. | 7А |  |

#### ШАГ 5B. Проверьте электропроводку кабины и переключатели для короткого замыкания на землю.

| **Условия:** Выключите замок зажигания. Отсоедините разъем 14-контактной кабины. Установите стояночный тормоз. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта J 14-контактного разъёма кабины, стороны кабины, к заземлению блока двигателя. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 100 тыс. ом | 6А |
|  | 5С |  |

#### ШАГ 5C. Проверьте лампу ICONTM на короткое замыкание на землю.

| **Условия:** Выключите замок зажигания. Отсоедините разъем лампы ICONTM от электропроводки кабины. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление от контакта В разъема лампы ICONTM к заземлению блока двигателя. Измерить сопротивление от контакта А разъема лампы ICONTM к заземлению блока двигателя. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 100 тыс. ом | 5D |
| Ремонт или замена лампы ICONTM Ремонт лампы ICONTM. См. процедуру 019-202 или 019-206. Заменить лампу ICONTM. См. процедуру 019-046. | 7А |  |

#### ШАГ 5D. Проверьте выключатель стояночного тормоза ICONTM для короткого замыкания на землю.

| **Условия:** Выключите замок зажигания. Отключите выключатель стояночного тормоза ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление от контакта А разъема переключателя стояночного тормоза к заземлению блока двигателя. Измерить сопротивление от контакта В разъема переключателя стояночного тормоза к заземлению блока двигателя. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 100 км/ч Заменить проводку кабины. См. процедуру[[97-019-305 — Cab Wiring Harness\|019-305]]. | 7А |
| Замените выключатель стояночного тормоза. См. процедуру[[97-019-299 — Parking Brake Switch\|019-299]]. | 7А |  |

### ШАГ 6. Проверьте компоненты блокировки ICONTM.

#### ШАГ 6A. Проверьте нейтральный переключатель положения ICONTM.

| **Условия:** Выключите замок зажигания. Отключите нейтральный переключатель положения. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление от контакта А нейтрального положения переключателя на блок двигателя заземления. Измерить сопротивление от контакта В нейтрального положения переключателя на блок двигателя заземления. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 100k Ом Заменить электропроводку двигателя ICONTM. См. процедуру[[97-019-043 — Engine Wiring Harness\|019-043]]. | 7А |
| Замените нейтральный переключатель. См. процедуру[[97-019-297 — Neutral Position Switch\|019-297]]. | 7А |  |

### ШАГ 7. Очистите код ошибки.

#### ШАГ 7A. Отключите код неисправности.

| **Условия: **Соединить все компоненты. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Цикл переключателя зажигания для проверки кода неисправности неактивен. | Код ошибки 767 обезврежен | Ремонт завершён |
| Устранение неполадок с оставшимися активными кодами неисправностей. | Соответствующие диаграммы устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 767 (Aftermarket and OEM)
>
> ### Starter Interlock Safety Circuit - Voltage Below Normal or Shorted to Low Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 767 PID(P): SPN: FMI: Lamp: SRT: | Starter Interlock Safety Circuit - Voltage Below Normal or Shorted to Low Source. Less than 6-VDC pulse detected at the interlock lamp output circuits when high voltage was expected by the ICON™ idle control module. | The ICON™ system will be disabled. **Only** mandatory shutdown will be enabled. Engine will start normally. |
>
> ### Circuit Description
>
> The interlock input and lamp output circuit provides power to the ICON™ lamp and to the interlock switches. The above circuit diagram can vary, such as connector or pins, depending on the vehicle make or model. OEM installations can possibly provide the harnessing between the idle control module and other ICON™ devices.
>
> ### Component Location
>
> The ICON™ lamp is typically located in the vehicle cab on the dash panel. The parking brake switch is typically located behind the dash on the parking brake air line. The hood tilt switch is typically located on the hood behind the left headlight housing. The neutral position switch is located on the top cover plate of the transmission near the gear shift.
>
> The ICON™ module can be located in a different location depending on the vehicle application.
>
> ### Shoptalk
>
> This fault indicates a short circuit to ground. This circuit outputs a pulse width modulated (PWM) voltage at pin 5 of the ICON™ idle control module A connector.
>
> The ICON™ system can display **only** the present active fault code. If more than one fault code is active at the same time, the ICON™ system flashes out the highest priority fault. After the fault has been corrected then the next active fault will be flashed out.
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
> |  | **STEP 1A.** Use the fault flashout feature or the ICON™ electronic service tool to read the fault codes. | Fault Code 767 active |
> | STEP 2. | Check the ICON™ idle control module. |  |
> |  | **STEP 2A.** Check the ICON™ idle control module A connector for damaged pins. | No damaged pins |
> |  | **STEP 2B.** Check the hood tilt switch for a short circuit to ground. | More than 100k ohms |
> |  | **STEP 2C.** Check the ICON™ components for a short circuit to ground. | More than 100k ohms |
> | STEP 3. | Identify the ICON™ system. |  |
> |  | **STEP 3A.** Identify whether the ICON™ system is an Aftermarket or an OEM. | ICON™ system is Aftermarket |
> | STEP 4. | Check the ICON™ engine harness. |  |
> |  | **STEP 4A.** Inspect the ICON™ engine harness 14-pin connector pins. | No damaged pins |
> |  | **STEP 4B.** Check the ICON™ engine harness for a short to ground. | More than 100k ohms |
> | STEP 5. | Check the ICON™ cab harness. |  |
> |  | **STEP 5A.** Inspect the ICON™ cab harness 14 pin connector pins. | No damaged pins |
> |  | **STEP 5B.** Check the cab harness and switches for a short circuit to ground. | More than 100k ohms |
> |  | **STEP 5C.** Check the ICON™ lamp for a short circuit to ground. | More than 100k ohms |
> |  | **STEP 5D.** Check the ICON™ parking brake switch for a short circuit to ground. | More than 100k ohms |
> | STEP 6. | Check the ICON™ interlock components. |  |
> |  | **STEP 6A.** Check the ICON™ neutral position switch. | More than 100k ohms |
> | STEP 7. | Clear the fault code. |  |
> |  | **STEP 7A.** Disable the fault code. | Fault Code 767 cleared |
>
> ### STEP 1. Read the fault codes.
>
> #### STEP 1A. Use the fault flashout feature or the ICON™ electronic service tool to read the fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect the ICON™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> |  | Fault Code 767 active. | 2A |
> | Refer to Inactive or Intermittent Fault Codes, Procedure [[99-019-362 — Inactive or Intermittent Fault Code\|019-362]]. | 7A |  |
>
> ### STEP 2. Check the ICON™ idle control module.
>
> #### STEP 2A. Check the ICON™ idle control module A connector for damaged pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module connector A from the ICON™ idle control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 2B |
> | Repair the damaged pins Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair or replace the OEM wiring harness as necessary. | 7A |  |
>
> #### STEP 2B. Check the hood tilt switch for a short circuit to ground.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ hood tilt switch. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin B of the ICON™ tilt switch to engine block ground. Measure the resistance from pin A of the ICON™ tilt switch to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 2C |
> | Replace the hood tilt switch. Refer to Procedure [[97-019-298 — Hood Tilt Switch\|019-298]]. | 7A |  |
>
> #### STEP 2C. Check the ICON™ components for a short circuit to ground.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module A and B connectors from the ICON™ idle control module. Set the vehicle parking brake. Put the vehicle in neutral. Close the hood tilt switch or bypass the switch. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 5 in the ICON™ idle control module A harness connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms Replace the ICON™ idle control module. Refer to Procedure [[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Repair Complete |
> |  | 3A |  |
>
> ### STEP 3. Identify the ICON™ system.
>
> #### STEP 3A. Identify whether the ICON™ system is an Aftermarket or an OEM.
>
> | **Conditions:** None |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Refer to Procedure [[97-209-017 — ICON™ Idle Control System\|209-017]]. | ICON™ system is Aftermarket | 4A |
> | Check the OEM wiring harness for a short circuit to ground in the lamp output circuit. | 7A |  |
>
> ### STEP 4. Check the ICON™ engine harness.
>
> #### STEP 4A. Inspect the ICON™ engine harness 14-pin connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the 14-pin pass-through connector at the vehicle bulkhead. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 4B |
> | Repair the damaged pins Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. | 7A |  |
>
> #### STEP 4B. Check the ICON™ engine harness for a short to ground.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module A connector from the ICON™ idle control module. Disconnect the 14-pin pass-through connector at the vehicle bulkhead. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 5 in the ICON™ idle control module A harness connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 5A |
> | Replace the ICON™ engine harness. Refer to Procedure [[97-019-043 — Engine Wiring Harness\|019-043]]. | 7A |  |
>
> ### STEP 5. Check the ICON™ cab harness.
>
> #### STEP 5A. Inspect the ICON™ cab harness 14 pin connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the 14-pin pass-through connector at the vehicle bulkhead. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 5B |
> | Repair the damaged pins Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the cab harness. Refer to Procedure 019-207 Replace the cab harness. Refer to Procedure 019-305. | 7A |  |
>
> #### STEP 5B. Check the cab harness and switches for a short circuit to ground.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the 14 pin cab harness connector. Set the vehicle parking brake. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin J of the 14 pin cab harness connector, cab harness side, to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 6A |
> |  | 5C |  |
>
> #### STEP 5C. Check the ICON™ lamp for a short circuit to ground.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ lamp connector from the cab harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin B of the ICON™ lamp connector to engine block ground. Measure the resistance from pin A of the ICON™ lamp connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 5D |
> | Repair or replace the ICON™ lamp Repair the ICON™ lamp. Refer to Procedure 019-202 or 019-206. Replace the ICON™ lamp. Refer to Procedure 019-046. | 7A |  |
>
> #### STEP 5D. Check the ICON™ parking brake switch for a short circuit to ground.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ parking brake switch. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin A of the parking brake switch connector to engine block ground. Measure the resistance from pin B of the parking brake switch connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms Replace the cab harness. Refer to Procedure [[97-019-305 — Cab Wiring Harness\|019-305]]. | 7A |
> | Replace the parking brake switch. Refer to Procedure [[97-019-299 — Parking Brake Switch\|019-299]]. | 7A |  |
>
> ### STEP 6. Check the ICON™ interlock components.
>
> #### STEP 6A. Check the ICON™ neutral position switch.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the neutral position switch. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin A of the neutral position switch to engine block ground. Measure the resistance from pin B of the neutral position switch to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms Replace the ICON™ engine harness. Refer to Procedure [[97-019-043 — Engine Wiring Harness\|019-043]]. | 7A |
> | Replace the neutral position switch. Refer to Procedure [[97-019-297 — Neutral Position Switch\|019-297]]. | 7A |  |
>
> ### STEP 7. Clear the fault code.
>
> #### STEP 7A. Disable the fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Cycle the keyswitch to verify the fault code is inactive. | Fault Code 767 cleared | Repair complete |
> | Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
