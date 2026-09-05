---
type: "Процедура"
doc: "300-015-093"
title_en: "Engine Interface Wiring Harness"
modified: "2019-07-17"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "4332828"
figures: 4
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-015-093.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-015-093.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/300"
  - "перевод/машинный"
---

# Engine Interface Wiring Harness

> [!abstract] Процедура · `300-015-093`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[4332828 — Marine C Command HD Elite™ Panel System Master Repair Manual|4332828]]
> **Секции:** Section 15 - Instruments and Controls - Group 15
> **Даты:** изменён 2019-07-17
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-015-093.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-015-093.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Выбор сервисного инструмента

#### Рекомендованный сервисный инструмент Cummins®

- Электрический испытательный щуп, номер детали 3823993
- Электрический испытательный щуп, номер детали 3824811
- Электрический испытательный щуп, номер детали 3823995.

#### Дополнительные сервисные позиции

- Никаких дополнительных предметов обслуживания не требуется.

### Общие сведения

Связь проводов интерфейса двигателя соединяет окно интерфейса клиента (C.I.B.) с модулем управления двигателем (ECM) оригинального производителя оборудования (OEM) интерфейсного соединения.

> [!note] Примечание
> Основная цель этой проводов заключается в обеспечении длины, необходимой для подключения компонентов и интерфейса с двигателем ECM. Используйте схему проводов для деталей.

![[00e00101.png]]

### Проверка

Используйте следующую процедуру для подробных диаграмм компонентов.[[513-208-002 — Component Diagrams|См. процедуру 208-002 в разделе E.]]

Используйте схему проводов, если это необходимо.

Проверьте электропроводку для подключения и повреждения. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter|См. процедуру 019-360 в разделе 19.]]

Используйте приведенный выше раздел «Выбрать инструменты обслуживания» для информации о тестировании.

Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection|См. процедуру 019-361 в разделе 19.]]

![[3164133.png]]

### Подготовительные операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Отсоедините аккумуляторные батареи. См. сервисную документацию изготовителя оборудования.

### Снятие

Отсоедините проводку интерфейса двигателя от двигателя и C.I.B.. При необходимости ремонта удалите проводку упряжки.

Обратите внимание на маршрутизацию и расположение точек монтажа жгута проводов для установки.

![[19c91598.png]]

### Установка

Подключите ремень проводов интерфейса двигателя к двигателю и C.I.B..

Маршрут и охраняйте электропроводку до точек монтажа, отмеченных во время удаления.

![[19c91598.png]]

### Завершающие операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Подсоедините аккумуляторные батареи. См. сервисную документацию изготовителя оборудования.
- Проведите системный тест для проверки правильности работы.[[513-015-047 — Final Verification|См. процедуру 015-047 в разделе 15.]]


> [!quote]- Original (English) · английский оригинал
> ### Select Service Tools
>
> #### Recommended Cummins® Service Tools
>
> - Electrical test lead, Part Number 3823993
> - Electrical test lead, Part Number 3824811
> - Electrical test lead, Part Number 3823995.
>
> #### Additional Service Items
>
> - No additional service items required.
>
> ### General Information
>
> The engine interface wiring harness connects the customer interface box (C.I.B.) to the engine control module (ECM) original equipment manufacturer (OEM) interface connection.
>
> **Note · Примечание**
> The primary purpose of this harness is to provide the length necessary to connect the components and interface with the engine ECM. Use the wiring diagram for details.
>
> ### Test
>
> Use the following procedure for detailed component diagrams. [[513-208-002 — Component Diagrams|Refer to Procedure 208-002 in Section E.]]
>
> Use the wiring diagram, if necessary.
>
> Check the harness for connectivity and damage. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter|Refer to Procedure 019-360 in Section 19.]]
>
> Use the above Select Service Tools section for test lead information.
>
> Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection|Refer to Procedure 019-361 in Section 19.]]
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
> Disconnect the engine interface wiring harness from the engine and the C.I.B.. If necessary for repair, remove the harness.
>
> Note the harness routing and location of harness mounting points for installation.
>
> ### Install
>
> Connect the engine interface wiring harness to the engine and C.I.B..
>
> Route and secure the harness to mounting points noted during removal.
>
> ### Finishing Steps
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Connect the batteries. See equipment manufacturer service information.
> - Perform system test to verify proper function. [[513-015-047 — Final Verification|Refer to Procedure 015-047 in Section 15.]]
