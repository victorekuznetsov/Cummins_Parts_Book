---
aliases:
  - "Цепь термостата кабины ICON™"
type: "Процедура"
doc: "82-fc469"
title_en: "ICON™ Cab Thermostat Circuit"
title_ru: "Цепь термостата кабины ICON™"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc469.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc469.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# ICON™ Cab Thermostat Circuit
**Цепь термостата кабины ICON™**

> [!abstract] Процедура · `82-fc469`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc469.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc469.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 469

### Цепь термостата кабины ICON™

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 469 PID(P): S215 SPN: ФМИ: 2/2 лампы: Нет, не srt: | Термостат ICONTM кабины зафиксировал неисправность (E3 на термостате кабины), или сигнал кабины термостата к ECM теряется. | E3 будет циклировать двигатель от 20 минут работы до 15 минут выключения или до достижения желаемой заданной точки. (Это выборочный ответ на неисправность E3 в таблице отделки термостата.) Система ICONTM будет отключена. Режим двигателя будет оставаться активным. |

![[19803218.png]]

Цепь термостата кабины ICON™

### Описание цепи

Термостат кабины используется для контроля температуры кабины, либо для нагревания, либо для охлаждения. Это необходимо для работы в режиме комфорта кабины. Термостат связывается с ECM, чтобы указать, когда следует запускать двигатель для поддержания температуры кабины. Кроме того, термостат подключен к переключателю зажигания для обнаружения, когда зажигание включено.

### Расположение компонента

Термостат кабины установлен в зоне койки, на стене над кроватью.

### Практические замечания

E3 является признаком того, что произошло одно из следующих событий: (1) Двигатель работает более 60 минут, и точка установки охлаждения или тепла не достигается, а внешняя температура окружающей среды находится в пределах от -18 ° до 43 ° C \[0 до 110° F \] (термостат-регулируемая отделка 01 и 02, см. таблицу отделки термостата в руководстве по эксплуатации и техническому обслуживанию ICONTM, Бюллетень [[3666422 — ICON™ Idle Control System\|3666422]]); (2) запрос термостата кабины для запуска двигателя был запрошен четыре раза за один час, а температура окружающей среды находится в пределах от -18 ° до 43 ° C \[0 до 110° F \]. E3 может указывать на потенциальное вмешательство термостата. Например, оператор выбрал холодный режим, но включил нагреватель или открыл окна. Система кондиционирования воздуха будет пытаться охладить грузовик ниже точки охлаждения в течение 60 минут. В это время будет зарегистрирована ошибка E3 (код ошибки 469). Аналогичная ситуация может возникнуть и в тепловом режиме. После того, как E3 будет отображаться на термостате, двигатель будет работать в течение 20 минут и выключаться в течение 15 минут. Если желаемая заданная температура достигается в режиме работы с подделкой (20 минут включения и 15 минут выключения), она возвращается к нормальной работе в режиме кабины. Чтобы очистить E3, отключите ICONTM, отключите ключ примерно на 30 секунд, а затем активируйте ICONTM.

Примечание: Неисправность термостата E1 (датчик температуры кабины), E2 (внешний датчик температуры окружающего воздуха) и E3 (режим включения) не мелькают на лампе ICONTM, а просто отображаются на экране дисплея термостата. Инструменты электронного сервиса INSITETM будут регистрировать активный код 469 ошибок до тех пор, пока не будут очищены. См. Cab Thermostat Отображает дерево симптомов устранения неисправностей кода ошибки в разделе TS. Исследуйте связанные коды ошибок, которые также могут быть активными.

Устранение неполадок код t05-469


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 469
>
> ### ICON™ Cab Thermostat Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 469 PID(P): S215 SPN: FMI: 2/2 Lamp: None SRT: | The ICON™ cab thermostat has logged a fault (E3 on the cab thermostat), or the cab thermostat signal to the ECM is lost. | E3 will cycle the engine between 20 minutes run and 15 minutes off or until the desired set-point is reached. (This is a selectable response of the E3 fault in the thermostat trim table.) The ICON™ system will **not** be disabled. Engine mode will remain active. |
>
> ICON™ Cab Thermostat Circuit
>
> ### Circuit Description
>
> The cab thermostat is used to control the cab temperature, either for heating or cooling. It is required for cab comfort mode operation. The thermostat communicates with the ECM to command when to autostart the engine to maintain cab temperature. Also, the thermostat is connected to the keyswitch to detect when the ignition is turned on.
>
> ### Component Location
>
> The cab thermostat is mounted in the bunk area, on the wall above the bed.
>
> ### Shoptalk
>
> E3 is an indication that one of the following has occurred: (1) Engine has run for more than 60 minutes, and cool or heat set point is **not** achieved, and external ambient temperature is within -18° to 43°C \[0 to 110°F\] (thermostat-adjustable trim 01 and 02, see thermostat trim table in the ICON™ Operation and Maintenance Manual, Bulletin [[3666422 — ICON™ Idle Control System\|3666422]]); (2) a cab thermostat request to start the engine has been requested four times in one hour, and the ambient temperature is within -18° to 43°C \[0 to 110°F\]. E3 can indicate potential tampering of the thermostat. For example, the operator has chosen cool mode but turned the heater on or opened the windows. The air-conditioning system will attempt to cool the truck below the cool set point for 60 minutes. At this time, an E3 fault (Fault Code 469) will be logged. A similar situation can occur for heat mode. Once an E3 is displayed on the thermostat, the engine will cycle on for 20 minutes and off for 15 minutes. If the desired temperature set-point is reached in the tamper mode operation (20 minutes on and 15 minutes off), it will return to normal cab mode operation. To clear E3, disable ICON™, key off for approximately 30 seconds, and then reactivate ICON™.
>
> Note: The thermostat fault E1 (cab temperature sensor), E2 (external ambient air temperature sensor), and E3 (tamper mode) do **not** flash out on the ICON™ lamp, but merely display on the thermostat display screen. INSITE™ electronic service tool will log an active Fault Code 469 until cleared. Refer to the Cab Thermostat Displays a Fault Code troubleshooting symptom tree in Section TS. Investigate the related fault codes that also can possibly be active.
>
> Refer to Troubleshooting Fault Code t05-469
