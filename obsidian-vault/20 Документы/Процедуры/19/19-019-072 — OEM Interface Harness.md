---
aliases:
  - "Интерфейсный жгут OEM"
type: "Процедура"
doc: "19-019-072"
title_en: "OEM Interface Harness"
title_ru: "Интерфейсный жгут OEM"
modified: "2003-01-09"
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
figures: 37
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-072.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-072.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# OEM Interface Harness
**Интерфейсный жгут OEM**

> [!abstract] Процедура · `19-019-072`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-01-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-072.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-072.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Двигатели, оснащенные QSK, используют три отдельных жгута для управления двигателем и некоторыми операциями транспортного средства.

1. Жгут проводов двигателя
2. Интерфейсный жгут OEM
3. Упряжка для проводов OEM.

![[19400385.png]]

Замените проводную упряжку, если есть открытая цепь или короткое замыкание, обнаруженное под защитным покрытием корпуса проводной упряжки.

![[19400386.png]]

### Снятие

Двигатели QSK19

Удалите трубки подачи топлива из верхней части корпуса клапана управления, чтобы получить доступ к OEM-интерфейсу проводов. См. процедуру 006-024 в Руководстве по устранению неполадок и ремонту, Двигатели серии QSK19, Вестник 3666098.

![[19801071.png]]

Отсоедините 21- и 31-контактные разъёмы от электропроводки OEM.

![[19400399.png]]

Отключите 2- и 6-контактные разъемы Deutsch.

![[19801070.png]]

Удалите 21- и 31-контактные разъёмы из опорных скобок проводов.

![[19400400.png]]

Используйте 4-мм \[5/32-в\] шестиугольник головного ключа для отключения OEM интерфейса проводов ремня разъема Deutsch от ECM.

![[19400401.png]]

Удалите шесть проводных связей из опорной кронштейна проводов и удалите опорную кронштейн OEM-интерфейса проводов из двигателя.

![[19801079.png]]

Двигатели QSK23

Удалите p-затворы (1) и скобки (2) вблизи нижней части ECM вблизи датчика давления окружающего воздуха (3).

![[19401009.png]]

Удалите восемь проводных связей, обеспечивающих электропроводку OEM-привода, в электропривод двигателя.

Отсоедините разъём B (1) от ECM.

![[19401017.png]]

Отсоедините разъем шины данных CAN (1), соединяющий OEM-проводку с электропроводкой двигателя.

Удалите p-клипы (2) в нижнем правом углу крышки с краном № 5.

Удалите соединительные гайки, закрепляющие 21- и 31-контактные разъёмы (3, 4) в скобке.

Удалите четыре болта (5), закрепив 9-контактный разъем Deutsch к скобке.

Удалите проводку OEM.

![[19401018.png]]

QSK45 и QSK60

Снимите сборку коробки для передышки.

- Освободите два шланговых зажима (1) и отсоедините два шланга (2) на дне коробки для передышки (3).
- Устраните зажим шланга (4) и отсоедините шланг датчика давления продувки (5).
- Освободите зажим шланга (6) и отсоедините нижний шланг для дыхания (7).
- Удалите шесть крепежных болтов (8) и коробку для передышки.

![[19400773.png]]

Используйте 4-мм \[5/32-в\] шестиугольник головного ключа для отключения OEM интерфейса проводов ремня разъема Deutsch от ECM.

![[19400401.png]]

Отключите три разъема шины данных CAN.

![[19400770.png]]

Удалите винты, крепящие три держателя предохранителей, из кронштейна ремня жгута двигателя.

![[19400776.png]]

Если CENSE оборудован, отсоедините проводку OEM-интерфейса от проводной ремни CENSETM.

> [!note] Примечание
> На двигателях, не оборудованных CENSETM, разъемы CENSETM будут соединены друг с другом и должны оставаться такими для правильной работы.

![[19400777.png]]

Отсоедините 21- и 31-контактные разъёмы от электропроводки OEM.

![[19400399.png]]

Удалите 21- и 31-контактные разъёмы OEM-интерфейса из опорной скобки для поддержки проводов двигателя.

![[19400400.png]]

Удалите шесть гаек, удерживающих три проводных зажима, которые обеспечивают безопасность проводов OEM-интерфейса.

Удалите OEM-интерфейс проводов из двигателя.

Отделите и удалите зажимы проводов из OEM-интерфейса проводов.

![[19400778.png]]

### Установка

Двигатели QSK19

Кормить шесть проводных связей через зажимы проводов упряжкой опоры скобки.

![[19801080.png]]

Подключите OEM-интерфейс проводов ремня Deutsch к разъему ECM. Затяните винт с помощью 4-мм \[5/32-в\] шестиугольного головного гаечного ключа.

