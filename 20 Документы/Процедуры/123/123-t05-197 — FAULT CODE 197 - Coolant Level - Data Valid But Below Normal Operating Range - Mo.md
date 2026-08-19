---
aliases:
  - "Код 197 — уровень ОЖ ниже нормы — умеренный уровень"
type: "Процедура"
doc: "123-t05-197"
title_en: "FAULT CODE 197 - Coolant Level - Data Valid But Below Normal Operating Range - Moderately Severe Level"
title_ru: "Код 197 — уровень ОЖ ниже нормы — умеренный уровень"
modified: "2015-03-10"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4022094"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-197.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-t05-197.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
  - "перевод/машинный"
---

# FAULT CODE 197 - Coolant Level - Data Valid But Below Normal Operating Range - Moderately Severe Level
**Код 197 — уровень ОЖ ниже нормы — умеренный уровень**

> [!abstract] Процедура · `123-t05-197`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-03-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-197.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-t05-197.pdf)

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
| ШАГ 1. | Проверьте коды неисправностей. |  |
|  | **СТЭП 1А.** Проверить код ошибки 197. | Активный или неактивный код 197. |
|  | **ШАГ 1В.** Проверьте наличие открытой цепи в электропроводке OEM. | Менее 10 Ом? |
|  | **STEP 1C.** Проверьте короткое замыкание в проводной упряжке OEM. | Больше 100 тысяч ом? |
| ШАГ 2. | Очистите код ошибки. |  |
|  | **STEP 2A.** Отключить код ошибки. | Код ошибки 197 неактивен? |
|  | **STEP 2B.** Очистить код неактивного отказа. | Все коды неисправностей очищены? |

### ШАГ 1. Проверьте коды неисправностей.

#### ШАГ 1A. Проверить код ошибки 197.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте коды неисправностей. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Активный или неактивный код 197. *Да** | 1В |
| Активный или неактивный код 197. ** НЕТ** | Ремонт завершён |  |

#### ШАГ 1B. Проверьте наличие открытой цепи в OEM-проводах.

| **Условия:** Выключите замок зажигания. Отсоедините разъём OEM-проводов от разъема ECM 60-pin порта. Отсоедините разъем датчика уровня охлаждающей жидкости двигателя от разъема OEM-проводов. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте цепь на обрыв. Измерить сопротивление между контактом питания охлаждающей жидкости уровня 1 5 вольт (сенсорная подачу 1) в разъёме 60-контактного порта OEM-проводов ECM и контактом подачи охлаждающей жидкости уровня 1 5 вольт (сенсорная подачу 1) в разъёме уровня охлаждающей жидкости двигателя OEM-проводов. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Менее 10 Ом? *Да** | 1С |
| Менее 10 Ом? **NORepair: ** В электропроводке OEM обнаружен открытый провод. Устранение неполадок в каждой секции проводов OEM, чтобы определить, которая содержит короткое контактное соединение. Проверьте все проводов, подключенные последовательно. Замените поврежденный участок ремня электропроводки двигателя или ремня электропроводки OEM. См. процедуру 019-071 в разделе 19. | 2А |  |

#### ШАГ 1C. Проверьте короткое замыкание контакт-контакт в электропроводке OEM.

| **Условия:** Выключите замок зажигания. Отсоедините проводку OEM от разъема порта ECM 60-pin. Отсоедините датчик уровня охлаждающей жидкости двигателя 1 от разъема OEM-проводов. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте цепь на обрыв. Измерьте сопротивление между уровнем 1 сигнала контакта охлаждающей жидкости двигателя с разъемом ECM проводов OEM и всеми другими штифтами в разъеме ECM проводов OEM. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Больше 100 тысяч ом? ** Ремонт: ** См. Дерево симптомов устранения неполадок при потере охлаждающей жидкости в QSK19, QSK19 CM850 MCRS и QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. Если код 197 по умолчанию активен, а уровень охлаждающей жидкости не является низким, вероятной причиной является неисправный датчик уровня охлаждающей жидкости. Смотрите руководство по обслуживанию OEM перед заменой датчика уровня охлаждающей жидкости. | Соответствующие шаги по устранению неполадок |
| Больше 100 тысяч ом? **NORepair:** В электропроводке OEM обнаружено короткое замыкание на проводе SIGNAL. Устранение неполадок в каждой секции проводов OEM, чтобы определить, которая содержит короткое замыкание контакта с контактом. Замените поврежденный участок ремня электропроводки двигателя или ремня электропроводки OEM. См. процедуру 019-071 в разделе 19. | Ремонт завершён |  |

