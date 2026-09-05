---
type: "Процедура"
doc: "97-fc766aft"
title_en: "Starter Interlock Safety Circuit - Voltage Above Normal or Shorted to High Source"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc766aft.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc766aft.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
  - "перевод/машинный"
---

# Starter Interlock Safety Circuit - Voltage Above Normal or Shorted to High Source

> [!abstract] Процедура · `97-fc766aft`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-10-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc766aft.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc766aft.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 766 (Послепродажное и OEM)

### Стартовая цепь безопасности блокировки - напряжение выше нормального или короткое до высокого источника

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 766 PID(P): СПН: ФМИ: Лампа: СТО: | Стартовая цепь безопасности блокировки - напряжение выше нормального или короткое до высокого источника. Высокое напряжение, обнаруженное на выходной положительной (+) цепи блокировки/лампы, когда низкое напряжение ожидалось модулем управления холостым ходом ICONTM. | Система ICONTM будет отключена. Включено только обязательное отключение. Двигатель можно запускать нормально. |

![[19803824.png]]

### Описание цепи

Схема запирания и вывода лампы обеспечивает питание лампы ICONTM и переключателей запирания. Вышеупомянутая схема может варьироваться, например, разъем или штифты, в зависимости от марки или модели транспортного средства. Установки OEM могут обеспечить взаимодействие между модулем управления холостым ходом и другими устройствами ICONTM.

### Расположение компонента

Лампа ICONTM обычно расположена в кабине автомобиля на панели приборов. Переключатель стояночного тормоза обычно расположен за тире на линии сжатого воздуха стояночного тормоза. Выключатель наклона капота обычно расположен на капоте позади левого корпуса фар. Переключатель нейтрального положения расположен на верхней крышке трансмиссии вблизи переключения передач.

Модуль ICONTM может быть расположен в другом месте в зависимости от применения транспортного средства.

### Практические замечания

Эта неисправность указывает на короткое замыкание к напряжению батареи. Эта схема выдает импульсное модулированное напряжение шириной импульса (PWM) при контакте 5 модуля управления ICONTM A разъема

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
|  | **STEP 1A.** Используйте функцию вспышки неисправности или инструмент электронного сервиса ICONTM для считывания кодов неисправностей. | Код 766 Active |
| ШАГ 2. | Проверьте модуль управления ICONTM. |  |
|  | **STEP 2A.** Проверьте модуль управления ICONTM бездействия Разъем А для поврежденных контактов. | Никаких поврежденных контактов |
|  | **STEP 2B.** Проверьте переключатель наклона капота для короткого замыкания к батарее. | Менее 1 VDC |
|  | **STEP 2C.** Проверьте систему ICONTM на короткое время до заряда батареи. | Менее 1 VDC |
| ШАГ 3. | Определите систему ICONTM. |  |
|  | **STEP 3A.** Определите, является ли система ICONTM послепродажным или OEM-производителем. | Система ICONTM является системой Aftermarket. |
| ШАГ 4. | Проверьте электропроводку двигателя ICONTM. |  |
|  | **STEP 4A.** Проверить контактные контакты 14-контактного разъема с помощью проводов двигателя ICONTM. | Никаких поврежденных контактов |
|  | **STEP 4B.** Проверьте упряжку для проводов двигателя ICONTM на короткое время до батареи. | Менее 1 VDC |
| ШАГ 5. | Проверьте электропроводку ICONTM. |  |
|  | **STEP 5A.** Проверить контактные контакты 14-контактного разъема кабины ICONTM. | Никаких поврежденных контактов |
|  | **STEP 5B.** Проверьте электропроводку ICONTM на короткое время до батареи. | Менее 1 VDC |
|  | **STEP 5C** Проверьте лампу ICONTM на короткое время до батареи. | Менее 1 VDC |
|  | **STEP 5D.** Проверьте выключатель стояночного тормоза на короткое замыкание к батарее. | Менее 1 VDC |
| ШАГ 6. | Проверьте нейтральный переключатель. |  |
|  | **STEP 6A.** Проверьте нейтральный переключатель положения для короткого замыкания на аккумуляторе. | Менее 1 VDC |
| ШАГ 7. | Очистите код ошибки. |  |
|  | **STEP 7A.** Отключить код ошибки. | Код 766 неисправности обезврежен |

### ШАГ 1. Считайте коды неисправностей.

