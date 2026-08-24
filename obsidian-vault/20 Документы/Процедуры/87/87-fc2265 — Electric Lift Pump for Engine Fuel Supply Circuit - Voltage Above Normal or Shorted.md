---
aliases:
  - "Цепь электроподкачивающего насоса — напряжение выше нормы или замыкание на плюс"
type: "Процедура"
doc: "87-fc2265"
title_en: "Electric Lift Pump for Engine Fuel Supply Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Цепь электроподкачивающего насоса — напряжение выше нормы или замыкание на плюс"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc2265.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc2265.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Electric Lift Pump for Engine Fuel Supply Circuit - Voltage Above Normal or Shorted to High Source
**Цепь электроподкачивающего насоса — напряжение выше нормы или замыкание на плюс**

> [!abstract] Процедура · `87-fc2265`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc2265.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc2265.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 2265

### Цепь электроподкачивающего насоса — напряжение выше нормы или замыкание на плюс

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 2265 PID(P): СПН: 1075 FMI: 3 лампы: Янтарная СРТ: | Цепь электроподкачивающего насоса — напряжение выше нормы или замыкание на плюс. Высокое напряжение или открытое обнаруженное на цепи сигнала насоса топливного подъема. | Двигатель может быть трудно запустить. |

![[19a00821.png]]

Электрический насос для подъема подъёмника для цепи подачи топлива для двигателя

### Описание цепи

Схема представляет собой 24-вольтовый боковой драйвер в ECM, который управляет реле электрического подъемного насоса для подачи топлива в двигатель.

### Расположение компонента

Электрический подъемный насос расположен на правом берегу сзади в высоком положении или на левом берегу спереди в высоком положении.

### Практические замечания

- Эта ошибка становится активной, если ECM обнаруживает открытую цепь при включении клавиши. Причиной этого кода неисправности является открытая схема в электрическом подъемном насосе для цепи подачи топлива двигателя между реле сигнала подачи топлива двигателя и разъемом ECM.

- Если код неисправности является прерывистым, ищите причину прерывистой открытой цепи, такой как свободные контакты или плохие соединения.

См. Код устранения неполадок t05-2265


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 2265
>
> ### Electric Lift Pump for Engine Fuel Supply Circuit - Voltage Above Normal or Shorted to High Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 2265 PID(P): SPN: 1075 FMI: 3 Lamp: Amber SRT: | Electric Lift Pump for Engine Fuel Supply Circuit - Voltage Above Normal or Shorted to High Source. High voltage or open detected at the fuel lift pump signal circuit. | Engine can be difficult to start. |
>
> Electric Lift Pump for Engine Fuel Supply Circuit
>
> ### Circuit Description
>
> The circuit is a 24 volt high side driver in the ECM that controls the electric lift pump relay for engine fuel supply.
>
> ### Component Location
>
> The electric lift pump is located on the right bank rear high position or on the left bank front high position.
>
> ### Shoptalk
>
> - This fault becomes active if the ECM detects an open circuit at key-on. The cause of this fault code is an open circuit in the electric lift pump for engine fuel supply circuit between the Engine Fuel Supply Signal relay and the ECM connector.
>
> - If the fault code is intermittent, look for the cause of an intermittent open circuit, such as loose pins or bad connections.
>
> Refer to Troubleshooting Fault Code t05-2265
