---
type: "Процедура"
doc: "101-014-013"
title_en: "Aftertreatment Testing"
modified: "2010-08-04"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
figures: 14
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/101/101-014-013.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/101-014-013.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/101"
  - "перевод/машинный"
---

# Aftertreatment Testing

> [!abstract] Процедура · `101-014-013`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 14 - Engine Testing - Group 14
> **Даты:** изменён 2010-08-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/101/101-014-013.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/101-014-013.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Испытание на ускорение Snap используется для проверки фильтра для очистки дизельных частиц на наличие трещин или других прогрессирующих повреждений, без удаления системы фильтрации. Он используется для проверки функциональности фильтра для твердых частиц дизельного топлива после обработки.

Для проведения стационарного регенерационного теста фильтра дизельных частиц INSITETM используется электронное оборудование:

- Регенерировать фильтр для дизельных частиц после обработки
- Восстановить после обработки дизельный катализатор окисления и после обработки дизельный фильтр твердых частиц после загрязнения охлаждающей жидкостью
- Проверьте эффективность катализатора окисления дизельного топлива после обработки
- Проверьте правильность установки датчиков температуры после обработки
- Сброс накопленной сажи в двигателе ECM
- Проверьте послеочистку топливного форсунка, запорный клапан и функциональность поезда.

Проверяйте активные коды неисправностей перед выполнением любой из этих процедур. Если присутствуют какие-либо активные коды неисправностей, следуйте соответствующему дереву устранения неисправностей кода неисправностей.

![[11c00245.png]]

Электронное сервисное оборудование INSITETM После обработки Дизельный фильтр твердых частиц Стационарный тест на регенерацию может быть использован для восстановления функциональности катализатора окисления дизельного топлива (DOC) и Дизельный фильтр твердых частиц после обработки (DPF) после того, как либо или оба подверглись воздействию охлаждающей жидкости.

> [!note] Примечание
> Если DOC и DPF подозреваются в загрязнении охлаждающей жидкости, их не нужно удалять и проверять. Проконсультируйтесь с разделом подготовительных шагов этой процедуры для получения дополнительной информации.

Температура, которая достигается во время регенерации, достаточно высока, чтобы испарить охлаждающую жидкость из обоих компонентов и вернуть оба компонента к нормальным эксплуатационным характеристикам.

> [!note] Примечание
> Если эти компоненты подозреваются в загрязнении охлаждающей жидкостью, не выполняйте тест ускорения перед выполнением регенерации.

![[11c00245.png]]

В этом разделе описывается проверка выпускных выпусков системы выхлопных газов.

Проверка выпускной отверстия выхлопной системы может выявить состояние фильтра для твердых частиц дизельного топлива после обработки. Выход выхлопной системы должен выглядеть чистым с небольшим или нулевым остатком выхлопных газов / накоплением сажи.

Последующая обработка дизельного фильтра твердых частиц **не** на 100% эффективна. Некоторое накопление остатка выхлопных газов / сажи является нормальным и не указывает на неисправность фильтра твердых частиц дизельного топлива после обработки.

Тяжелое накопление остатка выхлопных газов/сажи может указывать на неисправность фильтра для твердых частиц дизельного топлива после обработки.

Для определения того, является ли накопление остатка выхлопных газов/сажи на выпускной розетке выхлопной системы результатом неисправной после обработки фильтра для твердых частиц дизельного топлива, выполните одно из следующих действий:

1. Тест на ускорение Snap, описанный в этой процедуре.
2. Очистить последние 152 до 254 мм \[6 до 10 в\] выпускной системы выхлопной системы. Управляйте транспортным средством в течение одной смены или поездки и проверяйте выпуск выхлопной системы на предмет накопления остатков выхлопных газов/сажи.
3. Проверить фильтр для твердых частиц дизельного топлива после обработки.

![[14d00033.png]]

#### Тест на ускорение Snap

- Трансмиссия транспортного средства должна быть нейтральной.
- При этом необходимо использовать стояночный тормоз.

