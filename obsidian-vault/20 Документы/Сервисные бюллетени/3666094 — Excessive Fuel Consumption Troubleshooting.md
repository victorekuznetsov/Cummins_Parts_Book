---
type: "Сервисный бюллетень"
doc: "3666094"
title_en: "Excessive Fuel Consumption Troubleshooting"
released: "2007-11-30"
modified: "2010-09-28"
engines:
  - "37269910"
  - "37280605"
  - "77804810"
  - "80141463"
  - "80248213"
  - "93948840"
families:
  - "15N"
  - "K19"
  - "QSX15"
  - "QSZ13"
figures: 5
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/3666094.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/bulletin/3666094.pdf"
tags:
  - "документ/бюллетень"
  - "двигатель/15N"
  - "двигатель/K19"
  - "двигатель/QSX15"
  - "двигатель/QSZ13"
  - "перевод/машинный"
---

# Excessive Fuel Consumption Troubleshooting

> [!abstract] Сервисный бюллетень · `3666094`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]], [[77804810 — 15N CM2380 M104B CPL 5977|77804810]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]], [[93948840 — QSZ13 CM2150 Z102 CPL 4858|93948840]]
> **Семейство:** 15N, K19, QSX15, QSZ13
> **Даты:** выпущен 2007-11-30 · изменён 2010-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/3666094.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/bulletin/3666094.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Чрезмерное потребление топлива устраняет проблемы

Данный Бюллетень является руководством по поиску наиболее эффективного диагностического подхода в ответ на сообщение о чрезмерном расходе топлива. Поскольку каждая комбинация операций двигателя/транспортного средства уникальна, этапы или последовательности могут различаться в разных случаях. Прикладные знания о двигателе и установке являются лучшими инструментами для такого диагноза. Однако систематический, экономически эффективный метод проверки возможной проблемы с двигателем может быть полезен как для устранения неполадок, так и для оператора двигателя.

Первым шагом в эффективной диагностике любой жалобы на работу двигателя является правильное понимание того, что происходит на самом деле или что воспринимается как происходящее. Вместо немедленной работы двигателя для обнаружения заявленной неисправности необходимо принять разумное время для рассмотрения жалобы, понимания технического обслуживания и эксплуатации конкретного транспортного средства и проведения внешнего осмотра транспортного средства и двигателя на предмет соответствующих расхождений. Такой анализ внешних условий, влияющих на заявленную жалобу, является экономичным методом, позволяющим быть более уверенным в том, что относительно дорогие испытания и ремонт двигателя проводятся максимально точно.

Поскольку на расход топлива влияют многочисленные переменные, наиболее точным методом определения расхода топлива в полевых условиях, где имеется различная местность, скорости, время простоя и т.д., является проведение теста на проезд. Этот тест обсуждается в разделе «Прогулка на велосипеде». Тест «Вперед» не всегда (возможно или осуществимо) возможен. Поэтому знания о применяемых двигателях и установках, а также дополнительные элементы, предложенные в этом бюллетене, помогут понять расход топлива.

Следует также отметить, что в этом документе перечислены несколько инструментов (например, VE / VMS®, RoadRelay® и Cadec®), которые могут помочь определить расход топлива. Это **только **инструменты, и информация с этих устройств **должна использоваться для справки **только. Они не являются заменой для фактического тестирования.

Двигатель является только одной частью системы автомобиля. В этом случае Cummins Inc. **не может** и не гарантирует какого-либо конкретного уровня расхода топлива. Как видно из следующей информации, в этом процессе задействованы многочисленные переменные, многие из которых связаны с конструкцией транспортного средства, эксплуатацией владельца или операционной средой.

| Диагностический лист по потреблению топлива |  |
|---|---|
| Имя клиента |  |
| Дата |  |
| Технические характеристики автомобиля: |  |
| Модель двигателя |  |
| Год трактора, тип и модель |  |
| передача |  |
| Коэффициент задней оси |  |
| Количество осей |  |
| Типичный GVW |  |
| Трейлер |  |
| Смело / гладко |  |
| высота |  |
| широта |  |
| Трейлер Gap |  |
| Фейерверк (да/нет) |  |
| Длина |  |
| Аэродинамический % (см. раздел Аэродинамика) |  |
| Размер шин (11R24.5, низкий профиль и т.д.) |  |
| Тип шины (стандартный/дополнительный протектор) |  |
| Тип вентилятора (прямой привод / вискоз / сцепленный) |  |
| Управление питанием (да/нет) |  |
| Компрессор хладагента (да/нет) |  |
| Другие паразитические нагрузки |  |

