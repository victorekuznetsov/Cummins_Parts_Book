---
aliases:
  - "Нет связи по SAE J1939 с дистанционным пультом"
type: "Процедура"
doc: "115-t02-1040"
title_en: "No SAE J1939 Communication Remote Panel"
title_ru: "Нет связи по SAE J1939 с дистанционным пультом"
modified: "2007-01-08"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021587"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1040.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1040.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/115"
  - "перевод/машинный"
---

# No SAE J1939 Communication Remote Panel
**Нет связи по SAE J1939 с дистанционным пультом**

> [!abstract] Процедура · `115-t02-1040`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]]
> **Секции:** Section TT — Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2007-01-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1040.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1040.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- SAE J1939 Связь с пультом дистанционного управления панелью приборов.

- Панель машинного отделения имеет связь SAE J1939.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения неполадок в коммуникативных симптомах SAE J1939.

Начните с проверки конечных резисторов. Есть два конечных резистора. Конечные резисторы расположены в следующих точках:

Один резистор расположен на ремне жгута проводов двигателя.

Другой резистор расположен на последней удаленной панели, на концевой полосе X4 между терминалами SAE J1939 Supply и SAE J1939 Return.

Шаг 1 задаст ряд вопросов и предоставит список шагов по устранению неполадок, в зависимости от симптома.

### Практические замечания

Шина данных SAE J1939 CAN предоставляет информацию приборной панели в удаленной панели.

Шина данных SAE J1939 CAN обеспечивает следующие параметры:

- Коды неисправностей двигателя

- Параметры двигателя, контролируемые ECM.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | SAE J1939 CAN Data Bus Сигнал |  |
|  | **ШАГ 1А.** Проверить SAE J1939 CAN Data Bus Communication on Engine | Коммуникация установлена? |
|  | **STEP 1B.** Проверьте SAE J1939 Связь с шиной данных в удаленной панели | Коммуникация установлена? |
| ШАГ 2. | Проверьте удаленную панель Wiring |  |
|  | **STEP 2A.** Проверить удаленную панель SAE J1939 CAN шину передачи данных Провода (Подключатель панели инструментов к разъему порта обслуживания) | Сопротивление менее 10 Ом? |
|  | **STEP 2B.** Проверить удаленную панель SAE J1939 CAN Data Bus Return Wire (Подключение панели инструментов к порту обслуживания) | Сопротивление менее 10 Ом? |
|  | **STEP 2C.** Проверить удаленную панель SAE J1939 CAN шину данных Shield Wire (Подключатель панели инструментов к разъему порта обслуживания) | Сопротивление менее 10 Ом? |
| ШАГ 3. | Проверьте кабели Панельной системы |  |
|  | **STEP 3A.** Проверить кабель дистанционной панели (SAE J1939) | Сопротивление менее 10 Ом? |
|  | **STEP 3B.** Проверить кабель дистанционной панели (SAE J1939 Return and Shield Wires) | Сопротивление менее 10 Ом? |
|  | **STEP 3C.** Проверка кабеля панели машинного отделения (SAE J1939 Провода снабжения и возврата) | Сопротивление менее 10 Ом? |
|  | **STEP 3D.** Проверка кабеля панели машинного отделения (SAE J1939 Return and Shield Wires) | Сопротивление менее 10 Ом? |
| ШАГ 4. | Проверка проводки интерфейсной коробки заказчика |  |
|  | **STEP 4A.** Проверить SAE J1939 КАН шина передачи данных Провод | Сопротивление менее 10 Ом? |
|  | **STEP 4B.** Проверьте SAE J1939 МОЖЕТ ли шина данных Return Wire | Сопротивление менее 10 Ом? |
|  | **STEP 4C.** Проверить SAE J1939 можно шиной данных Shield Wire | Сопротивление менее 10 Ом? |
| ШАГ 5. | Проверка проводов панели Engine Room |  |
|  | **STEP 5A.** Проверьте SAE J1939 CAN шину передачи данных Провод (C14 Connector to Instrument Panel Connector) | Сопротивление менее 10 Ом? |
|  | **STEP 5B.** Проверьте SAE J1939 CAN шину данных Return Wire (C14 Connector to Instrument Panel Connector) | Сопротивление менее 10 Ом? |
|  | **STEP 5C.** Проверьте шину данных SAE J1939 CAN Shield Wire (C14 Connector to Instrument Panel Connector) | Сопротивление менее 10 Ом? |
| ШАГ 6. | Проверьте Display Wiring |  |
|  | **STEP 6A.** Проверить удаленную панель SAE J1939 CAN шину передачи данных Провод (Подключатель панели инструментов для отображения) | Сопротивление менее 10 Ом? |
|  | **STEP 6B.** Проверить удаленную панель SAE J1939 CAN шину данных Return Wire (Подключатель панели инструментов для отображения) | Сопротивление менее 10 Ом? |

