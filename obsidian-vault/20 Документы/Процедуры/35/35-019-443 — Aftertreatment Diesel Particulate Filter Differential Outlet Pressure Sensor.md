---
type: "Процедура"
doc: "35-019-443"
title_en: "Aftertreatment Diesel Particulate Filter Differential/Outlet Pressure Sensor"
modified: "2022-11-14"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
figures: 15
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-019-443.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-019-443.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/35"
  - "перевод/машинный"
---

# Aftertreatment Diesel Particulate Filter Differential/Outlet Pressure Sensor

> [!abstract] Процедура · `35-019-443`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 19 - Electronic Controls - Group 19
> **Даты:** изменён 2022-11-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-019-443.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-019-443.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Датчик дифференциального давления дизельного фильтра твердых частиц (DPF) после обработки представляет собой комбинированный датчик, который контролирует дифференциальное давление по DPF, а также давление на выходе DPF.

Датчик дифференциального давления дизельного фильтра твердых частиц после обработки расположен на фильтре твердых частиц дизельного топлива после обработки.

![[nobox.png]]

### Первичная проверка

Используйте электронный сервисный инструмент для мониторинга значения датчика дифференциального давления фильтра дизеля после обработки с помощью ключа в положении ON и выключенного двигателя.

Значение дифференциального давления фильтра твердых частиц дизельного топлива после обработки должно соответствовать следующей спецификации с ключом в положении Включения и выключенным двигателем.

| Дизельный фильтр Дифференциальное давление Дизельный фильтр Дифференциальное давление |  |  |
|---|---|---|
| каша |  | в хг |
| 0 ± 3 | НМ | 0 ± 0.89 |

Значение датчика давления на выходе дизельного фильтра твердых частиц после обработки должно соответствовать следующей спецификации с ключом в положении Включения и выключенным двигателем.

| После обработки дизельного фильтра твердых частиц давление в розетке |  |  |
|---|---|---|
| каша |  | в хг |
| 0 ± 3 | НМ | 0 ± 0.89 |

Если любое значение выходит за пределы указанных пределов, проверьте после обработки дизельные фильтры с твердыми частицами на наличие дифференциального давления в трубах для блокировки.

Если трубки дифференциального давления дизельного фильтра твердых частиц после обработки блокируются **не**, и если показания датчика выходят за пределы указанных пределов, замените датчик дифференциального давления дизельного фильтра твердых частиц после обработки.

Значение датчика давления на выходе дизельного фильтра твердых частиц после обработки должно соответствовать следующей спецификации с ключом в положении Включения и выключенным двигателем.

| После обработки дизельного фильтра твердых частиц напряжение датчика давления (VDC) |  |
|---|---|
| Минь | Макс |
| 0.5 | 4.5 |

Заменить датчик дифференциального давления фильтра твердых частиц дизельного топлива после обработки, если зарегистрированное напряжение **не** попадает в заданный диапазон напряжения.

![[19804012.png]]

### Подготовительные операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Отсоедините аккумуляторные батареи. См. сервисное руководство изготовителя машины.

![[ck800wa.png]]

### Снятие

Если оборудован дистанционно установленным датчиком перепада давления DPF после обработки:

- Удалите болты, которые обеспечивают изоляционную коробку датчика дифференциального давления DPF после обработки
- Скользите изоляционную коробку датчика дифференциального давления DPF после обработки вниз по трубкам датчика дифференциального давления DPF после обработки.

![[11d00873.png]]

Удалите быстроразъемные фитинги датчиков дифференциального давления из датчика дифференциального давления после обработки, нажав в запирающих тангах на быстроразъемную фитингу.

![[11d00874.png]]

Если оснащены DPF, установленным после обработки DPF датчиком дифференциального давления:

- Отсоедините разъем датчика от проводной упряжки
- Удалите крепежные болты.

![[19c01638.png]]

Если оборудован дистанционно установленным датчиком перепада давления DPF после обработки:

- В зависимости от установки OEM может быть проще получить доступ к датчику дифференциального давления DPF после обработки, если убрать изоляционную раму изоляционного датчика DPF после обработки.
- Удалите крепежи, которые обеспечивают защиту после обработки DPF дифференциального датчика давления изоляционной коробки. См. сервисное руководство изготовителя машины.

