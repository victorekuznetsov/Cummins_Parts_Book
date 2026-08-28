---
aliases:
  - "Код 2185 — цепь питания датчиков 4 — напряжение выше нормы"
type: "Процедура"
doc: "123-t05-2185"
title_en: "FAULT CODE 2185 - Sensor Supply 4 Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Код 2185 — цепь питания датчиков 4 — напряжение выше нормы"
modified: "2026-02-06"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4022094"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-2185.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/123-t05-2185.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
  - "перевод/машинный"
---

# FAULT CODE 2185 - Sensor Supply 4 Circuit - Voltage Above Normal or Shorted to High Source
**Код 2185 — цепь питания датчиков 4 — напряжение выше нормы**

> [!abstract] Процедура · `123-t05-2185`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2026-02-06
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-2185.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/123-t05-2185.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
> Чтобы уменьшить вероятность повреждения новой ECM, все другие активные коды неисправностей должны быть исследованы до замены ECM.

> [!warning] ОСТОРОЖНО
> Чтобы не повредить контакты и жгут, при измерениях пользуйтесь следующими измерительными проводами: Номер детали 3164133 — пробный щуп типа пробки DeutschTM/AMPTM/Metri-PackTM, номер детали 3822758 — пробный щуп типа пробки DeutschTM/AMPTM/Metri-PackTM, а номер детали 3822917 — пробный щуп типа пробки гнездовой пробки DeutschTM/AMPTM/Metri-PackTM.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте коды неисправностей. |  |
|  | **STEP 1A.** Проверить наличие активного кода неисправности. | Код ошибки 2185 активен? |
| ШАГ 2. | Проверьте ECM и электропроводку двигателя. |  |
|  | **STEP 2A.** Проверить контакты разъема электропроводки и электропроводки двигателя. | Грязные или поврежденные контакты? |
|  | **STEP 2B.** Проверьте реакцию ECM. | Код ошибки 2185 активен? |
| ШАГ 3. | Сбросьте коды неисправностей. |  |
|  | **STEP 3A.** Отключить код ошибки. | Код 2185 неактивен? |
|  | **STEP 3B.** Очистить коды неактивных ошибок. | Все коды неисправностей очищены? |

### ШАГ 1. Проверьте коды неисправностей.

#### ШАГ 1A. Проверьте активный код ошибки.

| **Условия:** Включите переключатель зажигания на электронном сервисном оборудовании Connect INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте активный код ошибки. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код ошибки 2185 активен? *Да | 2А |
| Код ошибки 2185 активен? **НЕТ** | Используйте следующую процедуру для неактивного или прерывистого кода неисправности.[[99-019-362 — Inactive or Intermittent Fault Code\|См. процедуру 019-362 в разделе 19.]] |  |

### ШАГ 2. Проверьте ECM и электропроводку двигателя.

#### ШАГ 2A. Проверьте контакты разъема ECM и проводов двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините разъем электропроводки ремня от разъема ECM 60-pin. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контактные линзы для проводов двигателя и разъёма датчика на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт: **В разъеме ECM или в ремне электропроводки двигателя обнаружено поврежденное соединение. Очистите разъем и булавки. См. схему или схему проводов для всех соединений проводов. Заменить поврежденный участок проводов двигателя ремнем. См. процедуру 019-043 в разделе 19. Заменить ECM. См. процедуру 019-031 в разделе 19. | 3А |
| Грязные или поврежденные контакты? **НЕТ** | 2В |  |

#### ШАГ 2B. Проверьте реакцию ECM.

| **Условия:** Замок зажигания отключите от электропроводки двигателя от 60-контактного разъема ECM. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте соответствующий ответ на ECM через 30 секунд. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код ошибки 2185 активен? Заменить ЭКМ. См. процедуру 019-031 в разделе 19. | 3А |
| Код ошибки 2185 активен? **NORepair:** Заменить поврежденный участок жгута проводов двигателя.[[123-019-043 — Engine Wiring Harness\|См. процедуру 019-043 в разделе 19.]]См. схему или схему проводов для всех соединений проводов. | 3А |  |

### ШАГ 3. Сбросьте коды неисправностей.

