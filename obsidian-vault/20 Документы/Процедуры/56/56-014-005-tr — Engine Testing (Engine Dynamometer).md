---
aliases:
  - "Испытание двигателя (на моторном стенде)"
type: "Процедура"
doc: "56-014-005-tr"
title_en: "Engine Testing (Engine Dynamometer)"
title_ru: "Испытание двигателя (на моторном стенде)"
modified: "2023-07-12"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "33239746"
families:
  - "QSK60"
  - "QSK60 CM2150 MCRS"
manuals:
  - "4021530"
figures: 41
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-014-005-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-014-005-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "двигатель/QSK60CM2150MCRS"
  - "группа/56"
  - "перевод/машинный"
---

# Engine Testing (Engine Dynamometer)
**Испытание двигателя (на моторном стенде)**

> [!abstract] Процедура · `56-014-005-tr`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]]
> **Семейство:** QSK60, QSK60 CM2150 MCRS
> **Входит в руководства:** [[4021530 — QSK45 and QSK60 Service Manual|4021530]]
> **Секции:** Section 14 - Engine Testing - Group 14 · Section 14 Engine Testing - Group 14
> **Даты:** изменён 2023-07-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-014-005-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-014-005-tr.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

В настоящем документе предусмотрены процедуры использования системы управления двигателем, номер детали 3163890. Управление двигателем - это портативное, портативное электронное управление, используемое для запуска и управления скоростью двигателя на электронных двигателях Cummins®. Он заменяет педаль дроссельной заслонки, панель интерфейса водителя и схемы мониторинга кода неисправности. Управление двигателем имеет положение шины данных CAN для подключения к электронному сервисному инструменту для мониторинга работы двигателя и кодов неисправностей. Рулевая проводка двигателя, необходимая для двигателей, приобретается отдельно. Усилители управления двигателем и проводов управления двигателем предназначены для использования как с (+) 12-VDC, так и с (+) 24-VDC аккумуляторными системами.

> [!note] Примечание
> Управление двигателем может быть использовано на двигателях с частотной калибровкой дроссельной заслонки путем первой загрузки линейной калибровки дроссельной заслонки в электронный модуль управления (ECM). После завершения тестирования/ремонта перезагрузите правильную калибровку частоты дроссельной заслонки.

### Установка

> [!note] Примечание
> : Убедитесь, что динамометр достаточной мощности, чтобы позволить тестирование на 100 процентов номинальной мощности двигателя. Если емкость недостаточна, процедура тестирования должна быть изменена до ограничений динамометра.

Используйте подъемный механизм двигателя, номер детали 3163264, для установки двигателя на испытательный стенд. Выровняйте и соедините динамометр. См. инструкции производителя по выравниванию и тестированию двигателя.

![[00600042.png]]

Охлаждающая сантехника

Подключите подачу охлаждающей жидкости к впускному соединению с водой.

Подключите охлаждающую жидкость к выходному соединению.

Установите дренажные пробки и закройте все дренажные краны.

> [!note] Примечание
> : Двигатели LTA требуют подключения водных линий LTA к удаленному теплообменнику.

![[08400044.png]]

Контроль температуры воздуха

Использование удаленного теплообменника является обязательным всякий раз, когда двигатель Cummins LTA прикреплен к динамометру двигателя с целью запуска двигателя, тестирования производительности и / или диагностики двигателя. Сделайте **не** попытку запустить двигатель Cummins® LTA без каких-либо средств контроля температуры воздуха впускного коллектора.

1. Послеохлаждение воды
2. Послеохлажденная вода в
3. Охлаждение воды для слива
4. Охлаждение воды.

![[10400042.png]]

ЛЕТ

Все промышленные двигатели QSK45 и QSK60 требуют LTA и, следовательно, имеют уникальные требования к радиатору.

Теплообменник должен быть размером для поддержания максимальной температуры воздуха при впуске 70°C[158°F] при полной мощности.

1. Охлаждение воды в
2. Корпус термостата
3. LTA выходит
4. Охлаждение воды
5. Возвращение LTA.

![[10400043.png]]

Двигатель Throttle Control

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Для уменьшения возможности дуги сначала удалите отрицательный (-) кабель батареи и прикрепите отрицательный (-) кабель батареи последним.

Механически приводимый в действие форсунка

Отключите кабели аккумулятора перед началом следующей процедуры.

