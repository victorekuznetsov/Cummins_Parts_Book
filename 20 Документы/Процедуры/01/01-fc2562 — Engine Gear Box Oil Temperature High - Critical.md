---
aliases:
  - "Высокая температура масла редуктора двигателя — критично"
type: "Процедура"
doc: "01-fc2562"
title_en: "Engine Gear Box Oil Temperature High - Critical"
title_ru: "Высокая температура масла редуктора двигателя — критично"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc2562.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc2562.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Engine Gear Box Oil Temperature High - Critical
**Высокая температура масла редуктора двигателя — критично**

> [!abstract] Процедура · `01-fc2562`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc2562.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc2562.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 2562

### Высокая температура масла редуктора двигателя — критично

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 2562 PCODE(P): СПН: ФМИ: Лампа: Отключение SRT: | Сигнал напряжения указывает, что температура масла в коробке передач двигателя превысила порог отключения для высокой температуры масла в коробке передач двигателя. | Генераторный набор отключится. |

![[19600392.png]]

Двигатель Gear Box датчик температуры масла

### Описание цепи

Датчик температуры масла в коробке передач двигателя является датчиком типа переключателя. После того, как температура повысится выше точки переключателя, датчик закроет цепь. Эта замкнутая цепь заставит цифровой модуль ввода LonWorks послать сигнал в сети LonWorks на генераторный набор ECM, указывающий на высокую температуру масла в коробке передач двигателя - критическое состояние существует.

### Расположение компонента

Датчик температуры масла в коробке передач двигателя расположен на коробке передач.

### Практические замечания

Этот код неисправности может быть вызван высокотемпературным состоянием или коротким замыканием в масляном переключателе коробки передач двигателя на цифровой модуль ввода. Как температура масла коробки передач, так и проверка короткого замыкания должны быть выполнены для устранения неисправности.

См. Код устранения неисправностей t05-2562


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 2562
>
> ### Engine Gear Box Oil Temperature High - Critical
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 2562 PCODE(P): SPN: FMI: Lamp: Shutdown SRT: | Voltage signal indicates the engine gear box oil temperature has exceeded the shutdown threshold for high engine gear box oil temperature. | Generator set will shutdown. |
>
> Engine Gear Box Oil Temperature Sensor Circuit
>
> ### Circuit Description
>
> The engine gear box oil temperature sensor is a switch type sensor. After the temperature increases above the switch point, the sensor will close the circuit. This closed circuit will cause the LonWorks digital input module to send a signal on the LonWorks network to the generator set ECM indicating an engine gear box oil temperature high - critical condition exists.
>
> ### Component Location
>
> The engine gear box oil temperature sensor is located on the gear box.
>
> ### Shoptalk
>
> This fault code can be caused by a high temperature condition, or a short circuit in the engine gear box oil temperature switch to digital input module circuit. Both temperature of the gear box oil and a check for a short circuit **must** be performed to troubleshoot this fault.
>
> Refer to Troubleshooting Fault Code t05-2562
