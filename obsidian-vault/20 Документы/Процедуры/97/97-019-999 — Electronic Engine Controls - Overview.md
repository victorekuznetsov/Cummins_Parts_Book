---
type: "Процедура"
doc: "97-019-999"
title_en: "Electronic Engine Controls - Overview"
modified: "2003-06-13"
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
figures: 30
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-999.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-999.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
  - "перевод/машинный"
---

# Electronic Engine Controls - Overview

> [!abstract] Процедура · `97-019-999`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-06-13
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-999.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-999.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Как использовать мультиметр

На большинстве метров отрицательный (черный) многометровый свинец **должен быть подключен в положении COM, а положительный (красный) многометровый свинец **должен быть подключен к одному из положений, отмеченных для силы тока, сопротивления или напряжения. Смотрите инструкции производителя для более подробной информации.

> [!note] Примечание
> При измерении до блочной поверхности используйте чистую, неокрашенную металлическую поверхность, чтобы убедиться в хорошем измерении.

![[19400203.png]]

Использование специального испытательного щупа

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте следующий испытательный щуп при проведении измерения:

(C) Испытательный щуп Male Deutsch/AMP/Metri-Pack, номер детали 3822758

(F) Испытательный щуп Female Deutsch/AMP/Metri-Pack, Part Number 3822917.

![[19800729.png]]

Как измерить амператив

Сделайте открытый контур в том месте, где необходимо измерить ток.

1. Выберите функцию тока переменного тока (A ~) или тока постоянного тока (A-) на мультиметре.
2. Включите мощность измеряемой цепи.
3. Поместите провода мультиметра через открытую цепь для измерения ампеража.
4. Прочитайте отображаемое измерение.

![[19400205.png]]

Как измерить напряжение

1. Выберите функцию напряжения переменного тока (V ~) или напряжения постоянного тока (V -) на мультиметре.
2. Включите мощность измеряемой цепи.
3. Прикоснитесь к положительному (+) свинцу мультиметра к терминалу или штифту, который измеряется для напряжения. Прикосновение к другому приводит к чистой, неокрашенной металлической поверхности, которая соединена с заземлением батареи или с отрицательным положением батареи.
4. Прочитайте отображаемое измерение.

![[19a00020.png]]

Как измерить сопротивление

1. Выберите функцию сопротивления на мультиметре.
2. Убедитесь, что нет питания для тестируемых компонентов.
3. Отсоедините оба конца схемы или компонента, который должен быть измерен. Прикосновение к одному из них приводит к одному концу цепи или терминала компонента. Прикосновение к другому приводит к другому концу цепи или к другому компоненту терминала.
4. Прочитайте отображаемое измерение.

![[19400207.png]]

Как найти внутреннее сопротивление измерителя

Важно знать внутреннее сопротивление мультиметра при измерении малых сопротивлений. Для точного измерения малых сопротивлений внутреннее сопротивление мультиметра должно быть вычтено из измеренного сопротивления.

1. Включите мультиметр.
2. Установите мультиметр на самую низкую шкалу омов.
3. Измерьте сопротивление мультиметра, соприкоснувшись с испытательным щупом вместе и считав значение сопротивления (включая специальный испытательный щуп, если они используются).
4. «НУЛЬТО» мультиметра или вычитают это значение при проведении измерений.

![[19400208.png]]

Как проверить на непрерывность

1. Выберите функцию непрерывности на мультиметре (обычно помеченный диодным символом).
2. Убедитесь, что нет мощности для измеряемого компонента.
3. Отсоедините оба конца схемы или компонента, который должен быть измерен. Прикосновение к одному из них приводит к одному концу цепи или терминала компонента. Прикосновение к другому приводит к другому концу цепи или к другому компоненту терминала.
4. Прочитайте отображаемое измерение. Мультиметр будет гудить, если сопротивление меньше примерно 150 Ом. Если есть открытая схема, мультиметр будет **не** звуковым сигналом.

![[19800311.png]]

Контакты разъема - Проверка

