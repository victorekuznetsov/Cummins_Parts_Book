---
type: "Процедура"
doc: "35-008-028-tr"
title_en: "Fan Clutch, Viscous"
modified: "2009-01-23"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
figures: 16
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-008-028-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-008-028-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/35"
  - "перевод/машинный"
---

# Fan Clutch, Viscous

> [!abstract] Процедура · `35-008-028-tr`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 8 - Cooling System - Group 08
> **Даты:** изменён 2009-01-23
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-008-028-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-008-028-tr.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Вентиляторные сцепления могут управляться электронным модулем управления (ECM). ECM запрограммирован на включение вентилятора, когда 0-VDC (обычно открытый переключатель) наносится на реле сцепления вентилятора, и выключение вентилятора, когда 12-VDC (обычно закрытый переключатель) наносится на реле сцепления вентилятора.

Следующие проверки сцепления вентиляторов предназначены для муфт вентиляторов, подключенных к топливной системе с электронным управлением. См. спецификации производителя транспортного средства для определения установки сцепления вентилятора.

![[fn2cnkc.png]]

### Первичная проверка

Вязкие вентиляторные накопители используются в качестве энергосберегающего устройства, активируемого встроенным датчиком за радиатором, используемым для мониторинга температуры воздуха.

Когда температура воздуха достигает определенного уровня, в зависимости от температуры установки используемого датчика, контроль температуры-чувствования перемещает привод, который позволяет вязкой жидкости включать вентиляторный привод и увеличивать скорость вентилятора.

![[fn8cnga.png]]

Используйте вентиляторное rpm-измерительное устройство для проверки работы вязкого вентиляторного узла. Можно использовать строб или цифровой оптический тахометр, номер детали 3377462.

![[fn8toga.png]]

Отметьте пятно на шкиве хоста вентилятора и одном лезвии вентилятора, чтобы измерительное устройство могло определить шкив и скорость вентилятора. Отражательная лента, номер 3377464, в цифровом оптическом тахометре, номер 3377462, может использоваться для маркировки лопасти вентилятора и шкива.

![[fa8puta.png]]

Пока двигатель еще теплый и автомобиль выключен, накройте решетку радиатора.

Оставьте отверстие диаметром около 0,3 м[1 фут] в картоне, чтобы позволить небольшому количеству воздуха течь в вязкий вентиляторный концентратор.

![[ra8cvhb.png]]

Запускай двигатель. Запускайте двигатель на холостом ходу в течение трех-пяти минут. Заблокируйте дроссел в положении высокого пальца.

Используйте опцию PTO для работы двигателя при максимальной скорости вращения двигателя PTO.

![[oi800ve.png]]

> [!danger] ОПАСНО
> Вентилятор охлаждения будет включен, когда двигатель запущен. Чтобы уменьшить вероятность получения травмы, не кладите руки на путь вращающегося вентилятора.

> [!warning] ОСТОРОЖНО
> Не превышайте температуру охлаждающей жидкости 100°C[212°F]. Более высокие температуры охлаждающей жидкости могут повредить двигатель.

![[fn800qc.png]]

Когда температура охлаждающей жидкости достигает 91 ° C \[195 ° F \], измеренная скорость вентилятора **должна **достигать минимум 85 процентов скорости шкива.

Измерьте скорость вентилятора, деленную на скорость вентилятора (пулея). Дивиденды должны быть больше или равны 0,85.

Измеренная скорость вентилятора ÷ Fan Hub (Pulley Speed) \>= 0,85

![[fn800kd.png]]

Пока двигатель еще находится на высоком холостом ходу, удалите крышку радиатора. Скорость вентилятора **должна **начать уменьшаться через 1 минуту и в конечном итоге упасть до максимума в 50 процентов от скорости входного шкива.

Если вязкий вентилятор не выдерживает этого теста, проверьте его у авторизованного дилера вентилятора для ремонта или замены.

![[ra8cvmb.png]]

Если вентилятор **не** работает в пределах температурного диапазона, указанного на датчике температуры охлаждающей жидкости (1), необходимо проверить сцепление вентилятора и элементы управления. См. сервисное руководство изготовителя машины.

![[08200052.png]]

Если устройство для измерения скорости вентилятора недоступно, и жалоба касается перегрева, удалите вязкую биметаллическую полосу вентилятора и контрольный штифт. Это заставит фан-центр работать все время.

![[fa8pima.png]]

Если жалоба на перегрев происходит **не** с удаленным контрольным штифтом, установите контрольный штифт и отнесите вентиляторный концентратор к авторизованному дилеру вентиляторного концентратора для ремонта или замены.

![[fa8piha.png]]

### Подготовительные операции

