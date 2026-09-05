---
type: "Процедура"
doc: "19-fc499"
title_en: "Oil Level Sensor Circuit"
modified: "2011-03-01"
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
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc499.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc499.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Oil Level Sensor Circuit

> [!abstract] Процедура · `19-fc499`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc499.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc499.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 499

### Сенсорная схема уровня масла

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 499 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Уровень масла в двигателе \#1 сигнал датчика - низкий. | Отсутствие защиты двигателя от уровня масла. Система Centinel отключена. |

![[19803584.png]]

Сенсорная схема уровня масла

### Описание цепи

Датчик уровня масла используется электронным модулем управления (ECM) для мониторинга уровня моторного масла. ECM контролирует напряжение на уровне масла и преобразует его в электронное значение. Значение уровня масла используется ECM для системы защиты двигателя.

### Расположение компонента

См. диаграммы двигателя в разделе E этого руководства для определения местоположения компонента.

### Практические замечания

Низкое напряжение может быть вызвано открытой цепью в сигнальном проводе, коротким к земле в сигнальном проводе, коротким к земле в питающем проводе, открытой цепью в питающем проводе или неисправным датчиком.

4-контактный датчик уровня масла не будет запускать код 499.

Устранение неполадок код t05-499


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 499
>
> ### Oil Level Sensor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 499 PID(P): SPN: FMI: Lamp: Warning SRT: | Engine oil level \#1 sensor signal - shorted low. | No engine protection for oil level. Centinel system is disabled. |
>
> Oil Level Sensor Circuit
>
> ### Circuit Description
>
> The oil level sensor is used by the electronic control module (ECM) to monitor the lubricating oil level. The ECM monitors the voltage on the oil level signal pin and converts this to an electronic value. The oil level value is used by the ECM for the engine protection system.
>
> ### Component Location
>
> Refer to the Engine Diagrams in Section E of this manual for the component location.
>
> ### Shoptalk
>
> Low voltage can be caused by an open circuit in the signal wire, a short to ground in the signal wire, a short to ground in the supply wire, an open circuit in the supply wire, or a faulty sensor.
>
> A 4-pin oil level sensor will not trigger Fault Code 499.
>
> Refer to Troubleshooting Fault Code t05-499
