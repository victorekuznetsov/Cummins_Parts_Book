---
aliases:
  - "Форсунка"
type: "Процедура"
doc: "40-006-026-tr"
title_en: "Injector"
title_ru: "Форсунка"
modified: "2012-02-07"
engines:
  - "93047320"
families:
  - "6B5.9"
manuals:
  - "3666087"
figures: 70
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-006-026-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-006-026-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/6B5.9"
  - "группа/40"
  - "перевод/машинный"
---

# Injector
**Форсунка**

> [!abstract] Процедура · `40-006-026-tr`
> **Двигатели:** [[93047320 — 6B5.9 CPL 3111|93047320]]
> **Семейство:** 6B5.9
> **Входит в руководства:** [[3666087 — B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual|3666087]]
> **Секции:** Section 6 - Injectors and Fuel Lines - Group 06
> **Даты:** изменён 2012-02-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-006-026-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-006-026-tr.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

> [!warning] ОСТОРОЖНО
> Используйте только указанный форсунка для двигателя.

Все двигатели используют закрытую форсуну, форсунка типа отверстия. Однако форсунка может иметь разные номера деталей для разных рейтингов двигателя. Последние четыре цифры номера детали Cummins® используются для идентификации форсунки.

![[06900172.png]]

Во время цикла впрыска высокое давление от насоса впрыска повышается до рабочего (поп) давления, что заставляет игловый клапан в топливной форсунке подниматься. Затем топливо впрыскивается в цилиндр. Прорезиненная пружина используется для того, чтобы заставить клапан иглы закрыться, поскольку давление инъекций падает ниже давления поп-образования, чтобы запечатать сопло после инъекции.

![[fi900kc.png]]

Отказ иглового клапана поднимать и закрывать в нужное время или застрявший в открытом положении игловый клапан может привести к неправильному запуску двигателя и производству низкой мощности. Утечка топлива из открытого сопла может вызвать стук топлива, плохую производительность, дым, плохую экономию топлива и грубый бег.

![[fi900kd.png]]

### Подготовительные операции

Поезд Front Gear

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Отсоедините аккумуляторные батареи.
- Очистите вокруг топливного форсунка.
- Отключите линии подачи топлива высокого давления.[[40-006-051-tr — Injector Supply Lines (High Pressure)|См. процедуру 006-051 в разделе 6.]]
- Отключите коллектор слива топлива.[[40-006-021-tr — Fuel Manifold (Drain)|См. процедуру 006-021 в разделе 6.]]

![[ck800wa.png]]

Поезд Rear Gear

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Отсоедините аккумуляторные батареи.

![[13900050.png]]

- Снимите крышку коромысел.[[40-003-011-tr — Rocker Lever Cover|См. процедуру 003-011 в разделе 6.]]
- Удалите линии подачи топливного форсунка.[[40-006-051-tr — Injector Supply Lines (High Pressure)|См. процедуру 006-051 в разделе 6.]]
- Удалите топливный разъем.[[40-006-052-tr — Fuel Connector (Head Mounted)|См. процедуру 006-052 в разделе 6.]]

> [!note] Примечание
> Топливный разъем должен быть удален до удаления топливного форсунка или в результате этого произойдет повреждение разъема.

![[ck800wa.png]]

### Снятие

Поезд Front Gear

Растворитель с прокалыванием

> [!danger] ОПАСНО
> При очистке растворителями, кислотами и щелочными составами соблюдайте указания их изготовителя. Работайте в защитных очках и защитной одежде, чтобы снизить риск травмы.

> [!danger] ОПАСНО
> Некоторые растворители огнеопасны и токсичны. Перед применением прочитайте указания изготовителя.

> [!warning] ОСТОРОЖНО
> Когда на удерживающем гайке образовалась ржавчина, форсунка может поворачиваться в цилиндре, когда гайка ослаблена. Это может привести к серьезному повреждению головы топливным форсункой, который разрезает канавку в цилиндре.

Замочите зажимную гайку с ржавеющим растворителем в течение как минимум 3 минут.

![[fi900wd.png]]

Ударьте по корпусу форсунки дрейфовым штифтом, чтобы ослабить любую ржавчину.

![[fi900we.png]]

Держите корпус форсунки с регулируемым гаечным ключом, ослабляя прижимной гайкой с 24-мм коробочным гаечным ключом.

![[fi9boca.png]]

Используйте топливный форсунок, номер детали 3823276, чтобы удалить топливный форсунок.

![[fi900mc.png]]

Часто необходимо нажать на форсунка с помощью съёмника форсунки, чтобы работать с топливным форсункой вверх и вниз, чтобы удалить его.

![[fi900vc.png]]

Поезд Rear Gear

Удалите затворы удерживания форсунки.

Наклоните стойки вверх и выполните их.

![[06900081.png]]

Используйте топливный форсунок, часть 3825156, чтобы удалить топливный форсунок из головы.

![[06900140.png]]

### Очистка и проверка при повторном использовании

> [!danger] ОПАСНО
> При очистке растворителями, кислотами и щелочными составами соблюдайте указания их изготовителя. Работайте в защитных очках и защитной одежде, чтобы снизить риск травмы.

> [!warning] ОСТОРОЖНО
> Не используйте абразивы (такие как стеклянная бусинка, песочная бумага, салфетка из ромашки, прокладки Scotch-BriteTM и т. Д.) или металлические предметы (включая проволочные щетки из любого металлического материала) для очистки форсунки. Использование любого метода очистки, кроме безопасного растворителя и мягкой, чистой, без ворсинок ткани, повредит отверстия насадки и вызовет проблемы с производительностью.

