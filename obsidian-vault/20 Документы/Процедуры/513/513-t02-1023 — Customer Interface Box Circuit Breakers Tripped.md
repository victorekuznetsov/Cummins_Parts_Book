---
type: "Процедура"
doc: "513-t02-1023"
title_en: "Customer Interface Box Circuit Breakers Tripped"
modified: "2019-10-22"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "5411480"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1023.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1023.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
  - "перевод/машинный"
---

# Customer Interface Box Circuit Breakers Tripped

> [!abstract] Процедура · `513-t02-1023`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-10-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1023.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1023.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Выключатели часто спотыкаются на окне интерфейса клиента двигателя (C.I.B.).

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения неполадок при спотыкании на C.I.B. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Проверьте, включен ли переключатель отключения батареи.

Возможные причины:

- схема переключателя зажигания закорочена

- Обратная связь с генератором

- И изолированные, и неизолированные системы находятся в опции. Будьте в курсе обоих.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте коды неисправностей. |  |
|  | **STEP 1A.** Проверка активных кодов неисправностей. | Какие-нибудь коды ошибок активны? |
|  | **STEP 1B.** Проверьте узлы проводов интерфейса двигателя. | 30 амперов на пробоину? |
|  | **STEP 1C** Проверьте жгут проводов интерфейса двигателя. | 10 амперных пробок? |
| ШАГ 2. | Проверьте адаптер экрана проводов жгута. |  |
|  | **STEP 2A.** Проверить контакты соединительного устройства жгута проводов. | Грязные или поврежденные контакты? |
|  | **STEP 2B.** Проверьте короткое контактное соединение в электропроводке. | Менее 10 Ом? |
| ШАГ 3. | Проверьте штурвал проводов. |  |
|  | **STEP 3A.** Проверить контакты соединительного устройства жгута проводов. | Грязные или поврежденные контакты? |
|  | **STEP 3B.** Проверьте короткое контактное соединение в электропроводке. | Больше 100 тысяч ом? |
| ШАГ 4. | Проверьте основной удлинитель проводов жгута и модуля управления двигателем (ECM). |  |
|  | **STEP 4A.** Проверить контакты соединительного устройства жгута проводов. | Грязные или поврежденные контакты? |
|  | **STEP 4B.** Проверьте короткое контактное соединение в электропроводке. | Больше 100 тысяч ом? |
| ШАГ 5. | Проверьте интерфейс двигателя проводов жгута. |  |
|  | **STEP 5A.** Проверить контакты соединительного устройства жгута проводов. | Грязные или поврежденные контакты? |
|  | **STEP 5B.** Проверьте короткое контактное соединение в электропроводке. | Больше 100 тысяч ом? |
| ШАГ 6. | Проверьте проводку интерфейса двигателя. |  |
|  | **STEP 6A.** Проверить контакты соединительного устройства жгута проводов. | Грязные или поврежденные контакты? |
|  | **STEP 6B.** Проверьте короткое контактное соединение в электропроводке. | Больше 100 тысяч ом? |

### ШАГ 1. Проверьте коды неисправностей.

#### ШАГ 1A. Проверьте наличие активных кодов неисправностей.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте наличие активных кодов неисправностей. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Какие-нибудь коды ошибок активны? *Да | Соответствующий код неисправности дерево |
| Какие-нибудь коды ошибок активны? **НЕТ** | 1В |  |

#### ШАГ 1B. Проверьте интерфейс двигателя проводов жгута.

| **Условия:** Система поворота позволяет выключать выключатель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте интерфейс двигателя проводов жгута. Проверьте состояние выключателей на C.I.B. | 30 амперов на пробоину? *Да | 5а |
| 30 амперов на пробоину? **НЕТ** | 1С |  |

#### ШАГ 1C. Проверьте интерфейс двигателя проводов жгута.

| **Условия:** Система поворота позволяет выключать выключатель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте интерфейс двигателя проводов жгута. Проверьте состояние выключателей на C.I.B. | 10 амперных пробок? *Да | 2А |
| 10 амперных пробок? **НЕТ** | Ремонт завершён |  |

### ШАГ 2. Проверьте адаптер экрана проводов жгута.

#### ШАГ 2A. Проверьте контакты разъёма проводов.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините рулевую проводку от адаптера дисплея. Отсоедините дисплей ED-4 от адаптера дисплея проводов ремня. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте контакты разъёма проводов. Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт: **Поврежденное соединение было обнаружено в ремне проводов адаптера дисплея или разъеме ремня проводов адаптера дисплея. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъем или штифты. См. процедуру 015-106 в разделе 15. | Ремонт завершён. |
| Грязные или поврежденные контакты? **НЕТ** | 2В |  |

