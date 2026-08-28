---
type: "Процедура"
doc: "1016-005-042"
title_en: "Fuel Regulator, NG"
modified: "2022-12-14"
engines:
  - "77804810"
families:
  - "15N"
manuals:
  - "5659763"
figures: 16
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/1016/1016-005-042.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/1016-005-042.pdf"
tags:
  - "документ/процедура"
  - "двигатель/15N"
  - "перевод/машинный"
---

# Fuel Regulator, NG

> [!abstract] Процедура · `1016-005-042`
> **Двигатели:** [[77804810 — 15N CM2380 M104B CPL 5977|77804810]]
> **Семейство:** 15N
> **Входит в руководства:** [[5659763 — 15N CM2380 M104B Service Manual|5659763]]
> **Секции:** Section 5 - Fuel System - Group 05
> **Даты:** изменён 2022-12-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/1016/1016-005-042.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/1016-005-042.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Выбор сервисного инструмента

#### Рекомендованный сервисный инструмент Cummins®

- Детектор газа, номер детали 3165179
- Цифровой мультиметр, часть 3400162
- Электрический испытательный щуп Kit, номер детали 5299367
- Адаптер для испытания на давление, номер детали 5394427

#### Дополнительные сервисные позиции

- 0 кПа [0 psi ] до 2068 кПа \[300 psi \] калибр давления.

### Общие сведения

Для двигателя сжиженного природного газа (СПГ) регулятор давления топлива интегрирован с запорным клапаном и клапаном сброса давления, а нижняя линия покрыта фильтром для вентиляции и для предотвращения попадания пыли, масла и т. Д., Войдя в пружинную камеру внутри регулятора давления.

![[05s00052.png]]

Для двигателя на сжатом природном газе (CNG) на этом продукте установлены два одинаковых регулятора давления топлива, установленных параллельно для расхода топлива (1). Каждый из них интегрирован с запорным клапаном, клапаном сброса давления и двумя портами охлаждающей жидкости (2). Эти два порта охлаждающей жидкости должны быть подключены к цепи охлаждения двигателя.

![[05s00073.png]]

### Первичная проверка

> [!danger] ОПАСНО
> Природный газ взрывоопасен и воспламеняется. Всегда следите за поддержанием адекватной вентиляции в рабочем помещении. Храните все сигареты, пламя, пилотные огни, дуговое оборудование и выключатели из рабочей зоны и областей с общей вентиляцией, чтобы уменьшить вероятность серьезных травм или смерти при работе на системе природного газа.

Переключатель зажигания включите в положение Включения.

Используйте детектор газа, номер детали 3165179, чтобы проверить разъем регулятора на утечку газа.

Проверьте регулятор, разъемы и газовые трубы, если утечка газа обнаружена из разъема регулятора.

![[05s00074.png]]

### Подготовительные операции

> [!danger] ОПАСНО
> Природный газ взрывоопасен и воспламеняется. Всегда следите за поддержанием адекватной вентиляции в рабочем помещении. Храните все сигареты, пламя, пилотные огни, дуговое оборудование и выключатели из рабочей зоны и областей с общей вентиляцией, чтобы уменьшить вероятность серьезных травм или смерти при работе на системе природного газа.

> [!danger] ОПАСНО
> Природный газ легче воздуха. Проверьте потолок в зоне, где должны быть выполнены работы для любого возможного источника зажигания.

> [!danger] ОПАСНО
> Всегда иметь правильную вентиляцию при работе на газотранспортной системе.

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

> [!warning] ОСТОРОЖНО
> Для уменьшения возможности ударной нагрузки компонентов ниже по потоку от клапана подачи необходимо медленно открывать и закрывать клапан подачи газа.

- Отсоедините аккумуляторные батареи. См. сервисную документацию изготовителя оборудования.
- Медленно закройте ручной клапан подачи газа. См. информацию об обслуживании производителя оборудования для определения местоположения клапана.
- Отсоедините проводную упряжку запорного клапана.

- Отключите трубопровод, подключенный к регулятору давления топлива. См. сервисную документацию изготовителя оборудования.

> [!note] Примечание
> Впускные и выпускные разъёмы на топливных регуляторах должны быть удерживаемы на месте с гаечным ключом при удалении газовой трубы из топливных регуляторов, чтобы предотвратить ослабление разъемов во время процесса удаления.

![[05s00075.png]]

### Снятие

Удалите клапанный узел регулятора давления топлива.

