---
aliases:
  - "Топливная система с электронным управлением"
type: "Процедура"
doc: "19-101-007"
title_en: "Electronic Controlled Fuel System"
title_ru: "Топливная система с электронным управлением"
modified: "2013-03-05"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 28
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-101-007.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-101-007.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Electronic Controlled Fuel System
**Топливная система с электронным управлением**

> [!abstract] Процедура · `19-101-007`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section F - Familiarization
> **Даты:** изменён 2013-03-05
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-101-007.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-101-007.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Описание системы QSK

Топливная система QSK представляет собой электронную систему управления двигателем, предназначенную для оптимизации управления двигателем и снижения выбросов выхлопных газов. Топливная система QSK управляет скоростью двигателя и давлением топлива на основе ввода от электрического дроссельного заслонка и других специфических для оборудования и/или модели особенностей.

![[ck800wa.png]]

### Диагностические коды ошибок

Топливная система QSK может отображать и регистрировать определенные условия обнаружения неисправностей. Эти сбои отображаются в виде кодов неисправностей, что облегчает устранение неполадок. Коды неисправностей сохраняются в модуле управления двигателем (ECM).

Существует два типа кодов неисправностей: Коды неисправностей в электронной топливной системе двигателя и коды неисправностей в системе защиты двигателя.

Все коды ошибок, записанные в системе, будут либо активными (код ошибки в настоящее время активен в двигателе), либо неактивными (код ошибки был активен в одно время, но не был активен в данный момент).

![[19400328.png]]

Активные коды неисправностей можно прочитать с помощью предупреждающих (желтых) и стоп-сигналов (красных) в кабине или INSITETM.

Неактивные коды ошибок можно просматривать только с помощью INSITETM.

![[19400330.png]]

Когда замок зажигания автомобиля включается и диагностический выключатель, лампы с кодом неисправности (красный, желтый и защита двигателя) будут освещаться в течение примерно 2 секунд, одна за другой, чтобы проверить их работу.

> [!note] Примечание
> Количество неисправных ламп может быть сокращено до двух для некоторых OEM-производителей. Защита двигателя и стоп-сигналы объединены в красный цвет, а предупредительная лампа в желтый.

![[19400331.png]]

Свет будет выключен до тех пор, пока не будет записан код неисправности. Если стоп (красный) свет включается во время работы двигателя, неисправность может отключить двигатель. Остановите двигатель как можно скорее.

Если сигнальное (желтое) освещение освещается, двигатель все еще может работать, но он может потерять некоторые системные функции, которые иногда могут привести к потере мощности. Неисправность должна быть исправлена, как только это практически возможно.

Система защиты двигателя записывает отдельные коды неисправностей, когда обнаруживается состояние вне зоны действия любого из датчиков в системе защиты двигателя.

![[19400332.png]]

Чтобы проверить наличие активных кодов неисправностей, переключите переключатель зажигания автомобиля в положение выключения. Переместить диагностический переключатель в положение ON.

> [!note] Примечание
> Некоторые OEM-производители используют шортинг-плагин.

![[19400336.png]]

Переключатель зажигания транспортного средства в положение Включения. Если не будет зарегистрировано активных кодов неисправностей, все три лампочки включатся и останутся включенными. Если активные коды неисправностей будут записаны, все три лампы будут включены на мгновение. Желтые (предупреждающие) и красные (стоп) огни начнут мигать кодом зарегистрированной неисправности.

![[19400337.png]]

Код неисправности будет мигать в следующей последовательности: Во-первых, желтая (предупредительная) лампа будет мигать. Затем будет короткая 1-секундная пауза, когда выключены желтый и красный свет. Затем номера записанного кода неисправности будут мигать красным цветом. Между каждым числом будет 1-секундная пауза. Когда число будет проблескивать, снова появится желтый свет. Число будет повторяться в той же последовательности.

![[19400338.png]]

