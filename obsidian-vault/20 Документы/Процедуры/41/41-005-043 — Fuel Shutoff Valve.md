---
aliases:
  - "Клапан отсечки топлива"
type: "Процедура"
doc: "41-005-043"
title_en: "Fuel Shutoff Valve"
title_ru: "Клапан отсечки топлива"
modified: "2016-07-29"
engines:
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "2883407"
  - "3381968"
  - "3666003"
  - "4021330"
figures: 51
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/41/41-005-043.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/41-005-043.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/41"
  - "перевод/машинный"
---

# Fuel Shutoff Valve
**Клапан отсечки топлива**

> [!abstract] Процедура · `41-005-043`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[2883407 — C8.3 (India) Operation and Maintenance Manual|2883407]], [[3381968 — C8.3 Recreational Marine Operation and Maintenance Manual|3381968]], [[3666003 — C Troubleshooting and Repair Manual|3666003]], [[4021330 — C8.3 Commercial Marine and Industrial Operation and Maintenance Manual|4021330]]
> **Секции:** Section 5 - Fuel System - Group 05 · Section A - Adjustment, Repair, and Replacement
> **Даты:** изменён 2016-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/41/41-005-043.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/41-005-043.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Взрывной вид

![[05500142.png]]

1. Коннектор запорного клапана - 1
2. Запорный клапан топлива - 1
3. О-кольцо-1
4. Адаптер клапана отключения топлива - 1
5. Обычная шайба - 2
6. Шайба - 2
7. Монтажные болты - 2
8. Затворы запорного клапана адаптера - 2
9. Кронштейн запорного клапана - 1
10. Затворы затвора топлива - 2.

### Выбор сервисного инструмента

#### Рекомендованный сервисный инструмент Cummins®

- Вольт-ом-метр, часть 3164488
- Инструмент для удаления отбросов Tamper Screw, номер детали 3399870.

#### Дополнительные сервисные позиции

- Не требуется никаких дополнительных предметов обслуживания.

### Общие сведения

#### Отключение Solenoid Troubleshooting (In-Line-Type Injection Pump)

- Двигатели, использующие встроенный тип насосов для впрыска, оснащены соленоидом отключения топлива Synchro-Start или WoodwardTM для приведения в действие рычага отключения. Доступны как 12 VDC, так и 24 VDC внешних соленоидов отключения топлива.

![[fv900ka.png]]

Двигатели, использующие встроенный тип насосов для впрыска, оснащены соленоидом отключения топлива Synchro-Start или WoodwardTM для приведения в действие рычага отключения.

Доступны как 12 VDC, так и 24 VDC внешних соленоидов отключения топлива.

| цвет | Наименование | Порт Weather-PackTM |
|---|---|---|
| черный | земля | C |
| белый | Щелчок | B |
| красный | держись | А. |

![[fv900gk.png]]

Используйте диаграмму ниже, чтобы найти правильный размер измерительной приборной ширины и длину непрерывного провода для белого (втягивающего) провода, который соединяется с соленоидной проводкой.

Это общая длина провода от батареи до соленоида и обратно к батарее. К ним следует добавить как белый, так и черный провод.

Четырнадцатимерный калибровочный провод требуется для красного (задерживаемого) провода, который соединяется с терминалом «Бег» на переключателе зажигания.

Черный (земляной) провод должен быть того же размера, что и белый (втягивающий) провод.

| Длина провода - максимальная длина |  |  |
|---|---|---|
| калибр | 12 VDC | 24 VDC |
| 14 | 1.5 мм \[5 футов \] | 2,7 мм[9 футов] |
| 12 | 2,7 мм[9 футов] | 4,3 мм[14 футов] |
| 10 | 4,3 мм[14 футов] | 7,0 мм[23 фута] |

![[05900603.png]]

### Подготовительные операции

BoschTM насос с RSV губернатором

> [!note] Примечание
> Этот ремонт можно выполнить без снятия топливного насоса с двигателя.

- Удаление рычага отключения, фильтра и линии подачи не требуется, если соленоид может быть доступен из нижней части топливного насоса.
- Удалите топливный фильтр и линию подачи топлива, если это необходимо.[[41-006-015-tr — Fuel Filter (Spin-On Type)|См. процедуру 006-015]]и[[41-006-024 — Fuel Supply Lines|См. процедуру 006-024 в разделе 6.]]
- Наклейте этикетку и удалите проводку из выключенного соленоида.

