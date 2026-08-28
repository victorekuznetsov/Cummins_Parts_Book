---
aliases:
  - "Цепь потенциометра регулировки статизма"
type: "Процедура"
doc: "01-fc1412"
title_en: "Droop Adjust Potentiometer Circuit"
title_ru: "Цепь потенциометра регулировки статизма"
modified: "2010-07-29"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1412.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1412.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Droop Adjust Potentiometer Circuit
**Цепь потенциометра регулировки статизма**

> [!abstract] Процедура · `01-fc1412`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1412.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1412.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1412

### Цепь потенциометра регулировки статизма

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1412 P(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Сигнал потенциометра с регулировкой падения высоко закорочен. | Функция настройки сбрасывания будет отключена, и будет использоваться значение нуля по умолчанию. Возможная потеря производительности. |

![[19802448.png]]

Цепь потенциометра регулировки статизма

### Описание цепи

Потенциометр с откидным регулированием является таковым, что оператор может регулировать количество перекрестного тока компенсации, которую регулятор напряжения производит при параллелизации. ECM контролирует напряжение и ожидает, что напряжение будет варьироваться от 0,5 до 4,5 ВДК во время нормальной работы. Высокое напряжение будет сбивать Код 1412 по умолчанию и может быть вызвано шортами в сигнальном проводе, открытым в обратном проводе или неисправным потенциометром.

### Расположение компонента

См. руководство OEM для определения местоположения.

### Практические замечания

Потенциометры очень чувствительны к окружающей среде. Очистите потенциометр и проверьте его сопротивление в первую очередь.

См. Код устранения неисправностей t05-1412


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1412
>
> ### Droop Adjust Potentiometer Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1412 PID(P): SPN: FMI: Lamp: Warning SRT: | Droop adjust potentiometer signal is shorted high. | The droop adjustment feature will be disabled and a default value of zero will be used. Possible loss of performance. |
>
> Droop Adjust Potentiometer Circuit
>
> ### Circuit Description
>
> The droop adjust potentiometer is so the operator can adjust the amount of cross-current compensation the voltage regulator produces when paralleling. The ECM monitors the voltage and expects to see the voltage vary between 0.5 and 4.5 VDC during normal operation. High voltage will trip Fault Code 1412 and can be caused by shorts in the signal wire, an open in the return wire, or a failed potentiometer.
>
> ### Component Location
>
> Refer to the OEM manual for location.
>
> ### Shoptalk
>
> Potentiometers are very sensitive to the environment. Clean the potentiometer and check its resistance first.
>
> Refer to Troubleshooting Fault Code t05-1412
