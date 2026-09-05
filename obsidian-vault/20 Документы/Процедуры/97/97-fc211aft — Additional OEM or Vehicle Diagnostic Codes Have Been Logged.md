---
type: "Процедура"
doc: "97-fc211aft"
title_en: "Additional OEM or Vehicle Diagnostic Codes Have Been Logged"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc211aft.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc211aft.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
  - "перевод/машинный"
---

# Additional OEM or Vehicle Diagnostic Codes Have Been Logged

> [!abstract] Процедура · `97-fc211aft`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-10-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc211aft.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc211aft.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 211 (Послепродажное обслуживание и OEM)

### Дополнительные OEM-коды или коды диагностики транспортных средств были зарегистрированы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 211 PID(P): СПН: ФМИ: Лампа: Нет, не srt: | Дополнительные OEM-коды или коды диагностики транспортных средств были зарегистрированы. Некоторая информация, ожидаемая на шине данных J1587 CAN от модуля управления холостым ходом ICONTM, была **не** получена от двигателя ECM. | Система ICONTM может быть отключена, а обязательное отключение может быть отключено. Двигатель запускается нормально. |

![[19802955.png]]

### Описание цепи

Шина данных J1587 CAN обеспечивает связь между электронным модулем управления двигателем (ECM) и модулем управления холостым ходом ICONTM. Вышеупомянутая схема может варьироваться, например, разъем или штифты, в зависимости от марки или модели транспортного средства. Установки OEM могут обеспечить взаимодействие между модулем управления холостым ходом и другими устройствами ICONTM.

### Расположение компонента

Шина данных J1587 CAN расположена в электропроводке OEM. Модуль управления ICONTM обычно подключается к проводной ремне J1587 за разъемом службы шины данных CAN в кабине. Модуль ICONTM может быть расположен в другом месте в зависимости от применения транспортного средства.

### Практические замечания

Эта неисправность устанавливается, когда информация, требуемая модулем управления холостым ходом ICONTM, **не** получена от двигателя ECM. Он также устанавливается, когда модуль управления ICONTM не может правильно установить скорость холостого хода. Проверьте двигатель ECM на наличие активных неисправностей и устраните их в первую очередь.

Модульные коммуникации перечислены ниже.

Двигатель ECM для модуля управления холостым ходом ICONTM:

- РРМ

- Температура охлаждающей жидкости

- Температура масла

- Положение дроссельной заслонки

- Переключатель сцепления

- Круизный переключатель

- Параметры скорости автомобиля.

Модуль управления холостым ходом ICONTM для двигателя ECM:

- Параметр сообщения управления скоростью один раз в секунду.

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
|  | **STEP 1A.** Используйте функцию вспышки неисправности или инструмент электронного сервиса ICONTM для считывания кода неисправности. | Код ошибки 211 неактивен |
| ШАГ 2. | Проверьте электропроводку двигателя ICONTM. |  |
|  | **STEP 2A.** Проверьте короткое замыкание в шине данных J1587 CAN. | Пин А: 2.5-5 VDC, Pin B: 0-2,5 VDC, Pin C: 10-27 VDC, Pin E: 0 VDC |
|  | **STEP 2B.** Проверьте коннекторы разъемов ICONTM и коннекторы модуля управления ICONTM. | Никаких поврежденных контактов |
|  | **STEP 2C.** Проверьте полную проводку ремня для короткого замыкания от пин-кодов до пин-кодов. | Более 100 тыс. ом |
|  | **STEP 2C-1.** Определите, является ли система ICONTM послепродажным или OEM-производителем. | Система ICONTM является системой Aftermarket. |
|  | **STEP 2C-2.** Проверьте электропроводку кабины на короткое замыкание от пин-кодов до пин-кодов. | Более 100 тыс. ом |
|  | **STEP 2D.** Проверьте полную проводку ремня для короткого замыкания на землю. | Более 100 тыс. ом |
|  | **STEP 2D-1.** Определите, является ли система ICONTM послепродажным или OEM-производителем. | Система ICONTM является системой Aftermarket. |
|  | **STEP 2D-2.** Проверьте электропроводку кабины на короткое время до земли. | Более 100 тыс. ом |
| ШАГ 3. | Очистите код ошибки. |  |
|  | **STEP 3A.** Отключить код ошибки. | Код ошибки 211 обезврежен |

### ШАГ 1. Считайте коды неисправностей.

#### ШАГ 1A. Используйте функцию вспышки неисправности или инструмент электронного сервиса ICONTM для считывания кодов неисправностей.

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите электронный сервис ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Инициировать кнопку тестирования шины данных CAN на инструменте службы, чтобы определить, работает ли шина данных CAN должным образом. | Код 211 неактивных ошибок Неактивные или прерывистые коды неисправностей, процедура[[99-019-362 — Inactive or Intermittent Fault Code\|019-362]]. | 3А |
|  | 2А |  |