### ШАГ 2. Очистить коды неисправностей

#### ШАГ 2A. Отключите код неисправности.

| **Условия: ** Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Отключите код неисправности. Используйте инструмент электронного сервиса INSITETM для проверки неактивности кода ошибки. | Код ошибки 197 неактивен? *Да** | 2В |
| Код ошибки 197 неактивен? **NORepair:** Возврат к шагам устранения неполадок или свяжитесь с авторизованным ремонтным центром Cummins®, если все шаги были завершены и проверены во второй раз. | 1А |  |

#### ШАГ 2B. Сбросьте неактивные коды неисправностей.

| **Условия: ** Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Сбросьте неактивные коды неисправностей. Используйте электронную службу INSITETM для очистки кодов неисправностей. | Все коды неисправностей очищены? *Да** | Ремонт завершён |
| Все коды неисправностей очищены? **NORepair: ** Устранение неполадок с оставшимися активными кодами неисправностей. | Соответствующие шаги по устранению неполадок |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the fault codes. |  |
> |  | **STEP 1A.** Check for Fault Code 197. | Active or inactive counts of Fault Code 197? |
> |  | **STEP 1B.** Check for an open circuit in the OEM harness. | Less than 10 ohms? |
> |  | **STEP 1C.** Check for a pin-to-pin short circuit in the OEM harness. | Greater than 100k ohms? |
> | STEP 2. | Clear the fault code. |  |
> |  | **STEP 2A.** Disable the fault code. | Fault Code 197 inactive? |
> |  | **STEP 2B.** Clear the inactive fault code. | All fault codes cleared? |
>
> ### STEP 1. Check the fault codes.
>
> #### STEP 1A. Check for Fault Code 197.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for fault codes. Use INSITE™ electronic service tool to read the fault codes. | Active or inactive counts of Fault Code 197? **YES** | 1B |
> | Active or inactive counts of Fault Code 197? **NO** | Repair complete |  |
>
> #### STEP 1B. Check for an open circuit in the OEM harness.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness connector from the ECM 60-pin port connector. Disconnect the engine coolant level sensor connector from the OEM harness connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an open circuit. Measure the resistance between the coolant level 1 5 volt (sensor supply 1) SUPPLY pin in the OEM harness ECM 60-pin port connector and the coolant level 1 5 volt supply (sensor supply 1) SUPPLY pin in the OEM harness engine coolant level sensor 1 connector. Refer to the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms? **YES** | 1C |
> | Less than 10 ohms? **NORepair:** An open SUPPLY wire has been detected in the OEM harness. Troubleshoot each section of the OEM harness to determine which contains the pin-to-pin short. Check all harnesses connected in series. Replace the damaged section of the engine harness or OEM harness. Refer to Procedure 019-071 in Section 19. | 2A |  |
>
> #### STEP 1C. Check for a pin-to-pin short circuit in the OEM harness.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ECM 60-pin port connector. Disconnect the engine coolant level sensor 1 from the OEM harness connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an open circuit. Measure the resistance between the engine coolant level 1 SIGNAL pin of the OEM harness ECM connector and all other pins in the OEM harness ECM connector. Refer to the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YESRepair:** See the Coolant Loss troubleshooting symptom tree in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. If Fault Code 197 is active and the coolant level is **not** low, a malfunctioning coolant level sensor is a likely cause. Refer to the OEM service manual before replacing the coolant level sensor. | Appropriate troubleshooting steps |
> | Greater than 100k ohms? **NORepair:** A pin-to-pin short circuit on the SIGNAL wire has been detected in the OEM harness. Troubleshoot each section of the OEM harness to determine which contains the pin-to-pin short circuit. Replace the damaged section of the engine harness or OEM harness. Refer to Procedure 019-071 in Section 19. | Repair complete |  |
>
> ### STEP 2. Clear the fault codes
>
> #### STEP 2A. Disable the fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable the fault code. Use INSITE™ electronic service tool to verify that the fault code is inactive. | Fault Code 197 inactive? **YES** | 2B |
> | Fault Code 197 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair location if all steps have been completed and checked a second time. | 1A |  |
>
> #### STEP 2B. Clear the inactive fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Clear the inactive fault codes. Use INSITE™ electronic service to clear the fault codes. | All fault codes cleared? **YES** | Repair complete |
> | All fault codes cleared? **NORepair:** Troubleshoot any remaining active fault codes. | Appropriate troubleshooting steps |  |
