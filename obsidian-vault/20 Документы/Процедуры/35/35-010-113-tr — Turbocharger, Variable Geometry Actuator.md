---
type: "Процедура"
doc: "35-010-113-tr"
title_en: "Turbocharger, Variable Geometry Actuator"
modified: "2011-10-05"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
figures: 12
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-010-113-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-010-113-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/35"
  - "перевод/машинный"
---

# Turbocharger, Variable Geometry Actuator

> [!abstract] Процедура · `35-010-113-tr`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 10 - Air Intake System - Group 10
> **Даты:** изменён 2011-10-05
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-010-113-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-010-113-tr.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Автомобильные модели CM875, CM870 и CM570

2.1.3.1.1.3.1 Трансформатор с турбокомпрессором переменной геометрии:

- Когда запускается поток рециркуляции выхлопных газов (EGR), турбокомпрессор переменной геометрии закрывает сопло в корпусе турбины, создавая большее обратное давление в выпускном коллекторе, чтобы заставить выхлопные газы вернуться в двигатель.

![[10c00065.png]]

- Турбокомпрессор также работает для улучшения производительности двигателя за счет ускорения здания быстрее во время ускорения.

![[10c00066.png]]

Турбокомпрессор с изменяемой геометрией функционирует как стандартный турбокомпрессор с добавлением следующего:

- Датчик скорости (1) в корпусе подшипника для контроля работы турбокомпрессора
- Подшипниковые кожухи с водяным охлаждением (в дополнение к масляной смазке)
- Раздвижное сопло (2) приводится в действие пневматическим приводом, прикрепленным к системе подачи воздуха транспортного средства (тормоза)
- Пневматический привод (3) управляется клапаном управления воздухом (4)
- На некоторых двигателях в линии сжатого воздуха между управляющим клапаном (4) и резервуаром (6) подачи воздуха используются фильтр и запорный клапан (5).

> [!note] Примечание
> Шум может быть слышен, когда воздух высвобождается из привода (3) через клапан (4), когда открывается турбокомпрессор с изменяемой геометрией.

![[10c00067.png]]

### Подготовительные операции

> [!danger] ОПАСНО
> При работе с пароочистителем надевайте защитные очки или щиток и защитную одежду. Горячий пар может привести к тяжёлой травме.

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- очищать паром область вокруг привода турбокомпрессора и сушить сжатым воздухом.
- Отсоедините аккумуляторные батареи.[[99-013-009 — Battery Cables and Connections|См. процедуру 013-009 в разделе 13.]]

![[ck800wa.png]]

### Снятие

Автомобильные модели CM875, CM870 и CM570

> [!warning] ОСТОРОЖНО
> Цинковый анод — жертвенная шайба, которая снижает возможность коррозии турбокомпрессора валом и втулкой. Неустановка приведет к чрезмерной коррозии и износу валовой втулки.

> [!warning] ОСТОРОЖНО
> Привод поддерживает пружинное напряжение на поперечном валу изменяемой геометрии и не может быть снят без высвобождения этого напряжения путем применения давления воздуха. Повреждение турбокомпрессора может возникнуть, если давление воздуха не будет применено до удаления привода.

Удалите линию сжатого воздуха из привода, если электронное оборудование обслуживания INSITETM не будет использоваться при удалении привода.

Удалите болты и цинковую анодную шайбу из поперечного вала турбокомпрессора.

Удалите кольцо щелчка из перекрестного вала.

![[10c00062.png]]

> [!danger] ОПАСНО
> Держите пальцы и руки подальше от привода, чтобы уменьшить вероятность получения травм в результате внезапного движения при подаче воздуха.

Используйте инструмент для электронного обслуживания INSITETM для переопределения положения привода турбокомпрессора или примените 620 кПа[90 psi] к 827 кПа[120 psi] регулируемого давления воздуха к приводу турбокомпрессора.

Удалите два болта, удерживающие привод турбокомпрессора, в корпус подшипника турбокомпрессора.

