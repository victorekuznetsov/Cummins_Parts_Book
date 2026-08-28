---
type: "Процедура"
doc: "98-101-025"
title_en: "CENTRY™ System"
modified: "2003-03-24"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 10
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-101-025.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-101-025.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# CENTRY™ System

> [!abstract] Процедура · `98-101-025`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section F - Familiarization
> **Даты:** изменён 2003-03-24
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-101-025.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-101-025.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Система CENTRYTM представляет собой интеллектуальную электронную систему управления двигателем, предназначенную для оптимизации управления двигателем на горнодобывающей, строительной, сельскохозяйственной и другой внедорожной технике. Эта система может быть применена ко всем моделям двигателей, использующих топливную систему PT®. Система CENTRYTM управляет скоростью двигателя и давлением топлива на основе ввода от электронного дроссельной заслонки и других специфических для оборудования и/или модели двигателя особенностей.

Система CENTRYTM состоит из гидромеханических и электронных подсистем. Электронная подсистема управляет доставкой топлива с использованием электронного клапана управления топливом (EFC), в то время как гидромеханическая подсистема обеспечивает максимальную защиту крутящего момента и скорости двигателя.

![[19801556.png]]

### Описание системы CENTRYTM

Гидромеханическая подсистема

**Гидромеханическая подсистема**

Эта подсистема содержит:

1. Топливный насос

  1. Электронный модуль управления топливом
  2. Резервный управляющий механика
  3. Управление воздушным топливом.

1. Клапан отсечки топлива
2. Топливные трубки
3. Топливный блок (маунт датчика давления на железной дороге)
4. Шаг синхронизации контроля
5. форсунка.

![[19801557.png]]

Топливный насос является основной частью гидромеханической подсистемы, поскольку он обеспечивает давление топлива, контролируемое электронным клапаном управления топливом. Механический регулятор для топливного насоса обеспечивает резервное максимальное управление крутящим моментом двигателя и скоростью.

![[19801558.png]]

Управление воздушным топливом топливного насоса использует линию давления наддува турбокомпрессора для регулирования давления топлива, подаваемого в электронный клапан управления топливом. Управление воздушным топливом уменьшает черный дым и улучшает работу двигателя в условиях низкой нагрузки.

![[19801559.png]]

Контроль за воздушным топливом, установка NO-AIR - это максимальное давление рельсов топлива, которое топливный насос может подавать, когда на линии измерения давления наддува не обнаруживается давление наддува. Следующий график показывает типичную кривую перехода давления рельса против ускорения давления наддува. Управление воздушным топливом позволяет увеличить максимальное доступное давление на топливных рельсах по мере увеличения давления наддува.

![[19801560.png]]

Многие модели двигателей используют клапан отключения топлива, имеющий ручной винт переопределения. Включение этого винта перекрывает запорный клапан и/или системы отключения, подключенные к запорному клапану топлива.

> [!note] Примечание
> Этот винт не переопределяет электронный клапан управления топливом в системе CENTRYTM.

![[19801561.png]]

Система CENTRYTM использует топливный блок для обеспечения надежного расположения датчика давления на рельсах.

![[19801562.png]]

На моделях двигателей, использующих STC, некоторые двигатели будут использовать линию измерения давления топлива для управления гидромеханическим переключателем управления временем шага, а другие двигатели будут использовать систему CENTRYTM для переключения электронного управления временем шага соленоида.

Идентификация контроля времени шага:

1. Линия датчика давления топлива
2. Масляная линия к Таппетам
3. Масляная вентиляция
4. Линия поставок масла
5. Провода привода CENTRYTM STC.

STC позволяет двигателю работать в расширенном режиме впрыска сразу после запуска и в условиях легкой нагрузки двигателя и вернуться к нормальному времени во время средних и высоких условий нагрузки двигателя. Преимущества этой функции включают в себя:

1. Улучшенные характеристики холостого хода
2. Сниженный холодный белый дым
3. Улучшенная экономия топлива при легкой нагрузке.

![[19801563.png]]

Гидромеханический STC позволяет использовать два различных режима впрыска, основанных на давлении рельсов топлива, обнаруженном на линии измерения давления топлива. Hysterisis обеспечивает максимальное давление на рельсах для двигателя, чтобы перейти от ADVANCEDTM к нормальному времени и минимальное давление на рельсах для перехода от нормального к ADVANCEDTM. Hysterisis предотвращает нестабильное и быстрое переключение режимов времени STC, когда двигатель работает при давлениях рельсов в диапазоне давления рельсов гистеризиса.

