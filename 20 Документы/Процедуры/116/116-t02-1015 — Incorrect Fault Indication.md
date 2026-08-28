---
aliases:
  - "Неверная индикация неисправности"
type: "Процедура"
doc: "116-t02-1015"
title_en: "Incorrect Fault Indication"
title_ru: "Неверная индикация неисправности"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1015.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1015.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# Incorrect Fault Indication
**Неверная индикация неисправности**

> [!abstract] Процедура · `116-t02-1015`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1015.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1015.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

Сигнальная лампа **не** освещается на блоке DCU410 или на удаленной панели при активном состоянии сигнализации.

- ECM Fault Acknowledgement **Not**

- Ложные указания на остановку двигателя.

### Как пользоваться этим деревом

По этому дереву симптомов можно вести поиск неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте индикатор сигнализации лампы Panel Alarm |  |
|  | **ШАГ 1А** Проверьте индикацию сигнализации на панели блоков DCU410. |  |
|  | **STEP 1B** Проверьте индикацию сигнализации на удаленной панели. |  |
| ШАГ 2. | Проверьте окно клиентского интерфейса |  |
|  | **STEP 2A.** Проверьте напряжение батареи 1 (основной источник питания) провода на наличие открытого. |  |
|  | **STEP 2B.** Проверьте напряжение батареи 1 (вторичный источник питания) провода на наличие открытого. |  |
|  | **STEP 2C.** Проверьте провод питания удаленной панели на наличие открытого. |  |
|  | **STEP 2D.** Проверьте напряжение батареи 1 (основной источник питания) провода для короткого провода к проводу. |  |
|  | **ШАГ 2Е.** Проверьте напряжение батареи 1 (вторичный источник питания) провода для короткого провода к проводу. |  |
|  | **STEP 2F.** Проверьте провод питания удаленной панели на короткое расстояние от провода к проводу. |  |
|  | **STEP 2G.** Проверьте напряжение батареи 1 (основной источник питания) провода на короткое время до земли. |  |
|  | **STEP 2H.** Проверьте напряжение батареи 1 (вторичный источник питания) провода на короткое время до земли. |  |
|  | **STEP 2I.** Проверьте провод питания удаленной панели на короткое время до земли. |  |

### ШАГ 1. Проверьте индикацию сигнализации панели.

#### ШАГ 1A. Проверьте индикатор сигнализации сигнализации панели DCU410.

| **Условия: **Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте, что лампа панели блока DCU410 освещена. | Сигнальная лампа подсвечивается? *Да | 1В |
| Сигнальная лампа подсвечивается? **НЕТ** | 2А |  |

#### ШАГ 1B. Проверьте индикацию сигнализации на удаленной панели.

| **Условия: **Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте, что лампа на удаленной панели освещена. | Сигнальная лампа подсвечивается? *Да | Ремонт завершён |
| Сигнальная лампа подсвечивается? **НЕТ** | Ремонт завершён |  |

### ШАГ 2. Проверьте окно интерфейса клиента.

#### ШАГ 2A. Проверьте напряжение батареи 1 (основной источник питания) провода для открытого.

| **Условия: **Откройте окно интерфейса клиента. Отключите провод напряжения батареи 1 (основной источник питания) на блоке DCU410 и соединении X4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение батареи 1 (основной источник питания) провода для открытого. Поместите один испытательный щуп на провод напряжения батареи 1 (основной источник питания) в блок DCU410. Поместите другой испытательный щуп на провод напряжения батареи 1 (основной источник питания) в соединение X4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 2В |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 2B. Проверьте напряжение батареи 1 (вторичный источник питания) провода на наличие открытого.

| **Условия: **Откройте окно интерфейса клиента. Отключите провод напряжения батареи 1 (вторичный источник питания) на блоке DCU410 и выключателе. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение батареи 1 (вторичный источник питания) провода на наличие открытого. Поместите один испытательный щуп на провод напряжения батареи 1 (вторичный источник питания) в блок DCU410. Поместите другой испытательный щуп на провод напряжения батареи 1 (вторичный источник питания) на выключателе. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 2C |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 2C. Проверьте провод питания удаленной панели на наличие открытого.

| **Условия: **Откройте окно интерфейса клиента. Отключите провод питания удаленной панели на соединении X4 и удаленной панели. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод питания удаленной панели на наличие открытого. Поместите один испытательный щуп на провод питания удаленной панели в соединение X4. Поместите другой испытательный щуп на провод питания удаленной панели на удаленной панели. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 2D |
| Менее 10 Ом? **NORepair:** Заменить провод или разъем. См. процедуру 015-023 (Customer Interface Box) в разделе 15 для замены провода. Свяжитесь с авторизованным местом ремонта Cummins® для замены разъема. | Ремонт завершён |  |

