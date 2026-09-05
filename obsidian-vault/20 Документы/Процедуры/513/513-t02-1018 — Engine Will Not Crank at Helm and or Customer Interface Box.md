---
type: "Процедура"
doc: "513-t02-1018"
title_en: "Engine Will Not Crank at Helm and/or Customer Interface Box"
modified: "2019-09-27"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1018.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1018.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
  - "перевод/машинный"
---

# Engine Will Not Crank at Helm and/or Customer Interface Box

> [!abstract] Процедура · `513-t02-1018`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-09-27
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1018.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1018.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Двигатель **не** будет работать при нажатии кнопки запуска.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения симптомов запуска двигателя. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Для запуска коленчатого механизма должны быть соблюдены следующие параметры панели:

- Система включения переключателя поворачивается в положение ON

- Двигатель остановлен

- Главная дроссельная заслонка и резервная дроссельная заслонка в нейтральном положении

- Тролль находится в нейтральном положении

- Отключение батареи включено.

Возможные причины:

- Старт короткий или открытый

- Запуск выключателя

- Нейтральная схема безопасности открыта

- Стартер локаут на двигателе задействован.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте выключатель и выключатели. |  |
|  | **STEP 1A.** Проверьте выключатель на окне интерфейса клиента (CIB). | Открывал или лопнул? |
|  | **ШАГ 1В.** Проверьте стартовое напряжение. | Равно напряжению батареи? |
| ШАГ 2. | Проверьте жгут электропроводки двигателя. |  |
|  | **STEP 2A.** Проверить жгут электропроводки двигателя. | Грязные или поврежденные контакты? |
|  | **STEP 2B.** Проверьте упряжку электропроводки двигателя на короткое время контакта с контактом в стартовом сигнале. | Сопротивление больше 100k Ом? |
|  | **STEP 2C.** Проверьте электропроводку двигателя на наличие открытого места в старте. | Сопротивление менее 10 Ом? |
| ШАГ 3. | Проверьте интерфейс двигателя проводов жгута. |  |
|  | **STEP 3A.** Проверить жгут проводов интерфейса двигателя. | Грязные или поврежденные контакты? |
|  | **STEP 3B.** Проверьте упряжку проводов интерфейса двигателя для короткого контакта в начале. | Сопротивление больше 100k Ом? |
|  | **STEP 3C.** Проверьте интерфейс двигателя на предмет наличия открытого в начале. | Сопротивление менее 10 Ом? |
| ШАГ 4. | Проверьте оригинальную проводку производителя оборудования (OEM). |  |
|  | **STEP 4A.** Проверить проводку OEM-интерфейса. | Грязные или поврежденные контакты? |
|  | **STEP 4B.** Проверьте проводку OEM-интерфейса для открытой цепи в нейтральной цепи безопасности. | Менее 10 Ом? |
| ШАГ 5. | Проверьте жгут проводов приложения привода. |  |
|  | **STEP 5A.** Проверить электропроводку привода. | Грязные или поврежденные контакты? |
|  | **STEP 5B.** Проверьте электропроводку прикладного привода для открытой цепи в нейтральной цепи безопасности. | Менее 10 Ом? |
| ШАГ 6. | Проверьте CIB. |  |
|  | **STEP 6A.** Проверьте стартовый локаут в CIB. | Светодиод для начального локаута подсвечивается? |
|  | **STEP 6B.** Проверьте выключатель «Пуск/Стоп» (CIB). | Сопротивление менее 10 Ом при включении переключателя? |
|  | **STEP 6C.** Проверьте стартовое напряжение от CIB. | Приблизительное напряжение батареи? |
| ШАГ 7. | Проверьте основную проводку расширения. |  |
|  | **STEP 7A.** Осмотрите основные проводов расширения. | Грязные или поврежденные контакты? |
|  | **STEP 7B.** Проверьте основную проводку расширения для короткого контакта в начале. | Сопротивление больше 100k Ом? |
|  | **STEP 7C.** Проверьте основные удлинители проводов на наличие открытого в начале. | Сопротивление менее 10 Ом? |
| ШАГ 8. | Проверьте штурвал. |  |
|  | **STEP 8A.** Проверьте стартовый выключатель (помощь). | Сопротивление менее 10 Ом при включении переключателя? |
|  | **ШАГ 8В.** Проверить штурвал проводов. | Грязные или поврежденные контакты? |
|  | **STEP 8C.** Проверьте упряжку для проводов рулевого управления для короткого контакта в начале. | Сопротивление больше 100k Ом? |
|  | **STEP 8D.** Проверьте упряжку для проводов руля на наличие открытого места в начале. | Сопротивление менее 10 Ом? |

