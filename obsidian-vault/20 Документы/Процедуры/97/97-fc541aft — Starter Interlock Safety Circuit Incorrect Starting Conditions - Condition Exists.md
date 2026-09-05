---
type: "Процедура"
doc: "97-fc541aft"
title_en: "Starter Interlock Safety Circuit Incorrect Starting Conditions - Condition Exists"
modified: "2004-10-07"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
  - "80141463"
  - "80248213"
families:
  - "QSM11"
  - "QSX15"
manuals:
  - "3666415"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc541aft.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc541aft.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
  - "перевод/машинный"
---

# Starter Interlock Safety Circuit Incorrect Starting Conditions - Condition Exists

> [!abstract] Процедура · `97-fc541aft`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-10-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc541aft.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc541aft.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 541 (Послепродажное и OEM)

### Стартовый блок Схема безопасности Неправильные условия запуска - условие существует

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 541 PID(P): СПН: ФМИ: Лампа: СТО: | Стартерный блок безопасности цепи Неправильные условия запуска - Состояние существует. Сигнал **не** обнаруживается на входной цепи блокировки, когда ожидается, что модуль управления ICONTM не работает, в то время как система ICONTM активна, или система ICONTM обнаруживает скорость транспортного средства, когда переключатель стояночного тормоза закрыт. | Система ICONTM будет отключена. Обязательная остановка все еще может быть включена. Двигатель можно запускать нормально. |

![[19803824.png]]

### Описание цепи

Схема ввода блокировок обеспечивает вход в модуль управления холостым ходом ICONTM для определения состояния переключателей безопасности блокировок. Вышеупомянутая схема может варьироваться, например, разъем или штифты, в зависимости от марки или модели транспортного средства. Установки OEM могут обеспечить взаимодействие между модулем управления холостым ходом и другими устройствами ICONTM. Вышеупомянутая схема может варьироваться, например, разъем или штифты, в зависимости от марки или модели транспортного средства. Установки OEM могут обеспечить взаимодействие между модулем управления холостым ходом и другими устройствами ICONTM.

### Расположение компонента

Лампа ICONTM обычно расположена в кабине автомобиля на панели приборов. Переключатель стояночного тормоза или дополнительный тормозной переключатель прицепа обычно расположен за тире на линии сжатого воздуха стояночного тормоза. Выключатель наклона капота обычно расположен на капоте за корпусом фар. Переключатель нейтрального положения расположен на верхней крышке трансмиссии вблизи переключения передач. Модуль ICONTM может быть расположен в другом месте в зависимости от применения транспортного средства. Модуль ICONTM может быть расположен в другом месте в зависимости от применения транспортного средства.

### Практические замечания

Эта неисправность указывает на короткое замыкание батареи, переключатель блокировки был открыт, когда система ICONTM была активной, или скорость транспортного средства была больше 0 миль в час, в то время как переключатель стояночного тормоза был закрыт. Все переключатели блокировки должны быть закрыты, и лампа ICONTM функционирует до того, как система ICONTM будет включена, или двигатель будет работать, пока система ICONTM активна. Эти схемы применяются только тогда, когда включена система ICONTM.

Попросите водителя определить, была ли система ICONTM отключена из-за чрезмерной вибрации двигателя (запуск двигателя или выключение системы ICONTM).

Система ICONTM может отображать только текущий активный код неисправности. Если одновременно активируется более одного кода неисправности, система ICONTM выдает наиболее приоритетную ошибку. После того, как ошибка была исправлена, будет выброшена следующая активная ошибка.

**Примечание: **Электронная система ICONTM может отображать более одного активного и неактивного кода неисправности одновременно.

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
>

