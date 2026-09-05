---
aliases:
  - "Диагностика топливной системы"
type: "Процедура"
doc: "269-005-236"
title_en: "Fuel System Diagnostics"
title_ru: "Диагностика топливной системы"
modified: "2020-07-01"
engines:
  - "93948840"
families:
  - "QSZ13"
manuals:
  - "4358369"
figures: 33
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/269/269-005-236.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/269-005-236.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSZ13"
  - "группа/269"
  - "перевод/машинный"
---

# Fuel System Diagnostics
**Диагностика топливной системы**

> [!abstract] Процедура · `269-005-236`
> **Двигатели:** [[93948840 — QSZ13 CM2150 Z102 CPL 4858|93948840]]
> **Семейство:** QSZ13
> **Входит в руководства:** [[4358369 — QSZ13 CM2150 Z102 Service Manual|4358369]]
> **Секции:** Section 5 - Fuel System - Group 05
> **Даты:** изменён 2020-07-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/269/269-005-236.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/269-005-236.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

> [!danger] ОПАСНО
> При работе со сжатым воздухом применяйте защиту глаз и лица. Разлетающиеся частицы и грязь могут привести к травме.

> [!danger] ОПАСНО
> При работе с пароочистителем надевайте защитные очки или щиток и защитную одежду. Горячий пар может привести к тяжёлой травме.

> [!warning] ОСТОРОЖНО
> Очистите все фитинги перед разборкой. Грязь или загрязняющие вещества могут повредить топливную систему.

Перед обслуживанием () любых компонентов топливной системы (таких как топливные линии, топливный насос, форсунка и т.д.), которые подвергают топливную систему или внутренние компоненты двигателя воздействию потенциальных загрязнителей до разборки, очистки фитингов, монтажного оборудования и области вокруг компонента, который должен быть удален. Грязь или загрязняющие вещества могут быть введены в топливную систему и двигатель, если окружающие области не очищены, что приводит к повреждению топливной системы и двигателя.[[99-000-009 — Engine Cleaning|См. процедуру 000-009 в разделе 0.]]

Чтобы предотвратить повреждение двигателя от мусора или загрязнения, крышка, крышка или заглушка любых отверстий как можно скорее при обслуживании топливной системы. Набор для чистого ухода, номер детали 4919073.

![[00c00206.png]]

Для диагностики проблем топливной системы используются следующие процедуры. Эти проверки и измерения по мере необходимости упоминаются во всех применимых деревьях кода неисправностей и неисправностей.

Эта процедура не предназначена для того, чтобы занять место направления устранения неполадок при ремонте деревьев.

Смотрите соответствующее дерево симптомов устранения неполадок для направления ремонта.

![[ck800wa.png]]

### Система высокого давления снимается с теста

> [!note] Примечание
> Этот тест может быть выполнен, если двигатель не запускается.

Подключите электронный сервис INSITETM.

Управляйте двигателем.

Контролируйте давление топливной рельсы.

Проверьте распад давления топлива.

Выключите двигатель и ждите, пока он полностью остановится. Включите переключатель зажигания быстро.

Мониторинг электронного оборудования для обслуживания INSITETM и запись давления топливной рельсы в течение 1 минуты.

Изменение давления топлива более 100 бар \[1450 psi\] за 1 минуту является признаком утечки топливной системы высокого давления.

Смотрите соответствующее дерево симптомов устранения неполадок для направления ремонта.

![[19c01817.png]]

### Проверка системы низкого давления

Система контроля низкого давления состоит из ряда измерений и проверок, чтобы убедиться, что топливная система низкого давления функционирует должным образом. Эти проверки будут варьироваться в зависимости от того, запустится двигатель или нет.

![[eg8gasj.png]]

Измерение - двигатель запустится

Проверьте воздух в топливе. См. процедуру 006-003 в разделе 6.

![[06d00542.png]]

Измерить ограничение впуска топлива. См. процедуру 006-020 в разделе 6.

![[05c00259.png]]

Измерьте выходное давление топливного насоса. Используйте инструкции в разделе Испытания давления нагнетателя нагнетателя на топливный насос в этой процедуре.

![[05c00436.png]]

Измерьте ограничение топливного фильтра. Используйте инструкции в разделе «Ограничение топливных фильтров» этой процедуры.

![[05c00438.png]]

Измерить ограничение линии слива топлива. См. процедуру 006-012 в разделе 6.

![[05c00438.png]]

Измерение: двигатель не запускается

Измерьте давление на выходе топливного переключателя во время проворачивания. Используйте инструкции в разделе Испытания давления нагнетателя нагнетателя на топливный насос в этой процедуре.

![[05c00436.png]]

Измерить ограничение линии слива топлива. См. процедуру 006-012 в разделе 6.

![[06c00256.png]]

### Испытание давления нагнетателя нагнетателя на топливный насос

Измерение - двигатель запустится

Установите датчик измерения давления от 0 до 2068 кПа \[0 до 300 psi\] на установке CompuchekTM на входе в головку установки топливного фильтра.

