---
aliases:
  - "Диагностика драйвера реле «готов к приёму нагрузки»"
type: "Процедура"
doc: "01-fc1491"
title_en: "Ready to Load Output Relay Driver Diagnostic"
title_ru: "Диагностика драйвера реле «готов к приёму нагрузки»"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1491.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1491.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Ready to Load Output Relay Driver Diagnostic
**Диагностика драйвера реле «готов к приёму нагрузки»**

> [!abstract] Процедура · `01-fc1491`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1491.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1491.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1491

### Диагностика драйвера реле «готов к приёму нагрузки»

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1491 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Диагностика драйвера реле Ready to Load выявила ошибку. | Любые системы/функции заказчика, зависящие от выхода готовой к загрузке, будут работать **не**. Никаких действий со стороны ЕКМ не предпринимается. Никаких потерь в производительности. |

![[19802916.png]]

Готовый к загрузке выходной релейный приводной контур

### Описание цепи

ECM проверяет драйвер реле Ready to Load, чтобы обеспечить правильную работу. ECM использует выход Ready to Load для информирования любых систем / функций клиентов, зависящих от ECM, о том, когда генераторная установка готова к нагрузке.

### Расположение компонента

См. раздел E для определения местоположения выхода для готовой к загрузке.

### Практические замечания

Возможные режимы отказа - это открытая схема, короткое замыкание, короткое к земле и потеря напряжения питания внутри ECM.

См. Код устранения неполадок t05-1491


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1491
>
> ### Ready to Load Output Relay Driver Diagnostic
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1491 PID(P): SPN: FMI: Lamp: Warning SRT: | The Ready to Load output relay driver diagnostic has detected an error. | Any customer systems/features dependent on the Ready to Load output will **not** function correctly. No action is taken by the ECM. No loss of performance. |
>
> The Ready to Load Output Relay Driver Circuit
>
> ### Circuit Description
>
> The ECM checks the Ready to Load output relay driver to ensure correct operation. The ECM uses the Ready to Load output to inform any customer systems/features dependent on the ECM for knowledge of when the generator set is ready to pick up load.
>
> ### Component Location
>
> Refer to section E for location of the output for the Ready to Load.
>
> ### Shoptalk
>
> The possible failure modes are open circuit, short circuit, short to ground, and loss of supply voltage inside the ECM.
>
> Refer to Troubleshooting Fault Code t05-1491
