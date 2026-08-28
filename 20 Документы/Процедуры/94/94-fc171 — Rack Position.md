---
aliases:
  - "Положение рейки"
type: "Процедура"
doc: "94-fc171"
title_en: "Rack Position"
title_ru: "Положение рейки"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-fc171.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/94-fc171.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/94"
  - "перевод/машинный"
---

# Rack Position
**Положение рейки**

> [!abstract] Процедура · `94-fc171`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2003-03-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-fc171.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/94-fc171.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 171

### Положение рейки

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 171 PID(P): СПН: ФМИ: Лампа: СТО: | Неисправность стойки топливного насоса. Одна или обе из стойок топливного насоса левого или правого берега находятся **не** в управляемом положении. | Производительность может быть вялой или медленной, чтобы реагировать. Общий предупредительный выход активизируется. |

![[19a00011.png]]

### Описание цепи

Измеренные, опорные и общие сигналы схемы датчика положения стойки используются электронным модулем управления (ECM) для проверки того, что стойка была правильно расположена приводом стойки. Энергоснабжение привода и схемы возврата PWM используются ECM для привода привода в нужное положение.

### Расположение компонента

Датчик положения стойки расположен в губернаторском корпусе топливного насоса. Двигатель QST30 G-Drive имеет по одному на каждом двигателе.

### Практические замечания

- Код 171 ошибки будет записан, если измеренная позиция стойки для любого банка **не** в управляемой позиции стойки. Сначала определите, какой банк вызывает ошибку, а затем определите, какая часть этой схемы неисправна.

- Код 171 неисправности может быть записан, если стойка топливного насоса прилипает в одной конкретной точке в пределах пути его перемещения. Возможно, вам придется загрузить двигатель, чтобы активировать неисправность.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Определите, в каком банке виноваты. |  |
|  | **STEP 1A.** Проведите испытание стойки топливного насоса. | Измеренное напряжение соответствует показанию напряжения инструментальной обработки (±0,2 VDC) |
|  | **STEP 1A-1.** Мониторинг напряжений положения стойки во время работы двигателя. | Чтение напряжения при контактах B и C одинаково (±0,2 VDC) |
| ШАГ 2. | Проверьте жгут электропроводки двигателя. |  |
|  | **STEP 2A.** Проверить проводку двигателя с помощью адаптерного кабеля и контактов разъема ECM. | Никаких поврежденных контактов |
|  | **STEP 2A-1.** Проверить контакты разъёма проводов двигателя и топливного насоса. | Никаких поврежденных контактов |
|  | **STEP 2A-2.** Проверить разъем для проводов двигателя и любой используемый кабель для расширения проводов двигателя. | Никаких поврежденных контактов |
|  | **STEP 2B.** Проверьте датчик положения стойки и схемы привода стойки для короткого замыкания от пин-кодов до пин-кодов. | Более 100 тыс. ом |
|  | **STEP 2B-1.** Проверьте короткое замыкание от штифта до штифта в кабеле адаптера жгута двигателя и любом используемом кабеле расширения жгута двигателя. | Более 100 тыс. ом |
|  | **STEP 2C.** Проверьте контуры срабатывания стойки и привода стойки на наличие открытой цепи. | Менее 10 Ом |
|  | **STEP 2C-1.** Проверьте наличие открытой цепи в кабеле адаптера жгута двигателя и любом используемом кабеле расширения жгута двигателя. | Менее 10 Ом |
|  | **STEP 2D.** Проверьте датчик положения стойки и цепи привода стойки для короткого замыкания на землю. | Более 100 тыс. ом |
|  | **STEP 2D-1.** Проверьте короткое замыкание в ремне электропроводки двигателя. | Более 100 тыс. ом |
| ШАГ 3. | Проверьте привод стойки. |  |
|  | **STEP 3A.** Проверьте сопротивление катушки привода стоек. | 0,55 - 0,90 Ом |
|  | **STEP 3B.** Проверить движение стойки. | Полный диапазон движения стойки |
| ШАГ 4. | Проверьте датчик положения стойки. |  |
|  | **STEP 4A.** Проверить сопротивление катушки датчика положения стойки. | 17-23 Ом |
|  | **STEP 4B.** Проверить сопротивление стойки расположения датчика опорной катушки. | 17-23 Ом |
| ШАГ 5. | Проверьте ECM. |  |
|  | **STEP 5A.** Проверьте стойки расположения датчиков сигнала на соответствующие уровни напряжения. | 2.4-2.6 VDC |
| ШАГ 6. | Очистите код ошибки. |  |
|  | **STEP 6A.** Отключить код ошибки. | Код 171 неактивный |
|  | **STEP 6B.** Чистые коды неактивных ошибок. | Все ошибки устранены |

