---
aliases:
  - "Разрешение на подключение не получено"
type: "Процедура"
doc: "01-fc1475"
title_en: "Permission to connect - not received"
title_ru: "Разрешение на подключение не получено"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1475.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1475.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Permission to connect - not received
**Разрешение на подключение не получено**

> [!abstract] Процедура · `01-fc1475`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1475.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1475.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1475

### Разрешение на подключение не получено

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1475 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Разрешение на подключение к закрытому автобусу в требуемое время получено не было. | Генераторный набор подключится к мертвому автобусу. |

![[19802910.png]]

Параллельный контроллер Circuit

### Описание цепи

Этот код неисправности используется ECM для того, чтобы сообщить оператору, что ECM не получил команду от параллельного контроллера для подключения к шине. ECM контролирует автобус в течение определенного количества времени, и если ECM все еще видит мертвый автобус после этого установленного количества времени, то он подключится к автобусу.

Контроллер параллелизма подключен к ECM и может давать ему команды для сбора нагрузки, сброса нагрузки или управляющих команд нагрузки.

### Расположение компонента

См. раздел E для определения местоположения клетки карты ECM.См. документацию о клиенте/объекте/установке для определения местоположения параллельного контроллера.

### Практические замечания

Возможные режимы отказа - короткое замыкание, открытое замыкание, короткое к земле и неисправное устройство ввода. Проверьте датчик первого запуска мастера на наличие сбоев.

См. Код устранения неисправностей t05-1475


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1475
>
> ### Permission to connect - not received
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1475 PID(P): SPN: FMI: Lamp: Warning SRT: | Permission to connect to a closed bus has **not** been received in the required time. | Generator set will connect to the dead bus. |
>
> Paralleling Controller Circuit
>
> ### Circuit Description
>
> This fault code is used by the ECM to tell the operator that the ECM did **not** receive a command from the paralleling controller to connect to the bus. The ECM monitors the bus for a set amount of time and if the ECM still sees a dead bus after that set amount of time, then it will connect to the bus.
>
> The paralleling controller is wired into the ECM and can give it commands to pick up load, dump load, or load governing commands.
>
> ### Component Location
>
> Refer to section E for location of the ECM card cage.Refer to customer/facility/installation documentation for the location of the paralleling controller.
>
> ### Shoptalk
>
> The possible failure modes are short circuit, open circuit, short to ground, and failed input device. Check the master first start sensor for failures.
>
> Refer to Troubleshooting Fault Code t05-1475
