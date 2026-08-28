---
type: "TSB"
doc: "tsb180136"
title_en: "Belt Shredding"
modified: "2018-12-05"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
parts:
  - "3009330"
  - "3026269"
  - "3036460"
  - "3093936"
  - "3093940"
  - "3104029"
  - "3681390"
  - "3681587"
  - "3902460"
  - "3903112"
  - "3914407"
  - "3935013"
figures: 6
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2018/tsb180136.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb180136.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QSX15"
  - "перевод/машинный"
---

# Belt Shredding

> [!abstract] TSB · `tsb180136`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Даты:** изменён 2018-12-05
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2018/tsb180136.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb180136.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Пояс Шреддинг

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### Содержание

**Затронутая продукция**

- QSX15 CM570

Варианты:

- FA1542
- FA1657

**Проблема**

Симптом:

- Прогрессивное измельчение пояса, вызванное прыжком пояса. См. рисунки 1 и 2 ниже.
- Измельчение пояса может привести к потере приводного ремня, что приведет к высоким температурам охлаждающей жидкости.

Первопричина:

- Высокий вентиляторный центр позволяет чрезмерное отклонение пояса между вентиляторным шкивом и коленчатым валом шкива.

![[16r00075.png]]

Рисунок 1 Пояс Шред показан над водяным насосом Пулли, с двумя левыми крайними ребрами.

![[16r00076.png]]

Рисунок 2, Снятый пояс с симптомом измельчения пояса - верхние ребра отсутствуют

**Описание изменения**

Новый 3-х холостый кронштейн для двигателей с особыми вентиляторными центрами (фан-приводы FA1542 и FA1657). 3-х шкивная кронштейна установлена на фан-бракет между шкивом вентилятора и коленчатым валом. См. рисунок 3 ниже.

![[16r00074.png]]

Рисунок 3. Обновленная компоновка диска с 3-idler кронштейном

**Проверка**

Верификатор двигателя был построен на FA1542 или FA1657.

Осмотрите ремень для измельчения или отсутствия ребер снаружи или внутри ремня перед удалением из двигателя.

Сравните ремень с рисунком 1 и рисунком 2 выше, чтобы подтвердить режим неисправности.

**Решение**

- Если опция вентилятора и режим неисправности соответствуют проверке, должна быть установлена 3-х холостая кронштейн.
- Двигатели с FA1542 должны иметь больший натяжитель ремня охлаждения, установленный на низком креплении двигателя, и шкив холостого хода, добавленный к центру привода.
- Двигатели с FA1657 уже будут иметь этот охлаждающий натяжитель ремня вентилятора и шкив холостого хода. В приведенной ниже информации показаны детали и инструкции по установке новых деталей для FA1542 и FA1657 в отдельных разделах. Проверьте, какой привод установлен на двигателе, и справьте правильные инструкции.
- До начала испытаний двигатели, построенные с использованием FA1542, не были обновлены до FA1657 в соответствии с [[tsb120285 — Belt Shredding on QSX15 CM570 With Fan Centers 18” and Above\|TSB120285]].

**Указания по обслуживанию**

См. QSX15 CM570 Service Manual, Bulletin number [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]].

**Инструкции по установке двигателей с FA1542**

Проверьте, что двигатель в настоящее время установлен на FA1542. См. рисунок 1 ниже. Натяжитель ремня охлаждения вентилятора будет установлен в середине привода, непосредственно над коленчатым валом.

![[16r00072.png]]

Рисунок 4, FA1542 Drive Layout.

Удаление компонентов FA1542:

- Удалите ремень привода вентилятора, натяжитель ремня охлаждения ремня вентилятора и поддержку натяжителя ремня охлаждения от кронштейна вентилятора.

![[08000055.png]]

Рисунок 5, болты водяного насоса должны быть сняты

Установка охлаждающего натяжителя ремня вентилятора и шкива холостого хода:

- Установите кронштейн натяжителя ремня охлаждения ремня, номер детали 3681191. Используйте болты, удаленные из водяного насоса. 1 - это номер детали[[3681390]]и болты 2 и 3 являются номером части[[3093936]]. 1 требуется шайба Часть Номер[[3036460]]и болты 3 требуют номер детали шайбы[[3009330]].
- Установите адаптеры часть номера[[3681587]], используя штифт-пальто номер 70760, и шкив-пальто номер[[3681587]].
- Установите низконапорный большой натяжитель ремня охлаждения Часть Номер[[3104029]].

Установка плотной боковой кронштейнной сборки и ремня привода вентилятора:

