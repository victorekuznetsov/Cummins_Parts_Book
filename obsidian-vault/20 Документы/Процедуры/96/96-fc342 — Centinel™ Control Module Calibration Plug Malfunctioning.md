---
aliases:
  - "Неисправность калибровочной перемычки блока Centinel™"
type: "Процедура"
doc: "96-fc342"
title_en: "Centinel™ Control Module Calibration Plug Malfunctioning"
title_ru: "Неисправность калибровочной перемычки блока Centinel™"
modified: "2004-02-25"
engines:
  - "37292556"
  - "37295879"
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
  - "QST30"
manuals:
  - "3666231"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-fc342.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/96-fc342.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "двигатель/QST30"
  - "группа/96"
  - "перевод/машинный"
---

# Centinel™ Control Module Calibration Plug Malfunctioning
**Неисправность калибровочной перемычки блока Centinel™**

> [!abstract] Процедура · `96-fc342`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11, QST30
> **Входит в руководства:** [[3666231 — Centinel™ Master Repair Manual|3666231]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-02-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-fc342.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/96-fc342.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 342

### Неисправность калибровочной перемычки блока Centinel™

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 342 P(P): СПН: ФМИ: Лампа: СТО: | CentinelTM Control Module Calibration Plug Неисправный тяжелый модуль: Не установлена калибровочная пробка. Высоколошадные: Сервисный плагин был **не** удален. | Система CentinelTM будет работать некорректно. |

![[05100039.png]]

### Описание цепи

Калибровочная пробка необходима для двигателей большой мощности.

### Расположение компонента

Тяжелая сыпь: Калибровочная пробка представляет собой 3-контактный разъем, который расположен на модуле управления CentinelTM.

Высоколошадные: Сервисная вилка представляет собой 3-контактный разъем в электропроводке упряжки рядом со световым ящиком.

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
>

Чтобы избежать повреждения штифта и проводов, используйте следующий испытательный щуп при проведении измерений: Испытательный щуп Male Cannon, Metri-Pack и Deutsch, Испытательный щуп Part Number 3822758 Female AMP, Metri-Pack и Deutsch, Испытательный щуп Part Number 3822917 Male Deutsch, Испытательный щуп Part Number 3823993 Female Deutsch, Часть Number 3823994.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте калибровочную пробку. |  |
|  | **STEP 1A.** Проверить калибровочную пробку. | Установите калибровочную вилку |
|  | **STEP 1B.** Проверьте наличие открытого отверстия в калибровочной пробке. | Менее 10 Ом |
| ШАГ 2. | Проверьте проводную упряжку CentinelTM. |  |
|  | **ШАГ 2А.** Проверить наличие открытой цепи. | Менее 10 Ом |
|  | **ШАГ 2В.** Проверить короткое замыкание на землю. | Более 1к Ом |
| ШАГ 3. | Сбросьте коды неисправностей. |  |
|  | **STEP 3A.** Отключить код ошибки. | Код 342 неактивен |

### ШАГ 1. Проверьте калибровочную пробку.

#### ШАГ 1A. Проверьте, установлена ли калибровочная пробка.

| **Условия:** Выключите замок зажигания. Удалён сервисный штепсель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить калибровочную пробку. | Калибровочная пробка устанавливается на сверхмощных. Сервисный плагин не устанавливается на высокой мощности. | 1В |
| **Тяжелый-долговатый: Установите калибровочный плагин High-Horsepower: Удалить плагин сервиса.** | 3А |  |

#### ШАГ 1B. Проверьте наличие открытого в калибровочной вилке.

| **Условия:** Выключите замок зажигания. Удалите калибровочную пробку из модуля управления CentinelTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Только для тяжелых: Измерьте сопротивление между контактами, которые связаны. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Менее 10 Ом | 2А |
| **Ремонт или замена калибровочной пробки** | 3А |  |

### ШАГ 2. Проверьте проводную упряжку CentinelTM.

#### ШАГ 2A. Проверьте цепь на обрыв.

| **Условия:** Тяжелая доза **только**: Выключите замок зажигания. Отсоедините проводную упряжку CentinelTM от модуля управления CentinelTM. Удалите калибровочную пробку из модуля управления CentinelTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление от контакта 7 12-контактного разъема модуля управления CentinelTM к контакту B 3-контактного разъема калибровочной пробки. См. схему проводов для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Менее 10 Ом | 2В |
| **Заменить модуль управления CentinelTM.**См. процедуру[[96-019-130-tr — Centinel™ Control Module\|019-130]]. | 3А |  |

#### ШАГ 2B. Проверьте короткое замыкание на землю.

| **Условия:** Тяжелопрочный**только**: Выключите замок зажигания. Удалите калибровочную пробку из проводной упряжки CentinelTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление от контакта В 3-контактной калибровочной пробки (со стороны модуля) к контактам А и С. См. схему проводов для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 1к Ом | 2D |
| **Заменить проводную упряжку CentinelTM**См. процедуру[[96-019-131-tr — Centinel™ Wiring Harness\|019-131]]. | 3А |  |

### ШАГ 3. Сбросьте коды неисправностей.

#### ШАГ 3A. Отключите код неисправности.

| **Условия:** Соедините все компоненты. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Запустите двигатель и запускайте его на холостом ходу в течение 1 минуты. Убедитесь, что код 342 неактивен. | Код 342 неактивен | Полный комплект |
| Вернитесь к шагам устранения неполадок или свяжитесь с вашим местным авторизованным ремонтным центром Cummins, если все шаги были завершены и проверены снова. | 1А |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 342
>
> ### Centinel™ Control Module Calibration Plug Malfunctioning
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 342 PID(P): SPN: FMI: Lamp: SRT: | Centinel™ Control Module Calibration Plug Malfunctioning Heavy-Duty: no calibration plug installed. High-Horsepower: service plug was **not** removed. | The Centinel™ system will **not** operate properly. |
>
> ### Circuit Description
>
> The calibration plug is necessary for heavy-duty engines.
>
> ### Component Location
>
> Heavy-Duty: The calibration plug is a 3-pin connector that is located on the Centinel™ control module.
>
> High-Horsepower: The service plug is a 3-pin connector in the wiring harness near the light box.
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
>
> **To avoid pin and harness damage, use the following test leads when taking measurements: Male Cannon, Metri-Pack, and Deutsch test lead, Part Number 3822758 Female AMP, Metri-Pack, and Deutsch test lead, Part Number 3822917 Male Deutsch test lead, Part Number 3823993 Female Deutsch test lead, Part Number 3823994.**
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check calibration plug. |  |
> |  | **STEP 1A.** Verify calibration plug is installed. | Install the calibration plug |
> |  | **STEP 1B.** Check for an open in the calibration plug. | Less than 10 ohms |
> | STEP 2. | Check the Centinel™ harness. |  |
> |  | **STEP 2A.** Check for an open circuit. | Less than 10 ohms |
> |  | **STEP 2B.** Check for a short circuit to ground. | More than 1k ohms |
> | STEP 3. | Clear the fault codes. |  |
> |  | **STEP 3A.** Disable the fault code. | Fault Code 342 inactive |
>
> ### STEP 1. Check the calibration plug.
>
> #### STEP 1A. Verify calibration plug is installed.
>
> | **Conditions:** Turn the keyswitch OFF. Service plug removed. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect calibration plug. | Calibration plug is installed on heavy-duty. Service plug is not installed on high-horsepower. | 1B |
> | **Heavy-Duty: install the calibration plugHigh-Horsepower: remove the service plug.** | 3A |  |
>
> #### STEP 1B. Check for an open in the calibration plug.
>
> | **Conditions:** Turn the keyswitch OFF. Remove the calibration plug from the Centinel™ control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Heavy-Duty only: measure the resistance between pins that are connected. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 10 ohms | 2A |
> | **Repair or replace the calibration plug** | 3A |  |
>
> ### STEP 2. Check the Centinel™ wiring harness.
>
> #### STEP 2A. Check for an open circuit.
>
> | **Conditions:** Heavy-Duty **only**: Turn the keyswitch OFF. Disconnect the Centinel™ harness from the Centinel™ control module. Remove the calibration plug from the Centinel™ control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 7 of the 12-pin Centinel™ control module connector to pin B of the 3-pin calibration plug connector. Refer to the wiring diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 10 ohms | 2B |
> | **Replace the Centinel™ control module.** Refer to Procedure [[96-019-130-tr — Centinel™ Control Module\|019-130]]. | 3A |  |
>
> #### STEP 2B. Check for a short circuit to ground.
>
> | **Conditions:** Heavy-duty **only**: Turn the keyswitch OFF. Remove the calibration plug from the Centinel™ harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin B of the 3-pin calibration plug (module side) to pins A and C. Refer to the wiring diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 1k ohms | 2D |
> | **Replace the Centinel™ wiring harness** Refer to Procedure [[96-019-131-tr — Centinel™ Wiring Harness\|019-131]]. | 3A |  |
>
> ### STEP 3. Clear the fault codes.
>
> #### STEP 3A. Disable the fault code.
>
> | **Conditions:** Connect all the components. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Start the engine and let it idle for 1 minute. Verify that Fault Code 342 is inactive. | Fault Code 342 inactive | Complete |
> | Return to troubleshooting steps or contact your local Cummins Authorized Repair Location if all the steps have been completed and checked again. | 1A |  |