### ШАГ 2. Проверьте электропроводку двигателя ICONTM.

#### ШАГ 2A. Проверьте короткое замыкание в шине данных J1587 CAN.

| **Условия:** Отсоединить разъем B модуля управления ICONTM от модуля управления ICONTM. Убедитесь, что 14-контактный проходной разъем подключен. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте напряжение от каждого штифта в разъеме шины данных J1587 CAN до заземления блока двигателя. Для методов использования мультиметра, обратитесь к использованию мультиметра, процедура[[99-019-359 — Multimeter Usage\|019-359]]. | Пин А: 2.5-5 VDC Pin B: От 0 до 2,5 VDC Pin C: 10-27 VDC Pin E: 0 VDC | 2В |
| Исправьте неправильно сплайсированные провода шины данных CAN. | 3А |  |

#### ШАГ 2B. Проверьте коннекторы проводов двигателя ICONTM и контакты разъема модуля управления ICONTM.

| **Условия:** Выключите замок зажигания. Отсоедините разъем B модуля управления ICONTM от модуля управления ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Корродированные штифты Бент или сломанные штифты Отталкивание назад или расширенные штифты Проводная изоляция Повреждение Влажность в или на разъем Пропавшие или поврежденные соединительные штифты Коннекторная оболочка разбитая Грязь или мусор в или на разъемных контактах. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 2C |
| Ремонт поврежденных контактов. Промывайте грязь, мусор или влагу от контактов разъема с помощью электрического контактного очистителя, Номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт ремня электропроводки двигателя ICONTM. См. процедуру 019-206. Заменить электропроводку двигателя ICONTM. См. процедуру 019-043. Заменить модуль управления ICONTM idle. См. процедуру 019-358. По мере необходимости ремонтировать или заменять электропроводку OEM. | 3А |  |

#### ШАГ 2C. Проверьте полную проводку ремня для короткого замыкания от пин-кодов до пин-кодов.

| **Условия:** Выключите замок зажигания. Отсоедините разъем B модуля управления ICONTM от модуля управления ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта 7 в неработающем модуле управления ICONTM B проводов жгута разъёма ко всем другим штифтам в разъеме. Измерьте сопротивление от контакта 8 в неработающем модуле управления ICONTM B проводов жгута разъёма ко всем другим штифтам в разъеме. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 100 тыс. ом | 2D |
|  | 2С-1 |  |

#### ШАГ 2C-1. Определите, является ли система ICONTM послепродажным или OEM-производителем.

| **Условия: **Ни одно |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| См. процедуру[[97-209-017 — ICON™ Idle Control System\|209-017]]. | Система ICONTM является системой Aftermarket. | 2С-2 |
| Проверьте OEM-проводку для короткого замыкания, чтобы закрепить цепь шины данных J1587 CAN. | 3А |  |

#### ШАГ 2C-2. Проверьте электропроводку кабины для короткого замыкания от пин-кодов до пин-кодов.

| **Условия:** Выключите замок зажигания. Отсоедините 14-контактный проходной разъем на переборке транспортного средства. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта G в 14-контактном проходном разъеме, кабинной проводах с ремнями безопасности, ко всем другим штифтам в разъеме, кроме контакта H. Измерьте сопротивление от контакта H в 14-контактном проходном разъеме, кабинной проводах с ремнями безопасности, ко всем другим штифтам в разъеме, кроме контакта G. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 100 000 Ом Ремонт или замена ремня электропроводки двигателя ICONTM Ремонт ремня электропроводки двигателя ICONTM. См. процедуру 019-206 или 019-207. Заменить электропроводку двигателя ICONTM. См. процедуру 019-043. | 3А |
| Ремонт или замена кабины проводов ремень ремонт кабины проводов ремень. См. процедуру 019-207. Замените проводку кабины. См. процедуру 019-305. | 3А |  |

#### ШАГ 2D. Проверьте полную проводку ремня для короткого замыкания на землю.

| **Условия:** Выключите замок зажигания. Отсоедините разъем B модуля управления ICONTM от модуля управления ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта 7 в неработающем модуле управления ICONTM B проводов ремня разъема к заземлению блока двигателя. Измерьте сопротивление от контакта 8 в неработающем модуле управления ICONTM B проводов ремня разъема к заземлению блока двигателя. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 100k Ом Заменить модуль управления ICONTM. См. процедуру[[97-019-358 — ICON™ Idle Control Module\|019-358]]. | 3А |
|  | 2D-1 |  |

