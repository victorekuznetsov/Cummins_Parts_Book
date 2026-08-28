---
aliases:
  - "Критический внутренний отказ ЭБУ — неисправное устройство"
type: "Процедура"
doc: "97-fc111aft"
title_en: "Engine Control Module Critical Internal Failure - Bad Intelligent Device or Component"
title_ru: "Критический внутренний отказ ЭБУ — неисправное устройство"
modified: "2004-10-15"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
  - "80141463"
  - "80248213"
families:
  - "QSM11"
  - "QSX15"
manuals:
  - "3666415"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc111aft.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc111aft.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
  - "перевод/машинный"
---

# Engine Control Module Critical Internal Failure - Bad Intelligent Device or Component
**Критический внутренний отказ ЭБУ — неисправное устройство**

> [!abstract] Процедура · `97-fc111aft`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-10-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc111aft.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc111aft.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 111 (Послепродажное обслуживание и OEM)

### Критический внутренний отказ ЭБУ — неисправное устройство

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 111 PID(P): СПН: ФМИ: Лампа: Нет, не srt: | Критический внутренний отказ ЭБУ — неисправное устройство. Ошибка, внутренняя для модуля управления ICONTM, связанная с аппаратными сбоями памяти или сбоями внутренней связи микропроцессора. | Система ICONTM будет отключена. Двигатель может **не** нормально завестись. Переключатель зажигания может работать **не** нормально. |

![[19802946.png]]

### Описание цепи

Модуль управления ICONTM idle — это компьютер, который управляет работой системы ICONTM.

### Расположение компонента

Модуль управления холостым ходом ICONTM обычно устанавливается на переборке транспортного средства на впускной стороне двигателя. Однако модуль ICONTM может быть расположен в другом месте в зависимости от применения транспортного средства.

### Практические замечания

Этот код неисправности может быть вызван только **внутренней проблемой модуля управления ICONTM. Ремонт **не возможен для модуля управления холостым ходом ICONTM.

Система ICONTM может отображать только текущий активный код неисправности. Если одновременно активируется более одного кода неисправности, система ICONTM выдает наиболее приоритетную ошибку. После того, как ошибка была исправлена, будет выброшена следующая активная ошибка.

Инструменты ICONTM могут отображать более одного активного и неактивного кода неисправности одновременно.

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
>

Чтобы избежать повреждения нового модуля управления бездействия ICONTM, все другие активные коды неисправностей должны быть исследованы до замены модуля управления бездействия ICONTM.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Считайте коды неисправностей. |  |
|  | **STEP 1A.** Используйте функцию вспышки неисправности или инструмент электронного сервиса ICONTM для считывания кодов неисправностей. | Код 111 неактивен |
| ШАГ 2. | Очистите код ошибки. |  |
|  | **STEP 2A.** Отключить код ошибки. | Код 111 неисправности обезврежен |

### ШАГ 1. Считайте коды неисправностей.

#### ШАГ 1A. Используйте функцию вспышки неисправности или инструмент электронного сервиса ICONTM для считывания кодов неисправностей.

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите электронный сервис ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
|  | Код 111 неактивен. Неактивные или прерывистые коды ошибок, процедура[[99-019-362 — Inactive or Intermittent Fault Code\|019-362]]. | 2А |
| Заменить модуль управления ICONTM idle. См. процедуру[[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Ремонт завершён |  |

### ШАГ 2. Очистите код ошибки.

#### ШАГ 2A. Отключите код неисправности.

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите электронный сервис ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Используйте инструмент электронного сервиса ICONTM для очистки кода неисправности. Цикл переключателя зажигания для проверки кода неисправности неактивен. | Код 111 неисправности обезврежен | Ремонт завершён |
| Устранение неполадок с оставшимися активными кодами неисправностей. | Соответствующие диаграммы устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 111 (Aftermarket and OEM)
>
> ### Engine Control Module Critical Internal Failure - Bad Intelligent Device or Component
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 111 PID(P): SPN: FMI: Lamp: None SRT: | Engine Control Module Critical Internal Failure - Bad Intelligent Device or Component. Error internal to the ICON™ idle control module related to memory hardware failures or internal microprocessor communication failures. | The ICON™ system will be disabled. Engine will possibly **not** start normally. Keyswitch can possibly **not** operate normally. |
>
> ### Circuit Description
>
> The ICON™ idle control module is a computer that controls the operation of the ICON™ system.
>
> ### Component Location
>
> The ICON™ idle control module is typically mounted on the vehicle bulkhead on the intake side of the engine. However, the ICON™ module can be located in a different location depending on the vehicle application.
>
> ### Shoptalk
>
> This fault code can be caused **only** by an internal ICON™ idle control module problem. Repairs are **not** possible for the ICON™ idle control module.
>
> The ICON™ system can display **only** the present active fault code. If more than one fault code is active at the same time, the ICON™ system flashes out the highest priority fault. After the fault has been corrected then the next active fault will be flashed out.
>
> The ICON™ electronic service tool can display more than one active and or inactive fault codes at the same time.
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
>
> **To avoid damaging a new ICON™ idle control module, all other active fault codes must be investigated prior to replacing the ICON™ idle control module.**
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Read the fault codes. |  |
> |  | **STEP 1A.** Use the fault flashout feature or the ICON™ electronic service tool to read the fault codes. | Fault Code 111 inactive |
> | STEP 2. | Clear the fault code. |  |
> |  | **STEP 2A.** Disable the fault code. | Fault Code 111 cleared |
>
> ### STEP 1. Read the fault codes.
>
> #### STEP 1A. Use the fault flashout feature or the ICON™ electronic service tool to read the fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect the ICON™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> |  | Fault Code 111 inactive. Refer to Inactive or Intermittent Fault Codes, Procedure [[99-019-362 — Inactive or Intermittent Fault Code\|019-362]]. | 2A |
> | Replace the ICON™ idle control module. Refer to Procedure [[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Repair complete |  |
>
> ### STEP 2. Clear the fault code.
>
> #### STEP 2A. Disable the fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect the ICON™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Use the ICON™ electronic service tool to clear the fault code. Cycle the keyswitch to verify the fault code is inactive. | Fault Code 111 cleared | Repair complete |
> | Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
