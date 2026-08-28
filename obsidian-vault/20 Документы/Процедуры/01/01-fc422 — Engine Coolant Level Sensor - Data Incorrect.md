---
aliases:
  - "Датчик уровня ОЖ — неверные данные"
type: "Процедура"
doc: "01-fc422"
title_en: "Engine Coolant Level Sensor - Data Incorrect"
title_ru: "Датчик уровня ОЖ — неверные данные"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc422.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc422.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Engine Coolant Level Sensor - Data Incorrect
**Датчик уровня ОЖ — неверные данные**

> [!abstract] Процедура · `01-fc422`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc422.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc422.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 422

### Датчик уровня ОЖ — неверные данные

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 422 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Ошибка датчика переключателя уровня охлаждающей жидкости двигателя. | Отсутствие защиты двигателя для уровня охлаждающей жидкости. Никакого влияния на производительность. |

![[19803601.png]]

Сенсорная схема переключателя уровня охлаждения

### Описание цепи

Датчик переключателя уровня охлаждающей жидкости контролирует уровень охлаждающей жидкости в системе охлаждающей жидкости и передает информацию в электронный модуль управления (ECM). Для нормального уровня охлаждающей жидкости ECM ожидает увидеть 5 VDC на переключателе высокого сигнала уровня охлаждающей жидкости и 0 VDC на переключателе низкого сигнала уровня охлаждающей жидкости. Для низкого уровня охлаждающей жидкости ECM ожидает увидеть 0 VDC на коммутаторе уровня охлаждающей жидкости с высоким сигнальным проводом и 5 VDC на коммутаторе уровня охлаждающей жидкости с низким сигнальным проводом. Этот код неисправности возникает, когда ECM получает противоречивые сообщения от двух сигнальных проводов на датчике переключателя уровня охлаждающей жидкости.

### Расположение компонента

Датчик переключателя уровня охлаждающей жидкости расположен на радиаторе.

### Практические замечания

Этот код неисправности будет активен, когда оба сигнальных провода показывают одинаковое напряжение. Открытая цепь в сигнальном проводе может заставить сигнал дать показания 5 VDC для ECM. Проверьте уровень охлаждающей жидкости. Возможный режим отказа заключается в том, что датчик вышел из строя, в то время как уровень охлаждающей жидкости был нормальным, и ECM не будет его обнаруживать. Если уровень охлаждающей жидкости затем снизился, ECM сообщит об ошибке датчика, **не** низкий уровень охлаждающей жидкости.

См. Код устранения неполадок t05-422


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 422
>
> ### Engine Coolant Level Sensor - Data Incorrect
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 422 PID(P): SPN: FMI: Lamp: Warning SRT: | Engine coolant level switch sensor error. | No engine protection for coolant level. No effect on performance. |
>
> Coolant Level Switch Sensor Circuit
>
> ### Circuit Description
>
> The coolant level switch sensor monitors the coolant level within the coolant system and passes information to the electronic control module (ECM). For normal coolant level the ECM expects to see 5 VDC on the coolant level switch high signal wire and 0 VDC on the coolant level switch low signal wire. For low coolant level, the ECM expects to see 0 VDC on the coolant level switch high signal wire and 5 VDC on the coolant level switch low signal wire. This fault code occurs when the ECM receives conflicting messages from the two signal wires on the coolant level switch sensor.
>
> ### Component Location
>
> The coolant level switch sensor is located on the radiator.
>
> ### Shoptalk
>
> This fault code will go active when both signal wires show the same voltage. An open circuit in a signal wire can cause the signal to give a 5 VDC reading to the ECM. Check the coolant level. A possible failure mode is that the sensor failed while coolant level was normal and the ECM will **not** detect it. If the coolant level then went low, the ECM will then report a sensor error, **not** low coolant level.
>
> Refer to Troubleshooting Fault Code t05-422
