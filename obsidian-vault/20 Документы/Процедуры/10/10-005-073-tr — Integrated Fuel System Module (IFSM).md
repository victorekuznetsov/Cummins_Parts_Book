---
type: "Процедура"
doc: "10-005-073-tr"
title_en: "Integrated Fuel System Module (IFSM)"
modified: "2013-10-02"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
manuals:
  - "3666239"
figures: 54
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-005-073-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-005-073-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSX15"
  - "группа/10"
  - "перевод/машинный"
---

# Integrated Fuel System Module (IFSM)

> [!abstract] Процедура · `10-005-073-tr`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Входит в руководства:** [[3666239 — Signature™, ISX, and QSX15 Service Manual|3666239]]
> **Секции:** Section 5 - Fuel System - Group 05
> **Даты:** изменён 2013-10-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-005-073-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-005-073-tr.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Подготовительные операции

Автомобильные модели CM870 и CM871

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Отсоедините провода аккумуляторных батарей. См. процедуру 013-009 в разделе 13.
- Снять смеситель рециркуляции выхлопных газов (EGR).[[10-011-021-tr — EGR Mixer|См. процедуру 011-021 в разделе 11.]]
- Отключите подключение воздухозаборника.[[10-010-080-tr — Air Intake Connection|См. процедуру 010-080 в разделе 10.]]
- Удалите электропроводку двигателя из всех датчиков температуры и давления, приводов заправки и синхронизации, клапана отключения топлива, датчика воды в топливе и насоса для подъёма топлива.
- Удалите трубки датчика дифференциального давления EGR. См. процедуру 011-026 в разделе 11.
- Удалите датчик дифференциального давления EGR. Используйте следующую процедуру в Руководстве по устранению неполадок и ремонту, Электронной системе управления CM870, Двигателях SignatureTM и ISX, Бюллетене 4021334. См. процедуру 019-370 в разделе 19.
- Удалите адаптер датчика дифференциального давления EGR. См. процедуру 011-028 в разделе 11.
- Удалите клиентскую аксессуарную скобку.
- Отключите линии подачи топлива и слива топлива. См. процедуру 006-024 в разделе 6.
- Удалите насос лифта. Используйте следующую процедуру в Руководстве по устранению неполадок и ремонту, Электронной системе управления CM870, Двигателях SignatureTM и ISX, Бюллетене 4021334. См. процедуру 019-396 в разделе 19.
- Удалите модуль управления двигателем (ECM) охлаждающей пластины линии подачи топлива (внизу) из интегрированного модуля топливной системы (IFSM) и линию возврата топлива (вверху) охлаждающей пластины ECM из топливного насоса. См. процедуру 006-006 в разделе 6.
- Удалите топливный фильтр.[[10-006-015-tr — Fuel Filter (Spin-On Type)|См. процедуру 006-015 в разделе 6.]]
- Удалите аксессуар, расположенный над IFSM. См. процедуру 001-082 в разделе 1.

![[ck800wa.png]]

CM570

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Отсоедините провода аккумуляторных батарей. См. процедуру 013-009 в разделе 13.
- Удалите трубы для впуска воздуха.[[10-010-080-tr — Air Intake Connection|См. процедуру 010-080 в разделе 10.]]
- Отсоедините проводку двигателя от всех датчиков давления и температуры, приводов заправки и синхронизации, клапана отключения топлива, датчика воды в топливе и насоса подъемника топлива.
- Удалите крышки управления топливом.
- Отключите подключение воздухозаборника.[[10-010-080-tr — Air Intake Connection|См. процедуру 010-080 в разделе 10.]]
- Удалите клиентскую аксессуарную скобку.
- Удалите линии подачи топлива и слива топлива. См. процедуру 006-024 в разделе 6.
- Удалите топливный фильтр.[[10-006-015-tr — Fuel Filter (Spin-On Type)|См. процедуру 006-015 в разделе 6.]]

![[ck800wa.png]]

### Снятие

> [!danger] ОПАСНО
> Масса этого узла больше 23 кг \[50 фунтов\]. Чтобы не получить тяжёлую травму, поднимайте этот узел с помощником или подходящим грузоподъёмным оборудованием.

Удалите два крепежных болта из IFSM.

Установите два направляющих шпильки.

Удалите оставшиеся болты, IFSM и прокладку. Откажитесь от прокладки, если она повреждена.

![[05c00131.png]]

### Разборка

Автомобильные модели CM870 и CM871

Удалить все компоненты:

- Сенсоры
- Регуляторы
- Обратный клапан
- Приводы топлива и время
- Запорный клапан топлива
- Грушевой насос (**только** снимите четыре длинных болта, как показано на иллюстрации).
- Впускная и сливная арматуры топлива
- Топливные амортизаторы (**только** снимают два верхних болта сборки амортизатора, как показано на иллюстрации).
- Все резьбовые вилки, о-кольца и прокладки.

![[05c00201.png]]

CM570

Удалить все компоненты:

- Сенсоры
- Регуляторы
- Обратный клапан
- Приводы топлива и время
- Запорный клапан топлива
- Грушевой насос (**только** снимите четыре длинных болта, как показано на иллюстрации).
- Впускная и сливная арматуры топлива
- Топливные амортизаторы (**только** снимают два верхних болта сборки амортизатора, как показано на иллюстрации).
- Все резьбовые вилки, о-кольца и прокладки.

![[05c00264.png]]

### Очистка и проверка при повторном использовании

Автомобильные модели CM870 и CM871

Проверить противоосушительный задний клапан на предмет повреждения или неправильной герметизации. Заменить, если это необходимо.

Убедитесь, что противоосушительные задние клапаны сидений должным образом и не имеют повреждений или мусора. Если повреждение обнаружено, замените клапан.

![[05c00190.png]]

Осмотрите отверстия крепления болтов на наличие трещин. Проверяйте IFSM на наличие утечек или трещин. Замените модуль, если обнаружены трещины.