Ответьте на следующие вопросы:

- Стало ли топливо экономичнее с тех пор, как двигатель стал новым?
- Каков ожидаемый и фактический расход топлива?
- Есть ли проблемы с ускорением или ответом? (Да/Нет)

Если да, то см. раздел Ответ.

| устранение неполадок |  |
|---|---|
| Причина | Устранение |
| На чем основаны ожидания? (Оригинальный пробег, предыдущий пробег, конкурентный двигатель, другие агрегаты, VE/VMS®/другие ожидания, или демонстрационный грузовик) | Запустите отчет VE/VMS®, чтобы определить, являются ли ожидания необоснованными. |
| Это спецификации поездов в Cummins Inc. Рекомендации? (Проверка с помощью VE/VMS®) | Правильно для передачи или компенсации путем установки более низкого регулятора скорости движения (RSG). Объясните компромисс экономии топлива по сравнению с производительностью с существующей передачей. |
| Оценка расхода топлива в течение длительного периода времени (от 3 до 6 месяцев) | Это необходимо для определения последствий сезонных и/или эксплуатационных изменений. |
| Правильно ли был произведен расчет расхода топлива? | Оцените метод для валидности. При необходимости исправлять и переоценивать. Также следует знать о топливных практиках (использование рефрижераторов, блендеров моторного масла, добавок и т.д.). |
| Были ли какие-либо изменения в операционной среде автомобиля, которые способствовали жалобе на расход топлива? (Изменение маршрута, изменение нагрузок, холодная температура окружающей среды, ветреные условия, снег/дождь) | Объясните влияние рабочей среды на измеренный расход топлива. Жалоба на расход топлива может быть основана на неблагоприятных погодных условиях (до одной мили на галлон) или изменениях в маршрутах и/или нагрузках. |
| Какой сорт или смесь топлива используется при подаче жалобы? (Дизель № 1, дизель № 2 или зимнее топливо (P40, P50 и т. д.)) | Дизель № 1 и более легкие зимние виды топлива имеют более низкое содержание тепла и приводят к более высокому расходу топлива. Переоценка с использованием дизельного топлива No2. |
| Достигает ли температура охлаждающей жидкости двигателя нормальной рабочей температуры? | Ремонт по мере необходимости. |
| В последнее время были введены в эксплуатацию тормоза трактора или прицепа? | Проверьте тормоза и ремонт по мере необходимости. |
| Правильно ли выравнивается трейлер? | Ремонт по мере необходимости. |
| Возникла ли жалоба после установки новых шин на трактор или прицеп? | Рассмотрим влияние новых шин и переоцените расход топлива. (Приблизительно 3-процентная разница в радиусе качения между новыми и старыми шинами.) |
| Правильно ли калиброваны одометр и хабометр? | См. раздел «Революции шин на милю» для определения фактических революций шин на милю, калибровки хабометра и параметров революций шин на милю в электронном модуле управления (ECM). См. раздел проверки Hubometer для проверки хабометра. Ремонт или калибровка по мере необходимости и переоценка расхода топлива. |
| Проверьте состояние протектора и инфляционное давление на шинах трактора и прицепа. | Ремонт и надувка шин по мере необходимости и переоценка расхода топлива. |
| Возникла ли жалоба на расход топлива после ремонта двигателя? | Исследуйте ремонт, чтобы определить его влияние на расход топлива (неправильный форсунка, неправильный турбокомпрессор, неправильный код SC и т. д.). |
| Может ли жалоба на расход топлива быть связана с изменением водителей? | Если да, то оцените необходимость обучения водителей. |
| Есть ли признаки внешней или внутренней утечки топлива? | Ремонт по мере необходимости и переоценка расхода топлива. |
| Имеются ли признаки вмешательства в систему CELECTTM (проверить датчик скорости транспортного средства и соответствующую проводку)? | Ремонтировать или исправлять по мере необходимости и переоценивать расход топлива. |
| Имеются ли признаки высоких температур выхлопных газов (треснутые выпускные коллекторы, корпуса турбин, монтажное оборудование и т.д.)? | Это является признаком неправильного соотношения воздух-топливо. Это должно быть проверено на динамометре шасси. |
| Является ли уровень масла правильным? | Высокий уровень масла может вызвать погружение коленчатых или стержней. Слить моторное масло и проверить уровень масла калибровки калибра. Переоценить расход топлива с правильным уровнем масла. |
| Проверьте наличие активных кодов неисправностей или большое количество неактивных кодов неисправностей в двигателях CELECTTM. | Ремонт по мере необходимости и переоценка расхода топлива. |
| Настраиваемые параметры и дополнительные функции (защита от перегрузки) устанавливаются на их правильные / ожидаемые значения и соответствуют ли они транспортным средствам, сравниваемым с автопарком? | Установите параметры на правильные значения и убедитесь, что защита от переключения передач активна и установлена правильно. Переоценить расход топлива. |
| Правильно ли выполняется калибровка ECM? | По мере необходимости снова калибровать и переоценить расход топлива. |
| Верны ли ограничения на расход топлива, наддув, впуск и выхлоп и т.д.? | Проверяйте эти измерения с помощью динамометра шасси. Ремонт по мере необходимости и переоценка расхода топлива. |
| Имеются ли утечки в системе впускного воздуха между турбокомпрессором и впускным коллектором? У кулера с заряженным воздухом есть утечки? | Ремонт системы впуска по мере необходимости. Проверьте охладитель воздуха. Используйте процедуру утечки в Руководстве по устранению неполадок и ремонту, Двигатели N14, Бюллетень 3810456. Ремонт по мере необходимости и переоценка расхода топлива. |