### ШАГ 1. Проверьте выключатель и выключатели.

#### ШАГ 1A. Проверьте выключатель на CIB.

| **Условия:** Система поворота позволяет выключать выключатель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте выключатель на CIB. Проверьте выключатель на CIB. | Открывал или лопнул? **Ремонт: **Перезагрузка выключателя на CIB. См. процедуру 015-023 в разделе 15. | Ремонт завершён. |
| Открывал или лопнул? **НЕТ** | 1В |  |

#### ШАГ 1B. Проверьте стартовое напряжение.

| **Условия:** Система включения включает включение. Нажмите и удерживайте стартовый/стоп-переключатель в стартовом положении (CIB). |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте стартовое напряжение. Поместите один испытательный щуп на магнитный стартовый терминал, а другой приведет к земле в стартере. | Равно напряжению батареи? **Ремонт:** Выявлена начальная проблема. Для стартового магнитного переключателя: Справочная процедура 013-017 в разделе 13 соответствующего руководства по эксплуатации двигателя. Для начала соленоид: Справочная процедура 013-019 в разделе 13 соответствующего руководства по эксплуатации двигателя. | Ремонт завершён. |
| Равно напряжению батареи? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте жгут электропроводки двигателя.

#### ШАГ 2A. Проверьте жгут электропроводки двигателя.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините проводку интерфейса двигателя от панели интерфейса OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте жгут электропроводки двигателя. Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема или разъема разъема разъема или разъема разъема разъема или на контакте разъема повреждения изоляции Проволоки Разъемная оболочка разбитого Поврежденного разъема блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт: **В разъёме жгута проводов обнаружено поврежденное соединение. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъем или штифты. Для электропроводки двигателя жгут: Справочная процедура 019-043 в разделе 19 соответствующего руководства по эксплуатации двигателя. | Ремонт завершён. |
| Грязные или поврежденные контакты? **НЕТ** | 2В |  |

#### ШАГ 2B. Проверьте упряжку проводов двигателя для короткого контакта в стартовом сигнале.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините проводку интерфейса двигателя от панели интерфейса OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте упряжку проводов двигателя для короткого контакта в стартовом сигнале. Измерьте сопротивление между стартовым контактом SIGNAL 24 в разъеме панели интерфейса OEM и всеми другими штифтами в разъеме ремня электропроводки двигателя. | Сопротивление больше 100k Ом? **Ремонт:** Перенаправить проводку жгута. | 2C |
| Сопротивление больше 100k Ом? **NORepair: **В стартовом сигнале было обнаружено короткое замыкание от контакта к контакту. Ремонт или замена ремня электропроводки двигателя. Справочная процедура 019-043 в разделе 19 соответствующего руководства по эксплуатации двигателя. | Ремонт завершён. |  |

#### ШАГ 2C. Проверьте упряжку для проводов двигателя на наличие открытого места в начале.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините электропроводку двигателя от модуля управления двигателем (ECM). Отсоедините проводку двигателя от панели интерфейса OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте упряжку для проводов двигателя на наличие открытого места в начале. Измерьте сопротивление между стартовым контактом 24 SIGNAL на разъеме панели интерфейса OEM и стартовым сигналом на стартовом магнитном переключателе. | Сопротивление менее 10 Ом? *Да | 3А |
| Сопротивление менее 10 Ом? **NORepair: **В начале была обнаружена открытая цепь. Ремонт или замена ремня электропроводки двигателя. Справочная процедура 019-043 в разделе 19 соответствующего руководства по эксплуатации двигателя. | Ремонт завершён. |  |

### ШАГ 3. Проверьте интерфейс двигателя проводов жгута.

#### ШАГ 3A. Проверьте жгут проводов интерфейса двигателя.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините проводку интерфейса двигателя от панели интерфейса OEM. Отсоедините проводку интерфейса двигателя от CIB. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте жгут проводов интерфейса двигателя. Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт: **В разъёме жгута проводов обнаружено поврежденное соединение. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъем или штифты. Для интерфейса двигателя жгут проводов: См. процедуру 015-093 в разделе 15. | Ремонт завершён. |
| Грязные или поврежденные контакты? **НЕТ** | 3B |  |

