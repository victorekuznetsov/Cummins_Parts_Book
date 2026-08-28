---
type: "Процедура"
doc: "1016-019-370"
title_en: "EGR Differential Pressure Sensor"
modified: "2022-11-23"
engines:
  - "77804810"
families:
  - "15N"
manuals:
  - "5659763"
figures: 5
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/1016/1016-019-370.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/1016-019-370.pdf"
tags:
  - "документ/процедура"
  - "двигатель/15N"
  - "перевод/машинный"
---

# EGR Differential Pressure Sensor

> [!abstract] Процедура · `1016-019-370`
> **Двигатели:** [[77804810 — 15N CM2380 M104B CPL 5977|77804810]]
> **Семейство:** 15N
> **Входит в руководства:** [[5659763 — 15N CM2380 M104B Service Manual|5659763]]
> **Секции:** Section 19 - Electronic Controls - Group 19
> **Даты:** изменён 2022-11-23
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/1016/1016-019-370.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/1016-019-370.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Выбор сервисного инструмента

#### Рекомендованный сервисный инструмент Cummins®

- Электронный сервисный инструмент Cummins® или эквивалент

#### Дополнительные сервисные позиции

- Никаких дополнительных предметов обслуживания не требуется.

### Общие сведения

Датчик дифференциального давления клапана с отработавшим газом (EGR) имеет два порта, которые ощущают падение давления через вход газа EGR в впускное соединение. Модуль управления двигателем (ECM) использует это падение давления для расчета количества газа EGR, поступающего в впуск. Этот расчет помогает определить командное положение клапана EGR, который будет контролировать количество потока газа EGR в двигатель.

Датчик дифференциального давления клапана EGR установлен на верхней части трубки вентури.

### Подготовительные операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Отсоедините аккумуляторные батареи. См. сервисную документацию изготовителя оборудования.
- Очистите область вокруг датчика дифференциального давления EGR.

### Снятие

Отсоедините разъем жгута проводов двигателя от датчика дифференциального давления EGR.

Удалите два болта из основания датчика и удалите датчик из двигателя.

![[19s00192.png]]

### Очистка и проверка при повторном использовании

> [!danger] ОПАСНО
> При работе со сжатым воздухом применяйте защиту глаз и лица. Разлетающиеся частицы и грязь могут привести к травме.

Очистите датчик дифференциального давления EGR и поверхности монтажа адаптера. Удалите любые остатки грязи или сажи.

Если датчик дифференциального давления EGR заморожен, разморозьте датчик, используя теплый воздух ниже 60°C[140°F].

Просушите сжатым воздухом.

Осмотрите кронштейн датчика дифференциального давления EGR на наличие трещин или трения. Если повреждение присутствует, датчик **должен быть заменен. Скобка **не является пригодным компонентом.

![[19b00265.png]]

Осмотрите кольца на наличие трещин или других повреждений.

Замените кольца, если обнаружены трещины или другие повреждения.

![[19c01419.png]]

### Установка

Убедитесь, что кольца расположены и поместите датчик дифференциального давления EGR на трубку вентури.

![[19s00193.png]]

Затяните болты.

> [!tip] Момент затяжки
> 8 Н·м [71 фунт-дюйм]

Подключите проводку к датчику (1).

![[19s00194.png]]

### Завершающие операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Подсоедините аккумуляторные батареи. См. сервисную документацию изготовителя оборудования.
- Используйте рекомендованную электронный сервисный инструмент Cummins® или эквивалент для сброса топливных столов, если заменен датчик дифференциального давления EGR. См. процедуру 005-263 в разделе 5.
- Управляйте двигателем. Проверьте на отсутствие утечек.


> [!quote]- Original (English) · английский оригинал
> ### Select Service Tools
>
> #### Recommended Cummins® Service Tools
>
> - Cummins® electronic service tool, or equivalent
>
> #### Additional Service Items
>
> - No additional service items required.
>
> ### General Information
>
> The Exhaust Gas Recirculation (EGR) valve differential pressure sensor has two ports that sense a pressure drop across the EGR gas entrance to the intake connection. The Engine Control Module (ECM) uses this pressure drop to calculate the amount of EGR gas entering the intake. This calculation helps to determine the commanded position of the EGR valve that will control the amount of EGR gas flow into the engine.
>
> The EGR valve differential pressure sensor is mounted on the top of the venturi tube.
>
> ### Preparatory Steps
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Disconnect the batteries. See equipment manufacturer service information.
> - Clean the area around the EGR differential pressure sensor.
>
> ### Remove
>
> Disconnect the engine harness connector from the EGR differential pressure sensor.
>
> Remove the two capscrews from the base of the sensor and remove the sensor from the engine.
>
> ### Clean and Inspect for Reuse
>
> **WARNING · Опасно**
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.
>
> Clean the EGR differential pressure sensor and adapter mounting surfaces. Remove any dirt buildup or soot residue.
>
> If the EGR differential pressure sensor has frozen, defrost the sensor using warm air that is below 60°C \[ 140°F \].
>
> Dry with compressed air.
>
> Inspect the EGR differential pressure sensor bracket for cracks or fretting. If damage is present, the sensor **must** be replaced. The bracket is **not** a serviceable component.
>
> Inspect the o-rings for cracks or other damage.
>
> Replace the o-rings if cracks or other damage is found.
>
> ### Install
>
> Make sure that the o-rings are seated and place the EGR differential pressure sensor onto the venturi tube.
>
> Tighten the capscrews.
>
> **Момент затяжки · Torque Value**
> 8 n•m [71 in-lb]
>
> Connect the wiring harness to the sensor (1).
>
> ### Finishing Steps
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Connect the batteries. See equipment manufacturer service information.
> - Use the recommended Cummins® electronic service tool, or equivalent, to reset the fuel tables if EGR differential pressure sensor is replaced. Refer to Procedure 005-263 in Section 5.
> - Operate the engine. Check for leaks.
