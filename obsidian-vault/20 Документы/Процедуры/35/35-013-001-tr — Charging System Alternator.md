---
aliases:
  - "Генератор системы зарядки"
type: "Процедура"
doc: "35-013-001-tr"
title_en: "Charging System Alternator"
title_ru: "Генератор системы зарядки"
modified: "2024-11-11"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
figures: 11
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-013-001-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-013-001-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/35"
  - "перевод/машинный"
---

# Charging System Alternator
**Генератор системы зарядки**

> [!abstract] Процедура · `35-013-001-tr`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 13 - Electrical Equipment - Group 13
> **Даты:** изменён 2024-11-11
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-013-001-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-013-001-tr.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Первичная проверка

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

> [!danger] ОПАСНО
> Кислота чрезвычайно опасна и может повредить оборудование, а также вызвать серьезные ожоги. Всегда предоставляйте резервуар с сильной содовой в качестве нейтрализующего агента при обслуживании батарей. Носите очки и защитную одежду, чтобы уменьшить вероятность серьезных травм.

Прикрепите тестер с углеродной смолой и зажим на амперметре, как показано. Нагрузка от тестера на углеродную кость до номинальной производительности генератора переменного тока.

Измерьте падение напряжения как в положительных, так и в отрицательных цепях. Сложите их вместе. Сумма может **не** превышать максимальное падение напряжения 0,5-VDC.

Ремонт или замена проводов, как это требуется для выполнения вышеуказанных спецификаций.

![[13800028.png]]

Прикрепите мультиметр к генератору переменного тока, как показано на графике.

С батареями в полностью заряженном состоянии и всеми аксессуарами выключите двигатель и запустите его на высоком холостом ходу. Дайте время для стабилизации напряжения, прежде чем принимать какие-либо показания.

Измерить выходное напряжение генератора. Максимальный выходной предел системы составляет 15,5-VDC.

Ремонт или замена генератора или регулятора, если предел напряжения превышает максимальный предел выхода.

См. спецификации производителя для минимального выходного напряжения.

![[13800026.png]]

Подключите углеродный тестер к батареям параллельно.

Закрепить амперметр индукции вокруг выходного провода генератора.

Если к выходному терминалу генератора подключено более одного провода, зажимайте амперметр вокруг всех проводов.

Запустите двигатель и работайте на высоком холостом ходу.

Убедитесь, что все грузы автомобиля выключены.

Проверьте скорость генератора с помощью цифрового оптического тахометра. Ремень привода генератора скольжения может привести к низкому выходному считыванию. Выход генератора переменного тока напрямую связан со скоростью, с которой он вращается.

Вращение генератора должно быть с приблизительной номинальной скоростью. Большинство тяжелых генераторов переменной мощности оцениваются в 5000 об/мин. Проверьте спецификации производителя для конкретного тестируемого генератора.

![[13800027.png]]

Включите тестер с углеродной смолой и настройте его до тех пор, пока амперметр не достигнет максимального значения. Запишите эту ценность.

Выключите тестер на углеродную клетку и выключите двигатель.

Если показания на амперметре равны нулю (отсутствие выхода), намагнитите ротор с помощью генератора переменного тока, подключенного нормально. Немедленно подсоедините прыгун, ведущий от положительной батареи (+) к реле генератора (R) или индикатору (I) терминала. Эта процедура применяется как к отрицательным (-), так и к положительным (+) наземным системам и восстановит нормальный остаточный магнетизм.

Повторите тест. Если выходной сигнал **не** в пределах 10 процентов от номинального значения (наклеен на корпус генератора), замените генератор.

![[13800027.png]]

### Подготовительные операции

> [!danger] ОПАСНО
> Батареи могут выделять взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Удалите кабели аккумулятора.[[99-013-009 — Battery Cables and Connections|См. процедуру 013-009 в разделе 13.]]
- Удалите электрическое соединение из генератора. Помечайте соединения, как они удалены.
- Снимите ремень привода генератора.[[35-013-005-tr — Charging System Alternator Drive Belt|См. процедуру 013-005 в разделе 13.]]

![[ck800wa.png]]

### Снятие

Гора Пад

Удалите четыре крепежных болта генератора.

Удалите генератор из кронштейна генератора.

![[13200097.png]]

Гора Спул

Удалите крепежные болты (3) и регулировочное звено.

Удалите крепежные болты генератора (1), гайку, шайбу (2) и генератор переменного тока.

![[eh8bdha.png]]

### Очистка и проверка при повторном использовании

Осмотрите шкив генератора на наличие трещин или сломанных канавок.

Замените шкив, если обнаружен ущерб.

![[13c00016.png]]

### Установка

Гора Пад

Установите генератор переменного тока и четыре крепежных болта.

Затяните болты.

> [!tip] Момент затяжки
> 36 Н·м [27 фунт-фут]

Для установки генератора в скобку генератора не требуется корректировка выравнивания.

![[13200097.png]]

Гора Спул

Установите регулировочную линию и крепежные болты (3).

Затягивайте крепежные болты.

> [!tip] Момент затяжки
> 47 Н·м [35 фунт-фут]

