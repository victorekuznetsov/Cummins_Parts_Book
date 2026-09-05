---
aliases:
  - "Регулировка клапанного механизма"
type: "Процедура"
doc: "1016-003-004-tr"
title_en: "Overhead Set"
title_ru: "Регулировка клапанного механизма"
modified: "2025-02-13"
engines:
  - "77804810"
families:
  - "15N"
manuals:
  - "5659763"
figures: 12
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/1016/1016-003-004-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/1016-003-004-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/15N"
  - "перевод/машинный"
---

# Overhead Set
**Регулировка клапанного механизма**

> [!abstract] Процедура · `1016-003-004-tr`
> **Двигатели:** [[77804810 — 15N CM2380 M104B CPL 5977|77804810]]
> **Семейство:** 15N
> **Входит в руководства:** [[5659763 — 15N CM2380 M104B Service Manual|5659763]]
> **Секции:** Section 3 - Rocker Levers - Group 03
> **Даты:** изменён 2025-02-13
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/1016/1016-003-004-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/1016-003-004-tr.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Выбор сервисного инструмента

#### Рекомендованный сервисный инструмент Cummins®

- Инструмент для заграждения двигателя, номер детали 4919092
- Запирающий штифт коленчатого вала, номер детали 5572844

#### Дополнительные сервисные позиции

- Измеритель щупальца с локтем.

### Общие сведения

Накладные настройки должны выполняться с интервалом, указанным в руководстве по эксплуатации и техническому обслуживанию, руководстве по эксплуатации, или когда ремонт двигателя вызывает удаление рычагов качения и/или ослабление регулирующих винтов.

Тормоза спроектированы как интегрированные рычаги коромысла с выхлопными.

Чрезмерная ресница клапана до этого может указывать на накладные расходы, неправильно установленные в результате предыдущего ремонта, изношенные стебли клапана, клапанные мосты, распределительный вал или рычаги коромысла.

[[1016-002-004 — Cylinder Head|См. процедуру 002-004 в разделе 2.]]См. процедуру 003-009 в разделе 3.

![[03r00062.png]]

### Подготовительные операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Отсоедините аккумуляторные батареи. См. сервисную документацию изготовителя оборудования.
- Снимите крышку коромысел.[[1016-003-011-tr — Rocker Lever Cover|См. процедуру 003-011 в разделе 3.]]

### Осмотр

Кольца должны быть правильно сидены на каждом стебле клапана. Визуально осмотрите кольты каждого клапана перед установкой клапанного моста или регулировкой накладных расходов.

Если нужно, подстройте коллет.[[1016-002-004 — Cylinder Head|См. процедуру 002-004 в разделе 2.]]

![[03r00092.png]]

Карман клапанного мостика **должен** располагаться над стеблем клапана. Визуально осмотрите клапанный мост, чтобы убедиться, что он правильно установлен.

![[03r00093.png]]

### Измерение

Следуйте разделу «Настройка» в этой процедуре, чтобы найти правильный цилиндр для измерения ресницы клапана.

Используйте набор датчиков щупальца для измерения количества зазора (режущего) между клапанным мостом и клапанной качалкой для подмышки.

Измерить и зафиксировать впускной и выпускной клапаны ресницы. Если ресница клапана **не** в пределах спецификаций, перечисленных ниже, клапан должен быть отрегулирован. Смотрите раздел «Регулировка» в этой процедуре.

| Лимиты проверки Lash |  |  |  |
|---|---|---|---|
|  | мм |  | в |
| принимать | 0.30 | Мин | 0.012 |
|  | 0.50 | Макс | 0.020 |
| выхлоп | 0.65 | Мин | 0.026 |
|  | 0.96 | Макс | 0.038 |

> [!note] Примечание
> Проверка накладных расходов обычно выполняется как часть процедуры устранения неполадок. Если измерение ресниц выходит за пределы указанных пределов, отрегулируйте ресницы в соответствии с номинальной спецификацией.

> [!note] Примечание
> Лимиты проверки стойки могут **не** использоваться в качестве обоснования для регулировки ресницы клапана или **не** при плановом обслуживании. Стрелка клапана должна быть сброшена к номинальному клапану, когда возникает интервал обслуживания.

### Регулировка

