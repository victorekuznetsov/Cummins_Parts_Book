---
aliases:
  - "Несовместимость калибровочного кода — вне калибровки"
type: "Процедура"
doc: "60-fc342-ecm1"
title_en: "Electronic Calibration Code Incompatibility - Out of Calibration"
title_ru: "Несовместимость калибровочного кода — вне калибровки"
modified: "2012-12-20"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc342-ecm1.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc342-ecm1.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Electronic Calibration Code Incompatibility - Out of Calibration
**Несовместимость калибровочного кода — вне калибровки**

> [!abstract] Процедура · `60-fc342-ecm1`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2012-12-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc342-ecm1.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc342-ecm1.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 342-ECM1

### Несовместимость калибровочного кода — вне калибровки

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 342 P(P): 630 SPN: ФМИ: 13 ламп: Красная СТО: | Несовместимость калибровочного кода — вне калибровки. | Трудно начать или нет. |

![[19a00867.png]]

Электронный модуль управления (ECM) - межсетевой движок QST30

### Описание цепи

ECM общаются через проводную упряжку.

### Расположение компонента

ECM1, ECM2 и ECM3 установлены над корпусом маховика на задней части двигателя. ECM1 расположен (слева направо) на левом берегу, затем ECM2 в середине и ECM3 на правом берегу.[[60-100-002 — Engine Diagrams|См. процедуру 100-002 в разделе E.]]

### Практические замечания

На этом двигателе есть несколько ECM. Каждый ECM имеет индивидуальный адрес источника, который отображается при подключении электронного инструментария INSITETM к соответствующему порту обслуживания. При устранении неисправности кода используйте адрес источника, отображаемый в инструменте электронного обслуживания INSITETM, вместе с которым подключен порт обслуживания (CM850 или CM552), чтобы определить, какая ECM и схема затронута.

ECM2 (CM850) содержит информацию о статусе ECM1 (CM552) и ECM3 (CM552). Включено ключом, если шина данных CAN прерывается между ECM2 и ECM1 и/или ECM3, сообщение не будет обновляться до тех пор, пока шина данных CAN не будет установлена. Если существует несовместимость между ECM1, ECM2 или ECM3, возникает неисправность, которая требует перекалибровки модулей, идентифицированных с неисправностью и адресом источника. Это касается несовместимости калибровок между ECM1 и ECM2 или ECM3 и не связано с доступностью. ECM1, ECM2 и ECM3 могут обмениваться данными, но что-то в калибровке ECM1 или ECM3 не соответствует ECM2.

Возможные причины:

- Неправильная или коррумпированная калибровка

- Неправильная или поврежденная ЭКМ

- Частный терминирующий резистор поврежден или отключен.

См. Код устранения неполадок t05-342


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 342-ECM1
>
> ### Electronic Calibration Code Incompatibility - Out of Calibration
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 342 PID(P): 630 SPN: FMI: 13 Lamp: Red SRT: | Electronic Calibration Code Incompatibility - Out of Calibration. | Hard to start or no start. |
>
> Electronic Control Module (ECM) - QST30 Power Generation Interface Engine
>
> ### Circuit Description
>
> The ECMs communicate via the wiring harness.
>
> ### Component Location
>
> ECM1, ECM2, and ECM3 are mounted above the flywheel housing on the rear of the engine. ECM1 is located (from left to right) on the left bank, followed by ECM2 in the middle, and ECM3 on the right bank. [[60-100-002 — Engine Diagrams|Refer to Procedure 100-002 in Section E.]]
>
> ### Shoptalk
>
> There are multiple ECMs on this engine. Each ECM has an individual source address that displays when INSITE™ electronic service tool is connected to the corresponding service port. When troubleshooting a fault code, use the source address displayed in INSITE™ electronic service tool along with which service port (CM850 or CM552) you are connected to in order to determine which ECM and circuit is affected.
>
> ECM2 (CM850) contains status information about ECM1 (CM552) and ECM3 (CM552). At key on, if the data link in interrupted between ECM2 and ECM1 and/or ECM3, the communication will not update until the data link is established. If there is a communication or performance calibration incompatibility between ECM1, ECM2, or ECM3, a fault occurs that requires a recalibration of the modules identified with the fault and source address. This is for incompatibilities in calibrations between ECM1 and ECM2 or ECM3, and not related to accessibility. ECM1, ECM2, and ECM3 can communicate, but something in ECM1 or ECM3 calibration does not match with ECM2.
>
> Possible causes:
>
> - Wrong or corrupt calibration
>
> - Wrong or damaged ECM
>
> - Private terminating resistor damaged or disconnected.
>
> Refer to Troubleshooting Fault Code t05-342
