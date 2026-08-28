---
type: "Процедура"
doc: "19-fc223"
title_en: "Burn Valve Solenoid Circuit"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc223.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc223.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Burn Valve Solenoid Circuit

> [!abstract] Процедура · `19-fc223`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc223.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc223.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 223

### Сжигать соленоидную цепь клапан

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 223 PID(P): S85 SPN: 1265 FMI: 4 лампы: Желтая СТО: | Схема соленоида горящего клапана CentinelTM открыта или коротковата. Менее 18,0 VDC, обнаруженных на контакте 8 подачи соленоидов с горящим клапаном CentinelTM, с проводкой OEM-интерфейса или сопротивлением соленоида упало ниже 80 Ом. | ECM отключает напряжение питания горящего клапана, и система CentinelTM отключена. |

![[19400727.png]]

Сжигать соленоидную цепь клапан

### Описание цепи

Соленоид горящего клапана контролирует поток масла в клапане управления маслом во время цикла горения.

### Расположение компонента

Сольноид горящего клапана расположен поверх клапана управления маслом.

См. Код устранения неполадок t05-223


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 223
>
> ### Burn Valve Solenoid Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 223 PID(P): S85 SPN: 1265 FMI: 4 Lamp: Yellow SRT: | The Centinel™ burn valve solenoid circuit is open or shorted. Less than 18.0 VDC detected at the Centinel™ burn valve solenoid supply pin 8 of the OEM interface harness or resistance of the solenoid has dropped below 80 ohms. | ECM turns off the burn valve supply voltage and the Centinel™ system is disabled. |
>
> Burn Valve Solenoid Circuit
>
> ### Circuit Description
>
> The burn valve solenoid controls the flow of oil in the oil control valve during the burn cycle.
>
> ### Component Location
>
> The burn valve solenoid is located on top of the oil control valve.
>
> Refer to Troubleshooting Fault Code t05-223
