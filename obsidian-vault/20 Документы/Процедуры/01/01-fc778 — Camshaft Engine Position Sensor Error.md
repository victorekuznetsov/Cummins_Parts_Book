---
aliases:
  - "Ошибка датчика положения распределительного вала"
type: "Процедура"
doc: "01-fc778"
title_en: "Camshaft Engine Position Sensor Error"
title_ru: "Ошибка датчика положения распределительного вала"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc778.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc778.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Camshaft Engine Position Sensor Error
**Ошибка датчика положения распределительного вала**

> [!abstract] Процедура · `01-fc778`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc778.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc778.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 778

### Ошибка датчика положения распределительного вала

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 778 PID(P): СПН: ФМИ: Лампа: Отключение SRT: | Сигнал о скорости двигателя не был обнаружен датчиком положения двигателя в распределительном валу. | Двигатель отключится. |

![[19803590.png]]

Camshaft Engine Position Sensor Circuit (Схема расположения датчика)

### Описание цепи

Датчик положения двигателя распределительного вала обеспечивает информацию о скорости двигателя и положении электронному модулю управления (ECM). Датчик должен быть включен 5 VDC для работы. Датчик генерирует сигнал из дополнительной доли на распределительном вале.

### Расположение компонента

См. схемы двигателя. 100-002 для расположения компонентов.

### Практические замечания

Возможные причины этого кода неисправности включают поврежденный датчик положения двигателя распределительного вала, открытый или короткий замыкание или отказ напряжения питания.

См. Код устранения неполадок t05-778


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 778
>
> ### Camshaft Engine Position Sensor Error
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 778 PID(P): SPN: FMI: Lamp: Shutdown SRT: | No engine speed signal detected from the camshaft engine position sensor. | Engine will shutdown. |
>
> Camshaft Engine Position Sensor Circuit
>
> ### Circuit Description
>
> The camshaft engine position sensor provides engine speed and position information to the electronic control module (ECM). The sensor **must** be powered up by 5 VDC to operate. The sensor generates the signal from an extra lobe on the camshaft.
>
> ### Component Location
>
> Refer to the Engine Diagrams. 100-002 for the component location.
>
> ### Shoptalk
>
> Possible causes of this fault code include damaged camshaft engine position sensor, open or shorted circuit, or power supply voltage failure.
>
> Refer to Troubleshooting Fault Code t05-778
