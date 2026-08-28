---
aliases:
  - "Топливная система с электронным управлением"
type: "Процедура"
doc: "28-101-007"
title_en: "Electronic Controlled Fuel System"
title_ru: "Топливная система с электронным управлением"
modified: "2005-11-11"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "3810497"
figures: 42
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/28/28-101-007.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/28-101-007.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/28"
  - "перевод/машинный"
---

# Electronic Controlled Fuel System
**Топливная система с электронным управлением**

> [!abstract] Процедура · `28-101-007`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[3810497 — K38, K50, QSK38 and QSK50 Operation and Maintenance Manual|3810497]]
> **Секции:** Section 1 - Operating Instructions
> **Даты:** изменён 2005-11-11
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/28/28-101-007.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/28-101-007.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Центр

Система CENTRYTM представляет собой интеллектуальную электронную систему управления двигателем, предназначенную для оптимизации системы управления двигателем на горнодобывающей, строительной, сельскохозяйственной и другой внедорожной технике. Эта система может быть применена ко всем моделям двигателей, которые используют PT®, систему с временным давлением, топливную систему. Система CENTRYTM управляет скоростью двигателя и давлением топлива на основе ввода от электронного дроссельной заслонки и других специфических для оборудования и/или модели двигателя особенностей.

Система CENTRYTM состоит из гидромеханических и электронных подсистем. Электронная подсистема управляет доставкой топлива с использованием электронного клапана управления топливом (EFC), в то время как гидромеханическая подсистема обеспечивает максимальную защиту крутящего момента и скорости двигателя.

![[19801556.png]]

Электронная подсистема

Подсистема двигателя содержит:

1. ЭКМ
2. Главная струя двигателя
3. Датчик давления в топливной рампе
4. Двигатель Speed Sensor
5. Электронный клапан управления топливом (EFC).

![[19801566.png]]

Система CENTRYTM предназначена для электрических систем производителя оригинального оборудования (OEM) 12- и 24-VDC. Следующие компоненты отличаются между 12- и 24-VDC системами:

1. ЭКМ
2. Электронный контроль топлива (EFC)
3. Клапан отсечки топлива
4. Электронный привод управления синхронизацией шагов (STC) (при использовании)
5. Вспомогательный выключатель (при использовании).

![[19801567.png]]

Следующие компоненты одинаковы как в 12-, так и в 24-VDC системах:

1. Главная струя двигателя
2. Датчик давления в топливной рампе
3. Двигатель Speed Sensor
4. OEM Throttle Switch Interface.

![[19801568.png]]

ECM CENTRYTM загружен калибровкой, содержащей управление двигателем и информацию о конкретных приложениях OEM. Авторизованное место ремонта Cummins может перекалибровать ECM на оборудовании с помощью инструментария электронного обслуживания INSITETM, CompulinkTM или EcheckTM и базы данных и сети электронного программного обеспечения (ESDN). Некоторые корректировки могут быть сделаны с помощью инструментария для электронных услуг Cummins INSITETM, CompulinkTM или EcheckTM, когда используется картридж CENTRYTM.

![[19800109.png]]

Функции CENTRYTM, используемые в приложении, будут отображаться в инструментах для электронных услуг INSITETM, в режиме монитора CompulinkTM или EcheckTM и на экранах параметров просмотра. OEM и калибровка определяют, какие функции используются и какие параметры могут быть регулируемыми.

![[19800109.png]]

Основная проводка двигателя CENTRYTM содержит следующие соединения и предохранители:

1. Коннектор ECM
2. Электронный топливный контроллер (EFC) клапан 90° Connectors
3. Закрытие терминала клапан Ring
4. предохранители (5-ампер)
5. Интерфейс шины данных Engine-Side CAN Connector
6. Сенсор давления Rail Pressure Connector
7. OEM 9-контактный коннектор (C-5)
8. OEM 9-контактный коннектор (C-6)
9. Терминал наземного кольца CentryTM
10. Электронный терминал STC Ring Terminal (факультативно)
11. Двигатель Speed Sensor Connectors

> [!note] Примечание
> Расположения веток соединительной проводов ремня разъемной проводов различаются между семействами двигателей.

![[19801570.png]]

Гидромеханическая подсистема

Эта подсистема содержит:

1. Топливный насос

1А. Электронный модуль управления топливом

1Б. Резервный управляющий механика

1С. Управление воздушным топливом

2. Клапан отсечки топлива

3. Топливные трубки

4. Топливный блок (маунт датчика давления на железной дороге)

5. Шаг синхронизации контроля

6. форсунка.

![[19801557.png]]

Топливный насос является основной частью гидромеханической подсистемы, поскольку он обеспечивает давление топлива, контролируемое электронным клапаном управления топливом. Механический регулятор для топливного насоса обеспечивает резервное максимальное управление крутящим моментом двигателя и скоростью.

![[19801558.png]]

Управление воздушным топливом топливного насоса использует линию давления наддува турбокомпрессора для регулирования давления топлива, подаваемого в электронный клапан управления топливом. Управление воздушным топливом уменьшает черный дым и улучшает работу двигателя в условиях низкой нагрузки.

![[19801559.png]]

Контроль за воздушным топливом, установка NO-AIR - это максимальное давление рельсов топлива, которое топливный насос может подавать, когда на линии измерения давления наддува не обнаруживается давление наддува. Следующий график иллюстрирует типичную кривую перехода давления рельса против ускорения давления наддува. Управление воздушным топливом позволяет увеличить максимальное доступное давление на топливных рельсах по мере увеличения давления наддува.

