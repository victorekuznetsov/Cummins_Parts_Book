---
type: "Процедура"
doc: "19-fc219"
title_en: "Make-Up Tank Oil Level Low Fault"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc219.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc219.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Make-Up Tank Oil Level Low Fault

> [!abstract] Процедура · `19-fc219`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc219.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc219.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 219

### Макияж танка уровень масла низкий

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 219 P(P): S153 SPN: 1380 FMI: 1 лампа: Защита двигателя SRT: | Низкий уровень масла обнаружен в удаленном масляном резервуаре, используемом в системе CentinelTM. | Система CentinelTM отключена. |

![[19400659.png]]

Макияж танка масло уровень низкий датчик

### Описание цепи

Низкий датчик уровня масла в масляном баке для макияжа контролирует уровень масла в масляном баке для макияжа и сообщает в ECM, когда масло опускается ниже указанного уровня.

### Расположение компонента

Низкий датчик уровня масла в масляном масле расположен на нижней части масляного резервуара системы CentinelTM.

### Практические замечания

Убедитесь, что в макияже есть соответствующий уровень масла.

См. Код устранения неполадок t05-219


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 219
>
> ### Make-Up Tank Oil Level Low Fault
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 219 PID(P): S153 SPN: 1380 FMI: 1 Lamp: Engine Protection SRT: | Low oil level detected in the remote oil reservoir used in the Centinel™ system. | Centinel™ system is disabled. |
>
> Make-up Tank Oil Level Low Sensor
>
> ### Circuit Description
>
> The make-up tank oil level low sensor monitors the oil level in the make-up oil tank and reports to the ECM when the oil drops below the specified level.
>
> ### Component Location
>
> The make-up tank oil level low sensor is located on the lower portion of the Centinel™ system make-up oil tank.
>
> ### Shoptalk
>
> Verify that the make-up tank has the appropriate level of oil.
>
> Refer to Troubleshooting Fault Code t05-219
