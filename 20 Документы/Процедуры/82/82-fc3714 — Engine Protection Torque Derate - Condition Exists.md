---
aliases:
  - "Снижение момента защитой двигателя — условие возникло"
type: "Процедура"
doc: "82-fc3714"
title_en: "Engine Protection Torque Derate - Condition Exists"
title_ru: "Снижение момента защитой двигателя — условие возникло"
modified: "2010-09-02"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc3714.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc3714.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Engine Protection Torque Derate - Condition Exists
**Снижение момента защитой двигателя — условие возникло**

> [!abstract] Процедура · `82-fc3714`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc3714.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc3714.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 3714

### Снижение момента защитой двигателя — условие возникло

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 3714 PID(P): СПН: ФМИ: 11/31 лампа: Янтарная СРТ: | Снижение момента защитой двигателя — условие возникло. SAE J1939 мультиплексирование сообщения сердцебиения от OEM-устройства потерянного или крутящего момента, наложенного OEM-устройством. | Янтарная предупредительная лампа будет светиться. Будет введено ограничение крутящего момента. |

![[19c00340.png]]

J1939 CAN шина данных Multiplexing Circuit

### Описание цепи

Как правило, переключатели, ускорители и другие компоненты подключаются к электронному модулю управления двигателем (ECM) непосредственно через отдельные провода. Мультиплексирование позволяет подключать те же самые компоненты к электронному блоку управления OEM (ECU) в кабине. Затем значения компонентов и состояния из таких компонентов, как датчики, ускорители и переключатели, могут передаваться от OEM-устройства к ECM двигателя Cummins® через шину данных SAE J1939 CAN.

Сообщения, отправленные с OEM-устройства, принимаются двигателем Cummins® ECM и используются для управления двигателем. Устройство Cummins® ECM и OEM ** должны быть правильно настроены, чтобы происходила правильная работа мультиплексированных компонентов.

### Расположение компонента

Двигатель ECM расположен на впускной стороне двигателя.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда переключатель зажигания находится в положении Включения.

### Условия установки кодов неисправностей

ECM не получает действительное сообщение о сердцебиении J1939 от мультиплексного OEM-устройства в течение более 60 секунд.

Мультиплексное OEM-устройство отправляет запрос на снижение крутящего момента.

### Действия системы при активном коде неисправности

- ECM освещает янтарный CHECK ENGINE через 30 секунд после того, как сообщение о сердцебиении от OEM-устройства потеряно или крутящий момент ухудшается по запросу OEM-устройства.

- ECM наложит крутящий момент.

### Условия сброса кода неисправности

ECM отключит янтарный CHECK ENGINE через 30 секунд после восстановления сообщения о сердцебиении от OEM-устройства или уменьшения крутящего момента, которое больше не запрашивается OEM-устройством.

### Практические замечания

Проверить правильность калибровки ECM. Проверьте историю калибровки, найденную на QuickServeTM Online, для применимых исправлений к калибровке, хранящейся в ECM. При необходимости откалибровать ECM.[[105-019-032 — Engine Control Module Calibration Code|См. процедуру 019-032 в разделе 19.]]

Когда этот код неисправности активен, некоторые мультиплексированные устройства могут работать по желанию.

Эта ошибка может возникнуть по следующим причинам:

- Когда ECM настроен правильно (компоненты включены и источник OEM-устройства адресован правильно) для получения информации от OEM-устройства, но OEM-устройство фактически передает сообщение, в котором говорится, что компонент ** не** доступен для мультиплексирования. Это может быть вызвано включением мультиплексированного компонента в Cummins® ECM, но адрес источника OEM-устройства устройства, передающего сообщение компонента, неверен в Cummins® ECM, или OEM-устройство настроено на передачу сообщения мультиплексированного компонента.

