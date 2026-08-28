---
aliases:
  - "Управление двигателем"
type: "Инструкция по инструменту"
doc: "3377847"
title_en: "Engine Control"
title_ru: "Управление двигателем"
released: "2006-10-05"
modified: "2006-10-06"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "37292556"
  - "37295879"
  - "80141463"
  - "80248213"
families:
  - "QSK60"
  - "QST30"
  - "QSX15"
figures: 36
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/sti/3377847.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/sti/3377847.pdf"
tags:
  - "документ/инструмент"
  - "двигатель/QSK60"
  - "двигатель/QST30"
  - "двигатель/QSX15"
  - "перевод/машинный"
---

# Engine Control
**Управление двигателем**

> [!abstract] Инструкция по инструменту · `3377847`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSK60, QST30, QSX15
> **Даты:** выпущен 2006-10-05 · изменён 2006-10-06
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/sti/3377847.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/sti/3377847.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Наименование

Управление двигателем

### Назначение

В настоящем документе приводится информация об использовании системы управления двигателем, номер детали 3163890. Управление двигателем представляет собой портативное, портативное электронное управление, используемое для запуска и управления скоростью двигателя на семействах электронных двигателей Cummins®, см. Таблицу 2. Он заменяет педаль дроссельной заслонки, панель интерфейса водителя и схемы мониторинга кода неисправности. Управление двигателем имеет положение шины данных CAN для подключения к электронному сервисному инструменту для мониторинга работы двигателя и кодов неисправностей. Требуемые проводов управления двигателем для соответствующих двигателей приобретаются отдельно. Усилители управления двигателем и проводов управления двигателем предназначены для использования как с системами батарей +12-VDC, так и +24-VDC.

Дополнительную информацию см. в следующих публикациях.

- См. процедуру[[20-014-005 — Engine Testing (Engine Dynamometer)|014-005]]или[[20-014-006 — Engine Run-in (Engine Dynamometer)|014-006]]в двигателях серий QSK19 и QSK19 CM850 с модульной системой общего пользования, бюллетень [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]

- См. процедуру 014-005 или 014-006 в Руководстве по устранению неполадок и ремонту двигателей серии QSK23, Бюллетень [[4021375 — QSK23 Troubleshooting and Repair Manual\|4021375]]

- См. процедуру 014-005 или 014-006 в Руководстве по эксплуатации двигателей серий K38, K50 и QSK50, Бюллетень [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]
- См. процедуру 014-005 или 014-006 в Руководстве по эксплуатации двигателей серии QSK45 и QSK60, Бюллетень [[4021530 — QSK45 and QSK60 Service Manual\|4021530]].

> [!note] Примечание
> Управление двигателем может быть использовано на двигателях с частотной дроссельной калибровкой, сначала загрузив линейную дроссельную калибровку в электронный модуль управления (ECM), а затем выполнив испытание, как определено в этой инструкции по инструменту обслуживания. После завершения тестирования/ремонта перезагрузите правильную калибровку частоты дроссельной заслонки.

![[22c00132.png]]

| Таблица 1, Управление двигателем, номер детали 3163890 |  |  |  |
|---|---|---|---|
| Пункт | Номер детали | Наименование | Количество |
| 1 | 3163890 | Управление двигателем | 1 |

| Таблица 2, Предметы, используемые с управлением двигателем, приобретенные отдельно |  |  |  |
|---|---|---|---|
| Пункт | Номер детали | Наименование | Количество |
| 2 | 3163891 | Усилитель электропроводки управления двигателем (QSK19, QSK23, QSK45 и QSK60) | 1 |
| 2 | 4918643 | Усилитель электропроводки двигателя (QSK19, QSK38, QSK50 и QSK60 с электронно приводимым в действие топливным форсункой) | 1 |
| 2 | 3163892 | Усилитель электропроводки управления двигателем (подпись, ISX, QSX15 и ISM) | 1 |
| 2 | 3164251 | Усилитель электропроводки управления двигателем (ISB, ISC и ISL) | 1 |
| 2 | 3163894 | Управляющая проводка двигателя (M11 и N14 CELECTTM Plus) | 1 |
| 2 | 3163818 | Усилитель электропроводки управления двигателем (L10, M11 и N14 CELECTTM) | 1 |
| 2 | 3164036 | Управляющая проводка двигателя (ISB e и ISB четырехцилиндровая) | 1 |
| 2 | 3164324 | Усилитель электропроводки управления двигателем (QST30 Industrial) | 1 |
| 2 | 3164820 | Управляющая проводка двигателя (QST30 G-Drive) | 1 |
| 2 | 3164242 | Усилитель электропроводки управления двигателем (подпись и ISX с CM870, ISB с CM850 и ISM с CM870) | 1 |
| 2 | 3165084 | Усилитель электропроводки двигателя (480C-E Marine) | 1 |
| 2 | 4918272 | Управляющая проводка двигателя (B Gas Plus, C Gas Plus, L Gas Plus и B LPG Plus) | 1 |
| 3 | 3163099 | Адаптерный комплект INLINETM | 1 |
| 3 | 3163583 | Адаптерный комплект 1 | 1 |
| 3 | 3163682 | Адаптер InLINETM 2 | 1 |
| 3 | 4918190 | InLINETM 4 Адаптерный комплект | 1 |
| 3 | 4918416 | INLINETM 5 Адаптерный комплект | 1 |
| 4 |  | INSITETM электронный сервис оснащён персональным компьютером | 1 |
| **Не показана** | 3163895 | Электрический кабель (6,1 м \[20 футов \] удлинительный кабель) | 1 |
| **Не показана** | 3164630 | Ford/Sterling OEM адаптерный кабель | 1 |
| **Не показана** | 3164653 | - электропроводка, адаптер шины данных CAN (ISB, ISC и ISL с CM850 и ISM и ISX с CM870) | 1 |

