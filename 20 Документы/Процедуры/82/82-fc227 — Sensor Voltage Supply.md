---
aliases:
  - "Питание датчиков"
type: "Процедура"
doc: "82-fc227"
title_en: "Sensor Voltage Supply"
title_ru: "Питание датчиков"
modified: "2010-09-02"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc227.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc227.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Sensor Voltage Supply
**Питание датчиков**

> [!abstract] Процедура · `82-fc227`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc227.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc227.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 227

### Питание датчиков

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 227 P(P): S232 SPN: 620 FMI: 3 лампы: Желтая СТО: | Высокое напряжение, обнаруженное на линии электронного модуля управления (ECM) для питания некоторых датчиков. (VSEN 2) | Двигатель будет работать с поломкой. Отсутствие защиты двигателя от давления масла и уровня охлаждающей жидкости. |

![[19200194.png]]

Сенсорная схема напряжения питания

### Описание цепи

ECM поставляет каждый из этих датчиков с +5 VDC. Если провод подачи к любому датчику поврежден, датчик будет работать ** не** правильно.

Примечание: На приведенном выше изображении схемы для датчика давления влажного резервуара / воздушного компрессора и проводов положения Top 2 Gear помечены по-разному на диаграмме промышленной проводов. Эквивалентные различия в промышленных этикетках заключаются в следующем:

- Датчик давления мокрого резервуара + 5-вольтовое снабжение = OEM-снабжение давлением (контакты 1-18)

- Сигнал давления в мокром резервуаре = сигнал давления OEM (контакты 3-19)

- Возвращение давления в мокром резервуаре = Возвращение давления OEM (контакты 2-20)

- Привод воздушного компрессора = выключенный выход A (контакты 5-14)

- Возвращение воздушного компрессора = запас (контакты 6-11)

- Топ 2 Положение наушников + 5-вольтное снабжение = запас (контакты 14-19)

- Топ 2 Gear Position Input = Spare (контакты 15-18)

- Вернуть позицию 2 Gear = Запас (контакты 16-17)

### Расположение компонента

Датчик ограничения впуска топлива расположен на входе топливного насоса.

Датчик давления/температуры масла расположен перед воздушным компрессором.

Датчик уровня масла расположен в масляной кастрюле.

Датчик давления влажного резервуара расположен на воздушном компрессоре.

Датчик уровня охлаждения. См. OEM для правильного местоположения.

Топ-2 датчика положения передачи - расположен на трансмиссии, если транспортное средство имеет трансмиссию SpicerTM Top 2 Automate. См. OEM для правильного местоположения.

### Практические замечания

Высокое напряжение на датчике + 5-VDC линии питания будет вызвано коротким зарядом батареи в линии питания или коротким между проводом привода и проводом питания.

См. Код устранения неполадок t05-227


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 227
>
> ### Sensor Voltage Supply
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 227 PID(P): S232 SPN: 620 FMI: 3 Lamp: Yellow SRT: | High voltage detected on the electronic control module (ECM) voltage supply line to some sensors. (VSEN 2) | Engine will run derated. No engine protection for oil pressure and coolant level. |
>
> Sensor Supply Voltage Circuit
>
> ### Circuit Description
>
> The ECM supplies each of these sensors with + 5 VDC. If the supply wire to any sensor is damaged, the sensor will **not** work correctly.
>
> Note: In the above picture, the circuits for the wet tank pressure sensor/air compressor and Top 2 Gear Position wires are labeled differently on the industrial wiring diagram. The equivalent differences in the industrial labels are as follows:
>
> - Wet Tank Pressure Sensor + 5-Volt Supply = OEM Pressure Supply (Pins 1 to 18)
>
> - Wet Tank Pressure Signal = OEM Pressure Signal (Pins 3 to 19)
>
> - Wet Tank Pressure Return = OEM Pressure Return (Pins 2 to 20)
>
> - Air Compressor Actuator = Switched Output A (Pins 5 to 14)
>
> - Air Compressor Return = Spare (Pins 6 to 11)
>
> - Top 2 Gear Position + 5-Volt Supply = Spare (Pins 14 to 19)
>
> - Top 2 Gear Position Input = Spare (Pins 15 to 18)
>
> - Top 2 Gear Position Return = Spare (Pins 16 to 17)
>
> ### Component Location
>
> Fuel inlet restriction sensor is located on the fuel pump inlet.
>
> Oil pressure/temperature sensor is located in front of the air compressor.
>
> Oil level sensor is located in the oil pan.
>
> Wet tank pressure sensor is located on the air compressor.
>
> Coolant level sensor. Refer to OEM for proper location.
>
> Top 2 transmission position sensor - located on the transmission if vehicle has a Spicer™ Top 2 Automate transmission. Refer to OEM for proper location.
>
> ### Shoptalk
>
> High voltage on the sensor + 5-VDC supply line will be caused by a short to battery in the supply line or a short between an actuator wire and the supply wire.
>
> Refer to Troubleshooting Fault Code t05-227
