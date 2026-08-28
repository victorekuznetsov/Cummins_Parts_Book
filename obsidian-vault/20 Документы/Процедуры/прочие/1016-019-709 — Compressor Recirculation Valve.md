---
type: "Процедура"
doc: "1016-019-709"
title_en: "Compressor Recirculation Valve"
modified: "2026-02-01"
engines:
  - "77804810"
families:
  - "15N"
manuals:
  - "5659763"
figures: 6
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/1016/1016-019-709.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/1016-019-709.pdf"
tags:
  - "документ/процедура"
  - "двигатель/15N"
  - "перевод/машинный"
---

# Compressor Recirculation Valve

> [!abstract] Процедура · `1016-019-709`
> **Двигатели:** [[77804810 — 15N CM2380 M104B CPL 5977|77804810]]
> **Семейство:** 15N
> **Входит в руководства:** [[5659763 — 15N CM2380 M104B Service Manual|5659763]]
> **Секции:** Section 19 - Electronic Controls - Group 19
> **Даты:** изменён 2026-02-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/1016/1016-019-709.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/1016-019-709.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Выбор сервисного инструмента

#### Рекомендованный сервисный инструмент Cummins®

- Цифровой мультиметр, часть 3400162
- Электрический испытательный щуп Kit, номер детали 5299367

#### Дополнительные сервисные позиции

- Никаких дополнительных предметов обслуживания не требуется.

### Общие сведения

Клапан (1) рециркуляции компрессора перенаправляет воздух от розетки турбокомпрессора к входу турбокомпрессора, когда дроссель закрывается. Клапан рециркуляции компрессора установлен на турбокомпрессоре. Клапан управляется модулем управления двигателем (ECM).

Клапан закрывается, когда клапан **не** заряжен. Клапан откроется, когда ECM обнаружит, что дроссел закрыт.

![[19s00256.png]]

### Первичная проверка

Отсоедините клапан рециркуляции компрессора от электропроводки двигателя.

Измерить сопротивление между штифтом рециркуляции компрессора (+) и штифтом рециркуляции компрессора (-). Используйте цифровой мультиметр, Часть Номер 3164489, из Цифровой мультиметрический комплект, Часть Номер 3400162, и измерительный щуп из Электрического испытательного щупа, Часть Номер 5299367.

| Сопротивление |  |
|---|---|
|  | Омс |
| Минь | 14.7 |
| Макс | 16.7 |

![[3377161.png]]

### Подготовительные операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Отсоедините аккумуляторные батареи. См. сервисную документацию изготовителя оборудования.

### Снятие

Отсоедините разъём ремня электропроводки двигателя от клапана рециркуляции компрессора.

Удалите четыре болта поочередно и клапан рециркуляции компрессора из турбокомпрессора.

![[19s00257.png]]

### Проверка при повторном использовании

Проверить клапан рециркуляции компрессора на наличие загрязнения маслом, поврежденных или открытых проводов, изогнутых или сломанных штифтов, поврежденного кольца и поврежденных разъёмов.

Замените клапан рециркуляции компрессора, если обнаружено повреждение.

![[19s00258.png]]

Измерить высоту свободного состояния головки клапанного чехла. Заменить клапан рециркуляции компрессора, если измерение не соответствует спецификации.

| Свободное состояние Высота клапанного чехла Головка |  |  |
|---|---|---|
| мм |  | в |
| 29.5 | Мин | 1.16 |
| 30.5 | Макс | 1.20 |

![[19s00259.png]]

### Установка

Установите клапан рециркуляции компрессора и четыре болта.

> [!tip] Момент затяжки
> 9 Н·м [80 фунт-дюйм]

Подключите разъём ремня электропроводки двигателя к клапану рециркуляции компрессора.

![[19s00257.png]]

### Завершающие операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Подсоедините аккумуляторные батареи. См. сервисную документацию изготовителя оборудования.
- Управляйте двигателем. Проверьте правильность операции.


> [!quote]- Original (English) · английский оригинал
> ### Select Service Tools
>
> #### Recommended Cummins® Service Tools
>
> - Digital Multimeter Kit, Part Number 3400162
> - Electrical Test Lead Kit, Part Number 5299367
>
> #### Additional Service Items
>
> - No additional service items required.
>
> ### General Information
>
> The compressor recirculation valve (1) recirculates air from the turbocharger outlet to the turbocharger inlet when the throttle closes. The compressor recirculation valve is mounted on the turbocharger. The valve is controlled by the Engine Control Module (ECM).
>
> The valve is closed when the valve is **not** energized. The valve will open when the ECM detects the throttle is closed.
>
> ### Initial Check
>
> Disconnect the compressor recirculation valve from the engine wiring harness.
>
> Measure the resistance between the compressor recirculation valve (+) pin and the compressor recirculation valve (-) pin. Use digital multimeter, Part Number 3164489, from Digital Multimeter Kit, Part Number 3400162, and test leads from Electrical Test Lead Kit, Part Number 5299367.
>
> | Resistance |  |
> |---|---|
> |  | Ohms |
> | Min | 14.7 |
> | Max | 16.7 |
>
> ### Preparatory Steps
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Disconnect the batteries. See equipment manufacturer service information.
>
> ### Remove
>
> Disconnect the engine harness connector from the compressor recirculation valve.
>
> Remove the four capscrews alternately and the compressor recirculation valve from turbocharger.
>
> ### Inspect for Reuse
>
> Inspect the compressor recirculation valve for oil contamination, damaged or exposed wires, bent or broken pins, damaged o-ring, and damaged connectors.
>
> Replace the compressor recirculation valve if damage is found.
>
> Measure the free state height of the valve cover head. Replace the compressor recirculation valve if the measurement does **not** meet the specification.
>
> | Free State Height of Valve Cover Head |  |  |
> |---|---|---|
> | mm |  | in |
> | 29.5 | MIN | 1.16 |
> | 30.5 | MAX | 1.20 |
>
> ### Install
>
> Install the compressor recirculation valve and four capscrews.
>
> **Момент затяжки · Torque Value**
> 9 n•m [80 in-lb]
>
> Connect the engine harness connector to the compressor recirculation valve.
>
> ### Finishing Steps
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Connect the batteries. See equipment manufacturer service information.
> - Operate the engine. Check for proper operation.
