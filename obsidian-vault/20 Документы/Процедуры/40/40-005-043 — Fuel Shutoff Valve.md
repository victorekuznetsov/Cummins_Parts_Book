---
aliases:
  - "Клапан отсечки топлива"
type: "Процедура"
doc: "40-005-043"
title_en: "Fuel Shutoff Valve"
title_ru: "Клапан отсечки топлива"
modified: "2005-01-14"
engines:
  - "93047320"
families:
  - "6B5.9"
manuals:
  - "4021538"
figures: 42
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-005-043.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-005-043.pdf"
tags:
  - "документ/процедура"
  - "двигатель/6B5.9"
  - "группа/40"
  - "перевод/машинный"
---

# Fuel Shutoff Valve
**Клапан отсечки топлива**

> [!abstract] Процедура · `40-005-043`
> **Двигатели:** [[93047320 — 6B5.9 CPL 3111|93047320]]
> **Семейство:** 6B5.9
> **Входит в руководства:** [[4021538 — B3.9 and B5.9 Recreational Marine Operation and Maintenance Manual|4021538]]
> **Секции:** Section A - Adjustment, Repair, and Replacement
> **Даты:** изменён 2005-01-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-005-043.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-005-043.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Отключение Solenoid Troubleshooting (In-Line-Type Injection Pump)

Двигатели, использующие встроенный тип насосов для впрыска, оснащены соленоидом отключения топлива Synchro-Start для приведения в действие рычага отключения. Доступны как 12-VDC, так и 24-VDC внешние соленоиды отключения топлива.

![[fv900ka.png]]

Synchro-Start имеет разъем Weather-Pack с тремя проводами в нем.

| цвет | Наименование | Погодный порт |
|---|---|---|
| черный | земля | C |
| белый | Щелчок | B |
| красный | держись | А. |

![[fv900gk.png]]

См. диаграмму ниже, чтобы найти правильный размер измерительной приборной ширины и длину непрерывного провода для белого (втягивающего) провода, который соединяется с соленоидной проводкой.

Это общая длина провода от батареи до соленоида и обратно к батарее. К ним следует добавить как белый, так и черный провод.

Четырнадцатимерный калибровочный провод требуется для красного (задерживаемого) провода, который соединяется с терминалом «Бег» на переключателе зажигания.

Черный (земляной) провод должен быть того же размера, что и белый (втягивающий) провод.

| Длина провода - максимальная длина |  |  |
|---|---|---|
| калибр | 12 VDC | 24 VDC |
| 14 | 1.5-m[5-ft] | 2,7 м[9 футов] |
| 12 | 2,7 м[9 футов] | 4,3 м[14 футов] |
| 10 | 4,3 м[14 футов] | 7.0-м[23-фут] |

![[05900603.png]]

### Подготовительные операции

Bosch® VE

Удалите электрический провод и выполните следующие действия.

Очистите клапан.

![[fv900mb.png]]

Bosch® насос с RSV-губернатором

Этот ремонт можно выполнить без снятия топливного насоса с двигателя.

Удаление рычага отключения, фильтра и линии подачи не требуется, если соленоид может быть доступен из нижней части топливного насоса.

Удалите топливный фильтр и линию подачи топлива, если это необходимо. См. процедуры[[40-006-015-tr — Fuel Filter (Spin-On Type)|006-015]]006-024.

Отсоедините проводную проводку от затвора топлива соленоида.

![[fs9ftec.png]]

### Первичная проверка

Впрыскивание топлива в ряд

> [!danger] ОПАСНО
> Носите защитную одежду, чтобы уменьшить вероятность получения травм. Температура поверхности соленоидов может превышать 175 ° C \[347 ° F \], что может вызвать серьезные ожоги кожи в случае контакта.

> [!note] Примечание
> Следующая проверка предназначена для всех встроенных топливных форсунок.

Значения принимаются при 20°C[68°F] и номинальном напряжении. Минимальные значения для 25-мм \[1.00-в\] максимальный плунжер путешествия. По мере увеличения температуры соленоида требования к напряжению и сопротивлению увеличиваются, а требования к усилию уменьшаются.