Конечная линия привода турбокомпрессора к перекрестному валу является плотной зазорной посадкой. Используйте осторожность, чтобы уменьшить возможность повреждения привода турбокомпрессора или поперечного вала турбокомпрессора при снятии привода.

Удалите привод турбокомпрессора из турбокомпрессора.

Выключите оверрайд в электронном сервисном оборудовании INSITETM или удалите регулируемый воздухоснабжение.

Удалите линию сжатого воздуха из привода турбокомпрессора, если **не** уже удалена.

![[10c00063.png]]

### Очистка и проверка при повторном использовании

Автомобильные модели CM875, CM870 и CM570

Осмотрите крепление привода, стержня и корпуса. Если привод согнут или треснут, его следует заменить.

Осмотрите втулку в конце приводного стержня, которая прикрепляется к поперечному валу турбокомпрессора для износа, забивания или другого повреждения. Замените привод, если обнаружен ущерб.

![[10c00064.png]]

Осмотрите внешний диаметр штифта турбокомпрессора. Замените турбокомпрессор, если найден износ.

| Минимум диаметра Pin |  |  |
|---|---|---|
| мм |  | в |
| 15.1 | Мин | 0.594 |

![[10c00124.png]]

### Проверка

> [!warning] ОСТОРОЖНО
> Внутри привода нет исправных деталей, не разбирать корпус привода.

Это испытание может быть выполнено с помощью привода, удаленного или установленного на турбокомпрессоре.

Прикрепите циферблатный индикатор, как показано, так что вал находится в соответствии с приводным стержнем.

Установите индикатор циферблата до нуля, без давления воздуха, приложенного к приводу.

Подключите чистый и регулируемый воздух под давлением и датчик измерения давления к приводу. Применяйте минимум 414 кПа[60 psi], чтобы убедиться, что привод работает должным образом.

Стержень должен двигаться, не прилипая.

| Диапазон движения Actuuator |  |  |
|---|---|---|
| мм |  | в |
| 12 | Мин | 0.472 |

Воздух **не должен **быть слышен, просачивающимся через функциональный привод.

Распылите мыльную воду на корпус привода, чтобы проверить наличие утечек воздуха. Замените корпус привода, если обнаружены утечки.

Заменить привод, если не обнаружено движения стержня привода, привод прилипает, или обнаружена утечка воздуха.

![[10c00081.png]]

### Установка

Автомобильные модели CM875, CM870 и CM570

> [!danger] ОПАСНО
> Держите пальцы и руки подальше от привода, чтобы уменьшить вероятность получения травм в результате внезапного движения при подаче воздуха.

Если при использовании электронного сервисного инструментария INSITETM переопределить положение привода турбокомпрессора, подсоедините линию подачи воздуха транспортного средства к приводу турбокомпрессора.

Если электронный инструмент INSITETM не используется для удаления привода, примените 620 кПа[90 psi] к 827 кПа[120 psi] регулируемого давления воздуха к приводу турбокомпрессора.

Конечная линия привода турбокомпрессора к перекрестному валу является плотной зазорной посадкой. Используйте осторожность, чтобы уменьшить возможность повреждения привода турбокомпрессора или турбокомпрессора или поперечного вала турбокомпрессора при снятии привода.

Установите на турбокомпрессор привод турбокомпрессора.

Если **не** установлен новый привод турбокомпрессора, нанесите на два болта, удерживающие привод турбокомпрессора, блокирующий резьбу клей, часть 3824040, перед установкой болтов на корпус подшипника турбокомпрессора.

> [!tip] Момент затяжки
> 17 Н·м [150 фунт-дюйм]

![[10c00063.png]]

> [!warning] ОСТОРОЖНО
> Цинковый анод — жертвенная шайба, которая снижает возможность коррозии турбокомпрессора валом и втулкой. Неустановка приведет к чрезмерной коррозии и износу валовой втулки.

