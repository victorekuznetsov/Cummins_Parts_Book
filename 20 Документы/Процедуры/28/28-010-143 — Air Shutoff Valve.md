---
aliases:
  - "Воздушная отсечная заслонка"
type: "Процедура"
doc: "28-010-143"
title_en: "Air Shutoff Valve"
title_ru: "Воздушная отсечная заслонка"
modified: "2023-08-30"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "3810497"
figures: 16
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/28/28-010-143.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/28-010-143.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/28"
  - "перевод/машинный"
---

# Air Shutoff Valve
**Воздушная отсечная заслонка**

> [!abstract] Процедура · `28-010-143`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[3810497 — K38, K50, QSK38 and QSK50 Operation and Maintenance Manual|3810497]]
> **Секции:** Section - Maintenance Procedures at 10000 Hours
> **Даты:** изменён 2023-08-30
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/28/28-010-143.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/28-010-143.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

> [!danger] ОПАСНО
> Не используйте дизельный двигатель, где есть или могут быть горючие пары. Эти пары могут всасываться через систему воздухозаборника и вызывать ускорение двигателя и превышение скорости, что может привести к пожару, взрыву и обширному имущественному ущербу. Доступны многочисленные устройства безопасности, такие как устройства отключения воздухозаборника, чтобы минимизировать риск превышения скорости, когда двигатель, из-за применения, работает в горючей среде, например, из-за разлива топлива или утечки газа. Помни, Камминс Инк. Вы не можете знать, как использовать ваш двигатель. Владелец и оператор оборудования несут ответственность за безопасную работу во враждебной среде. Проконсультируйтесь с авторизованным местом ремонта Cummins® для получения дополнительной информации.

> [!warning] ОСТОРОЖНО
> Работа клапанов отключения воздуха является аварийным ответом и может привести к возможному повреждению двигателя.

> [!note] Примечание
> В этом пакете установлены запорные клапаны воздухозаборника в качестве устройства безопасности, чтобы минимизировать риск превышения скорости, когда двигатель будет работать в потенциально горючей среде.

Воздушные запорные клапаны (1) расположены между турбокомпрессором и воздухозаборником кроссовера к послеохладителям. Один запорный клапан доступен на банк цилиндров.

![[10g00023.png]]

Ранние модели имеют ручную ручку сброса, расположенную под корпусом главного клапана (1).

![[10q00215.png]]

Более поздние модели имеют сбрасывание шестиугольника в том же месте (2). Это работает так же, как ручка сброса, но гаечный ключ ** должен использоваться для поворота шестиугольника.

![[10q00216.png]]

### Основное описание

Назначение клапана отключения воздуха предназначено для закрытия воздушного потока к системе впуска двигателя во время чрезвычайной ситуации.

Запорный клапан имеет четыре основных компонента:

1. Включает интегрированные штыревые/гнездовые фланцы мармонов.
2. Запечатанный корпус, который включает в себя соленоидную активированную систему защелки. Привод также включает в себя переключатель положения для указания состояния клапана (открытого/закрытого).
3. Ручная перезагрузка/торсионная пружина - обеспечивает необходимую силу для закрытия ворот с помощью ручки или шестиугольника.
4. Затвор - Движущийся металлический диск, который блокирует воздушный поток при активации клапана (показано в открытом положении).

![[10g00024.png]]

Клапан отключения воздуха является устройством с возможностью блокировки питания. Когда клапан соленоида под напряжением, привод отключается, позволяя воротам закрываться под действием торсионной пружины.

Клапаны ** должны быть сброшены вручную путем вращения ручного сброса (1) до тех пор, пока привод не «щелкнет» и не откроет затвор.

Контроллер двигателя ** не позволяет запустить двигатель, когда один или несколько клапанов отключения воздуха закрыты.

![[10g00025.png]]

Воздушные запорные клапаны работают в двух условиях:

Если обычный сигнал отключения скорости от контроллера не отключает двигатель, вторичный сигнал отключения скорости запускает отключение воздуха. Топливо отключается одновременно, и маяк на верхней части окна клиентского интерфейса (C.I.B.) будет включен.

![[10g00026.png]]

