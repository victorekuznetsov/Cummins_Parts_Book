---
aliases:
  - "Цепь подтверждения холостого хода"
type: "Процедура"
doc: "19-fc551"
title_en: "Idle Validation Circuit"
title_ru: "Цепь подтверждения холостого хода"
modified: "2011-03-01"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc551.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc551.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Idle Validation Circuit
**Цепь подтверждения холостого хода**

> [!abstract] Процедура · `19-fc551`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc551.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc551.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 551

### Цепь подтверждения холостого хода

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 551 PID(P): P91 SPN: 091 ФМИ: 4 лампы: Красная СТО: 00-675 | Нет напряжения, обнаруженного одновременно как на контактах 12 и 13 проводов OEM-интерфейса, так и на контактах бездействия и бездействия. | Двигатель будет по умолчанию до 0-процентного ускорителя. |

![[19400175.png]]

Цепь подтверждения холостого хода

### Описание цепи

Сигнал неработающей проверки является функцией безопасности, которая отключает педаль акселератора или рычаг управления, в то время как неправильный сигнал проверки обнаруживается ECM. Переключатель проверки бездействия обеспечивает сигналы проверки на холостом ходу и вне холостого хода для ECM через OEM-проводник и OEM-интерфейс.

### Расположение компонента

Расположение педали или рычага ускорителя варьируется в зависимости от каждого OEM. См. руководство по OEM.

### Практические замечания

Этот код неисправности обычно вызван неправильной проводкой жгутов проводов и холостым валидационным переключателем.

Примечание: Если педаль акселератора или датчик положения рычага изменены или после калибровочной загрузки, цикл педали акселератора или рычага (переключатель зажигания поворота) через его полное путешествие три раза. Эта процедура калибрует новую педаль акселератора или рычаг с помощью ECM.

См. Код устранения неполадок t05-551


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 551
>
> ### Idle Validation Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 551 PID(P): P91 SPN: 091 FMI: 4 Lamp: Red SRT: 00-675 | No voltage detected simultaneously on both the idle validation off-idle and idle signal pins 12 and 13 of the OEM interface harness. | Engine will default to 0-percent accelerator. |
>
> Idle Validation Circuit
>
> ### Circuit Description
>
> The idle validation signal is a safety feature that disables accelerator pedal or lever control while an improper validation signal is detected by the ECM. The idle validation switch provides on-idle and off-idle validation signals to the ECM through the OEM harness and OEM interface harness.
>
> ### Component Location
>
> The accelerator pedal or lever location varies with each OEM. Refer to the OEM manual.
>
> ### Shoptalk
>
> This fault code is usually caused by the improper wiring of the harnesses and idle validation switch.
>
> Note: If the accelerator pedal or lever position sensor is changed or after a calibration download, cycle the accelerator pedal or lever (turn keyswitch ON) through its complete travel three times. This procedure calibrates the new accelerator pedal or lever with the ECM.
>
> Refer to Troubleshooting Fault Code t05-551
