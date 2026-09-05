---
aliases:
  - "Цепь клапана отсечки топлива"
type: "Процедура"
doc: "07-019-049"
title_en: "Fuel Shutoff Valve Circuit"
title_ru: "Цепь клапана отсечки топлива"
modified: "2004-03-19"
engines:
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "4021442"
figures: 8
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-019-049.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-019-049.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
  - "перевод/машинный"
---

# Fuel Shutoff Valve Circuit
**Цепь клапана отсечки топлива**

> [!abstract] Процедура · `07-019-049`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2004-03-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-019-049.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-019-049.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Первичная проверка

Проверьте выключающую соленоидную позицию топлива на наличие дополнительных проводов, которые могут быть подключены для подачи питания на другое устройство.

Удалите дополнительные провода, которые найдены связанными с соленоидным столбом.

![[19400454.png]]

Убедитесь, что оконечная станция **не** находится в контакте с топливным амортизатором или любым другим металлическим объектом, кроме оконечного устройства проводной ремни.

![[19400742.png]]

### Проверка сопротивления

Схема запорного клапана топлива представляет собой сигнальный провод запорного клапана топлива ремня проводов двигателя к соленоиду запорного клапана топлива.

Соленоид заземляется через двигатель.

Отсоедините электропроводку двигателя от электронного модуля управления (ECM).

![[19400242.png]]

Проверьте контакты разъема ECM и проводов двигателя для повреждения.

![[19400007.png]]

Отсоедините отключение топлива соленоидной проволокой от соленоидного поста.

Проверьте терминал колец соленоидной проволоки на предмет повреждения. См. процедуру[[99-019-197 — Ring Terminal|019-197]].

![[19400088.png]]

> [!warning] ОСТОРОЖНО
> Не используйте щупы или испытательные щупы, кроме Части 3822758, иначе разъем будет поврежден. Лиды должны плотно помещаться в разъеме без расширения штифтов разъема.

Вставьте штифт одного свинца в сигнальный контакт запорного клапана двигателя разъёма жгута.

Подключите аллигатор к многометровому щупу.

Прикосновение к другому мультиметру приводит к запорному клапану соленоидного провода.

Измерьте сопротивление.

Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

Если цепь **не** закрыта, отремонтируйте или замените электропроводку двигателя.

См. процедуру[[07-019-043 — Engine Wiring Harness|019-043]],[[99-019-199 — Connector, Butt Splice|019-199]]или[[99-019-204 — Deutsch DRC Connector Series|019-204]].

Если цепь закрыта, ее все равно нужно проверить на короткое расстояние до земли и короткое расстояние от пин-кодов до пин-кодов.

![[19901406.png]]

### Проверка на замыкание на массу

Вставьте электрический свинец в запорный клапан топливного отключения.

Прикоснитесь к другому многометровому щупу, чтобы заблокировать двигатель.

Кольцевой терминал в соленоиде **должен быть отключен и может **не касаться ничего, что заземлено.

Измерьте сопротивление.

Мультиметр **должен** показывать открытую схему (более 100k ом).

Если цепь **не** открыта, в проводе, подключенном к штифту запорного клапана, есть короткое заземление.

Ремонт или замена ремня электропроводки двигателя.

См. процедуру[[07-019-043 — Engine Wiring Harness|019-043]],[[99-019-199 — Connector, Butt Splice|019-199]]или[[99-019-204 — Deutsch DRC Connector Series|019-204]].

![[19901407.png]]

### Проверка на замыкание между контактами

Проверьте короткое замыкание от зажима клапана отключения топлива до всех других зажимов в разъеме ремня электропроводки двигателя.

Подключите аллигаторный клип второго испытательного щупа к другому многометровому щупу.

Вставьте штифт свинца во все другие штифты в приводе.

Кольцевой терминал в соленоиде **должен быть отключен и может **не касаться ничего, что заземлено.

Аккумуляторный блок должен быть отключен.

Измерьте сопротивление.

