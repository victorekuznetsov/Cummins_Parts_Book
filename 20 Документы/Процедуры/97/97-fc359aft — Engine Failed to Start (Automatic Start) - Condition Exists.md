---
type: "Процедура"
doc: "97-fc359aft"
title_en: "Engine Failed to Start (Automatic Start) - Condition Exists"
modified: "2007-01-26"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
  - "80141463"
  - "80248213"
families:
  - "QSM11"
  - "QSX15"
manuals:
  - "3666415"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc359aft.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc359aft.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
  - "перевод/машинный"
---

# Engine Failed to Start (Automatic Start) - Condition Exists

> [!abstract] Процедура · `97-fc359aft`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2007-01-26
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc359aft.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc359aft.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 359 (Послепродажное и OEM)

### Не удалось запустить двигатель (автоматический запуск) - состояние

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 359 PID(P): СПН: ФМИ: Лампа: СТО: | Не удалось запустить двигатель (автоматический запуск) - состояние существует. Система ICONTM не смогла запустить двигатель автоматически. | Система ICONTM будет отключена. Включено только обязательное отключение. Может нормально запустить двигатель. |

![[19c01537.png]]

### Описание цепи

Контур выходящего контура реле/зажигания стартера управляет и контролирует как катушку реле стартера, так и входной модуль переключения зажигания ICONTM. Стартерная реле используется функцией ICONTM для выполнения автоматических запусков двигателя. Выход переключателя зажигания используется для обеспечения модуля управления холостым зажиганием ICONTM входным сигналом переключателя зажигания. Вышеупомянутая схема может варьироваться, например, разъем или штифты, в зависимости от марки или модели транспортного средства. Установки OEM могут обеспечить взаимодействие между модулем управления холостым ходом и другими устройствами ICONTM.

### Расположение компонента

Стартовая реле обычно устанавливается на переборке транспортного средства на впускной стороне двигателя. Модуль ICONTM может быть расположен в другом месте в зависимости от применения транспортного средства.

### Практические замечания

Этот код ошибки устанавливается, если два последовательных автоматических запуска не удались. Если стартом управляет модуль управления ICONTM, и ни 130 об/мин не достигается в течение 2 секунд, ни 450 об/мин в течение 14 секунд, то запуск не удался. После первого отказа система ICONTM выжидает 1 минуту, а затем снова пробует. Если вторая попытка старта не удалась, то ошибка устанавливается. Он очищается, как только ручной запуск увенчается успехом.

Если ситема ICONTM используется в режиме без ключа, провод питания стартера может быть неправильно установлен на оконечную позицию зажигания в сборке переключателя зажигания вместо оконечной позиции батареи.

Эта ошибка возникает, если между двумя автоматическими попытками перезапуска ICONTM возникает ошибка блокировки (код ошибки 541). Модуль управления ICONTM интерпретирует это как отказ от запуска, **не **неисправность блокировки. Это обычно может произойти, если переключатель наклона капота делает прерывистый контакт, когда грузовик трясется во время автозапуска.

Система ICONTM может отображать только текущий активный код неисправности. Если одновременно активируется более одного кода неисправности, система ICONTM выдает наиболее приоритетную ошибку. После того, как ошибка была исправлена, будет выброшена следующая активная ошибка.

**Примечание: **Электронная система ICONTM может отображать более одного активного и неактивного кода неисправности одновременно.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Попробуйте запустить двигатель. |  |
|  | **ШАГ 1А.** Попытайтесь запустить двигатель вручную. | Двигатель начинает |
|  | **STEP 1A-1.** Проверьте версию программного обеспечения ICONTM. | Программное обеспечение версии 15 или более |
| ШАГ 2. | Очистите код ошибки. |  |
|  | **STEP 2A.** Отключить код ошибки. | Двигатель запускается вручную в режиме ICONTM |

### ШАГ 1. Попробуйте запустить двигатель.

#### ШАГ 1A. Попробуйте запустить двигатель вручную.

| **Условия:** Включить переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Запустите двигатель вручную. | Двигатель начинает | 1А-1-1 |
| Двигатель **не** запускается | Соответствующие диаграммы устранения неполадок без старта |  |

#### ШАГ 1A-1. Проверьте версию программного обеспечения ICONTM.

