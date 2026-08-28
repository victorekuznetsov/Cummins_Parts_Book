---
aliases:
  - "Не работает функция отключения звука блока управления дизелем"
type: "Процедура"
doc: "116-t02-1053"
title_en: "Diesel Control Unit Silence Function Not Working"
title_ru: "Не работает функция отключения звука блока управления дизелем"
modified: "2008-05-22"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1053.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1053.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# Diesel Control Unit Silence Function Not Working
**Не работает функция отключения звука блока управления дизелем**

> [!abstract] Процедура · `116-t02-1053`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1053.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1053.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

Режим тишины настроен на сигнализацию, но все равно дает светодиодную лампу и звуковую сигнализацию.

### Как пользоваться этим деревом

По этому дереву симптомов можно вести поиск неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте окно интерфейса клиента. |  |
|  | **STEP 1A.** Проверьте дисплей блока DCU410 на наличие неисправностей. |  |
|  | **STEP 1A-1.** Проверьте провод блока питания DCU410 на напряжение +24-VDC. |  |
|  | **ШАГ 1А-2.** Проверьте провод блока питания CLU на напряжение +24-VDC. |  |
|  | **ШАГ 1В.** Проверить провод дистанционного сигнализации тишины на наличие открытого сигнала. |  |
|  | **STEP 1C.** Проверьте напряжение 1 батареи (переключенная мощность) провода питания на наличие открытого. |  |
|  | **STEP 1D.** Проверить провод питания лампы на предмет наличия открытого источника. |  |
|  | **ШАГ 1Е.** Проверить провод питания выключателя на наличие открытого. |  |
|  | **STEP 1F.** Проверьте провод питания коммутатора Ethernet на наличие открытого. |  |
|  | **STEP 1G.** Проверьте провода питания сигнализации дистанционного тишины на короткое время. |  |
|  | **STEP 1H.** Проверьте напряжение 1 батареи (переключенная мощность) провода питания для короткого провода к проводу. |  |
|  | **ШАГ 1I.** Проверить провод питания лампы на короткое расстояние от провода к проводу. |  |
|  | **STEP 1J.** Проверьте провод питания переключателя на короткое расстояние от провода к проводу. |  |
|  | **STEP 1K.** Проверьте провод питания Ethernet-коммутатора на короткое время. |  |
|  | **STEP 1L.** Проверить провод подачи сигнала тишины на короткое время до земли. |  |
|  | **STEP 1M.** Проверьте напряжение 1 батареи (переключенная мощность) провода питания для короткого наземного. |  |
|  | **ШАГ 1N.** Проверить провод питания лампы на короткое время до земли. |  |
|  | **ШАГ 1O.** Проверить провод питания выключателя на короткий срок до заземления. |  |
|  | **STEP 1P.** Проверьте провод питания коммутатора Ethernet на короткое время до заземления. |  |

### ШАГ 1. Проверьте окно интерфейса клиента.

#### ШАГ 1A. Проверьте дисплей блока DCU410 на наличие неисправностей.

| **Условия:** Найдите дисплей блока DCU410. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте дисплей блока DCU410 для указания неисправностей. | DCU410 указывает на неисправность (неисправности)? *Да | 1В |
| DCU410 указывает на неисправность (неисправности)? **НЕТ** | 1А-1-1 |  |

#### ШАГ 1A-1. Проверьте провод блока питания DCU410 на напряжение +24-VDC.

| **Условия:** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение на батарее 1 напряжения (переключенной мощности) в блоке DCU410. Поместите один тест на провод напряжения батареи 1 (переключенной мощности) в блок DCU410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Меньше +24-VDC? **Ремонт:** Проверить аккумуляторы. См. руководство по обслуживанию OEM. | Ремонт завершён |
| Меньше +24-VDC? **НЕТ** | 1А-2 |  |

#### ШАГ 1A-2. Проверьте провод блока питания CLU на напряжение +24-VDC.

| **Условия:** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение на батарее 1 напряжения (переключенной мощности) в блоке CLU. Поместите один тест на провод напряжения батареи 1 (переключенной мощности) в блоке CLU. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Меньше +24-VDC? **Ремонт:** Проверить аккумуляторы. См. руководство по обслуживанию OEM. | Ремонт завершён |
| Меньше +24-VDC? **НЕТ** | 1В |  |