Соленоидное сопротивление можно проверить с помощью мультиметра. Отключите проводку и проверьте сопротивление соленоидов.

![[fv900sa.png]]

Синхро-старт соленоидов с 44,45-мм \[1,75-в\] диаметром катушки канистра

| Синхро-старт соленоидов 44,5 мм \[1,75 дюйма \] Диаметр катушки канистра |  |  |
|---|---|---|
| Соленоидное напряжение | Допустимая дальность сопротивления в Омсе |  |
|  | Щелчок | держись |
| 12 | 0,198 - 0,242 | 10.00 - 12.21 |
| 24 | 0738 - 0.902 | 37.17 - 45.43 |

Синхро-старт соленоидов с 50,8-мм \[2,00-в\] Диаметр катушки канистра.

| Синхро-старт соленоидов 50,8 мм \[2,00-в\] Диаметр катушки Канистер |  |  |
|---|---|---|
| Соленоидное напряжение | Допустимая дальность сопротивления в Омсе |  |
|  | Щелчок | держись |
| 12 | 0.175 - 0.213 | 12.75 - 15.56 |
| 24 | 0,554 - 0,678 | 46.76 - 57.15 |

![[fv900sa.png]]

Проверка напряжения

> [!note] Примечание
> Следующая проверка предназначена для всех встроенных топливных форсунок.

Для выполнения проверки соленоидного напряжения отсоедините конец соленоидного стержня от рычага отключения на топливном насосе, соедините проводную упряжку и приложите напряжение к соленоиду с помощью ключа зажигания следующим образом:

1. С ключом в положении RUN проверьте напряжение удерживания.
2. С рычагом выключения, удерживаемым в положении выключения, переместить ключ в положение START и проверить напряжение вытягивания.

См. таблицу для спецификации напряжения Synchro-Start с соленоидом при 20°C \[68°F\]. Требования к напряжению будут выше по мере повышения температуры двигателя; поэтому эти значения действительны только при соленоиде при нормальных температурах окружающей среды.

| Синхро-старт соленоидов 20°C[68°F] |  |  |
|---|---|---|
| Соленоидное напряжение | Минимальное напряжение |  |
|  | Щелчок | Задержка |
| 12 | 8.5 | 5.2 |
| 24 | 17.0 | 9.4 |

![[fv900sb.png]]

Станадын DB4

> [!warning] ОСТОРОЖНО
> Не проверяйте работу с соленоидом с подзарядкой, удаленной из насоса для впрыска топлива.

Испытайте выключатель соленоида на насосе впрыска топлива Stanadyne DB4, применив электрический ток к терминалам и прослушивая щелчок. Если слышен сильный щелчок, соленоид работает свободно.

Используйте следующие значения для проверки энергетизированных соленоидов:

| Standadyne DB4 Solenoid |  |
|---|---|
| VDC | VDC для зарядки (минимум) |
| 12 | 8.8 |
| 24 | 17.6 |

![[ip900ka.png]]

Lucas CAV DPA или DPS

Когда клапан на насосе Lucas CAV DPA/DPS открывается, можно услышать щелчок.

Используйте следующие значения для проверки соленоида:

| CAV соленоидные значения |  |  |
|---|---|---|
| VDC | Сопротивление Омс | VDC для зарядки (минимум) |
| 12 | 9 при 22°C \[71.6°F\] | 9 |
| 24 | 36 при 22°C \[71.6°F\] | 18 |

![[fv900wc.png]]

Стеклоотвод (Back Leakage клапанs on Lucas CAV Pumps)

Для каждой разрядной трубки имеется клапан. Цель клапана заключается в контроле остаточного давления в линии высокого давления. Неисправный клапан вызовет дисбаланс остаточного давления, приводящего к грубой работе двигателя или к его росту.

![[fv900gj.png]]

Bosch® VE

Клапан Bosch® при приведении в действие издает очень громкий звук, но его можно проверить с помощью омметра на следующие значения:

| Ценности Bosch Shutdown | Сопротивление Омс | Пик Ампера |
|---|---|---|
| 12 VDC | 7.4 + 0.5 | 2 |
| 24 VDC | 29.5 + 2.5 | 1 |

