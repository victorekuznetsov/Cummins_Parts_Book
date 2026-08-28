---
aliases:
  - "Цепь датчика частоты вращения двигателя (ESS)"
type: "Процедура"
doc: "94-fc115"
title_en: "Engine Speed Sensor (ESS) Circuit"
title_ru: "Цепь датчика частоты вращения двигателя (ESS)"
modified: "2003-03-19"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666184"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-fc115.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/94-fc115.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/94"
  - "перевод/машинный"
---

# Engine Speed Sensor (ESS) Circuit
**Цепь датчика частоты вращения двигателя (ESS)**

> [!abstract] Процедура · `94-fc115`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2003-03-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-fc115.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/94-fc115.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 115

### Цепь датчика частоты вращения двигателя (ESS)

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 115 P(P): СПН: ФМИ: Лампа: СТО: 00-681 | Между контактами 21 и 22 разъёма жгутов проводов двигателя не было обнаружено никакой скорости двигателя. | Двигатель выключен и может **не** работать. Общий выход сигнализации активизирован. |

![[19a00001.png]]

### Описание цепи

Схема ESS обеспечивает сигнал скорости двигателя к электронному модулю управления (ECM) через электропроводку двигателя.

### Расположение компонента

ESS расположен в корпусе Flywheel.

### Практические замечания

- Если проблема возникает при определенной температуре двигателя, обязательно проверьте схему ESS, пока двигатель находится при этой конкретной температуре.

- Чистый сенсорный наконечник; мусор может вызывать прерывистые сигналы.

- Датчик должен быть отрегулирован должным образом, чтобы получить хороший сигнал. Убедитесь, что датчик от 1⁄2 до 3⁄4 выходит из контакта с зубом маховика и что запирающий орех плотный и правильно торвируется.

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
>

**Чтобы избежать повреждения штифта и проводов, используйте следующий испытательный щуп при проведении измерения: Часть нет. 3823996 - гнездовой испытательный щуп Weather-Pack Номер детали. 3822758 - пробный щуп типа пробоотвода Deutsch/Metri-Pack**

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте ESS. |  |
|  | **STEP 1A.** Осмотрите контакты разъема ESS и проводов двигателя. | Никаких поврежденных контактов |
|  | **ШАГ 1В.** Проверить ЭСС. | Не поврежденный ESS |
|  | **STEP 1C.** Проверьте наличие открытой цепи в ESS. | менее 1500 Ом |
|  | **ШАГ 1D.** Проверьте короткое замыкание в ESS. | Более 10 миллионов ом |
|  | **ШАГ 1Е.** Проверить короткое замыкание между катушками ESS. | Более 10 миллионов ом |
| ШАГ 2. | Проверьте жгут проводов двигателя. |  |
|  | **STEP 2A.** Проверить контактные линзы для проводов двигателя и разъема ECM. | Никаких поврежденных контактов |
|  | **STEP 2A-1.** Проверить кабель адаптера упряжки двигателя и удлинители упряжки двигателя. | Никаких поврежденных контактов |
|  | **STEP 2B.** Проверьте наличие открытой цепи в сигнале и обратных проводах. | менее 1500 Ом |
|  | **STEP 2B-1.** Проверьте наличие открытой цепи в кабеле адаптера для проводов двигателя и кабелях для расширения упругой проводов двигателя. | Менее 10 Ом |
|  | **STEP 2C.** Проверьте короткое замыкание на землю в сигнальных и обратных проводах с помощью адаптера для проводов двигателя и любых используемых удлинительных кабелей, установленных. | Более 10 миллионов ом |
|  | **STEP 2C-1.** Проверьте короткое замыкание на землю в сигнале ремня электропроводки двигателя и обратном проводе. | Более 10 миллионов ом |
|  | **STEP 2D.** Проверьте короткое замыкание сигнала и возвратите провода ко всем другим проводам в ремне электропроводки двигателя. | Более 10 миллионов ом |
|  | **STEP 2D-1.** Проверьте короткое замыкание от штифта до штифта в кабеле адаптера жгута двигателя и любых используемых удлинительных кабелей жгута жгута двигателя. | Более 10 миллионов ом |
| ШАГ 3. | Четкие коды ошибок. |  |
|  | **СТЭП 3А.**Чистые коды неисправностей. | Все коды ошибок очищены |

### ШАГ 1. Проверьте ESS.

#### ШАГ 1A. Проверьте контакты разъема ESS и проводов двигателя.

