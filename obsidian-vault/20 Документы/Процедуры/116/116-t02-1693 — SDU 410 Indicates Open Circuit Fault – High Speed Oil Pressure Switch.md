---
aliases:
  - "SDU 410: обрыв цепи датчика давления масла верхнего диапазона"
type: "Процедура"
doc: "116-t02-1693"
title_en: "SDU 410: Indicates Open Circuit Fault – High Speed Oil Pressure Switch"
title_ru: "SDU 410: обрыв цепи датчика давления масла верхнего диапазона"
modified: "2026-04-23"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1693.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1693.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# SDU 410: Indicates Open Circuit Fault – High Speed Oil Pressure Switch
**SDU 410: обрыв цепи датчика давления масла верхнего диапазона**

> [!abstract] Процедура · `116-t02-1693`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2026-04-23
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1693.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1693.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

Сообщение об ошибке отображается на блоке управления дизельным двигателем (DCU) 410E.

### Как пользоваться этим деревом

**Описание схемы**

SDU 410 имеет восемь входов переключателей. Каждый вход переключателя имеет обнаружение неисправности открытой цепи. SDU 410 отслеживает сопротивление цепи. Высокоскоростной переключатель давления масла контролирует давление масла выше 1400 оборотов в минуту. Резистор 10k Ом установлен в разъеме, который соединяется с переключателем.

**Местонахождение компонента**

SDU 410 находится в поле интерфейса клиента.

**Условия для проведения диагностики**

Включатель питания клиентского интерфейса.

**Условия для установки кода**

SDU 410 обнаруживает открытую цепь. Общее сопротивление цепи больше 10k ом.

**Действия, предпринимаемые при активной работе кода ошибки**

DCU 410E будет отображать одну из следующих ошибок:

Низкое давление масла (высокая скорость)

### Практические замечания

Возможные причины включают:

- Сломанная или отключенная проводка

- Поврежденный или отсутствующий резистор обнаружения открытой цепи

- Неисправный переключатель

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте проводные соединения. |  |
|  | **ШАГ 1А.** Проверить все точки подключения проводной упряжки. | Связи плотные и безопасные? |
| ШАГ 2. | Проверьте высокоскоростной переключатель давления масла. |  |
|  | **ШАГ 2А.** Проверьте быстродействующий переключатель давления масла. | Больше 100 тысяч ом? |
|  | **STEP 2B** Проверьте резистор переключателя высокого давления масла. | Больше 11 тысяч ом? |
| ШАГ 3. | Проверьте высокоскоростной переключатель давления масла. |  |
|  | **STEP 3A.** Проверьте сигнал высокого давления масла и провода возврата для открытой цепи. | Больше 10 Ом? |
|  | **STEP 3B.** Проверьте сигнал высокого давления масла и провода возврата для короткого провода к проводу. | Больше 10 Ом? |
|  | **STEP 3C** Проверить высокоскоростной сигнальный провод давления масла на короткое время до земли. | Больше 10 Ом? |

### ШАГ 1. Проверьте проводные соединения.

#### ШАГ 1A. Проверьте все точки подключения проводов.

| **Условия:** Двигатель выключен. Выключатель питания клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте следующие точки подключения для безопасного соединения. SDU 410 терминально-блоковое соединение внутри окна интерфейса клиента. Опциональные клиентские сетевые соединения. | Связи плотные и безопасные? *Да | 2А |
| Связи плотные и безопасные? **NORepair:** Подключите любые неподключенные проводные ремни. Ремонт или замена поврежденных соединений. Внутри клиентского интерфейса: См. процедуру 015-138 в разделе 15. Дополнительные клиентские сетевые соединения: См. сервисную документацию изготовителя оборудования. | Ремонт завершён. |  |

### ШАГ 2. Проверьте высокоскоростной переключатель давления масла.

#### ШАГ 2A. Проверьте высокоскоростной переключатель давления масла.

| **Условия:** Двигатель выключен. Выключатель питания клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите высокоскоростной разъём переключателя давления моторного масла. Измерьте сопротивление на высокоскоростном переключателе давления моторного масла. Поместите один испытательный щуп на высокоскоростной контакт сигнала давления моторного масла на выключателе. Поместите другой испытательный щуп на высокоскоростной обратный контакт давления моторного масла на выключателе. См. соответствующую схему проводов или идентификацию штифта и провода. | Больше 100 тысяч ом? *Да | 2В |
| Больше 100 тысяч ом? **NORepair:** Заменить высокоскоростной переключатель давления моторного масла.[[116-015-141 — Alarm System Engine Lubricating Oil Pressure Switch\|См. процедуру 015-141 в разделе 15.]] | Ремонт завершён. |  |

#### ШАГ 2B. Проверьте высокоскоростной резистор переключателя давления масла.

