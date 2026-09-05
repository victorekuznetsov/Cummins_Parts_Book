---
aliases:
  - "Цепь переключателя «Выкл/Ручной/Авто» — напряжение ниже нормы"
type: "Процедура"
doc: "01-fc1332"
title_en: "Off/Manual/Auto Switch Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Цепь переключателя «Выкл/Ручной/Авто» — напряжение ниже нормы"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1332.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1332.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Off/Manual/Auto Switch Circuit - Voltage Below Normal or Shorted to Low Source
**Цепь переключателя «Выкл/Ручной/Авто» — напряжение ниже нормы**

> [!abstract] Процедура · `01-fc1332`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1332.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1332.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1332

### Цепь переключателя «Выкл/Ручной/Авто» — напряжение ниже нормы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1332 P(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Сигнал выключателя Off/Manual/Auto является низким. | ECM позволит генераторной установке работать в Auto. |

![[19802777.png]]

Выключено/ручно/авто-коммутатор

### Описание цепи

Выключатель Off/Manual/Auto контролируется модулем управления двигателем (ECM) для определения режима работы генераторной установки.

ECM контролирует напряжение в режиме работы переключателя ручного контакта сигнала и ожидает увидеть, что напряжение изменяется между 0,5 и 4,5-VDC во время нормальной работы. ECM контролирует напряжение в режиме работы автоматического контакта с сигналом переключателя и ожидает увидеть напряжение 0 или 5-VDC во время нормальной работы. Низкое напряжение будет сбивать Код 1332 по умолчанию и может быть вызвано шортами в сигнале или обратными проводами, открытым в обратном проводе или неисправным переключателем.

### Расположение компонента

Справочный раздел E для расположения панели интерфейса оператора и выключателя Off/Manual/Auto.

### Практические замечания

Возможные режимы отказа - это открытая цепь, короткий к земле, неисправный переключатель и потеря напряжения питания внутри ECM.

ECM будет рассматривать переключатель в положении Авто, когда контакт с автосигналом заземлен, независимо от состояния контакта с ручным сигналом.

См. Код устранения неполадок t05-1332.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1332
>
> ### Off/Manual/Auto Switch Circuit - Voltage Below Normal or Shorted to Low Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1332 PID(P): SPN: FMI: Lamp: Warning SRT: | The Off/Manual/Auto switch signal is shorted low. | The ECM will **only** allow the generator set to run in Auto. |
>
> Off/Manual/Auto Switch Circuit
>
> ### Circuit Description
>
> The Off/Manual/Auto switch is monitored by the engine control module (ECM) to determine the operation mode of the generator set.
>
> The ECM monitors the voltage on the operation mode switch manual SIGNAL pin and expects to see a voltage vary between 0.5 and 4.5-VDC during normal operation. The ECM monitors the voltage on the operation mode switch auto SIGNAL pin and expects to see a voltage of either 0 or 5-VDC during normal operation. Low voltage will trip Fault Code 1332 and can be caused by shorts in the signal, or return wires, an open in the return wire, or a failed switch.
>
> ### Component Location
>
> Reference Section E for location of the operator interface panel and the Off/Manual/Auto switch.
>
> ### Shoptalk
>
> The possible failure modes are open circuit, short to ground, failed switch, and loss of supply voltage inside the ECM.
>
> The ECM will consider the switch to be in the Auto position when the auto SIGNAL pin is grounded, regardless of the state of the manual SIGNAL pin.
>
> Refer to Troubleshooting Fault Code t05-1332.
