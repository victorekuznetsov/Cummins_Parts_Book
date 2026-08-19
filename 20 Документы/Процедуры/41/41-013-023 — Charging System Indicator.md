---
aliases:
  - "Индикатор системы зарядки"
type: "Процедура"
doc: "41-013-023"
title_en: "Charging System Indicator"
title_ru: "Индикатор системы зарядки"
modified: "2004-12-07"
engines:
  - "93058669"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "3666003"
figures: 6
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/41/41-013-023.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/41-013-023.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/41"
  - "перевод/машинный"
---

# Charging System Indicator
**Индикатор системы зарядки**

> [!abstract] Процедура · `41-013-023`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[3666003 — C Troubleshooting and Repair Manual|3666003]]
> **Секции:** Section 13 - Electrical Equipment - Group 13
> **Даты:** изменён 2004-12-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/41/41-013-023.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/41-013-023.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Первичная проверка

Убедитесь, что на генераторе используются правильные терминалы. Терминал R (Delco®) или W-терминал (Bosch® K1) обеспечивает половину напряжения системы и используется для работы аксессуаров, таких как тахометр на генераторных установках.

![[es900ks.png]]

Проблемы с пусковой системой могут быть обозначены индикаторной лампой или амперметром.

![[es900kb.png]]

Проверьте лампу индикатора на предмет нормальной работы, как показано ниже:

| Двигатель | переключатель | лампа | амперметр |
|---|---|---|---|
| остановлен | вылет | вылет | 0 |
| остановлен | Включаю | Включаю | - |
| бегать | Включаю | вылет | + |

![[es900kc.png]]

Если лампа включена, когда выключатель выключен, а двигатель ** не** работает, отсоедините световой поток на выключателе зажигания.

- Если лампа остается включенной, то есть короткий положительный провод.
- Если лампа выходит, в выключателе есть короткое отверстие.

![[13900029.png]]

Если лампа выключается, когда выключатель включен, а двигатель не работает, в цепи может быть открыта.

Проверьте на продувной предохранитель, выгоревшую лампу, дефектную розетку лампы или открытую в No. 1 или D (+) ведущая схема между генератором и переключателем зажигания.

![[es900kf.png]]

Если лампа включена, когда выключатель включен и двигатель работает, отсоедините свинец к генератору переменного тока.

- Если лампа остается включенной, в цепи лампы есть короткий путь к земле.
- Если лампа выключается, проверьте генератор.

![[ea900wd.png]]


> [!quote]- Original (English) · английский оригинал
> ### Initial Check
>
> Be sure the correct terminals are being used on the alternator. The R terminal (Delco®) or W terminal (Bosch® K1) provide half of the system voltage and is used to operate accessories such as the tachometer on generator sets.
>
> Trouble with the starting system can be indicated by the indicator lamp or ampmeter.
>
> Check the indicator lamp for normal operation as shown below:
>
> | Engine | Switch | Lamp | Ampmeter |
> |---|---|---|---|
> | Stopped | OFF | OFF | 0 |
> | Stopped | ON | ON | - |
> | Running | ON | OFF | + |
>
> If the lamp is on when the switch is OFF and the engine is **not** running, disconnect the lamp lead at the ignition switch.
>
> - If the lamp stays on, there is a short to a positive wire.
> - If the lamp goes out, there is a short in the switch.
>
> If the lamp goes off when the switch is ON and the engine is **not** running, there can be an open in the circuit.
>
> Check for a blown fuse, a burned out bulb, defective bulb socket, or an open in the No. 1 or D (+) lead circuit between alternator and ignition switch.
>
> If the lamp is on when the switch is ON and the engine is running, disconnect the lead to the alternator.
>
> - If the lamp stays on, there is a short to the ground in the lamp circuit.
> - If the lamp goes out, inspect the alternator.
