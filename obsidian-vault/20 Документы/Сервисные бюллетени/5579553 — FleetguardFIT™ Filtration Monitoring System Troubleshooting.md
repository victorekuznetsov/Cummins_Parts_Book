---
type: "Сервисный бюллетень"
doc: "5579553"
title_en: "FleetguardFIT™ Filtration Monitoring System Troubleshooting"
released: "2018-11-08"
modified: "2018-11-16"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/5579553.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/bulletin/5579553.pdf"
tags:
  - "документ/бюллетень"
  - "двигатель/QSK60"
  - "перевод/машинный"
---

# FleetguardFIT™ Filtration Monitoring System Troubleshooting

> [!abstract] Сервисный бюллетень · `5579553`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Даты:** выпущен 2018-11-08 · изменён 2018-11-16
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/5579553.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/bulletin/5579553.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Система мониторинга фильтрации FleetguardFITTM устранение неполадок

**Цель:**

Устранение неполадок в системе мониторинга фильтрации FleetguardFITTM.

- Система FleetguardFITTM работает не так, как ожидалось.
- Данные FleetguardFITTM не видны на телематическом портале.
- Проблема с питанием FleetguardFITTM.
- Данные FleetguardFITTM некорректны на портале.

Это дерево симптомов может быть использовано для устранения неполадок в системе мониторинга фильтрации FleetguardFITTM. Выполните список шагов по устранению неполадок в показанной последовательности.

**Резюме по устранению неполадок**

| **СТЭП** |  |
|---|---|
| ШАГ 1. Определить состояние телематического портала |  |
|  | ШАГ 1A. Проверка неисправности оборудования на портале телематики |
|  | ШАГ 1B. Проверка видимости другого оборудования на телематическом портале |
| ШАГ 2. Подтвердите, что телематическое устройство работает правильно |  |
|  | ШАГ 2A. Мощность телематического устройства |
|  | ШАГ 2B. Телематическое устройство передачи данных |
| ШАГ 3. Определить состояние светодиодов системы FMS Filter Monitor System (FMS) |  |
|  | ШАГ 3A. Работа с светодиодом |
|  | ШАГ 3B. Синий светодиод устойчивый |
|  | ШАГ 3C. Зеленый и красный светодиодные вспышки |
| ШАГ 4. Определить состояние электроснабжения |  |
|  | ШАГ 4A. Состояние предохранителя |
|  | ШАГ 4B. Электропитание, зажигание и состояние наземного провода |
|  | ШАГ 4C. Электропитание, зажигание и наземные соединения шасси |
|  | ШАГ 4D. CAN подключение шины передачи данных к FleetguardFITTM FMS |
| ШАГ 5. Оборудование J1939 Connection |  |
|  | ШАГ 5A. Обследование оборудования и соединения FleetguardFITTM J1939 |
|  | ШАГ 5B. Проверка оборудования и телематических соединений J1939 |
|  | ШАГ 5C. Оборудование J1939 Public Connection |
|  | ШАГ 5D. Измерить сопротивление оборудования |
|  | ШАГ 5E. Осмотр резисторов магистральных терминалов J1939 |
| ШАГ 6. Идентификация совместимости FMS FleetguardFITTM |  |
|  | ШАГ 6A. Уровень коммуникативных бод |
| ШАГ 7. Определить состояние датчика (датчиков) FleetguardFITTM |  |
|  | ШАГ 7A. Проверить телематический портал данных датчиков качества масла FleetguardFITTM |
|  | ШАГ 7B. Данные датчиков качества масла |
|  | ШАГ 7C. Проверить телематический портал данных датчиков дифференциального давления и ограничения FleetguardFITTM |
|  | ШАГ 7D. данные датчика дифференциального давления и ограничения |
| ШАГ 8. Определить состояние установки датчиков FleetguardFITTM |  |
|  | ШАГ 8A. Датчик качества масла |
|  | ШАГ 8B. Датчик ограничения воздуха |
|  | ШАГ 8C. аппаратное обеспечение датчика дифференциального давления |
| ШАГ 9. Определить состояние датчиков FleetguardFITTM, расширяющих проводные ремни и FMS |  |
|  | ШАГ 9A. Сенсорная проводка жгут ветки жгут и удлинение жгут жгут условие |
|  | ШАГ 9B. Сенсорная проводка жгут ветки жгут и удлинение проводов жгут соединения |
|  | ШАГ 9C. Сенсорная проводка жгут ветки жгут и удлинение жгут проводов преемственность |
|  | ШАГ 9D. Замена модуля FMS |

