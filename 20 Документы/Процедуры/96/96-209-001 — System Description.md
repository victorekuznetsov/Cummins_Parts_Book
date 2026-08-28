---
aliases:
  - "Описание системы"
type: "Процедура"
doc: "96-209-001"
title_en: "System Description"
title_ru: "Описание системы"
modified: "2014-04-10"
engines:
  - "37292556"
  - "37295879"
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
  - "QST30"
manuals:
  - "3666231"
figures: 3
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-209-001.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/96-209-001.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "двигатель/QST30"
  - "группа/96"
  - "перевод/машинный"
---

# System Description
**Описание системы**

> [!abstract] Процедура · `96-209-001`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11, QST30
> **Входит в руководства:** [[3666231 — Centinel™ Master Repair Manual|3666231]]
> **Секции:** Section F - Familiarization
> **Даты:** изменён 2014-04-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-209-001.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/96-209-001.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Система CentinelTM представляет собой систему непрерывной замены масла электромеханической конструкции. Система CentinelTM может быть «интегрирована» (приобретена у завода) на выбранных моделях двигателей или «послепродажной» (переоборудована на существующие двигатели). Система CentinelTM расширяет интервалы изменения масла и масляного фильтра посредством непрерывного обмена маслами. Это достигается путем впрыскивания масла с контролируемой скоростью, пропорциональной потребленному топливу, в топливную систему для потребления. Масло макияжа вводится в двигатель со скоростью, равной потребляемой нефти. Это добавление масла происходит одним из двух способов. В одном случае имеется на борту танк с свежим маслом. Масло доставляется из этого резервуара клапаном CentinelTM в отстойник двигателя во время каждого цикла клапана. Система CentinelTM контролирует уровень масла в макияже. Во второй версии системы масло для макияжа добавляется вручную в отстойник моторного масла во время ежедневного профилактического обслуживания. Эта система только для сжигания предназначена только для тех операторов, которые имеют рутинную, ежедневную практику обслуживания.

> [!note] Примечание
> Система «только для ожога» отличается от стандартной системы CentinelTM. Стандартная система использует масляный бак для макияжа, чтобы постоянно пополнять масло, удаленное из двигателя через клапан управления маслом и сгоревшее. В системе только для сжигания нет масляного баллона; поэтому масло должно быть проверено и пополнено клиентом, добавив масло непосредственно в двигатель. Система CentinelTM предназначена для клиентов, которые ежедневно проверяют и поддерживают требуемый уровень моторного масла.

> [!note] Примечание
> Обе системы могут быть модифицированы для отвода отработанного масла в резервуар для улова для использования в районах, где действуют правила, которые не позволяют сжигать отработанное масло, а также с двигателями, которые используют оборудование для селективной каталитической редукции (SCR) после обработки. Эти модифицированные системы описаны как системы только для удаления и удаления и макияжа CentinelTM.

> [!note] Примечание
> Конфигурация двигателя CentinelTM запрещена для двигателей с высокой мощностью, которые используют SCR после обработки.

> [!note] Примечание
> Транспортные средства, имеющие местожительство в Калифорнии, могут не использовать любую систему (например, CentinelTM), которая смешивает использованное моторное масло с дизельным топливом (проверьте правила CARB).

### Теория операции

Клапаны управления маслом представляют собой электромеханические поршневые клапаны, которые обменивают используемое моторное масло на свежее масло (при использовании макияжного бака). Клапаны используют давление винтовки моторного масла для привода поршневого смещения. Для того чтобы модуль управления активировал систему, давление масляной винтовки **должно превышать заданное значение. Модуль управления запрограммирован для контроля давления масла и предотвращения работы до тех пор, пока давление масла не поднимется достаточно, чтобы привести в действие клапан. Модуль управления **не позволит клапану работать до истечения заданного периода времени (высокая мощность) или до достижения двигателем рабочей температуры 52°C[126°F] (тяжелая работа CELECTTM).

Система CentinelTM может **не** использоваться на установке, где давление возврата топлива выше 7 psi (14,3 рт. ст.)

> [!note] Примечание
> Ограничения на возврат топлива в двигатель могут быть меньше и должны быть проверены.

Двухпрофильная установка CentinelTM Oil Control клапан

Системы вторичного рынка используют двухпоршневой клапан управления маслом для управления обменом моторного масла. Горящий поршень вытесняет 34 куб.см моторного масла в линию возврата топлива, чтобы смешивать его с топливом в топливном баке. Поршень для макияжа вытесняет 17 куб.см свежего моторного масла в масляную поддон через блок двигателя, если используется макияжный бак. Клапан управления маслом может управлять порошком макияжа независимо от порошка ожога. Поршневой цикл макияжа дважды на каждый поршневой цикл ожога.

**Операция клапана управления маслом однопрофильного пинтонного центриналяTM**

Системы, которые используют однопоршневой клапан управления маслом, используют один поршень для управления обменом масла. Один конец поршня вытесняет 17 куб.см отработанного моторного масла на линию возврата топлива, в то время как другой конец поршня доставляет 17 куб.см свежего моторного масла в масляную поддон через блок двигателя, если используется макияж бака.

**Доступно несколько систем с различными типами CentinelTM**

Для систем послепродажного обслуживания с использованием двухпоршневого клапана имеется одна система для двигателей топливной системы K19/K38/50 PT® большой мощности, а другая для двигателей L10/M11/N14 CELECTTM большой мощности.

Они доступны как в 12, так и в 24 конфигурациях VDC. Для систем послепродажного обслуживания с использованием однопоршневого клапана имеется одна система для двигателя ISM в конфигурации 12 VDC. Для интегрированных систем имеется одна система для двигателя ISM в конфигурации 12 VDC и одна система для QSK45/60 в конфигурации 24 VDC.

В следующей таблице приведены конфигурации клапана управления маслом CentinelTM и модуля управления.