#### ШАГ 3B. Проверьте интерфейс проводов двигателя для короткого контакта в начале.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините проводку интерфейса двигателя от панели интерфейса OEM. Отсоедините проводку интерфейса двигателя от CIB. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте интерфейс проводов двигателя для короткого контакта в начале. Измерьте сопротивление между стартовым контактом SIGNAL 24 в разъёме ремня электропроводки интерфейса двигателя и всеми другими штифтами в разъёме ремня электропроводки интерфейса двигателя. | Сопротивление больше 100k Ом? *Да | 3C |
| Сопротивление больше 100k Ом? **NORepair: **В начале было обнаружено короткое замыкание. Ремонт или замена интерфейса двигателя проводкой ремня. См. процедуру 015-093 в разделе 15. | Ремонт завершён. |  |

#### ШАГ 3C. Проверьте интерфейс проводов двигателя для открытого в начале.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините проводку интерфейса двигателя от панели интерфейса OEM. Отсоедините проводку интерфейса двигателя от CIB. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте интерфейс проводов двигателя для открытого в начале. Измерьте сопротивление между стартовым контактом SIGNAL 24 в разъёме ремня проводов интерфейса двигателя (присоединение к панели интерфейса OEM) и запуском контакта SIGNAL 10 в разъёме интерфейса двигателя (присоединение к CIB). | Сопротивление менее 10 Ом? *Да | 4А |
| Сопротивление менее 10 Ом? **NORepair: **В начале была обнаружена открытая цепь. Ремонт или замена интерфейса двигателя проводкой ремня. См. процедуру 015-093 в разделе 15. | Ремонт завершён. |  |

### ШАГ 4. Проверьте OEM интерфейс проводов жгута.

#### ШАГ 4A. Проверьте OEM интерфейс проводов жгута.

| **Условия:** Система поворота позволяет выключать выключатель. Отключите OEM-интерфейс проводов от CIB. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте OEM интерфейс проводов жгута. Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт: **В разъёме жгута проводов обнаружено поврежденное соединение. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъем или штифты. Для OEM интерфейса проводов жгута: См. процедуру 015-104 в разделе 15. | Ремонт завершён. |
| Грязные или поврежденные контакты? **НЕТ** | 4B |  |

#### ШАГ 4B. Проверьте OEM интерфейс проводов жгута для открытой цепи в нейтральной цепи безопасности.

| **Условия:** Система поворота позволяет выключать выключатель. Отключите OEM-интерфейс проводов от CIB. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте OEM интерфейс проводов жгута для открытой цепи в нейтральной цепи безопасности. Измерьте сопротивление через нейтральные контакты 11 и 12 цепи безопасности на разъёме ремня электропроводки OEM-интерфейса. | Менее 10 Ом? *Да | 5а |
| Менее 10 Ом? **NORepair: **В нейтральной цепи безопасности обнаружена открытая поверхность. Ремонт OEM интерфейса проводов и межсоединений. См. процедуру 015-104 в разделе 15. | Ремонт завершён. |  |

### ШАГ 5. Проверьте жгут проводов приложения привода.

#### Шаг. Проверьте жгут проводов привода.

| **Условия:** Система поворота позволяет выключать выключатель. Отключите привод приложения проводов жгута от CIB. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте жгут проводов привода. Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт: **В разъёме жгута проводов обнаружено поврежденное соединение. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъем или штифты. Ремонт OEM интерфейса проводов жгута. См. процедуру 015-104 в разделе 15. | Ремонт завершён. |
| Грязные или поврежденные контакты? **НЕТ** | 5В |  |

#### ШАГ 5B. Проверьте приложение привода проводов жгута для открытой цепи в нейтральной цепи безопасности.

| **Условия:** Система поворота позволяет выключать выключатель. Отключите привод приложения проводов жгута от двигателя проводов жгута. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте приложение привода проводов жгута для открытой цепи в нейтральной цепи безопасности. Измерьте сопротивление по нейтральной цепи безопасности контактов 10 и 11 на разъеме электропроводки привода (прикрепление к электропроводке двигателя). | Менее 10 Ом? *Да | 6А |
| Менее 10 Ом? **NORepair: **В нейтральной цепи безопасности обнаружена открытая поверхность. Ремонт OEM интерфейса проводов и межсоединений. См. процедуру 015-099 в разделе 15. | Ремонт завершён. |  |

### ШАГ 6. Проверьте C.I.B.

#### ШАГ 6A. Проверьте реле начального локаута в CIB.