- Удалите скобки поддержки вентилятора (лестничная скобка).
- Установите брекет шкивов для холостого хода Часть Номер 5575127 в брекет поддержки вентилятора. Нижнее отверстие скобки шкива холостого хода должно выровняться с нижним правым отверстием скобки поддержки вентилятора. См. рисунок 3. Используйте хекс-гайку Часть Номер 3035803 и болты Часть Номер[[3093940]].
- Установите подложку для вентиляторов.
- Установите шкив idler Part Number[[3681587]]Для скобки шкивов для холостого хода часть 5575127. Используйте болты Part Number[[3903112]]и номер детали шайбы[[3026269]].
- Установить пылевой экран Part Number[[3935013]]Щит бездельника, нажимая на внешний диаметр щита, чтобы предотвратить повреждение пылевого щита.
- Установите ремень привода вентилятора, номер детали 3103848.

**Инструкции по установке двигателей с FA1657**

- Верификатор двигателя имеет опцию FA1657. См. рисунок 6 ниже.
- Напряжение будет установлено на низком креплении двигателя, и будет шкив холостого хода непосредственно над шкивом коленчатого вала. Также будет установлена узкая боковая шкивная панель.

![[16r00073.png]]

Рисунок 6, FA1657 Drive Layout.

Удаление компонентов FA1657

- Удалите ремень вентилятора.
- Удалите скобки поддержки вентилятора (лестничная скобка).
- Снимите плотную боковую кронштейну бездельника, которая прикреплена к кронштейну поддержки вентилятора с двумя болтами.

Установка плотной боковой кронштейнной сборки и ремня привода вентилятора:

- Установите брекет-ножку шкива для холостого хода Номер детали 5575127 в брекет-поддержку вентилятора (удаленный на предыдущем шаге). Нижнее отверстие скобки шкива холостого хода должно выстраиваться в линию с нижним правым отверстием скобки поддержки вентилятора. См. рисунок 3. Используйте хекс-гайку Часть Номер 3035803 и болты Часть Номер[[3093940]].
- Установите фан-брекет.
- Установите шкив idler Part Number[[3681587]]Для ленивца брекет-партия № 5575127. Используйте capscrePart 3[[3903112]]и номер детали3[[3026269]].
- Установить пылевой экран Part Number[[3935013]]Щит бездельника, нажимая на внешний диаметр щита, чтобы предотвратить повреждение пылевого щита.
- Установите ремень привода вентилятора, номер детали 3103848.

**Услуги**

Сервисные детали доступны для заказа. См. таблицы 1 и 2 ниже.

| Таблица 1, сервисные детали для двигателей, оснащенных опцией FA1542 |  |  |
|---|---|---|
| Номер детали | Количество | Часть описание |
| 70760 | 1 | Пин Дюваль |
| [[3009330]] | 1 | шайба |
| [[3026269]] | 2 | шайба |
| 3035803 | 3 | Гайка шестиугольника |
| [[3036460]] | 1 | Шайба (пружина) |
| [[3093936]] | 3 | болты |
| [[3093940]] | 3 | болты |
| 3103848 | 1 | Пояс |
| [[3104029]] | 1 | Натяжитель ремня |
| 3681191 | 1 | Брекет, Напряжённый пояс |
| [[3681390]] | 1 | болты |
| [[3681587]] | 2 | Идлер Пулли (плоский) |
| 3681715 | 1 | Пилотный адаптер для Idler Pulley |
| [[3902460]] | 1 | болты |
| [[3903112]] | 1 | болты |
| [[3914407]] | 1 | болты |
| [[3935013]] | 2 | Пыль (Debris) Щит |
| 5575127 | 1 | Idler Pully Bracket Assembly (включает два нижних шкива) |

| Таблица 2, Сервисные детали для двигателей, построенных с опцией FA1657 |  |  |
|---|---|---|
| Номер детали | Количество | Часть описание |
| [[3026269]] | 1 | шайба |
| 3035803 | 3 | Гайка шестиугольника |
| [[3093940]] | 3 | болты |
| 3103848 | 1 | Пояс |
| [[3681587]] | 1 | Идлер Пулли (Плоский) |
| [[3903112]] | 1 | болты |
| [[3935013]] | 1 | Пыль (Debris) Щит |
| 5575127 | 1 | Idler Pully Bracket Assembly (включает два нижних шкива) |

**Статус в производстве**

Внедрено в производство. См. таблицу 2.