Очистите наконечник форсунки и корпуса безопасным растворителем и мягкой, чистой тряпкой.

> [!note] Примечание
> При необходимости используйте щетку **brass** для очистки от углерода.

![[06900083.png]]

Осмотрите форсунку на заусеницах на входе в форсунка.

Осмотрите отверстия сопла на наличие любых признаков повреждения, таких как эрозия или затыкание.

Осмотрите цвет сопла на наличие признаков перегрева.

> [!note] Примечание
> Перегрев заставит сопло превратиться в темно-желтый/коричневый или синий цвет, в зависимости от степени перегрева.

Осмотрите кольцо на предмет повреждения.

![[06900084.png]]

О-кольца и герметичные шайбы

Если разъёмы высокого давления **не** повреждены, удалите форсунка и проверьте кольца и уплотнительные шайбы. Если есть **любые** повреждения частей форсунки, замените кольцо или уплотнительные шайбы.

Осмотрите точку контакта уплотнительных шайб с головкой цилиндра.

![[06900140.png]]

### Проверка

Поезд Front Gear

> [!danger] ОПАСНО
> Не вентилируйте топливную систему на горячий двигатель; это может привести к тому, что топливо разольется на горячий выхлопной коллектор, что может вызвать пожар.

Чтобы определить, какой цилиндр выключается, управляйте двигателем, ослабляйте гайку топливной линии на одном топливном форсунке и слушайте изменение скорости двигателя.

> [!note] Примечание
> Падение скорости двигателя указывает на то, что форсунка доставлял топливо в цилиндр.

> [!note] Примечание
> Обязательно затяните гайку топливной линии, прежде чем перейти к следующему топливному форсунке.

Проверяйте каждый цилиндр до тех пор, пока не будет найден неисправный форсунка.

![[fi900wc.png]]

Удалите неисправный форсунка для его испытания или замены.

Если двигатель продолжает работать неправильно после замены форсунки, проверьте наличие утечек в линии высокого давления. Кроме того, проверьте наличие поврежденного клапана доставки, который позволяет сливу топлива обратно в насос для впрыска.

![[fi900mb.png]]

Проверьте дополнительную медную герметичную шайбу на топливном форсунке.

![[fi900gj.png]]

Углеродное накопление в отверстиях в сопле также вызовет низкую мощность двигателя. Удалите и проверьте образец распыления или замените форсунку.

![[fi900sa.png]]

> [!danger] ОПАСНО
> Во время тестирования форсунки держите руки и части тела подальше от сопла форсунки. Топливо, поступающее из форсунки, находится под экстремальным давлением и может вызвать серьезные травмы, проникая в кожу.

Используйте тестер насадки форсунки, номер детали 3376946. Все сопла должны быть проверены на открывание давления, болтовни и распыления.

![[fi900db.png]]

Проверьте давление открытия топливного форсунка.

1. Откройте клапан.
2. Управляйте рычагом одним ударом каждую секунду.
3. Прочитайте давление, указанное при начале распыления форсунки.

![[fi900da.png]]

Если давление открытия не соответствует спецификациям, попробуйте одно из следующих решений:

1. Добавьте шим для повышения давления.
2. Удалить шим для снижения давления.

![[fi9smva.png]]

Тест на утечку

1. Откройте клапан (A).
2. Управляйте рычагом (B) для поддержания давления 20 бар \[290 psi\] ниже давления открытия (C).
3. Ни одна капля не должна упасть с кончика (D) в течение 10 секунд.

![[fi900dc.png]]

Тестирование Chatter

Тест на болтовню указывает на способность иглового клапана свободно перемещаться и правильно распылять топливо. Слышный звук может быть услышан, когда клапан быстро открывается и закрывается. Хорошо оптимизированный образец спрея можно увидеть.

> [!note] Примечание
> Используемые сопла **не должны **оцениваться для болтовни на более низких скоростях. Используемое сопло обычно может быть использовано, если оно проходит тест на утечку.

![[fi900dd.png]]

Поезд Rear Gear

> [!danger] ОПАСНО
> Не вентилируйте топливную систему на горячий двигатель; это может привести к тому, что топливо разольется на горячий выхлопной коллектор, что может вызвать пожар.

Испытание для определения того, какой цилиндр выключается, управлять двигателем, ослабить гайку топливной линии на одном топливном форсунке и слушать изменение скорости двигателя.

> [!note] Примечание
> Падение скорости двигателя указывает на то, что форсунка доставлял топливо в цилиндр.

> [!note] Примечание
> Обязательно затяните гайку топливной линии, прежде чем перейти к следующему топливному форсунке.

Проверяйте каждый цилиндр до тех пор, пока не будет найден неисправный форсунка.

![[06900047.png]]

Удалите неисправный форсунка для его испытания или замены.

Если двигатель продолжает работать неправильно после замены форсунки, проверьте наличие утечек в линии высокого давления.

Проверьте наличие дефектного клапана подачи, который позволяет топливу стекать обратно в насос для впрыска.

![[06900140.png]]

Используйте держатель форсунки, номер детали 3162269, для установки форсунки на испытательном стенде форсунки, номер детали 3376946.

Откройте обходной клапан для измерителя давления, чтобы можно было проверить образец распыления.

![[06900085.png]]

Управляйте рычагом испытательного стенда несколько раз быстро, чтобы проверить образец распыления форсунки. Убедитесь, что правильное количество шлейфов присутствует для количества отверстий, которые имеет форсунка. Также обратите пристальное внимание на размер и форму каждого шлейфа. Если возможно, сравните образец распыления с образцом нового форсунки с тем же номером сборки.