> [!danger] ОПАСНО
> При использовании управления двигателем на двигателе, установленном в транспортном средстве или оборудовании, убедитесь, что трансмиссия находится в нейтральном положении или трансмиссия отключена, стояночный тормоз включен, а колеса заблокированы. Неспособность сделать это может привести к повреждению транспортного средства или оборудования, серьезным травмам или смерти.

Управление двигателем предназначено только для **диагностических целей**. Он может использоваться для работы двигателя только в следующих ситуациях.

- Двигатель на динамометре двигателя
- Двигатель в транспортном средстве или оборудовании, которое находится в стационарном состоянии
- Двигатель в транспортном средстве или оборудовании на динамометрическом шасси.

![[22d00166.png]]

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

> [!note] Примечание
> Отключите кабели аккумулятора перед началом следующей процедуры.

Отсоедините электропроводку OEM от электронного модуля управления (ECM) (если применимо).

![[22c00124.png]]

> [!warning] ОСТОРОЖНО
> Не выдувайте сжатый воздух в порты или разъемы ECM. Сжатый воздух может содержать влагу (из-за конденсации), которая может повредить ECM.

Используйте быстросушливый электрический контактный очиститель, номер детали 3824510, для удаления всей грязи и влаги из разъемных портов ECM.

![[19800830.png]]

> [!note] Примечание
> CELECTTM и CELECTTM Plus используют различные электропроводки управления двигателем. Используйте соответствующую проводку управления двигателем.

Вставьте в сосуд "В" ECM проводку управления двигателем 28-контактного разъема AMP (1). Тщательно выровняйте и запустите соединительные крепежные болты в ECM вручную.

Затяните болты.

> [!tip] Момент затяжки
> 2 Н·м [18 фунт-дюйм]

![[22c00119.png]]

> [!note] Примечание
> Активный код 431 по умолчанию будет зарегистрирован при использовании управления двигателем на двигателе CELECTTM. Это не повлияет на производительность. Код 431 после проверки.

Подключите 3-контактный разъем Weather-Pack (2) к разъёму проводов приведения в действие (непереключенный аккумулятор).

Подключите 9-контактный разъем для 9-контактной проводов управления двигателем Deutsch для CELECTTM или 21-контактный разъем для CELECTTM Plus (3) к разъёму для соединительной проводов датчика.

![[22c00121.png]]

Выровнять проводку управления двигателем с помощью 50-контактных разъемов Deutsch с сосудом «B» ECM и вставить разъем в ECM.

Тщательно выровняйте и запустите соединительные крепежные болты в ECM вручную.

Затяните болт.

> [!tip] Момент затяжки
> 2 Н·м [18 фунт-дюйм]

![[19901103.png]]

Подключите 2-контактный разъем Metri-Pack к соединительному разъему датчика воды в топливе.

Удалите шортинговый колпачок, номер детали 3164250, из 4-контактного разъема Weather-Pack, если есть необходимость, для подключения нагревателя сетки.

Подключите 4-контактный разъем Weather-Pack к разъему нагревателя сетки.

![[19901104.png]]

> [!note] Примечание
> Некоторые двигатели, установленные на шасси Ford и Sterling, используют 16-контактный OEM-разъем Ford. Если это так, используйте адаптер Ford/Sterling OEM-разъема, номер детали 3164630.