| **Условия:** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините ESS от жгута проводов двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| для следующего: согнутые или сломанные штифты отодвигаются назад или расширенные штифты разъедают штифты влагой в или на разъеме. | Никаких поврежденных контактов | 1В |
| **Починить поврежденные контакты** Починить или заменить ремень электропроводки двигателя или ESS, в зависимости от того, какие контакты повреждены. Ремонт ремня электропроводки двигателя. См. процедуру 19-202 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Замените жгут проводов двигателя. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Замените ESS. См. процедуру 019-042 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3А |  |

#### ШАГ 1B. Проверьте ССС.

| **Условия:** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините ESS от жгута проводов двигателя. Удалить ESS. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| металлический мусор на конце датчика повреждения на конце датчика, вызванного контактом с утечкой маховика масла или проблемами изоляции, такими как отек поврежденного электрического горшка в сенсорном конце датчика. | Не поврежденный ESS | 1С |
| **Очистить или заменить ESS** Очистить ESS. См. процедуру 019-042 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Замените ESS. См. процедуру 019-042 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3А |  |

#### ШАГ 1C. Проверьте наличие открытой цепи в ESS.

| **Условия:** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините ESS от жгута проводов двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление от контакта А до контакта В первой катушки ESS. Измерить сопротивление от контакта А до контакта В второй катушки ESS. | менее 1500 Ом | 1D |
| **Заменить ESS** См. процедуру 019-042 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3А |  |

#### ШАГ 1D. Проверьте короткое замыкание, чтобы приземлиться в ESS.

| **Условия:** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините ESS от жгута проводов двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление от контакта А первой катушки ESS до заземления блока двигателя. Измерить сопротивление от контакта А второй катушки ESS до заземления блока двигателя. | Более 10 миллионов ом | 1Е |
| **Заменить ESS** См. процедуру 019-042 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3А |  |

#### ШАГ 1E. Проверьте короткое замыкание между катушками ESS.

| **Условия:** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините ESS от жгута проводов двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление от контакта А первой катушки ESS до контакта А второй катушки ESS. | Более 10 миллионов ом | 2А |
| **Заменить ESS** См. процедуру 019-042 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3А |  |

### ШАГ 2. Проверьте жгут проводов двигателя.

#### ШАГ 2A. Проверьте электропроводку двигателя и ECM.

| **Условия:** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от адаптера ремня от ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| согнутые или сломанные штифты отодвигаются назад или расширенные штифты разъедают штифты влагой в или на разъеме. | Никаких поврежденных контактов | 2А-1-1 |
| **Поврежденные контакты** Ремонт или замена проводов двигателя на адаптерный кабель или ECM, в зависимости от того, какие контакты повреждены. Ремонт проводов двигателя с помощью адаптера кабеля. См. процедуру 019-240 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Замените проводку двигателя адаптерным кабелем. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Заменить ECM. См. процедуры OEM. | 3А |  |

#### ШАГ 2A-1. Проверьте разъём жгутов проводов двигателя и кабели расширения жгутов проводов двигателя.

| **Условия:** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от удлинителей упряжей кабелей от упряжки проводов двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| согнутые или сломанные штифты отодвигаются назад или расширенные штифты разъедают штифты влагой в или на разъеме. | Никаких поврежденных контактов | 2В |
| **Поврежденные контакты** Починить или заменить упряжку для проводов двигателя или удлинитель для проводов двигателя, в зависимости от того, какие контакты повреждены. Ремонт ремня электропроводки двигателя или проводов двигателя удлинитель кабеля. См. процедуру 019-240 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Замените упряжку для проводов двигателя или удлинительный кабель для проводов двигателя. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3А |  |

#### ШАГ 2B. Проверьте наличие открытой цепи в сигнале и обратных проводах.

| **Условия:** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от адаптера адаптера кабельного разъема от ECM. Подключите ESS к жгуту проводов двигателя. Подключите жгут проводов двигателя к адаптерному кабелю. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта 22 до контакта 21 40-контактного штифта на разъёме адаптера ремня электропроводки двигателя. | менее 1500 Ом | 2C |
|  | 2В-1-1 |  |

#### ШАГ 2B-1. Проверьте наличие открытой цепи в кабеле адаптера для проводов двигателя и кабелях расширения упряжки двигателя.