![[fv900wd.png]]

> [!warning] ОСТОРОЖНО
> Не подключайте электрический провод к соленоиду, когда плунжер был удален. Без плунжера клапан может быть поврежден.

Неисправные клапаны и электрическая проводка к клапану могут быть диагностированы путем удаления плунжера и пружины, а затем переустановки соленоида.

![[fs900ba.png]]

Если двигатель запускается без клапана, клапан или проводка к клапану неисправны.

Этот способ удаления плунжера для запуска двигателя может быть использован, при необходимости, для перемещения оборудования в служебное место.

Используйте механический рычаг выключения, чтобы остановить двигатель.

![[fv900bb.png]]

### Снятие

Bosch® VE

Удалите клапан.

> [!note] Примечание
> Показано устройство Bosch® VE. Клапан для Lucas CAV расположен в нижней части насоса.

![[fv9vama.png]]

> [!warning] ОСТОРОЖНО
> При снятии клапана будьте осторожны, чтобы не сбросить плунжер и пружину. Это может привести к повреждению топливного насоса.

![[fv9vaea.png]]

Станадын DB4

Инструмент для удаления винта с помощью Tamper-Resistant Screw, номер детали 3399870

- Удалите электропроводку.
- Удалите линию слива топлива. См. процедуру 006-021.
- Удалите дроссель и отключите связь. См. сервисное руководство изготовителя машины.
- Удалите непроницаемые винты с помощью набора инструментов, часть номер. 3399870. См. процедуры[[40-005-012-tr — Fuel Injection Pumps, In-Line|005-012]]или[[40-005-014-tr — Fuel Injection Pump, Rotary|005-014]].
- Снимите крышку насоса для впрыска топлива. См. Руководство по ремонту магистратуры, насосы для форсунок и топливный форсунок, Бюллетень 3666037.
- Разобрать крышку топливного насоса. См. Руководство по ремонту магистратуры, насосы для форсунок и топливный форсунок, Бюллетень 3666037.

![[ip9cvmc.png]]

Bosch® насос с RSV-губернатором

Удалите конец стержня из рычага выключения.

![[05900738.png]]

Удалить стоп-винт и скобки сборки.

![[05900552.png]]

Удалите рычаг (10) отключения над выключающим валом на внутренней стороне топливного насоса.

![[05900743.png]]

Удалите соленоид из сборки соленоидных кронштейнов и сборки соленоидных кронштейнов из топливного насоса. Если старый 1-3/4-дюймовый соленоид и кронштейн заменяются новым 2-дюймовым соленоидом, откажитесь от соленоидных крепежных болтов.

![[05900739.png]]

Bosch P Pump с губернатором RQVK

Соленоид не должен быть удален из двигателя, чтобы заменить управляющий стержень.

Освободите шайбу (1) из соленоида (3).

Отсоедините управляющий стержень (2) на рычаге, если управляющий стержень **не **сломан.

Отвинтите управляющий стержень, удерживая соленоидный поворот.

![[05900834.png]]

Освободите болты и гайку, которые удерживают конец стержня на рычаге выключения.

Сохранить прокладку между концом стержня и рычагом отключения.

![[05900835.png]]

Проверьте рычаг шуфоффа стоп рычаг стоп скобка.

Рычаг **должен** соприкасаться с стоп-винтом на стоп-винтовом скобке. Если рычаг не касается стоп-винта, отрегулируйте стоп-винт 1-1/2, который проходит мимо точки контакта между стоп-винтом и выключающим рычагом.

![[05900836.png]]

### Установка

Bosch® VE

Упакуйте соленоид, кольцо, пружину и плунжер.

![[fv9pgha.png]]

Закрепите соленоид надежно.

Подключите электрический провод.

> [!tip] Момент затяжки
> 43 Н·м [32 фунт-фут]

![[fv900hb.png]]

Станадын DB4

Установите новые изоляционные трубки на терминалы на концевых шпильках нового соленоида.

Установите клапан в крышку.

