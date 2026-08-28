---
aliases:
  - "Цепь общедоступной шины данных"
type: "Процедура"
doc: "96-019-026"
title_en: "Data Link Circuit, Public"
title_ru: "Цепь общедоступной шины данных"
modified: "2004-04-28"
engines:
  - "37292556"
  - "37295879"
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
  - "QST30"
manuals:
  - "3666231"
figures: 11
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-019-026.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/96-019-026.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "двигатель/QST30"
  - "группа/96"
  - "перевод/машинный"
---

# Data Link Circuit, Public
**Цепь общедоступной шины данных**

> [!abstract] Процедура · `96-019-026`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11, QST30
> **Входит в руководства:** [[3666231 — Centinel™ Master Repair Manual|3666231]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2004-04-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-019-026.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/96-019-026.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Только тяжёлая

Для связи с модулем управления CentinelTM используется общедоступная схема шины данных CAN для электронного инструментария обслуживания.

> [!note] Примечание
> Сервисное оборудование не предоставляется для приложений Heavy-Duty. Модуль управления CentinelTM будет использовать шину данных CAN.

![[19800337.png]]

Для двигателей CelectTM Plus шина данных CAN работает и использует 6-контактный разъем Deutsch. (Для двигателей CelectTM к публичной шине данных CAN осуществляется доступ через сплайсы в кабине управляющей проводов.) Положения проводов следуют:

Положение A - шина данных CAN (+)

Положение B - шина данных CAN (-)

Положение C - батарея (12 или 24 VDC)

Позиция D - Открытый

Положение E - Блок-земля

Позиция F -

Не

использовано.

![[19801499.png]]

### Проверка сопротивления

> [!warning] ОСТОРОЖНО
> Используйте измерительный щуп, Номер детали 3822758, на разъеме модуля управления CentinelTM и используйте измерительный щуп, Номер детали 3823993, на разъеме 6-контактного Deutsch, чтобы избежать повреждения контактов разъема.

Отсоедините разъём жгута проводов от модуля управления CentinelTM и разъема Deutsch 6-pin.

Переключатель зажигания переключателя в положение "OFF".

Измерьте сопротивление от контакта 8 (тяжело-голубой) или контакта 6 (высокопроизводительный) разъёма управляющего модуля CentinelTM для подключения к контакту A 6-контактного разъема Deutsch (или надлежащего сплайса провода для установки Celect).

Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

Если схема **не** закрыта, отремонтируйте или замените проводную упряжку CentinelTM. См. процедуру[[96-019-131-tr — Centinel™ Wiring Harness|019-131]].

![[19801500.png]]

Измерьте сопротивление от контакта 9 (тяжело-голубой) или контакта 8 (высокопроизводительный) разъёма управляющего модуля CentinelTM для подключения к контакту B 6-контактного разъема Deutsch (или надлежащего сплайса провода для установки CelectTM).

Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

Если схема **не** закрыта, отремонтируйте или замените проводную упряжку CentinelTM. См. процедуру[[96-019-131-tr — Centinel™ Wiring Harness|019-131]].

![[19801501.png]]

### Проверка на замыкание на массу

> [!warning] ОСТОРОЖНО
> Используйте измерительный щуп, номер детали 3823993, для 6-контактного разъема Deutsch, чтобы избежать повреждения контактов разъема.

Отсоедините разъём жгута проводов от модуля управления CentinelTM.

Измерьте сопротивление от контакта А разъема Deutsch или контакта 8 модуля управления CentinelTM, проводящего разъем жгута проводов к блоку двигателя.

Мультиметр **должен** показывать открытую схему (1 М Ом или более).

Если схема **не** открыта, отремонтируйте или замените проводную упряжку CentinelTM. См. процедуру[[96-019-131-tr — Centinel™ Wiring Harness|019-131]].

![[19801502.png]]

Измерьте сопротивление от контакта B 6-контактного разъема Deutsch или контакта 9 модуля управления CentinelTM, проводящего разъем жгута проводов к блоку двигателя. Мультиметр **должен** показывать открытую схему (1 М Ом или более).

Если схема **не** открыта, отремонтируйте или замените проводную упряжку CentinelTM. См. процедуру[[96-019-131-tr — Centinel™ Wiring Harness|019-131]].

![[19801503.png]]

### Проверка на замыкание между контактами

немецкий

Измерьте сопротивление от контакта B ко всем другим штифтам в разъеме. Мультиметр **должен** показывать открытую схему (1 М Ом или более).

Если схема **не** открыта, отремонтируйте или замените проводную упряжку CentinelTM. Смотрите соответствующее руководство по устранению неполадок и ремонту базового двигателя.

![[19801505.png]]

Измерьте сопротивление от контакта C ко всем другим штифтам в разъеме. Мультиметр **должен** показывать открытую схему (1 М Ом или более).

Если схема **не** открыта, отремонтируйте или замените проводную упряжку CentinelTM. Смотрите соответствующее руководство по устранению неполадок и ремонту базового двигателя.

![[19801506.png]]

### Проверка напряжения

Найдите разъем шины данных CAN на проводной ремне CentinelTM. Месторасположение будет зависеть от процедур установки.

![[19801507.png]]

> [!warning] ОСТОРОЖНО
> Используйте измерительный щуп, номер детали 3823993, для 6-контактного разъема Deutsch, чтобы избежать повреждения контактов разъема.

Включите замок зажигания.

Включите циферблат на мультиметре для измерения напряжения постоянного тока.

Измерьте напряжение от контакта 8 модуля управления CentinelTM, проводящего разъём жгута проводов к блоку двигателя. Мультиметр **must** показывает от 2,5 до 5 VDC.

![[19801508.png]]

Измерьте напряжение от контакта 9 модуля управления CentinelTM, проводящего разъём жгута проводов к блоку двигателя. Мультиметр **must** показывает от 0 до 2,5 VDC.

![[19801509.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> Heavy-Duty Only
>
> To communicate with the Centinel™ control module, the public datalink circuit is used for an electronic service tool.
>
> **Note · Примечание**
> No service tool is provided for Heavy-Duty applications. The Centinel™ control module will use the public datalink.
>
> For Celect™ Plus engines, the datalink is powered and uses a 6-pin Deutsch connector. (For Celect™ engines, the public datalink is accessed by the control harness through splices in the cab.) The wiring positions follow:
>
> Position A - Datalink (+)
>
> Position B - Datalink (-)
>
> Position C - Battery (12 or 24 VDC)
>
> Position D - Open
>
> Position E - Block ground
>
> Position F -
>
> Not
>
> used.
>
> ### Resistance Check
>
> **CAUTION · Осторожно**
> Use test lead, Part Number 3822758, on the Centinel™ control module connector and use test lead, Part Number 3823993, on the 6-pin Deutsch connector to avoid damage to the connector pins.
>
> Disconnect the harness connector from the Centinel™ control module and the Deutsch 6-pin connector.
>
> Turn the keyswitch to the “OFF” position.
>
> Measure the resistance from pin 8 (Heavy-Duty) or pin 6 (High-Horsepower) of the Centinel™ control module harness connector to pin A of the 6-pin Deutsch connector (or the proper wire splice for the Celect installation).
>
> The multimeter **must** show a closed circuit (10 ohms or less).
>
> If the circuit is **not** closed, repair or replace the Centinel™ harness. Refer to Procedure [[96-019-131-tr — Centinel™ Wiring Harness|019-131]].
>
> Measure the resistance from pin 9 (Heavy-Duty) or pin 8 (High-Horsepower) of the Centinel™ control module harness connector to pin B of the 6-pin Deutsch connector (or the proper wire splice for the Celect™ installation).
>
> The multimeter **must** show a closed circuit (10 ohms or less).
>
> If the circuit is **not** closed, repair or replace the Centinel™ harness. Refer to Procedure [[96-019-131-tr — Centinel™ Wiring Harness|019-131]].
>
> ### Check for Short Circuit to Ground
>
> **CAUTION · Осторожно**
> Use test lead, Part Number 3823993, for the 6-pin Deutsch connector to avoid damage to the connector pins.
>
> Disconnect the harness connector from the Centinel™ control module.
>
> Measure the resistance from pin A of the Deutsch connector or pin 8 of the Centinel™ control module harness connector to the engine block.
>
> The multimeter **must** show an open circuit (1M ohms or more).
>
> If the circuit is **not** open, repair or replace the Centinel™ harness. Refer to Procedure [[96-019-131-tr — Centinel™ Wiring Harness|019-131]].
>
> Measure the resistance from pin B of the 6-pin Deutsch connector or pin 9 of the Centinel™ control module harness connector to the engine block. The multimeter **must** show an open circuit (1M ohms or more).
>
> If the circuit is **not** open, repair or replace the Centinel™ harness. Refer to Procedure [[96-019-131-tr — Centinel™ Wiring Harness|019-131]].
>
> ### Check for Short Circuit from Pin to Pin
>
> Deutsch
>
> Measure the resistance from pin B to all other pins in the connector. The multimeter **must** show an open circuit (1M ohms or more).
>
> If the circuit is **not** open, repair or replace the Centinel™ harness. Refer to the appropriate base engine troubleshooting and repair manual.
>
> Measure the resistance from pin C to all other pins in the connector. The multimeter **must** show an open circuit (1M ohms or more).
>
> If the circuit is **not** open, repair or replace the Centinel™ harness. Refer to the appropriate base engine troubleshooting and repair manual.
>
> ### Voltage Check
>
> Locate the datalink connector on the Centinel™ harness. The location will depend on the installation procedures.
>
> **CAUTION · Осторожно**
> Use test lead, Part Number 3823993, for the 6-pin Deutsch connector to avoid damage to the connector pins.
>
> Turn the keyswitch ON.
>
> Turn the dial on the multimeter to measure DC voltage.
>
> Measure the voltage from pin 8 of the Centinel™ control module harness connector to the engine block. The multimeter **must** show 2.5 to 5 VDC.
>
> Measure the voltage from pin 9 of the Centinel™ control module harness connector to the engine block. The multimeter **must** show 0 to 2.5 VDC.