> [!note] Примечание
> Образец распыления форсунки является отличным показателем состояния отверстия насадки. Внимательно проверьте каждый шлейф; возможно, что только одно отверстие имеет повреждение. Значительные проблемы производительности будут возникать, если есть повреждение любого количества отверстий.

![[06900085.png]]

Закройте обходной клапан для измерителя давления и используйте рычаг испытательного стенда для проверки давления открытия сопла.

Есть хороший хрустящий «поп», когда насадка открывается. Спецификация давления составляет 300 ± 10 бар \[4351 ± 145 psi\].

> [!note] Примечание
> Если давление открытия сопла выходит за пределы указанных пределов, можно добавить или удалить изгибы в форсунка для изменения давления открытия.

![[06900087.png]]

Если давление открытия сопла чрезмерно низкое и/или сопло распыляет чрезмерное топливо, игла форсунки, возможно, прилипает. Игла может застрять из-за плохой смазки или мусора.

Можно отклеить иглу форсунки с помощью испытательного стенда форсунки. Откройте обходной клапан для измерителя давления и быстро управляйте рычагом испытательного стенда на 10-20 ходов.

![[06900088.png]]

Проверьте давление открытия сопла и образец распыления снова, чтобы определить, вернулся ли форсунка к нормальной работе.

Если форсунка остается за пределами указанных пределов, замените форсунку.

![[06900141.png]]

Осмотрите форсунку для капания и / или чрезмерной утечки вниз.

Закройте обходной клапан для измерительного манометра и создайте давление в пределах 1000 кПа \[145 psi\] давления открытия сопла.

![[06900090.png]]

Тестирование Chatter

Тест на болтовню указывает на способность иглового клапана свободно перемещаться и правильно распылять топливо. Слышный звук может быть услышан, когда клапан быстро открывается и закрывается. Также можно наблюдать хорошо оптимизированный образец спрея.

> [!note] Примечание
> Используемые сопла **не должны **оцениваться для болтовни на более низких скоростях. Используемое сопло обычно может быть использовано, если оно проходит тест на утечку.

![[fi900dd.png]]

### Измерение

> [!warning] ОСТОРОЖНО
> Неправильная герметичная шайба может вызвать утечку топлива высокого давления и/или проблемы с производительностью из-за неправильной протрузии форсунки.

Установите калибр глубины, инструмент № 3164438, на палубу сгорания головки цилиндра и обнулите ее.

Поверните калибр глубины так, чтобы он измерял выступ форсунки в самой высокой точке на топливном форсунке.

Запись выступа форсунки для каждого форсунки.

| Форсунка Tip Protrusion B Series 1991 Automotive и CPL 1577 |  |  |
|---|---|---|
| мм |  | в |
| 3.5 | Мин | 0.1378 |
| 4.5 | Макс | 0.1772 |

| Твердый форсунка Tip Protrusion All Other B Series Pre 1991 Automotive и 1994 Automotive |  |  |
|---|---|---|
| мм |  | в |
| 4.5 | Мин | 0.1772 |
| 5.5 | Макс | 0.2165 |

| форсунка Tip Protrusion Non-Automotive B Series |  |  |
|---|---|---|
| мм |  | в |
| 3.0 | Мин | 0.1180 |
| 4.0 | Макс | 0.1575 |

Если выступ форсунки не соответствует спецификациям, обратитесь к диаграмме толщины уплотнения форсунки ниже для имеющихся толщин уплотнения.

| Форсунка Seal Thickness |  |  |  |
|---|---|---|---|
|  | мм |  | в |
| 1,5 мм уплотнение | 1.40 | Мин | 0.055 |
|  | 1.68 | Макс | 0.066 |

|  | мм |  | в |
|---|---|---|---|
| 2.5 мм уплотнение | 2.40 | Мин | 0.095 |
|  | 2.68 | Макс | 0.106 |

|  | мм |  | в |
|---|---|---|---|
| 3,0 мм уплотнение | 2.90 | Мин | 0.114 |
|  | 3.18 | Макс | 0.125 |

![[fi900na.png]]

### Разборка

Очистить углеродный остаток от насадки топливного форсунка. Используйте латунную проволочную щетку и кусок лиственной древесины, опущенный в тестируемое масло.

![[fi900ea.png]]

Удалите уплотнение форсунки и отбросьте уплотнение.

![[fi9wawa.png]]

Закрепить зажим удерживания форсунки в мягких шприцах, чтобы удерживать форсунка.

Удалите сопло форсунки, удерживающее гайку.

![[fi9numb.png]]

> [!warning] ОСТОРОЖНО
> Поместите сопло и иглы форсунки в подходящую ванну с чистым тестируемым маслом или произойдет повреждение.

Удалите клапан иглы сопла и промежуточную пластину.

![[fi9vama.png]]

> [!warning] ОСТОРОЖНО
> Держите игловый клапан только стеблем. Контакт с кожей будет разъедать тонко защелкнутую поверхность.

![[fi900va.png]]

> [!note] Примечание
> Игольчатый клапан и наконечник сопла точно соответствуют друг другу. Части не должны быть смешаны.

![[fi900wa.png]]

Удалите держатель сопла из форсунки.

Удалите веретено давления, пружину давления и тряпки.

![[fi900fa.png]]

Удалить и выбросить уплотнительный рукав форсунки.

![[fi9slma.png]]

### Очистка

> [!danger] ОПАСНО
> При очистке растворителями, кислотами и щелочными составами соблюдайте указания их изготовителя. Работайте в защитных очках и защитной одежде, чтобы снизить риск травмы.