При отключении разъемов во время устранения неполадок, контакты **должны всегда проверяться, чтобы убедиться, что они **не являются причиной плохого соединения. Во-первых, промыть и очистить контакты разъема с помощью электрического контактного очистителя, номер детали 3824510. Затем проверьте на изогнутые, расширенные, разъединенные и отодвинули булавки.

Влага в разъеме также может вызвать проблемы с производительностью системы. Много раз трудно увидеть влагу в разъеме. Если подозревается влажность, разъём **должен быть высушен. Применить контактный очиститель, номер детали 3824510, к разъему или использовать тепловую пушку на низкой температуре, чтобы она **не повредила разъем или провода.

> [!note] Примечание
> **Не** выдувать сжатый воздух в ЭКМ двигателя или неработающих портах или разъемах модуля управления. Сжатый воздух может содержать влагу из-за конденсации.

![[19900492.png]]

контактные линзы

Осмотрите штыревые терминалы разъема. Если какой-либо из терминалов согнут или расширен так, что они **не **легко спариваются с другой стороной разъема, то штифт должен быть заменен. См. раздел ремонта для конкретного разъема.

![[19900492.png]]

Корродированные пинсы

Осмотрите как штыревые, так и гнездовые терминалы на предмет коррозии, которая может вызвать плохое электрическое соединение внутри разъема. Если на штифтах очевидна коррозия, то корродированные штифты должны быть заменены. См. раздел ремонта для конкретного разъема.

![[19900492.png]]

Назад Пинс Back Pins

Осмотрите как штыревой, так и гнездовой терминалы на наличие контактов, которые могут **не **быть контактными, потому что они отодвинуты назад в разъеме. Для ремонта, нажмите штифт в корпус разъема с задней части разъема. Убедитесь, что терминал запирается на месте. Если терминал **не** запирается на месте, то замените его. См. раздел ремонта для конкретного разъема.

![[19900492.png]]

Короткая трасса на землю - Проверить

Процедура проверки короткого замыкания на землю выглядит следующим образом:

1. Переведите замок зажигания в положение OFF.
2. Отключите разъемы, которые необходимо протестировать.

![[19900493.png]]

При тестировании датчика необходимо только отключить соединение датчика.

При тестировании проводной упряжки отсоедините разъём проводной упряжки в модуль управления холостым ходом и разъем в датчике или нескольких датчиках.

1. Определите штифты, которые необходимо проверить.
2. Смой и очисти контакты разъема.
3. Осмотрите контакты разъёма на отсутствие повреждений.
4. Выберите функцию сопротивления на мультиметре.

![[19800313.png]]

> [!warning] ОСТОРОЖНО
> Используйте соответствующий испытательный щуп из комплекта ремонта электропроводки, номер детали 3163652 или 3824904, чтобы избежать повреждения контактов разъема.

1. Прикосновение к одному из мультиметров приводит к правильному штифту, который будет проверен.
2. Прикосновение к другому мультиметру приводит к блоку двигателя.
3. Прочитайте значение на многометровом дисплее.

![[19800314.png]]

Мультиметр **должен **показывать более 100k ом, что является открытой схемой.

Если цепь **не** открыта, проверяемый провод имеет короткий путь к земле или блоку двигателя.

1. Ремонт или замена компонента или провода.

![[19a00016.png]]

Короткая трасса от Pin до Pin - Check

Короткое замыкание от пин-кода к пин-коду является состоянием, при котором электрический путь существует между двумя пинами, где он не предназначен для существования.

Процедура проверки короткого замыкания от пин-кодов до пин-кодов выглядит следующим образом:

1. Переведите замок зажигания в положение OFF.
2. Отключите разъем, который должен быть протестирован.
3. Определите штифты, которые необходимо проверить.
4. Выберите функцию сопротивления на мультиметре.

![[19400213.png]]

> [!warning] ОСТОРОЖНО
> Используйте соответствующий испытательный щуп из комплекта ремонта электропроводки, номер детали 3163652 или 3824904, чтобы избежать повреждения контактов разъема.