Управляйте двигателем на высоком холостом ходу и наблюдайте за давлением топливного переключателя.

| Напорное давление на высоком холостом ходу |  |  |
|---|---|---|
| каша |  | пси |
| 1000 | Мин | 145 |

![[05c00436.png]]

Измерение: двигатель не запускается

Установите датчик измерения давления от 0 до 207 кПа \[0 до 30 psi\] на установке CompuchekTM на входе в головку установки топливного фильтра.

Прокрутите двигатель и наблюдайте за давлением топливного переключателя.

| Напорное давление в коленке |  |  |
|---|---|---|
| каша |  | пси |
| 69 | Мин | 10 |

![[05c00444.png]]

### Ограничение фильтрации топлива

Первоначальная настройка

Установите 1/8-дюймовый NPT CompuchekTM в адаптер для установки на банджо, номер детали 4919057, и установите собранную установку в выпускной отверстий топливного фильтра со стороны давления.

Подключите перфорированную диагностическую топливную линию, Номер детали 3164621, к адаптеру для установки на банджо и маршруту к топливному баку двигателя или другому подходящему контейнеру.

Пробная диагностическая топливная линия используется в процедурах для создания номинального потока через топливную систему низкого давления без необходимости работы двигателя под нагрузкой.

![[05c00437.png]]

Измерение

Установите датчик измерения давления от 0 до 2068 кПа \[0 до 300 psi\] на установке CompuchekTM на входе в головку установки топливного фильтра.

Управляйте двигателем при высоком холостом ходу и наблюдайте за давлением на входе фильтра.

Установите датчик измерения давления от 0 до 2068 кПа \[0 до 300 psi\] на установке CompuchekTM на выходе к головке установки топливного фильтра.

Управляйте двигателем на высоком холостом ходу и наблюдайте за давлением розетки фильтра.

| Ограничение фильтрации топлива |  |  |
|---|---|---|
| каша |  | пси |
| 138 | Макс | 20 |

Если разница между давлением на входе фильтра и давлением на выходе фильтра больше, чем указано в спецификации, замените топливный фильтр.

![[05c00438.png]]

### Испытание на возврат потока топливного насоса высокого давления

> [!danger] ОПАСНО
> В зависимости от обстоятельств, дизельное топливо легковоспламеняется. При осмотре или выполнении обслуживания или ремонта топливной системы, чтобы уменьшить вероятность пожара и в результате серьезных травм, смерти или повреждения имущества, никогда не курить или разрешать искры или пламя (например, пилотные огни, электрические выключатели или сварочное оборудование) в рабочей зоне.

> [!warning] ОСТОРОЖНО
> Установка адаптера потока банджо в любом месте, кроме рекомендуемых мест, может привести к повреждению компонентов топливной системы высокого давления.

В этом тесте используется адаптер потока. Цель установки адаптера потока состоит в том, чтобы направить поток слива головки топливного насоса **только **в устройство сбора, чтобы можно было измерить утечку.

Для этой процедуры требуется использовать тестировщик утечки топливной системы, номер детали 3164618.

![[05d00790.png]]

Первоначальная настройка

> [!warning] ОСТОРОЖНО
> Убедитесь, что держите фитинги банджо, затягивая болт банджо, чтобы предотвратить вращение фитинга. Разрешение вращать фитинг банджо может повредить топливную линию.

Удалите болт M12, соединяющий соединение слива топлива с головкой топливного насоса.

Установите адаптер потока банджо, номер детали 3164618, на соединение с отводом топлива и направляйте шланг от этого адаптера в ведро или топливный бак автомобиля. Это изолирует форсунка и слив клапана высокого давления из слива топливного насоса.

Отсоедините возврат топлива OEM и зажмите шланг над сливом топлива, который будет маршрутизирован для измерения.

![[05c00439.png]]

> [!warning] ОСТОРОЖНО
> Испытание на утечку под высоким давлением в электронном сервисном оборудовании INSITETM заставит двигатель работать при повышенных давлениях, пока двигатель не работает. Шум двигателя будет меняться, когда это испытание проводится из-за более высоких давлений впрыска топлива. Очки безопасности следует носить во время работы рядом с работающим двигателем. Топливные линии не должны корректироваться при выполнении этого испытания.

Закройте крышку (-ы) двигателя во время выполнения этих испытаний.

![[05d00818.png]]

Измерение - двигатель запустится

Если двигатель запускается, выполните электронный сервис INSITETM, оснащающий высоконапорный тест на утечку.

Подключите инструмент электронного сервиса INSITETM.

Запустите двигатель и позвольте двигателю простаивать с топливом, поступающим в устройство сбора.

Начните тест на утечку высокого давления.

Измерьте время, необходимое для сбора 450 мл (куб) расхода слива топливного насоса при выполнении испытания на утечку под высоким давлением.

Используйте градуированный цилиндр для этого измерения.

Это измерение следует принимать трижды, но используется только третье чтение.

