---
aliases:
  - "Диагностика драйвера топливоподающего насоса выявила ошибку"
type: "Процедура"
doc: "01-fc2297"
title_en: "Fuel Supply Pump Driver Diagnostic has Detected an Error"
title_ru: "Диагностика драйвера топливоподающего насоса выявила ошибку"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc2297.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc2297.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Fuel Supply Pump Driver Diagnostic has Detected an Error
**Диагностика драйвера топливоподающего насоса выявила ошибку**

> [!abstract] Процедура · `01-fc2297`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc2297.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc2297.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 2297

### Диагностика драйвера топливоподающего насоса выявила ошибку

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 2297 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Диагностика драйвера топливоподающего насоса выявила ошибку. | Приминг-насос отключен. Возможная потеря производительности. |

![[19803605.png]]

Схема подачи топлива

### Описание цепи

Трубопроводные насосы подают топливо в левый и правый боковые топливные насосы через топливный фильтр. ECM активирует насосы при запуске, в то время как двигатель закручивается, чтобы запускать топливные насосы левого и правого берега для запуска двигателя.

### Расположение компонента

См. процедуру 100-002 для определения местоположения компонента. Существует один корпус насоса для подъёмного топлива, который содержит двойные насосы для подъёмного механизма. Корпус расположен на правом берегу двигателя над маховиком и рядом с топливным фильтром.

### Практические замечания

Этот код неисправности вызван коротким замыканием в проводной упряжке или насосе. Это также может быть вызвано неудачной ЭКО.

Этот код ошибки будет **только **активен, когда двигатель работает или работает. Чтобы очистить код неисправности, режим отказа должен быть исправлен, и двигателю придется снова проворачивать, чтобы очистить.

Сервисная оснастка может использоваться для включения топливного насоса и проверки давления подачи топлива в качестве системной проверки.

См. Код устранения неполадок t05-2297


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 2297
>
> ### Fuel Supply Pump Driver Diagnostic has Detected an Error
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 2297 PID(P): SPN: FMI: Lamp: Warning SRT: | Fuel supply pump driver diagnostic has detected an error. | Priming pump is disabled. Possible loss of performance. |
>
> Fuel Supply Circuit
>
> ### Circuit Description
>
> The priming pumps supply fuel to the left and right bank fuel pumps through the fuel filter. The ECM activates the priming pumps at start up while the engine is cranking to prime the left and right bank fuel pumps for the engine to start.
>
> ### Component Location
>
> Refer to Procedure 100-002 for the component location. There is one fuel lift pump housing that contains dual lift pumps. The housing is located on the right bank of the engine above the flywheel and next to the fuel filter.
>
> ### Shoptalk
>
> This fault code is caused by a short circuit in the harness or priming pump. It can also be caused by a failed ECM.
>
> This fault code will **only** go active when the engine is cranking or running. To clear the fault code, the fail mode needs to be fixed and the engine will have to crank again to clear.
>
> The service tool can be used to enable the fuel pump and check the fuel supply pressure as a system check.
>
> Refer to Troubleshooting Fault Code t05-2297
