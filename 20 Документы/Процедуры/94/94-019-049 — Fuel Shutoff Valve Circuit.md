---
aliases:
  - "Цепь клапана отсечки топлива"
type: "Процедура"
doc: "94-019-049"
title_en: "Fuel Shutoff Valve Circuit"
title_ru: "Цепь клапана отсечки топлива"
modified: "2003-03-24"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666184"
figures: 14
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-019-049.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/94-019-049.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/94"
  - "перевод/машинный"
---

# Fuel Shutoff Valve Circuit
**Цепь клапана отсечки топлива**

> [!abstract] Процедура · `94-019-049`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-03-24
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-019-049.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/94-019-049.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Первичная проверка

Проверьте выключающую соленоидную позицию топлива на наличие дополнительных проводов, которые могут быть подключены для подачи питания на другое устройство. Удалите дополнительные провода, которые найдены связанными с соленоидным столбом.

> [!note] Примечание
> Обязательно проверьте оба соленоида отключения топлива.

![[19400454.png]]

### Проверка сопротивления

Схемы запорного клапана топлива представляют собой сигнальные провода B+, контакты 39 и 40, проводов двигателя к соленоидам запорного клапана топлива. Соленоиды заземляются через провода наземных проводов, которые крепятся к крепежному болту или посту на соленоиде, предусмотренному на изолированных топливных соленоидных запорных клапанах, которые являются необязательными.

![[19400242.png]]

Используйте 4 мм \[5/32 в \] шестиглавый ключ для отключения проводов двигателя с помощью разъема Deutsch от ECM.

![[19400242.png]]

Проверьте контакты разъема ECM и проводов двигателя для повреждения.

![[19400007.png]]

Отсоедините отключение топлива соленоидной проволокой от соленоидного поста. Проверьте терминал колец соленоидной проволоки на предмет повреждения.

> [!note] Примечание
> Обязательно проверьте оба соленоида отключения топлива.

![[19400088.png]]

> [!warning] ОСТОРОЖНО
> Не используйте ни пробы, ни зацепки, кроме Части Нет. 3822758. Разъём будет повреждён. Лиды должны плотно вписываться в разъем без расширения штифтов разъема.

Вставьте штифт одного свинца в контакт 39 разъёма проводов двигателя. Подключите аллигатор к многометровому щупу.

![[19a00033.png]]

Прикосновение к другому мультиметру приводит к соответствующему запорному клапану соленоидной проволоки. Измерьте сопротивление. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее). Если цепь ** не** закрыта, отремонтируйте или замените электропроводку двигателя. См. процедуры 019-197, 019-199,[[94-019-240 — Connector, 40-Pin|019-240]]или[[94-019-043 — Engine Wiring Harness|019-043]]. Если цепь закрыта, ее **** все равно нужно проверить на короткое расстояние до земли и короткое расстояние от пин-кодов до пин-кодов.

![[19a00033.png]]

Вставьте штифт одного свинца в контакт 40 разъёма ремня электропроводки двигателя. Подключите аллигатор к многометровому щупу.

Прикосновение к другому мультиметру приводит к соответствующему запорному клапану соленоидной проволоки. Измерьте сопротивление. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее). Если цепь ** не** закрыта, отремонтируйте или замените электропроводку двигателя. См. процедуры 019-197, 019-199,[[94-019-240 — Connector, 40-Pin|019-240]]или[[94-019-043 — Engine Wiring Harness|019-043]]. Если цепь закрыта, ее **** все равно нужно проверить на короткое расстояние до земли и короткое расстояние от пин-кодов до пин-кодов.

![[19a00033.png]]

### Проверка на замыкание на массу

Введите свинец в контакт 39. Прикоснитесь к другому многометровому щупу, чтобы заблокировать двигатель. Кольцевой терминал в соответствующем соленоиде ** должен быть отключен и может ** не касаться ничего, что заземлено. Измерьте сопротивление. Мультиметр ** должен** показывать открытую схему (более 100k ом). Если цепь ** не открыта, в проводе, подключенном к контакту 39, есть короткое заземление. Ремонт или замена ремня электропроводки двигателя. См. Процедуры 019-197,[[94-019-240 — Connector, 40-Pin|019-240]]и[[94-019-043 — Engine Wiring Harness|019-043]].

![[19a00033.png]]

Вставьте свинец в контакт 40. Прикоснитесь к другому многометровому щупу, чтобы заблокировать двигатель. Кольцевой терминал в соответствующем соленоиде ** должен быть отключен и может ** не касаться ничего, что заземлено. Измерьте сопротивление. Мультиметр ** должен** показывать открытую схему (более 100k ом). Если цепь ** не открыта, в проводе, подключенном к контакту 40, есть короткое заземление. Ремонт или замена ремня электропроводки двигателя. См. Процедуры 019-197,[[94-019-240 — Connector, 40-Pin|019-240]]и[[94-019-043 — Engine Wiring Harness|019-043]].

![[19a00033.png]]

### Проверка на замыкание между контактами

Проверьте короткое замыкание от контакта 39 до всех других контактов в разъеме ремня электропроводки двигателя. Подключите один измерительный щуп к контакту 39. Используйте другой щуп для проверки всех других контактов в разъеме.

Кольцевой терминал в соответствующем соленоиде ** должен быть отключен и может ** не касаться ничего, что заземлено.

![[19a00033.png]]

Измерьте сопротивление. Мультиметр ** должен** показывать открытую схему (более 100k ом). Если схема ** не открыта, между контактом 39 и любым штифтом, который измеряет замкнутую цепь, есть короткое расстояние. Ремонт или замена ремня электропроводки двигателя. См. Процедуры 019-199,[[94-019-240 — Connector, 40-Pin|019-240]]и[[94-019-043 — Engine Wiring Harness|019-043]].

