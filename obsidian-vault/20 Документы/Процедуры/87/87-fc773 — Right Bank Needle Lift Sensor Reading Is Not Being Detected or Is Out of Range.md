---
aliases:
  - "Показания датчика подъёма иглы правого ряда отсутствуют или вне диапазона"
type: "Процедура"
doc: "87-fc773"
title_en: "Right Bank Needle Lift Sensor Reading Is Not Being Detected or Is Out of Range."
title_ru: "Показания датчика подъёма иглы правого ряда отсутствуют или вне диапазона"
modified: "2012-04-30"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc773.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc773.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Right Bank Needle Lift Sensor Reading Is Not Being Detected or Is Out of Range.
**Показания датчика подъёма иглы правого ряда отсутствуют или вне диапазона**

> [!abstract] Процедура · `87-fc773`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-04-30
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc773.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc773.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 773

### Показания датчика подъёма иглы правого ряда отсутствуют или вне диапазона

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 773 PID(P): S118 SPN: ФМИ: 11 лампочка: Нет, не srt: | Считывание датчика подтяжки правой иглы в банке ** Не обнаруживается или находится вне зоны действия. | Модуль управления двигателем не выполняет никаких действий. Выходная мощность может быть низкой, а двигатель может производить белый дым. |

![[19a00820.png]]

Сенсор для подъема иглы Right Bank

### Описание цепи

Датчик подъема иглы используется для определения начала инъекции. Модуль управления двигателем (ECM) контролирует импульсы от датчика, чтобы определить, когда происходит впрыск в цикле. ECM контролирует импульсы при контакте 11.

### Расположение компонента

Датчик подъема иглы является неотъемлемой частью форсунки NBF (номер 1 левый берег и номер 1 правый форсун).

### Практические замечания

Общей причиной поврежденного датчика подъема иглы является слабое соединение.

Код неисправности будет **не** активироваться при скорости двигателя менее 800 об/мин.

Если двигатель показывает либо код 772, либо 773 (но не оба), то обменяйте иглы подъёмного топливного форсунка с левого берега № 1 на правый берег № 1 и посмотрите, следует ли код неисправности за поврежденным топливным форсуном.

В калибровочных доработках старше июля 2011 года будет отображаться янтарная предупредительная лампа.

См. Код устранения неполадок t05-773.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 773
>
> ### Right Bank Needle Lift Sensor Reading Is Not Being Detected or Is Out of Range.
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 773 PID(P): S118 SPN: FMI: 11 Lamp: None SRT: | Right Bank Needle Lift Sensor Reading Is **Not** Being Detected or Is Out of Range. | No action is taken by the engine control module. Power output can be low and engine can produce white smoke. |
>
> Right Bank Needle Lift Sensor
>
> ### Circuit Description
>
> The needle lift sensor is used to sense the start of injection. The engine control module (ECM) monitors the pulses from the sensor to determine when injection occurs in the cycle. The ECM monitors the pulses on pin 11.
>
> ### Component Location
>
> The needle lift sensor is an integral part of the NBF injectors (number 1 left bank and number 1 right bank injector).
>
> ### Shoptalk
>
> A common cause of a damaged needle lift sensor is a loose connection.
>
> The fault code will **not** become active at engine speeds less than 800 rpm.
>
> If the engine is showing either Fault Code 772 or 773 (but **not** both), then exchange the needle lift injectors from left bank Number 1 with right bank number 1 and see if the fault code follows the damaged injector.
>
> Calibration revisions older than July 2011 will display an amber warning lamp.
>
> Refer to Troubleshooting Fault Code t05-773.
