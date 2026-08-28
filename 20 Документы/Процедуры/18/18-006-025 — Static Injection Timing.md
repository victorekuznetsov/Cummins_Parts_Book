---
aliases:
  - "Статическая установка угла опережения впрыска"
type: "Процедура"
doc: "18-006-025"
title_en: "Static Injection Timing"
title_ru: "Статическая установка угла опережения впрыска"
modified: "2012-06-27"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "4021499"
figures: 21
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/18/18-006-025.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/18-006-025.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/18"
  - "перевод/машинный"
---

# Static Injection Timing
**Статическая установка угла опережения впрыска**

> [!abstract] Процедура · `18-006-025`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[4021499 — K19 Service Manual|4021499]]
> **Секции:** Section 6 - Injectors and Fuel Lines
> **Даты:** изменён 2012-06-27
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/18/18-006-025.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/18-006-025.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Сроки впрыска - это относительное измерение расстояния, остающегося между плунжером форсунки и чашкой форсунки, когда поршень составляет 5,16 мм \[0,2032 дюйма \], или 19 градусов до верхней точки на сжатии.

Время работы форсунки выражается количеством оставшегося проезда толкателя.

![[it800wa.png]]

Код времени форсунки появляется на табличке с данными двигателя. Коды — это буквы алфавита, которые относятся к числовым спецификациям.

Спецификации можно найти в руководстве по контрольной части (CPL), в бюллетене 4021328.

![[it800wb.png]]

Ниже приведен краткий обзор сроков инъекции и того, как ее можно регулировать.

Расширенное время означает, что топливо впрыскивается ранее в цилиндр во время такта сжатия.

Замедленное время означает, что впрыск топлива происходит ближе к верхней мертвой точке в цилиндре.

![[it400gb.png]]

Количество проезда толкателя определяет время впрыска топлива по отношению к положению поршня.

Чем выше числовое значение оставшегося хода толкателя, тем больше задержка или замедление времени.

Чем ниже числовое значение оставшегося хода толкателя, тем больше степень продвинутого или быстрого времени.

![[it400gc.png]]

Изменения времени инъекций осуществляются путем продвижения или замедления действия крана по отношению к положению поршня.

Это достигается путем изменения ориентации доли распределительного вала на кран с использованием различных ключей передачи распределительного вала.

Время движения поезда (выравнивание индексной отметки) всегда остается неизменным.

![[it400gd.png]]

Ключ кулачкового вала обеспечивает средство индексации кулачкового вала с помощью шестерни.

Смещение клавиш позволяет слегка повернуть профиль распределительного вала, в то время как время передачи остается тем же самым.

Чем больше верхняя часть смещения перемещается в направлении нормального вращения распределительного вала, тем больше время впрыска будет отставать. Числовой показатель перемещения толкателя будет увеличиваться.

Направление нормального вращения коленчатого вала двигателя K19 составляет **по часовой стрелке**, как видно спереди.

![[04400023.png]]

Смещение клавиш можно идентифицировать, измеряя смещение и ссылаясь на следующую диаграмму.

Каждый 0,025 мм \[0,001 в\] смещения вызовет изменение хода толкателя на 0,0127 мм \[0,0005 в\] от прямой клавиши.

При проверке или настройке момента впрыска рекомендуется использовать испытательную передачу. Испытательная передача представляет собой распределительную передачу, которая была модифицирована для обеспечения скольжения на распределительном вале.

Номер ключевой части распределительного вала, указанный в опции деталей для двигателей, является отправной точкой. **Не** Предполагайте, что указанный ключ обеспечит указанные сроки. **Всегда** измеряйте время впрыска, если передача, распределительный вал или ключ были изменены или если во время разборки было отмечено направление любого смещения **не**. Одной из причин существования смещенного ключа является возможность регулировать статические сроки на все допуски для детали, используемой в двигателе.

Если используется стойкое снаряжение, то время впрыска должно быть измерено снова после установки производственного снаряжения.

