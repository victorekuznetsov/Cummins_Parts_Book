---
aliases:
  - "Низкий уровень топлива в расходном баке"
type: "Процедура"
doc: "01-fc1439"
title_en: "Fuel Level Low in Day Tank"
title_ru: "Низкий уровень топлива в расходном баке"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1439.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1439.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Fuel Level Low in Day Tank
**Низкий уровень топлива в расходном баке**

> [!abstract] Процедура · `01-fc1439`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1439.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1439.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1439

### Низкий уровень топлива в расходном баке

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1439 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Низкий уровень топлива в расходном баке. | Никаких действий со стороны ЕКМ не предпринимается. Возможная потеря производительности. |

![[19802815.png]]

Дневной сенсор уровня бака топлива

### Описание цепи

Датчик уровня топлива контролирует уровень топлива в дневном баке и передает информацию в электронный модуль управления (ECM).

### Расположение компонента

См. документацию о местоположении бака для топливного дня и датчик уровня топлива, используемый в баке для дневного использования.

### Практические замечания

Когда уровень топлива падает ниже определенного уровня в баке, это может привести к тому, что топливный насос будет работать усерднее, чтобы получить желаемое давление топлива.

Если в схеме уровня топлива используется шортинг, убедитесь, что он правильно подключен.

Проверьте все разъемы и сенсорные штифты на предмет повреждения.

См. Код устранения неисправностей t05-1439


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1439
>
> ### Fuel Level Low in Day Tank
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1439 PID(P): SPN: FMI: Lamp: Warning SRT: | Fuel level low in day tank. | No action is taken by the ECM. Possible loss of performance. |
>
> Day Tank Fuel Level Sensor Circuit
>
> ### Circuit Description
>
> The fuel level sensor monitors the fuel level within the day tank and passes information to the electronic control module (ECM).
>
> ### Component Location
>
> Refer to customer/facility/installation documentation for the location of the fuel day tank and the fuel level sensor used on the day tank.
>
> ### Shoptalk
>
> When the fuel level drops below a certain level in the tank, it could cause the fuel pump to work harder to obtain the desired fuel pressure.
>
> If a shorting plug is used in the fuel level circuit, verify that it is wired correctly.
>
> Inspect all connectors and the sensor pins for damage.
>
> Refer to Troubleshooting Fault Code t05-1439