| **Условия:** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от адаптера адаптера кабельного разъема от ECM. Отсоедините проводку двигателя от проводов двигателя удлинителя кабеля. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить непрерывность контакта 22 каждого кабеля, используемого между ремнем электропроводки двигателя и ECM. Измерить непрерывность контакта 21 каждого кабеля, используемого между ремнем электропроводки двигателя и ECM. | Менее 10 Ом Ремонт или замена электропроводки двигателя жгута. Ремонт ремня электропроводки двигателя. См. Процедуры 019-202 и 019-240 в Руководстве по устранению неполадок и ремонту топливной системы QST серии QST30 G-Drive Engine, Бюллетень No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Замените жгут проводов двигателя. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3А |
| **Починить или заменить адаптерный кабель или удлинительный кабель упряжки упряжки двигателя, в зависимости от того, что признано неисправным** Починить адаптерный кабель упряжки двигателя или удлинительный кабель упряжки двигателя. См. процедуру 019-240 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Замените адаптерный кабель или удлинительный кабель упряжки двигателя. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3А |  |

#### ШАГ 2C. Проверьте короткое замыкание для заземления в сигнале и возвратных проводах с помощью адаптера для проводов двигателя и любых используемых удлинительных кабелей, установленных.

| **Условия:** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от адаптера ремня от ECM. Отсоедините ESS от жгута проводов двигателя. Подключите жгут проводов двигателя к адаптерному кабелю. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта 22 проводов двигателя с адаптерным кабелем разъёма к заземлению блока двигателя. Измерьте сопротивление от контакта 21 проводов двигателя с адаптерным кабелем разъёма к заземлению блока двигателя. | Более 10 миллионов ом | 2D |
|  | 2С-1 |  |

#### ШАГ 2C-1. Проверьте короткое замыкание, чтобы заземлиться в сигнале и вернуть провода.

| **Условия:** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините ESS от жгута проводов двигателя. Отсоедините проводку двигателя от проводов двигателя удлиняющие кабели. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта 22 с ремнем электропроводки двигателя до заземления блока двигателя. Измерьте сопротивление от контакта 21 с жгутом проводов двигателя до заземления блока двигателя. | Более 10 миллионов ом | 2D-1 |
| **Ремонт или замена электропроводки двигателя** Ремонт электропроводки двигателя ремня. См. Процедуры 019-202 и 019-240 в Руководстве по устранению неполадок и ремонту топливной системы QST серии QST30 G-Drive Engine, Бюллетень No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Замените жгут проводов двигателя. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3А |  |

#### ШАГ 2D. Проверьте короткое замыкание от пин-кодов до пин-кодов в адаптерном кабеле с жгутом двигателя и любых используемых удлинительных кабелей с жгутом двигателя.

| **Условия:** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от проводов двигателя удлиняющие кабели. Отсоедините ESS от жгута проводов двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта 22 разъёма ремня электропроводки двигателя со всеми другими штифтами в разъёме ремня электропроводки двигателя. Измерьте сопротивление от контакта 21 разъёма ремня электропроводки двигателя со всеми другими штифтами в разъёме ремня электропроводки двигателя. | Более 10 миллионов ом | 3А |
|  | 2D-1 |  |

#### ШАГ 2D-1. Проверьте короткое замыкание от пин-кодов до пин-кодов в адаптерном кабеле с жгутом двигателя и удлинительных кабелях с жгутом двигателя.

| **Условия:** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от адаптера ремня от ECM. Отсоедините провода двигателя от удлинителей упряжки от упряжи двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта 22 проводов двигателя с адаптерным кабелем и проводов двигателя с удлинительным кабелем на все другие штифты в применимом кабеле. Измерить сопротивление от контакта 21 проводов двигателя с помощью адаптера и проводов двигателя с помощью удлинителя провода ко всем другим штифтам в применимом кабеле. | Более 10 миллионов ом | 3А |
| **Починить или заменить адаптерный кабель или удлинительный кабель упряжки упряжки двигателя, в зависимости от того, что неисправно** Починить адаптерный кабель упряжки двигателя или удлинительный кабель упряжки двигателя. См. процедуру 019-240 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Замените адаптерный кабель или удлинительный кабель упряжки двигателя. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3А |  |

### ШАГ 3. Четкие коды ошибок.

#### ШАГ 3A. Четкие коды ошибок.