Клапаны отключения воздуха могут быть закрыты вручную, нажав кнопку E-stop на панели управления силовым модулем. Это экстренное действие, которое может привести к повреждению двигателя.

> [!note] Примечание
> Аварийное отключение может ** не** использоваться для нормального отключения двигателя.

![[10g00027.png]]

Когда произошло аварийное отключение, ручная перезагрузка (1) будет в закрытом положении. Проверьте двигатель на предмет повреждений перед перезагрузкой.

Проверьте наличие воспламеняющихся паров вблизи источника впускного воздуха.

Проверьте уплотнения турбокомпрессора, чтобы убедиться, что нет утечек масла. См. процедуру 010-040 в разделе 10.

Осмотрите датчики скорости/положения коленчатого вала двигателя и положения распределительного вала на наличие признаков повреждения или подделки.

![[10g00025.png]]

### Подготовительные операции

> [!danger] ОПАСНО
> Проверить, что клапан отключения воздуха находится в закрытом положении до удаления и обработки, чтобы уменьшить вероятность травмы.

> [!note] Примечание
> Эта процедура используется для удаления только одного из клапанов отключения воздуха от двигателя. Оставшийся клапан отключения воздуха можно удалить с помощью аналогичных шагов.

- Обезвредить систему и следовать всем процедурам безопасности (заблокировать / выключить). См. сервисную документацию изготовителя оборудования.
- Отключите подачу воздуха/топлива к воздухозаборнику, если он оборудован.[[102-012-022 — Air Starting Motor|См. процедуру 012-022 в разделе 12.]]
- Когда двигатель остановлен, вручную активируйте E-Stop, чтобы закрыть клапаны отключения воздуха, прежде чем их удалять.
- Перезагрузите E-Stop. Отключите электроснабжение. См. сервисную документацию изготовителя оборудования.

> [!note] Примечание
> E-Stop ** должен быть сброшен перед отключением питания, иначе клапан отключения воздуха автоматически закроется при подключении к электросети.

### Снятие

> [!danger] ОПАСНО
> Проверить, что клапан отключения воздуха находится в закрытом положении до удаления и обработки, чтобы уменьшить вероятность травмы.

Устраните зажимы (3) и удалите воздухозаборную трубу (2) от турбокомпрессора к клапану отключения воздуха.

Отсоедините проводную упряжку (1) от клапана отключения воздуха вблизи соленоида.

Удалите зажим V-диапазона (4) из соединения воздушного кроссовера.

Удалить клапан отключения воздуха (5).

Удалить и выбросить кольца (6).

![[10g00028.png]]

Покрыть воздушный кроссовер и точки соединения турбокомпрессора, чтобы предотвратить загрязнение мусора.

Повторите шаги удаления для противоположной стороны.

![[10l00030.png]]

### Очистка и проверка при повторном использовании

Осмотрите трубу воздухозаборника, соединительный шланг, шланговые зажимы и V-диапазонные зажимы.

Замените поврежденные части.

![[10l00031.png]]

Не разбирать корпус клапана. Корпус клапана ** не является пригодной частью.

![[10g00029.png]]

### Установка

> [!danger] ОПАСНО
> Проверить, что клапан отключения воздуха находится в закрытом положении до удаления и обработки, чтобы уменьшить вероятность травмы.

![[10g00030.png]]

Удалите любые защитные крышки от воздушных кроссоверов и турбокомпрессоров.

Установите новое кольцо на клапан отключения воздуха (1).

С ручкой сброса, обращенной вниз; свободно установить клапан отключения воздуха (2) на воздушный кроссовер на двигателе с использованием зажима V-диапазона (3).

![[10g00031.png]]

Поверните клапан (1) отключения воздуха, чтобы ручка сброса была обращена в сторону от двигателя, как показано.

Закрепите зажим V-диапазона, удерживающий клапан отключения воздуха к воздушному кроссоверу.

> [!tip] Момент затяжки
> 9 Н·м [80 фунт-дюйм]

![[10g00032.png]]

Установите новое кольцо (1) и воздушную кроссоверную трубу (2) на клапан отключения воздуха с использованием зажима (3) V-диапазона и турбокомпрессора с гибким шлангом. Зажим V-диапазона затягивается (3). Зажимы (4) затягивают на воздушном кроссовере шланг.

