---
aliases:
  - "Цепь постоянного питания от АКБ"
type: "Процедура"
doc: "87-fc442"
title_en: "Unswitched Battery Supply Circuit"
title_ru: "Цепь постоянного питания от АКБ"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc442.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc442.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Unswitched Battery Supply Circuit
**Цепь постоянного питания от АКБ**

> [!abstract] Процедура · `87-fc442`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc442.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc442.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 442

### Цепь постоянного питания от АКБ

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 442 P(P): P168 SPN: 168 ФМИ: 0 лампочка: Желтая СТО: | Более 35,0-ВДК напряжения батареи обнаружено в электронном модуле управления (ЭУМ). | Повреждение ECM произойдет. |

![[19a00581.png]]

Цепь постоянного питания от АКБ

### Описание цепи

ECM получает напряжение от выключенной батареи через OEM-проводку и электропроводку двигателя. Существует встроенный 15-амперный предохранитель в непереключенном проводе батареи провода OEM-интерфейса для защиты ECM. Провода возврата батареи в ремне проводов двигателя подключены к заземлению блока двигателя.

### Расположение компонента

Расположение батареи будет варьироваться в зависимости от OEM. См. руководство OEM для определения местоположения батареи.

### Практические замечания

Эта неисправность обычно вызвана неправильной проводкой цепи батареи.

Устранение неполадок код t05-442


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 442
>
> ### Unswitched Battery Supply Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 442 PID(P): P168 SPN: 168 FMI: 0 Lamp: Yellow SRT: | More than 35.0-VDC battery voltage detected at the electronic control module (ECM). | ECM damage will occur. |
>
> Unswitched Battery Supply Circuit
>
> ### Circuit Description
>
> The ECM receives unswitched battery voltage through the OEM harness and engine harness. There is an in-line 15-amp fuse in the unswitched battery wire of the OEM interface harness to protect the ECM. The battery return wires in the engine harness are connected to the engine block ground.
>
> ### Component Location
>
> The location of the battery will vary with the OEM. Refer to the OEM manual for the battery location.
>
> ### Shoptalk
>
> This fault is usually caused by improper wiring of the battery circuit.
>
> Refer to Troubleshooting Fault Code t05-442