ШАГ 1. Определить состояние телематического портала.

ШАГ 1A. Проверьте наличие неисправного оборудования на телематическом портале.

| **Условия: **В то время как оборудование включено |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Войдите на телематический портал и проверьте работу | Видно ли оборудование на портале? *Да** | **3A |
| Видно ли оборудование на портале? **Нет** | **1B** |  |

ШАГ 1B. Проверка видимости другого оборудования на телематическом портале.

| **Условия: **В то время как оборудование включено |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверка телематического портала на предмет видимости другого оборудования | Видно ли другое оборудование на портале? **Давайте не будем спорить с порталом | **2A |
| Видно ли другое оборудование на портале? **Нет** | **Контакты:** Поддержка провайдера телематических услуг |  |

ШАГ 2. Подтвердите, что телематическое устройство работает должным образом.

ШАГ 2A. Мощность телематического устройства.

| **Условия: **В то время как оборудование включено |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте питание телематического устройства | Телематическое устройство имеет мощность? **Давайте примечание: **Не проблема с электропитанием телематического устройства | **2B** |
| Телематическое устройство имеет мощность? **Нет** | **Контакты:** Поддержка провайдера телематических услуг |  |

ШАГ 2B. Телематическое устройство передачи данных.

| **Условия: **В то время как оборудование включено |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте устройство телематики для передачи данных | Телематическое устройство отправляет/принимает данные? **Давайте не будем замечать: **Не проблема с передачей данных телематическим устройством | **3A** |
| Телематическое устройство отправляет/принимает данные? **Нет** | **Контакт:** Поддержка провайдера телематических услуг**Примечание:** Могут возникнуть проблемы с SIM-картой, ограничениями данных, внутренними проблемами устройства, антенной устройства, обслуживанием сотовой связи или другими |  |

ШАГ 3. Определить состояние FMS-светодиодов FleetguardFITTM.

ШАГ 3A. Работа со светодиодами.

| **Условия: **В то время как оборудование включено |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Модуль FMS Inspect | Есть светодиоды? **Да, примечание: **ФМС получает питание | **3B** |
| Есть светодиоды? **Нет** | **4А** |  |

ШАГ 3B. Синий светодиод включен.

| **Условия: **В то время как оборудование включено |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Модуль FMS Inspect | Синий светодиод устойчив? **Да-нет: **Источник питания зажигания подключен правильно | **3C** |
| Синий светодиод устойчив? **Примечание:** Источник питания зажигания должен быть подключен или отремонтирован | **4А** |  |

ШАГ 3C. Зеленый и красный светодиодные вспышки.

| **Условия: **В то время как оборудование включено |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Модуль FMS Inspect | Зеленые и красные светодиоды мигают **Давайте пометим: **FMS отправляет / принимает данные | **5B** |
| Зеленые и красные светодиоды мигают **Нет** | **5А** |  |

ШАГ 4. Определить состояние электроснабжения.

ШАГ 4A. Условия взрыва.

| **Условия: **В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| 5.2.1 Проверка встроенных предохранителей для зажигания и подачи электроэнергии | Запал открыт? **Да, ремонт: **Заменить 10-амперный предохранитель | **Ремонт завершен** |
| Запал открыт? **Нет** | **4B** |  |

ШАГ 4B. Электропитание, зажигание и состояние проволоки.

