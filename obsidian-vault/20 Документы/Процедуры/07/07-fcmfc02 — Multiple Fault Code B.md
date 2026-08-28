---
aliases:
  - "Множественный код неисправности B"
type: "Процедура"
doc: "07-fcmfc02"
title_en: "Multiple Fault Code B"
title_ru: "Множественный код неисправности B"
modified: "2012-12-18"
engines:
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "4021442"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fcmfc02.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-fcmfc02.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
  - "перевод/машинный"
---

# Multiple Fault Code B
**Множественный код неисправности B**

> [!abstract] Процедура · `07-fcmfc02`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-12-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fcmfc02.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-fcmfc02.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: B

### Множественный код неисправности B

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: B PID(P): СПН: ФМИ: Лампа: СТО: | Несколько кодов неисправностей генерируются из-за общего отказа провода питания или возврата в ремне электропроводки двигателя. | Коды 123 и 141 ошибки активны. |

![[19900397.png]]

Электронный модуль управления (ECM)

### Описание цепи

Электронный модуль управления (ECM) поставляет все датчики давления двигателя на ремне электропроводки двигателя с +5 VDC. ECM имеет общую отдачу для всех датчиков давления и температуры двигателя. Ссылка на схему проводов, Bulletin 4021331, для пин-кодов этих схем. Неисправность в любой из этих схем вызывает несколько кодов неисправностей.

### Расположение компонента

Справочный раздел E для подробного описания местоположения компонента. ECM расположен в верхней части двигателя, смонтированный на коллектор воздухозаборника.

### Практические замечания

Открытая цепь в общих проводах питания и возврата, короткие замыкания от батареи или земли до подачи или дефектный источник питания ECM могут вызвать несколько кодов неисправностей.

Неисправный датчик давления может вызвать несколько кодов неисправностей.

Неисправный датчик давления может привести к тому, что несколько активных кодов неисправностей будут неактивны после запуска двигателя.

См. код устранения неисправностей t05-mfc02


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: B
>
> ### Multiple Fault Code B
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: B PID(P): SPN: FMI: Lamp: SRT: | Multiple fault codes are generated due to a common supply or return wire failure in the engine harness. | Fault Codes 123 and 141 are active. |
>
> Electronic Control Module (ECM)
>
> ### Circuit Description
>
> The electronic control module (ECM) supplies all engine pressure sensors on the engine harness with +5 VDC. The ECM has common returns for all the engine pressure and temperature sensors. Reference the wiring diagram, Bulletin 4021331, for the pin assignments of these circuits. A failure on either of these circuits causes multiple fault codes.
>
> ### Component Location
>
> Reference Section E for a detailed component location view. The ECM is located at the top of the engine, mounted to the air intake manifold.
>
> ### Shoptalk
>
> An open circuit in the common supply and return wires, short circuits from battery or ground to the supply, or a defective ECM power supply can cause multiple fault codes.
>
> A failed pressure sensor can cause multiple fault codes.
>
> A failed pressure sensor can cause multiple active fault codes to go inactive once the engine has been started.
>
> Refer to Troubleshooting Fault Code t05-mfc02
