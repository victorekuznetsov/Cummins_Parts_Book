---
aliases:
  - "Цепь реле шины зажигания"
type: "Процедура"
doc: "82-fc339"
title_en: "Ignition Bus Relay Circuit"
title_ru: "Цепь реле шины зажигания"
modified: "2010-09-02"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc339.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc339.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Ignition Bus Relay Circuit
**Цепь реле шины зажигания**

> [!abstract] Процедура · `82-fc339`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc339.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc339.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 339

### Цепь реле шины зажигания

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 339 P(P): S087, 4 SPN: 1267 FMI: 4 лампы: Желтая СТО: | Менее 6 VDC обнаружено на выходной цепи реле зажигания шины, когда высокое напряжение ожидалось ECM. | ICONTM будет отключен.  Включено только обязательное отключение. Постоянная мощность будет находиться в цепи зажигания переключателя зажигания. |

![[19803215.png]]

Idle Shutdown Vehicle Accessory/Ignition Bus Relay Circuit (недоступная ссылка)

### Описание цепи

Реле зажигания управляет цепями зажигания, питающими элементы управления кондиционированием отопления / воздуха и другое оборудование, подключенное к реле (реле) шины зажигания. Это реле(ы) управляется положительным (+) сигналом реле зажигания от контакта 35 разъема ECM OEM.

### Расположение компонента

Реле шины зажигания расположено под приборной панелью внутри кабины транспортного средства.

### Практические замечания

Этот дефект обычно указывает на короткое замыкание на землю или открытую цепь от контакта 35 разъема ECM (ретранслятор зажигания положительный (+)). Реле зажигания положительное (+) (контакт 35) выводит 12 VDC, чтобы открыть реле (реле) шины зажигания, когда ICONTM приводит в действие транспортное средство и нуждается в отключении питания, идущего в цепь кабины. Реле (ретрансляторы) шины ICONTM обычно закрывается, когда не применяется питание.

См. Код устранения неполадок t05-339


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 339
>
> ### Ignition Bus Relay Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 339 PID(P): S087, 4 SPN: 1267 FMI: 4 Lamp: Yellow SRT: | Less than 6 VDC detected at the ignition bus relay output circuit when the high voltage was expected by the ECM. | The ICON™ will be disabled. **Only** mandatory shutdown will be enabled. Constant power will be at the keyswitch ignition circuit. |
>
> Idle Shutdown Vehicle Accessory/Ignition Bus Relay Circuit
>
> ### Circuit Description
>
> The ignition bus relay controls ignition circuits powering the heating/air conditioning controls and other equipment connected to the ignition bus relay(s). This relay(s) is controlled by ignition relay positive (+) signal from the ECM OEM connector pin 35.
>
> ### Component Location
>
> The ignition bus relay is located under the dash inside the vehicle cab.
>
> ### Shoptalk
>
> This fault typically indicates a short circuit to ground or an open circuit from the ECM connector pin 35 (ignition relay positive (+)). Ignition relay positive (+) (pin 35) outputs 12 VDC to open the ignition bus relay(s) when ICON™ has powered down the vehicle and needs to disconnect power going to the cab circuit. The ICON™ bus relay(s) is normally closed when no power is applied.
>
> Refer to Troubleshooting Fault Code t05-339