Generator Set Applications (недоступная ссылка)

- Отсоедините аккумуляторные батареи. См. сервисную документацию изготовителя оборудования.
- Отсоедините проводную проводку от запорного клапана.
- Удалите линию подачи топлива.[[41-006-024 — Fuel Supply Lines|См. процедуру 006-024 в разделе 6.]]

![[05500137.png]]

### Первичная проверка

Впрыскивание топлива в ряд

> [!danger] ОПАСНО
> Носите защитную одежду, чтобы уменьшить вероятность получения травм. Температура поверхности соленоидов может превышать 175 ° C \[347 ° F \], что может вызвать серьезные ожоги кожи в случае контакта.

> [!note] Примечание
> Следующая проверка предназначена для всех встроенных топливных форсунок.

Значения принимаются при 20°C[68°F] и номинальном напряжении. Минимальные значения для 25-мм \[1.00-в\] максимальный плунжер путешествия. По мере увеличения температуры соленоида требования к напряжению и сопротивлению увеличиваются, а требования к усилию уменьшаются.

Соленоидное сопротивление можно проверить с помощью мультиметра. Отключите проводку и проверьте сопротивление соленоидов.

![[fv900sa.png]]

| Синхро-старт соленоидов 44,5 мм \[1,75 дюйма \] Диаметр катушки канистра |  |  |
|---|---|---|
| Соленоидное напряжение | Допустимая дальность сопротивления в Омсе |  |
|  | Щелчок | держись |
| 12 | 0,198 - 0,242 | 10.00 - 12.21 |
| 24 | 0,738 - 0,902 | 37.17 - 45.43 |

| Синхро-старт соленоидов 50,8 мм \[2,00 дюйма \] Диаметр катушки Канистер |  |  |
|---|---|---|
| Соленоидное напряжение | Допустимая дальность сопротивления в Омсе |  |
|  | Щелчок | держись |
| 12 | 0.175 - 0.213 | 12.75 - 15.56 |
| 24 | 0,554 - 0,678 | 46.76 - 57.15 |

| Соленоиды WoodwardTM с диаметром катушки 44,5 мм[1,75 дюйма] |  |  |
|---|---|---|
| Соленоидное напряжение | Допустимая дальность сопротивления в Омсе |  |
|  | Щелчок | держись |
| 12 | 0,232 - 0,284 | 9.818 - 12.001 |
| 24 | 0,878 - 1,073 | 46.548 - 56.892 |

| Соленоиды WoodwardTM с диаметром диаметрической катушки 50,8 мм \[2,00 дюйма \] |  |  |
|---|---|---|
| Соленоидное напряжение | Допустимая дальность сопротивления в Омсе |  |
|  | Щелчок | держись |
| 12 | 0.175 - 0.213 | 12.75 - 15.59 |
| 24 | 0,554 - 0,678 | 46.76 - 57.15 |

![[fv900sa.png]]

Проверка напряжения

> [!note] Примечание
> Следующая проверка предназначена для всех встроенных топливных форсунок.

Для выполнения проверки соленоидного напряжения отсоедините конец соленоидного стержня от рычага отключения на топливном насосе, соедините проводную упряжку и приложите напряжение к соленоиду с помощью ключа зажигания следующим образом:

1. С ключом в положении RUN проверьте напряжение удерживания.
2. С рычагом выключения, удерживаемым в положении выключения, переместить ключ в положение START и проверить напряжение вытягивания.

Используйте таблицу для спецификации напряжения Synchro-Start с соленоидом при 20 ° C \[68 ° F \]. Требования к напряжению будут выше по мере повышения температуры двигателя; поэтому эти значения действительны только при соленоиде при нормальных температурах окружающей среды.

| Синхро-старт соленоидов 20°C[68°F] |  |  |
|---|---|---|
| Соленоидное напряжение | Минимальное напряжение |  |
|  | Щелчок | держись |
| 12 | 8.5 | 5.2 |
| 24 | 17.0 | 9.4 |

![[fv900sb.png]]

BoschTM VE

| Ценности закрытия BoschTM | Сопротивление Омс | Пик Ампера |
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

