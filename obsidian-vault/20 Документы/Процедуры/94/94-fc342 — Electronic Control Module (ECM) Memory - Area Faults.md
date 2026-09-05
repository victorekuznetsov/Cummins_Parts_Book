---
aliases:
  - "Память ЭБУ — неисправности областей"
type: "Процедура"
doc: "94-fc342"
title_en: "Electronic Control Module (ECM) Memory - Area Faults"
title_ru: "Память ЭБУ — неисправности областей"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-fc342.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/94-fc342.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/94"
  - "перевод/машинный"
---

# Electronic Control Module (ECM) Memory - Area Faults
**Память ЭБУ — неисправности областей**

> [!abstract] Процедура · `94-fc342`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2003-03-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-fc342.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/94-fc342.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 342 или 346

### Память ЭБУ — неисправности областей

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 342 или 346 PID(P): СПН: ФМИ: Лампа: СТО: | FC 342 - ECM обнаружил ошибку суммы проверки памяти в памяти, содержащей критические параметры двигателя. FC 346 - ECM обнаружил ошибку суммы проверки памяти в памяти, содержащей некритические параметры двигателя. | FC 342 - двигатель отключается. Общий выход сигнализации активизирован. FC 346 - нет ни одного выступления. Общий предупредительный выход активизируется. **Примечание: **Данные ECM могут быть потеряны, включая данные кода неисправности, регулируемые параметры параметров, время ECM и время работы двигателя. |

![[19a00014.png]]

### Описание цепи

QST30 G-Drive ECM - это компьютер, который отвечает за управление двигателем, диагностику и функции двигателя.

### Расположение компонента

QST30 G-Drive ECM устанавливается генераторной установкой OEM. Обычно его можно найти рядом с панелью утилиты генератора.

### Практические замечания

Это связано с внутренней памятью ECM. Эта неисправность может быть вызвана прерыванием питания ECM или потерей мощности батареи. Для устранения неисправности может потребоваться частичная или основная перезагрузка контроллера.

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
>

**Чтобы избежать повреждения штифта и проводов, используйте следующий испытательный щуп при проведении измерения: Часть нет. 3822758 - пробный щуп типа пробки Deutsch/Cannon/Metri-Pack**

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте систему батарей оборудования. |  |
|  | **STEP 1A.** Проверить соединения кабеля аккумулятора. | Нет поврежденных соединений |
|  | **ШАГ 1В.** Проверьте напряжение батареи. | 17.3 - 34.7 VDC (24-вольтовая система) |
| ШАГ 2. | Проверьте жгут проводов двигателя. |  |
|  | **STEP 2A.** Проверить проводку двигателя на адаптерном кабеле и контактах разъема ECM. | Никаких поврежденных контактов |
|  | **STEP 2A-1.** Осмотрите контакты разъема (контактов) удлинителя (расширителей) кабеля (расширителей) упряжки двигателя и проводов двигателя. | Никаких поврежденных контактов |
|  | **STEP 2B.** Проверьте наличие открытой цепи в цепи питания без переключения. | Менее 10 Ом |
|  | **STEP 2B-1.** Проверьте наличие открытого в двигателе провода, адаптера жгута проводов и любого используемого удлинительного кабеля. | Менее 10 Ом |
|  | **STEP 2C.** Проверьте короткое замыкание от пин-кодов до пин-кодов в непереключенном источнике питания батареи. | Более 100 тыс. ом |
|  | **STEP 2C-1.** Проверьте короткое замыкание от штифта до штифта в кабеле адаптера жгута двигателя и любом используемом удлинительном кабеле. | Более 100 тыс. ом |
|  | **STEP 2D.** Проверьте наземное соединение с проводкой двигателя. | Нет поврежденных соединений |
|  | **ШАГ 2Е.** Проверьте наличие открытой цепи в цепи заземления блока. | Менее 10 Ом |
|  | **STEP 2E-1.** Проверьте наличие открытой цепи в цепочке блок-земли в кабеле адаптера жгута двигателя и любом используемом удлинительном кабеле. | Менее 10 Ом |
| ШАГ 3. | Выполните сброс контроллера. |  |
|  | **STEP 3A.** Выполните частичную сброс на контроллере. | Код 342 или 346 неактивен |
|  | **STEP 3B.** Выполните мастер-сброс на контроллере. | Код 342 или 346 неактивен |
| ШАГ 4. | Очистите код ошибки. |  |
|  | **STEP 4A.** Отключить код ошибки. | Код 342 или 346 неактивен |
|  | **STEP 4B.** Очистить коды неактивных ошибок. | Все коды ошибок очищены |