| Сроки действия кодекса | Рекомендуемый код | Направление Offset |
|---|---|---|
| АЭ | 216782 | Противоположное вращение распределительного вала |
| Эй Джей | 200706 | С вращением распределительного вала |
| АМ | 216782 | С вращением распределительного вала |
| CI | 200711 | С вращением распределительного вала |
| КЛ | S-302 | Нет |
| ТС | 3000492 | С вращением распределительного вала |

![[it4kega.png]]

### Измерение

Используйте инструмент для определения времени впрыска, номер детали 3824942. Показатели (1) и (2) идентичны.

- 1) Индикатор движения стержневой качки
- 2 Индикатор движения по Пистону
- (3) Устройства поддержки Piston plunger
- 4) Поддержка плунжеров с толкающими стержнями
- (5) Удерживающий адаптер
- (6) Устройства для расширения (автоматический ключ)
- 7) Расширение ствола индикатора.

![[it8toga.png]]

Выравнивание сборки плунжерной опоры толкателя имеет решающее значение.

Установите поддержку плунжера толкателя (4) во внешнем слоте в опоре поршня (3).

Выровнять поддержку плунжера с помощью метки. Затяните болт.

Установите на постах показатели (1) и (2). Переверните индикаторы так, чтобы они **не** над плунжерами.

Установите расширение стебля на индикаторы движения поршня.

![[it800sa.png]]

Установите форсунканый толкатель (8).

Установите инструмент синхронизации в цилиндр форсунки. Установите адаптер Hold-down.

Выровняйте плунжер и плунжер, чтобы убедиться, что они прямые.

Закройте замок поддержки (9).

![[it4toha.png]]

Используйте **только **коленчатый вал для вращения двигателя. Использование шестерен приведет к ложному измерению. Грушевую ресницу **следует закрыть в направлении нормального вращения (кранкшафт **по часовой стрелке).

Три направляющих болта, одинаково расположенных перед коленчатым валом, помогут в повороте двигателя.

При двигателе в такте сжатия поверните коленчатый вал в направлении нормального вращения и наблюдайте за обоими плунжерами инструмента синхронизации.

Оба плунжера начнут двигаться вверх, когда цилиндр находится на сжатии. Показатели будут вращаться в направлении **часовой стрелки**.

Если оба индикатора вращаются **не** по часовой стрелке, двигатель находится на ходу выхлопа. Поверните коленчатый вал на одну революцию, чтобы добраться до удара сжатия.

![[04400025.png]]

Медленно вращайте коленчатый вал в направлении нормального вращения при наблюдении поршневого плунжера (10). Прыгун будет двигаться вверх, останавливаться, затем начнет двигаться вниз. Точка остановки плунжера - верхняя мёртвая точка.

Поверните двигатель в направлении, противоположном нормальному вращению, пока плунжер не начнет двигаться вниз. Цилиндр теперь немного перед верхней мертвой точкой.

Поверните индикатор так, чтобы ствол касался плунжера.

Тщательно понижайте индикатор, пока он не опустится. Поднимите индикатор, когда игла повернула минимум три оборота 7,62 мм \[0,300 в\]. Заблокируйте индикатор в положении.

Медленно поверните коленчатый вал в направлении нормального вращения, пока игла индикатора не перестанет поворачиваться **по часовой стрелке** (верхняя мёртвая точка). Отрегулируйте индикатор до нуля.

**Всегда** ноль в верхней мертвой точке с коленчатым валом, только что повернутым в направлении нормального вращения.

Медленно и осторожно вращайте коленчатый вал назад и вперед, пока игла не остановится на нуле, прежде чем изменить направление, чтобы указать, что поршень находится после верхней мёртвой точки.

![[it800sc.png]]

Поверните указатель толкателя, чтобы ствол коснулся плунжера.

Тщательно понижайте индикатор, пока он не опустится. Поднимите индикатор, когда игла повернула минимум три оборота 7,62 мм \[0,300 в\].

![[it800sd.png]]