Generator Set Applications (недоступная ссылка)

> [!note] Примечание
> Там **должен быть **только один провод, подключенный к запорному клапану.

Подключите проводную проводку к катушке запорного клапана.

Убедитесь, что напряжение правильное.

Требуемое напряжение катушки и номер детали отбрасываются в корпус терминального соединения в конце запорного клапана.

![[fp8vacf.png]]

Переключатель зажигания переключателя в положение "Включено".

Проверьте напряжение постоянного тока катушки с помощью вольт-омметра, Номер детали 3164488 или эквивалент.

Напряжение должно быть таким же, как и спецификации напряжения.

Переключатель зажигания переключателя на положение "OFF".

![[fv2swkb.png]]

Убедитесь, что катушка провода **не подключена **перед проверкой сопротивления запорного клапана.

Проверьте сопротивление с помощью вольт-омметра. Сопротивление должно быть:

| Сопротивление катушке |  |
|---|---|
| Напряжение | Сопротивление |
| 24 VDC | 28-32 Ом |

Заменить запорный клапан, если сопротивление не соответствует спецификациям.

![[fv2swkc.png]]

Переключатель зажигания переключателя в положение "Включено". Слушайте, чтобы клапан «щелкнул», когда провод прикасается к терминалу катушки. Если клапан делает **не** "щелчок", ремонт или замена топливного отключающего клапана.

![[fv8elka.png]]

### Снятие

BoschTM VE

Удалите клапан.

> [!note] Примечание
> Показано устройство Bosch VE. Клапан для LucasTM CAV расположен в нижней части насоса.

![[fv9vama.png]]

> [!warning] ОСТОРОЖНО
> При снятии клапана будьте осторожны, чтобы не сбросить плунжер и пружину. Это может привести к повреждению топливного насоса.

![[fv9vaea.png]]

Станадын DB4

Инструмент для удаления отбросов Tamper Screw, номер детали 3399870.

- Удалите электропроводку.
- Удалите линию слива топлива. См. процедуру 006-021 в разделе 6.
- Удалите дроссель и отключите связь. См. сервисную документацию изготовителя оборудования.
- Удалите непроницаемые винты с помощью набора для инструментов, номер детали 3399870.[[41-005-012 — Fuel Injection Pumps, In-Line|См. процедуру 005-012 в разделе 5.]]
- Снимите крышку насоса для впрыска топлива. Ссылка на Руководство по ремонту, насосы для топливных форсунок и топливный форсунок, Вестник 3666037.

![[ip9cvmc.png]]

BoschTM насос с RSV губернатором

Удалите конец стержня из рычага выключения.

![[05900738.png]]

Удалить стоп-винт и скобки сборки.

![[05900552.png]]

Удалите рычаг (10) отключения над выключающим валом на внутренней стороне топливного насоса.

![[05900743.png]]

Удалите соленоид из сборки соленоидных кронштейнов и сборки соленоидных кронштейнов из топливного насоса. Если старый 1-3/4-дюймовый соленоид и кронштейн заменяются новым 2-дюймовым соленоидом, откажитесь от соленоидных крепежных болтов.

![[05900739.png]]

Bosch Pump с губернатором RQVK

Соленоид не должен быть удален из двигателя, чтобы заменить управляющий стержень.

Освободите шайбу (1) из соленоида (3).

Отсоедините управляющий стержень (2) на рычаге, если управляющий стержень **не **сломан.

Отвинтите управляющий стержень, удерживая соленоидный поворот.

![[05900834.png]]

Освободите болты и гайку, которые удерживают конец стержня на рычаге выключения.

Сохранить прокладку между концом стержня и рычагом отключения.

![[05900835.png]]

Проверьте рычаг выключения стоп-сигнал стоп-сигнала.

Рычаг **должен** соприкасаться с стоп-винтом на стоп-винтовом скобке. Если рычаг не касается стоп-винта, отрегулируйте стоп-винт 1-1/2, который проходит мимо точки контакта между стоп-винтом и выключающим рычагом.

![[05900836.png]]

Generator Set Applications (недоступная ссылка)

Удалите разъем запорного клапана топлива.

![[05500138.png]]

Удалите запорный клапан, кольцо, шайбу, простую шайбу и болты.

![[05500139.png]]