**Для уменьшения возможности повреждения штифта и проводов жгута проводов используйте при проведении измерений следующий испытательный щуп: Номер детали 3822758 - пробный щуп типа пробоотвода Deutsch/AMP/Metri-Pack Номер детали 3822917 - пробный щуп типа разъема Deutsch/AMP/Metri-Pack.**

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Интервью с водителем. |  |
|  | **ШАГ 1А.** Проведите собеседование с водителем, чтобы определить любые сценарии, которые могли вызвать неисправность. | Квалификационных событий не произошло |
| ШАГ 2. | Проверьте электронный модуль управления (ECM) для фазы калибровки. |  |
|  | **STEP 2A.** Проверить калибровку ECM. | Калибровка более 9.3 на ISM и Signature/ISX/QSX15; калибровка 4.2 на CELECTTM Plus |
|  | **ШАГ 2В.** Проверка на наличие активных неисправностей. | Код ошибки 541 активный |
| ШАГ 3. | Включите систему ICONTM. |  |
|  | **STEP 3A.** Проверить возможность включения системы ICONTM. | Система ICONTM может быть включена |
|  | **STEP 3B.** Мониторинг переключателей блокировки. | Ввод тормозов в парковку меняет статус |
|  | **STEP 3C** Проверить переход нейтрального переключателя. | Interlock (нейтральный и наклон капота) ввод изменения статуса |
| ШАГ 4. | Проверьте нейтральный переключатель. |  |
|  | **STEP 4A.** Проверьте нейтральный переключатель положения на наличие поврежденных контактов. | Никаких поврежденных контактов |
|  | **STEP 4B.** Проверить непрерывность в цепи переключателя нейтрального положения. | Менее 10 Ом |
|  | **STEP 4C.** Проверить, что нейтральный переключатель работает правильно. | В Гир: более 100 тыс. ом; в нейтральном: менее 10 Ом |
| ШАГ 5. | Проверьте выключатель наклона капота. |  |
|  | **STEP 5A.** Проверьте переключатель наклона капота на наличие поврежденных контактов. | Никаких поврежденных контактов |
|  | **STEP 5B.** Проверьте наличие открытой цепи в цепи переключателя наклона капота. | Менее 10 Ом |
|  | **STEP 5B-1.** Проверить непрерывность переключателя наклона капота на модуль ICONTM. | Менее 10 Ом |
|  | **STEP 5B-2.** Проверьте, работает ли выключатель наклона капота должным образом. | Hood open, 100k Ом; капот закрыт, менее 10 Ом |
| ШАГ 6. | Проверьте выключатель стояночного тормоза. |  |
|  | **ШАГ 6А.** Проверьте разъемы переключателей стояночного тормоза на наличие поврежденных контактов. | Никаких поврежденных контактов |
|  | **ШАГ 6В.** Проверить установку выключателя стояночного тормоза на линии стояночного тормоза. | Установка правильная |
|  | **STEP 6C.** Проверьте наличие открытой цепи в цепи стояночного тормоза. | Менее 10 Ом |
|  | **STEP 6D.** Проверьте наличие открытой цепи в цепи переключателя стояночного тормоза. | Менее 10 Ом |
|  | **ШАГ 6Е.** Проверьте, работает ли выключатель стояночного тормоза должным образом. | Выключатель стояночного тормоза отключен, более 100 км ом; включен выключатель стояночного тормоза, менее 10 ом |
| ШАГ 7. | Очистите код ошибки. |  |
|  | **STEP 7A.** Отключить код ошибки. | Код 541 ошибки обезврежен |

### ШАГ 1. Интервью с водителем.

#### ШАГ 1A. Проведите собеседование с водителем, чтобы определить любые сценарии, которые могли вызвать неисправность.

| **Условия: **Ни одно |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Машина была поставлена на передачу? Парковочный тормоз был отпущен? Открытый капот или оставленный открытым? Когда произошла ошибка? | Квалификационных событий не произошло | 2А |
| Исправьте проблему. | 8а |  |

### ШАГ 2. Проверьте электронный модуль управления (ECM) для фазы калибровки.

#### ШАГ 2A. Проверить калибровку ECM.

| **Условия:** Подключить электронный сервисный инструмент INSITETM. Включи зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте фазу калибровки ECM в режиме монитора. | Калибровка более 9.3 по ISM и калибровка 4.2 по подписи/ISX/QSX15 по CELECTTM Plus | 2В |
| Скачать последнюю калибровку ESDN | 7А |  |

