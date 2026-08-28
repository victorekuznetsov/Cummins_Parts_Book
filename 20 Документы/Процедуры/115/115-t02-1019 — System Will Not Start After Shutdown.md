---
aliases:
  - "Система не запускается после останова"
type: "Процедура"
doc: "115-t02-1019"
title_en: "System Will Not Start After Shutdown"
title_ru: "Система не запускается после останова"
modified: "2008-04-14"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021587"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1019.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1019.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/115"
  - "перевод/машинный"
---

# System Will Not Start After Shutdown
**Система не запускается после останова**

> [!abstract] Процедура · `115-t02-1019`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]]
> **Секции:** Section TT — Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-04-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1019.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1019.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Базовая система сигнализации **не** запускается после полного отключения системы.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения симптомов запуска панели. Начните с шага 1 поиска неисправностей. Шаг 2 задаст ряд вопросов и предоставит список шагов по устранению неполадок, которые необходимо выполнить в зависимости от симптома.

### Практические замечания

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте кнопку остановки двигателя |  |
|  | **Кнопка остановки двигателя для включения.** | Кнопка остановки двигателя включена? |
| ШАГ 2. | Проверьте клиентский интерфейс коробки аккумулятора |  |
|  | **STEP 2A.** Проверить напряжение в блоке логики клиентского интерфейса | +24-VDC? |
|  | **STEP 2B.** Проверьте провод питания аккумулятора (разрушитель цепи на логическом блоке окна интерфейса клиента) | Сопротивление менее 10 Ом? |
|  | **STEP 2C.** Проверьте подачу аккумулятора (разъем X4 к выключателю) | Сопротивление менее 10 Ом? |
|  | **STEP 2D.** Проверьте провод возврата батареи (разрушитель схемы на блок логики окна интерфейса клиента) | Сопротивление менее 10 Ом? |
|  | **ШАГ 2Е.** Проверьте провод возврата батареи (разъем X4 к выключателю) | Сопротивление менее 10 Ом? |
|  | **STEP 2F** Проверить выключатель цепи питания аккумулятора | Сопротивление менее 10 Ом? |
|  | **STEP 2G.** Проверьте провод электропитания (блок логики клиентского интерфейса на блоке логического прерывателя клиентского интерфейса) | Сопротивление менее 10 Ом? |
|  | **STEP 2H.** Проверьте провода питания блока логики клиентского интерфейса (блок управления логическим блоком клиентского интерфейса на блоке логики интерфейса клиента) | Сопротивление менее 10 Ом? |
|  | **STEP 2I** Проверьте логическую блок-выключатель клиентского интерфейса | Сопротивление менее 10 Ом? |
|  | **STEP 2J.** Проверьте провод электропитания (логикический блок коробки интерфейса клиента на выключатель питания панели машинного отделения) | Сопротивление менее 10 Ом? |
|  | **STEP 2K.** Проверьте провод питания панели машинного отделения (выключатель цепи питания панели двигателя для разъема C7) | Сопротивление менее 10 Ом? |
|  | **STEP 2L.** Проверьте выключатель цепи питания панели машинного отделения | Сопротивление менее 10 Ом? |
|  | **STEP 2M.** Проверьте провод возврата панели машинного отделения (логикический блок коробки интерфейса клиента для разъема C7) | Сопротивление менее 10 Ом? |
| ШАГ 3. | Проверка системных кабелей панели |  |
|  | **ШАГ 3А** Проверить кабель панели машинного отделения | Сопротивление менее 10 Ом? |
| ШАГ 4. | Проверка проводов панели |  |
|  | **STEP 4A** Проверить провода питания в машинном отделении | Сопротивление менее 10 Ом? |
|  | **STEP 4B** Проверить работу переключателя питания | Сопротивление менее 10 Ом? |

### ШАГ 1. Проверьте кнопку остановки двигателя

#### ШАГ 1A. Проверьте кнопку остановки двигателя для разъединения

| **Условия: **Закрыт интерфейс клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Убедитесь, что кнопка остановки двигателя полностью отключена. Поверните кнопку «Остановить двигатель» 1/16-й поворота по часовой стрелке. Кнопка остановки двигателя будет издавать звуковой шум при отключении. Примечание: Кнопка остановки двигателя **не** повернется, если она уже отключена. | Кнопка остановки двигателя включена? *Да | Ремонт завершён |
| Кнопка остановки двигателя включена? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте интерфейс коробки аккумулятора