Удалите адаптер клапана отключения топлива.

![[05500141.png]]

Снимите топливный запорный клапан и болты.

![[05500140.png]]

### Очистка и проверка при повторном использовании

Замените кронштейн клапана отключения топлива, разъём и адаптер, если обнаружена трещина или повреждение.

![[05500144.png]]

### Установка

> [!note] Примечание
> Убедитесь, что желудочный гайка затянут, чтобы быть прижатым к соленоидному валу отключения топлива (Synchro-start *только).

Установите новый топливный выключатель соленоида на скобку и соедините провода. Убедитесь, что проводка упряжки один соленоид Тромбетта установлен в шестичасовом положении.

> [!tip] Момент затяжки
> 10 Н·м [89 фунт-дюйм]

1. Синхро-старт
2. Тромбэтта
3. Прямое соединение.

![[fs900md.png]]

Активируйте выключатель и проверьте путешествие плунжера.

|  | Синхро-старт | Тромбэтта | Прямое соединение |
|---|---|---|---|
| A = | 86.8.2 мм \[3.4 in\] | 91,4 мм \[3,6 in\] |  |
| B = | 60,2 мм \[2,4 in\] | 63,5 мм \[2,5 in\] | 117,1 мм \[4,61 в\] |

Прыгун **должен** быть отведен, когда соленоид отключения топлива активирован до положения БПЛА В. Соленоид отключения топлива **должен **работать без привязки.

![[fs900we.png]]

Удалите зажим для зажима, крепежные болты и соленоид отключения топлива.

Установите новый соленоид в обратном порядке удаления и соедините провода.

> [!tip] Момент затяжки
> 10 Н·м [89 фунт-дюйм]

![[fs900ma.png]]

Отрегулируйте соленоидную связь по мере необходимости, чтобы плунжер магнитно удерживался с рычагом отключения в абсолютном положении полного хода. Поверните большой шестигранный гайка на конце плунжера, чтобы внести коррективы, и закрепите на месте с помощью креветки.

![[fv9pgua.png]]

BoschTM насос с RSV губернатором

> [!warning] ОСТОРОЖНО
> Несоблюдение надлежащих процедур проворачивания и зажигания топливной системы может привести к неисправности соленоидов.

> [!warning] ОСТОРОЖНО
> Новые соленоидные крепежные болты должны использоваться при замене старого 1-3/4-дюймового соленоида на 2-дюймовый соленоид. Недостаточное зацепление резьбы может привести к повреждению насоса и соленоида.

Установите выключатель соленоида на топливный насос с помощью двух новых болтов M16 x 1,5-16. Применять Loctite® к болтам резьбы. Затяните болты достаточно, чтобы удерживать соленоид на месте.

> [!note] Примечание
> Новые соленоидные крепежные болты имеют предварительно наложенный клей, блокирующий резьба. Применение Loctite® **не** необходимо при установке новых болтов.

![[05900739.png]]

Установите рычаг (10) отключения над выключающим валом на топливном насосе.

Используйте болты (7), ранее удаленные, чтобы удерживать рычаг отключения на месте.

> [!tip] Момент затяжки
> 9 Н·м [80 фунт-дюйм]

![[05900743.png]]

Подсоедините конец стержня соленоида к рычагу отключения.

Затяните гайку с запорным рычагом.

> [!tip] Момент затяжки
> 9 Н·м [80 фунт-дюйм]

![[05900744.png]]

> [!warning] ОСТОРОЖНО
> Соленоидные крепежные болты не должны быть перегружены. Искажение корпуса топливного насоса может привести к тому, что стойка застрянет в топливном насосе.

Затягивайте соленоидные крепежные болты.

> [!tip] Момент затяжки
> 24 Н·м [212 фунт-дюйм]

![[05900741.png]]

> [!note] Примечание
> Если стоп-винт **не** перемещен, может потребоваться перенастройка **не**.

Соберите стоп-винт к стоп-винту. Регулируйте стоп-винт (3) так, чтобы контактная поверхность винта выступала на 10 мм \[0,394 дюйма \] за поверхностью стоп-брекета (4).

Затянуть гайку (2) против стоп-брекетов, чтобы зафиксировать стоп-винт на месте.

![[05900551.png]]

Установите стоп-сборку с двумя болтами M6 x 1-16 (5).