#### ШАГ 1A. Используйте функцию вспышки неисправности или инструмент электронного сервиса ICONTM для считывания кодов неисправностей.

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите электронный сервис ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
|  | Код ошибки 766 активен. | 2А |
| Неактивные или прерывистые коды ошибок, процедура[[99-019-362 — Inactive or Intermittent Fault Code\|019-362]]. | 7А |  |

### ШАГ 2. Проверьте модуль управления ICONTM.

#### ШАГ 2A. Проверьте модуль управления ICONTM для неработающих контактов Разъем А для поврежденных контактов.

| **Условия:** Выключите замок зажигания. Отсоедините модуль управления ICONTM A и B проводов ремня разъемов от модуля управления ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Корродированные штифты Бент или сломанные штифты Отталкивание назад или расширенные штифты Проводная изоляция Повреждение Влажность в или на разъем Пропавшие или поврежденные соединительные штифты Коннекторная оболочка разбитая Грязь или мусор в или на разъемных контактах. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 2В |
| Ремонт поврежденных контактов Смывать грязь, мусор или влагу из контактов разъема с помощью электрического контактного очистителя, Номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт ремня электропроводки двигателя ICONTM. См. процедуру 019-206 или 019-207. Заменить электропроводку двигателя ICONTM. См. процедуру 019-043. По мере необходимости ремонтировать или заменять электропроводку OEM. | 7А |  |

#### ШАГ 2B. Проверьте переключатель наклона капота для короткого замыкания к батарее.

| **Условия:** Включить переключатель зажигания. Отключите переключатель наклона капота ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте напряжение от контакта B разъема переключателя наклона ICONTM до заземления блока двигателя. Измерьте напряжение от контакта А разъема переключателя наклона ICONTM до заземления блока двигателя. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для методов использования мультиметра, обратитесь к использованию мультиметра, процедура[[99-019-359 — Multimeter Usage\|019-359]]. | Менее 1 VDC | 2C |
| Замените выключатель наклона капота. См. процедуру[[97-019-298 — Hood Tilt Switch\|019-298]]. | 7А |  |

#### ШАГ 2C. Проверьте систему ICONTM для короткого доступа к батарее.