![[19c01817.png]]

| Максимальный объем топлива во время испытания на утечку под высоким давлением |  |
|---|---|
| мл (cc) | секунды |
| 450 | 30 |

Если расход слива головки насоса составляет 450 мл (cc) менее чем за 30 секунд, головка топливного насоса выходит из строя и должна быть заменена.

Эта спецификация действительна для двигателей, работающих на дизельном топливе. Низкая вязкость топлива увеличит скорость утечки; например, керосин или авиационное топливо приведут к чрезмерной утечке. Проверьте тип топлива перед заменой головки топливного насоса на чрезмерную утечку.

![[05d00821.png]]

Измерение: двигатель не запускается

Начните сворачивать двигатель, пока топливо не выйдет из линии слива.

> [!note] Примечание
> Не останавливайте двигатель в течение 30 секунд. Проворачивайте двигатель через 15 вторых интервалов с 15-секундной паузой между интервалами. Это снижает возможность перегрева пускового двигателя.

Когда топливо начинает выходить из линии слива, направляйте поток слива в градуированный цилиндр и продолжайте проворачивать в течение 30 секунд.

Это измерение следует принимать трижды, но используется только третье чтение.

| Максимальный объем топлива во время проворачивания |  |
|---|---|
| мл (cc) | секунды |
| 320 | 30 |

Если поток слива головки насоса 320 мл (cc) собирается менее чем за 30 секунд срабатывания, головка насоса вышла из строя и должна быть заменена.

![[05d00819.png]]

### Высоконапорный форсунка Return Flow Test

Первоначальная настройка

> [!warning] ОСТОРОЖНО
> Установка адаптера потока банджо в любом месте, кроме рекомендуемых мест, может привести к повреждению компонентов топливной системы высокого давления.

> [!note] Примечание
> Убедитесь, что двигатель находится в рабочем состоянии, прежде чем начинать это испытание.

Возвратное топливо передается от топливного форсунка и топливного рельсового предохранительного клапана высокого давления через общую обратную линию. Общая обратная линия соединяется с соединением слива топлива, которое также получает слив топлива из головки топливного насоса.

Измерение утечки топливного форсунка требует использования шланга возврата топлива и специальной топливной арматуры, Части № 4919058 и 3164618.

Инструменты используются в комбинации для изоляции утечки из форсунки, поэтому его можно измерить в градуированный цилиндр.

![[05d00255.png]]

> [!danger] ОПАСНО
> В зависимости от обстоятельств, дизельное топливо является легковоспламеняющимся. При осмотре или выполнении обслуживания или ремонта топливной системы, чтобы уменьшить вероятность пожара и в результате серьезных травм, смерти или повреждения имущества, никогда не курите и не допускайте искр или пламени (например, пилотные огни, электрические выключатели или сварочное оборудование) в рабочей зоне.

Удалите болт банджо, который соединяет общую линию стока с клапаном сброса высокого давления.

Установите 1/8-дюймовый NPT CompuchekTM в адаптер для монтажа на банджо, номер детали 4919058, и установите собранную установку на сливной клапан сброса давления топлива. Используйте быстрое подключение для маршрутизации топлива в устройство сбора или обратно в топливный бак автомобиля.

Удалите болт банджо, который соединяет общую линию слива с топливным сливным соединением на топливном насосе.Установите шланг возврата топлива, номер детали 3164618, на сливном соединении на топливном насосе.

Маршрут возврата топлива в устройство сбора, которое помечено кубическими сантиметрами.

> [!note] Примечание
> Может использоваться цилиндр с выпускным номером 4919139 или аналогичное измерительное устройство.

![[05c00440.png]]

Измерение - двигатель запустится

Если двигатель запускается, выполните электронный сервис INSITETM, оснащающий высоконапорный тест на утечку.

Подключите инструмент электронного сервиса INSITETM.

Запустите двигатель и позвольте двигателю простаивать с топливом, поступающим в устройство сбора.

Начните тест на утечку высокого давления.

| Спецификация на удачу с двигателем |  |
|---|---|
| Максимальная утечка за 1 минуту | 70 мл (cc) |

> [!note] Примечание
> Температура топлива и тип топлива будут влиять на это измерение. Например, по мере нагревания двигателя и нагрева форсунки скорость утечки будет увеличиваться. Кроме того, топливо с низкой вязкостью, такое как керосин, приведет к увеличению скорости утечки. Вышеуказанная спецификация является правильной для дизельного топлива на шоссе, где температура впуска топлива составляет менее 49 ° C \[120°F \].

После регистрации количества утечки топлива остановите электронный сервис INSITETM, оснащающий высоконапорный тест на утечку и выключите переключатель зажигания.

> [!note] Примечание
> Убедитесь, что постоянный поток топлива присутствует на линии слива перед началом измерения. Воздух в линии и движение шланга во время измерения могут привести к неточной оценке.

![[19c01817.png]]

