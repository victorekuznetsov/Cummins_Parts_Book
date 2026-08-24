---
aliases:
  - "Руководство по установке телематики PrevenTech™ Lite"
type: "Сервисный бюллетень"
doc: "5659895"
title_en: "PrevenTech™ Lite Telematics System Installation Manual"
title_ru: "Руководство по установке телематики PrevenTech™ Lite"
released: "2020-10-12"
modified: "2024-03-19"
group: "17 - Miscellaneous"
engines:
  - "33239746"
  - "33239899"
  - "41349633"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSK19"
figures: 20
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/5659895.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/bulletin/5659895.pdf"
tags:
  - "документ/бюллетень"
  - "двигатель/K38/K50"
  - "двигатель/QSK19"
  - "перевод/машинный"
  - "тема/miscellaneous"
---

# PrevenTech™ Lite Telematics System Installation Manual
**Руководство по установке телематики PrevenTech™ Lite**

> [!abstract] Сервисный бюллетень · `5659895`
> **Раздел Cummins:** 17 - Miscellaneous
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60, QSK19
> **Даты:** выпущен 2020-10-12 · изменён 2024-03-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/5659895.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/bulletin/5659895.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Руководство по установке телематики PrevenTech™ Lite

**Таблица содержимого**

- Системный и аппаратный обзор
- Установка
- Инструкции по установке: Оборудование PrevenTechTM Lite Telematics
- Аппендикс А: Спецификации Telematics Box Hardware
- Аппендикс Б: Примеры установки
- Аппендикс С: WIFI передача
- Аппендикс D: Заявление об отходах электрического и электронного оборудования

**Обзор систем и оборудования**

В данном руководстве подробно описывается установка телематической системы PrevenTechTM Lite. Хотя были предприняты усилия для того, чтобы сделать это руководство как можно более всеобъемлющим, установки ** должны быть адаптированы к конкретной модели применения/оборудования.

PrevenTechTM Lite Kit содержит следующее оборудование:

- Телематическая коробка PrevenTechTM Lite
- Сотовая/GPS/WIFI антенна
- Главная проводка
- Антенна монтажное оборудование

Набор PrevenTechTM Lite не содержит всего оборудования, необходимого для установки. SIM-карты и проводов подключения ** должны быть приобретены отдельно.

![[17r00859.png]]

Рисунок 1, PrevenTechTM Lite Kit Hardware

Экологические и физические требования к эксплуатации и хранению:

| **Таблица 1, Требования к эксплуатации и хранению** |  |
|---|---|
| ** Операция** | ** Хранение** |
| Операция "Температурный диапазон" | -5°C до +60°C (23°F до 140°F) |
| Диапазон температур хранения | -30°C до +80°C (86°F до 176°F) |
| влажность | До 95% - неконденсация |

**Предустановочные этапы**

Перед тем, как перенести аппаратное обеспечение PrevenTechTM Lite на сайт клиента, необходимо выполнить проверку стенда, чтобы убедиться, что система функциональна, а закупленная SIM-карта совместима с системой.

1. Зарегистрируйтесь, связавшись с командой CPS по адресу connectedsol.support@cummins.com. В поле PrevenTechTM Lite вы можете указать номера ID и IMEI. Также необходимы серийный номер двигателя (ESN), калибровка ECM, рейтинг hp, OEM / модель оборудования, номер блока, местоположение / минный сайт и информация о SIM-карте.

![[17r00860.png]]

Рисунок 2, Идентификационная этикетка на нижней части PrevenTechTM Lite Box

2. Удалите крышку телематической коробки и убедитесь, что выключатели SW2 выключены (внутреннее положение или влево, если разъём жгута проводов расположен сверху). Эти переключатели являются внутренними резисторами, которые не нужны.

> [!note] Примечание
> **Не меняйте коммутаторы на компоненте, обозначенном SW1, так как это предотвратит работу устройства.

![[17r00861.png]]

Рисунок 3, Интерьер PrevenTechTM Lite Box (Dip Switch Location Highlighted)

3. Закупить 4G GSM SIM-карту (размер Microsoft 3FF). Убедитесь, что в этом районе достаточно 4G. При активации карты требуется номер IMEI на этикетке коробки. Рекомендовать зарегистрировать клиента и оборудование и активировать доступ к www.preventech.cummins.com. Если клиент имеет **не** заказанные SIM-карты с активным планом данных, используйте совместимую SIM-карту с активированным планом данных для проверки работоспособности.

4. Установите SIM-карту с контактом лицом вниз и вырезанной вкладкой, обращенной к внешней стороне устройства.

![[17r00862.png]]

Рисунок 4, Интерьер люксовой коробки PrevenTechTM с установленной SIM-картой

5. Проверьте и убедитесь, что внутренние батареи установлены и подключены.

![[17r00863.png]]

Рисунок 5, внутренние батареи PrevenTechTM Lite

6. Подключите антенну к телематическому ящику и поместите в повышенное положение, чтобы получить сотовый сигнал.

7. Подключите проводку к коробке. Подключение VINPUT приводит к источнику питания 12/24 В, а GND приводит к отрицательному соединению. Примените силу. Через 5 минут зеленый свет должен быть устойчивым. Красный свет должен быть мигающим (2 секунды выключения - от 0 до 5 секунд Включения). Если красный свет устойчив, это означает, что нет связи сотовой связи. Если это происходит, обратитесь к приложению А для устранения неполадок.

8. Определить стратегию соединения автобусов J1939. Существует несколько способов подключения к двигателю J1939 CAN Bus. Выбранная стратегия определяет, какое периферийное оборудование необходимо заказать.

- Вариант 1: Автобус OEM J1939 CAN Bus

![[17r00864.png]]

Рисунок 6, CAN Bus Node

- Вариант 2: Расширьте магистраль двигателя до телематической коробки проводов ремня

![[17r00865.png]]

Рисунок 7, Расширение проводной узлы

Подключите канал CAN0 на проводах устройства.

9. Общее оборудование для установки не включено в комплект. Элементы, необходимые для выполнения полной установки, которые не включены в комплект. Эти элементы будут варьироваться в зависимости от типа приложения / модели.

- Зип-связь
- Владельцы предохранителей
- 3-амперный предохранитель
- Различные электрические терминалы / сплайсы прикладов
- Промышленный велькро
- Гландские орехи
- Дополнительный 18 AWG Wire (если требуется расширение проводов)

** Промышленные процедуры**