![[05c00132.png]]

Осмотрите 1724 кПа[250 psi] и 2620 кПа[380 psi] топливные регуляторы на предмет наличия мусора или повреждений (включая пружину внутри регуляторов). Заменить регулятор, если обнаружен ущерб.

![[05c00135.png]]

CM570

Осмотрите отверстия крепления болтов на наличие трещин.

![[05c00221.png]]

Удалите регулятор давления топлива 1724 кПа[250 psi].

Проверка на предмет наличия мусора или других повреждений. Заменить регулятор, если это необходимо.

Установите регулятор давления топлива и затяните.

> [!tip] Момент затяжки
> 27 Н·м [239 фунт-дюйм]

![[05c00109.png]]

Удалите регулятор давления топлива 2206 кПа[320 psi].

Проверка на предмет наличия мусора или других повреждений. Заменить регулятор, если это необходимо.

Установите регулятор давления топлива и затяните.

> [!tip] Момент затяжки
> 27 Н·м [239 фунт-дюйм]

![[05c00110.png]]

Удалите контрольные клапаны, расположенные в топливном впуске и головке крепления топливного фильтра.

Проверьте оба места должным образом и без повреждений или мусора. Заменить, если необходимо.

Установите как контрольные клапаны, так и затягивайте.

> [!tip] Момент затяжки
> 17 Н·м [150 фунт-дюйм]

![[05c00185.png]]

Проверьте экран фильтра входа на наличие мусора. Очистите фильтр или замените его, если это необходимо.

Установите экран впускного фильтра.

![[05c00150.png]]

### Сборка

Автомобильные модели CM870 и CM871

Проверьте уплотнение (1) в канавке демпфера (2) управления топливом и добавьте многоцелевую смазку LubriplateTM для удержания уплотнения на месте.

Прикрепить демпфер (2) управления топливом с болтами (3) и затянуть.

> [!tip] Момент затяжки
> 9.5 Н·м [84 фунт-дюйм]

![[05c00202.png]]

Установите кольца (2 и 3) на регулятор давления (1).

Установите (2620 кПа) \[380 psi\] регулятор давления (1) в корпус IFSM и затяните.

> [!tip] Момент затяжки
> 27 Н·м [239 фунт-дюйм]

![[05c00203.png]]

Установите кольца (2 и 3) на регулятор давления (1).

Установите регулятор давления топлива (1724 кПа) \[250 psi\] в корпус IFSM и затяните.

> [!tip] Момент затяжки
> 27 Н·м [239 фунт-дюйм]

![[05c00204.png]]

Установите уплотнение (2) на датчик давления топлива (1).

Установите датчик давления топлива (1) в корпус IFSM и затяните.

> [!tip] Момент затяжки
> 14 Н·м [124 фунт-дюйм]

![[05c00205.png]]

Установите уплотнение (2) на датчик температуры топлива (1).

Установите датчик температуры топлива в корпус IFSM и затяните.

> [!tip] Момент затяжки
> 23 Н·м [204 фунт-дюйм]

![[05c00206.png]]

Установите кольцо (2) на фитинг CompuchekTM (1).

Установите оба фитинга CompuchekTM (1) в корпус IFSM и затяните.

> [!tip] Момент затяжки
> 9.5 Н·м [84 фунт-дюйм]

![[05c00207.png]]

Установите кольцо (2) на противоосушительный задний клапан (1).

Установите противоосушительный задний клапан (1) в кожух и затяните.

> [!tip] Момент затяжки
> 17 Н·м [150 фунт-дюйм]

![[05c00208.png]]

Установите кольцо (2) на охлаждающую пластину, подающую топливо (1).

Установите в корпус и затяните подогнанный топливный элемент (1) охлаждающей пластины.

> [!tip] Момент затяжки
> 27 Н·м [239 фунт-дюйм]

Установите кольцо (3) на переднюю поверхность топливной арматуры охлаждающей пластины.

![[05c00209.png]]

Установите кольцо (2) на фитинг слива топлива (1).

Установите установку слива топлива (1).

Поверните гайку до самого верха.

Протяните фитинг до самого корпуса IFSM, пока он не остановится.

Поверните фитинг назад, пока резьбовый конец не будет ориентирован непосредственно на регулятор.

Запри крепление в положение и затяни запирающий гайка.

> [!tip] Момент затяжки
> 45 Н·м [33 фунт-фут]

Поддерживайте правильную ориентацию.

![[05c00210.png]]

Используйте небольшое количество многоцелевой смазки LubriplateTM в канавках на дне дозирующих приводов (2).

Установите прокладку (3) привода на каждый привод. Убедитесь, что выровняете каждый правильно.

Установите исполнительные механизмы (2) на корпус IFSM.

Используйте три болта (1), чтобы установить каждый привод на корпус и затянуть болты.

> [!tip] Момент затяжки
> 15 Н·м [133 фунт-дюйм]

![[05c00232.png]]

Используйте небольшое количество многоцелевой смазки LubriplateTM в канавках на дне исполнительных механизмов синхронизации (2).

Установите прокладку (3) привода на каждый привод. Убедитесь, что выровняете каждый правильно.

Установите исполнительные механизмы (2) на корпус IFSM.

Используйте три болта (1), чтобы установить каждый привод на корпус и затянуть болты.

> [!tip] Момент затяжки
> 15 Н·м [133 фунт-дюйм]

![[05c00233.png]]

Укажите тот же номер детали оригинального IFSM на метке (1) данных.

Прикрепить метку к корпусу, нажав винты (2) в корпус.

![[05c00213.png]]

Установите уплотнение (1) в канавку в корпусе IFSM.

Поместите приводной диск (2) над уплотнением (1), небольшой диаметр вниз.

Поместите клапанный диск (3) на приводной диск (2) с уплотняющей поверхностью вниз (пружиной диаметр пилота вверх).

