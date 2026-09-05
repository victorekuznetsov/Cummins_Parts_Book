---
type: "Процедура"
doc: "81-t05-622"
title_en: "FAULT CODE 622 - Exhaust Gas Temperature Deviation Low for Cylinder 3 - Data Valid But Below Normal Operating Range - Least Severe Level"
modified: "2014-06-03"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
manuals:
  - "3666410"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-t05-622.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-t05-622.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/81"
  - "перевод/машинный"
---

# FAULT CODE 622 - Exhaust Gas Temperature Deviation Low for Cylinder 3 - Data Valid But Below Normal Operating Range - Least Severe Level

> [!abstract] Процедура · `81-t05-622`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[3666410 — QSK45 and QSK60 CENSE™ Electronic Control System Troubleshooting and Repair Manual|3666410]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2014-06-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-t05-622.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-t05-622.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте точность схемы цилиндра 3 датчика температуры выхлопных газов. |  |
|  | **STEP 1A.** Проверить точность схемы цилиндра 3 датчика температуры выхлопных газов. | Измерение температуры инфракрасного термометра в пределах 15 процентов от температуры выхлопного газа датчик схемы цилиндра 1 считывания с помощью электронного сервисного инструментария INSITETM? |
| ШАГ 2. | Очистите код ошибки. |  |
|  | **STEP 2A.** Отключить код ошибки. | Код 622 неактивен? |
|  | **STEP 2B.** Очистить коды неактивных ошибок. | Все коды неисправностей очищены? |

### ШАГ 1. Проверьте точность схемы цилиндра 3 датчика температуры выхлопных газов.

#### ШАГ 1A. Проверьте точность схемы цилиндра 3 датчика температуры выхлопных газов.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте точность схемы цилиндра 3 датчика температуры выхлопных газов с помощью инфракрасного термометра. Запускай двигатель. Подключите инструмент электронного сервиса INSITETM. Используйте инфракрасный термометр для измерения и записи температуры поверхности на стороне выхлопного порта головки цилиндра. Сравните измерение температуры инфракрасного термометра с датчиком температуры выхлопных газов цилиндром 3 считывания на экране монитора электронного сервисного инструментария INSITETM. | Измерение температуры инфракрасного термометра в пределах 15 процентов от температуры выхлопного газа датчик схемы цилиндра 1 считывания с помощью электронного сервисного инструментария INSITETM? **Ремонт:** Необходимо исследовать возможные повреждения цилиндров или топливных форсунок. | Дерево диагностики мощностных характеристик |
| Измерение температуры инфракрасного термометра в пределах 15 процентов от температуры выхлопного газа датчик схемы цилиндра 1 считывания с помощью электронного сервисного инструментария INSITETM? **NORepair:** Был обнаружен неисправный датчик температуры выхлопных газов в цилиндре 3 схемы. Заменить датчик температуры выхлопных газов на цилиндр 3 схемы. См. процедуру 019-013 в разделе 19. | 2А |  |

### ШАГ 2. Сбросьте коды неисправностей.

#### ШАГ 2A. Отключите код неисправности.

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите код неисправности. Используйте инструмент электронного сервиса INSITETM для проверки неактивности кода ошибки. | Код 622 неактивен? *Да | 2В |
| Код 622 неактивен? **NORepair:** Возврат к шагам устранения неполадок или свяжитесь с авторизованным местом ремонта Cummins®, если все шаги были завершены и проверены снова. | 1А |  |

#### ШАГ 2B. Сбросьте неактивные коды неисправностей.

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сбросьте неактивные коды неисправностей. Используйте инструмент электронного сервиса INSITETM для очистки любых неактивных кодов неисправностей. | Все коды неисправностей очищены? *Да | Ремонт завершён |
| Все коды неисправностей очищены? **НЕТ** | Соответствующие шаги по устранению неполадок |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the exhaust gas temperature sensor circuit cylinder 3 accuracy. |  |
> |  | **STEP 1A.** Verify the exhaust gas temperature sensor circuit cylinder 3 accuracy. | Temperature measurement from the infrared thermometer within 15 percent of the exhaust gas temperature sensor circuit cylinder 1 reading with INSITE™ electronic service tool? |
> | STEP 2. | Clear the fault code. |  |
> |  | **STEP 2A.** Disable the fault code. | Fault Code 622 inactive? |
> |  | **STEP 2B.** Clear any inactive fault codes. | All fault codes cleared? |
>
> ### STEP 1. Check the exhaust gas temperature sensor circuit cylinder 3 accuracy.
>
> #### STEP 1A. Verify the exhaust gas temperature sensor circuit cylinder 3 accuracy.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify the exhaust gas temperature sensor circuit cylinder 3 accuracy with an infrared thermometer. Start the engine. Connect INSITE™ electronic service tool. Use an infrared thermometer to measure and record the surface temperature at the exhaust port side of the cylinder head. Compare the infrared thermometer temperature measurement with the exhaust gas temperature sensor circuit cylinder 3 reading on the INSITE™ electronic service tool monitor screen. | Temperature measurement from the infrared thermometer within 15 percent of the exhaust gas temperature sensor circuit cylinder 1 reading with INSITE™ electronic service tool? **YESRepair:** Possible cylinder or injector damage **must** be investigated. | Engine Performance Troubleshooting Tree |
> | Temperature measurement from the infrared thermometer within 15 percent of the exhaust gas temperature sensor circuit cylinder 1 reading with INSITE™ electronic service tool? **NORepair:** A faulty exhaust gas temperature sensor circuit cylinder 3 has been detected. Replace the exhaust gas temperature sensor circuit cylinder 3. Refer to Procedure 019-013 in Section 19. | 2A |  |
>
> ### STEP 2. Clear the fault codes.
>
> #### STEP 2A. Disable the fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable the fault code. Use INSITE™ electronic service tool to verify the fault code is inactive. | Fault Code 622 inactive? **YES** | 2B |
> | Fault Code 622 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
>
> #### STEP 2B. Clear the inactive fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Clear the inactive fault codes. Use INSITE™ electronic service tool to clear any inactive fault codes. | All fault codes cleared? **YES** | Repair complete |
> | All fault codes cleared? **NO** | Appropriate troubleshooting steps |  |
