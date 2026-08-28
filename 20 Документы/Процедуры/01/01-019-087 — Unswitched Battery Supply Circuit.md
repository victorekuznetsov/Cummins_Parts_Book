---
aliases:
  - "Цепь постоянного питания от АКБ"
type: "Процедура"
doc: "01-019-087"
title_en: "Unswitched Battery Supply Circuit"
title_ru: "Цепь постоянного питания от АКБ"
modified: "2003-12-04"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 8
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-087.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-087.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Unswitched Battery Supply Circuit
**Цепь постоянного питания от АКБ**

> [!abstract] Процедура · `01-019-087`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-12-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-087.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-087.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

ECM получает постоянное напряжение от батарей через непереключенные провода батареи, которые подключены непосредственно к положительному (+) посту батареи. Существует один встроенный 20 AMP предохранитель в непереключенном проводе батареи для защиты ECM.

![[19802554.png]]

### Первичная проверка

Проверьте соединения кабеля батареи на наличие свободных или разъединенных соединений. Ремонт или замена аккумуляторных батарей. См. руководство по OEM.

![[19400082.png]]

Осмотрите проводные соединения предохранителей для рыхлых или корродированных предохранителей. Замените предохранители. См. процедуру[[99-019-198 — Fuse, Harness In-Line|019-198]].

![[19400084.png]]

Проверьте напряжение батареи. Поместите многометровый положительный щуп на положительный (+) вывод батареи. Поместите многометровый отрицательный щуп на отрицательный (-) вывод батареи. Измерьте напряжение батареи. Напряжение должно составлять от 17,3 до 34,7 ВДК для системы 24 ВДК. Если напряжение батареи ниже 17,3 ВДК, замените батарею. См. руководство OEM для замены батареи.

![[19400083.png]]

### Проверка сопротивления

Отсоедините разъемы удлинительной проводов от ECM. Проверьте наличие поврежденных контактов в ECM и проводах.

![[19802555.png]]

> [!warning] ОСТОРОЖНО
> Не используйте щупы или провода, кроме Части № 3822917. Разъём будет повреждён. Лиды должны плотно помещаться в разъеме без расширения штифтов в разъеме.

Вставьте свинец в один из штифтов B+ жгута проводов двигателя. Подключите аллигатор к многометровому щупу. Прикоснитесь к другому многометровому щупу к разъему батареи на проводной упряжке. Измерьте сопротивление. Сопротивление должно быть 10 Ом или меньше.

![[19802550.png]]

Повторите этот тест для всех контактов B + в проводах. Измерьте сопротивление. Сопротивление должно быть 10 Ом или меньше.

Если в любой проверке измеряется более 10 Ом, то имеется открытая схема. Ремонт или замена ремня электропроводки двигателя. См. процедуру[[01-019-043 — Engine Wiring Harness|019-043]]или в руководстве по OEM.

![[19802550.png]]

Повторите этот тест для всех B-контактов в проводной упряжке. Измерьте сопротивление. Сопротивление должно быть 10 Ом или меньше.

Если в любой проверке измеряется более 10 Ом, то имеется открытая схема. Ремонт или замена ремня электропроводки двигателя. См. процедуру[[01-019-043 — Engine Wiring Harness|019-043]]или в руководстве по OEM.

![[19802550.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The ECM receives constant voltage from the batteries through the unswitched battery wires that are connected directly to the positive (+) battery post. There is one inline 20 AMP fuse in the unswitched battery wire to protect the ECM.
>
> ### Initial Check
>
> Inspect the battery cable connections for loose or corroded connections. Repair or replace the battery connections. Refer to the OEM manual.
>
> Inspect the harness fuse connections for loose or corroded fuses. Replace the fuses. Refer to Procedure [[99-019-198 — Fuse, Harness In-Line|019-198]].
>
> Check the battery voltage. Place the multimeter positive probe on the positive (+) terminal of the battery. Place the multimeter negative probe on the negative (-) terminal of the battery. Measure the battery voltage. The voltage should be 17.3 to 34.7 VDC for a 24 VDC system. If the battery voltage is below 17.3 VDC, replace the battery. Refer to the OEM manual for battery replacement.
>
> ### Resistance Check
>
> Disconnect the extension harness connectors from the ECM. Check for damaged pins in the ECM and the harness.
>
> **CAUTION · Осторожно**
> Do not use probes or leads other than Part Number 3822917. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins in the connector.
>
> Insert the lead into one of the B+ pins of the engine harness. Connect the alligator clip to the multimeter probe. Touch the other multimeter probe to the battery connector on the harness. Measure the resistance. The resistance **must** be 10 ohms or less.
>
> Repeat this test for all the B+ pins in the harness. Measure the resistance. The resistance **must** be 10 ohms or less.
>
> If more than 10 ohms are measured in any check, there is an open circuit. Repair or replace the engine harness. Refer to Procedure [[01-019-043 — Engine Wiring Harness|019-043]] or the OEM manual.
>
> Repeat this test for all the B - pins in the harness. Measure the resistance. The resistance **must** be 10 ohms or less.
>
> If more than 10 ohms are measured in any check, there is an open circuit. Repair or replace the engine harness. Refer to Procedure [[01-019-043 — Engine Wiring Harness|019-043]] or the OEM manual.