> [!tip] Момент затяжки
> 14 Н·м [124 фунт-дюйм]

![[ip9tbha.png]]

Установите крышку и прокладку на насос для впрыска топлива.

С помощью инструмента, установленного, как показано, поместите крышку в положение на корпус насоса. Вкрутите инструмент, чтобы выпустить его, и выскользните из между крышкой и корпусом.

Крайняя осторожность должна быть принята при сборке крышки насоса для впрыска топлива, чтобы убедиться, что выключатель находится в правильном контакте с вкладкой соединительного крючка.

![[ip9cvhb.png]]

В случае если инструмент службы **не доступен**, крышка губернатора должна быть установлена следующим образом:

Переведите рычаг отключения в положение остановки.

Установите крышку для насоса под углом вниз от конца вала впрыска топлива, затем сдвиньте крышку горизонтально в положение.

> [!tip] Момент затяжки
> 4.6 Н·м [41 фунт-дюйм]

![[ip9cvha.png]]

Bosch® насос с RSV-губернатором

> [!warning] ОСТОРОЖНО
> Несоблюдение надлежащих процедур проворачивания и зажигания топливной системы может вызвать сбои соленоидов.

Установите выключатель соленоида на топливный насос с помощью двух новых болтов M16 x 1,5-16. Применять LoctiteTM к болтам резьбы. Затяните болты достаточно, чтобы удерживать соленоид на месте.

> [!note] Примечание
> Новые соленоидные крепежные болты имеют предварительно наложенный клей, блокирующий резьба. Применение LoctiteTM не требуется при установке новых болтов.

> [!warning] ОСТОРОЖНО
> Новые соленоидные крепежные болты должны использоваться при замене старого 1-3/4-дюймового соленоида на 2-дюймовый соленоид. Недостаточное зацепление резьбы может привести к повреждению насоса и соленоида.

![[05900740.png]]

Установите рычаг (10) отключения над выключающим валом на топливном насосе.

Используйте болты (7), ранее удаленные, чтобы удерживать рычаг отключения на месте.

> [!tip] Момент затяжки
> 9 Н·м [84 фунт-дюйм]

![[05900743.png]]

Подсоедините конец стержня соленоида к рычагу отключения.

Затяните гайку с запорным рычагом.

> [!tip] Момент затяжки
> 9 Н·м [84 фунт-дюйм]

![[05900744.png]]

> [!warning] ОСТОРОЖНО
> Соленоидные крепежные болты не должны быть перегружены. Искажение корпуса топливного насоса может привести к тому, что стойка застрянет в топливном насосе.

Затягивайте соленоидные крепежные болты.

> [!tip] Момент затяжки
> 24 Н·м [212 фунт-дюйм]

![[05900741.png]]

> [!note] Примечание
> Если стоп-винт **не** перемещен, может потребоваться перенастройка **не**.

Соберите стоп-винт к стоп-винту. Регулируйте стоп-винт (3), чтобы контактная поверхность винтового выступа выходила на 10 мм за поверхность стоп-брекета (4).

Затянуть гайку (2) против стоп-брекетов, чтобы зафиксировать стоп-винт на месте.

![[05900551.png]]

Установите стоп-сборку с двумя болтами M6 x 1-16 (5).

Затяните болты.

> [!tip] Момент затяжки
> 7 Н·м [60 фунт-дюйм]

![[05900552.png]]

> [!warning] ОСТОРОЖНО
> Длина соленоидного стержня предварительно установлена. Корректировка соленоидного стержня может привести к повреждению соленоида или привести к жалобе на низкую мощность.

Убедитесь, что рычаг выключения контактирует с стоп-винтом и находится в полном положении стоп-сигнала. Если рычаг выключения **не** контактирует с стоп-винтом, убедитесь, что выключатель соленоид и стоп-винтовые кронштейны собраны правильно. Устраните соленоидные крепежные болты и при необходимости перенастройте соленоид.

![[05900742.png]]

Bosch P Pump с губернатором RQVK

Конец стержня для управления ориентацией стержня важен. Если стержень установлен неправильно, может произойти неправильная работа отключаемого соленоидного узла.

