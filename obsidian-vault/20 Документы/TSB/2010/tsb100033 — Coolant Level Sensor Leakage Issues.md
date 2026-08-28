---
type: "TSB"
doc: "tsb100033"
title_en: "Coolant Level Sensor Leakage Issues"
released: "2010-04-08"
modified: "2010-04-08"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
  - "80141463"
  - "80248213"
families:
  - "QSM11"
  - "QSX15"
figures: 2
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2010/tsb100033.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb100033.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "год/2010"
  - "перевод/машинный"
---

# Coolant Level Sensor Leakage Issues

> [!abstract] TSB · `tsb100033`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Даты:** выпущен 2010-04-08 · изменён 2010-04-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2010/tsb100033.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb100033.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Проблемы утечки датчиков уровня охлаждающей жидкости

### Суть проблемы

В этом бюллетене технической службы описывается состояние, при котором датчик уровня охлаждающей жидкости может работать неправильно, позволяя охлаждающей жидкости просачиваться в электропроводную упряжку и в другие датчики и электронные устройства системы управления. Было отмечено, что оба датчика уровня охлаждающей жидкости проволоки и три датчика уровня охлаждающей жидкости проволоки протекают внутри. Сертифицированные EPA автомобильные двигатели 2007 и 2010 годов, построенные с системой последующей обработки, могут испытывать белый дым в крайних случаях, когда охлаждающая жидкость просачивается через электропроводку к датчику дифференциального давления дизельного фильтра твердых частиц после обработки.

### Подтверждение

Пострадают автомобильные, промышленные и морские применения.

- ISB CM2250

- ISB CM2150

- ISB CM850

- QSB CM850

- ISC CM2250

- ISC CM2150

- ISC CM850

- QSC CM850

- ISL CM2250

- ISL CM2150

- ISL CM850

- QSL CM850

- ISM CM876

- ISM CM875

- QSM M570

- ISX CM2250

- ISX CM871

- ISX CM870

- QSX CM570

Симптомы могут варьироваться в зависимости от семейства двигателей, OEM и применения. Симптомы включают, но не ограничиваются:

- Медленное потребление охлаждающей жидкости.
- Коды неисправностей датчика уровня охлаждения. ECM двигателя всегда регистрирует код неисправности для датчика уровня охлаждающей жидкости, когда он начинает протекать внутри охлаждающей жидкости.
- Коррозия компонентов электронной системы.
- Электронная система компонент электрических соединений мокрый с охлаждающей жидкостью.
- Белый дым. Это происходит только на двигателях, построенных с системой последующей обработки и датчиком дифференциального давления дизельного фильтра твердых частиц.

Отсоедините проводную упряжку от датчика уровня охлаждающей жидкости и проверьте штыревые и гнездовые соединения на наличие признаков вторжения охлаждающей жидкости. Электрическое соединение представляет собой плотное уплотнение, и внешняя утечка будет **не**. То же самое следует сделать и с разъемами датчиков после обработки.

Датчик уровня охлаждающей жидкости протекает внутри. Современные датчики уровня охлаждающей жидкости изготавливаются из материалов, которые могут **не** выдерживать воздействие охлаждающей жидкости с увеличенным сроком службы.

Расширенная работа с датчиком уровня протекающей охлаждающей жидкости приведет к полному загрязнению ремня электропроводки двигателя. Необходимо будет отключить разъёмы проводной ремни, включая разъем OEM 60-pin ECM, для проверки на проникновение охлаждающей жидкости. Замените поврежденные компоненты.

### Решение

Датчики уровня охлаждающей жидкости обычно поставляются OEM. В зависимости от применения транспортного средства, возможно, что датчик был поставлен компанией Cummins Inc. Самый простой способ определить, кто поставлял датчик, - это просмотреть номер детали, проштампованный на датчике, и определить, является ли этот номер детали номером Cummins или номером детали OEM. Если датчик поставляется OEM, работайте с OEM-производителем транспортного средства, чтобы заменить любые поврежденные проводные ремни, датчики, ECM или другие модули управления, которые являются частью электронной системы управления. Это **не** неисправность, оправданная Cummins® Inc. Места ремонта должны работать с OEM-производителем транспортного средства для гарантийного возмещения.

![[19804021.png]]

Вторжение охлаждающей жидкости в датчик охлаждающей жидкости.

![[19804022.png]]

Коррозионное электрическое соединение, требующее замены.

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.


> [!quote]- Original (English) · английский оригинал
> ## Coolant Level Sensor Leakage Issues
>
> ### Core Issue
>
> This Technical Service Bulletin describes a condition in which the coolant level sensor can malfunction, allowing coolant to seep into the wiring harness and into other sensors and electronic control system devices. Both two wire and three wire coolant level sensors have been observed to leak internally. 2007 and 2010 EPA-certified automotive engines built with an aftertreatment system can experience white smoke in extreme cases where coolant seeps through the wiring harness to the aftertreatment diesel particulate filter differential pressure sensor.
>
> ### Confirmation
>
> Automotive, Industrial, and Marine applications are affected.
>
> - ISB CM2250
>
> - ISB CM2150
>
> - ISB CM850
>
> - QSB CM850
>
> - ISC CM2250
>
> - ISC CM2150
>
> - ISC CM850
>
> - QSC CM850
>
> - ISL CM2250
>
> - ISL CM2150
>
> - ISL CM850
>
> - QSL CM850
>
> - ISM CM876
>
> - ISM CM875
>
> - QSM CM570
>
> - ISX CM2250
>
> - ISX CM871
>
> - ISX CM870
>
> - QSX CM570
>
> Symptoms can vary by engine family, OEM, and application. Symptoms include, but are **not** limited to:
>
> - Slow coolant consumption.
> - Coolant level sensor fault codes. The engine ECM does **not** always log a fault code for the coolant level sensor when it begins to leak coolant internally.
> - Electronic system component corrosion.
> - Electronic system component electrical connections wet with coolant.
> - White smoke. This **only** occurs on engines built with an aftertreatment system and an aftertreatment diesel particulate filter differential pressure sensor.
>
> Disconnect the wiring harness from the coolant level sensor and inspect the male and female connections for evidence of coolant intrusion. The electrical connection is a tight seal and an external leak will **not** be evident. The same should also be done to the aftertreatment sensor connectors.
>
> The coolant level sensor is leaking internally. Current coolant level sensors are manufactured with materials that can **not** withstand exposure to extended life coolant.
>
> Extended operation with a leaking coolant level sensor will result in total contamination of the engine wiring harness. It will be necessary to disconnect the harness connectors, including the OEM 60-pin ECM connector, to inspect for coolant intrusion. Replace any damaged components.
>
> ### Resolution
>
> Coolant level sensors are commonly OEM-supplied. Depending upon vehicle application, it is possible that the sensor was supplied by Cummins Inc. The simplest method to determine who supplied the sensor, is to view the part number stamped on the sensor and determine if that part number is a Cummins part number or an OEM part number. If the sensor is OEM-supplied, work with the vehicle OEM to replace any damaged harnesses, sensors, ECMs, or other control modules that are part of the electronic control system. This is **not** a failure warrantable by Cummins® Inc. Repair locations should work with the vehicle OEM for warranty reimbursement.
>
> Coolant intrusion in the coolant sensor.
>
> A corroded electrical connection that requires replacement.
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
