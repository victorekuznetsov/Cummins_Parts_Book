---
type: "Процедура"
doc: "19-fc237"
title_en: "Multiple-Unit Synchronization"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc237.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc237.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Multiple-Unit Synchronization

> [!abstract] Процедура · `19-fc237`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc237.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc237.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 237

### Многоединая синхронизация

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 237 P(P): S30 SPN: 644 FMI: 2 лампы: Желтая СТО: 00-395 | Обязанность по циклу ввода дроссельного сигнала контакта 17 интерфейса OEM-проводов ремня составляет менее 3 процентов или более 97 процентов. | Основной двигатель и вторичные двигатели отключаются с увеличением времени после оповещения, если они жестко соединены. Только вторичные двигатели отключаются с увеличением времени после оповещения, если они мягкие. |

![[19801045.png]]

Многоединые схемы синхронизации: Мягкосвязанный, жесткосвязанный и мягкосвязанный морской

### Описание цепи

Основной двигатель выдает сигнал рабочего цикла дроссельной заслонки на контакте 24. Этот сигнал принимается вторичным двигателем (двигателями) и используется в качестве входного сигнала дроссельной заслонки. Для завершения этой схемы OEM обеспечивает подачу +5-VDC и подключается к контакту 18 вторичного двигателя.

### Расположение компонента

Выходное питание PWM расположено в OEM интерфейсе проводов.

### Практические замечания

Вторичный двигатель ожидает увидеть сигнал рабочего цикла, который варьируется от 3 до 97%. Сигнал менее 3 процентов или более 97 процентов будет генерировать код 237 ошибки во вторичном двигателе.

См. Код устранения неполадок t05-237


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 237
>
> ### Multiple-Unit Synchronization
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 237 PID(P): S30 SPN: 644 FMI: 2 Lamp: Yellow SRT: 00-395 | Duty cycle of input throttle signal pin 17 of the OEM interface harness is less than 3 percent or more than 97 percent. | The primary engine and secondary engines are shut down with increasing time after alert if hard-coupled. **Only** the secondary engines are shut down with increasing time after alert if soft-coupled. |
>
> Multiple-Unit Synchronization Circuits: Soft-Coupled, Hard-Coupled, and Soft-Coupled Marine
>
> ### Circuit Description
>
> The primary engine outputs a throttle duty cycle signal on pin 24. This signal is received by the secondary engine(s) and is used as the throttle input. To complete this circuit, a +5-VDC supply is provided by the OEM and connected to pin 18 of the secondary engine.
>
> ### Component Location
>
> The PWM output supply is located in the OEM interface harness.
>
> ### Shoptalk
>
> The secondary engine expects to see a duty cycle signal that varies between 3 and 97 percent. A signal less than 3 percent or greater than 97 percent will generate Fault Code 237 in the secondary engine.
>
> Refer to Troubleshooting Fault Code t05-237