Отсоедините электропроводку OEM от электронного модуля управления (ECM), если это применимо.

![[22c00141.png]]

Отсоедините проводные упряжки OEM 21-контактный и 31-контактный разъемы Deutsch от электропроводки двигателя.

Подключите электропроводку управления двигателем, номер детали 4918643.

Подключите к ремню 21-контактную и 31-контактную проводку управления двигателем к ремню электропроводки двигателя.

![[19a00768.png]]

> [!note] Примечание
> Если для подключения управления двигателем требуется дополнительная длина кабеля, используйте электрический кабель, номер детали 3163895.

Подключите проводку управления двигателем (2) к управлению двигателем. Электронный инструмент, оснащенный персональным компьютером INSITETM, может использоваться для мониторинга цепей для правильной работы. Подключите комплект адаптера шины данных INLINETM5 CAN (3), Номер детали 4918416 и персональный компьютер к разъему шины данных CAN управления двигателем.

![[22c00125.png]]

Двигатели, которые работают на динамометре двигателя, требуют установки и подключения к двигателю электропроводки. Кроме того, двигатель, номер детали 3163890, должен быть использован для правильного управления двигателем во время работы динамометра.

![[wr8coac.png]]

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Для уменьшения возможности дуги сначала удалите отрицательный (-) кабель батареи и прикрепите отрицательный (-) кабель батареи последним.

Подключите питание от батареи к стартеру.

Подключите динамометр теста OEM-проводов ремня стартера соленоидного свинца (желтого цвета) к стартерному соленоиду. Подключите грунтовый свинец (черный) к стартеру соленоида. Подключите грунтовый свинец черный к стартеру или аккумулятору отрицательной (-) или стороне земли. Подключите (+) 12 VDC с красным свинцом к стартеру или положительной (+) 12 стороне VDC батареи.

![[sb8coma.png]]

Вращайте ручку дроссельной заслонки полностью **против часовой стрелки**.

Нажмите на ручку дроссельной заслонки, чтобы вернуть дроссель в положение холостого хода.

Повторите этот шаг три раза.

Переключатель зажигания в положение выключения в течение 30 секунд.

![[22c00155.png]]

> [!warning] ОСТОРОЖНО
> Проверьте уровень охлаждающей жидкости и моторного масла перед запуском и работой двигателя. Если охлаждающая жидкость и моторное масло не находятся на должном уровне, может возникнуть повреждение двигателя.

Включите переключатель зажигания в положение START до запуска двигателя и отпустите переключатель зажигания.

![[22c00129.png]]

с форсункой электронного управления

Отсоедините проводку OEM-упряжи 16-контактных и 23-контактных разъемов Deutsch от электропроводки двигателя, если она подключена.

Удалите 3-контактный резистор Deutsch (кап будет иметь синюю вставку) из электропроводки.

Подключите 3-контактный разъем Deutsch для управления двигателем к разъему шины данных SAE J1939 CAN для проводов двигателя.

3-контактный резистор Deutsch концевой резисторной крышки должен быть установлен после того, как убрана проводка управления двигателем. Если крышка сломана или была неправильно расположена, замените резисторную крышку, номер детали 3163051.

![[22400280.png]]

Наземное соединение

Подключите черную проводку аллигатора к ремню управления двигателем к блоку двигателя, чтобы достичь электрического заземления.

![[19c01031.png]]

> [!warning] ОСТОРОЖНО
> Не подключайте зажим аллигатора к стартовому моторному соленоидному терминалу «S». Это может привести к повреждению оборудования.

Стартовое соединение

Если **не** уже оборудован, установите и проведите магнитный стартер.

Заткните разъем аллигатора к положительному (+) концевому клемму катушки магнитного стартера.

![[22400055.png]]

Air Starter

Если используется воздушный стартер, введите красный провод в петлю и закрепите петлю на электропроводке управления двигателем, чтобы защитить его от электрического короткого.

![[19c01032.png]]

Работа двигателя

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Для уменьшения возможности дуги сначала удалите отрицательный (-) кабель батареи и прикрепите отрицательный (-) кабель батареи последним.

Прикрепите управляющую проводку упряжкой с помощью кольцевого терминала красного провода к положительному (+) терминалу батареи.

Прикрепите управляющую проводку упряжкой с помощью кольцевого терминала черного провода к отрицательному (-) терминалу батареи.

