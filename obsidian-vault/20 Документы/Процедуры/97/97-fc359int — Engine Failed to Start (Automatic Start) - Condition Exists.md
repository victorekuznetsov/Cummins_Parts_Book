---
type: "Процедура"
doc: "97-fc359int"
title_en: "Engine Failed to Start (Automatic Start) - Condition Exists"
modified: "2004-10-04"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc359int.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc359int.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
  - "перевод/машинный"
---

# Engine Failed to Start (Automatic Start) - Condition Exists

> [!abstract] Процедура · `97-fc359int`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-10-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc359int.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc359int.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 359 (интегрированный)

### Не удалось запустить двигатель (автоматический запуск) - состояние

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 359 PID(P): СПН: ФМИ: 11 лампочка: Желтая СТО: | Не удалось запустить двигатель (автоматический запуск) - состояние существует. Система ICONTM не смогла запустить двигатель автоматически. | Система ICONTM будет отключена. Включено только обязательное отключение. Может нормально запустить двигатель. |

![[19803217.png]]

### Описание цепи

Схема ретрансляции стартера управляет и контролирует как катушку ретрансляции стартера, так и обратный сигнал. Стартерная реле используется функцией ICONTM для выполнения автоматических запусков двигателя.

### Расположение компонента

Стартерная реле установлена на огневой стенке транспортного средства на впускной стороне двигателя.

### Практические замечания

Этот код ошибки устанавливается, если два последовательных автоматических запуска не удались. Если запуском управляет электронный модуль управления двигателем (ECM) и 200 об/мин не достигается в течение 2 секунд или 450 об/мин в течение 14 секунд, то запуск не удался. После первого отказа система ICONTM выжидает 1 минуту и пробует снова. Если второй старт не удался, то ошибка устанавливается. Он очищается, как только ручной запуск увенчается успехом.

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
>

**Для уменьшения возможности повреждения нового двигателя ECM необходимо изучить все другие коды активных неисправностей перед заменой двигателя ECM.**

Чтобы не повредить контакты и жгут, при измерениях пользуйтесь следующими измерительными проводами: Номер детали 3822917 - розеточный пробоотборник типа Deutsch/AMP/Metri-Pack Номер детали 3822758 - пробоотборник типа plug-type Deutsch/AMP/Metri-Pack.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проведите собеседование с водителем, чтобы определить, когда произошел сбой, какова общая информация о настройке и возникают ли какие-либо проблемы с жестким запуском во время ручного запуска. |  |
|  | **ШАГ 1А.** Проведите собеседование с водителем, чтобы определить, когда произошел сбой, какова общая информация о настройке и возникают ли какие-либо проблемы с запуском во время ручного запуска. | Проблема с двигателем |
| ШАГ 2. | Прочитайте все коды ошибок. |  |
|  | **STEP 2A.** Прочитайте коды неисправностей с помощью инструментария электронного обслуживания INSITETM или выключите светильник ICONTM. | Код ошибки 359 неактивен |
|  | **СТЭП 2В.** Ручно запустите двигатель. | Двигатель начинает |
| ШАГ 3. | Проверьте контакты ретранслятора стартера. |  |
|  | **STEP 3A.** Выполните тест стартового реле и блокировок. | Стартовый вовлечённый |
|  | **STEP 3B.** Проверьте наличие открытой цепи в реле реле ICONTM. | Менее 10 Ом |
| ШАГ 4. | Активировать систему ICONTM; проверить ECM двигателя на наличие активных кодов неисправностей. |  |
|  | **STEP 4A.** Активировать систему ICONTM; проверить ECM двигателя на наличие активных кодов неисправностей. | Нет активных кодов неисправностей; двигатель выполняет автозапуск |
| ШАГ 5. | Сбросьте коды неисправностей. |  |
|  | **STEP 5A.** Отключить код ошибки. | Код ошибки 359 неактивен |

### ШАГ 1. Проведите собеседование с водителем, чтобы определить, когда произошел сбой, какова общая информация о настройке и возникают ли какие-либо проблемы с жестким запуском во время ручного запуска.

#### ШАГ 1A. Проведите собеседование с водителем, чтобы определить, когда произошел сбой, какова общая информация о настройке и возникают ли какие-либо проблемы с жестким запуском во время ручного запуска.

| **Условия:** Проверьте настройки кабины, установленной на термостате для системы ICONTM. Убедитесь, что таймер выключения и настройки термостата кабины исправны в инструменте электронного обслуживания INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
|  | Проблема с двигателем | Соответствующее руководство по устранению неполадок и ремонту |
| Код ошибки 359, проблема системы ICONTM | 2А |  |