#### ШАГ 2D. Проверьте напряжение батареи 1 (основной источник питания) провода для провода к проводу коротко.

| **Условия: **Откройте окно интерфейса клиента. Отключите провод напряжения батареи 1 (основной источник питания) на блоке DCU410 и соединении X4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод на короткое расстояние. Поместите один испытательный щуп на провод напряжения батареи 1 (основной источник питания) в блок DCU410. Поместите другой испытательный щуп на все провода в блок DCU410. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 2Е |
| Менее 10 Ом? **NORepair:** Заменить блок DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |  |

#### ШАГ 2E. Проверьте напряжение батареи 1 (вторичный источник питания) провода для провода к проводу коротко.

| **Условия: **Откройте окно интерфейса клиента. Отключите провод напряжения батареи 1 (вторичный источник питания) на блоке DCU410 и соединении X4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение батареи 1 (вторичный источник питания) провода для провода к проводу коротко. Поместите один испытательный щуп на провод напряжения батареи 1 (вторичный источник питания) в блок DCU410. Поместите другой испытательный щуп на все провода в блок DCU410. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 2F |
| Менее 10 Ом? **NORepair:** Заменить блок DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |  |

#### ШАГ 2F. Проверьте провод питания удаленной панели на короткое расстояние от провода к проводу.

| **Условия: **Откройте окно интерфейса клиента. Отключите провод питания удаленной панели на соединении X4 и удаленной панели. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод питания удаленной панели на короткое расстояние от провода к проводу. Поместите один испытательный щуп на провод питания удаленной панели в соединение X4. Поместите другой испытательный щуп на все провода в соединение X4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 2G |
| Менее 10 Ом? **NORepair:** Заменить пульт дистанционного управления. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |  |

#### ШАГ 2G. Проверьте напряжение батареи 1 (основной источник питания) провода для короткого наземного.

| **Условия: **Откройте окно интерфейса клиента. Отключите провод напряжения батареи 1 (основной источник питания) на блоке DCU410 и соединении X4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение батареи 1 (основной источник питания) провода для короткого наземного. Поместите один испытательный щуп на провод напряжения батареи 1 (основной источник питания) в блок DCU410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 2 ч. |
| Менее 10 Ом? **NORepair:** Заменить блок DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |  |

#### ШАГ 2H. Проверьте напряжение батареи 1 (вторичный источник питания) провода для короткого наземного.

| **Условия: **Откройте окно интерфейса клиента. Отключите провод напряжения батареи 1 (вторичный источник питания) на DCU410 и выключатель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение батареи 1 (вторичный источник питания) провода для короткого наземного. Поместите один испытательный щуп на провод напряжения батареи 1 (вторичный источник питания) в блок DCU410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 2II |
| Менее 10 Ом? **NORepair:** Заменить блок DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |  |

#### ШАГ 2I. Проверьте провод питания удаленной панели на короткое время до земли.