Прикрепите управляющую проводку упряжкой с помощью кольцевого терминала красного провода к положительному (+) терминалу батареи. Прикрепите управляющую проводку упряжкой с помощью кольцевого терминала черного провода к отрицательному (-) терминалу батареи.

![[sb8coma.png]]

> [!warning] ОСТОРОЖНО
> Проверить, что красный провод подключен к положительному (+) клемме батареи, а черный провод подключен к отрицательному (-) клемме батареи. Повреждение оборудования или двигателя может привести к неправильному подключению.

Силовой свет будет освещаться при подаче питания и переключатель зажигания поворачивается в положение аксессуара или Включено.

Если силовой свет не освещается, верните переключатель зажигания в положение выключения. Проверить, что красный провод подключен к положительному (+) клемме батареи, а черный провод подключен к отрицательному (-) клемме батареи.

Переведите замок зажигания в положение ON.

![[22c00127.png]]

Световые индикаторы на управлении двигателем, ОСТАНОВКА,

Предупреждение, УЧЕТ, ПОДДЕРЖАНИЕ и ЖДЕНИЕ СНВ, если применимо, будут освещаться. Световые индикаторы будут светиться в течение примерно 30 секунд. Если не будет найдено кодов неисправностей, световые индикаторы погаснут.

Если индикатор STOP (красный) или индикатор WARN (желтый) продолжает освещаться, используйте инструмент для электронного обслуживания INSITETM и литературу по обслуживанию OEM для диагностики кода неисправности двигателя.

![[22c00128.png]]

> [!warning] ОСТОРОЖНО
> Проверьте уровень охлаждающей жидкости и моторного масла перед запуском и работой двигателя. Если охлаждающая жидкость и моторное масло не находятся на должном уровне, может возникнуть повреждение двигателя.

Включите переключатель зажигания в положение START до запуска двигателя и отпустите переключатель зажигания.

![[22c00127.png]]

> [!note] Примечание
> Двигатель может быть возвращен в бездействие в любое время, нажав на ручку дросселя.

Медленно поверните ручку дроссельной заслонки **против часовой стрелки**, чтобы увеличить обороты двигателя.

Медленно поверните ручку дроссельной заслонки **по часовой стрелке**, чтобы уменьшить обороты двигателя.

![[22c00130.png]]

Включите переключатель зажигания в положение выключения, чтобы остановить двигатель.

![[22c00131.png]]

Возврат параметров к их исходным значениям, когда тест или запуск завершены.

Подключите панель переключателя зажигания CAN кабеля шины данных к электронному сервисному инструменту Cummins®.

Используйте инструмент электронного обслуживания INSITETM для настройки двигателя для динамометра.[[56-014-008-tr — Engine Testing (In Chassis)|См. процедуру 014-008 в разделе 14 для получения дополнительной информации об этой функции.]]

Настройка теперь завершена, и для управления скоростью двигателя можно использовать автоматическое / ручное дроссельное заслонки.

![[14c00040.png]]

Технические характеристики двигателя доступны в авторизованных местах ремонта Cummins®.

![[lt800ga.png]]

### Проверка

> [!warning] ОСТОРОЖНО
> Система моторного масла должна быть заряжена перед работой двигателя после реконструкции, чтобы избежать повреждения внутренних компонентов. Не загружайте систему из обходного фильтра, так как фильтр будет поврежден.

Промышленные двигатели QSK45 и QSK60 оснащены автоматической системой прелюбации с завода. Если двигатель **не** оборудован автоматической системой прелюбирования, следуйте инструкциям для прелюбирования двигателя вручную.

![[14400011.png]]

Для двигателей без автоматического прелюбационного устройства используйте насос, способный подавать 205 кПа \[30 psi\] непрерывного давления.

Удалите трубную пробку с передней задней стороны цельной головки фильтра моторного масла.

Установить удлиненный локоть (1) в задний порт, из которого была удалена трубная пробка. Окончательное положение этого локтя обращено к задней части двигателя и немного внутри, чтобы убедиться, что контрольный клапан очищает передний фильтр на цельной головке смазочного фильтра.

Затяните локоть.

> [!tip] Момент затяжки
> 60 Н·м [44 фунт-фут]

Нанесите небольшое количество Loctite® 641 на конусную резьбу штуцера с наружной резьбой (3) и установите его в конец потока контрольного клапана (2).

