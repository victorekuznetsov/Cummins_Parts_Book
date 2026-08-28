---
aliases:
  - "Цепь управления вентилятором"
type: "Процедура"
doc: "82-019-045"
title_en: "Fan Control Circuit"
title_ru: "Цепь управления вентилятором"
modified: "2005-01-28"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 16
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-045.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-045.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Fan Control Circuit
**Цепь управления вентилятором**

> [!abstract] Процедура · `82-019-045`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2005-01-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-045.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-045.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Система ISM может управлять активацией сцепления вентилятора. ECM заряжает энергией вентиляторное сцепление или соленоид воздушного клапана.

См. публикации производителя автомобилей для получения дополнительной информации о устранении неполадок и ремонте проводов сцепления вентилятора.

![[19c00703.png]]

Схема сцепления вентилятора находится в ремне электропроводки привода. Провод сигнала привода сцепления вентилятора проходит от контакта 5 в разъеме электропроводки привода до контакта 12 в 31-контактном разъеме Deutsch на OEM-проводах. Возвратный провод привода сцепления вентилятора проходит от контакта 42 в разъеме электропроводки привода до контакта 13 в 31-контактном разъеме Deutsch на ремне электропроводки OEM. От 31-контактного разъема Deutsch цепь проходит через OEM-проводку к сцеплению вентилятора.

![[19c00705.png]]

### Проверка сопротивления

> [!warning] ОСТОРОЖНО
> Не используйте щупы или провода, отличные от Части № 3822758. Разъём будет повреждён. Лиды должны плотно помещаться в разъеме без расширения штифтов разъема.

Отсоедините разъем электропроводки привода от ECM. Отключите OEM-проводку на соленоиде вентилятора. Установите мультиметр на установку сопротивления.

Вставьте испытательный щуп в контакт 5 с разъемом электропроводки привода и соедините его с многометровым щупом.

![[19c00704.png]]

Прикоснитесь к другому многометровому щупу к соединительному терминалу соленоида сцепления вентилятора. Убедитесь, что соленоид сцепления вентилятора отключен.

Измерьте сопротивление.

Мультиметр **должен** показать замкнутую цепь (10 Ом и менее). Если цепь закрыта, она **должна *** все еще проверяться на короткое замыкание на землю и короткое замыкание от пин-кодов до пин-кодов. Если цепь **не** закрыта, в электропроводке есть проблема с подключением или открытая цепь.

![[19c00704.png]]

Удалите свинец из контакта 5 и вставьте его в контакт 42 разъёма проводов привода. Прикоснитесь к другому многометровому щупу к соединительному терминалу другого соленоида сцепления вентилятора. Убедитесь, что соленоид сцепления вентилятора отключен.

Измерьте сопротивление.

Мультиметр **должен** показать замкнутую цепь (10 Ом и менее). Если цепь закрыта, она **должна *** все еще проверяться на короткое замыкание на землю и короткое замыкание от пин-кодов до пин-кодов.

Если цепь **не** закрыта, в электропроводке есть проблема с подключением или открытая цепь.

![[19c00888.png]]

Проверьте соединения жгута проводов на 31-контактном разъеме Deutsch.

Если соединения хорошие, изолируйте открытую цепь от OEM-проводов до соленоида сцепления вентилятора или ремня электропроводки привода, как описано на следующих этапах.

![[19c00705.png]]

Проверьте OEM-проводку на соленоиде сцепления вентилятора для открытой цепи. Отключите 31-контактный разъем Deutsch.

Вставьте многометровый свинец в контакт 12 31-контактного разъема.

Прикоснитесь к другому многометровому щупу к терминалу соленоидного разъема сцепления вентилятора. Измерьте сопротивление.

Мультиметр **должен** показать замкнутую цепь (10 Ом и менее). Если цепь **не** закрыта, в OEM-проводах к соленоиду сцепления вентилятора имеется открытая цепь. Ремонт или замена электропроводки OEM в соответствии с процедурами OEM.

![[19c00665.png]]

Удалите свинец из контакта 12 31-контактного разъема и вставьте его в контакт 13 31-контактного разъема.

Прикоснитесь к другому многометровому щупу к терминалу соленоидного разъема сцепления вентилятора. Измерьте сопротивление.

Мультиметр **должен** показать замкнутую цепь (10 Ом и менее). Если цепь **не** закрыта, в OEM-проводах к соленоиду сцепления вентилятора имеется открытая цепь.