![[11d00875.png]]

Отсоедините разъем датчика от проводной упряжки.

Удалите болты, которые обеспечивают защиту датчика дифференциального давления DPF после обработки.

![[11d00876.png]]

### Очистка и проверка при повторном использовании

Осмотрите внутреннюю часть соединений трубки на датчике для закупорки или накопления сажи. Если наблюдается закупорка или накопление сажи, то после обработки дизельными фильтрами твердых частиц трубы дифференциального давления должны быть очищены.

Осмотрите разъём и датчик для проводов двигателя для следующего:

- Разбитая или разбитая соединительная оболочка
- Пропавшие или поврежденные соединительные уплотнения
- Грязь, мусор или влага в или на контактах разъема
- Коррозийные, согнутые, сломанные, отодвинутые назад или расширенные булавки
- Измельченный, треснувший, экструдированный или поврежденный датчик.

Ремонт или замена деталей по мере необходимости.

![[19c01639.png]]

Если он оснащен дистанционно установленным датчиком перепада давления DPF после обработки, проверьте изоляционную коробку и клетку датчика перепада давления DPF после обработки на предмет повреждения. Заменить, если обнаружен ущерб.

![[11d00877.png]]

### Установка

Если он оснащен DPF, установленным датчиком перепада давления DPF после обработки, установите датчик перепада давления DPF после обработки на крепежную скобу.

Установите и затяните крепежные болты.

> [!tip] Момент затяжки
> 14 Н·м [124 фунт-дюйм]

Подключите электропроводку к датчику перепада давления DPF после обработки.

![[19c01638.png]]

Если оснащен дистанционно установленным датчиком перепада давления DPF после обработки, а если удален, то установите на шасси изоляционную коробку с изоляционным фильтром дифференцированного давления дизельного фильтра после обработки. См. сервисное руководство изготовителя машины.

Установите датчик дифференциального давления дизельного фильтра твердых частиц на крепежную кронштейн. Установите и затяните крепежные болты.

> [!tip] Момент затяжки
> 14 Н·м [124 фунт-дюйм]

Подключите электропроводку к датчику перепада давления DPF после обработки.

![[11d00876.png]]

Установите быстрое отсоединяющее оборудование датчиков дифференциального давления на датчик дифференциального давления после обработки.

![[11d00874.png]]

Скользите с изоляционного блока датчика дифференциального давления DPF после обработки в трубки датчика дифференциального давления DPF после обработки.

Установите болты, которые обеспечивают изоляционную коробку датчика дифференциального давления DPF после обработки.

> [!tip] Момент затяжки
> 14 Н·м [124 фунт-дюйм]

![[11d00873.png]]

### Завершающие операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Подсоедините аккумуляторные батареи. См. сервисное руководство изготовителя машины.
- Запустите двигатель и проверьте на отсутствие утечек.

