---
type: "Процедура"
doc: "10-101-001-om-auto"
title_en: "Engine Braking System"
modified: "2006-05-10"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
manuals:
  - "3666251"
  - "4960314"
figures: 39
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-101-001-om-auto.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-101-001-om-auto.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSX15"
  - "группа/10"
  - "перевод/машинный"
---

# Engine Braking System

> [!abstract] Процедура · `10-101-001-om-auto`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Входит в руководства:** [[3666251 — Signature and ISX Operation and Maintenance Manual|3666251]], [[4960314 — ISX Owners Manual|4960314]]
> **Секции:** Section 1 - Operating Instructions
> **Даты:** изменён 2006-05-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-101-001-om-auto.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-101-001-om-auto.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

> [!warning] ОСТОРОЖНО
> Не превышайте регулируемую скорость двигателя при работе тормозов двигателя. Может произойти повреждение двигателя. Тормоза двигателя предназначены для того, чтобы помочь рабочим тормозам транспортного средства замедлить транспортное средство.

![[nobox.png]]

Двигатели Signature и ISX оснащены системой IntebrakeTM (двигательные тормоза).

Тормоза двигателя используют энергию сжатия двигателя для обеспечения замедления транспортного средства путем преобразования двигателя в энергопоглощающее устройство для снижения скорости транспортного средства. Это достигается гидравлической схемой, которая открывает выпускные клапаны вблизи конца хода сжатия.

Изделие ISX CM870 и более новое используют дополнительное преимущество турбокомпрессора с изменяемой геометрией для торможения двигателя.

![[17c00015.png]]

Количество тормозной мощности, доступной на этом двигателе, составляет до 600 л.с. Тормозная способность управляется системой IntebrakeTM (двигательные тормоза).

![[17c00010.png]]

> [!warning] ОСТОРОЖНО
> Не работайте с двигателем, если тормоза двигателя не отключаются. Это приведет к серьезным повреждениям двигателя.

Если тормоза двигателя **не **выключаются, немедленно выключите двигатель и обратитесь в авторизованный ремонтный центр Cummins.

![[17c00172.png]]

Контроль тормозов двигателя состоит из следующих элементов:

- Шестипозиционный или трехпозиционный селекторный переключатель
- Выключатель on/off
- Переключатель сцепления
- Датчик дроссельной заслонки
- Регулятор рабочего тормоза.

![[17c00012.png]]

Другими переключателями для круиз-контроля, которые влияют на работу тормозов двигателя, являются:

- Круиз-контроль включения/выключения и переключения установки/резюме (если тормоза двигателя в функции круиз-контроля отключены)
- Обслуживание тормоза переключателя давления воздуха.

Тормоза двигателя могут работать, пока включен круиз-контроль. Электронная функция, торможение двигателя с управлением вентилятором, может быть включена для включения вентилятора во время торможения двигателя. Это увеличивает паразитарную нагрузку на двигатель при торможении. См. Программируемые функции в этом разделе.

![[es8bdga.png]]

> [!note] Примечание
> Некоторые производители предпочитают использовать трехпозиционный переключатель.

Шестипозиционный селекторный переключатель расположен рядом с выключателем в кабине и позволяет выбирать тормозную мощность от одного до шести тормозов.

![[17c00014.png]]

Технические характеристики тормозов двигателя:

Позиция "нет". 1 = 17% тормозной способности двигателя.

Позиция "нет". 2 = 33-процентная мощность торможения двигателя.

Позиция "нет". 3 = 50-процентная мощность торможения двигателя.

Позиция "нет". 4 = 67% тормозной способности двигателя.

Позиция "нет". 5 = 83-процентная мощность торможения двигателя.

Позиция "нет". 6 = 100-процентная мощность торможения двигателя.