| Матрица продуктов CentinelTM |  |  |  |  |  |
|---|---|---|---|---|---|
| Семейство двигателей | Модуль управления | Нефтяной контрольный клапан |  |  |  |
| Высокомощный модуль управления CentinelTM | Модуль управления Heavy Duty CentinelTM | ECM (1) | Двойной пистолет | Одноместный поршень |  |
| L10/M11(2) |  | X |  | X |  |
| ИСМ |  |  | X |  | X |
| N14(2) |  | X |  | X |  |
| K19 |  | X |  | X |  |
| QSK19 |  |  | X |  | X |
| QST30 |  |  | X |  | X |
| K38 | X |  |  | X |  |
| QSK38 |  |  | X |  | X |
| QSK45 |  |  | X |  | X |
| К50 | X |  |  | X |  |
| QSK50 |  |  | X |  | X |
| QSK60 |  |  | X |  | X |
| QSK78 |  |  | X |  | X |
| ECM = модуль управления двигателем CELECTTM и электронные двигатели CELECTTM Plus |  |  |  |  |  |

> [!note] Примечание
> С дополнительной функцией управления клапаном управления маслом CentinelTM с помощью ECM можно использовать второе сцепление вентилятора или автоматическую передачу Spicer-2.

Ниже приведен список компонентов, которые производитель оригинального оборудования (OEM) должен будет поставить для интегрированной системы CentinelTM:

- Макияжный нефтяной бак.
- Дистанционный переключатель уровня масла для макияжа
- Шкаф и фитинги для сантехники от макияжного бака до клапана управления маслом, установленного на двигателе.

Или только для ожогов.

- Проводка жгута «джампер» от удаленного переключателя уровня масла до разъема OEM-интерфейса двигателя (31-контактный разъем для переключателя уровня масла).

Любая из этих систем может быть сконфигурирована для использования бортового макияжа или в качестве систем только для сжигания, в зависимости от конкретной установки.

Компоненты системы CentinelTM показаны в «Структурах тит» и «Системных диаграммах» в конце этого раздела.

Система CentinelTM предназначена для поддержания качества масла в приемлемом диапазоне. Анализ масла необходим для контроля производительности двигателя и системы Centinel.[[3810340 — Cummins® Engine Oil and Oil Analysis Recommendations|Рекомендации по анализу моторного масла и масла Cummins®, Бюллетень 3810340,]]Обычно применяется, но  должно быть изменено и расширено для работы CentinelTM.

Используйте следующие процедуры для рекомендаций по свойству масла CentinelTM.[[96-018-017 — Lubricating Oil System|См. процедуру 018-017 в разделе V.]]Анализ используемого масла может помочь контролировать состояние двигателя при просмотре с пониманием системы CentinelTM и руководящих принципов.[[96-007-083 — Lubricating Oil and Filter Analysis|См. процедуру 007-083 в разделе 7.]]

### Вводы модуля управления

**Переключение на низкий уровень масла**

Модуль управления CentinelTM требует цифрового датчика уровня контакта с открытым/закрытым экраном, чтобы определить, есть ли в макияже масло. Если модуль управления CentinelTM считывает закрытый контакт с датчика, то макияж считается полным масла. Если контакт датчика открыт, то емкость для макияжа считается низкой. В этих условиях индикатор красного диагностического света будет мигать непрерывно, что указывает на низкий уровень макияжа. После заполнения до такой степени, что вход сигнала датчика высок, индикатор красной диагностической лампы перестанет мигать.

Этот переключатель обнаруживает низкое содержание масла в макияже CentinelTM.

Этот переключатель имеет две позиции: Ойл ДЕТЕКТИРОВАН и НЕОЙЛ НЕ ДЕТЕКТИРОВАН. Когда переключатель находится в положении OIL DETECTED, система CentinelTM работает нормально. Когда переключатель помещается в положение НЕ ДЕТЕКТОРНОГО НЕФТИ, код неисправности активируется, и система CentinelTM прекращает измерение моторного масла. Метерирование возобновляется, когда переключатель возвращается в позицию, защищенную от нефти.

Этот переключатель может быть любым из нескольких устройств, обычно используется магнитный переключатель SPST или поплавковый переключатель. Переключатель определен в следующей таблице. При использовании выключателя с физическими контактами рекомендуется получать надежные переключения при низких напряжениях и токах, но серебряные контакты приемлемы, если выключатель герметичен.

Используйте следующую процедуру для спецификаций переключателя удаленного уровня масла.[[96-018-017 — Lubricating Oil System|См. процедуру 018-017 в разделе V.]]

![[07800041.png]]

Cummins® Supplied Oil Level Switch (переключатель уровня масла)

**Низкий уровень масла коммутатора стыковки Connector**

Этот разъем соединяется с приемлемым переключателем низкого уровня масла для системы CentinelTM. Этот разъем несет сигналы, которые позволяют обнаружить низкое содержание масла в макияже CentinelTM. Этот разъем необходим для интегрированных систем CentinelTM, если установлен переключатель низкого уровня масла.

![[07800042.png]]

Низкий уровень масла коммутатора стыковка

Это двухсторонний разъем PackardTM Metri-PackTM 150 Series. Разъем черный, чтобы отличить его от аналогичных разъемов с различной каймой. Терминалы - это жестяные штифты. Требуются кабельные уплотнения. Требуется вторичная блокировка (TPA) (ссылка на таблицу списка деталей коммутатора с низким уровнем масла).

K19, K38 и K50 Двигатели

Модуль управления CentinelTM большой мощности будет установлен на кронштейн крепления клапана CentinelTM. Модуль управления CentinelTM должен быть запрограммирован с помощью инструментария электронного сервиса INSITETM с правильными параметрами для вашего приложения. Модуль управления CentinelTM контролирует работу системы.

L10, M11 и N14 Двигатели

Модуль управления CentinelTM будет установлен на масляном баке или другом видимом месте. Модуль управления CentinelTM будет иметь один внешний интерфейсный разъем и один калибровочный/сервисный разъем. Разъем внешнего интерфейса представляет собой 12-контактный запечатанный разъем типа блокировки DeutschTM. Калибровочный/сервисный разъем представляет собой герметичный разъем PackardTM с 3-контактным разъемом и будет соединяться с соответствующим калибровочным разъемом. Модуль управления CentinelTM запрограммирован заранее и **не** запрограммирован с помощью инструментария электронного обслуживания INSITETM.