| Открыть КИБ. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте реле начального локаута в CIB. Найдите стартовый локаут-ретранслятор LED. См. процедуру 015-023 в разделе 15. | Светодиод для начального локаута подсвечивается? **Ремонт: **ECM заблокировал двигатель от запуска. Исследуйте двигатель с помощью электронного инструментария обслуживания INSITETM для соответствующих кодов неисправностей. | Ремонт завершён |
| Светодиод для начального локаута подсвечивается? **НЕТ** | 6B |  |

#### ШАГ 6B. Проверьте выключатель запуска / остановки (CIB).

| **Условия: **Открыть CIB. Отключите стартовый/стоп-коммутатор. См. процедуру 015-109 в разделе 15. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте выключатель запуска / остановки (CIB). Измерьте сопротивление между контактом 2 и контактом 3 в разъеме стартового/стоп-коммутатора. | Сопротивление менее 10 Ом при включении переключателя? *Да | 6C |
| Сопротивление менее 10 Ом при включении переключателя? **NORepair:** Заменить выключатель «Пуск/Стоп».[[513-015-109 — Start Stop Switch\|См. процедуру 015-109 в разделе 15.]] | Ремонт завершён. |  |

#### ШАГ 6C. Проверьте стартовое напряжение от CIB.

| **Условия:** Включить систему, включить переключение. Отсоедините проводку интерфейса двигателя от CIB. Нажмите и удерживайте кнопку запуска/остановки в начальном положении. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте стартовое напряжение от CIB. Поместите один свинец на стартовый SIGNAL контакт 10 разъема CIB (прикрепление к интерфейсу двигателя проводной ремни). Поместите другой свинец на наземный контакт 4 разъема CIB (прикрепляется к интерфейсу двигателя проводной упряжкой). | Приблизительное напряжение батареи? **Ремонт: **ECM заблокировал двигатель от запуска. Исследуйте двигатель с помощью электронного инструментария обслуживания INSITETM для соответствующих кодов неисправностей. | Ремонт завершён. |
| Приблизительное напряжение батареи? **НЕТ** | 7А |  |

### ШАГ 7. Проверьте основную проводку расширения.

#### ШАГ 7A. Проверьте основную проводку расширения.

| **Условия:** Система поворота позволяет выключать выключатель. Отключите основную проводку расширения от CIB. Отсоедините основную удлинительную проводку от рулевой проводов |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте основную проводку расширения. Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт:** По возможности отремонтируйте поврежденную проводку, разъем или штифты. Для основной удлинительной проводов жгута: См. процедуру 015-077 в разделе 15. Для CIB: См. процедуру 015-023 в разделе 15. | Ремонт завершён. |
| Грязные или поврежденные контакты? **НЕТ** | 7B |  |

#### ШАГ 7B. Проверьте основную удлинительную проводку для короткого контакта в начале.

| **Условия:** Система поворота позволяет выключать выключатель. Отключите основную проводку расширения от CIB. Отсоедините основную удлинительную проводку от рулевой проводов |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте основную удлинительную проводку для короткого контакта в начале. Измерьте сопротивление между контактом стартового сигнала в разъеме главного удлинителя проводов и всеми другими штифтами в разъеме главного удлинителя проводов. | Сопротивление больше 100k Ом? *Да | 7C |
| Сопротивление больше 100k Ом? **NORepair: **В начале было обнаружено короткое замыкание. Ремонт или замена основного удлинителя проводов ремня. См. процедуру 015-077 в разделе 15. | Ремонт завершён. |  |

#### ШАГ 7C. Проверьте основную удлинительную проводку для открытия в начале.

| **Условия:** Система поворота позволяет выключать выключатель. Отключите основную проводку расширения от CIB. Отсоедините основную удлинительную проводку от рулевой проводов |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте основную удлинительную проводку для открытия в начале. Измерьте сопротивление между стартовым контактом SIGNAL 10 в главном разъеме удлинителя проводов жгута (присоединение к рулевой проводах упряжки) и запуском контакта SIGNAL 10 в главном разъеме удлинения (присоединение к CIB). | Сопротивление менее 10 Ом? *Да | 8а |
| Сопротивление менее 10 Ом? **NORepair: **В начале была обнаружена открытая цепь. Ремонт или замена основного удлинителя проводов ремня. См. процедуру 015-077 в разделе 15. | Ремонт завершён. |  |

### ШАГ 8. Проверьте штурвал.

#### ШАГ 8A. Проверьте стартовый выключатель (помощь).

