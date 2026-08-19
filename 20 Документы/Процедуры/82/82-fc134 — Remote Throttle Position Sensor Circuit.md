---
aliases:
  - "Цепь датчика положения дистанционного органа управления"
type: "Процедура"
doc: "82-fc134"
title_en: "Remote Throttle Position Sensor Circuit"
title_ru: "Цепь датчика положения дистанционного органа управления"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc134.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc134.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Remote Throttle Position Sensor Circuit
**Цепь датчика положения дистанционного органа управления**

> [!abstract] Процедура · `82-fc134`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc134.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc134.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 134

### Цепь датчика положения дистанционного органа управления

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 134 PID(P): P029 SPN: 974 FMI: 4/4 лампы: Красная СТО: | Низкое напряжение, обнаруженное в цепи сигнала удаленного положения дроссельной заслонки. | Ни один из них не работает, если используется удаленный дроссел ** не **. |

![[19c00110.png]]

Цепь датчика положения дистанционного органа управления

### Описание цепи

Педаль дистанционного дроссельного заслонка обеспечивает команду дроссельного заслонка водителя электронному модулю управления (ECM) через OEM-проводку и OEM-интерфейс. ECM использует этот сигнал для определения команды заправки.

### Расположение компонента

Удалённое расположение педали дросселя варьируется в зависимости от каждого OEM. См. руководство изготовителя машины по диагностике и ремонту.

### Практические замечания

Датчик положения удаленного дроссельного заслонка представляет собой потенциометр. Спецификации сопротивления датчика положения дроссельной заслонки:

- Между предложением и возвратом = 2000-3000 Ом

- Между поставкой и сигналом: Выпущено = 1500 до 3000 Ом, угнетено = 200 до 1500 Ом

** Примечание:** Если датчик положения удаленного дроссельного заслонка заменен или после выполнения калибровочной загрузки, проведите педаль дроссельного зажигания (включите переключатель зажигания поворота) через его полное перемещение три раза. Эта процедура калибрует новый дистанционный дроссел с ECM.

- Удаленный дроссел позволяет переключателю *** быть включенным для работы удаленного дросселя.

- Возможные причины этого кода неисправности включают открытую цепь в проводе питания, короткое замыкание для заземления в проводах питания или сигнала, дефектный датчик положения удаленного дроссельной заслонки или неисправный источник питания ECM.

Устранение неполадок код t05-134


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 134
>
> ### Remote Throttle Position Sensor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 134 PID(P): P029 SPN: 974 FMI: 4/4 Lamp: Red SRT: | Low voltage detected at the remote throttle position signal circuit. | None on performance if remote throttle is **not** used. |
>
> Remote Throttle Position Sensor Circuit
>
> ### Circuit Description
>
> The remote throttle pedal provides the driver's throttle command to the electronic control module (ECM) through the OEM harness and the OEM interface harness. The ECM uses this signal to determine the fueling command.
>
> ### Component Location
>
> The remote throttle pedal location varies with each OEM. Refer to the OEM troubleshooting and repair manual.
>
> ### Shoptalk
>
> The remote throttle position sensor is a potentiometer. The throttle position sensor resistance specifications are:
>
> - Between supply and return = 2000 to 3000 ohms
>
> - Between supply and signal: Released = 1500 to 3000 ohms, Depressed = 200 to 1500 ohms
>
> **Note:** If the remote throttle position sensor is replaced, or after a calibration download is performed, cycle the throttle pedal (turn keyswitch on) through its complete travel three times. This procedure calibrates the new remote throttle with the ECM.
>
> - The remote throttle enable switch **must** be on for the remote throttle to operate.
>
> - Possible causes of this fault code include an open circuit in the supply wire, short circuit to ground in the supply or signal wires, defective remote throttle position sensor, or a failed ECM power supply.
>
> Refer to Troubleshooting Fault Code t05-134