Затяните болты.

> [!tip] Момент затяжки
> 7 Н·м [62 фунт-дюйм]

![[05900552.png]]

> [!warning] ОСТОРОЖНО
> Длина соленоидного стержня предварительно установлена. Корректировка соленоидного стержня может привести к повреждению соленоида или привести к жалобе на низкую мощность.

Убедитесь, что рычаг выключения контактирует с стоп-винтом и находится в полном положении стоп-сигнала. Если рычаг выключения **не** контактирует с стоп-винтом, убедитесь, что выключатель соленоид и стоп-винтовые кронштейны собраны правильно. Устраните соленоидные крепежные болты и при необходимости перенастройте соленоид.

![[05900742.png]]

Bosch Pump с губернатором RQVK

Конец стержня для управления ориентацией стержня важен. Если стержень установлен неправильно, может произойти неправильная работа отключаемого соленоидного узла.

Установите шлюз (1) на новый управляющий стержень на конце штанги до тех пор, пока не будет 13 мм \[7/16 дюйма\] между началом резьбы (2) и гайкой (1).

![[05900837.png]]

Установите шайбу.

Ввиньте конец стержня в управляющий стержень, затягивайте вручную и убедитесь, что **не**, чтобы переместить каштан. Укладывайте управляющий стержень и стержень на плоскую поверхность. Поверните конец стержня так, чтобы и контрольный стержень, и конец стержня лежали плоско.

Затяните каштан на конец стержня.

![[05900838.png]]

Установите шнурок (2) на управляющий стержень на конце соленоида до тех пор, пока не будет 6 мм \[1/4 дюйма\] между началом резьбы (1) и шнуром (2).

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

Generator Set Applications (недоступная ссылка)

Установите кронштейн клапана отключения топлива.

> [!tip] Момент затяжки
> 43 Н·м [32 фунт-фут]

![[05500140.png]]

Установите адаптер клапана отключения топлива.

> [!tip] Момент затяжки
> 43 Н·м [32 фунт-фут]

![[05500141.png]]

Установите Уплотнительное кольцо на канавку.

![[05400430.png]]

Установите запорный клапан, шайбу, простую шайбу.

Затяните болты.

> [!tip] Момент затяжки
> 13 Н·м [115 фунт-дюйм]

![[05500143.png]]

Установите разъем запорного клапана топлива.

> [!tip] Момент затяжки
> 6 Н·м [53 фунт-дюйм]

![[05500138.png]]

### Завершающие операции

- Установите все компоненты, удаленные, включая топливный фильтр и линию подачи топлива, если они удалены.[[41-006-015-tr — Fuel Filter (Spin-On Type)|См. процедуру 006-015]]и[[41-006-024 — Fuel Supply Lines|См. процедуру 006-024 в разделе 6.]]
- Подключите проводную проводку к соленоиду отключения топлива.
- Запустите двигатель и проверьте его правильность.


