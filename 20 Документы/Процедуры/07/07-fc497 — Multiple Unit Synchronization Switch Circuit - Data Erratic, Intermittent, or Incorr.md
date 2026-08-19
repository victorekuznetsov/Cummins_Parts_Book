---
aliases:
  - "Цепь выключателя синхронизации агрегатов — данные нестабильны или неверны"
type: "Процедура"
doc: "07-fc497"
title_en: "Multiple Unit Synchronization Switch Circuit - Data Erratic, Intermittent, or Incorrect"
title_ru: "Цепь выключателя синхронизации агрегатов — данные нестабильны или неверны"
modified: "2012-12-18"
engines:
  - "93058669"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "4021442"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc497.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/07-fc497.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
  - "перевод/машинный"
---

# Multiple Unit Synchronization Switch Circuit - Data Erratic, Intermittent, or Incorrect
**Цепь выключателя синхронизации агрегатов — данные нестабильны или неверны**

> [!abstract] Процедура · `07-fc497`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-12-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc497.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/07-fc497.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 497

### Цепь выключателя синхронизации агрегатов — данные нестабильны или неверны

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 497 PID(P): S114 SPN: 1377 FMI: 2 лампы: Янтарная СРТ: | Цепь выключателя синхронизации агрегатов — данные нестабильны или неверны. | Двигатели ** не** могут управляться одним входом дроссельной заслонки. Вторичный двигатель ** должен управляться отдельно через вход дроссельной заслонки. |

![[19901352.png]]

Многофункциональная схема синхронизации Switch

### Описание цепи

Многофункциональная схема синхронизации использует дополнительный переключатель для подачи двух противоположных сигналов в электронный модуль управления (ECM). Двухполюсный переключатель с двойным броском используется для активации режима синхронизации на обоих двигателях.

### Расположение компонента

Многофункциональный блок синхронизации переключателя установлен на панели управления переключателем двигателя. Ссылка на руководство OEM для конкретного местоположения.

### Практические замечания

Переключатель синхронизации с несколькими блоками используется для активации функции синхронизации двигателя. ECM ожидает увидеть синхронизацию двигателя в / выключено и синхронизацию двигателя в / выключенном состоянии переключения после активации функции. Типичные режимы отказа, которые могут генерировать эту ошибку:

- Провода вытесняются из задней части выключателя.

- Прерывистые соединения находятся в сигнальном пути.

- Переключатель не сработал.

- Загрязненные соединения на коммутаторе синхронизации или на пути схемы.

- Эта неисправность может возникнуть, когда калибровка ECM с включенным «C-Cruise» неправильно загружена в двигателе, который не предназначен для использования многофункционального синхронизационного переключателя и не имеет установленного синхронизационного переключателя. В этой ситуации переопределение ECM с правильной не-C-Cruise калибровкой устранит неисправность.

См. Код устранения неполадок t05-497


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 497
>
> ### Multiple Unit Synchronization Switch Circuit - Data Erratic, Intermittent, or Incorrect
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 497 PID(P): S114 SPN: 1377 FMI: 2 Lamp: Amber SRT: | Multiple unit synchronization switch circuit - data erratic, intermittent, or incorrect. | Engines will **not** be able to be controlled with one throttle input. The secondary engine **must** be controlled separately via its throttle input. |
>
> Multiple Unit Synchronization Switch Circuit
>
> ### Circuit Description
>
> The multiple unit synchronization circuit uses a complimentary switch to provide two opposite signals into the electronic control module (ECM). A double-pole, double-throw switch is used to activate synchronization mode on both engines.
>
> ### Component Location
>
> The multiple unit synchronization switch is mounted on the engine switch control panel. Reference the OEM manual for the specific location.
>
> ### Shoptalk
>
> The multiple unit synchronization switch is used to activate the engine synchronization function. The ECM expects to see the engine synchronization on/off and engine synchronization on/off complimentary switch toggle state once the feature is activated. Typical fail modes which can generate this fault are:
>
> - Wires are dislodged from the rear of the switch.
>
> - Intermittent connections are in the signal path.
>
> - A switch has failed.
>
> - Contaminated connections at the synchronization switch or in the circuit path.
>
> - This fault can occur when a “C-Cruise” enabled ECM calibration is improperly loaded in an engine that is not intended to use multiple unit synchronization switch and does not have a synchronization switch installed. In this situation, realibrating the ECM with the correct non “C-Cruise” calibration will eliminate the fault.
>
> Refer to Troubleshooting Fault Code t05-497