Если расход топлива на форсунок является чрезмерным, необходимо изолировать поврежденный или изношенный топливный форсунок (форсунки) или топливный разъём (коннекторы).

Неплотный топливный разъем, удерживающий гайку, приводит к плохому уплотнению на границе между топливным разъемом и топливным форсункой. Свободное состояние приведет к утечке топлива высокого давления в слив топливного форсунка.

Сначала проверьте, что топливные разъемы правильно затянуты. См. процедуру 006-052 в разделе 6.

Если найдено рыхлое удерживающее (неактивное) орехо(ы), проверьте на утечку после затягивания удерживающего (неактивного) гайки(ов).

![[05c00442.png]]

Измерение: двигатель не запускается

Проворачивайте двигатель до тех пор, пока топливо не выйдет из линии слива.

> [!note] Примечание
> Не останавливайте двигатель в течение 30 секунд. Проворачивайте двигатель через 15 вторых интервалов с 15-секундной паузой между интервалами. Это снижает возможность перегрева пускового двигателя.

Когда топливо начинает выходить из линии слива, направляйте поток слива в градуированный цилиндр и продолжайте проворачивать в течение 30 секунд.

Утечка должна быть только несколько капель. Любое количество капель указывает на отказ форсунки или разъема высокого давления.

> [!note] Примечание
> Давление от топливной системы, направленное после каждого проворачивания.

![[05c00441.png]]

### Испытание на изоляцию потока топлива под высоким давлением

> [!danger] ОПАСНО
> Нормальная работа двигателя создает топливо под высоким давлением в топливной линии, которое останется в топливной линии после отключения двигателя. Никогда не открывайте топливную систему, когда двигатель работает. Перед обслуживанием топливной системы всегда ослабляйте топливный поток от насоса до рельса на рельсе, чтобы выпустить давление. Держите руки подальше от линии при растяжении. Топливный спрей высокого давления может проникать в кожу, что приводит к серьезным травмам или смерти.

Перед обслуживанием топливной системы высокого давления ослабьте линию насос-рельс на рельсе, чтобы выпустить давление.

Держите руки подальше от линии при растяжении.

Затяните гайку топливной рельсы.

Момент затяжки:

> [!note] Примечание
> Обрабатываемый слот в этой установке направляет топливный спрей к двигателю.

![[00c00206.png]]

> [!warning] ОСТОРОЖНО
> Не устанавливайте изоляционный инструмент на розетку насоса высокого давления. В результате будет получено серьезное повреждение двигателя. Этот инструмент должен быть установлен только на топливной рельсе с целью изоляции подачи топлива высокого давления от индивидуального топливного форсунка.

> [!warning] ОСТОРОЖНО
> Убедитесь, что переключатель зажигания находится в положении выключения (двигатель не работает) при ослаблении или затягивании топливных линий высокого давления.

Используйте инструмент для изоляции от утечек, номер детали 4918563, чтобы изолировать чрезмерный расход топлива от топливного форсунка или топливных разъемов.

Следуйте шагу сброса давления (показанному на предыдущем шаге) перед каждой установкой изоляционного инструмента.

![[05c00399.png]]

Изолируйте топливный форсунок и топливный разъем для каждого цилиндра, установив инструмент изоляции на топливной рельсе вместо топливной линии высокого давления, которая поставляет топливный разъем.

Момент затяжки:

![[05c00440.png]]

Зафиксируйте количество расхода топлива из линии слива топливного форсунка за 1 минуту во время работы двигателя. Используйте электронный сервис INSITETM для тестирования на утечку под высоким давлением. Делайте это до шести (6) раз, один раз, пока каждая линия изолирована.

Если выделение одного топливного форсунка и разъема топлива высокого давления приводит к значительному уменьшению утечки по сравнению с остальной частью набора, этот топливный форсунок и топливный разъем должны быть проверены.

> [!note] Примечание
> Убедитесь, что постоянный поток топлива присутствует на линии слива перед началом измерения. Воздух в линии и движение шланга во время измерения могут привести к неточной оценке.

Проверьте подозреваемый топливный разъем. См. процедуру 006-052 в разделе 6. Если топливный разъем не поврежден, замените топливный форсун и топливный разъем.

![[06d00483.png]]

### Тест на возврат потока клапана клапан Return Flow Test

Первоначальная настройка

> [!warning] ОСТОРОЖНО
> Установка адаптера потока банджо в любом месте, кроме рекомендуемых мест, может привести к повреждению компонентов топливной системы высокого давления.

Для измерения утечки клапана сброса давления топлива требуется использование испытательного фитинга для утечки топлива, части 4919058 и шланга для возврата топлива. Инструмент используется для изоляции утечки только из клапана сброса давления топлива, чтобы его можно было измерить в градуированном цилиндре.

> [!note] Примечание
> Если код 449 или 2311 неисправности активен, не заменяйте клапан сброса давления топлива без предварительного определения причины неисправности. См. соответствующее дерево (ы) устранения неполадок.

Удалите болт M16, который соединяет клапан сброса давления топлива с линией слива топлива.

