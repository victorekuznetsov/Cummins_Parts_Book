---
aliases:
  - "Генераторная установка не синхронизируется по фазе"
type: "Процедура"
doc: "01-fc1458"
title_en: "Generator Set - Cannot Synchronize Phase"
title_ru: "Генераторная установка не синхронизируется по фазе"
modified: "2012-05-09"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1458.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1458.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Generator Set - Cannot Synchronize Phase
**Генераторная установка не синхронизируется по фазе**

> [!abstract] Процедура · `01-fc1458`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1458.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1458.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1458

### Генераторная установка не синхронизируется по фазе

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1458 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Последовательности фаз генератора и электрической шины различаются. | Генератор будет продолжать работать, но не будет поднимать нагрузку. |

![[19802905.png]]

Схема генератора

### Описание цепи

Генераторная установка подбирает электрическую нагрузку из шины. Для того чтобы генератор подключался к шине (кроме мертвой шины), он должен соответствовать по фазовым последовательностям, а также с порогом, напряжением и частотой шины. Генераторная установка может **не** подключаться к шине, в то время как напряжение и частота находятся за пределами порога, или последовательности фаз генераторной установки **не** соответствуют электрической шине; в противном случае, повреждение может произойти с генераторной установкой.

Этот код неисправности используется ECM для того, чтобы сообщить оператору, что генераторная установка не синхронизировалась с электрической шиной.

### Расположение компонента

См. раздел E для определения местоположения клетки карты ECM.

См. документацию о клиенте/объекте/установке для определения местоположения выключателя генераторной установки и интерфейса с электрической шиной.

### Практические замечания

Проверьте провода обратной связи шины на PT.

Проверить фазовое вращение генератора и шины.

См. Код устранения неполадок t05-1458


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1458
>
> ### Generator Set - Cannot Synchronize Phase
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1458 PID(P): SPN: FMI: Lamp: Warning SRT: | Generator and electric bus phase sequences differ. | Generator will continue to run, but will **not** pick up load. |
>
> Generator Circuit
>
> ### Circuit Description
>
> The generator set picks up the electrical load from the bus. For the generator to connect to a bus (other than a dead bus), it **must** match, in phase sequences as well as with a threshold, the voltage and frequency of the bus. The generator set can **not** connect to the bus while voltage and frequency are outside the threshold, or the phase sequences of the generator set do **not** match the electric bus; otherwise, damage can occur to the generator set.
>
> This fault code is used by the ECM to tell the operator that the generator set failed to synchronize to the electric bus.
>
> ### Component Location
>
> Refer to Section E for location of the ECM card cage.
>
> Refer to customer/facility/installation documentation for the location of the generator set circuit breaker and interface with the electric bus.
>
> ### Shoptalk
>
> Check the bus feedback wires to the bus PT.
>
> Verify phase rotation of generator and bus.
>
> Refer to Troubleshooting Fault Code t05-1458