#### ШАГ 2B. Проверьте контакт-контакт коротко в проводах ремня.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините рулевую проводку от адаптера дисплея. Отсоедините дисплей ED-4 от адаптера дисплея проводов ремня. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте контакт-контакт коротко в проводах ремня. Измерить сопротивление между переключателем зажигания в разъеме проводов адаптера дисплея и всеми другими штифтами в разъеме проводов адаптера дисплея. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Больше 100 тысяч ом? *Да | 3А |
| Больше 100 тысяч ом? **NORepair:** Заменить неисправный провод. См. процедуру 015-106 в разделе 15. | Ремонт завершён |  |

### ШАГ 3. Проверьте штурвал проводов.

#### ШАГ 3A. Проверьте контакты разъёма проводов.

| **Условия:** Система поворота позволяет выключать выключатель. Отключите все проводные упряжки, соединяющиеся с рулевой проводкой. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте контакты разъёма проводов. Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт:** В штурвальном разъеме или штурвальном разъеме штурвальной проводов обнаружено поврежденное соединение. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъем или штифты. См. процедуру 015-078 в разделе 15. | Ремонт завершён |
| Грязные или поврежденные контакты? **НЕТ** | 3B |  |

#### ШАГ 3B. Проверьте контакт-контакт коротко в проводах ремня.

| **Условия:** Система поворота позволяет выключать выключатель. Отключите все проводные упряжки, соединяющиеся с рулевой проводкой. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте контакт-контакт коротко в проводах ремня. Измерить сопротивление между переключателем зажигания в штурвальной проводах жгута разъёма и всеми другими штифтами в штурвальной проводах жгута разъёма. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Больше 100 тысяч ом? *Да | 4А |
| Больше 100 тысяч ом? **NORepair:** Заменить неисправный провод. См. процедуру 015-078 в разделе 15. | Ремонт завершён |  |

### ШАГ 4. Проверьте основной удлинитель проводов жгута и модуля управления двигателем (ECM).

#### ШАГ 4A. Проверьте контакты разъёма проводов.

| **Условия:** Система поворота позволяет выключать выключатель. Отключите все проводные упряжки, подключающиеся к основной удлинительной проводах. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте контакты разъёма проводов. Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт:** Очистить разъем и штифты. По возможности отремонтируйте поврежденную проводку, разъем или штифты. См. процедуру 015-077 в разделе 15. | Ремонт завершён |
| Грязные или поврежденные контакты? **НЕТ** | 4B |  |

#### ШАГ 4B. Проверьте контакт-контакт коротко в проводах ремня.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините рулевую проводку от основной удлинительной проводов. Отсоедините основную проводку расширения от C.I.B. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте контакт-контакт коротко в проводах ремня. Измерить сопротивление между переключателем зажигания в главном разъеме удлинителя проводов и всеми другими штифтами в разъеме удлинителя проводов основной удлинителя. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Больше 100 тысяч ом? Заменить C.I.B. См. процедуру 015-023 в разделе 15. | Ремонт завершён |
| Больше 100 тысяч ом? **NORepair:** Заменить неисправный провод. См. процедуру 015-077 в разделе 15. | Ремонт завершён |  |

### ШАГ 5. Проверьте интерфейс двигателя проводов жгута.

#### ШАГ 5A. Проверьте контакты разъёма проводов.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините проводку интерфейса двигателя от C.I.B. Отключите проводку интерфейса двигателя от панели интерфейса оригинального производителя оборудования (OEM). |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте контакты разъёма проводов. Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? Поврежденное соединение было обнаружено в главном разъеме расширения или главном разъеме проводов расширения. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъем или штифты. См. процедуру 015-093 в разделе 15. | Ремонт завершён |
| Грязные или поврежденные контакты? **НЕТ** | 5В |  |

#### ШАГ 5B. Проверьте контакт-контакт коротко в проводах ремня.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините проводку интерфейса двигателя от C.I.B. Отсоедините проводку интерфейса двигателя от панели интерфейса OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте контакт-контакт коротко в проводах ремня. Измерить сопротивление между контактом 33 переключателя зажигания в разъёме ремня электропроводки двигателя и всеми другими штифтами в разъёме ремня электропроводки интерфейса двигателя. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Больше 100 тысяч ом? *Да | 6А |
| Больше 100 тысяч ом? **NORepair:** Заменить неисправный провод. См. процедуру 015-093 в разделе 15. | Ремонт завершён |  |

