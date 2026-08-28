---
aliases:
  - "Цепь положения привода рейки 1 — неверные данные (левый ряд)"
type: "Процедура"
doc: "01-fc171"
title_en: "Fuel Rack Actuator Position 1 Circuit - Data Incorrect (Left Bank)"
title_ru: "Цепь положения привода рейки 1 — неверные данные (левый ряд)"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc171.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc171.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Fuel Rack Actuator Position 1 Circuit - Data Incorrect (Left Bank)
**Цепь положения привода рейки 1 — неверные данные (левый ряд)**

> [!abstract] Процедура · `01-fc171`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc171.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc171.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 171

### Цепь положения привода рейки 1 — неверные данные (левый ряд)

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 171 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Цепь положения привода рейки 1 — неверные данные (левый ряд). | Производительность может быть вялой или медленной, чтобы реагировать. |

![[19803597.png]]

Завод привода топливного бака 1 позиция

### Описание цепи

Измеренные, опорные и общие сигналы схемы датчика положения топливной стойки используются ECM для проверки того, что стойка была правильно расположена приводом стойки. Этот код неисправности указывает, что либо стойка механически застряла, либо данные датчика положения стойки неверны. Это достигается следующим образом:

ECM посылает фиксированный сигнал частоты и напряжения на опорной линии сигнала топливному насосу. ECM также посылает сигнал фиксированной частоты, но переменного напряжения, который на 180 градусов выше фазы от опорного сигнала от измеренной сигнальной линии к топливному насосу. Амплитуда измеряемого напряжения сигнала измеряется в ECM и представляет положение стойки топливного насоса.

Схема внутри топливного насоса сравнивает разницу в напряжении между входом опорного сигнала и входом измеренного сигнала в насос и отправляет сигнал обратно в ECM, что является разницей этих двух сигналов. Сигнал разности напряжений выводится на общую сигнальную линию обратно в ECM. Амплитуда общего сигнала зависит от положения стойки внутри топливного насоса. Схема внутри ECM определяет, находится ли общий сигнал ниже определенного порога. Если это так, это означает, что положение стойки топливного насоса находится в управляемом положении. Значение напряжения измеренной сигнальной линии затем измеряется ECM и представляет положение стойки.

### Расположение компонента

Реечка топливного насоса, привод реечного насоса и датчик положения реечного насоса расположены внутри топливного насоса.

Этот код неисправности требует, чтобы скорость двигателя была больше нуля, прежде чем неисправность будет активна.

### Практические замечания

Возможные режимы отказа - механическая застрявшая стойка, датчик положения стойки, застрявший в диапазоне, датчик положения стойки из калибровки или плохой топливный насос.

Этот код неисправности требует, чтобы скорость двигателя была больше нуля, прежде чем неисправность будет активна.

Код 171 ошибки может активироваться после исправления кода 168 ошибки. Если это так, выключите ключ и код 171 ошибки, и вы сможете очистить его.

См. Устранение неполадок код t05-171


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 171
>
> ### Fuel Rack Actuator Position 1 Circuit - Data Incorrect (Left Bank)
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 171 PID(P): SPN: FMI: Lamp: Warning SRT: | Fuel rack actuator position 1 circuit - data incorrect (left bank). | Performance can be sluggish or slow to respond. |
>
> Fuel Rack Actuator Position 1 Circuit
>
> ### Circuit Description
>
> The fuel rack position sensor circuit's measured, reference and common signals are used by the ECM to verify that the rack has been properly positioned by the rack actuator. This fault code indicates that either the rack is mechanically stuck, or the rack position sensor data is incorrect. This is accomplished as follows:
>
> The ECM sends out a fixed frequency and voltage signal on the reference signal line to the fuel pump. The ECM also sends out a fixed frequency but variable voltage signal that is 180 degrees out of phase from the reference signal from the measured signal line to the fuel pump. The amplitude of the measured signal voltage is measured in the ECM and represents the rack position of the fuel pump.
>
> Circuitry inside the fuel pump compares the difference in voltage between the reference signal input and the measured signal input to the pump and sends a signal back to the ECM that is the difference of these two signals. The difference voltage signal is output on the common signal line back to the ECM. The amplitude of the common signal is dependent on the position of the rack inside the fuel pump. Circuitry inside the ECM determines if the common signal is below a certain threshold. If it is, this means that the rack position of the fuel pump is at the commanded position. The voltage value of the measured signal line is then measured by the ECM and represents the rack position.
>
> ### Component Location
>
> The fuel pump rack, rack actuator, and rack position sensor are all located within the fuel pump.
>
> This fault code requires engine speed greater than zero before the fault will go active.
>
> ### Shoptalk
>
> The possible failure modes are rack mechanically stuck, rack position sensor stuck in range, rack position sensor out of calibration, or bad fuel pump.
>
> This fault code requires engine speed greater than zero before the fault will go active.
>
> Fault Code 171 can go active after Fault Code 168 is corrected. If this is the case, key off and Fault Code 171 will go inactive and can be cleared
>
> Refer to Troubleshooting Fault Code t05-171