#### ШАГ 2B. Проверьте наличие активных дефектов.

| **Условия:** Выключите замок зажигания. Подключите электронный сервис ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Прочитайте коды неисправностей с помощью инструментария электронного сервиса ICONTM или выключите неисправности с лампой ICONTM. Проверяйте, чтобы лампа ICONTM мигала три раза при включении переключателя зажигания (лампа не выгорала). | Код ошибки 541 активный | 3А |
|  | Соответствующие диаграммы устранения неполадок |  |

### ШАГ 3. Включите систему ICONTM.

#### ШАГ 3A. Проверить, может ли быть включена система ICONTM.

| **Условия:** Включена система ICONTM. Подключите электронный сервис ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Включите систему ICONTM и выполните по меньшей мере один автозапуск с термостатом кабины или загрузите батареи до менее чем 12,3 ВДК. | Система ICONTM может быть включена для очистки кодов неисправностей. | 7А |
| Система ICONTM может быть включена **не** | 3B |  |

#### ШАГ 3B. Мониторинг переключателей блокировки.

| **Условия: **Двигатель работает. Подключите электронный сервис ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
|  | Ввод тормоза парковки меняет статус. | 3C |
| Входные данные модуля управления ICONTM idle **not** | 6А |  |

#### ШАГ 3C. Проверить переход нейтрального переключателя.

| **Условия:** Выключите замок зажигания. Подключите электронный сервис ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Переключите передачу с подголовника на подголовник. Проверьте блокировку (нейтральный и наклон капота) в изменении состояния экрана монитора от проверенного до непроверенного. | Интерлок (нейтральный и наклон капота) ввод изменения состояния Примечание: Код 541 неисправности может быть вызван моментальным открытием переключателя из-за возможной вибрации. | 7А |
|  | 4А |  |

### ШАГ 4. Проверьте нейтральный переключатель.

#### ШАГ 4A. Проверьте нейтральный переключатель положения для поврежденных контактов.

| **Условия:** Выключите замок зажигания. Отсоедините разъем переключателя нейтрального положения от электропроводки двигателя ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Корродированные штифты Бент или сломанные штифты Отталкивание назад или расширенные штифты Проводная изоляция Повреждение Влажность в или на разъем Пропавшие или поврежденные соединительные штифты Коннекторная оболочка разбитая Грязь или мусор в или на разъемных контактах. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 4B |
| Ремонт поврежденных контактов, смывание грязи, мусора или влаги с соединительных контактов с помощью электрического контактного очистителя, номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт контактов разъёма переключателя нейтрального положения. См. процедуру 019-202 или 019-206. | 7А |  |

#### ШАГ 4B. Проверить непрерывность в цепи переключателя нейтрального положения.

| **Условия:** Выключите замок зажигания. Отсоедините разъемы ICONTM Idle Control Module A и B от модуля ICONTM idle Control. Установите стояночный тормоз. Закрой капот. Автомобиль в нейтральном состоянии. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление от контакта В разъема переключателя нейтрального положения контакту 2 с разъемом модуля управления ICONTM холостого хода B. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Менее 10 Ом | 4C |
| Ремонт или замена упряжки для проводов двигателя ICONTM Ремонт упряжки для проводов двигателя ICONTM. См. процедуру 019-206 или 019-207. Заменить электропроводку двигателя ICONTM. См. процедуру 019-043. По мере необходимости ремонтировать или заменять электропроводку OEM. | 7А |  |

#### ШАГ 4C. Убедитесь, что нейтральный переключатель работает правильно.

| **Условия:** Выключите замок зажигания. Отключите нейтральный переключатель положения. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление на переключателе с помощью передачи транспортного средства, а затем обратно в нейтральном положении. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | В Гир: Более 100 000 Ом в нейтральном состоянии: менее 10 Ом | 5а |
| Замените нейтральный переключатель. См. процедуру[[97-019-297 — Neutral Position Switch\|019-297]]. | 7А |  |

### ШАГ 5. Проверьте выключатель наклона капота.

#### ШАГ 5A. Проверьте выключатель наклона капота на поврежденные контакты.

