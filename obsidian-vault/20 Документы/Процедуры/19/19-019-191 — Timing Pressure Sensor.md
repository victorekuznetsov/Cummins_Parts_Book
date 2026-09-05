---
aliases:
  - "Датчик давления опережения впрыска"
type: "Процедура"
doc: "19-019-191"
title_en: "Timing Pressure Sensor"
title_ru: "Датчик давления опережения впрыска"
modified: "2002-09-27"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 7
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-191.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-191.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Timing Pressure Sensor
**Датчик давления опережения впрыска**

> [!abstract] Процедура · `19-019-191`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2002-09-27
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-191.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-191.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Первичная проверка

Подключите электронный инструмент к шине данных CAN транспортного средства.

![[19400357.png]]

Переведите замок зажигания в положение ON.

Мониторинг давления с помощью электронного инструментария обслуживания.

Давление должно быть нулевым psi.

![[19800978.png]]

Запустите двигатель и запускайте его на холостом ходу.

Мониторинг давления с помощью электронного инструментария обслуживания.

Давление в синхронизации должно составлять 60 psi.

![[19800979.png]]

### Снятие

Удалить ECM. См. процедуру 019-031.

Очистите корпус управляющего клапана вокруг датчика давления.

Отсоедините разъем датчика от жгута проводов двигателя.

![[19400306.png]]

Удалите датчик давления с помощью 1 1/4-дюймовой фланговой розетки, части 3823843 и скобы.

![[19400307.png]]

### Установка

Осмотрите новый датчик на наличие кольца.

Установите новый датчик давления и затяните.

> [!tip] Момент затяжки
> 14 Н·м [124 фунт-дюйм]

Подключите сенсорное соединение.

![[19400308.png]]

Установите ECM. См. процедуру 019-031.

![[19400295.png]]


> [!quote]- Original (English) · английский оригинал
> ### Initial Check
>
> Connect an electronic service tool to the vehicle datalink.
>
> Turn the keyswitch to the ON position.
>
> Monitor the timing pressure with the electronic service tool.
>
> Timing pressure should be zero psi.
>
> Start the engine and let it idle.
>
> Monitor the timing pressure with the electronic service tool.
>
> The timing pressure should be 60 psi.
>
> ### Remove
>
> Remove the ECM. Refer to Procedure 019-031.
>
> Clean the control valve body around the pressure sensor.
>
> Disconnect the sensor connector from the engine harness.
>
> Remove the pressure sensor with a 1 1/4-inch deep flank drive socket, Part Number 3823843, and a ratchet.
>
> ### Install
>
> Inspect the new sensor for an o-ring.
>
> Install the new pressure sensor and tighten.
>
> **Момент затяжки · Torque Value**
> 14 n•m [124 in-lb]
>
> Connect the sensor connection.
>
> Install the ECM. Refer to Procedure 019-031.
