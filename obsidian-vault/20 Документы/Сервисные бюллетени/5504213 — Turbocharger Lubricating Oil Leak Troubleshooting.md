---
aliases:
  - "Диагностика утечек масла турбокомпрессора"
type: "Сервисный бюллетень"
doc: "5504213"
title_en: "Turbocharger Lubricating Oil Leak Troubleshooting"
title_ru: "Диагностика утечек масла турбокомпрессора"
released: "2017-11-10"
modified: "2024-04-05"
group: "10 - Intake Air Systems"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "33224404"
  - "33239746"
  - "33239899"
  - "35354607"
  - "35373113"
  - "37269910"
  - "37280605"
  - "37292556"
  - "37295879"
  - "41340468"
  - "41349633"
  - "41353297"
  - "71156161"
  - "80141463"
  - "80248213"
  - "82099327"
  - "85017333"
  - "93058669"
  - "93087701"
  - "93948840"
families:
  - "C8.3 · 6C8.3"
  - "K19"
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSB6.7"
  - "QSK19"
  - "QSK23"
  - "QSK50"
  - "QSK60"
  - "QSM11"
  - "QST30"
  - "QSX15"
  - "QSZ13"
figures: 4
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/5504213.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/bulletin/5504213.pdf"
tags:
  - "документ/бюллетень"
  - "двигатель/C8.3"
  - "двигатель/K19"
  - "двигатель/K38/K50"
  - "двигатель/QSB6.7"
  - "двигатель/QSK19"
  - "двигатель/QSK23"
  - "двигатель/QSK50"
  - "двигатель/QSK60"
  - "двигатель/QSM11"
  - "двигатель/QST30"
  - "двигатель/QSX15"
  - "двигатель/QSZ13"
  - "перевод/машинный"
  - "тема/intake-air-systems"
---

# Turbocharger Lubricating Oil Leak Troubleshooting
**Диагностика утечек масла турбокомпрессора**

> [!abstract] Сервисный бюллетень · `5504213`
> **Раздел Cummins:** 10 - Intake Air Systems
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[33224404 — QSK50 CM2150 MCRS CPL 3391|33224404]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41340468 — QSK50 CM2150 MCRS CPL 3728|41340468]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]], [[82099327 — QSB6.7 CM2150 B109 CPL 4375|82099327]], [[85017333 — QSK23 CM500 CPL 2858|85017333]], [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]], [[93948840 — QSZ13 CM2150 Z102 CPL 4858|93948840]]
> **Семейство:** C8.3 · 6C8.3, K19, K38/K50 · QSK38, QSK50, QSK60, QSB6.7, QSK19, QSK23, QSK50, QSK60, QSM11, QST30, QSX15, QSZ13
> **Даты:** выпущен 2017-11-10 · изменён 2024-04-05
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/5504213.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/bulletin/5504213.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Диагностика утечек масла турбокомпрессора

**Проблема**

Утечки моторного масла на компрессорной или турбинной стороне турбокомпрессора чаще всего являются результатом неисправности компонента двигателя и/или системы и очень редко указывают на неисправность турбокомпрессора. Если утечки моторного масла наблюдаются без осевых или радиальных проблем, не заменяйте турбокомпрессор для проблем, связанных с утечкой масла. Этот документ объяснит симптомы, первопричину и разрешение утечек турбокомпрессора и предоставит техническое объяснение того, что вызывает утечку турбокомпрессора.

**Симптом**

- Утечка моторного масла с боковым компрессором турбокомпрессора (CSOL)
- Утечка турбонаддува сбоку моторного масла (TSOL)
- Окрашивание моторного масла или объединение в нижней части корпуса компрессора турбокомпрессора или моторного масла, обнаруженного в трубопроводах воздухозаборника ниже по течению от турбокомпрессора
- Видимые утечки из корпуса компрессора турбокомпрессора или подзарядки сантехники воздушного охладителя

**Корневая причина**

- Коренная причина проблемы может быть связана с:
- Если присутствует какое-либо из перечисленных выше условий, может произойти неправильный перепад давления по уплотнению (уплотнениям) турбокомпрессора, что может привести к очевидной утечке моторного масла в компрессор турбокомпрессора или корпус турбины. Функциональность уплотнения турбокомпрессора может быть восстановлена путем исправления любой идентифицированной первопричины.
- Неэффективная или ограниченная система вентиляции закрытого картерного шкафа может позволить смазочному маслу двигателя из моторного масла втягиваться в компрессорную оболочку турбокомпрессора, а затем проталкиваться через охладитель воздуха с зарядом.
- Неисправная или ограниченная система вентиляции закрытого картера включает, но не ограничивается:

**Решение**

- **не** заменить турбокомпрессор, если **только **симптомом является моторное масло, содержащееся в компрессоре турбокомпрессора или корпусе турбины или в трубопроводах для впуска/выхлопа. Утечки моторного масла из компрессорных (холодная сторона) или турбинных (горячая сторона) уплотнений **не** указывают на неисправность уплотнения турбокомпрессора.
- При устранении неполадок при утечке моторного масла уплотнителя турбокомпрессора **никогда** не пытайтесь повторить утечку моторного масла, работая с двигателем, когда трубы розетки компрессора турбокомпрессора отключены, поскольку это всегда приведет к утечке моторного масла уплотнения турбокомпрессора независимо от состояния или возраста турбокомпрессора.
- Справочная обновленная инструкция по эксплуатации турбокомпрессора и диагностика при возникновении ситуации CSOL или TSOL.
- Если турбокомпрессор радиальный и осевой осевой зазор все еще находится в спецификации, очистите и установите турбокомпрессор и зарядите воздухоохладитель входной трубы.
- После завершения ремонта и работы двигателя остаточное моторное масло может быть вытеснено из корпуса компрессора турбокомпрессора и производить полосы моторного масла в трубопроводах турбокомпрессора или на них. Это не является неисправностью.
- Если устранение неполадок завершено и первопричина отказа **не определена, обратитесь в компанию Cummins Care по телефону 1-800-CUMMINSTM для получения указания по устранению неполадок. Замените турбокомпрессор **только, если он будет направлен компанией Cummins CareTM.

**Техническое резюме**

Моторное масло, содержащееся в корпусе компрессора турбокомпрессора, корпусе турбины, трубопроводах для заряжания воздуха, охладителях воздуха для заряда и/или выхлопных трубах, связано с конструкцией уплотнения поршня, используемой в турбокомпрессоре. Cummins Inc. Масляные уплотнения турбокомпрессора представляют собой металлическое уплотнение поршневого кольца (см. Рисунок 1 ниже), которое предназначено для функционирования при положительном перепаде давления между давлением в корпусе турбины или компрессора (связанное с давлением выхлопа или повышения) и давлением в корпусе турбокомпрессора (связанное с давлением в картере). В течение определенных рабочих циклов, таких как холостый ход и ускорения, давление турбины турбокомпрессора или корпуса компрессора падает ниже давления корпуса подшипника, заставляя моторное масло проходить герметизацию турбокомпрессора и в турбину турбокомпрессора или корпус компрессора. См. рисунок 2 ниже.

![[10v00074.png]]

Рисунок 1, пример уплотнения компрессорного масла турбокомпрессора.

![[10r00215.png]]

Рисунок 2, диаграмма утечки турбокомпрессора.

1. Линия снабжения моторным маслом
2. Взять давление воздуха
3. Моторное масло и давление воздуха
4. Турбокомпрессор моторное масло сливная линия
5. Давление в чемоданчике

![[10r00335.png]]

Рисунок 3, Зарядка охладителя воздуха, утечка утечка масла.

Если в трубе охладителя воздуха с зарядом протекает масло, см. Рисунок 4 ниже, например, масло в впускном отверстии компрессора из-за переноса масла с закрытой вентиляцией картера.

![[10r00336.png]]

Рисунок 4, Впуск компрессора турбокомпрессора (приемлем с масляными месторождениями от CCV Oil Carryover).

