---
aliases:
  - "Напряжение АКБ 1 выше нормы — умеренный уровень"
type: "Процедура"
doc: "60-fc442-ecm1"
title_en: "Battery 1 Voltage - Data Valid but Above Normal Operational Range - Moderately Severe Level"
title_ru: "Напряжение АКБ 1 выше нормы — умеренный уровень"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc442-ecm1.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc442-ecm1.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Battery 1 Voltage - Data Valid but Above Normal Operational Range - Moderately Severe Level
**Напряжение АКБ 1 выше нормы — умеренный уровень**

> [!abstract] Процедура · `60-fc442-ecm1`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2012-12-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc442-ecm1.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc442-ecm1.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 442-ECM1

### Напряжение АКБ 1 выше нормы — умеренный уровень

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 442 P(P): СПН: 168 ФМИ: 0/16 лампа: Янтарная СРТ: | Напряжение АКБ 1 выше нормы — умеренный уровень. Напряжение питания ECM выше максимального уровня напряжения системы. | Возможные повреждения всех электрических компонентов. |

![[19a00872.png]]

1-вольтовая цепь аккумулятора - QST30 Power Generation Interface Engine

### Описание цепи

ECM получает постоянное напряжение от батарей через непереключенные провода батареи, которые подключены непосредственно к положительному (+) посту батареи. В непереключенном проводе батареи есть один 10-амперный предохранитель для защиты проводов OEM. ECM принимает вводимую аккумуляторную батарею через провод переключателя зажигания транспортного средства, когда переключатель зажигания транспортного средства включен. Провода 1 ВПЕРЕДЕНИЯ аккумулятора соединены непосредственно с отрицательной (-) стойкой аккумулятора.

### Расположение компонента

Двигатель имеет 3 ECM. ECM расположены на опорном скобке над обшивкой маховика в задней части двигателя. ECM1 является наиболее монтируемым ECM слева. ECM2 находится в середине, а ECM3 является наиболее правильной конструкцией ECM. ECM подключаются к батарее с помощью двигателя и OEM-проводов. Это прямое соединение обеспечивает постоянный источник питания для ECM. Расположение батареи будет варьироваться в зависимости от OEM. Ссылка на руководство по устранению неполадок и ремонту OEM для определения местоположения батареи.

### Практические замечания

Существует несколько ECM. Каждый ECM имеет индивидуальный адрес источника, который отображается при подключении инструментария электронного сервиса INSITETM. При поиске неисправности по коду определяйте затронутый блок управления и цепь по адресу источника, который показывает INSITE™.

Этот код неисправности регистрируется, когда напряжение батареи ECM 1 превышает +36-VDC. Причины этого кода неисправности включают:

- Неисправный генератор или регулятор, который перегружает систему

- Аккумуляторы, соединенные последовательно, а не параллельно

- Неправильная процедура запуска прыжка.

Устранение неполадок код t05-442


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 442-ECM1
>
> ### Battery 1 Voltage - Data Valid but Above Normal Operational Range - Moderately Severe Level
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 442 PID(P): SPN: 168 FMI: 0/16 Lamp: Amber SRT: | Battery 1 Voltage - Data Valid but Above Normal Operational Range - Moderately Severe Level. ECM supply voltage is above the maximum system voltage level. | Possible electrical damage to all electrical components. |
>
> Battery 1 Voltage Circuit - QST30 Power Generation Interface Engine
>
> ### Circuit Description
>
> The ECM receives constant voltage from the batteries through the unswitched battery wires that are connected directly to the positive (+) battery post. There is one 10-ampere fuse in the unswitched battery wire to protect the OEM harness. The ECM receives switched battery input through the vehicle keyswitch wire when the vehicle keyswitch is turned on. The battery 1 RETURN wires are connected directly to the negative (-) battery post.
>
> ### Component Location
>
> The engine has 3 ECMs. ECMs are located on a support bracket above the flywheel housing at the rear of the engine. ECM1 is the left most mounted ECM. ECM2 is in the middle and ECM3 is the right most mounted ECM. The ECMs are connected to the battery by the engine and OEM harnesses. This direct link provides a constant power supply for the ECM. The location of the battery will vary with the OEM. Reference the OEM troubleshooting and repair manual for battery location.
>
> ### Shoptalk
>
> There are multiple ECMs. Each ECM has an individual source address that displays when the INSITE™ electronic service tool is connected. When troubleshooting a fault code, use the source address displayed in INSITE™ electronic service tool to determine which ECM and circuit is affected.
>
> This fault code is logged when the ECM battery 1 voltage exceeds +36-VDC. Causes of this fault code include:
>
> - Faulty alternator or regulator that is overcharging the system
>
> - Batteries connected in series instead of parallel
>
> - Incorrect jump-starting procedure.
>
> Refer to Troubleshooting Fault Code t05-442