1. J1939 Public CAN Bus 3-Pin Connection (англ.) (недоступная ссылка).

- Двигатели и оборудование могут иметь несколько сетей CAN в своей архитектуре. Рядовой. Идентификация общественного автобуса J1939 CAN необходима до установки телематической коробки PrevenTechTM Lite. Чтобы проверить правильность выбранного CAN Bus, свяжитесь с OEM-оборудованием. В качестве альтернативы, проверьте непрерывность между выбранным 3-контактным разъемом и 9-контактным сервисным разъемом.

Проверить сопротивление автобуса J1939 CAN путем измерения между положительным и отрицательным терминалом на 9-пиновом разъеме службы (Pins C и D на рисунке ниже). Если измерение сопротивления составляет 120 Ом, в основу должен быть добавлен дополнительный конечный резистор ***. Если измерение сопротивления составляет менее 60 Ом, то резистор *** должен быть удален.

![[17r00866.png]]

Рисунок 8, контактная схема разъема

3. Установите коробку PrevenTechTM Lite Telematics.

- Место установки должно соответствовать следующим критериям окружающей среды:
- Mount Telematics box использует либо промышленный класс Velcro, либо монтажное оборудование. Обратите внимание, что если используется Velcro, то на задней панели коробки PrevenTechTM Lite будет нанесена идентификационная метка **не**. Эта информация может потребоваться позже для идентификации.

![[17r00867.png]]

Рисунок 9, Velcro, прикладываемый к задней панели телематической коробки PrevenTechTM Lite

4. Подключите проводку.

- Универсал PrevenTech Lite имеет несколько проводов, которые не используются в существующей конфигурации. Составьте следующие соединения:

![[17r00868.png]]

Рисунок 10, проводка упряжка упряжка ветка

- Подключите проводку к PrevenTechTM Lite Telematics Box, вставив разъем и нажав на вкладку блокировки.

![[17r00869.png]]

Рисунок 11, PrevenTechTM Lite Wiring Harness Connection to PrevenTechTM Lite Telematics Box

5. Установите антенну.

- Антенна GSM/GP/WIFI** должна быть установлена снаружи оборудования, с прямой линией обзора в небо.
- Установлено не менее 40 см от оператора оборудования.
- Рассмотрим стратегию маршрутизации жгута проводов и близость к PrevenTechTM Lite Telematics Box.
- Маршрутные антенные разъемы через прокладку, скобки и удерживающий гай.
- Обеспечить безопасность кронштейна и крепления с использованием двух U-болтов.
- Маршрутные антенные разъемы подключаются к коробке PrevenTechTM Lite Telematics и сопоставляют разъемы с правильным портом на коробке.

![[17r00870.png]]

Рисунок 12, Узлы для проводов антенны, подключенные к телематической коробке и горе антенны на внешней стороне приложения

- Создайте облегчение напряжения, разрешив по меньшей мере 1 фут кабеля между антенными портами и размещением рельефа напряжения.
- Безопасная проводка по маршруту с использованием P-Clips или Zip-связей. Избыточная проводка упряжки должна быть аккуратно свернута и закреплена, чтобы предотвратить вмешательство с другими компонентами.

6. Примените мощность и убедитесь, что светодиодные фонари включены в соответствии со следующими таблицами. Если светодиоды не дают надлежащего указания, обратитесь к приложению А для устранения неполадок.

- Зеленый светодиод включится примерно через 30 секунд после подачи питания. Если оборудование принимает кадры через порт CAN0, светодиод будет мигать на высокой скорости, указывающей на передачу.

| ** Зеленый индикатор светодиодов - CAN Operation** |  |
|---|---|
| ** Государство** | ** Указание** |
| Не останавливайся. | Система инициализированная |
| мигающий | Данные передаются по CAN0 |
| Остановиться | Операционная система не инициализируется |

- Красный светодиод используется для обозначения состояния связи устройства. В течение первых нескольких минут с момента питания устройства светодиод будет отключен. Если телематическая коробка не достигла подключения, светодиод будет постоянно светиться. В отличие от этого, если подключение 4G / GSM стабильно, светодиод будет мигать каждые 2 секунды.

| ** Красный светодиодный индикатор - сетевое подключение** |  |
|---|---|
| ** Государство** | ** Указание** |
| Не останавливайся. | Нет 4G/GSM соединения |
| Вспышка (2 секунды OFF - 0 до 0,5 секунд ON) | Стабильная связь 4G/GSM |
| Остановиться | Только первые пару минут после питания |

- Синий светодиод используется для обозначения состояния активности центрального процессора (CPU). В течение первых нескольких минут с момента запуска устройства светодиод будет отключен. Если Telematics box достигла подключения светодиода со флэш-памятью, зависящей от активности процессора. Напротив, если светодиодная коробка Telematics будет отключена, когда связь не будет достигнута.

| ** Синий светодиодный индикатор - CPU ** |  |
|---|---|
| ** Государство** | ** Указание** |
| Не останавливайся. | Система инициализации |
| Flashing (зависит от активности CPU) | CPU активность |
| Остановиться | Операционная система не инициализируется |

7. После проверки регистрации оборудования используйте приборную панель PrevenTechTM для проверки местоположения GPS и активации связи. Если связь не может быть установлена, выполните шаги по устранению неполадок или свяжитесь с Cummins CARE.

**APPENDIX A: Устранение неполадок**

ШАГ 1A. Проверьте неисправность видимости оборудования на приборной панели PrevenTechTM.

| ** Условия: ** В то время как оборудование включено |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Войдите на панель инструментов PrevenTechTM, https://preventech.cummins.com; Проверьте панель инструментов для работы | Видно ли оборудование на приборной панели? *Да** | **2A** |
| Видно ли оборудование на приборной панели? **Нет** | **1B** |  |

ШАГ 1B. Проверьте видимость другого оборудования на приборной панели PrevenTechTM.

| ** Условия**: Пока оборудование находится на |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверить приборную панель на предмет видимости другого оборудования | Видно ли другое оборудование на приборной панели? **Давайте не будем мешать с Dashboard | **2A** |
| Видно ли другое оборудование на приборной панели? **Нет** | ** Контакт: ** Региональная поддержка PrevenTechTM Контакт или care.cummins.com |  |

ШАГ 2. Определите состояние светодиодов.

ШАГ 2A. Зеленый светодиод мигает