### ШАГ 2. Прочитайте все коды ошибок.

#### ШАГ 2A. Прочитайте коды неисправностей с помощью инструментария электронного обслуживания INSITETM или выключите лампу ICONTM.

| **Условия: **Соединить все компоненты. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Прочитайте коды неисправностей с помощью инструментария электронного обслуживания INSITETM или выключите лампу ICONTM. | Код ошибки 359 неактивен | 5а |
| Код ошибки 359 активный или Код ошибки 2291 неактивный | 2В |  |

#### ШАГ 2B. Ручно запустите двигатель.

| **Условия: **Соединить все компоненты. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Запуск двигателя с помощью переключателя зажигания. | Двигатель начинает | 3А |
| Смотрите соответствующее руководство по устранению неполадок и ремонту для симптомов трудного начала. | Соответствующее руководство по устранению неполадок и ремонту |  |

### ШАГ 3. Проверьте контакты ретранслятора стартера.

#### ШАГ 3A. Выполните тест стартового реле и блокировок.

| **Условия:** Подключить инструмент электронного сервиса INSITETM. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Выполните тест реле и блокировок стартера с использованием инструментария электронного обслуживания INSITETM. См. соответствующее руководство по электронному обслуживанию. | Стартовый вовлечённый | 4А |
| Стартер **не** вовлекается | 3B |  |

#### ШАГ 3B. Проверьте наличие открытой цепи в схеме ретрансляции стартера ICONTM.

| **Условия:** Выключите замок зажигания. Отключите стартовую реле ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление между контактом 14 разъема привода ECM и контактом 33 разъема ECM OEM. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Менее 10 Ом | 4А |
| не соответствует спецификациям. Ремонт или замена OEM-проводов см. Руководство по обслуживанию OEM. | 4А |  |

### ШАГ 4. Активировать систему ICONTM; проверить ECM двигателя на наличие активных кодов неисправностей.

#### ШАГ 4A. Активировать систему ICONTM; проверить ECM двигателя на наличие активных кодов неисправностей.

| **Условия: **Соединить все компоненты. Запуск и запуск двигателя в режиме ICONTM. Выполните автозапуск с помощью термостата кабины или запроса напряжения батареи. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Выполните автозапуск с системой ICONTM. После первоначального включения системы ICONTM двигатель отключится через 1 минуту. Запросить автозапуск с термостатом кабины. Если термостат кабины недоступен, загрузите батареи до менее чем 12,2 ВДК. | Никаких активных кодов неисправностей. Двигатель выполняет автозапуск | 5а |
| Присутствуют активные коды неисправностей. Двигатель делает **не** автозапуск | Устранение неисправностей с помощью активных кодов 5A |  |

### ШАГ 5. Сбросьте коды неисправностей.

#### ШАГ 5A. Отключите код неисправности.

