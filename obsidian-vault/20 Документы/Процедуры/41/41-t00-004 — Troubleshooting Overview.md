---
aliases:
  - "Поиск неисправностей — обзор"
type: "Процедура"
doc: "41-t00-004"
title_en: "Troubleshooting Overview"
title_ru: "Поиск неисправностей — обзор"
modified: "2012-06-07"
engines:
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "3666003"
figures: 2
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/41/41-t00-004.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/41-t00-004.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/41"
  - "перевод/машинный"
---

# Troubleshooting Overview
**Поиск неисправностей — обзор**

> [!abstract] Процедура · `41-t00-004`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[3666003 — C Troubleshooting and Repair Manual|3666003]]
> **Секции:** Section TS - Troubleshooting Symptoms
> **Даты:** изменён 2012-06-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/41/41-t00-004.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/41-t00-004.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Удобство вождения / низкая мощность - форма жалобы клиента

Имя клиента / Компания \_\_

1. Как возникла проблема? Внезапно \_\_\_\___ Постепенно \_\_
2. В какой час/миле началась проблема? Часы \_\_

- После ремонта двигателя? Да \_\_
- После ремонта оборудования? Да _
- После смены оборудования? Да _
- После изменения выбранных программируемых параметров? Да \_\_
- Если да, то что было исправлено и когда? \_\\___\_
- Не испытывает ли автомобиль также плохую экономию топлива? Да \_\_

Ответьте на вопросы 4-8 с помощью выбора (A-F), перечисленного ниже. Обведите букву или буквы, которые лучше всего описывают жалобу.

А. По сравнению с флотом

В. По сравнению с конкуренцией

C - по сравнению с предыдущим двигателем

D - личные ожидания

E - Will **not** pull on hill (не будет тянуть на холм)

F - будет **не** тянуться по ровной местности

B C D E F

A - Может ли автомобиль достичь ожидаемой скорости движения? Да \_\_

B - Какая скорость нужна? rpm/mph\_\\_____

C - Какая скорость достигается? rpm/mph\_\\_____

D - Валовой вес транспортного средства \_\_\_

A B C D

Способен ли автомобиль выдержать нагрузку? Да \_\_

Когда?

\_\_

\_\_

\_\_

\_\_

Если вопрос 4 или 5 не был решен, заполните список производных / низких / высоких потреблений и идите на низкую тягу к симптому.

Медленно ли автомобиль ускоряется или реагирует? Да \_\_

С остановки? Да \_\_

После смены? Да \_\_

Перед сменой? Да \_\_

Никакой смены? Да \_\_

Не колеблется ли автомобиль после длительных периодов замедления или движения? Да \_\_

Если вопрос 6 или 7 был ДА, заполните список КИП/Низкая мощность/ПРЕДОСТАВЛЕНИЕ ТРУДНОГО ПОЛУЧЕНИЯ И идите к бедной ТРЕЙКЕ СИМПТОМЫ ОТВЕТСТВЕННОСТИ/ОТВЕТСТВЕННОСТИ.

Дополнительные комментарии:

\_

Эту страницу можно скопировать для удобства.

### Движущая способность - общая информация

Движимость - это термин, который в целом описывает характеристики транспортного средства на дороге. Проблемы с управляемостью двигателя могут быть вызваны несколькими различными факторами. Некоторые из этих факторов связаны с двигателем, а некоторые - не связаны.

Перед устранением неполадок важно определить точную жалобу и имеет ли двигатель реальную проблему с управляемостью или он просто не соответствует ожиданиям водителя. Форма жалобы на управляемость с низким энергопотреблением представляет собой ценный список вопросов, которые должны быть использованы для оказания помощи технику по обслуживанию в определении типа проблемы управляемости транспортного средства. Заполните контрольный список перед устранением неполадок. Форма может быть найдена в конце этого раздела. Если двигатель соответствует заводским спецификациям, но не соответствует ожиданиям клиента, объясните клиенту, что с автомобилем и почему ничего не случилось.