| **Условия: ** В то время как оборудование включено **Примечание: ** через 30 секунд после подачи питания; зелёный светодиодный блок PrevenTechTM Lite Telematics начнет мигать на высокой скорости при приеме кадров через соединение PrevenTechTM Lite Telematics J1939 |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверить зеленый LED | Зеленый светодиод мигает? **Данные передаются на коробке PrevenTechTM Lite Telematics J1939; коробка PrevenTechTM Lite Telematics должна быть подключена к соединению J1939 двигателя, эталонный шаг **5A** | **2C** |
| Зеленый светодиод мигает? **Нет** | **2B** |  |

ШАГ 2B. Зеленый светодиод устойчивый

| Проверить зеленый LED | Зеленый светодиод устойчив? **Давайте заметим: ** Операционная система инициализирована | **5А** |
|---|---|---|
| Зеленый светодиод устойчив? **Примечание: ** Операционная система не инициализирована | **3A** |  |

ШАГ 2C. Красный светодиод мигает

| ** Условия: ** В то время как оборудование включено |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверить красный светодиод | Красный светодиод мигает? **Давайте поймем:** Стабильное подключение к Интернету | **Проверить информацию о конфигурации панели управления Контакт: ** Региональный контакт поддержки PrevenTechTM или care.cummins.com |
| Красный светодиод мигает? **Нет** | **2D** |  |

ШАГ 2D. Красный светодиод устойчивый

| **Условия:** При включении оборудования **Примечание:** Красный светодиод выключается в течение первых 5 минут после подачи питания в телематическую коробку PrevenTechTM Lite |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверить красный светодиод | Красный светодиод устойчив? **Да, нет подключения к Интернету | **6А** |
| Красный светодиод устойчив? **Нет** | **3A** |  |

ШАГ 2E. Синий LED Flashing

| ** Условия: ** В то время как оборудование включено |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверить синий LED | Синий светодиодный свет? *Да** | **************************************************************************************************************************************************************************************************************************************************************** |
| Синяя светодиодная вспышка? **Нет** | **2F** |  |

ШАГ 2F. Синий светодиод

| ** Условия:** При наличии оборудования |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверить синий LED | Синий светодиод выключен? **Нет** | ** Операционная система инициализацииRepair Complete** |
| Синий светодиод выключен? *Да** | **3A** |  |

ШАГ 3. Определить состояние электроснабжения.

> [!note] Примечание
> Коробка внутренней батареи картриджа PrevenTechTM Lite Telematics будет удерживать заряд в течение периода времени после того, как внешняя мощность будет удалена, и будет функционировать по назначению. При устранении неисправностей внешнего источника питания отключите коробку внутренней аккумуляторной батареи PrevenTechTM Lite Telematics. При необходимости обратитесь к шагу 4 для обнаружения неисправности внутренней батареи PrevenTechTM Lite Telematics, то есть к изменению времени печати данных на панели приборов PrevenTechTM.

ШАГ 3A. Состояние предохранителя

| ** Условия: ** В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверить встроенный предохранитель | Запал открыт? ** Да, ремонт: ** Заменить предохранитель | ** Ремонт завершен** |
| Запал открыт? **Нет** | **3B** |  |

ШАГ 3B. Электропитание, зажигание и состояние проволочного провода шасси

| ** Условия: ** В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Тщательно проверьте состояние основной проводов жгута проводов Справочное приложение H выше. | Являются ли подачу электроэнергии, зажигание и наземные провода шасси в хорошем состоянии без повреждений, т.е. Никаких слез? *Да** | **3C** |
| Являются ли провода питания, зажигания и заземления шасси в хорошем состоянии без повреждений? **NoRepair:** Заменить телематическую коробку PrevenTechTM Lite основной электропроводкой | ** Ремонт завершен** |  |

ШАГ 3C. Электропитание, зажигание и наземные соединения шасси

| ** Условия: ** В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Тщательно проверьте основные проводные соединения жгута | Подключены ли провода питания, зажигания и наземные провода шасси? *Да** | **3D** |
| Подключены ли провода питания, зажигания и наземные провода шасси? **NoRepair:** Подключите провод(ы), которые не подключены | ** Ремонт завершен** |  |

ШАГ 3D. Главная проводка подключения жгута к PrevenTechTM Lite Telematics box

| ** Условия: ** В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверить подключение к телематической коробке PrevenTechTM Lite. Справочный шаг 5 в инструкциях по установке: PrevenTechTM Lite Telematics Hardware выше. | Является ли основная проводка надежно подключена к телематической коробке PrevenTechTM Lite? *Да** | **3E** |
| Является ли основная проводка надежно подключена к телематической коробке PrevenTechTM Lite? **NoRepair:** Подключите и надежно заблокируйте основную проводку | ** Ремонт завершен** |  |

ШАГ 3E. Состояние внутренней проводов LED(s)

| **Условия:** При подаче питания в телематическую коробку PrevenTechTM Lite |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверить внутреннюю проводку LED(s), | Есть ли в них (или в них) светодиоды? **NoRepair:** Заменить телематическую коробку PrevenTechTM Lite | ** Ремонт завершен** |

ШАГ 4. PrevenTechTM Lite внутренние условия батареи

ШАГ 4A. Внутренние часы (круглые) аккумуляторные

| ** Условия: ** В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте временные метки приборной панели. | Есть ли неопределенность в штампе данных / часах реального времени? **Давайте заменим круглую батарею, ссылочный рисунок 5 выше. Включите устройство и проверьте панель инструментов PrevenTechTM на функциональность | ** Ремонт завершен** |

ШАГ 5. Оборудование J1939 Connection

ШАГ 5A. Проверить оборудование и подключение к телематической коробке PrevenTechTM Lite Telematics J1939

| ** Условия: ** В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверить связь PrevenTechTM Lite Telematics box J1939 с оборудованием | Подключен ли штекер PrevenTechTM Lite Telematics J1939 к общедоступному соединению данных J1939? *Да** | **5C** |
| Подключен ли штекер PrevenTechTM Lite Telematics J1939 к общедоступному соединению данных J1939? **Нет** | **5B** |  |

ШАГ 5B. Оборудование J1939 Public Connection

| ** Условия: ** В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Измерить непрерывность от 9-контактного сервисного разъема до 3-контактного разъема Deutsch | Подтверждена ли преемственность? **Подключите телематическую коробку PrevenTechTM Lite J1939 к общедоступным данным J1939 | ** Ремонт завершен** |
| Подтверждена ли преемственность? **Примечание:** Повторяйте этот шаг до тех пор, пока не будет установлено общественное соединение J1939 | ** Повторить шаг** |  |