Медленно поверните коленчатый вал в направлении нормального вращения до тех пор, пока индикатор толкателя не остановится (1), на мгновение изменит направление (2) (это - раздавленный нос на распредвале) и снова остановится (3). Лента теперь находится на внешнем основном круге распределительного вала. Поршень теперь находится примерно на 90 градусов после верхней мёртвой точки.

Важно записать количество поездок, остающихся в индикаторе движения толкателя для более поздней ссылки.

Тщательно опустите индикатор движения толкателя, пока он не опустится. Поднимите показатель приблизительно на 1⁄4 оборота 6,35 мм \[0,025 в\]. Заблокируйте индикатор в положении.

Установите индикатор на ноль.

![[it800se.png]]

Наблюдайте индикатор движения поршня, поскольку коленчатый вал медленно вращается напротив направления нормального вращения.

Прекратите вращать коленчатый вал, когда индикатор движения поршня указывает, что поршень находится в верхней мертвой точке (ноль).

![[it800sf.png]]

Кранкшафт должен быть повернут медленно, чтобы точно подсчитать обороты индикатора.

Поверните коленчатый вал напротив направления нормального вращения, пока игла индикатора не сдвинется на 21⁄2 оборота, 6,35 мм \[0,250 в\].

Поршень теперь 6,35 мм \[0,250 дюйма \] перед верхним мертвым центром.

![[it800sg.png]]

**Только **переместить поршень до 5,16 мм \[0,2032 в\] перед верхней мертвой центра, поворачивая коленчатый вал в направлении нормального вращения. Если коленчатый вал повернут слишком далеко, поверните коленчатый вал обратно в направлении нормального вращения более чем на 5,16 мм \[0,2032 в\] перед верхним мертвым центром. Затем очень медленно поворачивайте коленчатый вал в направлении нормального вращения, пока индикатор не покажет, что поршень находится на 5,16 мм \[0,2032 в\] перед верхним мертвым центром.

Все спецификации впрыска K19 имеют более чем один оборот индикатора 2,54 мм \[0,100 дюйма \].

Прочитайте индикатор толкателя **против часовой стрелки **с нуля. Это измерение времени инъекции. Пример 0,118 показан на графике.

Если вы не уверены в количестве оборотов индикатора толкателя, проверьте, тщательно подняв стебель индикатора, пока индикатор не опустится на дно. Опустите стебель на количество избыточных путешествий. Опустите ствол к плунжеру. Прочитайте индикатор.

Если сроки впрыска находятся в заданных пределах и используется стойкое приспособление, установите стандартную распределительную передачу. См. процедуру 001-012 в разделе 1. Повторите процедуру впрыска после того, как шестерня остыла.

Если время впрыска все еще не соответствует указанным пределам, повторите процедуру измерения, чтобы проверить настройку инструмента и нулевые настройки.

Если время все еще не соответствует указанным пределам, ключ распредвала должен быть изменен. Снимите валовую передачу. См. процедуру 001-012 в разделе 1.

Запишите ориентацию смещения ключа. Используйте следующий рабочий лист для определения альтернативного ключа.

Измерение времени должно быть подтверждено после изменения ключа.

![[it800sh.png]]

![[06400106.png]]

Необходимы скидки для правильной структуры

![[06400105.png]]

Необходимы скидки для правильной структуры

![[06400108.png]]

Необходимы скидки для правильной структуры

![[06400107.png]]

