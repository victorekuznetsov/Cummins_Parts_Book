---
aliases:
  - "Жгут управления генератором"
type: "Процедура"
doc: "01-019-183"
title_en: "Generator Control Harness"
title_ru: "Жгут управления генератором"
modified: "2004-04-06"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 25
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-183.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-183.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Generator Control Harness
**Жгут управления генератором**

> [!abstract] Процедура · `01-019-183`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2004-04-06
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-183.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-183.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Двигатели с системой управления генераторным приводом будут иметь несколько электропроводных ремней.

![[17600025.png]]

Усилитель управления генератором подается OEM и подключается к разъемам 03 и 06 модуля системы управления генератором-приводом.

> [!note] Примечание
> Следующие шаги предназначены для общей проводов ремня управления генератором. См. руководство OEM для более конкретных инструкций.

![[19400386.png]]

### Снятие

Отсоедините электропроводку управления генератором от батареи.

![[19802564.png]]

Отсоедините электропроводку управления генератором от переключателей.

1. аварийная остановка
2. Дистанционный аварийный выключатель
3. Переключатель Run/Stop
4. Переключатель аварийной сигнализации

![[19802565.png]]

1. Регулярный/рейтинговый переключатель
2. Диагностический переключатель режима
3. Переключатель переменной частоты
4. Крэнк-переключатель.

![[19802565.png]]

Отсоедините электропроводку управления генератором от потенциометра.

1. Потенциометр с регулировкой петли
2. Частотный регулировочный потенциометр.

![[19802566.png]]

Отсоедините электропроводку управления генератором от счетчиков.

1. Скорость двигателя метр
2. Счетчик давления масла
3. Измеритель температуры охлаждающей жидкости.

![[19802568.png]]

Отсоедините электропроводку управления генератором от ламп.

1. Общее предупреждение
2. Общее закрытие
3. Высокая температура двигателя
4. Низкое давление масла
5. сверхскоростной
6. высокая температура двигателя
7. Превышать давление масла
8. Не удалось начать.

![[19802567.png]]

Отсоедините электропроводку управления генератором от интерфейса RS-485 (при наличии оборудования).

![[19400417.png]]

Отсоедините электропроводку управления генератором от губернатора Вудворда или Барбера-Колмана (если она оборудована).

![[19400412.png]]

Отсоедините ремень управления генератором от коленчатой катушки.

![[19802646.png]]

Отключите электропроводку управления генератором от Back-up Start Disconnect.

![[19802565.png]]

Отсоедините разъемы 03 и 06 электропроводки управления генератором от ECM.

Удалите все проводов, поддерживающие ремни.

Дважды проверьте, что все проводные соединения жгутов проводов отключены и не запутанны.

Медленно оттяните проводку от генератора, убедившись, что нет связывания или запутывания.

![[19802555.png]]

### Установка

Поместите ремень управления генератором на генератор.

Пристегните ремень управления генератором к генератору на опорах ремня электропроводки.

> [!note] Примечание
> Следующие шаги предназначены для общей проводов ремня управления генератором. См. руководство OEM для конкретных инструкций.

Подключите к ECM разъёмы 03 и 06 управляющей проводов генератора.

![[19802555.png]]

Подключите резервный пуск Отключите к электропроводке управления генератором.

![[19802565.png]]

Подключите коленчатую катушку к электропроводке управления генератором.

![[19802646.png]]

Подключите управляющего Вудворда или Барбера-Колмана (если он оборудован) к электропроводке генератора.

![[19400412.png]]

Подключите интерфейс RS-485 (при его оснащении) к электропроводке генератора.

![[19400417.png]]

Подключите лампы к электропроводке управления генератором.

1. Общее предупреждение
2. Общее закрытие
3. Высокая температура двигателя
4. Низкое давление масла
5. сверхскоростной
6. высокая температура двигателя
7. Превышать давление масла
8. Не удалось начать.

![[19802567.png]]

Подключите счетчики к электропроводке управления генератором.

1. Скорость двигателя метр
2. Счетчик давления масла
3. Измеритель температуры охлаждающей жидкости.

![[19802568.png]]

Подключите потенциометры к электропроводке управления генератором.

1. Потенциометр с регулировкой петли
2. Частотный регулировочный потенциометр.

