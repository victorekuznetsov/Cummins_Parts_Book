---
aliases:
  - "Предупреждение о внутреннем аппаратном отказе ЭБУ"
type: "Процедура"
doc: "60-fc343"
title_en: "Engine Control Module Warning Internal Hardware Failure - Bad Intelligent Device or Component"
title_ru: "Предупреждение о внутреннем аппаратном отказе ЭБУ"
modified: "2020-09-28"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc343.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc343.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Engine Control Module Warning Internal Hardware Failure - Bad Intelligent Device or Component
**Предупреждение о внутреннем аппаратном отказе ЭБУ**

> [!abstract] Процедура · `60-fc343`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc343.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc343.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 343

### Предупреждение о внутреннем аппаратном отказе ЭБУ

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 343 P(P): S254 SPN: 629 FMI: 12/12 Лампа: Янтарная СРТ: | Обнаружен внутренний сбой связи ECM. | Возможно снижение производительности двигателя. |

![[19a00867.png]]

Модуль управления двигателем (ECM)

### Описание цепи

Модуль управления двигателем (ECM) получает постоянное напряжение от батарей через непереключенные провода батареи, которые подключены непосредственно к положительному (+) посту батареи. ECM принимает вводимую аккумуляторную батарею через провод переключателя зажигания, когда переключатель зажигания включен.

### Расположение компонента

Модули управления двигателем (ECM) расположены на пластине, которая находится над корпусом маховика.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда контроллер генераторного набора активен.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил ошибку показаний или записи внутри ECM.

### Действия системы при активном коде неисправности

- Контроллер генераторной установки показывает предупреждение сразу, как только диагностика выявляет отказ.

### Условия сброса кода неисправности

- Чтобы проверить результат ремонта, запустите двигатель и дайте ему поработать 1 минуту без нагрузки.

- Контроллер генераторной установки гасит предупреждающий индикатор сразу после нажатия сброса.

- Для сброса активных неисправностей можно воспользоваться командой «Reset All Faults» в рекомендованной программе Cummins® или её аналоге.

### Практические замечания

Возможные причины этого кода неисправности:

- Внутренний сбой ECM.

См. Код 343 устранения неполадок.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 343
>
> ### Engine Control Module Warning Internal Hardware Failure - Bad Intelligent Device or Component
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 343 PID(P): S254 SPN: 629 FMI: 12/12 Lamp: Amber SRT: | An internal ECM communication failure has been detected. | Possible reduced engine performance. |
>
> Engine Control Module (ECM)
>
> ### Circuit Description
>
> The engine control module (ECM) receives constant voltage from the batteries through the unswitched battery wires that are connected directly to the positive (+) battery post. The ECM receives switched battery input through the keyswitch wire when the keyswitch is turned ON.
>
> ### Component Location
>
> The Engine Control Modules (ECM) are located on a plate that is above the flywheel housing.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the generator set controller is active.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected a read or write error internal to the ECM.
>
> ### Action Taken When The Fault Code Is Active
>
> - The generator set controller displays a warning fault immediately when the diagnostics runs and fails.
>
> ### Conditions For Clearing The Fault Code
>
> - To validate the repair, start the engine and let it run for 1 minute at no load.
>
> - The generator set controller will turn off the warning indicator immediately after the user presses reset.
>
> - The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.
>
> ### Shoptalk
>
> Possible causes of this fault code include:
>
> - Internal ECM failure.
>
> Refer to Troubleshooting Fault Code 343.