#### ШАГ 2D-1. Определите, является ли система ICONTM послепродажным или OEM-производителем.

| **Условия: **Ни одно |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| См. процедуру[[97-209-017 — ICON™ Idle Control System\|209-017]]. | Система ICONTM является системой Aftermarket. | 2D-2 |
| Проверьте проводку OEM-производителя, чтобы замыкать короткое замыкание на цепи шины данных J1587 CAN. | 3А |  |

#### ШАГ 2D-2. Проверьте электропроводку кабины для короткого замыкания на землю.

| **Условия:** Выключите замок зажигания. Отсоедините 14-контактный проходной разъем на переборке транспортного средства. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта G в 14-контактном проходном разъеме, стороне проводов кабины, к заземлению блока двигателя. Измерьте сопротивление от контакта H в 14-контактном проходном разъеме, кабинной проводах с ремнями безопасности, к заземлению блока двигателя. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 100 000 Ом Ремонт или замена ремня электропроводки двигателя ICONTM Ремонт ремня электропроводки двигателя ICONTM. См. процедуру 019-206 или 019-207. Заменить электропроводку двигателя ICONTM. См. процедуру 019-043. | 3А |
| Ремонт или замена кабины проводов ремень ремонт кабины проводов ремень. См. процедуру 019-207. Замените проводку кабины. См. процедуру 019-305. | 3А |  |

### ШАГ 3. Очистите код ошибки.

#### ШАГ 3A. Отключите код неисправности.

