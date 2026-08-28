---
aliases:
  - "Датчик частоты вращения двигателя (ESS)"
type: "Процедура"
doc: "94-019-042"
title_en: "Engine Speed Sensor (ESS)"
title_ru: "Датчик частоты вращения двигателя (ESS)"
modified: "2003-03-24"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666184"
figures: 8
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-019-042.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/94-019-042.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/94"
  - "перевод/машинный"
---

# Engine Speed Sensor (ESS)
**Датчик частоты вращения двигателя (ESS)**

> [!abstract] Процедура · `94-019-042`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-03-24
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-019-042.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/94-019-042.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Снятие

Отсоедините разъем датчика скорости двигателя (ESS) от электропроводки двигателя.

Ослабьте локон.

Выключите ESS из корпуса маховика.

![[19a00045.png]]

### Установка

Убедитесь, что зубчатая передача выровнена с отверстием в корпусе маховика.

Установите ESS в отверстие, пока он не коснется зуба зубчатой передачи.

> [!note] Примечание
> Если ESS **не** включается с давлением пальца, проверьте резьбу резьбы корпуса маховика и резьбу датчика на предмет повреждения.

![[19400431.png]]

Выверните ESS от 1⁄2 до 3⁄4 поворота **против часовой стрелки**.

![[19a00046.png]]

Затяните локон против корпуса маховика.

> [!tip] Момент затяжки
> 34-47 Н·м [25-35 футов-lb]

> [!note] Примечание
> Чрезмерное затягивание локона может повредить датчик.

Установите разъем. Убедитесь, что он запирается на месте.

![[19a00047.png]]

### Проверка сопротивления

Удалите разъём ремня электропроводки двигателя из ESS.

Поместите выключатель Stop/Run в положение STOP.

Контроллер **не** в диагностическом режиме.

Измерьте сопротивление от контакта А до контакта В первой катушки ESS. Мультиметр **должен** показывать сопротивление менее 1500 Ом.

Если сопротивление не менее 1500 Ом, замените ESS. См. процедуру[[94-019-042 — Engine Speed Sensor (ESS)|019-042]].

![[19a00002.png]]

Измерьте сопротивление от контакта А до контакта В второй катушки ESS. Мультиметр **должен** показывать сопротивление менее 1500 Ом.

Если сопротивление не менее 1500 Ом, замените ESS. См. процедуру[[94-019-042 — Engine Speed Sensor (ESS)|019-042]].

![[19a00002.png]]

### Проверка на замыкание на массу

Используйте измерительный щуп, номер детали. 3823996, для разъема Weather-Pack.

Измерьте сопротивление от контакта А разъема ESS к блоку двигателя. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема не открыта, замените ESS. См. процедуру[[94-019-042 — Engine Speed Sensor (ESS)|019-042]].

![[19a00003.png]]

Измерьте сопротивление от контакта B разъема ESS к блоку двигателя. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема не открыта, замените ESS. См. процедуру[[94-019-042 — Engine Speed Sensor (ESS)|019-042]].

![[19a00003.png]]


> [!quote]- Original (English) · английский оригинал
> ### Remove
>
> Disconnect the engine speed sensor (ESS) connector from the engine harness.
>
> Loosen the locknut.
>
> Turn the ESS out of the flywheel housing.
>
> ### Install
>
> Make sure a gear tooth is aligned with the hole in the flywheel housing.
>
> Install the ESS into the hole until it touches the gear tooth.
>
> **Note · Примечание**
> If the ESS does **not** turn in with finger pressure, check the flywheel housing hole threads and sensor threads for damage.
>
> Turn the ESS out ½ to ¾ turn **counterclockwise**.
>
> Tighten the locknut against the flywheel housing.
>
> **Момент затяжки · Torque Value**
> 34 to 47 n•m [25 to 35 ft-lb]
>
> **Note · Примечание**
> Over-tightening the locknut can damage the sensor.
>
> Install the connector. Make sure it locks into place.
>
> ### Resistance Check
>
> Remove the engine harness connector from the ESS.
>
> Place the Stop/Run switch in the STOP position.
>
> Controller **not** in diagnostic mode.
>
> Measure the resistance from pin A to pin B of the first ESS coil. The multimeter **must** show a resistance of less than 1500 ohms.
>
> If the resistance is **not** less than 1500 ohms, replace the ESS. Refer to Procedure [[94-019-042 — Engine Speed Sensor (ESS)|019-042]].
>
> Measure the resistance from pin A to pin B of the second ESS coil. The multimeter **must** show a resistance of less than 1500 ohms.
>
> If the resistance is **not** less than 1500 ohms, replace the ESS. Refer to Procedure [[94-019-042 — Engine Speed Sensor (ESS)|019-042]].
>
> ### Check for Short Circuit to Ground
>
> Use test lead, Part No. 3823996, for the Weather-Pack connector.
>
> Measure the resistance from pin A of the ESS connector to the engine block. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, replace the ESS. Refer to Procedure [[94-019-042 — Engine Speed Sensor (ESS)|019-042]].
>
> Measure the resistance from pin B of the ESS connector to the engine block. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, replace the ESS. Refer to Procedure [[94-019-042 — Engine Speed Sensor (ESS)|019-042]].