#### ШАГ 1B. Проверьте провод подачи сигнала тишины для открытого.

| **Условия:** Откройте окно интерфейса клиента. Отключите провод дистанционной сигнализации тишины на блоке DCU410 и соединении X4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод подачи сигнала тишины для открытого. Поместите один испытательный щуп на провод дистанционного питания сигнализации тишины в блок DCU410. Поместите другой испытательный щуп на провод дистанционного питания сигнализации тишины на соединение X4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1С |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1C. Проверьте напряжение батареи 1 (переключенная мощность) провода питания для открытого.

| **Условия:** Откройте окно интерфейса клиента. Отключите провод питания 1 напряжения (переключенной мощности) батареи на блоке DCU410 и соединении X4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение батареи 1 (переключенная мощность) провода питания для открытого. Поместите один испытательный щуп на провод питания напряжения батареи 1 (переключенной мощности) в блоке DCU410. Поместите другой испытательный щуп на провод напряжения батареи 1 (переключенной мощности) в соединение X4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1D |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1D. Проверьте провод питания лампы на предмет открытия.

| **Условия:** Откройте окно интерфейса клиента. Отключите провод питания 1 напряжения (переключенной мощности) батареи на блоке DCU410 и подключение лампы питания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод питания лампы на предмет открытия. Поместите один испытательный щуп на провод питания напряжения батареи 1 (переключенной мощности) в блоке DCU410. Поместите другой испытательный щуп на провод питания лампы питания на подключение лампы питания. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1Е |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1E. Проверьте провод питания выключателя на наличие открытого.

| **Условия:** Откройте окно интерфейса клиента. Отключите провод питания 1 напряжения (переключенной мощности) батареи на блоке DCU410 и подключите переключатель питания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод питания выключателя на наличие открытого. Поместите один испытательный щуп на провод питания напряжения батареи 1 (переключенной мощности) в блоке DCU410. Поместите другой испытательный щуп на провод питания переключателя питания на подключение переключателя питания. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1F |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1F. Проверьте провод питания Ethernet-коммутатора на наличие открытого.

| **Условия:** Откройте окно интерфейса клиента. Отключите провод питания 1 напряжения (переключенной мощности) батареи на блоке DCU410 и соединении коммутатора Ethernet. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод питания Ethernet-коммутатора на наличие открытого. Поместите один испытательный щуп на провод питания напряжения батареи 1 (переключенной мощности) в блоке DCU410. Поместите другой измерительный щуп на провод питания коммутатора Ethernet в соединение коммутатора Ethernet. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1G |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1G. Проверьте провод подачи сигнала тишины для короткого провода к проводу.

| **Условия:** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод подачи сигнала тишины для короткого провода к проводу. Поместите один испытательный щуп на провод дистанционного питания сигнализации тишины в блок DCU410. Поместите другой испытательный щуп на все другие провода в блок DCU410. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1 ч. |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]]Заменить DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |  |

#### ШАГ 1H. Проверьте напряжение батареи 1 (переключенная мощность) провода питания для короткого провода к проводу.

| **Условия:** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение батареи 1 (переключенная мощность) провода питания для короткого провода к проводу. Поместите один испытательный щуп на провод питания напряжения батареи 1 (переключенной мощности) в блоке DCU410. Поместите другой испытательный щуп на все другие провода в блок DCU410. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1II |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1I. Проверьте провод питания лампы для короткого провода к проводу.

| **Условия:** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод питания лампы для короткого провода к проводу. Поместите один испытательный щуп на провод питания напряжения батареи 1 (переключенной мощности) в блоке DCU410. Поместите другой испытательный щуп на все другие провода в блок DCU410. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1J |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]]Заменить DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |  |

#### ШАГ 1J. Проверьте провод питания переключателя для короткого провода к проводу.

| **Условия:** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод питания переключателя для короткого провода к проводу. Поместите один испытательный щуп на провод питания напряжения батареи 1 (переключенной мощности) в блоке DCU410. Поместите другой испытательный щуп на все другие провода в блок DCU410. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1кг |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]]Заменить DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |  |

#### ШАГ 1K. Проверьте провод питания коммутатора Ethernet для короткого провода к проводу.