Мультиметр **должен** показывать открытую схему (более 100k ом).

Если цепь **не** открыта, между запорным клапаном отключения топлива и любым зажимом, измеряющим замкнутую цепь, имеется короткое расстояние.

Ремонт или замена ремня электропроводки двигателя. См. процедуру[[07-019-043 — Engine Wiring Harness|019-043]],[[99-019-199 — Connector, Butt Splice|019-199]]или[[99-019-204 — Deutsch DRC Connector Series|019-204]].

![[19901408.png]]


> [!quote]- Original (English) · английский оригинал
> ### Initial Check
>
> Inspect the fuel shutoff solenoid post for extra wires that may be connected to supply power to another device.
>
> Remove the extra wires that are found connected to the solenoid post.
>
> Check that the terminal post is **not** in contact with the fuel damper or any other metallic object other than the harness terminal.
>
> ### Resistance Check
>
> The fuel shutoff valve circuit is a signal wire of the fuel shutoff valve pin of the engine harness to the fuel shutoff valve solenoid.
>
> The solenoid is grounded through the engine.
>
> Disconnect the engine harness from the electronic control module (ECM).
>
> Check the ECM and engine harness connector pins for damage.
>
> Disconnect the fuel shutoff solenoid wire from the solenoid post.
>
> Check the solenoid wire ring terminal for damage. Refer to Procedure [[99-019-197 — Ring Terminal|019-197]].
>
> **CAUTION · Осторожно**
> Do not use probes or test leads other than Part Number 3822758 or the connector will be damaged. The leads must fit tightly in the connector without expanding the pins of the connector.
>
> Insert the pin of one lead into the fuel shutoff valve signal pin of the engine harness connector.
>
> Connect the alligator clip to the multimeter probe.
>
> Touch the other multimeter lead to the fuel shutoff valve solenoid wire.
>
> Measure the resistance.
>
> The multimeter **must** show a closed circuit (10 ohms or less).
>
> If the circuit is **not** closed, repair or replace the engine harness.
>
> Refer to Procedure [[07-019-043 — Engine Wiring Harness|019-043]], [[99-019-199 — Connector, Butt Splice|019-199]], or [[99-019-204 — Deutsch DRC Connector Series|019-204]].
>
> If the circuit is closed, it **must** still be checked for a short to ground and a short from pin to pin.
>
> ### Check for Short Circuit to Ground
>
> Insert the electrical lead into the fuel shutoff valve pin.
>
> Touch the other multimeter probe to engine block.
>
> The ring terminal at the solenoid **must** be disconnected and can **not** touch anything that is grounded.
>
> Measure the resistance.
>
> The multimeter **must** show an open circuit (more than 100k ohms).
>
> If the circuit is **not** open, there is a short to ground in the wire connected to the fuel shutoff valve pin.
>
> Repair or replace the engine harness.
>
> Refer to Procedure [[07-019-043 — Engine Wiring Harness|019-043]], [[99-019-199 — Connector, Butt Splice|019-199]], or [[99-019-204 — Deutsch DRC Connector Series|019-204]].
>
> ### Check for Short Circuit from Pin to Pin
>
> Check for a short circuit from the fuel shutoff valve pin to all other pins in the engine harness connector.
>
> Connect the alligator clip of a second test lead to the other multimeter probe.
>
> Insert the pin of the lead into all other pins in the actuator.
>
> The ring terminal at the solenoid **must** be disconnected and can **not** touch anything that is grounded.
>
> The battery supply **must** be disconnected.
>
> Measure the resistance.
>
> The multimeter **must** show an open circuit (more than 100k ohms).
>
> If the circuit is **not** open, there is a short between the fuel shutoff valve pin and any pin that measured a closed circuit.
>
> Repair or replace the engine harness. Refer to Procedure [[07-019-043 — Engine Wiring Harness|019-043]], [[99-019-199 — Connector, Butt Splice|019-199]], or [[99-019-204 — Deutsch DRC Connector Series|019-204]].