Установите шлюз (1) на новый управляющий стержень на конце штанги до тех пор, пока не будет \[13 мм\] 7/16 дюйма между началом резьбы (2) и гайкой (1).

![[05900837.png]]

Установите шайбу.

Ввиньте конец стержня в управляющий стержень, затягивая руки и делая так, чтобы **не** двигался каштан. Укладывайте управляющий стержень и стержень на плоскую поверхность. Поверните конец стержня так, чтобы и контрольный стержень, и конец стержня лежали плоско.

Затяните каштан на конец стержня.

![[05900838.png]]

Установите шлюз (2) на управляющий стержень на конце соленоида, пока не будет \[6 мм\] 1/4 дюйма между началом резьбы (1) и шлюзом (2).

Установите шайбу и ввинчайте управляющий стержень в соленоид.

![[05900839.png]]

Установите на рычаг отключения топливного насоса торцевые болты управляющего стержня, чтобы выровнять стержень управления.

Затянуть локон (1) при удерживании соленоидного поворота (3).

![[05900840.png]]

Соленоид предназначен для обеспечения вращения управляющего стержня.

Убедитесь, что установлен прокладка между концом стержня и рычагом выключения.

Затяните болты и гайку, которая удерживает конец стержня на рычаге выключения.

> [!tip] Момент затяжки
> 9 Н·м [80 фунт-дюйм]

![[05900835.png]]

### Завершающие операции

Установите все удаленные компоненты, включая топливный фильтр и линию подачи топлива.

Подключите проводную проводку к соленоиду отключения топлива.

