---
aliases:
  - "Топливная система с электронным управлением"
type: "Процедура"
doc: "94-101-007"
title_en: "Electronic Controlled Fuel System"
title_ru: "Топливная система с электронным управлением"
modified: "2003-03-19"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666184"
figures: 41
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-101-007.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/94-101-007.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/94"
  - "перевод/машинный"
---

# Electronic Controlled Fuel System
**Топливная система с электронным управлением**

> [!abstract] Процедура · `94-101-007`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]]
> **Секции:** Section F - Familiarization
> **Даты:** изменён 2003-03-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-101-007.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/94-101-007.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Описание системы QSK

QST Fuel System - это электронная система управления двигателем, предназначенная для оптимизации управления двигателем и снижения выбросов выхлопных газов. Эта система состоит из двух встроенных насосов впрыска топлива (по одному для каждого банка двигателя), управляемых электронным модулем управления (ECM). Топливная система QST управляет заправкой двигателя, помещая топливные насосные стойки в правильное положение для желаемого заправки.

![[19a00086.png]]

### Программируемые функции

Топливная система QST была разработана, чтобы быть гибкой для удовлетворения широкого спектра потребностей в управлении двигателем для внедорожного оборудования. Электронный модуль управления (ECM) может быть запрограммирован на соответствие установленным требованиям вашего приложения.

Введите диагностический режим, удалив диагностический шортинг-колпачок из жгута проводов двигателя.

![[19a00066.png]]

**Скорость холостого хода**

Функция Idle Speed позволяет регулировать скорость холостого хода двигателя между 700 и 900 оборотами в минуту. Данная корректировка может быть произведена с использованием INSITETM, номер детали. 3825145.

![[19a00075.png]]

**Губернатор набирает обороты**

Эта функция позволяет регулировать прирост губернатора для оптимальной производительности двигателя. Прирост корректируется с номинальной скоростью. Затем прирост скорости холостого хода автоматически рассчитывается из номинального прироста скорости. Прибыль губернатора корректируется с помощью INSITETM, номер детали. 3825145.

![[19a00042.png]]

**Тип входного сигнала для скоростных пересадок**

Эта функция позволяет настраивать ECM на входы с уклоном скорости либо Woodward, либо Barber-Colman. Тип ввода может быть изменен с помощью INSITETM, номер детали. 3825145.

![[19a00042.png]]

**Время броска**

Эта функция позволяет регулировать коэффициент времени накала ускорения от 0 до 30. Время разгона рампы - это количество времени, необходимое для ускорения скорости двигателя от холостого хода до номинальной скорости или от коленчатого в номинальную скорость. Для фактического времени рампы обратитесь к таблице времени рампы в руководстве пользователя INSITETM QST30 G-Drive. Каждое значение может быть скорректировано с помощью INSITETM, номер детали. 3825145.

![[19a00076.png]]

**Скорость настройки Knob**

Speed Adjust Knob позволяет регулировать номинальную скорость двигателя на ±6 процентов с помощью потенциометра с диапазоном от 500 до 5000 Ом. Этот вход ECM может быть включен с помощью INSITETM, номер детали. 3825145.

![[00a00029.png]]

**Альтернативный частотный коммутатор**

Настройки переключателя переменной частоты могут быть настроены с помощью INSITETM, номер детали. 3825145. Переключатель может быть настроен на один из следующих вариантов:

1. Нормальный = 50 Гц; Альтернативный = 60 Гц
2. Нормальный = 60 Гц; Альтернативный = 50 Гц
3. Всегда 50 Гц
4. Всегда 60 Гц

Для изменения частоты двигатель должен быть сначала отключен или выведен на холостую, а затем снова на номинальную скорость.

![[00a00030.png]]

**Губернатор Друп**

Функция Governor Droop позволяет регулировать скорость двигателя с 0 до 10 процентов. Данная корректировка может быть произведена с использованием INSITETM, номер детали. 3825145.

Скорость Droop (%) = \[(без скорости загрузки - полная скорость загрузки)/полная скорость загрузки\] x 100

![[19a00085.png]]

**Корректировка крутящего момента**

