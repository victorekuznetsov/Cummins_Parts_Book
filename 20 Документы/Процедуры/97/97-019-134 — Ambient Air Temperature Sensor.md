---
type: "Процедура"
doc: "97-019-134"
title_en: "Ambient Air Temperature Sensor"
modified: "2003-06-13"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
  - "80141463"
  - "80248213"
families:
  - "QSM11"
  - "QSX15"
manuals:
  - "3666415"
figures: 11
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-134.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-134.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
  - "перевод/машинный"
---

# Ambient Air Temperature Sensor

> [!abstract] Процедура · `97-019-134`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-06-13
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-134.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-134.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте пробный щуп, номер детали 3822917, при проведении измерения.

Найдите датчик температуры окружающего воздуха, установленный под или рядом с пятым колесом автомобиля.

Переведите замок зажигания в положение OFF.

Отсоедините датчик температуры окружающего воздуха от проводов датчика температуры.

![[19c00945.png]]

Установите мультиметр для измерения сопротивления.

Прикосновение к одному из мультиметров приводит к контакту 1 датчика температуры окружающего воздуха.

Прикосновение к другому мультиметру приводит к контакту 2 с датчиком температуры окружающего воздуха.

Считайте показания мультиметра.

![[19c00947.png]]

Сопротивление **должно** находиться в пределах диапазона сопротивления, как показано в таблице ниже. Если схема **не** закрыта, замените датчик температуры окружающего воздуха.

| **(°C)** | **[°F\]** | **(Ом)** |
|---|---|---|
| 0 | 32 | 29k до 36k |
| 25 | 77 | 9k до 11k |
| 50 | 122 | 3k - 4k |
| 75 | 167 | 1300—1600 |
| 100 | 212 | 600 к 750 |

После ремонта подсоедините все компоненты.

![[19c00947.png]]

### Проверка на замыкание на массу

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте пробный щуп, номер детали 3822917, при проведении измерения.

Найдите датчик температуры окружающего воздуха, установленный под или рядом с пятым колесом автомобиля.

Переведите замок зажигания в положение OFF.

Отсоедините датчик температуры окружающего воздуха от проводов датчика температуры.

![[19c00945.png]]

Установите мультиметр для измерения сопротивления.

Прикосновение к одному мультиметру приводит к контакту 1 датчика температуры окружающего воздуха.

Прикосновение к другому мультиметру приводит к корпусу датчика.

Считайте показания мультиметра.

![[19c00948.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой. Если схема **не **открыта, есть короткое замыкание на землю. Замените датчик температуры окружающего воздуха.

После ремонта подсоедините все компоненты.

![[19801621.png]]

### Снятие

Найдите датчик температуры окружающего воздуха, установленный под или рядом с пятым колесом автомобиля.

Удалите любые нейлоновые проводные связи, обеспечивающие датчик температуры окружающего воздуха и его проводку к линии сжатого воздуха или проводному трубопроводу.

![[15800060.png]]

Отсоедините датчик температуры окружающего воздуха от проводов датчика температуры.

Удалите датчик температуры окружающего воздуха.

![[19c00944.png]]

### Установка

Установите датчик температуры окружающего воздуха под или рядом с пятым колесом транспортного средства, используя нейлоновые проводные связи, чтобы обеспечить его к линии сжатого воздуха или проводному трубопроводу.

Убедитесь, что датчик расположен в месте, где он не подвергается воздействию тепла двигателя, выхлопа двигателя или прямого солнца, и не расположен непосредственно над осью. Он должен быть также расположен в районе с воздушным потоком.

![[15800060.png]]

> [!warning] ОСТОРОЖНО
> Используйте только рекомендованную Cummins смазку DS-ES, номер детали 3822934. Другие смазочные материалы, такие как моторное масло или смазка, в разъемах могут вызвать повреждение модуля управления холостым ходом, плохую производительность двигателя или преждевременный контактный износ разъема.

Нанесите небольшое количество смазки на соединительные терминалы. **не** заполнять всю полость смазкой.

![[19d00722.png]]

Подключите датчик температуры окружающего воздуха к проводах датчика температуры.

![[19c00944.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use test lead, Part Number 3822917, when taking a measurement.
>
> Locate the ambient air temperature sensor installed under or near the vehicle's fifth wheel.
>
> Turn the keyswitch to the OFF position.
>
> Disconnect the ambient air temperature sensor from the temperature sensor harness.
>
> Set the multimeter to measure resistance.
>
> Touch one of the multimeter leads to pin 1 of the ambient air temperature sensor.
>
> Touch the other multimeter lead to pin 2 of the ambient air temperature sensor.
>
> Read the value displayed on the multimeter.
>
> The resistance **must** fall within the resistance range as shown in the table below. If the circuit is **not** closed, replace the ambient air temperature sensor.
>
> | **(°C)** | **\[°F\]** | **(ohms)** |
> |---|---|---|
> | 0 | 32 | 29k to 36k |
> | 25 | 77 | 9k to 11k |
> | 50 | 122 | 3k to 4k |
> | 75 | 167 | 1300 to 1600 |
> | 100 | 212 | 600 to 750 |
>
> Connect all components after completing the repair.
>
> ### Check for Short Circuit to Ground
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use test lead, Part Number 3822917, when taking a measurement.
>
> Locate the ambient air temperature sensor installed under or near the vehicle's fifth wheel.
>
> Turn the keyswitch to the OFF position.
>
> Disconnect the ambient air temperature sensor from the temperature sensor harness.
>
> Set the multimeter to measure resistance.
>
> Touch one multimeter lead to pin 1 of the ambient air temperature sensor.
>
> Touch the other multimeter lead to the sensor casing.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short circuit to ground. Replace the ambient air temperature sensor.
>
> Connect all components after completing the repair.
>
> ### Remove
>
> Locate the ambient air temperature sensor installed under or near the vehicle's fifth wheel.
>
> Remove any nylon wire ties securing the ambient air temperature sensor and its wiring to an air line or wire conduit.
>
> Disconnect the ambient air temperature sensor from the temperature sensor harness.
>
> Remove the ambient air temperature sensor.
>
> ### Install
>
> Install the ambient air temperature sensor under or near the vehicle's fifth wheel using nylon wire ties to secure it to an air line or wire conduit.
>
> Make sure that the sensor is located in a spot where it is **not** exposed to engine heat, engine exhaust, or direct sun, and not located directly over an axle. It **must** also be located in an area with airflow.
>
> **CAUTION · Осторожно**
> Use only Cummins-recommended lubricant DS-ES, Part Number 3822934. Other lubricants, such as lubricating oil or grease, in the connectors can cause idle control module damage, poor engine performance, or premature connector pin wear.
>
> Apply a small amount of lubricant to the connector terminals. Do **not** fill the entire cavity with lubricant.
>
> Connect the ambient air temperature sensor to the temperature sensor harness.