> [!note] Примечание
> Для OEM-производителей, использующих трехпозиционный переключатель, спецификации уровня тормозов: Позиция "нет". 1 = 33-процентная мощность торможения двигателя. Позиция "нет". 2 = 67% тормозной способности двигателя. Позиция "нет". 3 = 100-процентная мощность торможения двигателя.

Для ISX CM870 и более новых продуктов выключатель выбора тормозов двигателя не всегда напрямую коррелирует с количеством активированных соленоидов тормозов двигателя. Это связано с дополнительным использованием турбокомпрессора с изменяемой геометрией для торможения двигателя и использованием только двух соленоидов тормоза двигателя.

![[17c00033.png]]

> [!note] Примечание
> Любой из этих переключателей может отключить тормоза двигателя. Если тормоза двигателя в функции круиз-контроля включены, переключатель круиз-контроля, PTO переключатели или оба будут **не **отключать тормоза двигателя.

С двигателем сигналы от переключателя включения / выключения, переключателя сцепления, датчика дроссельной заслонки и переключателя круиз-контроля, переключателей PTO или обоих подаются в электронный модуль управления.

![[17c00013.png]]

> [!note] Примечание
> Тормоза двигателя могут быть включены **не**:

Затем ECM электронно включает или отключает тормоза двигателя.

1. При активном круиз-контроле, если тормоза двигателя в функции круиз-контроля отключены
2. Когда скорость двигателя опускается ниже 850 об/мин или 30 миль в час
3. Когда активен электронный код неисправности
4. Когда педаль сцепления находится в депрессии
5. Когда педаль дросселя находится в депрессии
6. Когда PTO или удаленный PTO активен.

![[17c00015.png]]

Датчик положения дроссельной заслонки является частью педали акселератора, расположенной в кабине, и будет отключать тормоза двигателя при подавлении.

![[ea8swva.png]]

Переключатель сцепления использует движение соединения сцепления для отключения тормозов двигателя, когда педаль сцепления находится в подавленном состоянии. Угнетение сцепления во время круиз-контроля приведет к отключению круиз-контроля.

![[cl8swva.png]]

Переключатель рабочего тормоза прикрепляется к линии подачи воздуха рабочего тормоза.

Применение служебных тормозов во время круиз-контроля отключит круиз-контроль и позволит тормозам двигателя.

Если включена функция тормоза двигателя с педалью, педаль рабочего тормоза должна быть нажата до того, как будут активированы тормоза двигателя.

![[eb8swvo.png]]

Запуск двигателя на холостом ходу 3-5 минут при приблизительно 1000 оборотах в минуту, чтобы согреть двигатель перед активацией тормозов двигателя. **не** не гасить тормоза двигателя до тех пор, пока температура масла двигателя не превысит 30°C[86°F].

![[eb800va.png]]

> [!note] Примечание
> См. в этом разделе шаги «Наставления по эксплуатации» для получения конкретной информации о работе тормозов двигателя в определенных дорожных условиях.

Для активации тормозов двигателя переключите переключатель включения/выключения в положение Включения. После активации работа тормозов двигателя полностью автоматическая.

![[eb8swvc.png]]

> [!danger] ОПАСНО
> Не используйте тормоза двигателя при болтании или тяге пустого прицепа. При работе тормозов двигателя блокировка колес может происходить быстрее при применении служебных тормозов, особенно на транспортных средствах с одноприводными осями.

Убедитесь, что тормоза двигателя переключаются в положение выключения при болтании или тяге пустого прицепа.

![[eb8swqa.png]]

> [!warning] ОСТОРОЖНО
> Тормоза двигателя предназначены для оказания помощи рабочим тормозам транспортного средства в замедлении транспортного средства до остановки.

Помните, что для остановки транспортного средства потребуются служебные тормоза.

![[eb800be.png]]

> [!warning] ОСТОРОЖНО
> Не используйте тормоза двигателя, чтобы помочь бесцепочечному переключению передач. Это может привести к остановке двигателя или привести к повреждению двигателя.

![[eb800bf.png]]

