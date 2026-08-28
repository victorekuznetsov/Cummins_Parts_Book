---
type: "Процедура"
doc: "19-fc133"
title_en: "Remote Accelerator Position Sensor: CELECT™-Type Accelerator Pedal or Lever"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc133.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc133.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Remote Accelerator Position Sensor: CELECT™-Type Accelerator Pedal or Lever

> [!abstract] Процедура · `19-fc133`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc133.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc133.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 133

### Датчик положения дистанционного акселератора: Педаль или рычаг ускорителя CELECTTM-Type

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 133 P(P): P29 SPN: 029 FMI: 3 лампы: Красная СТО: 00-385 | Более 4,82 VDC обнаружены на удаленном дроссельном сигнале положения контакта 30 интерфейса OEM-проводов ремня. | Калибровочная зависимость мощности и скорости снижается. |

![[19400819.png]]

Датчик положения дистанционного акселератора: Педаль или рычаг ускорителя CELECTTM-Type

### Описание цепи

Педаль или рычаг удаленного ускорителя обеспечивает команду педали или рычага ускорителя оператора к ECM через OEM-проводник и OEM-интерфейс. ECM использует этот сигнал для определения команды заправки клапана привода топливной рельсы.

### Расположение компонента

Расположение педали или рычага ускорителя варьируется в зависимости от каждого OEM. См. руководство по OEM.

### Практические замечания

Педаль акселератора или датчик положения рычага представляет собой потенциометр. Спецификации сопротивления педали акселератора или датчика положения рычага следующие:

- Между предложением и возвратом = 2000 до 3000 Ом.

- Между поставкой и сигналом: Высвобожденный = 1500-3000 Ом; угнетенный = 200-1500 Ом.

Примечание: Если педаль акселератора или рычаг или педаль акселератора или датчик положения рычага изменены, или после калибровочной загрузки, цикл педали акселератора или рычага (переключатель зажигания поворота) через его полное путешествие три раза. Эта процедура калибрует новую педаль акселератора или рычаг с помощью ECM.

Устранение неполадок код t05-133


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 133
>
> ### Remote Accelerator Position Sensor: CELECT™-Type Accelerator Pedal or Lever
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 133 PID(P): P29 SPN: 029 FMI: 3 Lamp: Red SRT: 00-385 | More than 4.82 VDC detected at the remote throttle position signal pin 30 of the OEM interface harness. | Calibration-dependent power and speed derate. |
>
> Remote Accelerator Position Sensor: CELECT™-Type Accelerator Pedal or Lever
>
> ### Circuit Description
>
> The remote accelerator pedal or lever provides the operator's accelerator pedal or lever command to the ECM through the OEM harness and the OEM interface harness. The ECM uses this signal to determine the fueling command for the fuel rail actuator valve.
>
> ### Component Location
>
> The accelerator pedal or lever location varies with each OEM. Refer to the OEM manual.
>
> ### Shoptalk
>
> The accelerator pedal or lever position sensor is a potentiometer. The resistance specifications of the accelerator pedal or lever position sensor are the following:
>
> - Between supply and return = 2000 to 3000 ohms.
>
> - Between supply and signal: Released = 1500 to 3000 ohms; Depressed = 200 to 1500 ohms.
>
> Note: If the accelerator pedal or lever or accelerator pedal or lever position sensor is changed, or after a calibration download, cycle the accelerator pedal or lever (turn keyswitch ON) through its complete travel three times. This procedure calibrates the new accelerator pedal or lever with the ECM.
>
> Refer to Troubleshooting Fault Code t05-133