Диаграммы симптомов устранения неполадок были созданы для разделения проблем с управляемостью на два разных симптома: Мощность двигателя низкая, а ускорение или реакция двигателя плохая.

Низкая мощность - это термин, который используется в этой области для описания многих различных проблем производительности. Однако в данном руководстве низкая мощность определяется как неспособность двигателя вырабатывать мощность, необходимую для перемещения транспортного средства со скоростью, которая может разумно ожидаться при заданных условиях нагрузки, класса, ветра и т.д. Низкая мощность обычно вызвана отсутствием потока топлива, что может быть вызвано любым из следующих факторов:

- Отсутствие полного хода педали дроссельной заслонки
- Неудачный датчик импульса
- Чрезмерное ограничение впуска, впуска, выхлопа или дренажа топлива
- Линии всасывания топливного насоса.

Низкая мощность — это неспособность автомобиля удовлетворительно разгоняться от остановки или нижней части класса. См. дерево симптомов устранения неполадок в разделе TS для надлежащих процедур для определения и исправления проблемы с низким энергопотреблением. График начинается с основных элементов, которые могут вызвать снижение мощности.

В настоящем руководстве описано плохое ускорение или реакция как неспособность транспортного средства удовлетворительно разгоняться от остановки или снизу класса. Это также может быть задержка в ускорении во время попытки проехать или обогнать другое транспортное средство при условиях, меньших номинальной скорости и нагрузки. Плохое ускорение или ответ трудно устранить, поскольку это может быть вызвано такими факторами, как:

- Факторы, связанные с двигателем или насосом
- Методика водителя
- Неправильное переключение передач
- Неправильное применение двигателя
- Изношенное сцепление или сцепление.

Неудачное ускорение или реакция двигателя могут быть вызваны несколькими различными факторами, такими как:

- Неудачный датчик импульса
- Чрезмерное ограничение дренажа
- Помехи для дроссельной завязки.

См. дерево симптомов плохого устранения неполадок в разделе TS для надлежащих процедур для определения и исправления жалобы на плохое ускорение или ответ. Дополнительную информацию см. в Troubleshooting Driveability Complaints, Bulletin Number 3387245.

### Диагностика шума двигателя - общая информация

> [!note] Примечание
> При диагностике проблем с шумом двигателя убедитесь, что шумы, вызванные аксессуарами, такими как воздушный компрессор и взлет мощности, не принимаются за шумы двигателя. Удалите дополнительные приводные ремни, чтобы устранить шум, вызванный этими устройствами. Шум также будет распространяться на другие металлические детали, не связанные с проблемой. Использование стетоскопа может помочь определить местонахождение шума двигателя.

Шумы двигателя, слышные при скорости коленчатого вала, оборотах двигателя, — это шумы, связанные с коленчатым валом, стержнями, поршнями и поршневыми штифтами. Шумы, слышанные на скорости распредвала, половине оборотов двигателя, связаны с клапанным поездом. Портативный цифровой тахометр может помочь определить, связан ли шум с компонентами, работающими на скорости коленчатого вала или распредвала.

Шум двигателя иногда может быть изолирован путем выполнения испытания на вырез цилиндра. Если объем шума уменьшается или шум исчезает, это связано с конкретным цилиндром двигателя.

Существует не определенная норма или тест, который положительно определит источник жалобы на шум.

Компоненты и аксессуары, приводимые в действие двигателем, такие как вентиляторные сцепления с приводом, гидравлические насосы, генераторы с приводом ремня, компрессоры для кондиционирования воздуха и турбокомпрессоры, могут способствовать шуму двигателя. Используйте следующую информацию в качестве руководства для диагностики шума двигателя.

#### Главный несущий шум

