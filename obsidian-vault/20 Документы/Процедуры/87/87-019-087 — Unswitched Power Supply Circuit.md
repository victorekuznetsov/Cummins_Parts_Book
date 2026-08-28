---
aliases:
  - "Цепь постоянного питания"
type: "Процедура"
doc: "87-019-087"
title_en: "Unswitched Power Supply Circuit"
title_ru: "Цепь постоянного питания"
modified: "2018-08-09"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 8
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-087.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-087.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Unswitched Power Supply Circuit
**Цепь постоянного питания**

> [!abstract] Процедура · `87-019-087`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2018-08-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-087.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-087.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

ECM получает постоянное напряжение от батарей через непереключенные провода батареи, которые подключены непосредственно к (+) положительному заряду батареи. В непереключенных проводах батареи есть два встроенных 15-амперных предохранителя для защиты ECM.

![[19a00746.png]]

### Первичная проверка

Проверьте соединения кабеля батареи на наличие свободных или разъединенных соединений. Ремонт или замена аккумуляторных батарей. См. руководство по OEM.

![[19400082.png]]

Осмотрите OEM-интерфейс проводов жгутов предохранителей для рыхлых или корродированных предохранителей. Замените предохранители.

[[99-019-198 — Fuse, Harness In-Line|См. процедуру 019-198]].

Проверьте предохранители на сопротивление. Прикосновение к одному мультиметру приводит к каждому предохранителю и измеряет сопротивление. Запал должен измерять замкнутую цепь (10 Ом или меньше).

![[19400084.png]]

Проверьте напряжение батареи. Поместите многометровый положительный щуп на положительный (+) вывод батареи. Поместите многометровый отрицательный щуп на отрицательный (-) вывод батареи. Измерьте напряжение батареи. Напряжение должно быть 17,3-34,7 ВДК для системы 24-ВДК. Если напряжение батареи ниже 17,3 ВДК, замените батарею.

См. руководство OEM для замены батареи.

![[19400083.png]]

### Проверка сопротивления

Отсоедините разъем жгута проводов двигателя от ECM. Проверьте наличие поврежденных контактов в ECM и проводах.

![[19900781.png]]

> [!warning] ОСТОРОЖНО
> Не используйте щупы или испытательные щупы, кроме Части № 3822758. Разъём будет повреждён. Лиды должны плотно помещаться в разъеме без расширения штифтов в разъеме.

Вставьте свинец в контакт 38 разъёма проводов двигателя. Подключите аллигатор к многометровому щупу. Прикоснитесь к другому многометровому щупу к соединению батареи на ремне электропроводки двигателя. Измерьте сопротивление. Сопротивление должно быть 10 Ом или меньше.

![[19a00174.png]]

Удалите свинец из контакта 38 и вставьте его в контакт 39 разъёма ремня электропроводки двигателя. Прикоснитесь к другому многометровому щупу к соединению батареи на ремне электропроводки двигателя.

Измерьте сопротивление. Сопротивление должно быть 10 Ом или меньше.

Повторите проверку от контактов 40 и 50 разъёма ремня электропроводки двигателя к соединению батареи на ремне электропроводки двигателя.

Измерьте сопротивление. Сопротивление должно быть 10 Ом или меньше.

![[19a00175.png]]

Если в любой проверке измеряется более 10 Ом, то имеется открытая схема. Ремонт или замена ремня электропроводки двигателя.

[[99-019-197 — Ring Terminal|См. процедуру 019-197]],[[99-019-199 — Connector, Butt Splice|Процедура 019-199]],[[87-019-250 — Connector, 50-Pin|См. процедуру 019-250]]и[[87-019-043 — Engine Wiring Harness|См. процедуру 019-043]].

![[19a00176.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The ECM receives constant voltage from the batteries through the unswitched battery wires that are connected directly to the (+) positive battery post. There are two in-line 15-amp fuses in the unswitched battery wires to protect the ECM.
>
> ### Initial Check
>
> Inspect the battery cable connections for loose or corroded connections. Repair or replace the battery connections. Refer to the OEM manual.
>
> Inspect the OEM interface harness fuse connections for loose or corroded fuses. Replace the fuses.
>
> [[99-019-198 — Fuse, Harness In-Line|Refer to Procedure 019-198]].
>
> Check the fuses for resistance. Touch one multimeter lead to each fuse terminal and measure the resistance. The fuse should measure a closed circuit (10 ohms or less).
>
> Check the battery voltage. Place the multimeter positive probe on the positive (+) terminal of the battery. Place the multimeter negative probe on the negative (-) terminal of the battery. Measure the battery voltage. The voltage should be 17.3 to 34.7 VDC for a 24-VDC system. If the battery voltage is below 17.3 VDC, replace the battery.
>
> Refer to the OEM manual for battery replacement.
>
> ### Resistance Check
>
> Disconnect the engine harness connector from the ECM. Check for damaged pins in the ECM and the harness.
>
> **CAUTION · Осторожно**
> Do not use probes or test leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins in the connector.
>
> Insert the lead into pin 38 of the engine harness connector. Connect the alligator clip to the multimeter probe. Touch the other multimeter probe to the battery connection on the engine harness. Measure the resistance. The resistance **must** be 10 ohms or less.
>
> Remove the lead from pin 38 and insert it into pin 39 of the engine harness connector. Touch the other multimeter probe to the battery connection on the engine harness.
>
> Measure the resistance. The resistance **must** be 10 ohms or less.
>
> Repeat the check from pins 40 and 50 of the engine harness connector to the battery connection on the engine harness.
>
> Measure the resistance. The resistance **must** be 10 ohms or less.
>
> If more than 10 ohms are measured in any check, there is an open circuit. Repair or replace the engine harness.
>
> [[99-019-197 — Ring Terminal|Refer to Procedure 019-197]], [[99-019-199 — Connector, Butt Splice|Refer to Procedure 019-199]], [[87-019-250 — Connector, 50-Pin|Refer to Procedure 019-250]], and [[87-019-043 — Engine Wiring Harness|Refer to Procedure 019-043]].