ECM отключит тормоза двигателя, когда обороты двигателя ниже 850 оборотов в минуту, когда активен электронный код неисправности или если скорость транспортного средства меньше минимального параметра скорости транспортного средства при тормозах двигателя.

![[00800004.png]]

> [!warning] ОСТОРОЖНО
> Не работайте с двигателем, если тормоза двигателя не отключаются. Это приведет к серьезным повреждениям двигателя.

Если тормоза двигателя **не **выключаются, немедленно выключите двигатель и обратитесь в авторизованный ремонтный центр Cummins.

![[eb100ba.png]]

Советы по работе на уровне и сухом покрытии

Для работы на сухих и относительно плоских поверхностях, когда требуется большая тормозная способность, вы можете выбрать более низкое положение.

![[17c00016.png]]

Чтобы уменьшить скорость автомобиля, включите или выключите двигатель в положении ON. Удалите ногу с дроссельной заслонки и педали сцепления. Тормоза двигателя сразу начнут работать, замедляя автомобиль.

![[eb8swvn.png]]

Для работы на сухом тротуаре, когда требуется максимальная тормозная способность, выберите «Нет». 6 позиция.

![[17c00017.png]]

> [!danger] ОПАСНО
> Скорость безопасного управления транспортным средством будет варьироваться в зависимости от размера груза, типа груза, класса и дорожных условий.

> [!note] Примечание
> **Всегда** Будьте готовы использовать служебные тормоза транспортного средства для экстренной остановки.

Советы по эксплуатации на классах с сухим покрытием

Транспортные средства, оснащенные должным образом управляемыми тормозами двигателя, способны двигаться вниз по склону с немного более высокими скоростями управления, чем транспортные средства, не оснащенные тормозами двигателя.

![[eb800ba.png]]

> [!warning] ОСТОРОЖНО
> Никогда не превышайте регулируемую скорость двигателя, так как может произойти повреждение двигателя.

> [!note] Примечание
> Оптимальная тормозная способность тормозов двигателя достигается при номинальной скорости двигателя, поэтому правильный выбор передачи имеет решающее значение.

После того, как вы определили безопасную скорость для вашего автомобиля, работайте с тормозами двигателя с трансмиссией в самой низкой передаче, которая **не **приведет к превышению скорости двигателя над номинальной скоростью двигателя.

![[eb800vf.png]]

> [!note] Примечание
> Некоторые производители предпочитают использовать трехпозиционный переключатель.

Шестипозиционный селекторный переключатель может использоваться для изменения тормозной способности при изменении дорожных условий.

![[17c00018.png]]

Тормоза транспортного средства должны использоваться, когда требуется дополнительная тормозная способность.

![[eb800vg.png]]

> [!danger] ОПАСНО
> Частое использование служебных тормозов приведет к их нагреванию, что снижает способность замедлять или останавливать автомобиль.

![[eb800bb.png]]

> [!note] Примечание
> Чем длиннее или круче холм, тем важнее использовать тормоза двигателя. Максимально используйте тормоза двигателя, переключаясь вниз и позволяя тормозам двигателя выполнять работу.

Если требуется частое использование рабочих тормозов транспортного средства, рекомендуется использовать более медленную скорость управления путем выбора более низкой передачи.

![[eb800vi.png]]

### Советы по эксплуатации на Slick Roads

> [!warning] ОСТОРОЖНО
> Эксплуатация любого транспортного средства трудно предсказать на скользких дорогах. Первые 10-15 минут осадков являются самыми опасными, так как дорожная грязь и масло, смешанное с дождем, создают очень скользкую поверхность.

**Всегда** допускать дополнительное расстояние между вашим автомобилем и другими объектами при использовании служебных тормозов или тормозов двигателя на скользких дорогах.

![[eb800bc.png]]

> [!danger] ОПАСНО
> Использование тормозов двигателя на мокрых или скользких дорогах может вызвать переторможение колес, особенно транспортных средств с легкими нагрузками или одноприводных осей. Расстояние остановки может фактически увеличиться, или автомобиль может закатиться или джекниф.