| **Условия:** Соединить все компоненты. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Код 115 с явным нарушением с использованием INSITETM, номер детали. 3825145. **Примечание:** Разъем шины данных CAN расположен на правом берегу корпуса маховика. | Код 115 ошибки обезврежен | Ремонт завершён |
| Смотрите соответствующие диаграммы устранения неполадок для любых оставшихся активных кодов неисправностей. | Перейдите к соответствующим диаграммам устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 115
>
> ### Engine Speed Sensor (ESS) Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 115 PID(P): SPN: FMI: Lamp: SRT: 00-681 | No engine speed detected between pins 21 and 22 of the engine harness connector. | Engine is shutdown and can **not** be run. Common Alarm output is energized. |
>
> ### Circuit Description
>
> The ESS circuit provides the engine speed signal to the electronic control module (ECM) through the engine harness.
>
> ### Component Location
>
> The ESS is located in the Flywheel Housing.
>
> ### Shoptalk
>
> - If the problem occurs at a certain engine temperature, be sure to check the ESS circuit while the engine is at that particular temperature.
>
> - Clean sensor tip; debris can cause intermittent signals.
>
> - The sensor **must** be adjusted properly to obtain a good signal. Make sure the sensor is ½ to ¾ turns out from contacting a flywheel tooth and that the locking nut is tight and properly torqued.
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
>
> **To avoid pin and harness damage, use the following test leads when taking a measurement: Part No. 3823996 - female Weather-Pack test lead Part No. 3822758 - male Deutsch/Metri-Pack test lead.**
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the ESS. |  |
> |  | **STEP 1A.** Inspect the ESS and the engine harness connector pins. | No damaged pins |
> |  | **STEP 1B.** Inspect the ESS. | No damaged ESS |
> |  | **STEP 1C.** Check for an open circuit in the ESS. | Less than 1500 ohms |
> |  | **STEP 1D.** Check for a short circuit to ground in the ESS. | More than 10M ohms |
> |  | **STEP 1E.** Check for a short circuit between coils of the ESS. | More than 10M ohms |
> | STEP 2. | Check the engine harness. |  |
> |  | **STEP 2A.** Inspect the engine harness and ECM connector pins. | No damaged pins |
> |  | **STEP 2A-1.** Inspect the engine harness adaptor cable and the engine harness extension cables. | No damaged pins |
> |  | **STEP 2B.** Check for an open circuit in the signal and return wires. | Less than 1500 ohms |
> |  | **STEP 2B-1.** Check for an open circuit in the engine harness adaptor cable and the engine harness extension cables. | Less than 10 ohms |
> |  | **STEP 2C.** Check for a short circuit to ground in the signal and return wires with the engine harness adaptor cable, and any extension cables used, installed. | More than 10M ohms |
> |  | **STEP 2C-1.** Check for a short circuit to ground in the engine harness signal and return wires. | More than 10M ohms |
> |  | **STEP 2D.** Check for a short circuit from the signal and return wires to all other wires in the engine harness. | More than 10M ohms |
> |  | **STEP 2D-1.** Check for a short circuit from pin to pin in the engine harness adaptor cable, and any engine harness extension cables used. | More than 10M ohms |
> | STEP 3. | Clear fault codes. |  |
> |  | **STEP 3A.** Clear fault codes. | All fault codes cleared |
>
> ### STEP 1. Check the ESS.
>
> #### STEP 1A. Inspect the ESS and engine harness connector pins.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the ESS from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | for the following: bent or broken pins pushed back or expanded pins corroded pins moisture in or on the connector. | No damaged pins | 1B |
> | **Repair the damaged pins** Repair or replace the engine harness or ESS, whichever has the damaged pins. Repair the engine harness. Refer to Procedure 19-202 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the ESS. Refer to Procedure 019-042 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3A |  |
>
> #### STEP 1B. Inspect the ESS.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the ESS from the engine harness. Remove the ESS. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | metal debris on the end of the sensor damage to the end of the sensor caused by contact with the flywheel oil leakage or insulation problems such as swelling damaged electrical potting in the sensing end of the sensor. | No damaged ESS | 1C |
> | **Clean or replace the ESS** Clean the ESS. Refer to Procedure 019-042 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the ESS. Refer to Procedure 019-042 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3A |  |
>
> #### STEP 1C. Check for an open circuit in the ESS.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the ESS from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure resistance from pin A to pin B of the first ESS coil. Measure resistance from pin A to pin B of the second ESS coil. | Less than 1500 ohms | 1D |
> | **Replace the ESS** Refer to Procedure 019-042 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3A |  |
>
> #### STEP 1D. Check for a short circuit to ground in the ESS.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the ESS from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure resistance from pin A of the first ESS coil to engine block ground. Measure resistance from pin A of the second ESS coil to engine block ground. | More than 10M ohms | 1E |
> | **Replace the ESS** Refer to Procedure 019-042 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3A |  |
>
> #### STEP 1E. Check for a short circuit between coils of the ESS.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect ESS from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure resistance from pin A of the first ESS coil to pin A of second ESS coil. | More than 10M ohms | 2A |
> | **Replace the ESS** Refer to Procedure 019-042 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3A |  |
>
> ### STEP 2. Check the engine harness.
>
> #### STEP 2A. Inspect engine harness and ECM.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | bent or broken pins pushed back or expanded pins corroded pins moisture in or on the connector. | No damaged pins | 2A-1 |
> | **Repair damaged pins** Repair or replace the engine harness adaptor cable or ECM, whichever has the damaged pins. Repair the engine harness adaptor cable. Refer to Procedure 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness adaptor cable. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the ECM. Refer to OEM procedures. | 3A |  |
>
> #### STEP 2A-1. Inspect engine harness connector and engine harness extension cables.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect engine harness extension cables from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | bent or broken pins pushed back or expanded pins corroded pins moisture in or on the connector. | No damaged pins | 2B |
> | **Repair damaged pins** Repair or replace the engine harness or engine harness extension cable, whichever has the damaged pins. Repair the engine harness or engine harness extension cable. Refer to Procedure 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness or engine harness extension cable. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3A |  |
>
> #### STEP 2B. Check for an open circuit in the signal and return wires.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable connector from the ECM. Connect the ESS to the engine harness. Connect the engine harness to the engine harness adaptor cable. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 22 to pin 21 of the 40 pin on the engine harness adaptor connector. | Less than 1500 ohms | 2C |
> |  | 2B-1 |  |
>
> #### STEP 2B-1. Check for an open circuit in the engine harness adaptor cable and engine harness extension cables.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable connector from the ECM. Disconnect the engine harness from the engine harness extension cable. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the continuity of pin 22 of each cable used between the engine harness and the ECM. Measure the continuity of pin 21 of each cable used between the engine harness and the ECM. | Less than 10 ohms Repair or replace the engine harness. Repair the engine harness. Refer to Procedures 019-202 and 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3A |
> | **Repair or replace the engine harness adaptor cable or an engine harness extension cable, whichever is found faulty** Repair the engine harness adaptor cable or an engine harness extension cable. Refer to Procedure 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness adaptor cable or an engine harness extension cable. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3A |  |
>
> #### STEP 2C. Check for a short circuit to ground in the signal and return wires with the engine harness adaptor cable, and any extension cables used, installed.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. Disconnect the ESS from the engine harness. Connect the engine harness to the engine harness adaptor cable. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 22 of the engine harness adaptor cable connector to engine block ground. Measure the resistance from pin 21 of the engine harness adaptor cable connector to engine block ground. | More than 10M ohms | 2D |
> |  | 2C-1 |  |
>
> #### STEP 2C-1. Check for a short circuit to ground in the signal and return wires.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the ESS from the engine harness. Disconnect the engine harness from the engine harness extension cables. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 22 of the engine harness to engine block ground. Measure the resistance from pin 21 of the engine harness to engine block ground. | More than 10M ohms | 2D-1 |
> | **Repair or replace the engine harness** Repair the engine harness. Refer to Procedures 019-202 and 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3A |  |
>
> #### STEP 2D. Check for a short circuit from pin to pin in the engine harness adaptor cable, and any engine harness extension cables used.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness from the engine harness extension cables. Disconnect the ESS from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 22 of the engine harness connector to all other pins in the engine harness connector. Measure the resistance from pin 21 of the engine harness connector to all other pins in the engine harness connector. | More than 10M ohms | 3A |
> |  | 2D-1 |  |
>
> #### STEP 2D-1. Check for a short circuit from pin to pin in the engine harness adaptor cable and the engine harness extension cables.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. Disconnect the engine harness extension cables from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 22 of the engine harness adaptor cable and engine harness extension cable to all other pins in the applicable cable. Measure the resistance from pin 21 of the engine harness adaptor cable and engine harness extension cable to all other pins in the applicable cable. | More than 10M ohms | 3A |
> | **Repair or replace the engine harness adaptor cable or the engine harness extension cable, whichever is faulty** Repair the engine harness adaptor cable or the engine harness extension cable. Refer to Procedure 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness adaptor cable or the engine harness extension cable. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3A |  |
>
> ### STEP 3. Clear fault codes.
>
> #### STEP 3A. Clear fault codes.
>
> | **Conditions:** Connect all components. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Clear Fault Code 115 using INSITE™, Part No. 3825145. **NOTE:** The datalink connector is located on the right bank of the flywheel housing. | Fault Code 115 cleared | Repair complete |
> | Refer to the appropriate troubleshooting charts for any remaining active fault codes. | Go to the appropriate troubleshooting charts |  |