Запуск и запуск двигателя на холостом ходу.

Быстро нажимайте педаль акселератора с 0 до 100 процентов. При необходимости это можно сделать несколько раз.

![[14c00079.png]]

Во время этого испытания визуально проверьте наличие черного дыма, выходящего из выхлопной трубы, так как двигатель ускоряется от низкого холостого хода до высокого холостого хода.

> [!note] Примечание
> В некоторых случаях испытание на ускорение с помощью защелки может **не** обеспечить условия, необходимые для выявления неисправного фильтра твердых частиц дизельного топлива после обработки. Если на выходе выхлопной системы происходит сильное накопление остатка выхлопных газов / сажи и ускорение по щелчку показывает **не **состояние, изложенное в следующих шагах, может потребоваться выполнить:

- Тест на кабинку.[[101-014-008 — Engine Testing (In Chassis)|См. процедуру 014-008 в разделе 14.]]
- Короткое ускорение проходит под частичной до полной нагрузки.

См. Катализатор и после обработки фильтра твердых частиц повторное использование Руководство, бюллетень[[4021600 — Aftertreatment Diesel Oxidation Catalyst (DOC) and Aftertreatment Diesel Particulate|4021600]]Для прохождения или провала руководящих принципов.

![[11c00246.png]]

Если присутствует серый дым или слабый черный дым, обратитесь к рекомендациям по повторному использованию фильтра твердых частиц и после обработки.[[4021600 — Aftertreatment Diesel Oxidation Catalyst (DOC) and Aftertreatment Diesel Particulate|4021600]]Для прохождения или провала руководящих принципов.

Белый дым во время теста на ускорение затмения не указывает на сбой. Ремонт не требуется.

![[11c00247.png]]

### Подготовительные операции

> [!danger] ОПАСНО
> Во время регенерации температура выхлопных газов может достигать 800 ° C \[1500 ° F \], а температура поверхности выхлопной системы может превышать 700° C \[1300° F \], которая достаточно горячая, чтобы воспламенить или расплавить обычные материалы и вызвать серьезные ожоговые травмы. Выхлопные и выхлопные компоненты могут оставаться горячими после того, как транспортное средство перестало двигаться. Чтобы избежать риска пожара, повреждения имущества, ожогов или других серьезных травм, позвольте выхлопной системе остыть перед началом этой процедуры или ремонта и убедитесь, что горючие материалы не находятся там, где они могут вступать в контакт с горячими выхлопными газами или компонентами выхлопных газов.

Для выполнения стационарной регенерации подключите инструмент электронного сервиса INSITETM и проверьте активные коды неисправностей. Если коды неисправностей присутствуют, кроме кодов 2639 или 1921, перед началом работы перейдите в раздел TF для устранения неисправностей кода неисправности. Не выполнять регенерацию с активными кодами неисправностей, отличными от кодов 2639 или 1921, если только это не указано в руководстве по устранению неисправностей кода неисправности.

> [!note] Примечание
> Если стационарная регенерация выполняется для восстановления либо DOC, либо DPF, либо обоих после загрязнения охлаждающей жидкостью, DOC не нужно удалять или проверять, если нет активных кодов неисправностей, которые требуют проверки в рамках шагов по устранению неисправностей кода неисправности.

> [!note] Примечание
> Если во время работы не поступают жалобы на черный дым и выхлопная труба черная, DPF не требуется удалять или проверять во время этого процесса.

Перед выполнением стационарной регенерации выполните шаги, перечисленные ниже:

1. Выберите подходящее место для парковки автомобиля.
2. Припаркуйте грузовик надежно.
3. Установите безопасную зону выхлопа.
4. Проверьте поверхности выхлопной системы.
5. Готовьтесь к изменениям скорости двигателя во время регенерации.
6. Начните стационарную регенерацию. Это можно сделать двумя способами:
7. Следите за районом.

