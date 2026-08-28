---
aliases:
  - "Цепь переключателя «Выкл/Ручной/Авто» — напряжение выше нормы"
type: "Процедура"
doc: "01-fc1333"
title_en: "Off/Manual/Auto Switch Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Цепь переключателя «Выкл/Ручной/Авто» — напряжение выше нормы"
modified: "2012-05-08"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1333.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1333.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Off/Manual/Auto Switch Circuit - Voltage Above Normal or Shorted to High Source
**Цепь переключателя «Выкл/Ручной/Авто» — напряжение выше нормы**

> [!abstract] Процедура · `01-fc1333`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1333.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1333.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1333

### Цепь переключателя «Выкл/Ручной/Авто» — напряжение выше нормы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1333 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Сигнал выключателя Off/Manual/Auto высоко закорочен. | ECM будет по умолчанию выключать значение, когда переключатель находится в Ручном. Авто и выключенные позиции будут работать нормально. |

![[19802777.png]]

Выключено/ручно/авто-коммутатор

### Описание цепи

Выключатель Off/Manual/Auto контролируется модулем управления двигателем (ECM) для определения режима работы генераторной установки.

ECM контролирует напряжение в режиме работы переключателя ручного контакта сигнала и ожидает увидеть, что напряжение изменяется между 0,5 и 4,5-VDC во время нормальной работы. ECM контролирует напряжение в режиме работы автоматического контакта с сигналом переключателя и ожидает увидеть напряжение 0 или 5-VDC во время нормальной работы. Высокое напряжение будет сбивать Код 1333 по умолчанию и может быть вызвано шортами в сигнале или обратными проводами, открытым в обратном проводе или неисправным переключателем.

### Расположение компонента

Справочный раздел E для расположения панели интерфейса оператора и выключателя Off/Manual/Auto.

### Практические замечания

Возможные режимы отказа - это открытая схема, короткая до положительной батареи (+), неисправный переключатель и потеря напряжения питания внутри ECM.

См. Код устранения неполадок t05-1333.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1333
>
> ### Off/Manual/Auto Switch Circuit - Voltage Above Normal or Shorted to High Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1333 PID(P): SPN: FMI: Lamp: Warning SRT: | The Off/Manual/Auto switch signal is shorted high. | The ECM will default to an Off value when switch is in Manual. Auto and Off positions will function normally. |
>
> Off/Manual/Auto Switch Circuit
>
> ### Circuit Description
>
> The Off/Manual/Auto switch is monitored by the engine control module (ECM) to determine the operation mode of the generator set.
>
> The ECM monitors the voltage on the operation mode switch manual SIGNAL pin and expects to see a voltage vary between 0.5 and 4.5-VDC during normal operation. The ECM monitors the voltage on the operation mode switch auto SIGNAL pin and expects to see a voltage of either 0 or 5-VDC during normal operation. High voltage will trip Fault Code 1333 and can be caused by shorts in the signal, or return wires, an open in the return wire, or a failed switch.
>
> ### Component Location
>
> Reference Section E for location of the operator interface panel and the Off/Manual/Auto switch.
>
> ### Shoptalk
>
> The possible failure modes are open circuit, short to battery positive (+), failed switch, and loss of supply voltage inside the ECM.
>
> Refer to Troubleshooting Fault Code t05-1333.
