---
aliases:
  - "Информационные коды неисправностей"
type: "Процедура"
doc: "82-ifctabl"
title_en: "Information fault Codes"
title_ru: "Информационные коды неисправностей"
modified: "2002-06-28"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-ifctabl.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-ifctabl.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Information fault Codes
**Информационные коды неисправностей**

> [!abstract] Процедура · `82-ifctabl`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2002-06-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-ifctabl.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-ifctabl.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


> [!note] Примечание
> Коды ошибок информации имеют простые корректирующие действия и не имеют дерева устранения неисправностей кода. SRT 00-394 применяется ко всем кодам ошибок, перечисленным ниже. После исправления состояния, вызвавшего неисправность, пусть двигатель прогреется; затем пусть двигатель работает в течение 1 минуты, чтобы инактивировать код неисправности. Затем используйте INSITETM для очистки кода ошибки.

КОД:

143

Лэмп:

желтый

Причина:

Сигнал давления масла указывает на то, что давление масла ниже предела защиты двигателя низкого давления.

Последствие:

Прогрессивная мощность и скорость снижаются с увеличением времени после оповещения. Если функция защиты двигателя включена, двигатель отключается через 30 секунд после того, как красная лампа начинает мигать.

Действие:

См. процедуру устранения неполадок при симптомах низкого давления в руководстве по устранению неполадок и ремонту серии ISM/QSM11, Бюллетень No. [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]-00.

КОД:

151

Лэмп:

красный

Причина:

Сигнал температуры охлаждающей жидкости указывает на температуру выше 104 ° C (220° F).

Последствие:

Прогрессивная сила уменьшается с увеличением времени после оповещения. Если функция защиты двигателя включена, двигатель отключается через 30 секунд после того, как красная лампа начинает мигать.

Действие:

См. процедуру устранения неполадок при высоких температурах охлаждения в руководстве по устранению неполадок и ремонту двигателей серии ISM/QSM11, Бюллетень No. [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]-00.

КОД:

155

Лэмп:

красный

Причина:

Сигнал температуры коллектора потребления указывает на температуру выше 93 ° C (200° F).

Последствие:

Прогрессивная сила уменьшается с увеличением времени после оповещения. Если функция защиты двигателя включена, двигатель отключается через 30 секунд после того, как красная лампа начинает мигать.

Действие:

См. процедуру устранения неполадок при высоком уровне потребления в руководстве по устранению неполадок и ремонту двигателей серии ISM/QSM11, Бюллетень No. [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]-00.

КОД:

211

Лэмп:

Нет

Причина:

Были зарегистрированы дополнительные OEM-коды или диагностические коды транспортных средств. Проверьте другие ECM для диагностических кодов.

Последствие:

Ни одного по производительности двигателя.

Действие:

См. соответствующее руководство OEM для помощи в устранении неполадок по этой вине.

КОД:

214

Лэмп:

красный

Причина:

Сигнал температуры масла указывает на температуру масла выше 123,9 ° C (255 ° F).

Последствие:

Прогрессивная сила уменьшается с увеличением времени после оповещения. Если функция защиты двигателя включена, двигатель отключается через 30 секунд после того, как красная лампа начинает мигать.

Действие:

См. процедуру устранения неполадок при высоких температурах масла в руководстве по устранению неполадок и ремонту двигателей серии ISM/QSM11, Бюллетень No. [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]-00.

КОД:

219

Лэмп:

Техническое обслуживание

Причина:

Низкий уровень масла был обнаружен в масляном резервуаре для макияжа CentinelTM.

Последствие:

Ни одного на выступление. Система CentinelTM отключена.

Действие:

Добавьте моторное масло в масляный бак CentinelTM. Если неисправность остается активной с полным масляным баком, удалите и очистите датчик уровня масла.

КОД:

287

Лэмп:

красный

Причина:

Электронный блок управления OEM-автомобиля (VECU) обнаружил неисправность с педалью дроссельной заслонки.

Последствие:

Двигатель будет только простаивать.

Действие:

См. руководство изготовителя машины по диагностике и ремонту. Устранение неполадок педалью ускорителя, подключенной к электронному блоку управления транспортным средством (VECU), поставляемому OEM.

КОД:

288

Лэмп:

красный

Причина:

Электронный блок управления OEM-автомобиля (VECU) обнаружил неисправность с помощью дистанционного дросселя.

Последствие:

Двигатель не будет реагировать на удаленный дроссел.

Действие:

См. руководство изготовителя машины по диагностике и ремонту. Устранение неполадок с помощью педали дистанционного дроссельного заслонка, подключенной к электронному блоку управления транспортным средством (VECU), поставляемому OEM.

КОД:

295

Лэмп:

желтый

Причина:

Ошибка в сигнале датчика давления окружающего воздуха была обнаружена ECM.