Подключите к ремню 23-контактный разъем Deutsch к ремню электропроводки двигателя.

![[22c00140.png]]

Удалите 3-контактный резисторный колпачок Deutsch (колпачок будет иметь синюю вставку) из проводной упряжки.

Подключите 3-контактный разъем Deutsch к разъему J1939 на ремне электропроводки двигателя.

3-контактный резистор Deutsch с концевым резистором должен быть установлен после того, как убрана проводка управления двигателем. Если крышка сломана или была неправильно расположена, замените резисторную крышку, номер детали 3163051.

![[19901106.png]]

Выровнять проводку управления двигателем с помощью 50-контактных разъемов Deutsch с сосудом OEM ECM и вставить разъем в ECM.

Тщательно выровняйте и запустите соединительные крепежные болты в ECM вручную.

Затяните болт.

> [!tip] Момент затяжки
> 2 Н·м [18 фунт-дюйм]

![[19c01028.png]]

Отсоедините жгут электропроводки двигателя от OEM-проводов.

Подключите электропроводку управления двигателем к электропроводке двигателя.

![[19c01029.png]]

Отсоедините проводные упряжки OEM 21-контактный и 31-контактный разъемы Deutsch от электропроводки двигателя.

Подключите к ремню 21-контактную и 31-контактную проводку управления двигателем к ремню электропроводки двигателя.

![[19a00768.png]]

Удалите 3-контактный резисторный колпачок Deutsch (колпачок будет иметь синюю вставку) из проводной упряжки.

Подключите 3-контактный разъем Deutsch для управления двигателем к разъему J1939 для проводов двигателя.

3-контактный резистор Deutsch с концевым резистором должен быть установлен после того, как убрана проводка управления двигателем. Если крышка сломана или была неправильно расположена, замените резисторную крышку, номер детали 3163051.

![[19a00770.png]]

> [!note] Примечание
> Для контроля двигателя QST30 G-Drive с помощью электронного сервисного инструментария INSITETM подключите к 9-контактному разъему шины данных CAN на двигателе и **не** разъему на управлении двигателем.

Выровняйте проводку управления двигателем с помощью 40-контактных разъемов Deutsch с сосудом «B» ECM и вставьте разъем в ECM. Тщательно выровняйте и запустите соединительные крепежные болты в ECM вручную.

Затяните болт.

> [!tip] Момент затяжки
> 2 Н·м [18 фунт-дюйм]

![[19400401.png]]

Отсоедините проводные упряжки OEM 23-контактных и 31-контактных разъемов Deutsch от электропроводки двигателя.

Подключите к ремню 23-контактной и 31-контактной проводов управления двигателем разъёмы Deutsch к ремню электропроводки двигателя.

![[19a00768.png]]

Тщательно управлять защелкой разъема и отсоединять разъем.

Подключите ремень управления двигателем к 89-контактному разъему OEM двигателя на ECM.

![[22d00078.png]]

Подключите 2-контактный разъем Metri-Pack к соединительному разъему датчика воды в топливе.

Удалите шортинговый колпачок, номер детали 3164250, из 4-контактного разъема Weather-Pack, если есть необходимость, для подключения нагревателя сетки.

Подключите 4-контактный разъем Weather-Pack к разъему нагревателя сетки.

![[19901104.png]]

Выровнять проводку управления двигателем с помощью 50-контактных разъемов Deutsch с сосудом OEM ECM и вставить разъем в ECM. Тщательно выровняйте и запустите соединительные крепежные болты к ECM вручную.

Затяните болт.

> [!tip] Момент затяжки
> 2 Н·м [18 фунт-дюйм]

Отсоедините 4-контактный разъем Deutsch от ECM и соедините 4-контактный разъем Deutsch на ремне управления двигателем.

![[22100102.png]]

> [!warning] ОСТОРОЖНО
> Убедитесь, что крышка установлена на 1-контактный разъем Weather-Pack и / или 2-контактный разъем Deutsch, если разъемы не используются. Неспособность сделать это может привести к электрическим повреждениям.

> [!note] Примечание
> 1-контактный разъем Weather-Pack может **не** использоваться на ISX с CM870 или ISB с CM850.

> [!note] Примечание
> 2-контактный насос Deutsch может **не** использоваться на ISB с CM850.

Подключите 2-контактный разъем Deutsch на ремне управления двигателем к подъёмному насосу силового соединения на ремне электропроводки двигателя над ECM на ISX с CM870.

![[22c00168.png]]