## Аэродинамика

Конфигурация автомобиля играет жизненно важную роль в расходе топлива. Одним из наиболее эффективных инструментов, которые могут быть использованы для понимания передач, маршрутов, весов и аэродинамики, является VMS®. VMS® - это компьютерная программа, которая имитирует работу транспортного средства. Однако, как и в случае с любой компьютерной программой, результаты **только **так же точны, как и используемые данные. Поэтому в VMS® были установлены следующие рекомендации, отражающие эффекты аэродинамики.

Правила аэродинамических значений (дополнительные):

| Процентная доля | конфигурация |
|---|---|
| 0% | Стандартный автомобиль |
| 2% | Для аэродинамического бампера |
| 2% | Для наклонного капота, аэродинамических фар и воздухоочистителя под капотом |
| 1% | Для полных боковых юбок |
| 5-10% | Для дефлекторов крыши 5% для простых дефлекторов или 10% для полноразмерных дефлекторов с удлинителями |
| 0 - 7% | В зависимости от зазоров за кабиной, 0% для более чем 50-дюймового зазора или 1% для 45-49-дюймового зазора или 2% для 40-44-дюймового зазора или 3% для 35-39-дюймового зазора или 4% для 30-34-дюймового зазора или 5% для 25-29-дюймового зазора или 6% для 20-24-дюймового зазора или 7% для менее чем 20-дюймового зазора |

- Большинство грузовиков имеют аэродинамическую от 12 до 20 процентов.
- Наиболее аэродинамические грузовики составляют 22%.
- Некоторые грузовики на 0 процентов аэродинамические.
- Отрицательные аэродинамические средства (-10 процентов) могут возникать при неправильной форме нагрузки на прицепы для мальчиков.
- Отрицательные аэродинамические средства (-X процентов) также могут возникать, когда трактор имеет воздушный дефлектор и тянет плоскую кровать или что-то другое, чем прицеп фургона.
- Танкеры на 5 процентов аэродинамические.
- Ребра прицепов на 10 процентов аэродинамические.
- Плоские кровати на 10-30% аэродинамические.
- Автомобильные перевозчики -30 процентов аэродинамики.

## Ответ

Процедура испытания на реактивность двигателей CELECTTM большой мощности:

Для этого испытания необходим измеритель давления наддува, связанные с ним сантехнические линии и часы остановки.

1. Прикрепить трактор к загруженному прицепу (GCW должен быть от 65 000 до 80 000 фунтов).
2. Убедитесь, что двигатель прогрелся.
3. Определить давление полного повышения нагрузки при пиковом крутящем моменте двигателя при применении полного дроссельного заслонка. (Тормоза прицепа могут также применяться для дополнительной нагрузки, если это необходимо.) Обратите внимание на давление наддува при пиковом крутящем моменте оборота двигателя.
4. Проведите тест на спуске. Выберите второстепенную дорогу, которая имеет минимальный уровень движения. Ускорьте транспортное средство через шестерни, чтобы направить передачу (1 к 1) и на скорость двигателя не менее 300 об/мин выше пиковой скорости двигателя крутящего момента. Позвольте автомобилю спуститься вниз до пиковой скорости двигателя, а затем щелкните дроссель. Измерьте время, необходимое для развития 50% пикового крутящего момента (определяется на шаге 3 выше).
5. Повторите шаг 4 еще два раза для трех точек данных.
6. Вычислите среднее время до 50% повышения: Среднее время до 50% повышения = (время 1 + время 2 + время 3)/3.