#### ШАГ 2A. Проверка напряжения в блоке логики клиентского интерфейса

| **Условия: **Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение питания батареи на логическом блоке клиентского интерфейса. Поместите один измерительный щуп на терминал питания батареи на логический блок клиентского интерфейса. Поместите другой измерительный щуп на терминал возврата батареи на логический блок окна интерфейса клиента. См. соответствующую схему или схему проводов для правильной идентификации штифта и провода. | +24-VDC? *Да | 2G |
| +24-VDC? **НЕТ** | 2В |  |

#### ШАГ 2B. Проверьте провод питания батареи (разрушитель цепи к логическому блоку окна интерфейса клиента)

| **Условия: **Откройте окно клиентского интерфейса Отключите провод питания батареи от блока логики клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод питания батареи. Поместите один испытательный щуп на терминал подачи батареи выключателя цепи подачи батареи. Поместите другой измерительный щуп на терминал питания батареи логического блока клиентского интерфейса. См. соответствующую схему или схему проводов для правильной идентификации штифта и провода. | Сопротивление менее 10 Ом? *Да | 2C |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод.[[115-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён. |  |

#### ШАГ 2C. Проверьте аккумуляторную батарею (X4 Connector to Circuit Breaker)

| **Условия: **Откройте окно интерфейса клиента Отключите провод питания батареи от выключателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод питания батареи. Поместите один испытательный щуп на терминал питания батареи X4. Поместите другой испытательный щуп на терминал подачи батареи выключателя цепи питания батареи. См. соответствующую схему или схему проводов для правильной идентификации штифта и провода. | Сопротивление менее 10 Ом? *Да | 2D |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод.[[115-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён. |  |

#### ШАГ 2D. Проверьте провод возврата батареи (разрушитель схемы к логическому блоку окна интерфейса клиента)

| **Условия: **Откройте окно клиентского интерфейса Отключите провод возврата батареи от блока логики клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод возврата батареи. Поместите один испытательный щуп на терминал возврата батареи выключателя цепи питания батареи. Поместите другой измерительный щуп на терминал возврата батареи логического блока клиентского интерфейса. См. соответствующую схему или схему проводов для правильной идентификации штифта и провода. | Сопротивление менее 10 Ом? *Да | 2Е |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод.[[115-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён. |  |

#### ШАГ 2E. Проверьте провод возврата батареи (разъем X4 к выключателю)

| **Условия: **Откройте окно интерфейса клиента Отключите провод возврата батареи от выключателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод возврата батареи. Поместите один испытательный щуп на терминал возврата батареи X4. Поместите другой испытательный щуп на терминал возврата батареи выключателя цепи питания батареи. См. соответствующую схему или схему проводов для правильной идентификации штифта и провода. | Сопротивление менее 10 Ом? *Да | 2F |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод.[[115-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён. |  |

#### ШАГ 2F. Проверьте выключатель цепи питания батареи

| **Условия: **Откройте окно интерфейса клиента Отключите все провода от выключателя Закройте выключатель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте выключатель питания батареи. Поместите один испытательный щуп на терминал на одной стороне выключателя. Поместите другой испытательный щуп на соответствующий терминал на другой стороне выключателя. См. соответствующую схему или схему проводов для правильной идентификации штифта и провода. | Сопротивление менее 10 Ом? *Да | 2G |
| Сопротивление менее 10 Ом? **NORepair:** Заменить выключатель.[[115-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён. |  |

#### ШАГ 2G. Проверьте провод источника питания (блок логики клиентского интерфейса на блоке логического выключателя клиентского интерфейса)

| **Условия: **Откройте окно клиентского интерфейса Отключите провод питания от блока логики клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод электропитания. Поместите один измерительный щуп на терминал питания логического блока клиентского интерфейса. Поместите другой испытательный щуп на терминал питания логического блока блок-выключателя клиентского интерфейса. См. соответствующую схему или схему проводов для правильной идентификации штифта и провода. | Сопротивление менее 10 Ом? *Да | 2 ч. |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод.[[115-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён. |  |

#### ШАГ 2H. Проверьте провод поставки клиентского интерфейса (блок управления клиентским интерфейсом, выключатель схемы блока логики интерфейса, блок логики клиентского интерфейса)

| **Условия: **Откройте окно клиентского интерфейса Отключите провод поставки клиентского интерфейсного блока от блока логики клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте логический блок питания клиентского интерфейса. Поместите один измерительный щуп на терминал поставки блока логики клиентского интерфейса. Поместите другой измерительный щуп на терминал поставки блока логики клиентского интерфейса выключателя логического блока клиентского интерфейса. См. соответствующую схему или схему проводов для правильной идентификации штифта и провода. | Сопротивление менее 10 Ом? *Да | 2II |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод.[[115-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён. |  |

#### ШАГ 2I. Проверьте интерфейс клиента коробка логический блок выключатель цепи

| **Условия: **Откройте окно интерфейса клиента Отключите все провода от выключателя Закройте выключатель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте логический блок прерывателя клиентского интерфейса. Поместите один испытательный щуп на терминал на одной стороне выключателя. Поместите другой испытательный щуп на терминал на другой стороне выключателя. См. соответствующую схему или схему проводов для правильной идентификации штифта и провода. | Сопротивление менее 10 Ом? *Да | 2J |
| Сопротивление менее 10 Ом? **NORepair:** Заменить выключатель.[[115-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён. |  |

#### ШАГ 2J. Проверьте провод источника питания (логикический блок клиентского интерфейса для выключателя питания панели двигателя)

| **Условия: **Откройте окно клиентского интерфейса Отключите провод питания от блока логики клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод электропитания. Поместите один измерительный щуп на терминал питания логического блока клиентского интерфейса. Поместите другой испытательный щуп на терминал питания выключателя цепи питания панели машинного отделения. См. соответствующую схему или схему проводов для правильной идентификации штифта и провода. | Сопротивление менее 10 Ом? *Да | 2к |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод.[[115-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён. |  |

#### ШАГ 2K. Проверьте провод питания панели машинного отделения (выключатель цепи питания панели двигателя для разъема C7)

| **Условия: **Откройте окно интерфейса клиента Отключите кабель панели машинного отделения на разъеме C7 окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод питания панели машинного отделения. Поместите один испытательный щуп на панель двигателя, питающую контакт разъема С7. Поместите другой испытательный щуп на терминал подачи панели машинного отделения выключателя цепи питания панели машинного отделения. См. соответствующую схему или схему проводов для правильной идентификации штифта и провода. | Сопротивление менее 10 Ом? *Да | 2 л |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод.[[115-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён. |  |

#### ШАГ 2L. Проверьте выключатель цепи питания панели машинного отделения

| **Условия: **Откройте окно интерфейса клиента Отключите все провода от выключателя Закройте выключатель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте выключатель цепи питания панели машинного отделения. Поместите один испытательный щуп на терминал на одной стороне выключателя. Поместите другой испытательный щуп на терминал на другой стороне выключателя. См. соответствующую схему или схему проводов для правильной идентификации штифта и провода. | Сопротивление менее 10 Ом? *Да | 2М |
| Сопротивление менее 10 Ом? **NORepair:** Заменить выключатель.[[115-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён. |  |

#### ШАГ 2M. Проверьте обратный провод панели машинного отделения (логический блок коробки интерфейса клиента для разъема C7)

| **Условия: **Откройте окно интерфейса клиента Отключите кабель панели машинного отделения на разъеме C7 окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод возврата панели машинного отделения. Поместите один испытательный щуп на панель машинного отделения обратного контакта разъема С7. Поместите другой испытательный щуп на панель возвратного терминала панели управления двигателем логического блока клиентского интерфейса. См. соответствующую схему или схему проводов для правильной идентификации штифта и провода. | Сопротивление менее 10 Ом? *Да | 3А |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод.[[115-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён. |  |

### ШАГ 3. Проверка системных кабелей панели

#### ШАГ 3A. Проверить кабель панели машинного отделения

| **Условия:** Отсоединить кабельный разъём С14 от панели машинного отделения Отключить кабельный разъём С7 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте кабель панели машинного отделения. Установите перемычку между контактом питания панели машинного отделения и обратным контактом панели машинного отделения в разъеме C14. Поместите один испытательный щуп в контакт питания панели машинного отделения в разъем С7. Поместите другой испытательный щуп в панель машинного отделения обратного контакта в разъем С7. См. соответствующую схему или схему проводов для правильной идентификации штифта и провода. | Сопротивление менее 10 Ом? *Да | 4А |
| Сопротивление менее 10 Ом? **Заменить кабель.** | Ремонт завершён. |  |

### ШАГ 4. Проверка проводов панели

#### ШАГ 4A. Проверить провода питания в машинном отделении

| **Условия: **Найдите панель машинного отделения Открытая дверь панели машинного отделения. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверяйте провода между разъёмом жгута проводов и разъёмом панели управления. Отсоедините кабель C14 от панели машинного отделения. Поместите один испытательный щуп на контакт питания панели машинного отделения на разъем С14. Поместите другой испытательный щуп в контакт питания панели машинного отделения на разъем панели управления. См. соответствующую схему или схему проводов для правильной идентификации штифта и провода. | Сопротивление менее 10 Ом? *Да | 4B |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод.[[115-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён. |  |

#### ШАГ 4B. Проверить работу выключателя питания

| **Условия: **Открытая панель машинного отделения Отключить панель управления разъемом машинного отделения. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте работу выключателя питания. Отсоедините кабель C14 от панели машинного отделения. Поместите один испытательный щуп на терминал питания переключателя питания в машинном отделении разъема панели управления. Поместите другой испытательный щуп на терминал питания панели машинного отделения на разъем панели управления. Переместите переключатель питания в положение включенного. См. соответствующую схему или схему проводов для правильной идентификации штифта и провода. | Сопротивление менее 10 Ом? Заменить логический блок клиентского интерфейса.[[115-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён. |
| Сопротивление менее 10 Ом? **NORepair:** Заменить панель управления.[[115-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - The basic alarm panel system will **not** start up after a complete system shutdown.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot panel startup symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform depending on the symptom.
>
> ### Shoptalk
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the Engine Stop button |  |
> |  | **STEP 1A.** Check Engine Stop button for engagement. | Engine Stop button engaged? |
> | STEP 2. | Check customer interface box battery circuit |  |
> |  | **STEP 2A.** Check voltage at customer interface box logic unit | +24-VDC? |
> |  | **STEP 2B.** Check the battery supply wire (circuit breaker to customer interface box logic unit) | Less than 10 ohms resistance? |
> |  | **STEP 2C.** Check the battery suppy wire (X4 connector to circuit breaker) | Less than 10 ohms resistance? |
> |  | **STEP 2D.** Check the battery return wire (circuit breaker to customer interface box logic unit) | Less than 10 ohms resistance? |
> |  | **STEP 2E.** Check the battery return wire (X4 connector to circuit breaker) | Less than 10 ohms resistance? |
> |  | **STEP 2F.** Check battery supply circuit breaker | Less than 10 ohms resistance? |
> |  | **STEP 2G.** Check the power supply wire (customer interface box logic unit to customer interface box logic unit circuit breaker) | Less than 10 ohms resistance? |
> |  | **STEP 2H.** Check the customer interface box logic unit supply wire (customer interface box logic unit circuit breaker to customer interface box logic unit) | Less than 10 ohms resistance? |
> |  | **STEP 2I.** Check customer interface box logic unit circuit breaker | Less than 10 ohms resistance? |
> |  | **STEP 2J.** Check the power supply wire (customer interface box logic unit to engine room panel supply circuit breaker) | Less than 10 ohms resistance? |
> |  | **STEP 2K.** Check the engine room panel supply wire (engine room panel supply circuit breaker to connector C7) | Less than 10 ohms resistance? |
> |  | **STEP 2L.** Check the engine room panel supply circuit breaker | Less than 10 ohms resistance? |
> |  | **STEP 2M.** Check the engine room panel return wire (customer interface box logic unit to connector C7) | Less than 10 ohms resistance? |
> | STEP 3. | Check panel system cables |  |
> |  | **STEP 3A.** Check engine room panel cable | Less than 10 ohms resistance? |
> | STEP 4. | Check panel wiring |  |
> |  | **STEP 4A.** Check engine room panel supply wire | Less than 10 ohms resistance? |
> |  | **STEP 4B.** Check power switch operation | Less than 10 ohms resistance? |
>
> ### STEP 1. Check the Engine Stop button
>
> #### STEP 1A. Check the Engine Stop button for disengagement
>
> | **Conditions:** Customer interface box closed. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Be sure the Engine Stop button is fully disengaged. Turn the Engine Stop button 1/16th of a turn clockwise. The Engine Stop button will make an audible noise as it disengages. NOTE: The Engine Stop button will **not** turn if it is already disengaged. | Engine Stop button engaged? **YES** | Repair complete |
> | Engine Stop button engaged? **NO** | 2A |  |
>
> ### STEP 2. Check interface box battery circuit
>
> #### STEP 2A. Check voltage at customer interface box logic unit
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check battery supply voltage to the customer interface box logic unit. Place one test lead on the battery supply terminal on the customer interface box logic unit. Place the other test lead on the battery return terminal on the customer interface box logic unit. Refer to the appropriate circuit diagram or wiring diagram for correct pin and wire identification. | +24-VDC? **YES** | 2G |
> | +24-VDC? **NO** | 2B |  |
>
> #### STEP 2B. Check the battery supply wire (circuit breaker to customer interface box logic unit)
>
> | **Conditions:** Open the customer interface box Disconnect the battery supply wire from the customer interface box logic unit. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the battery supply wire. Place one test lead on the battery supply terminal of the battery supply circuit breaker. Place the other test lead on the battery supply terminal of the customer interface box logic unit. Refer to the appropriate circuit diagram or wiring diagram for correct pin and wire identification. | Less than 10 ohms resistance? **YES** | 2C |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. [[115-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete. |  |
>
> #### STEP 2C. Check the Battery Suppy Wire (X4 Connector to Circuit Breaker)
>
> | **Conditions:** Open the customer interface box Disconnect the battery supply wire from the circuit breaker. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the battery supply wire. Place one test lead on the battery supply terminal of X4. Place the other test lead on the battery supply terminal of the battery supply circuit breaker. Refer to the appropriate circuit diagram or wiring diagram for correct pin and wire identification. | Less than 10 ohms resistance? **YES** | 2D |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. [[115-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete. |  |
>
> #### STEP 2D. Check the battery return wire (circuit breaker to customer interface box logic unit)
>
> | **Conditions:** Open the customer interface box Disconnect the battery return wire from the customer interface box logic unit. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the battery return wire. Place one test lead on the battery return terminal of the battery supply circuit breaker. Place the other test lead on the battery return terminal of the customer interface box logic unit. Refer to the appropriate circuit diagram or wiring diagram for correct pin and wire identification. | Less than 10 ohms resistance? **YES** | 2E |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. [[115-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete. |  |
>
> #### STEP 2E. Check the battery return wire (X4 connector to circuit breaker)
>
> | **Conditions:** Open the customer interface box Disconnect the battery return wire from the circuit breaker. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the battery return wire. Place one test lead on the battery return terminal of X4. Place the other test lead on the battery return terminal of the battery supply circuit breaker. Refer to the appropriate circuit diagram or wiring diagram for correct pin and wire identification. | Less than 10 ohms resistance? **YES** | 2F |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. [[115-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete. |  |
>
> #### STEP 2F. Check battery supply circuit breaker
>
> | **Conditions:** Open the customer interface box Disconnect all wires from the circuit breaker Close the circuit breaker. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the battery supply circuit breaker. Place one test lead on a terminal on one side of the circuit breaker. Place the other test lead on the corresponding terminal on the other side of the circuit breaker. Refer to the appropriate circuit diagram or wiring diagram for correct pin and wire identification. | Less than 10 ohms resistance? **YES** | 2G |
> | Less than 10 ohms resistance? **NORepair:** Replace the circuit breaker. [[115-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete. |  |
>
> #### STEP 2G. Check the power supply wire (customer interface box logic unit to customer interface box logic unit circuit breaker)
>
> | **Conditions:** Open the customer interface box Disconnect the power supply wire from the customer interface box logic unit. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the power supply wire. Place one test lead on the power supply terminal of the customer interface box logic unit. Place the other test lead on the power supply terminal of the customer interface box logic unit circuit breaker. Refer to the appropriate circuit diagram or wiring diagram for correct pin and wire identification. | Less than 10 ohms resistance? **YES** | 2H |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. [[115-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete. |  |
>
> #### STEP 2H. Check the customer interface box logic unit supply wire (customer interface box logic unit circuit breaker to customer interface box logic unit)
>
> | **Conditions:** Open the customer interface box Disconnect the customer interface box logic unit supply wire from the customer interface box logic unit. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the customer interface logic unit supply wire. Place one test lead on the customer interface box logic unit supply terminal of the customer interface box logic unit. Place the other test lead on the customer interface box logic unit supply terminal of the customer interface box logic unit circuit breaker. Refer to the appropriate circuit diagram or wiring diagram for correct pin and wire identification. | Less than 10 ohms resistance? **YES** | 2I |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. [[115-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete. |  |
>
> #### STEP 2I. Check customer interface box logic unit circuit breaker
>
> | **Conditions:** Open the customer interface box Disconnect all wires from the circuit breaker Close the circuit breaker. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the customer interface logic unit circuit breaker. Place one test lead on the terminal on one side of the circuit breaker. Place the other test lead on the terminal on the other side of the circuit breaker. Refer to the appropriate circuit diagram or wiring diagram for correct pin and wire identification. | Less than 10 ohms resistance? **YES** | 2J |
> | Less than 10 ohms resistance? **NORepair:** Replace the circuit breaker. [[115-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete. |  |
>
> #### STEP 2J. Check the power supply wire (customer interface box logic unit to engine room panel supply circuit breaker)
>
> | **Conditions:** Open the customer interface box Disconnect the power supply wire from the customer interface box logic unit. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the power supply wire. Place one test lead on the power supply terminal of the customer interface box logic unit. Place the other test lead on the power supply terminal of the engine room panel supply circuit breaker. Refer to the appropriate circuit diagram or wiring diagram for correct pin and wire identification. | Less than 10 ohms resistance? **YES** | 2K |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. [[115-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete. |  |
>
> #### STEP 2K. Check the engine room panel supply wire (engine room panel supply circuit breaker to connector C7)
>
> | **Conditions:** Open the customer interface box Disconnect the engine room panel cable at connector C7 of the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine room panel supply wire. Place one test lead on the engine room panel supply pin of connector C7. Place the other test lead on the engine room panel supply terminal of the engine room panel supply circuit breaker. Refer to the appropriate circuit diagram or wiring diagram for correct pin and wire identification. | Less than 10 ohms resistance? **YES** | 2L |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. [[115-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete. |  |
>
> #### STEP 2L. Check the engine room panel supply circuit breaker
>
> | **Conditions:** Open the customer interface box Disconnect all wires from the circuit breaker Close the circuit breaker. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine room panel supply circuit breaker. Place one test lead on the terminal on one side of the circuit breaker. Place the other test lead on the terminal on the other side of the circuit breaker. Refer to the appropriate circuit diagram or wiring diagram for correct pin and wire identification. | Less than 10 ohms resistance? **YES** | 2M |
> | Less than 10 ohms resistance? **NORepair:** Replace the circuit breaker. [[115-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete. |  |
>
> #### STEP 2M. Check the engine room panel return wire (customer interface box logic unit to connector C7)
>
> | **Conditions:** Open the customer interface box Disconnect the engine room panel cable at connector C7 of the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine room panel return wire. Place one test lead on the engine room panel return pin of connector C7. Place the other test lead on the engine room panel return terminal of the customer interface box logic unit. Refer to the appropriate circuit diagram or wiring diagram for correct pin and wire identification. | Less than 10 ohms resistance? **YES** | 3A |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. [[115-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete. |  |
>
> ### STEP 3. Check panel system cables
>
> #### STEP 3A. Check engine room panel cable
>
> | **Conditions:** Disconnect cable connector C14 from the engine room panel Disconnect cable connector C7 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine room panel cable. Install a jumper between engine room panel supply pin and the engine room panel return pin in connector C14. Place one test lead in the engine room panel supply pin in connector C7. Place the other test lead in the engine room panel return pin in connector C7. Refer to the appropriate circuit diagram or wiring diagram for correct pin and wire identification. | Less than 10 ohms resistance? **YES** | 4A |
> | Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |
>
> ### STEP 4. Check panel wiring
>
> #### STEP 4A. Check engine room panel supply wire
>
> | **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check wires between harness connector and control panel connector. Disconnect cable C14 from the engine room panel. Place one test lead on the engine room panel supply pin on connector C14. Place the other test lead in the engine room panel supply pin on the control panel connector. Refer to the appropriate circuit diagram or wiring diagram for correct pin and wire identification. | Less than 10 ohms resistance? **YES** | 4B |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. [[115-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete. |  |
>
> #### STEP 4B. Check power switch operation
>
> | **Conditions:** Open engine room panel Disconnect engine room panel connector control panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the power switch operation. Disconnect cable C14 from the engine room panel. Place one test lead on the engine room panel power switch supply terminal of the control panel connector. Place the other test lead on the engine room panel power supply terminal on the control panel connector. Move the power switch to the on position. Refer to the appropriate circuit diagram or wiring diagram for correct pin and wire identification. | Less than 10 ohms resistance? **YESRepair:** Replace the customer interface box logic unit. [[115-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete. |
> | Less than 10 ohms resistance? **NORepair:** Replace the control panel. [[115-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete. |  |
