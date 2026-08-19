---
aliases:
  - "Короткое замыкание генератора — защита генератора"
type: "Процедура"
doc: "01-fc1445"
title_en: "Alternator Short Circuit - Alternator Protection"
title_ru: "Короткое замыкание генератора — защита генератора"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1445.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1445.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Alternator Short Circuit - Alternator Protection
**Короткое замыкание генератора — защита генератора**

> [!abstract] Процедура · `01-fc1445`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1445.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1445.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1445

### Короткое замыкание генератора — защита генератора

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1445 PID(P): СПН: ФМИ: Лампа: Отключение SRT: | Короткое замыкание альтернатора. | Генератор будет отключен. |

![[19802906.png]]

Альтернативный маршрут

### Описание цепи

Генератор превращает механическую энергию, вырабатываемую двигателем, в электрическую энергию. ECM контролирует работу и производительность генератора. Порог для состояния короткого замыкания составляет 175% от номинального.

ECM использует этот код неисправности, чтобы сообщить оператору, что в выходной цепи генераторного генератора существует условие короткого замыкания.

### Расположение компонента

См. раздел E для определения местоположения генератора. См. документацию о клиенте/объекте/установке для диаграмм на генераторной установке/настройке электрической шины.

### Практические замечания

Проверьте нагрузку и загрузку свинцовых соединений.

См. Код устранения неисправностей t05-1445


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1445
>
> ### Alternator Short Circuit - Alternator Protection
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1445 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Alternator short circuit. | Generator set will shut down. |
>
> Alternator Circuit
>
> ### Circuit Description
>
> The alternator turns the mechanical energy produced by the engine into electrical energy. The ECM monitors the performance and operation of the alternator. The threshold for short circuit condition is 175 percent of rated.
>
> The ECM uses this fault code to inform the operator that a short circuit condition exists in the generator set alternator output circuit.
>
> ### Component Location
>
> Refer to Section E for location of the alternator. Refer to customer/facility/installation documentation for diagrams on the generator set/electric bus setup.
>
> ### Shoptalk
>
> Check the load and load lead connections.
>
> Refer to Troubleshooting Fault Code t05-1445