Установите генератор, болты (1), шайбу и гайку (2) на монтажную кронштейн и регулировочную линию.

**не** затягивать болты и гайки до тех пор, пока ремень генератора не будет отрегулирован.

![[eh8bdha.png]]

### Завершающие операции

- Установите ремень привода генератора.[[35-013-005-tr — Charging System Alternator Drive Belt|См. процедуру 013-005 в разделе 13.]]
- Подключите электрические соединения генератора.
- Подсоедините провода аккумуляторных батарей.[[99-013-009 — Battery Cables and Connections|См. процедуру 013-009 в разделе 13.]]
- Управляйте двигателем и проверяйте его правильность.

![[ck800wa.png]]


> [!quote]- Original (English) · английский оригинал
> ### Initial Check
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> **WARNING · Опасно**
> Acid is extremely dangerous and can damage the machinery and can also cause serious burns. Always provide a tank of strong soda water as neutralizing agent when servicing the batteries. Wear goggles and protective clothing to reduce the possibility of serious personal injury.
>
> Attach the carbon-pile tester and clip on ammeter as shown. Adjust the load from the carbon-pile tester to the rated performance of the alternator.
>
> Measure the voltage drop in both the positive and negative circuits. Add these together. The sum can **not** exceed a maximum voltage drop of 0.5-VDC.
>
> Repair or replace the wiring as required to meet the above specifications.
>
> Attach the multimeter to the alternator as illustrated in the graphic.
>
> With the batteries in fully charged condition and all the accessories off, start the engine and run it at high idle. Allow time for the voltage to stabilize before taking any readings.
>
> Measure the alternator output voltage. The system maximum output limit is 15.5-VDC.
>
> Repair or replace the alternator or regulator if the voltage limit exceeds the maximum output limit.
>
> Refer to the manufacturer's specifications for minimum voltage output.
>
> Connect the carbon-pile tester to the batteries in parallel.
>
> Clamp the induction ammeter around the alternator output wire.
>
> If more than one wire is connected to the alternator output terminal, clamp the ammeter around all wires.
>
> Start the engine and operate at high idle.
>
> Make sure all vehicle loads are turned off.
>
> Check the speed of the alternator using a digital optical tachometer. A slipping alternator drive belt can result in a low output reading. The alternator output is directly related to the speed it is turning.
>
> The alternator **must** be turning at approximate rated speed. Most heavy-duty alternators are rated at 5000 rpm. Check the manufacturer's specifications for the specific alternator being tested.
>
> Turn on the carbon-pile tester and adjust until the ammeter reaches its highest reading. Record this value.
>
> Turn off the carbon-pile tester and shut off the engine.
>
> If the reading on the ammeter is zero (no output), magnetize the rotor with the alternator hooked up normally. Momentarily connect a jumper lead from the battery positive (+) to the alternator relay (R) or indicator (I) terminal. This procedure applies to both negative (-) and positive (+) ground systems, and will restore the normal residual magnetism.
>
> Repeat the test. If the output is **not** within 10 percent of the rated output (stamped on the alternator case), replace the alternator.
>
> ### Preparatory Steps
>
> **WARNING · Опасно**
> Batteries can emit explosive gasses. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Remove the battery cables. [[99-013-009 — Battery Cables and Connections|Refer to Procedure 013-009 in Section 13.]]
> - Remove the electrical connection from the alternator. Label the connections as they are removed.
> - Remove the alternator drive belt. [[35-013-005-tr — Charging System Alternator Drive Belt|Refer to Procedure 013-005 in Section 13.]]
>
> ### Remove
>
> Pad Mount
>
> Remove the four alternator mounting capscrews.
>
> Remove the alternator from the alternator bracket.
>
> Spool Mount
>
> Remove the adjusting link mounting capscrew (3) and the adjusting link.
>
> Remove the alternator mounting capscrew (1), nut, washer (2), and alternator.
>
> ### Clean and Inspect for Reuse
>
> Inspect the alternator pulley for cracks or broken grooves.
>
> Replace the pulley if damage is found.
>
> ### Install
>
> Pad Mount
>
> Install the alternator and the four mounting capscrews.
>
> Tighten the capscrews.
>
> **Момент затяжки · Torque Value**
> 36 n•m [27 ft-lb]
>
> No alignment adjustment is required for the alternator to the alternator bracket.
>
> Spool Mount
>
> Install the adjusting link and mounting capscrew (3).
>
> Tighten the mounting capscrew.
>
> **Момент затяжки · Torque Value**
> 47 n•m [35 ft-lb]
>
> Install the alternator, capscrew (1), washer, and nut (2) to the mounting bracket and adjusting link.
>
> Do **not** tighten the capscrews and nuts until the alternator belt is adjusted.
>
> ### Finishing Steps
>
> - Install the alternator drive belt. [[35-013-005-tr — Charging System Alternator Drive Belt|Refer to Procedure 013-005 in Section 13.]]
> - Connect the alternator electrical connections.
> - Connect the battery cables. [[99-013-009 — Battery Cables and Connections|Refer to Procedure 013-009 in Section 13.]]
> - Operate the engine and check for proper operation.
