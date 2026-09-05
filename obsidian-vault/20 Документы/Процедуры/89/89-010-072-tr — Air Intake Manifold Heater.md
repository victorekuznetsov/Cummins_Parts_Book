---
type: "Процедура"
doc: "89-010-072-tr"
title_en: "Air Intake Manifold Heater"
modified: "2016-11-04"
engines:
  - "85017333"
families:
  - "QSK23"
manuals:
  - "4021375"
figures: 7
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/89/89-010-072-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/89-010-072-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "группа/89"
  - "перевод/машинный"
---

# Air Intake Manifold Heater

> [!abstract] Процедура · `89-010-072-tr`
> **Двигатели:** [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23
> **Входит в руководства:** [[4021375 — QSK23 Troubleshooting and Repair Manual|4021375]]
> **Секции:** Section 10 - Air Intake System - Group 10
> **Даты:** изменён 2016-11-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/89/89-010-072-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/89-010-072-tr.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

> [!danger] ОПАСНО
> Чтобы уменьшить вероятность получения травм и повреждения имущества, никогда не используйте стартовую жидкость, если используется вариант нагревателя сетки. Запуск жидкости, которая содержит эфир, может вызвать взрыв.

Водоприемные воздушные нагреватели управляются модулем управления двигателем (ECM) и используются для нагрева воздуха во время холодных условий запуска.

Мощность аккумулятора для впускных воздушных нагревателей поставляет оригинальный производитель оборудования (OEM). Система имеет общую мощность вывода усилителя около 220 ампер при работе.

> [!note] Примечание
> Для двигателей, работающих в нормальных условиях, сетевой нагреватель предназначен для прочного срока службы двигателя. Для приложений, работающих в холодном климате и имеющих несколько пусков в день, нагреватель сети должен проверяться каждые 6000 часов.

![[10a00121.png]]

Имеется два впускных воздушных нагревателя (1). Они расположены на входе каждого впускного коллектора. Каждый нагреватель имеет свой соленоид. Ссылка на промышленную схему проводов QSK23, Бюллетень 4021394.

Впускные воздушные нагреватели функционируют как резистивный нагреватель. На одном конце прилагается напряжение или усилие, а другой конец привязан к заземлению блока.

Водоприемные нагреватели могут перестать функционировать, если у них неисправная земля, потеря питания батареи, неисправный соленоид или соленоид перестает получать команду ECM.

![[10r00004.png]]

ECM использует температуру воздуха впускного коллектора в качестве входа для определения того, должны ли активироваться нагреватели сетки.

Нагреватели сетки включаются в течение 30 секунд после включения ключа, если температура впускного коллектора ниже 0°C[32°F]. Мощность снимается, если двигатель начинает сворачивать и скорость двигателя превышает 50 оборотов в минуту.

![[10a00123.png]]

### Снятие

Отключите проводку воздухозаборника.

Удалите воздушные кроссоверы.

![[10h00001.png]]

### Очистка и проверка при повторном использовании

Проверить воздухозаборник коллектор нагревателя на предмет повреждения. Если нагреватель показывает признаки трещин или сломан, его необходимо заменить.

![[10d00624.png]]

### Установка

Установите воздушные кроссоверы.

> [!tip] Момент затяжки
> болты (1): 30 Н·м [22 фунт-фут]

> [!tip] Момент затяжки
> Все остальные болты: 66 Н·м [49 фунт-фут]

![[10h00002.png]]

Подключите кран для подогрева воздуха.

![[10a00121.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> **WARNING · Опасно**
> To reduce the possibility of personal injury and property damage, never use starting fluid if the grid heater option is used. Starting fluid, which contains ether, can cause an explosion.
>
> The intake air grid heaters are controlled by the engine control module (ECM), and are used to warm the intake air during cold starting conditions.
>
> The battery power for the intake air grid heaters is supplied by the original equipment manufacturer (OEM). The system has a total amperage draw capacity of approximately 220 amperes when operational.
>
> **Note · Примечание**
> For engines operating in normal conditions, the grid heater is designed to last the life of the engine. For applications which operate in cold climates and have multiple starts per day, the grid heater should be inspected every 6000 hours.
>
> There are two intake air grid heaters (1). They are located at the inlet of each intake manifold. Each grid heater has its own solenoid. Reference the QSK23 Industrial Wiring Diagram, Bulletin 4021394.
>
> The intake air grid heaters function as a resistive heater. On one end a voltage or amperage is applied, and the other end is tied to the block ground.
>
> The intake air grid heaters can stop functioning if they have a faulty ground, loss of battery supply, faulty solenoid, or the solenoid stops receiving the ECM command.
>
> The ECM uses intake manifold air temperature as the input to determine if the grid heaters should be activated.
>
> The grid heaters are turned on for 30 seconds after key ON if the intake manifold temperature is below 0° C \[32° F\]. Power is removed if the engine starts cranking and the engine speed exceeds 50 rpm.
>
> ### Remove
>
> Disconnect air intake heater harness.
>
> Remove the air crossover connections.
>
> ### Clean and Inspect for Reuse
>
> Inspect the air intake manifold heater for damage. If the heater shows signs of cracks or is broken, it **must** be replaced.
>
> ### Install
>
> Install the air crossover connections.
>
> **Момент затяжки · Torque Value**
> Capscrew (1): 30 n•m [22 ft-lb]
>
> **Момент затяжки · Torque Value**
> All Other Capscrews: 66 n•m [49 ft-lb]
>
> Connect the air intake heater harness.
