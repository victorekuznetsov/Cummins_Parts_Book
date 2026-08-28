---
aliases:
  - "Самопроизвольный останов двигателя"
type: "Процедура"
doc: "513-t02-1008"
title_en: "Un-requested Engine Stop"
title_ru: "Самопроизвольный останов двигателя"
modified: "2019-10-17"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1008.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1008.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
  - "перевод/машинный"
---

# Un-requested Engine Stop
**Самопроизвольный останов двигателя**

> [!abstract] Процедура · `513-t02-1008`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-10-17
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1008.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1008.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Двигатель выключается без выключения оператором системы, включающей переключатель у руля или клиентского интерфейса (C.I.B).

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения симптомов отключения двигателя. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

PS102 Systems оснащалась коммутаторами Start Switch и Stop Switch.

PS103 Systems поставляется с одной кнопкой START/STOP, которая является мгновенным переключателем или кнопкой.

Системы запуска PS103 являются модулями управления двигателем, а не C.I.B. контролируемый.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте Си Би. |  |
|  | **ШАГ 1А** Проверьте выключатель на C.I.B. | Откроется или лопнет выключатель? |
|  | **STEP 1B** Проверить сигнал переключателя зажигания в ЦБ. | Равно напряжению батареи? |
|  | **STEP 1C** Проверьте переключатель/кнопку START/STOP (помощь). | Сопротивление более 100k Ом, когда переключатель находится в положении выключения? |
| ШАГ 2. | Проверьте основную проводку расширения. |  |
|  | **STEP 2A.** Осмотрите основные проводов расширения. | Грязные или поврежденные контакты? |
|  | **STEP 2B.** Проверьте основную проводку расширения для короткого контакта в переключателе зажигания. | Сопротивление больше 100k Ом? |
| ШАГ 3. | Проверьте штурвал. |  |
|  | **ШАГ 3А.** Проверить штурвал проводов. | Грязные или поврежденные контакты? |
|  | **STEP 3B.** Проверьте упряжку проводов рулевого управления для короткого контакта в переключателе зажигания. | Сопротивление больше 100k Ом? |
|  | **STEP 3C.** Проверьте стоп-сигнал (помощь). | Сопротивление более 100 К Ом при выключателе в положении OFF? |
| ШАГ 4. | Проверьте оригинальную проводку производителя оборудования (OEM). |  |
|  | **STEP 4A.** Проверить проводку OEM-интерфейса. | Грязные или поврежденные контакты? |
|  | **STEP 4B.** Проверьте проводку OEM-интерфейса для открытой цепи в цепи пожаротушения. | Менее 10 Ом? |
| ШАГ 5. | Проверьте интерфейс двигателя проводов жгута. |  |
|  | **STEP 5A.** Проверить жгут проводов интерфейса двигателя. | Грязные или поврежденные контакты? |
|  | **STEP 5B.** Проверьте упряжку проводов интерфейса двигателя для короткого контакта в переключателе зажигания. | Сопротивление больше 100k Ом? |
| ШАГ 6. | Проверьте жгут электропроводки двигателя. |  |
|  | **STEP 6A.** Проверить жгут электропроводки двигателя. | Грязные или поврежденные контакты? |
|  | **STEP 6B.** Проверьте упряжку электропроводки двигателя на короткое время контакта с контактом в стартовом сигнале. | Сопротивление больше 100k Ом? |

### ШАГ 1. Проверьте Си Би.

#### ШАГ 1A. Проверьте выключатель на СиБи.

| **Условия:** Система поворота позволяет выключать выключатель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте выключатель на СиБи. Проверьте выключатель на Си Би. | Откроется или лопнет выключатель? **YESRepair:** Сброс выключателя на C.I.B. См. процедуру 015-023 в разделе 15. | 1В |
| Откроется или лопнет выключатель? **НЕТ** | Ремонт завершён |  |

#### ШАГ 1B. Проверьте сигнал переключения зажигания в отделе интенсивной терапии.