**ISM, QSK19, QST30, QSK38, QSK45, QSK50, QSK60 и QSK78 Двигатели**

Интегрированная система, используемая на двигателях ISM, QSK19, QST30, QSK38, QSK45, QSK50, QSK60 и QSK78, использует существующий двигатель ECM. После установки системы CentinelTM необходимо будет загрузить новый код ECM для активации клапана CentinelTM.

### Выходы модуля управления

K19, K38 и K50 Двигатели

Модуль управления CentinelTM контролирует работу системы. Если какие-либо параметры не будут выполнены, система отключится. Во время остановки модуль управления CentinelTM будет продолжать отслеживать используемое топливо и подсчитывать количество циклов пополнения масла, которые он пропустил. После того, как система будет введена в эксплуатацию, модуль управления CentinelTM будет составлять пропущенные циклы для поддержания качества масла или регистрации неисправности, что указывает на необходимость изменения масла. Любые неисправности CentinelTM зажигают диагностическую лампу, установленную на баке или в другом месте.

L10, M11 и N14 Двигатели

Если какие-либо параметры не будут выполнены, система отключится. Во время остановки модуль управления CentinelTM будет продолжать отслеживать используемое топливо и подсчитывать количество циклов пополнения масла, которые он пропустил. После того, как система будет введена в эксплуатацию, модуль управления CentinelTM будет составлять пропущенные циклы для поддержания качества масла или регистрации неисправности, указывающей на изменение масла. Любые неисправности CentinelTM зажигают диагностическую лампу, установленную на баке или в другом месте.

**ISM, QSK19, QST30, QSK38, QSK45, QSK50, QSK60 и QSK78 Двигатели**

Используя ECM двигателя, любые неисправности CentinelTM будут освещать лампы технического обслуживания (жидкости) и / или предупреждающие лампы на приборной панели или в другом месте (INSITETM также сможет считывать эти неисправности, и RoadRelayTM будет отображать их).

### Диагностические коды ошибок

**Интегрированные системы**

Интегрированная система CentinelTM установлена на двигателе и управляется электронным способом с помощью ECM. ECM контролирует время и количество ходов клапанов управления маслом в зависимости от рабочего цикла двигателя. При использовании ECM двигателя любые неисправности CentinelTM будут освещать лампы технического обслуживания (жидкости) и / или предупреждающие лампы на приборной панели или в другом месте. (Инструменты электронного сервиса InSITETM также смогут считывать неисправности, и RoadRelayTM будет их отображать.)

После выявления вины:

1. См. раздел TF.
2. Очистите код ошибки. Используйте соответствующее руководство по устранению неполадок и ремонту топливной системы.

**Послепродажная система с двумя поршнями**

Диагностический дисплей лампы прикреплен к масляному баку системы CentinelTM на двигателях большой мощности. Лампа является компонентом модуля управления CentinelTM и прикреплена к масляному баку для макияжа на тяжелых двигателях.

Для систем, предназначенных только для сжигания, есть две предупреждающие лампы. Они зеленого и красного цвета. Зеленая лампа указывает на то, что система CentinelTM имеет мощность и работает. Красная лампа указывает, что системный параметр **не** в пределах спецификации. Лампы должны быть установлены в месте, где их легко увидеть.

Если красная лампа освещена, поверните переключатель зажигания в положение выключения и обратно в положение Включения. Сразу же посмотрите на красную лампу. Он должен начать мигать трехзначным кодом. Этот код будет связан с кодом неисправности.

Коды гласят следующее:

1. Если красная лампа мигает три раза, то первая цифра - "3"; количество вспышек будет указывать первую цифру кода.
2. Будет пауза.
3. Если красная лампа мигает четыре раза, вторая цифра кода неисправности будет «4»; количество вспышек будет указывать вторую цифру кода.
4. Будет еще одна пауза.
5. Если красная лампа мигает два раза, то третья цифра кода — «2»; количество вспышек будет указывать на третью цифру кода.
6. В этом примере код 3-4-2. Код 342 неисправности - это ошибка калибровки модуля управления CentinelTM.

В этот момент будет более длительная пауза, прежде чем код ошибки будет проблескиваться снова. Этот процесс будет происходить четыре раза. После четвертого раза неисправность лампы остается красной, если она все еще активна. Чтобы снова прочитать код, поверните переключатель зажигания в положение выключения и обратно в положение Включения. Код снова будет мигать.

После того, как правильный код ошибки идентифицирован, перейдите в раздел TF этого руководства и начните устранение неполадок.

**Устранение активных ошибок**

#### Двигатели Heavy Duty

- Включите замок зажигания.
- Убедитесь, что двигатель не работает.
- Удалите калибровочную пробку.
- Установите сервисный штепсель.

> [!note] Примечание
> Подождите 2 минуты, чтобы установить служебную вилку, если установка сразу после выключения двигателя.

- Удалите плагин службы.
- Убедитесь, что все ошибки устранены.

> [!note] Примечание
> Сервисная вилка - это красная двухпроводная вилка.

#### Высокомощные двигатели

- Включите замок зажигания.
- Убедитесь, что двигатель не работает.
- Установите сервисный штепсель.

> [!note] Примечание
> Подождите 2 минуты, чтобы установить служебную вилку, если установка сразу после выключения двигателя.

- Удалите плагин службы.
- Убедитесь, что все ошибки устранены.

> [!note] Примечание
> Сервисная вилка - это красная двухпроводная вилка.

**Режим обслуживания**

Когда CentinelTM помещается в режим обслуживания, клапан управления маслом непрерывно цикличен независимо от расхода топлива.

Ниже приводится общая процедура установки модуля CentinelTM в режим обслуживания.

#### Двигатели Heavy Duty

- Выключите замок зажигания.
- Установлена калибровочная пробка.
- Включите замок зажигания.
- Запускай двигатель.
- Удалите калибровочную вилку и установите служебную вилку. Ищите зеленый светодиод для вспышки.

> [!note] Примечание
> Если двигатель остается работающим при попытке выйти из режима обслуживания, то для выхода из режима обслуживания может потребоваться до 4 минут.

