---
aliases:
  - "ТНВД P7100 и P8500 с опережением при малой нагрузке"
type: "TSB"
doc: "tsb100121"
title_en: "P7100 and P8500 Light-Load Advance Injection Pumps"
title_ru: "ТНВД P7100 и P8500 с опережением при малой нагрузке"
released: "2006-10-30"
modified: "2006-10-30"
group: "05 - Fuel Systems (Pumps)"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2010/tsb100121.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb100121.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QST30"
  - "год/2006"
  - "перевод/машинный"
  - "тема/fuel-systems-pumps"
---

# P7100 and P8500 Light-Load Advance Injection Pumps
**ТНВД P7100 и P8500 с опережением при малой нагрузке**

> [!abstract] TSB · `tsb100121`
> **Раздел Cummins:** 05 - Fuel Systems (Pumps)
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Даты:** выпущен 2006-10-30 · изменён 2006-10-30
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2010/tsb100121.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb100121.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## ТНВД P7100 и P8500 с опережением при малой нагрузке

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### Содержание

В настоящем Бюллетене по технической службе определено использование насосов для впрыска легких нагрузок P7100 и P8500 на QST30 на основе рейтинга.

Насосы для впрыска топлива P7100 теперь используются на G1 и G2 QST30. Накопитель правого берега - часть 3093280, насос левого берега - часть 3093281. Код времени для G1 и G2 с насосами P7100 - KT. Время должно быть установлено на 23,5 градуса перед верхним мертвым центром с поршнем правого берега № 1 на ударе сжатия. Оба насоса для впрыска установлены в одном и том же положении коленчатого вала. Двигатели с насосами P7100 требуют иной ECM, чем насосы P8500, ранее использовавшиеся на G1 и G2, но другие компоненты топливной системы (поддержки насосов, топливные линии высокого или низкого давления, топливный форсунок) остаются прежними. Насосы P7100 устанавливаются на все модели G1 и G2, построенные после 15 июля 2000 года.

Двигатели QST30 с рейтингом G3, G4 и G5 теперь используют насосы P8500 с увеличенной нагрузкой. Этот насос использует уникальный разрез спирали для увеличения времени впрыска во время условий работы с легкой нагрузкой для уменьшения белого дыма. Накопитель правого берега - часть 3093278, а насос левого берега - часть 3093279. Единственный способ определить разницу между P8500 и P8500 передовыми насосами легкой нагрузки - это прочитать номер детали на табличке с данными насоса. Номер детали — первые семь цифр четвертой строки на табличке. Двигатели с передовыми насосами с легкой нагрузкой P8500 требуют иной ECM, чем ранее используемые насосы P8500, но другие компоненты топливной системы остаются прежними. Насосы P8500 с заблаговременной загрузкой устанавливаются на все G3, G4 и G5, построенные после 15 июля 2000 года.

** Новые контрольные части **

| Таблица 1, Новые списки контрольных частей для изменения конфигурации |  |
|---|---|
| Насосы для инъекций | Новые контрольные части Список номеров |
| P7100 | 2839, 2949, 2968 |
| P8500 Lightload Avanced | 2499, 2548, 2840, 2879, 2880 |


> [!quote]- Original (English) · английский оригинал
> ## P7100 and P8500 Light-Load Advance Injection Pumps
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Contents
>
> This Technical Service Bulletin defines the use of the P7100 and P8500 light-load advance injection pumps on the QST30 based on rating.
>
> The P7100 fuel injection pumps are now used on G1 and G2 QST30 ratings. The right-bank pump is Part Number 3093280; the left-bank pump is Part Number 3093281. The timing code for G1 and G2 with P7100 pumps is KT. Timing should be set at 23.5 degrees before top dead center with the number 1 right-bank piston on the compression stroke. Both injection pumps are installed at the same crankshaft position. Engines with P7100 pumps require a different ECM than the P8500 pumps previously used on G1 and G2 ratings, but other fuel system components (pump supports, high- or low-pressure fuel lines, injectors) remain the same. The P7100 injection pumps are installed on every G1 and G2 rating built after July 15, 2000.
>
> QST30 engines rated G3, G4, and G5 now use P8500 light-load advance injection pumps. This pump uses a unique helix cut to advance injection timing during light-load operating conditions to reduce white smoke. The right-bank pump is Part Number 3093278 and the left-bank pump is Part Number 3093279. The **only** way to determine the difference between the P8500 and the P8500 light-load advance pumps is to read the part number on the pump dataplate. The part number is the first seven digits of the fourth line on the dataplate. Engines with P8500 light-load advance pumps require a different ECM than the P8500 pumps previously used, but other fuel system components remain the same. The P8500 light-load advance injection pumps are installed on every G3, G4, and G5 rating built after July 15, 2000.
>
> **New Control Parts Lists**
>
> | Table 1, New Control Parts Lists for Configuration Change |  |
> |---|---|
> | Injection Pumps | New Control Parts List Numbers |
> | P7100 | 2839, 2949, 2968 |
> | P8500 light-load advance | 2499, 2548, 2840, 2879, 2880 |
