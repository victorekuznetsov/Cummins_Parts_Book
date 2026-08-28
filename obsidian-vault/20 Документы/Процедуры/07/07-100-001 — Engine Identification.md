---
aliases:
  - "Идентификация двигателя"
type: "Процедура"
doc: "07-100-001"
title_en: "Engine Identification"
title_ru: "Идентификация двигателя"
modified: "2003-12-01"
engines:
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "4021442"
figures: 7
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-100-001.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-100-001.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
  - "перевод/машинный"
---

# Engine Identification
**Идентификация двигателя**

> [!abstract] Процедура · `07-100-001`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section E - Engine and System Identification
> **Даты:** изменён 2003-12-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-100-001.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-100-001.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Заводская табличка двигателя

Местонахождение Engine Dataplate

Используйте информацию из таблички с данными двигателя при обсуждении службы или источника деталей для двигателя.

![[00900309.png]]

Важная информация

Этот морской дизельный двигатель соответствует требованиям NOx Международной морской организации (ИМО), MARPOL 73/78, Приложение VI, Правило 3, если применимо.

![[00900310.png]]

Используйте информацию из таблички с данными двигателя при обсуждении службы или источника деталей для двигателя.

![[00900311.png]]

1. Смещение кубического дюйма/литр
2. Контрольные части Список номеров
3. Серийный номер двигателя
4. Идентификация семейства выбросов
5. Спецификация клиента - номер детали базового двигателя
6. Рейтинг лошадиных сил на rpm
7. Топливо, рассчитанное на лошадиные силы
8. Название модели
9. Система контроля выбросов (в настоящее время **не** используется на морском судне)
10. Распоряжение об обстреле
11. Вальве хлещет холодом
12. Время - Top Dead Center
13. Низкий холостый (rpm)
14. Дата изготовления
15. Предупреждение **Травма может быть получена, и гарантия недействительна, если норма топлива в об/мин или высоты превышают опубликованные максимальные значения для этой модели и приложения.**
16. Адрес Камминса: Cummins, Inc. Columbus, Indiana 47202-3005 Made in U.S.A.
17. Идентификация по сертификации двигателей (в настоящее время **не** используется на морском судне).

### Номенклатура двигателей Cummins

На следующем примере показано название модели двигателя для морских применений:

Пример: 6CTA8.3M2

6 = количество цилиндров

C = серия двигателей

T = турбированный

A = послеохлаждение

8.3 = смещение в литрах

M = морской

2 = фаза проектирования

### Таблица данных насоса для впрыска топлива

Таблица данных насоса впрыска топлива Bosch® расположена на стороне насоса впрыска. Он предоставляет информацию для калибровки топливного насоса.

![[fp901gl.png]]

Номер детали Cummins для комбинации топливного насоса-губернатора расположен на табличке губернатора.

![[fp901gm.png]]

### ECM Dataplate

Внешний регистрационный знак ECM расположен поверх ЭКМ.

![[19900348.png]]

В табличке с данными указаны номер детали ECM (P/N), серийный номер ECM (S/N), код даты изготовления (D/C), серийный номер двигателя (ESN) и код ECM.

![[19801041.png]]


> [!quote]- Original (English) · английский оригинал
> ### Engine Dataplate
>
> Location of Engine Dataplate
>
> Use the information from the engine dataplate when discussing service or the source of parts for the engine.
>
> Important Information
>
> This marine diesel engine conforms to the NOx requirements of the International Maritime Organization (IMO), MARPOL 73/78, Annex VI, Regulation 3 as applicable.
>
> Use the information from the engine dataplate when discussing service or the source of parts for the engine.
>
> 1. Cubic inch displacement/liters
> 2. Control parts list number
> 3. Engine serial number
> 4. Emission family identification
> 5. Customer specification - base engine part number
> 6. Rated horsepower at rpm
> 7. Fuel rated at horsepower
> 8. Model name
> 9. Emission control system (currently **not** used on marine)
> 10. Firing order
> 11. Valve lash cold
> 12. Timing - top dead center
> 13. Low idle (rpm)
> 14. Date of manufacture
> 15. Warning tag **WARNINGInjury may result and warranty is voided if fuel rate rpm or altitudes exceed published maximum values for this model and application.**
> 16. Cummins address: Cummins, Inc. Columbus, Indiana 47202-3005 Made in U.S.A.
> 17. Engine certification identification (currently **not** used on marine).
>
> ### Cummins Engine Nomenclature
>
> The following example shows a model name of an engine for marine applications:
>
> Example: 6CTA8.3M2
>
> 6 = number of cylinders
>
> C = engine series
>
> T = turbocharged
>
> A = aftercooled
>
> 8.3 = displacement in liters
>
> M = marine
>
> 2 = design phase
>
> ### Fuel Injection Pump Dataplate
>
> The Bosch® fuel injection pump dataplate is located on the side of the injection pump. It provides information for fuel pump calibration.
>
> The Cummins part number for the fuel pump-governor combination is located on the governor dataplate.
>
> ### ECM Dataplate
>
> The external ECM dataplate is located on top of the ECM.
>
> The dataplate contains the ECM part number (P/N), the ECM serial number (S/N), the manufacturing date code (D/C), the engine serial number (ESN), and the ECM code.