| **Условия: **В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Тщательно проверьте CAN Data Bus Wiring Grund | Являются ли источники питания, зажигания и наземные провода в хорошем состоянии без повреждений, т.е. Никаких слез? *Да** | **4C |
| Являются ли провода питания, зажигания и заземления шасси в хорошем состоянии без повреждений? **NoRepair:** Заменить или заменить шину данных CAN | **Ремонт завершен** |  |

ШАГ 4C. Электропитание, зажигание и наземные соединения шасси.

| **Условия: **В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Тщательно проверьте CAN Data Bus Wiring Grund | Подключены ли электропитание, зажигание и наземные провода? *Да** | **4D |
| Подключены ли провода питания, зажигания и наземные провода шасси? **NoRepair:** Подключите провод(ы), которые не подключены | **Ремонт завершен** |  |

ШАГ 4D. CAN шина передачи данных подключается к FleetguardFITTM FMS.

| **Условия: **В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить соединение шины данных CAN с модулем FMS | Является ли шина передачи данных CAN надежно подключенной к модулю FMS? *Да** | **5А |
| Является ли шина передачи данных CAN надежно подключенной к модулю FMS? **NoRepair:** Подключите шину передачи данных CAN к модулю FMS | **Ремонт завершен** |  |

ШАГ 5. Оборудование J1939 соединений.

ШАГ 5A. Проверить оборудование и соединение FleetguardFITTM J1939.

| **Условия: **В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверка соединения FleetguardFITTM J1939 с оборудованием | Имеется ли у FleetguardFITTM надлежащая связь с общедоступным соединением данных J1939? *Да** | **5B |
| Имеется ли у FleetguardFITTM надлежащая связь с общедоступным соединением данных J1939? **NoRepair:** Подключите FleetguardFITTM к публичной шине данных J1939 | **Ремонт завершен** |  |

ШАГ 5B. Проверить оборудование и телематическую связь J1939.

| **Условия: **В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверка телематического соединения J1939 с оборудованием | Телематическое устройство подключено к общедоступному соединению данных J1939? **Примечание:** ФМС и телематика FleetguardFITTM должны быть на разных узлах магистрали данных CAN**Да** | **5C** |
| Телематическое устройство подключено к общедоступному соединению данных J1939? **NoRepair:** Подключите телематику к публичной шине данных J1939 | **Ремонт завершен** |  |

ШАГ 5C. Оборудование J1939 Public Connection.

| **Условия: **В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить непрерывность от 9-контактного сервисного разъема до 3-контактного разъема Deutsch **Примечание: **Необходимо завершить для соединений FleetguardFITTM и телематики J1939 | Подтверждена ли преемственность? *Да** | **5D |
| Подтверждена ли преемственность? **NoRepair: **Найдите другое общественное соединение J1939 или ремонтную проводку, если известно, что 3-контактное соединение является публичным соединением J1939 | **Повторить шаг** |  |

ШАГ 5D. Измерить сопротивление оборудования.

| **Условия: **В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите соединение J1939; с помощью оборудования J1939 3-контактный или 9-контактный разъем службы измерения сопротивления оборудования | Является ли измеренное сопротивление 55-65 Ом? *Да** | **6А |
| Является ли измеренное сопротивление 55-65 Ом? **Нет** | **5E** |  |

ШАГ 5E. Проверить резисторы магистральных терминалов J1939.

| **Условия: **В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить резисторы терминала связи J1939; измерить сопротивление Примечание: Только два 120 Ом резистора, необходимых параллельно на магистрали для достижения общего сопротивления 60 Ом | Является ли измеренное сопротивление в каждом резисторе 120 Ом? *Да** | **6А |
| Является ли измеренное сопротивление в каждом резисторе 120 Ом? **NoRepair:** Откажитесь от резистора (резисторов) и замените его (их) | **Ремонт завершен** |  |

ШАГ 6. Идентификация совместимости FMS FleetguardFITTM.

ШАГ 6A. Уровень коммуникативных бод.

