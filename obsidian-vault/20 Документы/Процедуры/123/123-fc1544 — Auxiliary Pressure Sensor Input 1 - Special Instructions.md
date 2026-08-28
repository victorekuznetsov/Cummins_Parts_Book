---
aliases:
  - "Вход вспомогательного датчика давления 1 — особые указания"
type: "Процедура"
doc: "123-fc1544"
title_en: "Auxiliary Pressure Sensor Input 1 - Special Instructions"
title_ru: "Вход вспомогательного датчика давления 1 — особые указания"
modified: "2012-01-17"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4022094"
figures: 2
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-fc1544.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/123-fc1544.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
  - "перевод/машинный"
---

# Auxiliary Pressure Sensor Input 1 - Special Instructions
**Вход вспомогательного датчика давления 1 — особые указания**

> [!abstract] Процедура · `123-fc1544`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-01-17
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-fc1544.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/123-fc1544.pdf)

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
| Код неисправности: 1544 PID(P): СПН: 1387 FMI: 14 ламп: Обслуживание SRT: | Вход вспомогательного датчика давления 1 — особые указания | Возможная мощность двигателя снижается. |

![[19401823.png]]

QSK19 CM2150 Промышленный датчик вспомогательного давления Input 1 Sensor Circuit

![[19401851.png]]

QSK19 CM2150 Морской вспомогательный датчик давления Вход 1 Сенсорная схема

### Описание цепи

OEM имеет возможность подключения датчика давления к электронному модулю управления (ECM). Затем создается специальная калибровка для распознавания этого входа датчика давления. Этот код неисправности активируется, когда входное давление от датчика OEM превышает предел защиты двигателя, определенный OEM. В морских применениях этот датчик контролирует давление масла в шестерне и код неисправности активируется, когда давление падает ниже порога, который является регулируемым параметром электронного инструментария INSITETM. В зависимости от требований OEM, нарушение защиты двигателя может быть связано с кодом неисправности.

### Расположение компонента

Ввод датчика давления OEM будет варьироваться в зависимости от применения. См. руководство по обслуживанию OEM для определения местоположения датчика.

### Практические замечания

Этот код неисправности активируется, когда входное давление от датчика OEM превышает предел защиты двигателя, определенный OEM. Выпадение мощности двигателя возможно, в зависимости от применения OEM.

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
> | Fault Code: 1544 PID(P): SPN: 1387 FMI: 14 Lamp: Maintenance SRT: | Auxiliary Pressure Sensor Input 1 - Special Instructions | Possible engine power derate. |
>
> QSK19 CM2150 Industrial - Auxiliary Pressure Sensor Input 1 Sensor Circuit
>
> QSK19 CM2150 Marine- Auxiliary Pressure Sensor Input 1 Sensor Circuit
>
> ### Circuit Description
>
> The OEM has the option of wiring a pressure sensor input to the electronic control module (ECM). A specific calibration is then created to recognize this pressure sensor input. This fault code is activated when the pressure input from the OEM sensor exceeds the engine protection limit defined by the OEM. In marine applications, this sensor monitors gear oil pressure and the fault code is activated when the pressure falls below a threshold which is an INSITE™ electronic service tool adjustable parameter. Depending on the OEM requirements, an engine protection derate can be associated with the fault code.
>
> ### Component Location
>
> The OEM pressure sensor input will vary, depending on application. Refer to the OEM service manual for sensor location.
>
> ### Shoptalk
>
> This fault code is activated when the pressure input from the OEM sensor exceeds the engine protection limit defined by the OEM. An engine power derate is possible, depending on the OEM application.
>
> In marine applications, the default setting is intentionally set higher than any possible gear oil pressure. This is so the fault code will become active immediately after recalibration where the adjustable parameters were not overlaid on the new calibration. This prevents the customer from the assumption that he is protected by this lamp when the parameters were not adjusted properly. When the gear oil pressure sensor is not installed, the factory installed resistor is designed to signal to the ECM that gear oil pressure conditions are satisfactory at all times.
>
> Note: The fault code will only go inactive if the ECM sees a known condition for a period (about five seconds) and with the engine running above 1000 RPM.
>
> Refer to Troubleshooting Fault Code 1544.
