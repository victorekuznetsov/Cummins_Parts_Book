---
type: "Процедура"
doc: "513-t02-1019"
title_en: "Engine Will Not Stop From the Helm or Customer Interface Box"
modified: "2019-10-21"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1019.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1019.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
  - "перевод/машинный"
---

# Engine Will Not Stop From the Helm or Customer Interface Box

> [!abstract] Процедура · `513-t02-1019`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-10-21
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1019.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1019.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Двигатель будет **не** выключаться, когда стоп- или стоп-старт переключается на выключение в штурвале или в поле интерфейса клиента (CIB).

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения симптомов двигателя. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Возможные причины:

- Неисправный выключатель Stop

- Открытая цепь в сигнале Stop

- Короткое замыкание в сигнале Стоп.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте штурвал проводов. |  |
|  | **ШАГ 1А.** Проверьте переключатель/кнопку START/STOP (помощь). | Сопротивление менее 10 Ом при включении/нажатии переключателя? |
|  | **ШАГ 1В.** Проверить штурвал проводов. | Грязные или поврежденные контакты? |
|  | **STEP 1C.** Проверьте рулевую проводку на коротком контакте в переключателе зажигания. | Сопротивление больше 100k Ом? |
|  | **STEP 1D.** Проверьте рулевую проводку на наличие открытого сигнала Стоп. | Сопротивление менее 10 Ом? |
| ШАГ 2. | Проверьте основную проводку расширения. |  |
|  | **STEP 2A.** Осмотрите основные проводов расширения. | Грязные или поврежденные контакты? |
|  | **STEP 2B.** Проверьте основную проводку расширения для короткого контакта в переключателе зажигания. | Сопротивление больше 100k Ом? |
|  | **STEP 2C.** Проверьте основную проводку расширения на наличие открытого сигнала Stop. | Сопротивление менее 10 Ом? |
| ШАГ 3. | Проверьте C.I.B. |  |
|  | **STEP 3A.** Проверьте выключатель «Пуск/Стоп» (C.I.B). | Сопротивление менее 10 Ом при включении переключателя? |
|  | **STEP 3B** Проверьте выключатель «Пуск/Стоп» (C.I.B). | **Только **реле выключения включено. |

### ШАГ 1. Проверьте штурвал проводов.

#### ШАГ 1A. Проверьте переключатель / кнопку START / STOP (помощь).

| **Условия:** Отключить переключатель/кнопку START/STOP у руля. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление. Измерьте сопротивление между контактом 3 и контактом 4 в ремне тормозной проводов. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Сопротивление менее 10 Ом при включении/нажатии переключателя? *Да | 1В |
| Сопротивление менее 10 Ом при включении/нажатии переключателя? **NORepair:** Заменить стартовый выключатель. Для PS102 Systems:[[513-015-101 — Start Switch\|См. процедуру 015-101 в разделе 15.]]Для PS103 Systems:[[513-015-109 — Start Stop Switch\|См. процедуру 015-109 в разделе 15.]] | Ремонт завершён. |  |

#### ШАГ 1B. Проверьте штурвал проводов.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините рулевую проводку от основной удлинительной проводов. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт: **В разъёме жгута проводов обнаружено поврежденное соединение. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъем или штифты. Для штурвала проводов ремня: См. процедуру 015-078 в разделе 15. Для основной удлинительной проводов жгута: См. процедуру 015-077 в разделе 15. | Ремонт завершён |
| Грязные или поврежденные контакты? **НЕТ** | 1С |  |

#### ШАГ 1C. Проверьте рулевую проводку ремня для короткого контакта в переключателе зажигания.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините все спаривающиеся жгуты к рулевой жгут. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление между контактом Stop SIGNAL 3 в разъёме штурвала проводов (прикрепление к основному удлинению) и всеми другими штифтами в разъёме штурвала проводов. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Сопротивление больше 100k Ом? *Да | 1D |
| Сопротивление больше 100k Ом? **NORepair:** В переключателе зажигания обнаружено короткое замыкание. Ремонт или замена рулевой проводов. См. процедуру 015-077 в разделе 15. | Ремонт завершён |  |

#### ШАГ 1D. Проверьте штурвал проводов для открытого сигнала Стоп.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините все спаривающиеся жгуты к рулевой жгут. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление между контактом Stop SIGNAL 9 на разъёме штурвала проводов (прикрепление к главному удлинителю проводов) и контактом Stop SIGNAL 3 на разъёме рулевой проводов (прикрепление к выключателю Стоп). См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Сопротивление менее 10 Ом? *Да | 2А |
| Сопротивление менее 10 Ом? **NORepair:** В переключателе зажигания обнаружена открытая цепь. Ремонт или замена рулевой проводов. См. процедуру 015-077 в разделе 15. | Ремонт завершён |  |

