---
aliases:
  - "Блок останова указывает причину останова, которого не было"
type: "Процедура"
doc: "116-t02-1092"
title_en: "Shutdown Unit Indicates Shut Down Cause When Shutdown Did Not Occur"
title_ru: "Блок останова указывает причину останова, которого не было"
modified: "2008-04-04"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1092.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1092.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# Shutdown Unit Indicates Shut Down Cause When Shutdown Did Not Occur
**Блок останова указывает причину останова, которого не было**

> [!abstract] Процедура · `116-t02-1092`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-04-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1092.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1092.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

Двигатель не выключается, но SDU410 ошибочно указывает на то, что произошло выключение.

### Как пользоваться этим деревом

По этому дереву симптомов можно вести поиск неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Убедитесь, что режим остановки активен **не**. Если перекрытие активировано и остановка не произошла, но сигнал тревоги сообщает, что оператор был бы отключен, если бы он не был переопределен. Отключите сигнализацию о перекрытии. Если сигнализация может быть отключена **не**, обратитесь к соответствующему дереву устранения неполадок.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте окно интерфейса клиента |  |
|  | **ШАГ 1А.** Проверить наличие сигнализации и светодиодной подсветки. | Светодиодная вспышка? |
|  | **STEP 1A-1.** Проверьте блок отключения питания шины связи ModiconTM и провода возврата для открытого доступа. | Менее 10 Ом? |
|  | **STEP 1A-2.** Проверьте блок отключения питания шины связи ModiconTM и провода возврата для короткого провода к проводу. | Менее 10 Ом? |
|  | **ШАГ 1А-3.** Проверить отключаемый блок питания коммуникационной шины ModiconTM на короткое время до заземления. | Менее 10 Ом? |
|  | **ШАГ 1А-4.** Проверьте сигнал переопределения защиты двигателя и провода возврата для открытого. | Менее 10 Ом? |
|  | **STEP 1A-5.** Проверьте сигнал переопределения защиты двигателя и провода возврата для короткого провода к проводу. | Менее 10 Ом? |
|  | **ШАГ 1А-6.** Проверить защитный сигнал двигателя на короткое время до земли. | Менее 10 Ом? |
|  | **STEP 1A-7.** Проверьте реле реле защиты двигателя и сигнальные провода на предмет наличия открытого сигнала. | Менее 10 Ом? |
|  | **STEP 1A-8.** Проверьте сигнал реле переопределения защиты двигателя и провода возврата для короткого провода к проводу. | Менее 10 Ом? |
|  | **ШАГ 1А-9.** Проверить защитный релейный провод реле двигателя на короткое время до земли. | Менее 10 Ом? |

### ШАГ 1. Проверьте окно интерфейса клиента.

#### ШАГ 1A. Проверьте наличие сигнализации и светодиодной подсветки.

| **Условия:** Проверить наличие сигнализации и светодиодного освещения. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте схему переключения отключения для активации. | Светодиодная вспышка? Заменить модуль SDU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |
| Светодиодная вспышка? **НЕТ** | 1А-1-1 |  |

#### ШАГ 1A-1. Проверьте блок отключения питания коммуникационной шины ModiconTM и возвратные провода для открытого доступа.

| **Условия: **Откройте окно интерфейса клиента. Отключите блок отключения питания и возврата шины связи ModiconTM на блоке SDU410 и блоке DCU410. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте блок отключения питания коммуникационной шины ModiconTM и возвратные провода для открытого доступа. Поместите один испытательный щуп на блок отключения провода питания шины связи ModiconTM на блок SDU410. Поместите другой испытательный щуп на блок отключения провода питания шины связи ModiconTM в блок DCU410. Поместите один испытательный щуп на блок отключения провода обратной шины связи ModiconTM на блок SDU410. Поместите другой испытательный щуп на отключаемый модуль обратного провода шины связи ModiconTM в блок DCU410. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1А-2 |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1A-2. Проверьте блок отключения питания коммуникационной шины ModiconTM и возвратные провода для короткого провода к проводу.