Промойте корпуса сопла и иглы в растворителе, чтобы тщательно и полностью удалить все лаковые и углеродные отложения.

![[fi900eb.png]]

> [!warning] ОСТОРОЖНО
> Никогда не используйте износостойкую бумагу, стальную щетку или любой другой металлический скребок для очистки сопла. Части могут быть повреждены.

Опустите сиденье сопла в чистое измерительное масло и используйте комплект для очистки сопла, номер детали 3376947, для очистки сиденья сопла. Польское игольное сиденье с куском лиственной древесины, опущенной в тест-масло.

![[fi900ec.png]]

> [!danger] ОПАСНО
> При очистке растворителями, кислотами и щелочными составами соблюдайте указания их изготовителя. Работайте в защитных очках и защитной одежде, чтобы снизить риск травмы.

Очистить внутреннюю кольцевую канавку сопла скребком, как проиллюстрировано. Промойте сопло в растворителе, чтобы удалить всю грязь и углеродный остаток, и окуните его в чистое тестируемое масло.

![[fi900ed.png]]

Очистите распылительные отверстия с помощью иглы для очистки соответствующего размера, как показано на рисунке.

Удалите сгоревшие отложения горения на всех соплах с коммерчески доступным очистителем. Промыть все части в чистом тест-масле.

![[fi900ee.png]]

Очистить наконечник иглового клапана латунной щеткой.

![[06900173.png]]

### Осмотр

Поезд Front Gear

Проверьте форсунку. Осмотрите кольцо на предмет повреждения. Осмотрите заусеницы на входе в форсунка. Проверьте отверстия сопла на наличие любых признаков повреждения, таких как эрозия отверстия или затыкание отверстия. Также проверьте цвет насадки на наличие признаков перегрева. Перегрев заставит сопло превратиться в темно-желтый/коричневый или синий цвет, в зависимости от температуры перегрева.

Проверка неровных поверхностей и эрозии. Плечо под давлением обычно имеет грубый обрабатывающий вид.

Осмотрите цилиндр форсунки для старых уплотнительных шайб.

> [!note] Примечание
> Ухудшенные игловые клапаны должны быть заменены в качестве соответствующего устройства с совместимым корпусом сопла.

![[fi9vasa.png]]

Опустите игловой клапан в чистое измерительное масло и вставьте игловой клапан полностью в корпус сопла.

![[fi9vawa.png]]

Вытащите иглой клапан на одну треть пути из корпуса сопла. При игловом клапане в вертикальном положении игловый клапан **должен** скользить обратно в корпус сопла под собственным весом.

Если сопло не проходит испытание на скольжение, прочистите и снова проверьте сопло.

> [!note] Примечание
> Любой игловый клапан и форсунок, которые не проходят этот тест, должны быть заменены.

![[fi9vasb.png]]

Поезд Rear Gear

> [!warning] ОСТОРОЖНО
> Не прикасайтесь к игле кончиками пальцев. Масло из ваших пальцев повредит иглу. Держите иглу за стебель. Если игла затронута, протрите чистую мягкую ткань и окунитесь в чистое дизельное топливо.

Удалите иглу из наконечника насадки и проверьте цвет.

Проверьте наличие признаков чрезмерного углерода или перегрева (темно-желтый / загар или синий цвет иглы).

Проверьте следы от потасовки на игле.

![[06900094.png]]

Уберите иглу в чистое дизельное топливо и вставьте ее в сопло.

Держите насадку под углом 45 градусов и вытащите иглу 2/3 пути наружу. Под собственным весом игла **должна** плавно сползать обратно в сопло.

![[06900095.png]]

### Сборка

Поезд Front Gear

> [!danger] ОПАСНО
> При очистке растворителями, кислотами и щелочными составами соблюдайте указания их изготовителя. Работайте в защитных очках и защитной одежде, чтобы снизить риск травмы.

> [!note] Примечание
> Убедитесь, что все поверхности для спаривания и грани давления тщательно очищены и смазаны тестируемым маслом перед сборкой. Новые сопла должны быть очищены и смазаны перед сборкой.

![[fi900wb.png]]

> [!note] Примечание
> Установите ту же толщину изгибов, которые были удалены при разборке. Используйте пружину давления, чтобы убедиться, что шасси установлены плоскими.

Установите шампуни и пружину давления.

![[fi9spha.png]]

Установите веретено.

![[fi900aa.png]]

Установите промежуточную пластину.

![[fi9plaa.png]]

Установите игловой клапан и форсунок сборки.

![[fi9vaaa.png]]

Установите сопло, удерживающее гайку.

> [!tip] Момент затяжки
> 30 Н·м [22 фунт-фут]

![[fi9nuhb.png]]

Поезд Rear Gear

Очистите внутренние компоненты топливного форсунка чистым дизельным топливом и чистой тканью.

Убедитесь, что во внутренних частях топливного форсунка есть мусор **no**.

![[06900096.png]]

> [!note] Примечание
> Убедитесь, что промежуточная пластина находится в правильной ориентации, причем отверстие подачи на пластине выстилается с отверстием подачи на держателе.

Установите пружину, кнопку, промежуточную пластину и сопло/иглу.

![[06900098.png]]

Установите удерживающий гайка ручной герметично.

Поместите форсунка в зажим форсунки.

Затяните удерживающий гайка.

> [!tip] Момент затяжки
> 47 Н·м [35 фунт-фут]

Установите шайбу.

![[06900099.png]]

### Установка

Поезд Front Gear