![[19801564.png]]

Электронный STC CENTRYTM также позволяет использовать два различных режима впрыска, основанных на измеренном давлении на рельсах и скорости двигателя. Однако CENTRYTM имеет возможность обеспечивать два различных набора точек переключения STC на рельсах выше и ниже калиброванной точки скорости двигателя. Это обеспечивает дальнейшую оптимизацию производительности двигателя с помощью STC. ECM обеспечивает 12- или 24-VDC электронному приводу STC, когда он управляет режимом времени ADVANCEDTM.

![[19801565.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The CENTRY™ system is an intelligent electronic engine control system designed to optimize engine control on mining, construction, agriculture, and other off-highway equipment. This system can be applied to all engine models that use the PT® fuel system. The CENTRY™ system controls engine speed and fuel pressure based on input from the electronic throttle and other equipment-specific and/or engine-model-specific features.
>
> The CENTRY™ system consists of hydromechanical and electronic subsystems. The electronic subsystem manages fuel delivery using an electronic fuel control (EFC) valve while the hydromechanical subsystem provides backup maximum engine torque and speed protection.
>
> ### CENTRY™ System Description
>
> Hydromechanical Subsystem
>
> **Hydromechanical Subsystem**
>
> This subsystem contains:
>
> 1. Fuel Pump
>
>   1. Electronic Fuel Control Module Assembly
>   2. Backup Mechanical Governor
>   3. Air-Fuel Control.
>
> 1. Fuel Shutoff Valve
> 2. Fuel Tubes
> 3. Fuel Block (Rail Pressure Sensor Mount)
> 4. Step Timing Control
> 5. Injectors.
>
> The fuel pump is the main part of the hydromechanical subsystem because it supplies the fuel pressure controlled by the electronic fuel control valve. The mechanical governor for the fuel pump provides backup maximum engine torque and speed control.
>
> The fuel pump air-fuel control uses a turbocharger boost pressure line to regulate the fuel pressure supplied to the electronic fuel control valve. The air-fuel control reduces black smoke and improves engine performance during low-boost conditions.
>
> The air-fuel control, NO-AIR setting is the maximum fuel rail pressure that the fuel pump can supply when no boost pressure is detected on the boost pressure sensing line. The following graph shows a typical rail pressure versus boost pressure acceleration transition curve. The air-fuel control allows the maximum available fuel rail pressure to increase as boost pressure increases.
>
> Many engine models use a fuel shutdown valve having a manual override screw. Turning this screw in overrides the shutdown valve and/or shutdown systems connected to the fuel shutoff valve.
>
> **Note · Примечание**
> This screw does **not** override the electronic fuel control valve in the CENTRY™ system.
>
> The CENTRY™ system uses a fuel block to provide a solid location for the rail pressure sensor.
>
> On engine models that use STC, some engines will use a fuel pressure sensing line to control a hydromechanical step timing control switch and other engines will use the CENTRY™ system to switch an electronic step timing control solenoid.
>
> Step Timing Control Identification:
>
> 1. Fuel Pressure Sensing Line
> 2. Oil Line to the Tappets
> 3. Oil Vent Line
> 4. Oil Supply Line
> 5. CENTRY™ STC Actuator Lead Wire.
>
> STC allows the engine to operate in advanced injection timing immediately after start-up and light-duty engine load conditions and to return to normal timing during medium and high engine load conditions. The benefits of this feature include:
>
> 1. Improved cold weather idling characteristics
> 2. Reduced cold weather white smoke
> 3. Improved light-load fuel economy.
>
> The hydromechanical STC allows two different injection timing modes based on fuel rail pressure detected on the fuel pressure sensing line. Hysterisis provides the maximum rail pressure for the engine to shift from ADVANCED™ to normal timing and the minimum rail pressure for a shift from normal to ADVANCED™ timing. Hysterisis prevents unstable and rapid switching of STC timing modes when the engine is operating at rail pressures within the hysterisis rail pressure range.
>
> The CENTRY™ electronic STC also allows two different injection timing modes based on measured rail pressure and engine speed. However, CENTRY™ has the capability to provide two different sets of rail pressure STC switch points above and below a calibrated engine speed point. This provides further optimization of engine performance with STC. The ECM provides 12- or 24-VDC to the electronic STC actuator when it is commanding ADVANCED™ timing mode.
