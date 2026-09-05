---
type: "Процедура"
doc: "326-015-044"
title_en: "Managing Vessel Personalities"
modified: "2019-11-04"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "4358378"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/326/326-015-044.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/326-015-044.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/326"
  - "перевод/машинный"
---

# Managing Vessel Personalities

> [!abstract] Процедура · `326-015-044`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[4358378 — Cummins® Electronic Throttle and Shift (ETS) and Cummins® Inboard Joystick Marine Con|4358378]]
> **Секции:** Section 15 - Instruments and Controls - Group 15
> **Даты:** изменён 2019-11-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/326/326-015-044.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/326-015-044.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Бортовой джойстик Cummins® должен быть настроен на судно, в котором он установлен для максимальной производительности. Судовые джойстики поставляются с предварительно загруженным файлом личности по умолчанию при заказе с завода. Новые джойстики должны быть обновлены с помощью настроенного файла личности судна, который предназначен для производителя оригинального оборудования для лодок (OEM) и модели. Необходимо загрузить наиболее актуальную для судна индивидуальность судна. Если по другим причинам меняется файл личности судна, учитывайте множество факторов, которые могут способствовать маневренности судна, таких как:

- Вес лодки (количество пассажиров/груза, надстройки послепродажного обслуживания)
- балласт
- Дизайн корпуса
- Размер креста
- Местонахождение двигателя
- Наличие дополнительного кормового двигателя
- Размер/дизайн пропеллера
- Напряжение батареи/производительность
- Производительность переключателя (если батареи двигателя сконфигурированы для использования одного)
- Рулевое колесо/рулевое положение
- Мощность каждого двигателя
- Незанятость каждого двигателя.
- Строение, коррозия или эрозия пропеллера.

Изменения или изменения в заводской конструкции лодки могут привести к изменению производительности управления джойстиком. Важно изучить эти факторы, чтобы диагностировать первопричину проблемы производительности, прежде чем обращаться в авторизованное место ремонта Cummins®. Если требуется другая личность, пожалуйста, свяжитесь с авторизованным местом ремонта Cummins®.

Веб-страница QuickServe® Marine Panel Firmware содержит лист отслеживания личных файлов судна и файлы личности джойстика.