1. Прикосновение к одному из мультиметров приводит к правильному штифту, который будет протестирован на стороне проводов ремня разъема.
2. Прикосновение к другому мультиметру приводит к **всем **другим штифтам на стороне проводов этого разъема, по одному за раз.

![[19800315.png]]

1. Прочитайте значение на многометровом дисплее.
2. Мультиметр **должен **показывать более 100k ом, что является открытой схемой.
3. Если цепь не открыта, то проверяемые контакты электрически соединены.

> [!note] Примечание
> См. схему проводов, чтобы убедиться, что провода, о которых идет речь, **не** должны быть подключены.

1. Проверьте проводку разъёмов жгута на влажность, которая может вызвать электрическое соединение.
2. Ремонт или замена проводов жгута.

![[19a00016.png]]

Проверка напряжения

Проверка напряжения - это процедура измерения разности потенциалов напряжения между двумя точками.

Процедура проверки напряжения выглядит следующим образом:

1. Отключите разъемы, которые необходимо протестировать.
2. Переведите замок зажигания в положение ON.
3. Определите штифты, которые необходимо проверить.
4. Выберите функцию напряжения переменного тока (V ~) или напряжения постоянного тока (V-) на мультиметре.

![[19900494.png]]

> [!warning] ОСТОРОЖНО
> Используйте соответствующий испытательный щуп из комплекта ремонта электропроводки, номер детали 3163652 или 3824904, чтобы избежать повреждения контактов разъема.

1. Прикоснитесь к одному из многометровых испытательных щупов, чтобы правильно провести испытания.
2. Прикосновение к другому мультиметру приводит к чистой, неокрашенной поверхности на блоке двигателя или к соответствующему обратному контакту.

![[19900495.png]]

1. Прочитайте значение на многометровом дисплее. Сравните измеренное значение с диапазоном напряжения, приведенным в спецификациях.
2. Если измеренное значение выходит за пределы заданного диапазона, проверьте процедуру ремонта электрической системы, которая проверяется на предмет соответствующего действия.

![[19400217.png]]

Проверка полярности

В качестве примера будет использоваться батарея для проверки полярности цепи.

Терминалы батареи обозначены для полярности. Мультиметр отображает разность напряжений положительного (+) свинца (красного) к отрицательному (-) свинцу (черного).

![[19400221.png]]

Полярность является правильной, когда положительный (+) свинец (красный) мультиметра находится на положительном выводе батареи, а отрицательный (-) свинец (черный) мультиметра находится на отрицательном выводе батареи.

Мультиметр будет отображать положительное напряжение, если полярность верна.

Если мультиметровые провода будут обращены вспять, мультиметр будет отображать отрицательное напряжение.

![[19a00021.png]]

Проверка непрерывности

> [!warning] ОСТОРОЖНО
> Используйте соответствующий испытательный щуп из комплекта ремонта жгута проводов, Номер детали 3163652 или 3824904, чтобы избежать повреждения контактов разъема.

Непрерывность — электрическое соединение между двумя штифтами, которое меньше определенного значения сопротивления. Для проводов жгута спецификация составляет менее 10 Ом.

![[19900496.png]]

Процедура проверки непрерывности заключается в следующем:

1. Переведите замок зажигания в положение OFF.
2. Отключите проводные разъёмы жгута, которые будут протестированы.
3. Выберите функцию сопротивления на мультиметре.

![[19900497.png]]

> [!warning] ОСТОРОЖНО
> Используйте соответствующий испытательный щуп из комплекта ремонта электропроводки, номер детали 3163652 или 3824904, чтобы избежать повреждения контактов разъема.

1. Прикоснитесь к одному из многометровых испытательных щупов к испытуемому штифту провода.
2. Прикосновение к другому мультиметру приводит к штифту на другом конце провода, который тестируется.
3. Прочитайте значение на многометровом дисплее.

![[19900496.png]]

Мультиметр **must** отображает менее 10 Ом для непрерывности провода.

