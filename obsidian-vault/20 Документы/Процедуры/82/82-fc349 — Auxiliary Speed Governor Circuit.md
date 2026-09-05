---
aliases:
  - "Цепь вспомогательного регулятора частоты вращения"
type: "Процедура"
doc: "82-fc349"
title_en: "Auxiliary Speed Governor Circuit"
title_ru: "Цепь вспомогательного регулятора частоты вращения"
modified: "2010-09-02"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc349.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc349.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Auxiliary Speed Governor Circuit
**Цепь вспомогательного регулятора частоты вращения**

> [!abstract] Процедура · `82-fc349`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc349.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc349.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 349

### Цепь вспомогательного регулятора частоты вращения

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 349 PID(P): P191 SPN: ФМИ: 0/16 лампа: Желтая СТО: | Частота, превышающая калиброванный порог, была обнаружена при контакте сигнала управляющего хвостовым валом 31-контактного разъема. | Калибровочная зависимость мощности и скорости снижается. |

![[19c00563.png]]

Цепь вспомогательного регулятора частоты вращения

### Описание цепи

Вспомогательный регулятор скорости обеспечивает средство управления двигателем независимо от скорости двигателя. Эта схема управляет выходными валами или другими устройствами ниже по потоку от преобразователя крутящего момента.

Вспомогательный регулятор скорости обеспечивает средство для управления выходными валами или другими устройствами ниже по течению от преобразователя крутящего момента, независимо от скорости двигателя.

### Расположение компонента

Вспомогательная скорость губернатора местоположения варьируется с OEM. См. руководство изготовителя машины по диагностике и ремонту.

### Практические замечания

Эта неисправность может быть вызвана только высокочастотным входом во вспомогательную схему регулятора скорости.

См. Код устранения неполадок t05-349


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 349
>
> ### Auxiliary Speed Governor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 349 PID(P): P191 SPN: FMI: 0/16 Lamp: Yellow SRT: | A frequency greater than calibrated threshold was detected at the tailshaft governor signal pin of the 31-pin connector. | Calibration-dependent power and speed derate. |
>
> Auxiliary Speed Governor Circuit
>
> ### Circuit Description
>
> The auxiliary speed governor provides a means to govern the engine independent of engine speed. This circuit controls output shafts or other devices downstream of a torque converter.
>
> The auxiliary speed governor provides a means to control the output shafts or other devices downstream of a torque converter, independent of engine speed.
>
> ### Component Location
>
> The auxiliary speed governor location varies with the OEM. Refer to the OEM troubleshooting and repair manual.
>
> ### Shoptalk
>
> This fault can **only** be caused by a high-frequency input into the auxiliary speed governor circuit.
>
> Refer to Troubleshooting Fault Code t05-349