Это среднее время должно быть 3 секунды или меньше для приемлемой производительности.

## Тест Райд-Алонга

После выполнения шагов, изложенных ранее в этом бюллетене, иногда бывает полезно провести тест на расход топлива на транспортном средстве. Если все сделано правильно, то этот тест дает результаты экономии топлива, которые являются репрезентативными для тех, которые предсказываются компьютерным моделированием VE/VMS®. Это демонстрирует реалистичный пробег топлива в известных условиях и помогает клиенту понять факторы, которые влияют на пробег бака на транспортном средстве. Путем мониторинга скорости транспортного средства, наполнения топлива, нагрузок, техники водителя и местности можно определить точный показатель пробега топлива.

Другие типы дорожных испытаний, такие как SAE Type II и Type III, обеспечивают повышенную точность пробега танка в моделируемых условиях (определенный курс, скорости, время простоя и т. Д.) За счет дополнительной стоимости и сложности. Эти тесты являются отличным способом сравнения различных транспортных средств, но выходят за рамки этого бюллетеня.

Используйте следующую информацию для получения точных результатов испытаний:

Перед испытанием:

- Выберите маршрут, который является представителем того, что обычно ездит клиент.
- Если возможно, спланируйте поездку так, чтобы начало и конец были в одной точке.
- Если старт и финиш находятся в двух разных местах, имейте в виду, что разница в высоте (ноги над уровнем моря) и ориентация транспортного средства при окончательном заполнении может повлиять на экономию топлива.
- Используйте прицеп и груз, который является представителем нормального использования оператора.
- Планируйте эксплуатировать автомобиль как минимум на 966 км[600 миль], если это возможно. (Более высокие показатели пробега дают более точные результаты испытаний.)
- Проверьте инфляционное давление в шинах. Соблюдайте все шины на наличие признаков смещения.
- Сверху топливный бак (баки) на одной и той же топливной станции, с использованием одного и того же отсека (насоса), обращенного в одном направлении, в начале и в конце испытания.
- Используйте измерительное устройство для топлива, аналогичное измерителю сцепления, показанному в разделе Dangle Meter, для определения постоянной точки (точек) заполнения топливного бака (баков).
- Когда топливные баки заполнены, взвешивайте автомобиль с использованием сертифицированных весов.
- Запишите показания одометра. Если у грузовика есть хабометр, обратите внимание на это.

Во время испытания:

- Если у автомобиля есть круиз-контроль, поощрите водителя использовать это устройство как можно чаще. Это уменьшает вариацию дроссельной заслонки и помогает поддерживать постоянную скорость автомобиля.
- При испытании двигателя COMMAND Concept L10 или N14 оптимальная экономия топлива достигается при низкой оборотной массе (1400-1600 оборотов в минуту при крейсерской) работе. Поощряйте водителя притягивать двигатель на холмах до 1100-1200 об/мин. Минимизируйте работу двигателя выше 1700 об/мин в ситуациях с понижением.
- Проверяйте работу одометра с помощью маркеров мили вдоль шоссе. Точность спидометра также может быть проверена таким образом.
- Если скорость транспортного средства значительно изменяется в ходе испытания, разделить пройденное расстояние (мили) на количество часов, чтобы определить среднюю скорость.
- Обратите внимание на местность и попытайтесь определить, какое из трех симуляций VE / VMS® лучше всего представляет поездку:

- Почти 1 и 2 процента классов
- Короткие холмы до 5% классов
- Длинные горные сорта.

- Минимизируйте время простоя, если это возможно. Если оператор настаивает на холостом ходу двигателя в течение длительных периодов времени (более 5-минутных сегментов), запишите общее количество минут и разделите это число на общее количество минут работы двигателя, чтобы определить процент времени простоя для поездки.

В конце испытания:

- Если исходная точка испытания находится в том же месте, что и исходная точка, заполните бак (баки), используя тот же насос, в том же заливе, при этом транспортное средство припарковано в том же направлении, что и начальная заправка.
- Используйте измеритель расхода топлива для точного пополнения топливного бака (баков).

> [!note] Примечание
> Убедитесь, что датчик дунга последовательно расположен на шее наполнителя. Непоследовательное позиционирование может привести к расхождениям в ваших конечных результатах.

- Разделите расстояние (мили) на количество галлонов, используемых для определения миль на галлон.
- Если ошибка одометра была замечена ранее в поездке, вычислите скорректированные мили. Разделите скорректированные мили на количество галлонов, используемых в поездке, чтобы получить скорректированные мили на галлон.
- Если окончательная компьютерная симуляция VE/VMS® является опцией, запустите симуляцию, используя фактическую (или предполагаемую) скорость транспортного средства, массу брутто, рельеф местности и т. Д., Чтобы проверить более ранние прогнозы на пробег топлива.
- Поделитесь результатами теста с водителем и запишите комментарии водителя.