Светильники будут продолжать мигать по тому же коду неисправности, пока система не будет переведена на следующий активный код неисправности. Чтобы перейти ко второму коду неисправности, переключите переключатель настройки скорости холостого хода на «+», затем отпустите. Вы также можете вернуться к предыдущему коду ошибки, переместив переключатель на «-», а затем выпустив. Чтобы проверить третий или четвертый код ошибки, переведите переключатель на «+», а затем выпустите его, когда все активные коды ошибок были просмотрены. Переключение переключателя на «+» будет возвращаться к первому коду ошибки. Краткое объяснение всех кодов неисправностей приведено в разделе TF настоящего руководства.

![[19400339.png]]

Чтобы остановить диагностическую систему, переместить диагностический переключатель в положение OFF или удалить шортинг-розыгрыш. Переключатель зажигания транспортного средства в положение выключения.

> [!note] Примечание
> Некоторые OEM-производители используют шортинг-плагин.

![[gp8swvv.png]]

### Код ошибки Snapshot Data

Когда диагностический код неисправности записывается в ECM, данные ввода и вывода ECM регистрируются со всех датчиков и коммутаторов. Данные снимка позволяют просматривать и использовать взаимосвязи между входами и выходами ECM во время устранения неполадок.

Данные снимка с кода ошибки могут быть просмотрены только с помощью INSITETM.

![[19400349.png]]

### Система защиты двигателя

Двигатели топливной системы QSK оснащены системой защиты двигателя. Система контролирует критические температуры двигателя, уровень жидкости, положение переключателя и давление и регистрирует диагностические неисправности, когда происходит превышение или при нормальном рабочем диапазоне. Если существует вне диапазона, может быть инициировано действие разрушителя двигателя. Оператор будет предупрежден о включении лампы технического обслуживания в кабину. Предупреждающая лампа начнет мигать, когда состояние вне зоны действия будет ухудшаться, и произойдет отключение двигателя. Оператор должен тянуть в сторону дороги, когда это безопасно, чтобы уменьшить вероятность повреждения двигателя.

Система защиты двигателя мониторы:

- Температура охлаждающей жидкости
- Уровень охлаждения (необязательно)
- температура коллектора
- Масляное давление
- Охлаждающее давление (QSK45/60/78**только**)
- Давление в виде взрыва (QSK45/60/78 **только**)
- Уровень масла (QSK45/60/78**только**)
- Температура масла (QSK45/60/78 с CENSETM **только**)
- Температура топлива (QSK23/45/60/78**только**).

Система защиты двигателя мониторы для:

- Высокая температура охлаждающей жидкости
- Низкий уровень охлаждающей жидкости (необязательно)
- Высокая температура коллектора впуска
- Низкое/очень низкое давление масла
- Низкое давление охлаждающей жидкости (QSK45/60/78 **только**)
- Высокое давление в результате удара (QSK45/60/78**только**)
- Низкий уровень масла (QSK45/60/78 **только**)
- Высокая температура масла (QSK45/60/78 с CENSETM **только**)
- Высокая температура топлива (QSK23/45/60/78**только**).

В зависимости от конфигурации калибровки система защиты двигателя может иметь две выбираемые функции: Включается защита двигателя и отключение защиты двигателя. Если функция защиты двигателя отсеяна на INSITETM, то функция **не **регулируется инструментом и включена по умолчанию. Если функция защиты двигателя выбрана, мощность и скорость двигателя постепенно снижаются в зависимости от уровня тяжести наблюдаемого состояния. Если выберите функцию отключения защиты двигателя, двигатель отключится. Двигатель можно перезапустить, выключив замок зажигания, а затем снова включить.

Особенности защиты двигателя:

- Защита двигателя позволяет
- Защита двигателя отключена.

### Диаграмма потока

Топливный насос (1) извлекает топливо из топливного бака оборудования. Топливо циркулирует через топливные фильтры, прежде чем оно попадает в переключающий насос. Топливный насос регулирует давление на выходе топлива, основанное на скорости двигателя. Это регулирует давление топливного насоса, поступающее в корпус управляющего клапана (2).