Поместите пружину (4) клапана в корпус (5) привода с внутренним диаметром на лоцмане (3) клапанного диска.

Поместите корпус (5) привода над диском (2) привода.

Установить уплотнение (1) в канавку в корпусе привода (5).

Поместите запорный клапанный экран (6) над корпусом привода (5).

Выровнять рисунок отверстия экрана запорного клапана (6).

Поместите соленоид (7) над экраном (6) запорного клапана, заботясь о выравнивании отверстий и **не** защемляйте любые уплотнения. Направьте терминал, обращенный к переключателю насоса.

Используйте четыре болта (8) для крепления сборки к корпусу. Используйте шаблон «x».

> [!tip] Момент затяжки
> 5.5 Н·м [49 фунт-дюйм]

![[05c00214.png]]

Установите кольцо (2) на резьбовую вилку (1).

Установите три резьбовых вилки (1) в корпус.

> [!tip] Момент затяжки
> 17 Н·м [150 фунт-дюйм]

Установите кольцо (4) на большую резьбовую вилку (3).

Установите большую резьбовую вилку (3) в корпус.

> [!tip] Момент затяжки
> 14 Н·м [124 фунт-дюйм]

![[05c00215.png]]

Установите кольца (2) на резьбовые вилки (1).

Установите две резьбовые вилки (1) в корпус.

> [!tip] Момент затяжки
> 17 Н·м [150 фунт-дюйм]

Установите кольцо (4) на подачу топлива (3).

Установить в корпусе топливный бак (3).

> [!tip] Момент затяжки
> 27 Н·м [239 фунт-дюйм]

![[05c00216.png]]

Установите кольцо (1) на впускную установку (2) топлива из охлаждающей пластины ECM.

Установите фитинг (2) в насос топливной передачи и затяните.

> [!tip] Момент затяжки
> 27 Н·м [239 фунт-дюйм]

Установите кольцо (3) на впускную установку топлива (2).

![[05c00220.png]]

Установите кольцо (3) на насос топливной передачи (2).

Нанесите многоцелевую смазку LubriplateTM на кольцо (3).

Установите прокладку (4) на переключатель топливного насоса.

Используйте четыре болта (1) для установки насоса в корпус IFSM.

> [!tip] Момент затяжки
> 11 Н·м [97 фунт-дюйм]

![[05c00217.png]]

Установите прокладку подъемного насоса (1) на подъемный насос (2).

Используйте четыре болта (3) для установки подъемного насоса на корпус.

> [!tip] Момент затяжки
> 18 Н·м [159 фунт-дюйм]

![[05c00218.png]]

CM570

Проверьте уплотнение (1) в канавке демпфера (2) управления топливом и добавьте многоцелевую смазку LubriplateTM для удержания уплотнения на месте.

Прикрепить демпфер (2) управления топливом с болтами (3) и затянуть.

> [!tip] Момент затяжки
> 9.5 Н·м [84 фунт-дюйм]

![[05c00270.png]]

Установите кольца (2 и 3) на регулятор давления (1).

Установите регулятор давления 2206 кПа \[320 psi\] (1) в корпус IFSM и затяните.

> [!tip] Момент затяжки
> 27 Н·м [239 фунт-дюйм]

![[05c00273.png]]

Установите кольца (2 и 3) на регулятор давления (1).

Установите регулятор давления топлива 1724 кПа[250 psi] в корпус IFSM и затяните.

> [!tip] Момент затяжки
> 27 Н·м [239 фунт-дюйм]

![[05c00274.png]]

Установите кольца (2) на датчик давления топлива (1).

Установите датчик давления топлива (1) в корпус IFSM и затяните.

> [!tip] Момент затяжки
> 14 Н·м [124 фунт-дюйм]

> [!note] Примечание
> Некоторые IFSM содержат дополнительный датчик давления топлива.

![[05c00275.png]]

Установите воздушный кровоток (2) на воздушное кровоточащее отверстие в IFSM (1) через отверстие для фитинга CompuchekTM.

> [!tip] Момент затяжки
> 7.9 Н·м [70 фунт-дюйм]

![[05c00276.png]]

Установите кольцо (2) на фитинг CompuchekTM (1).

Установите оба фитинга CompuchekTM (1) в корпус IFSM и затяните.

> [!tip] Момент затяжки
> 9.5 Н·м [84 фунт-дюйм]

![[05c00277.png]]

Установите кольцо (2) на противоосушительный задний клапан (1).

Установите противоосушительный задний клапан (1) в кожух и затяните.

> [!tip] Момент затяжки
> 17 Н·м [150 фунт-дюйм]

![[05c00278.png]]

Установите кольцо (2) на противоосушительный задний клапан (1).

Установите противоосушительный задний клапан (1) для топливного фильтра в корпус и затяните.

> [!tip] Момент затяжки
> 17 Н·м [150 фунт-дюйм]

![[05c00279.png]]

Установите экран фильтра (1), пружину сжатия (2), кольцо (3) и крышку фильтра (4) в корпус.

> [!tip] Момент затяжки
> 17 Н·м [150 фунт-дюйм]

![[05c00280.png]]

Установите уплотнение (2) на фитинг (1) слива топлива.

Установите установку слива топлива (1).

Поверните гайку до самого верха.

Протяните фитинг до самого корпуса IFSM, пока он не остановится.

Поверните фитинг назад, пока резьбовый конец не будет ориентирован непосредственно на регулятор.

Запри крепление в положение и затяни запирающий гайка.

> [!tip] Момент затяжки
> 45 Н·м [33 фунт-фут]

Поддерживайте правильную ориентацию.

![[05c00281.png]]

Используйте небольшое количество многоцелевой смазки LubriplateTM в канавках на дне дозирующих приводов (2).

Установите прокладку (3) привода на каждый привод, убедившись, что каждый выровнен правильно.

Установите исполнительные механизмы (2) на корпус IFSM.