| Таблица 3, Информация о производстве |  |  |
|---|---|---|
| ESN последний | Постройте дату 1 | растение |
| 80074552 | Ноябрь 2018 | Джеймстаунский двигательный завод |
| 1 Дата сборки двигателя можно найти на табличке с данными двигателя. |  |  |

### История изменений документа

## Детали, упомянутые в документе

| Артикул | Наименование | Русское название |
|---|---|---|
| [[3009330]] | PLAIN WASHER | Плоская шайба |
| [[3026269]] | PLAIN WASHER | Плоская шайба |
| [[3036460]] | SPRING WASHER | Пружинная шайба |
| [[3093936]] | HEXAGON FLANGE HEAD CAP SCREW | Болт с шестигранной головкой и фланцем |
| [[3093940]] | HEXAGON FLANGE HEAD CAP SCREW | Болт с шестигранной головкой и фланцем |
| [[3104029]] | BELT TENSIONER | Натяжитель ремня |
| [[3681390]] | HEXAGON FLANGE HEAD CAP SCREW | Болт с шестигранной головкой и фланцем |
| [[3681587]] | IDLER PULLEY | Натяжной ролик |
| [[3902460]] | HEXAGON FLANGE HEAD CAP SCREW | Болт с шестигранной головкой и фланцем |
| [[3903112]] | HEXAGON FLANGE HEAD CAP SCREW | Болт с шестигранной головкой и фланцем |
| [[3914407]] | HEXAGON FLANGE HEAD CAP SCREW | Болт с шестигранной головкой и фланцем |
| [[3935013]] | DEBRIS SHIELD | Защитный экран от загрязнений |