Уменьшите тормозную способность или выключите тормоза двигателя на скользких дорогах.

![[17c00019.png]]

При движении по скользким дорогам начните с переключателя включения/выключения в положении OFF и переключателя шестипозиционного селектора в No. 1 или нет. 2 позиции.

Если ваш трактор оснащен задней осью с двойным винтом, используйте силовой разделитель в положении UNLOCKED.

![[17c00020.png]]

Удалите ногу из дроссельной заслонки, чтобы убедиться, что автомобиль будет поддерживать тягу только с тормозной способностью двигателя.

Если колеса привода автомобиля начинают заноситься или происходит движение рыбного хвоста, сделайте **не** активировать тормоза двигателя.

![[eb800vh.png]]

Если сцепление поддерживается и требуется больше тормозной мощности, вы можете выбрать следующее более высокое положение на шестипозиционном селекторном выключателе. Включите тормоза двигателя, включив выключатель в положение ON.

![[17c00021.png]]

Если приводные колеса транспортного средства начинают заноситься или происходит движение рыболовного хвоста, переключите переключатель включения/выключения в положение выключения.

![[17c00022.png]]

Если тяга сохраняется при активации тормозов двигателя и требуется больше тормозной мощности, переведите шестипозиционный селектор на No. 3 или 4 позиции.

![[17c00023.png]]

Опять же, если транспортное средство потеряло тягу или произошло движение рыболовного хвоста, переключите переключатель включения / выключения в положение выключения. Не пытайтесь использовать тормоза двигателя в No. 3 или 4 позиции.

![[17c00025.png]]

Повторите вышеуказанные процедуры, чтобы выбрать «нет». 5 или 6 положение на выключателе.

![[17c00024.png]]

Опять же, если транспортное средство потеряло тягу или произошло движение рыболовного хвоста, переключите переключатель включения / выключения в положение выключения. Не пытайтесь использовать тормоза двигателя в No. 5 или 6 позиции.