Необходимы скидки для правильной структуры


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The injection timing is the relative measurement of the distance remaining between the injector plunger and the injector cup when the piston is 5.16 mm \[0.2032 in\], or 19 degrees before top dead center on the compression stroke.
>
> Injector timing is expressed by the amount of push rod travel remaining.
>
> The injector timing code appears on the engine dataplate. Codes are alphabetic letters that relate to a numerical specification.
>
> Specifications can be found in the Control Part List (CPL) Manual, Bulletin 4021328.
>
> Below is a brief review of injection timing and how it can be adjusted.
>
> Advanced timing means the fuel is injected earlier into the cylinder during the compression stroke.
>
> Retarded timing means the fuel injection occurs closer to top dead center in the cylinder.
>
> The amount of push rod travel determines the time of fuel injection in relation to the piston position.
>
> The higher the numerical value of the push rod travel remaining indicates a greater degree of retarded or slow timing.
>
> The lower the numerical value of the push rod travel remaining indicates a greater degree of advanced or fast timing.
>
> Injection timing changes are accomplished by advancing or retarding the cam follower action in relation to the piston position.
>
> This is accomplished by changing the orientation of the camshaft lobe to the cam follower using different camshaft gear keys.
>
> Gear train timing (index mark alignment) always remain the same.
>
> The camshaft key provides a means of indexing the camshaft with the gear.
>
> Offset keys allow the camshaft profile to be rotated slightly while the gear train timing remains the same.
>
> The more the top of the offset is moved in the direction of the camshaft normal rotation, the more the injection timing will be retarded. The push rod travel numerical value will increase.
>
> The direction of normal rotation on a K19 engine crankshaft is **clockwise** as viewed from the front.
>
> Offset keys can be identified by measuring the offset and referring to the following chart.
>
> Each 0.025 mm \[0.001 in\] of offset will cause a 0.0127 mm \[0.0005 in\] change in push rod travel from a straight key.
>
> If checking or setting the injection timing, it is recommended to use a testing gear. A testing gear is a camshaft gear that has been modified to provide a slip-fit on the camshaft.
>
> The camshaft key part number listed in the engine performance parts option is a starting point. Do **not** assume the listed key will provide the specified timing. **Always** measure the injection timing if the gear, camshaft, or key have been changed or if during disassembly the direction of any offset was **not** noted. Part of the reason for the existence of the offset key is to be able to adjust the static timing to all tolerances for the part used in the engine.
>
> If a slip fit gear is used, the injection timing **must** be measured again after installation of the production gear.
>
> | Timing Code | Recommended Code | Direction of Offset |
> |---|---|---|
> | AE | 216782 | Opposite camshaft rotation |
> | AJ | 200706 | With camshaft rotation |
> | AM | 216782 | With camshaft rotation |
> | CI | 200711 | With camshaft rotation |
> | CL | S-302 | None |
> | CU | 3000492 | With camshaft rotation |
>
> ### Measure
>
> Use the injection timing tool, Part Number 3824942. The indicators (1) and (2) are identical.
>
> - (1) Push rod travel indicator
> - (2) Piston travel indicator
> - (3) Piston plunger support assembly
> - (4) Push rod plunger support
> - (5) Hold-down adapter
> - (6) Extension assembly (adapter wrench)
> - (7) Indicator stem extension.
>
> The push rod plunger support assembly alignment is critical.
>
> Install the push rod plunger support (4) in the outside slot in the piston support (3).
>
> Align the push rod plunger support with the mark. Tighten the capscrew.
>
> Install indicators (1) and (2) on the posts. Turn the indicators so they are **not** over the plungers.
>
> Install the stem extension on the piston travel indicators.
>
> Install the injector push rod (8).
>
> Install the timing tool in the injector bore. Install the hold-down adapter.
>
> Align the push rod plunger and the rod to be sure they are straight.
>
> Tighten the support lock (9).
>
> Use **only** the crankshaft to rotate the engine. The use of gears will result in false measurement. Gear lash **must** be closed up in the direction of normal rotation (crankshaft **clockwise**).
>
> Three guide bolts equally spaced in front of the crankshaft will aid in engine rotation.
>
> With the engine in the compression stroke, turn the crankshaft in the direction of normal rotation and observe both timing tool plungers.
>
> Both plungers will begin moving upward when the cylinder is on the compression stroke. The indicators will be rotating in a **clockwise** direction.
>
> If both indicators do **not** rotate in a **clockwise** direction, the engine is on the exhaust stroke. Rotate the crankshaft one revolution to get to the compression stroke.
>
> Slowly rotate the crankshaft in the direction of normal rotation while observing the piston plunger (10). The plunger will move upward, stop, then begin to move downward. The stop point of the plunger is top dead center.
>
> Rotate the engine opposite the direction of normal rotation until the plunger begins to move downward. The cylinder is now slightly before top dead center.
>
> Turn the indicator so the stem is touching the plunger.
>
> Carefully lower the indicator until it bottoms out. Raise the indicator when the needle has turned a minimum of three revolutions 7.62 mm \[0.300 in\]. Lock the indicator in position.
>
> Slowly turn the crankshaft in the direction of normal rotation until the indicator needle stops turning **clockwise** (top dead center). Adjust the indicator to zero.
>
> **Always** zero at top dead center with the crankshaft having just been rotated in the direction of normal rotation.
>
> Slowly and carefully rotate the crankshaft backward and forward until the needle stops at zero before reversing the direction to indicate the piston is after top dead center.
>
> Turn the push rod indicator so the stem touches the plunger.
>
> Carefully lower the indicator until it bottoms out. Raise the indicator when the needle has turned a minimum of three revolutions 7.62 mm \[0.300 in\].
>
> Slowly turn the crankshaft in the direction of normal rotation until the push rod indicator stops (1), momentarily reverses direction (2), (this is the crush nose on the camshaft), and stops again (3). The cam follower is now on the outer base circle of the camshaft. The piston is now approximately 90 degrees after top dead center.
>
> It is important to record the amount of travel remaining in the push rod travel indicator for later reference.
>
> Carefully lower the push rod travel indicator until it bottoms out. Raise the indicator approximately ¼ revolution 6.35 mm \[0.025 in\]. Lock the indicator in position.
>
> Set the indicator at zero.
>
> Observe the piston travel indicator as the crankshaft is slowly rotated opposite the direction of normal rotation.
>
> Stop rotating the crankshaft when the piston travel indicator indicates the piston is at top dead center (zero).
>
> The crankshaft **must** be turned slowly to accurately count the indicator revolutions.
>
> Turn the crankshaft opposite the direction of normal rotation until the indicator needle moves 2½ revolutions, 6.35 mm \[0.250 in\].
>
> The piston is now 6.35 mm \[0.250 in\] before top dead center.
>
> **Only** move the piston to 5.16 mm \[0.2032 in\] before top dead center by turning the crankshaft in the direction of normal rotation. If the crankshaft is turned too far, turn the crankshaft back opposite the direction of normal rotation more than 5.16 mm \[0.2032 in\] before top dead center. Then very slowly turn the crankshaft in the direction of normal rotation until the indicator indicates the piston is 5.16 mm \[0.2032 in\] before top dead center.
>
> All K19 injection timing specifications are more than one indicator revolution 2.54 mm \[0.100 in\].
>
> Read the push rod indicator **counterclockwise** from zero. This is the injection timing measurement. An example of 0.118 in is illustrated in the graphic.
>
> If unsure of the number of push rod indicator revolutions, check by carefully lifting the indicator stem until the indicator has bottomed out. Lower the stem the amount of excess travel. Lower the stem to the plunger. Read the indicator.
>
> If the injection timing is within specification and a slip fit gear is used, install the standard camshaft gear. Refer to Procedure 001-012 in Section 1. Repeat the injection timing procedure after the gear has cooled.
>
> If the injection timing is still **not** within specification, repeat the measurement procedure to check the tool set up and zero settings.
>
> If the timing is still **not** within specification, the camshaft key **must** be changed. Remove the camshaft gear. Refer to Procedure 001-012 in Section 1.
>
> Record the orientation of the offset of the key. Use the following worksheet to determine the alternate key.
>
> The timing measurement **must** be confirmed after changing the key.
>
> NEEDS TEXT FOR CORRECT STRUCTURE
>
> NEEDS TEXT FOR CORRECT STRUCTURE
>
> NEEDS TEXT FOR CORRECT STRUCTURE
>
> NEEDS TEXT FOR CORRECT STRUCTURE