![[19a00029.png]]

Проверьте короткое замыкание от контакта 40 до всех других контактов в разъеме ремня электропроводки двигателя. Подключите один измерительный щуп к контакту 40. Используйте другой щуп для проверки всех других контактов в разъеме.

Кольцевой терминал в соответствующем соленоиде ** должен быть отключен и может ** не касаться ничего, что заземлено.

![[19a00033.png]]

Измерьте сопротивление. Мультиметр ** должен** показывать открытую схему (более 100k ом). Если схема ** не открыта, между контактом 40 и любым штифтом, который измеряет замкнутую цепь, есть короткое расстояние. Ремонт или замена ремня электропроводки двигателя. См. Процедуры 019-199,[[94-019-240 — Connector, 40-Pin|019-240]]и[[94-019-043 — Engine Wiring Harness|019-043]].

![[19a00029.png]]


> [!quote]- Original (English) · английский оригинал
> ### Initial Check
>
> Inspect the fuel shutoff solenoid post for extra wires that may be connected to supply power to another device. Remove the extra wires that are found connected to the solenoid post.
>
> **Note · Примечание**
> Be sure to check both fuel shutoff solenoids.
>
> ### Resistance Check
>
> The fuel shutoff valve circuits are B+ signal wires, pins 39 and 40, of the engine harness to the fuel shutoff valve solenoids. The solenoids are grounded through the harness ground wires, which are attached to a mounting bolt or a post on the solenoid provided on isolated fuel solenoid shutoff valves, which are optional.
>
> Use a 4 mm \[5/32 in\] hex head wrench to disconnect the engine harness Deutsch connector from the ECM.
>
> Check the ECM and engine harness connector pins for damage.
>
> Disconnect the fuel shutoff solenoid wire from the solenoid post. Check the solenoid wire ring terminal for damage.
>
> **Note · Примечание**
> Be sure to check both fuel shutoff solenoids.
>
> **CAUTION · Осторожно**
> Do not use probes or leads other than Part No. 3822758. The connector will be damaged. The leads must fit tight in the connector without expanding the pins of the connector.
>
> Insert the pin of one lead into pin 39 of the engine harness connector. Connect the alligator clip to the multimeter probe.
>
> Touch the other multimeter lead to the corresponding fuel shutoff valve solenoid wire. Measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, repair or replace the engine harness. Refer to procedures 019-197, 019-199, [[94-019-240 — Connector, 40-Pin|019-240]], or [[94-019-043 — Engine Wiring Harness|019-043]]. If the circuit is closed, it **must** still be checked for a short to ground and a short from pin to pin.
>
> Insert the pin of one lead into pin 40 of the engine harness connector. Connect the alligator clip to the multimeter probe.
>
> Touch the other multimeter lead to the corresponding fuel shutoff valve solenoid wire. Measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, repair or replace the engine harness. Refer to procedures 019-197, 019-199, [[94-019-240 — Connector, 40-Pin|019-240]], or [[94-019-043 — Engine Wiring Harness|019-043]]. If the circuit is closed, it **must** still be checked for a short to ground and a short from pin to pin.
>
> ### Check for Short Circuit to Ground
>
> Insert the lead into pin 39. Touch the other multimeter probe to engine block. The ring terminal at the corresponding solenoid **must** be disconnected and can **not** touch anything that is grounded. Measure the resistance. The multimeter **must** show an open circuit (more than 100k ohms). If the circuit is **not** open, there is a short to ground in the wire connected to pin 39. Repair or replace the engine harness. Refer to Procedures 019-197, [[94-019-240 — Connector, 40-Pin|019-240]], and [[94-019-043 — Engine Wiring Harness|019-043]].
>
> Insert the lead into pin 40. Touch the other multimeter probe to engine block. The ring terminal at the corresponding solenoid **must** be disconnected and can **not** touch anything that is grounded. Measure the resistance. The multimeter **must** show an open circuit (more than 100k ohms). If the circuit is **not** open, there is a short to ground in the wire connected to pin 40. Repair or replace the engine harness. Refer to Procedures 019-197, [[94-019-240 — Connector, 40-Pin|019-240]], and [[94-019-043 — Engine Wiring Harness|019-043]].
>
> ### Check for Short Circuit from Pin to Pin
>
> Check for a short circuit from pin 39 to all of the other pins in the engine harness connector. Connect one test lead to pin 39. Use the other probe to test all of the other pins in the connector.
>
> The ring terminal at the corresponding solenoid **must** be disconnected and can **not** touch anything that is grounded.
>
> Measure the resistance. The multimeter **must** show an open circuit (more than 100k ohms). If the circuit is **not** open, there is a short between pin 39 and any pin that measured a closed circuit. Repair or replace the engine harness. Refer to Procedures 019-199, [[94-019-240 — Connector, 40-Pin|019-240]], and [[94-019-043 — Engine Wiring Harness|019-043]].
>
> Check for a short circuit from pin 40 to all of the other pins in the engine harness connector. Connect one test lead to pin 40. Use the other probe to test all of the other pins in the connector.
>
> The ring terminal at the corresponding solenoid **must** be disconnected and can **not** touch anything that is grounded.
>
> Measure the resistance. The multimeter **must** show an open circuit (more than 100k ohms). If the circuit is **not** open, there is a short between pin 40 and any pin that measured a closed circuit. Repair or replace the engine harness. Refer to Procedures 019-199, [[94-019-240 — Connector, 40-Pin|019-240]], and [[94-019-043 — Engine Wiring Harness|019-043]].