| **Условия:** Подключить инструмент электронного обслуживания ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте версию программного обеспечения ICONTM. | Программное обеспечение версии 15 или более | 2А |
| Заменить модуль управления ICONTM idle. См. процедуру[[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Ремонт завершён |  |

### ШАГ 2. Очистите код ошибки.

#### ШАГ 2A. Отключите код неисправности.

| **Условия:** Включить переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сбросьте коды неисправностей. Запустите двигатель вручную. Включите систему ICONTM и проверьте, что жалоба облегчена. | Двигатель запускается вручную в режиме ICONTM | Ремонт завершён |
| Устранение неполадок с оставшимися активными кодами неисправностей. | Соответствующие диаграммы устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 359 (Aftermarket and OEM)
>
> ### Engine Failed to Start (Automatic Start) - Condition Exists
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 359 PID(P): SPN: FMI: Lamp: SRT: | Engine Failed to Start (Automatic Start) - Condition Exists. The ICON™ system has failed to start the engine automatically. | The ICON™ system will be disabled. **Only** mandatory shutdown will be enabled. Can possibly start engine normally. |
>
> ### Circuit Description
>
> The starter relay/keyswitch output circuit controls and monitors both the starter relay coil and the ICON™ idle control module keyswitch input. The starter relay is used by the ICON™ feature to perform automatic starts of the engine. The keyswitch output is used to provide the ICON™ idle control module with a keyswitch input signal. The above circuit diagram can vary, such as connector or pins, depending on the vehicle make or model. OEM installations can possibly provide the harnessing between the idle control module and other ICON™ devices.
>
> ### Component Location
>
> The starter relay is typically mounted on the bulkhead of the vehicle on the intake side of the engine. The ICON™ module can be located in a different location depending on the vehicle application.
>
> ### Shoptalk
>
> This fault code is set if two consecutive automatic starts fail. If a start is commanded by the ICON™ idle control module and neither 130 rpm is reached within 2 seconds nor 450 rpm within 14 seconds then the start failed. After the first failure, the ICON™ system waits 1 minute and then tries again. If the second start attempt fails, the fault is set. It is cleared as soon as a manual start is successful.
>
> If the ICON™ sytem is being used in Keyless Engine Mode, the starter power wire can possibly be incorrectly installed onto the ignition terminal post in the keyswitch assembly instead of onto the battery terminal post.
>
> This fault will occur if an interlock fault (fault code 541) occurs between two automatic ICON™ restart attempts. The ICON™ idle control module interprets this as a fail-to-start, **not** an interlock fault. This can typically occur if the hood tilt switch is making intermittent contact when the truck shakes during an autostart.
>
> The ICON™ system can display **only** the current active fault code. If more than one fault code is active at the same time, the ICON™ system flashes out the highest priority fault. After the fault has been corrected then the next active fault will be flashed out.
>
> **Note:** The ICON™ electronic service tool can display more than one active and or inactive fault codes at the same time.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Attempt to start the engine. |  |
> |  | **STEP 1A.** Attempt to start the engine manually. | Engine starts |
> |  | **STEP 1A-1.** Check ICON™ software version. | Software Version 15 or greater |
> | STEP 2. | Clear the fault code. |  |
> |  | **STEP 2A.** Disable the fault code. | Engine starts manually while in ICON™ mode |
>
> ### STEP 1. Attempt to start the engine.
>
> #### STEP 1A. Attempt to start the engine manually.
>
> | **Conditions:** Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Start the engine manually. | Engine starts | 1A-1 |
> | Engine does **not** start | Appropriate troubleshooting charts for no start |  |
>
> #### STEP 1A-1. Check the ICON™ software version.
>
> | **Conditions:** Connect the ICON™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the ICON™ software version. | Software Version 15 or greater | 2A |
> | Replace the ICON™ idle control module. Refer to Procedure [[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Repair complete |  |
>
> ### STEP 2. Clear the fault code.
>
> #### STEP 2A. Disable the fault code.
>
> | **Conditions:** Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Clear the fault codes. Start the engine manually. Engage the ICON™ system and verify the complaint is alleviated. | Engine starts manually while in ICON™ mode | Repair complete |
> | Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