### ШАГ 1. Определите, в каком банке виноваты.

#### ШАГ 1A. Проведите тест стойки топливного насоса.

| **Условия:** Переключатель стоп/бега в положении «стоп». Контроллер в диагностическом режиме. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Использование INSITETM, номер детали. 3825145, выполнить испытание стойки топливного насоса. Постепенно наклоняйте стойку топливного насоса от ее нижнего предела проезда (0 мм) до максимального предела проезда (20 мм) при считывании напряжения от контакта B до контакта A на диагностическом разъеме для топливного насоса левого берега. Постепенно наклоняйте стойку топливного насоса от ее нижнего предела проезда (0 мм) до максимального предела проезда (20 мм) при считывании напряжения от контакта C до контакта A на диагностическом разъеме для топливного насоса правого берега. | Измеренное напряжение соответствует напряжениям положения стойки, указанным сервисной оснасткой (±0,2 VDC) | 1А-1-1 |
| Применяйте следующие шаги (шаг 2А) для банка двигателя по ошибке. | 2А |  |

#### ШАГ 1A-1. Контролируйте напряжения положения стойки, пока двигатель работает.

| **Условия:** Переключатель стоп/бега в положении «РУН». |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Прочитайте напряжения на диагностических соединительных контактах B (топливный насос левого берега) для контакта A (наземный) и контакта C (топливный насос правого берега) для контакта A (наземный) при различных уровнях нагрузки двигателя. | Показания напряжения между контактами А и В идентичны (±0,2 VDC) при заданном состоянии нагрузки, и оба показания напряжения колеблются с различными условиями нагрузки (заправки). | 6А |
|  | 2А |  |

### ШАГ 2. Проверьте жгут электропроводки двигателя.

#### ШАГ 2A. Проверьте проводку двигателя, адаптерный кабель и контакты разъема ECM.

| **Условия:** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от адаптера ремня от ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| согнутые или сломанные штифты отодвигаются назад или расширенные штифты разъедают штифты влагой в или на разъеме. | Никаких поврежденных контактов | 2А-1-1 |
| **Починить поврежденные контакты** Починить или заменить проводку двигателя на адаптерный кабель или ECM, в зависимости от того, какие контакты повреждены. Ремонт проводов двигателя с помощью адаптера кабеля. См. процедуру 019-240 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Замените проводку двигателя адаптерным кабелем. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Заменить ECM. См. процедуры OEM. Высушить разъем с помощью электрического контактного очистителя, номер детали. 3824510. | 6А |  |

#### ШАГ 2A-1. Проверьте контакты разъёма проводов двигателя и топливного насоса.

| **Условия:** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините разъём ремня электропроводки двигателя от топливного насоса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| согнутые или сломанные штифты отодвигаются назад или расширенные штифты разъедают штифты влагой в или на разъеме. | Никаких поврежденных контактов | 2А-2 |
| **Починить поврежденные контакты** Починить или заменить ремень электропроводки двигателя или топливный насос в зависимости от того, какие контакты повреждены. Ремонт ремня электропроводки двигателя. См. процедуру 019-209 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Замените жгут проводов двигателя. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Замените топливный насос. См. Руководство по устранению неполадок и ремонту базового двигателя. Высушить разъем с помощью электрического контактного очистителя, номер детали. 3824510. | 6А |  |

#### ШАГ 2A-2. Проверьте разъем для проводов двигателя и любой используемый кабель расширения для проводов двигателя.

| **Условия:** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините разъем жгута проводов двигателя от проводов удлинителя (расширителей) проводов двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| согнутые или сломанные штифты отодвигаются назад или расширенные штифты разъедают штифты влагой в или на разъеме. | Никаких поврежденных контактов | 2В |
| **Починить поврежденные контакты** Починить или заменить упряжку для проводов двигателя или удлинитель (расширительные кабели) упряжки двигателя, в зависимости от того, какие контакты повреждены. Ремонт ремня проводов двигателя или проводов двигателя удлинитель (ы) провода удлинителя (ов). См. процедуру 019-209 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Заменить упряжку или удлинитель (расширительные кабели) упряжки двигателя. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Высушить разъем с помощью электрического контактного очистителя, номер детали. 3824510. | 6А |  |

#### ШАГ 2B. Проверьте датчик положения стойки и схемы привода стойки для короткого замыкания от пин-кодов до пин-кодов.

