---
aliases:
  - "Неисправность отключения питания контроллера"
type: "Процедура"
doc: "01-fc1417"
title_en: "Controller Power Down Fault"
title_ru: "Неисправность отключения питания контроллера"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1417.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1417.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Controller Power Down Fault
**Неисправность отключения питания контроллера**

> [!abstract] Процедура · `01-fc1417`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1417.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1417.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1417

### Неисправность отключения питания контроллера

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1417 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Была обнаружена ошибка отключения питания контроллера. | ECM может **не** отключаться из-за какого-то неизвестного состояния. Возможен дренаж батареи. |

![[19802494.png]]

СХУ ECM

### Описание цепи

ECM проверяет во время последовательности выключения питания, чтобы увидеть, отключается ли питание. Если линия электропередачи все еще горячая, она проверяется по причине **не** отключения. Если нет причин, то должна быть проблема с модулем, который не позволяет ему отключаться.

### Расположение компонента

См. руководство по OEM для определения местоположения ECM.

### Практические замечания

Эта ошибка указывает на аппаратный сбой в ECM.

См. Код устранения неисправностей t05-1417


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1417
>
> ### Controller Power Down Fault
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1417 PID(P): SPN: FMI: Lamp: Warning SRT: | A controller power-down error has been detected. | The ECM can **not** power down because of some unknown condition. Possible drain on battery. |
>
> GCS ECM
>
> ### Circuit Description
>
> The ECM checks during the power-down sequences to see if power is being shut off. If the power line is still hot, it checks for a reason for **not** shutting down. If no reason exists, then there **must** be a problem with the module that is **not** allowing it to power down.
>
> ### Component Location
>
> Refer to the OEM manual for location of the ECM.
>
> ### Shoptalk
>
> This fault indicates a hardware failure in the ECM.
>
> Refer to Troubleshooting Fault Code t05-1417