Если есть доказательства масла в впускном отверстии компрессора турбокомпрессора, проверьте систему вентиляции закрытого картера. См. Service Bulletin, Closed Crankcase Ventilation System Engine Lubricating Oil Carryover and Associated Turbocharger Lubricating Oil Leak, Bulletin 5659915.

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## Turbocharger Lubricating Oil Leak Troubleshooting
>
> **Issue**
>
> Lubricating oil leaks on the compressor or turbine side of turbocharger are most often the result of an upstream engine component and/or system malfunction and very rarely indicate a turbocharger malfunction. If lubricating oil leaks without axial or radial play issues are observed, do **not** replace the turbocharger for oil leak related issues. This document will explain the symptoms, root cause, and resolution for turbocharger lubricating oil leaks and provide a technical explanation of what causes turbocharger lubricating oil leaks.
>
> **Symptom**
>
> - Turbocharger compressor side lubricating oil leak (CSOL)
> - Turbocharger turbine side lubricating oil leak (TSOL)
> - Lubricating oil staining or pooling in bottom of turbocharger compressor housing or lubricating oil found in air intake piping downstream from turbocharger
> - Apparent leaks from the turbocharger compressor housing or charge air cooler plumbing
>
> **Root Cause**
>
> - Root cause of problem can be related to:
> - If any of the conditions listed above are present, an incorrect pressure differential across the turbocharger seal(s) may occur resulting in apparent lubricating oil leakage into the turbocharger compressor or turbine housings. Turbocharger seal functionality can be restored by correcting any identified root cause.
> - An under-performing or restricted closed crankcase ventilation system can allow engine lubricating oil from the lubricating oil pan to be pulled into the compressor housing of the turbocharger then pushed through the charge air cooler.
> - An under-performing or restricted closed crankcase ventilation system includes but **not** limited to:
>
> **Resolution**
>
> - Do **not** replace turbocharger if **only** symptom is lubricating oil found in turbocharger compressor or turbine housing or in intake/exhaust piping. Lubricating oil leaks from compressor (cold side) or turbine (hot side) seals do **not** indicate a malfunction of turbocharger oil seal.
> - When troubleshooting suspected Turbocharger compressor seal lubricating oil leak, **never** attempt to replicate the lubricating oil leak by operating the engine with the turbocharger compressor outlet piping disconnected as this will always cause a turbocharger compressor seal lubricating oil leak regardless of turbocharger health or age.
> - Reference updated Turbocharger Service Manual Procedure and diagnostics when a CSOL or TSOL situation is encountered.
> - If turbocharger radial and axial end play is still in specification, clean and install turbocharger and charge air cooler inlet pipe.
> - After repair is complete and the engine is operated, residual lubricating oil could be pushed from the turbocharger compressor housing and produce lubricating oil streaks in or on the turbocharger piping. This does not constitute a malfunction.
> - If troubleshooting is completed and root cause of failure is **not** identified, contact Cummins Care at 1-800-CUMMINS™ for troubleshooting direction. Replace the turbocharger **only** if directed by Cummins Care™.
>
> **Technical Summary**
>
> Lubricating oil found in turbocharger compressor housing, turbine housing, charge air piping, charge air cooler, and/or exhaust piping is related to the piston seal design used in the turbocharger. Cummins Inc. turbocharger oil seals are a metal piston-ring seal (See Figure 1 below) that is designed to function under a positive pressure differential between turbine or compressor housing pressure (related to exhaust or boost pressure) and turbocharger bearing housing pressure (related to crankcase pressure). During certain duty cycles, such as idling and accelerations, the turbocharger turbine or compressor housing pressure drops below bearing housing pressure, forcing lubricating oil past turbocharger seal and into turbocharger turbine or compressor housing. See Figure 2 below.
>
> Figure 1, Example of Turbocharger Compressor Oil Seal.
>
> Figure 2, Turbocharger Oil Leak Diagram.
>
> 1. Turbocharger Lubricating Oil Supply Line
> 2. Intake Air Pressure
> 3. Lubricating Oil and Air Pressure
> 4. Turbocharger Lubricating Oil Drain Line
> 5. Crankcase Pressure
>
> Figure 3, Charge Air Cooler Plumbing Leaking Oil.
>
> If the charge air cooler plumbing is leaking oil, see Figure 4 below for example of oil in compressor inlet due to closed crankcase ventilation oil carryover.
>
> Figure 4, Turbocharger Compressor Inlet (Acceptable with Oil Deposits From CCV Oil Carryover).
>
> If there is evidence of oil in the turbocharger compressor inlet, check the closed crankcase ventilation system. See Service Bulletin, Closed Crankcase Ventilation System Engine Lubricating Oil Carryover and Associated Turbocharger Lubricating Oil Leak, Bulletin 5659915.
>
> ### Document History
