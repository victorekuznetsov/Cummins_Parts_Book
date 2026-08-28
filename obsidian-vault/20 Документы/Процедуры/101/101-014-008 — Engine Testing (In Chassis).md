---
aliases:
  - "Испытание двигателя на машине"
type: "Процедура"
doc: "101-014-008"
title_en: "Engine Testing (In Chassis)"
title_ru: "Испытание двигателя на машине"
modified: "2019-03-19"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/101/101-014-008.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/101-014-008.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/101"
  - "перевод/машинный"
---

# Engine Testing (In Chassis)
**Испытание двигателя на машине**

> [!abstract] Процедура · `101-014-008`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 14 - Engine Testing - Group 14
> **Даты:** изменён 2019-03-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/101/101-014-008.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/101-014-008.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Выбор сервисного инструмента

#### Рекомендованный сервисный инструмент Cummins®

- Не требуется никаких инструментов обслуживания Cummins®.

#### Дополнительные сервисные позиции

- Никаких дополнительных предметов обслуживания не требуется.

### Настройка

Функция «Настройка для динамометра» используется для подготовки модуля управления двигателем (ECM) для расширенного диагностического испытания на динамометре шасси. Для целей этого испытания максимальная скорость двигателя без датчика скорости транспортного средства (VSS), максимальная скорость транспортного средства в верхней передаче и максимальная скорость транспортного средства в нижней передаче устанавливаются на их максимальные значения. Функция отключения бездействия отключена, и вентилятор заблокирован в режиме ON. Все эти значения автоматически сбрасываются на свои предыдущие значения, когда переключатель зажигания двигателя поворачивается в положение выключения.

- Максимальная скорость двигателя без VSS: 2500 об/мин для целей тестирования. Эта скорость временно устанавливается на максимально допустимое значение.
- Максимальная скорость автомобиля в Top Gear: 120 миль в час для тестирования. Эта скорость временно устанавливается на максимально допустимое значение.
- Максимальная скорость автомобиля в нижней части: 120 миль в час для тестирования. Эта скорость временно устанавливается на максимально допустимое значение.
- Защита от груши: Эта функция временно отключена для целей тестирования.
- Муфта вентилятора: Продолжай.
- Idle Shutdown: Эта функция временно отключена для целей тестирования.

Некоторые электронные подсистемы Общества автомобильной инженерии (SAE) J1939 должны быть отключены. Пользователь имеет возможность включить или отключить шину данных SAE J1939 CAN с помощью инструментария службы.


> [!quote]- Original (English) · английский оригинал
> ### Select Service Tools
>
> #### Recommended Cummins® Service Tools
>
> - No Cummins® service tools required.
>
> #### Additional Service Items
>
> - No additional service items required.
>
> ### Setup
>
> The Setup for Dynamometer function is used to prepare the engine control module (ECM) for an advanced diagnostic test run on the chassis dynamometer. For purposes of this test, the maximum engine speed without vehicle speed sensor (VSS), the maximum vehicle speed in top gear, and the maximum vehicle speed in lower gear are set to their maximum values. The idle shutdown feature is disabled and the fan is locked in the ON mode. All of these values are automatically reset to their previous values when the engine keyswitch is turned to the OFF position.
>
> - Maximum Engine Speed without VSS: 2500 rpm for testing purposes. This speed is temporarily set to the maximum value allowed.
> - Maximum Vehicle Speed in Top Gear: 120 mph for testing purposes. This speed is temporarily set to the maximum value allowed.
> - Maximum Vehicle Speed in Lower Gear: 120 mph for testing purposes. This speed is temporarily set to the maximum value allowed.
> - Gear-Down Protection: This feature is temporarily disabled for testing purposes.
> - Fan Clutch: On.
> - Idle Shutdown: This feature is temporarily disabled for testing purposes.
>
> Some Society of Automotive Engineering (SAE) J1939 electronic subsystems **must** be disabled. The user has the ability to enable or disable the SAE J1939 data link with the service tool.