### ШАГ 6. Проверьте интерфейс двигателя проводов жгута.

#### ШАГ 6A. Проверьте контакты разъёма проводов.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините проводку интерфейса двигателя от панели интерфейса OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте контакты разъёма проводов. Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? Поврежденное соединение было обнаружено в главном разъеме расширения или главном разъеме проводов расширения. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъем или штифты. См. процедуру 015-093 в разделе 15. | Ремонт завершён |
| Грязные или поврежденные контакты? **НЕТ** | 6B |  |

#### ШАГ 6B. Проверьте контакт-контакт коротко в проводах ремня.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините проводку интерфейса двигателя от панели интерфейса OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте контакт-контакт коротко в проводах ремня. Измерить сопротивление между контактом 33 переключателя зажигания на разъёме интерфейса OEM-системы двигателя и всеми другими штифтами в разъеме интерфейса OEM-системы. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Больше 100 тысяч ом? Заменить C.I.B. См. процедуру 015-023 в разделе 15. | Ремонт завершён |
| Больше 100 тысяч ом? **NORepair:** Заменить неисправный провод. См. процедуру 015-093 в разделе 15. | Ремонт завершён |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - Circuit breakers are frequently tripping on the engine customer interface box (C.I.B.).
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot breaker tripping on the C.I.B. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> Verify battery disconnect switch is turned ON.
>
> Possible causes:
>
> - Keyswitch circuit is shorted
>
> - Backfeed from alternator
>
> - Both isolated and non-isolated systems are on option. Be aware of both.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check fault codes. |  |
> |  | **STEP 1A.** Check for active fault codes. | Any fault codes active? |
> |  | **STEP 1B.** Check the engine interface wiring harness. | 30 ampere breaker trip? |
> |  | **STEP 1C.** Check the engine interface wiring harness. | 10 ampere breaker trip? |
> | STEP 2. | Check the display adapter wiring harness. |  |
> |  | **STEP 2A.** Inspect the wiring harness connector pins. | Dirty or damaged pins? |
> |  | **STEP 2B.** Check for a pin-to-pin short in the wiring harness. | Less than 10 ohms? |
> | STEP 3. | Check the helm harness. |  |
> |  | **STEP 3A.** Inspect the wiring harness connector pins. | Dirty or damaged pins? |
> |  | **STEP 3B.** Check for a pin-to-pin short in the wiring harness. | Greater than 100k ohms? |
> | STEP 4. | Check the main extension harness and engine control module (ECM). |  |
> |  | **STEP 4A.** Inspect the wiring harness connector pins. | Dirty or damaged pins? |
> |  | **STEP 4B.** Check for a pin-to-pin short in the wiring harness. | Greater than 100k ohms? |
> | STEP 5. | Check the engine interface wiring harness. |  |
> |  | **STEP 5A.** Inspect the wiring harness connector pins. | Dirty or damaged pins? |
> |  | **STEP 5B.** Check for a pin-to-pin short in the wiring harness. | Greater than 100k ohms? |
> | STEP 6. | Check the Engine Interface wiring harness. |  |
> |  | **STEP 6A.** Inspect the wiring harness connector pins. | Dirty or damaged pins? |
> |  | **STEP 6B.** Check for a pin-to-pin short in the wiring harness. | Greater than 100k ohms? |
>
> ### STEP 1. Check fault codes.
>
> #### STEP 1A. Check for active fault codes.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for active fault codes. Use INSITE™ electronic service tool to read the fault codes. | Any fault codes active? **YES** | Appropriate fault code troubleshooting tree |
> | Any fault codes active? **NO** | 1B |  |
>
> #### STEP 1B. Check the engine interface wiring harness.
>
> | **Conditions:** Turn system enable switch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine interface wiring harness. Verify the status of the circuit breakers on the C.I.B. | 30 ampere breaker trip? **YES** | 5A |
> | 30 ampere breaker trip? **NO** | 1C |  |
>
> #### STEP 1C. Check the engine interface wiring harness.
>
> | **Conditions:** Turn system enable switch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine interface wiring harness. Verify the status of the circuit breakers on the C.I.B. | 10 ampere breaker trip? **YES** | 2A |
> | 10 ampere breaker trip? **NO** | Repair complete |  |
>
> ### STEP 2. Check the display adapter wiring harness.
>
> #### STEP 2A. Inspect the wiring harness connector pins.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the helm harness from the display adapter wiring harness. Disconnect the ED-4 display from the display adapter wiring harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the wiring harness connector pins. Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the display adapter harness or the display adapter harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Refer to Procedure 015-106 in Section 15. | Repair complete. |
> | Dirty or damaged pins? **NO** | 2B |  |
>
> #### STEP 2B. Check for a pin-to-pin short in the wiring harness.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the helm harness from the display adapter wiring harness. Disconnect the ED-4 display from the display adapter wiring harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a pin-to-pin short in the wiring harness. Measure resistance between the keyswitch in the display adapter wiring harness connector and all other pins in the display adapter wiring harness connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 3A |
> | Greater than 100k ohms? **NORepair:** Replace the faulty wire. Refer to Procedure 015-106 in Section 15. | Repair complete |  |
>
> ### STEP 3. Check the helm harness.
>
> #### STEP 3A. Inspect the wiring harness connector pins.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect all harnesses connecting to the helm wiring harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the wiring harness connector pins. Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the helm connector or the helm harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Refer to Procedure 015-078 in Section 15. | Repair complete |
> | Dirty or damaged pins? **NO** | 3B |  |
>
> #### STEP 3B. Check for a pin-to-pin short in the wiring harness.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect all harnesses connecting to the helm wiring harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a pin-to-pin short in the wiring harness. Measure resistance between the keyswitch in the helm wiring harness connector and all other pins in the helm wiring harness connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 4A |
> | Greater than 100k ohms? **NORepair:** Replace the faulty wire. Refer to Procedure 015-078 in Section 15. | Repair complete |  |
>
> ### STEP 4. Check the main extension harness and engine control module (ECM).
>
> #### STEP 4A. Inspect the wiring harness connector pins.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect all harnesses connecting to the main extension wiring harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the wiring harness connector pins. Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Refer to Procedure 015-077 in Section 15. | Repair complete |
> | Dirty or damaged pins? **NO** | 4B |  |
>
> #### STEP 4B. Check for a pin-to-pin short in the wiring harness.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect helm harnesses from the main extension wiring harness. Disconnect the main extension harness from the C.I.B. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a pin-to-pin short in the wiring harness. Measure resistance between the keyswitch in the main extension wiring harness connector and all other pins in the main extension wiring harness connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YESRepair:** Replace the C.I.B. Refer to Procedure 015-023 in Section 15. | Repair complete |
> | Greater than 100k ohms? **NORepair:** Replace the faulty wire. Refer to Procedure 015-077 in Section 15. | Repair complete |  |
>
> ### STEP 5. Check the engine interface wiring harness.
>
> #### STEP 5A. Inspect the wiring harness connector pins.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect engine interface wiring harness from the C.I.B. Disconnect engine interface wiring harness from the original equipment manufacturer (OEM) interface panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the wiring harness connector pins. Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the main extension connector or the main extension harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Refer to Procedure 015-093 in Section 15. | Repair complete |
> | Dirty or damaged pins? **NO** | 5B |  |
>
> #### STEP 5B. Check for a pin-to-pin short in the wiring harness.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect engine interface wiring harness from the C.I.B. Disconnect engine interface wiring harness from the OEM interface panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a pin-to-pin short in the wiring harness. Measure resistance between the keyswitch pin 33 in the engine interface wiring harness connector and all other pins in the engine interface wiring harness connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 6A |
> | Greater than 100k ohms? **NORepair:** Replace the faulty wire. Refer to Procedure 015-093 in Section 15. | Repair complete |  |
>
> ### STEP 6. Check the engine interface wiring harness.
>
> #### STEP 6A. Inspect the wiring harness connector pins.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect engine interface wiring harness from the OEM interface panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the wiring harness connector pins. Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the main extension connector or the main extension harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Refer to Procedure 015-093 in Section 15. | Repair complete |
> | Dirty or damaged pins? **NO** | 6B |  |
>
> #### STEP 6B. Check for a pin-to-pin short in the wiring harness.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect engine interface wiring harness from the OEM interface panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a pin-to-pin short in the wiring harness. Measure resistance between the keyswitch pin 33 on the engine wiring harness OEM interface connector and all other pins in the OEM interface connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YESRepair:** Replace the C.I.B.. Refer to Procedure 015-023 in Section 15. | Repair complete |
> | Greater than 100k ohms? **NORepair:** Replace the faulty wire. Refer to Procedure 015-093 in Section 15. | Repair complete |  |
