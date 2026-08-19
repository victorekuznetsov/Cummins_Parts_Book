---
aliases:
  - "Обслуживание журналов неисправностей и трендов модуля CM530 CENSE™"
type: "TSB"
doc: "tsb110093"
title_en: "CM530 CENSE™ Module Fault and Trend Log Maintenance"
title_ru: "Обслуживание журналов неисправностей и трендов модуля CM530 CENSE™"
released: "2011-04-29"
modified: "2011-04-29"
group: "19 - Electronic Engine Controls"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2011/tsb110093.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb110093.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QST30"
  - "год/2011"
  - "перевод/машинный"
  - "тема/electronic-engine-controls"
---

# CM530 CENSE™ Module Fault and Trend Log Maintenance
**Обслуживание журналов неисправностей и трендов модуля CM530 CENSE™**

> [!abstract] TSB · `tsb110093`
> **Раздел Cummins:** 19 - Electronic Engine Controls
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Даты:** выпущен 2011-04-29 · изменён 2011-04-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2011/tsb110093.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb110093.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Обслуживание журналов неисправностей и трендов модуля CM530 CENSE™

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### Содержание

#### Проблема:

- Проблема повреждения памяти была выявлена, когда модулю CENSETM разрешено быть полным в течение длительных периодов времени. В результате может возникнуть ряд кодов ошибок и симптомов с различной степенью тяжести.
- Модули CENSETM часто заполняются, когда происходит сбой прерывистого типа, который генерирует высокий уровень кода неисправности. Снимок хранится в буфере журнала неисправностей каждый раз, когда активируется код неисправности. Скорость, с которой буфер заполняется, зависит от количества регистрируемых параметров и частоты неисправности.
- Кроме того, оборудование для мониторинга RS-422 может запрашивать данные быстрее, чем это может быть передано через шину данных RS-422 CAN. В этой ситуации модуль CENSETM будет буферизировать данные о трендах, которые могут быть отправлены немедленно. Когда данные буферизируются в течение длительного периода времени, модуль CENSETM может стать полным. Скорость заполнения буфера зависит от количества регистрируемых параметров и частоты запроса данных системы удаленного мониторинга.
- Нечастая загрузка данных о неисправностях и тенденциях также может привести к заполнению буферов ошибок и тенденций.
- Также было установлено, что двигатели QSV могут страдать от того, что память данных о тренде заполняется во время нормальной работы двигателя.

> [!note] Примечание
> Перед попыткой устранения неполадок модуля CENSETM следует изучить все коды активных и неактивных неисправностей.

#### Проверка:

- Код 111 ошибки - внутренний электронный модуль управления (ECM)
- Код 335 - Ошибка внутреннего электронного модуля управления (ECM)
- Код ошибки 747 - память данных тренда 90%
- Код ошибки 748 - память данных Trend 100 процентов
- Код ошибки 749 - память журнала данных с кодом ошибки 90 процентов
- Код 754 — память Datalog на 100% полная

#### Симптомы:

- 5.2.1 Освещение неисправной лампы
- Прерывание дистанционного мониторинга
- Не двигайся.
- Не начинай.
- Двигатель отключился
- Связь с модулем CENSETM невозможна
- Повреждение данных - ESN, часы, расход топлива и т.д. неправильно
- Газовые двигатели могут страдать от неисправностей и неточных данных датчика температуры выхлопных газов.

Используйте следующие процедуры для устранения коррупции модуля CENSETM.

Если связь может быть установлена с модулем CENSETM, используйте следующую процедуру, когда испытывается любое количество симптомов или кодов неисправностей выше, и можно установить соединение с модулем CENSETM при использовании INSITE CENSE, в то время как модуль все еще установлен на блоке.

#### Коммуникация устанавливается

1. Скачать все данные, хранящиеся в модуле CENSETM
2. Очистить память журнала ошибок / трендов
3. Проверьте наличие доказательств повреждения памяти, таких как ESN, часы, расход топлива и т. д. быть некорректным. Если выявлена коррупция, продолжайте делать шаг 4. В противном случае перейдите к шагу 5
4. Калибровка модуля CENSETM с использованием последней калибровочной версии
5. Позволяет двигателю/оборудованию нормально работать в течение 1 часа. Скачать модуль CENSETM. После завершения загрузки проверьте модуль CENSETM на наличие повреждений памяти. Если обнаружена повреждение памяти, замените модуль CENSETM. Ссылка TSB110024 для получения дополнительной информации.

Если связь с модулем CENSETM может быть установлена **не**, используйте следующую процедуру, когда симптомы или коды неисправностей выше испытаны, и при использовании INSITE CENSE невозможно установить соединение с модулем CENSETM, в то время как модуль все еще установлен на блоке.

#### Коммуникация не установлена

1. Проверка шины данных CAN (разъем DB9 до 3-pin DeutschTM)
2. Электронные инструменты Проверка
3. Проверка оборудования

#### Если используется дополнительное оборудование дистанционного мониторинга:

- При использовании оборудования дистанционного мониторинга важно убедиться, что скорость передачи данных находится в пределах пропускной способности шины данных RS-422 CAN. Рекомендуется использовать частоту регистрации не более 0,1 Гц (1 журнал каждые 10 секунд), чтобы убедиться, что модуль CENSETM начинает буферизировать данные.

> [!note] Примечание
> Шина данных CAN J1939 и RS-232 имеют более высокую пропускную способность и могут ** не ** требовать снижения скорости отбора проб.

#### Рекомендуемая частота загрузки модуля CENSETM:

- Рекомендуется, чтобы модуль CENSETM, буфер ошибок и трендов, загружался и опорожнился во время каждого события службы. См. следующую таблицу для руководства по количеству часов, прежде чем модуль CENSETM станет на 100% полным.

| Пробная ставка \[hrs/request\] | Таблица 1: 100-процентное заполнение модуля CENSETM |  |  |  |  |
|---|---|---|---|---|---|
| Количество зарегистрированных параметров |  |  |  |  |  |
| 1 | 5 | 10 | 20 | 40 |  |
| 0.017 | 2133 | 427 | 213 | 107 | 53 |
| 0.25 | 32000 | 6400 | 3200 | 1600 | 800 |
| 0.5 | 64000 | 12800 | 6400 | 3200 | 1600 |
| 1 | 128000 | 25600 | 12800 | 6400 | 3200 |

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## CM530 CENSE™ Module Fault and Trend Log Maintenance
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Contents
>
> #### Issue:
>
> - A memory corruption issue has been identified when the CENSE™ module is allowed to become full for extended periods of time. A number of fault codes and symptoms with varying severity can be experienced as a result.
> - CENSE™ modules often become filled when an intermittent type failure, which generates high fault code counts, is experienced. A snapshot is stored to the fault log buffer every time a fault code is activated. The rate at which the buffer is filled up is dependent on the number of parameters being logged and the frequency of the fault.
> - It is also possible for RS-422 monitoring equipment to request data faster than it can be communicated across the RS-422 data link. In this situation, the CENSE™ module will buffer trend data which can **not** be immediately sent. When data is buffered for an extended period of time, the CENSE™ module can become full. The rate at which the buffer is filled up is dependent on the number of parameters being logged and the data request frequency of the remote monitoring system.
> - Infrequent download of fault and trend data can also result in the fault and trend buffers becoming full.
> - It has also been identified that QSV engines can suffer from the trend data memory becoming filled during normal operation of the engine.
>
> **Note · Примечание**
> Before attempting troubleshooting of the CENSE™ module, all active and inactive fault codes should be investigated.
>
> #### Verification:
>
> - Fault Code 111 – Internal Electronic Control Module (ECM) Error
> - Fault Code 335 - Internal Electronic Control Module (ECM) Error
> - Fault Code 747 - Trend Data Memory 90 percent Full
> - Fault Code 748 - Trend Data Memory 100 percent Full
> - Fault Code 749 – Fault Code Datalog Memory 90 percent Full
> - Fault Code 754 – Fault Code Datalog Memory 100 percent Full
>
> #### Symptoms:
>
> - Fault lamp illumination
> - Interruption of remote monitoring
> - No propel
> - No start
> - Engine shuts down
> - No communication possible with the CENSE™ module
> - Data corruption - ESN, hours, fuel consumption etc. incorrect
> - Gas engines can suffer misfires and inaccurate exhaust gas temperature sensor data.
>
> Use the following procedures to resolve CENSE™ module corruption.
>
> If communication can be established with the CENSE™ module use the following procedure when any number of the symptoms or fault codes above are experienced, and it is possible to establish a connection with the CENSE™ module when using INSITE CENSE, while the module is still installed on the unit.
>
> #### Communication is Established
>
> 1. Download all data held in the CENSE™ module
> 2. Clear the fault/trend log memory
> 3. Check for evidence of memory corruption, such as ESN, hours, fuel consumption, etc. being incorrect. If corruption is detected, continue to step 4. Otherwise move to step 5
> 4. Calibrate the CENSE™ module with the latest calibration version
> 5. Allow the engine/equipment to operate normally for 1 hour. Download the CENSE™ module. Once the download is complete, inspect the CENSE™ module for evidence of memory corruption. If memory corruption is detected, replace the CENSE™ module. Reference TSB110024 for further information.
>
> If communication can **not** be established with the CENSE™ module use the following procedure when the symptoms or fault codes above are experienced, and it is **not** possible to establish a connection with the CENSE™ module when using INSITE CENSE, while the module is still installed on the unit.
>
> #### Communication is not established
>
> 1. Data link checks (DB9 to 3-pin Deutsch™ connector)
> 2. Electronic tool checks
> 3. Hardware checks
>
> #### If additional remote monitoring equipment is used:
>
> - When remote monitoring equipment is used, it is essential to make sure the rate at which data is transmitted is within the bandwidth capabilities of the RS-422 data link. It is recommended that a logging frequency of no more than 0.1 Hz (1 log every 10 seconds) is used to make sure the CENSE™ module does **not** begin to buffer data.
>
> **Note · Примечание**
> Data link J1939 and RS-232 have higher bandwidth capabilities and may **not** require reduced sampling rates to be applied.
>
> #### Recommended CENSE™ module download frequency:
>
> - It is recommended that the CENSE™ module fault and trend buffer is downloaded and emptied during every service event. Refer to the following table for guidance on the number of hours before the CENSE™ module becomes 100 percent full.
>
> | Sample Rate \[hrs/request\] | Table 1: Hours to 100 percent fill of CENSE™ Module |  |  |  |  |
> |---|---|---|---|---|---|
> | Number of Parameters Logged |  |  |  |  |  |
> | 1 | 5 | 10 | 20 | 40 |  |
> | 0.017 | 2133 | 427 | 213 | 107 | 53 |
> | 0.25 | 32000 | 6400 | 3200 | 1600 | 800 |
> | 0.5 | 64000 | 12800 | 6400 | 3200 | 1600 |
> | 1 | 128000 | 25600 | 12800 | 6400 | 3200 |
>
> ### Document History
