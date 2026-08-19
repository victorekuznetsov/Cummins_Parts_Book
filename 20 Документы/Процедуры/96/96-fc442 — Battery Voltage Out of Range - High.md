---
aliases:
  - "Напряжение АКБ выше диапазона"
type: "Процедура"
doc: "96-fc442"
title_en: "Battery Voltage Out of Range - High"
title_ru: "Напряжение АКБ выше диапазона"
modified: "2004-02-25"
engines:
  - "37292556"
  - "37295879"
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
  - "QST30"
manuals:
  - "3666231"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-fc442.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/96-fc442.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "двигатель/QST30"
  - "группа/96"
  - "перевод/машинный"
---

# Battery Voltage Out of Range - High
**Напряжение АКБ выше диапазона**

> [!abstract] Процедура · `96-fc442`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11, QST30
> **Входит в руководства:** [[3666231 — Centinel™ Master Repair Manual|3666231]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-02-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-fc442.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/96-fc442.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 442

### Напряжение АКБ выше диапазона

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 442 P(P): СПН: ФМИ: Лампа: Красная СТО: | Напряжение АКБ выше диапазона. Напряжение батареи больше, чем высокий порог, обнаруженный модулем управления CentinelTM. | Напряжение блока управления CentinelTM приближается к уровню, при котором произойдет непредсказуемая работа. |

![[05800058.png]]

### Описание цепи

Модуль управления CentinelTM получает от стартера напряжение невыключенной батареи для большой мощности. Для высокой мощности модуль управления CentinelTM получает переключенную мощность от соленоида запорного клапана топлива. В модуле управления CentinelTM установлены два встроенных 5-амперных предохранителя для защиты модуля управления CentinelTM. Высокая мощность имеет ** только один 5-амперный предохранитель. Провода возврата батареи в ремне проводов двигателя подключены к заземлению блока двигателя.

### Расположение компонента

Расположение батареи будет варьироваться в зависимости от OEM. См. руководство OEM для определения местоположения батареи.

### Практические замечания

Эта неисправность может быть вызвана рыхлыми или разъединенными соединениями батареи.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте систему батарей оборудования. |  |
|  | **STEP 1A.** Проверить соединения кабеля аккумулятора. | Нет поврежденных соединений |
|  | **ШАГ 1В.** Проверьте напряжение батареи. | Тяжелая работа: 9-32 VDC 12-VDC Высокомощные: 8.2 - 17.3 VDC 24-VDC Высокомощные: 15.5 - 30.3 VDC |
|  | **STEP 1C** Проверьте напряжение аккумулятора модуля управления CentinelTM. |  |
| ШАГ 2. | Очистите код ошибки. |  |
|  | **STEP 2A.** Отключить код ошибки. | Код 442 неактивен |

### ШАГ 1. Проверьте систему батарей оборудования.

#### ШАГ 1A. Проверьте соединения кабеля батареи.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Коррозионно-розовая связь. | Нет поврежденных соединений | 1В |
| ** Ремонт или замена поврежденных соединений** Ремонт аккумулятора или стартерных соединений. Замените аккумулятор или стартовые соединения. См. сервисное руководство изготовителя машины. | 2А |  |

#### ШАГ 1B. Проверьте напряжение батареи.

| **Условия:** Включить переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Измерьте напряжение батареи. | Тяжелая работа: 9 - 32 VDC 12VDC Высокомощные: 8.2 - 17.3 VDC 24VDC Высокомощные: 15.5 - 30.3 VDC | 1С |
| ** Заменить батарею.** См. руководство по обслуживанию OEM. | 2А |  |

#### ШАГ 1C. Проверьте напряжение аккумулятора модуля управления CentinelTM.

| **Условия:** Включить переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Тяжелая работа: Измерить напряжение между контактами 1 (+) и 2 (-) разъёма управляющего модуля CentinelTM. Высокая мощность: Измерить напряжение между контактами 22 (+) и 25 (-) разъема модуля управления CentinelTM. | Чтение должно соответствовать шагу 1В. | Полный комплект |
| ** Заменить проводную упряжку CentinelTM.** См. процедуру[[96-019-131-tr — Centinel™ Wiring Harness\|019-131]]. | 2А |  |

### ШАГ 2. Очистите код ошибки.

#### ШАГ 2A. Отключите код неисправности.

| **Условия: ** Соедините все компоненты. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Подключите все компоненты. Запустите двигатель и запускайте его на холостом ходу в течение 1 минуты. Убедитесь, что код 442 неактивен. | Код 442 неактивен | Полный комплект |
| Вернитесь к этапу устранения неполадок или свяжитесь с вашим местным авторизованным ремонтным центром Cummins, если все этапы были завершены и проверены снова. | 1А |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 442
>
> ### Battery Voltage Out of Range - High
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 442 PID(P): SPN: FMI: Lamp: Red SRT: | Battery Voltage Out of Range - High. Battery voltage is more than the high threshold detected by the Centinel™ control module. | The Centinel™ control module voltage supply approaching a level at which unpredictable operation will occur. |
>
> ### Circuit Description
>
> The Centinel™ control module receives unswitched battery voltage from the starter for heavy-duty. For high-horsepower, the Centinel™ control module receives switched power from the fuel shutoff valve solenoid. There are two in-line 5-amp fuses in the Centinel™ control module heavy-duty harness to protect the Centinel™ control module. The high-horsepower has **only** one 5-amp fuse. The battery return wires in the engine harness are connected to the engine block ground.
>
> ### Component Location
>
> The location of the battery will vary with the OEM. Refer to the OEM manual for the battery location.
>
> ### Shoptalk
>
> This fault can be caused by loose or corroded battery connections.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the equipment battery system. |  |
> |  | **STEP 1A.** Inspect the battery cable connections. | No damaged connections |
> |  | **STEP 1B.** Check the battery voltage. | Heavy-duty: 9 to 32 VDC 12-VDC High-horsepower: 8.2 - 17.3 VDC 24-VDC High-horsepower: 15.5 - 30.3 VDC |
> |  | **STEP 1C.** Check the Centinel™ control module battery voltage. |  |
> | STEP 2. | Clear the fault code. |  |
> |  | **STEP 2A.** Disable the fault code. | Fault Code 442 inactive |
>
> ### STEP 1. Check the equipment battery system.
>
> #### STEP 1A. Inspect the battery cable connections.
>
> | **Conditions:** Turn the keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Corrosion Loose connection. | No damaged connections | 1B |
> | **Repair or replace the damaged connections** Repair the battery or starter connections. Replace the battery or starter connections. Refer to the OEM service manual. | 2A |  |
>
> #### STEP 1B. Check the battery voltage.
>
> | **Conditions:** Turn the keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the battery voltage. | Heavy-duty: 9 - 32 VDC 12VDC High-horsepower: 8.2 - 17.3 VDC 24VDC High-horsepower: 15.5 - 30.3 VDC | 1C |
> | **Replace the battery.** Refer to the OEM service manual. | 2A |  |
>
> #### STEP 1C. Check the Centinel™ control module battery voltage.
>
> | **Conditions:** Turn the keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Heavy-duty: Measure the voltage between pins 1 (+) and 2 (-) of the Centinel™ control module harness connector. High-horsepower: Measure the voltage between pins 22 (+) and 25 (-) of the Centinel™ control module connector. | Reading must match Step 1B. | Complete |
> | **Replace the Centinel™ wiring harness.** Refer to Procedure [[96-019-131-tr — Centinel™ Wiring Harness\|019-131]]. | 2A |  |
>
> ### STEP 2. Clear the fault code.
>
> #### STEP 2A. Disable the fault code.
>
> | **Conditions:** Connect all the components. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Connect all the components. Start the engine and let it idle for 1 minute. Verify that Fault Code 442 is inactive. | Fault Code 442 inactive | Complete |
> | Return to the troubleshooting step or contact your local Cummins Authorized Repair Location if all the steps have been completed and checked again. | 1A |  |
