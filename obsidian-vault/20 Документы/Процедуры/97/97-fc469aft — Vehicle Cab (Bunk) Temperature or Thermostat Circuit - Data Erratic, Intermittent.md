---
type: "Процедура"
doc: "97-fc469aft"
title_en: "Vehicle Cab (Bunk) Temperature or Thermostat Circuit - Data Erratic, Intermittent or Incorrect"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc469aft.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc469aft.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
  - "перевод/машинный"
---

# Vehicle Cab (Bunk) Temperature or Thermostat Circuit - Data Erratic, Intermittent or Incorrect

> [!abstract] Процедура · `97-fc469aft`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2007-01-26
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc469aft.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc469aft.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 469 (Послепродажное и OEM)

### Температура колпачка транспортного средства (банк) или схема термостата - данные нечеткие, прерывистые или неправильные

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 469 PID(P): СПН: ФМИ: Лампа: СТО: | Температура колпачка транспортного средства (банк) или схема термостата - данные нестабильные, прерывистые или неправильные. Термостат ICONTM с кабиной зафиксировал неисправность (E3 на термостате кабины). | E3 будет цикл двигателя между 20 минутами работы и 15 минутами выключения, или **не** автозапуск двигателя для комфортного режима кабины (это выборочный ответ на неисправность E3 в настройках термостата). Система ICONTM будет отключена **не**. Режим двигателя будет оставаться активным. |

![[19802976.png]]

### Описание цепи

Термостат кабины используется для контроля температуры кабины, либо для нагревания, либо для охлаждения. При первоначальном включении термостат будет отображать уровень доработки программного обеспечения, загруженного в термостат, то есть 01, 02, 03, 04, 05 или 06. Термостат кабины необходим для работы в режиме комфорта кабины. Термостат взаимодействует с модулем управления ICONTM, чтобы управлять моментом автозапуска двигателя для поддержания температуры кабины. Кроме того, термостат подключен к переключателю зажигания для обнаружения, когда зажигание включено. Вышеупомянутая схема может варьироваться, например, разъем или штифты, в зависимости от марки или модели транспортного средства. Установки OEM могут обеспечить взаимодействие между модулем управления холостым ходом и другими устройствами ICONTM.

### Расположение компонента

Термостат кабины обычно устанавливается в зоне койки, над кроватью на стене. Модуль ICONTM может быть расположен в другом месте в зависимости от применения транспортного средства.

### Практические замечания

Уровень обновления программного обеспечения, загруженного в термостат кабины, используется для определения заданных точек, в которых может возникнуть неисправность Е3. E3 является признаком того, что произошло одно из следующих событий:

- Двигатель работает более 45 минут (уровень 01 и 02) или 60 минут (уровень 03, 04, 05 или 06), и температура охлаждения или тепла не достигается, а внешняя температура окружающей среды находится в пределах от 0° до 100°F (уровень 01 или 02), от 0° до 110°F (уровень 03) или от 20 до 90°F (уровень 04, 05 или 06). Эти настройки температуры регулируются как отделки 1 и 2, см. настройки отделки термостата в Процедуре[[97-209-017 — ICON™ Idle Control System|209-017]]в разделе F)

Примечание: Уровень 06 пересмотра термостата ICONTM имеет расширенный диапазон для повышения общей эффективности ICONTM. Например, если заданное температурное значение точки и заданное значение пинты охлаждаются как на 21°C \[70°F\], так и на 4°, то, когда термостат находится в тепловом режиме, транспортное средство запускается, когда температура колпачка падает до 19°C \[66°F\] и продолжает работать до тех пор, пока температура кабины не достигнет 22°C \[72°F\]. Когда термостат находится в прохладном режиме, транспортное средство запускается, когда температура кабины достигает 23 ° C \[74 ° F \] и будет продолжать работать до тех пор, пока температура не упадет до 20 ° C \[68 ° F \]. Эта функция является регулируемой.

- Запрос на запуск двигателя был сделан в течение 10 минут после автоматического отключения, а температура окружающей среды находится в пределах от 0° до 100° F; то есть термостат запрашивает перезапуск двигателя в течение 10 минут после предыдущего отключения (уровень 01 или 02) или четыре раза в течение часа, а температура окружающей среды находится в пределах от 0° до 110° F (уровень 03). Уровни 04, 05 и 06 больше не являются неисправностью E3 при перезапуске двигателя в течение 10 минут после предыдущего отключения или четыре раза в течение часа.