- Неисправное соединение шины данных J1939 CAN между OEM-устройством и Cummins® ECM, неисправное соединение между компонентом и OEM-устройством, неисправное OEM-устройство или неисправное Cummins® ECM. Может потребоваться связаться с OEM для правильной конфигурации мультиплексирования.

- При сердцебиении сообщение от OEM-устройства теряется или прерывается. Помимо неисправности, будет введен 60-процентный крутящий момент. См. сервисное руководство изготовителя машины.

- Когда OEM-устройство запрашивает крутящий момент, он уменьшается на 0-100%. См. сервисное руководство изготовителя машины.

См. Код устранения неисправностей t05-3714


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 3714
>
> ### Engine Protection Torque Derate - Condition Exists
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 3714 PID(P): SPN: FMI: 11/31 Lamp: Amber SRT: | Engine Protection Torque Derate - Condition Exists. SAE J1939 multiplexing heartbeat message from OEM device lost or torque derate imposed by OEM device. | Amber warning lamp will illuminate. Torque derate will be imposed. |
>
> J1939 Data Link Multiplexing Circuit
>
> ### Circuit Description
>
> Normally, switches, accelerators, and other components are connected to the engine electronic control module (ECM) directly through individual wires. Multiplexing allows those same components to be hardwired to an OEM electronic control unit (ECU) in the cab. Then component values and states from components such as sensors, accelerators, and switches can be transmitted from the OEM device to the Cummins® engine ECM over the SAE J1939 data link.
>
> Messages sent from OEM device is received by the Cummins® engine ECM and used for controlling the engine. The Cummins® ECM and OEM device **must** be configured properly so that proper operation of the multiplexed components will occur.
>
> ### Component Location
>
> The engine ECM is located on the intake side of the engine.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the keyswitch is in the ON position.
>
> ### Conditions For Setting The Fault Codes
>
> The ECM does **not** receive a valid J1939 heartbeat message from the multiplexed OEM device for more than 60 seconds.
>
> The multiplexed OEM device sends a request for a torque derate.
>
> ### Action Taken When The Fault Code Is Active
>
> - The ECM illuminates the amber CHECK ENGINE light 30 seconds after the heartbeat message from the OEM device is lost or a torque derate is requested by the OEM device.
>
> - The ECM will impose a torque derate.
>
> ### Conditions For Clearing The Fault Code
>
> The ECM will turn off the amber CHECK ENGINE light 30 seconds after the heartbeat message from the OEM device is restored or a torque derate is no longer being requested by the OEM device.
>
> ### Shoptalk
>
> Verify the ECM calibration is correct. Check the calibration revision history found on QuickServe™ Online for applicable fixes to the calibration stored in the ECM. If necessary, calibrate the ECM. [[105-019-032 — Engine Control Module Calibration Code|Refer to Procedure 019-032 in Section 19.]]
>
> When this fault code is active, some multiplexed devices may **not** function as desired.
>
> This fault can occur for the following reasons:
>
> - When the ECM is setup properly (components enabled and OEM device source addressed correctly) to receive information from an OEM device, but the OEM device is actually transmitting a message that says that component is **not** available for multiplexing. This can be caused when a multiplexed component is enabled in the Cummins® ECM, but the OEM device source address of the device transmitting the component message is incorrect in the Cummins® ECM, or the OEM device is **not** setup to transmit the multiplexed component message.
>
> - A malfunctioning J1939 data link connection between the OEM device and Cummins® ECM, a malfunctioning connection between the component and the OEM device, a malfunctioning OEM device, or a malfunctioning Cummins® ECM. It can be necessary to contact the OEM for the proper multiplexing configuration.
>
> - When the heartbeat message from the OEM device is lost or interrupted. In addition to the fault, a 60 percent torque derate will be imposed. Refer to the OEM service manual.
>
> - When the OEM device is requesting a torque derate between 0 and 100 percent. Refer to the OEM service manual.
>
> Refer to Troubleshooting Fault Code t05-3714
