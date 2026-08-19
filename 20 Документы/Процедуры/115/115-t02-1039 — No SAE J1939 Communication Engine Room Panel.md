---
aliases:
  - "Нет связи по SAE J1939 с пультом машинного отделения"
type: "Процедура"
doc: "115-t02-1039"
title_en: "No SAE J1939 Communication Engine Room Panel"
title_ru: "Нет связи по SAE J1939 с пультом машинного отделения"
modified: "2007-01-08"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021587"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1039.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/115-t02-1039.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/115"
  - "перевод/машинный"
---

# No SAE J1939 Communication Engine Room Panel
**Нет связи по SAE J1939 с пультом машинного отделения**

> [!abstract] Процедура · `115-t02-1039`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]]
> **Секции:** Section TT — Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2007-01-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1039.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/115-t02-1039.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- SAE J1939 Связь с панелью приборов машинного отделения.

- Дистанционная панель имеет SAE J1939 связи.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения неполадок в коммуникативных симптомах SAE J1939. Начните с проверки конечных резисторов. Есть два конечных резистора. Конечные резисторы расположены в следующих точках:

Один резистор расположен на ремне жгута проводов двигателя.

Если используется удаленная панель (панели), второй резистор расположен на последней удаленной панели на концевой полосе X4 между терминалами SAE J1939 Supply и SAE J1939 Return.

Если удаленная панель не используется, второй резистор находится в поле интерфейса клиента на терминале X4 между терминалами SAE J1939 Supply и SAE J1939 Return.

Шаг 1 задаст ряд вопросов и предоставит список шагов по устранению неполадок, в зависимости от симптома.

### Практические замечания

Шина данных SAE J1939 CAN предоставляет информацию приборной панели в панели машинного отделения.

Шина данных SAE J1939 CAN обеспечивает следующие параметры:

- Коды неисправностей двигателя

- Параметры двигателя, контролируемые ECM.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | SAE J1939 CAN Data Bus Сигнал |  |
|  | **ШАГ 1А.** Проверить SAE J1939 CAN Data Bus Communication on Engine | Коммуникация установлена? |
|  | **STEP 1B.** Проверьте SAE J1939 Связь с шиной данных в панели машинного отделения | Коммуникация установлена? |
| ШАГ 2. | Проверить Panel Wiring |  |
|  | **STEP 2A.** Панель управления двигателем SAE J1939 CAN шина передачи данных Провод (Подключатель панели инструментов к разъёму порта обслуживания) | Сопротивление менее 10 Ом? |
|  | **STEP 2B.** Панель управления двигателем SAE J1939 CAN шина передачи данных Return Wire (Подключатель панели инструментов к разъему порта обслуживания) | Сопротивление менее 10 Ом? |
|  | **STEP 2C.** Панель управления двигателем SAE J1939 CAN шина передачи данных Shield Wire (Подключатель панели инструментов к разъему порта обслуживания) | Сопротивление менее 10 Ом? |
|  | **STEP 2D.** Проверьте SAE J1939 CAN шину передачи данных Провод (C14 Connector to Instrument Panel Connector) | Сопротивление менее 10 Ом? |
|  | **STEP 2E.** Проверьте SAE J1939 CAN шину данных Return Wire (C14 Connector to Instrument Panel Connector) | Сопротивление менее 10 Ом? |
|  | **STEP 2F.** Проверьте шину данных SAE J1939 CAN Shield Wire (C14 Connector to Instrument Panel Connector) | Сопротивление менее 10 Ом? |
| ШАГ 3. | Проверьте панельную систему кабеля |  |
|  | **STEP 3A.** Проверка кабеля панели машинного отделения (SAE J1939 Провода снабжения и возврата) | Сопротивление менее 10 Ом? |
|  | **STEP 3B.** Проверка кабеля панели машинного отделения (SAE J1939 Return and Shield Wires) | Сопротивление менее 10 Ом? |
|  | **STEP 3C.** Проверить кабель клиентского интерфейса (SAE J1939) | Сопротивление менее 10 Ом? |
|  | **STEP 3D.** Проверить кабель интерфейса клиента (SAE J1939 Return and Shield Wires) | Сопротивление менее 10 Ом? |
| ШАГ 4. | Проверка проводки интерфейсной коробки заказчика |  |
|  | **STEP 4A.** Проверить SAE J1939 КАН шина передачи данных Провод | Сопротивление менее 10 Ом? |
|  | **STEP 4B.** Проверьте SAE J1939 МОЖЕТ ли шина данных Return Wire | Сопротивление менее 10 Ом? |
|  | **STEP 4C.** Проверить SAE J1939 можно шиной данных Shield Wire | Сопротивление менее 10 Ом? |
| ШАГ 5. | Проверьте Display Wiring |  |
|  | **STEP 5A.** Панель управления двигателем SAE J1939 CAN шина передачи данных Провод (панель приборов X4 для отображения) | Сопротивление менее 10 Ом? |
|  | **STEP 5B.** Панель управления двигателем SAE J1939 CAN шина передачи данных Return Wire (панель управления X4 для отображения) | Сопротивление менее 10 Ом? |