| **Условия:** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от адаптера ремня от ECM. Отсоедините разъём ремня электропроводки двигателя от топливного насоса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта 5 (контакт 10 для правильного топливного насоса) проводов двигателя с помощью адаптера разъёма кабеля к другим штифтам в разъеме. Измерьте сопротивление от контакта 3 (контакт 4 для правильного топливного насоса) проводов двигателя, подключите адаптерный кабель к другим штифтам в разъеме. Измерьте сопротивление от контакта 6 (контакт 9 для правильного топливного насоса) проводов двигателя с помощью адаптера разъёма кабеля к другим штифтам в разъеме. Измерьте сопротивление от контакта 7 (контакт 8 для правильного топливного насоса) проводов двигателя с помощью адаптера разъёма кабеля к другим штифтам в разъеме. Измерьте сопротивление от контакта 1 (контакт 2 для правильного топливного насоса) проводов двигателя с помощью адаптера разъёма кабеля к другим штифтам в разъеме. | Более 100 тыс. ом | 2C |
|  | 2В-1-1 |  |

#### ШАГ 2B-1. Проверьте короткое замыкание от пин-кодов до пин-кодов в адаптерном кабеле с жгутом двигателя и любом используемом кабеле расширения с жгутом двигателя.

| **Условия:** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от проводов двигателя удлинитель (ы) удлинителя (ов) упряжки. Отсоедините проводку двигателя от адаптера ремня от ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта 5 (контакт 10 для правильного топливного насоса) кабельного разъема адаптера жгута двигателя и любого разъема удлинителя провода двигателя к другим штифтам в разъеме. Измерьте сопротивление от контакта 3 (контакт 4 для правильного топливного насоса) кабеля адаптера проводов двигателя и любого кабеля удлинителя проводов двигателя к другим штифтам в разъеме. Измерьте сопротивление от контакта 6 (контакт 9 для правильного топливного насоса) кабеля адаптера проводов двигателя и любого кабеля удлинителя проводов двигателя к другим штифтам в разъеме. Измерьте сопротивление от контакта 7 (контакт 8 для правильного топливного насоса) кабеля адаптера проводов двигателя и любого кабеля удлинителя проводов двигателя к другим штифтам в разъеме. Измерьте сопротивление от контакта 1 (контакт 2 для правильного топливного насоса) кабеля адаптера проводов двигателя и любого кабеля удлинителя проводов двигателя к другим штифтам в разъеме. | Более 100k Ом Ремонт или замена электропроводки двигателя Ремонт электропроводки двигателя ремня. См. процедуру 019-209 или 019-240 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Замените жгут проводов двигателя. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 6А |
| **Починить или заменить кабель адаптера или удлинитель (расширители) упряжки упряжки двигателя или проводку двигателя, в зависимости от того, что признано неисправным** Починить адаптер упряжки двигателя или удлинитель (расширители) упряжки двигателя. См. процедуру 019-209 или 019-240 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Заменить проводку двигателя адаптерным кабелем или проводкой двигателя удлинительным кабелем (расширительными кабелями). См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 6А |  |

#### ШАГ 2C. Проверьте датчик положения стойки и схемы привода стойки для открытой цепи.

| **Условия:** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините разъём ремня электропроводки двигателя от топливного насоса. Отсоедините проводку двигателя от адаптера ремня от ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта 5 (контакт 10 для топливного насоса правого берега) на разъёме адаптера жгута проводов двигателя для контакта E на стороне ремня электропроводки разъема топливного насоса. Измерьте сопротивление от контакта 3 (контакт 4 для топливного насоса правого берега) на разъёме адаптера жгута проводов двигателя для контакта G на стороне ремня электропроводки разъема топливного насоса. Измерьте сопротивление от контакта 6 (контакт 9 для топливного насоса правого берега) на разъёме адаптера жгута проводов двигателя к контакту F на стороне ремня электропроводки разъема топливного насоса. Измерьте сопротивление от контакта 7 (контакт 8 для топливного насоса правого берега) на разъёме адаптера жгута проводов двигателя для контакта А на стороне ремня электропроводки разъема топливного насоса. Измерьте сопротивление от контакта 1 (контакт 2 для топливного насоса правого берега) на разъёме адаптера жгута проводов двигателя к контакту B на стороне ремня электропроводки разъема топливного насоса. | Менее 10 Ом | 2D |
|  | 2С-1 |  |

#### ШАГ 2C-1. Проверьте наличие открытой цепи в кабеле адаптера жгута двигателя и любом используемом кабеле расширения жгута двигателя.