| **Условия:** Выключите замок зажигания. Отсоедините разъем переключателя наклона капота от электропроводки двигателя ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Корродированные штифты Бент или сломанные штифты Отталкивание назад или расширенные штифты Проводная изоляция Повреждение Влажность в или на разъем Пропавшие или поврежденные соединительные штифты Коннекторная оболочка разбитая Грязь или мусор в или на разъемных контактах. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 5В |
| Ремонт поврежденных контактов. Промывайте грязь, мусор или влагу от контактов разъема с помощью электрического контактного очистителя, Номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт контактов разъема переключателя наклона капота. См. процедуру 019-202 или 019-206. | 7А |  |

#### ШАГ 5B. Проверьте наличие открытой цепи в цепи переключателя наклона капота.

| **Условия:** Выключите замок зажигания. Отсоедините разъем переключателя наклона капота от электропроводки двигателя ICONTM. Установите стояночный тормоз. Отключите нейтральный выключатель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление от контакта В вытяжного переключателя наклона проводов жгута разъёма к контакту А нейтрального положения переключателя разъёма. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Менее 10 Ом | 5В-1-1 |
| Ремонт или замена ремня электропроводки двигателя ICONTM. Ремонт ремня электропроводки двигателя ICONTM. См. процедуру 019-202 или 019-206. Заменить электропроводку двигателя ICONTM. См. процедуру 019-043. По мере необходимости ремонтировать или заменять электропроводку OEM. | 7А |  |

#### ШАГ 5B-1. Проверьте непрерывность переключателя наклона капота на модуль ICONTM.

| **Условия:** Выключите замок зажигания. Отключите переключатель наклона капота. Отключите разъем A модуля управления ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Менее 10 Ом | 5В-2-2 |
| Ремонт или замена ремня электропроводки двигателя ICONTM. Ремонт ремня электропроводки двигателя ICONTM. См. процедуру 019-202 или 019-206. Заменить электропроводку двигателя ICONTM. См. процедуру 019-043. По мере необходимости ремонтировать или заменять электропроводку OEM. | 7А |  |

#### ШАГ 5B-2. Проверьте, что переключатель наклона капота работает правильно.

| **Условия:** Выключите замок зажигания. Отключите переключатель наклона капота. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление через выключатель наклона капота с открытым капотом, а затем с закрытым капотом. **Примечание: **Переключатель **должен **закрываться и открываться, когда капот наклонен примерно на 45 ± 15 градусов. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Открой копыта: Более 100 000 омов Гуд закрыт: меньше 10 Ом Примечание: Незначительная корректировка переключателя может потребоваться, чтобы убедиться, что угол закрытия или открытия находится на 45 градусов. Отключение и повторное подключение разъема исправило проблему. | 7А |
| Замените выключатель наклона капота или внесите незначительные коррективы, чтобы переключатель закрылся или открылся должным образом и перепроверил. См. процедуру[[97-019-298 — Hood Tilt Switch\|019-298]]. | 7А |  |

### ШАГ 6. Проверьте выключатель стояночного тормоза.

#### ШАГ 6A. Проверьте разъемы переключателей стояночного тормоза на наличие поврежденных контактов.

| **Условия:** Выключите замок зажигания. Отключите выключатель стояночного тормоза от электропроводки кабины. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Корродированные штифты Бент или сломанные штифты Отталкивание назад или расширенные штифты Проводная изоляция Повреждение Влажность в или на разъем Пропавшие или поврежденные соединительные штифты Коннекторная оболочка разбитая Грязь или мусор в или на разъемных контактах. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 6B |
| Ремонт поврежденных контактов. Промывайте грязь, мусор или влагу от контактов разъема с помощью электрического контактного очистителя, Номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт контактов разъема парковочного тормоза. См. процедуру 019-202 или 019-206. | 7А |  |

#### ШАГ 6B. Проверьте установку выключателя стояночного тормоза на линии стояночного тормоза.

