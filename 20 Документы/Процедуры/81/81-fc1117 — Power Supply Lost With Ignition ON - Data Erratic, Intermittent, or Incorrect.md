---
type: "Процедура"
doc: "81-fc1117"
title_en: "Power Supply Lost With Ignition ON - Data Erratic, Intermittent, or Incorrect"
modified: "2015-08-12"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-fc1117.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-fc1117.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/81"
  - "перевод/машинный"
---

# Power Supply Lost With Ignition ON - Data Erratic, Intermittent, or Incorrect

> [!abstract] Процедура · `81-fc1117`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[3666410 — QSK45 and QSK60 CENSE™ Electronic Control System Troubleshooting and Repair Manual|3666410]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-08-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-fc1117.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-fc1117.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1117

### Потеря питания при включённом зажигании — данные нестабильны или неверны

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1117 PID(P): S251 SPN: 627 FMI: 2/2 лампы: Нет, не srt: | Потеря питания при включённом зажигании — данные нестабильны или неверны. ECM не позволял правильно питать (сохранять напряжение батареи в течение 30 секунд после выключения ключа). | Двигатель может затормозить. |

![[19903736.png]]

Схема электроснабжения

### Описание цепи

Модуль управления двигателем (ECM) получает постоянное напряжение от батарей через силовые провода ECM, которые соединены через провода оригинального производителя оборудования (OEM). В электропроводке OEM есть предохранитель 30 ампер, чтобы защитить электропроводку от перегрева. ECM принимает вводимую аккумуляторную батарею через ввод выключателя зажигания, когда зажигание включено. Провода возврата ECM и встроенного модуля также соединены через проводную упряжку OEM.

### Расположение компонента

ECM подключается к батарее с помощью OEM-проводов электропроводки через заглушку питания батареи ECM. Это обеспечивает постоянный источник питания для ECM. Расположение батареи будет варьироваться в зависимости от OEM. См. информацию об услугах производителя оборудования.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда двигатель работает.

### Условия установки кодов неисправностей

ECM был не в состоянии правильно завершить режим выключения питания после выключения переключателя зажигания.

### Действия системы при активном коде неисправности

ECM будет **не** иметь возможность хранить обновления для параметров питания, таких как выборочные комплектации для клиентов или таблицы топливной системы.

### Условия сброса кода неисправности

Чтобы проверить ремонт, запустите двигатель и запустите его на холостом ходу в течение 1 минуты.

- Состояние кода неисправности станет неактивным сразу после того, как ECM исправно отключится.

- Код неисправности также может быть очищен с помощью электронного инструментария обслуживания INSITETM.

### Практические замечания

Если выключатель отключения батареи выключен после выключения выключателя зажигания, но до того, как ECM полностью выключится (до 30 секунд), этот код неисправности может зарегистрироваться.

См. код 1117 устранения неполадок.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1117
>
> ### Power Supply Lost With Ignition ON - Data Erratic, Intermittent, or Incorrect
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1117 PID(P): S251 SPN: 627 FMI: 2/2 Lamp: None SRT: | Power Supply Lost With Ignition ON - Data Erratic, Intermittent, or Incorrect. The ECM was **not** allowed to power down correctly (retain battery voltage for 30 seconds after key OFF). | Engine could possibly stall. |
>
> Power Supply Circuit
>
> ### Circuit Description
>
> The engine control module (ECM) receives constant voltage from the batteries through the ECM power wires that are connected through the original equipment manufacturer (OEM) harness. There is a 30 ampere fuse in the OEM harness to protect the harness from overheating. The ECM receives switched battery input through the keyswitch input when the ignition is turned ON. The ECM and inline module return wires are also connected through the OEM harness.
>
> ### Component Location
>
> The ECM is connected to the battery by the OEM power harness through the ECM battery supply stub. This provides a constant power supply for the ECM. The location of the battery will vary with the OEM. Refer to the equipment manufacturer service information.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the engine is running.
>
> ### Conditions For Setting The Fault Codes
>
> The ECM was **not** able to complete the power down routine correctly after keyswitch was turned OFF.
>
> ### Action Taken When The Fault Code Is Active
>
> The ECM will **not** be able to store updates to power down parameters such as customer selectable trims or fuel system tables.
>
> ### Conditions For Clearing The Fault Code
>
> To validate the repair, start the engine and let it idle for 1 minute.
>
> - The fault code state will become inactive immediately after the ECM has properly powered down.
>
> - The fault code can also be cleared with INSITE™ electronic service tool.
>
> ### Shoptalk
>
> If a battery disconnect switch is turned OFF after the keyswitch is turned OFF, but before the ECM completely powers down (up to 30 seconds), this fault code can register.
>
> Refer to Troubleshooting Fault Code 1117.