E3 может указывать на потенциальное вмешательство термостата; например, оператор выбрал холодный режим, но включил нагреватель или открыл окна. Система кондиционирования воздуха будет пытаться охладить грузовик ниже точки охлаждения заданного времени. В это время будет зарегистрирована ошибка E3 (код ошибки 469). Аналогичная ситуация может возникнуть и в тепловом режиме. Эта неисправность может также возникнуть, даже после достижения правильной температуры, если цепь зарядки аккумулятора не способна производить правильное напряжение для выключения со всеми вентиляторами, огнями, холодильниками и т. Д. Если это происходит, выполните проверку системы зарядки аккумулятора, как описано в Процедуре.[[97-210-001 — Installation Procedure|210-001]]Руководящие принципы установки. Реакция на неисправность Е3 регулируется с помощью термостата (трим 8). Выберите один из следующих вариантов ответа E3:

- Велосипед двигателя в течение 20 минут и выключен в течение 15 минут

- Обозначение системы ICONTM **not** выполняет автозапуск.

Примечание: Неисправность Е3, отображаемая на термостате, не является фактической неисправностью термостата. Это означает, что либо настройки отопления и кондиционирования воздуха должны быть увеличены, либо оператор установил температуру термостата сверх того, что может разместить система отопления и кондиционирования воздуха.

Примечание: Неисправности термостатов E1 и E2 не выплескиваются на лампе ICONTM, а просто отображаются на экране термостата. См. Cab Thermostat Отображает дерево симптомов устранения неисправностей кода ошибки в разделе TS.

Система ICONTM может отображать только текущий активный код неисправности. Если одновременно активируется более одного кода неисправности, система ICONTM выдает наиболее приоритетную ошибку. После того, как ошибка была исправлена, будет выброшена следующая активная ошибка.

Примечание: Инструменты ICONTM могут отображать более одного активного и неактивного кода неисправности одновременно.

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
>

**Для уменьшения возможности повреждения штифта и проводов жгута проводов используйте при проведении измерений следующий испытательный щуп: Номер детали 3822917 - розеточный пробный щуп типа Deutsch/AMP/Metri-Pack**

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте статус кода ошибки. |  |
|  | **STEP 1A.** Используйте функцию вспышки неисправности или инструмент электронного сервиса ICONTM для считывания кодов неисправностей. | Код 469 Active |
| ШАГ 2. | Проверьте термостат кабины установленные точки. |  |
|  | **STEP 2A.** Проверьте настройки термостата кабины. | Установка точек находится в пределах диапазона |
| ШАГ 3. | Проверьте датчик температуры окружающего воздуха. |  |
|  | **STEP 3A.** Проверьте датчик температуры окружающего воздуха и соединительные контакты с проводкой. | Никаких поврежденных контактов |
|  | **STEP 3B** Проверьте сопротивление датчика температуры окружающего воздуха. | Технические характеристики сопротивления при соответствующей температуре окружающего воздуха: 0°C \[32°F \] = 29 до 36k ом, 25°C \[77°F\] = 9 до 11k ом, 50°C \[122°F\] = 3 до 4k ом, 75°C до \[167°F\] = 1300 до 1600 ом, 100°C \[212°F\] = 600 до 750 ом |
|  | **STEP 3B-1.** Проверьте короткий к датчику случай. | Более 100 тыс. ом |
|  | **STEP 3C.** Проверить наличие открытой цепи. | Менее 10 Ом |
|  | **STEP 3D.** Проверьте короткое замыкание на землю. | Более 100 тыс. ом |
| ШАГ 4. | Очистите код ошибки. |  |
|  | **STEP 4A.** Отключить код ошибки. | Код 469 неисправности обезврежен |

### ШАГ 1. Проверьте статус кода ошибки.

#### ШАГ 1A. Используйте функцию вспышки неисправности или инструмент электронного сервиса ICONTM для считывания кодов неисправностей.

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите электронный сервис ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Используйте функцию вспышки неисправности или инструмент электронного сервиса ICONTM для считывания кодов неисправностей. | Код 469 активен. | 2А |
|  | 4А |  |

### ШАГ 2. Проверьте термостат кабины установленные точки.

#### ШАГ 2A. Проверьте настройки термостата кабины.

