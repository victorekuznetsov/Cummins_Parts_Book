---
aliases:
  - "Базовый жгут стендовой калибровки ЭБУ"
type: "Инструкция по инструменту"
doc: "3377791"
title_en: "ECM Bench Calibration Base Harness"
title_ru: "Базовый жгут стендовой калибровки ЭБУ"
released: "2019-12-16"
modified: "2023-05-12"
revision: "26"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "33224404"
  - "33239746"
  - "33239899"
  - "35354607"
  - "35373113"
  - "37292556"
  - "37295879"
  - "41340468"
  - "41349633"
  - "41353297"
  - "71156161"
  - "77804810"
  - "80141463"
  - "80248213"
  - "82099327"
  - "85017333"
  - "93058669"
  - "93087701"
  - "93948840"
families:
  - "15N"
  - "C8.3 · 6C8.3"
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
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/sti/3377791.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/sti/3377791.pdf"
tags:
  - "документ/инструмент"
  - "двигатель/15N"
  - "двигатель/C8.3"
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
---

# ECM Bench Calibration Base Harness
**Базовый жгут стендовой калибровки ЭБУ**

> [!abstract] Инструкция по инструменту · `3377791`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[33224404 — QSK50 CM2150 MCRS CPL 3391|33224404]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41340468 — QSK50 CM2150 MCRS CPL 3728|41340468]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[77804810 — 15N CM2380 M104B CPL 5977|77804810]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]], [[82099327 — QSB6.7 CM2150 B109 CPL 4375|82099327]], [[85017333 — QSK23 CM500 CPL 2858|85017333]], [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]], [[93948840 — QSZ13 CM2150 Z102 CPL 4858|93948840]]
> **Семейство:** 15N, C8.3 · 6C8.3, K38/K50 · QSK38, QSK50, QSK60, QSB6.7, QSK19, QSK23, QSK50, QSK60, QSM11, QST30, QSX15, QSZ13
> **Даты:** выпущен 2019-12-16 · изменён 2023-05-12 · ревизия 26
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/sti/3377791.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/sti/3377791.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Наименование

Базовый жгут стендовой калибровки ЭБУ

### Назначение

В этом бюллетене по инструменту службы представлена информация для модуля управления двигателем (ECM) испытательного стенда калибровочной основы электропроводки, номер детали 3163151. Базовая электропроводка используется с соответствующим испытательным стендом калибровочного адаптера (см. Таблицу 3) для калибровки ECM без установки его на двигатель. Это позволяет откалибровать его перед отправкой в место, где электронные сервисные инструменты недоступны. Схемы калибровки испытательного стенда также могут использоваться для устранения неполадок ECM. Таблицы 1, 2 и 3 содержат элементы, используемые для процедуры калибровки стенда испытания ECM.

Некоторые из испытательных стендов калибровочных адаптерных проводов включают в себя возможность загрузки ECM ROM (см. Таблицу 3). Процедура загрузки ПЗУ используется, когда ECM **не** принимает калибровку или **не** связывается с инструментами электронного обслуживания после того, как были предприняты все другие электронные методы устранения неполадок. Процедура загрузки ROM сбрасывает программное обеспечение, постоянное в ECM, и похожа на перезагрузку персонального компьютера. Необходимо откалибровать ECM после процедуры загрузки ROM.

![[22d00433.png]]

| Таблица 1 ECM Испытательный стенд калибровочный Основы проводной упряжки |  |  |  |
|---|---|---|---|
| Номер позиции | Номер детали | Наименование | Количество |
| 1 | 3163151 | Базовый жгут стендовой калибровки ЭБУ | 1 |
| **Не** Показано | 4918881 | Ремонтный комплект Toggle Switch Repair Kit | 1 |

| Таблица 2, Элементы, используемые с помощью электропроводки для калибровки стендов ECM, приобретенные отдельно |  |  |  |
|---|---|---|---|
| Номер позиции | Номер детали | Наименование | Количество |
| 2 | 2892089 | Комплект, электропитание (23 Amp, 120 Volt, 60 Hz с входными и выходными кабелями) | 1 |
| 2 | 2892090 | Комплект, электропитание (23 Amp, 230 Volt, 50Hz с входными и выходными кабелями) | 1 |
| 3 |  | INSITETM электронный сервис оснащён персональным компьютером | 1 |
| 4 | 2892092 | Адаптерный комплект 6 от INLINETM | 1 |
| 4 | 3163682 | Адаптерный комплект InLINETM II | 1 |
| 4 | 4918416 | Адаптерный комплект V INLINETM | 1 |
| 4 | 5299899 | Адаптерный комплект 7 от INLINETM | 1 |
|  | 2892085 | Съемный входной кабель с BS 1363 plug (для использования в Великобритании, используйте **только** с комплектом, номер детали 2892090) | 1 |