> [!tip] Момент затяжки
> 9 Н·м [80 фунт-дюйм]

Подключите проводную упряжку для клапана отключения воздуха вблизи соленоида (5).

> [!note] Примечание
> Избегайте маршрутизации проводов вблизи высокотемпературных компонентов.

Повторите для противоположной стороны.

![[10g00033.png]]

### Завершающие операции

> [!warning] ОСТОРОЖНО
> Не проверяйте функцию клапана отключения воздуха при работе двигателя.

- Зарядите систему и следуйте всем процедурам безопасности (Lock Out / Tag Out). См. сервисную документацию изготовителя оборудования.

Проверьте работу клапана отключения воздуха:

- Испытать функцию клапана отключения воздуха, нажав аварийную остановку системы с остановкой двигателя.
- Сбросьте клапаны в открытое положение. Проверяйте клапаны на наличие явных признаков повреждения/незакрепленных крепежных элементов.
- Используйте ручной выпуск для приведения в действие клапанов. Сбросьте клапан в открытое положение.
- Подключите подачу воздуха/топлива к воздухозаборнику, если он оборудован.[[102-012-022 — Air Starting Motor|См. процедуру 012-022 в разделе 12.]]
- Запуск и эксплуатация двигателя. Проверьте на наличие утечек и неисправностей.


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> **WARNING · Опасно**
> Do not operate a diesel engine where there are or can be combustible vapors. These vapors can be sucked through the air intake system and cause engine acceleration and over speeding that can result in a fire, an explosion, and extensive property damage. Numerous safety devices are available, such as air intake shutoff devices, to minimize the risk of over speeding where an engine, due to the application, is operating in a combustible environment, such as due to a fuel spill or gas leak. Remember, Cummins Inc. has no way of knowing the use you have for your engine. The equipment owner and operator are responsible for safe operation in a hostile environment. Consult a Cummins® Authorized Repair Location for further information.
>
> **CAUTION · Осторожно**
> Operation of the air shutoff valves is an emergency response and may result in possible damage to the engine.
>
> **Note · Примечание**
> This package has air intake shutoff valves installed as a safety device to minimize the risk of over speeding where an engine will be operated in a potentially combustible environment.
>
> The air shutoff valves (1) are located between the turbocharger and air intake crossover to the aftercoolers. One shutoff valve is available per cylinder bank.
>
> Early models have a manual reset handle located under the main valve body (1).
>
> Later models have a hexagon drive reset in the same location (2). This operates in the same way as the reset handle, but a wrench **must** be used to turn the hexagon drive.
>
> ### Basic Description
>
> The purpose of the air shutoff valve is intended to close the airflow off to the engine intake system during an emergency situation.
>
> The air shutoff valve has four major components:
>
> 1. Valve body- Includes integrated male/female Marmon flanges.
> 2. Actuator- Sealed housing that includes a solenoid activated latch system. The actuator also includes a position switch to indicate the state of the valve (open/closed).
> 3. Manual Reset/Torsional Spring- Provides the necessary force to close the gate using the handle or hexagon drive.
> 4. Gate- Moving metal disc that blocks airflow when the valve is activated (shown in the open position).
>
> The air shutoff valve is a power-to-close device. When the valve solenoid is energized, the actuator unlatches allowing the gate to close under the force of the torsional spring.
>
> The valves **must** be manually reset by rotating the manual reset (1) until the actuator "clicks" and holds the gate open.
>
> The engine controller will **not** allow the engine to be started when one or more air shutoff valves is closed.
>
> The air shutoff valves operate under two conditions:
>
> If a normal overspeed shutdown signal from the controller does **not** shut off the engine, a secondary overspeed signal triggers an air shut off shutdown. Fuel is shut off at the same time and the beacon on top of the Customer Interface Box (C.I.B.) will come on.
>
> The air shutoff valves can be manually closed by pushing the E-stop button on the power module control panel. This is an emergency action that can result in engine damage.
>
> **Note · Примечание**
> Emergency shutdown can **not** be used for normal shutdown of the engine.
>
> When an emergency shut off has occurred, the manual reset (1) will be in the closed position. Check the engine for damage before restarting.
>
> Check for evidence of flammable vapors near the intake air source.
>
> Check the turbocharger seals to verify there are no oil leaks. Refer to Procedure 010-040 in Section 10.
>
> Inspect the engine crankshaft speed/position and camshaft position sensors for signs of damage or tampering.
>
> ### Preparatory Steps
>
> **WARNING · Опасно**
> Verify the air shutoff valve is in the closed position prior to removal and handling to reduce the possibility of personal injury.
>
> **Note · Примечание**
> This procedure is used for removing just one of the air shutoff valves from the engine. The remaining air shutoff valve can be removed using similar steps.
>
> - De-energize the system and follow all safety procedures (Lock Out/Tag Out). See equipment manufacturer service information.
> - Disconnect the air/fuel supply to the air starter, if equipped. [[102-012-022 — Air Starting Motor|Refer to Procedure 012-022 in Section 12.]]
> - With the engine stopped, manually activate the E-Stop to close the air shutoff valves before removing them.
> - Reset the E-Stop. Disconnect power supply. See equipment manufacturer service information.
>
> **Note · Примечание**
> The E-Stop **must** be reset before disconnecting the power, otherwise the air shutoff valve will automatically close when the electrical connection is made.
>
> ### Remove
>
> **WARNING · Опасно**
> Verify the air shutoff valve is in the closed position prior to removal and handling to reduce the possibility of personal injury.
>
> Loosen the clamps (3) and remove the air intake pipe (2) from the turbocharger to the air shutoff valve.
>
> Disconnect the wiring harness (1) from the air shutoff valve near the solenoid.
>
> Remove the V-band clamp (4) from the air crossover connection.
>
> Remove the air shutoff valve (5).
>
> Remove and discard the o-rings (6).
>
> Cover the air crossover and turbocharger connection points to prevent debris contamination.
>
> Repeat the removal steps for the opposite side.
>
> ### Clean and Inspect for Reuse
>
> Inspect the air intake pipe, connection hose, hose clamps, and V-band clamps.
>
> Replace any damaged parts.
>
> Do **not** disassemble the valve body. The valve body is **not** a serviceable part.
>
> ### Install
>
> **WARNING · Опасно**
> Verify the air shutoff valve is in the closed position prior to removal and handling to reduce the possibility of personal injury.
>
> Remove any protective covers from the air crossover and turbocharger connections.
>
> Install a new o-ring onto the air shutoff valve (1).
>
> With the reset handle facing down; loosely install the air shutoff valve (2) to the air crossover on the engine using a V-band clamp (3).
>
> Rotate the air shutoff valve (1) so the reset handle is facing away from the engine, as shown.
>
> Tighten the V-band clamp holding the air shutoff valve to the air crossover.
>
> **Момент затяжки · Torque Value**
> 9 n•m [80 in-lb]
>
> Install a new o-ring (1) and the air crossover pipe (2) onto the air shutoff valve using a V-band clamp (3) and to the turbocharger with the flexible hose. Tighten the V-band clamp (3). Tighten the clamps (4) on the air crossover hose.
>
> **Момент затяжки · Torque Value**
> 9 n•m [80 in-lb]
>
> Connect the wiring harness for the air shutoff valve near the solenoid (5).
>
> **Note · Примечание**
> Avoid routing the wiring harness near high temperature components.
>
> Repeat for the opposite side.
>
> ### Finishing Steps
>
> **CAUTION · Осторожно**
> Do not check the air shutoff valve function with engine running.
>
> - Energize the system and follow all safety procedures (Lock Out/Tag Out). See equipment manufacturer service information.
>
> Check the air shutoff valve operation:
>
> - Test the air shutoff valve function by pressing the system emergency stop with the engine stopped.
> - Reset the valves to an open position. Inspect the valves for obvious signs of damage/loose fasteners.
> - Use the manual release to actuate the valves. Reset the valve to an open position.
> - Connect the air/fuel supply to the air starter, if equipped. [[102-012-022 — Air Starting Motor|Refer to Procedure 012-022 in Section 12.]]
> - Start and operate the engine. Check for leaks and faults.