![[05s00056.png]]

### Очистка и проверка при повторном использовании

> [!danger] ОПАСНО
> При очистке растворителями, кислотами и щелочными составами соблюдайте указания их изготовителя. Работайте в защитных очках и защитной одежде, чтобы снизить риск травмы.

Очистите скобку и регулятор растворителем.

![[05s00057.png]]

Проверить регулятор и скобку на предмет повреждения или обломков.

Заменить регулятор, если обнаружен ущерб.

![[05s00058.png]]

### Проверка

Используйте цифровой мультиметрический комплект, номер 3400162 и электрический испытательный щуп, номер 5299367. Измерить сопротивление между подачей и возвратом штифтов на разъеме клапана отключения топлива.

| Сопротивление |  |  |
|---|---|---|
|  | Омс (для двигателей с СПГ) | Омс (для двигателей СПГ) |
| Мин | 21.6 | 46.8 |
| Макс | 26.4 | 57.2 |

Если сопротивление не соответствует спецификациям, замените запорный клапан.

![[05s00059.png]]

Измерьте сопротивление между контактом подачи и корпусом запорного клапана топлива.

| Сопротивление |  |
|---|---|
|  | Омс |
| Мин | 100кг |

![[05s00060.png]]

### Установка

Установите клапанный узел регулятора давления топлива.

Затягивайте крепежные болты. См. сервисную документацию изготовителя оборудования.

![[05s00056.png]]

Момент затяжки для гаек регулятору и момент затяжки для газовой трубы производителя оригинального оборудования (OEM) для локтя адаптера штыревого пола рекомендуется Cummins Inc. как ниже.

> [!tip] Момент затяжки
> Гайки на входе регулятора (1) 55 Н·м [41 фут-лб]

> [!tip] Момент затяжки
> Гайки к регуляторной розетке (2) и каждый порт на локте штуцера с наружной резьбой (3) 80 Н·м [59 футов-лб]

![[05s00076.png]]

### Завершающие операции

> [!danger] ОПАСНО
> Природный газ взрывоопасен и воспламеняется. Всегда следите за поддержанием адекватной вентиляции в рабочем помещении. Храните все сигареты, пламя, пилотные огни, дуговое оборудование и выключатели из рабочей зоны и областей с общей вентиляцией, чтобы уменьшить вероятность серьезных травм или смерти при работе на системе природного газа.

> [!danger] ОПАСНО
> Природный газ легче воздуха. Проверьте потолок в зоне, где должны быть выполнены работы для любого возможного источника зажигания.

> [!danger] ОПАСНО
> Всегда иметь правильную вентиляцию при работе на газотранспортной системе.

- Подключите трубопровод, подключенный к регулятору давления топлива. См. сервисную документацию изготовителя оборудования.

> [!note] Примечание
> Впускные и выпускные разъёмы на топливных регуляторах **должны** удерживаться на месте с гаечным ключом при затягивании фитинговых разъёмов для предотвращения перегерметизации в процессе установки.

![[05s00075.png]]

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

> [!warning] ОСТОРОЖНО
> Для уменьшения возможности ударной нагрузки компонентов ниже по потоку от клапана подачи необходимо медленно открывать и закрывать клапан подачи газа.

- Подключите проводную упряжку запорного клапана.
- Медленно откройте ручной клапан подачи газа. См. информацию об обслуживании производителя оборудования для определения местоположения клапана.
- Подсоедините аккумуляторные батареи. См. сервисную документацию изготовителя оборудования.
- Запустите двигатель и проверьте на отсутствие утечек.

### Испытание на давление топлива

> [!warning] ОСТОРОЖНО
> Перед удалением любого компонента топливной системы выключите подачу топлива на главном клапане отключения газа транспортного средства.

Выключите главный клапан отключения газа.

Работайте с двигателем на низком холостом ходу, пока двигатель не отключится.

Удалите линию подачи топлива от входа в топливный фильтр на двигателе.

Установите адаптер для испытания на давление, номер детали 5394427, на входе в топливный фильтр на двигателе. В двигателях, оснащенных воздушным компрессором, может потребоваться регулировать угол фитинга, чтобы обеспечить установку служебной оснастки.

Соедините топливные линии.

![[05s00062.png]]

Соедините калибр давления с диапазоном 0 кПа [0 psi ] до 2068 кПа [300 psi ] до крепления давления CompuchekTM.

Включите главный клапан отключения газа.