![[19801560.png]]

Многие модели двигателей используют клапан отключения топлива, имеющий ручной винт переопределения. Включение этого винта перекрывает запорный клапан и/или системы отключения, подключенные к запорному клапану топлива.

> [!note] Примечание
> Этот винт не переопределяет электронный клапан управления топливом в системе CENTRYTM.

![[19801561.png]]

Система CENTRYTM использует топливный блок для обеспечения надежного расположения датчика давления на рельсах.

![[19801562.png]]

На моделях двигателей, использующих STC, некоторые двигатели будут использовать линию измерения давления топлива для управления гидромеханическим переключателем STC, а другие двигатели будут использовать систему CENTRYTM для переключения электронного соленоида STC.

Идентификация по ТТС:

1. Линия датчика давления топлива
2. Нефтяная линия к Таппетам
3. Нефтяная вентиляция
4. Линия поставок нефти
5. Провода привода CENTRYTM STC.

STC позволяет двигателю работать в продвинутом режиме впрыска сразу после запуска и в условиях легкой нагрузки двигателя и вернуться к нормальному времени во время средних и высоких условий нагрузки двигателя. Преимущества этой функции включают в себя:

- Улучшенные характеристики холостого хода
- Сниженный холодный белый дым
- Улучшенная экономия топлива при легкой нагрузке.

![[19801563.png]]

Гидромеханический STC позволяет использовать два различных режима впрыска, основанных на давлении рельсов топлива, обнаруженном на линии измерения давления топлива. Гистерезис обеспечивает максимальное давление на рельсах для двигателя, чтобы перейти от ADVANCEDTM к нормальному времени и минимальное давление на рельсах для перехода от нормального к ADVANCEDTM. Гистерезис предотвращает нестабильное и быстрое переключение режимов времени STC, когда двигатель работает при давлениях рельсов в диапазоне давления гистерезиса.

![[19801564.png]]

Электронный STC CENTRYTM также позволяет использовать два различных режима впрыска, основанных на измеренном давлении на рельсах и скорости двигателя. Однако CENTRYTM имеет возможность обеспечивать два различных набора точек переключения STC на рельсах выше и ниже калиброванной точки скорости двигателя. Это обеспечивает дальнейшую оптимизацию производительности двигателя с помощью STC. ECM обеспечивает 12- и 24-VDC электронному приводу STC, когда он управляет режимом времени ADVANCEDTM.

![[19801565.png]]

### Описание системы QSK

Промышленное применение

Топливная система QSK представляет собой систему с электронным управлением, предназначенную для оптимизации управления двигателем и снижения выбросов выхлопных газов. Топливная система QSK контролирует скорость двигателя и давление топлива на основе ввода от электрического дроссельного заслонка и других особенностей оборудования, специфичных для модели или обоих.

Промышленные применения топливных систем:

- Оптимизированный контроль двигателя
- Сокращение выбросов выхлопных газов.

![[05600069.png]]

INSITETM - это электронный инструмент для промышленных применений топливных систем. Используйте электронные сервисные инструменты INSITETM для:

- Информация, указанная владельцем программы в ECM (параметры и функции)
- Помощь в устранении неисправностей двигателя
- Измените мощность двигателя или калибровку номинальной скорости.

Свяжитесь с авторизованным местом ремонта Cummins для получения более подробной информации об этом инструменте.

![[19400357.png]]

Генерация электроэнергии

Система управления генераторным приводом представляет собой электронную систему управления, предназначенную для:

- Оптимизируйте управление двигателем.
- Уменьшить выбросы выхлопных газов.

Конструкция топливной системы QSK50 контролирует скорость двигателя и давление топлива с использованием электронных датчиков с системой QuantumTM.

Электронная система управления генерации электроэнергии имеет свой собственный электронный инструмент под названием INPOWERTM. INSITETM - это электронный сервисный инструмент, который может использоваться с двигателями генерации с электронным топливным форсункой. Инструменты для электронного обслуживания INPOWERTM можно приобрести через компанию Cummins Inc.

Свяжитесь с авторизованным местом ремонта Cummins для получения подробной информации об этих инструментах обслуживания:

- Неспособность
- Незащищенные.

INPOWERTM - это электронное средство обслуживания для систем управления генераторным приводом. Используйте инструмент электронного обслуживания INPOWERTM для:

- Информация, указанная владельцем программы в ECM (параметры и функции)
- Помощь в устранении неисправностей двигателя
- Измените мощность двигателя или калибровку номинальной скорости.

Свяжитесь с авторизованным местом ремонта Cummins для получения подробной информации об этом инструменте.

Функция регулировки электронного инструментария INPOWERTM позволяет вносить коррективы в параметры привода генератора для отделки и настроек. Существует несколько параметров регулировки. Не все генераторные установки будут иметь одинаковые настройки.

Режим монитора электронного сервиса INPOWERTM является полезным средством устранения неполадок, которое отображает ключевые входы и выходы ECM. Эта функция может использоваться для определения постоянных или аномально колеблющихся значений.

Входные данные ECM показывают данные, которые подаются в ECM датчиками и переключателями системы. Выходы ECM представляют собой значения, которые ECM командует системой управления генераторным приводом.

