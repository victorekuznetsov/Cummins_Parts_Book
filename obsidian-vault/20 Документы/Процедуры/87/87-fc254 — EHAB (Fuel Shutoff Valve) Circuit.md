---
aliases:
  - "Цепь EHAB (клапан отсечки топлива)"
type: "Процедура"
doc: "87-fc254"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc254.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc254.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# EHAB (Fuel Shutoff Valve) Circuit
**Цепь EHAB (клапан отсечки топлива)**

> [!abstract] Процедура · `87-fc254`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc254.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc254.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 254

### Цепь EHAB (клапан отсечки топлива)

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 254 PID(P): S17 SPN: 632 FMI: 4 лампы: Красная СТО: | Менее 16,5 ВДК обнаружено при отключении топлива соленоидным контактом питания 43 электропроводки двигателя. | Электронный модуль управления (ECM) не выполняет никаких действий. Низкое напряжение EHAB заставит его остановить поток топлива к соответствующему насосу и отключить этот двигатель. |

![[19a00573.png]]

Электрогидравлическое устройство отключения (EHAB)

### Описание цепи

EHAB (запорный клапан) - это устройство, используемое ECM для остановки подачи топлива в насос для впрыска. ECM может отключить двигатель, отключив питание от EHAB (запорный клапан топлива).

### Расположение компонента

EHAB (запорный клапан) является неотъемлемой частью топливного насоса RP39.

### Практические замечания

- EHAB (клапан отключения топлива) **только** останавливает топливо на топливном насосе RP39.

- Осмотрите цепь EHAB (запорный клапан топлива) для внешних проводов, которые могут быть подключены для питания другого устройства. Удалите любые дополнительные провода, которые находятся в цепи.

- Если на транспортном средстве установлена внешняя система отключения, которая использует EHAB (клапан отключения топлива) для отключения двигателя, убедитесь, что он **не** вышел из строя и понизил напряжение на EHAB (клапан отключения топлива).

- Проверьте блок двигателя на проволоке шасси, чтобы убедиться, что он надежно закреплен на чистой, сухой поверхности.

- Проверьте стартер соленоидного "+" терминала для рыхлого разъема и/или вспомогательной проводов с поврежденной изоляцией.

- Проверьте заземление модуля до блока.

- Используя сервисную оснастку, номер детали 3163531 (проводка EHAB с помощью ветвого кабеля) может быть полезна для измерения напряжений замкнутого контура. Клапан EHAB требует открытия 16,5 VDC.

См. Код устранения неполадок t05-254


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 254
>
> ### EHAB (Fuel Shutoff Valve) Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 254 PID(P): S17 SPN: 632 FMI: 4 Lamp: Red SRT: | Less than 16.5 VDC detected at fuel shutoff solenoid supply pin 43 of the engine harness. | No action is taken by the electronic control module (ECM). Low voltage to the EHAB will cause it to stop fuel flow to the corresponding pump and shut down that engine bank. |
>
> Electrohydraulic Shutoff Device (EHAB) Circuit
>
> ### Circuit Description
>
> The EHAB (fuel shutoff valve) is a device used by the ECM to stop the fuel supply into the injection pump. The ECM can shut down the engine by cutting off the power to the EHAB (fuel shutoff valve).
>
> ### Component Location
>
> The EHAB (fuel shutoff valve) is integral to the RP39 fuel pump.
>
> ### Shoptalk
>
> - The EHAB (fuel shutoff valve) **only** stops fuel to the RP39 fuel pump.
>
> - Inspect the EHAB (fuel shutoff valve) circuit for external wires that can be spliced in to power another device. Remove any extra wires that are found in the circuit.
>
> - If there is an external shutdown system on the vehicle that uses the EHAB (fuel shutoff valve) for engine shutdown, make sure it has **not** failed and lowered the voltage on the EHAB (fuel shutoff valve).
>
> - Inspect the engine block to chassis ground wire to make sure it is securely fastened to a clean, dry surface.
>
> - Check the starter solenoid "+" terminal for a loose connector and/or accessory wiring with damaged insulation.
>
> - Check the module grounding to the block.
>
> - Using the service tool, Part Number 3163531 (EHAB breakout cable), can be helpful for measuring closed circuit voltages. The EHAB valve requires 16.5 VDC to open.
>
> Refer to Troubleshooting Fault Code t05-254