| **Условия: **Отключите стартовый выключатель. См. процедуру 015-101 в разделе 15. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте стартовый выключатель (помощь). Измерить сопротивление между контактом 2 и контактом 3 в системе включить переключатель. | Сопротивление менее 10 Ом при включении переключателя? *Да | 8B |
| Сопротивление менее 10 Ом при включении переключателя? **NORepair:** Заменить стартовый выключатель.[[513-015-101 — Start Switch\|См. процедуру 015-101 в разделе 15.]] | Ремонт завершён. |  |

#### ШАГ 8B. Проверьте штурвал проводов.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините рулевую проводку от основной удлинительной проводов. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте штурвал проводов. Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт: **В разъёме жгута проводов обнаружено поврежденное соединение. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъем или штифты. Для штурвала проводов ремня: См. процедуру 015-078 в разделе 15. | Ремонт завершён. |
| Грязные или поврежденные контакты? **НЕТ** | 8C |  |

#### ШАГ 8C. Проверьте рулевую проводку для короткого контакта в начале.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините все спаривающиеся жгуты к рулевой жгут. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте рулевую проводку для короткого контакта в начале. Измерьте сопротивление между стартовым контактом SIGNAL 10 в разъёме штурвала жгута (привязка к основному удлинению) и всеми другими штифтами в разъёме штурвала жгута. | Сопротивление больше 100k Ом? *Да | 8D |
| Сопротивление больше 100k Ом? **NORepair: **В начале было обнаружено короткое замыкание. Ремонт или замена рулевой проводов. См. процедуру 015-078 в разделе 15. | Ремонт завершён. |  |

