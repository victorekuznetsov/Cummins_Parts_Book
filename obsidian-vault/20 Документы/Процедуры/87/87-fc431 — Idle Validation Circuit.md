---
aliases:
  - "Цепь подтверждения холостого хода"
type: "Процедура"
doc: "87-fc431"
title_en: "Idle Validation Circuit"
title_ru: "Цепь подтверждения холостого хода"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc431.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc431.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Idle Validation Circuit
**Цепь подтверждения холостого хода**

> [!abstract] Процедура · `87-fc431`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc431.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc431.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 431

### Цепь подтверждения холостого хода

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 431 PID(P): P91 SPN: 091, 607 ФМИ: 2 или 4 лампы: Желтый или красный: | Напряжение, обнаруживаемое одновременно как на контактах 25 и 26 проводов OEM-интерфейса, так и на контактах бездействия и сигнала холостого хода. | Ни одного на выступление. |

![[19900374.png]]

Цепь подтверждения холостого хода

### Описание цепи

Сигнал неработающей валидации является функцией, которая отключает управление ускорителем, в то время как неправильный сигнал валидации обнаруживается электронным модулем управления (ECM). Переключатель проверки бездействия обеспечивает сигнал проверки на холостом ходу и вне холостого хода для ECM через OEM-проводник и OEM-интерфейс.

### Расположение компонента

Расположение педали или рычага ускорителя варьируется в зависимости от каждого OEM. См. руководство по OEM.

### Практические замечания

Этот код неисправности обычно вызван неправильной проводкой жгутов проводов и холостым валидационным переключателем.

Примечание: Если датчик положения ускорителя или акселератора изменен или после калибровочной загрузки, проведите педаль акселератора (переключатель зажигания в положении Включения) через его полное путешествие три раза. Эта процедура калибрует новый ускоритель с помощью ECM.

Устранение неполадок код t05-431


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 431
>
> ### Idle Validation Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 431 PID(P): P91 SPN: 091, 607 FMI: 2 or 4 Lamp: Yellow or Red SRT: | Voltage detected simultaneously on both the idle validation off-idle and idle-signal pins 25 and 26 of the OEM interface harness. | None on performance. |
>
> Idle Validation Circuit
>
> ### Circuit Description
>
> The idle validation signal is a feature that disables accelerator control while an improper validation signal is detected by the electronic control module (ECM). The idle validation switch provides an on-idle and off-idle validation signal to the ECM through the OEM harness and OEM interface harness.
>
> ### Component Location
>
> The accelerator pedal or lever location varies with each OEM. Refer to the OEM manual.
>
> ### Shoptalk
>
> This fault code is usually caused by the improper wiring of the harnesses and idle validation switch.
>
> Note: If the accelerator or accelerator position sensor is changed, or after a calibration download, cycle the accelerator pedal (keyswitch in the ON position) through its complete travel three times. This procedure calibrates the new accelerator with the ECM.
>
> Refer to Troubleshooting Fault Code t05-431