Чтобы остановить стационарную регенерацию, включите сцепление, тормоз или педаль дросселя; или выключите двигатель.

После завершения регенерации температура выхлопных газов и поверхности выхлопных газов будет оставаться повышенной в течение 3-5 минут.

![[ck800wa.png]]

### Настройка

Запуск и запуск двигателя на холостом ходу.

Перед проведением испытания на регенерацию дизельного фильтра твердых частиц проверьте выхлопные трубы на наличие утечек, трещин и рыхлых соединений.

- Для двигателей ISM используйте следующую процедуру.[[35-010-024-tr — Air Leaks, Air Intake and Exhaust Systems|См. процедуру 010-024 в разделе 10.]]
- Для двигателей ISX используйте следующую процедуру. См. процедуру 010-024 в разделе 10.
- Для двигателей ISX11.9 используйте следующую процедуру: См. процедуру 010-024 в разделе 10.
- Для двигателей ISX15 используйте следующую процедуру: См. процедуру 010-024 в разделе 10.

При необходимости затягивайте выхлопные зажимы.

Проконсультируйтесь со спецификациями OEM для правильного значения крутящего момента.

Любые утечки в выхлопной системе приведут к тому, что тест на регенерацию дизельного фильтра будет менее эффективным в снижении нагрузки фильтра на сажу.

![[10d00395.png]]

### Проверка

Тест на регенерацию дизельного фильтра после обработки можно найти в меню «Диагностический тест ECM» в инструменте электронного обслуживания INSITETM.

![[19c00691.png]]

Если электронный сервисный инструмент INSITETM недоступен, некоторые транспортные средства могут быть оснащены стационарным переключателем регенерации в кабине. Переключатель может быть автономным переключателем или может быть объединен с диагностическим переключателем. Проверьте с OEM местоположение и доступность коммутатора.

> [!note] Примечание
> Для того чтобы переключатель регенерации работал, в ECM должен быть включен переключатель регенерации.

В отличие от теста на регенерацию дизельного фильтра с использованием электронного сервисного инструментария INSITETM, этот переключатель будет **только **запускать стационарную регенерацию, если нагрузка сажи фильтра достаточно высока. Это указывается при освещении или мигании лампы после обработки.

> [!note] Примечание
> Стационарная регенерация может быть инициирована **не** с помощью кабины-переключателя, если включено ингибирование регенерации. Электронный сервисный инструмент INSITETM должен быть использован для инициирования стационарной регенерации.

![[14d00035.png]]

> [!note] Примечание
> Если после лечения дизельный фильтр для твердых частиц будет **не **инициировать, используйте стационарную регенерацию - не начнет устранение неполадок дерево симптомов.

Когда испытание начнется, скорость холостого хода двигателя будет автоматически повышена до необходимого уровня. Ожидаемая скорость двигателя может достигать от 1000 до 1500 об/мин.

Затем двигатель будет работать таким образом, чтобы вырабатывать выхлопное тепло. Турбокомпрессор может издавать небольшой «свистящий» шум во время испытания. Это нормально.

Регенерация дизельного фильтра может занять до двух с половиной часов, в зависимости от загрузки сажи фильтра, а также условий окружающей среды, таких как, но не ограничиваясь температурой и влажностью.

После завершения испытаний на регенерацию дизельного фильтра дизельных частиц двигатель автоматически вернется к нормальной скорости холостого хода.

![[10900098.png]]

Во время испытания на регенерацию дизельного фильтра для твердых частиц после обработки будут контролироваться следующие элементы:

- Статус форсунки после обработки - информирует пользователя о том, когда топливо впрыскивается в небольшом количестве в выхлопную систему выше по потоку от катализатора окисления дизельного топлива
- После обработки температура выхода дизельного фильтра
- После обработки дизельный фильтр твердых частиц температура входа
- После обработки Diesel Oxidation Catalyst температура входа
- После обработки дизельный фильтр сажи фильтра сажи - информирует пользователя о текущей нагрузке сажи фильтра:

![[11d00240.png]]

> [!warning] ОСТОРОЖНО
> Во время стационарной регенерации температура выхлопных газов может достигать 800 ° C \[1500 ° F \], а температура поверхности может превышать 700° C \[1300° F \].

Стационарная регенерация может занять до 2-1/2 часов, в зависимости от загрузки сажи фильтра. В любое время стационарную регенерацию можно прервать, нажав на кнопку «Стоп» в инструменте электронного сервиса INSITETM.

Регенерация будет прекращена, если:

- Неисправность становится активной
- Ускоритель находится в депрессии
- Педаль сцепления находится в депрессии
- Педаль тормоза находится в депрессии
- Трансмиссия переводится в снаряжение.

> [!note] Примечание
> Если стационарная регенерация может быть инициирована или прервана, а двигатель имеет жалобу на низкую мощность, используйте следующие процедуры.

- Для двигателей ISM используйте следующую процедуру.[[101-011-009-tr — Exhaust Restriction|См. процедуру 011-009 в разделе 11.]]
- Для двигателей ISX используйте следующую процедуру.[[101-011-009-tr — Exhaust Restriction|См. процедуру 011-009 в разделе 11.]]
- Для двигателей ISX11.9 используйте следующую процедуру: См. процедуру 011-009 в разделе 11.
- Для двигателей ISX15 используйте следующую процедуру: См. процедуру 011-009 в разделе 11.

#### Пройти или не пройти критерии

- Пропуск: Процедура тестирования после обработки 014-013 в разделе 14 прошла, если не видно черного дыма и неподвижная регенерация завершается без генерирования кодов неисправностей после обработки.
- Неудача: Процедура тестирования после обработки 014-013 в разделе 14 не удалась, если есть видимый черный дым и/или генерируются коды неисправностей после обработки. Исправить причину черного дыма и/или исправить коды неисправностей.

![[19c00691.png]]

### Завершающие операции

Позвольте двигателю и выхлопной системе остыть. Температура может поддерживать повышенное состояние в течение нескольких минут.

Убедитесь, что лампа фильтра для дизельных частиц **не** освещена.

> [!note] Примечание
> Если лампа с фильтром для дизельных частиц подсвечивается и код поломки 2639 или 1921 все еще активен, потребуется вторая регенерация. Если неисправность все еще активна после второй регенерации, фильтр необходимо очистить от золы или сажи.

- Для двигателей ISM используйте следующую процедуру.[[101-011-041-tr — Aftertreatment Diesel Particulate Filter|См. процедуру 011-041 в разделе 11.]]
- Для двигателей ISX используйте следующую процедуру.[[101-011-041-tr — Aftertreatment Diesel Particulate Filter|См. процедуру 011-041 в разделе 11.]]
- Для двигателей ISX11.9 используйте следующую процедуру: См. процедуру 011-041 в разделе 11.
- Для двигателей ISX15 используйте следующую процедуру: См. процедуру 011-041 в разделе 11.

Проверьте наличие активных кодов неисправностей. Если присутствуют активные коды неисправностей, используйте раздел TF для устранения неисправностей кода неисправностей.

Используйте инструмент электронного сервиса INSITETM для очистки всех кодов неактивных ошибок.