### ШАГ 1. Проверьте систему батарей оборудования.

#### ШАГ 1A. Проверьте соединения кабеля батареи.

| **Условия: **Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Коррозионные рыхлые соединения. | Нет поврежденных соединений | 1В |
| **Ремонт поврежденных соединений** Ремонт или замена батарейных соединений. См. руководство изготовителя машины по диагностике и ремонту. | 4А |  |

#### ШАГ 1B. Проверьте напряжение батареи.

| **Условия: **Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте напряжение батареи. | 17.3 - 34.7 Вольт DC (система 24 Вольт) | 2А |
| **Заменить батарею** См. Процедуры OEM. | 4А |  |

### ШАГ 2. Проверьте жгут проводов двигателя.

#### ШАГ 2A. Проверьте кабель адаптера жгута двигателя и контакты разъема ECM.

| **Условия: **Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от адаптера ремня от ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| согнутые или сломанные штифты отодвигаются назад или расширенные штифты разъедают штифты влагой в или на разъеме. | Никаких поврежденных контактов | 2А-1-1 |
| **Починить поврежденные контакты** Починить или заменить проводку двигателя на адаптерный кабель или ECM, в зависимости от того, какие контакты повреждены. Ремонт проводов двигателя с помощью адаптера кабеля. См. процедуру 019-240 в Руководстве по устранению неполадок и ремонту, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Замените проводку двигателя адаптерным кабелем. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Заменить ECM. См. процедуры устранения неполадок OEM. Высушить разъем с помощью электрического контактного очистителя, номер детали. 3824510. | 4А |  |

#### ШАГ 2A-1. Осмотрите упряжку для проводов двигателя и любой удлинительный кабель (ы) удлинителя проводов двигателя.

| **Условия: **Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от проводов двигателя удлинитель (ы) удлинителя (ов) упряжки. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| согнутые или сломанные штифты отодвигаются назад или расширенные штифты разъедают штифты влагой в или на разъеме. | Никаких поврежденных контактов | 2В |
| **Починить поврежденные контакты** Починить или заменить упряжку для проводов двигателя или удлинитель (расширительные кабели) упряжки двигателя, в зависимости от того, какие контакты повреждены. Ремонт ремня проводов двигателя или проводов двигателя удлинитель (ы) провода удлинителя (ов). См. процедуру 019-240 в Руководстве по устранению неполадок и ремонту, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Заменить упряжку или удлинитель (расширительные кабели) упряжки двигателя. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Высушить разъем с помощью электрического контактного очистителя, номер детали. 3824510. | 4А |  |

#### ШАГ 2B. Проверьте наличие открытой цепи в непереключенной цепи питания батареи.

| **Условия: **Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от адаптера ремня от ECM. Отсоедините проводку двигателя от батареи. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление от контакта 38 проводов двигателя адаптерного кабеля разъёма к положительному соединению батареи на проводах двигателя ремня измерения сопротивления от контакта 16 через контакт 20 проводов двигателя адаптера ремня кабеля разъёма к положительному соединению батареи на ремне электропроводки двигателя. | Менее 10 Ом | 2C |
|  | 2В-1-1 |  |

#### ШАГ 2B-1. Проверьте наличие открытого в двигателе провода адаптерного кабеля и любого используемого удлинительного кабеля.

| **Условия: **Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от адаптера ремня от ECM. Отсоедините проводку двигателя от любого провода двигателя (расширяющего кабеля) удлинителя (расширяющих кабелей). |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить непрерывность контакта 38 проводов двигателя с адаптерным кабелем и любым используемым проводом (расширительными кабелями) удлинителя (расширяющими) упряжки двигателя. Измерить непрерывность контактов 16 через 20 проводов двигателя адаптерного кабеля и любой проводов двигателя удлинителя (расширителей) провода. | Менее 10 Ом Ремонт или замена электропроводки двигателя Ремонт электропроводки двигателя ремня. См. Процедуры 019-240 и 019-197 в Руководстве по устранению неполадок и ремонту, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Замените жгут проводов двигателя. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 4А |
| **Починить или заменить кабель адаптера или удлинитель (расширители) упряжки упряжки двигателя или проводку двигателя, в зависимости от того, что признано неисправным** Починить адаптер упряжки двигателя или удлинитель (расширители) упряжки двигателя. См. Процедуры 019-240 и 019-197 в Руководстве по устранению неполадок и ремонту, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Заменить проводку двигателя адаптерным кабелем или проводкой двигателя удлинительным кабелем (расширительными кабелями). См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 4А |  |