Подогнайте каждый привод к корпусу с помощью трех болтов (1) и затяните болты.

> [!tip] Момент затяжки
> 15 Н·м [133 фунт-дюйм]

![[05c00282.png]]

Используйте небольшое количество многоцелевой смазки LubriplateTM в канавках на дне исполнительных механизмов синхронизации (2).

Установите прокладку (3) привода на каждый привод, убедившись, что каждый выровнен правильно.

Установите исполнительные механизмы (2) на корпус IFSM.

Подогнайте каждый привод к корпусу с помощью трех болтов (1) и затяните болты.

> [!tip] Момент затяжки
> 15 Н·м [133 фунт-дюйм]

![[05c00283.png]]

Укажите тот же номер детали оригинального IFSM на метке (1) данных.

Прикрепить метку к корпусу, нажав винты (2) в корпус.

![[05c00284.png]]

Установите уплотнение (1) в канавку в корпусе IFSM.

Поместите приводной диск (2) над уплотнением (1), небольшой диаметр вниз.

Поместите клапанный диск (3) на приводной диск (2) с уплотняющей поверхностью вниз (пружиной диаметр пилота вверх).

Поместите пружину (4) клапана в корпус (5) привода с внутренним диаметром на лоцмане (3) клапанного диска.

Поместите корпус (5) привода над диском (2) привода.

Установить уплотнение (1) в канавку в корпусе привода (5).

Поместите запорный клапанный экран (6) над корпусом привода (5).

Выровнять рисунок отверстия экрана запорного клапана (6).

Поместите соленоид (7) над экраном запорного клапана (6), позаботившись о выравнивании отверстий и **не** защемляйте любые уплотнения. Направьте терминал, обращенный к переключателю насоса.

Прикрепите сборку к корпусу с помощью четырех болтов (8) и затяните с помощью рисунка «х».

> [!tip] Момент затяжки
> 5.5 Н·м [49 фунт-дюйм]

![[05c00285.png]]

Установите кольцо (2) на резьбовую вилку (1).

Установите три резьбовых вилки (1) в корпус.

> [!tip] Момент затяжки
> 17 Н·м [150 фунт-дюйм]

Установите кольцо (4) на большую резьбовую вилку (3).

Установите большую резьбовую вилку (3) в корпус.

> [!tip] Момент затяжки
> 14 Н·м [124 фунт-дюйм]

![[05c00286.png]]

Установите кольцо на подголовник подачи топлива.

Установите в корпус топливопровод, вмонтированный в корпус.

> [!tip] Момент затяжки
> 27 Н·м [239 фунт-дюйм]

Установите кольцо на впускную установку топлива.

![[05c00288.png]]

Установите кольцо (3) на насос топливной передачи (2).

Нанесите многоцелевую смазку LubriplateTM на кольцо (3).

Установите прокладку (4) на переключатель топливного насоса.

Используйте четыре болта (1) и установите насос на корпус IFSM.

> [!tip] Момент затяжки
> 11 Н·м [97 фунт-дюйм]

![[05c00289.png]]

Установите прокладку подъемного насоса (1) на подъемный насос (2).

Установите подъемный насос на кожух с помощью трех болтов (3).

> [!note] Примечание
> Некоторые ранние двигатели не были оснащены подъемным насосом. Эти двигатели используют ручной насос или они были оснащены вспомогательным насосом подъемника.

> [!tip] Момент затяжки
> 18 Н·м [159 фунт-дюйм]

![[05c00290.png]]

### Установка

Установите два направляющих штифта в монтажные отверстия на головке цилиндра.

![[05c00137.png]]

Установите новую прокладку на направляющие штифты.

![[05c00138.png]]

> [!danger] ОПАСНО
> Масса этого узла больше 23 кг \[50 фунтов\]. Чтобы не получить тяжёлую травму, поднимайте этот узел с помощником или подходящим грузоподъёмным оборудованием.

Установите IFSM на направляющие штифты.

Установите и затяните болты.

Удалите направляющие булавки.

Установите и затяните оставшиеся болты.

> [!tip] Момент затяжки
> 45 Н·м [33 фунт-фут]

![[05c00131.png]]

### Завершающие операции

Автомобильные модели CM870 и CM871

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Установите аксессуарную кронштейн. Он расположен над IFSM. См. процедуру 001-082 в разделе 1.
- Установите линию подачи топлива для охлаждающей пластины ECM (внизу) на линию возврата топлива для охлаждающей пластины IFSM и ECM (вверху) на топливный насос. См. процедуру 006-006 в разделе 6.
- Установите насос лифта. Используйте следующую процедуру в Руководстве по устранению неполадок и ремонту, Электронной системе управления CM870, Двигателях SignatureTM и ISX, Бюллетене 4021334. См. процедуру 019-396 в разделе 19.
- Установите клиентский аксессуар. Уплотнение до 18 Н•м[159 фунт-дюйм].
- Подключите линии подачи топлива и слива топлива. См. процедуру 006-024 в разделе 6.
- Установите адаптер датчика дифференциального давления EGR. См. процедуру 011-028 в разделе 11.
- Установите датчик дифференциального давления EGR. Используйте следующую процедуру в Руководстве по устранению неполадок и ремонту, Электронной системе управления CM870, Двигателях SignatureTM и ISX, Бюллетене 4021334. См. процедуру 019-370 в разделе 19.
- Установите датчики дифференциального давления EGR. См. процедуру 011-026 в разделе 11.
- Подключите электропроводку двигателя к датчикам температуры и давления, приводам заправки и синхронизации, клапану отключения топлива, датчику воды в топливе и насосу для подъёма топлива.
- Подключите воздухозаборник.[[10-010-080-tr — Air Intake Connection|См. процедуру 010-080 в разделе 10.]]
- Подключите смеситель EGR к воздухозаборнику.[[10-011-021-tr — EGR Mixer|См. процедуру 011-021 в разделе 11.]]
- Подключите кабель батареи. См. процедуру 013-009 в разделе 13.
- Установите топливный фильтр.[[10-006-015-tr — Fuel Filter (Spin-On Type)|См. процедуру 006-015 в разделе 6.]]
- Заправь топливную систему.
- Управляйте двигателем до нормальной рабочей температуры и проверяйте наличие утечек.

