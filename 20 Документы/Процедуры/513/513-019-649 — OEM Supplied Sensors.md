---
type: "Процедура"
doc: "513-019-649"
title_en: "OEM Supplied Sensors"
modified: "2019-09-27"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "5411480"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-019-649.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-019-649.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
  - "перевод/машинный"
---

# OEM Supplied Sensors

> [!abstract] Процедура · `513-019-649`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section 19 - Electronic Controls - Group 19
> **Даты:** изменён 2019-09-27
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-019-649.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-019-649.pdf)

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

### Общие сведения

Система Marine C Command Connect и Connect Premier Panel System требует от производителя оригинального оборудования (OEM) использовать клиентский интерфейс Cummins (CIB) и интерфейс двигателя.

Остальные компоненты системы (дисплеи, датчики и т. Д.) и проводные ремни могут быть спроектированы и закуплены OEM-производителем, если компоненты соответствуют руководящим принципам Cummins Application Engineering и проходят оценку качества установки.

См. информацию об обслуживании производителя оборудования для информации о эксплуатации, удалении и установке компонентов, поставляемых OEM.

Используйте следующую процедуру для получения информации о подключении датчика к системе управления морскими средствами C Command Connect и системе управления рабочей панелью Connect Premier.[[513-208-002 — Component Diagrams|См. процедуру 208-002 в разделе E.]]

На момент первоначального выпуска Marine C Command Connect and Connect Premier Panel System имеет следующие таблицы калибровки датчиков, загруженные в файл личности судна:

| Сенсор | Тип |
|---|---|
| Датчик температуры отработавших газов | резистивный |
| Переключатель температуры выхлопа | Обычно открыт, закрывается выше температурного порога. |
| Уровень топлива | резистивный |
| Английское название Rudder Angle | резистивный |
| Трансмиссия давления масла груши | Напряжение |
| Температура масла трансмиссии | Резистивная нота: CIB преобразует сигнал в напряжение для ED-4 для мониторинга. |

Для того, чтобы правильные значения отображались на дисплее ED-4, должен быть загружен соответствующий файл личности сосуда, содержащий соответствующие таблицы калибровки датчиков.[[513-015-044 — Managing Vessel Personalities|См. процедуру 015-044 в разделе 15.]]

Используйте следующую процедуру для использования ED-4 для устранения неполадок датчика.[[513-015-035 — Display(s) and Instrumentation|См. процедуру 015-035 в разделе 15.]]

> [!note] Примечание
> Некоторые приложения могут использовать модуль управления двигателем (ECM) для мониторинга этих датчиков. См. руководство по обслуживанию двигателя для получения дополнительной информации.


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
> ### General Information
>
> The Marine C Command Connect and Connect Premier Panel System requires the original equipment manufacturer (OEM) to use a Cummins designed customer interface box (CIB) and engine interface harness.
>
> The remaining system components (displays, sensors, etc.) and wiring harnesses can be designed and procured by the OEM as long as the components meet the Cummins Application Engineering guidelines and pass the installation quality assessment.
>
> See equipment manufacturer service information for information on operation, removal, and installation of the OEM supplied components.
>
> Use the following procedure for information on sensor connection with the Marine C Command Connect and Connect Premier Panel System. [[513-208-002 — Component Diagrams|Refer to Procedure 208-002 in Section E.]]
>
> At initial production release, the Marine C Command Connect and Connect Premier Panel System has the following sensor calibration tables loaded in the vessel personality file:
>
> | Sensor | Type |
> |---|---|
> | Exhaust Temperature Sensor | Resistive |
> | Exhaust Temperature Switch | Normally open that closes above a temperature threshold |
> | Fuel Level | Resistive |
> | Rudder Angle | Resistive |
> | Transmission Gear Oil Pressure | Voltage |
> | Transmission Gear Oil Temperature | Resistive Note: The CIB converts the signal to voltage for the ED-4 to monitor. |
>
> In order for the correct values to display on the ED-4 display, the proper vessel personality file **must** be loaded containing associated sensor calibration tables. [[513-015-044 — Managing Vessel Personalities|Refer to Procedure 015-044 in Section 15.]]
>
> Use the following procedure for using the ED-4 to troubleshoot sensor issues. [[513-015-035 — Display(s) and Instrumentation|Refer to Procedure 015-035 in Section 15.]]
>
> **Note · Примечание**
> Some applications may use the engine control module (ECM) to monitor these sensors. Refer to engine service manual for more information.