#### ШАГ 2C. Проверьте короткое замыкание от пин-кодов до пин-кодов в непереключенном источнике питания батареи.

| **Условия: **Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от адаптера ремня от ECM. Отсоедините проводку двигателя от батареи. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление от контакта 38 проводов двигателя, разъёма адаптера жгута проводов, ко всем другим штифтам в разъеме, за исключением контактов 16 через 20, измерить сопротивление от контактов 16 через 20 разъёма адаптера жгута проводов двигателя ко всем другим штифтам в разъеме, за исключением контактов 38 и 16 через 20. | Более 100 тыс. ом | 2D |
|  | 2С-1 |  |

#### ШАГ 2C-1. Проверьте короткое замыкание от пин-кодов до пин-кодов в адаптерном кабеле с жгутом двигателя и любом используемом удлинительном кабеле.

| **Условия: **Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от проводов двигателя удлинитель (ы) удлинителя (ов) упряжки. Отсоедините проводку двигателя от адаптера ремня от ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление от контакта 38 проводов двигателя, разъёма адаптера жгута проводов и любого разъёма проводов двигателя, разъёма удлинителя жгута проводов, ко всем другим контактам в разъеме, за исключением контактов 16 через 20, измерить сопротивление от контактов 16 через 20 разъёма адаптера проводов двигателя и любого разъёма удлинителя провода двигателя, кабеля разъема расширения жгута проводов, ко всем другим контактам в разъеме, за исключением контактов 38 и 16 через 20. | Более 100k Ом Ремонт или замена электропроводки двигателя Ремонт электропроводки двигателя ремня. См. Процедуры 019-240 и 019-197 в Руководстве по устранению неполадок и ремонту, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Замените жгут проводов двигателя. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 4А |
| **Починить или заменить кабель адаптера или удлинитель (расширители) упряжки упряжки двигателя или проводку двигателя, в зависимости от того, что признано неисправным** Починить адаптер упряжки двигателя или удлинитель (расширители) упряжки двигателя. См. Процедуры 019-240 и 019-197 в Руководстве по устранению неполадок и ремонту, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Заменить проводку двигателя адаптерным кабелем или проводкой двигателя удлинительным кабелем (расширительными кабелями). См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 4А |  |

#### ШАГ 2D. Проверьте проводку двигателя наземного соединения.

| **Условия: **Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от адаптера ремня от ECM. Отсоедините проводку двигателя от батареи. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Разорванные соединения разъедают соединения, разрыхляя связи чрезмерной краской, маслом или грязью. | Нет поврежденных соединений | 2Е |
| **Ремонт или замена электропроводки двигателя **Ремонт электропроводки двигателя ремня. См. процедуру 019-197 в Руководстве по устранению неполадок и ремонту, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Замените жгут проводов двигателя. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 4А |  |

#### ШАГ 2E. Проверьте наличие открытой цепи в цепочке блок-земли.

| **Условия: **Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от адаптера ремня от ECM. Отсоедините жгут электропроводки двигателя от заземления блока двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| измеряют сопротивление от контактов 26 через 30 проводов двигателя адаптерного кабеля разъёма к блоку двигателя наземного соединения на проводах двигателя ремня. | Менее 10 Ом | 3А |
|  | 2Е-1 |  |

#### ШАГ 2E-1. Проверьте наличие открытой цепи в цепочке блок-земли в адаптерном кабеле с жгутом двигателя и любом используемом удлинительном кабеле.

| **Условия: **Переключатель стоп/бега в положении «стоп». Контроллер не в диагностическом режиме. Отсоедините проводку двигателя от проводов двигателя удлинитель (ы) удлинителя (ов) упряжки. Отсоедините проводку двигателя от адаптера ремня от ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить непрерывность контактов 26-30 кабеля адаптера жгута двигателя и любого используемого удлинителя (расширителей) проводов жгута двигателя. | Менее 10 Ом Ремонт или замена электропроводки двигателя Ремонт электропроводки двигателя ремня. См. процедуры 019-197 и 019-240 в Руководстве по устранению неполадок и ремонту, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Замените жгут проводов двигателя. См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 4А |
| **Починить или заменить кабель адаптера или удлинитель (расширители) упряжки упряжки двигателя или проводку двигателя, в зависимости от того, что признано неисправным** Починить адаптер упряжки двигателя или удлинитель (расширители) упряжки двигателя. См. Процедуры 019-240 и 019-197 в Руководстве по устранению неполадок и ремонту, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Заменить проводку двигателя адаптерным кабелем или проводкой двигателя удлинительным кабелем (расширительными кабелями). См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 4А |  |

