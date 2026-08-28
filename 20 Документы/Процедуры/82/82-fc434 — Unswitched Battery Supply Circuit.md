---
aliases:
  - "Цепь постоянного питания от АКБ"
type: "Процедура"
doc: "82-fc434"
title_en: "Unswitched Battery Supply Circuit"
title_ru: "Цепь постоянного питания от АКБ"
modified: "2010-09-02"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc434.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc434.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Unswitched Battery Supply Circuit
**Цепь постоянного питания от АКБ**

> [!abstract] Процедура · `82-fc434`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc434.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc434.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 434

### Цепь постоянного питания от АКБ

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 434 PID(P): S251 SPN: 627 FMI: 2/2 лампы: Желтая СТО: | Напряжение подачи в электронный модуль управления (ECM) упало ниже (+) 6,2-VDC на долю секунды или ECM было **не** разрешено правильно отключать питание (сохранить напряжение батареи в течение 30 секунд после выключения переключателя зажигания). | Возможно, нет заметных эффектов производительности или отмирания двигателя или жесткого запуска. Информация о неисправности, информация о поездке и данные мониторинга технического обслуживания могут быть неточными. |

![[19c00043.png]]

Непереключенное питание батареи

### Описание цепи

ECM получает постоянное напряжение от батарей через непереключенные провода батареи, которые подключены непосредственно к положительному (+) посту батареи. В непереключенных проводах аккумуляторов есть два встроенных 15-амперных предохранителя, чтобы защитить жгут проводов двигателя от перегрева. ECM принимает вводимую аккумуляторную батарею через провод переключателя зажигания транспортного средства и один 5-амперный предохранитель при включении переключателя зажигания транспортного средства. Провода возврата аккумулятора соединены непосредственно с отрицательной (-) позицией аккумулятора.

### Расположение компонента

ECM подключается к батарее с помощью OEM-проводов. Это прямое соединение обеспечивает постоянный источник питания для ECM. Расположение батареи будет варьироваться в зависимости от OEM. См. сервисное руководство изготовителя машины.

### Практические замечания

- Проверьте форсунка свиных хвостовых орехов и убедитесь, что они сжаты до правильного крутящего момента. Подтвердите, что хрустящие орехи и соленоидные столбы **не** имеют поврежденную резьбу.

- Если отключаемый источник питания батареи ECM берется из стартера, проверьте низкое напряжение во время проворачивания. Низкое напряжение во время проворачивания может привести к тому, что источник питания ECM упадет ниже спецификации и войдет в систему кода 434 по умолчанию.

См. Код устранения неполадок t05-434


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 434
>
> ### Unswitched Battery Supply Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 434 PID(P): S251 SPN: 627 FMI: 2/2 Lamp: Yellow SRT: | Supply voltage to the electronic control module (ECM) fell below (+) 6.2-VDC for a fraction of a second or the ECM was **not** allowed to power down correctly (retain battery voltage for 30 seconds after keyswitch is turned off). | Possible no noticeable performance effects or engine dying or hard starting. Fault information, trip information, and maintenance monitor data can be inaccurate. |
>
> Unswitched Battery Supply
>
> ### Circuit Description
>
> The ECM receives constant voltage from the batteries through the unswitched battery wires that are connected directly to the positive (+) battery post. There are two in-line 15-ampere fuses in the unswitched battery wires to protect the engine harness from overheating. The ECM receives switched battery input through the vehicle keyswitch wire, and one 5-ampere fuse when the vehicle keyswitch is turned on. The battery return wires are connected directly to the negative (-) battery post.
>
> ### Component Location
>
> The ECM is connected to the battery by the OEM harness. This direct link provides a constant power supply for the ECM. The location of the battery will vary with the OEM. Refer to the OEM service manual.
>
> ### Shoptalk
>
> - Examine the injector pigtail nuts and make sure they are tightened down to the proper torque. Confirm that the pigtail nuts and solenoid posts do **not** have damaged threads.
>
> - If the ECM unswitched battery supply is taken from the starter, check for low voltage during cranking. Low voltage during cranking can cause the ECM power supply to drop below specification and log Fault Code 434.
>
> Refer to Troubleshooting Fault Code t05-434
