---
aliases:
  - "Новый датчик-реле частоты вращения"
type: "TSB"
doc: "tsb100632"
title_en: "New Speed Switch"
title_ru: "Новый датчик-реле частоты вращения"
released: "2007-09-17"
modified: "2007-09-17"
group: "19 - Electronic Engine Controls"
engines:
  - "93058669"
families:
  - "C8.3 · 6C8.3"
figures: 3
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2010/tsb100632.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb100632.pdf"
tags:
  - "документ/tsb"
  - "двигатель/C8.3"
  - "год/2007"
  - "перевод/машинный"
  - "тема/electronic-engine-controls"
---

# New Speed Switch
**Новый датчик-реле частоты вращения**

> [!abstract] TSB · `tsb100632`
> **Раздел Cummins:** 19 - Electronic Engine Controls
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3
> **Даты:** выпущен 2007-09-17 · изменён 2007-09-17
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2010/tsb100632.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb100632.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Новый датчик-реле частоты вращения

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### Содержание

В настоящем Бюллетене технической службы представлена общая информация и документы о преобразовании AMBAC International SWA675A1 в SWA675D1. Обе части были выпущены в Cummins Inc. Системы деталей под номером 3050323.

Общие сведения

SWA675D1 предназначен для мониторинга скорости двигателя или части вращающегося оборудования путем обнаружения импульсов от магнитного устройства.

Модуль может быть настроен для работы независимых реле при различных настройках скорости. Либо реле может быть отрегулировано для работы от 10 до 140 процентов скорости вращения двигателя.

Эта гибкость позволяет модулю использоваться для многих различных приложений, включая защиту от превышения скорости или средства отключения коленчатых винтов.

Корректировка

Корректировка точек поездки производится с помощью двух предустановленных потенциометров. Поворот ** по часовой стрелке** увеличивает соответствующую точку поездки, а поворот ** против часовой стрелки** уменьшает соответствующую точку поездки. Соответствующий светодиод будет освещен, чтобы указать, что поездка была активирована.

При применении постоянного напряжения питания постоянного тока модуль начнет подсчитывать импульсы от магнитного пикапа. Если эти импульсы превышают заданные уровни об/мин, то поездки будут активированы, а контакты реле изменят состояние.

Для предотвращения высвобождения реле предусмотрена защелка. Этот переключатель скорости может быть автоматически защелкнут и отключен путем подачи непрерывного отрицательного сигнала на терминал 5.

SWA675D1 позволит удаленному ключу или переключателю перезагрузить функцию, просто подключив терминал 2 и терминал 5 и поместив переключатель в нужное место.

Калибровка счетчика производится с использованием предварительно установленного потенциометра, который позволяет масштабировать выходной объем счетчика, чтобы соответствовать необязательному rpm-метру. Вращение заданного потенциометра ** по часовой стрелке** увеличивает показания счетчика.

| Модель SWA675A1 превращается в SWA675D1 |  |  |
|---|---|---|
|  | SWA675A1 | SWA675D1 |
| Функция | Пинз | Пинз |
| Магнитный пикап (+) | 1 | 3 |
| Магнитный пикап (-) | 2 | 4 |
| Аккумулятор (+) | 4 | 1 |
| Батарея (-) | 3 | 2 |
| Тахометр выключен (+) | 5 | 6 |
| Тахометр выключен (-) | 3 | 2 |
| хлопок | 6 | 7 |
| хлопок | 7 | 8 |
| хлопок | 8 | 9 |
| прыгать | Не применяется | 2 + 5 |
| ** Не используется | 9 | Не применяется |
| ** Не используется | 10 | Не применяется |
| ** Не используется | 11 | Не применяется |
| сверхскоростной | 12 | 10 |
| сверхскоростной | 13 | 11 |
| сверхскоростной | 14 | 12 |

> [!warning] ОСТОРОЖНО
> При замене старого блока на новый блок, если переключатель скорости используется совместно с панелью управления и эта панель управления имеет кнопку ручного сброса, очень важно, чтобы кнопка сброса была отключена. Новый SWA675D1 имеет функцию автоматического защелкивания, терминал 5 должен быть подключен к терминалу 2 для включения функции. Это позволяет защелке сбрасывать при остановке или при падении мощности.

![[19901541.png]]

Модель SWA675A1

![[19901542.png]]

Модель SWA675D1

![[19901543.png]]

Модель SWA675D1 - схема проводов


> [!quote]- Original (English) · английский оригинал
> ## New Speed Switch
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Contents
>
> This Technical Service Bulletin provides general information and documents the conversion of AMBAC International SWA675A1 to SWA675D1. Both parts were released in the Cummins Inc. parts system under Part Number 3050323.
>
> General Information
>
> The SWA675D1 speed switch is designed to monitor the speed of an engine or piece of rotating machinery by detecting the pulses from a magnetic pick-up device.
>
> The module can be set to operate the independent relays at different speed settings. Either relay can be adjusted to operate from between 10 to 140 percent of the engine rate running speed.
>
> This flexibility allows the module to be used for many different applications, including underspeed or overspeed protection or crank disconnect facilities.
>
> Adjustment
>
> Adjustment of the trip points is done using two preset potentiometers. Turning **clockwise** increases the appropriate trip point and turning **counterclockwise** decreases the appropriate trip point. The appropriate LED will be illuminated to indicate that the trip has been activated.
>
> On application of a continuous DC supply voltage, the module will start counting pulses from the magnetic pick-up. If these pulses exceed the preset rpm levels, the trips will be activated and the relay contacts will change state.
>
> A latch is provided to prevent the release of the relays. This speed switch can be made to be automatically latched and disabled by applying a continuous negative signal to terminal 5.
>
> The SWA675D1 will allow a remote key or toggle switch reset function by simply connecting terminal 2 and terminal 5 and placing the switch in the desired location.
>
> Meter calibration is done using a preset potentiometer, which enables the meter output to be scaled to match the optional rpm meter. Rotating the preset potentiometer **clockwise** increases the meter reading.
>
> | Conversion from Model SWA675A1 to SWA675D1 |  |  |
> |---|---|---|
> |  | SWA675A1 | SWA675D1 |
> | Function | Pins | Pins |
> | Magnetic Pick-up (+) | 1 | 3 |
> | Magnetic Pick-up (-) | 2 | 4 |
> | Battery (+) | 4 | 1 |
> | Battery (-) | 3 | 2 |
> | Tachometer out (+) | 5 | 6 |
> | Tachometer out (-) | 3 | 2 |
> | Crank | 6 | 7 |
> | Crank | 7 | 8 |
> | Crank | 8 | 9 |
> | Jump | N/A | 2 + 5 |
> | **Not** used | 9 | N/A |
> | **Not** used | 10 | N/A |
> | **Not** used | 11 | N/A |
> | Overspeed | 12 | 10 |
> | Overspeed | 13 | 11 |
> | Overspeed | 14 | 12 |
>
> **CAUTION · Осторожно**
> When replacing the old unit with the new unit, if the speed switch is used in conjunction with a control panel and that control panel has a manual reset button, it is very important that the reset button is disabled. The new SWA675D1 has an automatic latching reset feature, terminal 5 must be connected to terminal 2 to engage the feature. This allows the latch to reset while stopping or when the power drops.
>
> Model SWA675A1
>
> Model SWA675D1
>
> Model SWA675D1 - Wiring Diagram