Нанесите небольшое количество Loctite® 641 на коническую резьбу удлиненного локтя (1) и установите контрольный клапан со стрелкой, указывающей на локтевую часть в головке фильтра моторного масла.

Затянуть контрольный клапан.

> [!tip] Момент затяжки
> 48 Н·м [35 фунт-фут]

Подключите насос к штуцеру с наружной резьбой.

Используйте запас чистого масла. Поверните насос в положение ON. Проверьте датчик давления масла в двигателе. Когда калибр указывает на давление масла, начните мониторинг уровня масла в масляной кастрюле.

![[07600483.png]]

Проверьте уровень моторного масла двигателя, чтобы убедиться, что он заполнен до нужного уровня.

![[oi900sb.png]]

Удалите насос.

Удалите локоть (1), проверьте клапан (2) и адаптер (3) из головки фильтра моторного масла.

Установите трубную пробку.

![[07600483.png]]

> [!danger] ОПАСНО
> Не снимайте пробку радиатора с горячего двигателя. Снимайте пробку радиатора только после того, как температура охлаждающей жидкости опустится ниже 50 °C \[120 °F\]. Струя горячей охлаждающей жидкости или пар могут привести к травме.

> [!warning] ОСТОРОЖНО
> Не добавляйте холодную охлаждающую жидкость в горячий двигатель. Это может привести к повреждению литья двигателя. Позвольте двигателю охладиться до температуры ниже 50°C \[120°F\] перед добавлением охлаждающей жидкости.

Проверьте уровень охлаждающей жидкости двигателя.[[56-008-018-tr — Cooling System|См. процедуру 008-018 в разделе 8.]]

Используйте известный источник качественного дизельного топлива No2. Дизельные топлива № 1, наряду с большинством других альтернативных видов топлива, легче (более низкая удельная гравитация, более высокая гравитация API), чем дизельное топливо № 2. Чем легче топливо, тем ниже содержание энергии на галлон (литр).

![[ra200sa.png]]

Для правильного контроля работы двигателя запишите следующие параметры. Чтобы ограничить время работы динамометра, измерьте двигатель, чтобы сделать как можно больше проверок. Инструменты электронного обслуживания INSITETM будут предоставлять большинство, если **не**, следующих услуг:

- Скорость двигателя rpm с проверенным тахометром
- Топливное давление
- Расход топлива
- Температура топлива (если необходимо скорректировать расход топлива)
- Сопротивление на входе топлива
- Сопротивление магистрали слива топлива
- давление впуска многообразия (в банке).

![[eg200ka.png]]

- Ограничение потребления воздуха (в банке)
- Ограничение выхлопного воздуха (на банк)
- Температура охлаждающей жидкости
- Двигатель продувается
- Давление моторного масла
- Охлаждающее давление
- Впускной коллектор температуры воздуха
- Температура воздуха на входе турбокомпрессора.

![[eg100km.png]]

Скорость двигателя

Используйте цифровой оптический тахометр, номер 3377462, а также отражающую ленту, номер 3377464, для проверки скорости двигателя.

![[er2tova.png]]

> [!note] Примечание
> Не измеряйте ограничение линии слива топлива с установленным устройством измерения топлива. Это не будет измерять ограничение линии отвода от обратной сантехники транспортного средства.

Используйте калибр давления, часть номер ST-1273, для измерения ограничения линии слива топлива.[[56-006-012 — Fuel Drain Line Restriction|См. процедуру 006-012 в разделе 6.]]

![[06400051.png]]

Ограничение впуска воздуха

Установите измерительный датчик под углом 90 градусов к потоку воздуха в прямом участке трубы при диаметре не менее одной трубы перед турбокомпрессором.

Установите вакуумный калибр, номер детали ST-434 или манометр, номер детали ST-1111-3, в воздухозаборнике.

Измерьте ограничение входного воздуха.

[[56-010-031 — Air Intake Restriction|См. процедуру 010-031 в разделе 10.]]

![[10400011.png]]

Ограничение выхлопных газов

Установите измерительный датчик рядом с турбокомпрессором в прямом участке трубы на выходе турбины.

Установите калибр давления, номер детали ST-1273 или манометр в выхлопных трубах.

Измерьте ограничение выхлопного воздуха.

[[56-011-009 — Exhaust Restriction|См. процедуру 011-009 в разделе 11.]]