Чтобы выйти из режима обслуживания, удалите служебную вилку и установите необходимую калибровочную вилку.

#### Высокомощные двигатели

- Выключите замок зажигания.
- Сервисный плагин **не** установлен.
- Включите замок зажигания.
- Запускай двигатель.
- Установите сервисный штепсель.

> [!note] Примечание
> Если двигатель остается работающим при попытке выйти из режима обслуживания, то для выхода из режима обслуживания может потребоваться до 4 минут.

Чтобы выйти из режима обслуживания, удалите плагин службы.

### Рекомендации по установке

> [!warning] ОСТОРОЖНО
> Сантехнический и макияжный резервуары, включенные в комплекты CentinelTM, могут быть недостаточными для использования во всех областях применения. Все применимые местные, государственные и федеральные правила и любые институциональные кодексы должны быть проверены, чтобы убедиться, что все компоненты соответствуют этим правилам и кодексам. Любой компонент, который не удовлетворяет каким-либо применимым правилам или коду, должен быть заменен компонентом, который удовлетворяет требованиям.

Клапан управления маслом предназначен для работы при -9 ° C \[16 ° F \] с моторным маслом 15W-40. Важно понимать, что клапан управления маслом может работать не так, как предполагалось, если вязкость масла превышает этот предел.

- Масляный бак Cummins® поставляется в двух размерах, четыре галлона и шесть с половиной галлонов полезной емкости.
- Расположение крышки макияжа должно быть легко доступно.
- Макияжный бак должен быть расположен так, чтобы визуальные проверки были легко выполнены.

Если клиент хочет приобрести или изготовить макияж, он должен содержать датчик низкого уровня масла. Конкретные требования к этому датчику подробно описаны в этом разделе. Кроме того, масляный бак для макияжа должен содержать фильтрованный вентиляционный отверстий в атмосферу.

**Двухместный пикап**

> [!note] Примечание
> Для конструкций кабины наддувной бак может **не** быть установлен на кабине/спящем из-за наклона кабины для обслуживания двигателя.

- Полный уровень резервуара для макияжа не может быть выше 8,2 метра[27 футов] над впускным соединением масляного клапана CentinelTM.
- Макияжный бак должен быть установлен таким образом, чтобы минимальный рабочий уровень масла был по крайней мере на 25,4 мм \[1 дюйм \] выше клапана CentinelTM, чтобы убедиться, что масло является гравитацией, подаваемой в систему CentinelTM.
- Нижняя часть резервуара для макияжа не может быть ниже впускного соединения для макияжа на клапане управления маслом.
- Типичными местами установки масляного баллона для макияжа на тяжелых грузовиках могут быть:
- Типичными местами установки масляного резервуара для макияжа на высоких лошадиных силах могут быть:

**Место установки одноместного пикапа**

> [!note] Примечание
> Для конструкций кабины наддувной бак может **не** быть установлен на кабине/спящем из-за наклона кабины для обслуживания двигателя.

- Полный уровень резервуара для макияжа может быть не выше 2,6 м \[8,5 футов \] над впускным соединением встроенного клапана управления маслом CentinelTM. Угловатость транспортного средства должна учитываться при определении местоположения танка.
- Макияжный бак должен быть установлен таким образом, чтобы минимальный рабочий уровень масла был по крайней мере на 25,4 мм \[1 дюйм \] выше клапана CentinelTM, чтобы убедиться, что масло является гравитацией, подаваемой в систему CentinelTM.
- Дно макияжного бака может быть не ниже 0,9 м \[3,0 фута\] ниже впускного соединения макияжа на интегрированном клапане управления маслом CentinelTM. Угловатость транспортного средства должна учитываться при определении местоположения танка. (Ссылка на таблицу 1.)
- Расстояние от масляного баллона до интегрированного клапана CentinelTM должно быть как можно короче.
- Типичными местами установки масляного баллона для макияжа на тяжелых грузовиках могут быть:

![[07800039.png]]

Таблица 1 Установка цистерн относительно впуска клапана для однопоршневой системы (танк должен быть расположен в пределах обозначенной области)

**Требования к дизайну (двойной и однопоршневой)**

> [!note] Примечание
> Предупреждение должно быть добавлено для внутреннего осмотра цистерны, если произошло повреждение.

- Предпочтительная конструкция макияжного бака представляет собой сегментированную часть топливного бака (см. выше ограничения высоты установки). Это дает много преимуществ:
- Танк **должен иметь внутреннюю стойку (или капельную трубку, в зависимости от расположения и конструкции танка). Эта трубка для стоянки или трубка для капель** должна быть спроектирована таким образом, чтобы предотвратить попадание мусора (осадка, грязи и т.д.) в линию макияжа. Трубка для поднятия трапа или трубка для сброса **должны** иметь по крайней мере 1/2-дюймовый зазор снизу макияжа.
- Танк может иметь слив в нижней части резервуара, чтобы обеспечить удаление осадка, грязи и т. Д. Это будет собираться в нижней части макияжа. Рекомендуется сливать этот резервуар каждые 4000 часов / 500 000 миль, чтобы удалить эти загрязняющие вещества.
- Минимальный внутренний диаметр для линии от макияжного резервуара до клапана управления маслом составляет 3/4 дюйма. Все фитинги должны быть размером для использования с этим минимальным требованием 3/4 внутреннего диаметра. Чем больше внутренний диаметр, тем лучше для холодного потока масла.
- В макияжном баке требуется босс для удаленного переключателя уровня масла. Этот переключатель **должен быть расположен так, чтобы при наличии в баке не менее 1/2 галлона полезного масла датчик активировался. Этот датчик **должен быть выше значения 1/2-дюймового зазора, данного ранее для трубки для подвода/подвода в макияже. Размер резьбы для босса зависит от используемого выключателя уровня масла.
- Танк должен быть выброшен. Этот вентиляционный отверстий должен быть спроектирован и расположен против мусора, поступающего через этот вентиляционный отверстий или вентиляционного отверстия, засоряемого мусором (грязью, грязью, снегом и т.д.).
- Аккумулятор должен быть спроектирован с пространством расширения для масла при его нагревании. Это пространство расширения должно составлять не менее 3% от объема танка.
- Размер бака должен быть основан на использовании топлива и желаемых милях перед заправкой макияжа. Помните, что емкость - это полезные галлоны в баке, а не общая емкость, и что использование масла зависит от использования топлива в автомобиле.
- Танк должен быть спроектирован таким образом, чтобы выдерживать не менее 124 кПа[18 psi]. При заправке макияжа необходимо использовать максимум 124 кПа[18 psi]. Танк может быть оборудован соединением для герметизации.
- Макияжный бак должен быть спроектирован так, чтобы можно было легко выполнить визуальную проверку или контрольную проверку уровня масла в баке. Если используется измерительная система, то она должна быть легко видимой для водителя и/или обслуживающего лица.
- Пластиковые макияжные резервуары, предназначенные для использования с системой послепродажного обслуживания CentinelTM, могут использоваться с интегрированной системой CentinelTM. Эти баки для макияжа Cummins® имеют размеры 15,1 литра \[4 галлона\] и 24,6 литра \[6,5 галлона\] полезного масла.
- Заполните шейный участок макияжа бака может иметь экран в трубке наполнителя, чтобы поймать любой мусор, который может войти в бак (например, грязь и т. Д.). который прикрепляется к колпаку. Размер экрана **должен** быть 100 х 100 сеток. Этот экран должен быть легко чистить. Не должен быть фильтр, установленный либо на линии между гримом/клапаном, либо на выходе из резервуара; это может привести к ограничениям на поток холодного масла.