### ШАГ 2. Проверьте основную проводку расширения.

#### ШАГ 2A. Проверьте основную проводку расширения.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините основную проводку расширения от интерфейса двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт:** Очистить разъем и штифты. По возможности отремонтируйте поврежденную проводку, разъем или штифты. Для основной удлинительной проводов жгута: См. процедуру 015-077 в разделе 15. | Ремонт завершён |
| Грязные или поврежденные контакты? **НЕТ** | 2В |  |

#### ШАГ 2B. Проверьте основную проводку расширения для короткого контакта в переключателе зажигания.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините все спаривающиеся жгуты к основной удлинительной жгутке. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление между контактом Stop SIGNAL 9 в разъеме главного удлинителя проводов и всеми другими штифтами в разъеме главного удлинителя проводов. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Сопротивление больше 100k Ом? *Да | 2C |
| Сопротивление больше 100k Ом? **NORepair: **В сигнале Stop обнаружено короткое замыкание. Ремонт или замена основного удлинителя проводов ремня. См. процедуру 015-077 в разделе 15. | Ремонт завершён. |  |

#### ШАГ 2C. Проверьте основную проводку расширения для открытого сигнала Stop.

| **Условия:** Система поворота позволяет выключать выключатель. Отключите компьютерную систему. от основного удлинителя проводов жгута. Отсоедините рулевую проводку от основной удлинительной проводов |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление между контактом 9 Stop SIGNAL на главном разъеме удлинителя проводов (присоединение к C.I.B) и контактом 9 Stop SIGNAL на главном разъеме удлинителя проводов (присоединение к рулевой проводах). См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Сопротивление менее 10 Ом? *Да | 3А |
| Сопротивление менее 10 Ом? **NORepair: **В сигнале Stop обнаружена открытая цепь. Ремонт или замена основного удлинителя проводов ремня. См. процедуру 015-077 в разделе 15. | Ремонт завершён. |  |

### ШАГ 3. Проверьте C.I.B.

#### ШАГ 3A. Проверьте выключатель START/STOP (C.I.B).