| **Условия:** Выключите замок зажигания. Отсоедините разъем переключателя стояночного тормоза от электропроводки кабины. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Убедитесь, что соединения плотные и нет утечек от линии, а давление воздуха в автомобиле превышает 83 кПа ± 21 кПа ± 3 psi с включенным стояночным тормозом. | Установка правильная | 6C |
| Установите выключатель стояночного тормоза. См. процедуру[[97-019-299 — Parking Brake Switch\|019-299]]. | 7А |  |

#### ШАГ 6C. Проверьте наличие открытой цепи в цепи переключателя стояночного тормоза.

| **Условия:** Выключите замок зажигания. Отсоедините разъемы ICONTM Idle Control Module A и B от модуля ICONTM idle Control. Установите стояночный тормоз. Отключите выключатель стояночного тормоза. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление от контакта 5 модуля управления ICONTM холостого хода A проводов жгута разъёма к контакту B разъема переключателя стояночного тормоза. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Менее 10 Ом | 6D |
| Ремонт или замена ремня электропроводки двигателя ICONTM. Ремонт ремня электропроводки двигателя ICONTM. См. процедуру 019-202 или 019-206. Заменить электропроводку двигателя ICONTM. См. процедуру 019-043. По мере необходимости ремонтировать или заменять электропроводку OEM. | 7А |  |

#### ШАГ 6D. Проверьте наличие открытой цепи в цепи переключателя стояночного тормоза.

| **Условия:** Выключите замок зажигания. Отключите выключатель стояночного тормоза. Отсоедините разъемы ICONTM Idle Control Module A и B от модуля ICONTM idle Control. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление от контакта А разъема жгута жгута парковочного тормоза к контакту 2 модуля управления холостым ходом ICONTM B разъема жгута жгута проводов. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Менее 10 Ом | 6Е |
| Ремонт или замена ремня электропроводки двигателя ICONTM. Ремонт ремня электропроводки двигателя ICONTM. См. процедуру 019-202 или 019-206. Заменить электропроводку двигателя ICONTM. См. процедуру 019-043. По мере необходимости ремонтировать или заменять электропроводку OEM. | 7А |  |

#### ШАГ 6E. Проверьте, работает ли выключатель стояночного тормоза должным образом.

| **Условия: **Двигатель работает. Автомобиль в нейтральном или парковом месте. Шоковые колеса. Отключите выключатель стояночного тормоза. Отсоедините разъемы ICONTM Idle Control Module A и B от модуля ICONTM idle Control. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление через выключатель стояночного тормоза с включенным и отключенным стояночным тормозом. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Выключатель тормоза парковки: Более 100 км/ч парковочный тормоз включает: Менее 10 Ом отключение и подключение устраняет проблему. | 7А |
| Замените выключатель стояночного тормоза. См. процедуру[[97-019-299 — Parking Brake Switch\|019-299]]. | 7А |  |

### ШАГ 7. Очистите код ошибки.

#### ШАГ 7A. Отключите код неисправности.