![[pe4cokb.png]]

Двигатель Blowby

Измерьте давление в картере.[[56-014-010-tr — Crankcase Blowby, Measure|См. процедуру 014-010 в разделе 14.]]

![[eg8toga.png]]

Проверьте уровень моторного масла. Если уровень слишком высок, это может вызвать более высокое, чем обычно, давление в картере.

![[oi900sb.png]]

Давление моторного масла

Используйте калибр давления, часть 3375275, для измерения давления моторного масла.

Установите датчик измерения давления на главную масляную винт (1) или головку фильтра воздухоочистителя (2).

| Давление моторного масла |  |  |  |
|---|---|---|---|
|  | каша |  | пси |
| Низкий холостый | 138 | Мин | 20 |
| Рейтинг rpm | 413 | Мин | 60 |

![[ov400ha.png]]

Двигатель Охлаждающее давление

Используйте калибр давления, часть 3375275, для измерения давления моторного масла.

Установите датчик измерения давления на главную масляную винт (1) или головку фильтра воздухоочистителя (2).

| Давление моторного масла |  |  |  |
|---|---|---|---|
|  | каша |  | пси |
| Низкий холостый | 138 | Мин | 20 |
| Рейтинг rpm | 413 | Мин | 60 |

![[14400009.png]]

Воздушный компрессор

Все воздушные компрессоры, производимые компанией Cummins Inc. **должен работать во время работы двигателя. Во время проверки производительности все воздушные компрессоры **должны находиться в незагруженном или нерабочем режиме.

Подсоедините источник сжатого воздуха, способный производить 665 кПа[95 psi], к разгрузчику воздушного компрессора (1). Эта линия сжатого воздуха должна содержать клапан между источником и разгрузчиком.

Прикрепить сжатую воздушную нагрузку к выходу воздушного компрессора (2).

![[cp8vawa.png]]

Используйте воздушный танк (2). Установите регулятор (3) воздуха, способный поддерживать давление воздуха от 345 до 517 кПа [50-75-пси] при ± минимальном и максимальном ± ± оборотах двигателя при 260°C \[500°F\].

Установите стальную трубу или высокотемпературный шланг (1).

Подсоедините трубку или шланг (1) к выходу воздушного компрессора.

![[cp8tohc.png]]

Стартер

Проверьте рейтинг напряжения на стартовом двигателе перед установкой электрической проводов.

Установите электрическую проводку на стартовый двигатель и батареи, если они используются.

> [!note] Примечание
> Если используется другой способ запуска двигателя, следуйте инструкциям производителя для создания необходимых соединений.

