---
type: "Процедура"
doc: "19-t05-112"
title_en: "FAULT CODE 112- Timing Fueling Flow Mismatch"
modified: "2014-12-02"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-t05-112.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-t05-112.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# FAULT CODE 112- Timing Fueling Flow Mismatch

> [!abstract] Процедура · `19-t05-112`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2014-12-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-t05-112.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-t05-112.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте жалобу. |  |
|  | **STEP 1A.** Проверка активных кодов неисправностей, отличных от кода 112. | Активные коды ошибок? |
|  | **ШАГ 1В.** Интервью с водителем по поводу симптомов, присутствующих в двигателе. | Присутствуют симптомы? |
|  | **STEP 1C** Мониторинг параметров времени для перенапряжения топлива синхронизации. | Сроки топлива перенапряжены? |
| ШАГ 2. | Проверьте впускную сторону топливной системы. |  |
|  | **СТЭП 2А** Проверить уровень топливного бака. | Топливо в баке? |
|  | **STEP 2B** Проверить топливную систему на наличие утечек, неработающих линий и рыхлых фитингов. | Разорванные линии, свободная арматура или утечка топлива? |
|  | **STEP 2C.** Проверьте ограничение впуска топлива. | Больше 203 мм рт. ст. [8 в рт. ст.]? |
|  | **STEP 2D** Проверка наличия воздуха в топливе. | Воздух в топливе? |
| ШАГ 3. | Проверьте компоненты топливной системы. |  |
|  | **СТЭП 3А** Проверить выходное давление топливного насоса. | Давление на выходе топливного насоса правильное? |
|  | **ШАГ 3А-1.** Проверьте топливные форсунки. | Утечка равна выходу с передней и задней половинки? |
|  | **ШАГ 3А-2.** Проверить наличие топлива в масле или теплоносителях. | Топливо в масле или хладагенте? |
|  | **STEP 3B** Осмотрите экран привода на предмет наличия мусора. | Отбеливатели на входном экране привода? |
|  | **STEP 3C** Проверить привод на предмет коррозии. | Коррозия на приводе? |
| ШАГ 4. | Сбросьте коды неисправностей. |  |
|  | **STEP 4A.** Отключить код ошибки. | Код 112 неактивен? |
|  | **STEP 4B.** Очистить коды неактивных ошибок. | Коды неисправностей очищены? |

### ШАГ 1. Проверьте жалобу.

#### ШАГ 1A. Проверьте активные коды неисправностей, отличные от кода 112.

| **Условия:** Включить переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте активные коды неисправностей, отличные от кода 112. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Активные коды ошибок? В первую очередь исследуйте другие коды ошибок. | Соответствующая процедура кодирования неисправностей |
| Активные коды ошибок? **НЕТ** | 1В |  |

#### ШАГ 1B. Интервью с водителем для выявления симптомов двигателя.

| **Условия:** Включить переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Интервью с водителем для следующих целей: Спросите оператора, присутствуют ли конкретные симптомы или остановки / даты из-за кода 112 ошибки. | Присутствуют симптомы? *Да | 1С |
| Присутствуют симптомы? **NORepair:** Очистить код ошибки. Неактивные неисправности были зарегистрированы. Поскольку клиент не испытывает проблем, очистите код ошибки. | 4B |  |

#### ШАГ 1C. Мониторинг временных параметров для избыточного давления топлива.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Мониторинг временных параметров для избыточного давления топлива. Используйте инструмент электронного обслуживания INSITETM для мониторинга желаемого времени заправки топливом и расчетных параметров заправки топливом. Является ли расчетное время заправки топливом последовательно выше, чем желаемое время заправки топливом? Если он выше, он чрезмерно увеличивает давление при заправке топливом. | Сроки топлива перенапряжены? **Ремонт:** Заменить привод синхронизации.[[19-019-339 — Timing Actuator\|См. процедуру 019-339 в разделе 19.]] | 4А |
| Сроки топлива перенапряжены? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте впускную сторону топливной системы.

#### ШАГ 2A. Проверьте уровень топливного бака.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте уровень топливного бака на следующее: Топливо в баке? | Топливо в баке? *Да | 2В |
| Топливо в баке? **NORepair: **Заполните топливный бак. | 4А |  |

