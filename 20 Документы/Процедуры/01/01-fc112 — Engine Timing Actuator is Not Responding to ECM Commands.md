---
aliases:
  - "Привод опережения не отвечает на команды ЭБУ"
type: "Процедура"
doc: "01-fc112"
title_en: "Engine Timing Actuator is Not Responding to ECM Commands"
title_ru: "Привод опережения не отвечает на команды ЭБУ"
modified: "2011-10-03"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc112.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc112.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Engine Timing Actuator is Not Responding to ECM Commands
**Привод опережения не отвечает на команды ЭБУ**

> [!abstract] Процедура · `01-fc112`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-10-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc112.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc112.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 112

### Привод опережения не отвечает на команды ЭБУ

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 112 PID(P): СПН: ФМИ: Лампа: Отключение SRT: | Привод опережения не отвечает на команды ЭБУ. Погрешность между расчетным временем заправки топливом и желаемым временем заправки находится за пределами допустимых пределов. | Зависимое от калибровки отключение двигателя или отсутствие действий со стороны ECM. |

![[19400781.png]]

Схема расхода топлива

### Описание цепи

ECM использует сигнал давления времени и скорость двигателя для оценки фактического времени приема двигателя, а затем постоянно сравнивает это значение с желаемым временем для заданной скорости и нагрузки. Когда ошибка в этих значениях слишком велика слишком долго, код 112 ошибки регистрируется.

### Расположение компонента

Приводы рельсов расположены с левой стороны к вершине ECVA.

### Практические замечания

Расчетные сроки заправки топливом и желаемые параметры заправки топливом могут контролироваться на электронном сервисном оборудовании. Эта неисправность является проверкой контроля ECM за приводом рельсового привода и последующим потоком топлива. Если требуемое время заправки топливом может быть выполнено **не**, если требуется больше тока для привода или если требуемое время заправки топливом превышено и может **не** быть уменьшено путем уменьшения тока для привода, код 112 по умолчанию регистрируется.

- Код 112 не будет активирован, если активен код 116 или 117.

- После того, как переключатель запуска/остановки работает циклично, код 112 ошибки становится неактивным.

Выполните шаги по устранению неполадок, прежде чем заменить привод. Этот код неисправности обычно вызван:

- Воздух в топливной системе

- Внешний источник питания на проводах жгутовой проводов (батарейное зарядное устройство)

- Неисправность привода рельсов.

Устранение неполадок код t05-112


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 112
>
> ### Engine Timing Actuator is Not Responding to ECM Commands
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 112 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Engine Timing Actuator is Not Responding to ECM Commands. The error between the estimated timing fueling and the desired timing fueling is outside the allowable limits. | Calibration-dependent engine shutdown or no action is taken by ECM. |
>
> Fuel System Flow Schematic
>
> ### Circuit Description
>
> The ECM uses the timing pressure signal and engine speed to estimate the actual timing the engine is receiving and then constantly compares this value to the desired timing for the given speed and load. When the error in these values is too large for too long, Fault Code 112 is logged.
>
> ### Component Location
>
> The timing rail actuators are located at the left side toward the top of the ECVA.
>
> ### Shoptalk
>
> The estimated timing fueling and the desired timing fueling parameters can be monitored on the electronic service tool. This fault is a check on the ECM's control of the timing rail actuator and subsequent fuel flow. If the desired timing fueling can **not** be met by commanding more current to the actuator or if the desired timing fueling is being exceeded and can **not** be reduced by reducing the current to the actuator, Fault Code 112 is logged.
>
> - Fault Code 112 will not be triggered if Fault Code 116 or 117 is active
>
> - Once the run/stop switch is cycled, Fault Code 112 becomes inactive.
>
> Follow the troubleshooting steps before replacing the actuator. This fault code is commonly caused by:
>
> - Air in the fuel system
>
> - External power source on harness wiring (battery charger)
>
> - Timing rail actuator malfunction.
>
> Refer to Troubleshooting Fault Code t05-112