| **Условия:** Двигатель выключен. Выключатель питания клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите высокоскоростной разъём переключателя давления моторного масла. Измерьте сопротивление через SUPPLY и SIGNAL штифты на высокоскоростном разъеме переключателя давления масла. Поместите один испытательный щуп на высокоскоростную проводку под давлением моторного масла, чтобы установить контакт сигнала. Поместите другой испытательный щуп на контакт с поставкой. См. соответствующую схему проводов или идентификацию штифта и провода. | Больше 11 тысяч ом? **YESRepair:** Заменить резистор в разъеме высокоскоростного переключателя давления масла проводкой ремня. | Ремонт завершён. |
| Больше 11 тысяч ом? **НЕТ** | 3А |  |

### ШАГ 3. Проверьте высокоскоростной переключатель давления масла.

#### ШАГ 3A. Проверьте сигнал высокого давления масла и возвратные провода для открытой цепи.

| **Условия:** Откройте окно интерфейса клиента. Отсоедините высокоскоростные провода SIGNAL и RETURN на блоке SDU 410 и разъёме C4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте высокоскоростные провода давления масла SIGNAL и RETURN для открытой цепи. Поместите один испытательный щуп на высокоскоростной провод SIGNAL давления масла в блок SDU 410. Поместите другой испытательный щуп на высокоскоростной контакт сигнала давления масла на разъем С4. Поместите один испытательный щуп на высокоскоростной провод под давлением масла RETURN на блоке SDU 410. Поместите другой испытательный щуп на высокоскоростной обратный контакт давления масла на разъеме C4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Больше 10 Ом?  Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 в разделе 15.]] | Ремонт завершён. |
| Больше 10 Ом? **НЕТ** | 3B |  |

#### ШАГ 3B. Проверьте сигнал высокого давления масла и возвращайте провода для короткого провода к проводу.

| **Условия:** Откройте окно интерфейса клиента. Отключите высокоскоростные провода SIGNAL и RETURN на SDU 410 и разъеме C4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте высокоскоростные провода давления масла SIGNAL и RETURN для короткой проволоки. Поместите один испытательный щуп на высокоскоростной провод SIGNAL давления масла в блок SDU 410. Поместите другой испытательный щуп на все другие штифты на разъеме C4. Поместите один испытательный щуп на высокоскоростной провод под давлением масла RETURN на блоке SDU 410. Поместите другой испытательный щуп на все другие штифты на разъеме C4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Больше 10 Ом?  Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 в разделе 15.]] | Ремонт завершён. |
| Больше 10 Ом? **НЕТ** | 3B |  |

#### ШАГ 3C. Проверьте высокоскоростной сигнал давления масла для короткого приземления.