Функция регулировки кривой крутящего момента позволяет слегка регулировать кривую крутящего момента, чтобы точно настроить выходную мощность двигателя с требованиями ввода генератора. Данная корректировка производится с использованием INSITETM, номер детали. 3825145.

![[00a00031.png]]

**Предупреждение о корректировке порогового значения**

Предупреждающие пороги - это значения параметров двигателя, при которых ECM будет регистрировать и сообщать о состоянии предупреждения о неисправности. Следующие пороги предупреждения корректируются с помощью INSITETM, номер детали. 3825145:

1. Высокотемпературное предупреждение о холоде
2. Предупреждение о низком давлении в холостом состоянии
3. Предупреждение о низком давлении масла при номинальном обороте

![[19a00077.png]]

**Регулировка сверхскоростного отключения**

Порог остановки скорости является значением скорости двигателя, при котором ECM отключит подпитку двигателя. Это значение может быть скорректировано по сравнению с заводским значением по умолчанию. Данная корректировка может быть произведена с использованием INSITETM, номер детали. 3825145.

![[19a00079.png]]

**Калибровка приборов**

Функция калибровки прибора позволяет устанавливать счетчики GOEM для скорости двигателя, температуры охлаждающей жидкости и давления масла для калибровки на драйверы ECM-метра (от 0 до 1 мА). Эти калибровки могут быть выполнены с использованием INSITETM, номер детали. 3825145.

![[19a00078.png]]

**Время работы двигателя**

Время ECM - это количество времени в часах: Минутах, в которых включена ECM (режим запуска или диагностический режим).

Время работы двигателя - это количество времени в часах: Минуты, которые работает двигатель (rpm \> 0).

Оба эти значения могут быть отображены с помощью INSITETM, номер детали. 3825145.

![[19a00081.png]]

**Барбер-Колман шкала фактор**

Масштабный коэффициент Барбера-Колмана позволяет настраивать ECM для оптимальной работы параллелизма с оборудованием Барбера-Колмана. Этот масштабный коэффициент можно регулировать с помощью INSITETM, номер детали. 3825145.

> [!note] Примечание
> Не корректируйте этот параметр, если это не является абсолютно необходимым.

![[19a00084.png]]

**Фактор шкалы Вудворда**

Фактор масштаба Вудворда позволяет настраивать ECM для оптимальной работы с параллельным оборудованием Вудворда. Этот масштабный коэффициент можно регулировать с помощью INSITETM, номер детали. 3825145.

> [!note] Примечание
> Не корректируйте этот параметр, если это не является абсолютно необходимым.

![[19a00084.png]]

### Диагностические коды ошибок

Топливная система QST может отображать и записывать определенные условия обнаружения неисправностей. Эти условия отображаются в виде кодов неисправностей, что облегчает устранение неполадок. Коды неисправностей сохраняются в электронном модуле управления (ECM).

![[19400328.png]]

Существует два типа кодов неисправностей. Существуют коды неисправностей электронной топливной системы двигателя и коды неисправностей системы защиты двигателя.

Все коды ошибок, записанные в системе, будут либо активными (код ошибки в настоящее время активен в двигателе), либо неактивными (код ошибки был активен в какой-то момент, но в настоящее время активен не является).

![[19400329.png]]

Коды ошибок можно просматривать только с помощью INSITETM, номер детали. 3825145.

Чтобы прочитать коды неисправностей, ECM должен быть включен в режиме «Бег» или «Диагностика».

Чтобы войти в диагностический режим, удалите диагностический шортинг-коннектор на ремне проводов двигателя.

Для устранения неисправностей двигатель **должен работать, а ECM **должен быть в диагностическом режиме.

![[19a00042.png]]

Условия неисправности заставят выходы ретранслятора Common Warning или Common Alarm (2A @ 30 VDC) быть активизированы ECM. Выбранные GOEM устройства, используя эти схемы, заставят оператора знать, что существует неисправность.

Выход реле Common Warning по-прежнему позволит работать двигателю. Однако, если общее предупреждение вызвано плохой защитой датчика двигателя, этот параметр будет потерян. Условие должно быть исправлено, как только это удобно.

Выход реле Common Alarm отключит двигатель и не позволит ему работать до тех пор, пока выключатель Stop/Run не будет запущен.

