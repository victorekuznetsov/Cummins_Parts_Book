---
aliases:
  - "Цепь клапана отсечки топлива"
type: "Процедура"
doc: "98-019-049"
title_en: "Fuel Shutoff Valve Circuit"
title_ru: "Цепь клапана отсечки топлива"
modified: "2012-11-14"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 9
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-049.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-049.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Fuel Shutoff Valve Circuit
**Цепь клапана отсечки топлива**

> [!abstract] Процедура · `98-019-049`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2012-11-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-049.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-049.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Схема клапана отключения топлива представляет собой провод SIGNAL, подключенный к проводу аккумулятора переключателя SUPPLY. Клапан заземляется через двигатель.

> [!note] Примечание
> Если клапан отключения топлива подключен к вспомогательному отключающему проводу, проверьте цепь отключения провода.[[98-019-179 — Auxiliary Shutdown Circuit|См. процедуру 019-179 в разделе 19.]]

![[nobox.png]]

### Проверка сопротивления

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения соленоида, удерживайте терминальный гайка, ближайший к соленоиду, с надлежащим гаечным ключом при отключении соленоидного проволочного гайки.

Отсоедините основную проводку двигателя от модуля управления двигателем (ECM).

Смой и очисти контакты разъема. Используйте контактный очиститель, номер детали 3824510. Осмотрите разъемы ECM и основной проводов двигателя для поврежденных контактов.

Отсоедините соленоидный провод от соленоидного терминала.

Отключите разъемы C5 и C6.

![[19801708.png]]

Прикосновение к одному из мультиметров приводит к контакту 22 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к кольцевому терминалу на конце отключения топлива соленоидным проводом.

Убедитесь, что кольцевой терминал на конце соленоидного провода не касается ничего, что заземлено.