![[ck800wa.png]]

CM570

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Установите топливный фильтр.[[10-006-015-tr — Fuel Filter (Spin-On Type)|См. процедуру 006-015 в разделе 6.]]
- Подключите линии подачи топлива и слива топлива. См. процедуру 006-024 в разделе 6.
- Установите клиентский аксессуар. Уплотнение до 18 Н•м[159 фунт-дюйм].
- Подключите воздухозаборник.[[10-010-080-tr — Air Intake Connection|См. процедуру 010-080 в разделе 10.]]
- Установите крышки управления топливом.
- Подключите проводку двигателя от всех датчиков давления и температуры, приводов заправки и синхронизации, клапана отключения топлива, датчика воды в топливе и насоса подъемника топлива.
- Подключите впускной трубопровод.[[10-010-080-tr — Air Intake Connection|См. процедуру 010-080 в разделе 10.]]
- Подсоедините провода аккумуляторных батарей. См. процедуру 013-009 в разделе 13.
- Управляйте двигателем до нормальной рабочей температуры и проверяйте наличие утечек.

![[ck800wa.png]]


> [!quote]- Original (English) · английский оригинал
> ### Preparatory Steps
>
> Automotive with CM870 and CM871
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Disconnect the battery cables. Refer to Procedure 013-009 in Section 13.
> - Remove the exhaust gas recirculation (EGR) mixer. [[10-011-021-tr — EGR Mixer|Refer to Procedure 011-021 in Section 11.]]
> - Disconnect the air intake connection. [[10-010-080-tr — Air Intake Connection|Refer to Procedure 010-080 in Section 10.]]
> - Remove the engine wiring harness from all temperature and pressure sensors, fueling and timing actuators, the fuel shutoff valve, the water-in-fuel sensor, and the fuel lift pump.
> - Remove the EGR differential pressure sensor tubes. Refer to Procedure 011-026 in Section 11.
> - Remove the EGR differential pressure sensor. Use the following procedure in the Troubleshooting and Repair Manual, CM870 Electronic Control System, Signature™ and ISX Engines, Bulletin 4021334. Refer to Procedure 019-370 in Section 19.
> - Remove the EGR differential pressure sensor adapter. Refer to Procedure 011-028 in Section 11.
> - Remove the customer accessory bracket.
> - Disconnect the fuel supply and fuel drain lines. Refer to Procedure 006-024 in Section 6.
> - Remove the lift pump. Use the following procedure in the Troubleshooting and Repair Manual, CM870 Electronic Control System, Signature™ and ISX Engines, Bulletin 4021334. Refer to Procedure 019-396 in Section 19.
> - Remove the engine control module (ECM) cooling plate fuel supply line (bottom) from the integrated fuel system module (IFSM) and the ECM cooling plate fuel return line (top) from the fuel pump. Refer to Procedure 006-006 in Section 6.
> - Remove the fuel filter. [[10-006-015-tr — Fuel Filter (Spin-On Type)|Refer to Procedure 006-015 in Section 6.]]
> - Remove the accessory bracket located above the IFSM. Refer to Procedure 001-082 in Section 1.
>
> CM570
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Disconnect the battery cables. Refer to Procedure 013-009 in Section 13.
> - Remove the air inlet piping. [[10-010-080-tr — Air Intake Connection|Refer to Procedure 010-080 in Section 10.]]
> - Disconnect the engine wiring harness from all pressure and temperature sensors, fueling and timing actuators, the fuel shut off valve, the water-in-fuel sensor, and the fuel lift pump.
> - Remove the fuel control covers.
> - Disconnect the air intake connection. [[10-010-080-tr — Air Intake Connection|Refer to Procedure 010-080 in Section 10.]]
> - Remove the customer accessory bracket.
> - Remove the fuel supply and fuel drain lines. Refer to Procedure 006-024 in Section 6.
> - Remove the fuel filter. [[10-006-015-tr — Fuel Filter (Spin-On Type)|Refer to Procedure 006-015 in Section 6.]]
>
> ### Remove
>
> **WARNING · Опасно**
> This component or assembly weighs greater than 23 kg \[50 lb\]. To prevent serious personal injury, be sure to have assistance or use appropriate lifting equipment to lift this component or assembly.
>
> Remove two mounting capscrews from the IFSM.
>
> Install two guide studs.
>
> Remove the remaining capscrews, IFSM, and gasket. Discard the gasket, if damaged.
>
> ### Disassemble
>
> Automotive with CM870 and CM871
>
> Remove all components:
>
> - Sensors
> - Regulators
> - Check valve
> - Fuel and timing actuators
> - Fuel shut-off valve
> - Gear pump (**only** remove the four long capscrews, as shown in the illustration.)
> - Fuel inlet and drain fittings
> - Fuel dampers (**only** remove the two top capscrews of the damper assembly, as shown in the illustration.)
> - All threaded plugs, o-rings, and gaskets.
>
> CM570
>
> Remove all components:
>
> - Sensors
> - Regulators
> - Check valve
> - Fuel and timing actuators
> - Fuel shut-off valve
> - Gear pump (**only** remove the four long capscrews, as shown in the illustration.)
> - Fuel inlet and drain fittings
> - Fuel dampers (**only** remove the two top capscrews of the damper assembly, as shown in the illustration.)
> - All threaded plugs, o-rings, and gaskets.
>
> ### Clean and Inspect for Reuse
>
> Automotive with CM870 and CM871
>
> Inspect the anti-drain back valve for damage or improper sealing. Replace if necessary.
>
> Verify that the anti-drain back valve seats properly and is free of damage or debris. If damage is found, replace the valve.
>
> Inspect the mounting capscrew holes for cracks. Inspect the IFSM for leaks or cracks. Replace the module if cracks are found.
>
> Inspect the 1724 kPa \[250 psi\] and the 2620 kPa \[380 psi\] fuel regulators for debris or damage (including the spring inside the regulators). Replace the regulator, if damage is found.
>
> CM570
>
> Inspect the mounting capscrew holes for cracks.
>
> Remove the 1724 kPa \[250 psi\] fuel pressure regulator.
>
> Inspect for debris or other damage. Replace the regulator, if necessary.
>
> Install the fuel pressure regulator and tighten.
>
> **Момент затяжки · Torque Value**
> 27 n•m [239 in-lb]
>
> Remove the 2206 kPa \[320 psi\] fuel pressure regulator.
>
> Inspect for debris or other damage. Replace the regulator, if necessary.
>
> Install the fuel pressure regulator and tighten.
>
> **Момент затяжки · Torque Value**
> 27 n•m [239 in-lb]
>
> Remove the check valves located in the fuel inlet and fuel filter head.
>
> Verify both seat properly and are free of damage or debris. Replace, if necessary.
>
> Install both check valves and tighten.
>
> **Момент затяжки · Torque Value**
> 17 n•m [150 in-lb]
>
> Check the inlet filter screen for debris. Clean the filter, or replace, if necessary.
>
> Install the inlet filter screen.
>
> ### Assemble
>
> Automotive with CM870 and CM871
>
> Verify the seal (1) is in the groove of the fuel control damper (2) and add Lubriplate™ multi-purpose lubricant to hold the seal in place.
>
> Attach the fuel control damper (2) with capscrews (3) and tighten.
>
> **Момент затяжки · Torque Value**
> 9.5 n•m [84 in-lb]
>
> Install the o-rings (2 and 3) onto the pressure regulator (1).
>
> Install the (2620 kPa) \[380 psi\] pressure regulator (1) into the IFSM housing and tighten.
>
> **Момент затяжки · Torque Value**
> 27 n•m [239 in-lb]
>
> Install the o-rings (2 and 3) onto the pressure regulator (1).
>
> Install the (1724 kPa) \[250 psi\] fuel pressure regulator into the IFSM housing and tighten.
>
> **Момент затяжки · Torque Value**
> 27 n•m [239 in-lb]
>
> Install the o-ring seal (2) onto the fuel pressure sensor (1).
>
> Install the fuel pressure sensor (1) into the IFSM housing and tighten.
>
> **Момент затяжки · Torque Value**
> 14 n•m [124 in-lb]
>
> Install the o-ring seal (2) onto the fuel temperature sensor (1).
>
> Install the fuel temperature sensor into the IFSM housing and tighten.
>
> **Момент затяжки · Torque Value**
> 23 n•m [204 in-lb]
>
> Install the o-ring (2) onto the Compuchek™ fitting (1).
>
> Install both Compuchek™ fittings (1) into the IFSM housing and tighten.
>
> **Момент затяжки · Torque Value**
> 9.5 n•m [84 in-lb]
>
> Install the o-ring (2) onto the anti-drain back valve (1).
>
> Install the anti-drain back valve (1) into the housing and tighten.
>
> **Момент затяжки · Torque Value**
> 17 n•m [150 in-lb]
>
> Install the o-ring (2) onto the cooling plate fuel supply fitting (1).
>
> Install the cooling plate fuel supply fitting (1) into the housing and tighten.
>
> **Момент затяжки · Torque Value**
> 27 n•m [239 in-lb]
>
> Install the o-ring (3) onto the front face of the cooling plate fuel supply fitting.
>
> Install the o-ring (2) onto the fuel drain fitting (1).
>
> Install the fuel drain fitting (1).
>
> Turn the nut all the way to the top of the fitting.
>
> Thread the fitting all the way into the IFSM housing until it stops.
>
> Turn the fitting back until the threaded end is oriented directly over the regulator.
>
> Lock the fitting into position and tighten the locking nut.
>
> **Момент затяжки · Torque Value**
> 45 n•m [33 ft-lb]
>
> Maintain the correct orientation.
>
> Use a small amount of Lubriplate™ multi-purpose lubricant in the grooves on the bottom of the metering actuators (2).
>
> Install the actuator gasket (3) onto each actuator. Make sure to align each properly.
>
> Install the actuators (2) onto the IFSM housing.
>
> Use three capscrews (1) to mount each actuator to the housing and tighten the capscrews.
>
> **Момент затяжки · Torque Value**
> 15 n•m [133 in-lb]
>
> Use a small amount of Lubriplate™ multi-purpose lubricant in the grooves on the bottom of the timing actuators (2).
>
> Install the actuator gasket (3) onto each actuator. Make sure to align each properly.
>
> Install the actuators (2) onto the IFSM housing.
>
> Use three capscrews (1) to mount each actuator to the housing and tighten the capscrews.
>
> **Момент затяжки · Torque Value**
> 15 n•m [133 in-lb]
>
> Etch the same part number of the original IFSM on the data tag (1).
>
> Attach the tag to the housing by pressing the screws (2) into the housing.
>
> Install the seal (1) into the groove in the IFSM housing.
>
> Place the actuator disc (2) over the seal (1), small diameter down.
>
> Place the valve disc (3) onto the actuator disc (2) with the sealing surface down (spring pilot diameter up).
>
> Place the valve spring (4) into the actuator housing (5) with the inside diameter on the valve disc pilot (3).
>
> Place the actuator housing (5) over the actuator disc (2).
>
> Install the seal (1) into the groove in the actuator housing (5).
>
> Place the shutoff valve shield (6) over the actuator housing (5).
>
> Align the hole pattern of the shutoff valve shield (6).
>
> Place the solenoid (7) over the shutoff valve shield (6) taking care to align the holes and **not** pinch any seals. Orient the terminal facing the gear pump.
>
> Use four capscrews (8) to attach the assembly to the housing. Use an “x” pattern.
>
> **Момент затяжки · Torque Value**
> 5.5 n•m [49 in-lb]
>
> Install the o-ring (2) onto the threaded plug (1).
>
> Install the three threaded plugs (1) into the housing.
>
> **Момент затяжки · Torque Value**
> 17 n•m [150 in-lb]
>
> Install the o-ring (4) onto the large threaded plug (3).
>
> Install the large threaded plug (3) into the housing.
>
> **Момент затяжки · Torque Value**
> 14 n•m [124 in-lb]
>
> Install the o-rings (2) onto the threaded plugs (1).
>
> Install the two threaded plugs (1) into the housing.
>
> **Момент затяжки · Torque Value**
> 17 n•m [150 in-lb]
>
> Install the o-ring (4) onto the fuel supply fitting (3).
>
> Install the fuel supply fitting (3) into the housing.
>
> **Момент затяжки · Torque Value**
> 27 n•m [239 in-lb]
>
> Install the o-ring (1) onto the fuel inlet fitting (2) from the ECM cooling plate.
>
> Install the fitting (2) into the fuel gear pump and tighten.
>
> **Момент затяжки · Torque Value**
> 27 n•m [239 in-lb]
>
> Install the o-ring (3) onto the fuel inlet fitting (2).
>
> Install the o-ring (3) onto the fuel gear pump (2).
>
> Apply Lubriplate™ multi-purpose lubricant to the o-ring (3).
>
> Install the gasket (4) onto the gear fuel pump.
>
> Use four capscrews (1) to install the pump to the IFSM housing.
>
> **Момент затяжки · Torque Value**
> 11 n•m [97 in-lb]
>
> Install the lift pump gasket (1) onto the lift pump (2).
>
> Use four capscrews (3) to install the lift pump to the housing.
>
> **Момент затяжки · Torque Value**
> 18 n•m [159 in-lb]
>
> CM570
>
> Verify the seal (1) is in the groove of the fuel control damper (2) and add Lubriplate™ multi-purpose lubricant to hold the seal in place.
>
> Attach the fuel control damper (2) with capscrews (3) and tighten.
>
> **Момент затяжки · Torque Value**
> 9.5 n•m [84 in-lb]
>
> Install the o-rings (2 and 3) onto the pressure regulator (1).
>
> Install the 2206 kPa \[320 psi\] pressure regulator (1) into the IFSM housing and tighten.
>
> **Момент затяжки · Torque Value**
> 27 n•m [239 in-lb]
>
> Install the o-rings (2 and 3) onto the pressure regulator (1).
>
> Install the 1724 kPa \[250 psi\] fuel pressure regulator into the IFSM housing and tighten.
>
> **Момент затяжки · Torque Value**
> 27 n•m [239 in-lb]
>
> Install the o-rings (2) onto the fuel pressure sensor (1).
>
> Install the fuel pressure sensor (1) into the IFSM housing and tighten.
>
> **Момент затяжки · Torque Value**
> 14 n•m [124 in-lb]
>
> **Note · Примечание**
> Some IFSMs contain an additional fuel pressure sensor.
>
> Install the air bleed (2) onto the air bleed orifice into the IFSM (1) through the opening for the Compuchek™ fitting.
>
> **Момент затяжки · Torque Value**
> 7.9 n•m [70 in-lb]
>
> Install the o-ring (2) onto the Compuchek™ fitting (1).
>
> Install both Compuchek™ fittings (1) into the IFSM housing and tighten.
>
> **Момент затяжки · Torque Value**
> 9.5 n•m [84 in-lb]
>
> Install the o-ring (2) onto the anti-drain back valve (1).
>
> Install the anti-drain back valve (1) into the housing and tighten.
>
> **Момент затяжки · Torque Value**
> 17 n•m [150 in-lb]
>
> Install the o-ring (2) onto the anti-drain back valve (1).
>
> Install the anti-drain back valve (1) for the fuel filter into the housing and tighten.
>
> **Момент затяжки · Torque Value**
> 17 n•m [150 in-lb]
>
> Install the filter screen (1), compression spring (2), o-ring (3), and filter cap (4) into the housing.
>
> **Момент затяжки · Torque Value**
> 17 n•m [150 in-lb]
>
> Install the o-ring seal (2) onto the fuel drain fitting (1).
>
> Install the fuel drain fitting (1).
>
> Turn the nut all the way to the top of the fitting.
>
> Thread the fitting all the way into the IFSM housing until it stops.
>
> Turn the fitting back until the threaded end is oriented directly over the regulator.
>
> Lock the fitting into position and tighten the locking nut.
>
> **Момент затяжки · Torque Value**
> 45 n•m [33 ft-lb]
>
> Maintain the correct orientation.
>
> Use a small amount of Lubriplate™ multi-purpose lubricant in the grooves on the bottom of the metering actuators (2).
>
> Install the actuator gasket (3) onto each actuator, making sure to align each properly.
>
> Install the actuators (2) onto the IFSM housing.
>
> Mount each actuator to the housing using three capscrews (1) and tighten the capscrews.
>
> **Момент затяжки · Torque Value**
> 15 n•m [133 in-lb]
>
> Use a small amount of Lubriplate™ multi-purpose lubricant in the grooves on the bottom of the timing actuators (2).
>
> Install the actuator gasket (3) onto each actuator, making sure to align each properly.
>
> Install the actuators (2) onto the IFSM housing.
>
> Mount each actuator to the housing using three capscrews (1) and tighten the capscrews.
>
> **Момент затяжки · Torque Value**
> 15 n•m [133 in-lb]
>
> Etch the same part number of the original IFSM on the data tag (1).
>
> Attach the tag to the housing by pressing the screws (2) into the housing.
>
> Install the seal (1) into the groove in the IFSM housing.
>
> Place the actuator disc (2) over the seal (1), small diameter down.
>
> Place the valve disc (3) onto the actuator disc (2) with the sealing surface down (spring pilot diameter up).
>
> Place the valve spring (4) into the actuator housing (5) with the inside diameter on the valve disc pilot (3).
>
> Place the actuator housing (5) over the actuator disc (2).
>
> Install the seal (1) into the groove in the actuator housing (5).
>
> Place the shutoff valve shield (6) over the actuator housing (5).
>
> Align the hole pattern of the shutoff valve shield (6).
>
> Place the solenoid (7) over the shutoff valve shield (6), taking care to align the holes and **not** pinch any seals. Orient the terminal facing the gear pump.
>
> Attach the assembly to the housing using four capscrews (8) and tighten using an “x” pattern.
>
> **Момент затяжки · Torque Value**
> 5.5 n•m [49 in-lb]
>
> Install the o-ring (2) onto the threaded plug (1).
>
> Install the three threaded plugs (1) into the housing.
>
> **Момент затяжки · Torque Value**
> 17 n•m [150 in-lb]
>
> Install the o-ring (4) onto the large threaded plug (3).
>
> Install the larger threaded plug (3) into the housing.
>
> **Момент затяжки · Torque Value**
> 14 n•m [124 in-lb]
>
> Install the o-ring onto the fuel supply fitting.
>
> Install the fuel supply fitting into the housing.
>
> **Момент затяжки · Torque Value**
> 27 n•m [239 in-lb]
>
> Install the o-ring onto the fuel inlet fitting.
>
> Install the o-ring (3) onto the fuel gear pump (2).
>
> Apply Lubriplate™ multi-purpose lubricant to the o-ring (3).
>
> Install the gasket (4) onto the gear fuel pump.
>
> Use four capscrews (1) and install the pump to the IFSM housing.
>
> **Момент затяжки · Torque Value**
> 11 n•m [97 in-lb]
>
> Install the lift pump gasket (1) onto the lift pump (2).
>
> Install the lift pump to the housing using three capscrews (3).
>
> **Note · Примечание**
> Some early engines were not equipped with a lift pump. These engines use a hand priming pump or they have been fitted with an auxilary lift pump.
>
> **Момент затяжки · Torque Value**
> 18 n•m [159 in-lb]
>
> ### Install
>
> Install two guide pins into the mounting holes on the cylinder head.
>
> Install a new gasket onto the guide pins.
>
> **WARNING · Опасно**
> This component or assembly weighs greater than 23 kg \[50 lb\]. To prevent serious personal injury, be sure to have assistance or use appropriate lifting equipment to lift this component or assembly.
>
> Install the IFSM on the guide pins.
>
> Install and tighten the capscrews.
>
> Remove the guide pins.
>
> Install and tighten the remaining capscrews.
>
> **Момент затяжки · Torque Value**
> 45 n•m [33 ft-lb]
>
> ### Finishing Steps
>
> Automotive with CM870 and CM871
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Install the accessory bracket. It is located above the IFSM. Refer to Procedure 001-082 in Section 1.
> - Install the ECM cooling plate fuel supply line (bottom) to the IFSM and ECM cooling plate fuel return line (top) to the fuel pump. Refer to Procedure 006-006 in Section 6.
> - Install the lift pump. Use the following procedure in the Troubleshooting and Repair Manual, CM870 Electronic Control System, Signature™ and ISX Engines, Bulletin 4021334. Refer to Procedure 019-396 in Section 19.
> - Install the customer accessory bracket. Tighten to 18 N•m \[159 in-lb\].
> - Connect the fuel supply and fuel drain lines. Refer to Procedure 006-024 in Section 6.
> - Install the EGR differential pressure sensor adapter. Refer to Procedure 011-028 in Section 11.
> - Install the EGR differential pressure sensor. Use the following procedure in the Troubleshooting and Repair Manual, CM870 Electronic Control System, Signature™ and ISX Engines, Bulletin 4021334. Refer to Procedure 019-370 in Section 19.
> - Install the EGR differential pressure sensor tubes. Refer to Procedure 011-026 in Section 11.
> - Connect the engine wiring harness to all temperature and pressure sensors, fueling and timing actuators, the fuel shutoff valve, the water-in-fuel sensor, and the fuel lift pump.
> - Connect the air intake connection. [[10-010-080-tr — Air Intake Connection|Refer to Procedure 010-080 in Section 10.]]
> - Connect the EGR mixer to the air intake connection. [[10-011-021-tr — EGR Mixer|Refer to Procedure 011-021 in Section 11.]]
> - Connect the battery cable. Refer to Procedure 013-009 in Section 13.
> - Install the fuel filter. [[10-006-015-tr — Fuel Filter (Spin-On Type)|Refer to Procedure 006-015 in Section 6.]]
> - Prime the fuel system.
> - Operate the engine to normal operating temperature and check for leaks.
>
> CM570
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Install the fuel filter. [[10-006-015-tr — Fuel Filter (Spin-On Type)|Refer to Procedure 006-015 in Section 6.]]
> - Connect the fuel supply and fuel drain lines. Refer to Procedure 006-024 in Section 6.
> - Install the customer accessory bracket. Tighten to 18 N•m \[159 in-lb\]).
> - Connect the air intake connection. [[10-010-080-tr — Air Intake Connection|Refer to Procedure 010-080 in Section 10.]]
> - Install the fuel control covers.
> - Connect the engine wiring harness from all pressure and temperature sensors, fueling and timing actuators, the fuel shutoff valve, the water-in-fuel sensor, and the fuel lift pump.
> - Connect the air inlet piping. [[10-010-080-tr — Air Intake Connection|Refer to Procedure 010-080 in Section 10.]]
> - Connect the battery cables. Refer to Procedure 013-009 in Section 13.
> - Operate the engine to normal operating temperature and check for leaks.