Выровнять проводку управления двигателем с помощью 50-контактных разъемов Deutsch с сосудом OEM ECM и вставить разъем в ECM. Тщательно выровняйте и запустите соединительные крепежные болты к ECM вручную.

Затяните болт.

> [!tip] Момент затяжки
> 2 Н·м [18 фунт-дюйм]

Отсоедините 4-контактный разъем Deutsch от ECM.

![[22400159.png]]

> [!warning] ОСТОРОЖНО
> Убедитесь, что крышка установлена на 2-контактном разъеме Weather-Pack и/или 2-контактном разъеме Deutsch, если разъемы не используются. Неспособность сделать это может привести к электрическим повреждениям.

> [!note] Примечание
> 2-контактное подключение к насосу Deutsch может **не** использоваться на ISM с CM870.

Подключите 4-контактные разъемы Deutsch и 1-контактные разъемы Weather-Pack (1) на адаптере электропроводки, Номер детали 3164653, к соединительным разъемам на ремне электропроводки управления двигателем, Номер детали 3164242. Подключите 4-контактный разъем Deutsch на адаптерной проводах ремня, Номер детали 3164653, к соединительному разъему на ECM.

![[22600214.png]]

Подключите 3-контактный разъем Weather-Pack (1) к разъёму дросселя на ремне электропроводки двигателя. Подключите 3-контактный разъем Weather-Pack (2) к разъему переключателя проверки спаривания на ремне проводов двигателя. Подключите 4-контактный разъем Weather-Pack (3) к соединительному разъему питания ECM на ремне электропроводки двигателя. Подключите 40-контактный разъем Deutsch (4) к соединительному разъему на 40-контактной проводах двигателя.

![[22d00180.png]]

Подключите черную проводку аллигатора к ремню управления двигателем к блоку двигателя, чтобы достичь электрического заземления.

![[19c01031.png]]

> [!warning] ОСТОРОЖНО
> Не подключайте зажим аллигатора к стартовому моторному соленоидному терминалу «S». Это может привести к повреждению оборудования.

Если **не** уже оборудован, установите и проведите магнитный стартер.

Заткните разъем аллигатора к положительному (+) концевому клемму катушки магнитного стартера.

![[22400055.png]]

Если используется воздушный стартер, перевяжите красный провод в петлю и закрепите петлю к электропроводке управления двигателем, чтобы защитить его от электрического короткого.

![[19c01032.png]]

Если оборудована стартерная локаутная реле, подключите зеленую проволоку аллигатора к терминалу «S».

Если **не** оборудован реле блокировки стартера, введите зеленый провод в петлю и закрепите петлю на ремне электропроводки управления двигателем, чтобы защитить его от электрического короткого замыкания.

![[19c01032.png]]

> [!note] Примечание
> Если для подключения управления двигателем требуется дополнительная длина кабеля, используйте электрический кабель, номер детали 3163895.

Подключите проводку управления двигателем (2) к управлению двигателем. Персональный компьютер, оснащенный инструментами электронной службы INSITETM, может использоваться для мониторинга цепей для правильной работы. Подключите соответствующий комплект адаптера шины данных INLINETM CAN (3) и персональный компьютер к разъему шины данных CAN управления двигателем.

![[22c00125.png]]

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Для уменьшения возможности дуги сначала удалите отрицательный (-) кабель батареи и прикрепите отрицательный (-) кабель батареи последним.

> [!note] Примечание
> Для Signature и ISX с CM870, ISB с CM850 или ISM с CM870 с упряжкой для проводов управления двигателем, номер детали 3164242, подсоедините черный провод к шпильке наземного блока.

Прикрепите проводку управления двигателем с помощью кольцевого терминала красного провода к положительному (+) терминалу батареи.

Прикрепите проводку управления двигателем с помощью кольцевого терминала черного провода к отрицательному (-) терминалу батареи.

![[22c00141.png]]

> [!warning] ОСТОРОЖНО
> Проверить, что красный провод подключен к положительному (+) клемме батареи, а черный провод подключен к отрицательному (-) клемме батареи. Невыполнение этого требования может привести к повреждению оборудования или двигателя.

Силовой свет будет освещаться при подаче питания и переключатель зажигания поворачивается в положение аксессуара или Включено.

Если силовой свет не освещается, верните переключатель зажигания в положение выключения. Проверить, что красный провод подключен к положительному (+) клемме батареи, а черный провод подключен к отрицательному (-) клемме батареи.

Переведите замок зажигания в положение ON.

![[22c00127.png]]

Световые индикаторы на управлении двигателем, STOP, WARN, MAINT, WIF и WAIT TO START, будут освещаться, если это применимо. Световые индикаторы будут светиться в течение примерно 30 секунд. Если не будет найдено кодов неисправностей, световые индикаторы погаснут.