Все регулировки накладных расходов должны быть сделаны, когда двигатель холодный (любая стабилизированная температура охлаждающей жидкости при 60°C \[140°F \] или ниже).

![[03r00094.png]]

> [!danger] ОПАСНО
> Не тяните и не потянитесь на вентилятор, чтобы вручную вращать двигатель. Это может повредить лопасти вентилятора. Поврежденные лопасти вентилятора могут вызвать преждевременные сбои вентилятора, которые могут привести к серьезным травмам или имущественному ущербу.

Удалите запирающую вилку доступа к адаптеру с нижней части корпуса маховика.

![[03r00095.png]]

Цилиндры пронумерованы спереди двигателя (1-2-3-4-5-6).

Заказ на стрельбу двигателя составляет 1-5-3-6-2-4.

![[ew800va.png]]

Каждый цилиндр имеет два рычага коромысла:

- Рука качения клапана выхлопного клапана (с включенным тормозом двигателя, когда это применимо) (1)
- Впуск клапана клапана качели рычаг (2).

Рука качения выхлопного клапана всегда является самой короткой качкой клапана.

![[03r00096.png]]

> [!warning] ОСТОРОЖНО
> Стрелка впускного и выпускного клапанов должна устанавливаться с использованием индикаторов на шасси распределительного вала (задняя или передняя поверхность). Невыполнение этого требования может привести к повреждению двигателя.

На переднем конце распределительного вала имеется одно большее отверстие и шесть небольших отверстий (интервалы 60 градусов) для временного замка.

У шестерни Camshaft есть временные метки, которые видны сзади двигателя.

Найдите временные метки клапана на задней стороне распределительного механизма.

![[03r00105.png]]

Вращайте инструмент для блокировки двигателя, номер детали 4919092, в направлении вращения двигателя, **по часовой стрелке**. Выровнять временную метки 1 (нижний предел номера) на распределительной стойке с уплотнительным фланцем клапанного чехла.

Вставьте запирающий штифт коленчатого вала, номер детали 5572844, в небольшое отверстие, найденное на передней части распределительного вала, чтобы запереть распределительный вал. Распредвал будет заперт на месте, когда штифт будет правильно установлен.

На временной отметке 1, установите ресницу впускного и выпускного клапанов для цилиндра 1.

![[03s00124.png]]

> [!warning] ОСТОРОЖНО
> Повреждение двигателя может произойти, если ресница ходового клапана не соответствует спецификациям.

Ослабьте гайку на клапанном клапане, направляющем винт, и обратно отрегулирующем винт.

Вставьте калибр (1) для ощупывания между нижней частью электронной стопы и верхней частью клапанного мостика.

> [!note] Примечание
> Стрелка клапана должна быть сброшена до номинальных спецификаций, когда интервал технического обслуживания происходит для накладных расходов.

| Спецификации Lash Reset |  |  |  |
|---|---|---|---|
|  | мм |  | в |
| Стрелка клапана выхлопа | 0.90 | НМ | 0.035 |
| Впускная клапанная ресница | 0.45 | НМ | 0.018 |

> [!note] Примечание
> Для двигателей, оснащенных тормозами двигателя, будет существовать постоянный контакт между распределительным валом и выхлопным распределительным валом.

![[03r00100.png]]

Для регулирования ресницы клапана в впускном и выпускном клапанах используются следующие этапы:

1. Поверните регулировщик ресниц клапана **по часовой стрелке **до тех пор, пока не будет ощущаться контакт с датчиком измерения щупальца.
2. Вращайте клапанный регулировщик ресниц наполовину по стрелке **часовой стрелки**.
3. Удаляем ресничный регулировщик клапанов с половиной оборота.
4. Повторите шаги 2 и 3 четыре раза.
5. Затягивайте клапанный регулировщик ресниц до тех пор, пока контакт не будет ощущаться с помощью измерителя щупальца.

> [!note] Примечание
> **не** Применять крутящий момент к регулировщику ресниц клапана.

![[03r00101.png]]

Затянуть гайку регулировщика ресниц клапана, удерживающую регулировщик ресниц клапана.

> [!tip] Момент затяжки
> 28 Н·м [248 фунт-дюйм]