| **Условия:** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините разъем жгута проводов двигателя от проводов удлинителя (расширителей) проводов двигателя. Отсоедините проводку двигателя от адаптера ремня от ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте непрерывность контакта 5 (контакт 10 для топливного насоса правого берега) на адаптерном кабеле ремня электропроводки двигателя и любых используемых удлинительных кабелей ремня электропроводки двигателя. Измерьте непрерывность контакта 3 (контакт 4 для топливного насоса правого берега) на адаптерном кабеле ремня электропроводки двигателя и любых используемых удлинительных кабелей ремня электропроводки двигателя. Измерьте непрерывность контакта 6 (контакт 9 для топливного насоса правого берега) на адаптерном кабеле ремня электропроводки двигателя и любых используемых удлинительных кабелей ремня электропроводки двигателя. Измерьте непрерывность контакта 7 (контакт 8 для топливного насоса правого берега) на адаптерном кабеле ремня электропроводки двигателя и любых используемых удлинительных кабелей ремня электропроводки двигателя. Измерьте непрерывность контакта 1 (контакт 2 для топливного насоса правого берега) на адаптерном кабеле ремня электропроводки двигателя и любых используемых удлинительных кабелей ремня электропроводки двигателя. | Менее 10 Ом Ремонт или замена электропроводки двигателя Ремонт электропроводки двигателя ремня. См. процедуру 019-209 или 019-240 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Замените жгут проводов двигателя. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 6А |
| **Починить или заменить кабель адаптера или удлинитель (расширители) упряжки упряжки двигателя или проводку двигателя, в зависимости от того, что признано неисправным** Починить адаптер упряжки двигателя или удлинитель (расширители) упряжки двигателя. См. процедуру 019-209 или 019-240 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Заменить проводку двигателя адаптерным кабелем или проводкой двигателя удлинительным кабелем (расширительными кабелями). См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 6А |  |

#### ШАГ 2D. Проверьте датчик положения стойки и схемы привода стойки для короткого замыкания на землю.

| **Условия:** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от адаптера ремня от ECM. Отсоедините разъём ремня электропроводки двигателя от топливного насоса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта 5 (контакт 10 для правильного берег топливного насоса) на проводах двигателя адаптерного кабеля к блоку двигателя. Измерьте сопротивление от контакта 3 (контакт 4 для топливного насоса правого берега) на проводах двигателя, подключите адаптерный кабель к блоку двигателя. Измерьте сопротивление от контакта 6 (контакт 9 для топливного насоса правого берега) на проводах двигателя, подключите адаптерный кабель к блоку двигателя. Измерьте сопротивление от контакта 7 (контакт 8 для топливного насоса правого берега) на проводах двигателя, подключите адаптерный кабель к блоку двигателя. Измерьте сопротивление от контакта 1 (контакт 2 для правого берег топливного насоса) на проводах двигателя адаптерного кабеля к блоку двигателя. | Больше 100k Ом | 3А |
|  | 2D-1 |  |

#### ШАГ 2D-1. Проверьте короткое замыкание, чтобы заземлиться в ремне электропроводки двигателя.

| **Условия:** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините разъем жгута проводов двигателя от проводов удлинителя (расширителей) проводов двигателя. Отсоедините разъём ремня электропроводки двигателя от топливного насоса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта 5 (контакт 10 для топливного насоса правого берега) на разъёме ремня электропроводки двигателя к заземлению блока двигателя. Измерьте сопротивление от контакта 3 (контакт 4 для топливного насоса правого берега) на разъёме ремня электропроводки двигателя к заземлению блока двигателя. Измерьте сопротивление от контакта 6 (контакт 9 для топливного насоса правого берега) на разъёме ремня электропроводки двигателя к заземлению блока двигателя. Измерьте сопротивление от контакта 7 (контакт 8 для топливного насоса правого берега) на разъёме ремня электропроводки двигателя к заземлению блока двигателя. Измерьте сопротивление от контакта 1 (контакт 2 для правого берег топливного насоса) на разъёме ремня электропроводки двигателя к заземлению блока двигателя. | Больше 100k Ом | 3А |
| **Ремонт или замена электропроводки двигателя** Ремонт электропроводки двигателя ремня. См. процедуру 019-209 или 019-240 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Замените жгут проводов двигателя. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 6А |  |

### ШАГ 3. Проверьте привод стойки.

#### ШАГ 3A. Проверьте сопротивление катушки привода стойки.

| **Условия:** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините разъём ремня электропроводки двигателя от топливного насоса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление от контакта В до контакта G разъема топливного насоса. | Менее 10 Ом | 3B |
| **Заменить топливный насос** См. Руководство по устранению неполадок и ремонту базового двигателя. | 6А |  |

#### ШАГ 3B. Проверить движение стойки

