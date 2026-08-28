---
aliases:
  - "Цепь датчика положения рейки 2 — замыкание на плюс (правый ряд)"
type: "Процедура"
doc: "01-fc2975"
title_en: "Fuel Rack Position Sensor 2 Circuit - Shorted High (Right Bank)"
title_ru: "Цепь датчика положения рейки 2 — замыкание на плюс (правый ряд)"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc2975.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc2975.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Fuel Rack Position Sensor 2 Circuit - Shorted High (Right Bank)
**Цепь датчика положения рейки 2 — замыкание на плюс (правый ряд)**

> [!abstract] Процедура · `01-fc2975`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc2975.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc2975.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 2975

### Цепь датчика положения рейки 2 — замыкание на плюс (правый ряд)

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: P(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Труба топливной стойки 2 - первопричина **не** известна (правый берег). | Двигатель может работать грубо или перегружено и выключен. |

![[19803600.png]]

Схема установки датчика положения топливных стойок 2

### Описание цепи

ECM использует этот измеренный сигнал для определения, находится ли топливный стойка в управляемом положении. Это достигается следующим образом:

ECM посылает фиксированный сигнал частоты и напряжения на опорной линии сигнала топливному насосу. ECM также посылает сигнал фиксированной частоты, но переменного напряжения, который на 180 градусов выше фазы от опорного сигнала от измеренной сигнальной линии к топливному насосу. Амплитуда измеряемого напряжения сигнала измеряется в ECM и представляет положение стойки топливного насоса.

Схема внутри топливного насоса сравнивает разницу в напряжении между входом опорного сигнала и входом измеренного сигнала в насос и отправляет сигнал обратно в ECM, что является разницей этих двух сигналов. Сигнал разности напряжений выводится на общую сигнальную линию обратно в ECM. Амплитуда общего сигнала зависит от положения стойки внутри топливного насоса. Схема внутри ECM определяет, находится ли общий сигнал ниже определенного порога. Если это так, это означает, что положение стойки топливного насоса находится в управляемом положении. Значение напряжения измеренной сигнальной линии затем измеряется ECM и представляет положение стойки.

### Расположение компонента

Датчик 2 положения топливной стойки расположен внутри топливного насоса на правом берегу двигателя.

### Практические замечания

Возможные режимы отказа для этой схемы:

- Короткий к батарее на стойке измеряемый сигнал, общий сигнал, опорные схемы сигнала

- Короткий штифт для штифта на положение стойки измеряемый сигнал, общий сигнал, опорные схемы сигнала

- Короткое к земле на стойке положение измеряемого сигнала, общий сигнал, опорные схемы сигнала

- Открытая схема на стойке измеряемого положения сигнала, общий сигнал, опорные схемы сигнала

- Плохой топливный насос

- Плохая ECM.

Эта ошибка не требует неисправности двигателя. Двигатель может перескочить и выключиться. Если код ошибки 234 (неисправность скорости) и код ошибки 2975 присутствуют, сначала устраните неисправность кода 2975. Если вы отслеживаете положение топливной стойки на правом берегу, она будет считывать ноль миллиметров (нулевое заправление).

Если код 2975 и 182 ошибки активны, сначала устраните код 182 ошибки.

См. Код устранения неисправностей t05-2975


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 2975
>
> ### Fuel Rack Position Sensor 2 Circuit - Shorted High (Right Bank)
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: PID(P): SPN: FMI: Lamp: Warning SRT: | Fuel rack position 2 circuit - root cause **not** known (right bank). | Engine can possibly run rough or overspeed and shutdown. |
>
> Fuel Rack Position Sensor 2 Circuit
>
> ### Circuit Description
>
> The ECM uses this rack position measured signal to determine if the fuel rack is at the commanded position. This is accomplished as follows:
>
> The ECM sends out a fixed frequency and voltage signal on the reference signal line to the fuel pump. The ECM also sends out a fixed frequency but variable voltage signal that is 180 degrees out of phase from the reference signal from the measured signal line to the fuel pump. The amplitude of the measured signal voltage is measured in the ECM and represents the rack position of the fuel pump.
>
> Circuitry inside the fuel pump compares the difference in voltage between the reference signal input and the measured signal input to the pump and sends a signal back to the ECM that is the difference of these two signals. The difference voltage signal is output on the common signal line back to the ECM. The amplitude of the common signal is dependent on the position of the rack inside the fuel pump. Circuitry inside the ECM determines if the common signal is below a certain threshold. If it is, this means that the rack position of the fuel pump is at the commanded position. The voltage value of the measured signal line is then measured by the ECM and represents the rack position.
>
> ### Component Location
>
> The fuel rack position sensor 2 is located internal to the fuel pump on the right bank of the engine.
>
> ### Shoptalk
>
> The possible fail modes for this circuit are:
>
> - Short to battery on the rack position measured signal, common signal, reference signal circuits
>
> - Short pin to pin on the rack position measured signal, common signal, reference signal circuits
>
> - Short to ground on the rack position measured signal, common signal, reference signal circuits
>
> - Open circuit on the rack position measured signal, common signal, reference signal circuits
>
> - Bad fuel pump
>
> - Bad ECM.
>
> This fault does **not** require engine speed to log a fault. The engine can overspeed and shut down. If Fault Code 234 (overspeed fault) and Fault Code 2975 are present, troubleshoot the Fault Code 2975 first. If you are monitoring the fuel rack position for the right bank, it will read zero millimeters (zero fueling).
>
> If Fault Code 2975 and 182 are active, troubleshoot Fault Code 182 first.
>
> Refer to Troubleshooting Fault Code t05-2975