| **Условия: **В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Определить двигатель, провайдера телематических услуг (TSP) и скорость плавания FMS FleetguardFITTM **Примечание: **Варианты FMS FleetguardFITTM составляют 250 кбит/с и 500 кбит/с | Соответствуют ли показатели баудов для двигателей, TSP и FleetguardFITTM FMS? *Да** | **7A |
| Соответствуют ли показатели баудов для двигателей, TSP и FleetguardFITTM FMS? **NoRepair:** Заменить на соответствующий модуль FMS FleetguardFITTM | **Ремонт завершен** |  |

ШАГ 7. Определить состояние датчика (датчиков) FleetguardFITTM.

ШАГ 7A. Проверьте телематический портал для данных датчиков качества масла FleetguardFITTM.

| **Условия: **В то время как оборудование включено |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Войдите на телематический портал и проверьте данные датчика качества масла FleetguardFITTM | На портале видны данные датчиков качества масла? *Да** | **7B |
| На портале видны данные датчиков качества масла? **Нет** | **9А** |  |

ШАГ 7B. Данные датчиков качества масла.

| **Условия: **В то время как оборудование включено |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Войдите на телематический портал и проверьте данные датчика качества масла FleetguardFITTM | Данные датчиков качества масла в пределах ожидаемых диапазонов? *Да** | **7C |
| Данные датчиков качества масла в пределах ожидаемых диапазонов? **Нет** | **8А** |  |

ШАГ 7C. Проверьте телематический портал для данных датчиков дифференциального давления и ограничения FleetguardFITTM.

| **Условия: **В то время как оборудование включено |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Войдите на телематический портал и проверьте данные датчика дифференциального давления и ограничения FleetguardFITTM | Видны ли на портале данные датчика дифференциального давления и ограничения? *Да** | **7D |
| Видны ли на портале данные датчика дифференциального давления и ограничения? **Нет** | **9А** |  |

ШАГ 7D. Данные датчиков дифференциального давления и ограничения.

| **Условия: **В то время как оборудование включено |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Войдите на телематический портал и проверьте данные датчика дифференциального давления и ограничения FleetguardFITTM | Данные датчиков дифференциального давления и ограничения находятся в пределах ожидаемых диапазонов? *Да** | **Ремонт завершен |
| Данные датчиков дифференциального давления и ограничения находятся в пределах ожидаемых диапазонов? **Нет** | **8B** |  |

ШАГ 8. Определить состояние установки датчиков FleetguardFITTM.

ШАГ 8A. Датчик качества масла.

| **Условия: **В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Инспектировать установку датчика качества масла | Наконечник датчика расположен в области с горячим под давлением текучим маслом и отсутствием утечек? *Да** | **9А |
| Наконечник датчика расположен в области с горячим под давлением текучим маслом и отсутствием утечек? **Нет ремонта:** Переместить датчик качества масла в соответствии с инструкциями FleetguardFITTM | **Ремонт завершен** |  |

ШАГ 8B. Датчик ограничения воздуха.

| **Условия: **В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Инспектировать установку датчика ограничения воздуха | Является ли датчик видимо в хорошем состоянии и подключен к системе воздухозаборника без утечек? *Да** | **8C |
| Является ли датчик видимо в хорошем состоянии и подключен к системе воздухозаборника без утечек? **Заменить датчик ограничения | **Ремонт завершен |  |

ШАГ 8C. Датчик (датчики) дифференциального давления.

| **Условия: **В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить установку датчика дифференциального давления | Правильно ли датчик подключен к входному и выходному порту головки фильтра без утечек? *Да** | **9А |
| Правильно ли датчик подключен к входному и выходному порту головки фильтра без утечек? **NoRepair:** Правильно подсоедините датчик дифференциального давления к входным/выходным портам головки фильтра. Замените аппаратное обеспечение, если это необходимо. | **Ремонт завершен** |  |

ШАГ 9. Определите состояние датчиков FleetguardFITTM, проводных ремней и FMS.

ШАГ 9A. Сенсорная проводка жгута ветки жгута и удлинение жгута жгута.

