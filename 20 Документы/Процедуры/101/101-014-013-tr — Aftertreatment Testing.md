---
type: "Процедура"
doc: "101-014-013-tr"
title_en: "Aftertreatment Testing"
modified: "2015-08-28"
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
  - "3666239"
  - "3666322"
figures: 18
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/101/101-014-013-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/101-014-013-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/101"
  - "перевод/машинный"
---

# Aftertreatment Testing

> [!abstract] Процедура · `101-014-013-tr`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666239 — Signature™, ISX, and QSX15 Service Manual|3666239]], [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 14 - Engine Testing - Group 14
> **Даты:** изменён 2015-08-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/101/101-014-013-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/101-014-013-tr.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

> [!danger] ОПАСНО
> Во время регенерации температура выхлопных газов может достигать 800 ° C \[1500 ° F \], а температура поверхности выхлопной системы может превышать 700° C \[1300° F \], которая достаточно горячая, чтобы воспламенить или расплавить обычные материалы и вызвать серьезные ожоговые травмы. Выхлопные и выхлопные компоненты могут оставаться горячими после того, как транспортное средство перестало двигаться. Чтобы избежать риска пожара, повреждения имущества, ожогов или других серьезных травм, позвольте выхлопной системе остыть перед началом этой процедуры или ремонта и убедитесь, что горючие материалы не находятся там, где они могут вступать в контакт с горячими выхлопными газами или компонентами выхлопных газов.

Испытание на ускорение Snap используется для проверки фильтра твердых частиц дизельного топлива (DPF) на наличие трещин или других прогрессирующих повреждений без удаления системы фильтрации. Он используется для проверки функциональности послеоперационной DPF.

Для проведения стационарного регенерационного теста фильтра дизельных частиц INSITETM используется электронное оборудование:

- Регенерировать после лечения DPF
- Восстановление после обработки дизельного катализатора окисления (DOC) и после обработки DPF после загрязнения охлаждающей жидкостью
- Проверьте эффективность DOC после лечения
- Проверьте правильность установки датчиков температуры после обработки
- Сброс сохраненной нагрузки сажи в модуле управления двигателем (ECM)
- Проверьте послеочистку топливного форсунка, запорный клапан и функциональность поезда.

Проверяйте активные коды неисправностей перед выполнением любой из этих процедур. Если присутствуют какие-либо активные коды неисправностей, следуйте соответствующему дереву устранения неисправностей кода неисправностей.

![[11c00245.png]]

Электронное сервисное оборудование INSITETM Послеочистка Дизельный фильтр твердых частиц Стационарный тест на регенерацию может быть использован для восстановления функциональности послеочистки DOC и послеочистки DPF после того, как либо, либо оба подверглись воздействию охлаждающей жидкости.

> [!note] Примечание
> Если DOC и DPF подозреваются в загрязнении охлаждающей жидкости, их не нужно удалять и проверять. Проконсультируйтесь с разделом подготовительных шагов этой процедуры для получения дополнительной информации.

Температура, которая достигается во время регенерации, достаточно высока, чтобы испарить охлаждающую жидкость из обоих компонентов и вернуть оба компонента к нормальным эксплуатационным характеристикам.

> [!note] Примечание
> Если эти компоненты подозреваются в загрязнении охлаждающей жидкостью, не выполняйте тест на ускорение Snap перед регенерацией.

![[11c00245.png]]

В этом разделе излагается процедура проверки выпускных отверстий выхлопной системы.

Проверка выпускной системы выхлопных газов может выявить состояние после обработки DPF. Выход выхлопной системы должен выглядеть чистым, практически без остатка выхлопных газов / накопления сажи.

Последующая обработка DPF является **не** 100% эффективной. Некоторое накопление остатка выхлопных газов / сажи является нормальным и не указывает на неисправность после обработки DPF.

Тяжелое накопление остатка выхлопных газов/сажи может указывать на неисправность DPF после обработки.

Для определения того, является ли накопление остатка выхлопных газов/сажи на выпускной розетке выхлопной системы результатом неисправной послеочистки ДПФ, выполните одно из следующих действий:

1. Тест на ускорение Snap, описанный в этой процедуре.
2. Очистить последние 152 до 254 мм \[6 до 10 в\] выпускной системы выхлопной системы. Управляйте транспортным средством в течение одной смены или поездки и проверяйте выпуск выхлопной системы на предмет накопления остатков выхлопных газов/сажи.
3. Проверить послеоперационный ДПФ.[[101-011-041-tr — Aftertreatment Diesel Particulate Filter|См. процедуру 011-041 в разделе 11.]]

![[14d00033.png]]

### Настройка

Запуск и запуск двигателя на холостом ходу.

Перед проведением испытания на регенерацию дизельного фильтра твердых частиц проверьте выхлопные трубы на наличие утечек, трещин и рыхлых соединений.

- Для двигателей ISM используйте следующую процедуру.[[35-010-024-tr — Air Leaks, Air Intake and Exhaust Systems|См. процедуру 010-024 в разделе 10.]]
- Для двигателей ISX используйте следующую процедуру. См. процедуру 010-024 в разделе 10.

Затягивать выхлопные зажимы, если это необходимо.

Проконсультируйтесь со спецификациями OEM для правильного значения крутящего момента.

Любые утечки в выхлопной системе приведут к тому, что тест на регенерацию дизельного фильтра будет менее эффективным в снижении нагрузки фильтра на сажу.

![[10d00395.png]]

### Проверка

После обработки регенерация дизельного фильтра твердых частиц

Тест на регенерацию дизельного фильтра после обработки можно найти в меню ECM Diagnostic Test в электронном сервисном инструменте INSITETM.

Для выполнения стационарной регенерации подключите инструмент электронного сервиса INSITETM и проверьте активные коды неисправностей. Если коды неисправностей присутствуют, кроме кодов 2639 или 1921, перед началом работы перейдите в раздел TF для устранения неисправностей кода неисправности. Не выполнять регенерацию с активными кодами неисправностей, отличными от кодов ошибок 2639 или 1921, если только руководствоваться деревом устранения неисправностей кода неисправностей.

> [!note] Примечание
> Если во время работы не возникают жалобы на черный дым, а выхлопная труба черная, DPF не нужно удалять или проверять во время этого процесса.

![[19803969.png]]

Если электронный сервисный инструмент INSITETM недоступен, некоторые транспортные средства могут быть оснащены стационарным переключателем регенерации в кабине. Переключатель может быть автономным переключателем или может быть объединен с диагностическим переключателем. Проверьте с OEM местоположение и доступность коммутатора.

> [!note] Примечание
> Для того чтобы переключатель регенерации работал, в ECM должен быть включен переключатель регенерации.

В отличие от теста на регенерацию дизельного фильтра с использованием электронного сервисного инструментария INSITETM, этот переключатель будет **только **запускать стационарную регенерацию, если нагрузка сажи фильтра достаточно высока. Это указывается при освещении или мигании лампы после обработки.

> [!note] Примечание
> Стационарная регенерация может быть инициирована **не** с помощью кабины-переключателя, если включено ингибирование регенерации. Электронный сервисный инструмент INSITETM должен быть использован для инициирования стационарной регенерации.

![[14d00035.png]]

> [!note] Примечание
> Если после лечения дизельный фильтр для твердых частиц будет **не** инициировать, используйте стационарную регенерацию - не начнет устранение неполадок дерево симптомов в разделе TS.

Когда испытание начнется, скорость холостого хода двигателя будет автоматически повышена до необходимого уровня. Ожидаемая скорость двигателя может достигать от 1000 до 1500 об/мин.

Затем двигатель будет работать таким образом, чтобы вырабатывать выхлопное тепло. Турбокомпрессор может издавать небольшой «свистящий» шум во время испытания. Это нормально.

Регенерация дизельного фильтра может занять до 2-1⁄2 часов, в зависимости от загрузки сажи фильтра, а также условий окружающей среды, таких как, но не ограничиваясь, температура и влажность.

После завершения испытаний на регенерацию дизельного фильтра дизельных частиц двигатель автоматически вернется к нормальной скорости холостого хода.

![[10900098.png]]

Во время испытания на регенерацию дизельного фильтра для твердых частиц после обработки будут контролироваться следующие элементы:

- Статус форсунки после обработки - информирует пользователя о том, когда топливо впрыскивается в небольшом количестве в выхлопную систему выше по течению от DOC
- После обработки DPF выходной температуры
- После обработки ДПФ входная температура
- После обработки DOC входная температура
- После обработки DPF Soot Load - информирует пользователя о текущей нагрузке сажи фильтра:

![[19803969.png]]

> [!danger] ОПАСНО
> Во время регенерации температура выхлопных газов может достигать 800 ° C \[1500 ° F \], а температура поверхности выхлопной системы может превышать 700° C \[1300° F \], которая достаточно горячая, чтобы воспламенить или расплавить обычные материалы и вызвать серьезные ожоговые травмы. Выхлопные и выхлопные компоненты могут оставаться горячими после того, как транспортное средство перестало двигаться. Чтобы избежать риска пожара, повреждения имущества, ожогов или других серьезных травм, позвольте выхлопной системе остыть перед началом этой процедуры или ремонта и убедитесь, что горючие материалы не находятся там, где они могут вступать в контакт с горячими выхлопными газами или компонентами выхлопных газов.

Стационарная регенерация может занять до 2-1⁄2 часов, в зависимости от загрузки сажи фильтра. В любое время стационарная регенерация может быть прервана нажатием кнопки «Стоп» в инструменте электронного сервиса INSITETM.

Регенерация будет прекращена, если:

- Неисправность становится активной
- Ускоритель находится в депрессии
- Педаль сцепления находится в депрессии
- Педаль тормоза находится в депрессии
- Трансмиссия переводится в снаряжение.

> [!note] Примечание
> Если стационарная регенерация может быть инициирована или прервана, а двигатель имеет жалобу на низкую мощность, используйте следующую процедуру.

- [[101-011-009-tr — Exhaust Restriction|См. процедуру 011-009 в разделе 11.]]

Начните стационарную регенерацию. Это может быть выполнено стационарным переключателем регенерации в кабине или с помощью электронного инструментария INSITE.

- Стационарный регенерационный выключатель в кабине:
- Инструменты электронного обслуживания INSITETM:
- В любом случае двигатель создаст достаточно тепла для регенерации после обработки DPF. Скорость двигателя будет увеличиваться, и турбокомпрессор может громко свистеть во время процесса регенерации. После того, как последующая обработка DPF будет восстановлена, двигатель автоматически вернется к нормальной скорости холостого хода.
- Мониторинг автомобиля и окружающей среды во время регенерации. Если возникает какое-либо небезопасное состояние, немедленно выключите двигатель.

#### Пройти или не пройти критерии

- Пропуск: Процедура тестирования после обработки 014-013 в разделе 14 прошла, если не видно черного дыма и неподвижная регенерация завершается без генерирования кодов неисправностей после обработки.
- Неудача: Процедура тестирования после обработки 014-013 в разделе 14 не удалась, если имеется видимый черный дым и/или генерируются коды неисправностей после обработки. Исправить причину черного дыма и/или исправить коды неисправностей.

![[19803969.png]]

Ускорение Snap - после лечения подключено

Трансмиссия транспортного средства **должна быть нейтральной, а стояночный тормоз транспортного средства **должен применяться.

Запуск и запуск двигателя на холостом ходу. Быстро нажимайте педаль акселератора от 0 до 100 процентов. При необходимости это можно сделать несколько раз.

![[14c00079.png]]

Во время этого испытания проверьте наличие черного дыма, выходящего из выхлопной трубы, так как двигатель ускоряется от низкого холостого хода до высокого холостого хода.

> [!note] Примечание
> В некоторых случаях тест на ускорение Snap может **не** обеспечить условия, необходимые для выявления неисправности после обработки DPF. Если на выходе выхлопной системы происходит сильное накопление остатка/сажи выхлопных газов, и ускорение с помощью защелки **не** показывает состояние, изложенное на следующих этапах, может потребоваться выполнить короткий разгон при частичной до полной нагрузки и/или испытание на стойку.[[101-014-008 — Engine Testing (In Chassis)|См. процедуру 014-008 в разделе 14.]]

См. послеоперационный катализатор окисления дизельного топлива и последующее лечение Дизельный фильтр для твердых частиц повторное использование Руководство, бюллетень[[4021600 — Aftertreatment Diesel Oxidation Catalyst (DOC) and Aftertreatment Diesel Particulate|4021600]]Для прохождения или провала руководящих принципов.

![[14d00034.png]]

Если присутствует серый дым или слабый черный дым, обратитесь к рекомендациям по повторному использованию дизельного окислителя после обработки и к рекомендациям по повторному использованию дизельного фильтра для твердых частиц после обработки.[[4021600 — Aftertreatment Diesel Oxidation Catalyst (DOC) and Aftertreatment Diesel Particulate|4021600]]Для прохождения или провала руководящих принципов.

Белый дым во время испытания на ускорение snap не указывает на неисправность. Ремонт не требуется.

![[11c00247.png]]

Ускорение Snap - после лечения отключено

> [!danger] ОПАСНО
> Выхлопные газы и компоненты выхлопных газов могут оставаться горячими после того, как транспортное средство перестало двигаться. Чтобы избежать риска пожара, повреждения имущества, ожогов или других серьезных травм, позвольте выхлопной системе остыть перед началом этой процедуры или ремонта и убедитесь, что горючие материалы не находятся там, где они могут вступать в контакт с горячими выхлопными газами или компонентами выхлопных газов.

Одна из функций системы последующей обработки заключается в удалении частиц из выхлопных газов. Эта функция предотвращает использование черного дыма в качестве диагностического симптома.

Тест на ускорение Snap (после обработки отключен) используется для проверки аномально высокого количества черного дыма в выхлопных газах.

Отсоедините выхлопную трубу от розетки турбины турбокомпрессора.

![[11c00110.png]]

Трансмиссия транспортного средства должна быть нейтральной.

При этом необходимо использовать стояночный тормоз.

Может возникнуть необходимость временной корректировки максимальной скорости двигателя без параметра VSS в электронном сервисном оборудовании INSITETM до высокой скорости холостого хода двигателя.

Запустите двигатель и запускайте его на холостом ходу.

Быстро нажмите на педаль акселератора от 0 до 100 процентов и удерживайте 5 секунд после освобождения. При необходимости это можно сделать несколько раз.

![[14c00079.png]]

Во время этого испытания проверьте наличие черного дыма, выходящего из турбины турбокомпрессора, поскольку двигатель ускоряется от низкого до высокого холостого хода и при высоком холостом ходе.

![[14000010.png]]

Небольшой затяжной черный дым при ускорении, который очищается с постоянной высокой скоростью холостого хода, является нормальным.

Белый дым во время испытания на ускорение snap не указывает на неисправность. Ремонт не требуется.

Тяжелый черный дым указывает на другие проблемы с двигателем, которые необходимо диагностировать. Ссылка на Черный дым - Чрезмерное устранение неполадок дерево симптомов в разделе ТС.

![[14000011.png]]

Восстановите выхлопную систему.

Проверьте выхлопные трубы на наличие утечек, трещин и свободных соединений.

Затягивать выхлопные зажимы, если это необходимо.

Проконсультируйтесь с изготовителем оригинального оборудования (OEM) для правильного значения крутящего момента.

![[10d00395.png]]

### Завершающие операции

Позвольте двигателю и выхлопной системе остыть. Температура может поддерживать повышенное состояние в течение нескольких минут.

Убедитесь, что лампа DPF не освещена.

> [!note] Примечание
> Если лампа DPF зажжена и код ошибки 2639 или 1921 все еще активен, потребуется вторая регенерация. Если неисправность все еще активна после второй регенерации, фильтр необходимо очистить от золы или сажи.[[101-011-041-tr — Aftertreatment Diesel Particulate Filter|См. процедуру 011-041 в разделе 11.]]

Проверьте наличие активных кодов неисправностей. Если присутствуют активные коды неисправностей, используйте раздел TF для устранения неисправностей кода неисправностей.

Используйте инструмент электронного сервиса INSITETM для очистки всех кодов неактивных ошибок.

![[19803969.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> **WARNING · Опасно**
> During regeneration, exhaust gas temperature could reach 800°C \[1500°F\] and exhaust system surface temperature can exceed 700°C \[1300°F\], which is hot enough to ignite or melt common materials, and cause severe burn injuries. The exhaust and exhaust components can remain hot after the vehicle stopped moving. To avoid the risk of fire, property damage, burns or other serious personal injury, allow the exhaust system to cool before beginning this procedure or repair and make sure that no combustible materials are located where they are likely to come in contact with hot exhaust or exhaust components.
>
> The Snap Acceleration Test is used to check the aftertreatment diesel particulate filter (DPF) for cracks or other progressive damage, without removing the filter system. It is used to test the functionality of the aftertreatment DPF.
>
> The INSITE™ electronic service tool Aftertreatment Diesel Particulate Filter Stationary Regeneration Test is used to:
>
> - Regenerate an aftertreatment DPF
> - Recover the aftertreatment diesel oxidation catalyst (DOC) and aftertreatment DPF after coolant contamination
> - Check the aftertreatment DOC efficiency
> - Check for the correct installation of the aftertreatment temperature sensors
> - Reset the stored soot load in the engine control module (ECM)
> - Check the aftertreatment fuel injector, shutoff valve, and drive train functionality.
>
> Check for active fault codes prior to performing either of these procedures. If any active fault codes are present, follow the appropriate fault code troubleshooting tree.
>
> The INSITE™ electronic service tool Aftertreatment Diesel Particulate Filter Stationary Regeneration Test can be used to regain functionality of the aftertreatment DOC and aftertreatment DPF after either, or both, have been exposed to coolant.
>
> **Note · Примечание**
> If the DOC and DPF are suspected of having coolant contamination, they do **not** need to be removed and inspected. Consult the Preparatory Steps section of this procedure for further details.
>
> The temperatures that are achieved during the regeneration are high enough to evaporate the coolant out of both components and return both components to normal operating specifications.
>
> **Note · Примечание**
> If these components are suspected of having coolant contamination, do **not** perform the Snap Acceleration Test before performing the regeneration.
>
> This section outlines the exhaust system outlet inspection.
>
> Inspection of the exhaust system outlet can reveal the condition of the aftertreatment DPF. The exhaust system outlet should appear clean, with little to no exhaust residue/soot buildup.
>
> The aftertreatment DPF is **not** 100 percent efficient. Some accumulation of exhaust residue/soot is normal, and does **not** indicate a malfunctioning aftertreatment DPF.
>
> A heavy buildup of exhaust residue/soot can indicate a malfunction of the aftertreatment DPF.
>
> To determine if the exhaust residue/soot accumulation on the exhaust system outlet is the result of a malfunctioning aftertreatment DPF, perform one of the following:
>
> 1. Snap Acceleration Test as outlined in this procedure.
> 2. Clean the last 152 to 254 mm \[6 to 10 in\] of the exhaust system outlet. Operate the vehicle for one shift or trip and inspect the exhaust system outlet for exhaust residue/soot accumulation.
> 3. Inspect the aftertreatment DPF. [[101-011-041-tr — Aftertreatment Diesel Particulate Filter|Refer to Procedure 011-041 in Section 11.]]
>
> ### Setup
>
> Start and idle the engine.
>
> Prior to the Aftertreatment Diesel Particulate Filter Regeneration Test, inspect the exhaust piping for leaks, cracks, and loose connections.
>
> - For ISM engines, use the following procedure. [[35-010-024-tr — Air Leaks, Air Intake and Exhaust Systems|Refer to Procedure 010-024 in Section 10.]]
> - For ISX engines, use the following procedure. Refer to Procedure 010-024 in Section 10.
>
> Tighten the exhaust clamps, if necessary.
>
> Consult the OEM specifications for the correct torque value.
>
> Any leaks in the exhaust system will cause the Aftertreatment Diesel Particulate Filter Regeneration Test to be less efficient in reducing the soot load of the filter.
>
> ### Test
>
> Aftertreatment Diesel Particulate Filter Regeneration
>
> The Aftertreatment Diesel Particulate Filter Regeneration Test can be found under the ECM Diagnostic Test menu in INSITE™ electronic service tool.
>
> To perform a stationary regeneration, connect INSITE™ electronic service tool and check for active fault codes. If any fault codes are present other than Fault Codes 2639 or 1921, go to Section TF for any fault code troubleshooting before proceeding. Do **not** perform a stationary regeneration with active fault codes other than Fault Codes 2639 or 1921, unless guided to do so by the fault code troubleshooting tree.
>
> **Note · Примечание**
> Unless there are complaints of black smoke during operation and the exhaust stack is black, the DPF does **not** need to be removed or inspected during this process.
>
> If INSITE™ electronic service tool is **not** available, some vehicles can be equipped with a stationary regeneration switch in the cab. The switch can be a stand-alone switch or can be combined with the diagnostic switch. Check with the OEM for the location and availability of the switch.
>
> **Note · Примечание**
> In order for the stationary regeneration switch to function, the stationary regeneration switch **must** be enabled in the ECM.
>
> Unlike the Aftertreatment Diesel Particulate Filter Regeneration Test with INSITE™ electronic service tool, this switch will **only** start a stationary regeneration if the soot load of the filter is high enough. This is indicated by the aftertreatment lamp being illuminated or flashing.
>
> **Note · Примечание**
> A stationary regeneration can **not** be initiated through the use of the cab switch if regeneration inhibit is enabled. INSITE™ electronic service tool **must** then be used to initiate the stationary regeneration.
>
> **Note · Примечание**
> If the Aftertreatment Diesel Particulate Filter Regeneration Test will **not** initiate, use the Stationary Regeneration - Will Not Start troubleshooting symptom tree in Section TS.
>
> When the test is started, the engine idle speed will be raised automatically to the required level. Expected engine speed can reach between 1000 and 1500 rpm.
>
> The engine will then, through the engine controls, operate in a manner to build exhaust heat. The turbocharger can emit a slight “whining” noise during the test. This is normal.
>
> The Aftertreatment Diesel Particulate Filter Regeneration can take up to 2-½ hours to complete, depending on the soot loading of the filter, as well as conditions of the environment, such as, but **not** limited to, the temperature and humidity.
>
> Once the Aftertreatment Diesel Particulate Filter Regeneration Test is complete, the engine will automatically return to normal idle speed.
>
> During the Aftertreatment Diesel Particulate Filter Regeneration Test, the following items will be monitored:
>
> - Aftertreatment Injector Status - Informs the user when fuel is being injected, in small quantity, into the exhaust system upstream of the DOC
> - Aftertreatment DPF outlet temperature
> - Aftertreatment DPF inlet temperature
> - Aftertreatment DOC inlet temperature
> - Aftertreatment DPF Soot Load - Informs the user of the current soot load of the filter:
>
> **WARNING · Опасно**
> During regeneration, exhaust gas temperature could reach 800°C \[1500°F\] and exhaust system surface temperature can exceed 700°C \[1300°F\], which is hot enough to ignite or melt common materials, and cause severe burn injuries. The exhaust and exhaust components can remain hot after the vehicle stopped moving. To avoid the risk of fire, property damage, burns or other serious personal injury, allow the exhaust system to cool before beginning this procedure or repair and make sure that no combustible materials are located where they are likely to come in contact with hot exhaust or exhaust components.
>
> The stationary regeneration can take up to 2-½ hours to complete, depending on the soot loading of the filter. At any time the stationary regeneration can be aborted by clicking on the “Stop” button in INSITE™ electronic service tool.
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
> If a stationary regeneration can **not** be initiated or is aborted, and the engine has a low power complaint, use the following procedure.
>
> - [[101-011-009-tr — Exhaust Restriction|Refer to Procedure 011-009 in Section 11.]]
>
> Begin the stationary regeneration. This can be performed by a stationary regeneration switch in the cab or by INSITE electronic service tool.
>
> - Stationary regeneration switch in the cab:
> - INSITE™ electronic service tool:
> - In either case, the engine will create enough heat to regenerate the aftertreatment DPF. Engine speed will increase and the turbocharger can whistle loudly during the regeneration process. Once the aftertreatment DPF is regenerated, the engine will automatically return to normal idle speed
> - Monitor the vehicle and surrounding area during regeneration. If any unsafe condition occurs, shut off the engine immediately.
>
> #### Pass or Fail Criteria
>
> - Pass: Aftertreatment Testing Procedure 014-013 in Section 14 has passed if there is no visible black smoke and the stationary regeneration completes with no aftertreatment fault codes being generated.
> - Fail: Aftertreatment Testing Procedure 014-013 in Section 14 has failed if there is visible black smoke and/or aftertreatment fault codes are generated. Repair the cause of the black smoke and/or correct the fault codes.
>
> Snap Acceleration - Aftertreatment Connected
>
> The vehicle transmission **must** be in neutral and the vehicle parking brake **must** be applied.
>
> Start and idle the engine. Rapidly depress the accelerator pedal from 0 to 100 percent. This can be performed multiple times, if necessary.
>
> During this test, check for black smoke exiting the exhaust stack, as the engine is accelerated from low idle to high idle.
>
> **Note · Примечание**
> In some applications, a Snap Acceleration Test may **not** provide the conditions necessary to reveal a malfunctioning aftertreatment DPF. If there is a heavy buildup of exhaust residue/soot on the exhaust system outlet and a snap acceleration does **not** reveal a condition outlined in the following steps, it may be necessary to perform a brief acceleration run under partial to full load and/or a stall test. [[101-014-008 — Engine Testing (In Chassis)|Refer to Procedure 014-008 in Section 14.]]
>
> Refer to Aftertreatment Diesel Oxidation Catalyst and Aftertreatment Diesel Particulate Filter Reuse Guidelines, Bulletin [[4021600 — Aftertreatment Diesel Oxidation Catalyst (DOC) and Aftertreatment Diesel Particulate|4021600]], for pass or fail guidelines.
>
> If gray smoke or faint black smoke is present, refer to Aftertreatment Diesel Oxidation Catalyst and Aftertreatment Diesel Particulate Filter Reuse Guidelines, Bulletin [[4021600 — Aftertreatment Diesel Oxidation Catalyst (DOC) and Aftertreatment Diesel Particulate|4021600]], for pass or fail guidelines.
>
> White smoke during the Snap Acceleration Test does **not** indicate a malfunction. No repair is necessary.
>
> Snap Acceleration - Aftertreatment Disconnected
>
> **WARNING · Опасно**
> The exhaust gas and exhaust components can remain hot after a vehicle has stopped moving. To avoid the risk of fire, property damage, burns, or other serious injury, allow the exhaust system to cool before beginning this procedure or repair and make sure that no combustible materials are located where they are likely to come in contact with hot exhaust gas or exhaust components.
>
> One of the functions of the aftertreatment system is to remove particulates from the exhaust gas. This function prevents the use of black smoke as a diagnostic symptom.
>
> The Snap Acceleration Test (aftertreatment disconnected) is used to check for abnormally high amounts of black smoke in the exhaust gas.
>
> Disconnect the exhaust pipe from the turbocharger turbine outlet.
>
> The vehicle transmission **must** be in neutral.
>
> The vehicle parking brake **must** be applied.
>
> It may be necessary to temporarily adjust the maximum engine speed with no VSS parameter in INSITE™ electronic service tool to the high idle speed of the engine.
>
> Start the engine and let it idle.
>
> Quickly depress the accelerator pedal from 0 percent to 100 percent and hold 5 seconds then release. This can be performed multiple times, if necessary.
>
> During this test, check for black smoke exiting the turbocharger turbine outlet as the engine is accelerated from low idle to high idle and at high idle.
>
> A small puff of black smoke upon acceleration that clears at a steady high idle speed is normal.
>
> White smoke during the Snap Acceleration Test does **not** indicate a malfunction. No repair is necessary.
>
> Heavy black smoke indicates other upstream engine issues that need to be diagnosed. Reference the Black Smoke - Excessive troubleshooting symptom tree in Section TS.
>
> Reconnect the exhaust system.
>
> Inspect the exhaust piping for leaks, cracks, and loose connections.
>
> Tighten the exhaust clamps, if necessary.
>
> Consult the original equipment manufacturer (OEM) specifications for the correct torque specification value.
>
> ### Finishing Steps
>
> Allow the engine and exhaust system to cool down. Temperatures can maintain an elevated state for several minutes.
>
> Check to make sure the DPF lamp is **not** illuminated.
>
> **Note · Примечание**
> If the DPF lamp is illuminated and Fault Code 2639 or 1921 is still active, a second regeneration will be needed. If the fault is still active after a second regeneration, the filter needs to be cleaned of ash or soot. [[101-011-041-tr — Aftertreatment Diesel Particulate Filter|Refer to Procedure 011-041 in Section 11.]]
>
> Check for any active fault codes. If active fault codes are present, use Section TF for fault code troubleshooting.
>
> Use INSITE™ electronic service tool to clear all inactive fault codes.
