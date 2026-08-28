---
aliases:
  - "Цепь клапана отсечки топлива 2 — первопричина не определена (правый ряд)"
type: "Процедура"
doc: "01-fc1212"
title_en: "Fuel Shutoff Valve 2 Circuit - Root Cause Not Known (Right Bank)"
title_ru: "Цепь клапана отсечки топлива 2 — первопричина не определена (правый ряд)"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1212.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1212.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Fuel Shutoff Valve 2 Circuit - Root Cause Not Known (Right Bank)
**Цепь клапана отсечки топлива 2 — первопричина не определена (правый ряд)**

> [!abstract] Процедура · `01-fc1212`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1212.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1212.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1212

### Цепь клапана отсечки топлива 2 — первопричина не определена (правый ряд)

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1212 P(P): СПН: ФМИ: Лампа: Отключение SRT: | Схема 2 отключения топливного клапана - первопричина **не** известна (правый берег). | Двигатель отключится. |

![[19803752.png]]

Закрытие топливной системы клапан Solenoid Circuit

### Описание цепи

Соленоид топливного клапана представляет собой устройство, используемое электронным модулем управления (ECM) для управления подачей топлива в двигатель. ECM может отключить двигатель, отключив питание от запорного клапана топлива соленоида. Этот код неисправности может быть вызван сигналом, сокращенным до низкого или заземленного, открытым сигналом или открытым возвратом.

### Расположение компонента

См. схемы двигателя. 100-002 для расположения компонентов.

### Практические замечания

Проверьте цепь подачи топлива для внешних проводов, которые, возможно, подключены к другому устройству. Удалите любые дополнительные провода, которые находятся в цепи. Если на транспортном средстве есть внешняя система отключения, которая использует клапан отключения топлива для отключения двигателя, убедитесь, что он **не **вышел из строя и понизил напряжение на цепи отключения топлива. Проверьте блок двигателя на проволоке шасси, чтобы убедиться, что он надежно прикреплен к чистой сухой проводящей поверхности. Проверьте стартовый соленоидный положительный (+) терминал на наличие разъема или вспомогательной проводов с поврежденной изоляцией.

Диагностика включена, когда коммутатор Run/Stop находится в положении Run и двигатель работает. Режим отказа **должен быть исправлен, а неисправность **должна быть устранена и признана до перезапуска двигателя.

См. Устранение неполадок код t05-1212


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1212
>
> ### Fuel Shutoff Valve 2 Circuit - Root Cause Not Known (Right Bank)
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1212 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Fuel shutoff valve 2 circuit - root cause **not** known (right bank). | Engine will shut down. |
>
> Fuel Shutoff Valve Solenoid Circuit
>
> ### Circuit Description
>
> The fuel shutoff valve solenoid is a device used by the electronic control module (ECM) to control the engine fuel supply. The ECM can shut down the engine by cutting off the power to the fuel shutoff valve solenoid. This fault code can be caused by the signal shorted to low or ground, signal open, or return open.
>
> ### Component Location
>
> Refer to the Engine Diagrams. 100-002 for the component location.
>
> ### Shoptalk
>
> Inspect the fuel shutoff supply circuit for external wires that are, perhaps, spliced in to power another device. Remove any extra wires that are found in the circuit. If there is an external shutdown system on the vehicle that uses the fuel shutoff valve for engine shutdown, make sure it has **not** failed and lowered the voltage on the fuel shutoff circuit. Inspect the engine block to chassis ground wire to make sure it is securely fastened to a clean, dry conductive surface. Check the starter solenoid positive (+) terminal for a loose connector or accessory wiring with damaged insulation.
>
> The diagnostic is enabled when the Run/Stop Switch is in the Run position and the engine is cranking. The fail mode **must** be corrected and the fault **must** be cleared and acknowledged before the engine will restart.
>
> Refer to Troubleshooting Fault Code t05-1212