![[17c00025.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> **CAUTION · Осторожно**
> Do not exceed governed engine speed when operating engine brakes. Engine damage can occur. The engine brakes are designed to assist the vehicle's service brakes to slow down the vehicle.
>
> Signature and ISX engines are equipped with the Intebrake™ system (engine brakes).
>
> Engine brakes use the energy of engine compression to provide vehicle retardation by converting the engine to an energy-absorbing device to reduce vehicle speed. This is accomplished by a hydraulic circuit that opens the exhaust valves near the end of the compression stroke.
>
> The ISX CM870 product and newer use the added benefit of the variable geometry turbocharger to assist in engine braking.
>
> The amount of braking power available on this engine is up to 600 hp. Braking power is managed by the Intebrake™ system (engine brakes).
>
> **CAUTION · Осторожно**
> Do not operate the engine if the engine brakes will not deactivate. To do so will cause severe engine damage.
>
> If the engine brakes will **not** shut off, shut off the engine immediately, and contact a Cummins Authorized Repair Facility.
>
> Engine brake controls consist of the following:
>
> - A six-position or three-position selector switch
> - An on/off switch
> - A clutch switch
> - A throttle sensor
> - A service brake pressure switch.
>
> Other switches for cruise control that affect engine brake operations are:
>
> - Cruise control on/off and set/resume switches (if the engine brakes in cruise control feature is turned off)
> - Service brake air pressure switch.
>
> Engine brakes can operate while cruise control is turned on. The electronic feature, fan control engine braking, can be enabled to turn the fan on during engine braking. This increases the parasitic load on the engine during braking. Refer to Programmable Features in this section.
>
> **Note · Примечание**
> Some OEMs choose to use a three-position switch.
>
> The six-position selector switch is located next to the on/off switch in the cab, and allows you to select the retarding power from one to six brakes.
>
> The engine brake level specifications:
>
> Position No. 1 = 17-percent engine braking power.
>
> Position No. 2 = 33-percent engine braking power.
>
> Position No. 3 = 50-percent engine braking power.
>
> Position No. 4 = 67-percent engine braking power.
>
> Position No. 5 = 83-percent engine braking power.
>
> Position No. 6 = 100-percent engine braking power.
>
> **Note · Примечание**
> For OEMs that use a three-position switch, the brake level specifications are: Position No. 1 = 33-percent engine braking power. Position No. 2 = 67-percent engine braking power. Position No. 3 = 100-percent engine braking power.
>
> For ISX CM870 and newer products, the engine brake select switch does **not** always directly correlate to the number of engine brake solenoids that are activated. This is due to the added use of the variable geometry turbocharger to assist in engine braking and the use of **only** two engine brake solenoids.
>
> **Note · Примечание**
> Any one of these switches can deactivate the engine brakes. If the engine brakes in cruise control feature is turned on, the cruise control switch, PTO switches, or both will **not** deactivate the engine brakes.
>
> With the engine, signals from the on/off switch, the clutch switch, the throttle sensor, and the cruise control switch, PTO switches, or both are fed into the electronic control module.
>
> **Note · Примечание**
> Engine brakes can **not** be enabled:
>
> The ECM then electronically enables or disables the engine brakes.
>
> 1. When cruise control is active, if the engine brakes in cruise control feature is turned off
> 2. When engine speed goes below 850 rpm or 30 mph
> 3. When an electronic fault code is active
> 4. When the clutch pedal is depressed
> 5. When the throttle pedal is depressed
> 6. When the PTO or remote PTO is active.
>
> The throttle position sensor is part of the accelerator pedal assembly located in the cab and will deactivate the engine brakes when depressed.
>
> The clutch switch uses the motion of the clutch linkage to deactivate the engine brakes when the clutch pedal is depressed. Depressing the clutch while in cruise control will disengage the cruise control.
>
> The service brake pressure switch is attached to the service brake air supply line.
>
> Applying the service brakes while in cruise control will disengage the cruise control and enable the engine brakes.
>
> If the pedal-activated engine brake feature is enabled, the service brake pedal **must** be tapped before the engine brakes will be activated.
>
> Idle the engine 3 to 5 minutes at approximately 1000 rpm to warm the engine before activating the engine brakes. Do **not** operate the engine brakes until the engine oil temperature is above 30°C \[86°F\].
>
> **Note · Примечание**
> See the “Tips for Operation” steps in this section for specific information about engine brake operation under certain road conditions.
>
> To activate the engine brakes, switch the on/off switch to the ON position. Once activated, the operation of the engine brakes is fully automatic.
>
> **WARNING · Опасно**
> Do not use the engine brakes while bobtailing or pulling an empty trailer. With the engine brakes in operation, wheel lockup can occur more quickly when the service brakes are applied, especially on vehicles with single-drive axles.
>
> Make sure the engine brakes are switched to the OFF position when bobtailing or pulling an empty trailer.
>
> **CAUTION · Осторожно**
> The engine brakes are designed to assist the vehicle's service brakes in slowing the vehicle to a stop.
>
> Remember, service brakes will be required to bring the vehicle to a stop.
>
> **CAUTION · Осторожно**
> Do not use the engine brakes to aid clutchless gear shifting. This can cause the engine to stall or lead to engine damage.
>
> The ECM will disable the engine brakes when engine rpm is below 850 rpm, when an electronic fault code is active, or if the vehicle speed is less than the engine brake minimum vehicle speed parameter.
>
> **CAUTION · Осторожно**
> Do not operate the engine if the engine brakes will not deactivate. To do so will cause severe engine damage.
>
> If the engine brakes will **not** shut off, shut off the engine immediately, and contact a Cummins Authorized Repair Facility.
>
> Tips for Operating on Level and Dry Pavement
>
> For operating on dry and relatively flat surfaces when greater retarding power is **not** required, you can select a lower position.
>
> To reduce vehicle speed, put the engine brake on or off switch in the ON position. Remove your foot from the throttle and clutch pedal. The engine brakes will immediately begin to operate, slowing the vehicle.
>
> For operation on dry pavement when maximum retarding power is required, select the No. 6 position.
>
> **WARNING · Опасно**
> The safe control speed of a vehicle will vary with the size of the load, the type of load, the grade, and the road conditions.
>
> **Note · Примечание**
> **Always** be prepared to use the vehicle service brakes for emergency stopping.
>
> Tips for Operation on Grades with Dry Pavement
>
> Vehicles equipped with properly operated engine brakes are capable of traveling downhill at slightly higher control speeds than vehicles **not** equipped with engine brakes.
>
> **CAUTION · Осторожно**
> Never exceed governed engine speed as engine damage can occur.
>
> **Note · Примечание**
> The optimum braking power of engine brakes is reached at rated engine speed, therefore, correct gear selection is critical.
>
> Once you have determined the safe speed for your vehicle, operate the engine brakes with the transmission in the lowest gear which will **not** cause the engine speed to exceed the rated engine speed.
>
> **Note · Примечание**
> Some OEMs choose to use a three-position switch.
>
> The six-position selector switch can be used to vary braking power as road conditions change.
>
> Vehicle service brakes **must** be used when additional braking power is required.
>
> **WARNING · Опасно**
> Frequent use of the service brakes will cause them to heat up, which reduces the ability to slow or stop the vehicle.
>
> **Note · Примечание**
> The longer or steeper the hill, the more important it is to use your engine brakes. Make maximum use of your engine brakes by gearing down and letting the engine brakes do the work.
>
> If frequent use of the vehicle service brakes is required, it is recommended that a slower control speed be used by selecting a lower transmission gear.
>
> ### Tips for Operation on Slick Roads
>
> **CAUTION · Осторожно**
> The operation of any vehicle is difficult to predict on slick roads. The first 10 to 15 minutes of rainfall are the most dangerous, as road dirt and oil mixed with rain create a very slippery surface.
>
> **Always** allow for extra distance between your vehicle and other objects when using the service brakes or engine brakes on slick roads.
>
> **WARNING · Опасно**
> Using the engine brakes on wet or slippery roads can cause overbraking of the wheels, especially vehicles with light loads or single-drive axles. Stopping distance can actually increase, or the vehicle can skid or jackknife.
>
> Reduce the retarding power, or turn off the engine brakes on slick roads.
>
> When driving on slick roads, start with the on/off switch in the OFF position and the six-position selector switch in the No. 1 or No. 2 position.
>
> If your tractor is equipped with a twin-screw rear axle, use the power divider in the UNLOCKED position.
>
> Remove your foot from the throttle to make sure that the vehicle will maintain traction with the retarding power of the engine alone.
>
> If the vehicle drive wheels begin to skid or there is a fishtailing motion, do **not** activate the engine brakes.
>
> If traction is maintained and more braking power is required, you can select the next higher position on the six-position selector switch. Activate the engine brakes by switching the on - off switch to the ON position.
>
> If the vehicle's drive wheels begin to skid or there is a fishtailing motion, switch the on/off switch to the OFF position.
>
> If traction is maintained when the engine brakes are activated and more braking power is required, move the six-position selector switch to the No. 3 or 4 position.
>
> Again, if the vehicle has lost traction or there is a fishtailing motion, switch the on/off switch to the OFF position. Do **not** attempt to use the engine brakes in the No. 3 or 4 position.
>
> Repeat the above procedures to select the No. 5 or 6 position on the selector switch.
>
> Again, if the vehicle has lost traction or there is a fishtailing motion, switch the on/off switch to the OFF position. Do **not** attempt to use the engine brakes in the No. 5 or 6 position.
