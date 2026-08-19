---
aliases:
  - "Идентификация шин данных SAE J1939"
type: "TSB"
doc: "tsb110086"
title_en: "Identification of SAE J1939 Datalinks"
title_ru: "Идентификация шин данных SAE J1939"
released: "2011-03-23"
modified: "2011-03-24"
group: "19 - Electronic Engine Controls"
engines:
  - "93058669"
families:
  - "C8.3 · 6C8.3"
figures: 3
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2011/tsb110086.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb110086.pdf"
tags:
  - "документ/tsb"
  - "двигатель/C8.3"
  - "год/2011"
  - "перевод/машинный"
  - "тема/electronic-engine-controls"
---

# Identification of SAE J1939 Datalinks
**Идентификация шин данных SAE J1939**

> [!abstract] TSB · `tsb110086`
> **Раздел Cummins:** 19 - Electronic Engine Controls
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3
> **Даты:** выпущен 2011-03-23 · изменён 2011-03-24
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2011/tsb110086.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb110086.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Идентификация шин данных SAE J1939

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### Содержание

Этот документ был первоначально выпущен в период с 1994 по 2001 год. Он был добавлен в QSOL для информационных целей.

В этом документе содержится информация для определения типа шины данных SAE J1939 CAN на двигателе.

Во всех следующих случаях стандартный кабель связи, часть 3162847, должен быть подключен к адаптеру INSITETM.

![[19802394.png]]

SAE J1939 является опцией OEM на двигателях ISM и ISX.

Если OEM-производители поставили шину данных SAE J1939 CAN, треугольный разъем Deutsch 3-pin будет найден в пределах 0,66 м[2,16 фута] двигателя ECM. Если эта шина данных CAN является сосудом (разъемом разъема), у ремня проводов ** не ** есть магистраль; между кабелем связи и шиной данных CAN необходим адаптер мини-кабеля (иллюстрированный), Номер детали 3163096, чтобы осуществлять связь.

![[19803444.png]]

Если шина данных CAN представляет собой вилку (разъем для подключения), то необходимо измерить сопротивление между контактами A и B **.

Если значение сопротивления составляет 60 Ом, то устанавливается магистраль и мини-кабель ** не требуется.

Если сопротивление через штифты больше 100k Ом, то магистраль ** не была установлена, и кабель, Part Number 3163597, необходим в дополнение к адаптеру мини-кабеля, Part Number 3163096.

> [!note] Примечание
> Отсоедините 50-контактную проводку OEM от двигателя ECM перед выполнением проверки сопротивления.

![[19802397.png]]

Если сопротивление между контактами A и B составляет 120 Ом, то одна из оконечных резисторов (1) отсутствует в проводных штепсельных заглушках (2) и *** должна быть заменена для правильной связи на шине данных CAN.

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## Identification of SAE J1939 Datalinks
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Contents
>
> This document was originally released between 1994 and 2001. It has been added to QSOL for informational purposes
>
> This document provides information for identifying what type of SAE J1939 datalink is on an engine.
>
> In all the following cases, standard communication cable, Part Number 3162847, will need to be connected to the INSITE™ adapter.
>
> SAE J1939 is an OEM option on ISM and ISX engines.
>
> If the OEM has supplied a SAE J1939 datalink, a triangular Deutsch 3–pin connector will be found within 0.66 m \[2.16 ft\] of the engine ECM. If this datalink is a receptacle (female connector), the harness does **not** have a backbone; A minibackbone adapter cable (illustrated), Part Number 3163096, is needed between the communication cable and the datalink in order to communicate.
>
> If the datalink is a plug (male connector), the resistance between pins A and B **must** to be measured.
>
> If the resistance value is 60 ohms, the backbone is installed and the minibackbone cable is **not** needed.
>
> If the resistance across the pins is greater than 100k ohms, a backbone has **not** been installed and cable, Part Number 3163597, is needed in addition to the minibackbone adapter cable, Part Number 3163096.
>
> **Note · Примечание**
> Disconnect the 50–pin OEM harness from the engine ECM before performing the resistance check.
>
> If the resistance across pins A and B is 120 ohms, one of the termination resistor caps (1) is missing in the OEM wiring harness plugs (2) and **must** be replaced for correct communication on the datalink.
>
> ### Document History
