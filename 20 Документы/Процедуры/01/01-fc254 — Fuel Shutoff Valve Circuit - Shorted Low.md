---
aliases:
  - "Цепь клапана отсечки топлива — замыкание на массу"
type: "Процедура"
doc: "01-fc254"
title_en: "Fuel Shutoff Valve Circuit - Shorted Low"
title_ru: "Цепь клапана отсечки топлива — замыкание на массу"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc254.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc254.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Fuel Shutoff Valve Circuit - Shorted Low
**Цепь клапана отсечки топлива — замыкание на массу**

> [!abstract] Процедура · `01-fc254`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc254.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc254.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 254

### Цепь клапана отсечки топлива — замыкание на массу

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 254 PID(P): СПН: ФМИ: Лампа: Отключение SRT: | Цепь клапана отсечки топлива — замыкание на массу. Низкое напряжение, обнаруженное при контакте сигнала запорного клапана топлива или сопротивление соленоида, упало ниже заданного порога. | Двигатель будет выключен. |

![[19803585.png]]

Закрытие топливной системы клапан Solenoid Circuit

### Описание цепи

Соленоид топливного клапана представляет собой устройство, используемое электронным модулем управления (ECM) для управления подачей топлива в двигатель. ECM может отключить двигатель, отключив питание от запорного клапана топлива соленоида.

### Расположение компонента

См. диаграммы двигателя (Процедура)[[01-100-002-tr — Engine Diagrams|100-002]]) в разделе Е настоящего руководства по местоположению компонентов.

### Практические замечания

Проверьте цепь подачи топлива для внешних проводов, которые, возможно, подключены к другому устройству. Удалите любые дополнительные провода, которые находятся в цепи. Если на транспортном средстве есть внешняя система отключения, которая использует клапан отключения топлива для отключения двигателя, убедитесь, что он ** не ** вышел из строя и понизил напряжение на цепи отключения топлива. Проверьте блок двигателя на проволоке шасси, чтобы убедиться, что он надежно прикреплен к чистой сухой проводящей поверхности. Проверьте стартовый соленоидный положительный (+) терминал на наличие разъема или вспомогательной проводов с поврежденной изоляцией.

См. Код устранения неполадок t05-254


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 254
>
> ### Fuel Shutoff Valve Circuit - Shorted Low
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 254 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Fuel shutoff valve circuit - shorted low. Low voltage detected at the fuel shutoff valve signal pin or the resistance of the solenoid has dropped below specified threshold. | The engine will shut down. |
>
> Fuel Shutoff Valve Solenoid Circuit
>
> ### Circuit Description
>
> The fuel shutoff valve solenoid is a device used by the electronic control module (ECM) to control the engine fuel supply. The ECM can shut down the engine by cutting off the power to the fuel shutoff valve solenoid.
>
> ### Component Location
>
> Refer to the Engine Diagrams (Procedure [[01-100-002-tr — Engine Diagrams|100-002]]) in Section E of this manual for the component location.
>
> ### Shoptalk
>
> Inspect the fuel shutoff supply circuit for external wires that are, perhaps, spliced in to power another device. Remove any extra wires that are found in the circuit. If there is an external shutdown system on the vehicle that uses the fuel shutoff valve for engine shutdown, make sure it has **not** failed and lowered the voltage on the fuel shutoff circuit. Inspect the engine block to chassis ground wire to make sure it is securely fastened to a clean, dry conductive surface. Check the starter solenoid positive (+) terminal for a loose connector or accessory wiring with damaged insulation.
>
> Refer to Troubleshooting Fault Code t05-254