Установите щелчок на поперечный вал турбокомпрессора.

Нанесите блокирующий резьбу клей, номер детали 3824040, на болты, удерживающие шайбу с цинковым анодом, прежде чем устанавливать шайбу с цинковым анодом и болты.

> [!tip] Момент затяжки
> 23 Н·м [204 фунт-дюйм]

Выключите оверрайд в электронном сервисном оборудовании INSITETM или удалите регулируемый воздухоснабжение.

Если **не** уже установлен, установите линию сжатого воздуха на привод турбокомпрессора.

Запуск и эксплуатация двигателя.

Проверьте правильную работу и проверьте наличие утечек воздуха.

![[10c00062.png]]

### Завершающие операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Подсоедините аккумуляторные батареи.[[99-013-009 — Battery Cables and Connections|См. процедуру 013-009 в разделе 13.]]
- Запустите двигатель и проверьте на отсутствие утечек.

![[ck800wa.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> Automotive with CM875, CM870 and CM570
>
> Variable geometry turbocharger purpose:
>
> - When the exhaust gas recirculation (EGR) flow is commanded, the variable geometry turbocharger closes the nozzle in the turbine housing, creating more back pressure in the exhaust manifold to force exhaust gas back into the engine.
>
> - The turbocharger also functions to improve engine performance by building boost more quickly during acceleration.
>
> The variable geometry turbocharger functions as a standard turbocharger, with the addition of the following:
>
> - A speed sensor (1) in the bearing housing to monitor turbocharger operation
> - Water-cooled bearing housings (in addition to oil lubrication)
> - A sliding nozzle (2) is actuated by a pneumatic actuator attached to the vehicle (brake) air supply system
> - A pneumatic actuator (3) is operated by an air control valve (4)
> - On some engines, a filter and shutoff valve (5) are used in the air line between the control valve (4) and the air supply tank (6).
>
> **Note · Примечание**
> A noise can be heard as air is released from the actuator (3), through the control valve (4), when the variable geometry turbocharger mechanism opens.
>
> ### Preparatory Steps
>
> **WARNING · Опасно**
> When using a steam cleaner, wear safety glasses or a face shield, as well as protective clothing. Hot steam can cause serious personal injury.
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Steam clean the area around the turbocharger actuator and dry with compressed air.
> - Disconnect the batteries. [[99-013-009 — Battery Cables and Connections|Refer to Procedure 013-009 in Section 13.]]
>
> ### Remove
>
> Automotive with CM875, CM870 and CM570
>
> **CAUTION · Осторожно**
> The zinc anode is a sacrificial washer that reduces the possibility of corrosion of the turbocharger cross-shaft and bushing. The failure to install will result in excessive corrosion and wear to the cross-shaft bushing.
>
> **CAUTION · Осторожно**
> The actuator maintains a spring tension on the variable geometry cross-shaft and can not be removed without releasing this tension by applying air pressure. Damage to the turbocharger can possibly result if air pressure is not applied before removing the actuator.
>
> Remove the air line from the actuator if INSITE™ electronic service tool will **not** be used in the removal of the actuator.
>
> Remove the capscrew and zinc anode washer from the turbocharger cross-shaft.
>
> Remove the snap ring from the cross-shaft.
>
> **WARNING · Опасно**
> Keep fingers and hands away from the actuator link to reduce the possibility of personal injury as a result of sudden movement when air is supplied.
>
> Use INSITE™ electronic service tool to override the turbocharger actuator position or apply 620 kPa \[90 psi\] to 827 kPa \[120 psi\] of regulated air pressure to the turbocharger actuator.
>
> Remove the two capscrews holding the turbocharger actuator to the turbocharger bearing housing.
>
> The turbocharger actuator end link to cross-shaft is a tight clearance fit. Use care to reduce the possibility of damaging the turbocharger actuator or the turbocharger cross-shaft when removing the actuator.
>
> Remove the turbocharger actuator from the turbocharger.
>
> Turn off the override in INSITE™ electronic service tool or remove the regulated air supply.
>
> Remove the air line from the turbocharger actuator, if **not** already removed.
>
> ### Clean and Inspect for Reuse
>
> Automotive with CM875, CM870 and CM570
>
> Inspect the actuator mounting bracket, rod, and body. If the actuator is bent or cracked, it **must** be replaced.
>
> Inspect the bushing in the actuator rod end that attaches to the turbocharger cross-shaft for wear, scoring, or other damage. Replace the actuator if damage is found.
>
> Inspect the outside diameter of the turbocharger cross-shaft pin. Replace the turbocharger if wear is found.
>
> | Cross-shaft Pin Minimum Diameter |  |  |
> |---|---|---|
> | mm |  | in |
> | 15.1 | MIN | 0.594 |
>
> ### Test
>
> **CAUTION · Осторожно**
> There are no serviceable parts inside the actuator, do not disassemble the actuator body.
>
> This test can be performed with the actuator removed or installed on the turbocharger.
>
> Attach a dial indicator as shown, so the shaft is in line with the actuator rod.
>
> Set the dial indicator to zero, with no air pressure applied to the actuator.
>
> Connect clean and regulated pressurized air and a pressure gauge to the actuator. Apply a minimum of 414 kPa \[60 psi\] to make sure the actuator is functioning properly.
>
> The rod **must** move without sticking.
>
> | Actuator Movement Range |  |  |
> |---|---|---|
> | mm |  | in |
> | 12 | MIN | 0.472 |
>
> Air **must not** be heard leaking through a functional actuator.
>
> Spray soapy water on the actuator housing to check for air leaks. Replace the actuator housing if leaks are found.
>
> Replace the actuator if no movement of the actuator rod is detected, the actuator is sticking, or an air leak is found.
>
> ### Install
>
> Automotive with CM875, CM870 and CM570
>
> **WARNING · Опасно**
> Keep fingers and hands away from the actuator link to reduce the possibility of personal injury as a result of sudden movement when air is supplied.
>
> If using INSITE™ electronic service tool to override the turbocharger actuator position, connect the vehicle air supply line to the turbocharger actuator.
>
> If INSITE™ electronic service tool is **not** being used to remove the actuator, apply 620 kPa \[90 psi\] to 827 kPa \[120 psi\] of regulated air pressure to the turbocharger actuator.
>
> The turbocharger actuator end link to cross-shaft is a tight clearance fit. Use care to reduce the possibility of damaging the turbocharger actuator or the turbocharger or the turbocharger cross-shaft when removing the actuator.
>
> Install the turbocharger actuator onto the turbocharger.
>
> If **not** installing a new turbocharger actuator, apply Threadlocker, Part Number 3824040, onto the two capscrews holding the turbocharger actuator before installing the capscrews onto the turbocharger bearing housing.
>
> **Момент затяжки · Torque Value**
> 17 n•m [150 in-lb]
>
> **CAUTION · Осторожно**
> The zinc anode is a sacrificial washer that reduces the possibility of corrosion of the turbocharger cross-shaft and bushing. The failure to install will result in excessive corrosion and wear to the cross-shaft bushing.
>
> Install the snap ring onto the turbocharger cross-shaft.
>
> Apply Threadlocker, Part Number 3824040, onto the capscrew holding the zinc anode washer before installing the zinc anode washer and the capscrew.
>
> **Момент затяжки · Torque Value**
> 23 n•m [204 in-lb]
>
> Turn off the override in INSITE™ electronic service tool or remove the regulated air supply.
>
> If **not** already installed, install the air line to the turbocharger actuator.
>
> Start and operate the engine.
>
> Verify proper operation and check for air leaks.
>
> ### Finishing Steps
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Connect the batteries. [[99-013-009 — Battery Cables and Connections|Refer to Procedure 013-009 in Section 13.]]
> - Operate the engine and check for leaks.
