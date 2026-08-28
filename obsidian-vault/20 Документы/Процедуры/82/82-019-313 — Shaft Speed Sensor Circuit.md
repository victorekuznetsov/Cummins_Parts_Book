---
aliases:
  - "Цепь датчика частоты вращения вала"
type: "Процедура"
doc: "82-019-313"
title_en: "Shaft Speed Sensor Circuit"
title_ru: "Цепь датчика частоты вращения вала"
modified: "2005-01-28"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 5
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-313.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-313.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Shaft Speed Sensor Circuit
**Цепь датчика частоты вращения вала**

> [!abstract] Процедура · `82-019-313`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2005-01-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-313.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-313.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

Отсоедините разъем электропроводки привода от ECM. Убедитесь, что датчик скорости вала подключен к OEM-проводах.

> [!warning] ОСТОРОЖНО
> Не используйте щупы или провода, отличные от Части № 3822758. Узлы OEM-проводов будут повреждены. Лиды должны плотно помещаться в разъеме без расширения штифтов в разъеме.

Включить испытательный щуп в контакт 40 разъёма проводов привода. Вставьте другой свинец в контакт 30 разъёма.

![[19200265.png]]

Соедините два аллигатора с двумя зондами мультиметра. Настройте мультиметр на установку сопротивления и измерьте сопротивление. Значение сопротивления **должно быть** от 750 до 1500 Ом. Если значение **не** правильно, возникает проблема с проводкой привода при условии, что датчик скорости вала был предварительно проверен.

Ремонт или замена приводной электропроводки или электропроводки OEM в зависимости от местоположения повреждения. См. процедуру[[82-019-043-tr — Engine Wiring Harness|019-043]].

Если значение правильное, схема **должна *** все еще проверяться на короткое замыкание на землю и короткое замыкание от пин-кодов до пин-кодов.

![[19200265.png]]

### Проверка на замыкание на массу

Проверьте короткое замыкание на землю. Включить многометровый щуп с прикрепленным испытательным щупом в контакт 40 разъёма проводов привода ремня. Прикоснитесь к другому многометровому щупу блока двигателя. Измерьте сопротивление. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, в цепи датчика скорости вала в приводной проводах или OEM-проводах есть короткое замыкание для заземления.

Ремонт проводов, которые закорачиваются в цепи в соответствии с процедурами производителя транспортного средства.

![[19200254.png]]

### Проверка на замыкание между контактами

Проверьте короткое замыкание от пин-кодов до пин-кодов. Включить многометровый щуп с прикрепленным испытательным щупом в контакт 40 разъёма проводов привода ремня. Вставьте другой испытательный щуп в контакт 1 разъёма.

Измерьте сопротивление. Мультиметр **должен** показывать открытую схему (более 100k ом).

![[19c00436.png]]

Удалите пробный щуп из контакта 1 и проверьте все штифты в разъеме.

Измерьте сопротивление от контакта 40 разъёма проводов привода со всеми другими штифтами в разъеме, по одному за раз. Мультиметр **должен** показывать открытую схему (более 100k ом) на всех штифтах.

> [!note] Примечание
> Если значения верны для всех проверок цепи, схема датчика скорости вала хороша.

После ремонта подсоедините все компоненты.

> [!missing]- Иллюстрация `19c00437.png` не извлечена — смотрите PDF-оригинал документа


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> Disconnect the actuator harness connector from the ECM. Make sure the shaft speed sensor is connected to the OEM harness.
>
> **CAUTION · Осторожно**
> Do not use probes or leads other than Part Number 3822758. The OEM harness will be damaged. The leads must fit tightly in the connector without expanding the pins in the connector.
>
> Insert a test lead into pin 40 of the actuator harness connector. Insert the other lead into pin 30 of the connector.
>
> Connect the two alligator clips to the two probes of the multimeter. Adjust the multimeter to the resistance setting and measure resistance. The resistance value **must** be 750 to 1500 ohms. If the value is **not** correct, there is a problem with the actuator harness, provided that the shaft speed sensor has been previously checked.
>
> Repair or replace the actuator harness or the OEM harness, depending on the location of the damage. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].
>
> If the value is correct, the circuit **must** still be checked for a short circuit to ground and a short circuit from pin to pin.
>
> ### Check for Short Circuit to Ground
>
> Check for a short circuit to ground. Insert the multimeter probe with attached test lead into pin 40 of the actuator harness connector. Touch the other multimeter probe to the engine block. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, there is a short circuit to ground in the shaft speed sensor circuit in the actuator harness or OEM harness.
>
> Repair the wires which are shorted in the circuit according to the vehicle manufacturer's procedures.
>
> ### Check for Short Circuit from Pin to Pin
>
> Check for a short circuit from pin to pin. Insert the multimeter probe with attached test lead into pin 40 of the actuator harness connector. Insert the other test lead into pin 1 of the connector.
>
> Measure the resistance. The multimeter **must** show an open circuit (more than 100k ohms).
>
> Remove the test lead from pin 1 and test all pins in the connector.
>
> Measure the resistance from pin 40 of the actuator harness connector to all other pins in the connector, one at a time. The multimeter **must** show an open circuit (more than 100k ohms) at all pins.
>
> **Note · Примечание**
> If the values are correct for all of the circuit checks, the shaft speed sensor circuit is good.
>
> Connect all components after completing the repair.
