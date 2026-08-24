---
aliases:
  - "Загрузка ПЗУ ЭБУ (ROM boot)"
type: "Процедура"
doc: "122-019-427"
title_en: "Engine Control Module ROM Boot"
title_ru: "Загрузка ПЗУ ЭБУ (ROM boot)"
modified: "2019-12-11"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-019-427.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-019-427.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
  - "перевод/машинный"
---

# Engine Control Module ROM Boot
**Загрузка ПЗУ ЭБУ (ROM boot)**

> [!abstract] Процедура · `122-019-427`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section 19 - Electronic Controls
> **Даты:** изменён 2019-12-11
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-019-427.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-019-427.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

> [!note] Примечание
> При выполнении процедуры загрузки ПЗУ на двигателях с несколькими электронными модулями управления необходимо использовать комплект проводов Multiple Module. Для получения дополнительной информации см. раздел Установка многомодулей электропроводки ниже или инструментальная часть обслуживания, Номер детали 3163151.

Каждый переключатель передает питание правильной паре контактов модуля управления двигателем (ECM), поэтому инструмент электронного обслуживания INSITETM может считывать местоположения переключателей.

Установите Multiple Module Wiring Wight Kit на соответствующий калибровочный кабель с ROM-переключателем загрузки. Подключите калибровочный кабель с помощью переключателя ROM для загрузки к ECM, который желательно загрузить ROM. Выберите ECM для загрузки ROM, используйте 3-позиционный переключатель в коробке с несколькими модулями.

- При переходе в режим «PRIM» читается первичная ECM, а также любая единая ECM.
- При переходе в режим «SEC1» читается первая вторичная ECM.
- При переходе в режим «SEC2» будет обеспечена возможность показаний второго вторичного ECM.

Испытательный стенд калибровочной проводов работает с соответствующим загрузочным кабелем ROM, чтобы обеспечить загрузку ROM и калибровку двигателей с несколькими ECM.

Установите калибровочный кабель с помощью ROM-переключателя загрузки.

С помощью переключателя (2) зажигания в положении OFF нажмите загрузочный переключатель (1) ROM, расположенный на электропроводке специального калибровочного адаптера ECM, и удерживайте.

Переключите переключатель зажигания в положение Включения, удерживая выключатель загрузки ПЗУ; подождите 5 секунд.

Выпустите загрузочный коммутатор ROM.

Калибровка ECM.[[105-019-032 — Engine Control Module Calibration Code|См. процедуру 019-032 в разделе 19.]]

Удалить загрузочный кабель ROM из ECM.

![[22d00162.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> **Note · Примечание**
> When performing the ROM boot procedure on engines with multiple electronic control modules, a Multiple Module Harness Kit must be used. For additional information, see the Installation of Multiple Module Harness section below or service tool, Part Number 3163151.
>
> Each switch sends power to the correct pair of engine control module (ECM) contacts, so INSITE™ electronic service tool can read the switch locations.
>
> Install the Multiple Module Harness Kit on the appropriate calibration cable with ROM boot switch. Connect the calibration cable with ROM boot switch to the ECM desired to be ROM booted. Select ECM to ROM boot, use the 3 position switch on the multiple module box.
>
> - When switched to “PRIM” mode, the primary ECM is read, as well as any single ECM.
> - When switched to “SEC1” mode, the first secondary ECM is read.
> - When switched to “SEC2” mode, will enable the second secondary ECM is read.
>
> The bench calibration harness works with the appropriate ROM boot cable to enable ROM booting and the calibration of engines with multiple ECMs.
>
> Install the calibration cable with ROM boot switch.
>
> With the keyswitch (2) in the OFF position, press the ROM boot switch (1), located on the ECM specific calibration adapter harness, and hold.
>
> Switch the keyswitch to the ON position while holding the ROM boot switch down; wait for 5 seconds.
>
> Release the ROM boot switch.
>
> Calibrate the ECM. [[105-019-032 — Engine Control Module Calibration Code|Refer to Procedure 019-032 in Section 19.]]
>
> Remove the ROM boot cable from the ECM.