> [!tip] Момент затяжки
> 3 Н·м [27 фунт-дюйм]

![[19400401.png]]

Пристегните жгут проводов к поддерживающим скобкам жгута провода с помощью проводных стяжек.

![[19801081.png]]

Установите 21- и 31-контактные разъемы к поддерживающим кронштейнам проводов.

> [!tip] Момент затяжки
> 16 Н·м [142 фунт-дюйм]

![[19400400.png]]

Подключите 21- и 31-контактные разъемы к OEM-проводах.

![[19400399.png]]

Подключите 2- и 6-контактные разъемы Deutsch.

![[19801082.png]]

Установите трубки подачи топлива на верхнюю часть корпуса управляющего клапана. См. процедуру 006-024 в Руководстве по устранению неполадок и ремонту, Двигатели серии QSK19, Вестник 3666098.

![[19801083.png]]

Двигатели QSK23

Установите OEM проводку.

Установите четыре болта (5), закрепляющие 9-контактный разъем к скобке.

Установите соединительные гайки, закрепляющие 21- и 31-контактные разъёмы (3, 4) к скобке.

Установите p-клипы (2) рядом с нижним правым углом крышки крана № 5.

Подключите шину (1) передачи данных CAN от ремня электропроводки двигателя к ремню электропроводки OEM.

![[19401018.png]]

Подключите разъём B (1) к ECM.

Установите восемь проводных связей, обеспечивающих электропроводку OEM-привода к электропроводке двигателя.

![[19401023.png]]

Установите p-затворы (1) и скобки (2) вблизи нижней части ECM вблизи датчика давления окружающего воздуха (3).

![[19401009.png]]

QSK45 и QSK60

Поместите OEM-интерфейс проводов в три провода зажимы.

Установите три проводных зажима на опорную кронштейн проводов двигателя, используя шесть крепящих гаек для закрепления зажимов.

![[19400778.png]]

Установите интерфейс OEM-проводов 21- и 31-контактных разъемов на подлокотнике поддержки проводов двигателя.

![[19400400.png]]

Подключите 21- и 31-контактные разъёмы OEM-интерфейса к OEM-проводах.

![[19400399.png]]

Если CENSE оборудован, подключите OEM-интерфейс к проводной ремне CENSETM.

> [!note] Примечание
> На двигателях, не оборудованных CENSETM, разъемы CENSETM будут соединены друг с другом и должны оставаться такими для правильной работы.

![[19400777.png]]

Закрепите три держателя предохранителей на подлокотнике опорной кронштейна проводов двигателя.

![[19400776.png]]

Подключите три разъема шины данных CAN к проводах OEM-интерфейса.

![[19400770.png]]

Подключите OEM-интерфейс проводов ремня Deutsch к разъему ECM. Затяните винт с помощью 4-мм \[5/32-дюймовый\] шестиугольного головного гаечного ключа.

> [!tip] Момент затяжки
> 3 Н·м [27 фунт-дюйм]

![[19400401.png]]

Установите сборку дыхательной коробки.

- Подключите коробку передышки к кронштейну поддержки проводов с шестью болтами (8).

> [!tip] Момент затяжки
> 45 Н·м [33 фунт-фут]

- Соедините нижний дыхательный шланг (7) с зажимом шланга (6).
- Подсоедините шланг датчика давления (5) с зажимом шланга (4).
- Соедините два шланга (2) на дне коробки для передышки (3) с двумя шлангами (1).