| **Условия: **Откройте окно интерфейса клиента. Отсоедините проводку интерфейса двигателя от C.I.B. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнал переключения зажигания в отделе интенсивной терапии. Поместите один свинец на замок зажигания SIGNAL контакт 9 из C.I.B. разъем (присоединение к интерфейсу двигателя проводной ремни). Поместите другую свинцовую на контакт 4 C.I.B. разъем (присоединение к интерфейсу двигателя проводной ремни). См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов использования мультиметра.[[99-019-359 — Multimeter Usage\|См. процедуру 019-359 в разделе 19.]] | Равно напряжению батареи? *Да | 4А |
| Равно напряжению батареи? **НЕТ** | 1С |  |

#### ШАГ 1C. Проверьте переключатель / кнопку START / STOP (помощь).

| **Условия: **Отключите стартовый/стоп-переключатель/кнопку у руля. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление. Измерьте сопротивление переключателя / кнопки START. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Сопротивление более 100k Ом, когда переключатель находится в положении выключения? *Да | 2А |
| Сопротивление более 100k Ом, когда переключатель находится в положении выключения? **NORepair:** Заменить выключатель START. Для систем PS102:[[513-015-101 — Start Switch\|См. процедуру 015-101 в разделе 15.]]Для систем PS103:[[513-015-109 — Start Stop Switch\|См. процедуру 015-109 в разделе 15.]] | Ремонт завершён. |  |

### ШАГ 2. Проверьте основную проводку расширения.

#### ШАГ 2A. Проверьте основную проводку расширения.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините основную проводку расширения от C.I.B. Отсоедините основную удлинительную проводку от рулевой проводов. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте основную проводку расширения. Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт: **В разъёме жгута проводов обнаружено поврежденное соединение. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъем или штифты. Для основной удлинительной проводов жгута: См. процедуру 015-077 в разделе 15. Для C.I.B.: См. процедуру 015-023 в разделе 15. | Ремонт завершён. |
| Грязные или поврежденные контакты? **НЕТ** | 2В |  |

#### ШАГ 2B. Проверьте основную проводку расширения для короткого контакта в переключателе зажигания.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините все спаривающиеся жгуты к основной удлинительной жгутке. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте основную проводку расширения для короткого контакта в переключателе зажигания. Измерьте сопротивление между контактом сигнала переключателя зажигания в разъеме главного удлинителя проводов и всеми другими штифтами в разъеме главного удлинителя проводов. Измерьте сопротивление между контактом стоп-сигнала в разъеме главного удлинителя проводов и всеми другими штифтами в разъеме главного удлинителя проводов. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Сопротивление больше 100k Ом? *Да | 3А |
| Сопротивление больше 100k Ом? **NORepair: **В сигнале остановки обнаружено короткое замыкание. Ремонт или замена основного удлинителя проводов ремня. См. процедуру 015-077 в разделе 15. | Ремонт завершён |  |

### ШАГ 3. Проверьте штурвал.

#### ШАГ 3A. Проверьте штурвал проводов.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините рулевую проводку от основной удлинительной проводов. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте штурвал проводов. Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт: **В разъёме жгута проводов обнаружено поврежденное соединение. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъем или штифты. Для штурвала проводов ремня: См. процедуру 015-078 в разделе 15. Для основной удлинительной проводов жгута: См. процедуру 015-077 в разделе 15. | Ремонт завершён. |
| Грязные или поврежденные контакты? **НЕТ** | 3B |  |

#### ШАГ 3B. Проверьте рулевую проводку ремня для короткого контакта в переключателе зажигания.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините все спаривающиеся жгуты к рулевой жгут. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте рулевую проводку ремня для короткого контакта в переключателе зажигания. Измерить сопротивление между контактом сигнала переключателя зажигания в разъёме штурвала и всеми другими штифтами в разъёме штурвала проводов. Измерьте сопротивление между контактом стоп-сигнала в разъёме штурвала и всеми другими штифтами в разъёме штурвала. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Сопротивление больше 100k Ом? *Да | 3C |
| Сопротивление больше 100k Ом? **NORepair: **В сигнале остановки обнаружено короткое замыкание. Ремонт или замена рулевой проводов. См. процедуру 015-078 в разделе 15. | Ремонт завершён |  |