После подтяжки каштана до правильного значения крутящего момента, убедитесь, что датчик измерения щупальца будет скользить назад и вперед между клапанным мостом и рычагом качения клапанного клапана с **только **небольшим сопротивлением.

Удалите калибр для щупальца.

Удалите небольшой временной штифт блокировки, если он установлен.

![[03r00101.png]]

Повторите процесс для настройки всех рычагов коромысла в соответствии с графиком последовательности регулировки клапанного клапана ниже. **Всегда** начинайте с отметки 1 по времени и следуйте приказу об огне, описанному в графике.

Весь верхний блок должен быть сброшен каждый раз, когда любой накладной компонент удален.

| клапанный клапан коромысло рука Настройка последовательность |  |  |
|---|---|---|
| Camshaft Timing Mark | Установить номер выхлопа | Установить номер ввода |
| 1 | 1 | 1 |
| 5 | 5 | 5 |
| 3 | 3 | 3 |
| 6 | 6 | 6 |
| 2 | 2 | 2 |
| 4 | 4 | 4 |
| Огнестрельное предписание 1-5-3-6-2-4 |  |  |

### Завершающие операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Установите крышку коромысел.[[1016-003-011-tr — Rocker Lever Cover|См. процедуру 003-011 в разделе 3.]]
- Подсоедините аккумуляторные батареи. См. сервисную документацию изготовителя оборудования.
- Запустите двигатель и проверьте на отсутствие утечек.