![[19802566.png]]

Подключите переключатели к электропроводке управления генератором.

1. Кран-переключатель
2. Переключатель переменной частоты
3. Диагностический переключатель режима
4. Регулярный/рейтинговый переключатель

![[19802565.png]]

1. Переключатель аварийной сигнализации
2. Переключатель Run/Stop
3. Дистанционный аварийный выключатель
4. Выключатель аварийной остановки.

![[19802565.png]]

Подключите аккумулятор к электропроводке управления генератором.

![[19802564.png]]

Дважды проверьте, что все проводные соединения с жгутом безопасны.

Подключите инструмент электронного сервиса и проверьте наличие кодов неисправностей.

![[19800902.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The generator-drive control system-equipped engines will have multiple harnesses.
>
> The generator control harness is supplied by the OEM, and is wired to the generator-drive control system module connectors 03 and 06.
>
> **Note · Примечание**
> The following steps are for a generic wiring of the generator control harness. Refer to the OEM manual for more specific instructions.
>
> ### Remove
>
> Disconnect the generator control harness from the battery.
>
> Disconnect the generator control harness from the switches.
>
> 1. Emergency stop switch
> 2. Remote emergency stop switch
> 3. Run/stop switch
> 4. Alarm reset switch
>
> 1. Idle/rated switch
> 2. Diagnostic mode switch
> 3. Alternate frequency switch
> 4. Crank switch.
>
> Disconnect the generator control harness from the potentiometers.
>
> 1. Droop adjust potentiometer
> 2. Frequency adjust potentiometer.
>
> Disconnect the generator control harness from the meters.
>
> 1. Engine speed meter
> 2. Oil pressure meter
> 3. Coolant temperature meter.
>
> Disconnect the generator control harness from the lamps.
>
> 1. Common warning
> 2. Common shutdown
> 3. High engine temperature
> 4. Low oil pressure
> 5. Overspeed
> 6. Prehigh engine temperature
> 7. Prelow oil pressure
> 8. Fail to start.
>
> Disconnect the generator control harness from the RS-485 interface (if equipped).
>
> Disconnect the generator control harness from the Woodward or Barber-Colman governor (if equipped).
>
> Disconnect the generator control harness from the crank coil.
>
> Disconnect the generator control harness from the Back-up Start Disconnect.
>
> Disconnect the generator control harness connectors 03 and 06 from the ECM.
>
> Remove any harness supports.
>
> Double-check that all harness connections are disconnected and untangled.
>
> Slowly pull the harness away from the generator, making sure that there is no binding or tangling.
>
> ### Install
>
> Place the generator control harness on the generator.
>
> Fasten the generator control harness to the generator at the harness supports.
>
> **Note · Примечание**
> The following steps are for a generic wiring of the generator control harness. Refer to the OEM manual for specific instructions.
>
> Connect the generator control harness connectors 03 and 06 to the ECM.
>
> Connect the Back-up Start Disconnect to the generator control harness.
>
> Connect the crank coil to the generator control harness.
>
> Connect the Woodward or Barber-Colman governor (if equipped) to the generator control harness.
>
> Connect the RS-485 interface (if equipped) to the generator control harness.
>
> Connect the lamps to the generator control harness.
>
> 1. Common warning
> 2. Common shutdown
> 3. High engine temperature
> 4. Low oil pressure
> 5. Overspeed
> 6. Prehigh engine temperature
> 7. Prelow oil pressure
> 8. Fail to start.
>
> Connect the meters to the generator control harness.
>
> 1. Engine speed meter
> 2. Oil pressure meter
> 3. Coolant temperature meter.
>
> Connect the potentiometers to the generator control harness.
>
> 1. Droop adjust potentiometer
> 2. Frequency adjust potentiometer.
>
> Connect the switches to the generator control harness.
>
> 1. Crank switch
> 2. Alternate frequency switch
> 3. Diagnostic mode switch
> 4. Idle/rated switch
>
> 1. Alarm reset switch
> 2. Run/stop switch
> 3. Remote emergency stop switch
> 4. Emergency stop switch.
>
> Connect the battery to the generator control harness.
>
> Double-check that all harness connections are secure.
>
> Connect the electronic service tool and check for any fault codes.
