---
aliases:
  - "Низкое выходное напряжение генератора"
type: "Процедура"
doc: "01-fc1447"
title_en: "Generator AC Output Voltage - Low"
title_ru: "Низкое выходное напряжение генератора"
modified: "2012-05-08"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1447.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1447.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Generator AC Output Voltage - Low
**Низкое выходное напряжение генератора**

> [!abstract] Процедура · `01-fc1447`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1447.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1447.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1447

### Низкое выходное напряжение генератора

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1447 PID(P): СПН: ФМИ: Лампа: Отключение SRT: | Выходное напряжение генератора переменного тока низкое. | Генератор будет отключен. |

![[19802905.png]]

Схема генератора

### Описание цепи

Генераторная установка вырабатывает электроэнергию. Эта мощность находится в форме трехфазного АС. Модуль управления двигателем (ECM) контролирует производительность и работу генераторной установки. Порог для состояния низкого выходного напряжения переменного тока заключается в том, что одно или несколько фазовых напряжений упали ниже 85 процентов номинального в течение по крайней мере 10 секунд.

ECM использует этот код неисправности, чтобы сообщить оператору, когда он устанавливает выходное напряжение переменного тока на низком уровне.

### Расположение компонента

См. документацию о клиенте/объекте/установке для диаграмм на генераторной установке/настройке электрической шины.

### Практические замечания

Если выходное напряжение низкое, то управление может **не** приводить в действие выходное напряжение достаточно высокое. Эта неисправность может быть вызвана неисправным регулятором напряжения, платой PT / CT, плохой PMG на полевых проводах или открытым или коротким замыканием в одной из проводных ремней.

Если напряжения на выходных проводах генератора значительно выше, чем напряжения, считываемые электронным сервисным оборудованием INSITETM, проблема может быть в цепях датчика напряжения.

Если регулятор напряжения получает B положительно (+). Но изолированный источник питания светодиод **не** освещен, проблема с регулятором напряжения.

Проверьте перегрузку.

См. Код устранения неполадок t05-1447.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1447
>
> ### Generator AC Output Voltage - Low
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1447 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Generator AC output voltage is low. | Generator set will shut down. |
>
> Generator Circuit
>
> ### Circuit Description
>
> The generator set produces electric power. This power is in the form of three-phase AC. The engine control module (ECM) monitors the performance and operation of the generator set. The threshold for a low AC output voltage condition is that one or more of the phase voltages has dropped below 85 percent of nominal for at least 10 seconds.
>
> The ECM uses this fault code to tell the operator when he generator set AC output voltage is low.
>
> ### Component Location
>
> Refer to customer/facility/installation documentation for diagrams on the generator set/electrical bus setup.
>
> ### Shoptalk
>
> If output voltage is low, the control can **not** drive the output voltage high enough. This fault can be caused by a failed voltage regulator, PT/CT board, bad PMG on field wirings, or an open or short circuit in one of the harnesses.
>
> If the voltages at the output leads of the alternator are significantly higher than the voltages read by INSITE™ electronic service tool, the problem can be in the voltage sensing circuits.
>
> If the voltage regulator is getting B positive (+). but the isolated supply LED is **not** lit, the problem is with the voltage regulator.
>
> Check for overload.
>
> Refer to Troubleshooting Fault Code t05-1447.
