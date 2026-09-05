---
aliases:
  - "Вход вспомогательного датчика давления 1 — особые указания"
type: "Процедура"
doc: "122-fc1544"
title_en: "Auxiliary Pressure Sensor Input 1 - Special Instructions"
title_ru: "Вход вспомогательного датчика давления 1 — особые указания"
modified: "2012-01-17"
engines:
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50"
manuals:
  - "4022102"
figures: 4
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc1544.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-fc1544.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
  - "перевод/машинный"
---

# Auxiliary Pressure Sensor Input 1 - Special Instructions
**Вход вспомогательного датчика давления 1 — особые указания**

> [!abstract] Процедура · `122-fc1544`
> **Двигатели:** [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-01-17
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc1544.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-fc1544.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1544

### Вход вспомогательного датчика давления 1 — особые указания

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1544 PID(P): СПН: 1387 FMI: 14 ламп: Обслуживание SRT: | Вход вспомогательного датчика давления 1 — особые указания | Возможный выпад мощности двигателя или выключение двигателя, в зависимости от калибровки OEM. |

![[19602245.png]]

QSK38 CM2150 Промышленный - Вспомогательный датчик давления Ввод 1 цепи

![[19602246.png]]

QSK38 CM2150 Marine - вспомогательная схема ввода 1 датчика давления

![[19602247.png]]

QSK50 и QSK60 CM2150 Промышленный - вспомогательный датчик давления Ввод 1

![[19602248.png]]

QSK50 и QSK60 CM2150 Marine/QSK60 CM2150 Drill Rig - Вспомогательный датчик давления Input 1 Circuit

### Описание цепи

Производитель оригинального оборудования (OEM) имеет возможность подключения датчика давления к электронному модулю управления (ECM). Затем создается специальная калибровка для распознавания входного сигнала вспомогательного датчика давления 1. Этот код неисправности активируется, когда входное давление от датчика OEM превышает предел защиты двигателя, определенный OEM. В морских применениях этот датчик контролирует давление масла в шестерне и код неисправности активируется, когда давление падает ниже порога, который является регулируемым параметром электронного инструментария INSITETM. В зависимости от требований OEM, нарушение защиты двигателя или даже выключение двигателя может быть связано с кодом неисправности.

### Расположение компонента

Ввод датчика давления OEM будет варьироваться в зависимости от применения. Смотрите руководство по устранению неполадок и ремонту OEM для определения местоположения датчика.

### Практические замечания

У моделей двигателей, охваченных этим руководством, несколько электронных блоков управления. У каждого блока управления свой адрес источника, который отображается при подключении INSITE™. При поиске неисправности по коду определяйте затронутый блок управления и цепь по адресу источника, который показывает INSITE™.

Этот код неисправности активируется, когда входное давление от датчика OEM превышает предел защиты двигателя, определенный OEM. Выпадение мощности двигателя возможно в зависимости от применения OEM.

В морских применениях установка по умолчанию намеренно устанавливается выше, чем любое возможное давление масла в зубчатой коробке. Это означает, что код неисправности будет активирован сразу после перекалибровки, когда регулируемые параметры не были наложены на новую калибровку. Это не позволяет заказчику предположить, что он защищен этой лампой, когда параметры не были отрегулированы должным образом. Когда датчик давления масла в шестерне не установлен, установленный на заводе резистор предназначен для сигнализации ECM о том, что условия давления масла в шестерне удовлетворительны в любое время.

Примечание: Код неисправности будет неактивным только в том случае, если ECM увидит известное состояние в течение периода (около пяти секунд) и с двигателем, работающим выше 1000 оборотов в минуту.

См. Код 1544 устранения неполадок.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1544
>
> ### Auxiliary Pressure Sensor Input 1 - Special Instructions
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1544 PID(P): SPN: 1387 FMI: 14 Lamp: Maintenance SRT: | Auxiliary Pressure Sensor Input 1 - Special Instructions | Possible engine power derate or engine shutdown, depending on the OEM calibration. |
>
> QSK38 CM2150 Industrial - Auxiliary Pressure Sensor Input 1 Circuit
>
> QSK38 CM2150 Marine - Auxiliary Pressure Sensor Input 1 Circuit
>
> QSK50 and QSK60 CM2150 Industrial - Auxiliary Pressure Sensor Input 1 Circuit
>
> QSK50 and QSK60 CM2150 Marine/QSK60 CM2150 Drill Rig - Auxiliary Pressure Sensor Input 1 Circuit
>
> ### Circuit Description
>
> The original equipment manufacturer (OEM) has the option of wiring a pressure sensor input to the electronic control module (ECM). A specific calibration is then created to recognize the auxiliary pressure sensor input 1. This fault code is activated when the pressure input from the OEM sensor exceeds the engine protection limit defined by the OEM. In marine applications, this sensor monitors gear oil pressure and the fault code is activated when the pressure falls below a threshold which is an INSITE™ electronic service tool adjustable parameter. Depending on the OEM requirements, an engine protection derate or even engine shutdown can be associated with the fault code.
>
> ### Component Location
>
> The OEM pressure sensor input will vary depending on application. Refer to the OEM troubleshooting and repair manual for sensor location.
>
> ### Shoptalk
>
> There are multiple ECMs for the engine models included in this manual. Each ECM has an individual source address that displays when INSITE™ electronic service tool is connected. When troubleshooting a fault code, use the source address displayed in INSITE™ electronic service tool to determine which ECM and circuit is affected.
>
> This fault code is activated when the pressure input from the OEM sensor exceeds the engine protection limit defined by the OEM. An engine power derate is possible depending on the OEM application.
>
> In marine applications, the default setting is intentionally set higher than any possible gear oil pressure. This is so the fault code will become active immediately after recalibration where the adjustable parameters were not overlaid on the new calibration. This prevents the customer from the assumption that he is protected by this lamp when the parameters were not adjusted properly. When the gear oil pressure sensor is not installed, the factory installed resistor is designed to signal to the ECM that gear oil pressure conditions are satisfactory at all times.
>
> Note: The fault code will only go inactive if the ECM sees a known condition for a period (about five seconds) and with the engine running above 1000 RPM.
>
> Refer to Troubleshooting Fault Code 1544.