Корпус управляющего клапана защищает ECM (3) от нагрева двигателя и регулирует поток топлива к таймингу и заправке железнодорожных линий (4). Линии синхронизации и заправки соединяются с топливными блоками (5) на головке цилиндра. Цилиндр имеет сверления от топливного коллектора до форсунки.

![[19400345.png]]

QSK19 Контрольное тело клапана

Корпус управляющего клапана регулирует поток топлива с помощью рельсового привода (2) синхронизации и заправочного рельсового привода (6).

Топливо поступает в корпус управляющего клапана на подаче фитинга (1). Затем топливо циркулирует вокруг приводов (2) рельсов синхронизации, регулируемых датчиком (3) давления рельсов синхронизации, и вытекает из розетки (4).

Топливо также поступает в запорный клапан (5) топлива, а затем в привод заправочного рельса (6). Затем регулятор передает топливо на датчик рельса и до розетки давления в рельсах (8).

Датчик давления топливной рельсы (7) расположен под датчиком давления рельсовой рельсы (3).

Давление топливной рельсы **не** пересекается с рельсом синхронизации.

![[19400346.png]]

Двигатели QSK23

Корпус управляющего клапана регулирует поток топлива с помощью рельсового привода (6) и заправочного рельсового привода (4).

Топливо поступает в корпус управляющего клапана на подаче фитинга (7). Затем топливо циркулирует вокруг приводов (6) рельсового синхронизатора, регулируемых датчиком (1) давления рельсового синхронизатора, и вытекает из розетки (8) рельсового синхронизатора.

Топливо также поступает в запорный клапан (10), а затем в привод заправочного рельса (4). Затем регулятор передает топливо на датчик рельса и до розетки давления в рельсах (9).

Датчик давления топливной рельсы (2) расположен под датчиком давления рельсовой рельсы (1).

Датчик 3 окружающего воздуха расположен на нижней части корпуса управляющего клапана.

Давление топливной рельсы **не** пересекается с рельсом синхронизации.

![[05400182.png]]

QSK45, QSK60 и QSK78 Control клапан Body

Корпус управляющего клапана регулирует поток топлива с помощью рельсового привода (2) синхронизации и заправочного рельсового привода (6).

Топливо поступает в корпус управляющего клапана на подаче фитинга (1). Затем топливо циркулирует вокруг приводов (2 и 9) рельсового синхронизатора, регулируемых датчиком (3) давления рельсового синхронизатора, и вытекает из рельсового синхронизатора (4).

Топливо также поступает в запорный клапан (5) топлива, а затем в привод заправочного рельса (6). Затем регулятор передает топливо на датчик рельса и до розетки давления в рельсах (8).

Датчик давления рельсов синхронизации показан слева (3). Температура топлива контролируется датчиком (10) температуры топлива, установленным над датчиком (7) давления в топливной рельсе.

![[19400975.png]]

Регулируемый поток топлива из корпуса управляющего клапана перемещается от линий синхронизации и заправки рельсового давления; через топливный блок, топливный коллектор и сверления в головке цилиндра; и доставляется в временные и заправочные рельсовые отверстия.

![[19400347.png]]

### QSK23, QSK45, QSK60 и QSK78 системные компоненты

Топливная система QSK на двигателе состоит из:

1. Топливный насос
2. Исполнительный механизм опережения впрыска
3. Датчик давления опережения впрыска
4. Клапан отсечки топлива
5. Железнодорожный привод
6. Датчик давления в топливной рампе
7. Датчик давления во впускном коллекторе
8. Датчик давления масла
9. Датчик температуры воздуха во впускном коллекторе
10. Датчик температуры охлаждающей жидкости
11. Датчик скорости двигателя
12. Датчик уровня охлаждения
13. Жгут проводов двигателя
14. Интерфейсный жгут OEM
15. Модуль управления двигателем (ECM)
16. Топливный охладитель (**не** на QSK23)
17. Датчик атмосферного давления
18. Датчик температуры топлива (**не** на QSK19)
19. Датчик давления охлаждающей жидкости (**не** показан) (**не** на QSK19 и QSK23).

![[nobox.png]]