- Удалите ремень привода вентилятора.[[35-008-002-tr — Drive Belt, Cooling Fan|См. процедуру 008-002 в разделе 8.]]
- Удалите вентилятор и сборку вентилятора. См. сервисное руководство изготовителя машины.

![[ck800wa.png]]

### Снятие

Уберите гайки, шайбы и вентилятор.

![[fa8cnha.png]]

### Установка

Установите вентилятор на сборку вентиляторного сцепления.

Затяните крепежные гайки. См. руководство по обслуживанию OEM для спецификаций крутящего момента.

![[fa8cnha.png]]

### Завершающие операции

- Установите сцепление вентилятора и сборку вентилятора на двигатель. См. сервисное руководство изготовителя машины.
- Установите, настройте и затяните ремень привода вентилятора.[[35-008-002-tr — Drive Belt, Cooling Fan|См. процедуру 008-002 в разделе 8.]]
- Управляйте двигателем и проверяйте его правильность.

![[ck800wa.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The fan clutches can be controlled by the electronic control module (ECM). The ECM is programmed to turn the fan on when 0-VDC (normally open switch) is applied to the fan clutch relay, and turn the fan off when 12-VDC (normally closed switch) is applied to the fan clutch relay.
>
> The following fan clutch checks are for fan clutches wired to the electronically controlled fuel system. Refer to the vehicle manufacturer's specifications to determine the installation of the fan clutch.
>
> ### Initial Check
>
> Viscous fan drives are used as a power-saving device activated by a built-in sensor behind the radiator used to monitor air temperature.
>
> When the air temperature reaches a specific level, depending on the temperature setting of the sensor used, the temperature-sensing control moves an actuator that allows viscous fluid to engage the fan drive and increase the fan speed.
>
> Use a fan rpm-measuring device to check the operation of the viscous fan hub. A strobe or digital optical tachometer, Part Number 3377462, can be used.
>
> Mark a spot on the fan hub pulley and one fan blade so the measuring device can determine the pulley and the fan speed. Reflective tape, Part Number 3377464, in digital optical tachometer, Part Number 3377462, can be used to mark the fan blade and the pulley.
>
> While the engine is still warm and the vehicle is shut off, cover the radiator grill.
>
> Leave a hole approximately 0.3 m \[1-ft\] in diameter in the cardboard to allow some air to flow to the viscous fan hub.
>
> Start the engine. Idle the engine for three to five minutes. Lock the throttle in a HIGH IDLE position.
>
> Use the PTO option to operate the engine at maximum PTO engine rpm.
>
> **WARNING · Опасно**
> The cooling fan will engage when the engine is started. To reduce the possibility of personal injury, do not put your hands in the path of a rotating fan.
>
> **CAUTION · Осторожно**
> Do not exceed 100°C \[212°F\] coolant temperature. Higher coolant temperatures can damage the engine.
>
> When the coolant temperature reaches 91°C \[195°F\], measured fan speed **must** reach a minimum of 85 percent of the pulley speed.
>
> Measure the fan speed divided by the fan hub (pulley) speed. The dividend **must** be greater than or equal to 0.85.
>
> Measured Fan Speed ÷ Fan Hub (Pulley Speed) \>= 0.85
>
> While the engine is still at high idle, remove the radiator grill cover. The fan speed **must** begin to decrease after 1 minute and eventually drop to a maximum of 50 percent of the input pulley speed.
>
> If the viscous fan hub fails this test, have it checked by an authorized fan hub dealer for repair or replacement.
>
> If the fan does **not** operate within the temperature range indicated on the coolant temperature sensor (1), the fan clutch and the controls **must** be checked. Refer to the OEM service manual.
>
> If a fan speed measuring device is **not** available and the complaint concerns overheating, remove the viscous fan hub bimetal strip and the control pin. This will cause the fan hub to operate all the time.
>
> If the overheating complaint does **not** occur with the control pin removed, install the control pin, and take the fan hub to an authorized fan hub dealer for repair or replacement.
>
> ### Preparatory Steps
>
> - Remove the fan drive belt. [[35-008-002-tr — Drive Belt, Cooling Fan|Refer to Procedure 008-002 in Section 8.]]
> - Remove the fan and fan clutch assembly. Refer to the OEM service manual.
>
> ### Remove
>
> Remove the nuts, washers, and fan.
>
> ### Install
>
> Install the fan on the fan clutch assembly.
>
> Tighten the mounting nuts. Refer to the OEM service manual for torque specifications.
>
> ### Finishing Steps
>
> - Install the fan clutch and fan assembly on the engine. Refer to the OEM service manual.
> - Install, adjust, and tighten the fan drive belt. [[35-008-002-tr — Drive Belt, Cooling Fan|Refer to Procedure 008-002 in Section 8.]]
> - Operate the engine and check for proper operation.