Если индикатор STOP (красный) или индикатор WARN (желтый) продолжает освещаться, используйте инструмент для электронного обслуживания INSITETM и соответствующую служебную литературу для диагностики кода неисправности двигателя.

![[22c00128.png]]

> [!note] Примечание
> Дроссель можно вернуть в положение холостого хода, надавив на ручку дросселя в любое время.

Верните дроссель в положение холостого хода.

Переведите замок зажигания в положение ON.

![[22c00155.png]]

Вращайте ручку дроссельной заслонки полностью **против часовой стрелки**. Нажмите на ручку дроссельной заслонки, чтобы вернуть дроссель в положение холостого хода.

Повторите этот шаг три раза.

Переключатель зажигания в положение выключения в течение 30 секунд.

![[22c00156.png]]

> [!warning] ОСТОРОЖНО
> Проверьте уровень охлаждающей жидкости и моторного масла перед запуском и работой двигателя. Невыполнение этого требования может привести к повреждению двигателя.

> [!note] Примечание
> На двигателях B Gas Plus, C Gas Plus, L Gas Plus и B LPG Plus, оснащенных топливным соленоидом, переключатель зажигания транспортного средства **должен** находиться в положении ON.

Включите переключатель зажигания в положение START до запуска двигателя и отпустите переключатель зажигания.

![[22c00129.png]]

> [!note] Примечание
> Двигатель может быть возвращен в бездействие в любое время, нажав на ручку дросселя.

Медленно поверните ручку дроссельной заслонки **против часовой стрелки**, чтобы **увеличить** обороты двигателя.

Медленно поверните ручку дроссельной заслонки **по часовой стрелке**, чтобы **уменьшить** обороты двигателя.

![[22c00130.png]]

Включите переключатель зажигания в положение выключения, чтобы остановить двигатель.

![[22c00131.png]]