| **Условия:** Включить переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Прочитайте коды неисправностей на дисплее термостата кабины. Примечание: Если этот сбой произошел после 45 минут (уровень 01 или 02) или 60 минут (уровень 03, 04, 05 или 06), и точки охлаждения или нагрева были установлены должным образом, а окна и двери автомобиля закрыты, это указывает на то, что нагреватель или кондиционер работает плохо и требует ремонта. Это также может указывать на плохую изоляцию в кабине, которая не позволит кабине поддерживать температуру. Плохая изоляция может привести к тому, что кабина слишком быстро потеряет температуру, что приведет к перезапуску двигателя менее чем за 10 минут (уровень обзора 01 или 02) или четыре раза в час (уровень обзора 03, 04, 05 или 06). Может потребоваться уменьшить экстремальную жару (трим 1) или экстремальную холодную (трим 2). Это позволит системе ICONTM перейти в режим непрерывного движения, когда кабина **не** способна поддерживать температуру. Также может потребоваться увеличить дальность, чтобы уменьшить количество запусков двигателя. | Установка точек находится в пределах диапазона. | 3А |
| Проверьте установленные точки термостата и отрегулируйте, если это необходимо. См. процедуру[[97-019-300 — Cab Thermostat\|019-300]]и процедуры[[97-209-017 — ICON™ Idle Control System\|209-017]]. | 4А |  |

### ШАГ 3. Проверьте датчик температуры окружающего воздуха.

#### ШАГ 3A. Проверьте датчик температуры окружающего воздуха и контакты разъёма проводов.

| **Условия:** Выключите замок зажигания. Отсоедините датчик температуры окружающего воздуха от проводов датчика температуры. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте датчик температуры окружающего воздуха и контакты разъёма проводов жгута проводов для следующего: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема разъема разъема или разъема изоляции Поврежденный разъем блокировки вкладки. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов. | 3B |
| Ремонт поврежденных контактов. Промывайте грязь, мусор и влагу от контактов разъема с помощью электрического контактного очистителя, Номер детали 3824510. Ремонт контактов разъема. См. процедуру 019-202 или 019-206. | 4А |  |

#### ШАГ 3B. Проверьте сопротивление датчика температуры окружающего воздуха.

| **Условия:** Выключите замок зажигания. Отсоедините датчик температуры окружающего воздуха от проводов датчика температуры. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сопротивление датчика температуры окружающего воздуха. Измерьте сопротивление от контакта 1 до контакта 2 датчика температуры окружающего воздуха. См. схему проводов или схему схемы для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Технические характеристики сопротивления при соответствующей температуре окружающего воздуха: 0°C \[32°F\] = 29 до 36k ом 25°C \[77°F\] = 9 до 11k ом 50°C \[122°F\] = 3 до 4k ом 75°C \[167°F\] = 1300 до 1600 ом 100°C \[212°F\] = 600 до 750 ом | 3В-1-1 |
| Замените датчик температуры окружающего воздуха. См. процедуру[[97-019-134 — Ambient Air Temperature Sensor\|019-134]]. | 4А |  |

#### ШАГ 3B-1. Проверьте короткий к датчику случай.

| **Условия:** Выключите замок зажигания. Отсоедините датчик температуры окружающего воздуха от проводов датчика температуры. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте цепь на короткое замыкание. Измерить сопротивление от контакта 1 датчика температуры окружающего воздуха к корпусу датчика. Измерьте сопротивление от контакта 2 датчика температуры окружающего воздуха к корпусу датчика. См. схему проводов или схему схемы для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 100 тысяч омов. | 3C |
| Замените датчик температуры окружающего воздуха. См. процедуру[[97-019-134 — Ambient Air Temperature Sensor\|019-134]]. | 4А |  |

#### ШАГ 3C. Проверьте цепь на обрыв.

| **Условия:** Выключите замок зажигания. Отсоедините датчик температуры окружающего воздуха от проводов датчика температуры. Отсоедините проводку датчика температуры от термостата кабины. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте наличие открытой цепи в проводах датчика температуры. Измерить сопротивление от контакта 1 датчика температуры проводов жгута разъёма, конца датчика, до контакта 1 проводов жгута, конца кабины термостата. Измерить сопротивление от контакта 2 датчика температуры проводов жгута разъёма, конца датчика, до контакта 3 проводов жгута, конца кабины термостата. См. схему проводов или схему схемы для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Менее 10 Ом. | 3D |
| Ремонт или замена датчика температуры проводов жгута. Ремонтировать датчик температуры проводов жгута. См. процедуру 019-202 или 019-206. Замените проводку датчика температуры. См. процедуру 019-296. | 4А |  |