#### ШАГ 3C. Проверьте стоп-сигнал (помощь).

| **Условия: **Отключите стоп-сигнал. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте стоп-сигнал (помощь). Измерьте сопротивление между контактом 2 и контактом 3 на выключателе стоп. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Сопротивление более 100k Ом, когда переключатель находится в положении выключения? Заменить C.I.B. См. процедуру 015-023 в разделе 15. | Ремонт завершён |
| Сопротивление более 100k Ом, когда переключатель находится в положении выключения? **NORepair:** Заменить стартовый выключатель.[[513-015-101 — Start Switch\|См. процедуру 015-101 в разделе 15.]] | Ремонт завершён |  |

### ШАГ 4. Проверьте OEM интерфейс проводов жгута.

#### ШАГ 4A. Проверьте OEM интерфейс проводов жгута.

| **Условия:** Система поворота позволяет выключать выключатель. Отключите OEM-интерфейс проводов от C.I.B. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте OEM интерфейс проводов жгута. Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Сопротивление более 100k Ом, когда переключатель находится в положении выключения? **Ремонт: **В разъёме жгута проводов обнаружено поврежденное соединение. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъем или штифты. Для OEM интерфейса проводов жгута: См. процедуру 015-104 в разделе 15. | Ремонт завершён. |
| Сопротивление более 100k Ом, когда переключатель находится в положении выключения? **НЕТ** | 4B |  |

#### ШАГ 4B. Проверьте OEM-интерфейс проводов жгута для открытой цепи в цепи пожаротушения.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините проводку OEM Interface от C.I.B. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте OEM-интерфейс проводов жгута для открытой цепи в цепи пожаротушения. Измерьте сопротивление по всей цепи пожаротушения контактов 6 и 7 на разъёме OEM-интерфейса проводов жгута (присоединение к C.I.B.). См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Менее 10 Ом? *Да | 5а |
| Менее 10 Ом? **NORepair:** В цепи пожаротушения обнаружена открытая стрела. Ремонт OEM интерфейса проводов и межсоединений. См. процедуру 015-104 в разделе 15. | Ремонт завершён |  |

### ШАГ 5. Проверьте интерфейс двигателя проводов жгута.

#### ШАГ 5A. Проверьте жгут проводов интерфейса двигателя.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините проводку интерфейса двигателя от панели интерфейса OEM. Отсоедините проводку интерфейса двигателя от C.I.B. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте жгут проводов интерфейса двигателя. Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт: **В разъёме жгута проводов обнаружено поврежденное соединение. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъем или штифты. Для интерфейса двигателя жгут проводов: См. процедуру 015-093 в разделе 15. | Ремонт завершён. |
| Грязные или поврежденные контакты? **НЕТ** | 5В |  |

#### ШАГ 5B. Проверьте ремень проводов интерфейса двигателя для короткого контакта в переключателе зажигания.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините проводку интерфейса двигателя от панели интерфейса OEM. Отсоедините проводку интерфейса двигателя от C.I.B. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте ремень проводов интерфейса двигателя для короткого контакта в переключателе зажигания. Измерьте сопротивление между сигналом переключателя зажигания в разъёме ремня электропроводки двигателя и всеми другими штифтами в разъёме ремня электропроводки интерфейса двигателя. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Сопротивление больше 100k Ом? **Ремонт:** Соедините все компоненты и убедитесь, что судно работает. | 6А |
| Сопротивление больше 100k Ом? **NORepair: **В стартовом сигнале обнаружено короткое замыкание. Ремонт или замена интерфейса двигателя проводкой ремня. См. процедуру 015-093 в разделе 15. | Ремонт завершён |  |

### ШАГ 6. Проверьте жгут электропроводки двигателя.