![[19801717.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать менее 10 Ом, что является замкнутой схемой. Если цепь **не **закрыта, то в отключающем соленоидном проводе SUPPLY есть открытая цепь.

Ремонт или замена основного двигателя проводов жгута.

- См. процедуру 019-228 в разделе 19.
- [[98-019-043 — Engine Wiring Harness|См. процедуру 019-043 в разделе 19.]]

![[19801619.png]]

### Проверка на замыкание на массу

Прикосновение к одному из мультиметров приводит к контакту 22 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к заземлению блока двигателя. Убедитесь, что терминал колец соленоидной проволоки не касается ничего, что заземлено.

Измерьте сопротивление. Мультиметр **должен **показывать более 100k ом, что является открытой схемой. Если цепь не открыта, в проводе, подключенном к контакту 22, есть короткое заземление.

Ремонт или замена основного двигателя проводов жгута.

- См. процедуру 019-228 в разделе 19.
- [[98-019-043 — Engine Wiring Harness|См. процедуру 019-043 в разделе 19.]]

![[19801714.png]]

### Проверка на замыкание между контактами

Проверьте короткое замыкание между контактом 22 основного разъёма проводов двигателя и всеми другими штифтами в разъеме, кроме контакта 23.

Прикосновение к одному из мультиметров приводит к контакту 22 разъема. Прикосновение к другому мультиметру приводит ко всем другим штифтам в разъеме, кроме контакта 23. Убедитесь, что соленоидный кольцевой концевой провод не касается ничего, что заземлено.

![[19801715.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом, что является открытой схемой. Если схема **не** открыта, между проводами, подключенными к контакту 22 главного разъёма проводов двигателя, и **любым** другим штифтом, который измеряется менее 100k Ом.

Ремонт или замена основного двигателя проводов жгута.

- См. процедуру 019-228 в разделе 19.
- [[98-019-043 — Engine Wiring Harness|См. процедуру 019-043 в разделе 19.]]

![[19801621.png]]

### Проверка напряжения

Проверьте напряжение в клапане отключения топлива.

Убедитесь, что провод питания отключен.

Включите зажигание.

Выберите функцию постоянного напряжения на мультиметре. Прикосновение к одному из мультиметров приводит к терминалу соленоидного кольца. Прикосновение к другому мультиметру приводит к хорошей, чистой поверхности на блоке двигателя.

![[19801710.png]]

Измерьте напряжение.

Напряжение **должно быть таким же, как напряжение батареи. Если напряжение **не правильно, то проверьте терминал на предмет коррозии.

Если терминал чистый, то проверьте основную проводку двигателя и переключатель зажигания.

Проверьте провод SIGNAL на короткий от земли до земли или короткий от контакта к контакту.

![[19801711.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The fuel shutoff valve circuit is a SIGNAL wire connected to the switch battery SUPPLY wire. The valve is grounded through the engine.
>
> **Note · Примечание**
> If the fuel shutoff valve is connected to the auxiliary shutdown wire, check the shutdown wire circuit. [[98-019-179 — Auxiliary Shutdown Circuit|Refer to Procedure 019-179 in Section 19.]]
>
> ### Resistance Check
>
> **CAUTION · Осторожно**
> To avoid damage to the solenoid, hold the terminal nut closest to the solenoid with the proper wrench when disconnecting the solenoid wire nut.
>
> Disconnect the main engine harness from the engine control module (ECM).
>
> Flush and clean the connector pins. Use contact cleaner, Part Number 3824510. Inspect the ECM and main engine harness connectors for damaged pins.
>
> Disconnect the solenoid wire from the solenoid terminal.
>
> Disconnect the C5 and C6 connectors.
>
> Touch one of the multimeter leads to pin 22 of the main engine harness connector. Touch the other multimeter lead to the ring terminal on the end of the fuel shutoff solenoid wire.
>
> Make sure the ring terminal on the end of the solenoid wire is **not** touching anything that is grounded.
>
> Measure the resistance.
>
> The multimeter **must** show less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, then there is an open circuit in the fuel shutoff solenoid SUPPLY wire.
>
> Repair or replace the main engine harness.
>
> - Refer to Procedure 019-228 in Section 19.
> - [[98-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 in Section 19.]]
>
> ### Check for Short Circuit to Ground
>
> Touch one of the multimeter leads to pin 22 of the main engine harness connector. Touch the other multimeter lead to the engine block ground. Make sure the solenoid wire ring terminal is **not** touching anything that is grounded.
>
> Measure the resistance. The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short to ground in the wire connected to pin 22.
>
> Repair or replace the main engine harness.
>
> - Refer to Procedure 019-228 in Section 19.
> - [[98-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 in Section 19.]]
>
> ### Check for Short Circuit from Pin to Pin
>
> Check for a short circuit between pin 22 of the main engine harness connector and all other pins in the connector except pin 23.
>
> Touch one of the multimeter leads to pin 22 of the connector. Touch the other multimeter lead to all other pins in the connector except pin 23. Make sure the solenoid ring terminal wire is **not** touching anything that is grounded.
>
> Measure the resistance.
>
> The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short between the wires connected to pin 22 of the main engine harness connector and **any** other pin that measured less than 100k ohms.
>
> Repair or replace the main engine harness.
>
> - Refer to Procedure 019-228 in Section 19.
> - [[98-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 in Section 19.]]
>
> ### Voltage Check
>
> Check the voltage at the fuel shutoff valve.
>
> Make sure the voltage SUPPLY wire is disconnected.
>
> Turn keyswitch ON.
>
> Select the DC voltage function on the multimeter. Touch one of the multimeter leads to the solenoid wire ring terminal. Touch the other multimeter lead to a good, clean surface on the engine block.
>
> Measure the voltage.
>
> The voltage **must** be the same as the battery voltage. If the voltage is **not** correct, then inspect the terminal for corrosion.
>
> If the terminal is clean, then inspect the main engine harness and keyswitch.
>
> Check the SIGNAL wire for short to ground or short from pin-to-pin.
