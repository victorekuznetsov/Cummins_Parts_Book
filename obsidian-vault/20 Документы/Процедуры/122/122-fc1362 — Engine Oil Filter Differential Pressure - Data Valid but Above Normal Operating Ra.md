---
aliases:
  - "Перепад давления на масляном фильтре выше нормы — умеренный уровень"
type: "Процедура"
doc: "122-fc1362"
title_en: "Engine Oil Filter Differential Pressure - Data Valid but Above Normal Operating Range - Moderately Severe Level"
title_ru: "Перепад давления на масляном фильтре выше нормы — умеренный уровень"
modified: "2018-05-10"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
figures: 7
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc1362.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-fc1362.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
  - "перевод/машинный"
---

# Engine Oil Filter Differential Pressure - Data Valid but Above Normal Operating Range - Moderately Severe Level
**Перепад давления на масляном фильтре выше нормы — умеренный уровень**

> [!abstract] Процедура · `122-fc1362`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2018-05-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc1362.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-fc1362.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1362

### Перепад давления на масляном фильтре выше нормы — умеренный уровень

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1362 PID(P): СПН: 99 FMI: 16 ламп: Янтарная СРТ: | Перепад давления на масляном фильтре выше нормы — умеренный уровень. | Калибровка-зависимая прогрессивная мощность ухудшается и выключение двигателя с увеличением времени после оповещения. |

![[19602188.png]]

QSK38 CM2150 Industrial - схема дифференциального давления фильтра масла

![[19602189.png]]

QSK38 CM2150 Marine - схема дифференциального давления фильтра масел

![[19602190.png]]

QSK50 CM2150 Industrial - схема дифференциального давления фильтра масла

![[19602191.png]]

QSK50 CM2150 Power Generation with Advanced Engine Montoring - Engine Oil Filter Differential Pressure Circuit (недоступная ссылка — история).

![[19602192.png]]

QSK50 CM2150 Marine - схема дифференциального давления фильтра масла

![[19e02113.png]]

QSK60 CM2150 Industrial - схема дифференциального давления фильтра масла

![[19602194.png]]

QSK60 CM2150 Marine/QSK60 CM2150 Drill Rig - контур дифференциального давления фильтра масла двигателя

### Описание цепи

Дифференциальное давление фильтра моторного масла контролируется электронным модулем управления (ECM) до и после фильтрации. Датчик давления фильтра перед масляным фильтром контролирует давление масла перед фильтрами. Датчик давления после масляного фильтра контролирует давление после масляных фильтров на QSK60. Датчик давления винты 1 моторного масла отслеживает это давление на QSK38 и QSK50. ECM контролирует напряжение на контакте сигнала и преобразует его в значение давления.

### Расположение компонента

Датчики давления до и после масляного давления расположены на головке фильтра моторного масла или рядом с ней.

### Практические замечания

У моделей двигателей, охваченных этим руководством, несколько электронных блоков управления. У каждого блока управления свой адрес источника, который отображается при подключении INSITE™. При поиске неисправности по коду определяйте затронутый блок управления и цепь по адресу источника, который показывает INSITE™.

Код 1362 по умолчанию будет активен, когда разница между давлением масла на входе и выходе головки масляного фильтра достигнет заданного значения предупреждения. Причины этого кода неисправности включают:

- Засоряемые масляные фильтры

- Поврежденные датчики или проводная упряжка

- Закрепленная масляная головка фильтра.

См. Troubleshooting Fault Code 1362.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1362
>
> ### Engine Oil Filter Differential Pressure - Data Valid but Above Normal Operating Range - Moderately Severe Level
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1362 PID(P): SPN: 99 FMI: 16 Lamp: Amber SRT: | Engine Oil Filter Differential Pressure - Data Valid but Above Normal Operating Range - Moderately Severe Level. | Calibration-dependent progressive power derate and engine shutdown with increasing time after alert. |
>
> QSK38 CM2150 Industrial - Engine Oil Filter Differential Pressure Circuit
>
> QSK38 CM2150 Marine - Engine Oil Filter Differential Pressure Circuit
>
> QSK50 CM2150 Industrial - Engine Oil Filter Differential Pressure Circuit
>
> QSK50 CM2150 Power Generation with Advanced Engine Montoring - Engine Oil Filter Differential Pressure Circuit
>
> QSK50 CM2150 Marine - Engine Oil Filter Differential Pressure Circuit
>
> QSK60 CM2150 Industrial - Engine Oil Filter Differential Pressure Circuit
>
> QSK60 CM2150 Marine/QSK60 CM2150 Drill Rig - Engine Oil Filter Differential Pressure Circuit
>
> ### Circuit Description
>
> The engine oil filter differential pressure is monitored by the electronic control module (ECM) before and after filtration. The pre-oil filter pressure sensor monitors the oil pressure before the filters. The post-oil filter pressure sensor monitors the pressure after the oil filters on the QSK60. The engine oil rifle pressure 1 sensor monitors this pressure on the QSK38 and QSK50. The ECM monitors the voltage on the signal pin and converts it to a pressure value.
>
> ### Component Location
>
> The pre-oil pressure and post-oil pressure sensors are located on or near the lubricating oil filter head.
>
> ### Shoptalk
>
> There are multiple ECMs for the engine models included in this manual. Each ECM has an individual source address that displays when INSITE™ electronic service tool is connected. When troubleshooting a fault code, use the source address displayed in INSITE™ electronic service tool to determine which ECM and circuit is affected.
>
> Fault Code 1362 will go active when the difference between the oil pressure at the inlet and outlet of the oil filter head reaches a preset warning value. Reasons for this fault code include:
>
> - Plugged oil filters
>
> - Damaged sensors or harness
>
> - Plugged oil filter head.
>
> Refer to Troubleshooting Fault Code 1362.