Установите 1/8-дюймовый NPT CompuchekTM в адаптер для монтажа на банджо, номер детали 4919058, и установите собранную установку на сливной клапан сброса давления топлива.

> [!tip] Момент затяжки
> 16.8 Н·м [148 фунт-дюйм]

Используйте быстрое подключение для маршрутизации топлива в градуированный цилиндр.

![[05c00443.png]]

Измерение - двигатель запустится

Запустите двигатель и позвольте двигателю простаивать с топливом, поступающим в устройство сбора.

Начните тест на утечку высокого давления.

Когда топливо начинает выходить из линии слива, направляйте поток слива в градуированный цилиндр.

Утечка должна быть менее 10 капель в минуту.

Смотрите соответствующее дерево симптомов устранения неполадок для направления ремонта.

> [!note] Примечание
> Если код 449 или 2311 неисправности активен, не заменяйте клапан сброса давления топлива без предварительного определения причины неисправности. Используйте соответствующее дерево устранения неисправностей кода неисправности в разделе TF руководства по устранению неисправностей QSZ13 CM2150 Z101, Бюллетень 4358367.

![[19c01817.png]]

Измерение: двигатель не запускается

Начните сворачивать двигатель, пока топливо не выйдет из линии слива.

Когда топливо начинает выходить из линии слива, направляйте поток слива в градуированный цилиндр и продолжайте проворачивать в течение 30 секунд.

> [!note] Примечание
> Не останавливайте двигатель в течение 30 секунд. Проворачивайте двигатель через 15 вторых интервалов с 15-секундной паузой между интервалами. Это снижает возможность перегрева пускового двигателя.

Утечка должна быть **менее **10 капель в минуту.

> [!note] Примечание
> Если код 449 или 2311 неисправности активен, не заменяйте клапан сброса давления топлива без предварительного определения причины неисправности. Используйте соответствующее дерево устранения неисправностей кода неисправности в разделе TF руководства по устранению неисправностей QSZ13 CM2150 Z101, Бюллетень 4358367.

