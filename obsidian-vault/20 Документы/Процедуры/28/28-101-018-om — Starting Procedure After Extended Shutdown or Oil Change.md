---
aliases:
  - "Порядок пуска после длительной стоянки или замены масла"
type: "Процедура"
doc: "28-101-018-om"
title_en: "Starting Procedure After Extended Shutdown or Oil Change"
title_ru: "Порядок пуска после длительной стоянки или замены масла"
modified: "2008-10-20"
engines:
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50"
manuals:
  - "3667180"
  - "3810497"
figures: 3
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/28/28-101-018-om.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/28-101-018-om.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/28"
  - "перевод/машинный"
---

# Starting Procedure After Extended Shutdown or Oil Change
**Порядок пуска после длительной стоянки или замены масла**

> [!abstract] Процедура · `28-101-018-om`
> **Двигатели:** [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50
> **Входит в руководства:** [[3667180 — K38, K50, QSK38 and QSK50 Owners Manual|3667180]], [[3810497 — K38, K50, QSK38 and QSK50 Operation and Maintenance Manual|3810497]]
> **Секции:** Section 1 - Operating Instructions
> **Даты:** изменён 2008-10-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/28/28-101-018-om.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/28-101-018-om.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

> [!warning] ОСТОРОЖНО
> Не позволяйте двигателю исчерпать топливо. Потеря подачи топлива может привести к повреждению топливного насоса и форсунки.

Механически приводимый в действие форсунка

> [!note] Примечание
> Двигатели, оснащенные системой PrelubTM, являются самозагружающимися и не требуют следующей процедуры.

Выполните следующие действия после каждого изменения масла или после того, как двигатель был отключен более 5 дней, чтобы убедиться, что двигатель получает правильный поток масла через систему моторного масла.

1. Отсоедините электрический провод от соленоидного клапана топливного насоса.
2. Используйте пусковой двигатель для вращения коленчатого вала до тех пор, пока давление масла не будет указано на измерительном приборе или предупредительная лампа не погаснет.
3. Подключите электрический провод к соленоидному клапану топливного насоса. См. процедуру 018-006 (значения крутящего момента в компоненте двигателя) в разделе V.
4. Запуск двигателя; обратитесь к процедуре 101-014 (Обычная процедура запуска) в разделе 1.

![[19802010.png]]

Электронный форсунка

> [!note] Примечание
> Эта процедура приведет к регистрации кодов неисправностей для незаблокированных датчиков. Они будут неактивны и не будут влиять на работу двигателя после подключения датчиков.

> [!note] Примечание
> Двигатели, оснащенные системой PrelubTM, самостоятельно заряжаются для системы смазки и будут использовать следующую процедуру для заправки только топливной системы двигателя.

- Отключите датчик скорости двигателя и датчик положения распределительного вала. Двигатели с механическим топливным форсункой имеют только датчик скорости двигателя.
- Для двигателей с топливными системами MCRS включите переключатель зажигания и позвольте топливному насосу работать в течение 2 минут. Повторите этот шаг один раз, чтобы убедиться, что топливная система полностью заряжена.
- Используйте пусковой двигатель для вращения коленчатого вала до тех пор, пока давление масла не будет указано на измерительном приборе или не погаснет предупредительный свет.

![[14400007.png]]

Подключите датчики.

Запускай двигатель. См. процедуру 101-014 (нормальная процедура начала) в разделе 1.

![[19400429.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> **CAUTION · Осторожно**
> Do not allow the engine to run out of fuel. A loss of fuel supply can cause damage to the fuel pump and injectors
>
> Mechanically Actuated Injector
>
> **Note · Примечание**
> Engines equipped with a Prelub™ system are self priming and will **not** require the following procedure.
>
> Complete the following steps after each oil change, or after the engine has been shut down for more than 5 days to make sure the engine receives the correct oil flow through the lubricating oil system.
>
> 1. Disconnect the electrical wire from the fuel pump solenoid valve.
> 2. Use the starting motor to rotate the crankshaft until the oil pressure is indicated on the gauge or the warning lamp goes out.
> 3. Connect the electrical wire to the fuel pump solenoid valve. Refer to Procedure 018-006 (Engine Component Torque Values) in Section V.
> 4. Start the engine; refer to Procedure 101-014 (Normal Starting Procedure) in Section 1.
>
> Electronically Actuated Injector
>
> **Note · Примечание**
> This procedure will cause fault codes for the unplugged sensors to be logged. They will go inactive and have no effect on engine operation after the sensors are connected.
>
> **Note · Примечание**
> Engines equipped with a Prelub™ system are self priming for the lubricating system and will use the following procedure to prime only the engine fuel system.
>
> - Disconnect the engine speed sensor and the camshaft position sensor. Engines with mechanical injectors have **only** the engine speed sensor.
> - For engines with MCRS fuel systems, cycle the keyswitch on and allow the fuel priming pump to operate for 2 minutes. Repeat this step one time to make sure the fuel system is fully primed.
> - Use the starting motor to rotate the crankshaft until the oil pressure is indicated on the gauge or the warning light goes out.
>
> Connect the sensors.
>
> Start the engine. Refer to Procedure 101-014 (Normal Starting Procedure) in Section 1.