Последствие:

Двигатель отнесен к параметрам без воздуха.

Действие:

Проверить значение давления окружающего воздуха от 25,0 в Hg до 30,5 в Hg с помощью INSITETM. При необходимости заменяйте датчик давления воздуха в окружающей среде.

КОД:

299

Лэмп:

желтый

Причина:

Двигатель был выключен устройством, отличным от переключателя зажигания, до того, как надлежащий двигатель остыл, что привело к фильтрованному коэффициенту нагрузки выше максимального порога выключения.

Последствие:

Никаких действий со стороны ЕКМ не предпринималось.

Действие:

КОД:

415

Лэмп:

красный

Причина:

Сигнал давления масла указывает на давление масла ниже очень низкого предела защиты двигателя от давления масла.

Последствие:

Прогрессивная сила уменьшается с увеличением времени после оповещения. Если функция защиты двигателя включена, двигатель отключается через 30 секунд после того, как красная лампа начинает мигать.

Действие:

См. процедуру устранения неполадок при симптомах низкого давления в руководстве по устранению неполадок и ремонту двигателей серии ISM/QSM11, Бюллетень No. [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]-00.

КОД:

418

Лэмп:

Техническое обслуживание

Причина:

В топливном фильтре обнаружена вода.

Последствие:

Возможен белый дым, потеря энергии или жесткий старт.

Действие:

Сливать воду из топливного фильтра. См. процедуру устранения неполадок в симптомах воды в топливе в руководстве по устранению неполадок и ремонту двигателей серии ISM/QSM11, Бюллетень No. [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]-00, если неисправность повторяется часто.

КОД:

419

Лэмп:

желтый

Причина:

Ошибка в сигнале датчика давления впускного коллектора была обнаружена ECM.

Последствие:

Двигатель отнесен к параметрам без воздуха.

Действие:

Проверить значение давления впускного коллектора от -2,5 в рт.ст. до 2,5 в рт.ст. с помощью INSITETM. При необходимости заменить датчик давления/температуры впускного коллектора.

КОД:

435

Лэмп:

желтый

Причина:

Ошибка в сигнале датчика давления масла была обнаружена ECM.

Последствие:

Ни одного на выступление. Отсутствие защиты двигателя от давления масла.

Действие:

Проверка клапана давления масла составляет от -1,5 psi до 4,0 psi, когда двигатель прекращает работу с помощью INSITETM. При необходимости заменяйте датчик давления/температуры масла.

КОД:

471

Лэмп:

желтый

Причина:

Низкий уровень масла в картере был обнаружен ECM.

Последствие:

Ни одного на выступление. Система CentinelTM деактивирована.

Действие:

КОД:

595

Лэмп:

желтый

Причина:

Неисправность защиты от перегрузки турбокомпрессором.

Последствие:

Двигатель будет работать в сжатом состоянии.

Действие:

См. процедуру устранения неполадок с симптомами высокой скорости турбокомпрессора в руководстве по устранению неполадок и ремонту двигателей серии ISM/QSM11, Бюллетень No. [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]-00.

КОД:

611

Лэмп:

Нет

Причина:

Отключение двигателя оператором перед охлаждением правильного двигателя, что приводит к коэффициенту фильтрованной нагрузки выше максимального порога отключения.

Последствие:

Никаких действий со стороны ЕКМ не предпринималось.

Действие:

Смотрите процедуры устранения неполадок с симптомом горячего отключения.

КОД:

775

Лэмп:

Техническое обслуживание

Причина:

Медленная утечка была обнаружена в воздушной системе.

Последствие:

Ни одного на выступление.

Действие:

Проверьте систему воздушного транспорта на наличие утечек. См. раздел 012-019 в руководстве по устранению неполадок и ремонту двигателей серии ISM/QSM11, Бюллетень No. [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]-00.

КОД:

776

Лэмп:

желтый

Причина:

В воздушной системе обнаружена быстрая утечка.

Последствие:

Ни одного на выступление.

Действие:

Проверьте систему воздушного транспорта на наличие утечек. См. раздел 012-019 в руководстве по устранению неполадок и ремонту двигателей серии ISM/QSM11, Бюллетень No. [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]-00.

КОД:

951

Лэмп:

Нет

Причина:

Дисбаланс мощности между цилиндрами был обнаружен ECM.

Последствие:

Двигатель может иметь грубое бездействие или осечку.

Действие:

Проверьте качество топлива. Проверьте, не попадает ли воздух в топливо. Нормально иметь неактивный код 951 по умолчанию после процедуры подачи воздуха в топливную систему, например, изменения фильтра. Выполните испытание производительности цилиндра, чтобы определить, является ли конкретный цилиндр или цилиндры с высокой или низкой мощностью. См. процедуру 014-008 Испытание на эффективность цилиндров в руководстве по устранению неполадок и ремонту двигателей серии ISM/QSM11, Бюллетень No. [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]-00.


