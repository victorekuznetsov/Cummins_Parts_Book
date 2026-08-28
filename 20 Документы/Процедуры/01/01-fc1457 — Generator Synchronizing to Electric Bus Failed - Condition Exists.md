---
aliases:
  - "Синхронизация генератора с сетью не удалась — условие возникло"
type: "Процедура"
doc: "01-fc1457"
title_en: "Generator Synchronizing to Electric Bus Failed - Condition Exists"
title_ru: "Синхронизация генератора с сетью не удалась — условие возникло"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1457.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1457.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Generator Synchronizing to Electric Bus Failed - Condition Exists
**Синхронизация генератора с сетью не удалась — условие возникло**

> [!abstract] Процедура · `01-fc1457`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1457.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1457.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1457

### Синхронизация генератора с сетью не удалась — условие возникло

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1457 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Генератор, синхронизирующийся с электрическим автобусом, не сработал. | Генератор будет продолжать работать, но не будет поднимать нагрузку. |

![[19802905.png]]

Схема генератора

### Описание цепи

Генераторная установка подбирает электрическую нагрузку из автобуса. Для того чтобы генератор подключался к шине (кроме мертвой шины), он должен соответствовать порогу, напряжению и частоте шины. Генераторная установка может **не** подключаться к шине, в то время как напряжение и частота находятся за пределами порога; в противном случае, повреждение может произойти с генераторной установкой.

Этот код неисправности используется модулем управления двигателем (ECM) для того, чтобы сообщить оператору, что генераторная установка не синхронизировалась с электрической шиной.

### Расположение компонента

Справочный раздел E для определения местоположения клетки карты ECM.

Справочная клиентская/факультативно-установочная документация для определения местоположения генераторного набора выключателя и интерфейса с электрической шиной.

### Практические замечания

Проверьте губернатора на правильность настройки.

Проверьте параметры синхронизации для правильной настройки.

Проверьте топливную систему на наличие проблем, которые могут вызвать нестабильность.

См. Код устранения неполадок t05-1457.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1457
>
> ### Generator Synchronizing to Electric Bus Failed - Condition Exists
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1457 PID(P): SPN: FMI: Lamp: Warning SRT: | Generator synchronizing to electric bus failed. | Generator will continue to run, but will **not** pick up load. |
>
> Generator Circuit
>
> ### Circuit Description
>
> The generator set picks up the electrical load from the bus. For the generator to connect to a bus (other than a dead bus), it **must** match, with a threshold, the voltage and frequency of the bus. The generator set can **not** connect to the bus while voltage and frequency are outside the threshold; otherwise, damage could occur to the generator set.
>
> This fault code is used by the engine control module (ECM) to tell the operator that the generator set failed to synchronize to the electrical bus.
>
> ### Component Location
>
> Reference Section E for location of the ECM card cage.
>
> Reference customer/facility/installation documentation for the location of the generator set circuit breaker and interface with the electrical bus.
>
> ### Shoptalk
>
> Check the governor for correct setup.
>
> Check the synchronizing parameters for correct setup.
>
> Check the fuel system for problems that can cause instability.
>
> Refer to Troubleshooting Fault Code t05-1457.