> [!quote]- Original (English) · английский оригинал
> ### Description
>
> Engine Control
>
> ### Purpose
>
> This document provides information for the use of engine control, Part Number 3163890. The engine control is a portable, handheld electronic control, used to start and control engine speed on the Cummins® electronic engine families, refer to Table 2. It replaces the throttle pedal, driver interface panel, and fault code monitoring circuits. The engine control has a datalink provision to connect to an electronic service tool to monitor engine operation and fault codes. The required engine control harnesses for the appropriate engines are purchased separately. The engine control and engine control harnesses are designed to be used with both +12-VDC and +24-VDC battery systems.
>
> For additional information, see the following publications.
>
> - Refer to Procedure [[20-014-005 — Engine Testing (Engine Dynamometer)|014-005]] or [[20-014-006 — Engine Run-in (Engine Dynamometer)|014-006]] in the QSK19 and QSK19 CM850 Modular Common Rail System Series Engines, Bulletin [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]
>
> - Refer to Procedure [[89-014-005 — Engine Testing (Engine Dynamometer)|014-005]] or [[89-014-006 — Engine Run-in (Engine Dynamometer)|014-006]] in the Troubleshooting and Repair Manual QSK23 Series Engines, Bulletin [[4021375 — QSK23 Troubleshooting and Repair Manual\|4021375]]
>
> - Refer to Procedure 014-005 or 014-006 in the Service Manual K38, K50, and QSK50 Series Engines, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]
> - Refer to Procedure [[56-014-005-tr — Engine Testing (Engine Dynamometer)|014-005]] or [[56-014-006-tr — Engine Run-in (Engine Dynamometer)|014-006]] in the Service Manual QSK45 and QSK60 Series Engines, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]].
>
> **Note · Примечание**
> The engine control can be used on engines with frequency throttle calibrations by first downloading a linear throttle calibration to the electronic control module (ECM) and then performing the test as identified within this Service Tool Instruction. After the testing/repair is complete, reload the correct frequency throttle calibration.
>
> | Table 1, Engine Control, Part Number 3163890 |  |  |  |
> |---|---|---|---|
> | Item | Part Number | Description | Quantity |
> | 1 | 3163890 | Engine control | 1 |
>
> | Table 2, Items Used with the Engine Control, Purchased Separately |  |  |  |
> |---|---|---|---|
> | Item | Part Number | Description | Quantity |
> | 2 | 3163891 | Engine control harness (QSK19, QSK23, QSK45, and QSK60) | 1 |
> | 2 | 4918643 | Engine control harness (QSK19, QSK38, QSK50, and QSK60 with electronically actuated injectors) | 1 |
> | 2 | 3163892 | Engine control harness (Signature, ISX, QSX15, and ISM) | 1 |
> | 2 | 3164251 | Engine control harness (ISB, ISC, and ISL) | 1 |
> | 2 | 3163894 | Engine control harness (M11 and N14 CELECT™ Plus) | 1 |
> | 2 | 3163818 | Engine control harness (L10, M11, and N14 CELECT™) | 1 |
> | 2 | 3164036 | Engine control harness (ISB e and ISB four-cylinder) | 1 |
> | 2 | 3164324 | Engine control harness (QST30 Industrial) | 1 |
> | 2 | 3164820 | Engine control harness (QST30 G-Drive) | 1 |
> | 2 | 3164242 | Engine control harness (Signature and ISX with CM870, ISB with CM850, and ISM with CM870) | 1 |
> | 2 | 3165084 | Engine control harness (480C-E Marine) | 1 |
> | 2 | 4918272 | Engine control harness (B Gas Plus, C Gas Plus, L Gas Plus, and B LPG Plus) | 1 |
> | 3 | 3163099 | INLINE™ adapter kit | 1 |
> | 3 | 3163583 | INLINE™ 1 adapter kit | 1 |
> | 3 | 3163682 | INLINE™ 2 adapter kit | 1 |
> | 3 | 4918190 | INLINE™ 4 adapter kit | 1 |
> | 3 | 4918416 | INLINE™ 5 adapter kit | 1 |
> | 4 |  | INSITE™ electronic service tool-equipped personal computer | 1 |
> | **Not** shown | 3163895 | Electrical cable (6.1-m \[20-ft\] extension cable) | 1 |
> | **Not** shown | 3164630 | Ford/Sterling OEM connector adapter cable | 1 |
> | **Not** shown | 3164653 | Harness, datalink adapter (ISB, ISC, and ISL with CM850 and ISM and ISX with CM870) | 1 |
>
> **WARNING · Опасно**
> When using the engine control on an engine installed in a vehicle or equipment, make certain that the transmission is in neutral or the driveline is disengaged, the parking brake is on, and the wheels are blocked. Failure to do so can result in vehicle or equipment damage, serious personal injury, or death.
>
> The engine control is designed for **diagnostic purposes only**. It can be used to operate an engine **only** under the following situations.
>
> - An engine on an engine dynamometer
> - An engine in a vehicle or equipment that is stationary
> - An engine in a vehicle or equipment on a chassis dynamometer.
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> **Note · Примечание**
> Disconnect the battery cables before beginning the following procedure.
>
> Disconnect the OEM harness from the electronic control module (ECM) (if applicable).
>
> **CAUTION · Осторожно**
> Do not blow compressed air into the ECM ports or connectors. Compressed air can contain moisture (due to condensation) that can damage the ECM.
>
> Use quick-dry electrical contact cleaner, Part Number 3824510, to remove all dirt and moisture from the ECM connector ports.
>
> **Note · Примечание**
> CELECT™ and CELECT™ Plus use different engine control harnesses. Use the appropriate engine control harness.
>
> Insert the engine control harness 28-pin AMP connector (1) into the “B” receptacle of the ECM. Carefully align and start the connector mounting capscrews into the ECM by hand.
>
> Tighten the capscrews.
>
> **Момент затяжки · Torque Value**
> 2 n•m [18 in-lb]
>
> **Note · Примечание**
> An active Fault Code 431 will be logged when using the engine control on a CELECT™ engine. It will have no effect on performance. Clear Fault Code 431 after the test.
>
> Connect the engine control harness 3-pin Weather-Pack connector (2) to the mating actuator harness (unswitched battery power) connector.
>
> Connect the engine control harness 9-pin Deutsch connector for CELECT™ or the 21-pin connector for CELECT™ Plus (3) to the mating sensor harness connector.
>
> Align the engine control harness 50-pin Deutsch connector slots with the “B” receptacle of the ECM and insert the connector into the ECM.
>
> Carefully align and start the connector mounting capscrew into the ECM by hand.
>
> Tighten the capscrew.
>
> **Момент затяжки · Torque Value**
> 2 n•m [18 in-lb]
>
> Connect the engine control harness 2-pin Metri-Pack connector to the mating water-in-fuel sensor connector.
>
> Remove the shorting cap, Part Number 3164250, from the 4-pin Weather-Pack connector, if the need exists, to connect the grid heater.
>
> Connect the 4-pin Weather-Pack connector to the grid heater connector.
>
> **Note · Примечание**
> Some engines installed in Ford and Sterling chassis use a Ford 16-pin OEM connector. If so equipped, use the Ford/Sterling OEM connector adapter cable, Part Number 3164630.
>
> Connect the engine control harness 23-pin Deutsch connector to the engine wiring harness.
>
> Remove the 3-pin Deutsch terminating resistor cap (cap will have a blue insert) from the wiring harness.
>
> Connect the engine control harness 3-pin Deutsch connector to the J1939 connector on the engine wiring harness.
>
> The 3-pin Deutsch terminating resistor cap **must** be installed after the engine control harness is removed. If the cap is broken or has been misplaced, replace with resistor cap, Part Number 3163051.
>
> Align the engine control harness 50-pin Deutsch connector slots with the OEM receptacle of the ECM and insert the connector into the ECM.
>
> Carefully align and start the connector mounting capscrew into the ECM by hand.
>
> Tighten the capscrew.
>
> **Момент затяжки · Torque Value**
> 2 n•m [18 in-lb]
>
> Disconnect the engine wiring harness from the OEM harness.
>
> Connect the engine control harness to the engine wiring harness.
>
> Disconnect the OEM harness 21-pin and 31-pin Deutsch connectors from the engine harness.
>
> Connect the engine control harness 21-pin and 31-pin Deutsch connectors to the engine wiring harness.
>
> Remove the 3-pin Deutsch terminating resistor cap (cap will have a blue insert) from the wiring harness.
>
> Connect the engine control harness 3-pin Deutsch connector to the J1939 connector of the engine wiring harness.
>
> The 3-pin Deutsch terminating resistor cap **must** be installed after the engine control harness is removed. If the cap is broken or has been misplaced, replace with resistor cap, Part Number 3163051.
>
> **Note · Примечание**
> To monitor the QST30 G-Drive engine with INSITE™ electronic service tool, connect to the 9-pin datalink connector on the engine and **not** the connector on the engine control.
>
> Align the engine control harness 40-pin Deutsch connector slots with the “B” receptacle of the ECM and insert the connector into the ECM. Carefully align and start the connector mounting capscrew into the ECM by hand.
>
> Tighten the capscrew.
>
> **Момент затяжки · Torque Value**
> 2 n•m [18 in-lb]
>
> Disconnect the OEM harness 23-pin and 31-pin Deutsch connectors from the engine harness.
>
> Connect the engine control harness 23-pin and 31-pin Deutsch connectors to the engine wiring harness.
>
> Carefully operate the connector latch and disconnect the connector.
>
> Connect the engine control harness to the 89-pin OEM engine connector on the ECM.
>
> Connect the engine control harness 2-pin Metri-Pack connector to the mating water-in-fuel sensor connector.
>
> Remove the shorting cap, Part Number 3164250, from the 4-pin Weather-Pack connector, if the need exists, to connect the grid heater.
>
> Connect the 4-pin Weather-Pack connector to the grid heater connector.
>
> Align the engine control harness 50-pin Deutsch connector slots with the OEM receptacle of the ECM and insert the connector into the ECM. Carefully align and start the connector mounting capscrew to the ECM by hand.
>
> Tighten the capscrew.
>
> **Момент затяжки · Torque Value**
> 2 n•m [18 in-lb]
>
> Disconnect the engine wiring harness 4-pin Deutsch connector from the ECM and connect the 4-pin Deutsch connector on the engine control harness.
>
> **CAUTION · Осторожно**
> Make certain that the cap is installed on the 1-pin Weather-Pack connector and/or the 2-pin Deutsch connector, if the connectors are not used. Failure to do so can cause electrical damage.
>
> **Note · Примечание**
> The 1-pin Weather-Pack connector can **not** be used on the ISX with CM870 or the ISB with CM850.
>
> **Note · Примечание**
> The 2-pin Deutsch lift pump power connection can **not** be used on the ISB with CM850.
>
> Connect the 2-pin Deutsch connector on the engine control harness to the lift pump power connection on the engine wiring harness above the ECM on the ISX with CM870.
>
> Align the engine control harness 50-pin Deutsch connector slots with the OEM receptacle of the ECM and insert the connector into the ECM. Carefully align and start the connector mounting capscrew to the ECM by hand.
>
> Tighten the capscrew.
>
> **Момент затяжки · Torque Value**
> 2 n•m [18 in-lb]
>
> Disconnect the engine wiring harness 4-pin Deutsch connector from the ECM.
>
> **CAUTION · Осторожно**
> Make certain that the cap is installed on the 2-pin Weather-Pack connector and/or the 2-pin Deutsch connector, if the connectors are not used. Failure to do so can cause electrical damage.
>
> **Note · Примечание**
> The 2-pin Deutsch lift pump power connection can **not** be used on the ISM with CM870.
>
> Connect the 4-pin Deutsch and 1-pin Weather-Pack (1) connectors on the electrical wiring harness adapter, Part Number 3164653, to the mating connectors on the engine control harness, Part Number 3164242. Connect the 4-pin Deutsch connector on the adapter harness, Part Number 3164653, to the mating connector on the ECM.
>
> Connect the 3-pin Weather-Pack connector (1) to the mating throttle connector on the engine harness. Connect the 3-pin Weather-Pack connector (2) to the mating idle validation switch connector on the engine harness. Connect the 4-pin Weather-Pack connector (3) to the mating ECM power connector on the engine harness. Connect the 40-pin Deutsch connector (4) to the mating connector on the 40-pin engine harness.
>
> Connect the black-wire alligator clip of the engine control harness to the engine block to achieve electrical ground.
>
> **CAUTION · Осторожно**
> Do not connect the alligator clip to the starter motor solenoid “S” terminal. Doing so can cause equipment damage.
>
> If **not** already equipped, install and wire a magnetic starter switch.
>
> Clip the alligator connector to the positive (+) coil terminal of the magnetic starter switch.
>
> If an air starter is being used, coil the red wire into a loop and secure the loop to the engine control harness to protect it from an electrical short.
>
> If equipped with a starter lockout relay connect the green wire alligator clip to the “S” terminal.
>
> If **not** equipped with a starter lockout relay, coil the green wire into a loop and secure the loop to the engine control harness to protect it from an electrical short.
>
> **Note · Примечание**
> If additional cable length is needed to connect the engine control, use electrical cable, Part Number 3163895.
>
> Connect the engine control harness (2) to the engine control. An INSITE™ electronic service tool-equipped personal computer can be used to monitor circuits for proper operation. Connect the appropriate INLINE™ datalink adapter kit (3) and a personal computer to the datalink connector of the engine control.
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first, and attach the negative (-) battery cable last.
>
> **Note · Примечание**
> For Signature and ISX with CM870, ISB with CM850, or ISM with CM870 engine control harness, Part Number 3164242, connect the black wire to the block ground stud.
>
> Attach the engine control harness using the ring terminal of the red wire to the positive (+) terminal of the battery.
>
> Attach the engine control harness using the ring terminal of the black wire to the negative (-) terminal of the battery.
>
> **CAUTION · Осторожно**
> Verify the red wire is connected to the positive (+) battery terminal and the black wire is connected to the negative (-) battery terminal. Failure to do so can result in equipment or engine damage.
>
> The power light will illuminate when power is supplied and the keyswitch is turned to the accessory or ON position.
>
> If the power light does **not** illuminate, return the keyswitch to the OFF position. Verify the red wire is connected to the positive (+) battery terminal and the black wire is connected to the negative (-) battery terminal.
>
> Turn the keyswitch to the ON position.
>
> Light indicators on the engine control, STOP, WARN, MAINT, WIF, and WAIT TO START, will illuminate if applicable. The light indicators will illuminate for approximately 30 seconds. If no fault codes are found, the light indicators will extinguish.
>
> If the STOP light indicator (red) or WARN light indicator (yellow) continues to illuminate, use INSITE™ electronic service tool and the appropriate service literature to diagnose the engine fault code.
>
> **Note · Примечание**
> The throttle can be returned to the idle position by pushing down on the throttle knob at any time.
>
> Return the throttle to the idle position.
>
> Turn the keyswitch to the ON position.
>
> Rotate the throttle knob fully **counterclockwise**. Push down on the throttle knob to return the throttle to the idle position.
>
> Repeat this step three times.
>
> Turn the keyswitch to the OFF position for 30 seconds.
>
> **CAUTION · Осторожно**
> Check coolant and lubricating oil levels before starting and operating engine. Failure to do so can result in engine damage.
>
> **Note · Примечание**
> On the B Gas Plus, C Gas Plus, L Gas Plus and B LPG Plus engines equipped with a fuel solenoid, the vehicle ignition switch **must** be in the ON position.
>
> Turn the keyswitch to the START position until the engine starts and release the keyswitch.
>
> **Note · Примечание**
> The engine can be returned to idle at any time by pushing in on the throttle knob.
>
> Slowly rotate the throttle knob **counterclockwise** to **increase** the engine rpm.
>
> Slowly rotate the throttle knob **clockwise** to **decrease** the engine rpm.
>
> Turn the keyswitch to the OFF position to stop the engine.
