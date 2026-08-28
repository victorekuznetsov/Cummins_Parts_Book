---
aliases:
  - "Цепь электронного регулятора воздушного компрессора"
type: "Процедура"
doc: "82-fc475"
title_en: "Electronic Air Compressor Governor Circuit"
title_ru: "Цепь электронного регулятора воздушного компрессора"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc475.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc475.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Electronic Air Compressor Governor Circuit
**Цепь электронного регулятора воздушного компрессора**

> [!abstract] Процедура · `82-fc475`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc475.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc475.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 475

### Цепь электронного регулятора воздушного компрессора

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 475 PID(P): S089 SPN: 1351 FMI: 4/4 лампы: Желтая СТО: | Низкое напряжение было обнаружено на электронной схеме воздушного компрессора, когда ожидалось высокое напряжение. | Воздушный компрессор **не будет **выключен. |

![[19c00329.png]]

Цепь электронного регулятора воздушного компрессора

### Описание цепи

Электронный компрессорный регулятор воздуха - это устройство, используемое электронным модулем управления (ECM) для управления выходом воздушного компрессора.

### Расположение компонента

Электронный воздухокомпрессорный регулятор расположен на верхней части воздушного компрессора.

### Практические замечания

- Осмотрите блок двигателя на проволоку шасси, чтобы убедиться, что он надежно закреплен на чистой, сухой, проводящей поверхности.

- Проверьте стартовый соленоидный положительный (+) терминал на наличие разъема или вспомогательной проводов с поврежденной изоляцией.

- Низкое напряжение может быть вызвано коротким замыканием на землю, коротким замыканием на другой провод в проводной упряжке или короткой соленоидной катушкой.

- Напряжение требуется на компрессорном регуляторе электронного воздуха, чтобы выключить компрессор. Никакое напряжение не включает компрессор.

Устранение неполадок код t05-475


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 475
>
> ### Electronic Air Compressor Governor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 475 PID(P): S089 SPN: 1351 FMI: 4/4 Lamp: Yellow SRT: | Low voltage was detected on the electronic air compressor circuit when high voltage was expected. | Air compressor will **not** shut off. |
>
> Electronic Air Compressor Governor Circuit
>
> ### Circuit Description
>
> The electronic air compressor governor is a device used by the electronic control module (ECM) to control output of the air compressor.
>
> ### Component Location
>
> The electronic air compressor governor is located on the top of the air compressor.
>
> ### Shoptalk
>
> - Inspect the engine block to chassis ground wire to make sure it is securely fastened to a clean, dry, conductive surface.
>
> - Check the starter solenoid positive (+) terminal for a loose connector or accessory wiring with damaged insulation.
>
> - Low voltage can be caused by short circuit to ground, a short circuit to another wire in the harness, or a shorted solenoid coil.
>
> - Voltage is required at the electronic air compressor governor to turn the compressor off. No voltage turns the compressor on.
>
> Refer to Troubleshooting Fault Code t05-475
