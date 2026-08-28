---
aliases:
  - "Высокая частота вращения — критично"
type: "Процедура"
doc: "01-fc234"
title_en: "Engine Speed High - Critical"
title_ru: "Высокая частота вращения — критично"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc234.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc234.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Engine Speed High - Critical
**Высокая частота вращения — критично**

> [!abstract] Процедура · `01-fc234`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc234.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc234.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 234

### Высокая частота вращения — критично

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 234 PID(P): СПН: ФМИ: Лампа: Отключение SRT: | Сигналы скорости двигателя указывают на скорость двигателя, превышающую порог отключения. | Двигатель отключится. Запорные клапаны отключения топлива обесточены (клапаны закрыты). Водитель реле сверхскоростной передачи заряжается энергией. |

![[19803603.png]]

Разнос двигателя (превышение частоты вращения)

### Описание цепи

Датчик(ы) положения двигателя (мотор) контролирует(ют) положение двигателя и скорость двигателя. Затем он передает эту информацию электронному модулю управления (ECM) через электропроводку двигателя.

### Расположение компонента

Используйте следующую процедуру для определения местоположения компонентов. См. процедуру 100-002 для определения местоположения компонента.

### Практические замечания

Возможные причины этого кода неисправности включают внешние источники топлива, втягиваемые в воздухозаборник, обратное питание (моторирование) двигателя или подделку датчиков скорости / положения двигателя. Проверить впускной коллектор на наличие источников легковоспламеняющихся паров. Проверьте уплотнения турбокомпрессора, чтобы убедиться, что нет утечек масла. Осмотрите датчики скорости двигателя / положения на предмет повреждения или подделки.

См. Код устранения неполадок t05-234


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 234
>
> ### Engine Speed High - Critical
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 234 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Engine speed signals indicate an engine speed greater than shutdown threshold. | Engine will shut down. Fuel shutoff valves are de-energized (valves close). Overspeed relay driver is energized. |
>
> Engine Overspeed
>
> ### Circuit Description
>
> The engine position sensor(s) monitor the engine position and the engine speed. It then passes this information to the electronic control module (ECM) through the engine harness.
>
> ### Component Location
>
> Use the following procedure for component location. Refer to Procedure 100-002 for the component location.
>
> ### Shoptalk
>
> Possible causes of this fault code include external fuel sources drawn into the intake air passage, reverse powering (motoring) of the engine, or tampering of the engine speed/position sensors. Inspect the intake manifold for sources of flammable vapors. Check the turbocharger seals to verify that there are no oil leaks. Inspect the engine speed/position sensors for damage or tampering.
>
> Refer to Troubleshooting Fault Code t05-234
