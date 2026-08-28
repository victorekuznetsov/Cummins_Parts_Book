---
type: "Процедура"
doc: "1016-019-103"
title_en: "Wastegate Control Valve"
modified: "2024-04-03"
engines:
  - "77804810"
families:
  - "15N"
manuals:
  - "5659763"
figures: 8
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/1016/1016-019-103.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/1016-019-103.pdf"
tags:
  - "документ/процедура"
  - "двигатель/15N"
  - "перевод/машинный"
---

# Wastegate Control Valve

> [!abstract] Процедура · `1016-019-103`
> **Двигатели:** [[77804810 — 15N CM2380 M104B CPL 5977|77804810]]
> **Семейство:** 15N
> **Входит в руководства:** [[5659763 — 15N CM2380 M104B Service Manual|5659763]]
> **Секции:** Section 19 - Electronic Controls - Group 19
> **Даты:** изменён 2024-04-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/1016/1016-019-103.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/1016-019-103.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Выбор сервисного инструмента

#### Рекомендованный сервисный инструмент Cummins®

- Не требуется никаких рекомендуемых инструментов обслуживания Cummins®

#### Дополнительные сервисные позиции

- Никаких дополнительных предметов обслуживания не требуется.

### Общие сведения

Положение обходного клапана турбонаддувной турбины и давление наддува контролируются клапаном управления обходным клапаном турбины (1).

В положении по умолчанию клапан управления обходным клапаном турбины направляет полное давление на усилитель обходного клапана турбины.

![[19s00246.png]]

### Подготовительные операции

- Отсоедините привод турбокомпрессора от линии сжатого воздуха. См. процедуру 010-118 в разделе 10.

### Снятие

Отсоедините разъём ремня электропроводки двигателя от клапана управления обходным клапаном турбины.

Удалите два болта, соединяющие клапан управления обходным клапаном турбины с кронштейном.

Удалите два болта, соединяющие кронштейн клапана управления обходным клапаном турбины с впускным коллектором.

![[19s00247.png]]

Удалите и отбросьте шланг, соединяющий клапан управления обходным клапаном турбины с шлангом, если это необходимо.

![[19s00248.png]]

### Проверка при повторном использовании

Проверить клапан управления обходным клапаном турбины на наличие изогнутых или сломанных штифтов или поврежденных соединений.

Проверить кронштейн клапана управления обходным клапаном турбины на наличие трещин или других повреждений.

Заменить клапан управления обходным клапаном турбины или кронштейн, если обнаружено повреждение.

![[19s00249.png]]

Проверьте все шланги на наличие трещин, порезов или других повреждений, которые могут вызвать утечку.

Замените шланг, если обнаружен ущерб.

![[19s00250.png]]

### Проверка

Измерьте сопротивление между сигналом и обратными штифтами на разъёме клапана управления обходным клапаном турбины.

| турбинный шунтирующий клапан Control клапан Body Temperature | Сопротивление (Омс) |  |  |
|---|---|---|---|
| °C | градус | Мин | Макс |
| -40 | -40 | 65.5 | 72.4 |
| -35 | -31 | 67.2 | 74.2 |
| -30 | -22 | 68.8 | 76.1 |
| -25 | -13 | 70.5 | 77.9 |
| -20 | -4 | 72.2 | 79.8 |
| -15 | 5 | 73.8 | 81.6 |
| -10 | 14 | 75.5 | 83.4 |
| -5 | 23 | 77.2 | 85.3 |
| 0 | 32 | 78.8 | 87.1 |
| 5 | 41 | 80.5 | 89.0 |
| 10 | 50 | 82.2 | 90.8 |
| 15 | 59 | 83.8 | 92.7 |
| 20 | 68 | 85.5 | 94.5 |
| 25 | 77 | 87.2 | 96.3 |
| 30 | 86 | 88.8 | 98.2 |
| 35 | 95 | 90.5 | 100.0 |
| 40 | 104 | 92.2 | 101.9 |
| 45 | 113 | 93.8 | 103.7 |
| 50 | 122 | 95.5 | 105.6 |
| 55 | 131 | 97.2 | 107.4 |
| 60 | 140 | 98.8 | 109.2 |
| 65 | 149 | 100.5 | 111.1 |
| 70 | 158 | 102.2 | 112.9 |
| 75 | 167 | 103.8 | 114.8 |
| 80 | 176 | 105.5 | 116.6 |

Измерить сопротивление между сигнальным контактом и корпусом клапана управления обходным клапаном турбины.

Минимальное сопротивление: 100 тысяч Ом.

Если сопротивление не соответствует спецификациям, замените клапан управления обходным клапаном турбины.