> [!note] Примечание
> Ранее распределенный источник питания, номер детали 3164446, может **не** иметь возможность адекватно питать модули CM2150 и CM2250 во время калибровки. Индикатор источника питания **должен** непрерывно освещаться во время загрузки калибровки. Если индикаторная лампа гаснет или вспыхивает, подозревается неадекватное питание. Наборы питания, перечисленные в приведенной выше таблице, исправят эти проблемы и будут питать все кабели калибровки испытательных стендов, распределенные Cummins Inc.

| Таблица 3, Калибровочный адаптер проводов жгут, куплен отдельно |  |  |  |  |
|---|---|---|---|---|
| Номер позиции | Номер детали | ЭКМ | ROM Boot | Двигатель |
| 5 | 3162271 | CM420 | Нет | B5.9G B5.9LPG C8.3G L10G |
| 5 | 3164185 | CM850 | Да | ISB ISC ISL QSK19 MCRS QSK38 MCRS (см. таблицу 4) QSK50 MCRS (см. таблицу 4) QSK60 MCRS (см. таблицу 4) |
| 5 | 3164185 | CM870 | Да | Подпись TM и ISX ISM |
| 5 | 3164185 | CM871 | Да | ИСМ |
| 5 | 3164185 | CM875 | Да | ИСМ |
| 5 | 3164185 | CM876 | Да | ISX |
| 5 | 4918143 | CM556B | Да | B Gas Plus B LPG Plus BGI C Gas Plus L Gas Plus |
| 5 | 3164867 | CM554 | Да | ISC ISL |
| 5 | 3164868 | CM550 | Да | ISB QSB |
| 5 | 4918145 | ECM B | Нет | СЕЛЕКТМ |
| 5 | 3164869 | ECM C | Да | CELECT PlusTM |
| 5 | 3164789 | CM570 | Да | Подпись TM ISX ISM QSM11 |
| 5 | 3165030 | CM558 | Да | G5.9E GTA8.3SLB G8.3E G855E GTA855E QSK19G KTA19GC KTA19SLB KTA38GC QSK45G QSK60G QSV81G QSV91G |
| 5 | 3165031 | CM700 | Да | QSK19G QSK45G QSK60G QSV81G QSV91G |
| 5 | 3165062 | CM400 | Нет | Центр |
| 5 | 3165085 | CM552 | Да | QST30 (Промышленный) 480C-E (Морской) |
| 5 | 3164046 | CM800 | Нет | ISB e ISB четырехцилиндровый |
| 5 | 3163062 | CM551D | Нет | ISB Light-duty (ChryslerTM) |
| 5 | 4918142 | CM500 | Да | QSK19 QSK23 QSK45 QSK60 QSK78 |
| 5 | 4918583 | CM2150 | Да | ISB6.7 QSB3.3 ISC ISL QSK19 MCRS |
| 5 | 5572672 | CM2150 | Да | QSK38 MCRS QSK50 MCRS QSK60 MCRS |
| 5 | 4918802 | CM2180/CM2380 | Да | ISL G ISX12 G ISB5.9G ISB6.7G 15N X15N |
| 5 | 4918938 | CM2220 | Да | ISF2.8 ISF3.8 ISB3.9 |
| 5 | 4919009 | CM2250 | Да | ISX15 ISX11.9 ISB6.7 QSB6.7 ISC8.3 ISL9 QSL9 |
| 5 | 5298707 | CM2330 | Да | K38 K50 K2000 QSK45 QSK60 QSK78 QSK30 QSV81 QSV91 |
| 5 | 2892289 | CM2350/CM2450 | Да | ISB6.7 ISL9 ISX12 ISX15 |
| 5 | 5298994 | CM2350/CM2450 | Да | QSK50 QSK95 |
| 5 | 5298534 | CM2880 | Да | ISG11 ISG12 ISB/ISD6.7 ISB5.9 ISL8.9 QSB3.9 QSB5.9 QSB6.7 QSC8.3 QSF2.8 QSF3.8 QSL9.3.3 |
| 5 | 5299150 | CM3230 | Да | ISV5.0 |
| 5 | 5394436 | CM2358A | Да | QSK45G QSK60G QSV81G QSV91G |
| 5 | 5572846 | CM2620 | Да | F2.8 F3.8 F4.5 B4.0 D4.0 B4.5 D4.5 |
| 5 | 5572656 | CM2670 | Да | B6.2 B6.7 L9 X11 X12 X13 Z14 Z14 |