> [!quote]- Original (English) · английский оригинал
> ### Exploded View
>
> 1. Fuel shutoff valve connector - 1
> 2. Fuel shutoff valve - 1
> 3. O-ring-1
> 4. Fuel shutoff valve adapter - 1
> 5. Plain washer - 2
> 6. Lock washer - 2
> 7. Mounting capscrew - 2
> 8. Fuel shutoff valve adapter capscrew - 2
> 9. Fuel shutoff valve bracket - 1
> 10. Fuel shutoff valve bracket capscrew - 2.
>
> ### Select Service Tools
>
> #### Recommended Cummins® Service Tools
>
> - Volt-ohm Meter, Part Number 3164488
> - Tamper Screw Removal Tool, Part Number 3399870.
>
> #### Additional Service Items
>
> - No addition service items required.
>
> ### General Information
>
> #### Shutdown Solenoid Troubleshooting (In-Line-Type Injection Pump)
>
> - Engines using the in-line type of injection pumps are equipped with the Synchro-Start or Woodward™ fuel shutoff solenoid to actuate the shutoff lever. Both 12 VDC and 24 VDC external fuel shutoff solenoids are available.
>
> Engines using the in-line type of injection pumps are equipped with the Synchro-Start or Woodward™ fuel shutoff solenoid to actuate the shutoff lever.
>
> Both 12 VDC and 24 VDC external fuel shutoff solenoids are available.
>
> | Color | Description | Weather-Pack™ Port |
> |---|---|---|
> | Black | Ground | C |
> | White | Pull-in | B |
> | Red | Hold-in | A |
>
> Use the chart below to find the correct gauge size and length of continuous wire for the white (pull-in) wire which connects to the solenoid wiring.
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
> | 14 | 1.5 mm \[5 ft\] | 2.7 mm \[9 ft\] |
> | 12 | 2.7 mm \[9 ft\] | 4.3 mm \[14 ft\] |
> | 10 | 4.3 mm \[14 ft\] | 7.0 mm \[23 ft\] |
>
> ### Preparatory Steps
>
> Bosch™ A Pump with RSV Governor
>
> **Note · Примечание**
> This repair can be performed without removing the fuel pump from the engine.
>
> - Removal of the shutoff lever, filter, and supply line is **not** necessary, if the solenoid can be accessed from the bottom of the fuel pump.
> - Remove the fuel filter and fuel supply line, if necessary. [[41-006-015-tr — Fuel Filter (Spin-On Type)|Refer to Procedure 006-015]] and [[41-006-024 — Fuel Supply Lines|Refer to Procedure 006-024 in Section 6.]]
> - Label and remove the wiring harness from the shutoff solenoid.
>
> Generator Set Applications
>
> - Disconnect the batteries. See equipment manufacturer service information.
> - Disconnect the wire harness from the fuel shutoff valve.
> - Remove the fuel supply line. [[41-006-024 — Fuel Supply Lines|Refer to Procedure 006-024 in Section 6.]]
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
> | Synchro-Start Solenoids 44.5 mm \[1.75 in\] Diameter Coil Canister |  |  |
> |---|---|---|
> | Solenoid Voltage | Acceptable Resistance Range in Ohms |  |
> |  | Pull-in | Hold-in |
> | 12 | 0.198 to 0.242 | 10.00 to 12.21 |
> | 24 | 0.738 to 0.902 | 37.17 to 45.43 |
>
> | Synchro-Start Solenoids 50.8 mm \[2.00 in\] Diameter Coil Canister |  |  |
> |---|---|---|
> | Solenoid Voltage | Acceptable Resistance Range in Ohms |  |
> |  | Pull-in | Hold-in |
> | 12 | 0.175 to 0.213 | 12.75 to 15.56 |
> | 24 | 0.554 to 0.678 | 46.76 to 57.15 |
>
> | Woodward™ solenoids with a 44.5 mm \[1.75 in\] Diameter Coil Canister |  |  |
> |---|---|---|
> | Solenoid Voltage | Acceptable Resistance Range in Ohms |  |
> |  | Pull-in | Hold-in |
> | 12 | 0.232 to 0.284 | 9.818 to 12.001 |
> | 24 | 0.878 to 1.073 | 46.548 to 56.892 |
>
> | Woodward™ solenoids with a 50.8 mm \[2.00 in\] Diameter Coil Canister |  |  |
> |---|---|---|
> | Solenoid Voltage | Acceptable Resistance Range in Ohms |  |
> |  | Pull-in | Hold-in |
> | 12 | 0.175 to 0.213 | 12.75 to 15.59 |
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
> Use the table for Synchro-Start voltage specification with solenoid at 20°C \[68°F\]. Voltage requirements will be higher as engine temperature rises; therefore, these values are **only** valid with the solenoid at normal ambient temperatures.
>
> | Synchro-Start Solenoids 20° C \[68°F\] |  |  |
> |---|---|---|
> | Solenoid Voltage | Minimum Voltage |  |
> |  | Pull-in | Hold-in |
> | 12 | 8.5 | 5.2 |
> | 24 | 17.0 | 9.4 |
>
> Bosch™ VE
>
> | Bosch™ Shutdown Values | Resistance Ohms | Peak Amperes |
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
> Generator Set Applications
>
> **Note · Примечание**
> There **must** be **only** one wire connected to the shutoff valve.
>
> Connect the wire harness to the shutoff valve coil.
>
> Make sure the voltage is correct.
>
> The coil required voltage and part number are cast into the terminal connection case at the end of the shutoff valve.
>
> Turn the key switch to the "ON" position.
>
> Check the DC voltage of the coil with a volt-ohm meter, Part Number 3164488, or equivalent.
>
> The voltage **must** be same as the voltage specifications.
>
> Turn the key switch to the "OFF" position.
>
> Make sure the coil wire is **not** connected before checking the shutoff valve resistance.
>
> Check the resistance with a volt-ohm meter. The resistance **must** be:
>
> | Coil Resistance |  |
> |---|---|
> | Voltage | Resistance |
> | 24 VDC | 28 to 32 ohms |
>
> Replace the shutoff valve if the resistance does **not** meet the specifications.
>
> Turn the key switch to the "ON" position. Listen for the valve to "click" when the wire is touched to the coil terminal. If the valve does **not** "click", repair or replace the fuel shutoff valve.
>
> ### Remove
>
> Bosch™ VE
>
> Remove the valve.
>
> **Note · Примечание**
> The Bosch™ VE valve is shown. The valve for Lucas™ CAV is located at the bottom of the pump.
>
> **CAUTION · Осторожно**
> When removing the valve, be careful not to drop the plunger and spring. Doing so can result in fuel pump damage.
>
> Stanadyne DB4
>
> Tamper Screw Removal Tool, Part Number 3399870.
>
> - Remove the electrical wiring.
> - Remove the fuel drain line. Refer to Procedure 006- 021 in Section 6.
> - Remove the throttle and shutoff linkage. See equipment manufacturer service information.
> - Remove tamper-resistant screws using service tool kit, Part Number 3399870. [[41-005-012 — Fuel Injection Pumps, In-Line|Refer to Procedure 005-012 in Section 5.]]
> - Remove the fuel injection pump top cover. Reference the Master Repair Manual, Injector Pumps and Injectors, Bulletin 3666037.
>
> Bosch™ A Pump with RSV Governor
>
> Remove the rod end from the shutoff lever.
>
> Remove the stop screw and bracket assembly.
>
> Remove the shutoff lever (10) over the shutoff shaft on the inboard side of the fuel pump.
>
> Remove the solenoid from the solenoid bracket assembly and solenoid bracket assembly from the fuel pump. If the old 1-3/4 inch solenoid and bracket assembly is being replaced with the new 2-inch solenoid, discard the solenoid mounting capscrews.
>
> Bosch™ P Pump with RQVK Governor
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
> Check the shutoff lever stop lever stop bracket.
>
> The lever **must** make contact with the stop screw on the stop screw bracket. If the lever does **not** touch the stop screw, adjust the stop screw out 1-1/2 turns past the point of contact between the stop screw and the shutoff lever.
>
> Generator Set Applications
>
> Remove the fuel shutoff valve connector.
>
> Remove the fuel shutoff valve, o-ring, lock washer, plain washer and capscrews.
>
> Remove the fuel shutoff valve adapter.
>
> Remove the fuel shutoff valve bracket and capscrews.
>
> ### Clean and Inspect for Reuse
>
> Replace the fuel shutoff valve bracket, connector and adapter, if any crack or damage found.
>
> ### Install
>
> **Note · Примечание**
> Make sure the acorn nut is tightened to be snug on the fuel shutoff solenoid shaft (Synchro-start **only**).
>
> Install the new fuel shutoff solenoid to the bracket, and connect the wires. Make sure the wiring harness one the Trombetta solenoid is installed in the six-o'clock position.
>
> **Момент затяжки · Torque Value**
> 10 n•m [89 in-lb]
>
> 1. Synchro-start
> 2. Trombetta
> 3. Direct link.
>
> Activate the switch and check the plunger travel.
>
> |  | Synchro-start | Trombetta | Direct link |
> |---|---|---|---|
> | A = | 86.8.2 mm \[3.4 in\] | 91.4 mm \[3.6 in\] |  |
> | B = | 60.2 mm \[2.4 in\] | 63.5 mm \[2.5 in\] | 117.1 mm \[4.61 in\] |
>
> The plunger **must** be retracted when the fuel shutoff solenoid is activated to the RUN position B. The fuel shutoff solenoid **must** operate without binding.
>
> Remove the hitch pin clip, the mounting capscrews, and the fuel shutoff solenoid.
>
> Install the new solenoid in reverse order of removal, and connect the wires.
>
> **Момент затяжки · Torque Value**
> 10 n•m [89 in-lb]
>
> Adjust the solenoid linkage as necessary so that the plunger is magnetically held in with the shutoff lever in the absolute full-run position. Turn the large hex nut on the end of the plunger to make adjustments, and secure in place with a locknut.
>
> Bosch™ A Pump with RSV Governor
>
> **CAUTION · Осторожно**
> Failure to observe proper cranking and fuel system priming procedures can cause solenoid malfunction.
>
> **CAUTION · Осторожно**
> New solenoid mounting capscrews must be used if replacing an old 1-3/4-inch solenoid with a 2-inch solenoid. Insufficient thread engagement can cause damage to the pump and the solenoid.
>
> Install the shutoff solenoid on the fuel pump using two new M16 x 1.5-16 capscrews. Apply Loctite® to the capscrew threads. Tighten the capscrews just enough to hold the solenoid in place.
>
> **Note · Примечание**
> New solenoid mounting capscrews have threadlocker pre-applied. Loctite® application is **not** necessary when new capscrews are installed.
>
> Install the shutoff lever (10) over the shutoff shaft on the fuel pump.
>
> Use the capscrew (7) previously removed to hold the shutoff lever in place.
>
> **Момент затяжки · Torque Value**
> 9 n•m [80 in-lb]
>
> Connect the rod end of the solenoid to the shutoff lever.
>
> Tighten the shutoff lever nut.
>
> **Момент затяжки · Torque Value**
> 9 n•m [80 in-lb]
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
> Assemble the stop screw to the stop screw bracket. Adjust the stop screw (3) so the contact surface of the screw protrudes 10 mm \[0.394 in\] beyond the surface of the stop bracket (4).
>
> Tighten the nut (2) against the stop bracket to lock the stop screw in place.
>
> Install the stop bracket assembly using two M6 x 1-16 capscrews (5).
>
> Tighten the capscrews.
>
> **Момент затяжки · Torque Value**
> 7 n•m [62 in-lb]
>
> **CAUTION · Осторожно**
> The solenoid rod length is pre-set. Adjustment of the solenoid rod can cause damage to the solenoid or lead to a low power complaint.
>
> Verify the shutoff lever is contacting the stop screw and is in the full stop position. If the shutoff lever does **not** contact the stop screw, verify the shutoff solenoid and stop screw bracket are assembled correctly. Loosen the solenoid mounting capscrews and readjust the solenoid, if necessary.
>
> Bosch™ P Pump with RQVK Governor
>
> The rod end to control rod orientation is important. If the rod end is installed incorrectly, improper operation of the shutoff solenoid assembly can occur.
>
> Install the locknut (1) onto the new control rod at the rod end until there is 13 mm \[7/16 inch\] between the start of the threads (2) and nut (1).
>
> Install the lock washer.
>
> Screw the rod end onto the control rod, hand-tighten and make certain **not** to move the locknut. Lay the control rod and rod end on a flat surface. Rotate the rod end so both the control rod and the rod end lay flat.
>
> Tighten the locknut onto the rod end.
>
> Install the locknut (2) on the control rod at the solenoid end until there is 6 mm \[1/4 inch\] between start of the threads (1) and locknut (2).
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
> Generator Set Applications
>
> Install the fuel shutoff valve bracket.
>
> **Момент затяжки · Torque Value**
> 43 n•m [32 ft-lb]
>
> Install the fuel shutoff valve adapter.
>
> **Момент затяжки · Torque Value**
> 43 n•m [32 ft-lb]
>
> Install the O-ring to the groove.
>
> Install the fuel shutoff valve, lock washer, plain washer.
>
> Tighten the capscrews.
>
> **Момент затяжки · Torque Value**
> 13 n•m [115 in-lb]
>
> Install the fuel shutoff valve connector.
>
> **Момент затяжки · Torque Value**
> 6 n•m [53 in-lb]
>
> ### Finishing Steps
>
> - Install all components removed, including the fuel filter and fuel supply line, if removed. [[41-006-015-tr — Fuel Filter (Spin-On Type)|Refer to Procedure 006-015]] and [[41-006-024 — Fuel Supply Lines|Refer to Procedure 006-024 in Section 6.]]
> - Connect the wire harness to the fuel shutoff solenoid.
> - Start the engine and check for proper operation.
