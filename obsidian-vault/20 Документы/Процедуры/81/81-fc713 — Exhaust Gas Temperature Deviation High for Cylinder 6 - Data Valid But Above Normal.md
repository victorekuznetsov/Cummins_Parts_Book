---
type: "Процедура"
doc: "81-fc713"
title_en: "Exhaust Gas Temperature Deviation High for Cylinder 6 - Data Valid But Above Normal Operating Range - Moderately Severe Level"
modified: "2015-07-10"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
manuals:
  - "3666410"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-fc713.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-fc713.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/81"
  - "перевод/машинный"
---

# Exhaust Gas Temperature Deviation High for Cylinder 6 - Data Valid But Above Normal Operating Range - Moderately Severe Level

> [!abstract] Процедура · `81-fc713`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[3666410 — QSK45 and QSK60 CENSE™ Electronic Control System Troubleshooting and Repair Manual|3666410]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-07-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-fc713.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-fc713.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 713

### Отклонение температуры выхлопного газа для цилиндра 6 - данные действительны, но выше нормального диапазона - умеренно тяжелый уровень

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 713 P(P): СПН: 1328 FMI: 0/16 лампа: Янтарная СРТ: CE-713 | Отклонение температуры выхлопного газа для цилиндра 6 - данные действительны, но выше нормального рабочего диапазона - умеренно тяжелый уровень. Температура выхлопных газов цилиндра 6 выше нормального рабочего диапазона. | Никаких действий. |

![[19903744.png]]

Сенсор температуры выхлопных газов Цилиндр 6

### Описание цепи

Схема датчика температуры выхлопных газов контролирует температуру выхлопных газов для цилиндра 6 и передает информацию модулю управления двигателем CENSETM (ECM) через электропроводку двигателя. ECM контролирует температуру и сравнивает ее с температурой выхлопных газов других цилиндров.

### Расположение компонента

Датчик температуры выхлопных газов для цилиндра 6 расположен на интерфейсе коллектора головка-выхлоп.

### Практические замечания

Существует несколько ECM CENSETM для моделей двигателей, включенных в это руководство. Модель ECM отображается при подключении электронного инструментария обслуживания INSITETM. При устранении неисправности кода используйте модель ECM, отображаемую в инструменте электронного обслуживания INSITETM, чтобы определить, какой цилиндр затронут. Для двигателей с настоящим CM2330 ECM нумерация цилиндров описана в процедуре общего двигателя раздела V в руководстве по обслуживанию QSK45 и QSK60, бюллетень [[4021530 — QSK45 and QSK60 Service Manual\|4021530]].[[56-018-015-tr — General Engine|См. процедуру 018-015 в разделе V.]]

См. Код устранения неполадок t05-713


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 713
>
> ### Exhaust Gas Temperature Deviation High for Cylinder 6 - Data Valid But Above Normal Operating Range - Moderately Severe Level
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 713 PID(P): SPN: 1328 FMI: 0/16 Lamp: Amber SRT: CE-713 | Exhaust Gas Temperature Deviation High for Cylinder 6 - Data Valid But Above Normal Operating Range - Moderately Severe Level. Cylinder 6 exhaust temperature is above the normal operating range. | No action taken. |
>
> Exhaust Gas Temperature Sensor Circuit Cylinder 6
>
> ### Circuit Description
>
> The exhaust gas temperature sensor circuit monitors exhaust gas temperature for cylinder 6 and passes the information to the CENSE™ engine control module (ECM) through the engine harness. The ECM monitors the temperature and compares it to the exhaust gas temperatures of other cylinders.
>
> ### Component Location
>
> The exhaust gas temperature sensor for cylinder 6 is located at the cylinder head-to-exhaust manifold interface.
>
> ### Shoptalk
>
> There are multiple CENSE™ ECMs for the engine models included in this manual. The ECM model displays when INSITE™ electronic service tool is connected. When troubleshooting a fault code, use the ECM model displayed in INSITE™ electronic service tool to determine which cylinder is affected. For engines with the present CM2330 ECM, the cylinder numbering sequence is described in the General Engine procedure of Section V in the QSK45 and QSK60 Service Manual, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. [[56-018-015-tr — General Engine|Refer to Procedure 018-015 in Section V.]]
>
> Refer to Troubleshooting Fault Code t05-713