| **Условия:** Переключатель стоп/бега в положении «стоп». Контроллер в диагностическом режиме. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Использование INSITETM, номер детали. 3825145, выполнить тест на движение стойки. Включить верхние и нижние пределы положения стойки топливного насоса. Снимите крышку на передней части топливного насоса и проверьте движение стойки. **Примечание:** Если крышка топливного насоса недоступна для визуальной проверки движения стойки, пройдите этапы 4 и 5 перед удалением топливного насоса. | Полный диапазон движения стойки | 4А |
| **Заменить топливный насос** См. Руководство по устранению неполадок и ремонту базового двигателя. | 6А |  |

### ШАГ 4. Проверьте датчик положения стойки.

#### ШАГ 4A. Проверить сопротивление катушки датчика положения стойки.

| **Условия:** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините разъём ремня электропроводки двигателя от топливного насоса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта Е до контакта F разъема топливного насоса. | 17-23 Ом | 4B |
| **Заменить топливный насос** См. Руководство по устранению неполадок и ремонту базового двигателя. | 6А |  |

#### ШАГ 4B. Проверить сопротивление стойки датчика положения опорной катушки.

| **Условия:** Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините разъём ремня электропроводки двигателя от топливного насоса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта А до контакта F разъема топливного насоса. | 17-23 Ом | 5а |
| **Заменить топливный насос** См. Руководство по устранению неполадок и ремонту базового двигателя. | 6А |  |

### ШАГ 5. Проверьте ECM

#### ШАГ 5A. Проверьте стойку положения датчика сигнала для правильного напряжения.

| **Условия:** Переключатель стоп/бега в положении «стоп». Контроллер в диагностическом режиме. Отсоедините электропроводку двигателя от топливного насоса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте напряжение сигнала от контакта А на проводной стороне ремня разъема топливного насоса до земли. Измерьте напряжение сигнала от контакта Е на проводной стороне ремня разъема топливного насоса до земли. Измерьте напряжение сигнала от контакта F на проводной стороне ремня разъема топливного насоса до земли. | 2.4-2.6 VDC | 6А |
| **Заменить ECM** См. процедуры ОЕМ. | 6А |  |

### ШАГ 6. Очистите код ошибки.

#### ШАГ 6A. Отключите код неисправности.

| **Условия:** Соединить все компоненты. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Подключите все компоненты, запустите двигатель и запустите его на холостом ходу в течение одной минуты, чтобы убедиться, что код 171 неактивен. | Код 171 неактивный | 6B |
| Вернитесь к шагам устранения неполадок или свяжитесь с вашим местным авторизованным ремонтным центром Cummins, если все шаги были завершены и проверены снова. | 1А |  |

#### ШАГ 6B. Сбросьте неактивные коды неисправностей.

