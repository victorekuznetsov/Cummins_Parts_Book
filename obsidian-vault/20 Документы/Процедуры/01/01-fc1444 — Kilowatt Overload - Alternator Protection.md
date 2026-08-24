---
aliases:
  - "Перегрузка по мощности — защита генератора"
type: "Процедура"
doc: "01-fc1444"
title_en: "Kilowatt Overload - Alternator Protection"
title_ru: "Перегрузка по мощности — защита генератора"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1444.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1444.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Kilowatt Overload - Alternator Protection
**Перегрузка по мощности — защита генератора**

> [!abstract] Процедура · `01-fc1444`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1444.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1444.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1444

### Перегрузка по мощности — защита генератора

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1444 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Киловатт достиг перегрузки. | Никаких действий со стороны ЕКМ не предпринимается. |

![[19802905.png]]

Схема генератора

### Описание цепи

Генераторная установка вырабатывает электроэнергию. Когда генератор подключен к шине, он может регулироваться регулировкой нагрузки киловатт или нагрузки кВАР. Модуль управления двигателем (ECM) контролирует выход трехфазного генератора. Порог перегрузки киловатта составляет 115 процентов номинальной мощности. ECM использует этот код неисправности, чтобы сообщить оператору, что нагрузка в киловатте слишком высока для двигателя и должна быть уменьшена.

### Расположение компонента

См. раздел E для определения местоположения генератора.

См. документацию о клиенте/объекте/установке для диаграмм на генераторной установке/настройке электрической шины.

### Практические замечания

Проверьте нагрузку и загрузку свинцовых соединений.

См. Код устранения неполадок t05-1444.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1444
>
> ### Kilowatt Overload - Alternator Protection
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1444 PID(P): SPN: FMI: Lamp: Warning SRT: | The kilowatt has reached overload. | No action is taken by the ECM. |
>
> Generator Circuit
>
> ### Circuit Description
>
> The generator set produces electric power. When the generator is connected to the bus, it can be governed by adjusting the kilowatt load or the kVAR load. The engine control module (ECM) monitors the three-phase generator output. The threshold for kilowatt overload is 115 percent of rated power output. The ECM uses this fault code to inform the operator that the kilowatt load is too high for the engine and needs to be reduced.
>
> ### Component Location
>
> Refer to Section E for location of the alternator.
>
> Refer to customer/facility/installation documentation for diagrams on the generator set/electric bus setup.
>
> ### Shoptalk
>
> Check the load and load lead connections.
>
> Refer to Troubleshooting Fault Code t05-1444.