- (См. шум двигателя чрезмерный - основной несущий симптом дерева в разделе TS)
- Шум, вызванный рыхлым основным подшипником, является громким, тусклым стуком, слышащимся, когда двигатель тянет нагрузку. Если все основные подшипники рыхлые, будет слышен громкий грохот. Стуки регулярно слышны во всех других революциях. Шум является самым громким, когда двигатель затягивается или находится под большой нагрузкой. Стук тусклее, чем шум шатуна. Низкое давление масла также может сопровождать это состояние.
- Если подшипник не достаточно свободен, чтобы произвести стук сам по себе, подшипник может постучать, если масло слишком тонкое или если на подшипнике нет масла.
- Нерегулярный шум может указывать на изношенные подшипники тяги коленчатого вала.
- Перемежающийся, резкий стук указывает на чрезмерный зазор конца коленчатого вала. Повторные разъединения сцепления могут вызвать изменение шума.

#### Подключение Rod Bearing Noise

- (См. статью «Избыточный шум двигателя» - дерево симптомов устранения неполадок соединительного шнура в разделе TS)
- Соединение стержней с избыточным зазором будет стучать на всех скоростях двигателя как в условиях холостого хода, так и в условиях нагрузки. Когда подшипники начинают теряться, шум можно спутать с поршневым шлепком или рыхлыми поршневыми штифтами. Шум увеличивается в объеме при скорости двигателя. Низкое давление масла также может сопровождать это состояние.

#### Шум Пистона

- (См. статью «Избыточный шум двигателя» - дерево симптомов устранения неполадок в разделе TS)
- Трудно сказать разницу между поршневым штифтом, шатуном и поршневым шумом. Свободный поршневой штифт вызывает громкий двойной стук, который обычно слышится, когда двигатель работает на холостом ходу. Когда форсунка в этот цилиндр вырезается, в звуке стукательного шума будет слышно заметное изменение. Однако на некоторых двигателях стук становится более заметным, когда автомобиль работает на дороге с постоянной скоростью.

### Потребление нефти

В дополнение к следующей информации, доступна служебная публикация под названием Технический обзор потребления нефти, Бюллетень № 3379214.

Компания Cummins Engine Company, Inc. Определение термина «приемлемое использование нефти», как указано в следующей таблице.

| Приемлемое использование нефти |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| В любое время в период покрытия |  |  |  |  |  |  |  |  |  |
| Семейство двигателей | Часы за квартет | Часы на литр | Часы на императорскую квартплату | Мили за кварт | Мили за литр | Мили за Имперскую квартию | Километры на кварт | Километры на кварт | Километры на императорскую кварту |
| А. | 10.0 | 10.6 | 12.0 | 400 | 425 | 475 | 650 | 675 | 775 |
| 4B | 10.0 | 10.6 | 12.0 | 400 | 425 | 475 | 650 | 675 | 775 |
| 6B | 10.0 | 10.6 | 12.0 | 400 | 425 | 475 | 650 | 675 | 775 |
| 6C | 10.0 | 10.6 | 12.0 | 400 | 425 | 475 | 650 | 675 | 775 |
| V/VT-378 | 4.0 | 4.3 | 5.0 | - | - | - | - | - | - |
| V/VT-504 | 4.0 | 4.3 | 5.0 | 250 | 265 | 310 | 400 | 425 | 485 |
| V/VT-555 | 4.0 | 4.3 | 5.0 | 250 | 265 | 310 | 400 | 425 | 485 |
| Серия L | 4.0 | 4.3 | 5.0 | 250 | 265 | 310 | 400 | 425 | 485 |
| Серия M | 4.0 | 4.3 | 5.0 | 250 | 265 | 310 | 400 | 425 | 485 |
| Серия N | 4.0 | 4.3 | 5.0 | 250 | 265 | 310 | 400 | 425 | 485 |
| V/VT/VTA-903 | 4.0 | 4.3 | 5.0 | 250 | 265 | 310 | 400 | 425 | 485 |
| КТ/КТА-19 | 3.0 | 3.2 | 3.75 | 200 | 210 | 250 | 320 | 340 | 390 |
| V/VT/VTA28 | 2.0 | 2.1 | 2.5 | - | - | - | - | - | - |
| KT/KTA38 | 1.5 | 1.6 | 1.8 | - | - | - | - | - | - |
| ТА50 | 1.1 | 1.2 | 1.3 | - | - | - | - | - | - |