### ШАГ 1. SAE J1939 CAN Data Bus Сигнал

#### ШАГ 1A. SAE J1939 CAN Data Bus Communication on Engine (Связь с двигателем)

| **Условия: ** Включен выключатель питания панели машинного отделения и освещенная лампа питания Расположение проводов двигателя Узлы подключения INSITETM электронный сервисный инструмент. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверить SAE J1939 можно по шине передачи данных. Используйте инструмент электронного обслуживания INSITETM для установления связи. | Коммуникация установлена? *Да** | 1В |
| Коммуникация установлена? **NORepair: ** См. Руководство по устранению неполадок и ремонту, Электронная система управления, QSK19 CM850, Модульная общая железнодорожная система, Серийные двигатели, Бюллетень 4021493. | Ремонт завершён. |  |

#### ШАГ 1B. Проверить SAE J1939 МОЖНО Связаться с шиной данных в панели машинного отделения

| ** Условия:** Найдите панель машинного отделения Connect INSITETM для электронного обслуживания. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверить SAE J1939 можно по шине передачи данных. Используйте инструмент электронного обслуживания INSITETM для установления связи. | Коммуникация установлена? *Да** | 5а |
| Коммуникация установлена? ** НЕТ** | 2А. |  |

### ШАГ 2. Проверить Panel Wiring

#### ШАГ 2A. Панель управления машинным отделением SAE J1939 CAN Data Bus Supply Wire (Подключение панели инструментов к разъёму порта обслуживания)

| ** Условия: ** Найдите панель машинного отделения Открытая дверь панели машинного отделения. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте проводку панели машинного отделения. Отсоедините кабель C14 от панели машинного отделения. Подключите один испытательный щуп на панели питания машинного отделения SAE J1939 CAN к контакту питания шины данных на разъеме панели приборов Поместите другой испытательный щуп на панели управления двигателем SAE J1939 CAN к контакту питания шины данных на разъеме порта обслуживания. | Сопротивление менее 10 Ом? *Да** | 2В |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-024 — Engine Room Panel\|015-024]]. | 1В |  |

#### ШАГ 2B. Панель управления двигателем SAE J1939 CAN Data Bus Return Wire (Подключение панели инструментов к порту обслуживания)

| ** Условия: ** Найдите панель машинного отделения Открытая дверь панели машинного отделения. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте проводку панели машинного отделения. Отсоедините кабель C14 от панели машинного отделения. Подключите один испытательный щуп на панели машинного отделения SAE J1939 CAN Data Bus обратного контакта на разъеме приборной панели. Поместите другой испытательный щуп на панель машинного отделения SAE J1939 CAN Data Bus обратного контакта на разъеме порта обслуживания. | Сопротивление менее 10 Ом? *Да** | 2C |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-024 — Engine Room Panel\|015-024]]. | 1В |  |

