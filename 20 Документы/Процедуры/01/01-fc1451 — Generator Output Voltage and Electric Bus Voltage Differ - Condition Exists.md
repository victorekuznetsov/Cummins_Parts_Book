---
aliases:
  - "Напряжения генератора и сети различаются — условие возникло"
type: "Процедура"
doc: "01-fc1451"
title_en: "Generator Output Voltage and Electric Bus Voltage Differ - Condition Exists"
title_ru: "Напряжения генератора и сети различаются — условие возникло"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1451.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1451.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Generator Output Voltage and Electric Bus Voltage Differ - Condition Exists
**Напряжения генератора и сети различаются — условие возникло**

> [!abstract] Процедура · `01-fc1451`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1451.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1451.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1451

### Напряжения генератора и сети различаются — условие возникло

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1451 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Выходное напряжение генератора и напряжение электрической шины отличаются более чем допустимым порогом. | Никаких действий со стороны ЕКМ не предпринимается. |

![[19802905.png]]

Схема генератора

### Описание цепи

Генераторная установка вырабатывает электроэнергию. Эта мощность находится в форме трехфазного АС. Модуль управления двигателем (ECM) использует этот код неисправности, чтобы сообщить оператору, что после закрытия выключателя напряжение генераторной установки отличалось от напряжения шины.

### Расположение компонента

См. документацию о клиенте/объекте/установке для определения местоположения параллельного контроллера.

### Практические замечания

Проверьте калибровку напряжения генератора и калибровку напряжения шины.

См. Код устранения неполадок t05-1451.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1451
>
> ### Generator Output Voltage and Electric Bus Voltage Differ - Condition Exists
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1451 PID(P): SPN: FMI: Lamp: Warning SRT: | Generator output voltage and electric bus voltage differ by more than the allowed threshold. | No action is taken by the ECM. |
>
> Generator Circuit
>
> ### Circuit Description
>
> The generator set produces electric power. This power is in the form of three-phase AC. The engine control module (ECM) uses this fault code to tell the operator that after the circuit breaker closed, the voltage of the generator set was different from the voltage of the bus.
>
> ### Component Location
>
> Refer to customer/facility/installation documentation for the location of the paralleling controller.
>
> ### Shoptalk
>
> Check the alternator voltage calibration and bus voltage calibration.
>
> Refer to Troubleshooting Fault Code t05-1451.