Если мультиметр отображает более 10 Ом, провод должен быть отремонтирован или заменен электропроводкой.

![[19400225.png]]

Проверка сопротивления - катушка

1. Переведите замок зажигания в положение OFF.
2. Отсоедините проводную упряжку от катушки.
3. Выберите функцию сопротивления на мультиметре.

![[19900883.png]]

> [!warning] ОСТОРОЖНО
> Используйте соответствующий испытательный щуп из комплекта ремонта электропроводки, номер детали 3163652 или 3824904, чтобы избежать повреждения контактов разъема.

1. Прикосновение к одному из мультиметров приводит к контакту катушки.
2. Прикосновение к другому мультиметру приводит к другому контакту катушки.

> [!note] Примечание
> Для внутренне заземленных катушек прикоснитесь к одному многометровому выводу к терминалу катушки, а другой многометровый вывод к блоку двигателя.

1. Прочитайте измеренное сопротивление на многометровом дисплее.

![[19900884.png]]

Проверьте измеренное сопротивление по сравнению со спецификацией сопротивления для катушки.

> [!note] Примечание
> Внутреннее сопротивление мультиметра является значительным в некоторых проверках сопротивления катушке. Перед проведением измерения «НОЛЬ» измерителя или вычитают внутреннее сопротивление измерителя из измеренного значения.

![[19900884.png]]

> [!note] Примечание
> Рекомендуется, чтобы изображение работы с двигателя ECM было получено с использованием инструментария электронного обслуживания INSITETM, чтобы помочь в устранении неполадок.