#### ШАГ 2C. Панель управления двигателем SAE J1939 CAN шина данных Shield Wire (Подключатель панели инструментов к разъему порта обслуживания)

| ** Условия: ** Найдите панель машинного отделения Открытая дверь панели машинного отделения. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте проводку панели машинного отделения. Отсоедините кабель C14 от панели машинного отделения. Подключите один испытательный щуп на панели машинного отделения SAE J1939 CAN щитовой штифт шины данных на разъеме панели приборов. Поместите другой испытательный щуп на панель машинного отделения SAE J1939 CAN щитовой штифт шины данных на разъем порта обслуживания. | Сопротивление менее 10 Ом? *Да** | 2D |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-024 — Engine Room Panel\|015-024]]. | 1В |  |

#### ШАГ 2D. Проверить SAE J1939 CAN шину передачи данных Провода (C14 Connector to Instrument Panel Connector)

| ** Условия: ** Найдите панель машинного отделения Открытая дверь панели машинного отделения. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверяйте провода между разъёмом жгута проводов и разъемом панели приборов. Отсоедините кабель C14 от панели машинного отделения. Поместите один испытательный щуп на панель машинного отделения SAE J1939 CAN для передачи данных шины контакта на разъеме C14. Поместите другой испытательный щуп на панель машинного отделения SAE J1939 CAN передачи данных на контактную панель приборной панели. | Сопротивление менее 10 Ом? *Да** | 2Е |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-024 — Engine Room Panel\|015-024]]. | Ремонт завершён. |  |

#### ШАГ 2E. Проверить SAE J1939 CAN шину данных Return Wire (C14 Connector to Instrument Panel Connector)

| ** Условия: ** Найдите панель машинного отделения Открытая дверь панели машинного отделения. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверяйте провода между разъёмом жгута проводов и разъемом панели приборов. Отсоедините кабель C14 от панели машинного отделения. Поместите один испытательный щуп на панель машинного отделения SAE J1939 CAN Data Bus обратного контакта на разъеме C14. Поместите другой испытательный щуп на панель машинного отделения SAE J1939 CAN обратного контакта шины данных на разъем панели приборов. | Сопротивление менее 10 Ом? *Да** | 2F |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-024 — Engine Room Panel\|015-024]]. | Ремонт завершён. |  |

#### ШАГ 2F. Проверить SAE J1939 CAN шину данных Shield Wire (C14 Connector to Instrument Panel Connector)

| ** Условия: ** Найдите панель машинного отделения Открытая дверь панели машинного отделения. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверяйте провода между разъёмом жгута проводов и разъемом панели приборов. Отсоедините кабель C14 от панели машинного отделения. Поместите один испытательный щуп на панель машинного отделения SAE J1939 CAN на шине данных шины на разъеме C14. Поместите другой испытательный щуп на панель машинного отделения SAE J1939 CAN на разъем панели приборов. | Сопротивление менее 10 Ом? *Да** | 3А |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-024 — Engine Room Panel\|015-024]]. | Ремонт завершён. |  |

### ШАГ 3. Проверьте кабели Панельной системы

#### ШАГ 3A. Проверка кабеля панели машинного отделения (SAE J1939 Провода снабжения и возврата)

| **Условия:** Отсоединить кабельный разъём С14 от панели машинного отделения Отключить кабельный разъём С7 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте кабель панели машинного отделения. Установите перемычку между панелью блока питания шины данных SAE J1939 CAN и панелью блока данных машинного отделения SAE J1939 CAN обратного контакта шины данных в разъёме C14. Поместите один испытательный щуп в панель машинного отделения SAE J1939 CAN для передачи данных шины контакта в разъеме C7. Поместите другой испытательный щуп в панель машинного отделения SAE J1939 CAN с обратной связью шины данных в разъеме C7. | Сопротивление менее 10 Ом? *Да** | 3B |
| Сопротивление менее 10 Ом? **Заменить кабель.** | Ремонт завершён. |  |

