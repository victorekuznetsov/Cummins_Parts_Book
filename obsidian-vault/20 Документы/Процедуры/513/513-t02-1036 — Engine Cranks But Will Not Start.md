---
type: "Процедура"
doc: "513-t02-1036"
title_en: "Engine Cranks But Will Not Start"
modified: "2019-10-18"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1036.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1036.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
  - "перевод/машинный"
---

# Engine Cranks But Will Not Start

> [!abstract] Процедура · `513-t02-1036`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-10-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1036.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1036.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Двигатель будет работать, но **не**, когда нажата кнопка запуска.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения неполадок с симптомами мощности. Начните с шага 1 поиска неисправностей. Шаг 2 задаст ряд вопросов и предоставит список шагов по устранению неполадок, которые необходимо выполнить в зависимости от симптома.

### Практические замечания

Для запуска коленчатого механизма должны быть соблюдены следующие параметры панели:

- Система включения переключателя поворачивается в положение ON

- Двигатель остановлен

- Главная дроссельная заслонка и резервная дроссельная заслонка находятся в нейтральном положении

- Переключатель отключения батареи включен.

Возможные причины:

- Стоп закорочен или открыт

- Схема пожаротушения открыта

- Стартер локаут на двигателе задействован.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте окно интерфейса клиента (C.I.B.). |  |
|  | **STEP 1A.** Проверьте стартовый локаут-реле в C.I.B., если он оборудован. | Светодиод для начального локаута подсвечивается? |
|  | **STEP 1B.** Проверьте оригинальную проводку производителя оборудования (OEM) для открытой цепи в цепи пожаротушения. | Менее 10 Ом? |
|  | **STEP 1C** Проверить коды неисправностей модуля управления двигателем (ECM). | Активные коды ошибок на ECM? |

### ШАГ 1. Проверьте C.I.B.

#### ШАГ 1A. Проверьте реле начального локаута в СиБ. (если они оборудованы).

| **Условия: **Откройте C.I.B. См. процедуру 015-023 в разделе 15. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте реле начального локаута в СиБ. Найдите стартовый локаут-ретранслятор LED. См. процедуру 015-023 в разделе 15. | Светодиод для начального локаута подсвечивается? **Ремонт: **ECM заблокировал двигатель от запуска. Исследуйте двигатель с помощью электронного инструментария обслуживания INSITETM для соответствующих кодов неисправностей. | Ремонт завершён. |
| Светодиод для начального локаута подсвечивается? **НЕТ** | 1В |  |

#### ШАГ 1B. Проверьте OEM интерфейс проводов жгута для открытой цепи в цепи пожаротушения.

| **Условия:** Система поворота позволяет выключать выключатель. Отключите OEM-интерфейс проводов от C.I.B. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте OEM интерфейс проводов жгута для открытой цепи в цепи пожаротушения. Измерьте сопротивление по всей цепи пожаротушения контактов 11 и 12 на разъёме проводной упряжки OEM Interface (связывающемся с C.I.B). См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Менее 10 Ом? *Да | 2А |
| Менее 10 Ом? **NORepair:** В цепи пожаротушения обнаружена открытая стрела. Ремонт OEM интерфейса проводов и межсоединений. См. процедуру 015-104 в разделе 15. | Ремонт завершён. |  |

#### ШАГ 1C. Проверьте коды ошибок ECM.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте наличие активных кодов неисправностей. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Активные коды ошибок на ECM? *Да | Перейдите к соответствующему дереву устранения неисправностей кода ошибки. |
| Активные коды ошибок на ECM? **НЕТ** | См. Двигатель трудно запустить или будет **Не** Начать устранение неисправностей дерево симптомов в разделе ТС в соответствующем руководстве по обслуживанию. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - The engine will crank but **not** start when start button is pressed.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot display power symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform depending on the symptom.
>
> ### Shoptalk
>
> To initiate engine crank, the following panel parameters **must** be met:
>
> - The system enable switch is turned to the ON position
>
> - The engine is stopped
>
> - Main throttle and backup throttle are in neutral position
>
> - Battery disconnect switch is turned ON.
>
> Possible causes are:
>
> - Stop is shorted or open
>
> - Fire suppression circuit open
>
> - Starter lockout on engine is engaged.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the customer interface box (C.I.B.). |  |
> |  | **STEP 1A.** Check the starter lockout relay in the C.I.B., if equipped. | LED for starter lockout illuminated? |
> |  | **STEP 1B.** Check the original equipment manufacturer (OEM) interface wiring harness for an open circuit in the fire suppression circuit. | Less than 10 ohms? |
> |  | **STEP 1C.** Check for engine control module (ECM) fault codes. | Active fault codes on ECM? |
>
> ### STEP 1. Check the C.I.B.
>
> #### STEP 1A. Check the starter lockout relay in the C.I.B. (if equipped).
>
> | **Conditions:** Open up the C.I.B. Refer to Procedure 015-023 in Section 15. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the starter lockout relay in the C.I.B. Locate the starter lockout relay LED. Refer to Procedure 015-023 in Section 15. | LED for starter lockout illuminated? **YESRepair:** The ECM has locked out the engine from starting. Investigate engine with INSITE™ electronic service tool for related fault codes. | Repair complete. |
> | LED for starter lockout illuminated? **NO** | 1B |  |
>
> #### STEP 1B. Check the OEM Interface wiring harness for an open circuit in the fire suppression circuit.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect OEM interface wiring harness from the C.I.B. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the OEM Interface wiring harness for an open circuit in the fire suppression circuit. Measure the resistance across the fire suppression circuit pins 11 and 12 on the OEM Interface wiring harness connector (mating to the C.I.B). Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms? **YES** | 2A |
> | Less than 10 ohms? **NORepair:** An open in the fire suppression circuit has been detected. Repair the OEM interface wiring harness and interconnects. Refer to Procedure 015-104 in Section 15. | Repair complete. |  |
>
> #### STEP 1C. Check for ECM fault codes.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for active fault codes. Use INSITE™ electronic service tool to read the fault codes. | Active fault codes on ECM? **YES** | Go to the appropriate fault code troubleshooting tree. |
> | Active fault codes on ECM? **NO** | Refer to Engine Difficult To Start Or Will **Not** Start troubleshooting symptom tree in Section TS in the appropriate service manual. |  |