Режим монитора позволяет отслеживать и использовать взаимосвязь между входами и выходами ECM во время устранения неполадок.

Инструмент электронного сервиса INPOWER PROTM позволяет пользователю передавать новые или обновленные калибровочные файлы для системы управления генераторным приводом ECM из центрального местоположения в Cummins Inc. Дистрибьюторы.

Калибровочный файл — это электронные данные, которые дают двигателю его рейтинг производительности.

Калибровочный файл будет загружен в инструмент электронного сервиса INPOWERTM, который используется для загрузки файла в ECM.

Свяжитесь с авторизованным местом ремонта Cummins для получения более подробной информации об этом инструменте.

Функция тестирования электронного инструментария INPOWERTM представляет собой диагностический инструмент, который используется для выполнения внутренних самопроверок на управлении PowerCommandTM для проверки входов и выходов системы управления и функций защиты испытательного двигателя.

### Диагностические коды ошибок

Центр

Система CENTRYTM может отображать и записывать обнаруживаемые условия неисправности в своих системах и схемах. Желтая диагностическая лампа возле органов управления оператора будет освещена, когда система неисправности станет активной.

![[19801604.png]]

Лампа неисправности должна загораться в течение примерно 1 - 2 секунд после включения ключа, а затем выходить после того, как не было обнаружено неисправностей.

![[19802499.png]]

В то время как состояние неисправности обнаруживается, лампа неисправности включается или включается. CENTRYTM включает лампу для предупреждения неисправностей и ON FLASHING для более серьезных неисправностей, которые могут повлиять на работу двигателя и требуют немедленного внимания. Условия активного отказа должны быть исправлены как можно скорее.

![[19801605.png]]

Для определения активного кода неисправности CENTRYTM выключите двигатель и включите переключатель зажигания (двигатель **не** работает). Переключите диагностический переключатель в положение Включения в течение 1 - 2 секунд, а затем отпустите переключатель. Неисправная лампа будет освещаться, пока диагностический выключатель удерживается в положении Включения.

![[19801606.png]]

После выпуска диагностического выключателя наступает короткая пауза с последующим первым кодом неисправности. Коды ошибок CENTRYTM состоят из трех цифр с пятью вспышками для каждой цифры. Между каждой цифрой кода неисправности есть короткая пауза. После того, как три цифры мигнули и код известен, возникает более длительная пауза с последующим повторением одной и той же последовательности кода ошибки.

![[19801607.png]]

Переключение диагностического переключателя перейдет к следующему коду ошибки. После того, как все активные коды неисправностей будут отображены, последовательность вспышек кода неисправности будет повторяться, начиная с первого кода неисправности.

![[19801608.png]]

Запуск двигателя или поворот переключателя зажигания в положение выключения выключателя выведут из режима вспышки неисправности диагностики.

![[19801609.png]]

Промышленное применение

> [!note] Примечание
> Эта информация не относится к двигателям серии K38 и K50.

Топливная система промышленного применения может отображать и регистрировать определенные обнаруживаемые условия неисправности. Эти сбои отображаются в виде кодов неисправностей, что облегчает устранение неполадок. Коды неисправностей сохраняются в ECM.

Существует два типа кодов неисправностей:

- Коды неисправностей в электронной топливной системе двигателя
- Коды неисправностей системы защиты двигателя.

Все коды ошибок, записанные в протоколе, будут либо активными (код ошибок в настоящее время активен в двигателе), либо неактивными (код ошибок был активен в какой-то момент, но в настоящее время активен не является).

![[19400328.png]]

Активные коды неисправностей можно прочитать с помощью предупреждающих (янтарных) и останавливающих (красных) ламп в кабине.

Доступ к кодам активных неисправностей также можно получить с помощью инструментария электронного обслуживания INSITETM, Часть Номер 3824801.

Неактивные коды неисправностей могут быть прочитаны только с помощью инструментария электронного обслуживания INSITETM.

![[19400330.png]]

Когда замок зажигания автомобиля включается и диагностический выключатель выключается, лампы с кодом неисправности (красный, желтый и защита двигателя) будут освещаться в течение примерно 2 секунд, одна за другой, чтобы проверить их работу.

![[19400331.png]]

Свет будет выключен до тех пор, пока не будет записан код неисправности. Если стоп (красный) свет горит во время работы двигателя, неисправность может привести к отключению двигателя. Остановите двигатель как можно скорее.

Если лампа WARNING (янтарная) освещается, двигатель все еще может работать, но он может потерять некоторые системные функции, которые иногда могут привести к потере мощности. Неисправность должна быть исправлена, как только это удобно.

Система защиты двигателя записывает отдельные коды неисправностей, когда обнаруживается состояние вне зоны действия любого из датчиков в системе защиты двигателя.

Следующие датчики защиты двигателя будут доступны только с опцией электронной системы мониторинга двигателя CENSETM:

- Давление охлаждающего устройства двигателя
- Температура топлива
- Давление взрыва.

![[19400332.png]]

> [!note] Примечание
> Цвета ламп и этикетки будут варьироваться в зависимости от OEM.

Система защиты двигателя будет освещать лампу технического обслуживания (оранжевый), когда возникает вне диапазона.

![[19400334.png]]

Если лампа технического обслуживания двигателя освещается во время движения, это означает, что был записан код неисправности. Лампа будет оставаться подсвеченной до тех пор, пока происходит неисправность.