Корпус управляющего клапана содержит исполнительные механизмы, датчик температуры топлива и датчики давления, которые контролируют время и измерение топлива на топливном форсунке.

ECM обрабатывает информацию, которую он получает от датчиков, и контролирует открытие и закрытие исполнительных механизмов. Это действие контролирует время и измерение топлива, а затем производит правильную мощность и крутящий момент для последнего состояния двигателя.

![[19400349.png]]

Ввод модуля управления двигателем

1. Датчик давления опережения впрыска
2. Датчик давления в топливной рампе
3. Датчик скорости двигателя
4. Датчик положения дроссельной заслонки
5. Выключатель подтверждения холостого хода

![[19400350.png]]

1. Датчик давления воздуха в коллекторе
2. Датчик давления масла
3. температура воздуха в коллекторе
4. Датчик температуры охлаждающей жидкости
5. Датчик уровня охлаждения
6. Датчик атмосферного давления
7. Датчик давления охлаждающей жидкости
8. Датчик температуры топлива
9. Датчик давления насоса.

![[19400709.png]]

Датчик скорости двигателя предоставляет информацию о скорости двигателя и его положении. Датчик расположен на задней стороне корпуса блока цилиндров, ниже привода аксессуара.

Датчик скорости двигателя QSK23 расположен в верхней части корпуса маховика.

![[00a00035.png]]

Датчик давления впускного коллектора и датчик температуры воздуха впускного коллектора расположены в впускном коллекторе. Датчик давления впускного коллектора контролирует положительное давление коллектора, используемое в функции управления воздушным топливом. Датчик температуры воздуха впускного коллектора измеряет температуру воздуха с турбонаддувом. Датчик температуры воздуха впускного коллектора также используется для системы защиты двигателя.

![[19400352.png]]

Датчик температуры охлаждающей жидкости двигателя предоставляет данные для оптимизированного времени сокращения выбросов и используется для системы защиты двигателя.

Датчик температуры охлаждающей жидкости расположен в корпусе термостата.

![[19400353.png]]

Датчик уровня охлаждающей жидкости, если он оборудован, устанавливается в верхнем резервуаре радиатора. Это переключатель с уровнем жидкости, необходимый для системы защиты двигателя.

> [!note] Примечание
> Это дополнительный датчик, который будет **не **на всех транспортных средствах. Шортирующая вилка будет установлена, если датчик уровня охлаждающей жидкости не используется.

![[19400354.png]]

Датчик давления масла посылает сигналы в ECM для системы защиты двигателя. Датчик находится на блоке двигателя.

![[19400355.png]]

Датчик давления охлаждающей жидкости посылает сигналы в ECM для системы защиты двигателя. Датчик находится на блоке двигателя.

> [!note] Примечание
> Это дополнительный датчик, который будет **не **на всех транспортных средствах.

![[19801042.png]]

Выходы модуля управления двигателем

ECM обрабатывает входные данные и затем контролирует эти выходные части:

1. Сроки и приводы рельсов
2. Клапан отсечки топлива
3. Исполнительный механизм топливного насоса

> [!note] Примечание
> Существуют два привода синхронизации для двигателей QSK45, QSK60 и QSK78.

![[19400356.png]]

### INSITETM Электронный сервис Описание

INSITETM, часть 3824801, является сервисным инструментом для топливной системы QuantumTM. Используйте INSITETM для:

- Владелец программы указал информацию в ECM (параметры и функции)
- Помощь в устранении неисправностей двигателя
- Измените мощность двигателя или калибровку номинальной скорости.

Ссылка на INSITETM для руководства по топливной системе QSK19.

> [!note] Примечание
> INSITE будет **только **связываться с ECM по протоколу шины данных J1587 (1708) CAN во всех системах QuantumTM и будет **не** связываться с шиной данных J1939 CAN.

![[19400357.png]]


