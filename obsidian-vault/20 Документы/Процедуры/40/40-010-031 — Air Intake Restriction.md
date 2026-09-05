---
aliases:
  - "Сопротивление на впуске воздуха"
type: "Процедура"
doc: "40-010-031"
title_en: "Air Intake Restriction"
title_ru: "Сопротивление на впуске воздуха"
modified: "2004-02-19"
engines:
  - "93047320"
families:
  - "6B5.9"
manuals:
  - "4021538"
figures: 9
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-010-031.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-010-031.pdf"
tags:
  - "документ/процедура"
  - "двигатель/6B5.9"
  - "группа/40"
  - "перевод/машинный"
---

# Air Intake Restriction
**Сопротивление на впуске воздуха**

> [!abstract] Процедура · `40-010-031`
> **Двигатели:** [[93047320 — 6B5.9 CPL 3111|93047320]]
> **Семейство:** 6B5.9
> **Входит в руководства:** [[4021538 — B3.9 and B5.9 Recreational Marine Operation and Maintenance Manual|4021538]]
> **Секции:** Section 5 - Maintenance Procedures at 300 Hours or 1 Year
> **Даты:** изменён 2004-02-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-010-031.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-010-031.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Диагностика нарушений работы воздушной системы

Правильное количество чистого воздуха в цилиндрах необходимо для хорошей работы. Как обсуждалось ранее в Airflow System, попадание пыли и грязи повредит цилиндры двигателя. Пыль и грязь также могут повредить стебли и направляющие клапана, а также изнашивать лопасти компрессора турбокомпрессора, влияя на эффективность. Более крупный мусор может повредить лопасти турбокомпрессора.

![[ci900wa.png]]

Ограничение воздушного потока приводит к чрезмерному дыму и низкой мощности.

Ограничение увеличивается по мере того, как фильтр удаляет загрязняющие вещества из впускного воздуха. Ограничение воздушного потока изменяет соотношение воздух-топливо, уменьшая мощность и увеличивая дым от двигателя. Убедитесь, что воздухоочиститель поддерживается правильно.

![[ac9etwa.png]]

Ограничение воздуха - проверка

Заменить элемент воздухоочистителя, когда ограничение достигает максимального предела при номинальной мощности и скорости двигателя.

| Естественно, вдох | Турбонаддув |
|---|---|
| 50,8 мм Н2 ОО | 63,5 мм Н2 ОО |
| [2 в]. H 2 O\' | [2.5 в.] H 2 O\' |

> [!note] Примечание
> На иллюстрации показаны измерения в сантиметрах вместо миллиметров.

![[ci900na.png]]

Для двигателей с турбонаддувом измерьте ограничение непосредственно перед турбокомпрессором. Измерьте непосредственно перед впускным коллектором для двигателей с естественным аспирацией.

![[ci900nb.png]]

### Измерение

Установите вакуумный калибр или водный манометр, часть номер ST-1111-3, в воздухозаборнике.

Измерительный датчик адаптер должен быть установлен под углом 90 градусов к потоку воздуха в прямом участке трубы, диаметром в одну трубу перед турбокомпрессором.

![[ci900nb.png]]

Работайте с двигателем на полном дроссельном и номинальном оборотах при максимальной нагрузке.

Запишите данные на калибр или манометр.

|  | мм-h2o |  | в h2o |  |
|---|---|---|---|---|
| Турбонаддув |  | 63.5 | Макс | 2.5 |
| Естественно, вдох |  | 50.8 | Макс | 2 |

> [!note] Примечание
> На иллюстрации показаны измерения в сантиметрах вместо миллиметров.

![[xs800ia.png]]

Если ограничение превышает требования:

Замените или очистите фильтрующий элемент воздухоочистителя. Смотрите инструкции производителя оборудования.

![[ac1etma.png]]

Проверить впускные трубопроводы на предмет повреждения. Смотрите инструкции по ремонту оборудования производителя.

![[ca9tbsa.png]]

Удалите испытательное оборудование.

![[bp9gama.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> Diagnosing Air System Malfunctions
>
> The correct amount of clean air to the cylinders is required for good performance. As discussed earlier in Airflow System, ingested dust and dirt will damage the engine cylinders. Dust and dirt can also damage the valve stems and guides, as well as wear down the turbocharger compressor vanes affecting efficiency. Larger debris can damage the blades of the turbocharger.
>
> Airflow restriction results in excessive smoke and low power.
>
> Restriction increases as the filter removes contaminants from the intake air. Restriction airflow changes the air-to-fuel ratio, reducing power and increasing smoke from the engine. Verify that the air cleaner is being maintained correctly.
>
> Intake Air Restriction - Checking
>
> Replace the air cleaner element when the restriction reaches the maximum limit at rated engine power and speed.
>
> | Naturally Aspirated | Turbocharged |
> |---|---|
> | 50.8 mm H 2 O | 63.5 mm H 2 O |
> | \[2 in. H 2 O\] | \[2.5 in. H 2 O\] |
>
> **Note · Примечание**
> The illustration shows the measurement in centimeters instead of millimeters.
>
> For turbocharged engines, measure the restriction just before the turbocharger. Measure just before the intake manifold for naturally aspirated engines.
>
> ### Measure
>
> Install a vacuum gauge or water manometer, Part Number ST-1111-3, in the intake air piping.
>
> The gauge adapter **must** be installed at a 90-degree angle to the airflow in a straight section of pipe, one pipe diameter before the turbocharger.
>
> Operate the engine at full throttle and rated rpm with maximum load.
>
> Record the data on the gauge or manometer.
>
> |  | mm-h2o |  | in-h2o |  |
> |---|---|---|---|---|
> | Turbocharged |  | 63.5 | MAX | 2.5 |
> | Naturally Aspirated |  | 50.8 | MAX | 2 |
>
> **Note · Примечание**
> The illustration shows the measurement in centimeters instead of millimeters.
>
> If restriction exceeds specifications:
>
> Replace or clean the air filter element. Refer to the equipment manufacturer's instructions.
>
> Inspect the intake piping for damage. Refer to the equipment manufacturer's repair instructions.
>
> Remove the test equipment.