![[3377161.png]]

### Установка

Установите новый шланг, соединяющий клапан управления обходным клапаном турбины с шлангом, если он удален.

![[19s00248.png]]

Установите два болта, соединяющие кронштейн клапана управления обходным клапаном турбины с впускным коллектором.

> [!tip] Момент затяжки
> 5 Н·м [44 фунт-дюйм]

Затянуть два болта, соединяющие клапан управления обходным клапаном турбины с кронштейном.

> [!tip] Момент затяжки
> 5 Н·м [44 фунт-дюйм]

Подключите к клапану разъём ремня электропроводки двигателя.

![[19s00247.png]]

### Завершающие операции

- Подключите привод турбокомпрессора к линии сжатого воздуха. См. процедуру 010-118 в разделе 10.


> [!quote]- Original (English) · английский оригинал
> ### Select Service Tools
>
> #### Recommended Cummins® Service Tools
>
> - No recommended Cummins® service tools required
>
> #### Additional Service Items
>
> - No additional service items required.
>
> ### General Information
>
> The turbocharger wastegate position and boost pressure are controlled by the wastegate control valve (1).
>
> In default position, the wastegate control valve directs full boost pressure to the wastegate actuator.
>
> ### Preparatory Steps
>
> - Disconnect the turbocharger actuator air line. Refer to Procedure 010-118 in Section 10.
>
> ### Remove
>
> Disconnect the engine harness connector from the wastegate control valve.
>
> Remove the two capscrews connecting wastegate control valve to the bracket.
>
> Remove the two capscrews connecting wastegate control valve bracket to the intake manifold.
>
> Remove and discard the hose clamp connecting wastegate control valve to hose if required.
>
> ### Inspect for Reuse
>
> Inspect the wastegate control valve for bent or broken pins or damaged connections.
>
> Inspect the wastegate control valve bracket for cracks or other damage.
>
> Replace the wastegate control valve or bracket if damage is found.
>
> Inspect all hoses for cracks, cuts, or other damage that can cause leaks.
>
> Replace hose if damage is found.
>
> ### Test
>
> Measure the resistance between the signal and return pins at the wastegate control valve connector.
>
> | Wastegate Control Valve Body Temperature | Resistance (Ohms) |  |  |
> |---|---|---|---|
> | °C | °F | MIN | MAX |
> | -40 | -40 | 65.5 | 72.4 |
> | -35 | -31 | 67.2 | 74.2 |
> | -30 | -22 | 68.8 | 76.1 |
> | -25 | -13 | 70.5 | 77.9 |
> | -20 | -4 | 72.2 | 79.8 |
> | -15 | 5 | 73.8 | 81.6 |
> | -10 | 14 | 75.5 | 83.4 |
> | -5 | 23 | 77.2 | 85.3 |
> | 0 | 32 | 78.8 | 87.1 |
> | 5 | 41 | 80.5 | 89.0 |
> | 10 | 50 | 82.2 | 90.8 |
> | 15 | 59 | 83.8 | 92.7 |
> | 20 | 68 | 85.5 | 94.5 |
> | 25 | 77 | 87.2 | 96.3 |
> | 30 | 86 | 88.8 | 98.2 |
> | 35 | 95 | 90.5 | 100.0 |
> | 40 | 104 | 92.2 | 101.9 |
> | 45 | 113 | 93.8 | 103.7 |
> | 50 | 122 | 95.5 | 105.6 |
> | 55 | 131 | 97.2 | 107.4 |
> | 60 | 140 | 98.8 | 109.2 |
> | 65 | 149 | 100.5 | 111.1 |
> | 70 | 158 | 102.2 | 112.9 |
> | 75 | 167 | 103.8 | 114.8 |
> | 80 | 176 | 105.5 | 116.6 |
>
> Measure the resistance between the signal pin and wastegate control valve body.
>
> Minimum resistance: 100k ohms.
>
> If the resistance does **not** meet the specifications, replace the wastegate control valve.
>
> ### Install
>
> Install new hose clamp connecting wastegate control valve to hose if removed.
>
> Install the two capscrews connecting wastegate control valve bracket to the intake manifold.
>
> **Момент затяжки · Torque Value**
> 5 n•m [44 in-lb]
>
> Tighten the two capscrews connecting wastegate control valve to the bracket.
>
> **Момент затяжки · Torque Value**
> 5 n•m [44 in-lb]
>
> Connect the engine harness connector to the valve.
>
> ### Finishing Steps
>
> - Connect the turbocharger actuator air line. Refer to Procedure 010-118 in Section 10.
