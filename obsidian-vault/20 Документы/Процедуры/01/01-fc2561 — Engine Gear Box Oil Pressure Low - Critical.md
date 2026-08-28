---
aliases:
  - "Низкое давление масла редуктора двигателя — критично"
type: "Процедура"
doc: "01-fc2561"
title_en: "Engine Gear Box Oil Pressure Low - Critical"
title_ru: "Низкое давление масла редуктора двигателя — критично"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc2561.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc2561.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Engine Gear Box Oil Pressure Low - Critical
**Низкое давление масла редуктора двигателя — критично**

> [!abstract] Процедура · `01-fc2561`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc2561.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc2561.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 2561

### Низкое давление масла редуктора двигателя — критично

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 2561 PCODE(P): СПН: ФМИ: Лампа: Отключение SRT: | Сигнал напряжения указывает на то, что давление масла в коробке передач двигателя упало ниже порога выключения для низкого давления масла в коробке передач двигателя. | Генераторный набор отключится. |

![[19600393.png]]

Схема датчика давления масла Gear Box

### Описание цепи

Датчик давления масла в коробке передач двигателя является датчиком переключателя типа. После того, как давление падает ниже точки переключателя, датчик закрывает цепь. Эта замкнутая цепь заставит цифровой модуль ввода LonWorks послать сигнал в сети LonWorks на генераторный набор ECM, указывающий на низкое давление масла в коробке передач двигателя - критическое состояние существует.

### Расположение компонента

Датчик давления масла в коробке передач двигателя расположен на коробке передач.

### Практические замечания

Эта неисправность может быть вызвана состоянием низкого давления или коротким замыканием в масляном переключателе коробки передач двигателя на схему цифрового входного модуля. Как давление масла коробки передач, так и проверка короткого замыкания должны быть выполнены для устранения неисправности.

См. Код устранения неполадок t05-2561


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 2561
>
> ### Engine Gear Box Oil Pressure Low - Critical
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 2561 PCODE(P): SPN: FMI: Lamp: Shutdown SRT: | Voltage signal indicates the engine gear box oil pressure has dropped below the shutdown threshold for low engine gear box oil pressure. | Generator set will shutdown. |
>
> Engine Gear Box Oil Pressure Sensor Circuit
>
> ### Circuit Description
>
> The engine gear box oil pressure sensor is a switch type sensor. After the pressure drops below the switch point, the sensor will close the circuit. This closed circuit will cause the LonWorks digital input module to send a signal on the LonWorks network to the generator set ECM indicating an engine gear box oil pressure low - critical condition exists.
>
> ### Component Location
>
> The engine gear box oil pressure sensor is located on the gear box.
>
> ### Shoptalk
>
> This fault can be caused by a low pressure condition, or a short circuit in the engine gear box oil pressure switch to digital input module circuit. Both pressure of the gearbox oil and a check for a short circuit **must** be performed to troubleshoot this fault.
>
> Refer to Troubleshooting Fault Code t05-2561