| Таблица 4, Калибровочный адаптер, проводящий упряжку, используемую на двигателях с несколькими ECM. Закуплено отдельно (пункты **не** показаны) (для использования с соответствующей калибровочной адаптерной проводкой упряжкой) |  |  |
|---|---|---|
| Номер детали | Наименование | Количество |
| 4919064 | испытательный стенд калибровочный комплект* | 1 |
| 4919022 | Многомодульный жгут проводов | 1 |
| \*(Набор калибровки испытательного стенда, Часть Номер 4919064, содержит один, Часть Номер 4919022, несколько модулей проводов, также приобретенные отдельно, и один, Часть Номер 4918894, несколько модулей коммутатора проводов ремня, **не** продаются отдельно). |  |  |

### Связанные процедуры

| 05-019-427 | Загрузка ПЗУ ЭБУ (ROM boot) |
|---|---|


> [!quote]- Original (English) · английский оригинал
> ### Description
>
> ECM Bench Calibration Base Harness
>
> ### Purpose
>
> This service tool bulletin provides information for the engine control module (ECM) bench calibration base harness, Part Number 3163151. The base harness is used with the appropriate bench calibration adapter harness (see Table 3) to calibrate an ECM without installing it on the engine. This makes it possible to calibrate it before shipping the ECM to a location where electronic service tools are **not** available. The bench calibration harnesses can also be used for troubleshooting the ECM. Tables 1, 2, and 3 contain items used for the ECM bench calibration procedure.
>
> Some of the bench calibration adapter harnesses include ECM ROM boot capability, (see Table 3). The ROM boot procedure is used when an ECM will **not** accept a calibration or will **not** communicate with the electronic service tool after all other electronic troubleshooting methods have been attempted. The ROM boot procedure resets the software resident in the ECM and is similar to rebooting a personal computer. It is necessary to calibrate the ECM after the ROM boot procedure.
>
> | Table 1, ECM Bench Calibration Base Harness |  |  |  |
> |---|---|---|---|
> | Item Number | Part Number | Description | Quantity |
> | 1 | 3163151 | ECM bench calibration base harness | 1 |
> | **Not** Shown | 4918881 | Base Harness Toggle Switch Repair Kit | 1 |
>
> | Table 2, Items used with ECM Bench Calibration Base Harness, Purchased Separately |  |  |  |
> |---|---|---|---|
> | Item Number | Part Number | Description | Quantity |
> | 2 | 2892089 | Kit, Electrical Power Supply (23 Amp, 120 Volt, 60 Hz with input and output cables) | 1 |
> | 2 | 2892090 | Kit, Electrical Power Supply (23 Amp, 230 Volt, 50Hz with input and output cables) | 1 |
> | 3 |  | INSITE™ electronic service tool-equipped personal computer | 1 |
> | 4 | 2892092 | INLINE™ 6 Adapter Kit | 1 |
> | 4 | 3163682 | INLINE™ II Adapter Kit | 1 |
> | 4 | 4918416 | INLINE™ V Adapter Kit | 1 |
> | 4 | 5299899 | INLINE™ 7 Adapter Kit | 1 |
> |  | 2892085 | Detachable input cable with BS 1363 plug (For use in the United Kingdom, use **only** with kit, Part Number 2892090) | 1 |
>
> **Note · Примечание**
> Previously distributed power supply, Part Number 3164446, may **not** be able to adequately power the CM2150 and CM2250 modules during calibration. The power supply indicator lamp **must** remain continuously illuminated during the calibration download. If the indicator lamp extinguishes or flashes, an inadequate power supply is suspected. The Power Supply Kits listed in the above table will correct these concerns and will power all bench calibration cables distributed by Cummins Inc.
>
> | Table 3, Calibration Adapter Harness, Purchased Separately |  |  |  |  |
> |---|---|---|---|---|
> | Item Number | Part Number | ECM | ROM Boot | Engine |
> | 5 | 3162271 | CM420 | No | B5.9G B5.9LPG C8.3G L10G |
> | 5 | 3164185 | CM850 | Yes | ISB ISC ISL QSK19 MCRS QSK38 MCRS (see table 4) QSK50 MCRS (see table 4) QSK60 MCRS (see table 4) |
> | 5 | 3164185 | CM870 | Yes | Signature™ and ISX ISM |
> | 5 | 3164185 | CM871 | Yes | ISM |
> | 5 | 3164185 | CM875 | Yes | ISM |
> | 5 | 3164185 | CM876 | Yes | ISX |
> | 5 | 4918143 | CM556B | Yes | B Gas Plus B LPG Plus BGI C Gas Plus L Gas Plus |
> | 5 | 3164867 | CM554 | Yes | ISC ISL |
> | 5 | 3164868 | CM550 | Yes | ISB QSB |
> | 5 | 4918145 | ECM B | No | CELECT™ |
> | 5 | 3164869 | ECM C | Yes | CELECT Plus™ |
> | 5 | 3164789 | CM570 | Yes | Signature™ ISX ISM QSM11 |
> | 5 | 3165030 | CM558 | Yes | G5.9E GTA8.3SLB G8.3E G855E GTA855E QSK19G KTA19GC KTA19SLB KTA38GC QSK45G QSK60G QSV81G QSV91G |
> | 5 | 3165031 | CM700 | Yes | QSK19G QSK45G QSK60G QSV81G QSV91G |
> | 5 | 3165062 | CM400 | No | CENTRY™ |
> | 5 | 3165085 | CM552 | Yes | QST30 (Industrial) 480C-E (Marine) |
> | 5 | 3164046 | CM800 | No | ISB e ISB four-cylinder |
> | 5 | 3163062 | CM551D | No | ISB light-duty (Chrysler™) |
> | 5 | 4918142 | CM500 | Yes | QSK19 QSK23 QSK45 QSK60 QSK78 |
> | 5 | 4918583 | CM2150 | Yes | ISB6.7 QSB3.3 ISC ISL QSK19 MCRS |
> | 5 | 5572672 | CM2150 | Yes | QSK38 MCRS QSK50 MCRS QSK60 MCRS |
> | 5 | 4918802 | CM2180/CM2380 | Yes | ISL G ISX12 G ISB5.9G ISB6.7G 15N X15N |
> | 5 | 4918938 | CM2220 | Yes | ISF2.8 ISF3.8 ISB3.9 |
> | 5 | 4919009 | CM2250 | Yes | ISX15 ISX11.9 ISB6.7 QSB6.7 ISC8.3 ISL9 QSL9 |
> | 5 | 5298707 | CM2330 | Yes | K38 K50 K2000 QSK45 QSK60 QSK78 QST30 QSV81 QSV91 |
> | 5 | 2892289 | CM2350/CM2450 | Yes | ISB6.7 ISL9 ISX12 ISX15 |
> | 5 | 5298994 | CM2350/CM2450 | Yes | QSK50 QSK95 |
> | 5 | 5298534 | CM2880 | Yes | ISG11 ISG12 ISB/ISD6.7 ISB5.9 ISL8.9 QSB3.9 QSB5.9 QSB6.7 QSC8.3 QSF2.8 QSF3.8 QSL9.3 |
> | 5 | 5299150 | CM3230 | Yes | ISV5.0 |
> | 5 | 5394436 | CM2358A | Yes | QSK45G QSK60G QSV81G QSV91G |
> | 5 | 5572846 | CM2620 | Yes | F2.8 F3.8 F4.5 B4.0 D4.0 B4.5 D4.5 |
> | 5 | 5572656 | CM2670 | Yes | B6.2 B6.7 L9 X11 X12 X13 Z14 |
>
> | Table 4, Calibration adapter harness used on engines with multiple ECMs. Purchased separately (items **not** shown) (To be used with appropriate calibration adapter harness) |  |  |
> |---|---|---|
> | Part Number | Description | Quantity |
> | 4919064 | Bench Calibration Kit\* | 1 |
> | 4919022 | Multiple module harness | 1 |
> | \*(Bench Calibration Kit, Part Number 4919064, contains one, Part Number 4919022, multiple module harness, also purchased separately, and one, Part Number 4918894, multiple module switch harness, **not** sold separately.) |  |  |
>
> ### Related Procedures
>
> | 05-019-427 | Engine Control Module ROM Boot |
> |---|---|