### ШАГ 3. Выполните сброс контроллера.

#### ШАГ 3A. Выполните частичную перезагрузку контроллера.

| **Условия: **Переключатель стоп/бега в положении «стоп». Контроллер в диагностическом режиме. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Использование INSITETM, номер детали. 3825145, выберите меню «Инструменты» и выберите «Частичное перезагрузка контроллера». | Код 342 или 346 неактивен | 3B |
|  | 3B |  |

#### ШАГ 3B. Выполните сброс главного контроллера.

| **Условия: **Переключатель стоп/бега в положении «стоп». Контроллер в диагностическом режиме. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Использование INSITETM, номер детали. 3825145, выберите меню «Инструменты» и выберите «Сброс контроллера». **Примечание:** Выполнение мастер-сброса на контроллере приведет к потере всех данных (данных кода ошибки, параметров, времени ECM и времени работы двигателя) в ECM. Вы должны настроить все регулируемые параметры в их первоначальные настройки после выполнения сброса. | Код 342 или 346 неактивен | 4А |

### ШАГ 4. Очистите код ошибки.

#### ШАГ 4A. Отключите код неисправности.

| **Условия: **Соедините все компоненты. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| подсоединить все компоненты двигателя запуска и простаивать в течение одной минуты | Код 342 или 346 неактивен | 4B |
| Вернитесь к шагам устранения неполадок или свяжитесь с вашим местным авторизованным ремонтным центром Cummins, если все шаги были завершены и перепроверены. | 1А |  |

#### ШАГ 4B. Очистите неактивные коды ошибок.