#### ШАГ 3A. Отключите код неисправности.

| **Условия:** Подключить все компоненты Подключить электронный сервисный инструмент INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите код неисправности. Используйте инструмент электронного сервиса INSITETM для проверки неактивности кода ошибки. | Код 2185 неактивен? *Да | 3B |
| Код 2185 неактивен? **NORepair:** Возврат к шагам устранения неполадок или свяжитесь с авторизованным местом ремонта Cummins®, если все шаги были завершены и проверены снова. | 1А |  |

#### ШАГ 3B. Сбросьте неактивные коды неисправностей.

| **Условия:** Подключите все компоненты Включите переключатель зажигания ON Connect INSITETM электронный сервисный инструмент. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сбросьте неактивные коды неисправностей. Используйте инструмент электронного сервиса INSITETM для очистки кодов неактивных ошибок. | Все коды неисправностей очищены? *Да | Ремонт завершён |
| Все коды неисправностей очищены? **NORepair: **Устранение неполадок с оставшимися активными кодами неисправностей. | Соответствующие шаги по устранению неполадок |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
> To reduce the possibility of damaging a new ECM, all other active fault codes must be investigated prior to replacing the ECM.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3164133 - male Deutsch™/AMP™/Metri-Pack™ test lead, Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead, and Part Number 3822917 - female male Deutsch™/AMP™/Metri-Pack™ test lead.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the fault codes. |  |
> |  | **STEP 1A.** Check for an active fault code. | Fault Code 2185 active? |
> | STEP 2. | Check the ECM and engine harness. |  |
> |  | **STEP 2A.** Inspect the ECM and engine harness connector pins. | Dirty or damaged pins? |
> |  | **STEP 2B.** Check the ECM response. | Fault Code 2185 active? |
> | STEP 3. | Clear the fault codes. |  |
> |  | **STEP 3A.** Disable the fault code. | Fault Code 2185 inactive? |
> |  | **STEP 3B.** Clear the inactive fault codes. | All fault codes cleared? |
>
> ### STEP 1. Check the fault codes.
>
> #### STEP 1A. Check for an active fault code.
>
> | **Conditions:** Turn keyswitch ON Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an active fault code. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 2185 active? **YES** | 2A |
> | Fault Code 2185 active? **NO** | Use the following procedure for an inactive or intermittent fault code. [[99-019-362 — Inactive or Intermittent Fault Code\|Refer to Procedure 019-362 in Section 19.]] |  |
>
> ### STEP 2. Check the ECM and engine harness.
>
> #### STEP 2A. Inspect the ECM and engine harness connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM 60-pin connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and sensor connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the ECM connector or the engine harness. Clean the connector and pins. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of the engine harness. Refer to Procedure 019-043 in Section 19. Replace the ECM. Refer to Procedure 019-031 in Section 19. | 3A |
> | Dirty or damaged pins? **NO** | 2B |  |
>
> #### STEP 2B. Check the ECM response.
>
> | **Conditions:** Turn keyswitch OFF Disconnect the engine harness from the ECM 60-pin connector. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for the appropriate ECM response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 2185 active? **YESRepair:** Replace the ECM. Refer to Procedure 019-031 in Section 19. | 3A |
> | Fault Code 2185 active? **NORepair:** Replace the damaged section of the engine harness. [[123-019-043 — Engine Wiring Harness\|Refer to Procedure 019-043 in Section 19.]] Refer to the circuit diagram or wiring diagram for all harness interconnections. | 3A |  |
>
> ### STEP 3. Clear the fault codes.
>
> #### STEP 3A. Disable the fault code.
>
> | **Conditions:** Connect all components Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable the fault code. Use INSITE™ electronic service tool to verify the fault code is inactive. | Fault Code 2185 inactive? **YES** | 3B |
> | Fault Code 2185 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
>
> #### STEP 3B. Clear the inactive fault codes.
>
> | **Conditions:** Connect all components Turn keyswitch ON Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | Repair complete |
> | All fault codes cleared? **NORepair:** Troubleshoot any remaining active fault codes. | Appropriate troubleshooting steps |  |