| **Условия: **Откройте окно интерфейса клиента. Отключите блок отключения питания и возврата шины связи ModiconTM на блоке SDU410 и блоке DCU410. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте блок отключения питания коммуникационной шины ModiconTM и возвратные провода для короткого провода к проводу. Поместите один испытательный щуп на блок отключения провода питания шины связи ModiconTM на блок SDU410. Поместите другой испытательный щуп на все другие провода в блок DCU410. Поместите один испытательный щуп на блок отключения провода обратной шины связи ModiconTM на блок SDU410. Поместите другой испытательный щуп на все другие провода в блок DCU410. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 1А-3 |  |

#### ШАГ 1A-3. Проверьте блок отключения провода питания коммуникационной шины ModiconTM для короткого заземления.

| **Условия: **Откройте окно интерфейса клиента. Отключите отключающий блок провода питания шины связи ModiconTM на блоке SDU410 и блоке DCU410. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте блок отключения провода питания коммуникационной шины ModiconTM для короткого заземления. Поместите один испытательный щуп на блок отключения провода питания шины связи ModiconTM на блок SDU410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 1А-4 |  |

#### ШАГ 1A-4. Проверьте сигнал переопределения защиты двигателя и верните провода для открытого.

| **Условия: **Откройте окно интерфейса клиента. Отключите сигнал опровержения защиты двигателя и провода возврата на блоке SDU410 и реле оверрайда защиты двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнал переопределения защиты двигателя и верните провода для открытого. Поместите один испытательный щуп на сигнальный провод защиты двигателя на блоке SDU410. Поместите другой испытательный щуп на сигнальный провод оверрайда защиты двигателя на контакт реле реле защиты двигателя. Поместите один испытательный щуп на обратный провод защиты двигателя на блоке SDU410. Поместите другой испытательный щуп на обратный провод защиты двигателя при контакте реле реле защиты двигателя. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1А-5 |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1A-5. Проверьте сигнал переопределения защиты двигателя и возвратные провода для короткого провода к проводу.

| **Условия: **Откройте окно интерфейса клиента. Отключите сигнал опровержения защиты двигателя и провода возврата на блоке SDU410 и реле оверрайда защиты двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнал переопределения защиты двигателя и возвратные провода для короткого провода к проводу. Поместите один испытательный щуп на сигнальный провод защиты двигателя на блоке SDU410. Поместите другой испытательный щуп на все другие провода в блок SDU410. Поместите один испытательный щуп на обратный провод защиты двигателя на блоке SDU410. Поместите другой испытательный щуп на все другие контакты на реле переопределения защиты двигателя. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 1А-6 |  |

#### ШАГ 1A-6. Проверьте защитный сигнал двигателя на короткое время до земли.

| **Условия: **Откройте окно интерфейса клиента. Отключите сигнальный провод защиты двигателя на блоке DCU410. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте защитный сигнал двигателя на короткое время до земли. Поместите один испытательный щуп на сигнальный провод защиты двигателя на концевой полосе SDU410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 1А-7 |  |

#### ШАГ 1A-7. Проверьте защиту двигателя, перекрывающую реле питания и сигнальные провода для открытого.

| **Условия: **Откройте окно интерфейса клиента. Отключите реле реле защиты от двигателя и сигнальные провода на реле защиты от двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте защиту двигателя, перекрывающую реле питания и сигнальные провода для открытого. Поместите один испытательный щуп на провод ретрансляции реле защиты двигателя на реле ретрансляции защиты двигателя. Поместите другой испытательный щуп на контакт реле реле защиты двигателя на разъеме C3. Поместите один испытательный щуп на провод ретрансляции реле защиты двигателя на реле ретрансляции защиты двигателя. Поместите другой испытательный щуп на контакт реле реле защиты двигателя на разъеме X4. Поместите один испытательный щуп на обратный провод защиты двигателя на блоке SDU410. Поместите другой испытательный щуп на реле реле защиты двигателя поверх реле обратного провода на контакте реле защиты двигателя поверх реле. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1А-8 |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1A-8. Проверьте сигнал реле защиты двигателя и возвращайте провода для короткого провода к проводу.

