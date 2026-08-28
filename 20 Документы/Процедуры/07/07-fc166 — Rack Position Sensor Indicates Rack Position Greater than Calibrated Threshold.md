---
aliases:
  - "Датчик положения рейки показывает значение выше калибровочного порога"
type: "Процедура"
doc: "07-fc166"
title_en: "Rack Position Sensor Indicates Rack Position Greater than Calibrated Threshold"
title_ru: "Датчик положения рейки показывает значение выше калибровочного порога"
modified: "2012-12-18"
engines:
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "4021442"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc166.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-fc166.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
  - "перевод/машинный"
---

# Rack Position Sensor Indicates Rack Position Greater than Calibrated Threshold
**Датчик положения рейки показывает значение выше калибровочного порога**

> [!abstract] Процедура · `07-fc166`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-12-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc166.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-fc166.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 166

### Датчик положения рейки показывает значение выше калибровочного порога

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 166 PID (P): S24 SPN: 733 FMI: 3 лампы: Янтарная СРТ: | Датчик положения стойки указывает, что положение стойки больше, чем калиброванный порог. | Никаких действий, предпринятых электронным модулем управления (ECM). |

![[19901354.png]]

Цепь привода рейки

### Описание цепи

Реечный привод снабжен переменным источником тока от ECM. Редуктор стойки использует этот ток для изменения положения управляющей стойки, которая регулирует количество топлива, подаваемого от топливного насоса. Датчик обратной связи положения стойки ретранслирует положение стойки привода обратно в ECM.

### Расположение компонента

Реечный привод является неотъемлемой частью топливного насоса P7100.

### Практические замечания

- Подтвердите, что разъем привода прочно на месте.

- Когда нет питания на приводе, привод закрывается и поток топлива останавливается.

Устранение неполадок код t05-166


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 166
>
> ### Rack Position Sensor Indicates Rack Position Greater than Calibrated Threshold
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 166 PID(P): S24 SPN: 733 FMI: 3 Lamp: Amber SRT: | The rack position sensor indicates the rack position is greater than the calibrated threshold. | No action taken by the electronic control module (ECM). |
>
> Rack Actuator Circuit
>
> ### Circuit Description
>
> The rack actuator is supplied with a varying current source from the ECM. The rack actuator uses this current to change the position of the control rack, which regulates the amount of fuel delivered from the fuel pump. The rack position feedback sensor relays the actuator rack position back to the ECM.
>
> ### Component Location
>
> The rack actuator is an integral part of the P7100 fuel pump
>
> ### Shoptalk
>
> - Confirm the actuator connector is firmly in place.
>
> - When there is no power to the actuator, the actuator closes and fuel flow stops.
>
> Refer to Troubleshooting Fault Code t05-166