![[11800286.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> **WARNING · Опасно**
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.
>
> **WARNING · Опасно**
> When using a steam cleaner, wear safety glasses or a face shield, as well as protective clothing. Hot steam can cause serious personal injury.
>
> **CAUTION · Осторожно**
> Clean all fittings before disassembly. Dirt or contaminants can damage the fuel system.
>
> Before servicing **any** fuel system components, (such as fuel lines, fuel pump, injectors, etc.) which would expose the fuel system or internal engine components to potential contaminants prior to disassembly, clean the fittings, mounting hardware, and the area around the component to be removed. Dirt or contaminants can be introduced into the fuel system and engine if the surrounding areas are **not** cleaned, resulting in damage to the fuel system and engine. [[99-000-009 — Engine Cleaning|Refer to Procedure 000-009 in Section 0.]]
>
> To prevent engine damage from debris or contamination, cover, cap, or plug any openings as soon as possible when servicing the fuel system. Caps and plugs can be found in Clean Care Kit, Part Number 4919073.
>
> The following procedures are used to diagnose fuel system issues. These checks and measurements are referenced throughout the applicable troubleshooting and fault code trees as needed.
>
> This procedure is not intended to take the place of the troubleshooting tree repair direction.
>
> Refer to the appropriate troubleshooting symptom tree for repair direction.
>
> ### High-Pressure System Leak Down Test
>
> **Note · Примечание**
> This test can **not** be performed if the engine will **not** start.
>
> Connect INSITE ™ electronic service tool.
>
> Operate the engine.
>
> Monitor the fuel rail pressure.
>
> Check the fuel pressure decay.
>
> Shut off the engine and wait for it to completely stop. Turn the keyswitch ON quickly.
>
> Monitor INSITE™ electronic service tool and record the fuel rail pressure for 1 minute.
>
> A change in fuel pressure greater than 100 bar \[1450 psi\] in 1 minute is an indication of a high-pressure fuel system leak.
>
> Refer to the appropriate troubleshooting symptom tree for repair direction.
>
> ### Low-Pressure System Check
>
> The low-pressure system check consists of a number of measurements and checks to make sure that the low pressure fuel system is functioning properly. These checks will vary, depending on whether or not the engine will start.
>
> Measurement - Engine Will Start
>
> Check for air in the fuel. Refer to Procedure 006-003 in Section 6.
>
> Measure the fuel inlet restriction. Refer to Procedure 006-020 in Section 6.
>
> Measure the fuel gear pump output pressure. Use the instructions in the Fuel Pump Gear Pump Pressure Test section of this procedure.
>
> Measure the fuel filter restriction. Use the instructions in the Fuel Filter Restriction section of this procedure.
>
> Measure the fuel drain line restriction. Refer to Procedure 006-012 in Section 6.
>
> Measurement - Engine Will Not Start
>
> Measure the fuel gear pump output pressure while cranking. Use the instructions in the Fuel Pump Gear Pump Pressure Test section of this procedure.
>
> Measure the fuel drain line restriction. Refer to Procedure 006-012 in Section 6.
>
> ### Fuel Pump Gear Pump Pressure Test
>
> Measurement - Engine Will Start
>
> Install a 0 to 2068 kPa \[0 to 300 psi\] pressure gauge at the Compuchek™ fitting at the inlet to the fuel filter head.
>
> Operate the engine at high idle and observe the fuel gear pump pressure.
>
> | Gear Pump Pressure at High Idle |  |  |
> |---|---|---|
> | kpa |  | psi |
> | 1000 | MIN | 145 |
>
> Measurement - Engine Will Not Start
>
> Install a 0 to 207 kPa \[0 to 30 psi\] pressure gauge at the Compuchek™ fitting at the inlet to the fuel filter head.
>
> Crank the engine and observe the fuel gear pump pressure.
>
> | Gear Pump Pressure at Cranking |  |  |
> |---|---|---|
> | kpa |  | psi |
> | 69 | MIN | 10 |
>
> ### Fuel Filter Restriction
>
> Initial Setup
>
> Install a 1/8-inch NPT Compuchek™ into banjo fitting adapter, Part Number 4919057, and install the assembled fitting into the outlet of the pressure side fuel filter.
>
> Connect orificed diagnostic fuel line, Part Number 3164621, to the banjo fitting adapter and route to the engine fuel tank or other suitable container.
>
> The orificed diagnostic fuel line is used in procedures to create rated flow through the low pressure fuel system without the need to operate the engine under load.
>
> Measurement
>
> Install a 0 to 2068 kPa \[0 to 300 psi\] pressure gauge at the Compuchek™ fitting at the inlet to the fuel filter head.
>
> Operate the engine at high idle and observe the filter inlet pressure.
>
> Install a 0 to 2068 kPa \[0 to 300 psi\] pressure gauge at the Compuchek™ fitting at the outlet to the fuel filter head.
>
> Operate the engine at high idle and observe the filter outlet pressure.
>
> | Fuel Filter Restriction |  |  |
> |---|---|---|
> | kpa |  | psi |
> | 138 | MAX | 20 |
>
> If the difference between the filter inlet pressure and filter outlet pressure is greater than the specification, replace the fuel filter.
>
> ### High-Pressure Fuel Pump Return Flow Test
>
> **WARNING · Опасно**
> Depending on the circumstances, diesel fuel is flammable. When inspecting or performing service or repairs on the fuel system, to reduce the possibility of fire and resulting severe personal injury, death or property damage, never smoke or allow sparks or flames (such as pilot lights, electrical switches, or welding equipment) in the work area.
>
> **CAUTION · Осторожно**
> Installation of the banjo flow adapter at any place other than the recommended locations can cause damage to high-pressure fuel system components.
>
> This test uses a flow adapter fitting. The purpose of the flow adapter fitting is to route the drain flow of the fuel pump head **only** into a collection device so that leakage may be measured.
>
> This procedure requires the use of a fuel system leak tester, Part Number 3164618.
>
> Initial Setup
>
> **CAUTION · Осторожно**
> Make sure to hold the banjo fittings while tightening the banjo bolt to prevent fitting rotation. Allowing the banjo fitting to rotate may damage the fuel line.
>
> Remove the M12 banjo bolt connecting the fuel drain connection to the fuel pump head.
>
> Install a banjo flow adapter fitting, Part Number 3164618, at the fuel drain connection and route a hose from this adapter to a bucket or the vehicle's fuel tank. This will isolate the injector and high pressure relief valve drain from the fuel pump drain.
>
> Disconnect the OEM fuel return and clamp a hose over the fuel drain to be routed for measurement.
>
> **CAUTION · Осторожно**
> The High-Pressure Leakage Test in INSITE™ electronic service tool will cause the engine to operate at elevated pressures while the engine idles. The engine noise will change when this test is being performed due to the higher fuel injection pressures. Safety glasses should be worn while working near the running engine. Fuel lines should not be adjusted while performing this test.
>
> Close the engine cover(s) while performing these tests.
>
> Measurement - Engine Will Start
>
> If the engine will start, perform INSITE™ electronic service tool High-Pressure Leakage Test.
>
> Connect INSITE™ electronic service tool.
>
> Start the engine and allow the engine to idle with fuel flowing into a collection device.
>
> Begin the High-Pressure Leakage Test.
>
> Measure the time necessary to collect 450 ml (cc) of fuel pump head drain flow while performing the High-Pressure Leakage Test.
>
> Use a graduated cylinder for this measurement.
>
> This measurement should be taken three times, but **only** the third reading is used.
>
> | Maximum Volume of Fuel During High-Pressure Leakage Test |  |
> |---|---|
> | ml (cc) | Seconds |
> | 450 | 30 |
>
> If 450 ml (cc) pump head drain flow is collected in less than 30 seconds, the fuel pump head has malfunctioned and **must** be replaced.
>
> This specification is valid for engines operating on diesel fuels. Low fuel viscosity will increase the leakage rate; for example, kerosene or aviation fuels will result in excessive leakage. Verify the fuel type before replacing a fuel pump head for excessive leakage.
>
> Measurement - Engine Will Not Start
>
> Begin cranking the engine until fuel exits the drain line.
>
> **Note · Примечание**
> Do **not** crank the engine for 30 seconds continously. Crank the engine in 15 second intervals with a 15 second pause between intervals. This reduces the possibility of overheating the starting motor.
>
> When fuel begins to exit the drain line, route the drain flow to a graduated cylinder and continue cranking for 30 seconds.
>
> This measurement should be taken three times, but **only** the third reading is used.
>
> | Maximum Volume of Fuel During Cranking |  |
> |---|---|
> | ml (cc) | Seconds |
> | 320 | 30 |
>
> If 320 ml (cc) pump head drain flow is collected in less than 30 seconds of cranking, the pump head has malfunctioned and **must** be replaced.
>
> ### High-Pressure Injector Return Flow Test
>
> Initial Setup
>
> **CAUTION · Осторожно**
> Installation of the banjo flow adapter at any place other than the recommended locations can cause damage to high-pressure fuel system components.
>
> **Note · Примечание**
> Make sure the engine is at operating temperature before beginning this test.
>
> Return fuel is transmitted from the injectors and fuel rail high-pressure relief valve through a common return line. The common return line connects to a fuel drain connection that also receives fuel drain from the fuel pump head.
>
> Measurement of fuel injector leakage requires use of a fuel return hose and a special fuel fitting, Part Numbers 4919058 and 3164618.
>
> The tools are used in combination to isolate the leakage from the injectors, so it can be measured into a graduated cylinder.
>
> **WARNING · Опасно**
> Depending on the circumstance, diesel fuel is flammable. When inspecting or performing service or repairs on the fuel system, to reduce the possibility of fire and resulting severe personal injury, death, or property damage, never smoke or allow sparks or flames (such as pilot lights, electrical switches, or welding equipment) in the work area.
>
> Remove the banjo bolt that connects the common drain line to the high-pressure relief valve.
>
> Install a 1/8-inch NPT Compuchek™ into banjo fitting adapter, Part Number 4919058, and install the assembled fitting at the fuel pressure relief valve drain connection. Use a quick-connect to route the fuel into a collection device or back to the vehicle fuel tank.
>
> Remove the banjo bolt that connects the common drain line to the fuel drain connection at the fuel pump.Install the fuel return hose, Part Number 3164618, at the fuel drain connection at the fuel pump.
>
> Route the return fuel into a collection device that is marked in cubic centimeters.
>
> **Note · Примечание**
> Graduated cylinder, Part Number 4919139, or a similar measuring device may be used.
>
> Measurement - Engine Will Start
>
> If the engine will start, perform INSITE™ electronic service tool High-Pressure Leak Test.
>
> Connect INSITE™ electronic service tool.
>
> Start the engine and allow the engine to idle with fuel flowing into a collection device.
>
> Begin the High-Pressure Leakage Test.
>
> | Leagage Specification with Engine Running |  |
> |---|---|
> | Maximum Leakage in 1 Minute | 70 ml (cc) |
>
> **Note · Примечание**
> Fuel temperature and fuel type will influence this measurement. For example; as the engine is warmed up and the injectors become hot, the leakage rate will increase. Also, low viscosity fuels, such as kerosene will cause the leakage rate to increase. The above specification is correct for on-highway diesel fuels where fuel inlet temperature is less than 49°C \[120°F\].
>
> After recording the fuel leakage quantity, stop INSITE™ electronic service tool High-Pressure Leak Test and turn the keyswitch to OFF.
>
> **Note · Примечание**
> Make sure a steady flow of fuel is present at the drain line before beginning the measurement. Air in the line and movement of the hose during measurement can result in inaccurate measurements.
>
> If injector drain flow is excessive, it will be necessary to isolate the damaged or worn injector(s) or fuel connector(s).
>
> A loose fuel connector retaining nut results in a poor seal at the interface between the fuel connector and the injector. The loose condition will result in a leak of high-pressure fuel to the injector drain.
>
> Verify first that the fuel connectors are properly tightened. Refer to Procedure 006-052 in Section 6.
>
> If loose retaining nut(s) are found, test for leakage after tightening the retaining nut(s).
>
> Measurement - Engine Will Not Start
>
> Crank the engine until fuel exits the drain line.
>
> **Note · Примечание**
> Do **not** crank the engine for 30 seconds continously. Crank the engine in 15 second intervals with a 15 second pause between intervals. This reduces the possibility of overheating the starting motor.
>
> When fuel begins to exit the drain line, route the drain flow to a graduated cylinder and continue cranking for 30 seconds.
>
> The leakage should **only** be a few drops. Any more than a few drops indicates either an injector or a high-pressure connector failure.
>
> **Note · Примечание**
> Vent the pressure from the fuel system as directed after each cranking event.
>
> ### High-Pressure Injector Return Flow Isolation Test
>
> **WARNING · Опасно**
> Normal engine operation creates highly pressurized fuel in the fuel line which will remain in the fuel line after engine shutdown. Never open the fuel system when the engine is operating. Before servicing the fuel system, always loosen the pump-to-rail fuel line at the rail to vent the pressure. Keep hands clear of the line when loosening. High-pressure fuel spray can penetrate the skin, resulting in serious personal injury or death.
>
> Before servicing the high-pressure fuel system, loosen the pump-to-rail line at the rail to vent the pressure.
>
> Keep hands clear of the line when loosening.
>
> Tighten the fuel rail nut.
>
> Torque Value:
>
> **Note · Примечание**
> A machined slot in this fitting directs the fuel spray towards the engine.
>
> **CAUTION · Осторожно**
> Do not install the isolation tool at the high-pressure pump outlet fitting. Severe engine damage will result. This tool must only be installed at the fuel rail for the purpose of isolating the high-pressure fuel supply from individual injectors.
>
> **CAUTION · Осторожно**
> Make certain the keyswitch is in the OFF position (engine not running) when loosening or tightening high-pressure fuel lines.
>
> Use leak test isolation tool, Part Number 4918563, to isolate excessive fuel drain from injectors or fuel connectors.
>
> Follow the pressure relief step (shown in the previous step) prior to every installation of the isolation tool.
>
> Isolate the injector and fuel connector for each cylinder by installing the isolation tool at the fuel rail in place of the high-pressure fuel line that supplies the fuel connector.
>
> Torque Value:
>
> Record the amount of fuel flow from the injector drain line in 1 minute while the engine is running. Use INSITE™ electronic service tool High Pressure Leak Test. Do this up to six (6) times, once while each line is isolated.
>
> If isolating a single injector and high-pressure fuel connector causes the leakage to decrease significantly compared to the rest of the set, that injector and fuel connector **must** be inspected.
>
> **Note · Примечание**
> Make sure a steady flow of fuel is present at the drain line before beginning the measurement. Air in the line and movement of the hose during measurement can result in inaccurate measurements.
>
> Inspect the suspect fuel connector. Refer to Procedure 006-052 in Section 6. If the fuel connector is **not** damaged, replace both the injector and the fuel connector.
>
> ### Fuel Pressure Relief Valve Return Flow Test
>
> Initial Setup
>
> **CAUTION · Осторожно**
> Installation of the banjo flow adapter at any place other than the recommended locations can cause damage to high-pressure fuel system components.
>
> Measurement of fuel pressure relief valve leakage requires use of a fuel leak test fitting, Part Number 4919058, and a fuel return hose. The tool is used to isolate the leakage from just the fuel pressure relief valve so that it can be measured in a graduated cylinder.
>
> **Note · Примечание**
> If Fault Code 449 or 2311 is active, do **not** replace the fuel pressure relief valve without first determining the cause of the fault condition. See the appropriate troubleshooting tree(s).
>
> Remove the M16 banjo bolt that connects the fuel pressure relief valve to the fuel drain line.
>
> Install a 1/8-inch NPT Compuchek™ into banjo fitting adapter, Part Number 4919058, and install the assembled fitting at the fuel pressure relief valve drain connection.
>
> **Момент затяжки · Torque Value**
> 16.8 n•m [148 in-lb]
>
> Use a quick-connect to route the fuel into a graduated cylinder.
>
> Measurement - Engine Will Start
>
> Start the engine and allow the engine to idle with fuel flowing into a collection device.
>
> Begin the High-Pressure Leakage Test.
>
> When fuel begins to exit the drain line, route the drain flow into a graduated cylinder.
>
> The leakage **must** be less than 10 drops per minute.
>
> Refer to the appropriate troubleshooting symptom tree for repair directions.
>
> **Note · Примечание**
> If Fault Code 449 or 2311 is active, do **not** replace the fuel pressure relief valve without first determining the cause of the fault condition. Use the appropriate fault code troubleshooting tree in Section TF of the QSZ13 CM2150 Z101 Fault Code Troubleshooting Manual, Bulletin 4358367.
>
> Measurement - Engine Will Not Start
>
> Begin cranking the engine until fuel exits the drain line.
>
> When fuel begins to exit the drain line, route the drain flow to a graduated cylinder and continue cranking for 30 seconds.
>
> **Note · Примечание**
> Do **not** crank the engine for 30 seconds continously. Crank the engine in 15 second intervals with a 15 second pause between intervals. This reduces the possibility of overheating the starting motor.
>
> The leakage should be **less than** 10 drops per minute.
>
> **Note · Примечание**
> If Fault Code 449 or 2311 is active, do **not** replace the fuel pressure relief valve without first determining the cause of the fault condition. Use the appropriate fault code troubleshooting tree in Section TF of the QSZ13 CM2150 Z101 Fault Code Troubleshooting Manual, Bulletin 4358367.