#### ШАГ 6A. Проверьте жгут электропроводки двигателя.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините проводку двигателя от модуля управления двигателем (ECM). Отсоедините проводку интерфейса двигателя от панели интерфейса OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте жгут электропроводки двигателя. Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт: **В разъёме жгута проводов обнаружено поврежденное соединение. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъем или штифты. Для электропроводки двигателя жгут: Справочная процедура 019-043 в разделе 19 соответствующего руководства по эксплуатации двигателя. | Ремонт завершён. |
| Грязные или поврежденные контакты? **НЕТ** | 6B |  |

#### ШАГ 6B. Проверьте упряжку проводов двигателя для короткого контакта в стартовом сигнале.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините электропроводку двигателя от ECM. Отсоедините проводку двигателя от панели интерфейса OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте упряжку проводов двигателя для короткого контакта в стартовом сигнале. Измерьте сопротивление между контактом сигнала переключателя зажигания в разъеме жгутов проводов двигателя и всеми другими штифтами в разъеме жгутов проводов двигателя (присоединение к панели интерфейса OEM). См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Сопротивление больше 100k Ом? **Ремонт: **Ссылка на двигатель запускается, но не будет продолжать устранение неполадок дерево симптомов в разделе ТТ соответствующего руководства по обслуживанию двигателя. | Ремонт завершён |
| Сопротивление больше 100k Ом? **NORepair:** В сигнале переключателя зажигания обнаружено короткое замыкание. Ремонт или замена ремня электропроводки двигателя. Справочная процедура 019-043 в разделе 19 соответствующего руководства по эксплуатации двигателя. | Ремонт завершён |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - The engine shuts OFF without the operator switching OFF the system enable switch at the helm or customer interface box (C.I.B).
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot engine shutoff symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> PS102 Systems came equipped with Start Switch and Stop Switches.
>
> PS103 Systems came with a single START/STOP button that is a momentary switch or button.
>
> PS103 Starting systems are engine control module controlled rather than C.I.B. controlled.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check C.I.B. |  |
> |  | **STEP 1A.** Check the circuit breaker on the C.I.B. | Circuit breaker open or popped? |
> |  | **STEP 1B.** Check keyswitch signal at the C.I.B. | Equal to battery voltage? |
> |  | **STEP 1C.** Check the START/STOP switch/button (helm). | Greater than 100k ohms resistance when switch is in OFF position? |
> | STEP 2. | Check main extension wiring harness. |  |
> |  | **STEP 2A.** Inspect the main extension harness. | Dirty or damaged pins? |
> |  | **STEP 2B.** Check the main extension wiring harness for a pin-to-pin short in the keyswitch. | Greater than 100k ohms resistance? |
> | STEP 3. | Check the helm. |  |
> |  | **STEP 3A.** Inspect the helm harness. | Dirty or damaged pins? |
> |  | **STEP 3B.** Check the helm wiring harness for a pin-to-pin short in the keyswitch. | Greater than 100k ohms resistance? |
> |  | **STEP 3C.** Check the stop switch (helm). | Greater than 100K ohms resistance when switch is in OFF position? |
> | STEP 4. | Check the original equipment manufacturer (OEM) interface harness. |  |
> |  | **STEP 4A.** Inspect the OEM interface harness. | Dirty or damaged pins? |
> |  | **STEP 4B.** Check the OEM interface wiring harness for an open circuit in the fire suppression circuit. | Less than 10 ohms? |
> | STEP 5. | Check the engine interface harness. |  |
> |  | **STEP 5A.** Inspect the engine interface harness. | Dirty or damaged pins? |
> |  | **STEP 5B.** Check the engine interface wiring harness for a pin-to-pin short in the keyswitch. | Greater than 100k ohms resistance? |
> | STEP 6. | Check the engine wiring harness. |  |
> |  | **STEP 6A.** Inspect the engine wiring harness. | Dirty or damaged pins? |
> |  | **STEP 6B.** Check the engine wiring harness for a pin-to-pin short in the start signal. | Greater than 100k ohms resistance? |
>
> ### STEP 1. Check C.I.B.
>
> #### STEP 1A. Check the circuit breaker on the C.I.B.
>
> | **Conditions:** Turn system enable switch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the circuit breaker on the C.I.B. Check circuit breaker on C.I.B. | Circuit breaker open or popped? **YESRepair:** Reset circuit breaker on the C.I.B. Refer to Procedure 015-023 in Section 15. | 1B |
> | Circuit breaker open or popped? **NO** | Repair complete |  |
>
> #### STEP 1B. Check keyswitch signal at the C.I.B.
>
> | **Conditions:** Open up the customer interface box. Disconnect the engine interface wiring harness from the C.I.B. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check keyswitch signal at the C.I.B. Place one lead on the keyswitch SIGNAL pin 9 of the C.I.B. connector (mating to the engine interface harness). Place the other lead on RETURN pin 4 of the C.I.B. connector (mating to the engine interface harness). Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general multimeter usage techniques. [[99-019-359 — Multimeter Usage\|Refer to Procedure 019-359 in Section 19.]] | Equal to battery voltage? **YES** | 4A |
> | Equal to battery voltage? **NO** | 1C |  |
>
> #### STEP 1C. Check the START/STOP switch/button (helm).
>
> | **Conditions:** Disconnect the start/stop switch/button at the helm. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance. Measure the resistance of the START switch / button. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms resistance when switch is in OFF position? **YES** | 2A |
> | Greater than 100k ohms resistance when switch is in OFF position? **NORepair:** Replace the START switch. For PS102 systems: [[513-015-101 — Start Switch\|Refer to Procedure 015-101 in Section 15.]] For PS103 systems: [[513-015-109 — Start Stop Switch\|Refer to Procedure 015-109 in Section 15.]] | Repair complete. |  |
>
> ### STEP 2. Check main extension wiring harness.
>
> #### STEP 2A. Inspect the main extension harness.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the main extension harness from the C.I.B. Disconnect the main extension harness from the helm harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the main extension harness. Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. For the main extension harness: Refer to Procedure 015-077 in Section 15. For the C.I.B.: Refer to Procedure 015-023 in Section 15. | Repair complete. |
> | Dirty or damaged pins? **NO** | 2B |  |
>
> #### STEP 2B. Check the main extension wiring harness for a pin-to-pin short in the keyswitch.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect all mating harnesses to the main extension harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the main extension wiring harness for a pin-to-pin short in the keyswitch. Measure the resistance between the keyswitch SIGNAL pin in the main extension harness connector and all other pins in the main extension harness connector. Measure the resistance between the stop SIGNAL pin in the main extension harness connector and all other pins in the main extension harness connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms resistance? **YES** | 3A |
> | Greater than 100k ohms resistance? **NORepair:** A short circuit has been detected in the stop signal. Repair or replace the main extension wiring harness. Refer to Procedure 015-077 in Section 15. | Repair complete |  |
>
> ### STEP 3. Check the helm.
>
> #### STEP 3A. Inspect the helm harness.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the helm harness from the main extension harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the helm harness. Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. For the helm harness: Refer to Procedure 015-078 in Section 15. For the main extension harness: Refer to Procedure 015-077 in Section 15. | Repair complete. |
> | Dirty or damaged pins? **NO** | 3B |  |
>
> #### STEP 3B. Check the helm wiring harness for a pin-to-pin short in the keyswitch.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect all mating harnesses to the helm harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the helm wiring harness for a pin-to-pin short in the keyswitch. Measure the resistance between the keyswitch SIGNAL pin in the helm harness connector and all other pins in the helm harness connector. Measure the resistance between the stop SIGNAL pin in the helm harness connector and all other pins in the helm harness connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms resistance? **YES** | 3C |
> | Greater than 100k ohms resistance? **NORepair:** A short circuit has been detected in the stop signal. Repair or replace the helm wiring harness. Refer to Procedure 015-078 in Section 15. | Repair complete |  |
>
> #### STEP 3C. Check the stop switch (helm).
>
> | **Conditions:** Disconnect the stop switch. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the stop switch (helm). Measure the resistance between pin 2 and pin 3 at the stop switch. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms resistance when switch is in OFF position? **YESRepair:** Replace the C.I.B. Refer to Procedure 015-023 in Section 15. | Repair complete |
> | Greater than 100k ohms resistance when switch is in OFF position? **NORepair:** Replace the start switch. [[513-015-101 — Start Switch\|Refer to Procedure 015-101 in Section 15.]] | Repair complete |  |
>
> ### STEP 4. Check the OEM interface harness.
>
> #### STEP 4A. Inspect the OEM interface wiring harness.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect OEM interface wiring harness from the C.I.B. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the OEM interface wiring harness. Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Greater than 100k ohms resistance when switch is in OFF position? **YESRepair:** A damaged connection has been detected in the harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. For the OEM interface wiring harness: Refer to Procedure 015-104 in Section 15. | Repair complete. |
> | Greater than 100k ohms resistance when switch is in OFF position? **NO** | 4B |  |
>
> #### STEP 4B. Check the OEM interface wiring harness for an open circuit in the fire suppression circuit.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect OEM Interface wiring harness from the C.I.B. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the OEM interface wiring harness for an open circuit in the fire suppression circuit. Measure the resistance across the fire suppression circuit pins 6 and 7 on the OEM interface wiring harness connector (mating to the C.I.B.). Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms? **YES** | 5A |
> | Less than 10 ohms? **NORepair:** An open in the fire suppression circuit has been detected. Repair the OEM interface wiring harness and interconnects. Refer to Procedure 015-104 in Section 15. | Repair complete |  |
>
> ### STEP 5. Check engine interface harness.
>
> #### STEP 5A. Inspect the engine interface harness.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the engine interface harness from the OEM interface panel. Disconnect the engine interface harness from the C.I.B. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine interface harness. Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. For the engine interface harness: Refer to Procedure 015-093 in Section 15. | Repair complete. |
> | Dirty or damaged pins? **NO** | 5B |  |
>
> #### STEP 5B. Check the engine interface wiring harness for a pin-to-pin short in the keyswitch.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the engine interface harness from the OEM interface panel. Disconnect the engine interface harness from the C.I.B. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine interface wiring harness for a pin-to-pin short in the keyswitch. Measure the resistance between the keyswitch signal in the engine interface harness connector and all other pins in the engine interface harness connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms resistance? **YESRepair:** Connect all components and verify that the vessel is operational. | 6A |
> | Greater than 100k ohms resistance? **NORepair:** A short circuit has been detected in the start signal. Repair or replace the engine interface harness. Refer to Procedure 015-093 in Section 15. | Repair complete |  |
>
> ### STEP 6. Check engine wiring harness.
>
> #### STEP 6A. Inspect the engine wiring harness.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the engine harness from the engine control module (ECM). Disconnect the engine interface wiring harness from the OEM interface panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine wiring harness. Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. For the engine wiring harness: Reference Procedure 019-043 in Section 19 of the appropriate engine service manual. | Repair complete. |
> | Dirty or damaged pins? **NO** | 6B |  |
>
> #### STEP 6B. Check the engine wiring harness for a pin-to-pin short in the start signal.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect engine wiring harness from the ECM. Disconnect engine wiring harness from the OEM interface panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine wiring harness for a pin-to-pin short in the start signal. Measure the resistance between the keyswitch SIGNAL pin in the engine wiring harness connector and all other pins in the engine wiring harness connector (mating to the OEM interface panel). Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms resistance? **YESRepair:** Reference the Engine Starts But Will Not Keep Running Troubleshooting Symptom tree in Section TT of the appropriate engine service manual. | Repair complete |
> | Greater than 100k ohms resistance? **NORepair:** A short circuit has been detected in the keyswitch signal. Repair or replace the engine wiring harness. Reference Procedure 019-043 in Section 19 of the appropriate engine service manual. | Repair complete |  |