![[19400773.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> QSK-equipped engines use three separate wiring harnesses to control the engine and some of the vehicle operations.
>
> 1. Engine harness
> 2. OEM interface harness
> 3. OEM harness.
>
> Replace a harness if there is an open circuit or a short circuit found under the protective covering of the harness body.
>
> ### Remove
>
> QSK19 Engines
>
> Remove the fuel supply tubes from the top of the control valve body to gain access to the OEM interface harness. Refer to Procedure 006-024 in the Troubleshooting and Repair Manual, QSK19 Series Engines, Bulletin 3666098.
>
> Disconnect the 21- and 31-pin connectors from the OEM harness.
>
> Disconnect the 2- and 6-pin Deutsch connectors.
>
> Remove the 21- and 31-pin connectors from the harness support brackets.
>
> Use a 4-mm \[5/32-in\] hexagon head wrench to disconnect the OEM interface harness Deutsch connector from the ECM.
>
> Remove the six wire ties from the harness support bracket and remove the OEM interface harness from the engine.
>
> QSK23 Engines
>
> Remove the p-clips (1) and bracket (2) near the bottom of the ECM near the ambient air pressure sensor (3).
>
> Remove the eight wire ties securing the OEM harness to the engine harness.
>
> Disconnect connector B (1) from the ECM.
>
> Disconnect the datalink connector (1) connecting the OEM harness to the engine harness.
>
> Remove the p-clips (2) near the lower right corner of the number 5 cam follower cover.
>
> Remove the connector nuts securing the 21- and 31-pin connectors (3, 4) to the bracket.
>
> Remove the four capscrews (5) securing the 9-pin Deutsch connector to the bracket.
>
> Remove the OEM harness.
>
> QSK45 and QSK60
>
> Remove the breather box assembly.
>
> - Loosen the two hose clamps (1) and disconnect the two hoses (2) on the bottom of the breather box (3).
> - Loosen the hose clamp (4) and disconnect the blowby pressure sensor hose (5).
> - Loosen the hose clamp (6) and disconnect the lower breather hose (7).
> - Remove the six attaching bolts (8) and the breather box assembly.
>
> Use a 4-mm \[5/32-in\] hexagon head wrench to disconnect the OEM interface harness Deutsch connector from the ECM.
>
> Disconnect the three datalink connectors.
>
> Remove the screws attaching the three fuse holders from the engine wiring harness bracket.
>
> If CENSE™-equipped, disconnect the OEM interface harness from the CENSE™ harness.
>
> **Note · Примечание**
> On engines **not** equipped with CENSE™, the CENSE™ connectors will be connected to each other and **must** remain that way for proper operation.
>
> Disconnect the 21- and 31-pin connectors from the OEM harness.
>
> Remove the 21- and 31-pin OEM interface harness connectors from the engine harness support bracket.
>
> Remove the six nuts holding the three wire clamps that secure the OEM interface harness.
>
> Remove the OEM interface harness from the engine.
>
> Separate and remove the wire clamps from the OEM interface harness.
>
> ### Install
>
> QSK19 Engines
>
> Feed six wire ties through the clips of the harness support bracket.
>
> Connect the OEM interface harness Deutsch connector to the ECM. Tighten the screw using a 4-mm \[5/32-in\] hexagon head wrench.
>
> **Момент затяжки · Torque Value**
> 3 n•m [27 in-lb]
>
> Fasten the harness to the harness support brackets using wire ties.
>
> Install the 21- and 31-pin connectors to the harness support brackets.
>
> **Момент затяжки · Torque Value**
> 16 n•m [142 in-lb]
>
> Connect the 21- and 31-pin connectors to the OEM harness.
>
> Connect the 2- and 6-pin Deutsch connectors.
>
> Install the fuel supply tubes to the top of the control valve body. Refer to Procedure 006-024 in the Troubleshooting and Repair Manual, QSK19 Series Engines, Bulletin 3666098.
>
> QSK23 Engines
>
> Install the OEM harness.
>
> Install the four capscrews (5) securing the 9-pin connector to the bracket.
>
> Install the connector nuts securing 21- and 31-pin connectors (3, 4) to the bracket.
>
> Install the p-clips (2) near the lower right corner of the number 5 cam follower cover.
>
> Connect the datalink (1) connector from the engine harness to the OEM harness.
>
> Connect connector B (1) to the ECM.
>
> Install the eight wire ties securing the OEM harness to the engine harness.
>
> Install the p-clips (1) and bracket (2) near the bottom of the ECM near the ambient air pressure sensor (3).
>
> QSK45 and QSK60
>
> Position the OEM interface harness into the three wire clamps.
>
> Install the three wire clamps on the engine harness support bracket, using the six attaching nuts to secure the clamps.
>
> Install the OEM interface harness 21- and 31-pin connectors on the engine harness support bracket.
>
> Connect the 21- and 31-pin OEM interface harness connectors to the OEM harness.
>
> If CENSE™-equipped, connect the OEM interface harness to the CENSE™ harness.
>
> **Note · Примечание**
> On engines **not** equipped with CENSE™, the CENSE™ connectors will be connected to each other and **must** remain that way for proper operation.
>
> Secure the three fuse holders to the engine harness support bracket.
>
> Connect the three datalink connectors to the OEM interface harness.
>
> Connect the OEM interface harness Deutsch connector to the ECM. Tighten the screw using a 4-mm \[5/32-inch\] hexagon head wrench.
>
> **Момент затяжки · Torque Value**
> 3 n•m [27 in-lb]
>
> Install the breather box assembly.
>
> - Connect the breather box to the harness support bracket with six bolts (8).
>
> **Момент затяжки · Torque Value**
> 45 n•m [33 ft-lb]
>
> - Connect the lower breather hose (7) with the hose clamp (6).
> - Connect the blowby pressure sensor hose (5) with the hose clamp (4).
> - Connect the two hoses (2) on the bottom of the breather box (3) with the two hose clamps (1).
