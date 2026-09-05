---
type: "Процедура"
doc: "513-t02-7414"
title_en: "ED-4 Source Address Conflict on Network"
modified: "2019-10-25"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-7414.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-7414.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
  - "перевод/машинный"
---

# ED-4 Source Address Conflict on Network

> [!abstract] Процедура · `513-t02-7414`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-10-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-7414.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-7414.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Код тревоги 7414.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения симптомов сети контроллеров (CAN). Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Возможные причины включают:

- Оригинальный производитель оборудования (OEM) устройство в сети

- Адрес источника ED-4.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте дисплей ED-4 |  |
|  | **STEP 1A.** Проверьте программное обеспечение ED-4. | Последний файл личности судна (VPF) и программное обеспечение установлены? |
|  | **STEP 1B.** Проверьте конфигурацию в ED-4. | Дисплей ED-4 установлен правильно? |
|  | **STEP 1C** Проверьте устройство OEM. | Код тревоги 7414 активен? |

### ШАГ 1. Проверьте дисплей ED-4.

#### ШАГ 1A. Проверьте программное обеспечение ED-4.

| **Условия:** Система включения включает включение. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте, что последняя версия VPF загружена на дисплее. См. процедуру 015-044 в разделе 15. Проверьте, что новейшее программное обеспечение отображения загружается на дисплей ED-4. См. процедуру 015-107 в разделе 15. | Последние установленные VPF и программное обеспечение? *Да | 1В |
| Последние установленные VPF и программное обеспечение? **NORepair:** Скачать правильный файл личности судна на дисплей от Cummins QuickServe® Online.[[513-015-044 — Managing Vessel Personalities\|См. процедуру 015-044 в разделе 15.]]Скачайте последнюю версию программного обеспечения для отображения из Cummins QuickServe® Online.[[513-015-107 — Display Software\|См. процедуру 015-107 в разделе 15.]] | Ремонт завершён. |  |

#### ШАГ 1B. Проверьте конфигурацию в ED-4.

| **Условия:** Система включения включает включение. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить адрес источника всех дисплеев ED-4 в сети. См. процедуру 015-108 в разделе 15. | Дисплей ED-4 установлен правильно? *Да | 1С |
| Дисплей ED-4 установлен правильно? **NORepair: **На дисплее ED-4 обнаружена неправильная настройка. Выберите адрес источника.[[513-015-108 — Display Configuration\|См. процедуру 015-108 в разделе 15.]] | Ремонт завершён. |  |

#### ШАГ 1C. Проверьте OEM-устройство.

| **Условия:** Система поворота позволяет выключать выключатель. Удалите OEM-устройство из сети. Система включения включает переключатель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Подожди 30 секунд. Прочитайте дисплеи ED-4. | Код тревоги 7414 активен? Запросить инженера по морским приложениям Cummins® на месте. | Ремонт завершён. |
| Код тревоги 7414 активен? **NORepair:** Проверить, что адрес источника OEM-устройства установлен неправильно. См. сервисную документацию изготовителя оборудования. | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - Alarm Code 7414 is displayed.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot controller area network (CAN) symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> Possible causes include:
>
> - Original equipment manufacturer (OEM) device on network
>
> - ED-4 source address.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the ED-4 display |  |
> |  | **STEP 1A.** Check ED-4 software. | Latest vessel personality file (VPF) and software installed? |
> |  | **STEP 1B.** Check configuration in ED-4 setup. | ED-4 displays setup correctly? |
> |  | **STEP 1C.** Check the OEM device. | Alarm Code 7414 active? |
>
> ### STEP 1. Check the ED-4 display.
>
> #### STEP 1A. Check ED-4 software.
>
> | **Conditions:** Turn system enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify latest VPF is downloaded in the display. Refer to Procedure 015-044 in Section 15. Verify the latest display software is downloaded in the ED-4 display. Refer to Procedure 015-107 in Section 15. | Latest VPF and software installed? **YES** | 1B |
> | Latest VPF and software installed? **NORepair:** Download correct vessel personality file to the display from Cummins QuickServe® Online. [[513-015-044 — Managing Vessel Personalities\|Refer to Procedure 015-044 in Section 15.]] Download latest version of the display software from Cummins QuickServe® Online. [[513-015-107 — Display Software\|Refer to Procedure 015-107 in Section 15.]] | Repair complete. |  |
>
> #### STEP 1B. Check configuration in ED-4 setup.
>
> | **Conditions:** Turn system enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify the source address of all ED-4 displays on the network. Refer to Procedure 015-108 in Section 15. | ED-4 displays setup correctly? **YES** | 1C |
> | ED-4 displays setup correctly? **NORepair:** An incorrect setup has been detected in the ED-4 display. Select the source address. [[513-015-108 — Display Configuration\|Refer to Procedure 015-108 in Section 15.]] | Repair complete. |  |
>
> #### STEP 1C. Check the OEM device.
>
> | **Conditions:** Turn system enable switch OFF. Remove the OEM device from the network. Turn system enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Wait 30 seconds. Read the ED-4 display. | Alarm code 7414 active? **YESRepair:** Request a Cummins® Marine Application Engineer on site. | Repair complete. |
> | Alarm code 7414 active? **NORepair:** Verify the OEM device source address is setup incorrectly. See equipment manufacturer service information. | Repair complete. |  |
