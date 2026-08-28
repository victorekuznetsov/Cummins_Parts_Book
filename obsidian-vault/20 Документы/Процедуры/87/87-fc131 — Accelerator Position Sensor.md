---
aliases:
  - "Датчик положения акселератора"
type: "Процедура"
doc: "87-fc131"
title_en: "Accelerator Position Sensor"
title_ru: "Датчик положения акселератора"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc131.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc131.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Accelerator Position Sensor
**Датчик положения акселератора**

> [!abstract] Процедура · `87-fc131`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc131.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc131.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 131

### Датчик положения акселератора

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 131 PID(P): P091 SPN: 091 ФМИ: 3 лампы: Красная СТО: | Чрезмерное напряжение, обнаруженное на месте расположения ускорителя, сигнализирует контакт 30 проводов OEM-интерфейса. | Калибровочная зависимость мощности и скорости снижается. |

![[19a00603.png]]

Датчик положения акселератора

### Описание цепи

Педаль акселератора обеспечивает команду акселератора водителя электронному модулю управления (ECM) через OEM-проводник и OEM-интерфейс. ECM использует этот сигнал для определения команды заправки топливной стойки RP39.

### Расположение компонента

Расположение педали ускорителя варьируется в зависимости от каждого OEM. См. руководство изготовителя машины по диагностике и ремонту.

### Практические замечания

Датчик положения ускорителя представляет собой потенциометр. Спецификации сопротивления датчика положения ускорителя следующие:

- Между предложением и возвратом = 2000-3000 Ом

- Между поставкой и сигналом: Высвобожденный = 1500 до 3000 Ом, угнетенный = 200 до 1500 Ом.

Примечание: Если датчик положения ускорителя или акселератора изменен или после калибровочной загрузки, проведите педаль акселератора (переключатель зажигания поворота) через его полное путешествие три раза. Эта процедура калибрует новый ускоритель с помощью ECM.

См. Код устранения неполадок t05-131


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 131
>
> ### Accelerator Position Sensor
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 131 PID(P): P091 SPN: 091 FMI: 3 Lamp: Red SRT: | Excessive voltage detected at the accelerator position signal pin 30 of the OEM interface harness. | Calibration-dependent power and speed derate. |
>
> Accelerator Position Sensor
>
> ### Circuit Description
>
> The accelerator pedal provides the driver's accelerator command to the electronic control module (ECM) through the OEM harness and the OEM interface harness. The ECM uses this signal to determine the fueling command for the RP39 fuel pump rack.
>
> ### Component Location
>
> The accelerator pedal location varies with each OEM. Refer to the OEM troubleshooting and repair manual.
>
> ### Shoptalk
>
> The accelerator position sensor is a potentiometer. The resistance specifications of the accelerator position sensor are as follow:
>
> - Between supply and return = 2000 to 3000 ohms
>
> - Between supply and signal: Released = 1500 to 3000 ohms, Depressed = 200 to 1500 ohms.
>
> Note: If the accelerator or accelerator position sensor is changed, or after a calibration download, cycle the accelerator pedal (turn keyswitch ON) through its complete travel three times. This procedure calibrates the new accelerator with the ECM.
>
> Refer to Troubleshooting Fault Code t05-131
