---
aliases:
  - "Выключатель моторного тормоза"
type: "Процедура"
doc: "99-019-034"
title_en: "Engine Brake ON/OFF Switch"
title_ru: "Выключатель моторного тормоза"
modified: "2015-06-29"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 6
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-034.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-034.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/99"
  - "перевод/машинный"
---

# Engine Brake ON/OFF Switch
**Выключатель моторного тормоза**

> [!abstract] Процедура · `99-019-034`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2015-06-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-034.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-034.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Тормоз двигателя ON/OFF сигнализирует системе, что оператор просит активировать тормозную систему двигателя. Переключатель уровня тормозов двигателя определяет, какой процент мощности торможения двигателя будет использоваться для торможения двигателя. Для передачи установки на ECM используются три входа в электронный модуль управления (ECM) от переключателя уровня тормоза двигателя. Используются селектор тормозов двигателя № 1 сигнал, селектор тормозов двигателя № 2 сигнал, и селектор тормозов двигателя № 3 сигнал в разъеме оригинального производителя оборудования (OEM). Различные комбинации трех проводов используются для представления шести позиций переключателя.

После того, как ECM получит сигнал от переключателя ON/OFF тормоза двигателя и все другие предварительные условия торможения двигателя (РРМ двигателя и ограничения скорости на дороге), ECM поставит 12 VDC на соответствующие соленоиды тормоза двигателя в зависимости от того, как установлен переключатель уровня тормоза двигателя 3 или 6.

![[17c00022.png]]

### Проверка сопротивления

Если имеется электронный инструмент обслуживания, следите за переключателями ON/OFF тормоза двигателя для правильной работы. Если **не**, следуйте процедурам устранения неполадок в этом разделе.

![[19803969.png]]

Найдите выключатель ON/OFF тормоза двигателя. Удалите электрические разъемы из переключателя.

Пометьте провода с местоположением на выключателе или номером провода. Удалите электрические разъемы из переключателя.

Настройте мультиметр для измерения сопротивления.

Прикоснитесь одним многометровым щупом к одному из терминалов переключателя. Прикоснитесь к другому многометровому щупу к другому терминалу переключателя.

![[19900590.png]]

Переместите переключатель в положение выключения. Мультиметр **должен** показать обрыв цепи (100 кОм и более). Если схема не открыта, выключатель не работает.

См. руководство по устранению неполадок и ремонту OEM для процедур замены.

![[19900591.png]]

Поместите переключатель в положение ON. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее). Если цепь **не **закрыта, выключатель не работает.

См. руководство по устранению неполадок и ремонту OEM для процедур замены.

![[wr8swkd.png]]

### Проверка на замыкание на массу

Прикоснитесь к одному из многометровых щупов к одному из переключателей. Прикоснитесь к другому щупу на земле шасси. Переместите переключатель в положение Включения и измерьте сопротивление. Мультиметр **должен** показать обрыв цепи (100 кОм и более). Если схема **не открыта, выключатель не работает. См. руководство по устранению неполадок и ремонту OEM для процедур замены. Если переключатель проходит все предыдущие проверки, схема **должна быть проверена на открытую схему, короткое замыкание на землю, короткое замыкание от контакта к контакту и короткое замыкание к внешнему источнику напряжения.

![[19c01165.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The engine brake ON/OFF switch circuit signals the system that the operator is requesting the engine brake system to be activated. The engine brake level switch determines what percentage of engine braking power will be used for engine braking. Three inputs to the electronic control module (ECM) from the engine brake level switch are used to communicate the setting to the ECM. Engine brake selector number 1 signal, engine brake selector number 2 signal, and engine brake selector number 3 signal in the original equipment manufacturer (OEM) connector are used. Various combinations of the three wires are used to represent the six switch positions.
>
> After the ECM receives the signal from the engine brake ON/OFF switch and all other engine braking preconditions are met (engine RPM and road speed limits), the ECM will supply 12 VDC to the appropriate engine brake solenoids depending on how the 3 or 6 position engine brake level switch is set.
>
> ### Resistance Check
>
> If an electronic service tool is available, monitor the engine brake ON/OFF switches for proper operation. If **not**, follow the troubleshooting procedures in this section.
>
> Locate the engine brake ON/OFF switch. Remove the electrical connectors from the switch.
>
> Label the wires with the location on the switch or the wire number. Remove the electrical connectors from the switch.
>
> Adjust the multimeter to measure resistance.
>
> Touch one multimeter probe to one of the terminals of the switch. Touch the other multimeter probe to the other terminal of the switch.
>
> Move the switch to the OFF position. The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, the switch has failed.
>
> Refer to the OEM troubleshooting and repair manual for replacement procedures.
>
> Place the switch in the ON position. The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, the switch has failed.
>
> Refer to the OEM troubleshooting and repair manual for replacement procedures.
>
> ### Check for Short Circuit to Ground
>
> Touch one of the multimeter probes to one of the switch terminals. Touch the other probe to chassis ground. Move the switch to the ON position and measure the resistance. The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, the switch has failed. Refer to the OEM troubleshooting and repair manual for replacement procedures. If the switch passes all of the previous checks, the circuit **must** be checked for an open circuit, a short circuit to ground, a short circuit from pin-to-pin, and a short circuit to an external voltage source.