Лампа начнет мигать, если состояние продолжает ухудшаться. Мощность, скорость или и то, и другое будут постепенно снижаться. Если функция защиты двигателя включена, двигатель отключится, чтобы предотвратить повреждение.

![[19400335.png]]

Для проверки активных кодов неисправностей:

1. Переведите замок зажигания в положение OFF.
2. Переместить диагностический переключатель в положение ON.

> [!note] Примечание
> Некоторые OEM-производители используют шортинг-плагин.

![[19400336.png]]

Переключатель зажигания транспортного средства в положение Включения.

Если активные коды неисправностей не записаны, все три лампы будут освещаться и оставаться освещенными.

Если активные коды неисправностей будут записаны, все три лампы будут освещаться на мгновение. Предупреждающие (янтарные) и останавливающие (красные) лампы начнут мигать кодом зарегистрированной неисправности.

![[19400337.png]]

Код неисправности будет мигать в следующей последовательности:

1. Предупреждающая (янтарная) лампа будет мигать.
2. Вторая пауза с выключенными лампами предупреждения (янтарь) и остановки (красный).
3. Светильник STOP (красный) будет мигать записанным кодом неисправности с одной секундной паузой между цифрами.
4. Когда число перестанет мигать, загорится предупреждающая (янтарная) лампа.
5. Номер кода ошибки будет повторяться в той же последовательности.

![[19400338.png]]

Светильники будут продолжать мигать по тому же коду, пока система не будет переведена на следующий активный код.

Чтобы перейти ко второму коду неисправности, переключите переключатель настройки скорости холостого хода на положительный (+), затем отпустите его.

К предыдущему коду неисправности можно получить доступ, переместив переключатель в отрицательное (-) положение, а затем выпустив его.

Чтобы проверить третий или четвертый код неисправности, переведите переключатель в положительную (+) позицию, затем отпустите его.

Когда все активные коды неисправностей были просмотрены, переключение переключателя в положительную (+) позицию возвращает систему к первому коду неисправности.

Объяснение и исправление всех кодов неисправностей можно найти в таблицах устранения неполадок соответствующих электронных топливных систем и руководстве по устранению неисправностей и ремонту. Свяжитесь с авторизованным местом ремонта Cummins.

Электронный код неисправности деревьев находится в возрастающем численном порядке. Индекс находится в начале раздела.

![[19400339.png]]

> [!note] Примечание
> Некоторые OEM-производители используют шортинг-плаг

Чтобы остановить диагностическую систему, переведите диагностический переключатель в положение выключения.

Переключатель зажигания транспортного средства в положение выключения.

![[gp8swvv.png]]

Генерация электроэнергии

> [!note] Примечание
> Эта информация не относится к двигателям серии K38 и K50.

Система привода генератора может отображать и записывать определенные обнаруживаемые условия неисправности. Эти сбои отображаются в виде кодов неисправностей, что облегчает устранение неполадок. Коды неисправностей сохраняются в ECM.

Существует два типа кодов неисправностей. Существуют коды неисправностей электронной топливной системы двигателя и коды неисправностей системы защиты двигателя.

Все коды ошибок, записанные в системе, будут либо активными (код ошибки в настоящее время активен в двигателе), либо неактивными (код ошибки был активен в какой-то момент, но в настоящее время активен не является).

- Коды неисправностей в электронной топливной системе двигателя
- Коды неисправностей системы защиты двигателя.

Коды ошибок могут быть доступны тремя различными способами:

- Выключи свет
- Инструмент электронного обслуживания
- Панель интерфейса оператора.

![[19802544.png]]

Система управления генераторным приводом ECM имеет пять светодиодов для диагностики:

- OS - сверхскоростной
- LOP - низкое давление масла
- ET - высокая температура двигателя
- Закрытие - произошло отключение защиты двигателя
- Предупреждение - состояние предупреждения о защите двигателя существует.

Система управления генераторным приводом имеет восемь ретрансляторов для реле, поставляемых клиентами:

- OS - Overspeed
- LOP - низкое давление масла
- Высокий - высокая температура двигателя
- Закрытие - Закрытие системы защиты двигателя
- Предупреждение - состояние предупреждения о защите двигателя существует
- Преднизкое давление масла
- Предварительно высокая температура двигателя
- Не удалось начать.

![[19600091.png]]

Чтобы продемонстрировать код ошибки, ECM * должен быть введен в диагностический режим. Введите диагностический режим с помощью переключателя диагностического режима или соединив вместе два одноконтактных диагностических режима, включите разъемы. Во время нормальной работы ECM два разъема отсоединяются (открытая схема). ECM помещается в диагностический режим, когда эти два разъёма соединены вместе (короткая схема).

Предупреждающая лампа будет мигать (означая начало нового кода неисправности), а затем код неисправности будет мигать на выключаемой лампе.

![[19600090.png]]

Инструменты электронного сервиса могут использоваться для считывания кодов неисправностей. Подключите персональный компьютер с установленной электронной сервисной оснасткой к двигателю с помощью служебной проводов, номер детали 3163156.

Свяжитесь с авторизованным местом ремонта Cummins для получения подробной информации о том, как читать коды ошибок.

![[19800902.png]]

Если панель интерфейса оператора, поставляемая клиентом, была интегрирована с системой управления приводом генератора с использованием шины данных RS485 CAN, то доступна возможность считывать коды неисправностей.