**Поднять нос**

Макияжный шланг **должен **иметь минимальный внутренний диаметр 3/4 дюйма. Рекомендуется однотрубный усиленный устойчивый к погодным условиям шланг с внутренней трубкой из нефтестойкого нитрила или неопренового синтетического каучука. Устройство, соответствующее требованиям Общества инженеров автомобильной промышленности (SAE) 100R6 в соответствии с SAE J517, соответствует этой спецификации. Этот шланг должен быть разработан для использования с моторным маслом в диапазоне температур от -40 до +150°C \[-40 до +302°F\]. Он также должен работать при температуре воздуха до 70 ° C[158 ° F].

Рубль **не должен** протекать, лопаться или указывать на какие-либо признаки неисправности при воздействии максимального рабочего давления 300 psi или вакуума 15 рт.ст.

Все фитинги, имеющие кольца, должны иметь кольца, изготовленные из Витона®.


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The Centinel™ system is a continuous oil replacement system of electromechanical design. The Centinel™ system can be "integrated" (purchased from the factory) on selected engine models or "aftermarket" (retrofitted to existing engines). The Centinel™ system extends oil and oil filter change intervals through continuous oil exchange. This is accomplished by injecting oil at a controlled rate, proportional to fuel consumed, into the fuel system for consumption. Make-up oil is introduced into the engine at a rate equal to the oil consumed. This oil addition occurs in one of two ways. In one case there is an onboard fresh oil tank. Oil is delivered from this tank by the Centinel™ valve to the engine sump during each cycle of the valve. The Centinel™ system monitors the oil level in the make-up tank. In a second version of the system, make-up oil is added manually to the engine oil sump during the daily preventative maintenance process. This burn-only system is **only** for those operators who have routine, daily maintenance practices in place.
>
> **Note · Примечание**
> The burn-only system differs from the standard Centinel™ system. The standard system utilizes a make-up oil tank to continuously replenish oil removed from the engine via the oil control valve and burned. In the burn-only system, there is no make-up oil tank; therefore, oil must be checked and replenished by the customer by adding oil directly to the engine. The Centinel™ burn-only system is designed for customers who check and maintain required engine oil levels on a daily basis.
>
> **Note · Примечание**
> Both systems can be modified to divert used oil to a catch tank for use in areas that have regulations which do **not** allow for the burning of the used oil and with engines that utilize selective catalytic reduction (SCR) aftertreatment hardware. These modified systems are described as remove-only and remove and make-up Centinel™ systems
>
> **Note · Примечание**
> The burn configuration of Centinel™ is prohibited on high horsepower engines which utilize SCR aftertreatment.
>
> **Note · Примечание**
> Vehicles domiciled in California can **not** use any system (like Centinel™) that blends used engine oil with diesel fuel (check CARB regulations).
>
> ### Theory of Operation
>
> The oil control valves are electromechanical piston valves that exchange the used engine oil with fresh oil (if using a make-up tank). The valves use engine oil rifle pressure to drive piston displacement. In order for the control module to activate the system, the oil rifle pressure **must** exceed a predetermined value. The control module has been programmed to monitor the oil pressure and prevent operation until oil pressure rises enough to drive the valve. The control module will **not** permit the valve to operate until a predetermined time period has elapsed (high horsepower), or until the engine reaches its operating temperature of 52°C \[126° F\] (heavy duty CELECT™).
>
> The Centinel™ system can **not** be used on an installation where the fuel return pressure is higher than 7 psi (14.3 in Hg)
>
> **Note · Примечание**
> Engine fuel return restriction limits may be less and should be verified.
>
> **Dual-Piston Centinel™ Oil Control Valve Operation**
>
> Aftermarket systems use the dual-piston oil control valve to control the exchange of engine oil. The burn piston displaces 34 cc of engine oil into the fuel return line to be mixed with the fuel in the fuel tank. The make-up piston displaces 17 cc of fresh engine oil into the oil pan via the engine block, if using a make-up tank. The oil control valve can control the make-up piston independent of the burn piston. The make-up piston cycles twice for every burn piston cycle.
>
> **Single-Piston Centinel™ Oil Control Valve Operation**
>
> The systems that use the single-piston oil control valve use one piston to control the exchange of oil. One end of the piston displaces 17 cc of used engine oil to the fuel return line while the other end of the piston delivers 17 cc of fresh engine oil into the oil pan via the engine block, if using a make-up tank.
>
> **There are Several Distinct Centinel™ Systems Available**
>
> For aftermarket systems using the dual-piston valve, there is one system for the high horsepower K19/K38/50 PT® fuel system engines, and another for the heavy duty L10/M11/N14 CELECT™ engines.
>
> These are available in both 12 and 24 VDC configurations. For aftermarket systems using the single-piston valve, there is one system for the ISM engine in 12 VDC configuration. For integrated systems, there is one system for the ISM engine in a 12 VDC configuration and one system for the QSK45/60 in 24 VDC configuration.
>
> The following table summarizes the Centinel™ oil control valve and control module configurations.
>
> | Centinel™ Product Matrix |  |  |  |  |  |
> |---|---|---|---|---|---|
> | Engine Family | Control Module | Oil Control Valve |  |  |  |
> | High Horsepower Centinel™ Control Module | Heavy Duty Centinel™ Control Module | ECM (1) | Dual-Piston | Single-Piston |  |
> | L10/M11(2) |  | X |  | X |  |
> | ISM |  |  | X |  | X |
> | N14(2) |  | X |  | X |  |
> | K19 |  | X |  | X |  |
> | QSK19 |  |  | X |  | X |
> | QST30 |  |  | X |  | X |
> | K38 | X |  |  | X |  |
> | QSK38 |  |  | X |  | X |
> | QSK45 |  |  | X |  | X |
> | K50 | X |  |  | X |  |
> | QSK50 |  |  | X |  | X |
> | QSK60 |  |  | X |  | X |
> | QSK78 |  |  | X |  | X |
> | ECM = Engine Control Module CELECT™ and CELECT™ Plus electronic engines |  |  |  |  |  |
>
> **Note · Примечание**
> With the additional function of controlling the Centinel™ oil control valve by the ECM, a second fan clutch or Spicer automate-2 transmission can **not** be used.
>
> The following is a listing of components original equipment manufacturer (OEM)s will be required to supply for the integrated Centinel™ system:
>
> - Make-up oil tank.
> - Remote oil level switch for make-up tank
> - Hose and fittings for plumbing from make-up tank to oil control valve mounted on the engine.
>
> or, for burn-only.
>
> - Wiring harness "jumper" from remote oil level switch to engine OEM interface connector (31-pin connector for oil level switch).
>
> Any of these systems can be configured to use the onboard make-up tank or as burn-only systems, depending on the particular installation.
>
> The components of the Centinel™ system are shown in the "Kit Structures" and "System Diagrams" at the end of this section.
>
> The Centinel™ system is designed to maintain oil quality in an acceptable range. Oil analysis is required to monitor both the engine and Centinel™ system performance. [[3810340 — Cummins® Engine Oil and Oil Analysis Recommendations|The Cummins® Engine Oil and Oil Analysis Recommendations, Bulletin 3810340,]] generally apply, but **must** be modified and expanded for the Centinel™ operation.
>
> Use the following procedures for the Centinel™ oil property guidelines. [[96-018-017 — Lubricating Oil System|Refer to Procedure 018-017 in Section V.]] Used oil analysis can help monitor engine condition when viewed with the awareness of the Centinel™ system and the guidelines. [[96-007-083 — Lubricating Oil and Filter Analysis|Refer to Procedure 007-083 in Section 7.]]
>
> ### Control Module Inputs
>
> **Low Oil Level Switch**
>
> The Centinel™ control module requires a digital open/close contact level sensor to determine whether or **not** the make-up tank has oil in it. If the Centinel™ control module reads closed contact from the sensor, the make-up tank is deemed to be full of oil. If the sensor contact is opened, the make-up tank is deemed to be low. Under these conditions, the red diagnostic light indicator will flash continuously, indicating the make-up tank is low. Once filled to the point that the sensor signal input is high, the red diagnostic lamp indicator will stop flashing.
>
> This switch detects a low oil level condition in the Centinel™ make-up tank.
>
> This switch has two positions, OIL DETECTED and OIL NOT DETECTED. When the switch is in the OIL DETECTED position, the Centinel™ system operates normally. When the switch is placed into the OIL NOT DETECTED position, a fault code activates, and the Centinel™ system stops metering engine oil. Metering resumes when the switch is returned to the OIL DETECTED position.
>
> This switch can be any of several devices, an SPST magnetic or float-type switch is typically used. The switch is defined in the following table. When using a switch with physical contacts, gold-plated contacts are recommended to obtain reliable switching at low voltages and currents, but silver contacts are acceptable if the switch is hermetically sealed.
>
> Use the following procedure for the remote oil level switch specifications. [[96-018-017 — Lubricating Oil System|Refer to Procedure 018-017 in Section V.]]
>
> Cummins® Supplied Oil Level Switch
>
> **Low Oil Level Switch Mating Connector**
>
> This connector mates to the acceptable low oil level switch for the Centinel™ system. This connector carries signals that permit detection of a low oil level condition in the Centinel™ make-up tank. This connector is required for Centinel™ integrated systems if the low oil level switch is installed.
>
> Low Oil Level Switch Mating Connector
>
> This connector is a two-way Packard™ Metri-Pack™ 150 Series. The connector is black to distinguish it from similar connectors with different keying. Terminals are tin-plated pins. Cable seals are required. A secondary lock (TPA) is required (reference to Low Oil Level Switch Mating Connector Parts List table).
>
> **K19, K38, and K50 Engines**
>
> The high horsepower Centinel™ control module will be mounted to the Centinel™ valve mounting bracket. The Centinel™ control module **must** be programmed via INSITE™ electronic service tool with the correct parameters for your application. The Centinel™ control module monitors system operation.
>
> **L10, M11, and N14 Engines**
>
> The heavy duty Centinel™ control module will be mounted on the make-up oil tank or other visible location. The Centinel™ control module will have one external interface connector, and one calibration/service connector. The external interface connector is a 12 pin sealed Deutsch™ interlock-type connector. The calibration/service connector is a 3-pin Packard™ sealed connector and will mate with the matching calibration connector. The Centinel™ control module is pre-programmed and **not** programmed via INSITE™ electronic service tool.
>
> **ISM, QSK19, QST30, QSK38, QSK45, QSK50, QSK60, and QSK78 Engines**
>
> The integrated system used on ISM, QSK19, QST30, QSK38, QSK45, QSK50, QSK60, and QSK78 engines utilizes the existing engine ECM. Upon installation of the Centinel™ system, a new ECM code will need to be downloaded to activate the Centinel™ valve.
>
> ### Control Module Outputs
>
> **K19, K38, and K50 Engines**
>
> The Centinel™ control module monitors system operation. If any parameters are **not** met, the system will shutdown. During shutdown, the Centinel™ control module will continue to monitor fuel used and count the number of oil replenishment cycles that it missed. Once the system is put back into service, the Centinel™ control module will make up the missed cycles to maintain oil quality or log a fault, indicating an oil change is required. Any Centinel™ faults will light the diagnostics lamp mounted on the tank or elsewhere.
>
> **L10, M11, and N14 Engines**
>
> If any parameters are **not** met, the system will shutdown. During shutdown, the Centinel™ control module will continue to monitor fuel used and count the number of oil replenishment cycles that it missed. Once the system is put back into service, the Centinel™ control module will make up the missed cycles to maintain oil quality or log a fault indicating an oil change is required. Any Centinel™ faults will light the diagnostics lamp mounted on the tank or elsewhere.
>
> **ISM, QSK19, QST30, QSK38, QSK45, QSK50, QSK60, and QSK78 Engines**
>
> By using the engine's ECM, any Centinel™ faults will light the maintenance (Fluids) and/or warning lamps on the dash or elsewhere (INSITE™ will also be able to read these faults and RoadRelay™ will display them).
>
> ### Diagnostic Fault Codes
>
> **Integrated Systems**
>
> The integrated Centinel™ system is mounted on the engine and is electronically controlled by the ECM. The ECM controls the timing and number of oil control valve strokes based on the engine's duty cycle. By using the engine's ECM, any Centinel™ faults will light the maintenance (Fluids) and/or warning lamps on the dash or elsewhere. (INSITE™ electronic service tool will also be able to read faults and RoadRelay™ will display them.)
>
> Once fault is identified:
>
> 1. Refer to Section TF.
> 2. Clear the fault code. Use the appropriate fuel system troubleshooting and repair manual.
>
> **Aftermarket Dual-Piston Systems**
>
> The diagnostic lamp display is attached to the Centinel™ system make-up oil tank on high horsepower engines. The lamp is a component of the Centinel™ control module assembly and attached to the make-up oil tank on heavy duty engines.
>
> For burn-only systems, there are two warning lamps. They are green and red in color. The green lamp indicates that the Centinel™ system has power and is operating. The red lamp indicates that a system parameter is **not** within specification. The lamps **must** be mounted in a location where they can be easily seen.
>
> If the red lamp is illuminated, turn the keyswitch to the OFF position and back to the ON position. Immediately look at the red lamp. It should start flashing a three-digit code. This code will be associated with a fault code.
>
> The codes are read as follows:
>
> 1. If the red lamp flashes three times, the first digit is “3”; the number of flashes will indicate the first digit of the code.
> 2. There will be a pause.
> 3. If the red lamp flashes four times, the second digit of the fault code will be “4”; the number of flashes will indicate the second digit of the code.
> 4. There will be another pause.
> 5. If the red lamp flashes two times, the third digit of the code is “2”; the number of flashes will indicate the third digit of the code.
> 6. In this example, the code is 3-4-2. Fault Code 342 is a Centinel™ Control Module Calibration fault.
>
> At this point, there will be a longer pause before the fault code will be flashed again. This process will occur four times. After the fourth time, the fault lamp will stay red if the fault is still active. To read the code again, turn the key switch to the OFF position and back to the ON position. The code will flash again.
>
> Once the correct fault code is identified, go to Section TF of this manual and begin troubleshooting.
>
> **Clearing Active Faults**
>
> #### Heavy Duty Engines
>
> - Turn the keyswitch ON.
> - Make certain the engine is **not** running.
> - Remove the calibration plug.
> - Install the service plug.
>
> **Note · Примечание**
> Wait 2 minutes to install the service plug, if installing immediately after the engine is shut down.
>
> - Remove the service plug.
> - Verify that all the faults are cleared.
>
> **Note · Примечание**
> The service plug is a red, two-wired plug.
>
> #### High Horsepower Engines
>
> - Turn the keyswitch ON.
> - Make certain the engine is **not** running.
> - Install the service plug.
>
> **Note · Примечание**
> Wait 2 minutes to install the service plug, if installing immediately after the engine is shut down.
>
> - Remove the service plug.
> - Verify that all the faults are cleared.
>
> **Note · Примечание**
> The service plug is a red, two-wired plug.
>
> **Service Mode**
>
> When Centinel™ is placed into the service mode, the oil control valve is continuously cycling independent of fuel consumption
>
> The following is a general procedure for putting the Centinel™ module into the service mode.
>
> #### Heavy Duty Engines
>
> - Turn the keyswitch OFF.
> - Calibration plug installed.
> - Turn the keyswitch ON.
> - Start the engine.
> - Remove the calibration plug and install the service plug. Look for the green LED to flash.
>
> **Note · Примечание**
> If the engine is left running while attempting to exit the service mode, it can take up to 4 minutes to exit the service mode.
>
> To exit the service mode, remove the service plug and install the required calibration plug.
>
> #### High Horsepower Engines
>
> - Turn the keyswitch OFF.
> - Service plug **not** installed.
> - Turn the keyswitch ON.
> - Start the engine.
> - Install the service plug.
>
> **Note · Примечание**
> If the engine is left running while attempting to exit the service mode, it can take up to 4 minutes to exit the service mode.
>
> To exit the service mode, remove the service plug.
>
> ### Installation Recommendations
>
> **CAUTION · Осторожно**
> The plumbing and make-up tank included in the Centinel™ kits may not be adequate for use in all applications. All applicable local, state and federal regulations and any institutional codes must be consulted to make sure that all components satisfy these regulations and codes. Any component that does not satisfy any applicable regulation or code must be replaced with a component that does.
>
> The oil control valve is designed to perform at -9°C \[16°F\] with a 15W-40 engine oil. It is important to understand that the oil control valve can **not** operate as intended if the oil viscosity exceeds this limit.
>
> - The Cummins® supplied make-up oil tank comes in two sizes, four gallon and a six and one half gallon usable capacity.
> - The make-up tank fill cap location **must** be easily accessible.
> - The make-up tank **must** be located so that visual checks can be easily done.
>
> If a customer wishes to procure or fabricate a make-up tank, it **must** contain a low oil level sensor. The specific requirements for this sensor are detailed later in this section. Additionally, the make-up oil tank **must** contain a filtered vent to the atmosphere.
>
> **Dual-Piston Mounting Location**
>
> **Note · Примечание**
> For cab-over designs, the make-up tank can **not** be mounted on the cab/sleeper due to tilting of cab for engine servicing.
>
> - Full level of the make-up tank can be no higher than 8.2 meters \[27 feet\] above the make-up inlet connection of the Centinel™ oil control valve.
> - The make-up tank **must** be installed such that the minimum operating oil level is at least 25.4 mm \[1 inch\] above the Centinel™ valve to make sure that oil is gravity fed to the Centinel™ system.
> - Bottom of the make-up tank can be no lower than the make-up inlet connection on the oil control valve.
> - Typical mounting locations for the make-up oil tank on heavy duty trucks could be:
> - Typical mounting locations for the make-up oil tank on high horsepower applications could be:
>
> **Single-Piston Mounting Location**
>
> **Note · Примечание**
> For cab-over designs, the make-up tank can **not** be mounted on the cab/sleeper due to tilting of cab for engine servicing.
>
> - Full level of the make-up tank can be no higher than 2.6 meters \[8.5 feet\] above the make-up inlet connection of the integrated Centinel™ oil control valve. Vehicle angularity capability **must** be taken into consideration when locating the tank.
> - The make-up tank **must** be installed such that the minimum operating oil level is at least 25.4 mm \[1 inch\] above the Centinel™ valve to make sure that oil is gravity fed to the Centinel™ system.
> - Bottom of the make-up tank can be no lower than 0.9 meters \[3.0 feet\] below the make-up inlet connection on the integrated Centinel™ oil control valve. Vehicle angularity capability **must** be taken into consideration when locating the tank. (Reference to Table 1.)
> - Distance from make-up oil tank to integrated Centinel™ valve **must** be as short as possible.
> - Typical mounting locations for the make-up oil tank on heavy duty trucks could be:
>
> Table 1, Tank Installation Relative to Valve Inlet for Single-Piston System (tank must be located within the outlined area)
>
> **Design Requirements (dual- and single-piston)**
>
> **Note · Примечание**
> A warning **must** be added to inspect tank internally, if damage has occurred.
>
> - The preferred make-up tank design is as a segmented part of the fuel tank (see mounting height restrictions above). This offers many advantages:
> - The tank **must** have an internal standpipe (or drop tube, depending on tank location and design). This standpipe or drop tube **must** be designed to prevent debris (sediment, dirt, etc.) from entering into the make-up line. The standpipe or drop tube **must** have at least 1/2-inch clearance from bottom of the make-up tank.
> - The tank can have a drain in the bottom of the tank to allow for removal of sediment, dirt, etc. that will collect at the bottom of the make-up tank. It is recommended that this tank be drained every 4000 hours/500,000 miles to remove these contaminants.
> - Minimum inside diameter for line from make-up tank to the oil control valve is 3/4 inch. All fittings **must** be sized for use with this 3/4 inside diameter minimum requirement. The larger the inside diameter, the better for cold flow of oil.
> - A boss for a remote oil level switch is required in the make-up tank. This switch **must** be located so that when the tank has a minimum of 1/2 gallon of usable oil remaining, the sensor will activate. This sensor **must** be above the 1/2-inch clearance value given earlier for the standpipe/drop tube in the make-up tank. Thread size for boss is dependent on remote oil level switch used.
> - The tank **must** be vented. This vent **must** be designed and located against debris entering through this vent or the vent becoming plugged with debris (dirt, mud, snow, etc.).
> - The tank **must** be designed with an expansion space for the oil as it is warmed. This expansion space **must** be a minimum of 3 percent of the volume of the tank.
> - The tank sizing **must** be based on the fuel usage and desired miles before refilling the make-up tank. Remember that the capacity is the usable gallons in the tank, **not** overall capacity, and that oil usage is dependent on the fuel usage of the vehicle.
> - The tank **must** be designed to withstand at least 124 kPa \[18 psi\]. When priming the make-up system, a maximum of 124 kPa \[18 psi\] is to be used. The tank can be equipped with a connection for pressurization.
> - The make-up tank **must** be designed so that a visual check or gauge check of the oil level in the tank can be easily done. If a gauge system is used, then it **must** be easily visible to the driver and/or maintenance person.
> - The plastic make-up tanks designed for use with the aftermarket Centinel™ system can be used with the integrated Centinel™ system. These Cummins® aftermarket make-up tanks come in 15.1 liter \[4 gallon\] and 24.6 liter \[6.5 gallon\] usable oil sizes.
> - The fill neck section of the make-up tank can have a screen in the filler tube to catch any debris that can enter the tank (such as dirt, etc. that adheres to the cap). Screen size **must** be 100 x 100 mesh. This screen **must** be easy to clean. There **must not** be a filter installed either in the line between the make-up tank/valve or a filter at the outlet of the tank; these would cause restrictions for cold oil flow.
>
> **Make-Up Hose**
>
> The make-up hose **must** have a minimum 3/4 inch inside diameter. A single-braided reinforced weather-resistant hose with an inner tube of oil-resistant Nitrile or Neoprene synthetic rubber is recommended. Hose conforming to Society of Automotive Engineers (SAE) 100R6 in accordance with SAE J517 will meet this specification. This hose **must** be designed for use with lubricating oil within a temperature range of -40 to +150°C \[-40 to +302°F\]. It also **must** work in air temperatures up to 70°C \[158°F\].
>
> The hose **must not** leak, burst or indicate any sign of malfunction when subjected to a maximum working pressure of 300 psi or a vacuum of 15 in Hg.
>
> All fittings that have o-rings **must** have o-rings made of Viton®.
