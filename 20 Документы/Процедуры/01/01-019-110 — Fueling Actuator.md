---
aliases:
  - "Исполнительный механизм подачи топлива"
type: "Процедура"
doc: "01-019-110"
title_en: "Fueling Actuator"
title_ru: "Исполнительный механизм подачи топлива"
modified: "2004-07-16"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 9
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-110.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-110.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Fueling Actuator
**Исполнительный механизм подачи топлива**

> [!abstract] Процедура · `01-019-110`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2004-07-16
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-110.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-110.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Заправочные приводы контролируют подачу топлива в двигатель.

На топливной системе QSX15 приводы заправки являются частью корпуса подачи топлива, расположенного на левой стороне двигателя перед электронным модулем управления (ECM). Имеется два привода заправки, один передний и один задний.

Передний привод для заправки топлива управляет передними тремя цилиндрами, а задний привод для топлива управляет задними тремя цилиндрами.

![[05c00001.png]]

На топливных системах QSK23, QSK45, QSK60 и QSK78 привод топливной рельсы является частью корпуса управляющего клапана.

![[19400369.png]]

### Проверка

> [!note] Примечание
> Эта процедура испытаний используется только для двигателей серии QSX15.

Выполните электронный сервисный тест на производительность цилиндра INSITETM, чтобы определить, не вышел ли из строя привод. Если банк терпит неудачу, это может указывать на сбой привода.

Если в банке не сработали только два топливных форсунка, повторите тест. Переключите передний и задний приводы заправки, чтобы определить, следует ли за приводом неисправный банк цилиндров. Если это так, то необходимо заменить неисправный привод заправки.

Если **не**, поменяйте передний и задний приводы синхронизации, чтобы определить, следует ли за приводом неисправный берег цилиндров. Если это так, то заменяйте неисправный привод синхронизации по мере необходимости.

![[19800902.png]]

### Снятие

QSX15

Очистите область вокруг топливного привода.

Отсоедините разъем заправочного привода от жгута проводов двигателя.

![[19802669.png]]

Удалите три болта, обеспечивающие заправочный привод.

![[19802669.png]]

QSK23, QSK45, QSK60 и QSK78

Очистите область вокруг привода.

Отсоедините разъем привода от жгута проводов двигателя.

![[19400368.png]]

Удалите привод с помощью герметичной и 1-1⁄4-дюймовой фланцевой розетки, номер детали 3823843.

![[19400369.png]]

### Установка

QSX15

Установите новое уплотнительное кольцо. Нанесите смазку на канавку с кольцевым покрытием, чтобы сохранить кольцевое отверстие во время установки.

Установите новый привод для заправки.

> [!tip] Момент затяжки
> 5.4 Н·м [48 фунт-дюйм]

Подключите жгут электропроводки двигателя к приводу заправки.

Запустите двигатель и проверьте наличие утечек.

![[19802669.png]]

QSK23, QSK45, QSK60 и QSK78

Осмотрите новый привод для колец.

Установите новый привод.

> [!tip] Момент затяжки
> 25 Н·м [221 фунт-дюйм]

Подключите жгут электропроводки двигателя к приводу.

Запустите двигатель и проверьте наличие утечек.

> [!missing]- Иллюстрация `19400370.png` не извлечена — смотрите PDF-оригинал документа


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The fueling actuators control the delivery of fuel to the engine.
>
> On the QSX15 fuel system, the fueling actuators are a part of the fuel delivery housing, located on the left side of the engine in front of the Electronic Control Module (ECM). There are two fueling actuators, one front and one rear.
>
> The front fueling actuator controls the front three cylinders and the rear fuel actuator controls the rear three cylinders.
>
> On the QSK23, QSK45, QSK60, and QSK78 fuel system the fuel rail actuator is part of the control valve body.
>
> ### Test
>
> **Note · Примечание**
> This test procedure is used **only** for QSX15 series engines.
>
> Perform the INSITE™ electronic service tool cylinder performance test to determine if an actuator has failed. If a bank fails, this could indicate an actuator failure.
>
> If **only** two injectors in a bank fail, repeat the test. Swap the front and rear fueling actuators to determine if the failed bank of cylinders follows the actuator. If so, replace the failed fueling actuator as necessary.
>
> If **not**, swap the front and rear timing actuator to determine if the failed bank of cylinders follows the actuator. If so, replace failed timing actuator as necessary.
>
> ### Remove
>
> QSX15
>
> Clean the area around the fueling actuator.
>
> Disconnect the fueling actuator connector from the engine harness.
>
> Remove the three capscrews securing the fueling actuator.
>
> QSK23, QSK45, QSK60, and QSK78
>
> Clean the area around the actuator.
>
> Disconnect the actuator connector from the engine harness.
>
> Remove the actuator with a ratchet and 1-¼-inch-deep flange drive socket, Part Number 3823843.
>
> ### Install
>
> QSX15
>
> Install a new o-ring. Apply grease to the o-ring groove to retain the o-ring during installation.
>
> Install a new fueling actuator.
>
> **Момент затяжки · Torque Value**
> 5.4 n•m [48 in-lb]
>
> Connect the engine harness to the fueling actuator.
>
> Start the engine and check for leaks.
>
> QSK23, QSK45, QSK60, and QSK78
>
> Inspect the new actuator for o-rings.
>
> Install a new actuator.
>
> **Момент затяжки · Torque Value**
> 25 n•m [221 in-lb]
>
> Connect the engine harness to the actuator.
>
> Start the engine and check for leaks.
