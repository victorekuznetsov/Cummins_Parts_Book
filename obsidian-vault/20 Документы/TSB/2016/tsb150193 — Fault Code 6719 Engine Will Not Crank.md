---
aliases:
  - "Код 6719: двигатель не проворачивается"
type: "TSB"
doc: "tsb150193"
title_en: "Fault Code 6719 Engine Will Not Crank"
title_ru: "Код 6719: двигатель не проворачивается"
released: "2016-01-28"
modified: "2016-01-28"
group: "05 - Fuel Systems (Pumps)"
engines:
  - "33224404"
  - "33239746"
  - "33239899"
  - "41340468"
  - "41349633"
  - "41353297"
families:
  - "K38/K50 · QSK38, QSK50"
  - "QSK19"
  - "QSK50"
  - "QSK60 CM2150 MCRS"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2015/tsb150193.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb150193.pdf"
tags:
  - "документ/tsb"
  - "двигатель/K38/K50"
  - "двигатель/QSK19"
  - "двигатель/QSK50"
  - "двигатель/QSK60CM2150MCRS"
  - "год/2016"
  - "перевод/машинный"
  - "тема/fuel-systems-pumps"
---

# Fault Code 6719 Engine Will Not Crank
**Код 6719: двигатель не проворачивается**

> [!abstract] TSB · `tsb150193`
> **Раздел Cummins:** 05 - Fuel Systems (Pumps)
> **Двигатели:** [[33224404 — QSK50 CM2150 MCRS CPL 3391|33224404]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[41340468 — QSK50 CM2150 MCRS CPL 3728|41340468]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK19, QSK50, QSK60 CM2150 MCRS
> **Даты:** выпущен 2016-01-28 · изменён 2016-01-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2015/tsb150193.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb150193.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Код 6719: двигатель не проворачивается

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### Содержание

**Затронутая продукция**

- QSK19 CM2150 MCRS
- QSK38 CM2150 MCRS
- QSK50 CM2150 MCRS
- QSK60 CM2150 MCRS

**Проблема**

Клиенты могут столкнуться с отсутствием кривошипа и состояния запуска после того, как лампа STOP ENGINE (красная лампа) загорается для наиболее серьезных ошибок кода 6719.

Некоторые интерфейсы приложений производителя оригинального оборудования (OEM) **не** позволяют проворачивать, если активна лампа STOP ENGINE. В кодах калибровки ECM, перечисленных в таблице 1 ниже, код по умолчанию 6719, который вызывает лампу STOP ENGINE, **не может быть очищен с помощью цикла мощности ECM, если включено включение двигателя **не.

Наименее серьезный код 2261 и умеренно тяжелый код 2216 также активны для давления подачи топливного насоса, что означает проблему качества топлива и растущее ограничение топливного фильтра 2-й стадии.

Для того, чтобы коды ошибок были понятны без использования инструментов электронного обслуживания INSITETM, необходимо выполнить три условия:

1. Модуль управления двигателем (ECM) Power Cycle (отключаемый на 30 секунд)
2. 2 Стадия Датчик давления топлива измеряется ниже порога 1400 кПа[203 psi]
3. Двигатель rpm выше 600 об/мин.

**Проверка**

Приложения, которые позволяют **не** проворачивать активную лампу STOP ENGINE, будут затронуты, если верно следующее:

1. ECM имеет код калибровки ECM из таблицы 1 ниже
2. Заглушение топливного фильтра 2-й стадии приводит к появлению кода ошибки 6719
3. Приложение/OEM будет **не** включать стартер до тех пор, пока не выключится лампа STOP ENGINE, когда код ошибки 6719 не будет активирован.
4. Включение двигателя ECM завершено в попытке очистить код ошибки и перезапустить двигатель

| Таблица 1, Поврежденные коды калибровки ECM |  |  |  |  |
|---|---|---|---|---|
| AQ60479.04 | AQ60294.07 | AQ60376.09 | AQ60371.10 | AQ60691.05 |
| AQ60217.15 | AQ60458.05 | AQ60377.10 | AQ60416.07 | AQ60694.03 |
| AQ60252.10 | AQ60489.03 | AQ60378.11 | AQ60441.09 | AQ60677.03 |
| AQ60296.08 | AQ60492.04 | AQ60379.10 | AQ60455.08 |  |
| AQ60320.08 | AQ60301.09 | AQ60380.10 | AQ60361.10 |  |
| AQ60484.04 | AQ60493.05 | AQ60381.10 | AQ60363.12 |  |
| AQ60504.04 | AQ60421.07 | AQ60386.11 | AQ60364.10 |  |
| AQ60701.02 | AQ60498.04 | AQ60395.11 | AQ60365.10 |  |
| AQ60399.11 | AQ60429.07 | AQ60404.11 | AQ60387.13 |  |
| AQ60401.10 | AQ60500.04 | AQ60445.07 | AQ60388.10 |  |
| AQ60420.06 | AQ60297.06 | AQ60476.07 | AQ60389.10 |  |
| AQ60490.07 | AQ60309.08 | AQ60690.02 | AQ60390.10 |  |
| AQ60220.15 | AQ60310.08 | AQ60695.03 | AQ60391.12 |  |
| AQ60338.11 | AQ60444.06 | AQ60696.03 | AQ60392.08 |  |
| AQ60293.07 | AQ60463.05 | AQ60696.03 | AQ60397.09 |  |
| AQ60491.04 | AQ60464.06 | AQ60700.04 | AQ60402.10 |  |
| AQ60287.10 | AQ60453.08 | AQ60751.00 | AQ60410.09 |  |
| AQ60480.04 | AQ60359.11 | AQ60454.08 | AQ60440.08 |  |
| AQ60288.10 | AQ60362.10 | AQ60360.10 | AQ60442.07 |  |
| AQ60481.05 | AQ60366.10 | AQ60367.10 | AQ60443.11 |  |
| AQ60289.12 | AQ60373.12 | AQ60368.10 | AQ60456.08 |  |
| AQ60417.08 | AQ60374.10 | AQ60369.10 | AQ60475.08 |  |
| AQ60292.07 | AQ60375.10 | AQ60370.10 | AQ60499.06 |  |

**Решение**

Доступны новые калибровочные коды ECM, которые разрешают состояние без кривошипа без запуска, вызванное активным кодом 6719 по умолчанию.

- Установите последний калибровочный код ECM.
- Устранение основной причины заглушения топливного фильтра после проверки ограничения входного отверстия топлива.

Код 4615 ошибок заменил код 6719 в новых калибровочных кодах ECM.

Теория работы кода 2261, 2216 и 4615 с новыми кодами калибровки ECM приведена в таблице 2 ниже.

| Таблица 2, Теория кода ошибки |  |  |  |  |  |
|---|---|---|---|---|---|
| Код ошибки | Тип лампы | сцепление | Двигатель Derate | Условие для активации | Условия для очистки |
| 2261 | Техническое обслуживание | Нет | Нет | Давление подачи топлива выше 1000 кПа[145 psi] | Давление подачи топлива ниже 1000 кПа[145 psi] |
| 2216 | Эмбер Уорнинг | Да | Нет | Давление подачи топлива выше 1200 кПа[174 psi] | Запуск двигателя с частотой выше 600 оборотов в минуту и давлением подачи топлива ниже 1200 кПа[174 psi] |
| 4615 | Эмбер Уорнинг | Да | 1400 об/мин | Давление подачи топлива выше 1400 кПа[203 psi] | Включение вниз ECM, сопровождаемое скоростью двигателя выше 600 об/мин и давлением подачи топлива ниже 1400 кПа[203 psi] |

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## Fault Code 6719 Engine Will Not Crank
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Contents
>
> **Product Affected**
>
> - QSK19 CM2150 MCRS
> - QSK38 CM2150 MCRS
> - QSK50 CM2150 MCRS
> - QSK60 CM2150 MCRS
>
> **Issue**
>
> Customers may encounter a no crank no start condition after STOP ENGINE lamp (red lamp) illuminates for most severe Fault Code 6719.
>
> Certain Original Equipment Manufacturer (OEM) application interfaces will **not** enable cranking if a STOP ENGINE lamp is active. In the ECM calibration codes listed in Table 1 below, Fault Code 6719, which causes the STOP ENGINE lamp, is **not** able to be cleared with ECM power cycle if engine cranking is **not** enabled.
>
> Least severe Fault Code 2261 and moderately severe Fault Code 2216 also active for fuel pump supply pressure signify a fuel quality issue and rising Stage 2 fuel filter restriction.
>
> In order for the Fault Codes to clear without using INSITE™ electronic service tool, three things **must** be satisfied:
>
> 1. Engine Control Module (ECM) Power Cycle (key off for 30 seconds)
> 2. Stage 2 Fuel Pressure Sensor measures below threshold of 1400 kPa \[ 203 psi \]
> 3. Engine rpm is above 600 rpm.
>
> **Verification**
>
> Applications that do **not** enable cranking with an active STOP ENGINE lamp will be affected if the following is true:
>
> 1. ECM has ECM calibration code from Table 1 below
> 2. Stage 2 fuel filter plugging is generating Fault Code 6719
> 3. Application/OEM will **not** engage starter until STOP ENGINE lamp is turned off when Fault Code 6719 goes inactive
> 4. Engine ECM power down completed in attempt to clear Fault Code and restart engine
>
> | Table 1, Affected ECM Calibration Codes |  |  |  |  |
> |---|---|---|---|---|
> | AQ60479.04 | AQ60294.07 | AQ60376.09 | AQ60371.10 | AQ60691.05 |
> | AQ60217.15 | AQ60458.05 | AQ60377.10 | AQ60416.07 | AQ60694.03 |
> | AQ60252.10 | AQ60489.03 | AQ60378.11 | AQ60441.09 | AQ60677.03 |
> | AQ60296.08 | AQ60492.04 | AQ60379.10 | AQ60455.08 |  |
> | AQ60320.08 | AQ60301.09 | AQ60380.10 | AQ60361.10 |  |
> | AQ60484.04 | AQ60493.05 | AQ60381.10 | AQ60363.12 |  |
> | AQ60504.04 | AQ60421.07 | AQ60386.11 | AQ60364.10 |  |
> | AQ60701.02 | AQ60498.04 | AQ60395.11 | AQ60365.10 |  |
> | AQ60399.11 | AQ60429.07 | AQ60404.11 | AQ60387.13 |  |
> | AQ60401.10 | AQ60500.04 | AQ60445.07 | AQ60388.10 |  |
> | AQ60420.06 | AQ60297.06 | AQ60476.07 | AQ60389.10 |  |
> | AQ60490.07 | AQ60309.08 | AQ60690.02 | AQ60390.10 |  |
> | AQ60220.15 | AQ60310.08 | AQ60695.03 | AQ60391.12 |  |
> | AQ60338.11 | AQ60444.06 | AQ60696.03 | AQ60392.08 |  |
> | AQ60293.07 | AQ60463.05 | AQ60696.03 | AQ60397.09 |  |
> | AQ60491.04 | AQ60464.06 | AQ60700.04 | AQ60402.10 |  |
> | AQ60287.10 | AQ60453.08 | AQ60751.00 | AQ60410.09 |  |
> | AQ60480.04 | AQ60359.11 | AQ60454.08 | AQ60440.08 |  |
> | AQ60288.10 | AQ60362.10 | AQ60360.10 | AQ60442.07 |  |
> | AQ60481.05 | AQ60366.10 | AQ60367.10 | AQ60443.11 |  |
> | AQ60289.12 | AQ60373.12 | AQ60368.10 | AQ60456.08 |  |
> | AQ60417.08 | AQ60374.10 | AQ60369.10 | AQ60475.08 |  |
> | AQ60292.07 | AQ60375.10 | AQ60370.10 | AQ60499.06 |  |
>
> **Resolution**
>
> New ECM calibration codes are available that resolve the no crank no start condition caused by Fault Code 6719 coming active.
>
> - Install the latest ECM calibration code.
> - Address the root cause of fuel filter plugging after fuel inlet restriction is verified.
>
> Fault Code 4615 has replaced Fault Code 6719 in the new ECM calibration codes.
>
> The theory of operation for Fault Code 2261, 2216, and 4615 with the new ECM calibration codes can be found in Table 2 below.
>
> | Table 2, Fault Code Theory of Operation |  |  |  |  |  |
> |---|---|---|---|---|---|
> | Fault Code | Lamp Type | Latching | Engine Derate | Condition for Activation | Conditions for Clearing |
> | 2261 | Maintenance | No | No | Fuel supply pressure is above 1000 kPa \[ 145 psi \] | Fuel supply pressure below 1000 kPa \[ 145 psi \] |
> | 2216 | Amber Warning | Yes | No | Fuel supply pressure is above 1200 kPa \[ 174 psi \] | Powering down the ECM followed by engine speed above 600 rpm and fuel supply pressure below 1200 kPa \[ 174 psi \] |
> | 4615 | Amber Warning | Yes | 1400 rpm | Fuel supply pressure is above 1400 kPa \[ 203 psi \] | Powering down the ECM followed by engine speed above 600 rpm and fuel supply pressure below 1400 kPa \[ 203 psi \] |
>
> ### Document History
