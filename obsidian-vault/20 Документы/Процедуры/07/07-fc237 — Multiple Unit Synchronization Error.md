---
aliases:
  - "Ошибка синхронизации нескольких агрегатов"
type: "Процедура"
doc: "07-fc237"
title_en: "Multiple Unit Synchronization Error"
title_ru: "Ошибка синхронизации нескольких агрегатов"
modified: "2012-12-18"
engines:
  - "93058669"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "4021442"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc237.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/07-fc237.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
  - "перевод/машинный"
---

# Multiple Unit Synchronization Error
**Ошибка синхронизации нескольких агрегатов**

> [!abstract] Процедура · `07-fc237`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-12-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc237.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/07-fc237.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 237

### Ошибка синхронизации нескольких агрегатов

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 237 P(P): S30 SPN: 644 FMI: 2 лампы: Янтарная СРТ: | Внешний ввод скорости (многократная синхронизация единиц) - данные неустойчивые, прерывистые или неправильные. | Двигатели ** не** могут управляться одним входом дроссельной заслонки. Вторичный двигатель ** должен управляться отдельно через вход дроссельной заслонки. |

![[19901353.png]]

Многодиапазонный синхронизирующий контур

### Описание цепи

Основной двигатель выдает сигнал дроссельной заслонки вторичному двигателю через соединение J1939. Это активируется закрытием переключателя. Этот сигнал интерпретируется вторичным двигателем и используется в качестве входного сигнала дроссельной заслонки вторичным двигателем.

### Расположение компонента

** Не применяется.

### Практические замечания

Вторичный двигатель ожидает, что сигнал дроссельной заслонки будет передаваться от основного двигателя через шину данных J1939 CAN. Неисправный сигнал будет генерировать код 237 ошибки во вторичном двигателе.

Код 237 неисправности может возникать, когда вторичный переключатель зажигания включен, а первичный переключатель зажигания отключен. Это также может произойти, когда в проводах есть открытая схема, которая соединяет сигнал J1939 от первичного до вторичного двигателя. На приведенной выше диаграмме показаны схема и путь потока данных.

- Проверьте, что несколько единиц синхронизации прыгунов на месте.

- ****************************************************************************************************************************************************************************************************************************************************************

- Проверьте, что оба ключа включены.

- Переключите переключатель синхронизации, чтобы определить, активна ли ошибка и неактивна ли она.

Убедитесь, что шина данных SAE J1939 CAN активна и правильно взаимодействует с инструментами электронного обслуживания INSITETM на всех двигателях.[[00-022-999 — Service Tools and Hardware - Overview|Если какой-либо ECM не будет сообщаться через шину данных SAE J1939 CAN, следуйте процедуре 022-999 (Service Tools and Hardware - Overview) в разделе F.]]

См. Код устранения неполадок t05-237


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 237
>
> ### Multiple Unit Synchronization Error
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 237 PID(P): S30 SPN: 644 FMI: 2 Lamp: Amber SRT: | External speed input (multiple unit synchronization) - data erratic, intermittent, or incorrect. | Engines will **not** be able to be controlled with one throttle input. The secondary engine **must** be controlled separately via its throttle input. |
>
> Multiple Unit Synchronization Circuit
>
> ### Circuit Description
>
> The primary engine outputs a throttle signal to the secondary engine via the J1939 interconnect. This is activated by a switch closure. This signal is interpreted by the secondary engine and is used as the throttle signal input by the secondary engine.
>
> ### Component Location
>
> **Not** applicable.
>
> ### Shoptalk
>
> The secondary engine expects a throttle signal to be transmitted from the primary engine via the J1939 datalink. A faulty signal will generate Fault Code 237 in the secondary engine.
>
> Fault Code 237 can occur when the secondary keyswitch is ON and the primary keyswitch is OFF. It can also occur when there is an open circuit in the wires that connect the J1939 signal from the primary to the secondary engine. The diagram above illustrates the circuit and the data flow path.
>
> - Verify the multiple unit synchronization jumpers are in place.
>
> - Verify there is **only** one primary jumper and one secondary jumper.
>
> - Verify both keyswitches are ON.
>
> - Toggle the synchronization switch to determine if the fault goes active and inactive.
>
> Verify that the SAE J1939 datalink is active and communicates correctly with INSITE™ electronic service tool on all engines. [[00-022-999 — Service Tools and Hardware - Overview|Refer to Procedure If any ECM will not communicate over the SAE J1939 datalink, follow Procedure 022-999 (Service Tools and Hardware - Overview) in Section F.]]
>
> Refer to Troubleshooting Fault Code t05-237
