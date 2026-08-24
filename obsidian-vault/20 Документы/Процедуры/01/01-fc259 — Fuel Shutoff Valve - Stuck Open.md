---
aliases:
  - "Клапан отсечки топлива заклинил в открытом положении"
type: "Процедура"
doc: "01-fc259"
title_en: "Fuel Shutoff Valve - Stuck Open"
title_ru: "Клапан отсечки топлива заклинил в открытом положении"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc259.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc259.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Fuel Shutoff Valve - Stuck Open
**Клапан отсечки топлива заклинил в открытом положении**

> [!abstract] Процедура · `01-fc259`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc259.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc259.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 259

### Клапан отсечки топлива заклинил в открытом положении

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 259 PID (P): СПН: ФМИ: Лампа: Предупреждение СТО: | Клапан отсечки топлива заклинил в открытом положении. | Электронный модуль управления (ECM) не выполняет никаких действий. Возможно медленное отключение двигателя. |

![[19803585.png]]

Закрытие топливной системы клапан Solenoid Circuit

### Описание цепи

Напряжение подается в клапан отключения топлива ECM, в то время как выключатель Run/Stop находится в положении Run, а скорость двигателя равна коленчатой. При размещении выключателя Run/Stop в положении Stop напряжение на соленоиде запорного клапана топлива отключается ECM. Клапан отключения топлива закрывает и останавливает подачу топлива к приводам заправки и синхронизации.

### Расположение компонента

См. диаграммы двигателя (Процедура)[[01-100-002-tr — Engine Diagrams|100-002]]) в разделе Е настоящего руководства по местоположению компонентов.

### Практические замечания

С выключателем Run/Stop в положении Stop ECM отключает напряжение, подаваемое для поддержания открытого клапана отключения топлива. ECM продолжает запускать приводы заправки и синхронизации, когда двигатель крутится вниз. ECM контролирует скорость двигателя. Если скорость двигателя не падает после выключения соленоида клапана отключения топлива, ECM активирует эту неисправность.

См. Код устранения неполадок t05-259


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 259
>
> ### Fuel Shutoff Valve - Stuck Open
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 259 PID(P): SPN: FMI: Lamp: Warning SRT: | Fuel shutoff valve - stuck open. | No action is taken by the electronic control module (ECM). Possible engine slow shutdown. |
>
> Fuel Shutoff Valve Solenoid Circuit
>
> ### Circuit Description
>
> Voltage is supplied to the fuel shutoff valve by the ECM while the Run/Stop switch is in the Run position and engine speed is equal to crank. Upon placing the Run/Stop switch in the Stop position, the voltage to the fuel shutoff valve solenoid is turned off by the ECM. The fuel shutoff valve closes and stops fuel from flowing to the fueling and timing actuators.
>
> ### Component Location
>
> Refer to the Engine Diagrams (Procedure [[01-100-002-tr — Engine Diagrams|100-002]]) in Section E of this manual for the component location.
>
> ### Shoptalk
>
> With the Run/Stop switch in the Stop position, the ECM turns off the voltage supplied to keep the fuel shutoff valve open. The ECM continues to fire the fueling and timing actuators as the engine spins down. The ECM monitors the engine speed. If the engine speed does **not** drop after the fuel shutoff valve solenoid is turned off, the ECM activates this fault.
>
> Refer to Troubleshooting Fault Code t05-259
