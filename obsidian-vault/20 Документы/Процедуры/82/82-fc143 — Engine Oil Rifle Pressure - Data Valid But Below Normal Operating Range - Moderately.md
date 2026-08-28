---
aliases:
  - "Давление масла в главной магистрали — ниже нормы — умеренный уровень"
type: "Процедура"
doc: "82-fc143"
title_en: "Engine Oil Rifle Pressure - Data Valid But Below Normal Operating Range - Moderately Severe Level"
title_ru: "Давление масла в главной магистрали — ниже нормы — умеренный уровень"
modified: "2010-10-07"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc143.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc143.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Engine Oil Rifle Pressure - Data Valid But Below Normal Operating Range - Moderately Severe Level
**Давление масла в главной магистрали — ниже нормы — умеренный уровень**

> [!abstract] Процедура · `82-fc143`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-10-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc143.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc143.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 143

### Давление масла в главной магистрали — ниже нормы — умеренный уровень

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 143 PID(P): P100 SPN: 100 FMI: 1/18 лампы: Янтарная СРТ: | Давление масла в главной магистрали — ниже нормы — умеренный уровень. Сигнал давления масла в двигателе указывает, что давление масла в двигателе ниже предела предупреждения о защите двигателя. | Прогрессивная мощность ухудшается по степени тяжести с момента предупреждения. |

![[19202670.png]]

ISM - давление винтовки моторного масла 1

### Описание цепи

Электронный модуль управления (ECM) обеспечивает подачу 5 вольт на датчик давления масла двигателя по схеме SUPPLY 1. ECM также обеспечивает заземление на цепи возврата датчика. Датчик давления масла двигателя обеспечивает сигнал к ECM на цепи SIGNAL датчика давления масла двигателя. Этот датчик сигнала изменяет напряжение на основе давления в масляной винтовке. ECM будет обнаруживать низкое напряжение сигнала в рабочих условиях, когда давление масла может быть немного ниже. ECM будет обнаруживать высокое напряжение сигнала во время высоких оборотов двигателя или условий эксплуатации, когда температура масла низкая.

Если ECM обнаруживает низкое напряжение сигнала, указывающее на низкое давление масла в двигателе, этот код ошибки устанавливается.

### Расположение компонента

Датчик давления масла двигателя расположен на левой стороне блока двигателя. Используйте следующую процедуру для подробного просмотра местоположения компонента. См. процедуру 100-002 в разделе E.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда переключатель зажигания находится в положении Включения.

### Условия установки кодов неисправностей

ECM обнаруживает, что давление масла в двигателе составляет менее 55 кПа[8 psi] при 800 об/мин в течение более 5 секунд.

### Действия системы при активном коде неисправности

- ECM освещает янтарный свет CHECK ENGINE сразу же, когда диагностика проходит и не удается.

- Уменьшение крутящего момента производится ECM, ограничивающим выходную мощность двигателя.

### Условия сброса кода неисправности

ECM выключит янтарный CHECK ENGINE свет, и крутящий момент будет удален, когда будет обнаружено, что показания давления масла находятся в пределах нормального рабочего диапазона.

### Практические замечания

Проверить правильность калибровки электронного модуля управления (ECM). Проверьте историю калибровки, найденную на QuickServeTM Online, для применимых исправлений к калибровке, хранящейся в ECM. При необходимости откалибровать ECM.[[105-019-032 — Engine Control Module Calibration Code|См. процедуру 019-032 в разделе 19.]]

Этот код неисправности активируется, когда давление масла в двигателе падает ниже предела защиты двигателя. Устранение неисправностей двигателя при низком давлении масла.

См. Код устранения неполадок t05-143


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 143
>
> ### Engine Oil Rifle Pressure - Data Valid But Below Normal Operating Range - Moderately Severe Level
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 143 PID(P): P100 SPN: 100 FMI: 1/18 Lamp: Amber SRT: | Engine Oil Rifle Pressure - Data Valid but Below Normal Operating Range - Moderately Severe Level. Engine oil pressure signal indicates engine oil pressure is below the engine protection warning limit. | Progressive power derate increasing in severity from time of alert. |
>
> ISM - Engine Oil Rifle Pressure 1
>
> ### Circuit Description
>
> The electronic control module (ECM) provides a 5 volt supply to the engine oil pressure sensor on the sensor SUPPLY 1 circuit. The ECM also provides a ground on the sensor RETURN circuit. The engine oil pressure sensor provides a signal to the ECM on the engine oil pressure sensor SIGNAL circuit. This sensor signal voltage changes based on the pressure in the oil rifle. The ECM will detect a low signal voltage at operating conditions when the oil pressure may be slightly lower. The ECM will detect a high signal voltage during high engine speeds or operating conditions when the oil temperature is low.
>
> If the ECM detects low signal voltage indicating a low engine oil pressure, this fault code sets.
>
> ### Component Location
>
> The engine oil pressure sensor is located on the left side of the engine block. Use the following procedure for a detailed component location view. Refer to Procedure 100-002 in Section.E.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the keyswitch is in the ON position.
>
> ### Conditions For Setting The Fault Codes
>
> The ECM detects that the engine oil pressure is less than 55 kPa \[8 psi\] at 800 rpm for more than 5 seconds.
>
> ### Action Taken When The Fault Code Is Active
>
> - The ECM illuminates the amber CHECK ENGINE light immediately when the diagnostic runs and fails.
>
> - A torque derate is issued by the ECM limiting the power output of the engine.
>
> ### Conditions For Clearing The Fault Code
>
> The ECM will turn OFF the amber CHECK ENGINE light and the torque derate will be removed when the oil pressure reading is detected to be within the normal operating range.
>
> ### Shoptalk
>
> Verify the electronic control module (ECM) calibration is correct. Check the calibration revision history found on QuickServe™ Online for applicable fixes to the calibration stored in the ECM. If necessary, calibrate the ECM. [[105-019-032 — Engine Control Module Calibration Code|Refer to Procedure 019-032 in Section 19.]]
>
> This fault code goes active when the engine oil pressure drops below the engine protection limit. Troubleshoot the engine for low oil pressure.
>
> Refer to Troubleshooting Fault Code t05-143
