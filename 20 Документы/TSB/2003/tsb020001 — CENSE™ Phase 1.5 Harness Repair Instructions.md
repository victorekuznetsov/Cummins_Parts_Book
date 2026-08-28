---
type: "TSB"
doc: "tsb020001"
title_en: "CENSE™ Phase 1.5 Harness Repair Instructions"
released: "2003-10-09"
modified: "2003-10-09"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
figures: 6
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2002/tsb020001.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb020001.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QSK60"
  - "год/2003"
  - "перевод/машинный"
---

# CENSE™ Phase 1.5 Harness Repair Instructions

> [!abstract] TSB · `tsb020001`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Даты:** выпущен 2003-10-09 · изменён 2003-10-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2002/tsb020001.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb020001.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## CENSETM Фаза 1.5 Инструкции по ремонту проводов

### Суть проблемы

Недавно было обнаружено, что все жгуты проводов для электропроводки правого берега фазы 1.5 CENSETM, номер детали 4017464, на двигателях QSK60C были изготовлены неправильно. Разъемы температуры выхлопных газов были неправильно подключены для силовых цилиндров 1, 2, 5 и 7, что привело к неправильной диагностике кодов неисправностей цилиндров.

### Подтверждение

| Поврежденные серийные номера двигателя (только QSK60) |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
| 33150763 | 33150602 | 33150387 | 33150015 | 33149343 | 33148906 | 33148449 | 33147903 |
| 33150758 | 33150598 | 33150374 | 33149988 | 33149314 | 33148901 | 33148444 | 33147878 |
| 33150755 | 33150596 | 33150363 | 33149973 | 33149277 | 33148897 | 33148401 | 33147584 |
| 33150710 | 33150591 | 33150345 | 33149964 | 33149264 | 33148890 | 33148390 | 33147332 |
| 33150706 | 33150587 | 33150341 | 33149951 | 33149258 | 33148781 | 33148385 | 33147260 |
| 33150695 | 33150585 | 33150337 | 33149934 | 33149252 | 33148684 | 33148377 | 33147083 |
| 33150687 | 33150580 | 33150331 | 33149903 | 33149247 | 33148620 | 33148355 | 33147075 |
| 33150674 | 33150576 | 33150321 | 33149719 | 33149204 | 33148616 | 33148304 | 33146876 |
| 33150668 | 33150573 | 33150313 | 33149702 | 33149201 | 33148608 | 33148280 | 33146847 |
| 33150666 | 33150568 | 33150305 | 33149688 | 33149159 | 33148601 | 33148259 | 33146819 |
| 33150657 | 33150563 | 33150291 | 33149640 | 33149077 | 33148591 | 33148244 | 33146809 |
| 33150651 | 33150561 | 33150270 | 33149493 | 33149075 | 33148586 | 33148215 |  |
| 33150649 | 33150557 | 33150262 | 33149471 | 33149029 | 33148539 | 33148196 |  |
| 33150645 | 33150522 | 33150189 | 33149461 | 33148968 | 33148534 | 33148182 |  |
| 33150635 | 33150518 | 33150181 | 33149421 | 33148962 | 33148528 | 33148170 |  |
| 33150625 | 33150420 | 33150169 | 33149408 | 33148954 | 33148467 | 33148122 |  |
| 33150619 | 33150407 | 33150147 | 33149359 | 33148948 | 33148463 | 33148077 |  |
| 33150615 | 33150397 | 33150134 | 33149356 | 33148940 | 33148456 | 33148009 |  |

> [!note] Примечание
> Последующие двигатели ESN 33146793 были исправлены на заводе и поэтому не требуют модификации.

В результате показания температуры и коды неисправностей, полученные с помощью диагностического программного обеспечения CENSETM, INSITETM, **не** соответствуют соответствующим силовым цилиндрам.

Например, INSITETM может указывать низкую или высокую температуру выхлопных газов из цилиндра № 1, когда он фактически измеряет выхлопные газы из цилиндра № 7. Как следствие, это может ввести в заблуждение техников при разборке здорового силового цилиндра при расследовании причины неисправности.

Это подтвержденная проблема с проводкой CENSETM фазы 1.5, поэтому нет никаких требований к какой-либо процедуре проверки или проверки неисправности.

