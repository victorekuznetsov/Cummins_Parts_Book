---
aliases:
  - "Цепь выключателя подтверждения холостого хода"
type: "Процедура"
doc: "82-fc551iss"
title_en: "Idle Validation Switch Circuit"
title_ru: "Цепь выключателя подтверждения холостого хода"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc551iss.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc551iss.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Idle Validation Switch Circuit
**Цепь выключателя подтверждения холостого хода**

> [!abstract] Процедура · `82-fc551iss`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc551iss.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc551iss.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 551

МКС

### Цепь выключателя подтверждения холостого хода

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 551 PID(P): S230 SPN: 558 FMI: 4/4 лампы: Желтая СТО: | Нет напряжения, обнаруженного одновременно как на холостых валидирующих схемах off-idle, так и на холостых схемах. | Двигатель будет только * простаивать. |

![[19c00644.png]]

Цепь выключателя подтверждения холостого хода

### Описание цепи

Переключатель проверки бездействия используется электронным модулем управления (ECM) для указания, когда педаль акселератора выпущена (на холостом ходу) или подавлена (вне холостом ходу). Переключатель настраивается на заводе для переключения с on-idle на off-idle в правильном положении педали акселератора.

### Расположение компонента

Интегрированный датчик/переключатель (ISS) расположен на педальном сборе ускорителя.

### Практические замечания

- Этот код неисправности обычно вызван свободным соединением, педалью ускорителя, которая **не** калибрована, или IVS, который подключен неправильно. Для проверки уровней напряжения SSS требуется проводной ветвь ремня, номер детали 3824892.

- Если вся проводка и проверка датчиков хороши, замените провода переключателя проверки простоя между педалью ускорителя и ECM новыми проводами. Проведите провода через или вокруг переборки без использования разъема переборки. Испытайте грузовик с проводами на месте. Если неисправность устраняется, замените проводку OEM. Запечатайте отверстия в переборке вокруг разъема и проводов, чтобы предотвратить попадание токсичных и вредных паров в кабину.

- Убедитесь, что три провода переключателя проверки скручены вместе.

- Сборка педали ECM и педали акселератора **должна быть электрически откалибрована друг к другу для правильного отклика двигателя. Узел педали ECM и ускорителя** должен быть откалиброван, когда педаль акселератора первоначально установлена, заменена, когда заменена ECM, когда новая калибровка загружена в ECM, и когда педаль акселератора отключена, когда включен переключатель зажигания транспортного средства.

- При включении зажигания постепенно подталкивайте ускоритель к полу и отпустите. Уплотните и отпустите педаль акселератора три раза. Эта процедура позволит перекалибровать педаль ECM и ускорителя.

См. Troubleshooting Fault Code t05-551iss


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 551
>
> ISS
>
> ### Idle Validation Switch Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 551 PID(P): S230 SPN: 558 FMI: 4/4 Lamp: Yellow SRT: | No voltage detected simultaneously on both the idle validation off-idle and on-idle circuits. | Engine will **only** idle. |
>
> Idle Validation Switch Circuit
>
> ### Circuit Description
>
> The idle validation switch is used by the electronic control module (ECM) to indicate when the accelerator pedal is released (on-idle) or depressed (off-idle). The switch is adjusted at the factory to switch from on-idle to off-idle at the correct accelerator pedal position.
>
> ### Component Location
>
> The integrated sensor/switch (ISS) is located on the accelerator pedal assembly.
>
> ### Shoptalk
>
> - This fault code is usually caused by a loose connection, an accelerator pedal that is **not** calibrated, or an IVS that is wired wrong. Breakout cable, Part Number 3824892, is required to check the voltage levels of the SSS.
>
> - If all wiring and sensor checks are good, replace the idle validation switch circuit wires, between the accelerator pedal and ECM, with new wires. Run the wires through or around the bulkhead without using the bulkhead connector. Test the truck with the test wires in place. If the fault clears, replace the OEM harness. Seal the openings in the bulkhead around the connector and wires to prevent toxic and noxious fumes from seeping into the cab.
>
> - Verify that the three idle validation switch circuit wires are twisted together.
>
> - The ECM and accelerator pedal assembly **must** be electrically calibrated to each other for proper engine response. The ECM and accelerator pedal assembly **must** be calibrated when an accelerator pedal is initially installed, replaced, when an ECM is replaced, when a new calibration is downloaded to the ECM, and when the accelerator pedal wiring is disconnected while the vehicle keyswitch is on.
>
> - With keyswitch on, gradually push the accelerator to the floor and release. Depress and release the accelerator pedal three times. This procedure will recalibrate the ECM and accelerator pedal.
>
> Refer to Troubleshooting Fault Code t05-551iss
