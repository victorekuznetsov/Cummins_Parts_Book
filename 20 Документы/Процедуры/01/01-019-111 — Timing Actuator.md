---
aliases:
  - "Исполнительный механизм опережения впрыска"
type: "Процедура"
doc: "01-019-111"
title_en: "Timing Actuator"
title_ru: "Исполнительный механизм опережения впрыска"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-111.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-111.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Timing Actuator
**Исполнительный механизм опережения впрыска**

> [!abstract] Процедура · `01-019-111`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2004-07-16
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-111.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-111.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

QSX15

Приводы синхронизации расположены на двигателе перед ECM. Их две штуки. Передний привод синхронизации расположен на корпусе подачи топлива. Это второй привод с передней части двигателя.

Задний привод синхронизации расположен на корпусе подачи топлива. Это второй привод сзади двигателя.

![[05c00001.png]]

QSK23, QSK45, QSK60 и QSK78

Рельсовые приводы синхронизации являются частью корпуса управляющего клапана.

![[19400301.png]]

### Проверка

> [!note] Примечание
> Эта процедура испытаний используется только для двигателей серии QSX15.

Выполните электронный сервисный тест на производительность цилиндра INSITETM, чтобы определить, не вышел ли из строя привод. Если банк терпит неудачу, это может указывать на сбой привода.

Если в банке не сработали только два топливных форсунка, повторите тест. Переключите передний и задний приводы заправки, чтобы определить, следует ли за приводом неисправный ряд цилиндров. Если это так, то необходимо заменить неисправный привод заправки.

Если **не**, поменяйте передний и задний приводы синхронизации, чтобы определить, следует ли за приводом неисправный берег цилиндров. Если это так, то заменяйте неисправный привод синхронизации по мере необходимости.

![[19800902.png]]

### Снятие

QSX15

Очистите область вокруг привода синхронизации.

Отсоедините разъем привода синхронизации от жгута проводов двигателя.

![[19802663.png]]

Удалите три болта, обеспечивающие привод синхронизации.

![[19802663.png]]

QSK23, QSK45, QSK60 и QSK78

Очистите область вокруг привода синхронизации.

Отсоедините разъемы привода синхронизации от ремня электропроводки двигателя.

> [!note] Примечание
> Рельсовые приводы синхронизации являются частью корпуса управляющего клапана.

![[19400300.png]]

Удалите привод синхронизации.

![[19400301.png]]

### Установка

QSX15

Установите новые кольца. Нанесите смазку на канавку с кольцевым покрытием, чтобы сохранить кольцевое отверстие во время установки.

Установите новый привод времени.

> [!tip] Момент затяжки
> 5.4 Н·м [48 фунт-дюйм]

Подключите жгут электропроводки двигателя к приводу синхронизации.

Запустите двигатель и проверьте наличие утечек.

![[19802663.png]]

QSK23, QSK45, QSK60 и QSK78

Осмотрите новое кольцо.

Установите новый привод рельсов времени.

> [!tip] Момент затяжки
> 25 Н·м [18 фунт-фут]

Подключите жгут электропроводки двигателя к приводу рельсов синхронизации.

Запустите двигатель и проверьте наличие утечек.

![[19400302.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> QSX15
>
> The timing actuators are located on the engine in front of the ECM. There are two of them. The front timing actuator is located on the fuel delivery housing. It is the second actuator from the front of the engine.
>
> The rear timing actuator is located on the fuel delivery housing. It is the second actuator from the rear of the engine.
>
> QSK23, QSK45, QSK60, and QSK78
>
> The timing rail actuators are part of the control valve body.
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
> Clean the area around the timing actuator.
>
> Disconnect the timing actuator connector from the engine harness.
>
> Remove the three capscrews securing the timing actuator.
>
> QSK23, QSK45, QSK60, and QSK78
>
> Clean the area around the timing actuator.
>
> Disconnect the timing actuator connectors from the engine harness.
>
> **Note · Примечание**
> The timing rail actuators are part of the control valve body.
>
> Remove the timing actuator.
>
> ### Install
>
> QSX15
>
> Install new o-rings. Apply grease to the o-ring groove to retain the o-ring during installation.
>
> Install a new timing actuator.
>
> **Момент затяжки · Torque Value**
> 5.4 n•m [48 in-lb]
>
> Connect the engine harness to the timing actuator.
>
> Start the engine and check for leaks.
>
> QSK23, QSK45, QSK60, and QSK78
>
> Inspect the new o-ring.
>
> Install a new timing rail actuator.
>
> **Момент затяжки · Torque Value**
> 25 n•m [18 ft-lb]
>
> Connect the engine harness to the timing rail actuator.
>
> Start the engine and check for leaks.