Причина этой проблемы заключается в ошибке проектирования жгута проводов.

Неправильная диагностика производительности силового цилиндра может привести к тому, что нездоровый силовой цилиндр останется незамеченным. Это, очевидно, приведет к ухудшению общих характеристик двигателя и возможному прогрессивному повреждению компонентов.

### Решение

Из-за неисправности правого берега проводной ремни CENSETM (в которой лежит неисправность), инструкция по ремонту инструктирует модификацию проводов в корпусе ECM CENSETM. Изменение проводов в этом месте по существу «отменяет» неисправную проводку на правой стороне проводов.

![[rearofengine.jpg.png]]

Удалите шесть болтов М6.

Снимите крышку корпуса CENSETM.

![[alankey.jpg.png]]

Удалите верхний разъем модуля с помощью 4-мм ключа Allen, как показано.

![[plugdetach.jpg.png]]

Используя инструмент удаления штифтов Deutsch, номер детали 3824815, удалите и вставьте штифты в их правильный терминал. См. таблицу 1.

Нанесите этикетку на каждый провод при отключении с новым местоположением штифта.

Поскольку каждый штифт повторно вставляется, будет щелчок, как замки терминала в разъеме. Дайте проводу нежное притяжение, чтобы убедиться, что он расположен.

| Таблица 1 |  |
|---|---|
| Удаление из терминала | Включить в терминал |
| 31 | 01 |
| 21 | 11 |
| 01 | 14 |
| 11 | 04 |
| 14 | 22 |
| 04 | 32 |
| 22 | 31 |
| 32 | 21 |

![[alankey.jpg.png]]

Подсоедините разъем с 4-мм ключом Allen.

> [!tip] Момент затяжки
> 3 Н·м [27 фунт-дюйм]

![[rearofengine.jpg.png]]

Обновите обшивку корпуса CENSETM.

> [!tip] Момент затяжки
> 10 Н·м [89 фунт-дюйм]

После завершения перезапуска подключите разъем обратно в ECM CENSETM и протестируйте с помощью CENSETM INSITETM. Для этого необходимо перейти к функции монитора в реальном времени, выбрав все 16 датчиков EGT. Отсоедините выхлопные термопары от проводов за один раз, наблюдая за дисплеем монитора в реальном времени. Убедитесь, что правильное значение температуры цилиндра идет на «неудачу», поскольку его связанный датчик отключен. Если все работает правильно, перейдите на следующий датчик.

После того, как система CENSETM будет правильно функционировать, необходимо определить, что проводка CENSETM была изменена. Это должно быть сделано путем штамповки слова «RW» (переделано) буквенными штампами на правой стороне корпуса ECM CENSETM.

![[19600198.png]]

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.