| **Условия:** Соединить все компоненты. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Стирать неактивные коды неисправностей с помощью INSITETM, номер детали. 3825145. **Примечание:** Разъем шины данных CAN расположен на правом берегу корпуса маховика. | Все ошибки устранены | Ремонт завершён |
| **Устранение неполадок с оставшимися активными кодами ошибок.** | Соответствующая диаграмма устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 171
>
> ### Rack Position
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 171 PID(P): SPN: FMI: Lamp: SRT: | Fuel pump rack position fault. One or both of the left bank or right bank fuel pump racks is **not** at the commanded position. | Performance could be sluggish or slow to respond. Common Warning output is energized. |
>
> ### Circuit Description
>
> The rack position sensor circuit's measured, reference and common signals are used by the electronic control module (ECM) to verify that the rack has been properly positioned by the rack actuator. The actuator power supply and PWM return circuits are used by the ECM to drive the actuator to the desired position.
>
> ### Component Location
>
> The rack position sensor is located in the governor housing of the fuel pump. The QST30 G-Drive engine has one on each engine bank.
>
> ### Shoptalk
>
> - Fault Code 171 will be recorded if the measured rack position for either bank is **not** at commanded rack position. First determine which bank is causing the error, then determine what part of that circuit is at fault.
>
> - Fault Code 171 may be recorded if the fuel pump rack is sticking at one particular point within its travel path. You may need to load the engine to make the fault go active.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Determine which bank is at fault. |  |
> |  | **STEP 1A.** Perform fuel pump rack test. | The measured voltage matches the service tool voltage reading (±0.2 VDC) |
> |  | **STEP 1A-1.** Monitor the rack position voltages while the engine is in operation. | Voltage reading at pins B and C are identical (±0.2 VDC) |
> | STEP 2. | Check engine harness. |  |
> |  | **STEP 2A.** Inspect engine harness adaptor cable and ECM connector pins. | No damaged pins |
> |  | **STEP 2A-1.** Inspect engine harness and fuel pump connector pins. | No damaged pins |
> |  | **STEP 2A-2.** Inspect engine harness connector and any engine harness extension cable used. | No damaged pins |
> |  | **STEP 2B.** Check rack position sensor and rack actuator circuits for short circuit from pin to pin. | More than 100k ohms |
> |  | **STEP 2B-1.** Check for a short circuit from pin to pin in the engine harness adaptor cable and any engine harness extension cable used. | More than 100k ohms |
> |  | **STEP 2C.** Check rack position sensor and rack actuator circuits for an open circuit. | Less than 10 ohms |
> |  | **STEP 2C-1.** Check for an open circuit in the engine harness adaptor cable and any engine harness extension cable used. | Less than 10 ohms |
> |  | **STEP 2D.** Check rack position sensor and rack actuator circuits for short circuit to ground. | More than 100k ohms |
> |  | **STEP 2D-1.** Check for short circuit to ground in the engine harness. | More than 100k ohms |
> | STEP 3. | Check rack actuator. |  |
> |  | **STEP 3A.** Check the resistance of rack actuator coil. | 0.55 to 0.90 ohms |
> |  | **STEP 3B.** Verify rack movement. | Full range of rack movement |
> | STEP 4. | Check rack position sensor. |  |
> |  | **STEP 4A.** Check resistance of rack position sensor coil. | 17 to 23 ohms |
> |  | **STEP 4B.** Check resistance of rack position sensor reference coil. | 17 to 23 ohms |
> | STEP 5. | Check ECM. |  |
> |  | **STEP 5A.** Check rack position sensor signal pins for proper voltage levels. | 2.4 to 2.6 VDC |
> | STEP 6. | Clear the fault code. |  |
> |  | **STEP 6A.** Disable the fault code. | Fault Code 171 inactive |
> |  | **STEP 6B.** Clear inactive fault codes. | All faults cleared |
>
> ### STEP 1. Determine which bank is at fault.
>
> #### STEP 1A. Perform fuel pump rack test.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller in the diagnostic mode. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Using INSITE™, Part No. 3825145, perform fuel pump rack test. Gradually ramp the fuel pump rack from it's lower limit of travel (0 mm) to it's maximum limit of travel (20 mm) while reading the voltage from pin B to pin A at the diagnostic connector for the left bank fuel pump. Gradually ramp the fuel pump rack from it's lower limit of travel (0 mm) to it's maximum limit of travel (20 mm) while reading the voltage from pin C to pin A at the diagnostic connector for the right bank fuel pump. | The measured voltage matches the rack position voltages as indicated by the service tool (±0.2 VDC) | 1A-1 |
> | Proceed with the following steps (Step 2A) for the engine bank in error. | 2A |  |
>
> #### STEP 1A-1. Monitor the rack position voltages while the engine is in operation.
>
> | **Conditions:** Stop/Run switch in the "RUN" position. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Read the voltages at the diagnostic connector pins B (left bank fuel pump) to pin A (ground) and pin C (right bank fuel pump) to pin A (ground) at various levels of engine load. | Voltage readings between pins A and B are identical (±0.2 VDC) at a given load condition and both voltage reading fluctuate with varying load (fueling) conditions. | 6A |
> |  | 2A |  |
>
> ### STEP 2. Check engine harness.
>
> #### STEP 2A. Inspect engine harness adaptor cable and ECM connector pins.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | bent or broken pins pushed back or expanded pins corroded pins moisture in or on the connector. | No damaged pins | 2A-1 |
> | **Repair the damaged pins** Repair or replace the engine harness adaptor cable or the ECM, whichever has the damaged pins. Repair the engine harness adaptor cable. Refer to Procedure 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness adaptor cable. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the ECM. Refer to OEM procedures. Dry the connector by using electrical contact cleaner, Part No. 3824510. | 6A |  |
>
> #### STEP 2A-1. Inspect engine harness and fuel pump connector pins.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness connector from the fuel pump. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | bent or broken pins pushed back or expanded pins corroded pins moisture in or on the connector. | No damaged pins | 2A-2 |
> | **Repair the damaged pins** Repair or replace the engine harness or the fuel pump whichever has the damaged pins. Repair the engine harness. Refer to Procedure 019-209 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the fuel pump. Refer to Base Engine Troubleshooting and Repair Manual. Dry the connector by using electrical contact cleaner, Part No. 3824510. | 6A |  |
>
> #### STEP 2A-2. Inspect engine harness connector and any engine harness extension cable used.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness connector from the engine harness extension cable(s). |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | bent or broken pins pushed back or expanded pins corroded pins moisture in or on the connector. | No damaged pins | 2B |
> | **Repair the damaged pins** Repair or replace the engine harness or the engine harness extension cable(s), whichever has the damaged pins. Repair the engine harness or the engine harness extension cable(s). Refer to Procedure 019-209 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness or the engine harness extension cable(s). Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Dry the connector by using electrical contact cleaner, Part No. 3824510. | 6A |  |
>
> #### STEP 2B. Check rack position sensor and rack actuator circuits for short circuit from pin to pin.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. Disconnect the engine harness connector from the fuel pump. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 5 (pin 10 for the right fuel pump) of the engine harness adaptor cable connector to all other pins in the connector. Measure the resistance from pin 3 (pin 4 for the right fuel pump) of the engine harness adaptor cable connector to all other pins in the connector. Measure the resistance from pin 6 (pin 9 for the right fuel pump) of the engine harness adaptor cable connector to all other pins in the connector. Measure the resistance from pin 7 (pin 8 for the right fuel pump) of the engine harness adaptor cable connector to all other pins in the connector. Measure the resistance from pin 1 (pin 2 for the right fuel pump) of the engine harness adaptor cable connector to all other pins in the connector. | More than 100k ohms | 2C |
> |  | 2B-1 |  |
>
> #### STEP 2B-1. Check for a short circuit from pin to pin in the engine harness adaptor cable and any engine harness extension cable used.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness from the engine harness extension cable(s). Disconnect the engine harness adaptor cable from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 5 (pin 10 for the right fuel pump) of the engine harness adaptor cable connector and any engine harness extension cable connector to all other pins in the connector. Measure the resistance from pin 3 (pin 4 for the right fuel pump) of the engine harness adaptor cable connector and any engine harness extension cable connector to all other pins in the connector. Measure the resistance from pin 6 (pin 9 for the right fuel pump) of the engine harness adaptor cable connector and any engine harness extension cable connector to all other pins in the connector. Measure the resistance from pin 7 (pin 8 for the right fuel pump) of the engine harness adaptor cable connector and any engine harness extension cable connector to all other pins in the connector. Measure the resistance from pin 1 (pin 2 for the right fuel pump) of the engine harness adaptor cable connector and any engine harness extension cable connector to all other pins in the connector. | More than 100k ohms Repair or replace the engine harness Repair the engine harness. Refer to Procedure 019-209 or 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 6A |
> | **Repair or replace the engine harness adaptor cable or engine harness extension cable(s), whichever is found faulty** Repair the engine harness adaptor cable or engine harness extension cable(s). Refer to Procedure 019-209 or 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness adaptor cable or engine harness extension cable(s). Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 6A |  |
>
> #### STEP 2C. Check rack position sensor and rack actuator circuits for an open circuit.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness connector from the fuel pump. Disconnect the engine harness adaptor cable from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 5 (pin 10 for the right bank fuel pump) on the engine harness adaptor cable connector to pin E on the harness side of the fuel pump connector. Measure the resistance from pin 3 (pin 4 for the right bank fuel pump) on the engine harness adaptor cable connector to pin G on the harness side of the fuel pump connector. Measure the resistance from pin 6 (pin 9 for the right bank fuel pump) on the engine harness adaptor cable connector to pin F on the harness side of the fuel pump connector. Measure the resistance from pin 7 (pin 8 for the right bank fuel pump) on the engine harness adaptor cable connector to pin A on the harness side of the fuel pump connector. Measure the resistance from pin 1 (pin 2 for the right bank fuel pump) on the engine harness adaptor cable connector to pin B on the harness side of the fuel pump connector. | Less than 10 ohms | 2D |
> |  | 2C-1 |  |
>
> #### STEP 2C-1. Check for an open circuit in the engine harness adaptor cable and any engine harness extension cable used.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness connector from the engine harness extension cable(s). Disconnect the engine harness adaptor cable from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the continuity for pin 5 (pin 10 for the right bank fuel pump) on the engine harness adaptor cable and any engine harness extension cables used. Measure the continuity for pin 3 (pin 4 for the right bank fuel pump) on the engine harness adaptor cable and any engine harness extension cables used. Measure the continuity for pin 6 (pin 9 for the right bank fuel pump) on the engine harness adaptor cable and any engine harness extension cables used. Measure the continuity for pin 7 (pin 8 for the right bank fuel pump) on the engine harness adaptor cable and any engine harness extension cables used. Measure the continuity for pin 1 (pin 2 for the right bank fuel pump) on the engine harness adaptor cable and any engine harness extension cables used. | Less than 10 ohms Repair or replace the engine harness Repair the engine harness. Refer to Procedure 019-209 or 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 6A |
> | **Repair or replace the engine harness adaptor cable or engine harness extension cable(s), whichever is found faulty** Repair the engine harness adaptor cable or engine harness extension cable(s). Refer to Procedure 019-209 or 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness adaptor cable or engine harness extension cable(s). Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 6A |  |
>
> #### STEP 2D. Check rack position sensor and rack actuator circuits for short circuit to ground.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. Disconnect the engine harness connector from the fuel pump. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 5 (pin 10 for the right bank fuel pump) on the engine harness adaptor cable to engine block ground. Measure the resistance from pin 3 (pin 4 for the right bank fuel pump) on the engine harness adaptor cable to engine block ground. Measure the resistance from pin 6 (pin 9 for the right bank fuel pump) on the engine harness adaptor cable to engine block ground. Measure the resistance from pin 7 (pin 8 for the right bank fuel pump) on the engine harness adaptor cable to engine block ground. Measure the resistance from pin 1 (pin 2 for the right bank fuel pump) on the engine harness adaptor cable to engine block ground. | Greater than 100k ohms | 3A |
> |  | 2D-1 |  |
>
> #### STEP 2D-1. Check for short circuit to ground in the engine harness.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness connector from the engine harness extension cable(s). Disconnect the engine harness connector from the fuel pump. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 5 (pin 10 for the right bank fuel pump) on the engine harness connector to engine block ground. Measure the resistance from pin 3 (pin 4 for the right bank fuel pump) on the engine harness connector to engine block ground. Measure the resistance from pin 6 (pin 9 for the right bank fuel pump) on the engine harness connector to engine block ground. Measure the resistance from pin 7 (pin 8 for the right bank fuel pump) on the engine harness connector to engine block ground. Measure the resistance from pin 1 (pin 2 for the right bank fuel pump) on the engine harness connector to engine block ground. | Greater than 100k ohms | 3A |
> | **Repair or replace the engine harness** Repair the engine harness. Refer to Procedure 019-209 or 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 6A |  |
>
> ### STEP 3. Check rack actuator.
>
> #### STEP 3A. Check the resistance of the rack actuator coil.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness connector from the fuel pump. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin B to pin G of the fuel pump connector. | Less than 10 ohms | 3B |
> | **Replace the fuel pump** Refer to Base Engine Troubleshooting and Repair Manual. | 6A |  |
>
> #### STEP 3B. Verify rack movement
>
> | **Conditions:** Stop/Run switch in the "STOP” position. Controller in the diagnostic mode. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Using INSITE™, Part No. 3825145, perform a rack movement test. Insert upper and lower limits of fuel pump rack positions. Remove the cap on the front of the fuel pump and verify rack movement. **Note:** If the cap on the fuel pump is **not** accessible for visual verification of rack movement, proceed with steps 4 and 5 prior to removing the fuel pump. | Full range of rack movement | 4A |
> | **Replace the fuel pump** Refer to Base Engine Troubleshooting and Repair Manual. | 6A |  |
>
> ### STEP 4. Check rack position sensor.
>
> #### STEP 4A. Check resistance of rack position sensor coil.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness connector from the fuel pump. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin E to pin F of the fuel pump connector. | 17 to 23 ohms | 4B |
> | **Replace the fuel pump** Refer to Base Engine Troubleshooting and Repair Manual. | 6A |  |
>
> #### STEP 4B. Check resistance of rack position sensor reference coil.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness connector from the fuel pump. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin A to pin F of the fuel pump connector. | 17 to 23 ohms | 5A |
> | **Replace the fuel pump** Refer to Base Engine Troubleshooting and Repair Manual. | 6A |  |
>
> ### STEP 5. Check ECM
>
> #### STEP 5A. Check rack position sensor signal pins for proper voltage.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller in the diagnostic mode. Disconnect engine harness from fuel pump. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the signal voltage from pin A on the harness side of the fuel pump connector to ground. Measure the signal voltage from pin E on the harness side of the fuel pump connector to ground. Measure the signal voltage from pin F on the harness side of the fuel pump connector to ground. | 2.4 to 2.6 VDC | 6A |
> | **Replace the ECM** Refer to OEM procedures. | 6A |  |
>
> ### STEP 6. Clear the fault code.
>
> #### STEP 6A. Disable the fault code.
>
> | **Conditions:** Connect all components. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | connect all components start the engine and let it idle for one minute verify Fault Code 171 is inactive. | Fault Code 171 inactive | 6B |
> | Return to troubleshooting steps or contact your local Cummins Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
>
> #### STEP 6B. Clear the inactive fault codes.
>
> | **Conditions:** Connect all components. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Erase the inactive fault codes using INSITE™, Part No. 3825145. **NOTE:** The datalink connector is located on the right bank of the flywheel housing. | All faults cleared | Repair complete |
> | **Troubleshoot any remaining active fault codes.** | Appropriate troubleshooting chart |  |