![[00a00021.png]]

Условия заставят ретранслятор (200 мА @ 24 VDC) быть под напряжением ECM. Выбранные GOEM устройства, используя эти схемы, заставят оператора понять, что существует неисправность.

![[19a00087.png]]

Система защиты двигателя записывает отдельные коды неисправностей, когда обнаруживается состояние вне зоны действия любого из датчиков в системе защиты двигателя.

![[00a00022.png]]

Объяснение и исправление всех кодов неисправностей находится в графиках устранения неполадок и ремонта, раздел TF этого руководства. Они перечислены в численном порядке с индексом, расположенным в начале раздела.

![[19400340.png]]

Чтобы выйти из диагностического режима, установите шортинг-плагин в диагностическом разъеме.

![[19a00080.png]]

**Код ошибки Snapshot Data**

Когда диагностический код неисправности записывается в ECM, данные ввода и вывода ECM регистрируются со всех датчиков и коммутаторов. Данные снимка позволяют просматривать и использовать взаимосвязи между входами и выходами ECM во время устранения неполадок.

![[00a00024.png]]

### Система защиты двигателя

Двигатели QST оснащены системой защиты двигателя. Система контролирует критические скорости двигателя, температуру и давление и регистрирует диагностические неисправности при возникновении избыточного или недостаточного рабочего диапазона. Если вне диапазона условие существует, схема Общего предупреждения активизируется. Оператор будет оповещен выбранным OEM-устройством. Схема Common Alarm будет активирована, когда состояние вне зоны действия будет ухудшаться, и произойдет отключение двигателя.

![[00a00025.png]]

### Диаграмма потока

Насос (4) подъемника топлива извлекает топливо из топливного бака или дневного бака клиента (1). Топливо циркулирует через Cummins или префильтр клиента (2) и блок соединения топлива (3). Затем топливо поступает в насос (4) топливного подъемника, где оно помещается под давлением и циркулирует через топливные фильтры (5). Топливо течет через клапан (6) отключения топлива, а затем поступает в насос (7), который создает давление впрыска и отправляет топливо в каждый из топливных форсунок (9) в соответствующее время.

![[19400492.png]]

Переливной клапан (8) регулирует давление подачи топлива на насос для впрыска и отправляет избыточное топливо обратно в топливный бак (1). Это топливо будет проходить через переливной клапан (8) и через «Т», где оно будет соединяться с неиспользованным топливом из топливного форсунка (9). Затем топливо будет поступать через блок (3) топливного соединения и обратно в бак (1).

![[19400492.png]]

### QSK23, QSK45, QSK60 и QSK78 системные компоненты

Система QST на двигателе G-Drive состоит из:

1. Топливные насосы (2)
2. Заглушение клапанов (FSOV) (2)
3. Датчик давления масла (OPS)
4. Датчик температуры охлаждающей жидкости (CTS)
5. Датчик частоты вращения двигателя (ESS)
6. Жгут проводов двигателя
7. Двигатель с жгутом Adaptor Cable
8. Узлы для проводов OEM
9. Электронный модуль управления (ECM)

![[19a00074.png]]

![[00a00027.png]]

**Вводы ЕСМ**

- Датчик давления масла (OPS)
- Датчик температуры охлаждающей жидкости (CTS)
- Датчик частоты вращения двигателя (ESS)

![[00a00028.png]]

ESS предоставляет информацию о скорости двигателя. Датчик расположен в корпусе маховика.

![[19a00067.png]]

Двигатель CTS посылает сигналы в ECM для системы защиты двигателя. CTS расположен в верхнем корпусе корпуса термостата.

![[00a00036.png]]

OPS посылает сигналы в ECM для системы защиты двигателя. Датчик находится на левой стороне блока двигателя позади топливного насоса.

![[00a00037.png]]

**ECM Выходы**

ECM обрабатывает все входные данные и затем контролирует эти выходные части:

- Клапаны для отключения топлива
- Схема общего предупреждения
- Схема общей сигнализации
- Заправщик топливного насоса
- Ретрансляторы драйверов
- Водители метро

![[00a00034.png]]

### Описание Insite