ШАГ 5C. Измерить сопротивление оборудования

| ** Условия: ** В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Отключите соединение J1939; с помощью оборудования J1939 или 9 Pin сервисный разъем измеряет сопротивление оборудования, ссылочная фигура 8 выше. | Является ли измеренное сопротивление 60 Ом? *Да** | **5E** |
|  | Является ли измеренное сопротивление 60 Ом? **Нет** | **5D** |

ШАГ 5D. Осмотр резисторов магистральных терминалов J1939

| ** Условия: ** В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверить резисторы терминала связи J1939; измерить сопротивление. Примечание: Только два 120 Ом резистора, необходимых параллельно на магистрали для достижения общего сопротивления 60 Ом | Является ли измеренное сопротивление в каждом резисторе 120 Ом? *Да** | **5E** |
| Является ли измеренное сопротивление в каждом резисторе 120 Ом? **NoRepair:** Откажитесь от резистора (резисторов) и замените его (их) | ** Ремонт завершен** |  |

ШАГ 5E. Измерение сопротивления коробки PrevenTechTM Lite Telematics

| ** Условия: ** В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Измерить сопротивление на соединении PrevenTechTM Lite J1939, ссылочная фигура 8 выше. | Является ли измеренное сопротивление приблизительно 50 К-Ом? **Нет** | **5F** |
| Является ли измеренное сопротивление приблизительно 50 К-Ом? ** Да, нет проблемы сопротивления телематической связи PrevenTechTM Lite | ** Ремонт завершен** |  |

ШАГ 5F. PrevenTechTM Lite Телематика Коррекция сопротивления коробки

| ** Условия: ** В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Измерение сопротивления соединения PrevenTechTM Lite J1939 | Является ли измеренное сопротивление приблизительно 0 Ом? ** Дата выхода ** Короткое в коробке **Ремонт: ** Заменить PrevenTechTM Lite Telematics box | ** Ремонт завершен** |
| Является ли измеренное сопротивление приблизительно 120 Ом? ** Да, ремонт: ** Убедитесь, что переключатели внутреннего сопротивления находятся справа от батареи. Справочный шаг 13 в инструкциях по установке: PrevenTechTM Lite Telematics Hardware выше. | ** Ремонт завершен** |  |

ШАГ 6. Передача данных на приборную панель PrevenTechTM

ШАГ 6A. Антенны соединения

| ** Условия: ** В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверить антенные соединения в телематическом блоке PrevenTechTM Lite, ссылочный шаг 5 в Инструкции по установке: PrevenTechTM Lite Telematics Hardware выше | Являются ли провода антенн надежно и правильно соединены с телематическим блоком PrevenTechTM Lite? *Да** | **6B** |
| Являются ли провода антенн надежно и правильно соединены с телематическим блоком PrevenTechTM Lite? **NoRepair:** Правильно подсоедините антенные провода к правильным портам и надежно подключитесь. | ** Ремонт завершен** |  |

ШАГ 6B. Состояние антенных проводов

| ** Условия: ** В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверка проводов между телематическим ящиком PrevenTechTM Lite и круглым передатчиком антенн, ссылочный шаг 5 в Инструкции по установке: PrevenTechTM Lite Telematics Hardware выше | Повреждаются один или несколько антенных проводов, т.е. абразивный канал, круглое повреждение передатчика? ** Да, ремонт: ** Заменить и маршрутизировать антенны в коробку PrevenTechTM Lite Telematics | ** Ремонт завершен** |
| Повреждаются один или несколько антенных проводов, т.е. абразивный канал, круглое повреждение передатчика? **Нет** | **6C** |  |

ШАГ 6C. Статус SIM-карты

| ** Условия: ** В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Удалите SIM-карту Справочная фигура 4 выше. | Являются ли контакты SIM-карты и телематической коробки PrevenTechTM Lite грязными или скучными? **YesRepair:** Очистите все контакты, переустановите SIM-карту и проверьте передачу данных | ** Ремонт завершен** |
| Являются ли контакты SIM-карты и телематической коробки PrevenTechTM Lite грязными или скучными? **Нет** | **6D** |  |

ШАГ 6D. Данные SIM-карты

| **Условия: ** В то время как оборудование отключено **Примечание: ** Рассмотрите возможность использования мобильного телефона, совместимого с SIM-картой, того же сетевого провайдера для проверки функциональности данных; если передача данных установлена, может потребоваться замена телематического ящика PrevenTechTM Lite |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверка использования данных у сетевого провайдера | Достигнут ли максимальные пределы плана? **Да** Может рассмотреть возможность обновления до более высокого плана данных | ** Ремонт завершен** |
| Достигнут ли максимальные пределы плана? **NoRepair:** Коррумпированная SIM-карта; получить другую SIM-карту и перенастроить коробку PrevenTechTM Lite Telematics | ** Ремонт завершен** |  |

**APPENDIX B: Примеры установки**

Следующие фотографии документируют некоторые установки, проводимые в различных приложениях. Они предназначены только для справки. Каждая установка требует оценки, чтобы определить, какая стратегия подходит для этого конкретного устройства.

![[17r00871.png]]

Рисунок 13 Подключение к J1939 CAN Bus с помощью Гендерного Переключателя и Y Коннектора

![[17r00872.png]]

Рисунок 14, Полный план системы.

**APPENDIX C: WIFI трансляция**

EMD Configuration Utility (Полезность конфигурации)

EMD - это загружаемая программа конфигурации, которая будет необходима для настройки ячеистой сети на устройство Telematics.

Выполните следующие действия, чтобы загрузить программу:

