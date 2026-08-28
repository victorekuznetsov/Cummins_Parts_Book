---
aliases:
  - "Цепь постоянного питания от АКБ"
type: "Процедура"
doc: "87-fc441"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc441.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc441.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Unswitched Battery Supply Circuit
**Цепь постоянного питания от АКБ**

> [!abstract] Процедура · `87-fc441`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc441.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc441.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 441

### Цепь постоянного питания от АКБ

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 441 PID(P): P168 SPN: 168 ФМИ: 1 лампа: Желтая СТО: | Напряжение батареи менее 9,0-VDC, обнаруженное в электронном модуле управления (ECM). | Подача напряжения ECM приближается к уровню, при котором произойдет непредсказуемая операция. |

![[19a00581.png]]

Цепь постоянного питания от АКБ

### Описание цепи

ECM получает напряжение от выключенной батареи через OEM-проводку и электропроводку двигателя. Существует встроенный 15-амперный предохранитель в непереключенных проводах аккумулятора ремня электропроводки двигателя для защиты ECM. Провода возврата батареи в ремне проводов двигателя подключены к заземлению блока двигателя.

### Расположение компонента

Расположение батареи будет варьироваться в зависимости от OEM. См. руководство OEM для определения местоположения батареи.

### Практические замечания

Эта неисправность обычно вызвана рыхлыми или разъединенными соединениями батареи.

Устранение неполадок код t05-441


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 441
>
> ### Unswitched Battery Supply Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 441 PID(P): P168 SPN: 168 FMI: 1 Lamp: Yellow SRT: | Less than 9.0-VDC battery voltage detected at the electronic control module (ECM). | ECM voltage supply approaching a level at which unpredictable operation will occur. |
>
> Unswitched Battery Supply Circuit
>
> ### Circuit Description
>
> The ECM receives unswitched battery voltage through the OEM harness and the engine harness. There is an in-line 15-amp fuse in the unswitched battery wires of the engine harness to protect the ECM. The battery return wires in the engine harness are connected to the engine block ground.
>
> ### Component Location
>
> The location of the battery will vary with the OEM. Refer to the OEM manual for the battery location.
>
> ### Shoptalk
>
> This fault is usually caused by loose or corroded battery connections.
>
> Refer to Troubleshooting Fault Code t05-441