Соберите форсунка и новую медную герметичную шайбу.

Используйте только одну медную шайбу.

**Совет по обслуживанию: **Легкий слой чистого смазочного моторного масла между шайбой машиной и топливным форсункой может помочь предотвратить падение шайбы во время установки.

![[fi9waaa.png]]

> [!warning] ОСТОРОЖНО
> Ранняя модель форсунки (до 1991 года) имеет 9-мм наконечник форсунки, который не может быть использован в двигателях, построенных в 1991 году или позже, поскольку эти двигатели используют 7-мм наконечник форсунки.

![[fi901gb.png]]

Если на наконечник 7-мм форсунки установлен специальный адаптер, то в ранних моделях (9-мм) распылительных отверстий форсунок можно использовать 7-мм форсунка.

![[fi900wf.png]]

Нанесите слой анти-захватного соединения, номер детали 3824879, на резьба форсунки, удерживающего гайку, и между верхней частью гайки и корпусом форсунки.

![[fi9nuwa.png]]

> [!note] Примечание
> Выровнять выступ форсунки с выемкой в цилиндре.

> [!note] Примечание
> Настоящий форсунка Bosch® имеет кольцо, расположенное над зажимным гайком. После затягивания форсунки обязательно надавите на о-кольцо в канавку.

> [!tip] Момент затяжки
> 60 Н·м [44 фунт-фут]

![[fi9hdoa.png]]

Поезд Rear Gear

Поместите форсунка в голову в правильной ориентации.

Установите форсунку натяжным и затягивающим.

> [!tip] Момент затяжки
> 10 Н·м [89 фунт-дюйм]

![[06900143.png]]

### Завершающие операции

Поезд Front Gear

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Установите линии подачи топлива высокого давления.[[40-006-051-tr — Injector Supply Lines (High Pressure)|См. процедуру 006-051 в разделе 6.]]
- Установите коллектор слива топлива.[[40-006-021-tr — Fuel Manifold (Drain)|См. процедуру 006-021 в разделе 6.]]
- Подсоедините аккумуляторные батареи.
- Выкачивать весь воздух из топливной системы.[[40-006-051-tr — Injector Supply Lines (High Pressure)|См. процедуру 006-051 в разделе 6.]]
- Запустите двигатель и проверьте на отсутствие утечек.

![[ck800wa.png]]

Поезд Rear Gear

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Установите топливный разъем.[[40-006-052-tr — Fuel Connector (Head Mounted)|См. процедуру 006-052 в разделе 6.]]
- Установите крышку коромысел.[[40-003-011-tr — Rocker Lever Cover|См. процедуру 003-011 в разделе 3.]]
- Установите топливные линии высокого давления.[[40-006-051-tr — Injector Supply Lines (High Pressure)|См. процедуру 006-051 в разделе 6.]]
- Подсоедините аккумуляторные батареи.
- Выкачивает весь воздух из топливной системы.[[40-006-051-tr — Injector Supply Lines (High Pressure)|См. процедуру 006-051 в разделе 6.]]
- Запустите двигатель и проверьте на отсутствие утечек.

