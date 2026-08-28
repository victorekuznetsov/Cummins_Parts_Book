---
aliases:
  - "Цепь постоянного питания от АКБ"
type: "Процедура"
doc: "19-fc441"
title_en: "Unswitched Battery Supply Circuit"
title_ru: "Цепь постоянного питания от АКБ"
modified: "2011-03-01"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc441.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc441.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Unswitched Battery Supply Circuit
**Цепь постоянного питания от АКБ**

> [!abstract] Процедура · `19-fc441`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc441.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc441.pdf)

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
| Код неисправности: 441 PID(P): P168 SPN: 168 ФМИ: 1 лампа: Нет, не srt: 00-372 | Напряжение батареи менее 12,0-VDC, обнаруженное в ECM. | Подача напряжения ECM приближается к уровню, при котором произойдет непредсказуемая операция. |

![[19400081.png]]

Цепь постоянного питания от АКБ

### Описание цепи

ECM получает напряжение от выключенной батареи через OEM-проводку и электропроводку двигателя. В непереключенных проводах аккумуляторов OEM-интерфейса для защиты ECM есть два встроенных 10-амперных предохранителя. Провода возврата батареи в ремне проводов двигателя подключены к заземлению блока двигателя.

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
> | Fault Code: 441 PID(P): P168 SPN: 168 FMI: 1 Lamp: None SRT: 00-372 | Less than 12.0-VDC battery voltage detected at the ECM. | ECM voltage supply approaching a level at which unpredictable operation will occur. |
>
> Unswitched Battery Supply Circuit
>
> ### Circuit Description
>
> The ECM receives unswitched battery voltage through the OEM harness and the engine harness. There are two in-line 10-amp fuses in the unswitched battery wires of the OEM interface harness to protect the ECM. The battery return wires in the engine harness are connected to the engine block ground.
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
