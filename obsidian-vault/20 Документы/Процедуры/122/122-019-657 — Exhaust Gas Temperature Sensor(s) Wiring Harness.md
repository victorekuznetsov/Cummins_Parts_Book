---
aliases:
  - "Жгут проводов датчиков температуры ОГ"
type: "Процедура"
doc: "122-019-657"
title_en: "Exhaust Gas Temperature Sensor(s) Wiring Harness"
title_ru: "Жгут проводов датчиков температуры ОГ"
modified: "2017-01-23"
engines:
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50"
manuals:
  - "4022102"
figures: 10
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-019-657.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-019-657.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
  - "перевод/машинный"
---

# Exhaust Gas Temperature Sensor(s) Wiring Harness
**Жгут проводов датчиков температуры ОГ**

> [!abstract] Процедура · `122-019-657`
> **Двигатели:** [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2017-01-23
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-019-657.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-019-657.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Датчик температуры выхлопных газов расположен на соединении выхлопного коллектора рядом с головкой цилиндра.

Температура измеряется непосредственно модулем управления двигателем (ECM). Этот двигатель использует терморезистор для измерения температуры и не требует коробки преобразователя сигнала, как в предыдущих моделях.

Существует два типа топливных форсунок и датчиков температуры выхлопных газов. В зависимости от того, какая проводка используется, маршрутизация датчика температуры выхлопных газов отличается. Смотрите следующую процедуру, чтобы определить, какая проводка упряжка установлена. См. процедуру 019-043 в разделе 19.

![[19601595.png]]

Некоторые двигатели выполнены с топливными рельсовыми кронштейнами (1) на крышке рычага качения клапанного клапана.

![[19e02077.png]]

### Подготовительные операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Отсоедините аккумуляторные батареи. См. сервисную документацию изготовителя оборудования.
- Удалите датчик температуры выхлопных газов. См. процедуру 019-013 в разделе 19.

### Снятие

Без топливных рельсовых кронштейнов

Удалите зажимные болты (1).

![[19e02078.png]]

Сквозь топливный рельс

Удалите зажимные болты (1).

![[19e02079.png]]

### Установка

Без топливных рельсовых кронштейнов

Для двигателей с низкотемпературными афтеркулерными (LTA) трубками:

- Маршрутизация всех кабелей датчика температуры выхлопных газов между двумя трубками LTA.

![[19e02080.png]]

Для двигателей с турбокомпрессорными шлангами охлаждающей жидкости:

- Прокладывайте кабели датчика температуры выхлопных газов под шлангом охлаждающей жидкости.

![[19e02081.png]]

Маршрутизатор датчика температуры выхлопных газов проводкой упряжки **по часовой стрелке** вокруг форсунки.

Установите P-зажимы на крышку рычага клапанного клапана.

> [!tip] Момент затяжки
> 18 Н·м [159 фунт-дюйм]

![[19e02078.png]]

Сквозь топливный рельс

Для двигателей с LTA-трубками:

- Маршрутизация всех кабелей датчика температуры выхлопных газов между двумя трубками LTA.

![[19e02080.png]]

Для двигателей с турбокомпрессорными шлангами охлаждающей жидкости:

- Прокладывайте кабели датчика температуры выхлопных газов под шлангом охлаждающей жидкости.

![[19e02081.png]]

Маршрутизатор датчика температуры выхлопных газов проводкой упряжки **по часовой стрелке** вокруг форсунки.

Установите P-зажимы на крышку рычага качения клапанного клапана и боковую сторону топливной рельсовой кронштейн.

> [!tip] Момент затяжки
> 18 Н·м [159 фунт-дюйм]

![[19e02079.png]]

### Завершающие операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Установите датчик температуры выхлопных газов. См. процедуру 019-013 в разделе 19.
- Подсоедините аккумуляторные батареи. См. сервисную документацию изготовителя оборудования.


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The exhaust gas temperature sensor is located on the exhaust manifold connection next to the cylinder head.
>
> The temperatures are measured directly by the engine control module (ECM). This engine uses a thermistor to measure the temperature and does **not** require the signal converter box, as in earlier models.
>
> There are two types of injector and exhaust gas temperature sensor harnesses available. Depending on which harness is used, the routing of the exhaust gas temperature sensor wiring harness is different. See the following procedure to identify which harness is fitted. Refer to Procedure 019-043 in Section 19.
>
> Some engines are configured with fuel rail brackets (1) on the rocker lever cover.
>
> ### Preparatory Steps
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Disconnect the batteries. See equipment manufacturer service information.
> - Remove the exhaust temperature sensor. Refer to Procedure 019-013 in Section 19.
>
> ### Remove
>
> Without Fuel Rail Bracket
>
> Remove the wire clamp capscrews (1).
>
> With Fuel Rail Bracket
>
> Remove the wire clamp capscrews (1).
>
> ### Install
>
> Without Fuel Rail Bracket
>
> For engines with low temperature aftercooler (LTA) tubes:
>
> - Route all exhaust gas temperature sensor cables between the two LTA tubes.
>
> For engines with turbocharger coolant hoses:
>
> - Route the exhaust gas temperature sensor cables under the coolant hose.
>
> Route the exhaust gas temperature sensor harness **clockwise** around the injector.
>
> Install the P-clips onto the rocker lever cover.
>
> **Момент затяжки · Torque Value**
> 18 n•m [159 in-lb]
>
> With Fuel Rail Bracket
>
> For engines with LTA tubes:
>
> - Route all exhaust gas temperature sensor cables between the two LTA tubes.
>
> For engines with turbocharger coolant hoses:
>
> - Route the exhaust gas temperature sensor cables under the coolant hose.
>
> Route the exhaust gas temperature sensor harness **clockwise** around the injector.
>
> Install the P-clips onto the rocker lever cover and the side of the fuel rail bracket.
>
> **Момент затяжки · Torque Value**
> 18 n•m [159 in-lb]
>
> ### Finishing Steps
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Install the exhaust temperature sensor. Refer to Procedure 019-013 in Section 19.
> - Connect the batteries. See equipment manufacturer service information.
