---
aliases:
  - "Цепь привода перепускного клапана турбины №2"
type: "Процедура"
doc: "82-fc492"
title_en: "Wastegate Actuator Number 2 Circuit"
title_ru: "Цепь привода перепускного клапана турбины №2"
modified: "2010-09-02"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc492.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc492.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Wastegate Actuator Number 2 Circuit
**Цепь привода перепускного клапана турбины №2**

> [!abstract] Процедура · `82-fc492`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc492.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc492.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 492

### Цепь привода перепускного клапана турбины №2

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 492 PID(P): S088 SPN: 1189 FMI: 4/4 лампы: Желтая СТО: | Менее + 6 VDC, обнаруженных на цепи 2 обходного клапана турбины, когда активирован, указывает на избыточный ток, вытягиваемый из электронного модуля управления (ECM) или неисправной выходной цепи ECM. | Двигатель будет работать с поломкой. |

![[19c00620.png]]

Цепь привода перепускного клапана турбины №2

### Описание цепи

Вентиляционные приводы турбинного обхода - это устройства, используемые ECM для управления давлением наддува.

### Расположение компонента

Контроллер обходного клапана турбины расположен на впускном роге воздуха. Привод № 2 является самым задним соленоидом на контроллере.

### Практические замечания

- Проверьте блок двигателя на проволоке шасси, чтобы убедиться, что он надежно закреплен на чистой, сухой поверхности.

- Проверьте стартер соленоид + терминал для разъема или вспомогательной проводов с поврежденной изоляцией.

- Низкое напряжение может быть вызвано коротким замыканием на землю, коротким замыканием на другой провод в проводной упряжке или короткой соленоидной катушкой.

- Осмотрите схему 2 обходного клапана турбины для внешних проводов, которые могут быть сплайсированы для питания другого устройства. Удалите любые дополнительные провода, которые находятся в цепи.

См. Код устранения неполадок t05-492


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 492
>
> ### Wastegate Actuator Number 2 Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 492 PID(P): S088 SPN: 1189 FMI: 4/4 Lamp: Yellow SRT: | Less than + 6 VDC detected at the wastegate actuator number 2 circuit when activated indicates an excessive current draw from the electronic control module (ECM) or faulty ECM output circuit. | Engine will run derated. |
>
> Wastegate Actuator Number 2 Circuit
>
> ### Circuit Description
>
> The wastegate actuators are devices used by the ECM to control boost pressure.
>
> ### Component Location
>
> The wastegate controller is located on the air inlet horn. Actuator number 2 is the rear-most solenoid on the controller.
>
> ### Shoptalk
>
> - Inspect the engine block to chassis ground wire to make sure it is securely fastened to a clean, dry surface.
>
> - Check the starter solenoid + terminal for a loose connector or accessory wiring with damaged insulation.
>
> - Low voltage can be caused by short circuit to ground, a short circuit to another wire in the harness, or a shorted solenoid coil.
>
> - Inspect the wastegate actuator number 2 circuit for external wires that can be spliced into powering another device. Remove any extra wires that are found in the circuit.
>
> Refer to Troubleshooting Fault Code t05-492
