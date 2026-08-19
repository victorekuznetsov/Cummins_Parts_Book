---
aliases:
  - "Цепь входа реле стартера ICON™"
type: "Процедура"
doc: "82-fc541"
title_en: "ICON™ Starter Relay Input Circuit"
title_ru: "Цепь входа реле стартера ICON™"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc541.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc541.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# ICON™ Starter Relay Input Circuit
**Цепь входа реле стартера ICON™**

> [!abstract] Процедура · `82-fc541`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc541.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc541.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 541

### Цепь входа реле стартера ICON™

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 541 PID(P): S123 SPN: 615 FMI: 11/31 лампа: Желтая СТО: | Неправильное напряжение, обнаруженное в схеме ввода реле стартера ICONTM ECM. | Система ICONTM будет отключена. Обязательная остановка все еще может быть включена. Двигатель можно запускать нормально. |

![[19803219.png]]

ICONTM Starter-ретранслятор / Interlock-схема

### Описание цепи

Неправильное напряжение, обнаруженное в цепи реле стартера ICONTM ECM.

### Расположение компонента

Стартерная реле ICONTM расположена на стенке огня на стороне транспортного средства рядом с реле стартера транспортного средства.

### Практические замечания

Эта неисправность указывает на короткое замыкание к батарее / земле или открытой схеме реле стартера ICONTM. Все переключатели блокировки ** должны быть закрыты, а лампа ICONTM ** должна быть функциональной до того, как система ICONTM сможет работать, пока ICONTM активен. Эти схемы применяются только тогда, когда включена ICONTM.

Устранение неполадок код t05-541


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 541
>
> ### ICON™ Starter Relay Input Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 541 PID(P): S123 SPN: 615 FMI: 11/31 Lamp: Yellow SRT: | Incorrect voltage detected at the ICON™ starter relay input circuit by the ECM. | The ICON™ system will be disabled. Mandatory shutdown can still be enabled. Engine can be started normally. |
>
> ICON™ Starter Relay/Interlock Circuit
>
> ### Circuit Description
>
> Incorrect voltage detected at the ICON™ starter relay circuit by the ECM.
>
> ### Component Location
>
> The ICON™ starter relay is located on the vehicle-side fire wall near the vehicle starter relay.
>
> ### Shoptalk
>
> This fault indicates a short circuit to battery/ground or an open ICON™ starter relay circuit. All interlock switches **must** be closed and the ICON™ lamp **must** be functional before the ICON™ system can be enabled for the engine to run while ICON™ is active. These circuits apply **only** when ICON™ is enabled.
>
> Refer to Troubleshooting Fault Code t05-541
