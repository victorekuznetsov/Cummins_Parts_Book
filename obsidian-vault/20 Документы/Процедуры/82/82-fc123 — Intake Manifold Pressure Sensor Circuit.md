---
aliases:
  - "Цепь датчика давления во впускном коллекторе"
type: "Процедура"
doc: "82-fc123"
title_en: "Intake Manifold Pressure Sensor Circuit"
title_ru: "Цепь датчика давления во впускном коллекторе"
modified: "2010-09-02"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc123.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc123.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Intake Manifold Pressure Sensor Circuit
**Цепь датчика давления во впускном коллекторе**

> [!abstract] Процедура · `82-fc123`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc123.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc123.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 123

### Цепь датчика давления во впускном коллекторе

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 123 P(P): P102 SPN: 102 FMI: 4/4 лампы: Желтая СТО: | Низкое напряжение, обнаруженное на цепи датчика давления впускного коллектора. | Уменьшите выходную мощность двигателя. |

![[19200329.png]]

Цепь датчика давления во впускном коллекторе

### Описание цепи

Датчик давления впускного коллектора контролирует давление впускного коллектора и передает информацию в электронный модуль управления (ECM) через электропроводку двигателя. Если давление коллектора потребления становится слишком высоким, это вызовет ухудшение состояния.

### Расположение компонента

Датчик давления впускного коллектора расположен в коллекторе воздухозаборника по направлению к передней части двигателя.

### Практические замечания

- Проверьте наличие высокого ограничения в впускном коллекторе воздуха из-за выключателя в коллекторе, если транспортное средство оснащено одним из них. **Не удаляйте это устройство. Если двигатель работает в легковоспламеняющейся атмосфере, устройство является важной функцией безопасности. Удаление его может привести к серьезным травмам или смерти.

- Проверьте установку устройства ограничения крутящего момента проводов жгута ветвь проводов жгута. Временно снять крутящий момент-ограничивающее устройство с электропроводки двигателя жгута и установить датчик давления впускного коллектора непосредственно на электропроводку двигателя жгута. Если код 123 неисправности становится неактивным, проверьте устройство ограничения крутящего момента.

См. Устранение неполадок код t05-123


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 123
>
> ### Intake Manifold Pressure Sensor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 123 PID(P): P102 SPN: 102 FMI: 4/4 Lamp: Yellow SRT: | Low voltage detected on the intake manifold pressure sensor circuit. | Derate in power output of the engine. |
>
> Intake Manifold Pressure Sensor Circuit
>
> ### Circuit Description
>
> The intake manifold pressure sensor monitors intake manifold pressure and passes information to the electronic control module (ECM) through the engine harness. If intake manifold pressure becomes too high, it will cause a derate condition.
>
> ### Component Location
>
> The intake manifold pressure sensor is located in the air intake manifold toward the front of the engine.
>
> ### Shoptalk
>
> - Check for high restriction in the intake air manifold due to a shutdown device in the manifold if the vehicle is equipped with one. Do **not** remove this device. If the engine is operated in a flammable atmosphere, the device is an essential safety feature. Removing it can cause severe personal injury or death.
>
> - Check for installation of a torque-limiting device breakout wiring harness. Temporarily remove the torque-limiting device from the engine harness and install the intake manifold pressure sensor directly to the engine harness. If Fault Code 123 becomes inactive, inspect the torque-limiting device.
>
> Refer to Troubleshooting Fault Code t05-123
