---
type: "Процедура"
doc: "98-fc132as"
title_en: "Accelerator Position Sensor (Frequency Accelerator)"
modified: "2003-10-27"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc132as.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc132as.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Accelerator Position Sensor (Frequency Accelerator)

> [!abstract] Процедура · `98-fc132as`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2003-10-27
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc132as.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc132as.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 132-фа

### Датчик положения ускорителя (Frequency Accelerator)

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 132-фа PID (P): P91 SPN: ФМИ: 4 лампы: Флешинг SRT: 00-622 | Низкая частота обнаруженного на ускорителе положения сигнала контакта 18 главного провода двигателя с жгутом электронного модуля управления (ECM) разъема. | Потеря контроля ускорителя. Двигатель будет работать только на скорости 1250 об/мин. |

![[19802317.png]]

### Описание цепи

Генератор сигнала ускорителя обеспечивает команду акселератора водителя к ECM через OEM-проводку и главный двигатель. ECM использует этот сигнал для определения команды заправки электронного клапана управления топливом.

### Расположение компонента

Расположение генератора сигнала ускорителя варьируется в зависимости от каждого OEM. См. руководство по OEM.

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
>

**Для уменьшения возможности повреждения новой ЭКО необходимо изучить все другие активные коды неисправностей до замены ЭКО.**

> [!warning] ОСТОРОЖНО
>