#### ШАГ 3D. Проверьте короткое замыкание на землю.

| **Условия:** Выключите замок зажигания. Отсоедините датчик температуры окружающего воздуха от проводов датчика температуры. Отсоедините проводку датчика температуры от термостата кабины. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание на землю. Измерьте сопротивление от контакта 1 датчика температуры проводов ремня разъема, конца датчика, к заземлению блока двигателя. Измерьте сопротивление от контакта 2 датчика температуры проводов ремня разъема, конца датчика, к блоку двигателя. См. схему проводов или схему схемы для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 100 тысяч омов. | 4А |
| Ремонт или замена датчика температуры проводов жгута. Ремонтировать датчик температуры проводов жгута. См. процедуру 019-202 или 019-206. Замените проводку датчика температуры. См. процедуру 019-296. | 4А |  |

### ШАГ 4. Очистите код ошибки.

#### ШАГ 4A. Отключите код неисправности.

| **Условия: **Соединить все компоненты. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Очистите код неактивной ошибки. | Код 469 неисправности обезврежен. | Ремонт завершён |
| Если код 469 по умолчанию все еще активен, замените модуль управления ICONTM. См. процедуру[[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Ремонт завершён |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 469 (Aftermarket and OEM)
>
> ### Vehicle Cab (Bunk) Temperature or Thermostat Circuit - Data Erratic, Intermittent or Incorrect
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 469 PID(P): SPN: FMI: Lamp: SRT: | Vehicle Cab (Bunk) Temperature or Thermostat Circuit - Data Erratic, Intermittent or Incorrect. The ICON™ cab thermostat has logged a fault (E3 on the cab thermostat). | E3 will cycle the engine between 20 minutes run and 15 minutes off, or **not** autostart the engine for cab comfort mode (this is a selectable response of the E3 fault in the thermostat trim settings). The ICON™ system will **not** be disabled. Engine mode will remain active. |
>
> ### Circuit Description
>
> The cab thermostat is used to control the cab temperature, either for heating or cooling. At initial turn-on, the thermostat will display the revision level of the software loaded into the thermostat, that is 01, 02, 03, 04, 05 or 06. The cab thermostat is required for cab comfort mode operation. The thermostat communicates with the ICON™ idle control module to command when to autostart the engine to maintain cab temperature. Also, the thermostat is connected to the keyswitch to detect when the ignition is turned on. The above circuit diagram can vary, such as connector or pins, depending on the vehicle make or model. OEM installations can possibly provide the harnessing between the idle control module and other ICON™ devices.
>
> ### Component Location
>
> The cab thermostat is typically mounted in the bunk area, above the bed on the wall. The ICON™ module can be located in a different location depending on the vehicle application.
>
> ### Shoptalk
>
> The revision level of the software loaded into the cab thermostat is used to identify the set points at which an E3 fault can occur. E3 is an indication that one of the following has occurred:
>
> - Engine has run for more than 45 minutes (revision level 01 and 02) or 60 minutes (revision level 03, 04, 05 or 06) and cool or heat set point is **not** achieved, and the external ambient temperature is within 0° to 100°F (revision level 01 or 02), 0° to 110°F (revision level 03), or 20 to 90°F (revision level 04, 05 or 06). These temperature settings are adjustable as trims 1 and 2, see thermostat trim settings in Procedure [[97-209-017 — ICON™ Idle Control System|209-017]] in Section F)
>
> NOTE: ICON™ thermostat revision level 06 features an expanded range to improve overall ICON™ efficiency. For example, if the set point heat and the set pint cool are both set to 21°C \[70°F\], and the range is 4, then, when the thermostat is in heat mode, the vehicle will start when the cap temperature drops to 19°C \[66°F\] and continue to run until the cab temperature reaches 22°C \[72°F\]. When the thermostat is in cool mode, the vehicle will start when the cab temperature reaches 23°C \[74°F\] and will continue to run until the temperature has dropped to 20°C \[68°F\]. This feature is adjustable.
>
> - A cab thermostat request to start the engine has been made within 10 minutes of an auto-shutdown and the ambient temperature is within 0° to 100° F; that is the thermostat requests an engine restart within 10 minutes of previous shutdown (revision level 01 or 02) or four times within an hour and the ambient temperature is within 0° to 110°F (revision level 03). Revision levels 04, 05, and 06 no longer an E3 fault when the engine is restarted within 10 minutes of a previous shutdown or four times within an hour.
>
> E3 can indicate potential tampering of the thermostat; for example, the operator has chosen cool mode but turned the heater on or opened the windows. The air conditioning system will attempt to cool the truck below the cool set point for correct specified time. At this time, an E3 fault (Fault Code 469) will be logged. A similar situation can occur for heat mode. This fault can also occur, even after achieving the correct temperature, if the battery charging circuit is **not** able to produce the correct voltage for shutdown with all of the fans, lights, refrigerators, and so forth turned on. If this occurs, perform a charging battery system checkout as described in Procedure [[97-210-001 — Installation Procedure|210-001]], Installation Guidelines. The response to an E3 fault is adjustable via the thermostat (trim 8). Select between the following E3 response choices:
>
> - Cycling the engine on for 20 minutes and off for 15 minutes
>
> - Designating that ICON™ system **not** perform an autostart.
>
> Note: An E3 fault displayed on the thermostat is **not** an actual fault with the thermostat. It means that either the heating and air conditioning settings need to be increased, or the operator has set the thermostat temperature beyond what the heating and air conditioning system can accommodate.
>
> Note: The thermostat faults E1 and E2 do **not** flash out on the ICON™ lamp but merely display on the thermostat screen. Refer to the Cab Thermostat Displays a Fault Code troubleshooting symptom tree in Section TS.
>
> The ICON™ system can display **only** the present active fault code. If more than one fault code is active at the same time, the ICON™ system flashes out the highest priority fault. After the fault has been corrected then the next active fault will be flashed out.
>
> Note: The ICON™ electronic service tool can display more than one active and or inactive fault codes at the same time.
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
>
> **To reduce the possibility of pin and harness damage, use the following test lead when taking a measurement: Part Number 3822917 - female Deutsch/AMP/Metri-Pack test lead.**
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the fault code status. |  |
> |  | **STEP 1A.** Use the fault flashout feature or the ICON™ electronic service tool to read the fault codes. | Fault Code 469 active |
> | STEP 2. | Check the cab thermostat set points. |  |
> |  | **STEP 2A.** Check the cab thermostat settings. | Set points are within range |
> | STEP 3. | Check the ambient air temperature sensor. |  |
> |  | **STEP 3A.** Check the ambient air temperature sensor and harness connector pins. | No damaged pins |
> |  | **STEP 3B.** Check the resistance of the ambient air temperature sensor. | Specifications for resistance at respective ambient air temperature: 0° C \[32° F \] = 29 to 36k ohms, 25° C \[77° F\] = 9 to 11k ohms, 50° C \[122° F\] = 3 to 4k ohms, 75° C to \[167° F\] = 1300 to 1600 ohms, 100° C \[212° F\] = 600 to 750 ohms |
> |  | **STEP 3B-1.** Check for a short to sensor case. | More than 100k ohms |
> |  | **STEP 3C.** Check for an open circuit. | Less than 10 ohms |
> |  | **STEP 3D.** Check for a short circuit to ground. | More than 100k ohms |
> | STEP 4. | Clear the fault code. |  |
> |  | **STEP 4A.** Disable the fault code. | Fault Code 469 cleared |
>
> ### STEP 1. Check the fault code status.
>
> #### STEP 1A. Use the fault flashout feature or the ICON™ electronic service tool to read the fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect ICON™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Use the fault flashout feature or the ICON™ electronic service tool to read the fault codes. | Fault Code 469 active. | 2A |
> |  | 4A |  |
>
> ### STEP 2. Check the cab thermostat set points.
>
> #### STEP 2A. Check the cab thermostat settings.
>
> | **Conditions:** Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Read the fault codes on the cab thermostat display. Note: If this fault occurs after 45 minutes have elapsed (revision level 01 or 02) or 60 minutes have elapsed (revision level 03, 04, 05, or 06), and the cool or heat set points have been set properly, and the vehicle's windows and doors are closed, it is an indication that the heater or air conditioner is performing poorly and requires repair. It can also indicate poor insulation in the cab, which will **not** allow the cab to maintain temperature. Poor insulation can cause the cab to lose temperature too quickly, which will cause an engine restart in less than 10 minutes (revision level 01 or 02) or four times in an hour (revision level 03, 04, 05, or 06). It can be necessary to decrease the Extreme Hot (trim 1) or the Extreme Cold (trim 2). This will allow the ICON™ system to transition into a continuous run mode when the cab is **not** capable of maintaining temperature. It can also be necessary to increase the range to decrease the number of times the engine will be started. | Set points are within range. | 3A |
> | Check the thermostat set points and adjust if necessary. Refer to Procedure [[97-019-300 — Cab Thermostat\|019-300]] and Procedure [[97-209-017 — ICON™ Idle Control System\|209-017]]. | 4A |  |
>
> ### STEP 3. Check the ambient air temperature sensor.
>
> #### STEP 3A. Check the ambient air temperature sensor and harness connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ambient air temperature sensor from the temperature sensor harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check ambient air temperature sensor and harness connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris on or in the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins. | 3B |
> | Repair the damaged pins. Flush the dirt, debris, and moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Repair the connector pins. Refer to Procedure 019-202 or 019-206. | 4A |  |
>
> #### STEP 3B. Check the resistance of the ambient air temperature sensor.
>
> | **Conditions:** Turn the keyswitch OFF. Disconnect the ambient air temperature sensor from the temperature sensor harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the resistance of the ambient air temperature sensor. Measure the resistance from pin 1 to pin 2 of the ambient air temperature sensor. Refer to the wiring diagram or the circuit diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Specifications for resistance at respective ambient air temperature: 0° C \[32° F\] = 29 to 36k ohms 25° C \[77° F\] = 9 to 11k ohms 50° C \[122° F\] = 3 to 4k ohms 75° C \[167° F\] = 1300 to 1600 ohms 100° C \[212° F\] = 600 to 750 ohms | 3B-1 |
> | Replace the ambient air temperature sensor. Refer to Procedure [[97-019-134 — Ambient Air Temperature Sensor\|019-134]]. | 4A |  |
>
> #### STEP 3B-1. Check for a short to sensor case.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ambient air temperature sensor from the temperature sensor harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit. Measure the resistance from pin 1 of the ambient air temperature sensor to the sensor case. Measure the resistance from pin 2 of the ambient air temperature sensor to the sensor case. Refer to the wiring diagram or the circuit diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms. | 3C |
> | Replace the ambient air temperature sensor. Refer to Procedure [[97-019-134 — Ambient Air Temperature Sensor\|019-134]]. | 4A |  |
>
> #### STEP 3C. Check for an open circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ambient air temperature sensor from the temperature sensor harness. Disconnect the temperature sensor harness from the cab thermostat. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an open circuit in the temperature sensor harness. Measure the resistance from pin 1 of the temperature sensor harness connector, sensor end, to pin 1 of the harness, cab thermostat end. Measure the resistance from pin 2 of the temperature sensor harness connector, sensor end, to pin 3 of the harness, cab thermostat end. Refer to the wiring diagram or the circuit diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 10 ohms. | 3D |
> | Repair or replace the temperature sensor harness. Repair the temperature sensor harness. Refer to Procedure 019-202 or 019-206. Replace the temperature sensor harness. Refer to Procedure 019-296. | 4A |  |
>
> #### STEP 3D. Check for a short circuit to ground.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ambient air temperature sensor from the temperature sensor harness. Disconnect the temperature sensor harness from the cab thermostat. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit to ground. Measure the resistance from pin 1 of the temperature sensor harness connector, sensor end, to engine block ground. Measure the resistance from pin 2 of the temperature sensor harness connector, sensor end, to engine block ground. Refer to the wiring diagram or the circuit diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms. | 4A |
> | Repair or replace the temperature sensor harness. Repair the temperature sensor harness. Refer to Procedure 019-202 or 019-206. Replace the temperature sensor harness. Refer to Procedure 019-296. | 4A |  |
>
> ### STEP 4. Clear the fault code.
>
> #### STEP 4A. Disable the fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Clear the inactive fault code. | Fault Code 469 cleared. | Repair complete |
> | If Fault Code 469 is still active, replace the ICON™ idle control module. Refer to Procedure [[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Repair complete |  |
