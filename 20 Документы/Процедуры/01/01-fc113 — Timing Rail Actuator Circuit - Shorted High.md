---
aliases:
  - "Цепь привода рампы опережения — замыкание на плюс"
type: "Процедура"
doc: "01-fc113"
title_en: "Timing Rail Actuator Circuit - Shorted High"
title_ru: "Цепь привода рампы опережения — замыкание на плюс"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc113.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc113.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Timing Rail Actuator Circuit - Shorted High
**Цепь привода рампы опережения — замыкание на плюс**

> [!abstract] Процедура · `01-fc113`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc113.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc113.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 113

### Цепь привода рампы опережения — замыкание на плюс

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 113 P(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Схема привода привода двигателя синхронизации — закороченная высокая. Схема привода тайминга открыта, или контакт сигнала привода синхронизации закорочен на землю, или обратный контакт привода синхронизации закорочен на батарею. | Никаких действий со стороны ЕКМ не предпринимается. Актуатор открыт, закрыт или частично закрыт. Выходная мощность двигателя будет варьироваться, и может возникнуть белый дым. Также можно записать код 112. |

![[19803582.png]]

Схема движения поездов

### Описание цепи

Схема привода рельсового механизма синхронизации подает ток на привод (приводы) рельсового механизма (приводов) синхронизации. Модуль управления двигателем (ECM) командует переменным количеством тока к приводу рельса синхронизации для управления количеством давления синхронизации к топливному форсунке.

### Расположение компонента

Приводы рельсов расположены с левой стороны, к вершине, ECVA.

### Практические замечания

Подтвердите, что разъем привода прочно на месте. Когда есть питание к приводу(ам), привод открывается. Это может привести к неисправности кода 112, несоответствию потока времени.

Устранение неполадок код t05-113


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 113
>
> ### Timing Rail Actuator Circuit - Shorted High
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 113 PID(P): SPN: FMI: Lamp: Warning SRT: | Engine timing actuator circuit - shorted high. Timing actuator circuit is open, or the timing rail actuator signal pin is shorted to ground, or the timing rail actuator return pin is shorted to battery. | No action by the ECM is taken. Actuator is open, closed, or partially closed. Engine power output will vary and white smoke can occur. Fault Code 112 can also be logged. |
>
> Timing Rail Actuator Circuit
>
> ### Circuit Description
>
> The timing rail actuator circuit supplies current to the timing rail actuator(s). The engine control module (ECM) commands a varying amount of current to the timing rail actuator to control the amount of timing pressure to the injectors.
>
> ### Component Location
>
> The timing rail actuators are located at the left side, toward top, of the ECVA.
>
> ### Shoptalk
>
> Confirm that the actuator connector is firmly in place. When there is power to the actuator(s), the actuator opens. This can cause Fault Code 112, timing flow mismatch.
>
> Refer to Troubleshooting Fault Code t05-113