> [!quote]- Original (English) · английский оригинал
> **Note · Примечание**
> - Information Fault Codes have simple, corrective actions and no fault code troubleshooting tree. - SRT 00-394 applies to all of the Information Fault Codes listed below. - After correcting the condition that caused the fault, let the engine warm up; then let the engine run for 1 minute to inactivate the fault code. Then, use INSITE™ to clear the fault code.
>
> CODE:
>
> 143
>
> LAMP:
>
> Yellow
>
> REASON:
>
> Oil pressure signal indicates oil pressure is below the low-pressure engine protection limit.
>
> EFFECT:
>
> Progressive power and speed derate with increasing time after alert. If engine protection shutdown feature is enabled, engine will shut down 30 seconds after the red lamp starts flashing.
>
> ACTION:
>
> Refer to the Low Oil Pressure symptom troubleshooting procedure in the ISM/QSM11 Series Engines, Troubleshooting and Repair Manual, Bulletin No. [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]-00.
>
> CODE:
>
> 151
>
> LAMP:
>
> Red
>
> REASON:
>
> Coolant temperature signal indicates temperature is above 104°C (220°F).
>
> EFFECT:
>
> Progressive power derate with increasing time after alert. If engine protection shutdown feature is enabled, engine will shut down 30 seconds after the red lamp starts flashing.
>
> ACTION:
>
> Refer to the High Coolant Temperature symptom troubleshooting procedure in the ISM/QSM11 Series Engines Troubleshooting and Repair Manual, Bulletin No. [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]-00.
>
> CODE:
>
> 155
>
> LAMP:
>
> Red
>
> REASON:
>
> Intake manifold temperature signal indicates temperature is above 93°C (200°F).
>
> EFFECT:
>
> Progressive power derate with increasing time after alert. If engine protection shutdown feature is enabled, engine will shut down 30 seconds after the red lamp starts flashing.
>
> ACTION:
>
> Refer to the High Intake Manifold Temperature symptom troubleshooting procedure in the ISM/QSM11 Series Engines Troubleshooting and Repair Manual, Bulletin No. [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]-00.
>
> CODE:
>
> 211
>
> LAMP:
>
> None
>
> REASON:
>
> Additional OEM or vehicle diagnostic codes have been logged. Check other ECMs for diagnostic codes.
>
> EFFECT:
>
> None on engine performance.
>
> ACTION:
>
> Refer to the appropriate OEM manual for assistance in troubleshooting this fault.
>
> CODE:
>
> 214
>
> LAMP:
>
> Red
>
> REASON:
>
> Oil temperature signal indicates oil temperature is above 123.9°C (255°F).
>
> EFFECT:
>
> Progressive power derate with increasing time after alert. If engine protection shutdown feature is enabled, engine will shut down 30 seconds after the red lamp starts flashing.
>
> ACTION:
>
> Refer to the High Oil Temperature symptom troubleshooting procedure in the ISM/QSM11 Series Engines Troubleshooting and Repair Manual, Bulletin No. [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]-00.
>
> CODE:
>
> 219
>
> LAMP:
>
> Maintenance
>
> REASON:
>
> Low oil level was detected in the Centinel™ makeup oil tank.
>
> EFFECT:
>
> None on performance. Centinel™ system deactivated.
>
> ACTION:
>
> Add engine oil to the Centinel™ makeup oil tank. If fault remains active with a full oil tank, remove and clean the oil level sensor.
>
> CODE:
>
> 287
>
> LAMP:
>
> Red
>
> REASON:
>
> The OEM vehicle electronic control unit (VECU) detected a fault with its throttle pedal.
>
> EFFECT:
>
> The engine will only idle.
>
> ACTION:
>
> Refer to the OEM troubleshooting and repair manual. Troubleshoot the accelerator pedal connected to the OEM supplied vehicle electronic control unit (VECU).
>
> CODE:
>
> 288
>
> LAMP:
>
> Red
>
> REASON:
>
> The OEM vehicle electronic control unit (VECU) detected a fault with its remote throttle.
>
> EFFECT:
>
> The engine will NOT respond to the remote throttle.
>
> ACTION:
>
> Refer to the OEM Troubleshooting and Repair Manual. Troubleshoot the remote throttle pedal connected to the OEM supplied vehicle electronic control unit (VECU).
>
> CODE:
>
> 295
>
> LAMP:
>
> Yellow
>
> REASON:
>
> An error in the ambient air pressure sensor signal was detected by the ECM.
>
> EFFECT:
>
> Engine is derated to no-air setting.
>
> ACTION:
>
> Verify ambient air pressure value is from 25.0 in Hg to 30.5 in Hg using INSITE™. Replace ambient air pressure sensor if necessary.
>
> CODE:
>
> 299
>
> LAMP:
>
> Yellow
>
> REASON:
>
> The engine was shut down by a device other than the keyswitch before the proper engine cool down resulting in a filtered load factor above the maximum shutdown threshold.
>
> EFFECT:
>
> No action taken by the ECM.
>
> ACTION:
>
> CODE:
>
> 415
>
> LAMP:
>
> Red
>
> REASON:
>
> Oil pressure signal indicates oil pressure below the very low oil pressure engine protection limit.
>
> EFFECT:
>
> Progressive power derate with increasing time after alert. If engine protection shutdown feature is enabled, engine will shut down 30 seconds after the red lamp starts flashing.
>
> ACTION:
>
> Refer to the Low Oil Pressure symptom troubleshooting procedure in the ISM/QSM11 Series Engines Troubleshooting and Repair Manual, Bulletin No. [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]-00.
>
> CODE:
>
> 418
>
> LAMP:
>
> Maintenance
>
> REASON:
>
> Water has been detected in the fuel filter.
>
> EFFECT:
>
> Possible white smoke, loss of power, or hard starting.
>
> ACTION:
>
> Drain water from fuel filter. Refer to the Water in Fuel symptom troubleshooting procedure in the ISM/QSM11 Series Engines Troubleshooting and Repair Manual, Bulletin No. [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]-00, if fault reoccurs frequently.
>
> CODE:
>
> 419
>
> LAMP:
>
> Yellow
>
> REASON:
>
> An error in the intake manifold pressure sensor signal was detected by the ECM.
>
> EFFECT:
>
> Engine is derated to no-air setting.
>
> ACTION:
>
> Verify intake manifold pressure value is from -2.5 in Hg to 2.5 in Hg using INSITE™. Replace intake manifold pressure/temperature sensor if necessary.
>
> CODE:
>
> 435
>
> LAMP:
>
> Yellow
>
> REASON:
>
> An error in the oil pressure sensor signal was detected by the ECM.
>
> EFFECT:
>
> None on performance. No engine protection for oil pressure.
>
> ACTION:
>
> Verify oil pressure valve is from -1.5 psi to 4.0 psi when the engine is stopped using INSITE™. Replace oil pressure/temperature sensor if necessary.
>
> CODE:
>
> 471
>
> LAMP:
>
> Yellow
>
> REASON:
>
> Low crankcase oil level was detected by the ECM.
>
> EFFECT:
>
> None on performance. Centinel™ system is deactivated.
>
> ACTION:
>
> CODE:
>
> 595
>
> LAMP:
>
> Yellow
>
> REASON:
>
> Turbocharger overspeed protection fault.
>
> EFFECT:
>
> The engine will run derated.
>
> ACTION:
>
> Refer to the High Turbocharger Speed symptom troubleshooting procedure in the ISM/QSM11 Series Engines Troubleshooting and Repair Manual, Bulletin No. [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]-00.
>
> CODE:
>
> 611
>
> LAMP:
>
> None
>
> REASON:
>
> Engine shutdown by operator before the proper engine cool down, resulting in filtered load factor above maximum shutdown threshold.
>
> EFFECT:
>
> No action taken by the ECM.
>
> ACTION:
>
> Refer to the Hot Shutdown symptom troubleshooting procedures.
>
> CODE:
>
> 775
>
> LAMP:
>
> Maintenance
>
> REASON:
>
> A slow leak has been detected in the air system.
>
> EFFECT:
>
> None on performance.
>
> ACTION:
>
> Check the vehicle air system for leaks. Refer to Section 012-019 in the ISM/QSM11 Series Engines Troubleshooting and Repair Manual, Bulletin No. [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]-00.
>
> CODE:
>
> 776
>
> LAMP:
>
> Yellow
>
> REASON:
>
> A fast leak has been detected in the air system.
>
> EFFECT:
>
> None on performance.
>
> ACTION:
>
> Check the vehicle air system for leaks. Refer to Section 012-019 in the ISM/QSM11 Series Engines Troubleshooting and Repair Manual, Bulletin No. [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]-00.
>
> CODE:
>
> 951
>
> LAMP:
>
> None
>
> REASON:
>
> A power imbalance between cylinders was detected by the ECM.
>
> EFFECT:
>
> Engine can possibly have rough idle or misfire.
>
> ACTION:
>
> Check fuel quality. Check for air being ingested by the fuel. It is normal to have an inactive Fault Code 951 after a service procedure introduced air into the fuel system, such as a filter change. Perform Cylinder Performance Test to determine if a particular cylinder or cylinders are high or low on power. Refer to Procedure 014-008 Cylinder Performance Test in the ISM/QSM11 Series Engines Troubleshooting and Repair Manual, Bulletin No. [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]-00.