### ШАГ 1. SAE J1939 CAN Data Bus Сигнал

#### ШАГ 1A. SAE J1939 CAN Data Bus Communication on Engine (Связь с двигателем)

| **Условия:** Найдите электропроводку двигателя, подключите электронный сервисный инструмент INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить SAE J1939 можно по шине передачи данных. Используйте инструмент электронного обслуживания INSITETM для установления связи. | Коммуникация установлена? *Да | 1В |
| Коммуникация установлена? **NORepair:** См. руководство по устранению неполадок и ремонту, электронная система управления, двигатели серии модульных систем общей железнодорожной системы QSK19 CM850, Bulletin 4021493. | Ремонт завершён. |  |

#### ШАГ 1B. Проверить SAE J1939 Связь с шиной данных на удаленной панели

| **Условия:** Расположение удаленной панели Подключение электронного сервисного инструментария. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить SAE J1939 можно по шине передачи данных. Используйте инструмент электронного обслуживания INSITETM для установления связи. | Коммуникация установлена? *Да | 6А |
| Коммуникация установлена? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте удаленную панель Wiring

#### ШАГ 2A. Проверить удаленную панель SAE J1939 CAN шину передачи данных Провода (Подключение панели инструментов к порту обслуживания Подключение)

| **Условия:** Расположение удаленной панели. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте удаленную проводку панели. Отсоедините кабель дистанционной панели от приборной панели разъема X4. Подключите один испытательный щуп на удаленной панели SAE J1939 CAN передачи данных контакта на приборной панели разъема X4. Поместите другой испытательный щуп на удаленную панель SAE J1939 CAN передачи данных шины контакта на разъеме порта обслуживания. | Сопротивление менее 10 Ом? *Да | 2В |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-025 — Remote Panel\|015-025]]. | 1В |  |

#### ШАГ 2B. Проверить удаленную панель SAE J1939 CAN Data Bus Return Wire (Подключение панели инструментов к порту обслуживания)

| **Условия:** Расположение удаленной панели. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте удаленную проводку панели. Отсоедините удаленный панельный кабель от разъема панели приборов. Подключите один испытательный щуп на удаленной панели SAE J1939 CAN обратного контакта шины данных на разъеме панели приборов. Поместите другой измерительный щуп на удаленную панель SAE J1939 CAN обратного контакта шины данных на разъеме порта обслуживания. | Сопротивление менее 10 Ом? *Да | 2C |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-025 — Remote Panel\|015-025]]. | 1В |  |

#### ШАГ 2C. Проверить удаленную панель SAE J1939 CAN шину данных Shield Wire (Подключение панели инструментов к порту обслуживания)

| **Условия:** Расположение удаленной панели |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте удаленную проводку панели. Отсоедините удаленный панельный кабель от разъема панели приборов. Подключите один испытательный щуп на удаленной панели SAE J1939 CAN щитовой штифт шины данных на разъеме панели приборов. Поместите другой измерительный щуп на удаленную панель SAE J1939 CAN щитовой штифт шины данных на разъем порта обслуживания. | Сопротивление менее 10 Ом? *Да | 3А |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-025 — Remote Panel\|015-025]]. | 1В |  |

### ШАГ 3. Проверьте кабели Панельной системы

#### ШАГ 3A. Проверка кабеля с дистанционным управлением (SAE J1939 Supply and Return Wires)

| **Условия:** Найти и открыть окно интерфейса клиента Найти удаленную панель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте кабель удаленной панели. Установите перемычку между терминалом передачи данных шины SAE J1939 CAN и терминалом возврата шины данных удаленной панели SAE J1939 CAN на панели приборов X4 в удаленной панели. Поместите один измерительный щуп в терминал передачи данных SAE J1939 CAN в разъеме клиентского интерфейса X4. Поместите другой измерительный щуп в терминал возврата шины данных SAE J1939 CAN в разъеме интерфейса клиента X4. | Сопротивление менее 10 Ом? *Да | 3B |
| Сопротивление менее 10 Ом? **Заменить кабель.** | Ремонт завершён. |  |

