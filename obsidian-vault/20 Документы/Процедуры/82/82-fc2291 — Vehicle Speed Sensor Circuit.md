---
aliases:
  - "Цепь датчика скорости машины"
type: "Процедура"
doc: "82-fc2291"
title_en: "Vehicle Speed Sensor Circuit"
title_ru: "Цепь датчика скорости машины"
modified: "2010-09-02"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc2291.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc2291.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Vehicle Speed Sensor Circuit
**Цепь датчика скорости машины**

> [!abstract] Процедура · `82-fc2291`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc2291.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc2291.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 2291

### Цепь датчика скорости машины

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 2291 PID(P): СПН: ФМИ: Лампа: Желтая СТО: | Скорость автомобиля более 0 миль в час, обнаруженная при включении ICONTM. | Система ICONTM будет отключена.  Включено только обязательное отключение. |

![[19803217.png]]

Интегрированная схема Idle ICONTM

### Описание цепи

ECM контролирует скорость автомобиля, когда включена функция ICONTM для нарушения безопасности. ECM анализирует данные через магнитный пикап. Этот код неисправности указывает на то, что скорость автомобиля была обнаружена.

### Расположение компонента

Схема датчика скорости транспортного средства расположена на стороне передачи транспортного средства.

### Практические замечания

Эта неисправность указывает на скорость транспортного средства, превышающую 0 миль в час, когда включен ICONTM. Как правило, свободный или неисправный грунт будет генерировать шум в цепи датчика скорости транспортного средства.

См. Код устранения неполадок t05-2291


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 2291
>
> ### Vehicle Speed Sensor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 2291 PID(P): SPN: FMI: Lamp: Yellow SRT: | More than 0-mph vehicle speed detected when ICON™ is enabled. | The ICON™ system will be disabled. **Only** mandatory shutdown will be enabled. |
>
> Integrated Idle ICON™ Circuit
>
> ### Circuit Description
>
> The ECM monitors vehicle speed when ICON™ is enabled for safety violation. The ECM reviews data through the magnetic pickup. This fault code indicates that vehicle speed has been detected.
>
> ### Component Location
>
> The vehicle speed sensor circuit is located on the vehicle transmission side.
>
> ### Shoptalk
>
> This fault indicates a vehicle speed greater than 0 mph when ICON™ is enabled. Typically, a loose or faulty ground will generate noise in the vehicle speed sensor circuit.
>
> Refer to Troubleshooting Fault Code t05-2291