| **Условия: **Соедините все компоненты. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Стирать неактивные коды неисправностей с помощью INSITETM, номер детали. 3825145. **Примечание:** Разъем шины данных CAN расположен на правом берегу корпуса маховика. | Все ошибки устранены | Ремонт завершён |
| **Устранение неполадок с оставшимися активными кодами ошибок.** | Соответствующая диаграмма устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 342 or 346
>
> ### Electronic Control Module (ECM) Memory - Area Faults
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 342 or 346 PID(P): SPN: FMI: Lamp: SRT: | FC 342 - The ECM has detected a memory check sum error in the memory containing critical engine parameters. FC 346 - The ECM has detected a memory check sum error in the memory containing non-critical engine parameters. | FC 342 - Engine will shutdown. Common Alarm output is energized. FC 346 - None on performance. Common Warning output is energized. **NOTE:** ECM data may be lost, including fault code data, adjustable parameter settings, ECM time, and engine run time). |
>
> ### Circuit Description
>
> The QST30 G-Drive ECM is a computer that is responsible for engine control, diagnostics, and engine features.
>
> ### Component Location
>
> The QST30 G-Drive ECM is installed by the generator set OEM. It can usually be found mounted near the generator utility panel.
>
> ### Shoptalk
>
> This is a fault with the internal memory of the ECM. This fault can be caused by a power interruption to the ECM or a loss of battery power. A partial or master controller reset may be necessary to clear the fault.
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
>
> **To avoid pin and harness damage, use the following test leads when taking a measurement: Part No. 3822758 - male Deutsch/Cannon/Metri-Pack test lead.**
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the equipment battery system. |  |
> |  | **STEP 1A.** Inspect the battery cable connections. | No damaged connections |
> |  | **STEP 1B.** Check the battery voltage. | 17.3 to 34.7 VDC (24 Volt System) |
> | STEP 2. | Check the engine harness. |  |
> |  | **STEP 2A.** Inspect the engine harness adaptor cable and ECM connector pins. | No damaged pins |
> |  | **STEP 2A-1.** Inspect the engine harness and engine harness extension cable(s) connector pins. | No damaged pins |
> |  | **STEP 2B.** Check for an open circuit in the unswitched battery supply circuit. | Less than 10 Ohms |
> |  | **STEP 2B-1.** Check for an open in the engine harness adaptor cable and any extension cable used. | Less than 10 Ohms |
> |  | **STEP 2C.** Check for a short circuit from pin to pin in the unswitched battery supply. | More than 100k ohms |
> |  | **STEP 2C-1.** Check for a short circuit from pin to pin in the engine harness adaptor cable and any extension cable used. | More than 100k ohms |
> |  | **STEP 2D.** Check the engine harness ground connection. | No damaged connections |
> |  | **STEP 2E.** Check for an open circuit in the block ground circuit. | Less than 10 ohms |
> |  | **STEP 2E-1.** Check for an open circuit in the block ground circuit in the engine harness adaptor cable and any extension cable used. | Less than 10 ohms |
> | STEP 3. | Perform a Controller Reset. |  |
> |  | **STEP 3A.** Perform a partial reset on the controller. | Fault Code 342 or 346 inactive |
> |  | **STEP 3B.** Perform a master reset on the controller. | Fault Code 342 or 346 inactive |
> | STEP 4. | Clear the fault code. |  |
> |  | **STEP 4A.** Disable the fault code. | Fault Code 342 or 346 inactive |
> |  | **STEP 4B.** Clear any inactive fault codes. | All fault codes cleared |
>
> ### STEP 1. Check the equipment battery system.
>
> #### STEP 1A. Inspect the battery cable connections.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | corrosion loose connections. | No damaged connections | 1B |
> | **Repair damaged connections** Repair or replace the battery connections. Refer to the OEM Troubleshooting and Repair Manual. | 4A |  |
>
> #### STEP 1B. Check the battery voltage.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | measure the battery voltage. | 17.3 to 34.7 Volts DC (24 Volt System) | 2A |
> | **Replace the battery** Refer to OEM Procedures. | 4A |  |
>
> ### STEP 2. Check the engine harness.
>
> #### STEP 2A. Inspect the engine harness adaptor cable and the ECM connector pins.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | bent or broken pins pushed back or expanded pins corroded pins moisture in or on the connector. | No damaged pins | 2A-1 |
> | **Repair the damaged pins** Repair or replace the engine harness adaptor cable or the ECM, whichever has the damaged pins. Repair the engine harness adaptor cable. Refer to Procedure 019-240 in the Troubleshooting and Repair Manual, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness adaptor cable. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the ECM. Refer to OEM troubleshooting procedures. Dry the connector by using electrical contact cleaner, Part No. 3824510. | 4A |  |
>
> #### STEP 2A-1. Inspect the engine harness and any engine harness extension cable(s).
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness from the engine harness extension cable(s). |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | bent or broken pins pushed back or expanded pins corroded pins moisture in or on the connector. | No damaged pins | 2B |
> | **Repair the damaged pins** Repair or replace the engine harness or the engine harness extension cable(s), whichever has the damaged pins. Repair the engine harness or the engine harness extension cable(s). Refer to Procedure 019-240 in the Troubleshooting and Repair Manual, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness or the engine harness extension cable(s). Refer to Procedure 019-043 in the Troubleshooting and Repair Manual, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Dry the connector by using electrical contact cleaner, Part No. 3824510. | 4A |  |
>
> #### STEP 2B. Check for an open circuit in the unswitched battery supply circuit.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. Disconnect the engine harness from the battery. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | measure the resistance from pin 38 of the engine harness adaptor cable connector to the positive battery connection on the engine harness measure the resistance from pin 16 thru pin 20 of the engine harness adaptor cable connector to the positive battery connection on the engine harness. | Less than 10 Ohms | 2C |
> |  | 2B-1 |  |
>
> #### STEP 2B-1. Check for an open in the engine harness adaptor cable and any extension cable used.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. Disconnect the engine harness from any engine harness extension cable(s). |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | measure the continuity for pin 38 of the engine harness adaptor cable and any engine harness extension cable(s) used. measure the continuity for pins 16 thru 20 of the engine harness adaptor cable and any engine harness extension cable(s) used. | Less than 10 Ohms Repair or replace the engine harness Repair the engine harness. Refer to Procedures 019-240 and 019-197 in the Troubleshooting and Repair Manual, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 4A |
> | **Repair or replace the engine harness adaptor cable or engine harness extension cable(s), whichever is found faulty** Repair the engine harness adaptor cable or engine harness extension cable(s). Refer to Procedures 019-240 and 019-197 in the Troubleshooting and Repair Manual, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness adaptor cable or engine harness extension cable(s). Refer to Procedure 019-043 in the Troubleshooting and Repair Manual, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 4A |  |
>
> #### STEP 2C. Check for a short circuit from pin to pin in the unswitched battery supply.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. Disconnect the engine harness from the battery. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | measure the resistance from pin 38 of the engine harness adaptor cable connector to all other pins in the connector except pins 16 thru 20 measure the resistance from pins 16 thru 20 of the engine harness adaptor cable connector to all other pins in the connector except pins 38 and 16 thru 20. | More than 100k ohms | 2D |
> |  | 2C-1 |  |
>
> #### STEP 2C-1. Check for a short circuit from pin to pin in the engine harness adaptor cable and any extension cable used.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness from the engine harness extension cable(s). Disconnect the engine harness adaptor cable from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | measure the resistance from pin 38 of the engine harness adaptor cable connector and any engine harness extension cable connectors to all other pins in the connector except pins 16 thru 20 measure the resistance from pins 16 thru 20 of the engine harness adaptor cable connector and any engine harness extension cable connectors to all other pins in the connector except pins 38 and 16 thru 20. | More than 100k ohms Repair or replace the engine harness Repair the engine harness. Refer to Procedures 019-240 and 019-197 in the Troubleshooting and Repair Manual, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 4A |
> | **Repair or replace the engine harness adaptor cable or engine harness extension cable(s), whichever is found faulty** Repair the engine harness adaptor cable or engine harness extension cable(s). Refer to Procedures 019-240 and 019-197 in the Troubleshooting and Repair Manual, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness adaptor cable or engine harness extension cable(s). Refer to Procedure 019-043 in the Troubleshooting and Repair Manual, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 4A |  |
>
> #### STEP 2D. Check the engine harness ground connection.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. Disconnect the engine harness from the battery. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | broken connections corroded connections loose connections excessive paint, oil, or dirt. | No damaged connections | 2E |
> | **Repair or replace engine harness** Repair the engine harness. Refer to Procedure 019-197 in the Troubleshooting and Repair Manual, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 4A |  |
>
> #### STEP 2E. Check for an open circuit in the block ground circuit.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. Disconnect the engine harness from engine block ground. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | measure the resistance from pins 26 thru 30 of the engine harness adaptor cable connector to the engine block ground connection on the engine harness. | Less than 10 ohms | 3A |
> |  | 2E-1 |  |
>
> #### STEP 2E-1. Check for an open circuit in the block ground circuit in the engine harness adaptor cable and any extension cable used.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness from the engine harness extension cable(s). Disconnect the engine harness adaptor cable from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | measure the continuity for pins 26 thru 30 of the engine harness adaptor cable and any engine harness extension cable(s) used. | Less than 10 ohms Repair or replace engine harness Repair the engine harness. Refer to Procedure 019-197 and 019-240 in the Troubleshooting and Repair Manual, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 4A |
> | **Repair or replace the engine harness adaptor cable or engine harness extension cable(s), whichever is found faulty** Repair the engine harness adaptor cable or engine harness extension cable(s). Refer to Procedures 019-240 and 019-197 in the Troubleshooting and Repair Manual, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness adaptor cable or engine harness extension cable(s). Refer to Procedure 019-043 in the Troubleshooting and Repair Manual, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 4A |  |
>
> ### STEP 3. Perform a controller reset.
>
> #### STEP 3A. Perform a partial controller reset.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller in the diagnostic mode. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Using INSITE™, Part No. 3825145, pull down the “Tools” menu and select “Controller Partial Reset”. | Fault Code 342 or 346 inactive | 3B |
> |  | 3B |  |
>
> #### STEP 3B. Perform a master controller reset.
>
> | **Conditions:** Stop/Run switch in the "STOP" position. Controller in the diagnostic mode. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Using INSITE™, Part No. 3825145, pull down the “Tools” menu and select “Controller Master Reset”. **NOTE:** Performing a master reset on the controller will cause all data (fault code data, parameter settings, ECM time and engine run time) in the ECM to be lost. You must configure all adjustable parameters to their original settings after performing the reset. | Fault Code 342 or 346 inactive | 4A |
>
> ### STEP 4. Clear the fault code.
>
> #### STEP 4A. Disable the fault code.
>
> | **Conditions:** Connect all of the components. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | connect all components start engine and idle for one minute | Fault Code 342 or 346 inactive | 4B |
> | Return to troubleshooting steps or contact your local Cummins Authorized Repair Location if all steps have been completed and rechecked. | 1A |  |
>
> #### STEP 4B. Clear any inactive fault codes.
>
> | **Conditions:** Connect all of the components. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Erase inactive fault codes using INSITE™, Part No. 3825145. **NOTE:** The datalink connector is located on the right bank of the flywheel housing. | All faults cleared | Repair complete |
> | **Troubleshoot any remaining active fault codes.** | Appropriate troubleshooting chart |  |