![[ck800wa.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> Shutdown Solenoid Troubleshooting (In-Line-Type Injection Pump)
>
> Engines using the in-line type of injection pumps are equipped with the Synchro-Start fuel shutoff solenoid to actuate the shutoff lever. Both 12-VDC and 24-VDC external fuel shutoff solenoids are available.
>
> The Synchro-Start has a Weather-Pack connector with three wires in it.
>
> | Color | Description | Weather-Pack Port |
> |---|---|---|
> | Black | Ground | C |
> | White | Pull-in | B |
> | Red | Hold-in | A |
>
> Refer to the chart below to find the correct gauge size and length of continuous wire for the white (pull-in) wire which connects to the solenoid wiring.
>
> This is the total wire length from the battery to the solenoid and back to the battery. Both white and black wire length **must** be added.
>
> Fourteen-gauge wire is required for the red (hold-in) wire, which connects to the “Run” terminal on the ignition switch.
>
> The black (ground) wire **must** be the same size as the white (pull-in) wire.
>
> | Length of Wire - Maximum Length |  |  |
> |---|---|---|
> | Gauge | 12 VDC | 24 VDC |
> | 14 | 1.5-m \[5-ft\] | 2.7-m \[9-ft\] |
> | 12 | 2.7-m \[9-ft\] | 4.3-m \[14-ft\] |
> | 10 | 4.3-m \[14-ft\] | 7.0-m \[23-ft\] |
>
> ### Preparatory Steps
>
> Bosch® VE
>
> Remove the electrical wire and complete the following steps.
>
> Clean around the valve.
>
> Bosch® A Pump with RSV Governor
>
> This repair can be performed without removing the fuel pump from the engine.
>
> Removal of the shutoff lever, filter, and supply line is **not** necessary if the solenoid can be accessed from the bottom of the fuel pump.
>
> Remove the fuel filter and fuel supply line, if necessary. Refer to Procedures [[40-006-015-tr — Fuel Filter (Spin-On Type)|006-015]] and 006-024.
>
> Disconnect the wire harness from the fuel shutoff solenoid.
>
> ### Initial Check
>
> In-line Fuel Injection Pumps
>
> **WARNING · Опасно**
> Wear protective clothing to reduce the possibility of personal injury. Solenoid surface temperature can exceed 175°C \[347°F\], which can cause serious burns to the skin in the event of contact.
>
> **Note · Примечание**
> The following check is for all In-line fuel injector pumps.
>
> Values are taken at 20°C \[68°F\] and rated voltage. Minimum values are for 25-mm \[1.00-in\] maximum plunger travel. As the temperature of the solenoid increases, the voltage and resistance requirements increase, while the amperage requirements decrease.
>
> The solenoid resistance can be checked using a multimeter. Disconnect the wiring harness and check the solenoid resistance.
>
> Synchro-Start solenoids with a 44.45-mm \[1.75-in\] diameter coil canister
>
> | Synchro-Start Solenoids 44.5-mm \[1.75-in\] Diameter Coil Canister |  |  |
> |---|---|---|
> | Solenoid Voltage | Acceptable Resistance Range in Ohms |  |
> |  | Pull-in | Hold-in |
> | 12 | 0.198 to 0.242 | 10.00 to 12.21 |
> | 24 | 0738 to 0.902 | 37.17 to 45.43 |
>
> Synchro-Start Solenoids with a 50.8-mm \[2.00-in\] Diameter Coil Canister.
>
> | Synchro-Start Solenoids 50.8-mm \[2.00-in\] Diameter Coil Canister |  |  |
> |---|---|---|
> | Solenoid Voltage | Acceptable Resistance Range in Ohms |  |
> |  | Pull-in | Hold-in |
> | 12 | 0.175 to 0.213 | 12.75 to 15.56 |
> | 24 | 0.554 to 0.678 | 46.76 to 57.15 |
>
> Voltage Checking
>
> **Note · Примечание**
> The following check is for all In-line fuel injector pumps.
>
> To perform the solenoid voltage check, disconnect the solenoid rod end from the shutdown lever on the fuel pump, connect the wiring harness, and apply voltage to the solenoid with the ignition key as follows:
>
> 1. With the key in the RUN position, check the hold-in voltage.
> 2. With the shutdown lever held in the shutdown position, move the key to the START position, and check the pull-in voltage.
>
> Refer to the table for Synchro-Start voltage specification with solenoid at 20°C \[68°F\]. Voltage requirements will be higher as engine temperature rises; therefore, these values are **only** valid with the solenoid at normal ambient temperatures.
>
> | Synchro-Start Solenoids 20° C \[68°F\] |  |  |
> |---|---|---|
> | Solenoid Voltage | Minimum Voltage |  |
> |  | Pull-in | Hold-In |
> | 12 | 8.5 | 5.2 |
> | 24 | 17.0 | 9.4 |
>
> Stanadyne DB4
>
> **CAUTION · Осторожно**
> Do not check energize-to-run solenoid operation with governor cover removed from the fuel injection pump.
>
> Test the shutdown solenoid on the Stanadyne DB4 fuel injection pump by applying an electrical current to the terminals and listening for a click. If a solid click is heard, the solenoid is operating freely.
>
> Use the following values to check energize-to-run solenoids:
>
> | Standadyne DB4 Solenoid |  |
> |---|---|
> | VDC | VDC to Energize (Minimum) |
> | 12 | 8.8 |
> | 24 | 17.6 |
>
> Lucas CAV DPA or DPS
>
> When the valve on the Lucas CAV DPA/DPS pump opens, a click can be heard.
>
> Use the following values to check the solenoid:
>
> | CAV Solenoid Values |  |  |
> |---|---|---|
> | VDC | Resistance Ohms | VDC to Energize (Minimum) |
> | 12 | 9 at 22°C \[71.6°F\] | 9 |
> | 24 | 36 at 22°C \[71.6°F\] | 18 |
>
> Delivery Valves (Back Leakage Valves on Lucas CAV Pumps)
>
> There is a valve for each discharge tube. The purpose of the valve is to control the residual pressure in the high-pressure line. A malfunctioning valve will cause an imbalance of the residual pressure resulting in rough engine operation or surging.
>
> Bosch® VE
>
> The Bosch® valve does **not** make a very loud sound when actuated, but it can be checked with an ohmmeter for the following values:
>
> | Bosch Shutdown Values | Resistance Ohms | Peak Amperes |
> |---|---|---|
> | 12 VDC | 7.4 + 0.5 | 2 |
> | 24 VDC | 29.5 + 2.5 | 1 |
>
> **CAUTION · Осторожно**
> Do not connect the electrical wire to the solenoid when the plunger has been removed. Without the plunger, the valve can be damaged.
>
> Malfunctioning valves and electrical wiring to the valve can be diagnosed by removing the plunger and spring, and then reinstalling the solenoid.
>
> If the engine will start without the valve, the valve or the wiring to the valve is malfunctioning.
>
> This method of removing the plunger to start the engine can be used, if necessary, to move the equipment to a service location.
>
> Use the mechanical shutdown lever to stop the engine.
>
> ### Remove
>
> Bosch® VE
>
> Remove the valve.
>
> **Note · Примечание**
> The Bosch® VE valve is shown. The valve for Lucas CAV is located at the bottom of the pump.
>
> **CAUTION · Осторожно**
> When removing the valve, be careful not to drop the plunger and spring. Doing so can result in fuel pump damage.
>
> Stanadyne DB4
>
> Tamper-Resistant Screw Removal Tool, Part Number 3399870
>
> - Remove the electrical wiring.
> - Remove the fuel drain line. Refer to Procedure 006-021.
> - Remove the throttle and shutoff linkage. Refer to the OEM service manual.
> - Remove tamper-resistant screws using service tool kit, Part Number. 3399870. Refer to Procedures [[40-005-012-tr — Fuel Injection Pumps, In-Line|005-012]] or [[40-005-014-tr — Fuel Injection Pump, Rotary|005-014]].
> - Remove the fuel injection pump top cover. Refer to the Master Repair Manual, Injector Pumps and Injectors, Bulletin 3666037.
> - Disassemble the fuel injection pump top cover. Refer to the Master Repair Manual, Injector Pumps and Injectors, Bulletin 3666037.
>
> Bosch® A Pump with RSV Governor
>
> Remove the rod end from the shutoff lever.
>
> Remove the stop screw and bracket assembly.
>
> Remove the shutoff lever (10) over the shutoff shaft on the inboard side of the fuel pump.
>
> Remove the solenoid from the solenoid bracket assembly and solenoid bracket assembly from the fuel pump. If the old 1-3/4 inch solenoid and bracket assembly is being replaced with the new 2-inch solenoid, discard the solenoid mounting capscrews.
>
> Bosch® P Pump with RQVK Governor
>
> The solenoid does **not** have to be removed from engine to replace the control rod.
>
> Loosen the locknut washer (1) from the solenoid (3).
>
> Disconnect the control rod (2) at the lever if control rod is **not** broken.
>
> Unscrew the control rod while holding the solenoid swivel.
>
> Loosen the capscrew and nut that holds the rod end onto the shutoff lever.
>
> Retain the spacer between the rod end and the shutoff lever.
>
> Check the shufoff lever stop lever stop bracket.
>
> The lever **must** make contact with the stop screw on the stop screw bracket. If the lever does **not** touch the stop screw, adjust the stop screw out 1-1/2 turns past the point of contact between the stop screw and the shutoff lever.
>
> ### Install
>
> Bosch® VE
>
> Package the solenoid, o-ring, spring, and plunger.
>
> Tighten the solenoid securely.
>
> Connect the electric wire.
>
> **Момент затяжки · Torque Value**
> 43 n•m [32 ft-lb]
>
> Stanadyne DB4
>
> Install new insulating tubes onto the terminals on the terminal studs of the new solenoid.
>
> Install the valve into the cover.
>
> **Момент затяжки · Torque Value**
> 14 n•m [124 in-lb]
>
> Install the cover and gasket onto the fuel injection pump.
>
> With the tool installed as shown, place the cover in position on the pump housing. Twist the tool to release it, and slide it out from between the cover and the housing.
>
> Extreme care **must** be taken in assembling the cover to a fuel injection pump to make sure the shutoff arm is in proper contact with the linkage hook tab.
>
> In the event the service tool is **not** available, the governor cover **must** be installed as follows:
>
> Move the shutoff lever to the stop position.
>
> Install the cover to pump at a downward angle from the driveshaft end of the fuel injection pump, then slide the cover horizontally into position.
>
> **Момент затяжки · Torque Value**
> 4.6 n•m [41 in-lb]
>
> Bosch® A Pump with RSV Governor
>
> **CAUTION · Осторожно**
> Failure to observe proper cranking and fuel system priming procedures can cause solenoid failures.
>
> Install the shutoff solenoid on the fuel pump using two new M16 x 1.5-16 capscrews. Apply Loctite™ to the capscrew threads. Tighten the capscrews just enough to hold the solenoid in place.
>
> **Note · Примечание**
> New solenoid mounting capscrews have threadlocker pre-applied. Loctite™ application is **not** necessary when new capscrews are installed.
>
> **CAUTION · Осторожно**
> New solenoid mounting capscrews must be used if replacing an old 1-3/4-inch solenoid with a 2-inch solenoid. Insufficient thread engagement can cause damage to the pump and the solenoid.
>
> Install the shutoff lever (10) over the shutoff shaft on the fuel pump.
>
> Use the capscrew (7) previously removed to hold the shutoff lever in place.
>
> **Момент затяжки · Torque Value**
> 9 n•m [84 in-lb]
>
> Connect the rod end of the solenoid to the shutoff lever.
>
> Tighten the shutoff lever nut.
>
> **Момент затяжки · Torque Value**
> 9 n•m [84 in-lb]
>
> **CAUTION · Осторожно**
> The solenoid mounting capscrews must not be overtightened. Distortion to the fuel pump body can result causing the rack to stick in the fuel pump.
>
> Tighten the solenoid mounting capscrews.
>
> **Момент затяжки · Torque Value**
> 24 n•m [212 in-lb]
>
> **Note · Примечание**
> If the stop screw is **not** moved, readjustment may **not** be necessary.
>
> Assemble the stop screw to the stop screw bracket. Adjust the stop screw (3) so the contact surface of the screw protrudes 10 mm beyond the surface of the stop bracket (4).
>
> Tighten the nut (2) against the stop bracket to lock the stop screw in place.
>
> Install the stop bracket assembly using two M6 x 1-16 capscrews (5).
>
> Tighten the capscrews.
>
> **Момент затяжки · Torque Value**
> 7 n•m [60 in-lb]
>
> **CAUTION · Осторожно**
> The solenoid rod length is pre-set. Adjustment of the solenoid rod can cause damage to the solenoid or lead to a low power complaint.
>
> Verify the shutoff lever is contacting the stop screw and is in the full stop position. If the shutoff lever does **not** contact the stop screw, verify the shutoff solenoid and stop screw bracket are assembled correctly. Loosen the solenoid mounting capscrews and readjust the solenoid, if necessary.
>
> Bosch® P Pump with RQVK Governor
>
> The rod end to control rod orientation is important. If the rod end is installed incorrectly, improper operation of the shutoff solenoid assembly can occur.
>
> Install the locknut (1) onto the new control rod at the rod end until there is \[13 mm\] 7/16 inch between the start of the threads (2) and nut (1).
>
> Install the lock washer.
>
> Screw the rod end onto the control rod, hand tightening and making certain **not** to move the locknut. Lay the control rod and rod end on a flat surface. Rotate the rod end so both the control rod and the rod end lay flat.
>
> Tighten the locknut onto the rod end.
>
> Install the locknut (2) on the control rod at the solenoid end until there is \[6 mm\] 1/4 inch between start of the threads (1) and locknut (2).
>
> Install the lock washer and screw the control rod into the solenoid.
>
> Install the control rod end capscrew onto the fuel pump shutoff lever to align the control rod.
>
> Tighten the locknut (1) while holding the solenoid swivel (3).
>
> The solenoid is designed to allow rotation of the control rod.
>
> Make certain to install the spacer between the rod end and the shutoff lever.
>
> Tighten the capscrew and nut that holds the rod end onto the shutoff lever.
>
> **Момент затяжки · Torque Value**
> 9 n•m [80 in-lb]
>
> ### Finishing Steps
>
> Install all components removed, including the fuel filter and fuel supply line.
>
> Connect the wire harness to the fuel shutoff solenoid.