| **Условия: **Откройте окно клиентского интерфейса. См. процедуру 015-023 в разделе 15. Отключите переключатель START/STOP. См. процедуру 015-109 в разделе 15. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление между контактом 2 и контактом 3 в разъеме переключателя START/STOP. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Сопротивление менее 10 Ом при включении переключателя? *Да | 3B |
| Сопротивление менее 10 Ом при включении переключателя? **NORepair:** Заменить выключатель START/STOP.[[513-015-109 — Start Stop Switch\|См. процедуру 015-109 в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 3B. Проверьте выключатель START/STOP (C.I.B.).

| **Условия: **Откройте C.I.B. См. процедуру 015-023 в разделе 15. Нажмите и удерживайте кнопку START/STOP. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Реле выключения монитора LED. | **Только **реле выключения включено. **Ремонт: **См. двигатель будет **Не **Закрыть в дерево симптомов устранения неполадок в разделе TS | Ремонт завершён |
| **Только **реле выключения включено. **NORepair:** В ЦБ обнаружена неисправность. Замените информатора. См. процедуру 015-023 в разделе 15. | Ремонт завершён |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - Engine will **not** shutoff when the Stop or Stop/Start is switched to OFF at the helm or customer interface box (CIB).
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot engine symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> Possible Causes:
>
> - Malfunctioning Stop switch
>
> - Open circuit in the Stop signal
>
> - Short circuit in the Stop signal.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the helm wiring harness. |  |
> |  | **STEP 1A.** Check the START/STOP switch/button (helm). | Less than 10 ohms resistance when switch is in ON/Pushed position? |
> |  | **STEP 1B.** Inspect the helm harness. | Dirty or damaged pins? |
> |  | **STEP 1C.** Check the helm wiring harness for a pin-to-pin short in the keyswitch. | Greater than 100k ohms resistance? |
> |  | **STEP 1D.** Check the helm wiring harness for an open in the Stop signal. | Less than 10 ohms resistance? |
> | STEP 2. | Check main extension wiring harness. |  |
> |  | **STEP 2A.** Inspect the main extension harness. | Dirty or damaged pins? |
> |  | **STEP 2B.** Check the main extension wiring harness for a pin-to-pin short in the keyswitch. | Greater than 100k ohms resistance? |
> |  | **STEP 2C.** Check the main extension wiring harness for an open in the Stop signal. | Less than 10 ohms resistance? |
> | STEP 3. | Check the C.I.B. |  |
> |  | **STEP 3A.** Check the Start/Stop switch (C.I.B). | Less than 10 ohms resistance when switch is in ON position? |
> |  | **STEP 3B.** Check the Start/Stop switch (C.I.B). | **Only** shutdown relay ON? |
>
> ### STEP 1. Check the helm wiring harness.
>
> #### STEP 1A. Check the START/STOP switch/button (helm).
>
> | **Conditions:** Disconnect the START/STOP switch/button at the helm. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance. Measure the resistance between pin 3 and pin 4 at the Stop switch pigtail harness. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms resistance when switch is in ON/Pushed position? **YES** | 1B |
> | Less than 10 ohms resistance when switch is in ON/Pushed position? **NORepair:** Replace the start switch. For PS102 Systems:. [[513-015-101 — Start Switch\|Refer to Procedure 015-101 in Section 15.]] For PS103 Systems:. [[513-015-109 — Start Stop Switch\|Refer to Procedure 015-109 in Section 15.]] | Repair complete. |  |
>
> #### STEP 1B. Inspect the helm harness.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the helm harness from the main extension harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. For the helm harness: Refer to Procedure 015-078 in Section 15. For the main extension harness: Refer to Procedure 015-077 in Section 15. | Repair complete |
> | Dirty or damaged pins? **NO** | 1C |  |
>
> #### STEP 1C. Check the helm wiring harness for a pin-to-pin short in the keyswitch.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect all mating harnesses to the helm harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance between the Stop SIGNAL pin 3 in the helm harness connector (mating to the main extension) and all other pins in the helm harness connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms resistance? **YES** | 1D |
> | Greater than 100k ohms resistance? **NORepair:** A short circuit has been detected in the keyswitch. Repair or replace helm wiring harness. Refer to Procedure 015-077 in Section 15. | Repair complete |  |
>
> #### STEP 1D. Check the helm wiring harness for an open in the Stop signal.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect all mating harnesses to the helm harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance between the Stop SIGNAL pin 9 at the helm harness connector (mating to the main extension harness) and Stop SIGNAL pin 3 at the helm harness connector (mating to the Stop switch). Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms resistance? **YES** | 2A |
> | Less than 10 ohms resistance? **NORepair:** A open circuit has been detected in the keyswitch. Repair or replace helm wiring harness. Refer to Procedure 015-077 in Section 15. | Repair complete |  |
>
> ### STEP 2. Check main extension wiring harness.
>
> #### STEP 2A. Inspect the main extension harness.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the main extension harness from the engine interface harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. For the main extension harness: Refer to Procedure 015-077 in Section 15. | Repair complete |
> | Dirty or damaged pins? **NO** | 2B |  |
>
> #### STEP 2B. Check the main extension wiring harness for a pin-to-pin short in the keyswitch.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect all mating harnesses to the main extension harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance between the Stop SIGNAL pin 9 in the main extension harness connector and all other pins in the main extension harness connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms resistance? **YES** | 2C |
> | Greater than 100k ohms resistance? **NORepair:** A short circuit has been detected in the Stop signal. Repair or replace main extension wiring harness. Refer to Procedure 015-077 in Section 15. | Repair complete. |  |
>
> #### STEP 2C. Check the main extension wiring harness for an open in the Stop signal.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the C.I.B. from the main extension wiring harness. Disconnect the helm harness from the main extension wiring harness |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance between the Stop SIGNAL pin 9 at the main extension wiring harness connector (mating to the C.I.B) and Stop SIGNAL pin 9 at the main extension wiring harness connector (mating to the helm harness). Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms resistance? **YES** | 3A |
> | Less than 10 ohms resistance? **NORepair:** An open circuit has been detected in the Stop signal. Repair or replace the main extension wiring harness. Refer to Procedure 015-077 in Section 15. | Repair complete. |  |
>
> ### STEP 3. Check the C.I.B.
>
> #### STEP 3A. Check the START/STOP switch (C.I.B).
>
> | **Conditions:** Open up the customer interface Box. Refer to Procedure 015-023 in Section 15. Disconnect the START/STOP switch. Refer to Procedure 015-109 in Section 15. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance between pin 2 and pin 3 at the START/STOP switch connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms resistance when switch is in ON position? **YES** | 3B |
> | Less than 10 ohms resistance when switch is in ON position? **NORepair:** Replace the START/STOP switch. [[513-015-109 — Start Stop Switch\|Refer to Procedure 015-109 in Section 15.]] | Repair complete |  |
>
> #### STEP 3B. Check the START/STOP switch (C.I.B.).
>
> | **Conditions:** Open up the C.I.B. Refer to Procedure 015-023 in Section 15. Press and hold START/STOP button. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Monitor shutdown relay LED. | **Only** shutdown relay ON? **YESRepair:** Refer to the Engine Will **Not** Shutoff in the troubleshooting symptom tree in Section TS | Repair complete |
> | **Only** shutdown relay ON? **NORepair:** A malfunction has been detected in the C.I.B. Replace the C.I.B. Refer to Procedure 015-023 in Section 15. | Repair complete |  |