![[sb8coma.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> This document provides procedures for the use of an engine control, Part Number 3163890. The engine control is a portable, handheld electronic control, used to start and control engine speed on the Cummins® electronic engines. It replaces the throttle pedal, driver interface panel, and fault code monitoring circuits. The engine control has a datalink provision to connect to an electronic service tool to monitor engine operation and fault codes. The engine control harnesses required for the engines are purchased separately. The engine control and engine control harnesses are designed to be used with both (+) 12-VDC and (+) 24-VDC battery systems.
>
> **Note · Примечание**
> The engine control can be used on engines with frequency throttle calibrations by first downloading a linear throttle calibration to the electronic control module (ECM). After the testing/repair is complete, reload the correct frequency throttle calibration.
>
> ### Install
>
> **Note · Примечание**
> : Make sure the dynamometer capacity is sufficient to permit testing at 100 percent of the engine's rated horsepower. If the capacity is not enough, the testing procedure **must** be modified to the restrictions of the dynamometer.
>
> Use engine lifting fixture, Part Number 3163264, to install the engine to the test stand. Align and connect the dynamometer. See the manufacturer's instructions for aligning and testing the engine.
>
> Coolant Plumbing
>
> Connect the coolant supply to the water inlet connection.
>
> Connect the coolant return to the water outlet connection.
>
> Install the drain plugs, and close all of the water draincocks.
>
> **Note · Примечание**
> : LTA engines require connecting the LTA water lines to a remote heat exchanger.
>
> Intake Air Temperature Control
>
> The use of a remote heat exchanger is mandatory whenever a Cummins LTA engine is attached to an engine dynamometer for the purpose of engine run-in, performance testing, and/or engine diagnostics. Do **not** attempt to run a Cummins® LTA engine with out any means of controlling the intake manifold air temperature.
>
> 1. Aftercooler water out
> 2. Aftercooler water in
> 3. Cooling water out to drain
> 4. Cooling water in.
>
> LTA
>
> All QSK45 and QSK60 industrial engines require LTA and, therefore, have unique radiator requirements.
>
> The heat exchanger **must** be sized to maintain 70°C \[158°F\] maximum intake air temperature at full power.
>
> 1. Cooling water in
> 2. Thermostat housing
> 3. LTA out
> 4. Cooling water out
> 5. LTA return.
>
> Engine Throttle Control
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first, and attach the negative (-) battery cable last.
>
> Mechanically Actuated Injectors
>
> Disconnect the battery cables before beginning the following procedure.
>
> Disconnect the OEM harness from the electronic control module (ECM), if applicable.
>
> Disconnect the OEM harness 21-pin and 31-pin Deutsch connectors from the engine harness.
>
> Connect the engine control harness, Part Number 4918643.
>
> Connect the engine control harness 21-pin and 31 pin Deutsch connectors to the engine wiring harness.
>
> **Note · Примечание**
> If additional cable length is needed to connect the engine control, use electrical cable, Part Number 3163895.
>
> Connect the engine control harness (2) to the engine control. An INSITE™ electronic service tool equipped personal computer can be used to monitor circuits for proper operation. Connect the INLINE™5 datalink adapter kit (3), Part Number 4918416,, and a personal computer to the datalink connector of the engine control.
>
> Engines that are run on an engine dynamometer require the engine harness be installed and connected to the engine. Additionally, the engine control, Part Number 3163890, **must** be used to properly control the engine during the dynamometer run.
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first, and attach the negative (-) battery cable last.
>
> Connect battery power to the starter.
>
> Connect the dynamometer test OEM wiring harness starter solenoid lead (yellow) to the starter solenoid. Connect the ground lead (black) to the starter solenoid. Connect the ground lead black) to the starter or battery negative (-) or ground side. Connect the (+) 12 VDC power lead red) to either the starter or battery positive (+) 12 VDC side.
>
> Rotate the throttle knob fully **counterclockwise**.
>
> Push down on the throttle knob to return the throttle to the idle position.
>
> Repeat this step three times.
>
> Turn the keyswitch to the OFF position for 30 seconds.
>
> **CAUTION · Осторожно**
> Check coolant and lubricating oil levels before starting and operating engine. If coolant and lubricating oil are not at the proper level, engine damage can result.
>
> Turn the keyswitch to the START position until the engine starts and release the keyswitch.
>
> with Electronically Actuated Injector
>
> Disconnect the OEM harness 16-pin and 23-pin Deutsch connectors from the engine harness, if connected.
>
> Remove the 3-pin Deutsch terminal resistor cap (cap will have a blue insert) from the wiring harness.
>
> Connect the engine control harness 3-pin Deutsch connector to the SAE J1939 Datalink connector of the engine wiring harness.
>
> The 3-pin Deutsch terminal resistor cap **must** be installed after the engine control harness is removed. If the cap is broken or has been misplaced, replace with resistor cap, Part Number 3163051.
>
> Ground Connection
>
> Connect the black-wire alligator clip of the engine control harness to the engine block to achieve electrical ground.
>
> **CAUTION · Осторожно**
> Do not connect the alligator clip to the starter motor solenoid “S” terminal. Doing so can cause equipment damage.
>
> Starter Connection
>
> If **not** already equipped, install and wire a magnetic starter switch.
>
> Clip the alligator connector to the positive (+) coil terminal of the magnetic starter switch.
>
> Air Starter
>
> If an air starter is being used, coil the red wire into a loop and secure the loop to the engine control harness to protect it from an electrical short.
>
> Engine Operation
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first, and attach the negative (-) battery cable last.
>
> Attach the control harness using the ring terminal of the red wire to the positive (+) terminal of the battery.
>
> Attach the control harness using the ring terminal of the black wire to the negative (-) terminal of the battery.
>
> Attach the control harness using the ring terminal of the red wire to the positive (+) terminal of the battery. Attach the control harness using the ring terminal of the black wire to the negative (-) terminal of the battery.
>
> **CAUTION · Осторожно**
> Verify the red wire is connected to the positive (+) battery terminal and the black wire is connected to the negative (-) battery terminal. Equipment or engine damage can result if not connected properly.
>
> The power light will illuminate when power is supplied and the keyswitch is turned to the accessory or ON position.
>
> If the power light does **not** illuminate, return the keyswitch to the OFF position. Verify the red wire is connected to the positive (+) battery terminal and the black wire is connected to the negative (-) battery terminal.
>
> Turn the keyswitch to the ON position.
>
> Light indicators on the engine control, STOP,
>
> WARN, MAINT, WIF, and WAIT TO START, will illuminate if applicable. The light indicators will illuminate for approximately 30 seconds. If no fault codes are found, the light indicators will extinguish.
>
> If the STOP light indicator (red) or WARN light indicator (yellow) continues to illuminate, use INSITE™ electronic service tool and the OEM service literature to diagnose the engine fault code.
>
> **CAUTION · Осторожно**
> Check coolant and lubricating oil levels before starting and operating engine. If coolant and lubricating oil are not at the proper level, engine damage can result.
>
> Turn the keyswitch to the START position until the engine starts and release the keyswitch.
>
> **Note · Примечание**
> The engine can be returned to idle at any time by pushing in on the throttle knob.
>
> Slowly rotate the throttle knob **counterclockwise** to increase the engine rpm.
>
> Slowly rotate the throttle knob **clockwise** to decrease the engine rpm.
>
> Turn the keyswitch to the OFF position to stop the engine.
>
> Return parameters to their original values when the test or run-in is complete.
>
> Connect the keyswitch panel datalink cable to the Cummins® electronic service tool.
>
> Use INSITE™ electronic service tool to set the engine up for the dynamometer. [[56-014-008-tr — Engine Testing (In Chassis)|Refer to Procedure 014-008 in Section 14 for more information on this feature.]]
>
> The setup is now complete, and the auto/manual throttle can be used to control engine speed.
>
> Engine operating specifications are available from Cummins® authorized repair locations.
>
> ### Test
>
> **CAUTION · Осторожно**
> The lubricating oil system must be primed before operating the engine after rebuild to avoid internal component damage. Do not prime the system from the bypass filter as the filter will be damaged.
>
> Industrial QSK45 and QSK60 engines are equipped with an automatic prelube system from the factory. If the engine is **not** equipped with an automatic prelube system, follow the instructions to prelube the engine manually.
>
> For engines without an automatic prelube device, use a pump capable of supplying 205 kPa \[30 psi\] continuous pressure.
>
> Remove the pipe plug at the front rear underside of the one-piece lubricating oil filter head.
>
> Install an extended elbow (1) into the rear port the pipe plug was removed from. The final position of this elbow is facing the rear of the engine and slightly inboard to make sure the check valve clears the front filter on the one-piece lubricating filter head.
>
> Tighten the elbow.
>
> **Момент затяжки · Torque Value**
> 60 n•m [44 ft-lb]
>
> Apply a small amount of Loctite® 641 to the tapered threads of the male adapter (3) and install it into the flow end of the check valve (2).
>
> Apply a small amount of Loctite® 641 to the tapered threads of the extended elbow (1) and install the check valve with the arrow pointing at the elbow in the lubricating oil filter head.
>
> Tighten the check valve.
>
> **Момент затяжки · Torque Value**
> 48 n•m [35 ft-lb]
>
> Connect the pump to the male adapter.
>
> Use a supply of clean oil. Turn the pump to the ON position. Check the engine oil pressure gauge. When the gauge indicates oil pressure, begin monitoring the oil level in the oil pan.
>
> Check the engine lubricating oil level to make sure it is filled to the proper level.
>
> Remove the pump.
>
> Remove the elbow (1), check valve (2), and adapter (3) from the lubricating oil filter head.
>
> Install the pipe plug.
>
> **WARNING · Опасно**
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.
>
> **CAUTION · Осторожно**
> Do not add cold coolant to a hot engine. This can cause engine casting damage. Allow the engine to cool to below 50°C \[120°F\] before adding coolant.
>
> Check the engine coolant level. [[56-008-018-tr — Cooling System|Refer to Procedure 008-018 in Section 8.]]
>
> Use a known source of good-quality number 2 diesel fuel. Number 1 diesel fuels, along with most other alternate fuels, are lighter (lower specific gravity, higher API gravity) than number 2 diesel fuel. The lighter the fuel, the lower the energy content per gallon (liter).
>
> To properly monitor engine performance, record the following parameters. To limit dynamometer operating time, instrument the engine to make as many checks as possible. The INSITE™ electronic service tool will provide most, if **not** all of the following:
>
> - Engine speed rpm with a verified tachometer
> - Fuel pressure
> - Fuel rate
> - Fuel temperature (if needed to correct fuel rate)
> - Fuel inlet restriction
> - Fuel drain line restriction
> - Intake manifold pressure (per bank).
>
> - Intake air restriction (per bank)
> - Exhaust air restriction (per bank)
> - Coolant temperature
> - Engine blowby
> - Lubricating oil pressure
> - Coolant pressure
> - Inlet manifold air temperature
> - Turbocharger inlet air temperature.
>
> Engine Speed
>
> Use digital optical tachometer, Part Number 3377462, along with reflective tape, Part Number 3377464, to check the engine speed.
>
> **Note · Примечание**
> Do **not** measure fuel drain line restriction with the fuel measuring device installed. This will **not** measure the drain line restriction of the vehicle's return plumbing.
>
> Use pressure gauge, Part Number ST-1273, to measure fuel drain line restriction. [[56-006-012 — Fuel Drain Line Restriction|Refer to Procedure 006-012 in Section 6.]]
>
> Intake Air Restriction
>
> Install the gauge adapter at a 90-degree angle to the airflow in a straight section of pipe at a minimum of one pipe diameter before the turbocharger.
>
> Install the vacuum gauge, Part Number ST-434, or a manometer, Part Number ST-1111-3, in the intake air piping.
>
> Measure the inlet air restriction.
>
> [[56-010-031 — Air Intake Restriction|Refer to Procedure 010-031 in Section 10.]]
>
> Exhaust Air Restriction
>
> Install the gauge adapter near the turbocharger in a straight section of pipe at the turbine outlet.
>
> Install the pressure gauge, Part Number ST-1273, or a manometer in the exhaust air piping.
>
> Measure the exhaust air restriction.
>
> [[56-011-009 — Exhaust Restriction|Refer to Procedure 011-009 in Section 11.]]
>
> Engine Blowby
>
> Measure the crankcase pressure. [[56-014-010-tr — Crankcase Blowby, Measure|Refer to Procedure 014-010 in Section 14.]]
>
> Check the engine oil level. If the level is too high, it can cause a higher than normal crankcase pressure.
>
> Lubricating Oil Pressure
>
> Use pressure gauge, Part Number 3375275, to measure lubricating oil pressure.
>
> Install the pressure gauge to the main oil rifle (1) or air filter head (2).
>
> | Lubricating Oil Pressure |  |  |  |
> |---|---|---|---|
> |  | kpa |  | psi |
> | Low Idle | 138 | MIN | 20 |
> | Rated rpm | 413 | MIN | 60 |
>
> Engine Coolant Pressure
>
> Use pressure gauge, Part Number 3375275, to measure lubricating oil pressure.
>
> Install the pressure gauge to the main oil rifle (1) or air filter head (2).
>
> | Lubricating Oil Pressure |  |  |  |
> |---|---|---|---|
> |  | kpa |  | psi |
> | Low Idle | 138 | MIN | 20 |
> | Rated rpm | 413 | MIN | 60 |
>
> Air Compressor
>
> All air compressors manufactured by Cummins Inc. **must** be operating during the engine run-in. During the performance check, all air compressors **must** be in the unloaded or non-operating mode.
>
> Connect a source of compressed air capable of producing 665 kPa \[95 psi\] to the air compressor unloader (1). This air line **must** contain a valve between the source and the unloader.
>
> Attach compressed air load to the air compressor outlet (2).
>
> Use an air tank (2). Install an air regulator (3) capable of maintaining 345- to 517-kPa \[50- to 75-psi\] air pressure at both **minimum and maximum** engine rpm at 260°C \[500°F\].
>
> Install a steel tube or high-temperature hose (1).
>
> Connect the tube or hose (1) to the air compressor outlet.
>
> Starting Motor
>
> Inspect the voltage rating on the starting motor before installing the electrical wiring.
>
> Install the electrical wiring to the starting motor and batteries, if used.
>
> **Note · Примечание**
> If another method of starting the engine is used, follow the manufacturer's instructions to make the necessary connections.