> [!note] Примечание
> Отключение аккумуляторных батарей автомобиля может потребовать сброса часов ECM в режиме реального времени с помощью INSITETM.


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> How to Use a Multimeter
>
> On most meters, the negative (black) multimeter lead **must** be plugged in the COM position and the positive (red) multimeter lead **must** be plugged into one of the positions marked for amperage, resistance, or voltage. Refer to the manufacturer's instructions for more detail.
>
> **Note · Примечание**
> When measuring to a block ground, use a clean, unpainted metal surface to make sure of a good measurement.
>
> Use of Special Test Leads
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use the following test leads when taking a measurement:
>
> (C) Male Deutsch/AMP/Metri-Pack test lead, Part Number 3822758
>
> (F) Female Deutsch/AMP/Metri-Pack test lead, Part Number 3822917.
>
> How to Measure Amperage
>
> Make an open circuit at the place where the current needs to be measured.
>
> 1. Select the AC current (A∼) or DC current (A-) function on the multimeter.
> 2. Turn on the power in the circuit being measured.
> 3. Put the leads of the multimeter across the open circuit to measure the amperage.
> 4. Read the displayed measurement.
>
> How to Measure Voltage
>
> 1. Select the AC voltage (V∼) or DC voltage (V−) function on the multimeter.
> 2. Turn on the power in the circuit being measured.
> 3. Touch the positive (+) lead of the multimeter to the terminal or pin that is being measured for voltage. Touch the other lead to a clean, unpainted metal surface that is connected to battery ground or to the negative post of the battery.
> 4. Read the displayed measurement.
>
> How to Measure Resistance
>
> 1. Select the resistance function on the multimeter.
> 2. Verify that there is no power to the components being tested.
> 3. Disconnect both ends of the circuit or component to be measured. Touch one lead to one end of the circuit or component terminal. Touch the other lead to the other end of the circuit or the other component terminal.
> 4. Read the displayed measurement.
>
> How to Find the Internal Resistance of the Meter
>
> It is important to know the internal resistance of the multimeter when measuring small resistances. To measure small resistances accurately, the internal resistance of the multimeter **must** be subtracted from the measured resistance.
>
> 1. Turn the multimeter on.
> 2. Set the multimeter to the lowest ohm scale.
> 3. Measure the resistance of the multimeter by touching the test leads together and reading the resistance value (including special test leads, if they are being used).
> 4. “ZERO” the multimeter or subtract this value when taking measurements.
>
> How to Test for Continuity
>
> 1. Select the continuity function on the multimeter (usually marked with a diode symbol).
> 2. Make sure there is no power to the component being measured.
> 3. Disconnect both ends of the circuit or component to be measured. Touch one lead to one end of the circuit or component terminal. Touch the other lead to the other end of the circuit or the other component terminal.
> 4. Read the displayed measurement. The multimeter will beep if the resistance is less than about 150 ohms. If there is an open circuit, the multimeter will **not** beep.
>
> Connector Pins - Checking
>
> When disconnecting connectors during troubleshooting, the pins **must** always be inspected to make sure they are **not** the cause of a bad connection. First, flush and clean the connector pins using electrical contact cleaner, Part Number 3824510. Then, inspect for bent, expanded, corroded, and pushed back pins.
>
> Moisture in a connector can also cause system performance issues. Many times it is difficult to see moisture in a connector. If moisture is suspected, the connector **must** be dried. Apply contact cleaner, Part Number 3824510, to the connector, or use a heat gun on a low heat setting so that it will **not** damage the connector or wires.
>
> **Note · Примечание**
> Do **not** blow compressed air in the engine ECM or idle control module ports or connectors. Compressed air can contain moisture due to condensation.
>
> Bent Pins
>
> Inspect the male terminals of the connector. If any of the terminals are bent or expanded so that they will **not** easily mate with the other side of the connector, then the pin **must** be replaced. Refer to the repair section for the specific connector in question.
>
> Corroded Pins
>
> Inspect both the male and female terminals for corrosion which can cause a poor electrical connection within the connector. If any corrosion is evident on the pins, then the corroded pins **must** be replaced. Refer to the repair section for the specific connector in question.
>
> Pushed Back Pins
>
> Inspect both the male and female terminals for pins that can **not** be making contact because they are pushed back in the connector. To repair, push the pin into the connector body from the back of the connector. Make sure the terminal locks into place. If the terminal will **not** lock into place, then replace it. Refer to the repair section for the specific connector in question.
>
> Short Circuit to Ground - Check
>
> The procedure for checking for a short circuit to ground is as follows:
>
> 1. Turn the keyswitch to the OFF position.
> 2. Disconnect the connectors that need to be tested.
>
> When testing a sensor, it is **only** necessary to disconnect the sensor connection.
>
> When testing a harness, disconnect the harness connector at the idle control module, and the connector at the sensor, or multiple sensors.
>
> 1. Identify the pins that need to be tested.
> 2. Flush and clean the connector pins.
> 3. Inspect the connector pins for damage.
> 4. Select the resistance function on the multimeter.
>
> **CAUTION · Осторожно**
> Use the appropriate test leads from the wiring harness repair kit, Part Number 3163652 or 3824904, to avoid damage to the connector pins.
>
> 1. Touch one of the multimeter leads to the correct pin to be tested.
> 2. Touch the other multimeter lead to the engine block.
> 3. Read the value on the multimeter display.
>
> The multimeter **must** show greater than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, the wire being checked has a short to ground or the engine block.
>
> 1. Repair or replace the component or wire.
>
> Short Circuit from Pin to Pin - Check
>
> Short circuit from pin to pin is a condition where an electrical path exists between two pins where it is **not** intended to exist.
>
> The procedure for checking short circuit from pin to pin is as follows:
>
> 1. Turn the keyswitch to the OFF position.
> 2. Disconnect the connector that needs to be tested.
> 3. Identify the pins that need to be tested.
> 4. Select the resistance function on the multimeter.
>
> **CAUTION · Осторожно**
> Use the appropriate test leads from the wiring harness repair kit, Part Number 3163652 or 3824904, to avoid damage to the connector pins.
>
> 1. Touch one of the multimeter leads to the correct pin to be tested on the harness side of the connector.
> 2. Touch the other multimeter lead to **all** other pins on the harness side of this connector, one at a time.
>
> 1. Read the value on the multimeter display.
> 2. The multimeter **must** show greater than 100k ohms, which is an open circuit.
> 3. If the circuit is **not** open, the pins being checked are electrically connected.
>
> **Note · Примечание**
> Refer to the wiring diagram to verify that the wires in question are **not** supposed to be connected.
>
> 1. Inspect the harness connectors for moisture, which can cause an electrical connection.
> 2. Repair or replace the harness.
>
> Voltage Checking
>
> Voltage check is a procedure to measure the difference in voltage potential between two points.
>
> The procedure for checking voltage is as follows:
>
> 1. Disconnect the connectors that need to be tested.
> 2. Turn the keyswitch to the ON position.
> 3. Identify the pins that need to be tested.
> 4. Select the AC voltage (V∼) or DC voltage (V-) function on the multimeter.
>
> **CAUTION · Осторожно**
> Use the appropriate test leads from the wiring harness repair kit, Part Number 3163652 or 3824904, to avoid damage to the connector pins.
>
> 1. Touch one of the multimeter test leads to the correct lead to be tested.
> 2. Touch the other multimeter lead to a clean, unpainted surface on the engine block, or to the appropriate return pin.
>
> 1. Read the value on the multimeter display. Compare the measured value to the range of voltage given in the specifications.
> 2. If the measured value falls outside of the specified range, check the repair procedure of the electrical system that is being checked for the appropriate action.
>
> Polarity Check
>
> A battery will be used as an example to check polarity of a circuit.
>
> The terminals of a battery are marked for polarity. The multimeter displays the voltage difference of the positive (+) lead (red) to the negative (-) lead (black).
>
> The polarity is correct when the positive (+) lead (red) of the multimeter is on the positive terminal of the battery and the negative (-) lead (black) of the multimeter is on the negative terminal of the battery.
>
> The multimeter will display positive voltage if the polarity is correct.
>
> If the multimeter leads are reversed, the multimeter will display negative voltage.
>
> Continuity Check
>
> **CAUTION · Осторожно**
> Use the appropriate test leads from wiring harness repair kit, Part Number 3163652 or 3824904, to avoid damage to the connector pins.
>
> Continuity is an electrical connection between two pins that is less than a certain resistance value. For harness wires, the specification is less than 10 ohms.
>
> The procedure for checking continuity is as follows:
>
> 1. Turn the keyswitch to the OFF position.
> 2. Disconnect the harness connectors to be tested.
> 3. Select the resistance function on the multimeter.
>
> **CAUTION · Осторожно**
> Use the appropriate test leads from the wiring harness repair kit, Part Number 3163652 or 3824904, to avoid damage to the connector pins.
>
> 1. Touch one of the multimeter test leads to the pin of the wire being tested.
> 2. Touch the other multimeter lead to the pin at the other end of the wire being tested.
> 3. Read the value on the multimeter display.
>
> The multimeter **must** display less than 10 ohms for wire continuity.
>
> If the multimeter displays greater than 10 ohms, the wire **must** be repaired or the harness replaced.
>
> Resistance Check - Coil
>
> 1. Turn the keyswitch to the OFF position.
> 2. Disconnect the harness from the coil.
> 3. Select the resistance function on the multimeter.
>
> **CAUTION · Осторожно**
> Use the appropriate test leads from the wiring harness repair kit, Part Number 3163652 or 3824904, to avoid damage to the connector pins.
>
> 1. Touch one of the multimeter leads to the coil connector pin.
> 2. Touch the other multimeter lead to the other coil connector pin.
>
> **Note · Примечание**
> For internally grounded coils, touch one multimeter lead to the coil terminal and the other multimeter lead to the engine block.
>
> 1. Read the measured resistance on the multimeter display.
>
> Check the measured resistance against the resistance specification for the coil.
>
> **Note · Примечание**
> The internal resistance of the multimeter is significant in some coil resistance checks. Before taking the measurement, “ZERO” the meter, or subtract the meter's internal resistance from the measured value.
>
> **Note · Примечание**
> It is recommended that a job image from the engine ECM be taken, using the electronic service tool, INSITE™, to aid in troubleshooting.
>
> **Note · Примечание**
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset using INSITE™