## Революции в МИЛЕ

![[05800092.png]]

1 Измерение расстояния 1 революция

1. Накачайте шины до 621/689 кПа \[90/100 psi\] или до рекомендуемого давления и запишите значения.
2. Задний ход автомобиля под загруженным прицепом.
3. Располагайте трактор и прицеп на ровной поверхности.
4. Поставьте вертикальную отметку в верхней и нижней части шины и соответствующую отметку на плоской поверхности.
5. Переверните автомобиль вперед ровно на одну (1) оборот шины; и поставьте вторую отметку на поверхности, выровнявшись с вертикальной отметкой, ранее размещенной в нижней части шины. Используйте уровень, чтобы выровнять отметки в верхней и нижней части шины с отметкой, помещенной на поверхность.
6. Измерьте расстояние между отметками и разделите значение (в футах) на 5280 (фут/ми), чтобы точно определить обороты шин на милю.

Окружность шины:

Революции шин/миля:

Инфляционное давление:

Комментарии:

![[05800093.png]]

## ВЕРИФИКАЦИЯ БУМЕТЕРА

- Поместите хабометр на испытательный стенд топливного насоса Cummins®, используя переднюю крышку топливного насоса PT с адаптером резьбы (см. выше иллюстрацию).
- Установите подставку топливного насоса, работающую на оборотах, на заданную революцию хабометра на милю.

![[05800094.png]]

10 минут = 10 миль

- Провести верификационное испытание в течение 10 минут при указанной оборотной частоте для определения точности губометра (см. выше иллюстрацию).

![[05800090.png]]

## Щелкунчик

Калибр с болтовым измерителем используется для последовательного измерения уровня топлива в баке во время испытаний расхода топлива объемного типа.

![[05800091.png]]