| **Условия: **Соединить все компоненты. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
|  | Код 541 ошибки обезврежен | Ремонт завершён |
| Устранение неполадок с оставшимися активными кодами неисправностей. | Соответствующие диаграммы устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 541 (Aftermarket and OEM)
>
> ### Starter Interlock Safety Circuit Incorrect Starting Conditions - Condition Exists
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 541 PID(P): SPN: FMI: Lamp: SRT: | Starter Interlock Safety Circuit Incorrect Starting Conditions - Condition Exists. Signal **not** detected on the interlock input circuit when expected by the ICON™ idle control module while the ICON™ system is active, or the ICON™ system detected vehicle speed while parking brake switch is closed. | The ICON™ system will be disabled. Mandatory shutdown can still be enabled. Engine can be started normally. |
>
> ### Circuit Description
>
> The interlock input circuit provides input to the ICON™ idle control module to determine the state of the interlock safety switches. The above circuit diagram can vary, such as connector or pins, depending on the vehicle make or model. OEM installations can possibly provide the harnessing between the idle control module and other ICON™ devices. The above circuit diagram can vary, such as connector or pins, depending on the vehicle make or model. OEM installations can possibly provide the harnessing between the idle control module and other ICON™ devices.
>
> ### Component Location
>
> The ICON™ lamp is typically located in the vehicle cab on the dash panel. The parking brake switch or optional trailer brake switch is typically located behind the dash on the parking brake air line. The hood tilt switch is typically located on the hood behind the headlight housing. The neutral position switch is located on the top cover plate of the transmission near the gear shift. The ICON™ module can be located in a different location depending on the vehicle application. The ICON™ module can be located in a different location depending on the vehicle application.
>
> ### Shoptalk
>
> This fault indicates a short circuit to battery, an interlock switch was opened while the ICON™ system was active, or vehicle speed was greater than 0 mph while the parking brake switch was closed. All interlock switches **must** be closed and the ICON™ lamp functional before the ICON™ system can be enabled, or for the engine to run while the ICON™ system is active. These circuits apply **only** when the ICON™ system is enabled.
>
> Question the driver to determine if the ICON™ system has been deactivating due to excessive engine vibration (engine being started or shutting down by the ICON™ system).
>
> The ICON™ system can display **only** the present active fault code. If more than one fault code is active at the same time, the ICON™ system flashes out the highest priority fault. After the fault has been corrected then the next active fault will be flashed out.
>
> **Note:** The ICON™ electronic service tool can display more than one active and or inactive fault codes at the same time.
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
>
> **To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch/AMP/Metri-Pack test lead Part Number 3822917 - female Deutsch/AMP/Metri-Pack test lead.**
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Interview the driver. |  |
> |  | **STEP 1A.** Interview the driver to determine any scenarios that could have caused a fault. | No qualifying events occurred |
> | STEP 2. | Check the electronic control module (ECM) for calibration phase. |  |
> |  | **STEP 2A.** Verify ECM calibration. | Calibration later than 9.3 on ISM and Signature/ISX/QSX15; Calibration 4.2 on CELECT™ Plus |
> |  | **STEP 2B.** Check for active faults. | Fault Code 541 active |
> | STEP 3. | Enable the ICON™ system. |  |
> |  | **STEP 3A.** Verify the ICON™ system can be enabled. | ICON™ system can be enabled |
> |  | **STEP 3B.** Monitor interlock switches. | Parking brake input changes status |
> |  | **STEP 3C.** Verify transition of neutral switch. | Interlock (neutral and hood tilt) input changes status |
> | STEP 4. | Check the neutral position switch. |  |
> |  | **STEP 4A.** Check the neutral position switch for damaged pins. | No damaged pins |
> |  | **STEP 4B.** Check for continuity in the neutral position switch circuit. | Less than 10 ohms |
> |  | **STEP 4C.** Verify the neutral switch is working properly. | In Gear: more than 100k ohms; In Neutral: less than 10 ohms |
> | STEP 5. | Check the hood tilt switch. |  |
> |  | **STEP 5A.** Check the hood tilt switch for damaged pins. | No damaged pins |
> |  | **STEP 5B.** Check for an open circuit in the hood tilt switch circuit. | Less than 10 ohms |
> |  | **STEP 5B-1.** Check the continuity of the hood tilt switch to the ICON™ module. | Less than 10 ohms |
> |  | **STEP 5B-2.** Verify the hood tilt switch is working properly. | Hood open, 100k ohms; hood closed, less than 10 ohms |
> | STEP 6. | Check the parking brake switch. |  |
> |  | **STEP 6A.** Check the parking brake switch connectors for damaged pins. | No damaged pins |
> |  | **STEP 6B.** Check the installation of the parking brake switch in the parking brake line. | Installation is correct |
> |  | **STEP 6C.** Check for an open circuit in the parking brake circuit. | Less than 10 ohms |
> |  | **STEP 6D.** Check for an open circuit in the parking brake switch circuit. | Less than 10 ohms |
> |  | **STEP 6E.** Verify the parking brake switch is working properly. | Parking brake switch disengaged, more than 100k ohms; parking brake switch engaged, less than 10 ohms |
> | STEP 7. | Clear the fault code. |  |
> |  | **STEP 7A.** Disable the fault code. | Fault Code 541 cleared |
>
> ### STEP 1. Interview the driver.
>
> #### STEP 1A. Interview the driver to determine any scenarios that could have caused a fault.
>
> | **Conditions:** None |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Was the vehicle placed in gear? Was the parking brake released? Was the hood opened or left open? When did fault occur? | No qualifying events occurred | 2A |
> | Correct the problem. | 8A |  |
>
> ### STEP 2. Check the electronic control module (ECM) for calibration phase.
>
> #### STEP 2A. Verify ECM calibration.
>
> | **Conditions:** Connect INSITE™ electronic service tool. Turn keyswitch on. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the ECM calibration phase in monitor mode. | Calibration later than 9.3 on ISM and Signature/ISX/QSX15 Calibration 4.2 on CELECT™ Plus | 2B |
> | Download latest ESDN calibration | 7A |  |
>
> #### STEP 2B. Check for active faults.
>
> | **Conditions:** Turn keyswitch OFF. Connect the ICON™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Read fault codes with the ICON™ electronic service tool or flash out the faults with the ICON™ lamp. Verify the ICON™ lamp flashes three times when keyswitch is turned on (lamp is not burned out). | Fault Code 541 active | 3A |
> |  | Appropriate troubleshooting charts |  |
>
> ### STEP 3. Enable the ICON™ system.
>
> #### STEP 3A. Verify the ICON™ system can be enabled.
>
> | **Conditions:** Enabled ICON™ system. Connect ICON™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Enable the ICON™ system and perform at least one autostart with cab thermostat or load batteries to less than 12.3 VDC. | ICON™ system can be enabled Clear the fault codes. | 7A |
> | ICON™ system can **not** be enabled | 3B |  |
>
> #### STEP 3B. Monitor interlock switches.
>
> | **Conditions:** Engine running. Connect the ICON™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> |  | Parking brake input changes status. | 3C |
> | ICON™ idle control module inputs are **not** active | 6A |  |
>
> #### STEP 3C. Verify transition of neutral switch.
>
> | **Conditions:** Turn the keyswitch OFF. Connect the ICON™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Move gear shift from in-gear to out-of-gear. Verify interlock (neutral and hood tilt) in monitor screen status changes from checked to unchecked. | Interlock (neutral and hood tilt) input changes status Note: Fault Code 541 can possibly have been caused by a momentary opening of the switch due to possible vibration. | 7A |
> |  | 4A |  |
>
> ### STEP 4. Check the neutral position switch.
>
> #### STEP 4A. Check the neutral position switch for damaged pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the neutral position switch connector from the ICON™ engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 4B |
> | Repair the damaged pins, Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the neutral position switch connector pins. Refer to Procedure 019-202 or 019-206. | 7A |  |
>
> #### STEP 4B. Check for continuity in the neutral position switch circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module A and B connectors from the ICON™ idle control module. Set the parking brake. Close the hood. Vehicle in neutral. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin B of the neutral position switch connector to pin 2 of the ICON™ idle control module B connector. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 10 ohms | 4C |
> | Repair or replace the ICON™ engine harness Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair or replace the OEM wiring harness as necessary. | 7A |  |
>
> #### STEP 4C. Verify the neutral switch is working properly.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the neutral position switch. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance across the switch with the vehicle in gear and then back in neutral. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | In Gear: more than 100k ohms In Neutral: less than 10 ohms | 5A |
> | Replace the neutral position switch. Refer to Procedure [[97-019-297 — Neutral Position Switch\|019-297]]. | 7A |  |
>
> ### STEP 5. Check the hood tilt switch.
>
> #### STEP 5A. Check the hood tilt switch for damaged pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the hood tilt switch connector from the ICON™ engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 5B |
> | Repair the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the hood tilt switch connector pins. Refer to Procedure 019-202 or 019-206. | 7A |  |
>
> #### STEP 5B. Check for an open circuit in the hood tilt switch circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the hood tilt switch connector from the ICON™ engine harness. Set the parking brake. Disconnect the neutral switch. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin B of the hood tilt switch harness connector to pin A of the neutral position switch connector. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 10 ohms | 5B-1 |
> | Repair or replace the ICON™ engine harness. Repair the ICON™ engine harness. Refer to Procedure 019-202 or 019-206. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair or replace the OEM wiring harness as necessary. | 7A |  |
>
> #### STEP 5B-1. Check the continuity of the hood tilt switch to the ICON™ Module.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the hood tilt switch. Disconnect the ICON™ idle control module connector A. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 10 ohms | 5B-2 |
> | Repair or replace the ICON™ engine harness. Repair the ICON™ engine harness. Refer to Procedure 019-202 or 019-206. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair or replace the OEM wiring harness as necessary. | 7A |  |
>
> #### STEP 5B-2. Verify the hood tilt switch is working properly.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the hood tilt switch. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance across the hood tilt switch with the hood open and then with the hood closed. **Note:** The switch **must** close and open when the hood is tilted to an approximately 45 ± 15 degree angle. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Hood open: more than 100k ohms Hood closed: less than 10 ohms Note: Minor adjustment to the switch can possibly be needed to make sure the close or open angle is at 45 degrees. Disconnecting and reconnecting the connector has corrected the problem. | 7A |
> | Replace the hood tilt switch or make minor adjustments so the switch will close or open properly and recheck. Refer to Procedure [[97-019-298 — Hood Tilt Switch\|019-298]]. | 7A |  |
>
> ### STEP 6. Check the parking brake switch.
>
> #### STEP 6A. Check the parking brake switch connectors for damaged pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the parking brake switch from the cab harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 6B |
> | Repair the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the parking brake switch connector pins. Refer to Procedure 019-202 or 019-206. | 7A |  |
>
> #### STEP 6B. Check the installation of the parking brake switch in the parking brake line.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the parking brake switch connector from the cab harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify that connections are tight and there are no leaks from the line and vehicle air pressure is greater than 83 kPa \[12 psi\] ± 21 kPa \[3 psi\] with the parking brake engaged. | Installation is correct | 6C |
> | Install the parking brake switch. Refer to Procedure [[97-019-299 — Parking Brake Switch\|019-299]]. | 7A |  |
>
> #### STEP 6C. Check for an open circuit in the parking brake switch circuit.
>
> | **Conditions:** Turn the keyswitch OFF. Disconnect the ICON™ idle control module A and B connectors from the ICON™ idle control module. Set the parking brake. Disconnect the parking brake switch. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 5 of the ICON™ idle control module A harness connector to pin B of the parking brake switch connector. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 10 ohms | 6D |
> | Repair or replace the ICON™ engine harness. Repair the ICON™ engine harness. Refer to Procedure 019-202 or 019-206. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair or replace the OEM wiring harness as necessary. | 7A |  |
>
> #### STEP 6D. Check for an open circuit in the parking brake switch circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the parking brake switch. Disconnect the ICON™ idle control module A and B connectors from the ICON™ idle control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin A of the parking brake switch harness connector to pin 2 of the ICON™ idle control module B harness connector. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 10 ohms | 6E |
> | Repair or replace the ICON™ engine harness. Repair the ICON™ engine harness. Refer to Procedure 019-202 or 019-206. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair or replace the OEM wiring harness as necessary. | 7A |  |
>
> #### STEP 6E. Verify the parking brake switch is working properly.
>
> | **Conditions:** Engine running. Vehicle in neutral or park. Chock wheels. Disconnect parking brake switch. Disconnect the ICON™ idle control module A and B connectors from the ICON™ idle control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance across the parking brake switch with the parking brake engaged and disengaged. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Parking brake switch disengaged: more than 100k ohms Parking brake switch engaged: less than 10 ohms Disconnecting and connecting fixes the problem. | 7A |
> | Replace the parking brake switch. Refer to Procedure [[97-019-299 — Parking Brake Switch\|019-299]]. | 7A |  |
>
> ### STEP 7. Clear the fault code.
>
> #### STEP 7A. Disable the fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> |  | Fault Code 541 cleared | Repair complete |
> | Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