![[ck800wa.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The aftertreatment diesel particulate filter (DPF) differential pressure sensor is a combination sensor that monitors the differential pressure across the DPF, as well as the pressure at the outlet of the DPF.
>
> The aftertreatment diesel particulate filter differential pressure sensor is located on the aftertreatment diesel particulate filter.
>
> ### Initial Check
>
> Use an electronic service tool to monitor the value of the aftertreatment diesel particulate filter differential pressure sensor with the key in the ON position and the engine off.
>
> The value of the aftertreatment diesel particulate filter differential pressure should meet the following specification with the key in the ON position and the engine off.
>
> | Aftertreatment Diesel Particulate Filter Differential Pressure |  |  |
> |---|---|---|
> | kpa |  | in-hg |
> | 0 ± 3 | NOM | 0 ± 0.89 |
>
> The value of the aftertreatment diesel particulate filter outlet pressure sensor should meet the following specification with the key in the ON position and the engine off.
>
> | Aftertreatment Diesel Particulate Filter Outlet Pressure |  |  |
> |---|---|---|
> | kpa |  | in-hg |
> | 0 ± 3 | NOM | 0 ± 0.89 |
>
> If either value is out of specification, inspect the aftertreatment diesel particulate filter differential pressure tubes for blockage.
>
> If the aftertreatment diesel particulate filter differential pressure tubes are **not** blocked, and if either sensor reading is out of specification, replace the aftertreatment diesel particulate filter differential pressure sensor.
>
> The value of the aftertreatment diesel particulate filter outlet pressure sensor **must** meet the following specification with the key in the ON position and the engine off.
>
> | Aftertreatment Diesel Particulate Filter Outlet Pressure Sensor Voltage (VDC) |  |
> |---|---|
> | Min | Max |
> | 0.5 | 4.5 |
>
> Replace the aftertreatment diesel particulate filter differential pressure sensor if the voltage recorded does **not** fall within the specified voltage range.
>
> ### Preparatory Steps
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Disconnect the batteries. Refer to the OEM service manual.
>
> ### Remove
>
> If equipped with a remote mounted aftertreatment DPF differential pressure sensor:
>
> - Remove the capscrews that secure the aftertreatment DPF differential pressure sensor insulation box
> - Slide the aftertreatment DPF differential pressure sensor insulation box down the aftertreatment DPF differential pressure sensor tubes.
>
> Remove the quick disconnect fittings of the differential pressure sensor tubes from the aftertreatment differential pressure sensor by pressing in the locking tangs on the quick disconnect fitting.
>
> If equipped with a DPF mounted aftertreatment DPF differential pressure sensor:
>
> - Disconnect the sensor connector from the wiring harness
> - Remove the mounting capscrew.
>
> If equipped with a remote mounted aftertreatment DPF differential pressure sensor:
>
> - Depending on the OEM installation it may be easier to access the aftertreatment DPF differential pressure sensor if the aftertreatment DPF differential pressure sensor insulation box frame is removed.
> - Remove the fasteners that secure the aftertreatment DPF differential pressure sensor insulation box frame. Refer to the OEM service manual.
>
> Disconnect the sensor connector from the wiring harness.
>
> Remove the capscrews that secure the aftertreatment DPF differential pressure sensor.
>
> ### Clean and Inspect for Reuse
>
> Inspect the inside of the tube connections on the sensor for plugging or soot accumulation. If plugging or soot accumulation is observed, the aftertreatment diesel particulate filter differential pressure tubes **must** be cleaned.
>
> Inspect the engine harness connector and sensor for the following:
>
> - Cracked or broken connector shell
> - Missing or damaged connector seals
> - Dirt, debris, or moisture in or on the connector pins
> - Corroded, bent, broken, pushed back, or expanded pins
> - Chipped, cracked, extruded, or damaged sensor.
>
> Repair or replace parts as necessary.
>
> If equipped with a remote mounted aftertreatment DPF differential pressure sensor, inspect the aftertreatment DPF differential pressure sensor insulation box and cage for damage. Replace if damage is found.
>
> ### Install
>
> If equipped with a DPF mounted aftertreatment DPF differential pressure sensor, install the aftertreatment DPF differential pressure sensor onto the mounting bracket.
>
> Install and tighten the mounting capscrew.
>
> **Момент затяжки · Torque Value**
> 14 n•m [124 in-lb]
>
> Connect the wiring harness to the aftertreatment DPF differential pressure sensor.
>
> If equipped with a remote mounted aftertreatment DPF differential pressure sensor, and if removed install the aftertreatment diesel particulate filter differential pressure sensor insulation box cage onto the chassis. Refer to the OEM service manual.
>
> Install the aftertreatment diesel particulate filter differential pressure sensor onto the mounting bracket. Install and tighten the mounting capscrews.
>
> **Момент затяжки · Torque Value**
> 14 n•m [124 in-lb]
>
> Connect the wiring harness to the aftertreatment DPF differential pressure sensor.
>
> Install the quick disconnect fittings of the differential pressure sensor tubes to the aftertreatment differential pressure sensor.
>
> Slide the aftertreatment DPF differential pressure sensor insulation box up the aftertreatment DPF differential pressure sensor tubes.
>
> Install the capscrews that secure the aftertreatment DPF differential pressure sensor insulation box.
>
> **Момент затяжки · Torque Value**
> 14 n•m [124 in-lb]
>
> ### Finishing Steps
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Connect the batteries. Refer to the OEM service manual.
> - Operate the engine and check for leaks.
