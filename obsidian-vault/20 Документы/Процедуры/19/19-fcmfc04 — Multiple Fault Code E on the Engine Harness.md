---
type: "Процедура"
doc: "19-fcmfc04"
title_en: "Multiple Fault Code E on the Engine Harness"
modified: "2010-08-19"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fcmfc04.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fcmfc04.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Multiple Fault Code E on the Engine Harness

> [!abstract] Процедура · `19-fcmfc04`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-08-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fcmfc04.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fcmfc04.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: Многократный E

### Многократный код ошибки E на ремне жгута проводов двигателя

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: Многократный E PID(P): СПН: ФМИ: Лампа: СТО: 00-381 | Напряжение питания от контакта 16 проводов интерфейса OEM имеет: Неудачи внутри ECM были сокращены до основания открытой цепи, внешней в ECM. | Несколько кодов ошибок. |

![[nobox.png]]

### Описание цепи

ECM поставляет датчик уровня охлаждающей жидкости и датчик положения удаленного ускорителя с +5 VDC от контакта 16. ECM имеет общую отдачу для всех датчиков давления двигателя и всех датчиков температуры при контакте 21. Неисправность на любом из этих проводов вызовет несколько кодов неисправностей.

### Расположение компонента

См. схемы двигателя.

### Практические замечания

Ищите открытые цепи в общих проводах питания и возврата и шортах от батареи или земли до проводов питания и возврата или дефектного источника питания ECM. Неисправный датчик давления может вызвать несколько кодов неисправностей.

См. Код устранения неисправностей t05-mfc04


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: Multiple E
>
> ### Multiple Fault Code E on the Engine Harness
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: Multiple E PID(P): SPN: FMI: Lamp: SRT: 00-381 | The supply voltage from pin 16 of the OEM interface harness has: Failed internally in the ECM Been shorted to ground An open circuit external in the ECM. | Multiple fault codes. |
>
> ### Circuit Description
>
> The ECM supplies the coolant level sensor and the remote accelerator position sensor with +5 VDC from pin 16. The ECM has common returns for all of the engine pressure sensors and all of the temperature sensors on pin 21. A failure on either of these wires will cause multiple fault codes.
>
> ### Component Location
>
> Refer to the engine diagrams.
>
> ### Shoptalk
>
> Look for open circuits in the common supply and return wires and shorts from battery or ground to the supply and return wires or defective ECM power supply. A failed pressure sensor can cause multiple fault codes.
>
> Refer to Troubleshooting Fault Code t05-mfc04