Ремонт или замена электропроводки OEM в соответствии с процедурами OEM.

![[19c00706.png]]

### Проверка на замыкание между контактами

Проверьте короткое замыкание между контактом 5 и всеми другими штифтами в разъеме электропроводки привода. Убедитесь, что соленоид сцепления вентилятора отключен. Убедитесь, что источник напряжения батареи отключен.

Включить испытательный щуп в контакт 5 разъёма проводов привода. Вставьте другой испытательный щуп во все другие штифты разъёма проводов привода, по одному за раз.

Измерьте сопротивление.

Мультиметр **должен** показывать открытую схему (более 100k ом) на всех штифтах.

![[19200309.png]]

Если схема не открыта, между контактом 5 и любым штифтом, который измерял замкнутую цепь, есть короткое замыкание.

Ремонт или замена привода проводов жгута.

См. процедуру[[82-019-043-tr — Engine Wiring Harness|019-043]].

![[19200309.png]]

Проверьте короткое замыкание между контактом 42 и всеми другими штифтами в разъеме электропроводки привода. Убедитесь, что соленоид сцепления вентилятора отключен. Убедитесь, что источник напряжения батареи отключен.

Включить испытательный щуп в контакт 42 разъёма проводов привода. Вставьте другой свинец во все другие штифты разъёма проводов привода, по одному за раз.

Измерьте сопротивление.

Мультиметр **должен** показывать открытую схему (более 100k ом) на всех штифтах.

![[19200310.png]]

Если схема не открыта, между контактом 42 и любым штифтом, который измеряет замкнутую цепь, имеется короткое замыкание.

Ремонт или замена привода проводов жгута. См. процедуру[[82-019-043-tr — Engine Wiring Harness|019-043]].

![[19200310.png]]

Отсоедините разъем датчика проводов ремня от ECM.

Проверьте короткое замыкание от контакта 5 разъёма проводов привода со всеми штифтами в разъёме проводов датчика.

Включить испытательный щуп в контакт 5 разъёма проводов привода. Подсоедините аллигаторный клип испытательного щупа к многометровому щупу. Вставьте другой измерительный щуп во все штифты разъёма датчика проводов.

Измерьте сопротивление.

Мультиметр **должен** показывать открытую схему (более 100k ом).

![[19200394.png]]

Если схема **не** открыта, между контактом 5 разъёма приводной проводов и любым штифтом в разъёме датчика проводов жгута имеется короткое замыкание, которое измеряет замкнутую цепь.

Ремонт или замена датчика проводов жгута. См. процедуру[[82-019-043-tr — Engine Wiring Harness|019-043]].

![[19200394.png]]

Проверьте короткое замыкание от контакта 42 разъёма проводов привода со всеми штифтами в разъёме проводов датчика.

Включить испытательный щуп в контакт 42 разъёма проводов привода. Подсоедините аллигаторный клип испытательного щупа к многометровому щупу. Вставьте другой измерительный щуп во все штифты разъёма датчика проводов.

Измерьте сопротивление.

Мультиметр **должен** показывать открытую схему (более 100k ом).

> [!missing]- Иллюстрация `19200395.png` не извлечена — смотрите PDF-оригинал документа

Если схема **не** открыта, между контактом 42 разъёма приводной проводов и любым штифтом в разъёме проводной цепи датчика, который измерял замкнутую цепь, имеется короткое замыкание.

Ремонт или замена датчика проводов жгута. См. процедуру[[82-019-043-tr — Engine Wiring Harness|019-043]].

Подключите все компоненты после завершения ремонта.

