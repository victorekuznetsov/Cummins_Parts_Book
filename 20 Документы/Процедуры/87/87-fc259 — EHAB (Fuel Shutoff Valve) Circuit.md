---
aliases:
  - "Цепь EHAB (клапан отсечки топлива)"
type: "Процедура"
doc: "87-fc259"
title_en: "EHAB (Fuel Shutoff Valve) Circuit"
title_ru: "Цепь EHAB (клапан отсечки топлива)"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc259.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc259.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# EHAB (Fuel Shutoff Valve) Circuit
**Цепь EHAB (клапан отсечки топлива)**

> [!abstract] Процедура · `87-fc259`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc259.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc259.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 259

### Цепь EHAB (клапан отсечки топлива)

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 259 PID (P): S17 SPN: 632 FMI: 7 ламп: Красная СТО: | EHAB (запорный клапан) открыт и не будет закрываться. | ECM командует положением стойки до нуля, что останавливает заправку соответствующего банка двигателя. |

![[19a00135.png]]

Электрогидравлическое устройство отключения (EHAB)

### Описание цепи

EHAB (запорный клапан) - это устройство, используемое ECM для остановки подачи топлива в насос для впрыска. ECM может отключить двигатель, отключив питание от клапана отключения топлива.

### Расположение компонента

Соленоид EHAB (запорный клапан) является неотъемлемой частью топливного насоса RP39.

### Практические замечания

- EHAB (клапан отключения топлива) соленоид **только **останавливает топливо на топливный насос RP39.

- Осмотрите цепь питания EHAB (запорный клапан) для внешних проводов, которые могут быть подключены для питания другого устройства. Удалите любые дополнительные провода, которые находятся в цепи.

- Если на транспортном средстве имеется внешняя система отключения, которая использует EHAB (клапан отключения топлива) для отключения двигателя, убедитесь, что он **не **вышел из строя и понизил напряжение на цепи EHAB (клапан отключения топлива).

- Проверьте блок двигателя на проволоке шасси, чтобы убедиться, что он надежно закреплен на чистой, сухой поверхности.

- Проверьте стартер соленоидного терминала «+» на наличие разъема и/или вспомогательной проводов с поврежденной изоляцией.

- Проверьте заземление модуля до блока.

См. Код устранения неполадок t05-259


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 259
>
> ### EHAB (Fuel Shutoff Valve) Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 259 PID(P): S17 SPN: 632 FMI: 7 Lamp: Red SRT: | EHAB (fuel shutoff valve) is open and will **not** close. | ECM commands rack position to zero, which stops fueling corresponding engine bank. |
>
> Electrohydraulic Shutoff Device (EHAB) Circuit
>
> ### Circuit Description
>
> The EHAB (fuel shutoff valve) is a device used by the ECM to stop the fuel supply into the injection pump. The ECM can shut down the engine by cutting off the power to the fuel shutoff valve.
>
> ### Component Location
>
> The EHAB (fuel shutoff valve) solenoid is integral to the RP39 fuel pump.
>
> ### Shoptalk
>
> - The EHAB (fuel shutoff valve) solenoid **only** stops fuel to the RP39 fuel pump.
>
> - Inspect the EHAB (fuel shutoff valve) supply circuit for external wires that can be spliced in to power another device. Remove any extra wires that are found in the circuit.
>
> - If there is an external shutdown system on the vehicle that uses the EHAB (fuel shutoff valve) for engine shutdown, make sure it has **not** failed and lowered the voltage on the EHAB (fuel shutoff valve) circuit.
>
> - Inspect the engine block to chassis ground wire to make sure it is securely fastened to a clean, dry surface.
>
> - Check the starter solenoid "+" terminal for a loose connector and/or accessory wiring with damaged insulation.
>
> - Check the module grounding to the block.
>
> Refer to Troubleshooting Fault Code t05-259