Insite, номер детали. 3825145, является электронным сервисным инструментом для системы QST30 G-Drive. Используйте INSITETM для:

- Владелец программы указал информацию в ECM (параметры и функции)
- помощь в устранении неисправностей двигателя
- настроить ECM так, чтобы он соответствовал приложению, в котором он установлен.

См. InsiteTM G-Drive User's Manual (QST30), Bulletin No. 3666196.

![[19a00042.png]]

**Режим монитора InSITETM**

Режим монитора INSITETM является полезным средством устранения неполадок, которое отображает ключевые входы и выходы ECM. Эта функция может использоваться для определения постоянных или аномально колеблющихся значений.

![[19400360.png]]

В режиме монитора есть один экран. Этот экран определяется пользователем путем запуска настройки монитора и ограничен 16 параметрами. Входные данные ECM показывают данные, которые подаются в ECM датчиками и переключателями системы. Выходы ECM представляют собой значения, которые ECM командует системой QST. Режим мониторинга позволяет отслеживать и использовать взаимосвязь между входами и выходами ECM во время устранения неполадок.

![[nobox.png]]

На рисунках в этом разделе показаны все возможные параметры, которые могут отображаться в режиме монитора, как они могут быть видны с помощью INSITETM.

Режим монитора может использоваться для поиска аномально колеблющихся показаний при устранении неполадок. Датчики, которые не работают в диапазоне, также можно найти, ища фиксированные показания (например, показания температуры охлаждающей жидкости не изменяются с фактической температурой охлаждающей жидкости).

![[nobox.png]]

![[00a00032.png]]

![[00a00033.png]]