| Допустимое использование масла (транзитный автобус, автобус-шаттл и школьный автобус) |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| В любое время в период покрытия |  |  |  |  |  |  |  |  |  |
| Семейство двигателей | Часы за квартет | Часы на литр | Часы на императорскую квартплату | Мили за кварт | Мили за литр | Мили за Имперскую квартию | Километры на кварт | Километры на литр | Километры на императорскую кварту |
| B | 10.0 | 10.6 | 12.0 | 200 | 210 | 240 | 320 | 340 | 385 |
| C | 8.0 | 8.5 | 10.0 | 150 | 160 | 180 | 240 | 255 | 290 |
| L, M, N | 4.0 | 4.3 | 5.0 | 100 | 105 | 120 | 160 | 170 | 195 |

![[15200020.png]]

| Отчет о потреблении моторного моторного масла |  |  |  |
|---|---|---|---|
| Имя владельца | Дата доставки | Серийный номер двигателя |  |
| месяц | День | Год |  |
| Адрес | Производитель оборудования | Модели двигателей и лошадиные силы |  |
| Город | Государство/провинция | Серийный номер оборудования | Серийный номер топливного насоса |
| Применение двигателя (описание) | Интервал изменения масла и фильтра | Жалоба первоначально зарегистрирована |  |
| Нефть | Фильтры | Дата | Миля/часы/километры |

| Добавлено моторное масло |  |  |  |
|---|---|---|---|
| Дата добавления масла | Работа двигателя Мили/Часы/Километры | Кварты - масло литра добавлено | Бренд и вязкость используемого масла |
| Начало теста |  |  |  |
| Последние милиады/часы/километры \_\_ |  |  |  |
| Подпись клиента | Дилер Cummins | Дистрибьютор Cummins |  |
| Компания Cummins Engine, Inc. Форма 4755 |  |  |  |

![[15200020.png]]

| Отчет о потреблении нефти |  |
|---|---|
| Имя клиента: | Дистанция/дир: |
| Модель двигателя: | Ми/Км/Гр: |
| Серийный номер двигателя: | CPL Номер: |
| Автомобильный дизайн/модель: | Дата: |
| Обзор истории технического обслуживания: Перечислите любые предыдущие сбои, которые могли оказать вредное влияние на срок службы компонентов цилиндра. Неисправности могут включать в себя топливо, охлаждающую жидкость и / или инородные абразивы в масле, второй кольцевой канавочный выхлоп, заглушку фильтра и т. Д. |  |
| Используемое моторное масло: Интервал изменения вязкости бренда (ми/км/ч) |  |
| Комбинированный фильтр для масла: Интервал изменения элементов модели (ми/км/ч) |  |
| Обходной фильтр масла: Интервал изменения элементов модели (ми/км/ч) |  |
| Фильтр полноразмерного масла: Интервал изменения элементов модели (ми/км/ч) |  |
| Очиститель воздуха: Интервал изменения модели и макета |  |
| Перечислите любые внешние утечки двигателя. |  |
| Проверьте любые внутренние утечки и перечислите их. Проверьте уплотнения турбокомпрессора, направляющие клапана, воздушный компрессор и так далее. |  |
| Был ли подделан топливный насос? \_\_ Если да, насос **должен быть сброшен в заводские спецификации, и клиент отправлен для восстановления уровня потребления масла. Требования к кандидатам** должны быть выполнены снова. |  |
| Слив и пополнение масляной поддона для проверки уровня масла измерительной маркировки и отметить выводы. ОПАСНО: По заключению ряда государственных органов отработанное моторное масло может обладать канцерогенным действием и вредить репродуктивной функции. Не вдыхайте пары, не допускайте попадания внутрь и длительного контакта с отработанным моторным маслом. Если деталь не используется повторно, утилизируйте её по местным природоохранным требованиям. |  |
|  Только после завершения вышеупомянутых проверок, исправления утечек и завершения надлежащей документации разобрать двигатель для определения причины отказа и ремонта по мере необходимости. |  |
| Государственные причины потребления нефти. |  |
| Подпись: \_\_ |  |