> [!quote]- Original (English) · английский оригинал
> ### QSK System Description
>
> The QSK fuel system is an electronic engine control system designed to optimize engine control and reduce exhaust emissions. The QSK fuel system controls engine speed and fuel pressure based on input from the electric throttle and other equipment-specific and/or model-specific features.
>
> ### Diagnostic Fault Codes
>
> The QSK fuel system can display and record certain detectable fault conditions. These failures are displayed as fault codes, which makes troubleshooting easier. The fault codes are retained in the engine control module (ECM).
>
> There are two types of fault codes: engine electronic fuel system fault codes and engine protection system fault codes.
>
> All fault codes recorded will either be active (fault code is presently active on the engine) or inactive (fault code was active at one time, but **not** at the moment).
>
> Active fault codes can be read using the warning (yellow) and stop lamps (red) in the cab panel or INSITE™.
>
> Inactive fault codes can **only** be viewed with INSITE™.
>
> When the vehicle keyswitch is turned on and the diagnostic switch off, the fault code lamps (red, yellow, and engine protection) will illuminate for approximately 2 seconds, one after another, to check their operation.
>
> **Note · Примечание**
> The number of fault lamps could be reduced to two for certain OEMs. The engine protection and stop lamps are combined as red and the warning lamp as yellow.
>
> The lights will remain off until a fault code is recorded. If a stop (red) light comes on while the engine is in operation, the fault can disable the engine. Stop the engine in a safe manner as soon as possible.
>
> If the warning (yellow) light illuminates, the engine can still be operated, but it can lose some system features that can sometimes result in a power loss. The failure **must** be repaired as soon as is practicable.
>
> The engine protection system records separate fault codes when an out-of-range condition is found for any of the sensors in the engine protection system.
>
> To check for active fault codes, turn the vehicle keyswitch to the OFF position. Move the diagnostic switch to the ON position.
>
> **Note · Примечание**
> Some OEMs use a shorting plug.
>
> Turn the vehicle keyswitch to the ON position. If no active fault codes are recorded, all three lights will come on and stay on. If active fault codes are recorded, all three lights will come on momentarily. The yellow (warning) and red (stop) lights will begin to flash the code of the recorded fault.
>
> The fault code will flash in the following sequence: First, the yellow (warning) lamp will flash. Then there will be a short, 1-second pause when both the yellow and red lights are off. The numbers of the recorded fault code will then flash in red. There will be a 1-second pause between each number. When the number is done flashing, a yellow light will appear again. The number will repeat in the same sequence.
>
> The lights will continue to flash the same fault code until the system is advanced to the next active fault code. To go to the second fault code, move the idle speed adjust switch to "+," then release. You can also go back to the previous fault code by moving the switch to "-," then releasing. To check the third or fourth fault code, move the switch to "+," then release it when all active fault codes have been viewed. Moving the switch to "+" will go back to the first fault code. A brief explanation of all of the fault codes is in Section TF of this manual.
>
> To stop the diagnostic system, move the diagnostic switch to the OFF position, or remove the shorting plug. Turn the vehicle keyswitch to the OFF position.
>
> **Note · Примечание**
> Some OEMs use a shorting plug.
>
> ### Fault Code Snapshot Data
>
> When a diagnostic fault code is recorded in the ECM, ECM input and output data are recorded from all sensors and switches. Snapshot data allow the relationships between ECM inputs and outputs to be viewed and used during troubleshooting.
>
> Fault code snapshot data can **only** be viewed with INSITE™.
>
> ### Engine Protection System
>
> The QSK fuel system engines are equipped with an engine protection system. The system monitors critical engine temperatures, fluid level, switch position, and pressure and will log diagnostic faults when an over or under normal operating range condition occurs. If an out-of-range condition exists, engine derate action can be initiated. The operator will be alerted by the illumination of the in-cab maintenance lamp. The warning lamp will start to flash when out-of-range condition continues to get worse and engine shutdown will occur. The operator **must** pull to the side of the road, when it is safe to do so, to reduce the possibility of engine damage.
>
> Engine protection system monitors:
>
> - Coolant temperature
> - Coolant level (optional)
> - Intake manifold temperature
> - Oil pressure
> - Coolant pressure (QSK45/60/78 **only**)
> - Blowby pressure (QSK45/60/78 **only**)
> - Oil level (QSK45/60/78 **only**)
> - Oil temperature (QSK45/60/78 with CENSE™ **only**)
> - Fuel temperature (QSK23/45/60/78 **only**).
>
> Engine protection system monitors for:
>
> - High coolant temperature
> - Low coolant level (optional)
> - High intake manifold temperature
> - Low/very low oil pressure
> - Low coolant pressure (QSK45/60/78 **only**)
> - High blowby pressure (QSK45/60/78 **only**)
> - Low oil level (QSK45/60/78 **only**)
> - High oil temperature (QSK45/60/78 with CENSE™ **only**)
> - High fuel temperature (QSK23/45/60/78 **only**).
>
> Depending on the calibration configuration, the engine protection system can have two selectable features: Engine protection enable and engine protection shutdown. If the engine protection feature is grayed-out on INSITE™, then the feature is **not** tool adjustable and is on by default. If engine protection enable feature is selected, engine power and speed are gradually reduced, depending on the level of severity of the observed condition. If engine protection shutdown feature is selected, the engine will shut down. The engine can be restarted by turning the keyswitch off and then back on.
>
> Engine protection features:
>
> - Engine protection enable
> - Engine protection shutdown.
>
> ### Flow Diagram
>
> The fuel pump (1) draws fuel from the equipment fuel tank. The fuel circulates through the fuel filters before it enters the gear pump. The fuel pump governs the fuel output pressure, based on engine speed. This governed fuel pump pressure flows to the control valve body (2).
>
> The control valve body protects the ECM (3) from engine heat and regulates fuel flow to the timing and fueling rail lines (4). The timing and fueling lines connect to fuel blocks (5) on the cylinder head. The cylinder has drillings from the fuel manifold to the injectors.
>
> QSK19 Control Valve Body
>
> The control valve body regulates the fuel flow with timing rail actuator (2), and a fueling rail actuator (6).
>
> Fuel flows into the control valve body at the supply fitting (1). Fuel then circulates around the timing rail actuators (2), regulated by the timing rail pressure sensor (3), and flows out the timing rail outlet (4).
>
> Fuel also flows to the fuel shut off valve (5) and then to the fueling rail actuator (6). The regulator then passes fuel to the rail sensor and up to the fueling rail pressure outlet (8).
>
> The fuel rail pressure sensor (7) is located under the timing rail pressure sensor (3).
>
> The fuel rail pressure does **not** intersect with the timing rail.
>
> QSK23 Engines
>
> The control valve body regulates the fuel flow with timing rail actuator (6), and a fueling rail actuator (4).
>
> Fuel flows into the control valve body at the supply fitting (7). Fuel then circulates around the timing rail actuators (6), regulated by the timing rail pressure sensor (1), and flows out the timing rail outlet (8).
>
> Fuel also flows to the fuel shut off valve (10) and then to the fueling rail actuator (4). The regulator then passes fuel to the rail sensor and up to the fueling rail pressure outlet (9).
>
> The fuel rail pressure sensor (2) is located under the timing rail pressure sensor (1).
>
> The ambient air sensor (3) is located on the bottom of the control valve body.
>
> The fuel rail pressure does **not** intersect with the timing rail.
>
> QSK45, QSK60, and QSK78 Control Valve Body
>
> The control valve body regulates the fuel flow with timing rail actuator (2), and a fueling rail actuator (6).
>
> Fuel flows into the control valve body at the supply fitting (1). Fuel then circulates around the timing rail actuators (2 and 9), regulated by the timing rail pressure sensor (3), and flows out the timing rail outlet (4).
>
> Fuel also flows to the fuel shut off valve (5) and then to the fueling rail actuator (6). The regulator then passes fuel to the rail sensor and up to the fueling rail pressure outlet (8).
>
> The timing rail pressure sensor is shown at left (3). Fuel temperature is monitored by a fuel temperature sensor (10) mounted above the fuel rail pressure sensor (7).
>
> The regulated fuel flow from the control valve body travels from the timing and fueling rail pressure lines; through the fuel block, fuel manifold, and drillings in the cylinder head; and delivered to the timing and fueling rail orifices.
>
> ### QSK23, QSK45, QSK60, and QSK78 System Components
>
> The QSK fuel system on an engine consists of:
>
> 1. Fuel pump
> 2. Timing actuator
> 3. Timing pressure sensor
> 4. Fuel shutoff valve
> 5. Rail actuator
> 6. Rail pressure sensor
> 7. Intake manifold pressure sensor
> 8. Oil pressure sensor
> 9. Intake manifold air temperature sensor
> 10. Coolant temperature sensor
> 11. Engine speed sensor
> 12. Coolant level sensor
> 13. Engine harness
> 14. OEM interface harness
> 15. Engine control module (ECM)
> 16. Fuel cooler (**not** on QSK23)
> 17. Ambient air pressure sensor
> 18. Fuel temperature sensor (**not** on QSK19)
> 19. Coolant pressure sensor (**not** shown) (**not** on QSK19 and QSK23).
>
> The control valve body contains actuators, fuel temperature sensor, and pressure sensors that control timing and fuel metering at the injector.
>
> The ECM processes the information it receives from the sensors and controls the opening and closing of the actuators. This action controls timing and fuel metering, and then produces the correct horsepower and torque for the latest engine condition.
>
> Engine Control Module Inputs
>
> 1. Timing pressure sensor
> 2. Rail pressure sensor
> 3. Engine speed sensor
> 4. Throttle position sensor
> 5. Idle validation switch
>
> 1. Intake manifold air pressure sensor
> 2. Oil pressure sensor
> 3. Intake manifold air temperature
> 4. Coolant temperature sensor
> 5. Coolant level sensor
> 6. Ambient air pressure sensor
> 7. Coolant pressure sensor
> 8. Fuel temperature sensor
> 9. Pump pressure sensor.
>
> The engine speed sensor provides engine speed and position information. The sensor is located on the back side of the cylinder block gear housing flange, below the accessory drive.
>
> The QSK23 engine speed sensor is located in the top of the flywheel housing.
>
> The intake manifold pressure sensor and the intake manifold air temperature sensor are located in the intake manifold. The intake manifold pressure sensor monitors positive manifold pressures used in the air-fuel control function. The intake manifold air temperature sensor measures the turbocharged air temperature. The intake manifold air temperature sensor is also used for the engine protection system.
>
> The engine coolant temperature sensor provides data for optimized timing for emissions reduction, and is used for the engine protection system.
>
> The coolant temperature sensor is located in the thermostat housing.
>
> The coolant level sensor, if equipped, is mounted in the radiator top tank. It is a fluid level-actuated switch required for the engine protection system.
>
> **Note · Примечание**
> This is an optional sensor which will **not** be on all vehicles. A shorting plug will be installed if the coolant level sensor is **not** used.
>
> The oil pressure sensor sends signals to the ECM for the engine protection system. The sensor is on the engine block.
>
> The coolant pressure sensor sends signals to the ECM for the engine protection system. The sensor is on the engine block.
>
> **Note · Примечание**
> This is an optional sensor which will **not** be on all vehicles.
>
> Engine Control Module Outputs
>
> The ECM processes input data and then controls these output parts:
>
> 1. Timing and rail actuators
> 2. Fuel shutoff valve
> 3. Fuel pump actuator
>
> **Note · Примечание**
> There are **two** timing actuators for QSK45, QSK60, and QSK78 engines.
>
> ### INSITE™ Electronic Service Tool Description
>
> INSITE™, Part Number 3824801, is a service tool for the Quantum™ fuel system. Use INSITE™ to:
>
> - Program owner specified information into the ECM (parameters and features)
> - Aid in troubleshooting the engine
> - Change the engine power or rated speed calibration.
>
> Reference the INSITE™ for QSK19 Fuel System Manual.
>
> **Note · Примечание**
> INSITE will **only** communicate with the ECM over the J1587 (1708) data link protocol in all Quantum™ systems and will **not** communicate with a J1939 data link.