1. Иди к нему.[https://www.emd.io/downloads/](https://www.emd.io/downloads/)
2. Нажмите на вторую подсказку, которая называется: (Windows Portable, 32bit)
3. Используйте WinZip и откройте программу.
4. Пароль: вводить

Подключите компьютер к устройству с помощью адаптера модема USB-RS-232 и доступного подключения RS-232 на устройстве проводов жгута.

![[17r00873.png]]

Рисунок 15, Устройство проводов жгута RS-232 Connection.

Запустите утилиту конфигурации EMD и дождитесь появления диалогового окна с просьбой использовать последовательный порт для связи с устройством, по умолчанию устройство будет обмениваться данными со скоростью 115200 б/с. Выберите подходящий и нажмите кнопку OK.

![[17r00874.png]]

Рисунок 16, окно полезной конфигурации EMD.

Всплывает окно с просьбой дать пароль. Введите правильный пароль и нажмите OK.

> [!note] Примечание
> Пароль устройства **должен** быть получен путем обращения в команду PrevenTechTM.

![[17r00875.png]]

Рисунок 17, окно ввода пароля устройства.

Информация DNS Server, необходимая ИТ-отделу клиента для подключения устройств:

- Режим: Переключитесь на ручной
- IP-адрес:
- Сетевая маска:
- Ворота:
- DNS1:
- DNS2:

Под вкладкой Network Tab вводится информация, собранная в соответствующих местах и нажмите Apply.

![[17r00876.png]]

Рисунок 18, Окно конфигурации сети.

Альтернативное соединение WIFI

- Зависимость от моего участка. Если клиент хочет использовать жесткое проводное соединение с внешним концентратором WIFI для передачи, необходимо приобрести совместимый провод соединения M8 с RJ45 (длина зависит от настройки оборудования) и подключить к телематическому окну через разъем Ethernet M8, доступный на устройстве.

![[17r00877.png]]

Рисунок 19, M8 Ethernet Port Connection.

**APPENDIX D: Заявление об отходах электрического и электронного оборудования**

Электрическое и электронное оборудование (ЭЭО) и батареи содержат материалы, компоненты и вещества, которые могут быть опасными и представлять опасность для здоровья человека и окружающей среды, когда отходы электрического и электронного оборудования (ЭЭО) и батареи обрабатываются неправильно.

Электрическое и электронное оборудование и батареи обозначены вычеркнутым колесным символом, указывающим, что электрическое и электронное оборудование и батареи должны быть утилизированы в обычном потоке бытовых отходов, но должны быть собраны отдельно. В случае, если батареи содержат более 0,0005% ртути (Hg), 0,002% кадмия (Cd) или 0,004% свинца (Pb) (по весу), соответствующий химический символ отображается на батарее. См. рисунок 20.

![[18r00017.png]]

Рисунок 20, Иконки типа отходов. Слева: МАЛЫШАЯ: Правильно: Аккумуляторные батареи.

> [!note] Примечание
> Бар ниже ведра WEEE слева на рисунке 20 рекомендуется включить, чтобы доказать, что продукт был сделан после 13 августа 2005 года. В качестве альтернативы можно указать дату.

Потребители играют важную роль в переработке этого оборудования и вносят свой вклад в защиту окружающей среды. Следовать местным правилам утилизации, чтобы уменьшить негативное воздействие на окружающую среду в связи с утилизацией WEEE и батарей, а также расширить возможности для повторного использования, переработки и восстановления WEEE и батарей. Для этого во многих областях доступны бесплатные пункты сбора. Пользователи несут ответственность за удаление персональных данных с электронных устройств до их удаления. По возможности, перед возвращением на переработку удалите старые батареи или аккумуляторы из электронного устройства.

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## PrevenTech™ Lite Telematics System Installation Manual
>
> **Table of Contents**
>
> - System and Hardware Overview
> - Installation
> - Installation Instructions: PrevenTech™ Lite Telematics Hardware
> - APPENDIX A: Telematics Box Hardware Specifications
> - APPENDIX B: Installation Examples
> - APPENDIX C: WIFI Transmission
> - APPENDIX D: Waste Electrical and Electronic Equipment Statement
>
> **System and Hardware Overview**
>
> This instruction manual details the installation of the PrevenTech™ Lite telematics system. While efforts have been made to make this manual as comprehensive as possible, installations **must** be tailored to the particular application/equipment model.
>
> The PrevenTech™ Lite Kit contains the following hardware:
>
> - PrevenTech™ Lite telematics box
> - Cellular/GPS/WIFI antenna
> - Main wiring harness
> - Antenna mounting hardware
>
> The PrevenTech™ Lite kit does not contain all the hardware needed for the installation. SIM cards and connection wiring harnesses **must** be purchased separately.
>
> Figure 1, PrevenTech™ Lite Kit Hardware
>
> Environmental and physical requirements operation and storage requirements:
>
> | **Table 1, Operation and Storage Requirements** |  |
> |---|---|
> | **Operation** | **Storage** |
> | Circuitry Operation Temperature Range | -5°C to +60°C (23 °F to 140 ˚F) |
> | Storage Temperature Range | -30°C to +80°C (86 °F to 176 ˚F) |
> | Humidity | Up to 95% - non-condensing |
>
> **Pre-Installation Steps**
>
> Prior to taking the PrevenTech™ Lite hardware to customer site, a bench test must be performed to verify that system is functional and procured SIM card is compatible with system.
>
> 1. Register box by contacting CPS team at connectedsol.support@cummins.com. On PrevenTech™ Lite box, provide ID and IMEI numbers. Also, needed are engine serial number (ESN), ECM calibration, hp rating, equipment OEM/model, unit number, location/mine site, and SIM card information.
>
> Figure 2, Identification label on Bottom of PrevenTech™ Lite Box
>
> 2. Remove telematics box cover and verify that SW2 dip switches are switched off (towards inner position or to left if harness connector is located on top). These switches are internal resistors that are **not** needed.
>
> **Note · Примечание**
> Do **not** change dipswitches on the component labeled SW1 as it will prevent unit from operating.
>
> Figure 3, Interior of PrevenTech™ Lite Box (Dip Switch Location Highlighted)
>
> 3. Procure 4G GSM SIM card (Micro 3FF size). Verify that there is adequate 4G coverage in the area. When activating the card, the IMEI number on the box label is required. Recommend that the customer and equipment is registered and access to www.preventech.cummins.com is activated. If the customer has **not** ordered SIM cards with active data plan, use a compatible SIM card with activated data plan for operational validation.
>
> 4. Install SIM card with contact facing down and notched tab facing outer side of device.
>
> Figure 4, Interior of PrevenTech™ Lite Box with SIM Card Installed
>
> 5. Inspect and make sure internal batteries are installed and connected.
>
> Figure 5, PrevenTech™ Lite Internal Batteries
>
> 6. Connect antenna to Telematics box and place in an elevated position to get cellular signal.
>
> 7. Connect wiring harness to box. Connect VINPUT lead to 12/24 V power source and GND lead to negative connection. Apply power. After 5 minutes, the green light should be Steady On. The red light should be Flashing (2 seconds OFF – 0 to 5 seconds ON). If the red light is Steady On, it means that there is no cell connectivity. If this occurs, reference Appendix A for troubleshooting.
>
> 8. Determine J1939 CAN Bus connection strategy. There are a couple different methods to connect to the engine J1939 CAN Bus. The strategy chosen determines what peripheral hardware needs to be ordered.
>
> - Option 1: Node off OEM J1939 CAN Bus
>
> Figure 6, CAN Bus Node
>
> - Option 2: Extend Engine Backbone to Telematics Box Harness
>
> Figure 7, Extension Wiring Harness
>
> Connect CAN0 channel on device harness.
>
> 9. General installation hardware is not included in the kit. Items required to perform complete installation that are not included in the kit. These items will vary depending on application/model type.
>
> - Zip ties
> - Fuse holders
> - 3 Amp fuse
> - Various electrical terminals/butt splices
> - Industrial Velcro
> - Gland Nuts
> - Additional 18 AWG Wire (if extension of wiring harness leads needed)
>
> **Industrial Procedures**
>
> 1. Select J1939 Public CAN Bus 3-Pin Connection.
>
> - It is possible for engines and equipment to have multiple CAN networks within their architecture – Public vs. Private. Identifying the Public J1939 CAN Bus is essential prior to installation of the PrevenTech™ Lite telematics box. To verify the correct CAN Bus has been selected, contact the equipment OEM. Alternatively, check continuity between the selected 3-pin connector and the 9-Pin service connector.
>
> Verify J1939 CAN Bus resistance by measuring between Positive and Negative terminal on the 9-Pin service connector (Pins C and D in figure below). If resistance measurement is 120 ohms, an additional terminating resistor **must** be added to the backbone. If the resistance measurement is less than 60 ohms, then a resistor **must** be removed.
>
> Figure 8, Connector Pin Diagram
>
> 3. Install PrevenTech™ Lite Telematics box.
>
> - Installation location must meet the following environment criteria:
> - Mount Telematics box using either industrial grade Velcro or mounting hardware. Note that if Velcro is used, verify identification label on the back of the PrevenTech™ Lite box is **not** covered. This information might be needed later for identification.
>
> Figure 9, Velcro Applied to Rear of PrevenTech™ Lite Telematics Box
>
> 4. Connect wiring harness.
>
> - The PrevenTech™ Lite wiring harness has several wires that are not used in the existing configuration. Make the following connections:
>
> Figure 10, Harness Breakout
>
> - Connect wiring harness to PrevenTech™ Lite Telematics Box by inserting connector and pushing in lock tab.
>
> Figure 11, PrevenTech™ Lite Wiring Harness Connection to PrevenTech™ Lite Telematics Box
>
> 5. Install antenna.
>
> - GSM/GP/WIFI antenna **must** be installed on the outside of the equipment, with direct line of sight to the sky.
> - Installed at least 40 cm from equipment operator.
> - Consider wiring harness routing strategy and proximity to PrevenTech™ Lite Telematics Box.
> - Route antenna connectors through gasket, bracket, and retaining nut.
> - Secure to bracket and mount using two U-bolts provided.
> - Route antenna connectors to PrevenTech™ Lite Telematics box and match the connectors to the correct port on the box.
>
> Figure 12, Antenna Harness Connected to Telematics Box and Antenna Mount on Exterior of Application
>
> - Create a strain relief by allowing at least 1 foot of cabling between the antennae ports and the placement of the strain relief.
> - Secure wiring harness along route using P-Clips or zip ties. Excess wiring harness should be neatly coiled up and secured to prevent from interfering with other components.
>
> 6. Apply power and verify that LED lights are on in accordance with the following tables. If LEDs do not give proper indication, reference Appendix A for troubleshooting steps.
>
> - The green LED will turn on after approximately 30 seconds as the power has been supplied. If the equipment is receiving frames through the CAN0 port, the LED will flash at high speed indicating transmission.
>
> | **Green LED Indicator – CAN Operation** |  |
> |---|---|
> | **State** | **Indication** |
> | Steady on | Operating system initialized |
> | Flashing | Data is being transmitted on CAN0 |
> | Off | Operating system not initialized |
>
> - The red LED is used to indicate the communication status of the device. During first couple minutes since device has been powered, LED will be off. If the Telematics box has not achieved connectivity, the LED will light up steadily. In contrast, if 4G/GSM connectivity is stable, the LED will flash every 2 seconds.
>
> | **Red LED Indicator – Network Connection** |  |
> |---|---|
> | **State** | **Indication** |
> | Steady on | No 4G/GSM connectivity |
> | Flashing (2 seconds OFF – 0 to 0.5 seconds ON) | Stable 4G/GSM connectivity |
> | Off | Only first couple minutes after powered on |
>
> - The blue LED is used to indicate Central Processing Unit (CPU) activity status. During the first couple minutes since device has been powered, LED will be off. If Telematics box has achieved connectivity LED with flash dependent on CPU activity. In contrast, if Telematics box LED will be off when connectivity has not been achieved.
>
> | **Blue LED Indicator – CPU Operation** |  |
> |---|---|
> | **State** | **Indication** |
> | Steady on | Operating system initializing |
> | Flashing (dependent on CPU activity) | CPU activity |
> | Off | Operating system not initialized |
>
> 7. After equipment registration is verified, use PrevenTech™ dashboard to verify GPS location and communication is active. If communication cannot be established, perform troubleshooting steps or contact Cummins CARE.
>
> **APPENDIX A: Troubleshooting**
>
> STEP 1A. Check for faulty equipment visibility on PrevenTech™ dashboard.
>
> | **Conditions:** While equipment is on |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Log on to PrevenTech™ dashboard, https://preventech.cummins.com; Check dashboard for operation | Is equipment in question visible on dashboard? **Yes** | **2A** |
> | Is equipment in question visible on dashboard? **No** | **1B** |  |
>
> STEP 1B. Check for visibility of other equipment on PrevenTech™ dashboard.
>
> | **Conditions**: While equipment is on |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check dashboard for visibility of other equipment | Is other equipment visible on dashboard? **YesNote:** Not an issue with dashboard | **2A** |
> | Is other equipment visible on dashboard? **No** | **Contact:** PrevenTech™ Regional Support Contact or care.cummins.com |  |
>
> STEP 2. Identify state of LEDs.
>
> STEP 2A. Green LED flashing
>
> | **Conditions:** While equipment is on **Note:** 30 seconds after power is supplied; PrevenTech™ Lite Telematics box green LED will start to flash at high speed when receiving frames through PrevenTech™ Lite Telematics J1939 connection |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect green LED | Is green LED flashing? **YesNote:** Data is being transmitted on PrevenTech™ Lite Telematics box J1939 connection; PrevenTech™ Lite Telematics box should be connected to engine's J1939 connection, reference step **5A** | **2C** |
> | Is green LED flashing? **No** | **2B** |  |
>
> STEP 2B. Green LED steady on
>
> | Inspect green LED | Is green LED steady on? **YesNote:** Operating System initialized | **5A** |
> |---|---|---|
> | Is green LED steady on? **NoNote:** Operating System not initialized | **3A** |  |
>
> STEP 2C. Red LED flashing
>
> | **Conditions:** While equipment is on |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect red LED | Is red LED flashing? **YesNote:** Stable internet connectivity | **Check dashboard configuration informationContact:** PrevenTech™ Regional Support Contact or care.cummins.com |
> | Is red LED flashing? **No** | **2D** |  |
>
> STEP 2D. Red LED steady on
>
> | **Conditions:** While equipment is on **Note:** Red LED will be off for the first 5 minutes after power has been supplied to PrevenTech™ Lite telematics box |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect red LED | Is red LED steady on? **YesNote:** No internet connectivity | **6A** |
> | Is red LED steady on? **No** | **3A** |  |
>
> Step 2E. Blue LED Flashing
>
> | **Conditions:** While equipment is on |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect blue LED | Is blue LED Flashing? **Yes** | **CPU activity presentRepair Complete** |
> | Is blue LED flashing? **No** | **2F** |  |
>
> Step 2F. Blue LED Off
>
> | **Conditions:** While equipment |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect blue LED | Is blue LED off? **No** | **Operating System is initializingRepair Complete** |
> | Is blue LED off? **Yes** | **3A** |  |
>
> STEP 3. Identify state of power supply.
>
> **Note · Примечание**
> PrevenTech™ Lite Telematics box internal cartridge battery will hold charge for a period of time after external power has been removed and will function as intended. When troubleshooting the external power supply, disconnect PrevenTech™ Lite Telematics box internal cartridge battery. If needed, refer to Step 4 for PrevenTech™ Lite Telematics box internal battery fault finding, i.e., data time stamp variation on PrevenTech™ dashboard.
>
> STEP 3A. Fuse condition
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect inline fuse | Is fuse open? **YesRepair:** Replace fuse | **Repair Complete** |
> | Is fuse open? **No** | **3B** |  |
>
> STEP 3B. Power supply, ignition, and chassis ground wire condition
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Carefully inspect main harness wiring condition Reference Appendix H above. | Are power supply, ignition, and chassis ground wires in good condition with no damage, i.e. no tears? **Yes** | **3C** |
> | Are power supply, ignition, and chassis ground wires in good condition with no damage? **NoRepair:** Replace PrevenTech™ Lite telematics box main harness | **Repair Complete** |  |
>
> STEP 3C. Power supply, ignition, and chassis ground connections
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Carefully inspect main harness connections | Are power supply, ignition, and chassis ground wires connected? **Yes** | **3D** |
> | Are power supply, ignition, and chassis ground wires connected? **NoRepair:** Connect wire(s) that are not connected | **Repair Complete** |  |
>
> STEP 3D. Main harness connection to PrevenTech™ Lite Telematics box
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect main harness connection to PrevenTech™ Lite telematics box. Reference Step 5 in Installation Instructions: PrevenTech™ Lite Telematics Hardware above. | Is the main harness connected securely to PrevenTech™ Lite telematics box? **Yes** | **3E** |
> | Is the main harness connected securely to PrevenTech™ Lite telematics box? **NoRepair:** Connect and securely lock main harness | **Repair Complete** |  |
>
> STEP 3E. Condition of LED(s) internal wiring
>
> | **Conditions:** While power is supplied to PrevenTech™ Lite telematics box |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect LED(s) internal wiring, | Are LED(s) on? **NoRepair:** Replace PrevenTech™ Lite telematics box | **Repair complete** |
>
> STEP 4. PrevenTech™ Lite internal battery conditions
>
> STEP 4A. Internal clock (round) battery condition
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check dashboard data time stamps. | Is there ambiguity in the data time stamp/real time clock? **YesNote:** Replace round battery, Reference Figure 5 above. Turn on device and check PrevenTech™ dashboard for functionality | **Repair Complete** |
>
> STEP 5. Equipment J1939 connections
>
> STEP 5A. Inspect equipment and PrevenTech™ Lite Telematics box J1939 connection
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect PrevenTech™ Lite Telematics box J1939 connection with equipment | Is PrevenTech™ Lite Telematics box J1939 plug connected to equipment's J1939 public data connection? **Yes** | **5C** |
> | Is PrevenTech™ Lite Telematics box J1939 plug connected to equipment's J1939 public data connection? **No** | **5B** |  |
>
> STEP 5B. Equipment J1939 Public Connection
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure continuity from 9-pin service connector to 3-pin Deutsch connector | Was continuity confirmed? **YesRepair:** Connect PrevenTech™ Lite telematics box J1939 connection to public data J1939 connection on equipment | **Repair Complete** |
> | Was continuity confirmed? **NoNote:** Repeat this step until equipment J1939 public connection is located | **Repeat Step** |  |
>
> STEP 5C. Measure equipment resistance
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disconnect the J1939 connection; using the equipment J1939 or 9 Pin service connector measure the equipment resistance, reference Figure 8 above. | Is the measured resistance 60 Ohms? **Yes** | **5E** |
> |  | Is the measured resistance 60 Ohms? **No** | **5D** |
>
> STEP 5D. Inspect J1939 backbone terminal resistors
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect J1939 connection terminal resistors; measure resistance. Note: ONLY two 120 Ohms resistors needed in parallel on backbone to achieve a total resistance of 60 Ohms | Is the measured resistance in each resistor 120 Ohms? **Yes** | **5E** |
> | Is the measured resistance in each resistor 120 Ohms? **NoRepair:** Discard and replace resistor(s) | **Repair Complete** |  |
>
> STEP 5E. Measure PrevenTech™ Lite Telematics box resistance
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure resistance on PrevenTech™ Lite J1939 connection, reference Figure 8 above. | Is the measured resistance approximately 50 K-Ohms? **No** | **5F** |
> | Is the measured resistance approximately 50 K-Ohms? **YesNote:** No PrevenTech™ Lite telematics resistance issue | **Repair Complete** |  |
>
> STEP 5F. PrevenTech™ Lite Telematics box resistance correction
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure resistance on PrevenTech™ Lite J1939 connection | Is the measured resistance approximately 0 Ohms? **YesNote:** Short in box **Repair:** Replace PrevenTech™ Lite Telematics box | **Repair Complete** |
> | Is the measured resistance approximately 120 Ohms? **YesRepair:** Ensure internal resistance dip switches are all to the right of the battery. Reference Step 13 in Installation Instructions: PrevenTech™ Lite Telematics Hardware above. | **Repair Complete** |  |
>
> STEP 6. Data transmission to PrevenTech™ dashboard
>
> STEP 6A. Antennae connections
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect antennae connections on PrevenTech™ Lite telematics box, reference Step 5 in Installation Instructions: PrevenTech™ Lite Telematics Hardware above | Are the antennae wires connect securely and correct to PrevenTech™ Lite telematics box? **Yes** | **6B** |
> | Are the antennae wires connect securely and correct to PrevenTech™ Lite telematics box? **NoRepair:** Correctly wire the antennae wires to the correct ports and securely connect. | **Repair Complete** |  |
>
> STEP 6B. Condition of antennae wires
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect wires between PrevenTech™ Lite telematics box and antennae round transmitter, reference Step 5 in Installation Instructions: PrevenTech™ Lite Telematics Hardware above | Are one or more antennae wires damaged, i.e. abrasion to conduit, round transmitter physical damage? **YesRepair:** Replace and route antennae to PrevenTech™ Lite Telematics box | **Repair Complete** |
> | Are one or more antennae wires damaged, i.e. abrasion to conduit, round transmitter physical damage? **No** | **6C** |  |
>
> STEP 6C. SIM card status
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Remove SIM card Reference Figure 4 above. | Are SIM card and PrevenTech™ Lite telematics box motherboard contacts dirty or dull? **YesRepair:** Clean all contacts, reinstall SIM, and check for data transmission | **Repair Complete** |
> | Are SIM card and PrevenTech™ Lite telematics box motherboard contacts dirty or dull? **No** | **6D** |  |
>
> STEP 6D. SIM card data
>
> | **Conditions:** While equipment is off **Note:** Consider using a mobile phone compatible with SIM card, same network provider, to check data functionality; if data transmission is established, replacement of PrevenTech™ Lite telematics box may be necessary |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check data usage with network provider | Has data plan maximum limit been reached? **YesRepair** May consider upgrading to a higher data plan | **Repair Complete** |
> | Has data plan maximum limit been reached? **NoRepair:** Corrupt SIM card; obtain another SIM card and re-configure PrevenTech™ Lite Telematics box | **Repair Complete** |  |
>
> **APPENDIX B: Installation Examples**
>
> The following pictures document some of the installations conducted on various applications. These are for reference only. Each installation requires evaluation to determine what the correct strategy is for that particular unit.
>
> Figure 13, Connecting into J1939 CAN Bus using Gender Changer and Y Connector
>
> Figure 14, Complete System Layout.
>
> **APPENDIX C: WIFI Transmission**
>
> EMD Configuration Utility
>
> EMD is a downloadable configuration program that will be needed to configure mesh network to Telematics device.
>
> Follow the steps below to download the program:
>
> 1. Go to [https://www.emd.io/downloads/](https://www.emd.io/downloads/)
> 2. Click on second prompt called: (Windows Portable, 32bit).
> 3. Use WinZip and open the program.
> 4. Password: emd
>
> Connect computer to device using a USB to RS-232 modem adapter and available RS-232 connection on device harness.
>
> Figure 15, Device Harness RS-232 Connection.
>
> Launch EMD configuration utility and wait until dialog box appears asking for a serial port to use for communication with device, by default device will communicate at 115200 bps. Select appropriate and click OK button.
>
> Figure 16, EMD Configuration Utility Window.
>
> A window pops up asking for a device password. Input correct password and click OK.
>
> **Note · Примечание**
> Password of the device **must** be obtained by contacting PrevenTech™ team.
>
> Figure 17, Device Password Input Window.
>
> DNS Server information required from customer's IT department to link devices:
>
> - Mode: Switch to Manual
> - IP Address:
> - Network Mask:
> - Gateway:
> - DNS1:
> - DNS2:
>
> Under the Network Tab input information gathered in appropriate locations and click Apply.
>
> Figure 18, Network Configuration Window.
>
> Alternate WIFI Connection
>
> - Mine site dependent. If the customer would like to use a hard wire connection to an external WIFI hub for transmission, a compatible M8 to RJ45 connection wire (length is dependent on equipment setup) will need to be purchased and connected to Telematics box via M8 Ethernet connector available on device.
>
> Figure 19, M8 Ethernet Port Connection.
>
> **APPENDIX D: Waste Electrical and Electronic Equipment Statement**
>
> Electrical and electronic equipment (EEE) and batteries contain materials, components and substances that may be hazardous and present a risk to human health and the environment when waste electrical and electronic equipment (WEEE) and batteries are **not** handled correctly.
>
> Electrical and electronic equipment and batteries are marked with the crossed-out wheeled bin symbol indicating that electrical and electronic equipment and batteries should **not** be disposed of in the regular household waste stream but need to be collected separately. In case batteries contain more than 0,0005% mercury (Hg), 0,002% cadmium (Cd) or 0,004% lead (Pb) (by weight), the corresponding chemical symbol is displayed on the battery. See Figure 20.
>
> Figure 20, Waste Type Icons. Left: WEEE; Right: Batteries.
>
> **Note · Примечание**
> The bar below the WEEE bin at left in Figure 20 is recommended to include to prove that a product was made after the 13 August 2005. Alternatively, a date can be included.
>
> Consumers have an important role in recycling this equipment and contributing to the protection of the environment. Follow local recycling regulations to reduce adverse environmental impact in connection with disposal of WEEE and batteries and to increase opportunities for reuse, recycling, and recovery of WEEE and batteries. To facilitate this, free collection points are available in many areas. Users are responsible for removing personal data from electronic devices prior to disposal. If possible, remove old batteries or accumulators from the electronic device before returning for recycling.
>
> ### Document History