#### ШАГ 3B. Проверка кабеля панели машинного отделения (SAE J1939 Return and Shield Wires)

| **Условия:** Отсоединить кабельный разъём С14 от панели машинного отделения Отключить кабельный разъём С7 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте кабель панели машинного отделения. Установите перемычку между панелью шин SAE J1939 CAN для обратного контакта с шиной данных КАН и панелью щита шин данных SAE J1939 CAN для шин данных КАН в разъёме C14. Поместите один испытательный щуп в панель машинного отделения SAE J1939 CAN Data Bus обратного контакта в разъеме C7. Поместите другой испытательный щуп в панель машинного отделения SAE J1939 CAN щитовой штифт шины данных в разъем C7. | Сопротивление менее 10 Ом? *Да** | 3C |
| Сопротивление менее 10 Ом? **Заменить кабель.** | Ремонт завершён. |  |

#### ШАГ 3C. Проверка кабеля интерфейса клиента (SAE J1939)

| **Условия:** Отключить кабельный разъем шины данных SAE J1939 CAN от проводов двигателя Узлы отсоединить кабельный разъем C3 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте кабель клиентского интерфейса. Установите перемычку между контактом передачи данных шины данных SAE J1939 CAN и обратным контактом шины данных SAE J1939 CAN в разъеме кабеля шины данных SAE J1939 CAN. Поместите один измерительный щуп в контактную шину передачи данных SAE J1939 CAN в разъём C3. Поместите другой измерительный щуп в шину данных SAE J1939 CAN обратного контакта в разъеме C3. | Сопротивление менее 10 Ом? *Да** | 3D |
| Сопротивление менее 10 Ом? **Заменить кабель.** | Ремонт завершён. |  |

#### ШАГ 3D. Проверка кабеля интерфейса клиента (SAE J1939 Return and Shield Wires)

| **Условия:** Отключить кабельный разъем шины данных SAE J1939 CAN от проводов двигателя Узлы отсоединить кабельный разъем C3 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте кабель клиентского интерфейса. Установите перемычку между обратным контактом шины данных SAE J1939 CAN и штифтом экрана шины данных SAE J1939 CAN в разъеме кабеля шины данных SAE J1939 CAN. Поместите один измерительный щуп в шину данных SAE J1939 CAN обратного контакта в разъеме C3. Поместите другой измерительный щуп в штифт шины данных SAE J1939 CAN в разъём C3. | Сопротивление менее 10 Ом? *Да** | 4А |
| Сопротивление менее 10 Ом? **Заменить кабель.** | Ремонт завершён. |  |

### ШАГ 4. Проверка проводки интерфейсной коробки заказчика

#### ШАГ 4A. SAE J1939 CAN Data Bus Провода для передачи данных

| **Условия: ** Откройте окно интерфейса клиента Отключите кабель машинного отделения на разъеме C7 от окна интерфейса клиента Отключите кабель интерфейса клиента на разъеме C3 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверить провода питания шины данных SAE J1939 CAN. Поместите один измерительный щуп на штифт передачи данных SAE J1939 CAN (C3) в разъем C7. Поместите другой испытательный щуп на двигатель SAE J1939 CAN, который может поддерживать контакт с шиной передачи данных в разъеме C3. | Сопротивление менее 10 Ом? *Да** | 4B |
| Сопротивление менее 10 Ом? **NORepair:** Заменить провод. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

#### ШАГ 4B. SAE J1939 может возвращать данные

| **Условия: ** Откройте окно интерфейса клиента Отключите кабель машинного отделения на разъеме C7 от окна интерфейса клиента Отключите кабель интерфейса клиента на разъеме C3 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверить данные на шине SAE J1939 можно по проводу обратной связи. Поместите один измерительный щуп на штифт возврата шины данных SAE J1939 CAN (C3) в разъем C7. Поместите другой испытательный щуп на машинное отделение SAE J1939 CAN обратного контакта шины данных на разъеме C3. | Сопротивление менее 10 Ом? *Да** | 4C |
| Сопротивление менее 10 Ом? **NORepair:** Заменить провод. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

