---
aliases:
  - "Напряжение АКБ 1 ниже нормы — умеренный уровень"
type: "Процедура"
doc: "60-fc441-ecm1"
title_en: "Battery 1 Voltage - Data Valid but Below Normal Operational Range - Moderately Severe Level"
title_ru: "Напряжение АКБ 1 ниже нормы — умеренный уровень"
modified: "2012-12-20"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc441-ecm1.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc441-ecm1.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Battery 1 Voltage - Data Valid but Below Normal Operational Range - Moderately Severe Level
**Напряжение АКБ 1 ниже нормы — умеренный уровень**

> [!abstract] Процедура · `60-fc441-ecm1`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2012-12-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc441-ecm1.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc441-ecm1.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 441-ECM1

### Напряжение АКБ 1 ниже нормы — умеренный уровень

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 441 PID(P): СПН: 168 ФМИ: 1/18 лампы: Янтарная СРТ: | Напряжение АКБ 1 ниже нормы — умеренный уровень. Напряжение питания ECM ниже минимального уровня напряжения системы. | Двигатель может перестать работать или его трудно запустить. |

![[19a00872.png]]

Непереключенное питание батареи - QST30 Power Generation Interface Engine

### Описание цепи

ECM получает постоянное напряжение от батарей через провода напряжения батареи 1, которые подключены непосредственно к положительному (+) посту батареи. В аккумуляторе 1 есть один 10-амперный предохранитель для защиты электропроводки и ECM. ECM принимает вводимую аккумуляторную батарею через провод зажигания при включении зажигания. Провода возврата аккумулятора соединены непосредственно с отрицательной (-) позицией аккумулятора.

### Расположение компонента

ECM расположены на опорном скобке над обшивкой маховика в задней части двигателя. ECM1 является передней наиболее левой крепленной ECM. ECM2 находится в середине, а ECM3 является наиболее правильной конструкцией ECM. ECM подключены к батарее с помощью OEM-проводов и электропроводки двигателя. Эта прямая связь обеспечивает постоянное электроснабжение для ECM. Расположение батареи будет варьироваться в зависимости от OEM. Ссылка на руководство по устранению неполадок и ремонту OEM для определения местоположения батареи.

### Практические замечания

Существует несколько ECM. У каждого блока управления свой адрес источника, который отображается при подключении INSITE™. При поиске неисправности по коду определяйте затронутый блок управления и цепь по адресу источника, который показывает INSITE™.

Этот код неисправности регистрируется, когда напряжение питания батареи ECM падает ниже минимального уровня напряжения системы.

- Убедитесь, что питание без переключения ECM поступает от батарей, а не от стартера или другого устройства. Проверьте наличие слабых батарей.

- Низкое напряжение во время проворачивания может привести к тому, что источник питания ECM упадет ниже спецификаций и войдет в систему кода 441.

Устранение неполадок код t05-441


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 441-ECM1
>
> ### Battery 1 Voltage - Data Valid but Below Normal Operational Range - Moderately Severe Level
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 441 PID(P): SPN: 168 FMI: 1/18 Lamp: Amber SRT: | Battery 1 Voltage - Data Valid but Below Normal Operational Range - Moderately Severe Level. ECM supply voltage is below the minimum system voltage level. | Engine can stop running or be difficult to start. |
>
> Unswitched Battery Supply - QST30 Power Generation Interface Engine
>
> ### Circuit Description
>
> The ECM receives constant voltage from the batteries through the battery 1 voltage wires that are connected directly to the positive (+) battery post. There is one 10-ampere fuse in the battery 1 voltage wires to protect the harness and ECM. The ECM receives switched battery input through the ignition wire when the ignition is turned on. The battery return wires are connected directly to the negative (-) battery post.
>
> ### Component Location
>
> The ECMs are located on a support bracket above the flywheel housing at the rear of the engine. ECM1 is the front most left mounted ECM. ECM2 is in the middle and ECM3 is the right most mounted ECM. The ECMs are connected to the battery by the OEM harness and engine harness. This direct link provides a constant power supply for the ECMs. The location of the battery will vary with the OEM. Reference the OEM troubleshooting and repair manual for battery location.
>
> ### Shoptalk
>
> There are multiple ECMs. Each ECM has an individual source address that displays when INSITE™ electronic service tool is connected. When troubleshooting a fault code, use the source address displayed in INSITE™ electronic service tool to determine which ECM and circuit is affected.
>
> This fault code is logged when the ECM battery supply voltage drops below the minimum system voltage level.
>
> - Verify that the ECM unswitched power is coming from the batteries and **not** the starter or other device. Check for possible weak batteries.
>
> - Low voltage during cranking can cause the ECM power supply to drop below specifications and log Fault Code 441.
>
> Refer to Troubleshooting Fault Code t05-441
