---
type: "Процедура"
doc: "81-fc635"
title_en: "Exhaust Gas Temperature Deviation Low for Cylinder 10 - Data Valid But Below Normal Operating Range - Least Severe Level"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-fc635.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-fc635.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/81"
  - "перевод/машинный"
---

# Exhaust Gas Temperature Deviation Low for Cylinder 10 - Data Valid But Below Normal Operating Range - Least Severe Level

> [!abstract] Процедура · `81-fc635`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[3666410 — QSK45 and QSK60 CENSE™ Electronic Control System Troubleshooting and Repair Manual|3666410]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-07-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-fc635.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-fc635.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 635

### Отклонение температуры выхлопных газов от низкого для цилиндра 10 - данные действительны, но ниже нормального диапазона работы - наименее тяжелый уровень

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 635 PID(P): СПН: 1332 FMI: 0/17 Лампа: Обслуживание SRT: | Отклонение температуры выхлопного газа для цилиндра 10 - данные действительны, но ниже нормального рабочего диапазона - наименее тяжелый уровень. | Возможно, низкая мощность. Отсутствие защиты двигателя от температуры выхлопных газов. |

![[19903748.png]]

Цилиндр выхлопных газовых датчиков 10 - двигатели QSK45 и QSK60

### Описание цепи

Цилиндр 10 схемы датчика температуры выхлопных газов контролирует температуру выхлопных газов и передает информацию модулю управления двигателем (ECM) через электропроводку двигателя.

### Расположение компонента

Цилиндр 10 схемы датчика температуры выхлопных газов для этого кода неисправности расположен в выпускном коллекторе на головке 10 цилиндра для интерфейса выпускного коллектора.

### Практические замечания

Существует несколько ECM CENSETM для моделей двигателей, включенных в это руководство. Модель ECM отображается при подключении электронного инструментария обслуживания INSITETM. При устранении неисправности кода используйте модель ECM, отображаемую в инструменте электронного обслуживания INSITETM, чтобы определить, какой цилиндр затронут. Для двигателей с настоящим CM2330 ECM нумерация цилиндров описана в процедуре общего двигателя раздела V в руководстве по обслуживанию QSK45 и QSK60, бюллетень [[4021530 — QSK45 and QSK60 Service Manual\|4021530]].[[56-018-015-tr — General Engine|См. процедуру 018-015 в разделе V.]]

Цилиндр 10 схемы датчика температуры выхлопных газов измеряет температуру выхлопных газов цилиндра 10. ECM контролирует температуру и сравнивает ее с температурой выхлопных газов других цилиндров.

Возможно, что датчик температуры выхлопных газов 5 вольт питания может быть открыт и неисправность будет установлена. Если это произойдет, температура датчика температуры выхлопных газов будет считываться 474 ° C \[885 ° F \] для всего банка датчиков, подключенных к этому преобразователю датчика температуры выхлопных газов. См. раздел TT Руководства по обслуживанию QSK45 и QSK60, Бюллетень [[4021530 — QSK45 and QSK60 Service Manual\|4021530]], чтобы устранить это состояние.

Возможные причины этой ошибки включают:

- Ограниченный послеохладитель.

- Повреждение клапанов, колец или поршня.

- Повреждение форсунки.

См. Код устранения неполадок t05-635.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 635
>
> ### Exhaust Gas Temperature Deviation Low for Cylinder 10 - Data Valid But Below Normal Operating Range - Least Severe Level
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 635 PID(P): SPN: 1332 FMI: 0/17 Lamp: Maintenance SRT: | Exhaust Gas Temperature Deviation Low for Cylinder 10 - Data Valid But Below Normal Operating Range - Least Severe Level. | Possible low power. No engine protection for exhaust gas temperature. |
>
> Exhaust Gas Temperature Sensor Circuit Cylinder 10 - QSK45 and QSK60 Engines
>
> ### Circuit Description
>
> The exhaust gas temperature sensor circuit cylinder 10 monitors exhaust gas temperature and passes information to the engine control module (ECM) through the engine harness.
>
> ### Component Location
>
> The exhaust gas temperature sensor circuit cylinder 10 for this fault code is located in the exhaust manifold at the cylinder head 10 to exhaust manifold interface.
>
> ### Shoptalk
>
> There are multiple CENSE™ ECMs for the engine models included in this manual. The ECM model displays when INSITE™ electronic service tool is connected. When troubleshooting a fault code, use the ECM model displayed in INSITE™ electronic service tool to determine which cylinder is affected. For engines with the present CM2330 ECM, the cylinder numbering sequence is described in the General Engine procedure of Section V in the QSK45 and QSK60 Service Manual, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. [[56-018-015-tr — General Engine|Refer to Procedure 018-015 in Section V.]]
>
> The exhaust gas temperature sensor circuit cylinder 10 measures the exhaust temperature of cylinder 10. The ECM monitors the temperature and compares it to the exhaust gas temperatures of other cylinders.
>
> It is possible that the exhaust gas temperature sensor 5 volt supply can be open and a fault will **not** be set. If this happens, the temperature of the exhaust gas temperature sensor will read 474°C \[885°F\] for the entire bank of sensors connected to that exhaust gas temperature sensor converter. See the Engine Performance Troubleshooting Tree in Section TT of the QSK45 and QSK60 Service Manual, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]], to troubleshoot this condition.
>
> Possible causes of this fault include:
>
> - Restricted aftercooler.
>
> - Damage valves, rings, or piston.
>
> - Injector damage.
>
> Refer to Troubleshooting Fault Code t05-635.