| **Условия:** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод питания коммутатора Ethernet для короткого провода к проводу. Поместите один испытательный щуп на провод питания напряжения батареи 1 (переключенной мощности) в блоке DCU410. Поместите другой испытательный щуп на все другие провода в блок DCU410. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1 л |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]]Заменить DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |  |

#### ШАГ 1L. Проверьте провод подачи сигнала тишины на короткое время до земли.

| **Условия:** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод подачи сигнала тишины на короткое время до земли. Поместите один испытательный щуп на провод дистанционного питания сигнализации тишины в блок DCU410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1 мкм |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]]Заменить DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |  |

#### ШАГ 1M. Проверьте напряжение батареи 1 (переключенная мощность) провода питания для короткого наземного.

| **Условия:** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение батареи 1 (переключенная мощность) провода питания для короткого наземного. Поместите один испытательный щуп на провод питания напряжения батареи 1 (переключенной мощности) в блоке DCU410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1NN |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]]Заменить DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |  |

#### ШАГ 1N. Проверьте провод питания лампы на короткое время до земли.

| **Условия:** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод питания лампы на короткое время до земли. Поместите один испытательный щуп на провод питания лампы в блок DCU410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1О |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]]Заменить DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |  |

#### ШАГ 1O. Проверьте провод питания выключателя на короткий срок до земли.

| **Условия:** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод питания выключателя на короткий срок до земли. Поместите один испытательный щуп на провод питания переключателя питания в блок DCU410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1P |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]]Заменить DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |  |

#### ШАГ 1P. Проверьте провод питания Ethernet-коммутатора для короткого наземного подключения.

