---
aliases:
  - "Цепь общедоступной шины данных"
type: "Процедура"
doc: "01-019-026"
title_en: "Data Link Circuit, Public"
title_ru: "Цепь общедоступной шины данных"
modified: "2002-12-05"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 6
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-026.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-019-026.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Data Link Circuit, Public
**Цепь общедоступной шины данных**

> [!abstract] Процедура · `01-019-026`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2002-12-05
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-026.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-019-026.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Схема шины данных RS232 для связи с ECM используется для INPOWERTM. Шина данных RS485 может использоваться для передачи информации в электронном виде с другими электронными устройствами, такими как переключатели и внешние параллельные контроллеры.

![[19800902.png]]

Шина передачи данных CAN работает через 9-контактный разъем Deutsch. Позиции проводов следуют:

Позиция А - готовый набор данных

Позиция B - Получить

Положение С - передавать

Положение D - терминал данных готов

Положение Е - земля

Положение F - детектор несущих

Позиция G - просьба отправить

Позиция H - ясно для отправки

Положение J — кольцевой индикатор.

![[19802482.png]]

### Проверка сопротивления

Удалите разъем удлинителя проводов ремня от разъема ECM 05.

Используйте измерительный щуп, Номер детали 3822758, на разъеме ECM; и используйте измерительный щуп, Номер детали 3824812, на 9-контактном разъеме Deutsch.

Переключатель Run/Stop переключается в положение Stop.

Измерить сопротивление от набора данных готового провода, измеряя сопротивление от контакта А 9-контактного разъема Deutsch к соответствующим штифтам на разъеме ECM.

![[19802483.png]]

Если цепь ** не** закрыта, отремонтируйте или замените электропроводку двигателя. См. процедуру[[01-019-043 — Engine Wiring Harness|019-043]].

Сделайте выше для каждого штифта в 9-пиновом Deutsch.

![[19802483.png]]

### Проверка на замыкание на массу

Удалите разъём жгута проводов двигателя из разъема ECM 05.

Используйте измерительный щуп, номер детали 3824811, для 9-контактного разъема Deutsch.

Измерить сопротивление от набора данных готового провода, измеряя сопротивление от контакта А 9-контактного разъема Deutsch к блоку двигателя. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема ** не** открыта, отремонтируйте или замените электропроводку двигателя. См. процедуру[[01-019-043 — Engine Wiring Harness|019-043]].

Делайте это для каждого штифта в 9-пиновом Deutsch, кроме земли.

![[19802484.png]]

### Проверка на замыкание между контактами

** Deutsche Connector**

Удалите разъем удлинителя проводов ремня от разъема ECM 05.

Используйте измерительный щуп, номер детали 3824811, для 9-контактного разъема Deutsch. Измерьте сопротивление от узла обнаружения носителя ко всем другим штангам в разъеме. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема ** не** открыта, отремонтируйте или замените электропроводку двигателя. См. процедуру[[01-019-043 — Engine Wiring Harness|019-043]].

Следуйте приведенным выше инструкциям для каждого штифта в 9-контактном разъеме Deutsch.

![[19802485.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The RS232 public datalink circuit is used for INPOWER™ to communicate with the ECM. The RS485 public datalink can be used to communicate information electronically with other electronic devices, such as switch gears and external paralleling controllers.
>
> The datalink is powered through and uses a 9-pin Deutsch connector. The wiring positions follow:
>
> Position A - data set ready
>
> Position B - receive
>
> Position C - transmit
>
> Position D - data terminal ready
>
> Position E - ground
>
> Position F - carrier detect
>
> Position G - request to send
>
> Position H - clear to send
>
> Position J - ring indicator.
>
> ### Resistance Check
>
> Remove the extension harness connector from the ECM 05 connector.
>
> Use test lead, Part Number 3822758, on the ECM connector; and use test lead, Part Number 3824812, on the 9-pin Deutsch connector.
>
> Turn the Run/Stop switch to the Stop position.
>
> Measure the resistance from the data set ready wire by measuring the resistance from pin A of the 9-pin Deutsch connector to the corresponding pins on the ECM connector.
>
> If the circuit is **not** closed, repair or replace the engine harness. Refer to Procedure [[01-019-043 — Engine Wiring Harness|019-043]].
>
> Do the above for every pin in the 9-pin Deutsch.
>
> ### Check for Short Circuit to Ground
>
> Remove the engine harness connector from the ECM 05 connector.
>
> Use test lead, Part Number 3824811, for the 9-pin Deutsch connector.
>
> Measure the resistance from the data set ready wire by measuring the resistance from pin A of the 9-pin Deutsch connector to the engine block. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the engine harness. Refer to Procedure [[01-019-043 — Engine Wiring Harness|019-043]].
>
> Do this for every pin in the 9-pin Deutsch, except ground.
>
> ### Check for Short Circuit from Pin to Pin
>
> **Deutsch Connector**
>
> Remove the extension harness connector from the ECM 05 connector.
>
> Use test lead, Part Number 3824811, for the 9-pin Deutsch connector. Measure the resistance from the carrier detect pin to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the engine harness. Refer to Procedure [[01-019-043 — Engine Wiring Harness|019-043]].
>
> Follow the above instructions for every pin in the 9-pin Deutsch connector.