#### ШАГ 4C. SAE J1939 может работать с шиной данных Shield Wire

| **Условия: ** Откройте окно интерфейса клиента Отключите кабель машинного отделения на разъеме C7 от окна интерфейса клиента Отключите кабель интерфейса клиента на разъеме C3 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверить провод щита шины данных SAE J1939 CAN. Поместите один измерительный щуп на шину данных SAE J1939 CAN (C3) в разъем C7. Поместите другой измерительный щуп на штифт шины данных SAE J1939 CAN на разъем C3. | Сопротивление менее 10 Ом? ** Ремонт: ** См. раздел TF в Руководстве по устранению неполадок и ремонту, Электронная система управления, Модульные двигатели серии Common Rail System QSK19 CM850, Бюллетень 4021493. | 5а |
| Сопротивление менее 10 Ом? **NORepair:** Заменить провод. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

### ШАГ 5. Проверьте Display Wiring

#### ШАГ 5A. Панель управления машинным отделением SAE J1939 CAN Data Bus Supply Wire (панель приборов X4 для отображения)

| ** Условия: ** Найдите панель машинного отделения Открытая дверь панели машинного отделения. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте проводку панели машинного отделения. Отсоедините кабель C14 от панели машинного отделения. Поместите один испытательный щуп на панель машинного отделения SAE J1939 CAN передачи данных на контактную панель приборной панели. Поместите другой испытательный щуп на панель машинного отделения SAE J1939 CAN на дисплей. | Сопротивление менее 10 Ом? *Да** | 5В |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-024 — Engine Room Panel\|015-024]]. | Ремонт завершён. |  |

#### ШАГ 5B. Панель управления двигателем SAE J1939 CAN Data Bus Return Wire (панель инструментов X4 для отображения)