> [!missing]- Иллюстрация `19200395.png` не извлечена — смотрите PDF-оригинал документа


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The ISM system can control the fan clutch activation. The ECM energizes the fan clutch or air valve solenoid.
>
> See vehicle manufacturer's publications for more information on troubleshooting and repair of the fan clutch wiring.
>
> The fan clutch circuit is in the actuator harness. The fan clutch actuator signal wire runs from pin 5 in the actuator harness connector to pin 12 in the 31-pin Deutsch connector at the OEM harness. The fan clutch actuator return wire runs from pin 42 in the actuator harness connector to pin 13 in the 31-pin Deutsch connector at the OEM harness. From the 31-pin Deutsch connector, the circuit passes through the OEM wiring to the fan clutch.
>
> ### Resistance Check
>
> **CAUTION · Осторожно**
> Do not use probes or leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins of the connector.
>
> Disconnect the actuator harness connector from the ECM. Disconnect the OEM wiring at the fan clutch solenoid. Set the multimeter to the resistance setting.
>
> Insert a test lead into pin 5 of the actuator harness connector, and connect it to the multimeter probe.
>
> Touch the other multimeter probe to the connector terminal of the fan clutch solenoid. Make sure the fan clutch solenoid is disconnected.
>
> Measure the resistance.
>
> The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is closed, it **must** still be checked for a short circuit to ground and a short circuit from pin to pin. If the circuit is **not** closed, there is a connection problem or an open circuit in the wiring harness.
>
> Remove the lead from pin 5 and insert it into pin 42 of the actuator harness connector. Touch the other multimeter probe to the connector terminal of the other fan clutch solenoid. Make sure the fan clutch solenoid is disconnected.
>
> Measure the resistance.
>
> The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is closed, it **must** still be checked for a short circuit to ground and a short circuit from pin to pin.
>
> If the circuit is **not** closed, there is a connection problem or an open circuit in the wiring harness.
>
> Check the harness connections at the 31-pin Deutsch connector.
>
> If the connections are good, isolate the open circuit to the OEM wiring to the fan clutch solenoid or the actuator harness as described in the following steps.
>
> Check the OEM wiring to the fan clutch solenoid for an open circuit. Disconnect the 31-pin Deutsch connector.
>
> Insert the multimeter lead into pin 12 of the 31-pin connector.
>
> Touch the other multimeter probe to the fan clutch solenoid connector terminal. Measure the resistance.
>
> The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, there is an open circuit in the OEM wiring to the fan clutch solenoid. Repair or replace the OEM harness according to the OEM procedures.
>
> Remove the lead from pin 12 of the 31-pin connector and insert it into pin 13 of the 31-pin connector.
>
> Touch the other multimeter probe to the fan clutch solenoid connector terminal. Measure the resistance.
>
> The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, there is an open circuit in the OEM wiring to the fan clutch solenoid.
>
> Repair or replace the OEM harness according to the OEM procedures.
>
> ### Check for Short Circuit from Pin to Pin
>
> Check for a short circuit between pin 5 and all of the other pins in the actuator harness connector. Make sure the fan clutch solenoid is disconnected. Make sure the battery voltage supply is disconnected.
>
> Insert a test lead into pin 5 of the actuator harness connector. Insert the other test lead into all other pins of the actuator harness connector, one at a time.
>
> Measure the resistance.
>
> The multimeter **must** show an open circuit (more than 100k ohms) at all pins.
>
> If the circuit is **not** open, there is a short circuit between pin 5 and any pin that measured a closed circuit.
>
> Repair or replace the actuator harness.
>
> Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].
>
> Check for a short circuit between pin 42 and all other pins in the actuator harness connector. Make sure the fan clutch solenoid is disconnected. Make sure the battery voltage supply is disconnected.
>
> Insert a test lead into pin 42 of the actuator harness connector. Insert the other lead into all other pins of the actuator harness connector, one at a time.
>
> Measure the resistance.
>
> The multimeter **must** show an open circuit (more than 100k ohms) at all pins.
>
> If the circuit is **not** open, there is a short circuit between pin 42 and any pin that measured a closed circuit.
>
> Repair or replace the actuator harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].
>
> Disconnect the sensor harness connector from the ECM.
>
> Check for a short circuit from pin 5 of the actuator harness connector to all pins in the sensor harness connector.
>
> Insert test lead into pin 5 of the actuator harness connector. Connect the alligator clip of the test lead to the multimeter probe. Insert the other test lead into all pins of the sensor harness connector.
>
> Measure the resistance.
>
> The multimeter **must** show an open circuit (more than 100k ohms).
>
> If the circuit is **not** open, there is a short circuit between pin 5 of the actuator harness connector and any pin in the sensor harness connector which measured a closed circuit.
>
> Repair or replace the sensor harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].
>
> Check for a short circuit from pin 42 of the actuator harness connector to all pins in the sensor harness connector.
>
> Insert the test lead into pin 42 of the actuator harness connector. Connect the alligator clip of the test lead to the multimeter probe. Insert the other test lead into all pins of the sensor harness connector.
>
> Measure the resistance.
>
> The multimeter **must** show an open circuit (more than 100k ohms).
>
> If the circuit is **not** open, there is a short circuit between pin 42 of the actuator harness connector and any pin in the sensor harness connector which measured a closed circuit.
>
> Repair or replace the sensor harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].
>
> Connect all components after the repair is complete.