#### ШАГ 8D. Проверьте рулевую проводку для открытия в начале.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините все спаривающиеся жгуты к рулевой жгут. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте рулевую проводку для открытия в начале. Измерьте сопротивление между стартовым контактом SIGNAL 3 в разъеме рулевой проводов (присоединение к системе позволяет переключатель) и запуском контакта SIGNAL 10 в разъеме рулевой проводов (присоединение к главному удлинителю проводов). | Сопротивление менее 10 Ом? **Ремонт: **В CIB обнаружена неисправность. Заменить CIB. См. процедуру 015-023 в разделе 15. | Ремонт завершён. |
| Сопротивление менее 10 Ом? **NORepair: **В начале была обнаружена открытая цепь. Ремонт или замена рулевой проводов. См. процедуру 015-078 в разделе 15. | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - The engine will **not** crank when start button is pressed.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot engine starting symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> To initiate engine crank, the following panel parameters **must** be met:
>
> - The system enable switch is turned to the ON position
>
> - The engine is stopped
>
> - Main throttle and backup throttle in neutral position
>
> - Throttle is in neutral position
>
> - Battery disconnect is switched ON.
>
> Possible causes are:
>
> - Start is shorted or open
>
> - Start switch malfunction
>
> - Neutral safety circuit open
>
> - Starter lockout on engine is engaged.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the breaker and switches. |  |
> |  | **STEP 1A.** Check the breaker on the customer interface box (CIB). | Breaker open or popped? |
> |  | **STEP 1B.** Check the starter voltage. | Equal to battery voltage? |
> | STEP 2. | Check the engine wiring harness. |  |
> |  | **STEP 2A.** Inspect the engine wiring harness. | Dirty or damaged pins? |
> |  | **STEP 2B.** Check the engine wiring harness for a pin-to-pin short in the start signal. | Greater than 100k ohms resistance? |
> |  | **STEP 2C.** Check the engine wiring harness for an open in the start. | Less than 10 ohms resistance? |
> | STEP 3. | Check the engine interface harness. |  |
> |  | **STEP 3A.** Inspect the engine interface harness. | Dirty or damaged pins? |
> |  | **STEP 3B.** Check the engine interface wiring harness for a pin-to-pin short in the start. | Greater than 100k ohms resistance? |
> |  | **STEP 3C.** Check the engine interface wiring harness for an open in the start. | Less than 10 ohms resistance? |
> | STEP 4. | Check the original equipment manufacturer (OEM) interface harness. |  |
> |  | **STEP 4A.** Inspect the OEM interface wiring harness. | Dirty or damaged pins? |
> |  | **STEP 4B.** Check the OEM interface wiring harness for an open circuit in the neutral safety circuit. | Less than 10 ohms? |
> | STEP 5. | Check the drive application harness. |  |
> |  | **STEP 5A.** Inspect the drive application wiring harness. | Dirty or damaged pins? |
> |  | **STEP 5B.** Check the drive application wiring harness for an open circuit in the neutral safety circuit. | Less than 10 ohms? |
> | STEP 6. | Check the CIB. |  |
> |  | **STEP 6A.** Check the starter lockout relay in the CIB. | LED for starter lockout illuminated? |
> |  | **STEP 6B.** Check the start/stop switch (CIB). | Less than 10 ohms resistance when switch is in ON position? |
> |  | **STEP 6C.** Check the starter voltage from the CIB. | Approximate battery voltage? |
> | STEP 7. | Check main extension wiring harness. |  |
> |  | **STEP 7A.** Inspect the main extension harness. | Dirty or damaged pins? |
> |  | **STEP 7B.** Check the main extension wiring harness for a pin-to-pin short in the start. | Greater than 100k ohms resistance? |
> |  | **STEP 7C.** Check the main extension wiring harness for an open in the start. | Less than 10 ohms resistance? |
> | STEP 8. | Check the helm. |  |
> |  | **STEP 8A.** Check the start switch (helm). | Less than 10 ohms resistance when switch is in ON position? |
> |  | **STEP 8B.** Inspect the helm harness. | Dirty or damaged pins? |
> |  | **STEP 8C.** Check the helm wiring harness for a pin-to-pin short in the start. | Greater than 100k ohms resistance? |
> |  | **STEP 8D.** Check the helm wiring harness for an open in the start. | Less than 10 ohms resistance? |
>
> ### STEP 1. Check the breaker and switches.
>
> #### STEP 1A. Check the breaker on the CIB.
>
> | **Conditions:** Turn system enable switch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the breaker on the CIB. Check the circuit breaker on CIB. | Breaker open or popped? **YESRepair:** Reset breaker on the CIB. Refer to Procedure 015-023 in Section 15. | Repair complete. |
> | Breaker open or popped? **NO** | 1B |  |
>
> #### STEP 1B. Check the starter voltage.
>
> | **Conditions:** Turn system enable switch ON. Press and hold the start/stop switch in the start position (CIB). |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the starter voltage. Place one test lead on the magnetic start terminal and the other lead to ground at the starter. | Equal to battery voltage? **YESRepair:** Starter issue has been detected. For starter magnetic switch: Reference Procedure 013-017 in Section 13 of the appropriate engine service manual. For starter solenoid: Reference Procedure 013-019 in Section 13 of the appropriate engine service manual. | Repair complete. |
> | Equal to battery voltage? **NO** | 2A |  |
>
> ### STEP 2. Check the engine wiring harness.
>
> #### STEP 2A. Inspect the engine wiring harness.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the engine interface wiring harness from the OEM interface panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine wiring harness. Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Wire insulation damage Connector shell broken Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. For the engine wiring harness: Reference Procedure 019-043 in Section 19 of the appropriate engine service manual. | Repair complete. |
> | Dirty or damaged pins? **NO** | 2B |  |
>
> #### STEP 2B. Check the engine wiring harness for a pin-to-pin short in the start signal.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect engine interface wiring harness from the OEM interface panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine wiring harness for a pin-to-pin short in the start signal. Measure the resistance between the start SIGNAL pin 24 in the OEM interface panel connector and all other pins in the engine wiring harness connector. | Greater than 100k ohms resistance? **YESRepair:** Reroute the harness. | 2C |
> | Greater than 100k ohms resistance? **NORepair:** A pin-to-pin short circuit has been detected in the start signal. Repair or replace the engine wiring harness. Reference Procedure 019-043 in Section 19 of the appropriate engine service manual. | Repair complete. |  |
>
> #### STEP 2C. Check the engine wiring harness for an open in the start.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect engine wiring harness from the engine control module (ECM). Disconnect engine wiring harness from the OEM interface panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine wiring harness for an open in the start. Measure the resistance between the start SIGNAL pin 24 at the OEM interface panel connector and start signal at the starter magnetic switch. | Less than 10 ohms resistance? **YES** | 3A |
> | Less than 10 ohms resistance? **NORepair:** An open circuit has been detected in the start. Repair or replace the engine wiring harness. Reference Procedure 019-043 in Section 19 of the appropriate engine service manual. | Repair complete. |  |
>
> ### STEP 3. Check the engine interface harness.
>
> #### STEP 3A. Inspect the engine interface harness.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the engine interface harness from the OEM interface panel. Disconnect the engine interface harness from the CIB. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine interface harness. Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. For the engine interface harness: Refer to Procedure 015-093 in Section 15. | Repair complete. |
> | Dirty or damaged pins? **NO** | 3B |  |
>
> #### STEP 3B. Check the engine interface wiring harness for a pin-to-pin short in the start.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the engine interface harness from the OEM interface panel. Disconnect the engine interface harness from the CIB. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine interface wiring harness for a pin-to-pin short in the start. Measure the resistance between the start SIGNAL pin 24 in the engine interface harness connector and all other pins in the engine interface harness connector. | Greater than 100k ohms resistance? **YES** | 3C |
> | Greater than 100k ohms resistance? **NORepair:** A short circuit has been detected in the start. Repair or replace the engine interface harness. Refer to Procedure 015-093 in Section 15. | Repair complete. |  |
>
> #### STEP 3C. Check the engine interface wiring harness for an open in the start.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the engine interface harness from the OEM interface panel. Disconnect the engine interface harness from the CIB. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine interface wiring harness for an open in the start. Measure the resistance between the start SIGNAL pin 24 in the engine interface harness connector (mating to the OEM interface panel) and start SIGNAL pin 10 in the engine interface connector (mating to the CIB). | Less than 10 ohms resistance? **YES** | 4A |
> | Less than 10 ohms resistance? **NORepair:** A open circuit has been detected in the start. Repair or replace the engine interface harness. Refer to Procedure 015-093 in Section 15. | Repair complete. |  |
>
> ### STEP 4. Check the OEM interface harness.
>
> #### STEP 4A. Inspect the OEM interface wiring harness.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect OEM interface wiring harness from the CIB. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the OEM interface wiring harness. Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. For the OEM interface wiring harness: Refer to Procedure 015-104 in Section 15. | Repair complete. |
> | Dirty or damaged pins? **NO** | 4B |  |
>
> #### STEP 4B. Check the OEM interface wiring harness for an open circuit in the neutral safety circuit.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect OEM interface wiring harness from the CIB. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the OEM interface wiring harness for an open circuit in the neutral safety circuit. Measure the resistance across the neutral safety circuit pins 11 and 12 on the OEM interface wiring harness connector. | Less than 10 ohms? **YES** | 5A |
> | Less than 10 ohms? **NORepair:** An open in the neutral safety circuit has been detected. Repair the OEM interface wiring harness and interconnects. Refer to Procedure 015-104 in Section 15. | Repair complete. |  |
>
> ### STEP 5. Check the drive application harness.
>
> #### STEP. Inspect the drive application wiring harness.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect drive application wiring harness from the CIB. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the drive application wiring harness. Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Repair the OEM interface wiring harness. Refer to Procedure 015-104 in Section 15. | Repair complete. |
> | Dirty or damaged pins? **NO** | 5B |  |
>
> #### STEP 5B. Check the drive application wiring harness for an open circuit in the neutral safety circuit.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect drive application wiring harness from engine wiring harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the drive application wiring harness for an open circuit in the neutral safety circuit. Measure the resistance across the neutral safety circuit pins 10 and 11 on the drive application wiring harness connector (mating to the engine wiring harness). | Less than 10 ohms? **YES** | 6A |
> | Less than 10 ohms? **NORepair:** An open in the neutral safety circuit has been detected. Repair the OEM interface wiring harness and interconnects. Refer to Procedure 015-099 in Section 15. | Repair complete. |  |
>
> ### STEP 6. Check the C.I.B.
>
> #### STEP 6A. Check the starter lockout relay in the CIB.
>
> | **Conditions:** Open up the CIB. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the starter lockout relay in the CIB. Locate the starter lockout relay LED. Refer to Procedure 015-023 in Section 15. | LED for starter lockout illuminated? **YESRepair:** The ECM has locked out the engine from starting. Investigate engine with INSITE™ electronic service tool for related fault codes. | Repair complete |
> | LED for starter lockout illuminated? **NO** | 6B |  |
>
> #### STEP 6B. Check the start/stop switch (CIB).
>
> | **Conditions:** Open the CIB. Disconnect the start/stop switch. Refer to Procedure 015-109 in Section 15. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the start/stop switch (CIB). Measure the resistance between pin 2 and pin 3 at the start/stop switch connector. | Less than 10 ohms resistance when switch is in ON position? **YES** | 6C |
> | Less than 10 ohms resistance when switch is in ON position? **NORepair:** Replace the start/stop switch. [[513-015-109 — Start Stop Switch\|Refer to Procedure 015-109 in Section 15.]] | Repair complete. |  |
>
> #### STEP 6C. Check the starter voltage from the CIB.
>
> | **Conditions:** Turn the system enable switch ON. Disconnect the engine interface wiring harness from the CIB. Press and hold the start/stop button in the starting position. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the starter voltage from the CIB. Place one lead on the start SIGNAL pin 10 of the CIB connector (mating to the engine interface wiring harness). Place the other lead on the ground pin 4 of the CIB connector (mating to the engine interface wiring harness). | Approximate battery voltage? **YESRepair:** The ECM has locked out the engine from starting. Investigate engine with INSITE™ electronic service tool for related fault codes. | Repair complete. |
> | Approximate battery voltage? **NO** | 7A |  |
>
> ### STEP 7. Check main extension wiring harness.
>
> #### STEP 7A. Inspect the main extension harness.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the main extension harness from the CIB. Disconnect the main extension harness from the helm harness |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the main extension harness. Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** Repair the damaged harness, connector, or pins, if possible. For the main extension harness: Refer to Procedure 015-077 in Section 15. For the CIB: Refer to Procedure 015-023 in Section 15. | Repair complete. |
> | Dirty or damaged pins? **NO** | 7B |  |
>
> #### STEP 7B. Check the main extension wiring harness for a pin-to-pin short in the start.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the main extension harness from the CIB. Disconnect the main extension harness from the helm harness |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the main extension wiring harness for a pin-to-pin short in the start. Measure the resistance between the start SIGNAL pin in the main extension harness connector and all other pins in the main extension harness connector. | Greater than 100k ohms resistance? **YES** | 7C |
> | Greater than 100k ohms resistance? **NORepair:** A short circuit has been detected in the start. Repair or replace the main extension wiring harness. Refer to Procedure 015-077 in Section 15. | Repair complete. |  |
>
> #### STEP 7C. Check the main extension wiring harness for an open in the start.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the main extension harness from the CIB. Disconnect the main extension harness from the helm harness |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the main extension wiring harness for an open in the start. Measure the resistance between the start SIGNAL pin 10 in the main extension harness connector (mating to the helm harness) and start SIGNAL pin 10 in the main extension connector (mating to the CIB). | Less than 10 ohms resistance? **YES** | 8A |
> | Less than 10 ohms resistance? **NORepair:** An open circuit has been detected in the start. Repair or replace the main extension wiring harness. Refer to Procedure 015-077 in Section 15. | Repair complete. |  |
>
> ### STEP 8. Check the helm.
>
> #### STEP 8A. Check the start switch (helm).
>
> | **Conditions:** Disconnect the start switch. Refer to Procedure 015-101 in Section 15. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the start switch (helm). Measure the resistance between pin 2 and pin 3 at the system enable switch. | Less than 10 ohms resistance when switch is in ON position? **YES** | 8B |
> | Less than 10 ohms resistance when switch is in ON position? **NORepair:** Replace the start switch. [[513-015-101 — Start Switch\|Refer to Procedure 015-101 in Section 15.]] | Repair complete. |  |
>
> #### STEP 8B. Inspect the helm harness.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the helm harness from the main extension harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the helm harness. Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. For the helm harness: Refer to Procedure 015-078 in Section 15. | Repair complete. |
> | Dirty or damaged pins? **NO** | 8C |  |
>
> #### STEP 8C. Check the helm wiring harness for a pin-to-pin short in the start.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect all mating harnesses to the helm harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the helm wiring harness for a pin-to-pin short in the start. Measure the resistance between the start SIGNAL pin 10 in the helm harness connector (mating to the main extension) and all other pins in the helm harness connector. | Greater than 100k ohms resistance? **YES** | 8D |
> | Greater than 100k ohms resistance? **NORepair:** A short circuit has been detected in the start. Repair or replace the helm wiring harness. Refer to Procedure 015-078 in Section 15. | Repair complete. |  |
>
> #### STEP 8D. Check the helm wiring harness for an open in the start.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect all mating harnesses to the helm harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the helm wiring harness for an open in the start. Measure the resistance between the start SIGNAL pin 3 in the helm harness connector (mating to the system enable switch) and start SIGNAL pin 10 in the helm harness connector (mating to the main extension harness). | Less than 10 ohms resistance? **YESRepair:** A malfunction has been detected in the CIB. Replace the CIB. Refer to Procedure 015-023 in Section 15. | Repair complete. |
> | Less than 10 ohms resistance? **NORepair:** A open circuit has been detected in the start. Repair or replace the helm wiring harness. Refer to Procedure 015-078 in Section 15. | Repair complete. |  |