| **Условия:** Включить переключатель зажигания. Отсоедините разъемы ICONTM Idle Control Module A и B от модуля ICONTM idle Control. Установите стояночный тормоз. Поставьте автомобиль на нейтральный уровень. Закройте или обойдите выключатель наклона капота. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте напряжение от контакта 5 в неработающем модуле управления ICONTM Разъем проводов жгута проводов к заземлению блока двигателя. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для методов использования мультиметра, обратитесь к использованию мультиметра, процедура[[99-019-359 — Multimeter Usage\|019-359]]. | Менее 1 VDC Заменить модуль управления ICONTM. См. процедуру[[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Ремонт завершён |
|  | 3А |  |

### ШАГ 3. Определите систему ICONTM.

#### ШАГ 3A. Определите, является ли система ICONTM послепродажным или OEM-производителем.

| **Условия: **Ни одно |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| См. процедуру[[97-209-017 — ICON™ Idle Control System\|209-017]]. | Система ICONTM является системой Aftermarket. | 4А |
| Проверьте OEM-проводку для короткого замыкания к батарее в выходной цепи лампы. | 7А |  |

### ШАГ 4. Проверьте электропроводку двигателя ICONTM.

#### ШАГ 4A. Осмотрите контакты 14-контактного разъема с помощью проводов двигателя ICONTM.

| **Условия:** Выключите замок зажигания. Отсоедините 14-контактный проходной разъем на переборке транспортного средства. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Корродированные штифты Бент или сломанные штифты Отталкивание назад или расширенные штифты Проводная изоляция Повреждение Влажность в или на разъем Пропавшие или поврежденные соединительные штифты Коннекторная оболочка разбитая Грязь или мусор в или на разъемных контактах. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 4B |
| Ремонт поврежденных контактов Смывать грязь, мусор или влагу из контактов разъема с помощью электрического контактного очистителя, Номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт ремня электропроводки двигателя ICONTM. См. процедуру 019-206 или 019-207. Заменить электропроводку двигателя ICONTM. См. процедуру 019-043. | 7А |  |

#### ШАГ 4B. Проверьте упряжку для проводов двигателя ICONTM для короткого доступа к батарее.

| **Условия:** Включить переключатель зажигания. Отсоедините модуль управления ICONTM A и B проводов ремня разъемов от модуля управления ICONTM. Отсоедините 14-контактный проходной разъем на переборке транспортного средства. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте напряжение от контакта 5 в неработающем модуле управления ICONTM Разъем проводов жгута проводов к заземлению блока двигателя. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для методов использования мультиметра, обратитесь к использованию мультиметра, процедура[[99-019-359 — Multimeter Usage\|019-359]]. | Менее 1 VDC | 5а |
| Заменить электропроводку двигателя ICONTM. См. процедуру[[97-019-043 — Engine Wiring Harness\|019-043]]. | 7А |  |

### ШАГ 5. Проверьте электропроводку ICONTM.

#### ШАГ 5A. Осмотрите контакты 14-контактного разъема кабины ICONTM.

| **Условия:** Выключите замок зажигания. Отсоедините 14-контактный проходной разъем на переборке транспортного средства. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Корродированные штифты Бент или сломанные штифты Отталкивание назад или расширенные штифты Проводная изоляция Повреждение Влажность в или на разъем Пропавшие или поврежденные соединительные штифты Коннекторная оболочка разбитая Грязь или мусор в или на разъемных контактах. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 5В |
| Ремонт поврежденных контактов. Промывайте грязь, мусор или влагу от контактов разъема с помощью электрического контактного очистителя, Номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт проводов такси. См. процедуру 019-207. Замените проводку кабины. См. процедуру 019-305. | 7А |  |

#### ШАГ 5B. Проверьте электропроводку ICONTM для короткого доступа к батарее.

| **Условия:** Включить переключатель зажигания. Отсоедините 14-контактный проходной разъем на переборке транспортного средства. Установите стояночный тормоз. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте напряжение от контакта J в кабине проводов 14-контактного пропускного разъема к заземлению блока двигателя. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для методов использования мультиметра, обратитесь к использованию мультиметра, процедура[[99-019-359 — Multimeter Usage\|019-359]]. | Менее 1 VDC | 6А |
|  | 5С |  |

#### ШАГ 5C. Проверьте лампу ICONTM на короткое время до батареи.

| **Условия:** Включить переключатель зажигания. Отсоедините разъем лампы ICONTM от электропроводки кабины. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте напряжение от контакта B разъема лампы ICONTM до заземления блока двигателя. Измерьте напряжение от контакта А разъема лампы ICONTM до заземления блока двигателя. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для методов использования мультиметра, обратитесь к использованию мультиметра, процедура[[99-019-359 — Multimeter Usage\|019-359]]. | Менее 1 VDC | 5D |
| Заменить лампу ICONTM. См. процедуру[[99-019-046 — Fault Lamp\|019-046]]. | 7А |  |

#### ШАГ 5D. Проверьте выключатель стояночного тормоза для короткого замыкания к батарее.

| **Условия:** Включить переключатель зажигания. Отсоедините разъем переключателя стояночного тормоза от электропроводки кабины. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте напряжение от контакта B разъема переключателя парковочного тормоза ICONTM до заземления блока двигателя. Измерьте напряжение от контакта А разъема переключателя парковочного тормоза ICONTM до заземления блока двигателя. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для методов использования мультиметра, обратитесь к использованию мультиметра, процедура[[99-019-359 — Multimeter Usage\|019-359]]. | Менее 1 VDC Заменить проводку кабины. См. процедуру[[97-019-305 — Cab Wiring Harness\|019-305]]. | 7А |
| Замените выключатель стояночного тормоза. См. процедуру[[97-019-299 — Parking Brake Switch\|019-299]]. | 7А |  |

### ШАГ 6. Проверьте нейтральный переключатель.

#### ШАГ 6A. Проверьте нейтральное положение переключателя для короткого замыкания к батарее.

| **Условия:** Включить переключатель зажигания. Отсоедините разъем переключателя нейтрального положения от электропроводки двигателя ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте напряжение от контакта B разъема переключателя нейтрального положения до заземления блока двигателя. Измерьте напряжение от контакта А разъема переключателя нейтрального положения до заземления блока двигателя. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для методов использования мультиметра, обратитесь к использованию мультиметра, процедура[[99-019-359 — Multimeter Usage\|019-359]]. | Менее 1 VDC Заменить электропроводку двигателя ICONTM. См. процедуру[[97-019-043 — Engine Wiring Harness\|019-043]]. | 7А |
| Замените нейтральный переключатель. См. процедуру[[97-019-297 — Neutral Position Switch\|019-297]]. | 7А |  |

### ШАГ 7. Очистите код ошибки.

#### ШАГ 7A. Отключите код неисправности.

| **Условия: **Соединить все компоненты. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Введите переключатель зажигания, запустите двигатель и проведите автомобиль в течение 1 минуты со скоростью более 10 миль в час, чтобы проверить, что код неисправности неактивен. | Код 766 неисправности обезврежен | Ремонт завершён |
| Устранение неполадок с оставшимися активными кодами неисправностей. | Соответствующие диаграммы устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 766 (Aftermarket and OEM)
>
> ### Starter Interlock Safety Circuit - Voltage Above Normal or Shorted to High Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 766 PID(P): SPN: FMI: Lamp: SRT: | Starter Interlock Safety Circuit - Voltage Above Normal or Shorted to High Source. High voltage detected at the interlock/lamp output positive (+) circuit when low voltage was expected by the ICON™ idle control module. | The ICON™ system will be disabled. **Only** mandatory shutdown will be enabled. Engine can be started normally. |
>
> ### Circuit Description
>
> The interlock and lamp output circuit provides power to the ICON™ lamp and to the interlock switches. The above circuit diagram can vary, such as connector or pins, depending on the vehicle make or model. OEM installations can possibly provide the harnessing between the idle control module and other ICON™ devices.
>
> ### Component Location
>
> The ICON™ lamp is typically located in the vehicle cab on the dash panel. The parking brake switch is typically located behind the dash on the parking brake air line. The hood tilt switch is typically located on the hood behind the left headlight housing. The neutral position switch is located on the top cover plate of the transmission near the gear shift.
>
> The ICON™ module can be located in a different location depending on the vehicle application.
>
> ### Shoptalk
>
> This fault indicates a short circuit to battery voltage. This circuit outputs a pulse width modulated (PWM) voltage at pin 5 of the ICON™ idle control module A connector
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
> |  | **STEP 1A.** Use the fault flashout feature or the ICON™ electronic service tool to read the fault codes. | Fault Code 766 active |
> | STEP 2. | Check the ICON™ idle control module. |  |
> |  | **STEP 2A.** Check the ICON™ idle control module A connector for damaged pins. | No damaged pins |
> |  | **STEP 2B.** Check the hood tilt switch for a short circuit to the battery. | Less than 1 VDC |
> |  | **STEP 2C.** Check the ICON™ system for a short to the battery. | Less than 1 VDC |
> | STEP 3. | Identify the ICON™ system. |  |
> |  | **STEP 3A.** Identify whether the ICON™ system is an Aftermarket or an OEM. | ICON™ system is Aftermarket |
> | STEP 4. | Check the ICON™ engine harness. |  |
> |  | **STEP 4A.** Inspect the ICON™ engine harness 14-pin connector pins. | No damaged pins |
> |  | **STEP 4B.** Check the ICON™ engine harness for a short to the battery. | Less than 1 VDC |
> | STEP 5. | Check the ICON™ cab harness. |  |
> |  | **STEP 5A.** Inspect the ICON™ cab harness 14-pin connector pins. | No damaged pins |
> |  | **STEP 5B.** Check the ICON™ cab harness for a short to the battery. | Less than 1 VDC |
> |  | **STEP 5C.** Check the ICON™ lamp for a short to the battery. | Less than 1 VDC |
> |  | **STEP 5D.** Check the parking brake switch for a short circuit to the battery. | Less than 1 VDC |
> | STEP 6. | Check the neutral position switch. |  |
> |  | **STEP 6A.** Check the neutral position switch for a short circuit to the battery. | Less than 1 VDC |
> | STEP 7. | Clear the fault code. |  |
> |  | **STEP 7A.** Disable the fault code. | Fault Code 766 cleared |
>
> ### STEP 1. Read the fault codes.
>
> #### STEP 1A. Use the fault flashout feature or the ICON™ electronic service tool to read the fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect the ICON™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> |  | Fault Code 766 active. | 2A |
> | Refer to Inactive or Intermittent Fault Codes, Procedure [[99-019-362 — Inactive or Intermittent Fault Code\|019-362]]. | 7A |  |
>
> ### STEP 2. Check the ICON™ idle control module.
>
> #### STEP 2A. Check the ICON™ idle control module A connector for damaged pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module A and B harness connectors from the ICON™ idle control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 2B |
> | Repair the damaged pins Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair or replace the OEM wiring harness as necessary. | 7A |  |
>
> #### STEP 2B. Check the hood tilt switch for a short circuit to the battery.
>
> | **Conditions:** Turn keyswitch ON. Disconnect the ICON™ hood tilt switch. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the voltage from pin B of the ICON™ tilt switch connector to engine block ground. Measure the voltage from pin A of the ICON™ tilt switch connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For multimeter usage techniques, refer to Multimeter Usage, Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | Less than 1 VDC | 2C |
> | Replace the hood tilt switch. Refer to Procedure [[97-019-298 — Hood Tilt Switch\|019-298]]. | 7A |  |
>
> #### STEP 2C. Check the ICON™ system for a short to the battery.
>
> | **Conditions:** Turn keyswitch ON. Disconnect the ICON™ idle control module A and B connectors from the ICON™ idle control module. Set the parking brake. Put the vehicle in neutral. Close or bypass the hood tilt switch. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the voltage from pin 5 in the ICON™ idle control module A harness connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For multimeter usage techniques, refer to Multimeter Usage, Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | Less than 1 VDC Replace the ICON™ idle control module. Refer to Procedure [[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Repair Complete |
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
> | Check the OEM wiring harness for a short circuit to battery in the lamp output circuit. | 7A |  |
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
> #### STEP 4B. Check the ICON™ engine harness for a short to the battery.
>
> | **Conditions:** Turn keyswitch ON. Disconnect the ICON™ idle control module A and B harness connectors from the ICON™ idle control module. Disconnect the 14-pin pass-through connector at the vehicle bulkhead. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the voltage from pin 5 in the ICON™ idle control module A harness connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For multimeter usage techniques, refer to Multimeter Usage, Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | Less than 1 VDC | 5A |
> | Replace the ICON™ engine harness. Refer to Procedure [[97-019-043 — Engine Wiring Harness\|019-043]]. | 7A |  |
>
> ### STEP 5. Check the ICON™ cab harness.
>
> #### STEP 5A. Inspect the ICON™ cab harness 14-pin connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the 14-pin pass-through connector at the vehicle bulkhead. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 5B |
> | Repair the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the cab harness. Refer to Procedure 019-207. Replace the cab harness. Refer to Procedure 019-305. | 7A |  |
>
> #### STEP 5B. Check the ICON™ cab harness for a short to the battery.
>
> | **Conditions:** Turn keyswitch ON. Disconnect the 14-pin pass-through connector at the vehicle bulkhead. Set the parking brake. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the voltage from pin J in the cab harness 14 pin pass-through connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For multimeter usage techniques, refer to Multimeter Usage, Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | Less than 1 VDC | 6A |
> |  | 5C |  |
>
> #### STEP 5C. Check the ICON™ lamp for a short to the battery.
>
> | **Conditions:** Turn keyswitch ON. Disconnect the ICON™ lamp connector from the cab harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the voltage from pin B of the ICON™ lamp connector to engine block ground. Measure the voltage from pin A of the ICON™ lamp connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For multimeter usage techniques, refer to Multimeter Usage, Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | Less than 1 VDC | 5D |
> | Replace the ICON™ lamp. Refer to Procedure [[99-019-046 — Fault Lamp\|019-046]]. | 7A |  |
>
> #### STEP 5D. Check the parking brake switch for a short circuit to the battery.
>
> | **Conditions:** Turn keyswitch ON. Disconnect the parking brake switch connector from the cab harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the voltage from pin B of the ICON™ parking brake switch connector to engine block ground. Measure the voltage from pin A of the ICON™ parking brake switch connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For multimeter usage techniques, refer to Multimeter Usage, Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | Less than 1 VDC Replace the cab harness. Refer to Procedure [[97-019-305 — Cab Wiring Harness\|019-305]]. | 7A |
> | Replace the parking brake switch. Refer to Procedure [[97-019-299 — Parking Brake Switch\|019-299]]. | 7A |  |
>
> ### STEP 6. Check the neutral position switch.
>
> #### STEP 6A. Check the neutral position switch for a short circuit to the battery.
>
> | **Conditions:** Turn keyswitch ON. Disconnect the neutral position switch connector from the ICON™ engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the voltage from pin B of the neutral position switch connector to engine block ground. Measure the voltage from pin A of the neutral position switch connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For multimeter usage techniques, refer to Multimeter Usage, Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | Less than 1 VDC Replace the ICON™ engine harness. Refer to Procedure [[97-019-043 — Engine Wiring Harness\|019-043]]. | 7A |
> | Replace the neutral position switch. Refer to Procedure [[97-019-297 — Neutral Position Switch\|019-297]]. | 7A |  |
>
> ### STEP 7. Clear the fault code.
>
> #### STEP 7A. Disable the fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Cycle the keyswitch, start the engine, and drive the vehicle for 1 minute at more than 10 mph to verify the fault code is inactive. | Fault Code 766 cleared | Repair complete |
> | Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