> [!quote]- Original (English) · английский оригинал
> ## CENSE™ Phase 1.5 Harness Repair Instructions
>
> ### Core Issue
>
> It has recently been discovered that the all Phase 1.5 CENSE™ right-bank wiring harness, Part Number 4017464, on QSK60C engines have been produced incorrectly. The exhaust gas temperature connectors have been wired incorrectly for power cylinders 1, 2, 5, and 7, resulting in incorrect diagnosis of cylinder fault codes.
>
> ### Confirmation
>
> | Engine Serial Numbers Affected (QSK60 Only) |  |  |  |  |  |  |  |
> |---|---|---|---|---|---|---|---|
> | 33150763 | 33150602 | 33150387 | 33150015 | 33149343 | 33148906 | 33148449 | 33147903 |
> | 33150758 | 33150598 | 33150374 | 33149988 | 33149314 | 33148901 | 33148444 | 33147878 |
> | 33150755 | 33150596 | 33150363 | 33149973 | 33149277 | 33148897 | 33148401 | 33147584 |
> | 33150710 | 33150591 | 33150345 | 33149964 | 33149264 | 33148890 | 33148390 | 33147332 |
> | 33150706 | 33150587 | 33150341 | 33149951 | 33149258 | 33148781 | 33148385 | 33147260 |
> | 33150695 | 33150585 | 33150337 | 33149934 | 33149252 | 33148684 | 33148377 | 33147083 |
> | 33150687 | 33150580 | 33150331 | 33149903 | 33149247 | 33148620 | 33148355 | 33147075 |
> | 33150674 | 33150576 | 33150321 | 33149719 | 33149204 | 33148616 | 33148304 | 33146876 |
> | 33150668 | 33150573 | 33150313 | 33149702 | 33149201 | 33148608 | 33148280 | 33146847 |
> | 33150666 | 33150568 | 33150305 | 33149688 | 33149159 | 33148601 | 33148259 | 33146819 |
> | 33150657 | 33150563 | 33150291 | 33149640 | 33149077 | 33148591 | 33148244 | 33146809 |
> | 33150651 | 33150561 | 33150270 | 33149493 | 33149075 | 33148586 | 33148215 |  |
> | 33150649 | 33150557 | 33150262 | 33149471 | 33149029 | 33148539 | 33148196 |  |
> | 33150645 | 33150522 | 33150189 | 33149461 | 33148968 | 33148534 | 33148182 |  |
> | 33150635 | 33150518 | 33150181 | 33149421 | 33148962 | 33148528 | 33148170 |  |
> | 33150625 | 33150420 | 33150169 | 33149408 | 33148954 | 33148467 | 33148122 |  |
> | 33150619 | 33150407 | 33150147 | 33149359 | 33148948 | 33148463 | 33148077 |  |
> | 33150615 | 33150397 | 33150134 | 33149356 | 33148940 | 33148456 | 33148009 |  |
>
> **Note · Примечание**
> Subsequent engines from and including ESN 33146793 were rectified in the manufacturing plant and therefore require no modification.
>
> As a result, the temperature readings and fault codes obtained via the CENSE™ diagnostic software, INSITE™, do **not** correspond correctly to their associated power cylinders.
>
> For example, INSITE™ can indicate low or high exhaust gas temperature from cylinder number 1 when it is actually measuring the exhaust gas from cylinder number 7. As a consequence, this would mislead a technician into disassembling a healthy power cylinder when investigating the cause of the fault code.
>
> This is a confirmed issue with the Phase 1.5 CENSE™ harness; therefore, there is no requirement for any inspection or fault verification procedure.
>
> The cause of this issue is through a wiring harness design error.
>
> Mis-diagnosing power cylinder performance can lead an unhealthy power cylinder going undetected. This would obviously result in degradation in general engine performance and possible progressive component damage.
>
> ### Resolution
>
> Due to un-serviceability of the right bank CENSE™ harness (in which the fault lies), the repair instructions instruct modification to the wiring within the CENSE™ ECM housing. Altering the wiring at this location essentially “cancels out” the mis-wire on the right bank harness.
>
> Remove the six M6 capscrews.
>
> Remove the CENSE™ housing cover.
>
> Remove the module upper connector with a 4-mm allen key as shown.
>
> Using the Deutsch pin removal tool, Part Number 3824815, remove and reinsert the pins into their correct terminal. See table 1.
>
> Label each wire when disconnected with the new pin location.
>
> As each pin is reinserted, there will be a click as the terminal locks in the connector. Give the wire a gentle pull to ensure it is located.
>
> | Table 1 |  |
> |---|---|
> | Remove from Terminal | Reinsert into Terminal |
> | 31 | 01 |
> | 21 | 11 |
> | 01 | 14 |
> | 11 | 04 |
> | 14 | 22 |
> | 04 | 32 |
> | 22 | 31 |
> | 32 | 21 |
>
> Reconnect the connector with the 4-mm allen key.
>
> **Момент затяжки · Torque Value**
> 3 n•m [27 in-lb]
>
> Refit the CENSE™ housing cover.
>
> **Момент затяжки · Torque Value**
> 10 n•m [89 in-lb]
>
> After completing the rewire, plug the connector back into the CENSE™ ECM and test using CENSE™ INSITE™. Do this by going into the real time monitor feature, selecting all 16 EGT sensors. Disconnect the exhaust thermocouples from the wiring harness one at a time while observing the real time monitor display. Ensure that the correct cylinder temperature reading goes to “failed” as its associated sensor is disconnected. If everything is functioning correctly, move onto the next sensor.
>
> Once satisfied that the CENSE™ system is functioning correctly, there is a need to identify that the CENSE™ wiring has been modified. This **must** be done by stamping the word “RW” (rewired) with letter stamps on the right hand side of the CENSE™ ECM housing.
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