| ** Условия: ** Найдите панель машинного отделения Открытая дверь панели машинного отделения. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте проводку панели машинного отделения. Отсоедините кабель C14 от панели машинного отделения. Поместите один испытательный щуп на панель машинного отделения SAE J1939 CAN Data Bus обратного контакта на разъем панели прибора. Поместите другой испытательный щуп на панель машинного отделения SAE J1939 CAN Data Bus Return Wire на дисплее. | Сопротивление менее 10 Ом? *** Заменить дисплей. См. процедуру[[115-015-024 — Engine Room Panel\|015-024]]. | Ремонт завершён. |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-024 — Engine Room Panel\|015-024]]. | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - No SAE J1939 Communication with the engine room panel instrument panel.
>
> - Remote panel has SAE J1939 communication.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot SAE J1939 communication symptoms. Start by checking the terminating resistors. There are two terminating resistors. The terminating resistors are located at the following points:
>
> One resistor is located on the engine wiring harness.
>
> If remote panel(s) are used, the second resistor is located at the last remote panel at the X4 terminal strip between the SAE J1939 Supply and SAE J1939 Return terminals.
>
> If a remote panel is **not** used, the second resistor is located in the Customer Interface Box at the X4 terminal between SAE J1939 Supply and SAE J1939 Return terminals.
>
> Step 1 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> The SAE J1939 datalink provides information to the instrument panel in the engine room panel.
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
> |  | **STEP 1B.** Check SAE J1939 Datalink Communication at Engine Room Panel | Communication established? |
> | STEP 2. | Check Panel Wiring |  |
> |  | **STEP 2A.** Check Engine Room Panel SAE J1939 Datalink Supply Wire (Instrument Panel Connector to Service Port Connector) | Less than 10 ohms resistance? |
> |  | **STEP 2B.** Check Engine Room Panel SAE J1939 Datalink Return Wire (Instrument Panel Connector to Service Port Connector) | Less than 10 ohms resistance? |
> |  | **STEP 2C.** Check Engine Room Panel SAE J1939 Datalink Shield Wire (Instrument Panel Connector to Service Port Connector) | Less than 10 ohms resistance? |
> |  | **STEP 2D.** Check SAE J1939 Datalink Supply Wire (C14 Connector to Instrument Panel Connector) | Less than 10 ohms resistance? |
> |  | **STEP 2E.** Check SAE J1939 Datalink Return Wire (C14 Connector to Instrument Panel Connector) | Less than 10 ohms resistance? |
> |  | **STEP 2F.** Check SAE J1939 Datalink Shield Wire (C14 Connector to Instrument Panel Connector) | Less than 10 ohms resistance? |
> | STEP 3. | Check Panel System Cable |  |
> |  | **STEP 3A.** Check Engine Room Panel Cable (SAE J1939 Supply and Return Wires) | Less than 10 ohms resistance? |
> |  | **STEP 3B.** Check Engine Room Panel Cable (SAE J1939 Return and Shield Wires) | Less than 10 ohms resistance? |
> |  | **STEP 3C.** Check Customer Interface Box Cable (SAE J1939 Supply and Return Wires) | Less than 10 ohms resistance? |
> |  | **STEP 3D.** Check Customer Interface Box Cable (SAE J1939 Return and Shield Wires) | Less than 10 ohms resistance? |
> | STEP 4. | Check Customer Interface Box Wiring |  |
> |  | **STEP 4A.** Check SAE J1939 Datalink Supply Wire | Less than 10 ohms resistance? |
> |  | **STEP 4B.** Check SAE J1939 Datalink Return Wire | Less than 10 ohms resistance? |
> |  | **STEP 4C.** Check SAE J1939 Datalink Shield Wire | Less than 10 ohms resistance? |
> | STEP 5. | Check Display Wiring |  |
> |  | **STEP 5A.** Check Engine Room Panel SAE J1939 Datalink Supply Wire (Instrument Panel X4 to Display) | Less than 10 ohms resistance? |
> |  | **STEP 5B.** Check Engine Room Panel SAE J1939 Datalink Return Wire (Instrument Panel X4 to Display) | Less than 10 ohms resistance? |
>
> ### STEP 1. Check SAE J1939 Datalink Signal
>
> #### STEP 1A. Check SAE J1939 Datalink Communication on Engine
>
> | **Conditions:** Engine room panel power switch turned on and power lamp illuminated Locate engine wiring harness Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check SAE J1939 datalink communications. Use INSITE™ electronic service tool to establish communication. | Communication established? **YES** | 1B |
> | Communication established? **NORepair:** Refer to the Troubleshooting and Repair Manual, Electronic Control System, QSK19 CM850, Modular Common Rail System, Series Engines, Bulletin 4021493. | Repair complete. |  |
>
> #### STEP 1B. Check SAE J1939 Datalink Communication at Engine Room Panel
>
> | **Conditions:** Locate engine room panel Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check SAE J1939 datalink communications. Use INSITE™ electronic service tool to establish communication. | Communication established? **YES** | 5A |
> | Communication established? **NO** | 2A. |  |
>
> ### STEP 2. Check Panel Wiring
>
> #### STEP 2A. Check Engine Room Panel SAE J1939 Datalink Supply Wire (Instrument Panel Connector to Service Port Connector)
>
> | **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check engine room panel wiring. Disconnect cable C14 from the engine room panel. Connect one test lead on the engine room panel SAE J1939 datalink supply pin on the instrument panel connector Place the other test lead on the engine room panel SAE J1939 datalink supply pin on the service port connector. | Less than 10 ohms resistance? **YES** | 2B |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | 1B |  |
>
> #### STEP 2B. Check Engine Room Panel SAE J1939 Datalink Return Wire (Instrument Panel Connector to Service Port Connector)
>
> | **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check engine room panel wiring. Disconnect cable C14 from the engine room panel. Connect one test lead on the engine room panel SAE J1939 datalink return pin on the instrument panel connector. Place the other test lead on the engine room panel SAE J1939 datalink return pin on the service port connector. | Less than 10 ohms resistance? **YES** | 2C |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | 1B |  |
>
> #### STEP 2C. Check Engine Room Panel SAE J1939 Datalink Shield Wire (Instrument Panel Connector to Service Port Connector)
>
> | **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check engine room panel wiring. Disconnect cable C14 from the engine room panel. Connect one test lead on the engine room panel SAE J1939 datalink shield pin on the instrument panel connector. Place the other test lead on the engine room panel SAE J1939 datalink shield pin on the service port connector. | Less than 10 ohms resistance? **YES** | 2D |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | 1B |  |
>
> #### STEP 2D. Check SAE J1939 Datalink Supply Wire (C14 Connector to Instrument Panel Connector)
>
> | **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check wires between harness connector and instrument panel connector. Disconnect cable C14 from the engine room panel. Place one test lead on the engine room panel SAE J1939 datalink supply pin on connector C14. Place the other test lead on the engine room panel SAE J1939 datalink supply pin on the instrument panel connector. | Less than 10 ohms resistance? **YES** | 2E |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |
>
> #### STEP 2E. Check SAE J1939 Datalink Return Wire (C14 Connector to Instrument Panel Connector)
>
> | **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check wires between harness connector and instrument panel connector. Disconnect cable C14 from the engine room panel. Place one test lead on the engine room panel SAE J1939 datalink return pin on connector C14. Place the other test lead on the engine room panel SAE J1939 datalink return pin on the instrument panel connector. | Less than 10 ohms resistance? **YES** | 2F |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |
>
> #### STEP 2F. Check SAE J1939 Datalink Shield Wire (C14 Connector to Instrument Panel Connector)
>
> | **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check wires between harness connector and instrument panel connector. Disconnect cable C14 from the engine room panel. Place one test lead on the engine room panel SAE J1939 datalink shield pin on connector C14. Place the other test lead on the engine room panel SAE J1939 datalink shield pin on the instrument panel connector. | Less than 10 ohms resistance? **YES** | 3A |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |
>
> ### STEP 3. Check Panel System Cables
>
> #### STEP 3A. Check Engine Room Panel Cable (SAE J1939 Supply and Return Wires)
>
> | **Conditions:** Disconnect cable connector C14 from the engine room panel Disconnect cable connector C7 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine room panel cable. Install a jumper between engine room panel SAE J1939 datalink supply pin and the engine room panel SAE J1939 datalink return pin in connector C14. Place one test lead in the engine room panel SAE J1939 datalink supply pin in connector C7. Place the other test lead in the engine room panel SAE J1939 datalink return pin in connector C7. | Less than 10 ohms resistance? **YES** | 3B |
> | Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |
>
> #### STEP 3B. Check Engine Room Panel Cable (SAE J1939 Return and Shield Wires)
>
> | **Conditions:** Disconnect cable connector C14 from the engine room panel Disconnect cable connector C7 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine room panel cable. Install a jumper between engine room panel SAE J1939 datalink return pin and the engine room panel SAE J1939 datalink shield pin in connector C14. Place one test lead in the engine room panel SAE J1939 datalink return pin in connector C7. Place the other test lead in the engine room panel SAE J1939 datalink shield pin in connector C7. | Less than 10 ohms resistance? **YES** | 3C |
> | Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |
>
> #### STEP 3C. Check Customer Interface Box Cable (SAE J1939 Supply and Return Wires)
>
> | **Conditions:** Disconnect SAE J1939 datalink cable connector from the engine wiring harness Disconnect cable connector C3 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the customer interface box cable. Install a jumper between SAE J1939 datalink supply pin and the SAE J1939 datalink return pin in SAE J1939 datalink cable connector. Place one test lead in the SAE J1939 datalink supply pin in connector C3. Place the other test lead in the SAE J1939 datalink return pin in connector C3. | Less than 10 ohms resistance? **YES** | 3D |
> | Less than 10 ohms resistance? **NORepair:** Replace the cable? | Repair complete. |  |
>
> #### STEP 3D. Check Customer Interface Box Cable (SAE J1939 Return and Shield Wires)
>
> | **Conditions:** Disconnect SAE J1939 datalink cable connector from the engine wiring harness Disconnect cable connector C3 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the customer interface box cable. Install a jumper between SAE J1939 datalink return pin and the SAE J1939 datalink shield pin in SAE J1939 datalink cable connector. Place one test lead in the SAE J1939 datalink return pin in connector C3. Place the other test lead in the SAE J1939 datalink shield pin in connector C3. | Less than 10 ohms resistance? **YES** | 4A |
> | Less than 10 ohms resistance? **NORepair:** Replace the cable? | Repair complete. |  |
>
> ### STEP 4. Check Customer Interface Box Wiring
>
> #### STEP 4A. Check SAE J1939 Datalink Supply Wire
>
> | **Conditions:** Open the customer interface box Disconnect engine room cable at connector C7 from the customer interface box Disconnect customer interface box cable at connector C3 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the SAE J1939 datalink supply wire. Place one test lead on the SAE J1939 datalink supply (C3) pin in connector C7. Place the other test lead on the engine SAE J1939 datalink supply pin on in the C3 connector. | Less than 10 ohms resistance? **YES** | 4B |
> | Less than 10 ohms resistance? **NORepair:** Replace the wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> #### STEP 4B. Check SAE J1939 Datalink Return Wire
>
> | **Conditions:** Open the customer interface box Disconnect engine room cable at connector C7 from the customer interface box Disconnect customer interface box cable at connector C3 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the SAE J1939 datalink return wire. Place one test lead on the SAE J1939 datalink return (C3) pin in connector C7. Place the other test lead on the engine room SAE J1939 datalink return pin on the C3 connector. | Less than 10 ohms resistance? **YES** | 4C |
> | Less than 10 ohms resistance? **NORepair:** Replace the wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> #### STEP 4C. Check SAE J1939 Datalink Shield Wire
>
> | **Conditions:** Open the customer interface box Disconnect engine room cable at connector C7 from the customer interface box Disconnect customer interface box cable at connector C3 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the SAE J1939 datalink shield wire. Place one test lead on the SAE J1939 datalink shield (C3) pin in connector C7. Place the other test lead on the SAE J1939 datalink shield pin on the C3 connector. | Less than 10 ohms resistance? **YESRepair:** Refer to Section TF in the Troubleshooting and Repair Manual, Electronic Control System, QSK19 CM850 Modular Common Rail System Series Engines, Bulletin 4021493. | 5A |
> | Less than 10 ohms resistance? **NORepair:** Replace the wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> ### STEP 5. Check Display Wiring
>
> #### STEP 5A. Check Engine Room Panel SAE J1939 Datalink Supply Wire (Instrument Panel X4 to Display)
>
> | **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check engine room panel wiring. Disconnect cable C14 from the engine room panel. Place one test lead on the engine room panel SAE J1939 datalink supply pin on the instrument panel connector. Place the other test lead on the engine room panel SAE J1939 datalink supply wire at the display. | Less than 10 ohms resistance? **YES** | 5B |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |
>
> #### STEP 5B. Check Engine Room Panel SAE J1939 Datalink Return Wire (Instrument Panel X4 to Display)
>
> | **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check engine room panel wiring. Disconnect cable C14 from the engine room panel. Place one test lead on the engine room panel SAE J1939 datalink return pin on the instrument panel connector. Place the other test lead on the engine room panel SAE J1939 datalink return wire at the display. | Less than 10 ohms resistance? **YESRepair:** Replace the display. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |
