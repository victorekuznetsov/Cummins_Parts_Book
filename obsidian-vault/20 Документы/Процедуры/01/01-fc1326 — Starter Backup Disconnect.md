---
aliases:
  - "Резервный размыкатель стартера"
type: "Процедура"
doc: "01-fc1326"
title_en: "Starter Backup Disconnect"
title_ru: "Резервный размыкатель стартера"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1326.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1326.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Starter Backup Disconnect
**Резервный размыкатель стартера**

> [!abstract] Процедура · `01-fc1326`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1326.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1326.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1326

### Резервный размыкатель стартера

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1326 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Отключение стартового резервного копирования не удалось. | Никаких действий со стороны ЕКМ не предпринимается. Возможные повреждения могут возникнуть у стартера. |

![[19802801.png]]

Стартовый круг

### Описание цепи

Стартер генераторной установки имеет два отключения: Стартерный главный отключается и резервная копия. Этот код неисправности используется ECM для информирования оператора о том, что отключение стартера резервного копирования вышло из строя, скорость двигателя выше 950 об/мин, а отключение старта резервного копирования все еще подключено. Поэтому, если основное стартер отключение не удается, повреждение может произойти для стартера.

### Расположение компонента

См. раздел E для определения местоположения отключения стартового резервного копирования

### Практические замечания

Там, где основным стартерным отключением управляет датчик скорости двигателя, резервным стартерным отключением управляет напряжение возбуждения PMG, отправленное в регулятор напряжения. Это напряжение возбуждения возникает после запуска двигателя и поворота ротора генератора. Резервный стартер отключается, как только напряжение PMG составляет 105 VAC или выше.

Возможные режимы отказа - это открытая схема, короткая к земле и неисправный регулятор напряжения.

См. Код устранения неполадок t05-1326


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1326
>
> ### Starter Backup Disconnect
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1326 PID(P): SPN: FMI: Lamp: Warning SRT: | The starter backup disconnect has failed. | No action is taken by the ECM. Possible damage can occur to the starter. |
>
> Starter Circuit
>
> ### Circuit Description
>
> The generator set starter has two disconnects: The starter main disconnect and a backup. This fault code is used by the ECM to inform the operator that the backup starter disconnect has failed, engine speed is above 950 rpm, and backup start disconnect is still connected. Therefore, if the main starter disconnect fails, damage can possibly occur to the starter.
>
> ### Component Location
>
> Refer to Section E for location of the starter backup disconnect
>
> ### Shoptalk
>
> Where the main starter disconnect gets commanded by the engine speed sensor, the backup starter disconnect gets commanded by the PMG excitation voltage sent to the voltage regulator. This excitation voltage occurs once the engine has started and the alternator rotor is turning. The backup starter disconnect activates once the PMG voltage is 105 VAC or higher.
>
> The possible failure modes are open circuit, short to ground, and failed voltage regulator.
>
> Refer to Troubleshooting Fault Code t05-1326