| **Условия: **Откройте окно интерфейса клиента. Отключите сигнал реле оверрайда защиты двигателя и провода возврата на блоке SDU410 и реле оверрайда защиты двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнал реле защиты двигателя и возвращайте провода для короткого провода к проводу. Поместите один испытательный щуп на провод ретрансляции реле защиты двигателя на блоке SDU410. Поместите другой испытательный щуп на все другие провода в блок SDU410. Поместите один испытательный щуп на реле реле обратной проволоки защиты двигателя на блоке SDU410. Поместите другой испытательный щуп на все другие контакты на реле переопределения защиты двигателя. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 1А-9 |  |

#### ШАГ 1A-9. Проверьте защитный реле реле двигателя на короткое время до земли.

| **Условия: **Откройте окно интерфейса клиента. Отключите сигнальный провод ретрансляции защиты двигателя на блоке DCU410. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте защитный реле реле двигателя на короткое время до земли. Поместите один испытательный щуп на провод ретрансляции реле защиты двигателя на концевой полосе SDU410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | Свяжитесь с авторизованным местом ремонта Cummins® |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> The engine does **not** shut down, but the SDU410 unit falsely indicates that a shutdown has occurred.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> Check that the Shutdown Override is **not** active. If the Shutdown Override is active and no shutdown occurred but an alarm informs operator shut down would have occurred if it had **not** been overridden. Deactivate the shutdown override alarm. If the alarm can **not** be deactivated, reference the appropriate troubleshooting tree.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the customer interface box |  |
> |  | **STEP 1A.** Check for alarm and LED illumination. | LED flashing? |
> |  | **STEP 1A-1.** Check the shutdown unit Modicon™ communication bus supply and return wires for an open. | Less than 10 ohms? |
> |  | **STEP 1A-2.** Check the shutdown unit Modicon™ communication bus supply and return wires for a wire-to-wire short. | Less than 10 ohms? |
> |  | **STEP 1A-3.** Check the shutdown unit Modicon™ communication bus supply wire for a short to ground. | Less than 10 ohms? |
> |  | **STEP 1A-4.** Check the engine protection override signal and return wires for an open. | Less than 10 ohms? |
> |  | **STEP 1A-5.** Check the engine protection override signal and return wires for a wire-to-wire short. | Less than 10 ohms? |
> |  | **STEP 1A-6.** Check the engine protection override signal wire for a short to ground. | Less than 10 ohms? |
> |  | **STEP 1A-7.** Check the engine protection override relay supply and signal wires for an open. | Less than 10 ohms? |
> |  | **STEP 1A-8.** Check the engine protection override relay signal and return wires for wire-to-wire short. | Less than 10 ohms? |
> |  | **STEP 1A-9.** Check the engine protection override relay signal wire for a short to ground. | Less than 10 ohms? |
>
> ### STEP 1. Check the customer interface box.
>
> #### STEP 1A. Check for alarm and LED illumination.
>
> | **Conditions:** Check for alarm and LED illumination. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the Shutdown Override circuit for activation. | LED flashing? **YESRepair:** Replace the SDU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
> | LED flashing? **NO** | 1A-1 |  |
>
> #### STEP 1A-1. Check the shutdown unit Modicon™ communication bus supply and return wires for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the shutdown unit Modicon™ communication bus supply and return wires at the SDU410 unit and DCU410 unit. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the shutdown unit Modicon™ communication bus supply and return wires for an open. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit. Place the other test lead on the shutdown unit Modicon™ communication bus supply wire at the DCU410 unit. Place one test lead on the shutdown unit Modicon™ communication bus return wire at the SDU410 unit. Place the other test lead on the shutdown unit Modicon™ communication bus return wire at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1A-2 |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 1A-2. Check the shutdown unit Modicon™ communication bus supply and return wires for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. Disconnect the shutdown unit Modicon™ communication bus supply and return wires at the SDU410 unit and DCU410 unit. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the shutdown unit Modicon™ communication bus supply and return wires for a wire-to-wire short. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit. Place the other test lead on all other wires at the DCU410 unit. Place one test lead on the shutdown unit Modicon™ communication bus return wire at the SDU410 unit. Place the other test lead on all other wires at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 1A-3 |  |
>
> #### STEP 1A-3. Check the shutdown unit Modicon™ communication bus supply wire for a short to ground.
>
> | **Conditions:** Open the customer interface box. Disconnect the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit and DCU410 unit. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the shutdown unit Modicon™ communication bus supply wire for a short to ground. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 1A-4 |  |
>
> #### STEP 1A-4. Check the engine protection override signal and return wires for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the engine protection override signal and return wires at the SDU410 unit and engine protection override relay. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine protection override signal and return wires for an open. Place one test lead on the engine protection override signal wire at the SDU410 unit. Place the other test lead on the engine protection override signal wire at the engine protection override relay contact. Place one test lead on the engine protection override return wire at the SDU410 unit. Place the other test lead on the engine protection override return wire at the engine protection override relay contact. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1A-5 |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 1A-5. Check the engine protection override signal and return wires for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. Disconnect the engine protection override signal and return wires at the SDU410 unit and engine protection override relay. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine protection override signal and return wires for a wire-to-wire short. Place one test lead on the engine protection override signal wire at the SDU410 unit. Place the other test lead on all other wires at the SDU410 unit. Place one test lead on the engine protection override return wire at the SDU410 unit. Place the other test lead on all other contacts on the engine protection override relay. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 1A-6 |  |
>
> #### STEP 1A-6. Check the engine protection override signal wire for a short to ground.
>
> | **Conditions:** Open the customer interface box. Disconnect the engine protection override signal wire at the DCU410 unit. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine protection override signal wire for a short to ground. Place one test lead on the engine protection override signal wire at the SDU410 terminal strip. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 1A-7 |  |
>
> #### STEP 1A-7. Check the engine protection override relay supply and signal wires for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the engine protection override relay supply and signal wires at the engine protection override relay. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine protection override relay supply and signal wires for an open. Place one test lead on the engine protection override relay signal wire at the engine protection override relay. Place the other test lead on the engine protection override relay signal pin at the C3 connector. Place one test lead on the engine protection override relay signal wire at the engine protection override relay. Place the other test lead on the engine protection override relay signal pin at the X4 connector. Place one test lead on the engine protection override return wire at the SDU410 unit. Place the other test lead on the engine protection override relay return wire at the engine protection override relay contact. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1A-8 |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 1A-8. Check the engine protection override relay signal and return wires for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. Disconnect the engine protection override relay signal and return wires at the SDU410 unit and engine protection override relay. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine protection override relay signal and return wires for a wire-to-wire short. Place one test lead on the engine protection override relay signal wire at the SDU410 unit. Place the other test lead on all other wires at the SDU410 unit. Place one test lead on the engine protection override relay return wire at the SDU410 unit. Place the other test lead on all other contacts on the engine protection override relay. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 1A-9 |  |
>
> #### STEP 1A-9. Check the engine protection override relay signal wire for a short to ground.
>
> | **Conditions:** Open the customer interface box. Disconnect the engine protection override relay signal wire at the DCU410 unit. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine protection override relay signal wire for a short to ground. Place one test lead on the engine protection override relay signal wire at the SDU410 terminal strip. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | Contact a Cummins® Authorized Repair Location |  |