| **Условия:** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод питания Ethernet-коммутатора для короткого наземного подключения. Поместите один измерительный щуп на провод питания коммутатора Ethernet в блок DCU410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | Обратитесь в авторизованный сервисный центр Cummins®. |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]]Заменить DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> Silence mode set for alarm, but still is giving an LED lamp and audible alarm.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the customer interface box. |  |
> |  | **STEP 1A.** Check the DCU410 unit display for faults. |  |
> |  | **STEP 1A-1.** Check the DCU410 unit power supply wire for voltage +24-VDC. |  |
> |  | **STEP 1A-2.** Check the CLU unit power supply wire for voltage +24-VDC. |  |
> |  | **STEP 1B.** Check the remote silence alarm supply wire for an open. |  |
> |  | **STEP 1C.** Check the battery 1 voltage (switched power) supply wire for an open. |  |
> |  | **STEP 1D.** Check the power lamp supply wire for an open. |  |
> |  | **STEP 1E.** Check the power switch supply wire for an open. |  |
> |  | **STEP 1F.** Check the Ethernet switch supply wire for an open. |  |
> |  | **STEP 1G.** Check the remote silence alarm supply wire for a wire-to-wire short. |  |
> |  | **STEP 1H.** Check the battery 1 voltage (switched power) supply wire for a wire-to-wire short. |  |
> |  | **STEP 1I.** Check the power lamp supply wire for a wire-to-wire short. |  |
> |  | **STEP 1J.** Check the power switch supply wire for a wire-to-wire short. |  |
> |  | **STEP 1K.** Check the Ethernet switch supply wire for a wire-to-wire short. |  |
> |  | **STEP 1L.** Check the remote silence alarm supply wire for a short to ground. |  |
> |  | **STEP 1M.** Check the battery 1 voltage (switched power) supply wire for a short to ground. |  |
> |  | **STEP 1N.** Check the power lamp supply wire for a short to ground. |  |
> |  | **STEP 1O.** Check the power switch supply wire for a short to ground. |  |
> |  | **STEP 1P.** Check the Ethernet switch supply wire for a short to ground. |  |
>
> ### STEP 1. Check the customer interface box.
>
> #### STEP 1A. Check the DCU410 unit display for faults.
>
> | **Conditions:** Locate the DCU410 unit display. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the DCU410 unit display for indication of faults. | DCU410 unit indicates fault(s)? **YES** | 1B |
> | DCU410 unit indicates fault(s)? **NO** | 1A-1 |  |
>
> #### STEP 1A-1. Check the DCU410 unit power supply wire for voltage +24-VDC.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the voltage at the battery 1 voltage (switched power) at the DCU410 unit. Place one test on the battery 1 voltage (switched power) wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than +24-VDC? **YESRepair:** Check the batteries. Refer to OEM service manual. | Repair complete |
> | Less than +24-VDC? **NO** | 1A-2 |  |
>
> #### STEP 1A-2. Check the CLU unit power supply wire for voltage +24-VDC.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the voltage at the battery 1 voltage (switched power) at the CLU unit. Place one test on the battery 1 voltage (switched power) wire at the CLU unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than +24-VDC? **YESRepair:** Check the batteries. Refer to OEM service manual. | Repair complete |
> | Less than +24-VDC? **NO** | 1B |  |
>
> #### STEP 1B. Check the remote silence alarm supply wire for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the remote silence alarm wire at the DCU410 unit and X4 connection. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the remote silence alarm supply wire for an open. Place one test lead on the remote silence alarm supply wire at the DCU410 unit. Place the other test lead on the remote silence alarm supply wire at the X4 connection. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1C |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 1C. Check the battery 1 voltage (switched power) supply wire for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the battery 1 voltage (switched power) supply wire at the DCU410 unit and X4 connection. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the battery 1 voltage (switched power) supply wire for an open. Place one test lead on the battery 1 voltage (switched power) supply wire at the DCU410 unit. Place the other test lead on the battery 1 voltage (switched power) wire at the X4 connection. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1D |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 1D. Check the power lamp supply wire for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the battery 1 voltage (switched power) supply wire at the DCU410 unit and power lamp connection. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the power lamp supply wire for an open. Place one test lead on the battery 1 voltage (switched power) supply wire at the DCU410 unit. Place the other test lead on the power lamp supply wire at the power lamp connection. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1E |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 1E. Check the power switch supply wire for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the battery 1 voltage (switched power) supply wire at the DCU410 unit and power switch connection. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the power switch supply wire for an open. Place one test lead on the battery 1 voltage (switched power) supply wire at the DCU410 unit. Place the other test lead on the power switch supply wire at the power switch connection. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1F |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 1F. Check the Ethernet switch supply wire for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the battery 1 voltage (switched power) supply wire at the DCU410 unit and the Ethernet switch connection. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the Ethernet switch supply wire for an open. Place one test lead on the battery 1 voltage (switched power) supply wire at the DCU410 unit. Place the other test lead on the Ethernet switch supply wire at the Ethernet switch connection. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1G |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 1G. Check the remote silence alarm supply wire for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the remote silence alarm supply wire for a wire-to-wire short. Place one test lead on the remote silence alarm supply wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1H |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
>
> #### STEP 1H. Check the battery 1 voltage (switched power) supply wire for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the battery 1 voltage (switched power) supply wire for a wire-to-wire short. Place one test lead on the battery 1 voltage (switched power) supply wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1I |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 1I. Check the power lamp supply wire for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the power lamp supply wire for a wire-to-wire short. Place one test lead on the battery 1 voltage (switched power) supply wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1J |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
>
> #### STEP 1J. Check the power switch supply wire for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the power switch supply wire for a wire-to-wire short. Place one test lead on the battery 1 voltage (switched power) supply wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1K |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
>
> #### STEP 1K. Check the Ethernet switch supply wire for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the Ethernet switch supply wire for a wire-to-wire short. Place one test lead on the battery 1 voltage (switched power) supply wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1L |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
>
> #### STEP 1L. Check the remote silence alarm supply wire for a short to ground.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the remote silence alarm supply wire for a short to ground. Place one test lead on the remote silence alarm supply wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1M |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
>
> #### STEP 1M. Check the battery 1 voltage (switched power) supply wire for a short to ground.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the battery 1 voltage (switched power) supply wire for a short to ground. Place one test lead on the battery 1 voltage (switched power) supply wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1N |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
>
> #### STEP 1N. Check the power lamp supply wire for a short to ground.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the power lamp supply wire for a short to ground. Place one test lead on the power lamp supply wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1O |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
>
> #### STEP 1O. Check the power switch supply wire for a short to ground.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the power switch supply wire for a short to ground. Place one test lead on the power switch supply wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1P |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
>
> #### STEP 1P. Check the Ethernet switch supply wire for a short to ground.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the Ethernet switch supply wire for a short to ground. Place one test lead on the Ethernet switch supply wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | Contact a Cummins® Authorized Repair Location. |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