**Для уменьшения возможности повреждения штифта и проводов жгута проводов используйте при проведении измерений следующий испытательный щуп: Номер детали 3822917 - пробный щуп типа сокетов Deutsch/AMP/Metri-Pack Номер детали 3823993 - пробный щуп типа пробок Deutsch Номер детали 3823994 - пробный щуп типа сокетов Deutsch.**

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте другие коды неисправностей. |  |
|  | **СТЭП 1А.** Прочитайте коды неисправностей. | Код 443 не зарегистрирован |
| ШАГ 2. | Проверьте OEM-проводку и генератор сигналов ускорителя. (Созданы следующие этапы для устранения общих неполадок OEM цепи OEM. Смотрите руководство OEM для более подробной информации. |  |
|  | **STEP 2A.** Проверить контакты разъема OEM и основной проводов двигателя. | Никаких поврежденных контактов |
|  | **ШАГ 2В.** Проверить наличие открытой цепи. | 800-1200 Ом |
|  | **ШАГ 2С.** Проверить короткое замыкание на землю. | Более 100 тыс. ом |
|  | **STEP 2D.** Проверьте короткое замыкание от пин-кодов до пин-кодов. | Более 100 тыс. ом |
| ШАГ 3. | Проверьте основную проводку двигателя. |  |
|  | **STEP 3A.** Осмотрите основные контакты с электропроводкой двигателя и разъемом ECM. | Никаких поврежденных контактов |
|  | **STEP 3B.** Проверьте наличие открытой цепи. | Менее 10 Ом |
|  | **ШАГ 3С.** Проверить короткое замыкание на землю. | Более 100 тыс. ом |
|  | **STEP 3D.** Проверьте короткое замыкание от пин-кодов до пин-кодов. | Более 100 тыс. ом |
| ШАГ 4. | Сбросьте коды неисправностей. |  |
|  | **STEP 4A.** Отключить код ошибки. | Код 132 неактивен |
|  | **STEP 4B.** Очистить коды неактивных ошибок. | Все коды ошибок очищены |

### ШАГ 1. Проверьте другие коды неисправностей.

#### ШАГ 1A. Считайте коды неисправностей.

| **Условия:** Включить переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Прочтите коды неисправностей с помощью CompulinkTM, Part Number 3823549; EchekTM, Part Number 3824437; или INSITETM, Part Number 3824638. | Код 443 не зарегистрирован | 2А |
| Устранение неисправностей Код 443. См. код ошибки 443 дерево устранения неполадок. | Соответствующая диаграмма устранения неполадок |  |

### ШАГ 2. Проверьте OEM-проводку и генератор сигналов ускорителя. (Созданы следующие этапы для устранения общих неполадок OEM цепи OEM. Смотрите руководство OEM для более подробной информации.

#### ШАГ 2A. Проверьте контакты разъема OEM и основной проводов двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините проводку OEM от основной проводов двигателя на разъеме C6. Промывайте и очищайте контакты разъема с помощью электронного контактного очистителя, номер детали 3824510. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Корродированные штифты Сгибаемые или сломанные штифты Отталкивающиеся или расширенные штифты Влажность в или на разъеме Пропавшие или поврежденные соединительные штифты Грязь или мусор в или на контактах разъема. | Никаких поврежденных контактов | 2В |
| Ремонт поврежденных контактов. Смой грязь, мусор или влагу из контактов разъема. Ремонт или замена основного электропроводного ремня или электропроводного ремня OEM, в зависимости от того, какие контакты повреждены. Смывать грязь, мусор или влагу с контактов разъема с помощью электронного контактного очистителя, номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт основной электропроводки двигателя. См. процедуру 019-043. Замените основную проводку двигателя. См. процедуру 019-043. Ремонт проводной упряжки OEM. См. руководство изготовителя машины по диагностике и ремонту. Замените проводку OEM. См. руководство изготовителя машины по диагностике и ремонту. | 4А |  |

#### ШАГ 2B. Проверьте цепь на обрыв.

| **Условия:** Выключите замок зажигания. Отсоедините проводку OEM от основной проводов двигателя на разъеме C6. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление от контакта E проводов OEM ремня С6 разъёма к контакту D проводов OEM ремня С6 разъёма. | 800-1200 Ом | 2C |
| Ремонт или замена OEM-проводов или генератора сигнала ускорителя, в зависимости от того, какая из них имеет открытую цепь. Ремонт проводной упряжки OEM. См. руководство изготовителя машины по диагностике и ремонту. Замените проводку OEM. См. руководство изготовителя машины по диагностике и ремонту. Ремонт генератора сигнала ускорителя. См. руководство изготовителя машины по диагностике и ремонту. Замените генератор сигнала ускорителя. См. руководство изготовителя машины по диагностике и ремонту. | 4А |  |

#### ШАГ 2C. Проверьте короткое замыкание на землю.

| **Условия:** Выключите замок зажигания. Отсоедините проводку OEM от основной проводов двигателя на разъеме C6. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта E проводов OEM-разъема C6 к заземлению блока двигателя. Измерьте сопротивление от контакта D проводов OEM-разъема C6 к заземлению блока двигателя. | Более 100 тыс. ом | 2D |
| Ремонт или замена OEM-проводов или генератора сигнала ускорителя, в зависимости от того, какое короткое замыкание имеет место. Ремонт проводной упряжки OEM. См. руководство изготовителя машины по диагностике и ремонту. Замените проводку OEM. См. руководство изготовителя машины по диагностике и ремонту. Ремонт генератора сигнала ускорителя. См. руководство изготовителя машины по диагностике и ремонту. Замените генератор сигнала ускорителя. См. руководство изготовителя машины по диагностике и ремонту. | 4А |  |

#### ШАГ 2D. Проверьте короткое замыкание от пин-кодов до пин-кодов.

| **Условия:** Выключите замок зажигания. Отсоедините проводку OEM от основной проводов двигателя на разъемах C5 и C6. Отсоедините педаль акселератора или рычаг акселератора от электропроводки OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта D разъёма С6 проводов OEM ко всем другим штифтам в разъемах С5 и С6 проводов OEM, за исключением контакта Е разъема С6 проводов OEM. Измерьте сопротивление от контакта E разъёма проводов OEM C6 к всем другим штифтам в разъемах проводов OEM C5 и C6, за исключением контакта D разъема проводов OEM C6. | Более 100 тыс. ом | 3А |
| Ремонт или замена OEM-проводов или генератора сигнала ускорителя, в зависимости от того, что имеет короткое замыкание. Ремонт проводной упряжки OEM. См. руководство изготовителя машины по диагностике и ремонту. Замените проводку OEM. См. руководство изготовителя машины по диагностике и ремонту. Ремонт генератора сигнала ускорителя. См. руководство изготовителя машины по диагностике и ремонту. Замените генератор сигнала ускорителя. См. руководство изготовителя машины по диагностике и ремонту. | 4А |  |

### ШАГ 3. Проверьте основную проводку двигателя.

#### ШАГ 3A. Проверьте основные контакты электропроводки двигателя и разъема ECM.

| **Условия:** Выключите замок зажигания. Отсоедините ECM от основной электропроводки двигателя. Промывайте и очищайте контакты разъема с помощью электронного контактного очистителя, номер детали 3824510. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Корродированные штифты Сгибаемые или сломанные штифты Отталкивающиеся или расширенные штифты Влажность в или на разъеме Пропавшие или поврежденные соединительные штифты Грязь или мусор в или на контактах разъема. | Никаких поврежденных контактов | 3B |
| Ремонт поврежденных контактов. Смой грязь, мусор или влагу из контактов разъема. Ремонт или замена основного электропроводного жгута проводов двигателя, или замена ECM, в зависимости от того, какие контакты повреждены. Смывать грязь, мусор или влагу с контактов разъема с помощью электронного контактного очистителя, номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт основной электропроводки двигателя. См. процедуру 019-043. Замените основную проводку двигателя. См. процедуру 019-043. Заменить ECM. См. процедуру 019-031. | 4А |  |

#### ШАГ 3B. Проверьте цепь на обрыв.

| **Условия:** Выключите замок зажигания. Отсоедините проводку OEM от основной проводов двигателя на разъеме C6. Отсоедините ECM от основной электропроводки двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление от контакта 13 главного провода двигателя с ремнем разъема ECM к контакту E главного разъёма электропроводки двигателя C6. Измерить сопротивление от контакта 18 главного провода двигателя с помощью разъема ECM к контакту D главного разъема проводов двигателя C6. | Менее 10 Ом | 3C |
| Ремонт или замена основного двигателя проводов жгута. Ремонт основной электропроводки двигателя. См. процедуру 019-043. Замените основную проводку двигателя. См. процедуру 019-043. | 4А |  |

#### ШАГ 3C. Проверьте короткое замыкание на землю.

| **Условия:** Выключите замок зажигания. Отсоедините проводку OEM от основной проводов двигателя на разъемах C5 и C6. Отсоедините ECM от основной электропроводки двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта 13 основной проводов двигателя с помощью разъема ECM к заземлению блока двигателя. Измерить сопротивление от контакта 18 основной проводов двигателя с помощью разъема ECM к блоку двигателя. | Более 100 тыс. ом | 3D |
| Ремонт или замена основного двигателя проводов жгута. Ремонт основной электропроводки двигателя. См. процедуру 019-043. Замените основную проводку двигателя. См. процедуру 019-043. | 4А |  |

#### ШАГ 3D. Проверьте короткое замыкание от пин-кодов до пин-кодов.

| **Условия:** Выключите замок зажигания. Отсоедините проводку OEM от основной проводов двигателя на разъемах C5 и C6. Отсоедините ECM от основной электропроводки двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта 13 основного разъёма электропроводки двигателя с разъемом ECM ко всем другим штифтам в разъеме ECM основной электропроводки двигателя. Измерить сопротивление от контакта 18 основного двигателя проводов ремня разъема ECM со всеми другими штифтами в главном двигателе проводов ремня разъема ECM. | Более 100 тыс. ом | 4А |
| Ремонт или замена основного двигателя проводов жгута. Ремонт основной электропроводки двигателя. См. процедуру 019-043. Замените основную проводку двигателя. См. процедуру 019-043. | 4А |  |

### ШАГ 4. Сбросьте коды неисправностей.

#### ШАГ 4A. Отключите код неисправности.

| **Условия: **Соединить все компоненты. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Запуск двигателя и холостость в течение одной минуты. Проверить, что код 132 неактивен. | Код 132 неактивен | 4B |
| Вернитесь к шагам устранения неполадок или свяжитесь с местным авторизованным ремонтным центром Cummins, если все шаги были завершены и перепроверены. | 1А |  |

#### ШАГ 4B. Сбросьте неактивные коды неисправностей.

| **Условия: **Соединить все компоненты. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Стирать коды неактивных ошибок с помощью CompulinkTM, Part Number 3823549; EchekTM, Part Number 3824437; или INSITETM, Part Number 3824638. | Все коды ошибок очищены | Ремонт завершён |
| Устранение неполадок с оставшимися активными кодами неисправностей. | Соответствующие диаграммы устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 132-fa
>
> ### Accelerator Position Sensor (Frequency Accelerator)
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 132-fa PID(P): P91 SPN: FMI: 4 Lamp: Flashing SRT: 00-622 | Low frequency detected at accelerator position signal pin 18 of the main engine harness electronic control module (ECM) connector. | Loss of accelerator control. Engine will **only** run at 1250 rpm. |
>
> ### Circuit Description
>
> The accelerator signal generator provides the driver's accelerator command to the ECM through the OEM harness and main engine harness. The ECM uses this signal to determine the fueling command for the electronic fuel control valve.
>
> ### Component Location
>
> The accelerator signal generator location varies with each OEM. Refer to the OEM manual.
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
>
> **To reduce the possibility of damaging the new ECM, all other active fault codes must be investigated prior to replacing the ECM.**
>
> **CAUTION · Осторожно**
>
> **To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822917 - female Deutsch/AMP/Metri-Pack test lead Part Number 3823993 - male Deutsch test lead Part Number 3823994 - female Deutsch test lead.**
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check for other fault codes. |  |
> |  | **STEP 1A.** Read the fault codes. | Fault Code 443 not logged |
> | STEP 2. | Check the OEM harness and accelerator signal generator. (The following steps have been constructed for generic OEM troubleshooting of the OEM circuit. See the OEM manual for more details.) |  |
> |  | **STEP 2A.** Inspect the OEM and main engine harness connector pins. | No damaged pins |
> |  | **STEP 2B.** Check for an open circuit. | 800 to 1200 ohms |
> |  | **STEP 2C.** Check for a short circuit to ground. | More than 100k ohms |
> |  | **STEP 2D.** Check for a short circuit from pin to pin. | More than 100k ohms |
> | STEP 3. | Check the main engine harness. |  |
> |  | **STEP 3A.** Inspect the main engine harness and ECM connector pins. | No damaged pins |
> |  | **STEP 3B.** Check for an open circuit. | Less than 10 ohms |
> |  | **STEP 3C.** Check for a short circuit to ground. | More than 100k ohms |
> |  | **STEP 3D.** Check for a short circuit from pin to pin. | More than 100k ohms |
> | STEP 4. | Clear the fault codes. |  |
> |  | **STEP 4A.** Disable the fault code. | Fault Code 132 inactive |
> |  | **STEP 4B.** Clear the inactive fault codes. | All fault codes cleared |
>
> ### STEP 1. Check for other fault codes.
>
> #### STEP 1A. Read the fault codes.
>
> | **Conditions:** Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Read the fault codes using Compulink™, Part Number 3823549; Echek™, Part Number 3824437; or INSITE ™, Part Number 3824638. | Fault Code 443 not logged | 2A |
> | Troubleshoot Fault Code 443. Refer to Fault Code 443 troubleshooting tree. | Appropriate troubleshooting chart |  |
>
> ### STEP 2. Check the OEM harness and accelerator signal generator. (The following steps have been constructed for generic OEM troubleshooting of the OEM circuit. See the OEM manual for more details.)
>
> #### STEP 2A. Inspect the OEM and main engine harness connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the main engine harness at the C6 connector. Flush and clean the connector pins using electronic contact cleaner, Part Number 3824510. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins. | No damaged pins | 2B |
> | Repair the damaged pins. Flush the dirt, debris, or moisture from the connector pins. Repair or replace the main engine harness or the OEM harness, whichever has the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electronic contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the main engine harness. Refer to Procedure 019-043. Replace the main engine harness. Refer to Procedure 019-043. Repair the OEM harness. Refer to the OEM troubleshooting and repair manual. Replace the OEM harness. Refer to the OEM troubleshooting and repair manual. | 4A |  |
>
> #### STEP 2B. Check for an open circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the main engine harness at the C6 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin E of the OEM harness C6 connector to pin D of the OEM harness C6 connector. | 800 to 1200 ohms | 2C |
> | Repair or replace the OEM harness or the accelerator signal generator, whichever has the open circuit. Repair the OEM harness. Refer to the OEM troubleshooting and repair manual. Replace the OEM harness. Refer to the OEM troubleshooting and repair manual. Repair the accelerator signal generator. Refer to the OEM troubleshooting and repair manual. Replace the accelerator signal generator. Refer to the OEM troubleshooting and repair manual. | 4A |  |
>
> #### STEP 2C. Check for a short circuit to ground.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the main engine harness at the C6 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin E of the OEM harness C6 connector to engine block ground. Measure the resistance from pin D of the OEM harness C6 connector to engine block ground. | More than 100k ohms | 2D |
> | Repair or replace the OEM harness or the accelerator signal generator, whichever has the short circuit to ground. Repair the OEM harness. Refer to the OEM troubleshooting and repair manual. Replace the OEM harness. Refer to the OEM troubleshooting and repair manual. Repair the accelerator signal generator. Refer to the OEM troubleshooting and repair manual. Replace the accelerator signal generator. Refer to the OEM troubleshooting and repair manual. | 4A |  |
>
> #### STEP 2D. Check for a short circuit from pin to pin.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the main engine harness at the C5 and C6 connectors. Disconnect the accelerator pedal or accelerator lever from the OEM harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin D of the OEM harness C6 connector to all other pins in the OEM harness C5 and C6 connectors, except pin E of the OEM harness C6 connector. Measure the resistance from pin E of the OEM harness C6 connector to all other pins in the OEM harness C5 and C6 connectors, except pin D of the OEM harness C6 connector. | More than 100k ohms | 3A |
> | Repair or replace the OEM harness or the accelerator signal generator, whichever has the short circuit. Repair the OEM harness. Refer to the OEM troubleshooting and repair manual. Replace the OEM harness. Refer to the OEM troubleshooting and repair manual. Repair the accelerator signal generator. Refer to the OEM troubleshooting and repair manual. Replace the accelerator signal generator. Refer to the OEM troubleshooting and repair manual. | 4A |  |
>
> ### STEP 3. Check the main engine harness.
>
> #### STEP 3A. Inspect the main engine harness and ECM connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ECM from the main engine harness. Flush and clean the connector pins using electronic contact cleaner, Part Number 3824510. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins. | No damaged pins | 3B |
> | Repair the damaged pins. Flush the dirt, debris, or moisture from the connector pins. Repair or replace the main engine harness, or replace the ECM, whichever has the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electronic contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the main engine harness. Refer to Procedure 019-043. Replace the main engine harness. Refer to Procedure 019-043. Replace the ECM. Refer to Procedure 019-031. | 4A |  |
>
> #### STEP 3B. Check for an open circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the main engine harness at the C6 connector. Disconnect the ECM from the main engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 13 of the main engine harness ECM connector to pin E of the main engine harness C6 connector. Measure the resistance from pin 18 of the main engine harness ECM connector to pin D of the main engine harness C6 connector. | Less than 10 ohms | 3C |
> | Repair or replace the main engine harness. Repair the main engine harness. Refer to Procedure 019-043. Replace the main engine harness. Refer to Procedure 019-043. | 4A |  |
>
> #### STEP 3C. Check for a short circuit to ground.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the main engine harness at the C5 and C6 connectors. Disconnect the ECM from the main engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 13 of the main engine harness ECM connector to engine block ground. Measure the resistance from pin 18 of the main engine harness ECM connector to engine block ground. | More than 100k ohms | 3D |
> | Repair or replace the main engine harness. Repair the main engine harness. Refer to Procedure 019-043. Replace the main engine harness. Refer to Procedure 019-043. | 4A |  |
>
> #### STEP 3D. Check for a short circuit from pin to pin.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the main engine harness at the C5 and C6 connectors. Disconnect the ECM from the main engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 13 of the main engine harness ECM connector to all other pins in the main engine harness ECM connector. Measure the resistance from pin 18 of the main engine harness ECM connector to all other pins in the main engine harness ECM connector. | More than 100k ohms | 4A |
> | Repair or replace the main engine harness. Repair the main engine harness. Refer to Procedure 019-043. Replace the main engine harness. Refer to Procedure 019-043. | 4A |  |
>
> ### STEP 4. Clear the fault codes.
>
> #### STEP 4A. Disable the fault code.
>
> | **Conditions:** Connect all components. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Start the engine and idle for one minute. Verify Fault Code 132 is inactive. | Fault Code 132 inactive | 4B |
> | Return to troubleshooting steps or contact a local Cummins Authorized Repair Location if all steps have been completed and rechecked. | 1A |  |
>
> #### STEP 4B. Clear the inactive fault codes.
>
> | **Conditions:** Connect all components. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Erase the inactive fault codes using Compulink™, Part Number 3823549; Echek™, Part Number 3824437; or INSITE™, Part Number 3824638. | All fault codes cleared | Repair complete |
> | Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
