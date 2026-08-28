---
type: "Процедура"
doc: "19-fc132"
title_en: "Accelerator Position Sensor: CELECT™-Type Accelerator Pedal or Lever"
modified: "2011-03-01"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc132.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc132.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Accelerator Position Sensor: CELECT™-Type Accelerator Pedal or Lever

> [!abstract] Процедура · `19-fc132`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc132.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc132.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 132

### Датчик положения акселератора: Педаль или рычаг ускорителя CELECTTM-Type

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 132 PID(P): P91 SPN: 091 ФМИ: 4 лампы: Красная СТО: 00-351 | Менее 0,13 VDC обнаруживается на педали акселератора или рычага положения сигнала контакта 29 интерфейса OEM проводов ремня разъема ECM. | Калибровочная зависимость мощности и скорости снижается. |

![[19400817.png]]

Датчик положения акселератора: Педаль или рычаг ускорителя CELECTTM-Type

### Описание цепи

Педаль или рычаг акселератора обеспечивает команду педали или рычага акселератора оператора к ECM через упряжку проводов OEM и упряжку проводов интерфейса OEM. ECM использует этот сигнал для определения команды заправки клапана привода топливной рельсы.

### Расположение компонента

Расположение педали или рычага ускорителя варьируется в зависимости от каждого OEM. См. руководство по OEM.

### Практические замечания

Педаль акселератора или датчик положения рычага представляет собой потенциометр. Спецификации сопротивления педали акселератора или датчика положения рычага следующие:

- Между предложением и возвратом = 2000-3000 Ом

- Между подачей и сигналом: Выпущен = 1500-3000 Ом. Депрессия = 200-1500 Ом.

Примечание: Если педаль акселератора или рычаг или педаль акселератора или датчик положения рычага изменены, или после калибровочной загрузки, цикл педали акселератора или рычага (переключатель зажигания поворота) через его полное путешествие три раза. Эта процедура калибрует новую педаль акселератора или рычаг с помощью ECM.

Устранение неполадок код t05-132


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 132
>
> ### Accelerator Position Sensor: CELECT™-Type Accelerator Pedal or Lever
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 132 PID(P): P91 SPN: 091 FMI: 4 Lamp: Red SRT: 00-351 | Less than 0.13 VDC detected at the accelerator pedal or lever position signal pin 29 of the OEM interface harness ECM connector. | Calibration-dependent power and speed derate. |
>
> Accelerator Position Sensor: CELECT™-Type Accelerator Pedal or Lever
>
> ### Circuit Description
>
> The accelerator pedal or lever provides the operator's accelerator pedal or lever command to the ECM through the OEM harness and OEM interface harness. The ECM uses this signal to determine the fueling command for the fuel rail actuator valve.
>
> ### Component Location
>
> The accelerator pedal or lever location varies with each OEM. Refer to the OEM manual.
>
> ### Shoptalk
>
> The accelerator pedal or lever position sensor is a potentiometer. The resistance specifications of the accelerator pedal or lever position sensor are the following:
>
> - Between the supply and the return = 2000 to 3000 ohms
>
> - Between the supply and the signal: Released = 1500 to 3000 ohms. Depressed = 200 to 1500 ohms.
>
> Note: If the accelerator pedal or lever or accelerator pedal or lever position sensor is changed, or after a calibration download, cycle the accelerator pedal or lever (turn keyswitch ON) through its complete travel three times. This procedure calibrates the new accelerator pedal or lever with the ECM.
>
> Refer to Troubleshooting Fault Code t05-132