| **Условия:** Откройте окно интерфейса клиента. Отсоедините высокоскоростной провод SIGNAL с давлением масла на блоке SDU 410 и разъеме C4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте высокоскоростной провод SIGNAL на короткое время до земли. Поместите один испытательный щуп на высокоскоростной провод SIGNAL давления масла в блок SDU 410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Больше 10 Ом?  Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 в разделе 15.]] | Ремонт завершён. |
| Больше 10 Ом? **NORepair:** Заменить SDU 410.[[116-015-122 — Customer Interface Box Shutdown Unit\|См. процедуру 015-122 в разделе 15.]] | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> The fault message is displayed on the diesel control unit (DCU) 410E.
>
> ### How To Use This Tree
>
> **Circuit Description**
>
> The SDU 410 has eight switch inputs. Each switch input has open circuit fault detection. The SDU 410 is monitoring the resistance of the circuit. The high speed oil pressure switch monitors oil pressure above 1400 RPM. A 10k ohm resistor is installed in the connector that mates to the switch.
>
> **Component Location**
>
> The SDU 410 is in the customer interface box.
>
> **Conditions for Running the Diagnostics**
>
> Customer interface box power switch ON.
>
> **Conditions for Setting the Code**
>
> The SDU 410 detects an open circuit. The overall resistance of the circuit is greater than 10k ohms.
>
> **Actions Taken when the Fault Code is Active**
>
> The DCU 410E will display one of the following faults:
>
> Lube Oil Pressure Low (High Speed)
>
> ### Shoptalk
>
> Possible causes include:
>
> - Broken or disconnected wiring
>
> - Damaged or missing open circuit detection resistor
>
> - Malfunctioning switch
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check wiring connections. |  |
> |  | **STEP 1A.** Check all wiring harness connection points. | Connections tight and secure? |
> | STEP 2. | Check the high speed oil pressure switch. |  |
> |  | **STEP 2A.** Check the high speed oil pressure switch. | Greater than 100k ohms? |
> |  | **STEP 2B.** Check the high speed oil pressure switch connector resistor. | Greater than 11k ohms? |
> | STEP 3. | Check the high speed oil pressure switch wiring harness. |  |
> |  | **STEP 3A.** Check the high speed oil pressure signal and return wires for an open circuit. | Greater than 10 ohms? |
> |  | **STEP 3B.** Check the high speed oil pressure signal and return wires for a wire-to-wire short. | Greater than 10 ohms? |
> |  | **STEP 3C.** Check the high speed oil pressure signal wire for a short to ground. | Greater than 10 ohms? |
>
> ### STEP 1. Check wiring connections.
>
> #### STEP 1A. Check all wiring harness connection points.
>
> | **Conditions:** Engine OFF. Customer interface box power switch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the following connection points for secure connection. SDU 410 terminal block connection inside the customer interface box. Optional customer-provided circuit connections. | Connections tight and secure? **YES** | 2A |
> | Connections tight and secure? **NORepair:** Connect any disconnected harnesses. Repair or replace damaged connections. Inside customer interface box: Refer to Procedure 015-138 in Section 15. Optional customer-provided circuit connections: See equipment manufacturer service information. | Repair complete. |  |
>
> ### STEP 2. Check the high speed oil pressure switch.
>
> #### STEP 2A. Check the high speed oil pressure switch.
>
> | **Conditions:** Engine OFF. Customer interface box power switch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disconnect the high speed lubricating oil pressure switch connector. Measure the resistance at the high speed lubricating oil pressure switch. Place one test lead on the high speed lubricating oil pressure SIGNAL pin at the switch. Place the other test lead on the high speed lubricating oil pressure RETURN pin at the switch. See the appropriate wiring diagram or pin and wire identification. | Greater than 100k ohms? **YES** | 2B |
> | Greater than 100k ohms? **NORepair:** Replace the high speed lubricating oil pressure switch. [[116-015-141 — Alarm System Engine Lubricating Oil Pressure Switch\|Refer to Procedure 015-141 in Section 15.]] | Repair complete. |  |
>
> #### STEP 2B. Check the high speed oil pressure switch connector resistor.
>
> | **Conditions:** Engine OFF. Customer interface box power switch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disconnect the high speed lubricating oil pressure switch connector. Measure the resistance across SUPPLY and the SIGNAL pins on the high speed oil pressure switch connector. Place one test lead on the high speed lubricating oil pressure wiring harness SIGNAL pin. Place the other test lead on the SUPPLY pin. See the appropriate wiring diagram or pin and wire identification. | Greater than 11k ohms? **YESRepair:** Replace the resistor in the connector of the high speed oil pressure switch wiring harness. | Repair complete. |
> | Greater than 11k ohms? **NO** | 3A |  |
>
> ### STEP 3. Check the high speed oil pressure switch wiring harness.
>
> #### STEP 3A. Check the high speed oil pressure signal and return wires for an open circuit.
>
> | **Conditions:** Open the customer interface box. Disconnect the high speed oil pressure SIGNAL and RETURN wires at the SDU 410 unit and connector C4. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the high speed oil pressure SIGNAL and RETURN wires for an open circuit. Place one test lead on the high speed oil pressure SIGNAL wire at the SDU 410 unit. Place the other test lead on the high speed oil pressure SIGNAL pin at the C4 connector. Place one test lead on the high speed oil pressure RETURN wire at the SDU 410 unit. Place the other test lead on the high speed oil pressure RETURN pin at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Greater than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete. |
> | Greater than 10 ohms? **NO** | 3B |  |
>
> #### STEP 3B. Check the high speed oil pressure signal and return wires for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. Disconnect the high speed oil pressure SIGNAL and RETURN wires at the SDU 410 unit and C4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the high speed oil pressure SIGNAL and RETURN wires for a wire-to-wire short. Place one test lead on the high speed oil pressure SIGNAL wire at the SDU 410 unit. Place the other test lead on all other pins at the C4 connector. Place one test lead on the high speed oil pressure RETURN wire at the SDU 410 unit. Place the other test lead on all other pins at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Greater than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete. |
> | Greater than 10 ohms? **NO** | 3B |  |
>
> #### STEP 3C. Check the high speed oil pressure signal wire for a short to ground.
>
> | **Conditions:** Open the customer interface box. Disconnect the high speed oil pressure SIGNAL wire at the SDU 410 unit and C4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the high speed oil pressure SIGNAL wire for a short to ground. Place one test lead on the high speed oil pressure SIGNAL wire at the SDU 410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Greater than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete. |
> | Greater than 10 ohms? **NORepair:** Replace the SDU 410. [[116-015-122 — Customer Interface Box Shutdown Unit\|Refer to Procedure 015-122 in Section 15.]] | Repair complete. |  |