![[ck800wa.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> **CAUTION · Осторожно**
> Use only the specified injector for the engine.
>
> All engines use closed nozzle, hole-type injectors. However, the injectors can have different part numbers for different engine ratings. The last four digits of the Cummins® part number are used to identify the injectors.
>
> During the injection cycle, high pressure from the injection pump rises to the operating (pop) pressure, which causes the needle valve in the injector to lift. Fuel is then injected into the cylinder. A shimmed spring is used to force the needle valve closed as the injection pressure drops below the pop pressure to seal off the nozzle after injection.
>
> Failure of the needle valve to lift and close at the correct time or the needle valve stuck open can cause the engine to misfire and produce low power. Fuel leaking from the open nozzle can cause a fuel knock, poor performance, smoke, poor fuel economy, and rough running.
>
> ### Preparatory Steps
>
> Front Gear Train
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Disconnect the batteries.
> - Clean around the injectors.
> - Disconnect the high-pressure fuel supply lines. [[40-006-051-tr — Injector Supply Lines (High Pressure)|Refer to Procedure 006-051 in Section 6.]]
> - Disconnect the fuel drain manifold. [[40-006-021-tr — Fuel Manifold (Drain)|Refer to Procedure 006-021 in Section 6.]]
>
> Rear Gear Train
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Disconnect the batteries.
>
> - Remove the rocker lever cover. [[40-003-011-tr — Rocker Lever Cover|Refer to Procedure 003-011 in Section 6.]]
> - Remove the injector supply lines. [[40-006-051-tr — Injector Supply Lines (High Pressure)|Refer to Procedure 006-051 in Section 6.]]
> - Remove the fuel connector. [[40-006-052-tr — Fuel Connector (Head Mounted)|Refer to Procedure 006-052 in Section 6.]]
>
> **Note · Примечание**
> The fuel connector **must** be removed before removing the injector or damage to the connector will result.
>
> ### Remove
>
> Front Gear Train
>
> Rust-Penetrating Solvent
>
> **WARNING · Опасно**
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.
>
> **WARNING · Опасно**
> Some solvents are flammable and toxic. Read the manufacturer's instructions before using.
>
> **CAUTION · Осторожно**
> When rust has formed on the hold-down nut, the injector can turn in the bore when the nut is loosened. This can cause severe damage to the head by the injector locating ball cutting a groove in the bore.
>
> Soak the hold-down nut with a rust-penetrating solvent for a minimum of 3 minutes.
>
> Hit the injector body with a drift pin to loosen any rust.
>
> Hold the injector body with an adjustable wrench while loosening the hold-down nut with a 24-mm box wrench.
>
> Use an injector puller, Part Number 3823276, to remove the injectors.
>
> It is often necessary to tap the injector with the injector puller to work the injector up and down to remove it.
>
> Rear Gear Train
>
> Remove the injector hold-down capscrews.
>
> Tilt the hold-downs up, and slide them out.
>
> Use an injector puller, Part Number 3825156, to remove the injectors from the head.
>
> ### Clean and Inspect for Reuse
>
> **WARNING · Опасно**
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.
>
> **CAUTION · Осторожно**
> Do not use any abrasives (such as glass beading, sand paper, emery cloth, Scotch-Brite™ pads, etc) or metallic items (including wire brushes made of any metallic material) to clean the injectors. The use of any cleaning method other than safety solvent and a soft, clean, lint-free cloth will damage the nozzle holes and cause performance issues.
>
> Clean the injector tip and body with safety solvent and a soft, clean rag.
>
> **Note · Примечание**
> If necessary, use a **brass** brush to clean off carbon.
>
> Inspect the injector for burrs on the inlet to the injector.
>
> Inspect the nozzle holes for any signs of damage, such as erosion or plugging.
>
> Inspect the nozzle color for signs of overheating.
>
> **Note · Примечание**
> Overheating will cause the nozzle to turn a dark yellow/tan or blue color, depending on the degree of overheating.
>
> Inspect the o-ring for damage.
>
> O-rings and Sealing Washers
>
> If the high-pressure connectors are **not** damaged, remove the injectors and inspect the o-rings and sealing washers. If there is **any** damage to the injector parts, replace the o-ring or sealing washers.
>
> Inspect the contact point of the sealing washers to the cylinder head.
>
> ### Test
>
> Front Gear Train
>
> **WARNING · Опасно**
> Do not vent the fuel system on a hot engine; this can cause fuel to spill onto a hot exhaust manifold, which can cause a fire.
>
> To determine which cylinder is misfiring, operate the engine, loosen the fuel line nut at one injector, and listen for a change in engine speed.
>
> **Note · Примечание**
> A drop in engine speed indicates the injector was delivering fuel to the cylinder.
>
> **Note · Примечание**
> Be sure to tighten the fuel line nut before proceeding to the next injector.
>
> Check each cylinder until the malfunctioning injector is found.
>
> Remove the malfunctioning injector to test or replace it.
>
> If the engine continues to misfire after replacing the injector, check for leaks in the high-pressure line. Also, check for a damaged delivery valve that lets the fuel drain back into the injection pump.
>
> Check for an extra copper sealing washer on the injector.
>
> Carbon buildup in the orifices in the nozzle will also cause low power from the engine. Remove and check the spray pattern, or replace the injectors.
>
> **WARNING · Опасно**
> While testing the injectors, keep hands and body parts away from the injector nozzle. Fuel coming from the injector is under extreme pressure and can cause serious injury by penetrating the skin.
>
> Use an injector nozzle tester, Part Number 3376946. All nozzles **must** be tested for opening pressure, chatter, and spray pattern.
>
> Check the injector opening pressure.
>
> 1. Open the valve.
> 2. Operate the lever at one stroke every second.
> 3. Read the pressure indicated when the injector spray begins.
>
> If the opening pressure does **not** meet specifications, attempt one of the following solutions:
>
> 1. Add shims to increase pressure.
> 2. Remove shims to decrease pressure.
>
> Leakage Test
>
> 1. Open the valve (A).
> 2. Operate the lever (B) to maintain a pressure of 20 bar \[290 psi\] below opening pressure (C).
> 3. No drops should fall from the tip (D) within 10 seconds.
>
> Chatter Test
>
> The chatter test indicates the ability of the needle valve to move freely and atomize the fuel correctly. An audible sound will possibly be heard as the valve rapidly opens and closes. A well-optimized spray pattern can possibly be seen.
>
> **Note · Примечание**
> Used nozzles **must not** be evaluated for chatter at lower speeds. A used nozzle can usually be used if it passes the leakage test.
>
> Rear Gear Train
>
> **WARNING · Опасно**
> Do not vent the fuel system on a hot engine; this can cause fuel to spill onto a hot exhaust manifold, which can cause a fire.
>
> Test to determine which cylinder is misfiring, operate the engine, loosen the fuel line nut at one injector, and listen for a change in engine speed.
>
> **Note · Примечание**
> A drop in engine speed indicates the injector was delivering fuel to the cylinder.
>
> **Note · Примечание**
> Be sure to tighten the fuel line nut before proceeding to the next injector.
>
> Check each cylinder until the malfunctioning injector is found.
>
> Remove the malfunctioning injector to test or replace it.
>
> If the engine continues to misfire after replacing the injector, check for leaks in the high-pressure line.
>
> Check for a defective delivery valve that allows the fuel to drain back into the injection pump.
>
> Use an injector holder, Part Number 3162269, to install the injector on the injector test stand, Part Number 3376946.
>
> Open the bypass valve for the pressure gauge so the spray pattern can be checked.
>
> Operate the test stand lever quickly several times to check the spray pattern of the injectors. Verify that the correct number of plumes are present for the number of holes the injector has. Also, pay close attention to the size and shape of each plume. If possible, compare the spray pattern to that of a new injector with the same assembly number.
>
> **Note · Примечание**
> The injector spray pattern is an excellent indicator of the nozzle hole condition. Check each plume carefully; it is possible that **only** a single hole has damage. Significant performance problems will result if there is damage to any number of the holes.
>
> Close the bypass valve for the pressure gauge, and operate the test stand lever to check nozzle opening pressure.
>
> There is a good crisp "pop" when the nozzle opens. The pressure specification is 300 ± 10 Bar \[4351 ± 145 psi\].
>
> **Note · Примечание**
> If the nozzle opening pressure is out of specification, it is possible to add or remove shims to the injector to modify the opening pressure.
>
> If the nozzle opening pressure is excessively low and/or the nozzle sprays excessive fuel, the injector needle is possibly sticking. The needle can be stuck because of poor lubrication or debris.
>
> It is possible to unstick an injector needle by use of the injector test stand. Open the bypass valve for the pressure gauge and operate the test stand lever rapidly for 10 to 20 strokes.
>
> Check the nozzle opening pressure and spray pattern again to determine if the injector has returned to normal operation.
>
> If the injector remains out of specification, replace the injector.
>
> Inspect the injector for dripping and/or excessive leak down.
>
> Close the bypass valve for the pressure gauge and build pressure to within 1000 kPa \[145 psi\] of the opening pressure of the nozzle.
>
> Chatter Test
>
> The chatter test indicates the ability of the needle valve to move freely and atomize the fuel correctly. An audible sound can be heard as the valve rapidly opens and closes. A well-optimized spray pattern can also be observed.
>
> **Note · Примечание**
> Used nozzles **must not** be evaluated for chatter at lower speeds. A used nozzle can usually be used if it passes the leakage test.
>
> ### Measure
>
> **CAUTION · Осторожно**
> The incorrect sealing washer can cause high-pressure fuel leaks and/or performance problems because of incorrect injector protrusion.
>
> Install the depth gauge assembly, Tool Number 3164438, on the cylinder head combustion deck and zero it.
>
> Rotate the depth gauge so that it measures the injector protrusion at the highest point on the injector.
>
> Record the injector protrusion for each injector.
>
> | Injector Tip Protrusion B Series 1991 Automotive and CPL 1577 |  |  |
> |---|---|---|
> | mm |  | in |
> | 3.5 | MIN | 0.1378 |
> | 4.5 | MAX | 0.1772 |
>
> | Injector Tip Protrusion All Other B Series Pre 1991 Automotive and 1994 Automotive |  |  |
> |---|---|---|
> | mm |  | in |
> | 4.5 | MIN | 0.1772 |
> | 5.5 | MAX | 0.2165 |
>
> | Injector Tip Protrusion Non-Automotive B Series |  |  |
> |---|---|---|
> | mm |  | in |
> | 3.0 | MIN | 0.1180 |
> | 4.0 | MAX | 0.1575 |
>
> If the injector protrusion is not within the specifications, reference the injector seal thickness chart below for the available seal thicknesses.
>
> | Injector Seal Thickness |  |  |  |
> |---|---|---|---|
> |  | mm |  | in |
> | 1.5 mm Seal | 1.40 | MIN | 0.055 |
> |  | 1.68 | MAX | 0.066 |
>
> |  | mm |  | in |
> |---|---|---|---|
> | 2.5 mm Seal | 2.40 | MIN | 0.095 |
> |  | 2.68 | MAX | 0.106 |
>
> |  | mm |  | in |
> |---|---|---|---|
> | 3.0 mm Seal | 2.90 | MIN | 0.114 |
> |  | 3.18 | MAX | 0.125 |
>
> ### Disassemble
>
> Clean the carbon residue from the injector nozzle. Use a brass wire brush and a piece of hardwood dipped in test oil.
>
> Remove the injector seal and discard the seal.
>
> Clamp an injector hold-down clamp in a soft-jawed vise to hold the injector.
>
> Remove the injector nozzle retaining nut.
>
> **CAUTION · Осторожно**
> Place the injector nozzle and needle valve in a suitable bath of clean test oil or damage will occur.
>
> Remove the nozzle needle valve and intermediate plate.
>
> **CAUTION · Осторожно**
> Hold the needle valve by the stem only. Contact from the skin will corrode the finely lapped surface.
>
> **Note · Примечание**
> The needle valve and nozzle tip are precisely matched for fit. The parts **must not** be intermixed.
>
> Remove the nozzle holder from the vise.
>
> Remove the pressure spindle, pressure spring, and shims.
>
> Remove and discard the injector sealing sleeve.
>
> ### Clean
>
> **WARNING · Опасно**
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.
>
> Rinse the nozzle bodies and needle valves in solvent to flush them thoroughly and completely remove all varnish and carbon deposits.
>
> **CAUTION · Осторожно**
> Never use emery paper, a steel brush, or any other metal scraper to clean the nozzle. The parts can be damaged.
>
> Dip the nozzle seat in clean test oil, and use the nozzle cleaning kit, Part Number 3376947, to clean the nozzle seat. Polish the needle seat with a piece of hardwood dipped in test oil.
>
> **WARNING · Опасно**
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.
>
> Clean the interior ring groove of the nozzle with a scraper, as illustrated. Rinse the nozzle in solvent to remove all dirt and carbon residue, and dip it in clean test oil.
>
> Clean the spray holes with an appropriate size cleaning needle, as illustrated.
>
> Remove burned-on combustion deposits on all nozzles with a commercially available cleaner. Rinse all parts in clean test oil.
>
> Clean the needle valve tip with a brass brush.
>
> ### Inspect
>
> Front Gear Train
>
> Inspect the injector. Inspect the o-ring for damage. Inspect for burrs on the inlet to the injector. Check the nozzle holes for any signs of damage such as hole erosion or hole plugging. Also, check the nozzle color for signs of overheating. Overheating will cause the nozzle to turn a dark yellow/tan or blue color, depending on the temperature of the overheat.
>
> Inspect for rough surfaces and erosion. The pressure shoulder will normally have a rough machined appearance.
>
> Inspect the injector bore for old sealing washers.
>
> **Note · Примечание**
> Deteriorated needle valves **must** be replaced as a matched unit with their compatible nozzle body.
>
> Dip the needle valve in clean test oil and insert the needle valve all the way into the nozzle body.
>
> Pull the needle valve one-third of the way out of the nozzle body. With the needle valve in the vertical position, the needle valve **must** slide all the way back into the nozzle body under its own weight.
>
> If the nozzle fails the slide test, clean and test the nozzle again.
>
> **Note · Примечание**
> Any needle valve and nozzle body assembly that does **not** pass this test **must** be replaced.
>
> Rear Gear Train
>
> **CAUTION · Осторожно**
> Do not touch the needle with your fingertips. Oil from your fingers will damage the needle. Hold the needle by the stem. If the needle is touched, wipe clean with a soft cloth and dip in clean diesel fuel.
>
> Remove the needle from the nozzle tip and inspect the color.
>
> Check for signs of excessive carbon or overheating (dark yellow/tan or blue needle color).
>
> Check for scuff marks on the needle.
>
> Dip the needle in clean diesel fuel and insert it into the nozzle.
>
> Hold the nozzle at a 45-degree angle and pull the needle 2/3 of the way out. Under its own weight, the needle **must** slide smoothly back into the nozzle.
>
> ### Assemble
>
> Front Gear Train
>
> **WARNING · Опасно**
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.
>
> **Note · Примечание**
> Make sure that all mating surfaces and pressure faces are thoroughly cleaned and lubricated with test oil before assembly. New nozzles **must** be cleaned and lubricated before assembly.
>
> **Note · Примечание**
> Install the same thickness of shims that were removed in disassembly. Use the pressure spring to make sure the shims are installed flat.
>
> Install the shims and pressure spring.
>
> Install the spindle.
>
> Install the intermediate plate.
>
> Install the needle valve and nozzle assembly.
>
> Install the nozzle retaining nut.
>
> **Момент затяжки · Torque Value**
> 30 n•m [22 ft-lb]
>
> Rear Gear Train
>
> Clean the internal components of the injector with clean diesel fuel and a clean cloth.
>
> Make sure there is **no** debris in the internal parts of the injector.
>
> **Note · Примечание**
> Make sure the intermediate plate is in the correct orientation, with the supply hole on the plate lining up with the supply hole on the holder.
>
> Install the spring, button, intermediate plate, and nozzle/needle.
>
> Install the retaining nut hand-tight.
>
> Place the injector in the injector clamp.
>
> Tighten the retaining nut.
>
> **Момент затяжки · Torque Value**
> 47 n•m [35 ft-lb]
>
> Install the sealing washer.
>
> ### Install
>
> Front Gear Train
>
> Assemble the injector and a new copper sealing washer.
>
> Use **only** one copper washer.
>
> **Service Tip:** A light coat of clean lubricating engine oil between the washer and injector can help to keep the washer from falling during installation.
>
> **CAUTION · Осторожно**
> Early model injectors (pre-1991) have a 9-mm injector tip that can not be used in engines built in 1991 or later as these engines use a 7-mm injector tip.
>
> If the special adapter sleeve is installed onto the 7-mm injector tip, 7-mm injectors can be used in early model (9-mm) injector holes.
>
> Apply a coat of anti-seize compound, Part Number 3824879, to the threads of the injector hold-down nut and between the top of the nut and the injector body.
>
> **Note · Примечание**
> Align the injector's protrusion with the notch in the bore.
>
> **Note · Примечание**
> The present Bosch® injector has an o-ring located above the hold-down nut. After tightening the injector, be sure to push the o-ring into the groove.
>
> **Момент затяжки · Torque Value**
> 60 n•m [44 ft-lb]
>
> Rear Gear Train
>
> Place the injector in the head in the proper orientation.
>
> Install the injector hold-down and tighten.
>
> **Момент затяжки · Torque Value**
> 10 n•m [89 in-lb]
>
> ### Finishing Steps
>
> Front Gear Train
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Install the high-pressure fuel supply lines. [[40-006-051-tr — Injector Supply Lines (High Pressure)|Refer to Procedure 006-051 in Section 6.]]
> - Install the fuel drain manifold. [[40-006-021-tr — Fuel Manifold (Drain)|Refer to Procedure 006-021 in Section 6.]]
> - Connect the batteries.
> - Bleed all air from the fuel system. [[40-006-051-tr — Injector Supply Lines (High Pressure)|Refer to Procedure 006-051 in Section 6.]]
> - Operate the engine and check for leaks.
>
> Rear Gear Train
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Install the fuel connector. [[40-006-052-tr — Fuel Connector (Head Mounted)|Refer to Procedure 006-052 in Section 6.]]
> - Install the rocker lever cover. [[40-003-011-tr — Rocker Lever Cover|Refer to Procedure 003-011 in Section 3.]]
> - Install the high-pressure fuel lines. [[40-006-051-tr — Injector Supply Lines (High Pressure)|Refer to Procedure 006-051 in Section 6.]]
> - Connect the batteries.
> - Bleed all the air from the fuel system. [[40-006-051-tr — Injector Supply Lines (High Pressure)|Refer to Procedure 006-051 in Section 6.]]
> - Operate the engine and check for leaks.
