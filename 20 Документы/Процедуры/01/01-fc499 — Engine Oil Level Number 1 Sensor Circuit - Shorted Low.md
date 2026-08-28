---
aliases:
  - "Цепь датчика уровня масла №1 — замыкание на массу"
type: "Процедура"
doc: "01-fc499"
title_en: "Engine Oil Level Number 1 Sensor Circuit - Shorted Low"
title_ru: "Цепь датчика уровня масла №1 — замыкание на массу"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc499.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc499.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Engine Oil Level Number 1 Sensor Circuit - Shorted Low
**Цепь датчика уровня масла №1 — замыкание на массу**

> [!abstract] Процедура · `01-fc499`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc499.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc499.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 499

### Цепь датчика уровня масла №1 — замыкание на массу

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 499 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Уровень масла двигателя No1 сигнал датчика - низкий. | Отсутствие защиты двигателя от уровня масла. Система Centinel отключена. |

![[19803584.png]]

Сенсорная схема уровня масла

### Описание цепи

Датчик уровня масла используется электронным модулем управления (ECM) для мониторинга уровня моторного масла. ECM контролирует напряжение на уровне масла и преобразует его в электронное значение. Значение уровня масла используется ECM для системы защиты двигателя.

### Расположение компонента

См. схемы двигателя. 100-002 для расположения компонентов.

### Практические замечания

Низкое напряжение может быть вызвано открытой цепью в сигнальном проводе, коротким к земле в сигнальном проводе, коротким к земле в питающем проводе, открытой цепью в питающем проводе или неисправным датчиком.

4-контактный датчик уровня масла **не** запускает код 499 ошибки.

Устранение неполадок код t05-499


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 499
>
> ### Engine Oil Level Number 1 Sensor Circuit - Shorted Low
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 499 PID(P): SPN: FMI: Lamp: Warning SRT: | Engine oil level Number 1 sensor signal - shorted low. | No engine protection for oil level. Centinel system is disabled. |
>
> Oil Level Sensor Circuit
>
> ### Circuit Description
>
> The oil level sensor is used by the electronic control module (ECM) to monitor the lubricating oil level. The ECM monitors the voltage on the oil level signal pin and converts this to an electronic value. The oil level value is used by the ECM for the engine protection system.
>
> ### Component Location
>
> Refer to the Engine Diagrams. 100-002 for the component location.
>
> ### Shoptalk
>
> Low voltage can be caused by an open circuit in the signal wire, a short to ground in the signal wire, a short to ground in the supply wire, an open circuit in the supply wire, or a faulty sensor.
>
> A 4-pin oil level sensor will **not** trigger Fault Code 499.
>
> Refer to Troubleshooting Fault Code t05-499
