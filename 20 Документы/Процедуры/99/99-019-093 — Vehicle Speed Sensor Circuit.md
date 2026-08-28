---
aliases:
  - "Цепь датчика скорости машины"
type: "Процедура"
doc: "99-019-093"
title_en: "Vehicle Speed Sensor Circuit"
title_ru: "Цепь датчика скорости машины"
modified: "2015-06-29"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 3
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-093.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-093.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/99"
  - "перевод/машинный"
---

# Vehicle Speed Sensor Circuit
**Цепь датчика скорости машины**

> [!abstract] Процедура · `99-019-093`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2015-06-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-093.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-093.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

> [!warning] ОСТОРОЖНО
> Правильные провода и/или одобренный Cummins® инструмент для тестирования цепи должны использоваться при работе с электрическими разъемами для предотвращения расширения штифта и повреждения разъема.

Отключите разъем интерфейса оригинального производителя оборудования (OEM) проводов жгута проводов двигателя. Чтобы определить местоположение разъема, см. соответствующую схему проводов двигателя. Убедитесь, что датчик скорости автомобиля подключен к OEM-проводах.

Вставьте измерительный щуп в магнитный датчик скорости транспортного средства сигнал положительный (+) штифт в разъёме проводов OEM. Вставьте другой свинец в магнитный датчик скорости транспортного средства сигнал отрицательного (-) штифта разъема.

Соедините два аллигатора с двумя зондами мультиметра. Настройте мультиметр на установку сопротивления и измерьте сопротивление. При измерении сопротивления с подключенным датчиком обратитесь к руководству по устранению неполадок и ремонту OEM для правильного значения сопротивления. Если значение **не** правильно, возникает проблема с проводкой OEM при условии, что компонент датчика скорости транспортного средства был ранее проверен.

> [!note] Примечание
> Ремонт или замена OEM проводов жгута.[[99-019-071 — OEM Wiring Harness|См. процедуру 019-071]]или к руководству по устранению неполадок и ремонту для замены проводов OEM.

Если значение правильное, схема должна быть проверена на короткое замыкание на землю и короткое замыкание от контакта к контакту.

![[19c01215.png]]

### Проверка на замыкание на массу

Проверьте короткое замыкание на землю. Вставьте многометровый щуп с прикрепленным испытательным щупом в магнитный датчик скорости транспортного средства сигнала положительного (+) штифта разъёма проводов OEM-подключателя. Прикоснитесь к другому многометровому щупу блока двигателя. Измерьте сопротивление. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, в цепи датчика скорости транспортного средства в ремне электропроводки двигателя или OEM-проводах есть короткое замыкание для заземления.

Ремонт проводов, которые закорачиваются в цепи в соответствии с процедурами производителя транспортного средства.

![[19c01241.png]]

### Проверка на замыкание между контактами

Проверьте короткое замыкание от контакта к контакту. Вставьте многометровый щуп с прикрепленным испытательным щупом в магнитный датчик скорости транспортного средства сигнала положительного (+) штифта разъёма проводов OEM-подключателя. Вставьте другой измерительный щуп во все другие штифты, по одному за раз, чтобы проверить короткий штифт на другой штифт.

Измерьте сопротивление. Мультиметр **должен** показывать открытую схему (более 100k ом).

![[19c01215.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> **CAUTION · Осторожно**
> Proper leads and/or a Cummins® approved circuit testing tool must be used when working with electrical connectors to prevent pin expansion and damage to the connector.
>
> Disconnect the original equipment manufacturer (OEM) harness engine interface connector. To determine the location of the connector, see the corresponding engine wiring diagram. Make sure the vehicle speed sensor is connected to the OEM harness.
>
> Insert a test lead into the magnetic vehicle speed sensor signal positive (+) pin in the OEM harness connector. Insert the other lead into the magnetic vehicle speed sensor signal negative (-) pin of the connector.
>
> Connect the two alligator clips to the two probes of the multimeter. Adjust the multimeter to the resistance setting and measure resistance. When measuring the resistance with the sensor connected, refer to the OEM troubleshooting and repair manual for the correct resistance value. If the value is **not** correct, there is a problem with the OEM harness, provided that the vehicle speed sensor component has been previously checked.
>
> **Note · Примечание**
> Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071]], or to the OEM troubleshooting and repair manual for OEM harness replacement.
>
> If the value is correct, the circuit **must** still be checked for a short circuit to ground and a short circuit from pin-to-pin.
>
> ### Check for Short Circuit to Ground
>
> Check for a short circuit to ground. Insert the multimeter probe with attached test lead into the magnetic vehicle speed sensor signal positive (+) pin of the OEM harness connector. Touch the other multimeter probe to the engine block. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, there is a short circuit to ground in the vehicle speed sensor circuit in the engine harness or OEM harness.
>
> Repair the wires which are shorted in the circuit according to the vehicle manufacturer's procedures.
>
> ### Check for Short Circuit from Pin to Pin
>
> Check for a short circuit from pin-to-pin. Insert the multimeter probe with attached test lead into the magnetic vehicle speed sensor signal positive (+) pin of the OEM harness connector. Insert the other test lead into all the other pins, one at a time, to check for a short to another pin.
>
> Measure the resistance. The multimeter **must** show an open circuit (more than 100k ohms).