Свяжитесь с авторизованным местом ремонта Cummins для получения подробной информации о том, как читать коды ошибок.

![[19802725.png]]

### Код ошибки Snapshot Data

Промышленная и энергетическая генерация

> [!note] Примечание
> Эта информация не относится к двигателям серии K38 и K50.

Когда диагностический код неисправности записывается в ECM, данные ввода и вывода ECM регистрируются со всех датчиков и коммутаторов. Данные снимка позволяют просматривать и использовать взаимосвязи между входами и выходами ECM во время устранения неполадок.

Чтобы очистить код ошибки:

* Неактивные коды неисправностей могут быть удалены. Единственный способ очистить неактивный код неисправности - использовать инструмент электронного сервиса.

Двигатель должен быть выключен для устранения неактивных неисправностей выключения.

Все коды ошибок, записанные в системе, будут либо активными (код ошибок в настоящее время активен в двигателе), либо неактивными (были активны в какой-то момент времени, но в настоящее время активны не были).

![[19400349.png]]

### Система защиты двигателя

Промышленная и энергетическая генерация

> [!note] Примечание
> Эта информация не относится к двигателям серии K38 и K50.

Все двигатели серии QSK50 оснащены системой защиты двигателя. Система контролирует критические температуры двигателя, уровни жидкости, положения переключателей и давления и регистрирует диагностические неисправности, когда происходит превышение или при нормальном рабочем диапазоне. Если вне диапазона условие существует, двигатель выпадения будет инициировано. Оператор будет предупрежден о включении лампы технического обслуживания в кабину. Предупреждающая лампа начнет мигать, когда состояние вне зоны действия будет продолжать ухудшаться, и произойдет отключение двигателя. Оператор должен тянуться к обочине дороги, когда это безопасно, чтобы уменьшить вероятность повреждения двигателя.

- Высокая температура охлаждающей жидкости двигателя
- Низкий уровень охлаждающей жидкости двигателя (факультативно)
- Низкое давление охлаждающей жидкости двигателя
- Высокая температура топлива
- Высокая температура коллектора впуска
- Низкое и очень низкое давление моторного масла
- Высокое давление.

Система защиты двигателя имеет три выбираемых функции. Если функция защиты двигателя выбрана, мощность и скорость двигателя будут постепенно снижаться в зависимости от уровня тяжести наблюдаемого состояния. Если функция защиты двигателя была выбрана, двигатель будет отключен. Если функция перезапуска двигателя была выбрана, двигатель может **не** быть запущен снова после отключения.

