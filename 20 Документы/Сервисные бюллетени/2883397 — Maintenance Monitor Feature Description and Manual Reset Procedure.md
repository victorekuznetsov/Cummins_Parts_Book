---
type: "Сервисный бюллетень"
doc: "2883397"
title_en: "Maintenance Monitor Feature Description and Manual Reset Procedure"
released: "2009-10-18"
modified: "2023-03-13"
engines:
  - "77804810"
  - "80141463"
  - "80248213"
families:
  - "15N"
  - "QSX15"
figures: 12
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/2883397.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/bulletin/2883397.pdf"
tags:
  - "документ/бюллетень"
  - "двигатель/15N"
  - "двигатель/QSX15"
  - "перевод/машинный"
---

# Maintenance Monitor Feature Description and Manual Reset Procedure

> [!abstract] Сервисный бюллетень · `2883397`
> **Двигатели:** [[77804810 — 15N CM2380 M104B CPL 5977|77804810]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** 15N, QSX15
> **Даты:** выпущен 2009-10-18 · изменён 2023-03-13
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/2883397.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/bulletin/2883397.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Описание функции мониторинга технического обслуживания и ручная процедура сброса

**Описание характеристик**

Эта функция, когда включена, заставит электронный модуль управления (ECM) мигать лампой в течение 30 секунд, когда переключатель зажигания включен, предупреждая оператора, когда пришло время обслуживать двигатель. Эта функция может быть отрегулирована на основе измерения расстояния ECM или времени работы двигателя. После того, как ECM определит, что интервал обслуживания истек, он будет мигать либо на лампу MAINTENANCE, либо на лампу CHECK ENGINE (см. спецификации OEM для соответствующей лампы, которая будет освещена) в течение 30 секунд, когда переключатель зажигания включен.

Кроме того, эта функция может быть настроена (используй электронный сервисный инструмент Cummins® INSITETM) для освещения лампы в некоторое время до окончания интервала технического обслуживания (пример: Эта функция может быть отрегулирована для освещения лампы в любой момент, когда истекает от 50 до 100 процентов интервала технического обслуживания. Это достигается путем выбора соответствующего значения для процента тревоги.

Наконец, некоторые приложения (в частности, ISM и ISX) могут иметь ECM, определяющий интервал обслуживания с использованием автоматического режима монитора технического обслуживания. В этих случаях пользователь **должен** ввести интервальный фактор (используй инструмент электронного сервиса Cummins® INSITETM). Интервальный фактор будет основан на рабочем цикле автомобиля и классе моторного масла. Затем ECM рассчитает конец интервала технического обслуживания, исходя из условий работы двигателя.

**Регулируемые параметры**

Имя: Монитор технического обслуживания

Диапазон: Включаемый/отключаемый

Наименование: Позволяет пользователю включить функцию мониторинга технического обслуживания.

Имя: Режим

Диапазон: Авто, расстояние, время (или руководство)

Наименование: Выбор режима «Авто», «Расстояние», «Время» (или «Ручное») определит, как ECM реализует функцию мониторинга технического обслуживания.

Авто - Если доступен Авто режим монитора технического обслуживания, необходимо ввести интервальный коэффициент (см. Интервал-фактор в этом бюллетене службы), и интервал технического обслуживания будет основан на определении срока службы масла ECM.

Расстояние - Если выбран режим расстояния, необходимо ввести расстояние, и интервал обслуживания будет основан на измеренном расстоянии ECM. Необходимо, чтобы транспортное средство имело рабочий датчик скорости транспортного средства для правильной работы этого режима мониторинга технического обслуживания.

Время (или Руководство) - Если выбран режим времени, необходимо ввести время, и интервал обслуживания будет основан на измеренном времени работы двигателя ECM.

В некоторых промышленных приложениях режим времени помечается как ручной режим на электронном сервисном инструменте Cummins® INSITETM.

Имя: расстояние

Диапазон: Варианты для разных двигателей (KM/Mi)

Наименование: При работе в режиме дистанционного управления введенное расстояние определяет интервал обслуживания. См. соответствующее Руководство по эксплуатации и техническому обслуживанию для конкретного применения двигателя для правильного интервала слива масла.

Имя: Время

Диапазон: Разные варианты двигателей (часы)

Наименование: При работе в режиме времени (также называемом ручным режимом в некоторых промышленных двигателях) введенное время определяет интервал обслуживания. См. соответствующее Руководство по эксплуатации и техническому обслуживанию для конкретного применения двигателя для правильного интервала слива масла.

Имя: Процентное значение тревоги

Диапазон: 50 % до 100 %

Наименование: Это значение должно быть введено. ECM использует коэффициент оповещения, чтобы определить, когда следует зажечь соответствующую лампу. Например: Если вводится 90%-ный процент оповещения, то ЭКМ будет освещать соответствующую лампу на расстоянии, соответствующем 90% от общего интервала технического обслуживания.

Имя: Предупреждать во время бега

Диапазон: Включить или отключить

Наименование: Некоторые двигатели будут иметь эту функцию монитора технического обслуживания. Когда включено предупреждение во время бега, соответствующая лампа будет освещаться, как только будет достигнут пробег или временной порог. В противном случае подходящая лампа будет **только **освещаться на клавише Включено. Этот компонент функции монитора технического обслуживания полезен в некоторых промышленных приложениях, где двигатели не выключаются ежедневно.

Имя: Интервальный фактор

Диапазон: Варианты для различных двигателей (номер без единицы, который используется ECM для расчета рабочего цикла и класса масла транспортного средства).

Наименование: Это значение используется при работе в режиме Auto. Некоторые двигатели имеют калибровки, которые будут основывать интервал технического обслуживания на рабочем цикле и условиях эксплуатации двигателя. В этом режиме двигатель позволит максимально продлить срок службы масла, если двигатель слегка загружен, и в то же время предупредить оператора об изменении масла раньше, если будет обнаружен более тяжелый рабочий цикл.

Имя: сброс

Диапазон: сброс

Наименование: Сброс интервальных данных монитора технического обслуживания. Смотрите следующие таблицы в этом бюллетене службы, чтобы правильно выбрать интервал для различных типов двигателей. Если тип двигателя **не**, конкретно перечисленный ниже, рекомендуется запускать монитор технического обслуживания в режиме «Расстояние» или «Время» **только**.

**ISX и SignatureTM Двигатели**

Во-первых, используйте таблицу 1 для выбора рабочего цикла. Оцените рабочий цикл автомобиля на основе всех трех эксплуатационных критериев. Правильный рабочий цикл транспортного средства является наихудшим рабочим циклом, основанным на трех эксплуатационных критериях (Пример: Самосвал, который в среднем составляет 6,5 МПГ и ГВВ, составляет 30844 кг [68 000 фунтов], будет рассматриваться как цикл тяжелой службы, если транспортное средство эксплуатируется в пыльных условиях.

| Таблица 1 |  |  |  |
|---|---|---|---|
| Оперативные критерии | Тяжелая обязанность | Обычный долг | Светлый Двигатель |
| Среднее потребление топлива | Менее 5,5 Мпг | 5.5-6.5 MPG | Выше 6.5 MPG |
| Валовой вес автомобиля (GVW) | Выше 36 287 кг [80 000 фунтов] | 31 752 до 36 287 кг [70 000 до 80 000 фунтов] | Ниже 31 752 кг[70 000 фунтов] |
| Работает ли автомобиль в грязных условиях? | Да | Нет | Нет |

Выберите правильный интервальный коэффициент на основе таблицы 2.

Правильный интервальный коэффициент как по циклу работы, так и по классу используемого клиентом масла, если класс используемого клиентом масла изменяется, интервальный коэффициент должен быть оценен повторно.

| Таблица 2 |  |  |  |
|---|---|---|---|
| Класс масла | Тяжелая обязанность | Обычный долг | Светлый Двигатель |
| Стандартный CG-4 | Интервальный фактор 1.0 | Интервальный фактор 1.5 | Интервальный фактор 2.0 |
| CES 20071 (CH-4) | Интервальный фактор 1.25 | Интервальный фактор 2.71 | Интервальный фактор 3.43 |
| CES 20076 | Интервальный фактор 1.5 | Интервальный фактор 3.07 | Интервальный фактор 3.79 |

**Двигатели ИСМ**

Во-первых, используйте таблицу 3 для выбора рабочего цикла. Оцените рабочий цикл автомобиля на основе всех трех эксплуатационных критериев. Правильный рабочий цикл для транспортного средства является более сложным, основанным на трех эксплуатационных критериях (Пример: Самосвал, который в среднем составляет 7,0 МПГ и ГВВ, составляет 30844 кг [68 000 фунтов], будет рассматриваться как цикл тяжелой службы, если транспортное средство эксплуатируется в пыльных условиях.

| Таблица 3 |  |  |  |
|---|---|---|---|
| Оперативные критерии | Тяжелая обязанность | Обычный долг | Светлый Двигатель |
| Среднее потребление топлива | Менее 6,0 МПГ | 6.0 до 7.0 MPG | Выше 7,0 MPG |
| Валовой вес автомобиля (GVW) | Выше 36 287 кг [80 000 фунтов] | 31 752 до 36 287 кг [70 000 до 80 000 фунтов] | Ниже 31 752 кг[70 000 фунтов] |
| Работает ли автомобиль в грязных условиях? | Да | Нет | Нет |

Выберите правильный интервальный коэффициент на основе таблицы 4.

Правильный интервальный коэффициент как по циклу работы, так и по классу используемого клиентом масла, если класс используемого клиентом масла изменяется, интервальный коэффициент должен быть оценен повторно.

Транспортное средство накапливает 13 000 км \[8000 миль \] (или более) в месяц, а двигатель имеет турбокомпрессор с турбинным обходным клапаном.

| Таблица 4 |  |  |  |
|---|---|---|---|
| Класс масла | Тяжелая обязанность | Обычный долг | Светлый Двигатель |
| Стандартный CG-4 | Интервалный фактор 0,67 | Интервальный фактор 1.33 | Интервальный фактор 1.67 |
| CES 20071 (CH-4) | Интервальный фактор 1.00 | Интервальный фактор 2.00 | Интервальный фактор 2.67 |
| CES 20076 | Интервальный фактор 1.33 | Интервальный фактор 2.33 | Интервальный фактор 3.00 |

Транспортное средство накапливает 13 000 км \[8000 миль \] (или более) в месяц, а двигатель имеет турбокомпрессор с турбинным обходным клапаном.

| Таблица 5 |  |  |  |
|---|---|---|---|
| Класс масла | Тяжелая обязанность | Обычный долг | Светлый Двигатель |
| Стандартный CG-4 | Интервал 0,33 | Интервальный фактор 0,53 | Интервалный фактор 0,80 |
| CES 20071 (CH-4) | Интервалный фактор 0,67 | Интервальный фактор 1.00 | Интервальный фактор 1.67 |
| CES 20076 | Интервал 0,83 | Интервальный фактор 1.33 | Интервальный фактор 2.00 |

Автомобиль накапливает менее 13 000 км \[8000 миль] в месяц.

| Таблица 6 |  |  |  |
|---|---|---|---|
| Класс масла | турбинный обходной клапан Turbocharger | Нетурбинный обходной клапан Турбокомпрессор | Не применяется |
| Стандартный CG-4 | Интервальный фактор 0,17 | Интервалный фактор 0.30 | Не применяется |
| CES 20071 (CH-4) | Интервалный фактор 0.30 | Интервальный фактор 0,47 | Не применяется |
| CES 20076 | Интервальный фактор 0,40 | Интервалный фактор 0,60 | Не применяется |

Автомобиль является рекреационным транспортным средством или пожарным автомобилем.

| Таблица 7 |  |  |
|---|---|---|
| Класс масла | 450 лошадиных сил | 500 лошадиных сил |
| Стандартный CG-4 | Интервальный фактор 0,40 | Интервалный фактор 0,20 |
| CES 20071 (CH-4) | Интервалный фактор 0,60 | Интервалный фактор 0.30 |
| CES 20076 | Интервалный фактор 0,80 | Интервальный фактор 0,40 |

**Активация/деактивация водителя**

Используйте инструмент электронного обслуживания INSITETM для включения этой функции.

только драйвер или взаимодействие пользователя должны сбросить соответствующую лампу вручную. В противном случае, электронный сервисный инструмент Cummins® INSITETM может быть использован для сброса соответствующей лампы.

Сброс Монитора технического обслуживания на двигателях без последующей обработки может быть выполнен путем нажатия кнопки сброса на экране Монитора технического обслуживания, с использованием инструментария электронного обслуживания INSITETM или с помощью одной из следующих процедур.

> [!danger] ОПАСНО
> Установите рабочий тормоз с помощью ручного клапана прицепа. Убедитесь, что давление воздуха достаточно, чтобы активировать переключатель давления тормоза. Безопасно забивайте колеса. Движение грузовика во время устранения неполадок может привести к серьезному повреждению оборудования, травмам или смерти.

> [!note] Примечание
> Включите переключатель зажигания в положение Включения (но сделайте **НЕ** запуск двигателя).

1. Переведите замок зажигания в положение ON.

![[19c01704.png]]

2. Отпустите педаль рабочего тормоза.

![[19c01705.png]]

3. Удавите педаль дроссельной заслонки и удерживайте на 100% дроссельной заслонки.

![[19c01706.png]]

4. Нажмите и отпустите педаль рабочего тормоза 3 раза.

![[19c01707.png]]

5. Отпустите педаль дросселя.

![[19c01708.png]]

6. Нажмите и отпустите педаль рабочего тормоза 1 раз.

![[19c01709.png]]

7. Нажмите и удерживайте педаль дроссельной заслонки на 100 процентов снова.

![[19c01706.png]]

8. Нажмите и отпустите педаль рабочего тормоза еще 3 раза.

![[19c01707.png]]

9. Отпустите педаль дросселя.

![[19c01708.png]]

10. Нажмите и отпустите педаль рабочего тормоза 1 раз.

![[19c01709.png]]

11. Подходящая лампа будет мигать 3 раза.

![[19c01773.png]]

12. Переведите замок зажигания в положение OFF.

![[19c01711.png]]

**Процедура подачи заявок без педалей-дроссельной заслонки**

1. Включите переключатель зажигания в положение Включения (но сделайте **НЕ** запуск двигателя).
2. Поверните диагностический переключатель в положение Включения в течение не менее 3 секунд, а затем поверните его в положение Выключения.
3. Поверните диагностический переключатель в положение Включения (менее 3 секунд), а затем в положение Выключения дважды, с менее чем 3 секундами между каждым переключением.
4. Поверните диагностический переключатель в положение Включения в течение не менее 3 секунд, а затем поверните его в положение Выключения.

Процедура **должна быть завершена в течение 20 секунд, или данные будут **не сброшены.

Соответствующая лампа будет мигать 3 раза, чтобы указать, что сброс завершен.

**Взаимодействие с другими функциями и параметрами**

Не все двигатели (пример: CELECTTM) оснащены отдельной лампой MAINTENANCE. В этих случаях двигатель может использовать другой метод (пример: Двигатели CELECTTM предупреждают оператора, мигая лампой ENGINE PROTECTION через 5, 3-флеш циклов примерно через 12 секунд после включения клавиши. Посмотрите соответствующее Руководство по эксплуатации и техническому обслуживанию, чтобы увидеть, как оператор оповещен, когда эта функция включена.

Монитор технического обслуживания будет включен, если CentinelTM установлен на транспортном средстве.

**Специальные инструкции**

Включите режим автоматического мониторинга технического обслуживания, не ссылаясь сначала на конкретное руководство по эксплуатации и техническому обслуживанию двигателя и правильно оценивая рабочий цикл транспортного средства. Необходимо, чтобы правильный интервальный фактор был выбран при использовании режима авто.

**Недостатки**

Приложения, которые не используют отдельную лампу MAINTENANCE, могут освещать лампы предупреждения двигателя, что может привести к ложным жалобам на обслуживание, если водители не обучены использовать функцию мониторинга технического обслуживания.

**Визуальная помощь**

Нет.

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## Maintenance Monitor Feature Description and Manual Reset Procedure
>
> **Feature Description**
>
> This feature, when enabled will cause the electronic control module (ECM) to flash a lamp for 30 seconds when the keyswitch is turned ON, alerting the operator when it is time to service the engine. This feature can be adjusted, based on ECM measured distance or engine running time. Once the ECM determines the maintenance interval has expired, it will flash either the MAINTENANCE or the amber CHECK ENGINE lamp (refer to the OEM specifications for appropriate lamp that will be illuminated) for 30 seconds when the keyswitch is turned ON.
>
> Furthermore, the feature can be customized (use Cummins® INSITE™ electronic service tool) to illuminate the lamp at sometime prior to the end of the maintenance interval (Example: The feature can be adjusted to illuminate the lamp at any point when 50 to 100 percent of the maintenance interval has expired. This is accomplished by selecting an appropriate value for Alert Percentage.)
>
> Finally, some applications (specifically ISM and ISX) can have the ECM determine the maintenance interval using the Auto mode of the Maintenance Monitor. If these instances, the user **must** enter an Interval Factor (use Cummins® INSITE™ electronic service tool). The Interval Factor will be based on the vehicle's duty cycle and engine oil grade. The ECM will then calculate the end of the maintenance interval, based on engine operating conditions.
>
> **Adjustable Parameters**
>
> Name: Maintenance Monitor
>
> Range: Enable/Disable
>
> Description: Allows the user to enable the Maintenance Monitor feature.
>
> Name: Mode
>
> Range: Auto, Distance, Time (or Manual)
>
> Description: Choosing Auto, Distance, Time (or Manual) mode will determine how the ECM enacts the Maintenance Monitor Feature.
>
> Auto - If the Auto mode of Maintenance Monitor is available, it is necessary that an interval factor be entered (see Interval Factor in this Service Bulletin), and the maintenance interval will be based on an ECM determination of oil life.
>
> Distance - If the Distance mode is chosen, it is necessary that a distance be entered, and the maintenance interval will be based on ECM measured distance traveled. It is necessary that the vehicle have a working vehicle speed sensor for this mode of Maintenance Monitor to work properly.
>
> Time (or Manual) - If the Time mode is chosen, it is necessary that a time be entered, and the maintenance interval will be based on ECM measured engine run time.
>
> In some industrial applications, the Time mode is labeled Manual mode on Cummins® INSITE™ electronic service tool.
>
> Name: Distance
>
> Range: Varies for different engines (KM/Mi)
>
> Description: When operating in the Distance mode, the distance entered defines the maintenance interval. See the appropriate Operation and Maintenance Manual for a specific engine application for the correct oil drain interval.
>
> Name: Time
>
> Range: Varies for different engines (Hours)
>
> Description: When operating in the Time mode (also called Manual mode in some industrial engines), the time entered defines the maintenance interval. See the appropriate Operation and Maintenance Manual for a specific engine application for the correct oil drain interval.
>
> Name: Alert Percentage
>
> Range: 50 percent to 100 percent
>
> Description: This value **must** be entered. The ECM uses the Alert Percentage to determine when to illuminate the appropriate lamp. For example: If the Alert Percentage is entered as 90 percent, the ECM will illuminate the appropriate lamp at a time or distance corresponding to 90 percent of the total maintenance interval.
>
> Name: Warn While Running
>
> Range: Enable or Disable
>
> Description: Some engines will have this component of the Maintenance Monitor feature available. When Warning While Running is enabled, the appropriate lamp will illuminate as soon as the mileage or time threshold is reached. Otherwise, the appropriate lamp will **only** illuminate at key ON. This component of the Maintenance Monitor feature is useful in some industrial applications where the engines are **not** turned off on a daily basis.
>
> Name: Interval Factor
>
> Range: Varies for different engines (a unit-less number that is used by the ECM to calculate the vehicle's duty cycle and oil grade).
>
> Description: This value is used when operating in the Auto mode. Some engines have calibrations that will base the maintenance interval on duty-cycle and engine operating conditions. In this mode, the engine will allow the maximum oil life if the engine is lightly loaded, and at the same time alert the operator to change the oil sooner if a more severe duty cycle is detected.
>
> Name: Reset
>
> Range: Reset
>
> Description: Resets the Maintenance Monitor interval data. See the following tables in this Service Bulletin to properly select an Interval Factor for various engine types. If the engine type is **not** specifically listed below, it is recommended that Maintenance Monitor be run in either the Distance or Time mode **only**.
>
> **ISX and Signature™ Engines**
>
> First, use Table 1 to select a duty cycle. Evaluate the vehicle's duty cycle based on all three Operational Criteria. The correct duty cycle for the vehicle is the worst case duty cycle based on the three Operational Criteria (Example: A dump truck that averages 6.5 MPG and GVW is 30844 kg \[68,000 lbs\] will be considered as a Severe Duty cycle if the vehicle is operated in dusty environments).
>
> | Table 1 |  |  |  |
> |---|---|---|---|
> | Operational Criteria | Severe Duty | Normal Duty | Light Duty |
> | Average Fuel Consumption | Less than 5.5 MPG | 5.5 to 6.5 MPG | Above 6.5 MPG |
> | Gross Vehicle Weight (GVW) | Above 36,287 kg \[80,000 lbs\] | 31,752 to 36,287 kg \[70,000 to 80,000 lbs\] | Below 31,752 kg \[70,000 lbs\] |
> | Does the Vehicle Operate in Dusty Environments? | YES | NO | NO |
>
> Pick the correct interval factor based on Table 2.
>
> The correct interval factor on both the duty cycle and the grade of oil used by the customer, if the grade of oil used by the customer changes, the interval factor **must** be evaluated again.
>
> | Table 2 |  |  |  |
> |---|---|---|---|
> | Oil Grade | Severe Duty | Normal Duty | Light Duty |
> | Standard CG-4 | Interval Factor 1.0 | Interval Factor 1.5 | Interval Factor 2.0 |
> | CES 20071 (CH-4) | Interval Factor 1.25 | Interval Factor 2.71 | Interval Factor 3.43 |
> | CES 20076 | Interval Factor 1.5 | Interval Factor 3.07 | Interval Factor 3.79 |
>
> **ISM Engines**
>
> First, use Table 3 to select a duty cycle. Evaluate the vehicle's duty cycle based on all three Operational Criteria. The correct duty cycle for the vehicle is the worse case duty cycle based on the three Operational Criteria (Example: A dump truck that averages 7.0 MPG and GVW is 30844 kg \[68,000 lbs\] will be considered as a Severe Duty cycle if the vehicle is operated in dusty environments).
>
> | Table 3 |  |  |  |
> |---|---|---|---|
> | Operational Criteria | Severe Duty | Normal Duty | Light Duty |
> | Average Fuel Consumption | Less than 6.0 MPG | 6.0 to 7.0 MPG | Above 7.0 MPG |
> | Gross Vehicle Weight (GVW) | Above 36,287 kg \[80,000 lbs\] | 31,752 to 36,287 kg \[70,000 to 80,000 lbs\] | Below 31,752 kg \[70,000 lbs\] |
> | Does the Vehicle Operate in Dusty Environments? | YES | NO | NO |
>
> Pick the correct interval factor based on Table 4.
>
> The correct interval factor on both the duty cycle and the grade of oil used by the customer, if the grade of oil used by the customer changes, the interval factor **must** be evaluated again.
>
> Vehicle accumulates 13,000 km \[8000 mi\] (or more) per month and engine has a wastegate turbocharger.
>
> | Table 4 |  |  |  |
> |---|---|---|---|
> | Oil Grade | Severe Duty | Normal Duty | Light Duty |
> | Standard CG-4 | Interval Factor 0.67 | Interval Factor 1.33 | Interval Factor 1.67 |
> | CES 20071 (CH-4) | Interval Factor 1.00 | Interval Factor 2.00 | Interval Factor 2.67 |
> | CES 20076 | Interval Factor 1.33 | Interval Factor 2.33 | Interval Factor 3.00 |
>
> Vehicle accumulates 13,000 km \[8000 mi\] (or more) per month and engine has a wastegate turbocharger.
>
> | Table 5 |  |  |  |
> |---|---|---|---|
> | Oil Grade | Severe Duty | Normal Duty | Light Duty |
> | Standard CG-4 | Interval Factor 0.33 | Interval Factor 0.53 | Interval Factor 0.80 |
> | CES 20071 (CH-4) | Interval Factor 0.67 | Interval Factor 1.00 | Interval Factor 1.67 |
> | CES 20076 | Interval Factor 0.83 | Interval Factor 1.33 | Interval Factor 2.00 |
>
> Vehicle accumulates less than 13,000 km \[8000 mi\] per month.
>
> | Table 6 |  |  |  |
> |---|---|---|---|
> | Oil Grade | Wastegate Turbocharger | Non-Wastegate Turbocharger | N/A |
> | Standard CG-4 | Interval Factor 0.17 | Interval Factor 0.30 | N/A |
> | CES 20071 (CH-4) | Interval Factor 0.30 | Interval Factor 0.47 | N/A |
> | CES 20076 | Interval Factor 0.40 | Interval Factor 0.60 | N/A |
>
> Vehicle is a recreational vehicle or fire truck.
>
> | Table 7 |  |  |
> |---|---|---|
> | Oil Grade | 450 Horsepower | 500 Horsepower |
> | Standard CG-4 | Interval Factor 0.40 | Interval Factor 0.20 |
> | CES 20071 (CH-4) | Interval Factor 0.60 | Interval Factor 0.30 |
> | CES 20076 | Interval Factor 0.80 | Interval Factor 0.40 |
>
> **Driver Activation/Deactivation**
>
> Use INSITE™ electronic service tool to enable this feature.
>
> The **only** driver or user interaction is to reset the appropriate lamp manually. Otherwise, Cummins® INSITE™ electronic service tool can be used to reset the appropriate lamp.
>
> The Maintenance Monitor reset, on engines without aftertreatment, can be accomplished by clicking the reset button on the Maintenance Monitor screen, using INSITE™ electronic service tool, or by using one of the following procedures.
>
> **WARNING · Опасно**
> Set the service brake using the trailer brake hand valve. Make sure there is enough air pressure to activate the brake pressure switch. Securely chock the wheels. Truck movement during troubleshooting can cause severe equipment damage, personal injury, or death.
>
> **Note · Примечание**
> Turn the keyswitch to the ON position (but do **NOT** start the engine).
>
> 1. Turn the keyswitch to the ON position.
>
> 2. Release the service brake pedal.
>
> 3. Depress the throttle pedal and hold at 100 percent throttle.
>
> 4. Press and release the service brake pedal 3 times.
>
> 5. Release the throttle pedal.
>
> 6. Press and release the service brake pedal 1 time.
>
> 7. Depress and hold the throttle pedal at 100 percent throttle again.
>
> 8. Press and release the service brake pedal 3 more times.
>
> 9. Release the throttle pedal.
>
> 10. Press and release the service brake pedal 1 time.
>
> 11. The appropriate lamp will flash 3 times.
>
> 12. Turn the keyswitch to the OFF position.
>
> **Procedure for Applications without a Throttle Pedal**
>
> 1. Turn the keyswitch to the ON position (but do **NOT** start the engine).
> 2. Turn the diagnostic switch to the ON position for at least 3 seconds and then turn it to the OFF position.
> 3. Turn the diagnostic switch to the ON position (for less than 3 seconds) and then to the OFF position, twice, with less than 3 seconds between each switching.
> 4. Turn the diagnostic switch to the ON position for at least 3 seconds and then turn it to the OFF position.
>
> The procedure **must** be completed within 20 seconds or data will **not** reset.
>
> The appropriate lamp will flash 3 times to indicate that the reset has been completed.
>
> **Interaction with other Features and Parameters**
>
> Not all engines (Example: CELECT™) are equipped with a separate MAINTENANCE lamp. In these cases, the engine can utilize another method (Example: CELECT™ engines alert the operator by flashing the ENGINE PROTECTION lamp through 5, 3-flash cycles approximately 12 seconds after key ON). See the appropriate Operation and Maintenance Manual to see how the operator is alerted when this feature is enabled.
>
> Maintenance Monitor will **not** be enabled if Centinel™ is installed on the vehicle.
>
> **Special Instructions**
>
> Do **not** enable the Auto mode of Maintenance Monitor without referring first to a specific engine application Operation and Maintenance Manual and correctly evaluating the vehicle's duty cycle. It is necessary that the correct Interval Factor be chosen if using the Auto Mode.
>
> **Disadvantages**
>
> Applications that do **not** utilize a separate MAINTENANCE lamp can illuminate engine WARNING lamps, which can result in false service complaints if drivers are **not** trained to use the Maintenance Monitor feature.
>
> **Visual Aids**
>
> None.
>
> ### Document History
