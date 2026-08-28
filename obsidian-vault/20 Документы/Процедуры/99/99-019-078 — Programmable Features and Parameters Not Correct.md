---
aliases:
  - "Программируемые функции и параметры заданы неверно"
type: "Процедура"
doc: "99-019-078"
title_en: "Programmable Features and Parameters Not Correct"
title_ru: "Программируемые функции и параметры заданы неверно"
modified: "2020-02-28"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-078.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-078.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/99"
  - "перевод/машинный"
---

# Programmable Features and Parameters Not Correct
**Программируемые функции и параметры заданы неверно**

> [!abstract] Процедура · `99-019-078`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2020-02-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-078.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-078.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Эта процедура была разработана в связи с увеличением числа предлагаемых параметров и функций, которые могут повлиять на производительность автомобиля. Используйте следующую таблицу для устранения жалоб на производительность, обнаружив соответствующий симптом в левой колонке. Затем следуйте вероятной причине и корректирующему действию в соседних колонках.

Настройка функций или параметров с помощью рекомендованного инструментария для электронных услуг Cummins® или эквивалента.

![[19803969.png]]

### Регулировка

| Программируемые функции/параметры некорректны |  |  |
|---|---|---|
| Признак неисправности | Вероятная причина | Устранение |
| Превышение скорости на дорогах губернатора установило скорость на холмах | Круиз-контроль или регулятор скорости движения на дороге ниже понижается установлен слишком высоко. | Измените круиз-контроль или регулятор скорости движения на более низкое значение. Если проблема продолжается, измените активацию тормоза двигателя круиз-контроля на более низкое значение. |
| Плохое ускорение на холмах | Круиз-контроль и/или верхняя петля регулятора скорости на дороге установлена слишком высоко. | Измените круиз-контроль или верхнюю часть регулятора скорости движения на более низкое значение. |
| Круиз-контроль включается автоматически. | Функция автоматического резюме круиз-контроля включена. | Выключите функцию автоматического резюме круиз-контроля. |
| Выхлопные тормоза включаются автоматически. | Функция тормоза автоматического двигателя круиз-контроля включена или выхлопной тормозной переключатель не работает. | Выключите функцию тормоза автоматического двигателя круиз-контроля или отремонтируйте выключатель. |
| Невозможность получить максимальную скорость автомобиля. | Функция защиты Gear-down включена. | Выключите или отрегулируйте параметры защиты от переключения передач. |
| Плохое взаимодействие сцепления | Низкая скорость холостого хода установлена слишком низкой для приложения. | Увеличьте скорость на низких холостых ходах с помощью переключателя регулирования холостого хода.[[99-019-052 — Idle Adjust Switch\|См. процедуру 019-052]]. Увеличьте параметр скорости низкого холостого хода. |
| Спидометр на приборной панели **не** правильная или транспортное средство, превышающее установленную скорость регулятора скорости. | Параметры скорости транспортного средства не установлены должным образом. | Убедитесь, что следующие являются правильными: Размер шин, соотношение задних осей, тип датчика скорости транспортного средства и зубья передач на оборот. |
| Данные о пробеге в поездке **не** верны. | Параметр размера шины был изменен без сброса информационной системы поездки. | Установите информационную систему поездки снова, когда параметр размера шины изменяется. |
| Может **не** получить максимальную скорость автомобиля с полуавтоматической трансмиссией. | Параметры защиты от переключения передач **не установлены должным образом. | Изменить верхний параметр передаточного числа, чтобы он был равен первому передаточному соотношению, **не**верхнему передаточному соотношению. Например, на коробке передач с 0,75, 0,87 и 1,0 отношением, верхний параметр передаточного отношения** должен быть установлен на 0,87. |
| Двигатель не заводится. | Пароль Antitheft активен. | Введите идентификационный номер (PIN) для предотвращения кражи с помощью RoadRelayTM или удалите пароль с помощью Zap-It. |
| Низкая мощность в нижних передачах или верхней передаче | Параметры защиты силовых агрегатов установлены слишком низко. | Измените пределы крутящего момента защиты силового агрегата, чтобы соответствовать крутящему моменту трансмиссии транспортного средства. |
| Семейная трансмиссия **не** переключается на верхнюю передачу. | Верхнее передаточное число соответствует **не** верхнему передаточному устройству. | Установите правильное верхнее передаточное число. |
| Функция CentinelTM была включена, но автомобиль имеет трансмиссию Spicer Top 2TM. | Характеристики и параметры не установлены должным образом. | Выключите функцию CentinelTM и включите функцию Top 2. |
| Двигатель недавно начал перегреваться, потому что вентилятор будет **не** включаться. | Функция управления вентилятором не установлена должным образом. | Проверьте, все параметры функции управления вентилятором правильно установлены для автомобиля. |
| Фан не будет **выключаться. | Функция управления вентилятором** не установлена должным образом. | Проверьте, все параметры функции управления вентилятором правильно установлены для автомобиля. |
| Переключатель управления вентилятором **не** включает вентилятор. | Вентилятор управления 1 управления вспомогательным выключателем выключен. | Включите управление вентилятором 1 управление вспомогательным переключателем. |
| Невозможность получить максимальную скорость автомобиля. | Максимальная скорость круиз-контроля или максимальная скорость акселератора транспортного средства не установлена достаточно высоко. | Проверить или изменить настройки. |
| Система поощрения водителя наказывает водителя с пониженной максимальной скоростью транспортного средства или максимальной скоростью круиз-контроля за плохую экономию топлива или длительное время простоя. | Водитель не знаком с функцией или функцией, а параметры **не** установлены должным образом. | Объясните водителю функцию или измените параметры настройки на более подходящие значения. |
| Педаль акселератора не влияет на скорость двигателя. | Транспортное средство находится в режиме PTO, а в ECM включено оверрайдер PTO. | Выключите опрокидывание ускорителя PTO. |
| Педаль акселератора не влияет на скорость двигателя. | Транспортное средство имеет педаль мультиплексного дросселя, и функция мультиплексирования выключена. | Убедитесь, что педаль дросселя мультиплексирована. Включите функцию мультиплексирования педали дроссельной заслонки. |
| Дистанционное управление ускорителем не влияет на скорость двигателя. | Функция удаленного ускорителя отключена. | Включите функцию удаленного ускорителя. |
| Дистанционное управление ускорителем не влияет на скорость двигателя. | Транспортное средство имеет мультиплексное дистанционное управление ускорителем, и функция мультиплексирования выключена. | Убедитесь, что управление удаленным ускорителем мультиплексировано. Включите функцию мультиплексирования для дистанционного управления дроссельной заслонки. |
| Лампы работают **не**. | Фьюжн не сработал. | Проверьте предохранители и убедитесь, что ECM получает питание на проводе переключателя зажигания. |
| Лампы работают **не**. | Транспортное средство имеет мультиплексные лампы, и функция мультиплексирования выключена. | Убедитесь, что лампы мультиплексированы. Включите функцию мультиплексирования для ламп. |
| Тормоза двигателя работают **не**. | Транспортное средство имеет мультиплексные тормозные выключатели двигателя, и функция мультиплексирования выключена. | Убедитесь, что переключатели тормозов двигателя мультиплексированы. Включите функцию мультиплексирования для переключателей тормозов двигателя. |
| Двигатель **не будет** реагировать на один или все переключатели оператора. | Транспортное средство имеет мультиплексные переключатели, и функция мультиплексирования выключена. | Убедитесь, что переключатели мультиплексированы. Включите функцию мультиплексирования для переключателей. |


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> This procedure was developed due to the increasing number of parameters and features offered which can affect vehicle performance. Use the following table to troubleshoot performance complaints by locating the appropriate symptom in the left column. Then follow the probable cause and corrective action in the adjacent columns.
>
> Adjust the features or parameters with the recommended Cummins® electronic service tool or equivalent.
>
> ### Adjust
>
> | Programmable Feature/Parameters Not Correct |  |  |
> |---|---|---|
> | Symptom | Probable Cause | Correction |
> | Exceeding road speed governor set speed down hills | Cruise control or road speed governor lower droop is set too high. | Change the cruise control or road speed governor lower droop to a lower value. If the problem continues, change the cruise control engine brake activation to a lower value. |
> | Poor acceleration up hills | Cruise control and/or road speed governor upper droop is set too high. | Change the cruise control or road speed governor upper droop to a lower value. |
> | Cruise control turns on automatically. | Cruise control auto-resume feature is enabled. | Turn off the cruise control auto-resume feature. |
> | Exhaust brakes turn on automatically. | Cruise control auto engine brake feature is enabled or exhaust brake switch is failed. | Turn off the cruise control auto engine brake feature or repair the switch. |
> | Unable to obtain maximum vehicle speed. | Gear-down protection feature is enabled. | Turn off or adjust the gear-down protection parameters. |
> | Poor clutch engagement | The low idle speed is set too low for the application. | Increase the low-idle speed using the idle adjust switch. [[99-019-052 — Idle Adjust Switch\|Refer to Procedure 019-052]]. Increase the low-idle speed parameter. |
> | Speedometer on the dashboard is **not** correct or vehicle exceeding road speed governor set speed. | Vehicle speed parameters are **not** set properly. | Make sure the following are correct: tire size, rear axle ratio, vehicle speed sensor type, and gear teeth per revolution. |
> | Trip information mileage readings are **not** correct. | The tire size parameter was changed without resetting the trip information system. | Set the trip information system again whenever the tire size parameter is changed. |
> | Can **not** obtain maximum vehicle speed with semiautomatic transmission. | The gear-down protection parameters are **not** set properly. | Change the top gear ratio parameter to be equal to the first gear-down ratio, **not** the top gear ratio. For example, on a transmission with a 0.75, 0.87, and 1.0 ratio set, the top gear ratio parameter **must** be set to 0.87. |
> | Engine won't start. | Antitheft password is active. | Enter antitheft personal identification number (PIN) using RoadRelay™ or delete password with Zap-It. |
> | Low power in lower gears or top gear | Power train protection parameters are set too low. | Change power train protection torque limits to match torque capability of the vehicle's transmission. |
> | Semiautomatic transmission will **not** shift into top gear. | Top gear ratio setting does **not** match top gear of transmission. | Set the proper top gear ratio. |
> | Centinel™ feature has been turned on but vehicle has a Spicer Top 2™ transmission. | Feature and parameters are **not** set properly. | Turn off the Centinel™ feature and turn on the Top 2 feature. |
> | Engine recently started overheating because the fan will **not** turn on. | Fan control feature is **not** set properly. | Verify all fan control feature parameters are properly set for the vehicle. |
> | Fan will **not** turn off. | Fan control feature is **not** set properly. | Verify all fan control feature parameters are properly set for the vehicle. |
> | Fan control switch will **not** turn on the fan. | Fan control 1 accessory switch control is turned off. | Turn on fan control 1 accessory switch control. |
> | Unable to obtain maximum vehicle speed. | Cruise control maximum vehicle speed or accelerator maximum vehicle speed is **not** set high enough. | Verify or change settings. |
> | Driver reward system is penalizing the driver with reduced top vehicle speed or cruise control maximum speed for poor fuel economy or extended idle time. | Driver is unfamiliar with feature or feature and parameters are **not** set properly. | Explain feature to the driver or change parameter settings to more appropriate values. |
> | Accelerator pedal has no effect on engine speed. | Vehicle is in PTO mode and PTO accelerator override is turned on in the ECM. | Turn off PTO accelerator override. |
> | Accelerator pedal has no effect on engine speed. | Vehicle has a multiplexed throttle pedal and the multiplexing feature is turned off. | Verify that the throttle pedal is multiplexed. Turn on the multiplexing feature for the throttle pedal. |
> | Remote accelerator control has no effect on engine speed. | Remote accelerator feature is turned off. | Turn on the remote accelerator feature. |
> | Remote accelerator control has no effect on engine speed. | Vehicle has a multiplexed remote accelerator control and the multiplexing feature is turned off. | Verify that the remote accelerator control is multiplexed. Turn on the multiplexing feature for the remote throttle control. |
> | Lamps do **not** operate. | Fuse is failed. | Check fuses and verify the ECM is getting power on the keyswitch wire. |
> | Lamps do **not** operate. | Vehicle has multiplexed lamps and the multiplexing feature is turned off. | Verify that the lamps are multiplexed. Turn on the multiplexing feature for the lamps. |
> | Engine brakes do **not** operate. | Vehicle has multiplexed engine brake switches and the multiplexing feature is turned off. | Verify that the engine brake switches are multiplexed. Turn on the multiplexing feature for the engine brake switches. |
> | Engine will **not** respond to one or all of the operator's switch(es). | Vehicle has multiplexed switches and the multiplexing feature is turned off. | Verify that the switches are multiplexed. Turn on the multiplexing feature for the switches. |