> [!quote]- Original (English) · английский оригинал
> ### Driveability/Low Power - Customer Complaint Form
>
> Customer Name/Company \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_Date \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
>
> 1. How did the problem occur? Suddenly\_\_\_\_\_\_\_\_ Gradually \_\_\_\_\_\_\_\_
> 2. At what hour/mileage did the problem begin? Hours \_\_\_\_\_\_\_\_ Miles \_\_\_\_\_\_\_\_ Since New \_\_\_\_\_\_\_\_
>
> - After engine repair? Yes \_\_\_\_\_\_\_\_No \_\_\_\_\_\_\_\_
> - After equipment repair? Yes\_\_\_\_\_\_\_\_ No \_\_\_\_\_\_\_\_
> - After change in equipment use? Yes\_\_\_\_\_\_\_\_ No \_\_\_\_\_\_\_\_
> - After change in selected programmable parameters? Yes \_\_\_\_\_\_\_\_ No \_\_\_\_\_\_\_\_
> - If so, what was repaired and when?\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
> - Does the vehicle also experience poor fuel economy? Yes \_\_\_\_\_\_\_\_ No \_\_\_\_\_\_\_\_
>
> Answer questions 4 through 8 using selections (A through F) listed below. Circle the letter or letters that best describe the complaint.
>
> A - Compared to fleet
>
> B - Compared to competition
>
> C - Compared to previous engine
>
> D - Personal expectation
>
> E - Will **not** pull on hill
>
> F - Will **not** pull on flat terrain
>
> A B C D E F
>
> A - Can the vehicle obtain the expected road speed? Yes \_\_\_\_\_\_\_\_ No \_\_\_\_\_\_\_\_
>
> B - What is desired speed? rpm/mph\_\_\_\_\_\_\_\_
>
> C - What is achieved speed? rpm/mph\_\_\_\_\_\_\_\_
>
> D - Gross Vehicle Weight \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
>
> A B C D
>
> Is the vehicle able to pull the load? Yes \_\_\_\_\_\_\_\_ No \_\_\_\_\_\_\_\_
>
> When?
>
> \_\_\_\_\_\_\_\_ On hilly terrain
>
> \_\_\_\_\_\_\_\_ With a loaded trailer
>
> \_\_\_\_\_\_\_\_ On flat terrrain
>
> \_\_\_\_\_\_\_\_ Other \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
>
> IF QUESTION 4 OR 5 WAS ANSWERED NO, FILL OUT THE DRIVEABILITY/LOW-POWER/EXCESSIVE FUEL CONSUMPTION CHECKLIST AND GO TO THE LOW-POWER SYMPTOM TREE.
>
> Is the vehicle slow to accelerate or respond? Yes \_\_\_\_\_\_\_\_ No \_\_\_\_\_\_\_\_
>
> From a stop? Yes \_\_\_\_\_\_\_\_ No\_\_\_\_\_\_\_\_
>
> After a shift? Yes \_\_\_\_\_\_\_\_No \_\_\_\_\_\_\_\_ rpm \_\_\_\_\_\_\_\_
>
> Before a shift? Yes \_\_\_\_\_\_\_\_No \_\_\_\_\_\_\_\_ rpm \_\_\_\_\_\_\_\_
>
> No shift? Yes \_\_\_\_\_\_\_\_ No \_\_\_\_\_\_\_\_rpm \_\_\_\_\_\_\_\_
>
> Does the vehicle hesitate after periods of long deceleration or coasting? Yes \_\_\_\_\_\_\_\_ No \_\_\_\_\_\_\_\_ rpm\_\_\_\_\_\_\_\_
>
> IF QUESTION 6 OR 7 WAS ANSWERED YES, FILL OUT THE DRIVEABILITY/LOW-POWER/EXCESSIVE FUEL CONSUMPTION CHECKLIST AND GO TO THE POOR ACCELERATION/RESPONSE SYMPTOM TREE.
>
> Additional Comments:
>
> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
>
> This page can be copied for convenience.
>
> ### Driveability - General Information
>
> Driveability is a term that in general describes vehicle performance on the road. Driveability problems for an engine can be caused by several different factors. Some of the factors are engine-related and some are **not**.
>
> Before troubleshooting, it is important to determine the exact complaint and whether the engine has a real driveability problem or if it simply does **not** meet driver expectations. The Driveability-Low-Power Customer Complaint Form is a valuable list of questions that **must** be used to assist the service technician in determining what type of driveability problem the vehicle is experiencing. Complete the checklist before troubleshooting the problem. The form can be found at the end of this section. If an engine is performing to factory specifications but does **not** meet the customer's expectations, explain to the customer that nothing is wrong with the vehicle and why.
>
> The troubleshooting symptom charts have been set up to divide driveability problems into two different symptoms: Engine Power Output Low and Engine Acceleration or Response Poor.
>
> Low power is a term that is used in the field to describe many different performance problems. However, in this manual low power is defined as the inability of the engine to produce the power necessary to move the vehicle at a speed that can be reasonably expected under the given conditions of load, grade, wind, and so on. Low power is usually caused by the lack of fuel flow that can be caused by any of the following factors:
>
> - Lack of full travel of the throttle pedal
> - Failed boost sensor
> - Excessive fuel inlet, intake, exhaust, or drainline restriction
> - Loose fuel pump suction lines.
>
> Low power is **not** the inability of the vehicle to accelerate satisfactorily from a stop or the bottom of a grade. Refer to the Engine Power Output Low troubleshooting symptom tree in Section TS for the proper procedures to locate and correct a low-power problem. The chart starts off with basic items that can cause lower power.
>
> Poor acceleration or response is described in this manual as the inability of the vehicle to accelerate satisfactorily from a stop or from the bottom of a grade. It can also be the lag in acceleration during an attempt to pass or overtake another vehicle at conditions less than rated speed and load. Poor acceleration or response is difficult to troubleshoot since it can be caused by factors such as:
>
> - Engine- or pump-related factors
> - Driver technique
> - Improper gear shifting
> - Improper engine application
> - Worn clutch or clutch linkage.
>
> Engine-related poor acceleration or response can be caused by several different factors such as:
>
> - Failed boost sensor
> - Excessive drainline restriction
> - Throttle deadband.
>
> Refer to the Engine Acceleration or Response Poor troubleshooting symptom tree in Section TS for the proper procedures to locate and correct a poor acceleration or response complaint. For additional information, see Troubleshooting Driveability Complaints, Bulletin Number 3387245.
>
> ### Engine Noise Diagnostic Procedures - General Information
>
> **Note · Примечание**
> When diagnosing engine noise problems, make sure that noises caused by accessories, such as the air compressor and power take-off, are **not** mistaken for engine noises. Remove the accessory drive belts to eliminate noise caused by these units. Noise will also travel to other metal parts **not** related to the problem. The use of a stethoscope can help locate an engine noise.
>
> Engine noises heard at the crankshaft speed, engine rpm, are noises related to the crankshaft, rods, pistons, and piston pins. Noises heard at the camshaft speed, one-half of the engine rpm, are related to the valve train. A handheld digital tachometer can help determine if the noise is related to components operating at the crankshaft or camshaft speed.
>
> Engine noise can sometimes be isolated by performing a cylinder cutout test. If the volume of the noise decreases or the noise disappears, it is related to that particular engine cylinder.
>
> There is **not** a definite rule or test that will positively determine the source of a noise complaint.
>
> Engine-driven components and accessories, such as gear-driven fan clutches, hydraulic pumps, belt-driven alternators, air-conditioning compressors, and turbochargers, can contribute to engine noise. Use the following information as a guide to diagnosing engine noise.
>
> #### Main Bearing Noise
>
> - (Refer to the Engine Noise Excessive - Main Bearing troubleshooting symptom tree in Section TS)
> - The noise caused by a loose main bearing is a loud, dull knock heard when the engine is pulling a load. If all main bearings are loose, a loud clatter will be heard. The knock is heard regularly every other revolution. The noise is the loudest when the engine is lugging or under heavy load. The knock is duller than a connecting rod noise. Low oil pressure can also accompany this condition.
> - If the bearing is **not** loose enough to produce a knock by itself, the bearing can knock if the oil is too thin or if there is no oil on the bearing.
> - An irregular noise can indicate worn crankshaft thrust bearings.
> - An intermittent, sharp knock indicates excessive crankshaft end clearance. Repeated clutch disengagements can cause a change in the noise.
>
> #### Connecting Rod Bearing Noise
>
> - (Refer to the Engine Noise Excessive - Connecting Rod troubleshooting symptom tree in Section TS)
> - Connecting rods with excessive clearance will knock at all engine speeds under both idle and load conditions. When the bearings begin to become loose, the noise can be confused with piston slap or loose piston pins. The noise increases in volume with engine speed. Low oil pressure can also accompany this condition.
>
> #### Piston Noise
>
> - (Refer to the Engine Noise Excessive - Piston troubleshooting symptom tree in Section TS)
> - It is difficult to tell the difference between piston pin, connecting rod, and piston noise. A loose piston pin causes a loud double knock that is usually heard when the engine is idling. When the injector to this cylinder is cut out, a noticeable change will be heard in the sound of the knocking noise. However, on some engines the knock becomes more noticeable when the vehicle is operated on the road at a steady speed.
>
> ### Oil Consumption
>
> In addition to the information that follows, a service publication is available entitled Technical Overview of Oil Consumption, Bulletin Number 3379214.
>
> Cummins Engine Company, Inc. defines “acceptable oil usage” as outlined in the following table.
>
> | Accetable Oil Usage |  |  |  |  |  |  |  |  |  |
> |---|---|---|---|---|---|---|---|---|---|
> | Any Time During Coverage Period |  |  |  |  |  |  |  |  |  |
> | Engine Family | Hours per Quart | Hours per Liter | Hours per Imperial Quart | Miles per Quart | Miles per Liter | Miles per Imperial Quart | Kilometers per Quart | Kilometers per Quart | Kilometers per Imperial Quart |
> | A | 10.0 | 10.6 | 12.0 | 400 | 425 | 475 | 650 | 675 | 775 |
> | 4B | 10.0 | 10.6 | 12.0 | 400 | 425 | 475 | 650 | 675 | 775 |
> | 6B | 10.0 | 10.6 | 12.0 | 400 | 425 | 475 | 650 | 675 | 775 |
> | 6C | 10.0 | 10.6 | 12.0 | 400 | 425 | 475 | 650 | 675 | 775 |
> | V/VT-378 | 4.0 | 4.3 | 5.0 | - | - | - | - | - | - |
> | V/VT-504 | 4.0 | 4.3 | 5.0 | 250 | 265 | 310 | 400 | 425 | 485 |
> | V/VT-555 | 4.0 | 4.3 | 5.0 | 250 | 265 | 310 | 400 | 425 | 485 |
> | L Series | 4.0 | 4.3 | 5.0 | 250 | 265 | 310 | 400 | 425 | 485 |
> | M Series | 4.0 | 4.3 | 5.0 | 250 | 265 | 310 | 400 | 425 | 485 |
> | N Series | 4.0 | 4.3 | 5.0 | 250 | 265 | 310 | 400 | 425 | 485 |
> | V/VT/VTA-903 | 4.0 | 4.3 | 5.0 | 250 | 265 | 310 | 400 | 425 | 485 |
> | KT/KTA-19 | 3.0 | 3.2 | 3.75 | 200 | 210 | 250 | 320 | 340 | 390 |
> | V/VT/VTA28 | 2.0 | 2.1 | 2.5 | - | - | - | - | - | - |
> | KT/KTA38 | 1.5 | 1.6 | 1.8 | - | - | - | - | - | - |
> | KTA50 | 1.1 | 1.2 | 1.3 | - | - | - | - | - | - |
>
> | Acceptable Oil Usage (Transit Bus, Shuttle Bus, and School Bus) |  |  |  |  |  |  |  |  |  |
> |---|---|---|---|---|---|---|---|---|---|
> | Any Time During Coverage Period |  |  |  |  |  |  |  |  |  |
> | Engine Family | Hours per Quart | Hours per Liter | Hours per Imperial Quart | Miles per Quart | Miles per Liter | Miles per Imperial Quart | Kilometers per Quart | Kilometers per Liter | Kilometers per Imperial Quart |
> | B | 10.0 | 10.6 | 12.0 | 200 | 210 | 240 | 320 | 340 | 385 |
> | C | 8.0 | 8.5 | 10.0 | 150 | 160 | 180 | 240 | 255 | 290 |
> | L, M, N | 4.0 | 4.3 | 5.0 | 100 | 105 | 120 | 160 | 170 | 195 |
>
> | Engine Lubricating Oil Consumption Report |  |  |  |
> |---|---|---|---|
> | Owner's Name | Date of Delivery | Engine Serial Number |  |
> | Month | Day | Year |  |
> | Address | Equipment Manufacturer | Engine Model and Horsepower |  |
> | City | State/Province | Equipment Serial Number | Fuel Pump Serial Number |
> | Engine Application (Describe) | Oil and Filter Change Interval | Complaint Originally Registered |  |
> | Oil | Filters | Date | Mile/Hours/Kilometers |
>
> | Lubricating Oil Added |  |  |  |
> |---|---|---|---|
> | Date Added Oil | Engine Operation Miles/Hours/Kilometers | Quarts - Liters Oil Added | Brand and Viscosity of Oil Used |
> | Start Test |  |  |  |
> | Last Mileage/Hours/Kilometers \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Minus Start Mileage/Hours/Kilometers \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Equals Test Mileage/Hours/Kilometers \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Divided by Oil Added \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Equals \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Usage Rate\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |  |  |  |
> | Customer Signature | Cummins Dealer | Cummins Distributor |  |
> | Cummins Engine Company, Inc.Form 4755 |  |  |  |
>
> | Oil Consumption Report |  |
> |---|---|
> | Customer Name: | Dist/Dir: |
> | Engine Model: | Mi/Km/Hr: |
> | Engine Serial Number: | CPL Number: |
> | Vehicle Make/Model: | Date: |
> | Review of maintenance history: List any previous failures that could have had a detrimental effect on cylinder component life. Failures could include fuel, coolant, and/or foreign abrasives in the oil, second ring groove beat-out, filter plugging, etc. |  |
> | Lubrication Oil Used: Brand Viscosity Change Interval (mi/km/hr) |  |
> | Combination Oil Filter: Model Element Change Interval (mi/km/hr) |  |
> | Bypass Oil Filter: Model Element Change Interval (mi/km/hr) |  |
> | Full-Flow Oil Filter: Model Element Change Interval (mi/km/hr) |  |
> | Air Cleaner: Make and Model Change Interval |  |
> | List any external engine leaks. |  |
> | Check for any internal leaks and list them. Check turbocharger seals, valve guides, air compressor, and so forth. |  |
> | Had the fuel pump been tampered with? \_\_\_\_\_\_\_\_\_\_What is maximum rail pressure readings? \_\_\_\_\_\_\_\_\_\_ If yes, the pump **must** be reset to factory specifications and the customer sent out to reevalute the oil consumption rate. The eligibility requirements **must** be met again, also. |  |
> | Drain and refill oil pan to check dipstick markings and note findings. WARNING: Some state and federal agencies have determined that used engine oil can be carcinogenic and cause reproductive toxicity. Avoid inhalation of vapors, ingestion, and prolonged contact with used engine oil. If not reused, dispose of in accordance with local environmental regulations. |  |
> | **Only** after above checks are completed, leaks corrected, and proper documentation completed, disassemble engine to determine cause of the failure and repair as required. |  |
> | State reason for oil consumption. |  |
> | Signed: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |  |
