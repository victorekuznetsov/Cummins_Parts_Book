---
aliases:
  - "Код 173 — заклинивание рейки управления подачей"
type: "Процедура"
doc: "87-t05-173"
title_en: "FAULT CODE 173 - Fuel Control Rack Stuck"
title_ru: "Код 173 — заклинивание рейки управления подачей"
modified: "2018-08-14"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-t05-173.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-t05-173.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# FAULT CODE 173 - Fuel Control Rack Stuck
**Код 173 — заклинивание рейки управления подачей**

> [!abstract] Процедура · `87-t05-173`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2018-08-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-t05-173.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-t05-173.pdf)

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
| ШАГ 1. | Проверьте наличие активных кодов неисправностей. |  |
|  | **СТЭП 1А.** Прочитайте коды неисправностей. | Код 166 Active |
| ШАГ 2. | Сбросьте коды неисправностей. |  |
|  | **STEP 2A.** Отключить код ошибки. | Код 173 неактивен |
|  | **STEP 2B.** Очистить коды неактивных ошибок. | Все коды ошибок очищены |

### ШАГ 1. Проверьте наличие активных кодов неисправностей.

#### ШАГ 1A. Считайте коды неисправностей.

| **Условия:** Включить переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Считайте коды неисправностей. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 166 Active | Код ошибки 166 |
| Замените топливный насос. См. процедуру 005-012 в разделе 5. | 2А |  |

### ШАГ 2. Сбросьте коды неисправностей.

#### ШАГ 2A. Отключите код неисправности.

| **Условия: **Соединить все компоненты. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключить код ошибки. Запустите двигатель и запускайте его на холостом ходу в течение 1 минуты. Используйте инструмент электронного сервиса INSITETM для проверки вины. | Код 173 неактивен | 2В |
| Убедитесь, что все шаги были завершены. Если все шаги выполнены, то следуйте процессу технической эскалации. | Эскалация или призыв к помощи. |  |

#### ШАГ 2B. Сбросьте неактивные коды неисправностей.

| **Условия: **Соединить все компоненты. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сбросьте неактивные коды неисправностей. Используйте инструмент электронного сервиса INSITETM для очистки кодов неактивных ошибок. | Все коды ошибок очищены | Ремонт завершён |
| Устранение неполадок с оставшимися активными кодами неисправностей. | Соответствующие диаграммы устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check for active fault codes. |  |
> |  | **STEP 1A.** Read the fault codes. | Fault Code 166 active |
> | STEP 2. | Clear the fault codes. |  |
> |  | **STEP 2A.** Disable the fault code. | Fault Code 173 inactive |
> |  | **STEP 2B.** Clear the inactive fault codes. | All fault codes cleared |
>
> ### STEP 1. Check for active fault codes.
>
> #### STEP 1A. Read the fault codes.
>
> | **Conditions:** Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Read the fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 166 active | Fault Code 166 |
> | Replace the fuel pump. Refer to Procedure 005-012 in Section 5. | 2A |  |
>
> ### STEP 2. Clear the fault codes.
>
> #### STEP 2A. Disable the fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable fault code. Start the engine and let it idle for 1 minute. Use INSITE™ electronic service tool to verify that the fault. | Fault Code 173 inactive | 2B |
> | Verify that all steps have been completed. If all steps have been completed, then follow the technical escalation process. | Escalate or call for assistance. |  |
>
> #### STEP 2B. Clear the inactive fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared | Repair complete |
> | Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