Веб-страница Cummins® Inboard Joystick (https://quickserve.cummins.com/qs3/qsol/service/marine/mpf\_joystick.html) содержит таблицу с информацией о каждом файле личности судна, которая помогает выбрать правильный файл и уровень пересмотра для джойстика (ов) судна.

> [!note] Примечание
> [https://quickserve.cummins.com/qs3/qsol/service/marine/mpf\_joystick.html](https://quickserve.cummins.com/qs3/qsol/service/marine/mpf_joystick.html)

Формат имени файла Joystick Vessel Personality состоит из 1 буквы, 4 цифр и 2-значного уровня редактирования. Пример: J1234.01.jst.

Файлы личности Cummins® на борту джойстика загружаются в джойстик с помощью электронного инструментария для обслуживания конфигурации джойстика. Используйте следующую процедуру для более подробной информации о конфигурации судна электронное сервисное оборудование.[[326-015-042 — Vessel Configuration Tool|См. процедуру 015-042 в разделе 15.]]

После загрузки личности джойстика используйте следующую процедуру для получения информации об идентификационном номере джойстика, связанном идентификационном номере ручки и настройке типа джойстика.[[326-015-054 — Vessel Configuration|См. процедуру 015-054 в разделе 15.]]

Если один и тот же файл личности загружается в несколько станций джойстиков на судне, соответствующий идентификационный номер ручки должен быть установлен по-разному в каждом месте станции.[[326-015-054 — Vessel Configuration|См. процедуру 015-054 в разделе 15.]]

Все функции управления электронным дросселем и переключением Cummins® и бортовым джойстиком Cummins® должны быть протестированы перед выходом из дока после служебного мероприятия. См. процедуру 015-046 в разделе 15.

После загрузки файла личности джойстика, если есть новый код тревоги или жалоба на производительность, следуйте коду тревоги или соответствующему дереву симптомов устранения неполадок, чтобы понять, правильно ли работает личность и является ли она подходящей личностью для приложения.

Если есть подозрение, что файл личности работает неправильно, убедитесь, что соответствующий файл был загружен для двигателя, оборудования и приложения.

Используйте следующую процедуру для более подробной информации.[[326-015-042 — Vessel Configuration Tool|См. процедуру 015-042 в разделе 15.]]

> [!note] Примечание
> «Личный лист отслеживания файлов Vessel» на веб-странице Cummins® Inboard Joystick предоставляет информацию, касающуюся изменений, внесенных в личность. Эта информация может быть использована для установления, существует ли общность между изменениями, внесенными в личность, и наблюдаемыми симптомами.


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The Cummins® inboard joystick must be tuned to the vessel it is installed in for maximum performance. Vessel joysticks come with a preloaded default personality file when ordered from the factory. New joysticks have to be updated with a tuned vessel personality file that is specific to boat original equipment manufacturer (OEM) and model. It is necessary to load the most current vessel personality for the vessel. If changing a vessel personality file for other reasons, consider the many factors that can contribute to vessel maneuverability such as the following:
>
> - Boat weight (Number of passengers/cargo, aftermarket add-ons)
> - Ballast
> - Hull design
> - Thruster size
> - Location of thruster
> - Presence of an optional stern thruster
> - Propeller size/design
> - Battery voltage/performance
> - Alternator performance (if thruster batteries are configured to utilize one)
> - Steering wheel/rudder position
> - Horsepower output of each engine
> - Idle setting of each engine.
> - Buildup, corrosion, or erosion of propeller.
>
> Changes or alterations from the factory design of the boat can result in altering the performance of the joystick control. It is important to examine these factors to diagnose the root cause of the performance issue before contacting a Cummins® Authorized Repair Location. If a different personality is needed, please contact the a Cummins® Authorized Repair Location.
>
> The QuickServe® Marine Panel Firmware webpage contains a vessel personality file tracking sheet and joystick vessel personality files.
>
> The Marine Panel Firmware webpage for Cummins® Inboard Joystick (https://quickserve.cummins.com/qs3/qsol/service/marine/mpf\_joystick.html) contains a table with information about each vessel personality file, which helps select the correct file and revision level for the vessel's joystick(s).
>
> **Note · Примечание**
> [https://quickserve.cummins.com/qs3/qsol/service/marine/mpf\_joystick.html](https://quickserve.cummins.com/qs3/qsol/service/marine/mpf_joystick.html)
>
> The Joystick Vessel Personality File Name format consists of 1 letter, 4 digits, and a 2 digit revision level. Example: J1234.01.jst.
>
> Cummins® inboard joystick vessel personality files are loaded into the joystick using the joystick configuration electronic service tool. Use the following procedure for more detail about the vessel configuration electronic service tool. [[326-015-042 — Vessel Configuration Tool|Refer to Procedure 015-042 in Section 15.]]
>
> After a joystick personality download, use the following procedure for information on joystick handle identification number, associated handle identification number, and joystick type setup. [[326-015-054 — Vessel Configuration|Refer to Procedure 015-054 in Section 15.]]
>
> If the same personality file is downloaded into multiple joysticks stations on the vessel, the associated handle identification number will need to be set up differently at each station location. [[326-015-054 — Vessel Configuration|Refer to Procedure 015-054 in Section 15.]]
>
> All control functionality of the Cummins® electronic throttle and shift and Cummins® inboard joystick **must** be tested before leaving the dock after a service event. Refer to Procedure 015-046 in Section 15.
>
> Following a joystick personality file download, if there is a new alarm code or performance complaint, follow the alarm code or the appropriate troubleshooting symptom tree in order to understand if the personality is working correctly and is the appropriate personality for the application.
>
> If it is suspected that the personality file is **not** working correctly, make sure that the appropriate file was loaded for the engine, equipment, and application.
>
> Use the following procedure for more detail. [[326-015-042 — Vessel Configuration Tool|Refer to Procedure 015-042 in Section 15.]]
>
> **Note · Примечание**
> The “Vessel Personality File Tracking Sheet” on the Marine Panel Firmware Updates - Cummins® Inboard Joystick webpage provides information relating to changes made to a personality. This information can be used to establish if there is a commonality between changes made to the personality and the symptoms being observed.