> [!quote]- Original (English) · английский оригинал
> ### Select Service Tools
>
> #### Recommended Cummins® Service Tools
>
> - Engine barring tool, Part Number 4919092
> - Camshaft timing pin, Part Number 5572844
>
> #### Additional Service Items
>
> - Feeler gauge with elbow.
>
> ### General Information
>
> Overhead setting **must** be performed at the interval specified in the operation and maintenance manual, owners manual, or when engine repairs cause removal of the rocker levers and/or loosening of the adjusting screws.
>
> The brakes are designed as integrated rocker levers with the exhaust rockers.
>
> Excessive valve lash prior to this can indicate an overhead set incorrectly from a previous repair, worn valve stems, crossheads, camshaft, or rocker levers.
>
> [[1016-002-004 — Cylinder Head|Refer to Procedure 002-004 in Section 2.]] Refer to Procedure 003-009 in Section 3.
>
> ### Preparatory Steps
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Disconnect the batteries. See equipment manufacturer service information.
> - Remove the rocker lever cover. [[1016-003-011-tr — Rocker Lever Cover|Refer to Procedure 003-011 in Section 3.]]
>
> ### Inspect
>
> The collets **must** be seated properly on each valve stem. Visually inspect the collets of each valve before installing the crosshead or adjusting the overhead.
>
> If needed, adjust the collet. [[1016-002-004 — Cylinder Head|Refer to Procedure 002-004 in Section 2.]]
>
> The pocket of the crosshead **must** be seated over the valve stem. Visually inspect the crosshead to ensure it is properly installed.
>
> ### Measure
>
> Follow the Adjust section in this procedure to locate correct cylinder to measure valve lash.
>
> Use a set of feeler gauges to measure the amount of clearance (lash) between the crosshead and the rocker lever foot.
>
> Measure and record the intake and exhaust valve lash. If the valve lash is **not** within the specifications listed below, the valve **must** be adjusted. See the Adjust section in this procedure.
>
> | Lash Check Limits |  |  |  |
> |---|---|---|---|
> |  | mm |  | in |
> | Intake | 0.30 | MIN | 0.012 |
> |  | 0.50 | MAX | 0.020 |
> | Exhaust | 0.65 | MIN | 0.026 |
> |  | 0.96 | MAX | 0.038 |
>
> **Note · Примечание**
> Checking the overhead setting is usually performed as part of a troubleshooting procedure. If the lash measurement is out of specification, adjust the lash to the nominal specification.
>
> **Note · Примечание**
> Lash check limits can **not** be used as the justification to adjust valve lash or **not** in scheduled maintenance. The valve lash **must** be reset to nominal valve when maintenance interval occurs.
>
> ### Adjust
>
> All overhead adjustments **must** be made when the engine is cold (any stabilized coolant temperature at 60°C \[ 140°F \] or below).
>
> **WARNING · Опасно**
> Do not pull or pry on the fan to manually rotate the engine. To do so can damage the fan blades. Damaged fan blades can cause premature fan failures which can result in serious personal injury or property damage.
>
> Remove the barring adapter access plug from the bottom of the flywheel housing.
>
> The cylinders are numbered from the front of the engine (1-2-3-4-5-6).
>
> The engine firing order is 1-5-3-6-2-4.
>
> Each cylinder has two rocker levers:
>
> - Exhaust rocker lever (with engine brake integrated when applicable) (1)
> - Intake rocker lever (2).
>
> Exhaust rocker lever is **always** the shortest rocker lever.
>
> **CAUTION · Осторожно**
> Intake and exhaust valve lash must be set using the indicators on the camshaft gear (rear or front face). Failure to do so may result in engine damage.
>
> There are one bigger hole and six small holes (60 degree intervals) on the front end of camshaft for timing lock.
>
> Camshaft gear has timing marks which are visible from the rear of the engine.
>
> Locate the valve timing marks on the rear side of the camshaft gear.
>
> Rotate the engine barring tool, Part Number 4919092, in the direction of engine rotation, **clockwise**. Align the timing mark 1 (bottom of the number) on the camshaft gear with the valve cover sealing flange.
>
> Insert camshaft timing pin, Part Number 5572844, into the small hole found on the front of camshaft to lock the camshaft. The camshaft will be locked in place when the pin is properly in place.
>
> At timing mark 1, set the intake and exhaust valve lash for cylinder 1.
>
> **CAUTION · Осторожно**
> Engine damage can occur if the running valve lash is not within specifications.
>
> Loosen the locknut on the rocker lever adjusting screw, and back out the adjusting screw.
>
> Insert the feeler gauge (1) between the bottom of the e-foot and the top of the crosshead.
>
> **Note · Примечание**
> The valve lash **must** be reset to nominal specifications when maintenance interval occurs for overhead set.
>
> | Lash Reset Specifications |  |  |  |
> |---|---|---|---|
> |  | mm |  | in |
> | Exhaust valve lash | 0.90 | NOM | 0.035 |
> | Intake valve lash | 0.45 | NOM | 0.018 |
>
> **Note · Примечание**
> For engines equipped with engine brakes, constant contact will exist between the camshaft and the exhaust camshaft follower.
>
> To adjust the valve lash in the intake and exhaust valves, the following steps shall be used:
>
> 1. Rotate the valve lash adjuster **clockwise** until contact is felt with feeler gauge.
> 2. Rotate valve lash adjuster half a revolution **clockwise**.
> 3. Loosen valve lash adjuster half a revolution.
> 4. Repeat steps 2 and 3 four times.
> 5. Tighten valve lash adjuster until contact is felt with feeler gauge.
>
> **Note · Примечание**
> Do **not** apply torque to valve lash adjuster.
>
> Tighten the valve lash adjuster nut holding down the valve lash adjuster.
>
> **Момент затяжки · Torque Value**
> 28 n•m [248 in-lb]
>
> After tightening the locknut to the correct torque value, check to make sure the feeler gauge will slide backward and forward between the crosshead and the rocker lever with **only** a slight drag.
>
> Remove the feeler gauge.
>
> Remove the small timing locking pin if installed.
>
> Repeat process to adjust all rocker levers according to Rocker Lever Adjustment Sequence chart below. **Always** start at timing mark 1 and follow firing order described in chart.
>
> Entire overhead assembly **must** be reset every time any overhead component is removed.
>
> | Rocker Lever Adjustment Sequence |  |  |
> |---|---|---|
> | Camshaft Timing Mark | Set Exhaust Number | Set Intake Number |
> | 1 | 1 | 1 |
> | 5 | 5 | 5 |
> | 3 | 3 | 3 |
> | 6 | 6 | 6 |
> | 2 | 2 | 2 |
> | 4 | 4 | 4 |
> | Firing order 1-5-3-6-2-4 |  |  |
>
> ### Finishing Steps
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Install the rocker lever cover. [[1016-003-011-tr — Rocker Lever Cover|Refer to Procedure 003-011 in Section 3.]]
> - Connect the batteries. See equipment manufacturer service information.
> - Operate the engine and check for leaks.
