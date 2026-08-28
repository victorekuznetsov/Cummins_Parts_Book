---
aliases:
  - "Цепь выключателя регулировки холостого хода"
type: "Процедура"
doc: "99-019-053"
title_en: "Idle Adjust Switch Circuit"
title_ru: "Цепь выключателя регулировки холостого хода"
modified: "2015-06-25"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "37292556"
  - "37295879"
  - "41343322"
  - "41370103"
  - "85017333"
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
  - "NT/NTA855 · ISM/QSM11"
  - "QSK23"
  - "QSK60"
  - "QST30"
manuals:
  - "3666113"
  - "3666214"
  - "3666266"
  - "4021442"
figures: 6
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-053.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-053.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "двигатель/NT/NTA855"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "двигатель/QST30"
  - "группа/99"
  - "перевод/машинный"
---

# Idle Adjust Switch Circuit
**Цепь выключателя регулировки холостого хода**

> [!abstract] Процедура · `99-019-053`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]], [[85017333 — QSK23 CM500 CPL 2858|85017333]], [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3, NT/NTA855 · ISM/QSM11, QSK23, QSK60, QST30
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]], [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]], [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]], [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section 19 - Electronic Engine Controls · Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2015-06-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-053.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-053.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

> [!warning] ОСТОРОЖНО
> Правильные провода и/или одобренный Cummins® инструмент для тестирования цепи должны использоваться при работе с электрическими разъемами для предотвращения расширения штифта и повреждения разъема.

> [!note] Примечание
> Диагностический переключатель (Idle/diagnostic increment/decrement switch) - это переключатель выбора круиз-контроля/PTO/set/resume.

Если доступна электронная сервисная оснастка, проверьте схему переключателя настройки холостого хода для правильной работы. Если **не,** следуйте процедурам устранения неполадок в этом разделе.

Отключите разъем интерфейса оригинального производителя оборудования (OEM) проводов жгута проводов двигателя. Чтобы определить местоположение разъема, см. соответствующую схему проводов двигателя.

Вставьте штифт испытательного щупа в сигнал круиз-контроля/PTO-набора/переключателя поперечной связи в разъеме OEM-проводов. Измерьте сопротивление от сигнала круиз-контроля / PTO-набора / поворота на блок двигателя.

![[19c01166.png]]

Держите выключатель регулирования холостого хода в положительном (+) положении приращения.

Если OEM подключил обратный провод к земле шасси, мультиметр **должен** показать замкнутую цепь (10 Ом или менее) при удерживании переключателя и вернуться к открытой цепи (100 К Ом или более), когда переключатель выпущен. Схема **должна** оставаться открытой, когда переключатель находится в отрицательном (-) положении декремента.

Если OEM подключил обратный провод к разъему ECM OEM, мультиметр **должен** показать открытую схему (100k Ом или более) при включении переключателя и возврате к замкнутой схеме (10 Ом или менее), когда переключатель выпущен. Схема **должна** оставаться замкнутой, когда переключатель находится в отрицательном (-) положении декремента.

Если значения сопротивления **не** верны, убедитесь, что обратный провод и провод сигнала круиз-контроля / PTO-набора / поперечного переключателя правильно установлены на выключателе регулирования холостого хода. Если оба провода правильно установлены, проверьте обратный провод и провод сигнала круиз-контроля / PTO-набора / поперечного переключателя для открытых цепей при условии, что переключатель регулирования холостого хода ранее был проверен на короткое замыкание на землю.

![[19c01245.png]]

Удалите свинец из сигнала круиз-контроля / PTO set / Coast switch и вставьте его в сигнал коммутатора круиз-контроля / PTO resume / Acceleerator.

Держите выключатель регулирования холостого хода в отрицательном (-) положении декремента. Мультиметр **должен **показывать замкнутую цепь (10 Ом или меньше), когда переключатель удерживается в положении декремента, и открытую цепь (100 К Ом или более), когда переключатель высвобождается. Схема должна оставаться открытой, когда переключатель находится в положительном (+) положении приращения.

Если значения сопротивления **не** верны, убедитесь, что на выключателе регулирования холостого хода правильно установлен сигнальный провод круиз-контроля/PTO-резюме/ускорителя. Если провод сигнала коммутатора круиз-контроля/PTO-резюме/ускорителя правильно установлен на выключателе регулирования холостого хода, проверьте провод сигнала коммутатора круиз-контроля/PTO-резюме/ускорителя для открытой цепи при условии, что выключатель регулирования холостого хода ранее был проверен на короткое замыкание на землю.

![[19c01246.png]]

### Проверка на замыкание на массу

Отсоедините провод простаивания/диагностики (прикрепленный к сигналу переключения круиз-контроля/PTO-резюме/ускорителя) от переключателя.

Измерьте сопротивление сигнала переключения круиз-контроля / PTO / ускорителя от разъема проводов OEM к блоку двигателя.

![[19c01247.png]]

Мультиметр **должен** показать обрыв цепи (100 кОм и более). Если схема **не** открыта, в схеме коммутатора круиз-контроля/PTO-резюме/ускорителя есть короткое замыкание, при условии, что выключатель регулирования холостого хода был ранее проверен.

Ремонт или замена провода, подключенного к сигналу коммутатора круиз-контроля/PTO-резюме/ускорителя в электропроводке OEM-прицепа в соответствии с инструкциями производителя транспортного средства.

Чтобы проверить провод инкремента холостого/диагностического приращения (прикрепленный к сигналу круиз-контроля/PTO-набора/переключателя прикрытия) для коротких замыканий на землю, следуйте той же процедуре, что описана выше для провода холостого/диагностического убывания.

![[19c01248.png]]

### Проверка на замыкание между контактами

Измерьте сопротивление от сигнала переключения круиз-контроля / PTO-резюме / ускорителя разъёма проводов OEM-проводов со всеми другими штифтами в разъеме. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, между проводом, подключенным к сигналу переключения круиз-контроля/PTO-резюме/ускорителю, и любым штифтом, который измеряется менее 100k Ом, есть короткое замыкание.

Ремонт или замена проводов в электропроводке OEM в соответствии с инструкциями производителя транспортного средства.

Удалите свинец из сигнала коммутатора круиз-контроля / PTO resume / ускорителя разъёма проводов OEM-проводов и вставьте его в сигнал коммутатора круиз-контроля / PTO set / Coastt разъема. Измерьте сопротивление от сигнала круиз-контроля / PTO-набора / поворота на все другие контакты в разъеме. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, между проводом, подключенным к сигналу круиз-контроля/PTO-набора/побережного переключателя, и любым штифтом, который измеряется менее 100k Ом, имеется короткое замыкание при условии, что переключатель регулирования холостого хода был ранее проверен.

Ремонт или замена проводов в электропроводке OEM в соответствии с инструкциями производителя транспортного средства.

После ремонта подсоедините все компоненты.

![[19c01249.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> **CAUTION · Осторожно**
> Proper leads and/or a Cummins® approved circuit testing tool must be used when working with electrical connectors to prevent pin expansion and damage to the connector.
>
> **Note · Примечание**
> The idle/diagnostic increment/decrement switch is the cruise control/PTO/set/resume select switch.
>
> If electronic service tool is available, monitor the idle adjust switch circuit for proper operation. If **not,** follow the troubleshooting procedures in this section.
>
> Disconnect the original equipment manufacturer (OEM) harness engine interface connector. To determine the location of the connector, see the corresponding engine wiring diagram.
>
> Insert the pin of the test lead into the cruise control/PTO set/coast switch signal in the OEM harness connector. Measure the resistance from the cruise control/PTO set/coast switch signal to the engine block.
>
> Hold the idle adjust switch in the positive (+) increment position.
>
> If the OEM connected the return wire to chassis ground the multimeter **must** show a closed circuit (10 ohms or less) while holding the switch on and return to an open circuit (100K ohms or more) when the switch is released. The circuit **must** remain an open circuit when the switch is in the decrement negative (-) position.
>
> If the OEM connected the return wire to the ECM OEM connector the multimeter **must** show an open circuit (100k ohms or more) while holding the switch on and return to a closed circuit (10 ohms or less) when the switch is released. The circuit **must** remain a closed circuit when the switch is in the decrement negative (-) position.
>
> If the resistance values are **not** correct, make sure the return wire and the cruise control/PTO set/coast switch signal wire are properly installed on the idle adjust switch. If both wires are correctly installed, inspect the return wire and the cruise control/PTO set/coast switch signal wire for open circuits, provided the idle adjust switch has been previously checked for short circuits to ground.
>
> Remove the lead from the cruise control/PTO set/coast switch signal and insert it into the cruise control/PTO resume/accelerator switch signal.
>
> Hold the idle adjust switch in the negative (-) decrement position. The multimeter **must** show a closed circuit (10 ohms or less) when the switch is held in the decrement position and an open circuit (100K ohms or more) when the switch is released. The circuit **must** remain an open circuit when the switch is in the positive (+) increment position.
>
> If the resistance values are **not** correct, make sure the cruise control/PTO resume/accelerator switch signal wire is properly installed on the idle adjust switch. If the cruise control/PTO resume/accelerator switch signal wire is properly installed on the idle adjust switch, inspect the cruise control/PTO resume/accelerator switch signal wire for an open circuit, provided the idle adjust switch has been previously checked for short circuits to ground.
>
> ### Check for Short Circuit to Ground
>
> Disconnect the idle/diagnostic decrement wire (attached to the cruise control/PTO resume/ accelerator switch signal) from the switch.
>
> Measure the resistance from the cruise control/PTO resume/accelerator switch signal of the OEM harness connector to the engine block.
>
> The multimeter **must** show an open circuit (100K ohms or more). If the circuit is **not** open, there is a short circuit to ground in the cruise control/PTO resume/accelerator switch signal circuit, provided the idle adjust switch has been previously checked.
>
> Repair or replace the wire connected to the cruise control/PTO resume/accelerator switch signal in the OEM harness according to the vehicle manufacturer's instructions.
>
> To check the idle/diagnostic increment wire (attached the to cruise control/PTO set/coast switch signal) for short circuits to ground, follow the same procedure as described above for the idle/diagnostic decrement wire.
>
> ### Check for Short Circuit from Pin to Pin
>
> Measure the resistance from the cruise control/PTO resume/accelerator switch signal of the OEM harness connector to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, there is a short circuit between the wire connected to the cruise control/PTO resume/accelerator switch signal and any pin that measured less than 100k ohms.
>
> Repair or replace the wires in the OEM harness according to the vehicle manufacturer's instructions.
>
> Remove the lead from the cruise control/PTO resume/accelerator switch signal of the OEM harness connector and insert it into the cruise control/PTO set/coast switch signal of the connector. Measure the resistance from the cruise control/PTO set/coast switch signal to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, there is a short circuit between the wire connected to the cruise control/PTO set/coast switch signal and any pin that measured less than 100k ohms, provided the idle adjust switch has been previously checked.
>
> Repair or replace the wires in the OEM harness according to the vehicle manufacturer's instructions.
>
> Connect all components after completing the repair.