> [!note] Примечание
> Убедитесь, что датчик дунга последовательно расположен на шее наполнителя. Непоследовательное позиционирование может привести к расхождениям в конечных результатах.

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## Excessive Fuel Consumption Troubleshooting
>
> This Service Bulletin is a guide for finding the most effective diagnostic approach in response to a report of excessive fuel consumption. Because each engine/vehicle operation combination is unique, the steps or sequences can vary for different cases. Applied engine and installation knowledge are the best tools for such a diagnosis. However, a systematic, cost-effective method of checking for a possible engine problem can be valuable to both the troubleshooter and engine operator.
>
> The first step in the effective diagnosis of any complaint about engine operation is a proper understanding of what is actually happening, or what is perceived to be happening. Rather than immediate engine work to locate a reported malfunction, reasonable time **must** be taken to review the complaint, understand the maintenance and operation of the particular vehicle, and to make an external examination of the vehicle and engine for related discrepancies. Such a review of external conditions which impact the reported complaint is a time and labor-saving method to be more certain that the relatively expensive engine tests and repairs are directed as accurately as possible.
>
> Because numerous variables affect fuel consumption, the most accurate method of determining fuel consumption in the field, where there is varying terrain, speeds, idle time, etc., is to conduct a ride-along test. This test is discussed in the Ride-Along Test section. The ride-along test is **not always** possible or feasible. Therefore, applied engine and installation knowledge, along with additional items suggested in this bulletin, will assist in understanding fuel consumption.
>
> It **must** also be noted that there are several tools (i.e., VE/VMS®, RoadRelay®, and Cadec®) listed in this document which can help determine fuel consumption. These are **only** tools, and the information from these devices **must** be used for reference **only**. They are **not** a substitute for actual ride-along testing.
>
> The engine is **only** one part of the vehicle system. Therefore, Cummins Inc. can **not** and does **not** guarantee any specific fuel consumption level. As can be seen by the following information, numerous variables are involved, many being related to the vehicle design, owner operation, or operating environment.
>
> | Fuel Consumption Diagnostic Worksheet |  |
> |---|---|
> | Customer Name |  |
> | Date |  |
> | Vehicle Specifications: |  |
> | Engine Model |  |
> | Tractor Year, Type, and Model |  |
> | Transmission |  |
> | Rear Axle Ratio |  |
> | Number of Axles |  |
> | Typical GVW |  |
> | Trailer |  |
> | Ribbed/Smooth |  |
> | Height |  |
> | Width |  |
> | Trailer Gap |  |
> | Fairing (Yes/No) |  |
> | Length |  |
> | Vehicle Aerodynamic % (See the Aerodynamics Section) |  |
> | Tire Size (11R24.5, Low Profile, etc.) |  |
> | Tire Type (Standard/Extra Tread) |  |
> | Fan Type (Direct Drive/Viscous/Clutched) |  |
> | Power Steering (Yes/No) |  |
> | Refrigerant Compressor (Yes/No) |  |
> | Other Parasitic Loads |  |
>
> Answer the following questions:
>
> - Has fuel economy gotten worse since the engine was new?
> - What is the expected and actual fuel mileage?
> - Is there a problem with acceleration or response? (Yes/No) \*
>
> \*If yes, see the Response section.
>
> | Troubleshooting |  |
> |---|---|
> | Cause | Correction |
> | What are the expectations based on? (Original mileage, previous mileage, competitive engine, other units, VE/VMS®/other expectations, or demonstration truck) | Run a VE/VMS® report to determine if expectations are unreasonable. |
> | Are the drive train specifications within Cummins Inc. recommendations? (Verify with a VE/VMS® run) | Correct for gearing or compensate by setting a lower road speed governor (RSG). Explain the trade-off of fuel economy versus performance with present gearing. |
> | Evaluate fuel consumption over an extended period of time (3 to 6 months) | This is necessary to determine the effects of seasonal and/or operational changes. |
> | Was the calculation of fuel consumption done correctly? | Evaluate the method for validity. Correct and reevaluate, if necessary. Also, be aware of fuel practices (use of reefers, lubricating oil blenders, additives, etc.). |
> | Were there any changes in the vehicle's operating environment that contributed to the fuel consumption complaint? (Change of route, change of loads, cold ambient temperatures, windy conditions, snow/rain) | Explain the effects of the operating environment on the measured fuel consumption. A fuel consumption complaint may be based on adverse weather (up to one mile per gallon) or changes in routes and/or loads. |
> | What grade or blend of fuel is being used when the complaint is generated? (Diesel number 1, diesel number 2, or winter fuel (P40, P50, etc.)) | Diesel number 1 and lighter winter fuels are lower in heat content and result in higher fuel consumption. Reevaluate using number 2 diesel fuel. |
> | Does the engine coolant temperature reach normal operating temperature? | Repair as necessary. |
> | Have the tractor or trailer brakes been recently serviced? | Check for dragging brakes and repair as necessary. |
> | Is the trailer alignment correct? | Repair as necessary. |
> | Has the complaint occurred after new tires were installed either on the tractor or the trailer? | Consider the effects of new tires and reevaluate fuel consumption. (There is an approximate 3 percent difference in the rolling radius between new and old tires.) |
> | Are the hubometer and odometer calibrated correctly? | See the Tire Revolutions Per Mile section to determine the actual tire revolutions per mile, in calibration of hubometer and tire revolutions per mile parameter in the electronic control module (ECM). See the Hubometer Verification section for hubometer verification. Repair or calibrate as necessary and reevaluate fuel consumption. |
> | Check the tread condition and the inflation pressure on both the tractor and the trailer tires. | Repair and inflate the tires as necessary and reevaluate fuel consumption. |
> | Has the fuel consumption complaint occurred after an engine repair? | Investigate the repair to determine its effect on fuel consumption (incorrect injectors, incorrect turbocharger, incorrect SC code, etc.). |
> | Can the fuel consumption complaint be correlated to a change in drivers? | If yes, evaluate the need for driver training. |
> | Are there any signs of external or internal (crankcase) fuel leakage? | Repair as necessary and re-evaluate fuel consumption. |
> | Are there signs of tampering with the CELECT™ system (inspect the vehicle speed sensor and the corresponding harness)? | Repair or correct as necessary and re-evaluate fuel consumption. |
> | Are there indications of high exhaust temperatures (cracked exhaust manifolds, turbine casings, mounting hardware, etc.)? | This is an indication of an incorrect air-to-fuel ratio. This **must** be verified on a chassis dynamo-meter. |
> | Is the oil level correct? | High oil levels can cause crank or rod dipping. Drain the engine oil and verify the dipstick calibration. Reevaluate fuel consumption with the correct oil level. |
> | Check for active fault codes or high counts of inactive fault codes on CELECT™ engines. | Repair as necessary and reevaluate fuel consumption. |
> | Are adjustable parameters and optional features (gear down protection) set to their correct/expected values, and are they consistent with vehicles being compared to in the fleet? | Set the parameters to the correct values and make sure that gear down protection is active and set correctly. Reevaluate fuel consumption. |
> | Is the ECM calibration correct? | Calibrate again, as necessary, and reevaluate fuel consumption. |
> | Are fuel rate, boost, intake and exhaust restrictions, etc., correct? | Verify these measurements using a chassis dynamometer. Repair as necessary and reevaluate fuel consumption. |
> | Are there leaks in the intake air system between the turbocharger and the intake manifold? Does the charge air cooler have leaks? | Repair the intake system as necessary. Check the charge air cooler. Use the leak down procedure in the Troubleshooting and Repair Manual, N14 Engines, Bulletin 3810456. Repair as necessary and reevaluate fuel consumption. |
>
> ## AERODYNAMICS
>
> The vehicle configuration plays a vital role in fuel consumption. One of the most effective tools that can be used in understanding gearing, routes, weights, and aerodynamics is VMS®. VMS® is a computer program that simulates the vehicle operation. However, as with any computer program, the results are **only** as accurate as the data used. Therefore, the following guidelines have been established in VMS® to reflect the effects of aerodynamics.
>
> Rules for aerodynamic values (additive):
>
> | Percentage | Configuration |
> |---|---|
> | 0% | Standard vehicle |
> | 2% | For aerodynamic bumper |
> | 2% | For sloped hood, aerodynamic headlights, and under-hood air cleaner |
> | 1% | For full side skirts |
> | 5 to 10% | For roof deflector, 5% for simple deflectors or 10% for full width deflectors with extenders |
> | 0 to 7% | Depending on gaps beyond cab, 0% for more than 50-inch gap or 1% for 45 to 49-inch gap or 2% for 40 to 44-inch gap or 3% for 35 to 39-inch gap or 4% for 30 to 34-inch gap or 5% for 25 to 29-inch gap or 6% for 20 to 24-inch gap or 7% for less than 20-inch gap |
>
> - Most trucks are 12 to 20 percent aerodynamic.
> - The most aerodynamic trucks are 22 percent aerodynamic.
> - Some trucks are 0 percent aerodynamic.
> - Negative aerodynamic aids (-10 percent) can occur with irregularly shaped loads on lowboy trailers.
> - Negative aerodynamic aids (-X percent) can also occur when the tractor has an air deflector and is pulling a flatbed or something other than a van trailer.
> - Tanker trucks are -5 percent aerodynamic.
> - Rib trailers are -10 percent aerodynamic.
> - Flat beds are -10 to -30 percent aerodynamic.
> - Car haulers are -30 percent aerodynamic.
>
> ## RESPONSE
>
> Response testing procedure for heavy duty CELECT™ engines:
>
> For this test, a boost pressure gauge, associated plumbing lines, and a stop watch are needed.
>
> 1. Attach the tractor to a loaded trailer (GCW **must** be 65,000 to 80,000 pounds).
> 2. Make sure the engine is warmed up.
> 3. Determine the full load boost pressure at torque peak engine speed while applying full throttle. (Trailer brakes may also be applied for additional loading, if required.) Note the boost pressure at torque peak engine speed.
> 4. Perform the coast down test. Select a secondary road that is level and has minimal traffic. Accelerate the vehicle up through the gears to direct gear (1 to 1) and to an engine speed of at least 300 rpm above the torque peak engine speed. Allow the vehicle to coast down to torque peak engine speed then snap the throttle. Measure the time required to develop 50 percent of torque peak boost (determined in Step 3 above).
> 5. Repeat Step 4 two more times for a total of three data points.
> 6. Calculate the average time to 50 percent boost: Average time to 50 percent boost = (time 1 + time 2 + time 3)/3.
>
> This average time **must** be 3 seconds or less for acceptable performance.
>
> ## RIDE-ALONG TEST
>
> After completing the steps outlined previously in this bulletin, there are occasional instances where it is beneficial to conduct a ride-along fuel consumption test on the vehicle. If done correctly, this test provides fuel economy results which are representative of those predicted by the VE/VMS® computer simulation. This demonstrates realistic fuel mileage under known conditions, and helps a customer understand the factors which influence tank mileage on the vehicle. By monitoring vehicle speed, fuel fill, loads, driver technique, and terrain, an accurate fuel mileage figure can be determined.
>
> Other types of road tests, such as SAE Type II and Type III provide increased tank mileage accuracy under simulated conditions (defined course, speeds, idle time, etc.) at the expense of added cost and complexity. These tests are excellent ways to compare different vehicles but are beyond the scope of this bulletin.
>
> Use the following information to obtain accurate ride-along test results:
>
> Prior to the test:
>
> - Choose a route that is representative of what the customer normally drives.
> - If possible, plan the trip so that the start and finish are at the same point.
> - If the start and finish are at two different locations, be aware that differences in elevation (feet above sea level) and the orientation of vehicle at final fill can impact fuel economy.
> - Use a trailer and load that is representative of the operator's normal use.
> - Plan to operate the vehicle for a minimum of 966 km \[600 mi\], if possible. (Higher mileage accumulations provide more accurate test results.)
> - Check the tire inflation pressures. Observe all tires for signs of misalignment.
> - Top off the fuel tank(s) at the same fuel station, using the same bay (pump), facing the same direction, at the start and at the conclusion of the test.
> - Use a fuel gauge device similar to the dangle meter shown in the Dangle Meter section to determine consistent fill point(s) in the fuel tank(s).
> - When the fuel tanks are full, weigh the vehicle using certified scales.
> - Record the odometer reading. If the truck has a hubometer, note that as well.
>
> During the test:
>
> - If the vehicle has cruise control, encourage the driver to use this device as much as possible. This reduces throttle variation and helps maintain a consistent vehicle speed.
> - If testing a COMMAND concept L10 or N14 engine, optimum fuel economy is obtained with low rpm (1400 to 1600 rpm at cruise) operation. Encourage the driver to lug the engine to 1100 to 1200 rpm on hills. Minimize engine operation above 1700 rpm in downshift situations.
> - Verify odometer operation using mile markers along the highway. Speedometer accuracy can also be verified in this manner.
> - If the vehicle speed varies significantly through the test, divide the distance traveled (miles) by the number of hours to determine the average speed.
> - Note the terrain and attempt to determine which of the three VE/VMS® simulations best represents the trip:
>
> - Near level 1 and 2 percent grades
> - Short hills up to 5 percent grades
> - Long mountain grades.
>
> - Minimize idle time, if possible. If the operator insists on idling the engine for extended periods of time (greater than 5-minute segments), record the total minutes and divide this number by the total engine operation minutes to determine the percentage of idle time for the trip.
>
> At the end of the test:
>
> - Assuming the end point of the test is at the same location as the start point, fill the tank(s), using the same pump, in the same bay, with the vehicle parked in the same direction as the initial fill.
> - Use the fuel gauge dangle meter to accurately top off the fuel tank(s).
>
> **Note · Примечание**
> Make sure the dangle meter is consistently positioned on the filler neck. Inconsistent positioning can cause discrepancies in your final results.
>
> - Divide the distance (miles) by the number of gallons used to determine miles per gallon.
> - If an odometer error was noted earlier in the trip, calculate the corrected miles. Divide the corrected miles by the number of gallons used on the trip to get the corrected miles per gallon.
> - If a final VE/VMS® computer simulation is an option, run the simulation, using actual (or estimated) vehicle speed, gross vehicle weight, terrain, etc., to verify earlier predictions on fuel mileage.
> - Share the test results with the driver and record the driver's comments.
>
> ## TIRE REVOLUTIONS PER MILE
>
> (1) Measure distance (1 revolution)
>
> 1. Inflate the tires to 621/689 kpa \[90/100 psi\], or to the recommended pressure, and record the values.
> 2. Back the vehicle under a loaded trailer.
> 3. Locate the tractor and trailer on a flat surface.
> 4. Put a vertical mark at the top and bottom of the tire and a corresponding mark on the flat surface.
> 5. Roll the vehicle forward exactly one (1) tire revolution; and put a second mark on the surface, aligning with the vertical mark previously placed at the bottom of the tire. Use a level to align the marks at the top and bottom of the tire with the mark being placed on the surface.
> 6. Measure the distance between the marks and divide the value (in feet) into 5280 (ft/mi) to accurately determine the tire revolutions per mile.
>
> Tire circumference:
>
> Tire revolutions/mile:
>
> Inflation pressure:
>
> Comments:
>
> ## HUBOMETER VERIFICATION
>
> - Put the hubometer on a Cummins® fuel pump test stand by using a front cover from a PT fuel pump with a thread adapter (see above illustration).
> - Set the fuel pump stand operating rpm to the specified hubometer revolution per mile.
>
> 10 minutes = 10 miles
>
> - Conduct a verification test for 10 minutes at the specified rpm to determine the accuracy of the hubometer (see above illustration).
>
> ## DANGLE METER
>
> A dangle meter gauge is used to consistently measure the fuel level in the tank during volumeteric-type fuel consumption testing.
>
> **Note · Примечание**
> Make sure the dangle meter is consistently positioned on the filler neck. Inconsistent positioning can cause discrepancies in the final results.
>
> ### Document History