| **Условия: **В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Тщательно проверьте датчик проводов жгута ветки жгута проводов и удлинителя жгута проводов | Электропроводка упряжки в хорошем состоянии без повреждений, т.е. Никаких слез? *Да** | **9B |
| Электропроводка упряжки в хорошем состоянии без повреждений, т.е. Никаких слез? **NoRepair:** Заменить или отремонтировать электропроводку | **Ремонт завершен** |  |

ШАГ 9B. Сенсорная проводка жгута ветки жгута и удлинительная проводка жгута соединения.

| **Условия: **В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Тщательно проверьте датчик проводов жгута ветки жгута проводов и удлинителя жгута проводов | Правильно ли подключены электропроводки к FMS, проводов жгута, проводов ветки и каждого датчика? *Да** | **9C |
| Правильно ли подключены электропроводки к FMS, проводов жгута, проводов ветки и каждого датчика? **NoRepair:** Подключите провод(ы), которые не подключены | **Ремонт завершен** |  |

ШАГ 9C. Сенсорная проводка жгута проводов ветки жгута и удлинение жгута проводов преемственности.

| **Условия: **В то время как оборудование отключено |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить непрерывность от конца до конца для проводов жгута ветка проводов жгута и каждого расширения проводов жгута | Подтверждена ли преемственность? **Да, ремонт: **Заменить датчик | **9D** |
| Подтверждена ли преемственность? **NoRepair:** Исправить или заменить проводные ремни | **Ремонт завершен** |  |

ШАГ 9D. Замена модуля FMS.