- Защита двигателя позволяет
- Защита двигателя отключена
- Защита двигателя возобновлена.


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> CENTRY™
>
> The CENTRY™ system is an intelligent electronic engine control system designed to optimize engine control system on mining, construction, agriculture, and other off-highway equipment. This system can be applied to all engine models that use the PT®, pressure timed, fuel system. The CENTRY™ system controls engine speed and fuel pressure based on input from the electronic throttle and other equipment-specific and/or engine-model-specific features.
>
> The CENTRY™ system consists of hydromechanical and electronic subsystems. The electronic subsystem manages fuel delivery using an electronic fuel control (EFC) valve while the hydromechanical subsystem provides backup maximum engine torque and speed protection.
>
> Electronic Subsystem
>
> The engine subsystem contains:
>
> 1. ECM
> 2. Main Engine Harness
> 3. Rail Pressure Sensor
> 4. Engine Speed Sensor
> 5. Electronic Fuel Control Valve (EFC).
>
> The CENTRY™ system has been designed for both 12- and 24-VDC original equipment manufacturer (OEM) electrical systems. The following components are different between 12- and 24-VDC systems:
>
> 1. ECM
> 2. Electronic Fuel Control (EFC)
> 3. Fuel Shutoff Valve
> 4. Electronic step timing control (STC) Actuator (if used)
> 5. Auxiliary Shutdown Device (if used).
>
> The following components are the same in both 12- and 24- VDC systems:
>
> 1. Main Engine Harness
> 2. Rail Pressure Sensor
> 3. Engine Speed Sensor
> 4. OEM Throttle Switch Interface.
>
> The CENTRY™ ECM is loaded with a calibration containing engine control and OEM application-specific information. A Cummins Authorized Repair Location can recalibrate an ECM on the equipment by use of the INSITE™ electronic service tool, Compulink™, or Echeck™, and the Electronic Software Database and Network (ESDN). Some adjustments can be made with the Cummins INSITE™ electronic service tool, Compulink™, or Echeck™, when a CENTRY™ cartridge is used.
>
> CENTRY™ features used in an application will be displayed in INSITE™ electronic service tool, Compulink™, or Echeck™ monitor mode and view parameter screens. The OEM and calibration will determine which features are used and which parameters can be adjustable.
>
> The CENTRY™ main engine harness contains the following connections and fuses:
>
> 1. ECM Connector
> 2. Electronic Fuel Control (EFC) Valve 90° Connectors
> 3. Fuel Shutoff Valve Ring Terminal
> 4. Fuses (5-amp)
> 5. Engine-Side Datalink Connector
> 6. Rail Pressure Sensor Connector
> 7. OEM 9-pin Connector (C-5)
> 8. OEM 9-pin Connector (C-6)
> 9. CENTRY™ Ground Ring Terminal
> 10. Electronic STC Ring Terminal (optional)
> 11. Engine Speed Sensor Connectors
>
> **Note · Примечание**
> Harness connector breakout locations differ between engine families.
>
> Hydromechanical Subsystem
>
> This subsystem contains:
>
> 1. Fuel Pump
>
> 1A. Electronic Fuel Control Module Assembly
>
> 1B. Backup Mechanical Governor
>
> 1C. Air-Fuel Control
>
> 2. Fuel Shutoff Valve
>
> 3. Fuel Tubes
>
> 4. Fuel Block (Rail Pressure Sensor Mount)
>
> 5. Step Timing Control
>
> 6. Injectors.
>
> The fuel pump is the main part of the hydromechanical subsystem because it supplies the fuel pressure controlled by the electronic fuel control valve. The mechanical governor for the fuel pump provides backup maximum engine torque and speed control.
>
> The fuel pump air-fuel control uses a turbocharger boost pressure line to regulate the fuel pressure supplied to the electronic fuel control valve. The air-fuel control reduces black smoke and improves engine performance during low-boost conditions.
>
> The air-fuel control, NO-AIR setting is the maximum fuel rail pressure that the fuel pump can supply when no boost pressure is detected on the boost pressure sensing line. The following graph illustrates a typical rail pressure versus boost pressure acceleration transition curve. The air-fuel control allows the maximum available fuel rail pressure to increase as boost pressure increases.
>
> Many engine models use a fuel shutdown valve having a manual override screw. Turning this screw in overrides the shutdown valve and/or shutdown systems connected to the fuel shutoff valve.
>
> **Note · Примечание**
> This screw does **not** override the electronic fuel control valve in the CENTRY™ system.
>
> The CENTRY™ system uses a fuel block to provide a solid location for the rail pressure sensor.
>
> On engine models that use STC, some engines will use a fuel pressure sensing line to control a hydromechanical STC switch and other engines will use the CENTRY™ system to switch an electronic STC solenoid.
>
> STC identification:
>
> 1. Fuel Pressure Sensing Line
> 2. Oil Line to the Tappets
> 3. Oil Vent Line
> 4. Oil Supply Line
> 5. CENTRY™ STC Actuator Lead Wire.
>
> The STC allows the engine to operate in advanced injection timing immediately after start-up and light-duty engine load conditions and to return to normal timing during medium and high engine load conditions. The benefits of this feature include:
>
> - Improved cold weather idling characteristics
> - Reduced cold weather white smoke
> - Improved light-load fuel economy.
>
> The hydromechanical STC allows two different injection timing modes based on fuel rail pressure detected on the fuel pressure sensing line. Hysteresis provides the maximum rail pressure for the engine to shift from ADVANCED™ to normal timing and minimum rail pressure for a shift from normal to ADVANCED™ timing. Hysteresis prevents unstable and rapid switching of STC timing modes when the engine is operating at rail pressures within the hysteresis rail pressure range.
>
> The CENTRY™ electronic STC also allows two different injection timing modes based on measured rail pressure and engine speed. However, CENTRY™ has the capability to provide two different sets of rail pressure STC switch points above and below a calibrated engine speed point. This provides further optimization of engine performance with STC. The ECM provides 12- and 24- VDC to the electronic STC actuator when it is commanding ADVANCED™ timing mode.
>
> ### QSK System Description
>
> Industrial Applications
>
> The QSK fuel system is an electronically controlled system designed to optimize engine control and reduce exhaust emissions. The QSK fuel system controls engine speed and fuel pressure, based on input from the electric throttle and other equipment-specific, model-specific, or both, features.
>
> Industrial applications fuel systems:
>
> - Optimized engine control
> - Reduced exhaust emissions.
>
> INSITE™ is an electronic service tool for the industrial applications fuel systems. Use INSITE™ electronic service tool to:
>
> - Program owner-specified information into the ECM (parameters and features)
> - Aid in troubleshooting the engine
> - Change the engine power or rated speed calibration.
>
> Contact a Cummins Authorized Repair Location for more specifics on this tool.
>
> Power Generation
>
> The generator-drive control system is an electronic control system designed to:
>
> - Optimize engine control.
> - Reduce exhaust emissions.
>
> The QSK50 fuel system design controls engine speed and fuel pressure utilizing electronic sensors with the Quantum™ system.
>
> The power-generation electronic control system has its own electronic tool called INPOWER™. INSITE™ is the **only** electronic service tool that can be used with power-generation engines with electronically actuated injectors. INPOWER™ electronic service tool can be purchased through Cummins Inc.
>
> Contact a Cummins Authorized Repair Location for specifics on the these service tools:
>
> - INPOWER™
> - INPOWER PRO™.
>
> INPOWER™ is an electronic service tool for the generator-drive control systems. Use the INPOWER™ electronic service tool to:
>
> - Program owner-specified information into the ECM (parameters and features)
> - Aid in troubleshooting the engine
> - Change the engine power or rated speed calibration.
>
> Contact a Cummins Authorized Repair Location for specifics on this tool.
>
> The INPOWER™ electronic service tool adjustment feature allows adjustments to be made to the generator-drive parameters for trims and settings. There are several adjustment parameters. **Not** all generator sets will have the same adjustments available.
>
> The INPOWER™ electronic service tool monitor mode is a useful troubleshooting aid that displays the key ECM inputs and outputs. This feature can be used to spot constant or abnormally fluctuating values.
>
> The ECM inputs show the data that is being fed into the ECM by the system's sensors and switches. The ECM outputs are values that the ECM commands to the generator-drive control system.
>
> The monitor mode allows the relationship between the ECM inputs and outputs to be monitored and used during troubleshooting.
>
> The INPOWER PRO™ electronic service tool allows the user to transfer new or updated calibration files for the generator-drive control system ECM from a central location to Cummins Inc. distributors.
>
> A calibration file is electronic data that gives the engine its performance rating.
>
> The calibration file will be loaded into the INPOWER™ electronic service tool, which is used to load the file into the ECM.
>
> Contact a Cummins Authorized Repair Location for more specifics on this tool.
>
> The INPOWER™ electronic service tool test mode feature is a diagnostic tool that is used to perform internal self-checks on the PowerCommand™ control to verify inputs and outputs of the control system and test engine protection functions.
>
> ### Diagnostic Fault Codes
>
> CENTRY™
>
> The CENTRY™ system can display and record detectable fault conditions within its systems and circuits. A yellow diagnostic lamp near the operator's controls will be illuminated when a system fault becomes active.
>
> The fault lamp should light for about 1 to 2 seconds after key-on, and then go out after no faults have been detected.
>
> While a fault condition is being detected, the fault lamp will turn ON or ON FLASHING. CENTRY™ will turn the lamp ON for warning faults, and ON FLASHING for more severe faults that can affect engine operation and need immediate attention. Active fault conditions **must** be corrected as soon as possible.
>
> To determine an active CENTRY™ fault code, shut off the engine and turn keyswitch on (engine **not** running). Toggle the diagnostic switch to the ON position for 1 to 2 seconds and then release the switch. The fault lamp will illuminate while the diagnostic switch is held in the ON position.
>
> After releasing the diagnostic switch, there is a short pause followed by the first fault code. CENTRY™ fault codes consist of three digits with up to five flashes for each digit. There is a short pause between each digit of the fault code. Once the three digits have flashed and the code is known, there is a longer pause followed by a repeating of the same fault code sequence.
>
> Toggling the diagnostic switch will advance to the next fault code. Once all active fault codes have been displayed, the fault code flash sequence will be repeated, starting from the first fault code.
>
> Starting the engine or turning the keyswitch to the OFF position will exit the diagnostic's fault flash mode.
>
> Industrial Applications
>
> **Note · Примечание**
> This information does **not** apply to the K38, K50 Series engines.
>
> The industrial application fuel system can display and record certain detectable fault conditions. These failures are displayed as fault codes, which make troubleshooting easier. The fault codes are retained in the ECM.
>
> There are two types of fault codes:
>
> - Engine electronic fuel system fault codes
> - Engine protection system fault codes.
>
> All fault codes recorded will either be active (fault code is presently active on engine) or inactive (fault code was active at some time, but is **not** presently active).
>
> Active fault codes can be read using the WARNING (amber) and STOP (red) lamps in the cab panel.
>
> The active fault codes can also be accessed using INSITE™ electronic service tool, Part Number 3824801.
>
> Inactive fault codes can **only** be read with the INSITE™ electronic service tool.
>
> When the vehicle keyswitch is turned on and the diagnostic switch is off, the fault code lamps (red, yellow, and engine protection) will illuminate for approximately 2 seconds, one after the other, to check their operation.
>
> The lights will remain off until a fault code is recorded. If a STOP (red) light illuminates while the engine is in operation, the fault can be engine-disabling. Stop the engine in a safe manner as soon as possible.
>
> If the WARNING (amber) lamp illuminates, the engine can still be operated, but it can lose some system features that can sometimes result in a power loss. The failure **must** be repaired as soon as it is convenient.
>
> The engine protection system records separate fault codes when an out-of-range condition is found for any of the sensors in the engine protection system.
>
> The following engine protection sensors will **only** be available with the CENSE™ electronic engine monitoring system option:
>
> - Engine coolant pressure
> - Fuel temperature
> - Blowby pressure.
>
> **Note · Примечание**
> Lamp colors and labels will vary by OEM.
>
> The engine protection system will illuminate the maintenance lamp (orange) when an out-of-range condition occurs.
>
> If the engine protection maintenance lamp illuminates while driving, it means that a fault code has been recorded. The lamp will remain illuminated as long as the fault is occurring.
>
> The lamp will begin to flash if the condition continues to get worse. The engine power, speed, or both, will be gradually reduced. If the engine protection shutdown feature is enabled, the engine will shut down to prevent damage.
>
> To check for active fault codes:
>
> 1. Turn the keyswitch to the OFF position.
> 2. Move the diagnostic switch to the ON position.
>
> **Note · Примечание**
> Some OEMs use a shorting plug.
>
> Turn the vehicle keyswitch to the ON position.
>
> If active fault codes are **not** recorded, all three lamps will illuminate and stay illuminated.
>
> If active fault codes are recorded, all three lamps will illuminate momentarily. The WARNING (amber) and the STOP (red) lamps will begin to flash the code of the recorded fault.
>
> The fault code will flash in the following sequence:
>
> 1. The WARNING (amber) lamp will flash.
> 2. A one second pause with both WARNING (amber) and STOP (red) lamps off.
> 3. The STOP (red) lamp will flash the recorded fault code with a one second pause between digits.
> 4. When the number has stopped flashing, the WARNING (amber) lamp will illuminate.
> 5. The fault code number will repeat in the same sequence.
>
> The lights will continue to flash the same fault code until the system has been advanced to the next active fault code.
>
> To advance to the second fault code, move the idle speed adjust switch to the positive (+), then release it.
>
> The previous fault code can be accessed by moving the switch to the negative (-) position, then releasing it.
>
> To check the third or fourth fault code, move the switch to the positive (+) position, then release it.
>
> When all active fault codes have been viewed, moving the switch to the positive (+) position will return the system to the first fault code.
>
> The explanation and correction of all fault codes can be found in the troubleshooting charts of the appropriate electronic fuel systems troubleshooting and repair manual. Contact a Cummins Authorized Repair Location.
>
> Electronic fault code troubleshooting trees are in ascending numerical order. An index is located at the beginning of the section.
>
> **Note · Примечание**
> Some OEMs use a shorting plug
>
> To stop the diagnostic system, move the diagnostic switch to the OFF position.
>
> Turn the vehicle keyswitch to the OFF position.
>
> Power Generation
>
> **Note · Примечание**
> This information does **not** apply to the K38, K50 Series engines.
>
> The generator-drive system can display and record certain detectable fault conditions. These failures are displayed as fault codes, which make troubleshooting easier. The fault codes are retained in the ECM.
>
> There are two types of fault codes. There are engine electronic fuel system fault codes and engine protection system fault codes.
>
> All fault codes recorded will either be active (fault code is presently active on the engine) or inactive (fault code was active at some time, but is **not** presently active).
>
> - Engine electronic fuel system fault codes
> - Engine protection system fault codes.
>
> Fault codes can be accessed in three different ways:
>
> - Flash out
> - Electronic service tool
> - Operator interface panel.
>
> The generator-drive control system ECM has five LEDs for diagnostics:
>
> - OS - overspeed
> - LOP - low oil pressure
> - HET - high engine temperature
> - Shutdown - engine protection shutdown has occurred
> - Warning - engine protection warning condition exists.
>
> The generator-drive control system has eight relay drivers for customer-supplied relays:
>
> - OS - Overspeed
> - LOP - Low oil pressure
> - HET - High engine temperature
> - Shutdown - Engine protection shutdown has occurred
> - Warning - Engine protection warning condition exists
> - Pre-low oil pressure
> - Pre-high engine temperature
> - Fail to start.
>
> To flash out a fault code, the ECM **must** be put into the diagnostic mode. Enter the diagnostic mode using the diagnostic mode switch or by connecting together the two single-pin diagnostic mode enable connectors. During normal ECM operation, the two connectors are disconnected (open circuit). The ECM is placed in diagnostic mode when these two connectors are joined together (short circuit).
>
> The warning lamp will flash (signifying the start of a new fault code), and then the fault code will flash out on the shutdown lamp.
>
> The electronic service tool can be used to read the fault codes. Connect a personal computer, with the electronic service tool installed, to the engine using the service harness, Part Number 3163156.
>
> Contact a Cummins Authorized Repair Location for specifics on how to read the fault codes.
>
> If the customer-supplied operator interface panel has been integrated with the generator-drive control system using the RS485 datalink, the ability to read the fault codes is available.
>
> Contact a Cummins Authorized Repair Location for specifics on how to read the fault codes.
>
> ### Fault Code Snapshot Data
>
> Industrial and Power Generation
>
> **Note · Примечание**
> This information does **not** apply to the K38, K50 Series engines.
>
> When a diagnostic fault code is recorded in the ECM, ECM input and output data are recorded from all sensors and switches. Snapshot data allow the relationships between ECM inputs and outputs to be viewed and used during troubleshooting.
>
> To Clear a Fault Code:
>
> **Only** inactive fault codes can be cleared. The **only** way to clear an inactive fault code is to use the electronic service tool.
>
> The engine **must** be shut down to clear inactive shutdown faults.
>
> All fault codes recorded will either be active (fault code is presently active on the engine) or inactive (was active at some time, but is **not** presently active).
>
> ### Engine Protection System
>
> Industrial and Power Generation
>
> **Note · Примечание**
> This information does **not** apply to the K38, K50 Series engines.
>
> All QSK50 series engines are equipped with an engine protection system. The system monitors critical engine temperatures, fluid levels, switch positions, and pressures and will log diagnostic faults when an over or under normal operating range condition occurs. If an out-of-range condition exists, engine derate action will be initiated. The operator will be alerted by the illumination of the in-cab maintenance lamp. The warning lamp will start to flash when an out-of-range condition continues to worsen and engine shutdown will occur. The operator **must** pull to the side of the road when it is safe to do so to reduce the possibility of engine damage.
>
> - High engine coolant temperature
> - Low engine coolant level (optional)
> - Low engine coolant pressure
> - High fuel temperature
> - High intake manifold temperature
> - Low and very low lubricating oil pressure
> - High blowby pressure.
>
> The engine protection system has three selectable features. If the engine protection enable feature has been selected, engine power and speed will be gradually reduced depending on the level of severity of the observed condition. If the engine protection shutdown feature has been selected, the engine will be shut down. If the engine restart feature has been selected, the engine can **not** be started again after shutdown.
>
> - Engine protection enable
> - Engine protection shut down
> - Engine protection restart.