#### ШАГ 3B. Проверка кабеля дистанционной панели (SAE J1939 Return and Shield Wires)

| **Условия:** Найти и открыть окно интерфейса клиента Найти удаленную панель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте кабель удаленной панели. Установите перемычку между терминалом возврата шины данных SAE J1939 CAN и терминалом экрана шины данных SAE J1939 CAN на панели приборов X4 в удаленной панели. Поместите один измерительный щуп на терминал возврата шины данных SAE J1939 CAN в разъеме клиентского интерфейса X4. Поместите другой измерительный щуп на терминал шины данных SAE J1939 CAN в разъеме интерфейса клиента X4. | Сопротивление менее 10 Ом? *Да | 3C |
| Сопротивление менее 10 Ом? **Заменить кабель.** | Ремонт завершён. |  |

#### ШАГ 3C. Проверка кабеля панели машинного отделения (SAE J1939 Провода снабжения и возврата)

| **Условия:** Отсоединить кабельный разъем С14 от панели машинного отделения. Отсоедините кабельный разъем C7 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте кабель панели машинного отделения. Установите перемычку между панелью блока питания шины данных SAE J1939 CAN и панелью блока данных машинного отделения SAE J1939 CAN обратного контакта шины данных в разъёме C14. Поместите один испытательный щуп в панель машинного отделения SAE J1939 CAN для передачи данных шины контакта в разъеме C7. Поместите другой испытательный щуп в панель машинного отделения SAE J1939 CAN с обратной связью шины данных в разъеме C7. | Сопротивление менее 10 Ом? *Да | 3D |
| Сопротивление менее 10 Ом? **Заменить кабель.** | Ремонт завершён. |  |

#### ШАГ 3D. Проверка кабеля панели машинного отделения (SAE J1939 Return and Shield Wires)

| **Условия:** Отсоединить кабельный разъем С14 от панели машинного отделения. Отсоедините кабельный разъем C7 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте кабель панели машинного отделения. Установите перемычку между панелью шин SAE J1939 CAN для обратного контакта с шиной данных КАН и панелью щита шин данных SAE J1939 CAN для шин данных КАН в разъёме C14. Поместите один испытательный щуп в панель машинного отделения SAE J1939 CAN Data Bus обратного контакта в разъеме C7. Поместите другой испытательный щуп в панель машинного отделения SAE J1939 CAN щитовой штифт шины данных в разъем C7. | Сопротивление менее 10 Ом? *Да | 4А |
| Сопротивление менее 10 Ом? **Заменить кабель.** | Ремонт завершён. |  |

### ШАГ 4. Проверка проводки интерфейсной коробки заказчика

#### ШАГ 4A. SAE J1939 CAN Data Bus Провода для передачи данных

| **Условия:** Откройте окно интерфейса клиента Отключите кабель машинного отделения на разъеме C7 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить провода питания шины данных SAE J1939 CAN. Поместите один измерительный щуп на штифт передачи данных SAE J1939 CAN (C3) в разъем C7. Поместите другой измерительный щуп на двигатель SAE J1939 CAN терминала передачи данных шины в разъеме клиентского интерфейса X4. | Сопротивление менее 10 Ом? *Да | 4B |
| Сопротивление менее 10 Ом? **NORepair:** Заменить провод. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

#### ШАГ 4B. SAE J1939 может возвращать данные

| **Условия:** Откройте окно интерфейса клиента Отключите кабель машинного отделения на разъеме C7 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить данные на шине SAE J1939 можно по проводу обратной связи. Поместите один измерительный щуп на штифт возврата шины данных SAE J1939 CAN (C3) в разъем C7. Поместите другой измерительный щуп на терминал возврата шины данных SAE J1939 CAN в разъеме интерфейса клиента X4. | Сопротивление менее 10 Ом? *Да | 4C |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

#### ШАГ 4C. SAE J1939 может работать с шиной данных Shield Wire