| **Условия: **В то время как оборудование отключено |  |  |
|---|---|---|
| **Спецификация/ремонт** | **Действие** | **Следующий шаг** |
| Имеются ли данные в пределах ожидаемых диапазонов? *Да** | Войдите на телематический портал и проверьте неисправное оборудование для данных FleetguardFITTM | **Ремонт завершен |
| Имеются ли данные в пределах ожидаемых диапазонов? **Заменить модуль FMS | **Свяжитесь с: FIT.Support@cummins.com |  |

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## FleetguardFIT™ Filtration Monitoring System Troubleshooting
>
> **Purpose:**
>
> Troubleshooting of FleetguardFIT™ filtration monitoring system.
>
> - FleetguardFIT™ system not working as expected.
> - FleetguardFIT™ data not visible on telematics portal.
> - FleetguardFIT™ power issue.
> - FleetguardFIT™ data incorrect on portal.
>
> This symptom tree can be used to troubleshoot the FleetguardFIT™ filtration monitoring system. Perform the list of troubleshooting steps in the sequence shown.
>
> **Troubleshooting Summary**
>
> | **STEPS** |  |
> |---|---|
> | STEP 1. Identify telematics portal state |  |
> |  | STEP 1A. Check for faulty equipment visibility on telematics portal |
> |  | STEP 1B. Check for visibility of other equipment on telematics portal |
> | STEP 2. Confirm telematics device operating properly |  |
> |  | STEP 2A. Telematics device power |
> |  | STEP 2B. Telematics device data communication |
> | STEP 3. Identify state of FleetguardFIT™ Filter Monitor System (FMS) LEDs |  |
> |  | STEP 3A. LED operation |
> |  | STEP 3B. Blue LED steady on |
> |  | STEP 3C. Green and red LED flashing |
> | STEP 4. Identify state of power supply |  |
> |  | STEP 4A. Fuse condition |
> |  | STEP 4B. Power supply, ignition, and ground wire condition |
> |  | STEP 4C. Power supply, ignition, and chassis ground connections |
> |  | STEP 4D. Datalink harness connection to FleetguardFIT™ FMS |
> | STEP 5. Equipment J1939 connections |  |
> |  | STEP 5A. Inspect equipment and FleetguardFIT™ J1939 connection |
> |  | STEP 5B. Inspect equipment and telematics J1939 connection |
> |  | STEP 5C. Equipment J1939 public connection |
> |  | STEP 5D. Measure equipment resistance |
> |  | STEP 5E. Inspect J1939 backbone terminal resistors |
> | STEP 6. Identify FleetguardFIT™ FMS compatibility |  |
> |  | STEP 6A. Communication baud rate |
> | STEP 7. Identify state of FleetguardFIT™ sensor(s) |  |
> |  | STEP 7A. Check telematics portal for FleetguardFIT™ oil quality sensor data |
> |  | STEP 7B. Oil quality sensor data |
> |  | STEP 7C. Check telematics portal for FleetguardFIT™ differential pressure and restriction sensor data |
> |  | STEP 7D. differential pressure and restriction sensor data |
> | STEP 8. Identify state of FleetguardFIT™ sensor installations |  |
> |  | STEP 8A. Oil quality sensor |
> |  | STEP 8B. Air restriction sensor |
> |  | STEP 8C. differential pressure sensor hardware |
> | STEP 9. Identify state of FleetguardFIT™ sensor extension harnesses and FMS |  |
> |  | STEP 9A. Sensor breakout harness and extension harness condition |
> |  | STEP 9B. Sensor breakout harness and extension harness connection |
> |  | STEP 9C. Sensor breakout harness and extension harness continuity |
> |  | STEP 9D. FMS module replacement |
>
> STEP 1. Identify telematics portal state.
>
> STEP 1A. Check for faulty equipment visibility on telematics portal.
>
> | **Conditions:** While equipment is on |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Log on to telematics portal and check for operation | Is equipment in question visible on portal? **Yes** | **3A** |
> | Is equipment in question visible on portal? **No** | **1B** |  |
>
> STEP 1B. Check for visibility of other equipment on telematics portal.
>
> | **Conditions:** While equipment is on |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check telematics portal for visibility of other equipment | Is other equipment visible on portal? **YesNote:** Not an issue with portal | **2A** |
> | Is other equipment visible on portal? **No** | **Contact:** Telematics service provider support |  |
>
> STEP 2. Confirm telematics device operating properly.
>
> STEP 2A. Telematics device power.
>
> | **Conditions:** While equipment is on |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check telematics device power supply | Does the telematics device have power? **YesNote:** Not an issue with telematics device power supply | **2B** |
> | Does the telematics device have power? **No** | **Contact:** Telematics service provider support |  |
>
> STEP 2B. Telematics device data communication.
>
> | **Conditions:** While equipment is on |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check telematics device for data communication | Is the telematics device sending / receiving data? **YesNote:** Not an issue with telematics device data communication | **3A** |
> | Is the telematics device sending / receiving data? **No** | **Contact:** Telematics service provider support **Note:** May be issue with SIM card, data limits, internal device issue, device antenna, cell service, or other |  |
>
> STEP 3. Identify state of FleetguardFIT™ FMS LEDs.
>
> STEP 3A. LED operation.
>
> | **Conditions:** While equipment is on |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect FMS module | Are any LEDs on? **YesNote:** FMS is receiving power | **3B** |
> | Are any LEDs on? **No** | **4A** |  |
>
> STEP 3B. Blue LED steady on.
>
> | **Conditions:** While equipment is on |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect FMS module | Is blue LED steady on? **YesNote:** Ignition power source is wired correctly | **3C** |
> | Is blue LED steady on? **NoNote:** Ignition power source needs to be connected or repaired | **4A** |  |
>
> STEP 3C. Green and red LED flashing.
>
> | **Conditions:** While equipment is on |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect FMS module | Are green and red LEDs flashing **YesNote:** FMS is sending / receiving data | **5B** |
> | Are green and red LEDs flashing **No** | **5A** |  |
>
> STEP 4. Identify state of power supply.
>
> STEP 4A. Fuse condition.
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect inline fuses for ignition and power supply | Is fuse open? **YesRepair:** Replace 10 ampere fuse | **Repair Complete** |
> | Is fuse open? **No** | **4B** |  |
>
> STEP 4B. Power supply, ignition, and ground wire condition.
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Carefully inspect datalink harness | Are power supply, ignition, and ground wires in good condition with no damage, i.e. no tears? **Yes** | **4C** |
> | Are power supply, ignition, and chassis ground wires in good condition with no damage? **NoRepair:** Replace or replace datalink harness | **Repair Complete** |  |
>
> STEP 4C. Power supply, ignition, and chassis ground connections.
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Carefully inspect datalink harness | Are power supply, ignition, and ground wires connected? **Yes** | **4D** |
> | Are power supply, ignition, and chassis ground wires connected? **NoRepair:** Connect wire(s) that are not connected | **Repair Complete** |  |
>
> STEP 4D. Datalink harness connection to FleetguardFIT™ FMS.
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect datalink harness connection to FMS module | Is the datalink harness connected securely to FMS module? **Yes** | **5A** |
> | Is the datalink harness connected securely to FMS module? **NoRepair:** Connect datalink harness to FMS module | **Repair Complete** |  |
>
> STEP 5. Equipment J1939 connections.
>
> STEP 5A. Inspect equipment and FleetguardFIT™ J1939 connection.
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect FleetguardFIT™ J1939 connection with equipment | Is FleetguardFIT™ properly connected to equipment's J1939 public data connection? **Yes** | **5B** |
> | Is FleetguardFIT™ properly connected to equipment's J1939 public data connection? **NoRepair:** Connect FleetguardFIT™ properly to J1939 public datalink | **Repair Complete** |  |
>
> STEP 5B. Inspect equipment and telematics J1939 connection.
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect telematics J1939 connection with equipment | Is telematics device properly connected to equipment's J1939 public data connection? **Note:** FleetguardFIT™ FMS and telematics should be on different nodes of the datalink backbone **Yes** | **5C** |
> | Is telematics device properly connected to equipment's J1939 public data connection? **NoRepair:** Connect telematics properly to J1939 public datalink | **Repair Complete** |  |
>
> STEP 5C. Equipment J1939 public connection.
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure continuity from 9-pin service connector to 3-pin Deutsch connector **Note:** Needs to be completed for FleetguardFIT™ and telematics J1939 connections | Was continuity confirmed? **Yes** | **5D** |
> | Was continuity confirmed? **NoRepair:** Locate different public J1939 public connection or repair wiring if 3 pin is known to be a public J1939 connection | **Repeat Step** |  |
>
> STEP 5D. Measure equipment resistance.
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disconnect the J1939 connection; using the equipment J1939 3 pin or 9 Pin service connector measure the equipment resistance | Is the measured resistance 55-65 Ohms? **Yes** | **6A** |
> | Is the measured resistance 55-65 Ohms? **No** | **5E** |  |
>
> STEP 5E. Inspect J1939 backbone terminal resistors.
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect J1939 connection terminal resistors; measure resistance Note: ONLY two 120 Ohms resistors needed in parallel on backbone to achieve a total resistance of 60 Ohms | Is the measured resistance in each resistor 120 Ohms? **Yes** | **6A** |
> | Is the measured resistance in each resistor 120 Ohms? **NoRepair:** Discard and replace resistor(s) | **Repair Complete** |  |
>
> STEP 6. Identify FleetguardFIT™ FMS compatibility.
>
> STEP 6A. Communication baud rate.
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Determine engine, Telematics Service Provider(TSP), and FleetguardFIT™ FMS baud rate **Note:** FleetguardFIT™ FMS modules options are 250 kbps and 500 kbps | Do engine, TSP, and FleetguardFIT™ FMS baud rates match? **Yes** | **7A** |
> | Do engine, TSP, and FleetguardFIT™ FMS baud rates match? **NoRepair:** Replace with proper FleetguardFIT™ FMS module | **Repair Complete** |  |
>
> STEP 7. Identify state of FleetguardFIT™ sensor(s).
>
> STEP 7A. Check telematics portal for FleetguardFIT™ oil quality sensor data.
>
> | **Conditions:** While equipment is on |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Log on to telematics portal and check for FleetguardFIT™ oil quality sensor data | Is any oil quality sensor data visible on portal? **Yes** | **7B** |
> | Is any oil quality sensor data visible on portal? **No** | **9A** |  |
>
> STEP 7B. Oil quality sensor data.
>
> | **Conditions:** While equipment is on |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Log on to telematics portal and check for FleetguardFIT™ oil quality sensor data | Is oil quality sensor data within expected ranges? **Yes** | **7C** |
> | Is oil quality sensor data within expected ranges? **No** | **8A** |  |
>
> STEP 7C. Check telematics portal for FleetguardFIT™ differential pressure and restriction sensor data.
>
> | **Conditions:** While equipment is on |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Log on to telematics portal and check for FleetguardFIT™ differential pressure and restriction sensor data | Is any differential pressure and restriction sensor data visible on portal? **Yes** | **7D** |
> | Is any differential pressure and restriction sensor data visible on portal? **No** | **9A** |  |
>
> STEP 7D. differential pressure and restriction sensor data.
>
> | **Conditions:** While equipment is on |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Log on to telematics portal and check for FleetguardFIT™ differential pressure and restriction sensor data | Is differential pressure and restriction sensor data within expected ranges? **Yes** | **Repair Complete** |
> | Is differential pressure and restriction sensor data within expected ranges? **No** | **8B** |  |
>
> STEP 8. Identify state of FleetguardFIT™ sensor installations.
>
> STEP 8A. Oil quality sensor.
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect oil quality sensor installation | Is the sensor tip located in an area with hot pressurized flowing oil and no leaks? **Yes** | **9A** |
> | Is the sensor tip located in an area with hot pressurized flowing oil and no leaks? **NoRepair:** Relocate oil quality sensor according to FleetguardFIT™ instructions | **Repair Complete** |  |
>
> STEP 8B. Air restriction sensor.
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect air restriction sensor installation | Is the sensor visibly in good condition and connected to air intake system with no leaks? **Yes** | **8C** |
> | Is the sensor visibly in good condition and connected to air intake system with no leaks? **NoRepair:** Replace restriction sensor | **Repair Complete** |  |
>
> STEP 8C. differential pressure sensor(s).
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect differential pressure sensor installation | Is the sensor properly connected to an inlet and outlet port of the filter head with no leaks? **Yes** | **9A** |
> | Is the sensor properly connected to an inlet and outlet port of the filter head with no leaks? **NoRepair:** Properly connect differential pressure sensor to inlet/outlet ports of the filter head. Replace hardware if needed. | **Repair Complete** |  |
>
> STEP 9. Identify state of FleetguardFIT™ sensor extension harnesses and FMS.
>
> STEP 9A. Sensor breakout harness and extension harness condition.
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Carefully inspect sensor breakout harness and extension harness | Are electrical harnesses in good condition with no damage, i.e. no tears? **Yes** | **9B** |
> | Are electrical harnesses in good condition with no damage, i.e. no tears? **NoRepair:** Replace or repair harness | **Repair Complete** |  |
>
> STEP 9B. Sensor breakout harness and extension harness connection.
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Carefully inspect sensor breakout harness and extension harness | Are electrical harnesses connected properly to FMS, breakout harness, and each sensor? **Yes** | **9C** |
> | Are electrical harnesses connected properly to FMS, breakout harness, and each sensor? **NoRepair:** Connect wire(s) that are not connected | **Repair Complete** |  |
>
> STEP 9C. Sensor breakout harness and extension harness continuity.
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure continuity from end to end for breakout harness and each extension harness | Was continuity confirmed? **YesRepair:** Replace sensor | **9D** |
> | Was continuity confirmed? **NoRepair:** Fix or replace harnesses | **Repair complete** |  |
>
> STEP 9D. FMS module replacement.
>
> | **Conditions:** While equipment is off |  |  |
> |---|---|---|
> | **Specification/Repair** | **Action** | **Next Step** |
> | Is data available and within expected ranges? **Yes** | Log on to telematics portal and check faulty equipment for FleetguardFIT™ data | **Repair Complete** |
> | Is data available and within expected ranges? **NoRepair:** Replace FMS module | **Contact:FIT.Support@cummins.com** |  |
>
> ### Document History