> [!quote]- Original (English) · английский оригинал
> ### QSK System Description
>
> The QST Fuel System is an electronic engine control system designed to optimize engine control and reduce exhaust emissions. This system consists of two in-line fuel injection pumps (one for each engine bank) controlled by an Electronic Control Module (ECM). The QST Fuel System controls engine fueling by placing the fuel pump racks in the correct position for the desired fueling.
>
> ### Programmable Features
>
> The QST Fuel System has been designed to be flexible to meet the wide variety of engine control needs for off-highway equipment. The electronic control module (ECM) can be programmed to meet the specified requirements of your application.
>
> Enter the diagnostic mode by removing the diagnostic connector shorting cap from the engine harness.
>
> **Idle Speed**
>
> The Idle Speed feature allows the engine idle speed to be adjusted between 700 rpm and 900 rpm. This adjustment can be made using INSITE™, Part No. 3825145.
>
> **Governor Gain Adjust**
>
> This feature allows the governor gain to be adjusted for optimum engine performance. The gain is adjusted at rated speed. The idle speed gain is then automatically calculated from the rated speed gain. The Governor Gain is adjusted by using INSITE™, Part No. 3825145.
>
> **Speed Bias Input Type**
>
> This feature allows the ECM to be configured to either Woodward or Barber-Colman speed bias inputs. The input type can be changed by using INSITE™, Part No. 3825145.
>
> **Ramp Time**
>
> This feature allows the acceleration ramp time factor to be adjusted from 0 to 30. The acceleration ramp time is the amount of time it takes for the engine speed to accelerate from idle to rated speed or from crank to rated speed. For actual ramp time refer to the table of ramp times in the INSITE™ QST30 G-Drive User's Manual. Each value can be adjusted with INSITE™, Part No. 3825145.
>
> **Speed Adjust Knob**
>
> The Speed Adjust Knob allows the adjustment of rated engine speed by ±6 percent using a potentiometer with a range of 500 to 5000 ohms. This ECM input can be enabled with INSITE™, Part No. 3825145.
>
> **Alternate Frequency Switch**
>
> The Alternate Frequency switch settings can be configured using INSITE™, Part No. 3825145. The switch can be configured to one of the following options:
>
> 1. Normal = 50 Hz; Alternate = 60 Hz
> 2. Normal = 60 Hz; Alternate = 50 Hz
> 3. Always 50 Hz
> 4. Always 60 Hz
>
> To change frequencies, the engine **must** first be shutdown or brought to idle then back to rated speed.
>
> **Governor Droop**
>
> The Governor Droop feature allows the engine speed governor droop to be adjusted from 0 to 10 percent. This adjustment can be made using INSITE™, Part No. 3825145.
>
> Speed Droop (%) = \[(no load speed - full load speed)/full load speed\] x 100
>
> **Torque Curve Adjustment**
>
> The Torque Curve Adjustment feature allows the torque curve to be adjusted slightly in order to fine tune the engine output power with the alternator input requirements. This adjustment is made using INSITE™, Part No. 3825145.
>
> **Warning Threshold Adjustment**
>
> Warning thresholds are engine parameter values at which the ECM will record and report a warning fault condition. The following warning thresholds are adjustable using INSITE™, Part No. 3825145:
>
> 1. High Coolant Temperature Warning
> 2. Low Oil Pressure Warning at idle
> 3. Low Oil Pressure Warning at rated rpm
>
> **Overspeed Shutdown Adjustment**
>
> The Overspeed Shutdown Threshold is the engine speed value at which the ECM will shutoff fueling to the engine. This value can be adjusted down from the factory default value. This adjustment can be made using INSITE™, Part No. 3825145.
>
> **Meter Calibration**
>
> The Meter Calibration feature allows the GOEM installed meters for engine speed, coolant temperature, and oil pressure to be calibrated to the ECM meter drivers (0 to 1 mA). These calibrations can be performed using INSITE™, Part No. 3825145.
>
> **ECM Time and Engine Run Time**
>
> ECM Time is the amount of time in Hours:Minutes that the ECM has been powered up (run mode or diagnostic mode).
>
> Engine Run Time is the amount of time in Hours:Minutes that the engine has been running (rpm \> 0).
>
> Both of these values can be displayed using INSITE™, Part No. 3825145.
>
> **Barber-Colman Scale Factor**
>
> The Barber-Colman Scale Factor allows the ECM to be adjusted for optimum paralleling operation with Barber-Colman paralleling equipment. This scale factor can be adjusted using INSITE™, Part No. 3825145.
>
> **Note · Примечание**
> Do **not** adjust this parameter unless absolutely necessary.
>
> **Woodward Scale Factor**
>
> The Woodward Scale Factor allows the ECM to be adjusted for optimum paralleling operation with Woodward paralleling equipment. This scale factor can be adjusted using INSITE™, Part No. 3825145.
>
> **Note · Примечание**
> Do **not** adjust this parameter unless absolutely necessary.
>
> ### Diagnostic Fault Codes
>
> The QST Fuel System can display and record certain detectable fault conditions. These conditions are displayed as fault codes which makes troubleshooting easier. The fault codes are retained in the electronic control module (ECM).
>
> There are two types of fault codes. There are engine electronic fuel system fault codes and engine protection system fault codes.
>
> All fault codes recorded will either be active (fault code is presently active on the engine) or inactive (fault code was active at some time, but is **not** presently active).
>
> Fault codes can **only** be viewed using INSITE™, Part No. 3825145.
>
> To read the fault codes, the ECM must be powered up either in the “Run” or “Diagnostic” mode.
>
> To enter the diagnostic mode, remove the diagnostic connector shorting cap on the engine harness.
>
> To clear fault codes the engine **must not** be running and the ECM **must** be in the diagnostic mode.
>
> The fault conditions will cause the Common Warning or Common Alarm relay outputs (2A @ 30 VDC) to be energized by the ECM. GOEM selected devices, using these circuits, will make the operator aware that a fault condition exists.
>
> A Common Warning relay output will still allow the engine to be operated. However, if a common warning is caused by a bad sensor engine protection will be lost for that parameter. The condition **must** be repaired as soon as convenient.
>
> A Common Alarm relay output will shutdown the engine and will **not** allow it to be operated until the Stop/Run switch is cycled.
>
> The conditions will cause the Relay Driver (200 mA @ 24 VDC) to be energized by the ECM. GOEM selected devices, using these circuits, will make the operator aware what fault condition exists.
>
> The engine protection system records separate fault codes when an out-of-range condition is found for any of the sensors in the engine protection system.
>
> The explanation and correction of all fault codes is in the troubleshooting and repair charts, Section TF of this manual. They are listed in numerical order with an index located at the beginning of the section.
>
> To exit the diagnostic mode, install the shorting plug in the diagnostic connector.
>
> **Fault Code Snapshot Data**
>
> When a diagnostic fault code is recorded in the ECM, ECM input and output data is recorded from all sensors and switches. Snapshot data allows the relationships between ECM inputs and outputs to be viewed and used during troubleshooting.
>
> ### Engine Protection System
>
> QST engines are equipped with an engine protection system. The system monitors critical engine speeds, temperature and pressure, and will log diagnostic faults when an over- or under-normal operating range condition occurs. If an out-of-range condition exists, the Common Warning circuit is energized. The operator will be alerted by an OEM selected device. The Common Alarm circuit will be energized when an out-of-range condition continues to get worse and engine shutdown occurs.
>
> ### Flow Diagram
>
> The fuel lift pump (4) draws fuel from the customer's fuel or day tank (1). The fuel is circulated through a Cummins or customer prefilter (2) and the fuel connection block (3). The fuel then enters the fuel lift pump (4) where it is placed under pressure and circulated through the on engine fuel filters (5). The fuel flows through the fuel shutoff valve (6) and then enters the injection pump (7), which builds injection pressure and sends fuel to each of the injectors (9) at the appropriate time.
>
> The overflow valve (8) regulates the fuel supply pressure to the injection pump and sends excess fuel back to the fuel tank (1). This fuel will travel through the overflow valve (8) and through a “T” where it will join with the unused fuel from the injector's (9). The fuel will then flow through the fuel connection block (3) and back to the tank (1).
>
> ### QSK23, QSK45, QSK60, and QSK78 System Components
>
> The QST system on a G-Drive engine consists of:
>
> 1. Fuel Pumps (2)
> 2. Fuel Shut Off Valves (FSOV) (2)
> 3. Oil Pressure Sensor (OPS)
> 4. Coolant Temperature Sensor (CTS)
> 5. Engine Speed Sensor (ESS)
> 6. Engine Harness
> 7. Engine Harness Adaptor Cable
> 8. OEM Harness
> 9. Electronic Control Module (ECM)
>
> **ECM Inputs**
>
> - Oil Pressure Sensor (OPS)
> - Coolant Temperature Sensor (CTS)
> - Engine Speed Sensor (ESS)
>
> The ESS provides engine speed information. The sensor is located in the flywheel housing.
>
> The engine CTS sends signals to the ECM for the engine protection system. The CTS is located in the upper casing of the thermostat housing.
>
> The OPS sends signals to the ECM for the engine protection system. The sensor is on the left bank side of the engine block behind the fuel pump.
>
> **ECM Outputs**
>
> The ECM processes all of the input data and then controls these output parts:
>
> - Fuel Shutoff Valves
> - Common Warning circuit
> - Common Alarm circuit
> - Fuel Pump Rack Actuator
> - Relay Drivers
> - Meter Drivers
>
> ### INSITE™ Description
>
> INSITE™, Part No. 3825145, is the electronic service tool for the QST30 G-Drive system. Use INSITE™ to:
>
> - program owner specified information into the ECM (parameters and features)
> - aid in troubleshooting the engine
> - configure the ECM to match the application in which it is installed.
>
> Refer to INSITE™ G-Drive User's Manual (QST30), Bulletin No. 3666196.
>
> **INSITE™ Monitor Mode**
>
> The INSITE™ monitor mode is a useful troubleshooting aid that displays the key ECM inputs and outputs. This feature can be used to spot constant or abnormally fluctuating values.
>
> There is one screen in monitor mode. This screen is user defined by running monitor setup, and limited to 16 parameters. The ECM inputs show the data that is being fed into the ECM by the system's sensors and switches. The ECM outputs are values that the ECM commands to the QST system. Monitor mode allows the relationship between the ECM inputs and outputs to be monitored and used during troubleshooting.
>
> The figures in this section show all of the possible parameters that can be displayed in monitor mode as they can be seen with INSITE™.
>
> Monitor mode can be used to look for abnormally fluctuating readings while troubleshooting. Sensors that are failed in range can also be found by looking for fixed readings (for example, coolant temperature reading does **not** change with actual coolant temperature).