> [!quote]- Original (English) · английский оригинал
> ## Belt Shredding
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Contents
>
> **Product Affected**
>
> - QSX15 CM570
>
> Options:
>
> - FA1542
> - FA1657
>
> **Issue**
>
> Symptom:
>
> - Progressive belt shredding caused by belt jump. See Figures 1 and 2 below.
> - Belt shredding can lead to loss of drive belt which will cause high coolant temperatures.
>
> Root Cause:
>
> - High fan center allows excessive belt deflection between fan pulley and crankshaft pulley.
>
> Figure 1, Belt Shred Shown Over Waterpump Pulley, Msing Two Leftmost Ribs.
>
> Figure 2, Removed belt with belt shred symptom – top ribs are missing
>
> **Description of Change**
>
> A new 3-idler pulley bracket for engines with specific high mount fan centers (fan drive options FA1542 and FA1657). The 3-idler pulley bracket is mounted on fan bracket between fan and crankshaft pulley. See Figure 3 below.
>
> Figure 3. Updated drive layout with 3-idler bracket
>
> **Verification**
>
> Verify engine was built with FA1542 or FA1657.
>
> Inspect belt for shredding or missing ribs on outside or inside of belt before removing from engine.
>
> Compare belt to Figure 1 and Figure 2 above to confirm malfunction mode is belt shred.
>
> **Resolution**
>
> - If fan drive option and malfunction mode match verification, a 3-idler bracket is to be installed.
> - Engines with FA1542 will need to have a larger cooling fan belt tensioner installed on low engine mount and an idler pulley added to center of drive.
> - Engines with FA1657 will already have this cooling fan belt tensioner and idler pulley installed. The information below shows parts and instructions for installing new parts for FA1542 and FA1657 in separate sections. Verify which drive is installed on engine and reference correct instructions.
> - Verify engines built with FA1542 have not been updated to FA1657 according to [[tsb120285 — Belt Shredding on QSX15 CM570 With Fan Centers 18” and Above\|TSB120285]] before proceding.
>
> **Service Instructions**
>
> See QSX15 CM570 Service Manual, Bulletin number [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]].
>
> **Installation Instructions for Engines with FA1542**
>
> Verify that engine currently has FA1542 installed. See Figure 1 below. The belt cooling fan belt tensioner will be installed in middle of drive, directly above crankshaft pulley.
>
> Figure 4, FA1542 Drive Layout.
>
> Removal of FA1542 components:
>
> - Remove fan drive belt, belt cooling fan belt tensioner, and cooling fan belt tensioner support from fan bracket.
>
> Figure 5, Water Pump Capscrews to be Removed
>
> Installation of cooling fan belt tensioner and idler pulley:
>
> - Install belt cooling fan belt tensioner bracket, Part Number 3681191. Use capscrews removed from water pump. Capscrew 1 is Part Number [[3681390]] and capscrews 2 and 3 are Part Number [[3093936]]. Capscrew 1 requires washer Part Number [[3036460]] and Capscrew 3 requires washer Part Number [[3009330]].
> - Install pilot adapter Part Number [[3681587]], using dowel pin Part Number 70760, and idler pulley Part Number [[3681587]].
> - Install low-mount large cooling fan belt tensioner Part Number [[3104029]].
>
> Installation of tight side idler bracket assembly and fan drive belt:
>
> - Remove fan support bracket (ladder bracket).
> - Install idler pulley bracket Part Number 5575127 to fan support bracket. bottom hole of idler pulley bracket should line up with bottom right hole of fan support bracket. See Figure 3. Use hex nut Part Number 3035803 and capscrew Part Number [[3093940]].
> - Reinstall fan support bracket.
> - Install idler pulley Part Number [[3681587]] to idler pulley bracket Part Number 5575127. Use capscrew Part Number [[3903112]] and washer Part Number [[3026269]].
> - Install dust shield Part Number [[3935013]] to idler pulley by pressing on outside diameter of shield to prevent damage to dust shield.
> - Install fan drive belt,Part Number 3103848.
>
> **Installation Instructions for Engines with FA1657**
>
> - Verify engine has FA1657 option. See Figure 6 below.
> - Tensioner will be installed on low engine mount and there will be an idler pulley directly above crankshaft pulley. There will be a tight side idler pulley, too.
>
> Figure 6, FA1657 Drive Layout.
>
> Removal of FA1657 Components
>
> - Remove fan drive belt.
> - Remove fan support bracket (ladder bracket).
> - Remove tight side idler bracket that is attached to fan support bracket with two capscrews.
>
> Installation of tight side idler bracket assembly and fan drive belt:
>
> - Install idler pulley bracket Part Number 5575127 to fan support bracket (removed in previous step). The bottom hole of idler pulley bracket should line up with bottom right hole of fan support bracket. See Figure 3. Use hex nut Part Number 3035803 and capscrew Part Number [[3093940]].
> - Reinstall fan bracket.
> - Install idler pulley Part Number [[3681587]] to idler pulley bracketPart Number 5575127. Use capscrePart Number 3 [[3903112]] and washePart Number 3 [[3026269]].
> - Install dust shield Part Number [[3935013]] to idler pulley by pressing on outside diameter of shield to prevent damage to dust shield.
> - Install fan drive belt, Part Number 3103848.
>
> **Service Parts**
>
> Service parts are available. See Tables 1 and 2 below.
>
> | **Table 1, Service Parts for Engines Equipped with FA1542 Option** |  |  |
> |---|---|---|
> | Part Number | Quantity | Part Description |
> | 70760 | 1 | Dowel Pin |
> | [[3009330]] | 1 | Washer |
> | [[3026269]] | 2 | Washer |
> | 3035803 | 3 | Hexagon Nut |
> | [[3036460]] | 1 | Washer (spring) |
> | [[3093936]] | 3 | Capscrew |
> | [[3093940]] | 3 | Capscrew |
> | 3103848 | 1 | Belt |
> | [[3104029]] | 1 | Belt Tensioner |
> | 3681191 | 1 | Bracket, Belt Tensioner |
> | [[3681390]] | 1 | Capscrew |
> | [[3681587]] | 2 | Idler Pulley (flat) |
> | 3681715 | 1 | Pilot Adapter for Idler Pulley |
> | [[3902460]] | 1 | Capscrew |
> | [[3903112]] | 1 | Capscrew |
> | [[3914407]] | 1 | Capscrew |
> | [[3935013]] | 2 | Dust (Debris) Shield |
> | 5575127 | 1 | Idler Pully Bracket Assembly (includes bottom two idler pulleys) |
>
> | **Table 2, Service Parts for Engines Currently Built with FA1657 Option** |  |  |
> |---|---|---|
> | Part Number | Quantity | Part Description |
> | [[3026269]] | 1 | Washer |
> | 3035803 | 3 | Hexagon Nut |
> | [[3093940]] | 3 | Capscrew |
> | 3103848 | 1 | Belt |
> | [[3681587]] | 1 | Idler Pulley (Flat) |
> | [[3903112]] | 1 | Capscrew |
> | [[3935013]] | 1 | Dust (Debris) Shield |
> | 5575127 | 1 | Idler Pully Bracket Assembly (includes bottom two idler pulleys) |
>
> **Production Status**
>
> Implemented for production. See Table 2.
>
> | Table 3, Production Information |  |  |
> |---|---|---|
> | ESN Last | Build Date 1 | Plant |
> | 80074552 | Nov 2018 | Jamestown Engine Plant |
> | 1 Engine build date can be found on engine dataplate. |  |  |
>
> ### Document History