| **Условия:** Откройте окно интерфейса клиента Отключите кабель машинного отделения на разъеме C7 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить провод щита шины данных SAE J1939 CAN. Поместите один измерительный щуп на шину данных SAE J1939 CAN (C3) в разъем C7. Поместите другой измерительный щуп на терминал шины данных SAE J1939 CAN в разъеме интерфейса клиента X4. | Сопротивление менее 10 Ом? *Да | 5а |
| Сопротивление менее 10 Ом? **NORepair:** Заменить провод. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

### ШАГ 5. Проверка проводов панели Engine Room

#### ШАГ 5A. Проверить SAE J1939 CAN шину передачи данных Провода (C14 Connector to Instrument Panel Connector)

| **Условия:** Найдите панель машинного отделения Открытая дверь панели машинного отделения. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверяйте провода между разъёмом жгута проводов и разъемом панели приборов. Отсоедините кабель C14 от панели машинного отделения. Поместите один испытательный щуп на панель машинного отделения SAE J1939 CAN для передачи данных шины контакта на разъеме C14. Поместите другой испытательный щуп на панель машинного отделения SAE J1939 CAN передачи данных на контактную панель приборной панели. | Сопротивление менее 10 Ом? *Да | 5В |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-024 — Engine Room Panel\|015-024]]. | Ремонт завершён. |  |

#### ШАГ 5B. Проверить SAE J1939 CAN шину данных Return Wire (C14 Connector to Instrument Panel Connector)

| **Условия:** Найдите панель машинного отделения Открытая дверь панели машинного отделения. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверяйте провода между разъёмом жгута проводов и разъемом панели приборов. Отсоедините кабель C14 от панели машинного отделения. Поместите один испытательный щуп на панель машинного отделения SAE J1939 CAN Data Bus обратного контакта на разъеме C14. Поместите другой испытательный щуп на панель машинного отделения SAE J1939 CAN обратного контакта шины данных на разъем панели приборов. | Сопротивление менее 10 Ом? *Да | 5С |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-024 — Engine Room Panel\|015-024]]. | Ремонт завершён. |  |

#### ШАГ 5C. Проверить SAE J1939 CAN шину данных Shield Wire (C14 Connector to Instrument Panel Connector)

| **Условия:** Найдите панель машинного отделения Открытая дверь панели машинного отделения. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверяйте провода между разъёмом жгута проводов и разъемом панели приборов. Отсоедините кабель C14 от панели машинного отделения. Поместите один испытательный щуп на панель машинного отделения SAE J1939 CAN на шине данных шины на разъеме C14. Поместите другой испытательный щуп на панель машинного отделения SAE J1939 CAN на разъем панели приборов. | Сопротивление менее 10 Ом? *Да | 6А |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-024 — Engine Room Panel\|015-024]]. | Ремонт завершён. |  |

### ШАГ 6. Проверьте Display Wiring

#### ШАГ 6A. Проверить удаленную панель SAE J1939 CAN шину передачи данных Провод (Подключатель панели инструментов для отображения)

| **Условия:** Расположение удаленной панели. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте удаленную проводку панели. Отсоедините удаленный панельный кабель от разъема панели приборов. Поместите один испытательный щуп на удаленную панель SAE J1939 CAN передачи данных контакта на разъем панели прибора. Поместите другой измерительный щуп на удаленную панель SAE J1939 CAN на дисплее. | Сопротивление менее 10 Ом? *Да | 6B |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-025 — Remote Panel\|015-025]]. | Ремонт завершён. |  |

#### ШАГ 6B. Проверить удаленную панель SAE J1939 CAN Data Bus Return Wire (Подключение панели инструментов к дисплею)