Используйте детектор газа, номер детали 3165179, чтобы проверить все фитинги на наличие утечек топлива.

![[05s00063.png]]

Подтвердить спецификацию топливных баков OEM на измерителе давления топлива.

Измерьте давление газа на входной стороне при работе двигателя при полной нагрузке и номинальных условиях оборота.

| Газовое давление (измерительный датчик) для двигателей СПГ |  |  |
|---|---|---|
| каша |  | пси |
| 600 | Мин | 87 |
| 1600 | Макс | 232 |

| Газовое давление (измерительный датчик) для двигателей с СПГ |  |  |
|---|---|---|
| каша |  | пси |
| 2000 | Мин | 290 |
| 22,000 | Макс | 3191 |

Если давление ниже или выше спецификаций, см. информацию об обслуживании производителя оборудования.

![[05s00077.png]]

Измерьте давление газа на стороне выхода при работе двигателя при полной нагрузке и номинальных условиях оборота.

| Давление газа (калибр) |  |  |
|---|---|---|
| каша |  | пси |
| 510 | Мин | 74 |
| 690 | Макс | 100 |

Если давление ниже или выше спецификаций, замените регулятор.

![[05s00064.png]]


> [!quote]- Original (English) · английский оригинал
> ### Select Service Tools
>
> #### Recommended Cummins® Service Tools
>
> - Gas detector, Part Number 3165179
> - Digital Multimeter Kit, Part Number 3400162
> - Electrical Test Lead Kit, Part Number 5299367
> - Pressure test adapter, Part Number 5394427
>
> #### Additional Service Items
>
> - 0 kPa \[ 0 psi \] to 2068 kPa \[ 300 psi \] pressure gauge.
>
> ### General Information
>
> For Liquefied Natural Gas (LNG) engine, the fuel pressure regulator is integrated with a shutoff valve and a pressure relief valve, and the bottom line is covered by a filter for venting and to avoid dust, oil, and so forth, entering the spring chamber inside the pressure regulator.
>
> For Compressed Natural Gas (CNG) engine, there are two same fuel pressure regulators on this product, installed in parallel for fuel flow (1). Each one is integrated with a shutoff valve, a pressure relief valve, and two coolant ports (2). These two coolant ports need to be connected to the engine cooling circuit.
>
> ### Initial Check
>
> **WARNING · Опасно**
> Natural gas is explosive and flammable. Always be sure to maintain adequate ventilation in the work area. Keep all cigarettes, flames, pilot lights, arcing equipment, and switches out of the work area and areas with shared ventilation to reduce the possibility of severe personal injury or death when working on a natural gas system.
>
> Turn the keyswitch to ON position.
>
> Use a gas detector, Part Number 3165179, to check the regulator connector for gas leak.
>
> Check the regulator, connectors, and gas pipes if gas leak is found from the regulator connector.
>
> ### Preparatory Steps
>
> **WARNING · Опасно**
> Natural gas is explosive and flammable. Always be sure to maintain adequate ventilation in the work area. Keep all cigarettes, flames, pilot lights, arcing equipment, and switches out of the work area and areas with shared ventilation to reduce the possibility of severe personal injury or death when working on a natural gas system.
>
> **WARNING · Опасно**
> Natural gas is lighter than air. Check the ceiling of the area where work is to be done for any possible ignition source.
>
> **WARNING · Опасно**
> Always have proper ventilation when working on a natural gas system.
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> **CAUTION · Осторожно**
> To reduce the possibility of shock loading of components downstream of the supply valve, opening and closing of the gas supply valve must be done slowly.
>
> - Disconnect the batteries. See equipment manufacturer service information.
> - Slowly close the manual gas supply valve. See equipment manufacturer service information for the location of the valve.
> - Disconnect the wiring harness of the shutoff valve.
>
> - Disconnect the piping connected to the fuel pressure regulator. See equipment manufacturer service information.
>
> **Note · Примечание**
> The fuel inlet and outlet connectors on fuel regulators **must** be held in place with a wrench when removing gas pipe from fuel regulators to prevent loosening the connectors during the removal process.
>
> ### Remove
>
> Remove the fuel pressure regulator valve assembly.
>
> ### Clean and Inspect for Reuse
>
> **WARNING · Опасно**
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.
>
> Clean the bracket and the regulator with solvent.
>
> Inspect the regulator and the bracket for damage or debris.
>
> Replace the regulator if damage is found.
>
> ### Test
>
> Use Digital Multimeter Kit, Part Number 3400162, and Electrical Test Lead Kit, Part Number 5299367. Measure the resistance between the supply and return pins at the fuel shutoff valve connector.
>
> | Resistance |  |  |
> |---|---|---|
> |  | Ohms (for CNG engines) | Ohms (for LNG engines) |
> | MIN | 21.6 | 46.8 |
> | MAX | 26.4 | 57.2 |
>
> If the resistance does **not** meet the specifications, replace the fuel shutoff valve.
>
> Measure the resistance between the supply pin and fuel shutoff valve body.
>
> | Resistance |  |
> |---|---|
> |  | Ohms |
> | MIN | 100k |
>
> ### Install
>
> Install the fuel pressure regulator valve assembly.
>
> Tighten the mounting capscrews. See equipment manufacturer service information.
>
> The torque value for the nuts to regulator and the torque value for the Original Equipment Manufacturer (OEM) gas pipe to male adapter elbow are recommended by Cummins Inc. as below.
>
> **Момент затяжки · Torque Value**
> Nuts to regulator inlet (1) 55 n•m [41 ft-lb]
>
> **Момент затяжки · Torque Value**
> Nuts to regulator outlet (2) and each port on male adapter elbow (3) 80 n•m [59 ft-lb]
>
> ### Finishing Steps
>
> **WARNING · Опасно**
> Natural gas is explosive and flammable. Always be sure to maintain adequate ventilation in the work area. Keep all cigarettes, flames, pilot lights, arcing equipment, and switches out of the work area and areas with shared ventilation to reduce the possibility of severe personal injury or death when working on a natural gas system.
>
> **WARNING · Опасно**
> Natural gas is lighter than air. Check the ceiling of the area where work is to be done for any possible ignition source.
>
> **WARNING · Опасно**
> Always have proper ventilation when working on a natural gas system.
>
> - Connect the piping connected to the fuel pressure regulator. See equipment manufacturer service information.
>
> **Note · Примечание**
> The fuel inlet and outlet connectors on fuel regulators **must** be held in place with a wrench when tightening the fitting connectors to prevent overtightening during the installation process.
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> **CAUTION · Осторожно**
> To reduce the possibility of shock loading of components downstream of the supply valve, opening and closing of the gas supply valve must be done slowly.
>
> - Connect the wiring harness of the shutoff valve.
> - Slowly open the manual gas supply valve. See equipment manufacturer service information for the location of the valve.
> - Connect the batteries. See equipment manufacturer service information.
> - Operate the engine and check for leaks.
>
> ### Fuel Pressure Test
>
> **CAUTION · Осторожно**
> Before removing any fuel system component, turn off the fuel supply at the vehicle's main gas shutoff valve.
>
> Turn off the vehicle's main gas shutoff valve.
>
> Operate the engine at low idle until the engine shuts down.
>
> Remove the fuel supply line from the inlet to the fuel filter on the engine.
>
> Install pressure test adapter, Part Number 5394427, at the inlet to the fuel filter on the engine. In engines that feature an air compressor, it may be necessary to adjust the angle of the fitting to allow installation of the service tool.
>
> Connect the fuel lines.
>
> Connect a pressure gauge with a 0 kPa \[ 0 psi \] to 2068 kPa \[ 300 psi \] range to the Compuchek™ pressure fitting.
>
> Turn on the vehicle's main gas shutoff valve.
>
> Use a gas detector, Part Number 3165179, to check all fittings for fuel leaks.
>
> Confirm the specification of the OEM fuel tanks at the fuel pressure gauge.
>
> Measure the gas pressure at the inlet side while operating the engine at full load and rated rpm conditions.
>
> | Gas Pressure (Gauge) for LNG Engines |  |  |
> |---|---|---|
> | kpa |  | psi |
> | 600 | MIN | 87 |
> | 1600 | MAX | 232 |
>
> | Gas Pressure (Gauge) for CNG Engines |  |  |
> |---|---|---|
> | kpa |  | psi |
> | 2000 | MIN | 290 |
> | 22,000 | MAX | 3191 |
>
> If the pressure is below or above specifications, see equipment manufacturer service information.
>
> Measure the gas pressure at the outlet side while operating the engine at full load and rated rpm conditions.
>
> | Gas Pressure (Gauge) |  |  |
> |---|---|---|
> | kpa |  | psi |
> | 510 | MIN | 74 |
> | 690 | MAX | 100 |
>
> If the pressure is below or above specifications, replace the regulator.