| **Условия: **Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод питания удаленной панели на короткое время до земли. Поместите один испытательный щуп на провод питания удаленной панели в соединение X4. Поместите другой испытательный щуп на удаленную панель. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | Обратитесь в авторизованный сервисный центр Cummins®. |
| Менее 10 Ом? **NORepair:** Заменить пульт дистанционного управления. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> Alarm lamp is **not** illuminated at the DCU410 unit or the remote panel when alarm condition is active.
>
> - ECM Fault Acknowledgement **Not** Operational
>
> - False Indication of Engine Shutdown.
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
> | STEP 1. | Check the Panel Alarm Lamp Indication |  |
> |  | **STEP 1A.** Check the DCU410 unit panel alarm lamp indication. |  |
> |  | **STEP 1B.** Check the remote panel alarm lamp indication. |  |
> | STEP 2. | Check the Customer Interface Box |  |
> |  | **STEP 2A.** Check the battery voltage 1 (primary power supply) wire for an open. |  |
> |  | **STEP 2B.** Check the battery voltage 1 (secondary power supply) wire for an open. |  |
> |  | **STEP 2C.** Check the remote panel supply wire for an open. |  |
> |  | **STEP 2D.** Check the battery voltage 1 (primary power supply) wire for a wire-to-wire short. |  |
> |  | **STEP 2E.** Check the battery voltage 1 (secondary power supply) wire for a wire-to-wire short. |  |
> |  | **STEP 2F.** Check the remote panel supply wire for a wire-to-wire short. |  |
> |  | **STEP 2G.** Check the battery voltage 1 (primary power supply) wire for a short to ground. |  |
> |  | **STEP 2H.** Check the battery voltage 1 (secondary power supply) wire for a short to ground. |  |
> |  | **STEP 2I.** Check the remote panel supply wire for a short to ground. |  |
>
> ### STEP 1. Check the panel alarm lamp indication.
>
> #### STEP 1A. Check the DCU410 unit panel alarm lamp indication.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify the DCU410 unit panel lamp is illuminated. | Alarm lamp illuminated? **YES** | 1B |
> | Alarm lamp illuminated? **NO** | 2A |  |
>
> #### STEP 1B. Check the remote panel alarm lamp indication.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify the remote panel lamp is illuminated. | Alarm lamp illuminated? **YES** | Repair complete |
> | Alarm lamp illuminated? **NO** | Repair complete |  |
>
> ### STEP 2. Check the customer interface box.
>
> #### STEP 2A. Check the battery voltage 1 (primary power supply) wire for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the battery voltage 1 (primary power supply) wire at the DCU410 unit and X4 connection. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the battery voltage 1 (primary power supply) wire for an open. Place one test lead on the battery voltage 1 (primary power supply) wire at the DCU410 unit. Place the other test lead on the battery voltage 1 (primary power supply) wire at the X4 connection. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2B |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 2B. Check the battery voltage 1 (secondary power supply) wire for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the battery voltage 1 (secondary power supply) wire at the DCU410 unit and circuit breaker. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the battery voltage 1 (secondary power supply) wire for an open. Place one test lead on the battery voltage 1 (secondary power supply) wire at the DCU410 unit. Place the other test lead on the battery voltage 1 (secondary power supply) wire at the circuit breaker. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2C |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 2C. Check the remote panel supply wire for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the remote panel supply wire at the X4 connection and remote panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the remote panel supply wire for an open. Place one test lead on the remote panel supply wire at the X4 connection. Place the other test lead on the remote panel supply wire at the remote panel. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2D |
> | Less than 10 ohms? **NORepair:** Replace the wire or connector. Refer to Procedure 015-023 (Customer Interface Box) in Section 15 to replace the wire. Contact a Cummins® Authorized Repair Location to replace the connector. | Repair complete |  |
>
> #### STEP 2D. Check the battery voltage 1 (primary power supply) wire for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. Disconnect the battery voltage 1 (primary power supply) wire at the DCU410 unit and X4 connection. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the wire for a wire-to-wire short. Place one test lead on the battery voltage 1 (primary power supply) wire at the DCU410 unit. Place the other test lead on all wires at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2E |
> | Less than 10 ohms? **NORepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair location. | Repair complete |  |
>
> #### STEP 2E. Check the battery voltage 1 (secondary power supply) wire for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. Disconnect the battery voltage 1 (secondary power supply) wire at the DCU410 unit and X4 connection. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the battery voltage 1 (secondary power supply) wire for a wire-to-wire short. Place one test lead on the battery voltage 1 (secondary power supply) wire at the DCU410 unit. Place the other test lead on all wires at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2F |
> | Less than 10 ohms? **NORepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair location. | Repair complete |  |
>
> #### STEP 2F. Check the remote panel supply wire for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. Disconnect the remote panel supply wire at the X4 connection and remote panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the remote panel supply wire for a wire-to-wire short. Place one test lead on the remote panel supply wire at the X4 connection. Place the other test lead on all wires at the X4 connection. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2G |
> | Less than 10 ohms? **NORepair:** Replace the remote panel. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
>
> #### STEP 2G. Check the battery voltage 1 (primary power supply) wire for a short to ground.
>
> | **Conditions:** Open the customer interface box. Disconnect the battery voltage 1 (primary power supply) wire at the DCU410 unit and X4 connection. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the battery voltage 1 (primary power supply) wire for a short to ground. Place one test lead on the battery voltage 1 (primary power supply) wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2H |
> | Less than 10 ohms? **NORepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair location. | Repair complete |  |
>
> #### STEP 2H. Check the battery voltage 1 (secondary power supply) wire for a short to ground.
>
> | **Conditions:** Open the customer interface box. Disconnect the battery voltage 1 (secondary power supply) wire at the DCU410 and circuit breaker. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the battery voltage 1 (secondary power supply) wire for a short to ground. Place one test lead on the battery voltage 1 (secondary power supply) wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2I |
> | Less than 10 ohms? **NORepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
>
> #### STEP 2I. Check the remote panel supply wire for a short to ground.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the remote panel supply wire for a short to ground. Place one test lead on the remote panel supply wire at the X4 connection. Place the other test lead on remote panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | Contact a Cummins® Authorized Repair Location. |
> | Less than 10 ohms? **NORepair:** Replace the remote panel. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
