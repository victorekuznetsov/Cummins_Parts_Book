---
aliases:
  - "Цепь потенциометра регулировки усиления"
type: "Процедура"
doc: "01-fc1418"
title_en: "Gain Adjust Potentiometer Circuit"
title_ru: "Цепь потенциометра регулировки усиления"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1418.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1418.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Gain Adjust Potentiometer Circuit
**Цепь потенциометра регулировки усиления**

> [!abstract] Процедура · `01-fc1418`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1418.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1418.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1418

### Цепь потенциометра регулировки усиления

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1418 P(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Сигнал потенциометра с регулировкой нарастания закорочен высоко. | Функция корректировки усиления будет отключена, и будет использоваться значение нуля по умолчанию. Возможная потеря производительности. |

![[19802448.png]]

Цепь потенциометра регулировки усиления

### Описание цепи

Потенциометр с регулировкой усиления позволяет оператору регулировать усиление разницы в значении между «желательной скоростью» и «фактической скоростью» двигателя, чтобы управляющий мог реагировать на колебания скорости двигателя. Разница между «желательной скоростью» и «фактической скоростью» называется сигналом ошибки. При увеличении усиления сигнала ошибки усиливается, губернатором предпринимаются более корректирующие действия, а его ответ — более быстрый. При уменьшении усиления сигнала ошибки уменьшается усиление, губернатором предпринимаются менее корректирующие действия, а его ответ медленнее. Если коэффициент усиления установлен слишком высоко, то регулятор может перекорректировать сигнал ошибки скорости, что приведет к увеличению скорости двигателя или «охоте». ECM контролирует напряжение и ожидает увидеть, что напряжение изменяется в диапазоне от 0,5 до 4,5 вольт во время нормальной работы. Высокое напряжение будет сбивать Код 1418 поломки и может быть вызвано шортами в сигнальном проводе, открытым в обратном проводе или неисправным потенциометром.

### Расположение компонента

См. руководство OEM для определения местоположения.

### Практические замечания

Потенциометры очень чувствительны к окружающей среде. Очистите потенциометр и проверьте его сопротивление в первую очередь.

См. Код устранения неисправностей t05-1418


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1418
>
> ### Gain Adjust Potentiometer Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1418 PID(P): SPN: FMI: Lamp: Warning SRT: | Gain adjust potentiometer signal is shorted high. | The gain adjustment feature will be disabled, and a default value of zero will be used. Possible loss of performance. |
>
> Gain Adjust Potentiometer Circuit
>
> ### Circuit Description
>
> The gain adjust potentiometer is so the operator can adjust the amplification of the difference in the value between the “desired speed” and the “actual speed” of the engine, so that the governor can respond to engine speed fluctuations. The difference between the “desired speed” and the “actual speed” is called the error signal. When the gain is increased, the error signal amplification is increased, more corrective action is taken by the governor, and its response is quicker. When the gain is reduced, the error signal amplification is reduced, less corrective action is taken by the governor, and its response is slower. If the gain is set too high, the governor can overcorrect the speed error signal, which will lead to engine speed surging or “hunting.” The ECM monitors the voltage and expects to see the voltage vary between 0.5 and 4.5 volts during normal operation. High voltage will trip Fault Code 1418 and can be caused by shorts in the signal wire, an open in the return wire, or a failed potentiometer.
>
> ### Component Location
>
> Refer to the OEM manual for location.
>
> ### Shoptalk
>
> Potentiometers are very sensitive to the environment. Clean the potentiometer, and check its resistance first.
>
> Refer to Troubleshooting Fault Code t05-1418
