---
type: "Процедура"
doc: "19-fc225"
title_en: "Make-Up Valve Solenoid Circuit"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc225.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc225.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Make-Up Valve Solenoid Circuit

> [!abstract] Процедура · `19-fc225`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc225.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc225.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 225

### Соленоидная схема клапан Solenoid Circuit

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 225 P(P): S85 SPN: 1266 FMI: 4 лампы: Желтая СТО: | Магазинный клапан CentinelTM соленоидный контур открыт или коротковат. Менее 18,0 VDC, обнаруженный в соленоидном контакте 2 подачи соленоида в макияжном клапане CentinelTM, с жгутом проводов двигателя или сопротивлением соленоида упало ниже 80 Ом. | ECM отключает напряжение питания клапана для макияжа CentinelTM, а система CentinelTM отключена. |

![[19400728.png]]

Соленоидная схема клапан Solenoid Circuit

### Описание цепи

Соленоид макияжного клапана контролирует поток масла в клапане управления маслом во время цикла макияжа.

### Расположение компонента

Соленоид макияжного клапана расположен поверх клапана управления маслом.

См. Код устранения неполадок t05-225


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 225
>
> ### Make-Up Valve Solenoid Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 225 PID(P): S85 SPN: 1266 FMI: 4 Lamp: Yellow SRT: | The Centinel™ make-up valve solenoid circuit is open or shorted. Less than 18.0 VDC detected at Centinel™ make-up valve solenoid supply pin 2 of the engine harness or resistance of the solenoid has dropped below 80 ohms. | ECM turns off the Centinel™ make-up valve supply voltage and the Centinel™ system is disabled. |
>
> Make-Up Valve Solenoid Circuit
>
> ### Circuit Description
>
> The make-up valve solenoid controls the flow of oil within the oil control valve during the make-up cycle.
>
> ### Component Location
>
> The make-up valve solenoid is located on top of the oil control valve.
>
> Refer to Troubleshooting Fault Code t05-225