| **Условия: **Соединить все компоненты. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить код 359 неактивен с помощью инструментария электронного обслуживания INSITETM. Стирайте неактивные коды неисправностей с помощью инструментария электронного обслуживания INSITETM. | Код ошибки 359 неактивен. Все коды неисправностей очищены. | Ремонт завершён |
| Вернитесь к шагам устранения неполадок или свяжитесь с ближайшим авторизованным ремонтным центром Cummins, если все шаги были завершены и перепроверены. Устранение неполадок с оставшимися активными кодами неисправностей. | Соответствующие диаграммы устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 359 (Integrated)
>
> ### Engine Failed to Start (Automatic Start) - Condition Exists
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 359 PID(P): SPN: FMI: 11 Lamp: Yellow SRT: | Engine Failed to Start (Automatic Start) - Condition Exists. The ICON™ system has failed to start the engine automatically. | The ICON™ system will be disabled. **Only** mandatory shutdown will be enabled. Can possibly start engine normally. |
>
> ### Circuit Description
>
> The starter relay circuit controls and monitors both the starter relay coil and return signal. The starter relay is used by the ICON™ feature to perform automatic starts of the engine.
>
> ### Component Location
>
> The starter relay is mounted on the fire wall of the vehicle on the intake side of the engine.
>
> ### Shoptalk
>
> This fault code is set if two consecutive automatic starts fail. If a start is commanded by the engine electronic control module (ECM) and 200 rpm is **not** reached within 2 seconds nor 450 rpm within 14 seconds, then the start failed. After the first failure, the ICON™ system waits 1 minute and tries again. If the second start fails, the fault is set. It is cleared as soon as a manual start is successful.
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
>
> **To reduce the possibility of damaging a new engine ECM, all other active fault codes must be investigated prior to replacing the engine ECM.**
>
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822917 - female Deutsch/AMP/Metri-Pack test lead Part Number 3822758 - male Deutsch/AMP/Metri-Pack test lead.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Interview the driver to determine when the failure occurred, what the general setup information is, and if any hard start problems occur during manual starts. |  |
> |  | **STEP 1A.** Interview the driver to determine when the failure occurred, what the general setup information is, and if any hard start problems occur during manual starts. | Engine problem |
> | STEP 2. | Read all fault codes. |  |
> |  | **STEP 2A.** Read fault codes with INSITE™ electronic service tool or flash out with ICON™ lamp. | Fault Code 359 inactive |
> |  | **STEP 2B.** Manually start the engine. | Engine starts |
> | STEP 3. | Check the starter relay contacts. |  |
> |  | **STEP 3A.** Perform the starter relay and interlocks test. | Starter engages |
> |  | **STEP 3B.** Check for an open circuit in the ICON™ starter relay coil. | Less than 10 ohms |
> | STEP 4. | Activate the ICON™ system; check the engine ECM for active fault codes. |  |
> |  | **STEP 4A.** Activate the ICON™ system; check the engine ECM for active fault codes. | No active fault codes; Engine performs autostart |
> | STEP 5. | Clear the fault codes. |  |
> |  | **STEP 5A.** Disable the fault code. | Fault Code 359 inactive |
>
> ### STEP 1. Interview the driver to determine when the failure occurred, what the general setup information is, and if any hard start problems occur during manual starts.
>
> #### STEP 1A. Interview the driver to determine when the failure occurred, what the general setup information is, and if any hard start problems occur during manual starts.
>
> | **Conditions:** Check the settings of the cab-mounted thermostat for ICON™ system. Make certain that the idle shutdown timer and cab thermostat settings are correct in INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> |  | Engine problem | Appropriate troubleshooting and repair manual |
> | Fault Code 359, ICON™ system problem | 2A |  |
>
> ### STEP 2. Read all fault codes.
>
> #### STEP 2A. Read fault codes with INSITE™ electronic service tool or flash out with ICON™ lamp.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Read the fault codes with INSITE™ electronic service tool or flash out with ICON™ lamp. | Fault Code 359 inactive | 5A |
> | Fault Code 359 active or Fault Code 2291 inactive | 2B |  |
>
> #### STEP 2B. Manually start the engine.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Start the engine using the keyswitch. | Engine starts | 3A |
> | Refer to the appropriate troubleshooting and repair manual for hard start symptoms. | Appropriate troubleshooting and repair manual |  |
>
> ### STEP 3. Check the starter relay contacts.
>
> #### STEP 3A. Perform the starter relay and interlocks test.
>
> | **Conditions:** Connect the INSITE™ electronic service tool. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Perform the starter relay and interlocks test using INSITE™ electronic service tool. Refer to the appropriate electronic service tool manual. | Starter engages | 4A |
> | Starter does **not** engage | 3B |  |
>
> #### STEP 3B. Check for an open circuit in the ICON™ starter relay circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ starter relay. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance between pin 14 of the ECM actuator connector to pin 33 of the ECM OEM connector. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 10 ohms | 4A |
> | Does **not** meet specifications. Repair or replace the OEM harness Refer to the OEM service manual. | 4A |  |
>
> ### STEP 4. Activate the ICON™ system; check the engine ECM for active fault codes.
>
> #### STEP 4A. Activate the ICON™ system; check the engine ECM for active fault codes.
>
> | **Conditions:** Connect all components. Start and run the engine in ICON™ mode. Perform autostart with the cab thermostat or battery voltage request. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Perform an autostart with the ICON™ system. After initial activation of the ICON™ system, engine will shut down in 1 minute. Request autostart with the cab thermostat. If the cab thermostat is not available, load the batteries to less than 12.2 VDC. | No active fault codes. Engine performs autostart | 5A |
> | Active fault codes present. Engine does **not** autostart | Troubleshoot active fault codes 5A |  |
>
> ### STEP 5. Clear the fault codes.
>
> #### STEP 5A. Disable the fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify Fault Code 359 is inactive using INSITE™ electronic service tool. Erase the inactive fault codes using INSITE™ electronic service tool. | Fault Code 359 inactive. All fault codes cleared. | Repair complete |
> | Return to the troubleshooting steps, or contact the nearest Cummins Authorized Repair Location if all the steps have been completed and rechecked. Troubleshooting any remaining active fault codes. | Appropriate troubleshooting charts |  |