| **Условия: **Соединить все компоненты. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Цикл переключателя зажигания для проверки кода неисправности неактивен. | Код ошибки 211 обезврежен | Ремонт завершён |
| Устранение неполадок с оставшимися активными кодами неисправностей. | Соответствующие диаграммы устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 211 (Aftermarket and OEM)
>
> ### Additional OEM or Vehicle Diagnostic Codes Have Been Logged
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 211 PID(P): SPN: FMI: Lamp: None SRT: | Additional OEM or Vehicle Diagnostic Codes Have Been Logged. Some information expected on the J1587 datalink by the ICON™ idle control module was **not** received from the engine ECM. | The ICON™ system can be disabled and mandatory shutdown can be disabled. Engine will start normally. |
>
> ### Circuit Description
>
> The J1587 datalink provides communication between the engine electronic control module (ECM) and the ICON™ idle control module. The above circuit diagram can vary, such as connector or pins, depending on the vehicle make or model. OEM installations can possibly provide the harnessing between the idle control module and other ICON™ devices.
>
> ### Component Location
>
> The J1587 datalink is located in the OEM wiring harness. The ICON™ idle control module typically connects into the J1587 wiring harness behind the in-cab datalink service connector. The ICON™ module can be located in a different location depending on the vehicle application.
>
> ### Shoptalk
>
> This fault is set when information that is required by the ICON™ idle control module is **not** received from the engine ECM. It is also set when the ICON™ idle control module is unable to set the idle speed correctly. Check the engine ECM for active faults and troubleshoot those first.
>
> Module communications are listed below.
>
> Engine ECM to ICON™ idle control module:
>
> - RPM
>
> - Coolant temperature
>
> - Oil temperature
>
> - Throttle position
>
> - Clutch switch
>
> - Cruise switch
>
> - Vehicle speed parameters.
>
> ICON™ idle control module to engine ECM:
>
> - speed control message parameter once per second.
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
> |  | **STEP 1A.** Use the fault flashout feature or the ICON™ electronic service tool to read the fault code. | Fault Code 211 inactive |
> | STEP 2. | Check the ICON™ engine harness. |  |
> |  | **STEP 2A.** Check for a short circuit in the J1587 datalink. | Pin A: 2.5 to 5 VDC, Pin B: 0 to 2.5 VDC, Pin C: 10 to 27 VDC, Pin E: 0 VDC |
> |  | **STEP 2B.** Check the ICON™ engine harness and the ICON™ idle control module connector pins. | No damaged pins |
> |  | **STEP 2C.** Check the complete harness for a short circuit from pin to pin. | More than 100k ohms |
> |  | **STEP 2C-1.** Identify whether the ICON™ system is an Aftermarket or an OEM. | ICON™ system is Aftermarket |
> |  | **STEP 2C-2.** Check the cab harness for a short circuit from pin to pin. | More than 100k ohms |
> |  | **STEP 2D.** Check the complete harness for a short circuit to ground. | More than 100k ohms |
> |  | **STEP 2D-1.** Identify whether the ICON™ system is an Aftermarket or an OEM. | ICON™ system is Aftermarket |
> |  | **STEP 2D-2.** Check the cab harness for a short to ground. | More than 100k ohms |
> | STEP 3. | Clear the fault code. |  |
> |  | **STEP 3A.** Disable the fault code. | Fault Code 211 cleared |
>
> ### STEP 1. Read the fault codes.
>
> #### STEP 1A. Use the fault flashout feature or the ICON™ electronic service tool to read the fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect the ICON™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Initiate the datalink test button on the service tool to determine if the datalink is working properly. | Fault Code 211 inactive Refer to Inactive or Intermittent Fault Codes, Procedure [[99-019-362 — Inactive or Intermittent Fault Code\|019-362]]. | 3A |
> |  | 2A |  |
>
> ### STEP 2. Check the ICON™ engine harness.
>
> #### STEP 2A. Check for a short circuit in the J1587 datalink.
>
> | **Conditions:** Disconnect the ICON™ idle control module B connector from the ICON™ idle control module. Make sure the 14-pin pass-through connector is connected. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the voltage from each pin in the J1587 datalink connector to engine block ground. For multimeter usage techniques, refer to Multimeter Usage, Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | Pin A: 2.5 to 5 VDC Pin B: 0 to 2.5 VDC Pin C: 10 to 27 VDC Pin E: 0 VDC | 2B |
> | Correct the incorrectly spliced datalink wires. | 3A |  |
>
> #### STEP 2B. Check the ICON™ engine harness and the ICON™ idle control module connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module B connector from the ICON™ idle control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 2C |
> | Repair the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the ICON™ engine harness. Refer to Procedure 019-206. Replace the ICON™ engine harness. Refer to Procedure 019-043. Replace the ICON™ idle control module. Refer to Procedure 019-358. Repair or replace the OEM wiring harness as necessary. | 3A |  |
>
> #### STEP 2C. Check the complete harness for a short circuit from pin to pin.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module B connector from the ICON™ idle control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 7 in the ICON™ idle control module B harness connector to all other pins in the connector. Measure the resistance from pin 8 in the ICON™ idle control module B harness connector to all other pins in the connector. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 2D |
> |  | 2C-1 |  |
>
> #### STEP 2C-1. Identify whether the ICON™ system is an Aftermarket or an OEM.
>
> | **Conditions:** None |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Refer to Procedure [[97-209-017 — ICON™ Idle Control System\|209-017]]. | ICON™ system is Aftermarket | 2C-2 |
> | Check the OEM wiring harness for a short circuit pin to pin on the J1587 datalink circuit. | 3A |  |
>
> #### STEP 2C-2. Check the cab harness for a short circuit from pin to pin.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the 14-pin pass-through connector at the vehicle bulkhead. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin G in the 14-pin pass-through connector, cab harness side, to all other pins in the connector, except pin H. Measure the resistance from pin H in the 14-pin pass-through connector, cab harness side, to all other pins in the connector, except pin G. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms Repair or replace the ICON™ engine harness Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. | 3A |
> | Repair or replace the cab harness Repair the cab harness. Refer to Procedure 019-207. Replace the cab harness. Refer to Procedure 019-305. | 3A |  |
>
> #### STEP 2D. Check the complete harness for a short circuit to ground.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module B connector from the ICON™ idle control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 7 in the ICON™ idle control module B harness connector to engine block ground. Measure the resistance from pin 8 in the ICON™ idle control module B harness connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms Replace the ICON™ idle control module. Refer to Procedure [[97-019-358 — ICON™ Idle Control Module\|019-358]]. | 3A |
> |  | 2D-1 |  |
>
> #### STEP 2D-1. Identify whether the ICON™ system is an Aftermarket or an OEM.
>
> | **Conditions:** None |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Refer to Procedure [[97-209-017 — ICON™ Idle Control System\|209-017]]. | ICON™ system is Aftermarket | 2D-2 |
> | Check the OEM wiring harness a short circuit to ground on the J1587 datalink circuit. | 3A |  |
>
> #### STEP 2D-2. Check the cab harness for a short circuit to ground.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the 14-pin pass-through connector at the vehicle bulkhead. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin G in the 14-pin pass-through connector, cab harness side, to engine block ground. Measure the resistance from pin H in the 14-pin pass-through connector, cab harness side, to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms Repair or replace the ICON™ engine harness Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. | 3A |
> | Repair or replace the cab harness Repair the cab harness. Refer to Procedure 019-207. Replace the cab harness. Refer to Procedure 019-305. | 3A |  |
>
> ### STEP 3. Clear the fault code.
>
> #### STEP 3A. Disable the fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Cycle the keyswitch to verify the fault code is inactive. | Fault Code 211 cleared | Repair complete |
> | Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