| **Условия:** Расположение панели машинного отделения. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте удаленную проводку панели. Отсоедините удаленный панельный кабель от разъема панели приборов. Поместите один испытательный щуп на удаленную панель SAE J1939 CAN обратного контакта шины данных на разъем панели приборов. Поместите другой измерительный щуп на удаленную панель SAE J1939 CAN Data Bus Return Wire на дисплее. | Сопротивление менее 10 Ом?  Заменить дисплей. См. процедуру[[115-015-025 — Remote Panel\|015-025]]. | Ремонт завершён. |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-025 — Remote Panel\|015-025]]. | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - No SAE J1939 Communication with the remote panel instrument panel.
>
> - Engine room panel has SAE J1939 communication.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot SAE J1939 communications symptoms.
>
> Start by checking the terminating resistors. There are two terminating resistors. The terminating resistors are located at the following points:
>
> One resistor is located on the engine wiring harness.
>
> The other resistor is located at the last remote panel, at the X4 terminal strip between the SAE J1939 Supply and SAE J1939 Return terminals.
>
> Step 1 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> The SAE J1939 datalink provides information to the instrument panel in the remote panel.
>
> The SAE J1939 datalink provides the following parameters:
>
> - Engine fault codes
>
> - Engine parameters monitored by the ECM.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check SAE J1939 Datalink Signal |  |
> |  | **STEP 1A.** Check SAE J1939 Datalink Communication on Engine | Communication established? |
> |  | **STEP 1B.** Check SAE J1939 Datalink Communication at Remote Panel | Communication established? |
> | STEP 2. | Check Remote Panel Wiring |  |
> |  | **STEP 2A.** Check Remote Panel SAE J1939 Datalink Supply Wire (Instrument Panel Connector to Service Port Connector) | Less than 10 ohms resistance? |
> |  | **STEP 2B.** Check Remote Panel SAE J1939 Datalink Return Wire (Instrument Panel Connector to Service Port Connector) | Less than 10 ohms resistance? |
> |  | **STEP 2C.** Check Remote Panel SAE J1939 Datalink Shield Wire (Instrument Panel Connector to Service Port Connector) | Less than 10 ohms resistance? |
> | STEP 3. | Check Panel System Cables |  |
> |  | **STEP 3A.** Check Remote Panel Cable (SAE J1939 Supply and Return Wires) | Less than 10 ohms resistance? |
> |  | **STEP 3B.** Check Remote Panel Cable (SAE J1939 Return and Shield Wires) | Less than 10 ohms resistance? |
> |  | **STEP 3C.** Check Engine Room Panel Cable (SAE J1939 Supply and Return Wires) | Less than 10 ohms resistance? |
> |  | **STEP 3D.** Check Engine Room Panel Cable (SAE J1939 Return and Shield Wires) | Less than 10 ohms resistance? |
> | STEP 4. | Check Customer Interface Box Wiring |  |
> |  | **STEP 4A.** Check SAE J1939 Datalink Supply Wire | Less than 10 ohms resistance? |
> |  | **STEP 4B.** Check SAE J1939 Datalink Return Wire | Less than 10 ohms resistance? |
> |  | **STEP 4C.** Check SAE J1939 Datalink Shield Wire | Less than 10 ohms resistance? |
> | STEP 5. | Check Engine Room Panel Wiring |  |
> |  | **STEP 5A.** Check SAE J1939 Datalink Supply Wire (C14 Connector to Instrument Panel Connector) | Less than 10 ohms resistance? |
> |  | **STEP 5B.** Check SAE J1939 Datalink Return Wire (C14 Connector to Instrument Panel Connector) | Less than 10 ohms resistance? |
> |  | **STEP 5C.** Check SAE J1939 Datalink Shield Wire (C14 Connector to Instrument Panel Connector) | Less than 10 ohms resistance? |
> | STEP 6. | Check Display Wiring |  |
> |  | **STEP 6A.** Check Remote Panel SAE J1939 Datalink Supply Wire (Instrument Panel Connector to Display) | Less than 10 ohms resistance? |
> |  | **STEP 6B.** Check Remote Panel SAE J1939 Datalink Return Wire (Instrument Panel Connector to Display) | Less than 10 ohms resistance? |
>
> ### STEP 1. Check SAE J1939 Datalink Signal
>
> #### STEP 1A. Check SAE J1939 Datalink Communication on Engine
>
> | **Conditions:** Locate engine wiring harness Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check SAE J1939 datalink communication. Use INSITE™ electronic service tool to establish communication. | Communication established? **YES** | 1B |
> | Communication established? **NORepair:** Refer to the Troubleshooting and Repair Manual, Electronic Control System, QSK19 CM850 Modular Common Rail System Series Engines, Bulletin 4021493. | Repair complete. |  |
>
> #### STEP 1B. Check SAE J1939 Datalink Communication at Remote Panel
>
> | **Conditions:** Locate remote panel Connect electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check SAE J1939 datalink communications. Use INSITE™ electronic service tool to establish communication. | Communication established? **YES** | 6A |
> | Communication established? **NO** | 2A |  |
>
> ### STEP 2. Check Remote Panel Wiring
>
> #### STEP 2A. Check Remote Panel SAE J1939 Datalink Supply Wire (Instrument Panel Connector to Service Port Connector)
>
> | **Conditions:** Locate remote panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check remote panel wiring. Disconnect remote panel cable from the instrument panel X4 connector. Connect one test lead on the remote panel SAE J1939 datalink supply pin on the instrument panel X4 connector. Place the other test lead on the remote panel SAE J1939 datalink supply pin on the service port connector. | Less than 10 ohms resistance? **YES** | 2B |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-025 — Remote Panel\|015-025]]. | 1B |  |
>
> #### STEP 2B. Check Remote Panel SAE J1939 Datalink Return Wire (Instrument Panel Connector to Service Port Connector)
>
> | **Conditions:** Locate remote panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check remote panel wiring. Disconnect remote panel cable from the instrument panel connector. Connect one test lead on the remote panel SAE J1939 datalink return pin on the instrument panel connector. Place the other test lead on the remote panel SAE J1939 datalink return pin on the service port connector. | Less than 10 ohms resistance? **YES** | 2C |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-025 — Remote Panel\|015-025]]. | 1B |  |
>
> #### STEP 2C. Check Remote Panel SAE J1939 Datalink Shield Wire (Instrument Panel Connector to Service Port Connector)
>
> | **Conditions:** Locate remote panel |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check remote panel wiring. Disconnect remote panel cable from the instrument panel connector. Connect one test lead on the remote panel SAE J1939 datalink shield pin on the instrument panel connector. Place the other test lead on the remote panel SAE J1939 datalink shield pin on the service port connector. | Less than 10 ohms resistance? **YES** | 3A |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-025 — Remote Panel\|015-025]]. | 1B |  |
>
> ### STEP 3. Check Panel System Cables
>
> #### STEP 3A. Check Remote Panel Cable (SAE J1939 Supply and Return Wires)
>
> | **Conditions:** Locate and open customer interface box Locate remote panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the remote panel cable. Install a jumper between the remote panel SAE J1939 datalink supply terminal and the remote panel SAE J1939 datalink return terminal on instrument panel X4 in the remote panel. Place one test lead in the SAE J1939 datalink supply terminal in customer interface box X4 connector. Place the other test lead in the SAE J1939 datalink return terminal in the customer interface box X4 connector. | Less than 10 ohms resistance? **YES** | 3B |
> | Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |
>
> #### STEP 3B. Check Remote Panel Cable (SAE J1939 Return and Shield Wires)
>
> | **Conditions:** Locate and open customer interface box Locate remote panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the remote panel cable. Install a jumper between remote panel SAE J1939 datalink return terminal and the remote panel SAE J1939 datalink shield terminal on instrument panel X4 in the remote panel. Place one test lead on the SAE J1939 datalink return terminal in customer interface box X4 connector. Place the other test lead on the SAE J1939 datalink shield terminal in the customer interface box X4 connector. | Less than 10 ohms resistance? **YES** | 3C |
> | Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |
>
> #### STEP 3C. Check Engine Room Panel Cable (SAE J1939 Supply and Return Wires)
>
> | **Conditions:** Disconnect cable connector C14 from the engine room panel. Disconnect cable connector C7 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine room panel cable. Install a jumper between engine room panel SAE J1939 datalink supply pin and the engine room panel SAE J1939 datalink return pin in connector C14. Place one test lead in the engine room panel SAE J1939 datalink supply pin in connector C7. Place the other test lead in the engine room panel SAE J1939 datalink return pin in connector C7. | Less than 10 ohms resistance? **YES** | 3D |
> | Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |
>
> #### STEP 3D. Check Engine Room Panel Cable (SAE J1939 Return and Shield Wires)
>
> | **Conditions:** Disconnect cable connector C14 from the engine room panel. Disconnect cable connector C7 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine room panel cable. Install a jumper between engine room panel SAE J1939 datalink return pin and the engine room panel SAE J1939 datalink shield pin in connector C14. Place one test lead in the engine room panel SAE J1939 datalink return pin in connector C7. Place the other test lead in the engine room panel SAE J1939 datalink shield pin in connector C7. | Less than 10 ohms resistance? **YES** | 4A |
> | Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |
>
> ### STEP 4. Check Customer Interface Box Wiring
>
> #### STEP 4A. Check SAE J1939 Datalink Supply Wire
>
> | **Conditions:** Open the customer interface box Disconnect engine room cable at connector C7 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the SAE J1939 datalink supply wire. Place one test lead on the SAE J1939 datalink supply (C3) pin in connector C7. Place the other test lead on the engine SAE J1939 datalink supply terminal in the customer interface box X4 connector. | Less than 10 ohms resistance? **YES** | 4B |
> | Less than 10 ohms resistance? **NORepair:** Replace the wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> #### STEP 4B. Check SAE J1939 Datalink Return Wire
>
> | **Conditions:** Open the customer interface box Disconnect engine room cable at connector C7 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the SAE J1939 datalink return wire. Place one test lead on the SAE J1939 datalink return (C3) pin in connector C7. Place the other test lead on the SAE J1939 datalink return terminal in the customer interface box X4 connector. | Less than 10 ohms resistance? **YES** | 4C |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> #### STEP 4C. Check SAE J1939 Datalink Shield Wire
>
> | **Conditions:** Open the customer interface box Disconnect engine room cable at connector C7 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the SAE J1939 datalink shield wire. Place one test lead on the SAE J1939 datalink shield (C3) pin in connector C7. Place the other test lead on the SAE J1939 datalink shield terminal in the customer interface box X4 connector. | Less than 10 ohms resistance? **YES** | 5A |
> | Less than 10 ohms resistance? **NORepair:** Replace the wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> ### STEP 5. Check Engine Room Panel Wiring
>
> #### STEP 5A. Check SAE J1939 Datalink Supply Wire (C14 Connector to Instrument Panel Connector)
>
> | **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check wires between harness connector and instrument panel connector. Disconnect cable C14 from the engine room panel. Place one test lead on the engine room panel SAE J1939 datalink supply pin on connector C14. Place the other test lead on the engine room panel SAE J1939 datalink supply pin on the instrument panel connector. | Less than 10 ohms resistance? **YES** | 5B |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |
>
> #### STEP 5B. Check SAE J1939 Datalink Return Wire (C14 Connector to Instrument Panel Connector)
>
> | **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check wires between harness connector and instrument panel connector. Disconnect cable C14 from the engine room panel. Place one test lead on the engine room panel SAE J1939 datalink return pin on connector C14. Place the other test lead on the engine room panel SAE J1939 datalink return pin on the instrument panel connector. | Less than 10 ohms resistance? **YES** | 5C |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |
>
> #### STEP 5C. Check SAE J1939 Datalink Shield Wire (C14 Connector to Instrument Panel Connector)
>
> | **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check wires between harness connector and instrument panel connector. Disconnect cable C14 from the engine room panel. Place one test lead on the engine room panel SAE J1939 datalink shield pin on connector C14. Place the other test lead on the engine room panel SAE J1939 datalink shield pin on the instrument panel connector. | Less than 10 ohms resistance? **YES** | 6A |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |
>
> ### STEP 6. Check Display Wiring
>
> #### STEP 6A. Check Remote Panel SAE J1939 Datalink Supply Wire (Instrument Panel Connector to Display)
>
> | **Conditions:** Locate remote panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check remote panel wiring. Disconnect remote panel cable from the instrument panel connector. Place one test lead on the remote panel SAE J1939 datalink supply pin on the instrument panel connector. Place the other test lead on the remote panel SAE J1939 datalink supply wire at the display. | Less than 10 ohms resistance? **YES** | 6B |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-025 — Remote Panel\|015-025]]. | Repair complete. |  |
>
> #### STEP 6B. Check Remote Panel SAE J1939 Datalink Return Wire (Instrument Panel Connector to Display)
>
> | **Conditions:** Locate engine room panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check remote panel wiring. Disconnect remote panel cable from the instrument panel connector. Place one test lead on the remote panel SAE J1939 datalink return pin on the instrument panel connector. Place the other test lead on the remote panel SAE J1939 datalink return wire at the display. | Less than 10 ohms resistance? **YESRepair:** Replace the display. Refer to Procedure [[115-015-025 — Remote Panel\|015-025]]. | Repair complete. |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-025 — Remote Panel\|015-025]]. | Repair complete. |  |