![[11d00240.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The Snap-Acceleration Test is used to check the aftertreatment diesel particulate filter for cracks or other progressive damage, without removing the filter system. It is used to test the functionality of the aftertreatment diesel particulate filter.
>
> The INSITE™ electronic service tool Aftertreatment Diesel Particulate Filter Stationary Regeneration Test is used to:
>
> - Regenerate an aftertreatment diesel particulate filter
> - Recover the aftertreatment diesel oxidation catalyst and aftertreatment diesel particulate filter after coolant contamination
> - Check the aftertreatment diesel oxidation catalyst efficiency
> - Check for the correct installation of the aftertreatment temperature sensors
> - Reset the stored soot load in the engine ECM
> - Check the aftertreatment fuel injector, shutoff valve, and drive train functionality.
>
> Check for active fault codes prior to performing either of these procedures. If any active fault codes are present, follow the appropriate fault code troubleshooting tree.
>
> The INSITE™ electronic service tool Aftertreatment Diesel Particulate Filter Stationary Regeneration Test can be used to regain functionality of the Aftertreatment Diesel Oxidation Catalyst (DOC) and Aftertreatment Diesel Particulate Filter (DPF) after either, or both, have been exposed to coolant.
>
> **Note · Примечание**
> If the DOC and DPF are suspected of having coolant contamination, they do **not** need to be removed and inspected. Consult the Preparatory Steps section of this procedure for further details.
>
> The temperatures that are achieved during the Regeneration are high enough to evaporate the coolant out of both components and return both components to normal operating specifications.
>
> **Note · Примечание**
> If these components are suspected of having coolant contamination, do **not** perform the snap acceleration test before performing the regeneration.
>
> This section outlines the Exhaust System Outlet Inspection.
>
> Inspection of the exhaust system outlet can reveal the condition of the aftertreatment diesel particulate filter. The exhaust system outlet should appear clean with little to no exhaust residue/soot buildup.
>
> The aftertreatment diesel particulate filter is **not** 100 percent efficient. Some accumulation of exhaust residue/soot is normal, and does **not** indicate a malfunctioning aftertreatment diesel particulate filter.
>
> A heavy buildup of exhaust residue/soot can indicate a malfunction of the aftertreatment diesel particulate filter.
>
> To determine if the exhaust residue/soot accumulation on the exhaust system outlet is the result of a malfunctioning aftertreatment diesel particulate filter, perform one of the following:
>
> 1. Snap Acceleration Test as outlined in this procedure.
> 2. Clean the last 152 to 254 mm \[6 to 10 in\] of the exhaust system outlet. Operate the vehicle for one shift or trip and inspect the exhaust system outlet for exhaust residue/soot accumulation.
> 3. Inspect the aftertreatment diesel particulate filter.
>
> #### Snap Acceleration Test
>
> - The vehicle transmission **must** be in neutral.
> - The vehicle parking brake **must** be applied.
>
> Start and idle the engine.
>
> Rapidly depress the accelerator pedal from 0 percent to 100 percent. This can be performed multiple times, if necessary.
>
> During this test, visually check for black smoke exiting the exhaust stack, as the engine is accelerated from low idle to high idle
>
> **Note · Примечание**
> In some applications, a snap acceleration test may **not** provide the conditions necessary to reveal a malfunctioning aftertreatment diesel particulate filter. If there is a heavy buildup of exhaust residue/soot on the exhaust system outlet and a snap acceleration does **not** reveal a condition outlined in the following steps, it can be necessary to perform:
>
> - A stall test. [[101-014-008 — Engine Testing (In Chassis)|Refer to Procedure 014-008 in Section 14.]]
> - A brief acceleration run under partial to full load.
>
> Refer to the Catalyst and Aftertreatment Particulate Filter Reuse Guidelines, Bulletin [[4021600 — Aftertreatment Diesel Oxidation Catalyst (DOC) and Aftertreatment Diesel Particulate|4021600]], for pass or fail guidelines.
>
> If gray smoke or faint black smoke is present, refer to the Catalyst and Aftertreatment Particulate Filter Reuse Guidelines, Bulletin [[4021600 — Aftertreatment Diesel Oxidation Catalyst (DOC) and Aftertreatment Diesel Particulate|4021600]], for pass or fail guidelines.
>
> White smoke during the snap-acceleration test does **not** indicate a failure. No repair is necessary.
>
> ### Preparatory Steps
>
> **WARNING · Опасно**
> During regeneration, exhaust gas temperature could reach 800°C \[1500°F\] and exhaust system surface temperature can exceed 700°C \[1300°F\], which is hot enough to ignite or melt common materials, and cause severe burn injuries. The exhaust and exhaust components can remain hot after the vehicle stopped moving. To avoid the risk of fire, property damage, burns or other serious personal injury, allow the exhaust system to cool before beginning this procedure or repair and make sure that no combustible materials are located where they are likely to come in contact with hot exhaust or exhaust components.
>
> To perform a stationary regeneration, connect INSITE™ electronic service tool and check for active fault codes. If any fault codes are present other than Fault Codes 2639 or 1921, go to Section TF for any fault code troubleshooting before proceeding. Do **not** perform a stationary regeneration with active fault codes other than Fault Codes 2639 or 1921, unless guided to do so by the fault code troubleshooting.
>
> **Note · Примечание**
> If the stationary regeneration is being performed to recover either the DOC, the DPF, or both after coolant contamination, the DOC does **not** need to be removed or inspected unless there are active fault codes that require inspection as part of the fault code troubleshooting steps.
>
> **Note · Примечание**
> **Unless** there are complaints of black smoke during operation and the exhaust stack is black, the DPF does **not** need to be removed or inspected during this process.
>
> Before performing a stationary regeneration, follow the steps listed below:
>
> 1. Select an appropriate location to park the vehicle.
> 2. Park the truck securely.
> 3. Set up a safe exhaust area.
> 4. Check exhaust system surfaces.
> 5. Prepare for engine speed changes during regeneration.
> 6. Begin the stationary regeneration. This can be performed in two ways:
> 7. Monitor the area.
>
> To stop a stationary regeneration, engage the clutch, brake, or throttle pedal; or turn off the engine.
>
> Once regeneration is complete, exhaust gas and exhaust surface temperatures will remain elevated for 3 to 5 minutes.
>
> ### Setup
>
> Start and idle the engine.
>
> Prior to the Aftertreatment Diesel Particulate Filter Regeneration Test, inspect the exhaust piping for leaks, cracks, and loose connections.
>
> - For ISM engines, use the following procedure. [[35-010-024-tr — Air Leaks, Air Intake and Exhaust Systems|Refer to Procedure 010-024 in Section 10.]]
> - For ISX engines, use the following procedure. Refer to Procedure 010-024 in Section 10.
> - For ISX11.9 engines, use the following procedure. Refer to Procedure 010-024 in Section 10.
> - For ISX15 engines, use the following procedure. Refer to Procedure 010-024 in Section 10.
>
> Tighten the exhaust clamps if necessary.
>
> Consult the OEM specifications for the correct torque value.
>
> Any leaks in the exhaust system will cause the Aftertreatment Diesel Particulate Filter Regeneration Test to be less efficient in reducing the soot load of the filter.
>
> ### Test
>
> The Aftertreatment Diesel Particulate Filter Regeneration Test can be found under the ECM Diagnostic Test menu in the INSITE™ electronic service tool.
>
> If INSITE™ electronic service tool is **not** available, some vehicles can be equipped with a stationary regeneration switch in the cab. The switch can be a stand-alone switch or can be combined with the diagnostic switch. Check with the OEM for the location and availability of the switch.
>
> **Note · Примечание**
> In order for the stationary regeneration switch to function, the stationary regeneration switch **must** be enabled in the ECM.
>
> Unlike the Aftertreatment Diesel Particulate Filter Regeneration Test with the INSITE™ electronic service tool, this switch will **only** start a stationary regeneration if the soot load of the filter is high enough. This is indicated by the aftertreatment lamp being illuminated or flashing.
>
> **Note · Примечание**
> A stationary regeneration can **not** be initiated through the use of the cab switch if regeneration inhibit is enabled. INSITE™ electronic service tool **must** then be used to initiate the stationary regeneration.
>
> **Note · Примечание**
> If the Aftertreatment Diesel Particulate Filter Regeneration Test will **not** initiate, use the Stationary Regeneration - Will Not Start troubleshooting symptom tree.
>
> When the test is started, the engine idle speed will be raised automatically to the required level. Expected engine speed can reach between 1000 and 1500 rpm.
>
> The engine will then, through the engine controls, operate in a manner to build exhaust heat. The turbocharger can emit a slight “whining” noise during the test. This is normal.
>
> The Aftertreatment Diesel Particulate Filter Regeneration can take up to two and one half hours to complete, depending on the soot loading of the filter as well as conditions of the environment, such as but **not** limited to the temperature and humidity.
>
> Once the Aftertreatment Diesel Particulate Filter Regeneration Test is complete, the engine will automatically return to normal idle speed.
>
> During the Aftertreatment Diesel Particulate Filter Regeneration Test, the following items will be monitored:
>
> - Aftertreatment Injector Status - Informs the user when fuel is being injected, in small quantity, into the exhaust system upstream of the diesel oxidation catalyst
> - Aftertreatment Diesel Particulate Filter outlet temperature
> - Aftertreatment Diesel Particulate Filter inlet temperature
> - Aftertreatment Diesel Oxidation Catalyst inlet temperature
> - Aftertreatment Diesel Particulate Filter Soot Load - Informs the user of the current soot load of the filter:
>
> **CAUTION · Осторожно**
> During the stationary regeneration, the exhaust gas temperature can reach 800°C \[1500°F\] and the surface temperature can exceed 700°C \[1300°F\].
>
> The stationary regeneration can take up to 2-1/2 hours to complete, depending on the soot loading of the filter. At any time the stationary regeneration can be aborted by clicking on the “Stop” button in the INSITE™ electronic service tool.
>
> The stationary regeneration will be aborted if:
>
> - A fault becomes active
> - The accelerator is depressed
> - The clutch pedal is depressed
> - The brake pedal is depressed
> - The transmission is put into gear.
>
> **Note · Примечание**
> If a stationary regeneration can **not** be initiated or is aborted, and the engine has a low power complaint, use the following procedures.
>
> - For ISM engines, use the following procedure. [[101-011-009-tr — Exhaust Restriction|Refer to Procedure 011-009 in Section 11.]]
> - For ISX engines, use the following procedure. [[101-011-009-tr — Exhaust Restriction|Refer to Procedure 011-009 in Section 11.]]
> - For ISX11.9 engines, use the following procedure. Refer to Procedure 011-009 in Section 11.
> - For ISX15 engines, use the following procedure. Refer to Procedure 011-009 in Section 11.
>
> #### Pass or Fail Criteria
>
> - Pass: Aftertreatment Testing Procedure 014-013 in Section 14 has passed, if there is no visible black smoke and the stationary regeneration completes with no aftertreatment fault codes being generated.
> - Fail: Aftertreatment Testing Procedure 014-013 in Section 14 has failed, if there is visible black smoke and/or aftertreatment fault codes are generated. Repair the cause of the black smoke and/or correct the fault codes.
>
> ### Finishing Steps
>
> Allow the engine and exhaust system to cool down. Temperatures can maintain an elevated state for several minutes.
>
> Check to make sure the diesel particulate filter lamp is **not** illuminated.
>
> **Note · Примечание**
> If the diesel particulate filter lamp is illuminated and Fault Code 2639 or 1921 are still active, a second regeneration will be needed. If the fault is still active after a second regeneration, the filter needs to be cleaned of ash or soot.
>
> - For ISM engines, use the following procedure. [[101-011-041-tr — Aftertreatment Diesel Particulate Filter|Refer to Procedure 011-041 in Section 11.]]
> - For ISX engines, use the following procedure. [[101-011-041-tr — Aftertreatment Diesel Particulate Filter|Refer to Procedure 011-041 in Section 11.]]
> - For ISX11.9 engines, use the following procedure. Refer to Procedure 011-041 in Section 11.
> - For ISX15 engines, use the following procedure. Refer to Procedure 011-041 in Section 11.
>
> Check for any active fault codes. If active fault codes are present, use Section TF for fault code troubleshooting.
>
> Use INSITE™ electronic service tool to clear all inactive fault codes.