#### ШАГ 2B. Осмотрите топливную систему на наличие утечек, сломанных линий и рыхлых фитингов.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить топливную систему на предмет: Утечка разорванных линий Размытые фитинги. | Разорванные линии, свободная арматура или утечка топлива? **Ремонт:** Ремонт утечек. Затянуть или заменить протекающую фитинг или топливную линию. Замените топливный трубопровод. Используйте следующую процедуру в руководстве по обслуживанию QSK19, QSK19 CM850 MCRS и QSK19 CM2150 MCRS, в бюллетене [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. См. процедуру 006-024 в разделе 6. Используйте следующую процедуру в руководстве по устранению неполадок и ремонту QSK23, Bulletin [[4021375 — QSK23 Troubleshooting and Repair Manual\|4021375]]. См. процедуру 006-024 в разделе 6. Используйте следующую процедуру в руководстве по обслуживанию QSK45 и QSK60, в бюллетене [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. См. процедуру 006-024 в разделе 6. Используйте следующую процедуру в руководстве по устранению неполадок и ремонту QSK78, Бюллетень 3666727. См. процедуру 006-024 в разделе 6. | 4А |
| Разорванные линии, свободная арматура или утечка топлива? **НЕТ** | 2C |  |

#### ШАГ 2C. Проверьте ограничение входного отверстия топлива.

