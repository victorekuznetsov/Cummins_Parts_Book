---
aliases:
  - "Цепь датчика давления во впускном коллекторе"
type: "Процедура"
doc: "19-fc123"
title_en: "Intake Manifold Pressure Sensor Circuit"
title_ru: "Цепь датчика давления во впускном коллекторе"
modified: "2026-05-28"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc123.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc123.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Intake Manifold Pressure Sensor Circuit
**Цепь датчика давления во впускном коллекторе**

> [!abstract] Процедура · `19-fc123`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2026-05-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc123.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc123.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 123

### Цепь датчика давления во впускном коллекторе

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 123 P(P): P102 SPN: 102 FMI: 4 лампы: Нет, не srt: 00-349 | Менее 0,33-VDC обнаруживается при входном коллекторе датчика давления воздуха, контактирующего с 35 проводкой двигателя ремня. | Мощность двигателя снижается до уровня без воздуха. |

![[19400118.png]]

Цепь датчика давления во впускном коллекторе

### Описание цепи

Датчик давления впускного коллектора контролирует давление повышения и передает информацию в ECM через контакт 35 с ремнем электропроводки двигателя. ECM контролирует напряжение на контакте 35 и ожидает, что напряжение будет варьироваться от 0,5 до 4,5-VDC во время нормальной работы двигателя. Напряжение ниже 0,33-VDC на контакте 35 может быть вызвано шортами в подаче, сигнале или обратном проводе, открытой цепью в подаче или сигнальных проводах, низким напряжением питания от ECM или неисправным датчиком.

### Расположение компонента

Датчик давления впускного коллектора расположен на среднем нижнем краю коллектора впускного воздуха.

### Практические замечания

Возможные причины этого кода неисправности:

- Неисправность или повреждение датчика давления впускного коллектора

- Неисправная или поврежденная электропроводка двигателя

См. Устранение неполадок код t05-123


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 123
>
> ### Intake Manifold Pressure Sensor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 123 PID(P): P102 SPN: 102 FMI: 4 Lamp: None SRT: 00-349 | Less than 0.33-VDC detected at the intake manifold air pressure sensor signal pin 35 of the engine harness. | Engine power derate to no-air setting. |
>
> Intake Manifold Pressure Sensor Circuit
>
> ### Circuit Description
>
> The intake manifold pressure sensor monitors boost pressure and passes information to the ECM through pin 35 of the engine harness. The ECM monitors the voltage on pin 35 and expects to see the voltage vary between 0.5 and 4.5-VDC during normal engine operation. Voltage below 0.33-VDC on pin 35 can be caused by shorts in the supply, signal, or return wires, an open circuit in the supply or signal wires, low supply voltage from the ECM, or a failed sensor.
>
> ### Component Location
>
> The intake manifold pressure sensor is located on the middle lower edge of the air intake manifold.
>
> ### Shoptalk
>
> Possible causes of this fault code include:
>
> - Malfunctioning or damaged intake manifold pressure sensor
>
> - Malfunctioning or damaged engine wiring harness
>
> Refer to Troubleshooting Fault Code t05-123