| **Условия:** Включить переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте ограничение впуска топлива следующим образом: Измерьте ограничение входа. Используйте следующую процедуру в руководстве по обслуживанию QSK19, QSK19 CM850 MCRS и QSK19 CM2150 MCRS, в бюллетене [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. См. процедуру 005-016 в разделе 5. Используйте следующую процедуру в руководстве по устранению неполадок и ремонту QSK23, Bulletin [[4021375 — QSK23 Troubleshooting and Repair Manual\|4021375]]. См. процедуру 005-016 в разделе 5. Используйте следующую процедуру в руководстве по обслуживанию QSK45 и QSK60, в бюллетене [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. См. процедуру 005-016 в разделе 5. Используйте следующую процедуру в руководстве по устранению неполадок и ремонту QSK78, Бюллетень 3666727. См. процедуру 005-016 в разделе 5. | Больше 203 мм рт. ст. [8 в рт. ст.]? **Ремонт: **Найдите причину ограничения и удалите ограничение. Проверить наличие забитых топливных фильтров, мусора в топливном баке, забитых вентиляционных отверстий топливного бака, обрушенных или неисправных топливных линий или неисправных контрольных клапанов. | 4А |
| Больше 203 мм рт. ст. [8 в рт. ст.]? **НЕТ** | 2D |  |

#### ШАГ 2D. Проверьте воздух в топливе.

| **Условия:** Включить переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте воздух в топливе. Проверьте наличие воздуха в топливной системе. Используйте следующую процедуру в руководстве по обслуживанию QSK19, QSK19 CM850 MCRS и QSK19 CM2150 MCRS, в бюллетене [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. См. процедуру 005-016 в разделе 5. Используйте следующую процедуру в руководстве по устранению неполадок и ремонту QSK23, Bulletin [[4021375 — QSK23 Troubleshooting and Repair Manual\|4021375]]. См. процедуру 005-016 в разделе 5. Используйте следующую процедуру в руководстве по обслуживанию QSK45 и QSK60, в бюллетене [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. См. процедуру 005-016 в разделе 5. Используйте следующую процедуру в руководстве по устранению неполадок и ремонту QSK78, Бюллетень 3666727. См. процедуру 005-016 в разделе 5. | Воздух в топливе? **Ремонт: **Найдите причину попадания воздуха в топливо. Проверьте наличие отсутствующих уплотнений на входных топливных фитингах, рыхлых или сломанных фитингах и сломанных линиях. | 4А |
| Воздух в топливе? **НЕТ** | 3А |  |

### ШАГ 3. Проверьте компоненты топливной системы.

#### ШАГ 3A. Проверьте выходное давление топливного насоса.

| **Условия:** Включить переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте выходное давление топливного насоса. Измерить выходное давление насоса на фитинге CompuchekTM. Используйте следующую процедуру в руководстве по обслуживанию QSK19, QSK19 CM850 MCRS и QSK19 CM2150 MCRS, в бюллетене [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. См. процедуру 005-016 в разделе 5. Используйте следующую процедуру в руководстве по устранению неполадок и ремонту QSK23, Bulletin [[4021375 — QSK23 Troubleshooting and Repair Manual\|4021375]]. См. процедуру 005-016 в разделе 5. Используйте следующую процедуру в руководстве по обслуживанию QSK45 и QSK60, в бюллетене [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. См. процедуру 005-016 в разделе 5. Используйте следующую процедуру в руководстве по устранению неполадок и ремонту QSK78, Бюллетень 3666727. См. процедуру 005-016 в разделе 5. | Давление на выходе топливного насоса правильное? Давление на выходной сигнал QSK19: Минимальный 379 кПа \[55 psi\] @ 600 rpm Минимальный 1207 кПа \[175 psi\] @ 1300 rpm Минимальный 1724 кПа \[250 psi\] @ 2100 rpm Минимальный 1827 кПа \[265 psi\] @ 2350 rpm. Минимальное давление на выход QSK23: Минимальный 689 кПа \[100 psi\] @ 600 rpm Минимальный 910 кПа \[132 psi\] @ 1000 rpm Минимальный 1207 кПа \[175 psi\] @ 1400 rpm Минимальный 1434 кПа \[208 psi\] Минимальный 1779 кПа \[258 psi\] @ 1800 rpm Минимальный 1999 кПа \[290 psi\] @ 2100 rpm. Минимальное давление на выход QSK45 и QSK60: Минимальный 758 кПа \[110 psi\] @ 600 rpm Минимальный 1379 кПа \[200 psi\] @ 1300 rpm Минимальный 1724 кПа \[250 psi\] @ 1900 rpm Минимальный 1793 кПа \[260 psi\] @ 2300 rpm. Минимальное давление на выход QSK78: Минимальный 793 кПа \[115 psi\] @ 600 rpm Минимальный 1689 кПа \[245 psi\] @ 1300 rpm Минимальный 2068 кПа \[300 psi\] @ 1900 rpm Минимальный 2482 кПа \[360 psi\] @ 2300 rpm. | 3B |
| Давление на выходе топливного насоса правильное? **NORepair:** Продолжайте устранение неполадок. | 3А-1-1 |  |

#### ШАГ 3A-1. Проверьте топливные форсунки.

| **Условия:** Включить переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте топливные форсунки. Кольца могут быть проверены путем наблюдения выходной мощности передних трех цилиндров по сравнению с задними тремя цилиндрами на двигателях серии QSK19 и наблюдения выходной мощности слива левого берега цилиндров по сравнению с правым берегом цилиндров на двигателях серии QSK45 и QSK60. Отсоедините дренажные линии на Т-переходе. Разместите каждую половину в отдельные ведра одинакового размера. Управляйте двигателем с номинальной скоростью в течение достаточного времени, чтобы определить, равна ли мощность с каждой половины. | Утечка равна выходу с передней и задней половинки? *Да | 3А-2 |
| Утечка равна выходу с передней и задней половинки? **NORepair:** Заменить топливные форсунки на неисправном берегу. Замените форсунку. Используйте следующую процедуру в руководстве по обслуживанию QSK19, QSK19 CM850 MCRS и QSK19 CM2150 MCRS, в бюллетене [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. См. процедуру 006-026 в разделе 6. Используйте следующую процедуру в руководстве по устранению неполадок и ремонту QSK23, Bulletin [[4021375 — QSK23 Troubleshooting and Repair Manual\|4021375]]. См. процедуру 006-026 в разделе 6. Используйте следующую процедуру в руководстве по обслуживанию QSK45 и QSK60, в бюллетене [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. См. процедуру 006-026 в разделе 6. Используйте следующую процедуру в руководстве по устранению неполадок и ремонту QSK78, Бюллетень 3666727. См. процедуру 006-026 в разделе 6. | 4А |  |

#### ШАГ 3A-2. Проверьте наличие топлива в масле или охлаждающей жидкости.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте наличие топлива в масле или охлаждающей жидкости. Исследуйте топливо или масло в охлаждающей жидкости. | Топливо в масле или хладагенте? **Ремонт:** Заменить привод синхронизации.[[19-019-339 — Timing Actuator\|См. процедуру 019-339 в разделе 19.]] | Соответствующее дерево симптомов устранения неполадок |
| Топливо в масле или хладагенте? **НЕТ** | 4А |  |

#### ШАГ 3B. Проверьте экран привода на предмет мусора.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте экран привода на предмет мусора. Удалите привод времени, чтобы осмотреть экран на предмет наличия мусора. См. процедуру 019-339 в разделе 19. | Отбеливатели на входном экране привода? **Ремонт: **Заменить экран привода синхронизации. См. процедуру 019-112 в разделе 19. | 4А |
| Отбеливатели на входном экране привода? **НЕТ** | 3C |  |

#### ШАГ 3C. Проверьте привод на коррозию.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте привод на коррозию. Удалите привод времени для проверки на коррозию. См. процедуру 019-339 в разделе 19. | Коррозия на приводе? **Ремонт:** Заменить привод синхронизации. См. процедуру 019-112 в разделе 19. | 4А |
| Коррозия на приводе? **НЕТ** | 4А |  |

### ШАГ 4. Очистите код ошибки.

#### ШАГ 4A. Отключите код неисправности.

| **Условия: **Соединить все компоненты. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите код неисправности. Запустите двигатель и пройдите весь рабочий диапазон, чтобы убедиться, что код 112 неактивен. | Код 112 неактивен? *Да | 4B |
| Код 112 неактивен? **NORepair:** Возврат к шагам устранения неполадок или свяжитесь с авторизованным местом ремонта Cummins®, если все шаги были завершены и проверены снова. | 1А |  |

#### ШАГ 4B. Сбросьте неактивные коды неисправностей.

| **Условия: **Соединить все компоненты. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сбросьте неактивные коды неисправностей. Используйте инструмент электронного сервиса INSITETM для очистки кодов неактивных ошибок. | Коды неисправностей очищены? Исправление неполадок: устранение любых оставшихся активных кодов неисправностей. | Ремонт завершён |
| Коды неисправностей очищены? **НЕТ** | Соответствующие диаграммы устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Verify the complaint. |  |
> |  | **STEP 1A.** Check for active fault codes other than Fault Code 112. | Fault codes active? |
> |  | **STEP 1B.** Interview the driver for engine symptoms present. | Symptoms present? |
> |  | **STEP 1C.** Monitor the timing parameters for over-pressurization of the timing fuel. | Timing fuel over-pressurized? |
> | STEP 2. | Check the inlet side of the fuel system. |  |
> |  | **STEP 2A.** Check the fuel tank level. | Fuel in tank? |
> |  | **STEP 2B.** Inspect the fuel system for leaks, broken lines, and loose fittings. | Broken lines, loose fittings or fuel leaks? |
> |  | **STEP 2C.** Check the fuel inlet restriction. | Greater than 203 mm Hg \[8 in Hg\]? |
> |  | **STEP 2D.** Check for air in the fuel. | Air in fuel? |
> | STEP 3. | Check the fuel system components. |  |
> |  | **STEP 3A.** Check the fuel pump output pressure. | Fuel pump output pressure correct? |
> |  | **STEP 3A-1.** Check the injector o-rings. | Drain output equal from front and rear halves? |
> |  | **STEP 3A-2.** Check for fuel in the oil or coolant. | Fuel in oil or coolant? |
> |  | **STEP 3B.** Inspect the actuator screen for debris. | Debris on inlet actuator screen? |
> |  | **STEP 3C.** Inspect the actuator for corrosion. | Corrosion on actuator? |
> | STEP 4. | Clear the fault codes. |  |
> |  | **STEP 4A.** Disable the fault code. | Fault Code 112 inactive? |
> |  | **STEP 4B.** Clear the inactive fault codes. | Fault codes cleared? |
>
> ### STEP 1. Verify the complaint.
>
> #### STEP 1A. Check for active fault codes other than Fault Code 112.
>
> | **Conditions:** Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for active fault codes other than Fault Code 112. Use INSITE™ electronic service tool to read the fault codes. | Fault codes active? **YESRepair:** Investigate other fault codes first. | Appropriate fault code procedure |
> | Fault codes active? **NO** | 1B |  |
>
> #### STEP 1B. Interview the driver for engine symptoms present.
>
> | **Conditions:** Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Interview the driver for the following: Ask the operator if specific symptoms or shutdowns/derates due to Fault Code 112 are present. | Symptoms present? **YES** | 1C |
> | Symptoms present? **NORepair:** Clear the fault code. Inactive faults have been logged. Since the customer is **not** experiencing a problem, clear the fault code. | 4B |  |
>
> #### STEP 1C. Monitor the timing parameters for over-pressurization of the timing fuel.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Monitor the timing parameters for over-pressurization of the timing fuel. Use INSITE™ electronic service tool to monitor the desired timing fueling and the estimated timing fueling parameters. Is the estimated timing fueling consistently higher than the desired timing fueling? If it is higher, it is over-pressurizing the timing fueling. | Timing fuel over-pressurized? **YESRepair:** Replace the timing actuator. [[19-019-339 — Timing Actuator\|Refer to Procedure 019-339 in Section 19.]] | 4A |
> | Timing fuel over-pressurized? **NO** | 2A |  |
>
> ### STEP 2. Check the inlet side of the fuel system.
>
> #### STEP 2A. Check the fuel tank level.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the fuel tank level for the following: Fuel in the tank? | Fuel in tank? **YES** | 2B |
> | Fuel in tank? **NORepair:** Fill the fuel tank. | 4A |  |
>
> #### STEP 2B. Inspect the fuel system for leaks, broken lines, and loose fittings.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the fuel system for the following: Leaks Broken lines Loose fittings. | Broken lines, loose fittings or fuel leaks? **YESRepair:** Repair the leak. Tighten or replace the leaking fitting or fuel line. Replace the fuel line. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. Refer to Procedure 006-024 in Section 6. Use the following procedure in the QSK23 Troubleshooting and Repair Manual, Bulletin [[4021375 — QSK23 Troubleshooting and Repair Manual\|4021375]]. Refer to Procedure 006-024 in Section 6. Use the following procedure in the QSK45 and QSK60 Service Manual, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. Refer to Procedure 006-024 in Section 6. Use the following procedure in the QSK78 Troubleshooting and Repair Manual, Bulletin 3666727. Refer to Procedure 006-024 in Section 6. | 4A |
> | Broken lines, loose fittings or fuel leaks? **NO** | 2C |  |
>
> #### STEP 2C. Check the fuel inlet restriction.
>
> | **Conditions:** Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the fuel inlet restriction as follows: Measure the inlet restriction. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. Refer to Procedure 005-016 in Section 5. Use the following procedure in the QSK23 Troubleshooting and Repair Manual, Bulletin [[4021375 — QSK23 Troubleshooting and Repair Manual\|4021375]]. Refer to Procedure 005-016 in Section 5. Use the following procedure in the QSK45 and QSK60 Service Manual, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. Refer to Procedure 005-016 in Section 5. Use the following procedure in the QSK78 Troubleshooting and Repair Manual, Bulletin 3666727. Refer to Procedure 005-016 in Section 5. | Greater than 203 mm Hg \[8 in Hg\]? **YESRepair:** Find the cause of restriction and remove restriction. Check for clogged fuel filters, debris in the fuel tank, fuel tank vents clogged, collapsed or faulty fuel lines, or faulty check valves. | 4A |
> | Greater than 203 mm Hg \[8 in Hg\]? **NO** | 2D |  |
>
> #### STEP 2D. Check for air in the fuel.
>
> | **Conditions:** Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for air in the fuel. Check for air in the fuel system. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. Refer to Procedure 005-016 in Section 5. Use the following procedure in the QSK23 Troubleshooting and Repair Manual, Bulletin [[4021375 — QSK23 Troubleshooting and Repair Manual\|4021375]]. Refer to Procedure 005-016 in Section 5. Use the following procedure in the QSK45 and QSK60 Service Manual, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. Refer to Procedure 005-016 in Section 5. Use the following procedure in the QSK78 Troubleshooting and Repair Manual, Bulletin 3666727. Refer to Procedure 005-016 in Section 5. | Air in fuel? **YESRepair:** Find the cause of air in the fuel. Check for missing o-ring seals in the inlet fuel fittings, loose or broken fittings, and broken lines. | 4A |
> | Air in fuel? **NO** | 3A |  |
>
> ### STEP 3. Check the fuel system components.
>
> #### STEP 3A. Check the fuel pump output pressure.
>
> | **Conditions:** Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the fuel pump output pressure. Measure the output pressure of the pump at the Compuchek™ fitting. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. Refer to Procedure 005-016 in Section 5. Use the following procedure in the QSK23 Troubleshooting and Repair Manual, Bulletin [[4021375 — QSK23 Troubleshooting and Repair Manual\|4021375]]. Refer to Procedure 005-016 in Section 5. Use the following procedure in the QSK45 and QSK60 Service Manual, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. Refer to Procedure 005-016 in Section 5. Use the following procedure in the QSK78 Troubleshooting and Repair Manual, Bulletin 3666727. Refer to Procedure 005-016 in Section 5. | Fuel pump output pressure correct? **YESRepair:** Minimum Output Pressure for QSK19: Minimum 379 kPa \[55 psi\] @ 600 rpm Minimum 1207 kPa \[175 psi\] @ 1300 rpm Minimum 1724 kPa \[250 psi\] @ 2100 rpm Minimum 1827 kPa \[265 psi\] @ 2350 rpm. Minimum Output Pressure for QSK23: Minimum 689 kPa \[100 psi\] @ 600 rpm Minimum 910 kPa \[132 psi\] @ 1000 rpm Minimum 1207 kPa \[175 psi\] @ 1400 rpm Minimum 1434 kPa \[208 psi\] @1500 rpm Minimum 1779 kPa \[258 psi\] @ 1800 rpm Minimum 1999 kPa \[290 psi\] @ 2100 rpm. Minimum Output Pressure for QSK45 and QSK60: Minimum 758 kPa \[110 psi\] @ 600 rpm Minimum 1379 kPa \[200 psi\] @ 1300 rpm Minimum 1724 kPa \[250 psi\] @ 1900 rpm Minimum 1793 kPa \[260 psi\] @ 2300 rpm. Minimum Output Pressure for QSK78: Minimum 793 kPa \[115 psi\] @ 600 rpm Minimum 1689 kPa \[245 psi\] @ 1300 rpm Minimum 2068 kPa \[300 psi\] @ 1900 rpm Minimum 2482 kPa \[360 psi\] @ 2300 rpm. | 3B |
> | Fuel pump output pressure correct? **NORepair:** Continue troubleshooting. | 3A-1 |  |
>
> #### STEP 3A-1. Check the injector o-rings.
>
> | **Conditions:** Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the injector o-rings. The o-rings can be checked by observing the drain output of the front three versus the rear three cylinders on the QSK19 series engines and by observing the drain output of the left bank of cylinders versus the right bank of cylinders on the QSK45 and QSK60 series engines. Disconnect the drain lines at the T-junction. Place each half into separate, equal-size buckets. Operate the engine at rated speed for enough time to determine if output is equal from each half. | Drain output equal from front and rear halves? **YES** | 3A-2 |
> | Drain output equal from front and rear halves? **NORepair:** Replace the injector o-rings on the faulty bank. Replace the injector. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. Refer to Procedure 006-026 in Section 6. Use the following procedure in the QSK23 Troubleshooting and Repair Manual, Bulletin [[4021375 — QSK23 Troubleshooting and Repair Manual\|4021375]]. Refer to Procedure 006-026 in Section 6. Use the following procedure in the QSK45 and QSK60 Service Manual, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. Refer to Procedure 006-026 in Section 6. Use the following procedure in the QSK78 Troubleshooting and Repair Manual, Bulletin 3666727. Refer to Procedure 006-026 in Section 6. | 4A |  |
>
> #### STEP 3A-2. Check for fuel in the oil or coolant.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for fuel in the oil or coolant. Investigate for fuel or oil in coolant. | Fuel in oil or coolant? **YESRepair:** Replace the timing actuator. [[19-019-339 — Timing Actuator\|Refer to Procedure 019-339 in Section 19.]] | Appropriate troubleshooting symptom tree |
> | Fuel in oil or coolant? **NO** | 4A |  |
>
> #### STEP 3B. Inspect the actuator screen for debris.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the actuator screen for debris. Remove the timing actuator to inspect the screen for debris. Refer to Procedure 019-339 in Section 19. | Debris on inlet actuator screen? **YESRepair:** Replace the timing actuator screen. Refer to Procedure 019-112 in Section 19. | 4A |
> | Debris on inlet actuator screen? **NO** | 3C |  |
>
> #### STEP 3C. Inspect the actuator for corrosion.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the actuator for corrosion. Remove the timing actuator to inspect for corrosion. Refer to Procedure 019-339 in Section 19. | Corrosion on actuator? **YESRepair:** Replace the timing actuator. Refer to Procedure 019-112 in Section 19. | 4A |
> | Corrosion on actuator? **NO** | 4A |  |
>
> ### STEP 4. Clear the fault code.
>
> #### STEP 4A. Disable the fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable the fault code. Start the engine and run throughout the operating range to verify that Fault Code 112 stays inactive. | Fault Code 112 inactive? **YES** | 4B |
> | Fault Code 112 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
>
> #### STEP 4B. Clear the inactive fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | Fault codes cleared? **YESRepair:** Troubleshoot any remaining active fault codes. | Repair complete |
> | Fault codes cleared? **NO** | Appropriate troubleshooting charts |  |
