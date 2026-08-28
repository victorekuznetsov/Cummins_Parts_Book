---
aliases:
  - "Статическая установка угла опережения впрыска"
type: "Процедура"
doc: "20-006-025-tr"
title_en: "Static Injection Timing"
title_ru: "Статическая установка угла опережения впрыска"
modified: "2018-11-13"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021592"
figures: 25
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-006-025-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/20-006-025-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/20"
  - "перевод/машинный"
---

# Static Injection Timing
**Статическая установка угла опережения впрыска**

> [!abstract] Процедура · `20-006-025-tr`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual|4021592]]
> **Секции:** Section 6 - Injectors and Fuel Lines · Section 6 - Injectors and Fuel Lines - Group 06
> **Даты:** изменён 2018-11-13
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-006-025-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/20-006-025-tr.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

с форсункой механического управления

Сроки впрыска - это относительное измерение расстояния, остающегося между плунжером форсунки и чашкой форсунки, когда поршень составляет 5,16 мм \[0,2032 дюйма \], или 19 градусов до TDC на ходе сжатия.

Время подачи топлива в форсунка выражается количеством оставшегося проезда в толкаемой трубе.

![[cg100wa.png]]

Код времени впрыска появляется на табличке данных двигателя. Коды — это буквы алфавита, которые относятся к числовым спецификациям.

Спецификации можно найти в руководстве по контрольной части (CPL), в бюллетене 4021328.

![[cg100wh.png]]

Следующие шесть кадров представляют собой краткий обзор времени инъекции и того, как его можно отрегулировать.

Расширенное время (1) означает, что топливо впрыскивается ранее в цилиндр во время такта сжатия.

Замедленное время (2) означает, что впрыск топлива происходит ближе к верхней мертвой точке (TDC) в цилиндре.

![[cg100wc.png]]

Количество проезда толкателя определяет время впрыска топлива по отношению к положению поршня.

Низкое числовое значение оставшегося хода толкателя указывает на большую степень продвинутого (1) или быстрого времени.

Большое число остающихся проездов стержневого хода указывает на большую степень замедления (2) или медленного времени.

![[it400gc.png]]

Изменения времени инъекций осуществляются путем продвижения или замедления действия крана по отношению к положению поршня.

Это достигается путем изменения ориентации доли распределительного вала на кран с использованием различных ключей передачи распределительного вала.

> [!note] Примечание
> Время движения поезда (выравнивание индексной отметки) всегда остается неизменным.

![[cg100we.png]]

Ключ кулачкового вала обеспечивает средство индексации кулачкового вала с помощью шестерни.

Смещение клавиш позволяет слегка повернуть профиль распределительного вала, в то время как время передачи остается тем же самым.

Чем больше верхняя часть смещения перемещается в направлении нормального вращения распределительного вала, тем больше время впрыска будет отставать. Числовой показатель перемещения толкателя будет увеличиваться.

> [!note] Примечание
> Направление нормального вращения коленчатого вала двигателя QSK19 составляет **по часовой стрелке**, как видно спереди.

![[00400010.png]]

Смещение клавиш можно определить, измерив смещение и ссылаясь на диаграмму в конце этого раздела.

> [!note] Примечание
> Каждый 0,025 мм \[0,001 дюйма\] смещения вызовет изменение хода толкателя на 0,0127 мм \[0,0005 дюйма\] от прямой клавиши.

![[it4kega.png]]

При проверке или настройке момента впрыска рекомендуется использовать испытательную передачу. Испытательная передача представляет собой распределительную передачу, которая была модифицирована для обеспечения скольжения на распределительном вале.

![[01400035.png]]

### Подготовительные операции

Подготовьте двигатель для регулировки статического времени.

- Снимите крышку коромысел.[[20-003-011-tr — Rocker Lever Cover|См. процедуру 003-011 в разделе 3.]]
- Удалите клапанный клапанный рычаг-руку из цилиндра № 3.[[20-003-009-tr — Rocker Lever Assembly|См. процедуру 003-009 в разделе 3.]]
- Удалите форсунка из цилиндра № 3.[[20-006-026-tr — Injector|См. процедуру 006-026 в разделе 6.]]

Примечание: не обязательно удалять весь форсунка; однако вращение двигателя будет легче при удалении всего форсунки.

![[ck800wa.png]]

### Настройка

Используйте инструмент для определения времени впрыска, номер детали 3824942. Показатели (1) и (2) идентичны.

1. Индикатор движения в трубе
2. Индикатор путешествия по Пистону
3. Сборка поддержки Piston plunger
4. 2.3.1.1 Установка опоры для плунжерных стержней
5. Адаптер Hold-down
6. Устройства для расширения (adapter wrench)
7. Расширение индикаторного стеблеобразования

![[it8toga.png]]

Выравнивание сборки плунжерной опоры толкателя имеет решающее значение.

Установите поддержку плунжера толкателя (4) во внешнем слоте в поддержку поршневого плунжера (3).

Выровнять поддержку плунжера с помощью метки. Затяните болт.

Установите на постах показатели (1) и (2). Переверните индикаторы так, чтобы они **не** над плунжерами.

Установите расширение стебля на индикатор движения поршня.

![[it800sa.png]]

Установите форсунканый толкатель (8) для цилиндра № 3.

Установите инструмент синхронизации в цилиндр форсунки № 3. Установите адаптеры с задержкой.

Выровняйте плунжер и плунжер, чтобы убедиться, что они прямые.

Закройте замок поддержки (9).

![[it4toha.png]]

### Измерение

Используйте **только **коленчатый вал для вращения двигателя. Использование шестерен приведет к ложному измерению. Грушевую ресницу  следует закрыть в направлении нормального вращения.

> [!note] Примечание
> Три направляющих болта, одинаково расположенных перед коленчатым валом, помогут вращать двигатель.

Поверните коленчатый вал в направлении нормального вращения при наблюдении обоих плунжеров инструмента синхронизации. Оба плунжера начнут двигаться вверх, когда цилиндр находится на сжатии.

Если предположить, что все указатели зубчатой передачи были выровнены при запуске процесса впрыска, коленчатый вал должен быть повернут примерно на три четверти оборота, чтобы получить ход сжатия для цилиндра № 3.

Если оба плунжера **не** движутся вверх (один вверх и один вниз), двигатель находится на ходу выхлопа. Поверните коленчатый вал на одну революцию, чтобы добраться до удара сжатия.

![[00400009.png]]

Установить TDC путем медленного вращения коленчатого вала в направлении нормального вращения при наблюдении поршневого плунжера (10). Прыгун будет двигаться вверх, останавливаться, затем начнет двигаться вниз. Точка остановки плунжера - TDC. Поверните двигатель в направлении, противоположном нормальному вращению, пока плунжер не начнет двигаться вниз. Сейчас цилиндр немного опережает TDC.

![[it800sc.png]]

Поверните индикатор так, чтобы ствол касался плунжера. Тщательно двигайте индикатор вниз, пока игла не превратится минимум в пять оборотов \[0,500 дюйма\]. Оставьте индикатор в положении.

Медленно поверните коленчатый вал в направлении нормального вращения до поворота индикаторной иглы STOPS **по часовой стрелке** (TDC). Переместите индикатор вниз, пока не произойдет только один оборот \[0,100 дюйма\], оставшийся до тех пор, пока индикатор не достигнет дна.

Отрегулируйте индикатор до нуля.

![[it800sc.png]]

Поверните указатель толкателя так, чтобы ствол касался плунжера.

Тщательно понижайте индикатор, пока он не опустится. Поднимите индикатор, когда игла повернула минимум три оборота \[0,300 дюйма\].

![[it800sd.png]]

Медленно поверните коленчатый вал в направлении нормального вращения до указателя толкателя STOPS (1), на мгновение переверните направление (2) (это дробь носа на распредвале), и STOPS снова (3). Лента теперь находится на внешнем основном круге распределительного вала. Сейчас поршень находится примерно на 45 градусов после TDC.

Важно записать количество поездок, остающихся в индикаторе движения толкателя для более поздней ссылки.

Тщательно опустите индикатор движения толкателя, пока он не опустится. Поднимите индикатор примерно на половину оборота \[0,050 дюйма\]. Оставьте индикатор в положении.

Установите индикатор на ноль.

![[it800se.png]]

Установите поршень на \[0.2032 дюйма\] перед TDC

Наблюдайте индикатор движения поршня, когда вы медленно вращаете коленчатый вал напротив направления нормального вращения.

Прекратите вращение коленчатого вала, когда индикатор движения поршня указывает, что поршень находится в TDC (ZERO).

![[it800sf.png]]

Кранкшафт должен быть повернут медленно, чтобы точно подсчитать обороты индикатора.

Поверните коленчатый вал напротив направления нормального вращения, пока игла индикатора не сдвинется на два с половиной оборота \[0,250 дюйма\].

Теперь поршень на 0.250 дюйма впереди TDC.

![[it800sg.png]]

**Только** перед TDC переведите поршень на \[0.2032 дюйма\], повернув коленчатый вал в направлении нормального вращения. Если вы случайно повернете коленчатый вал слишком далеко, вы должны повернуть коленчатый вал напротив направления нормального вращения больше, чем \[0.2032 дюйма\] перед TDC. Затем очень медленно поворачивайте коленчатый вал в направлении нормального вращения, пока индикатор не покажет, что поршень находится \[0,2032 дюйма\] перед TDC.

> [!note] Примечание
> Помните, что все спецификации QSK19 для впрыска являются более чем одним индикатором оборота \[0,100 дюйма\].

Прочитайте индикатор движения толкателя **против часовой стрелки** с нуля. Это измерение времени впрыска для сравнения со спецификацией. Приведен пример \[0.118 дюйма\].

![[it800sh.png]]

Если **не** уверены в количестве оборотов указателя стержня, проверьте:

- Тщательно поднимая стебель индикатора, пока индикатор не опустится на дно
- Понижайте стебель количества избыточных путешествий, которые вы установили на третьем предыдущем шаге.
- Опустите ствол к плунжеру.
- Прочитайте индикатор.

Если время впрыска находится в пределах спецификации и вы используете скользкое снаряжение, установите стандартное снаряжение.[[20-001-012-tr — Camshaft Gear (Camshaft Installed)|См. процедуру 001-012 в разделе]]. Повторите процедуру впрыска после того, как распределительная передача остыла.

![[dp8gewa.png]]

Если время впрыска **не** в пределах спецификации, повторите процедуру измерения для проверки установки инструмента и настройки ZERO.

Если время все еще не соответствует указанным пределам, ключ распредвала должен быть изменен.[[20-001-012-tr — Camshaft Gear (Camshaft Installed)|См. процедуру 001-012 в разделе]]для инструкций по снятию распредвалной передачи.

Запишите ориентацию любого смещения ключа. Используйте следующий рабочий лист для определения альтернативного ключа.

Вы должны подтвердить измерение времени после изменения ключа.

![[06400081.png]]

![[06400106.png]]

![[06400105.png]]

### Завершающие операции

с форсункой механического управления

- Установите форсунка из цилиндра № 3.[[20-006-026-tr — Injector|См. процедуру 006-026 в разделе 6.]]
- Установите клапанный клапанный качельной рычаг из цилиндра № 3.[[20-003-009-tr — Rocker Lever Assembly|См. процедуру 003-009 в разделе 3.]]
- Установите крышку коромысел.[[20-003-011-tr — Rocker Lever Cover|См. процедуру 003-011 в разделе 3.]]
- Запустите двигатель и проверьте на отсутствие утечек.

![[ck800wa.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> with Mechanically Actuated Injector
>
> The injection timing is the relative measurement of the distance remaining between the injector plunger and the injector cup when the piston is 5.16 mm \[0.2032 inch\], or 19 degrees before TDC on the compression stroke.
>
> Injector timing is expressed by the amount of push tube travel remaining.
>
> The injection timing code appears on the engine dataplate. Codes are alphabetic letters that relate to a numerical specification.
>
> Specifications can be found in the Control Part List (CPL) Manual, Bulletin 4021328.
>
> The next six frames are a brief review of injection timing and how it can be adjusted.
>
> Advanced timing (1) means the fuel is injected earlier into the cylinder during the compression stroke.
>
> Retarded timing (2) means the fuel injection occurs closer to top dead center (TDC) in the cylinder.
>
> The amount of push rod travel determines the time of fuel injection in relation to the piston position.
>
> A low numerical value of the push rod travel remaining indicates a greater degree of advanced (1) or fast timing.
>
> A high numerical value of push rod travel remaining indicates a greater degree of retarded (2) or slow timing.
>
> Injection timing changes are accomplished by advancing or retarding the cam follower action in relation to the piston position.
>
> This is accomplished by changing the orientation of the camshaft lobe to the cam follower using different camshaft gear keys.
>
> **Note · Примечание**
> Gear train timing (index mark alignment) always remains the same.
>
> The camshaft key provides a means of indexing the camshaft with the gear.
>
> Offset keys allow the camshaft profile to be rotated slightly while the gear train timing remains the same.
>
> The more the top of the offset is moved in the direction of the camshaft normal rotation, the more the injection timing will be retarded. The push rod travel numerical value will increase.
>
> **Note · Примечание**
> The direction of normal rotation on a QSK19 engine crankshaft is **clockwise** as viewed from the front.
>
> Offset keys can be identified by measuring the offset and referring to the chart at the end of this section.
>
> **Note · Примечание**
> Each 0.025 mm \[0.001 inch\] of offset will cause a 0.0127 mm \[0.0005 inch\] change in the push rod travel from a straight key.
>
> If checking or setting the injection timing, it is recommended to use a testing gear. A testing gear is a camshaft gear that has been modified to provide a slip-fit on the camshaft.
>
> ### Preparatory Steps
>
> Prepare the engine to adjust the static timing.
>
> - Remove the rocker lever cover. [[20-003-011-tr — Rocker Lever Cover|Refer to Procedure 003-011 in Section 3.]]
> - Remove the rocker lever assembly from cylinder Number 3. [[20-003-009-tr — Rocker Lever Assembly|Refer to Procedure 003-009 in Section 3.]]
> - Remove the injector from cylinder Number 3. [[20-006-026-tr — Injector|Refer to Procedure 006-026 in Section 6.]]
>
> NOTE: It is **not** necessary to remove all injectors; however, engine rotation will be easier with all injectors removed.
>
> ### Setup
>
> Use the injection timing tool, Part Number 3824942. The indicators (1) and (2) are identical.
>
> 1. Push tube travel indicator
> 2. Piston travel indicator
> 3. Piston plunger support assembly
> 4. Push rod plunger support assembly
> 5. Hold-down adapter
> 6. Extension assembly (adapter wrench)
> 7. Indicator stem extension
>
> The push rod plunger support assembly alignment is critical.
>
> Install the push rod plunger support (4) in the outside slot in the piston plunger support (3).
>
> Align the push rod plunger support with the mark. Tighten the capscrew.
>
> Install the indicators (1) and (2) on the posts. Turn the indicators so they are **not** over the plungers.
>
> Install the stem extension on the piston travel indicator.
>
> Install the injector push rod (8) for cylinder Number 3.
>
> Install the timing tool in the injector bore Number 3. Install the hold-down adapters.
>
> Align the push rod plunger and the rod to be sure they are straight.
>
> Tighten the support lock (9).
>
> ### Measure
>
> Use **only** the crankshaft to rotate the engine. The use of the gears will result in false measurement. Gear lash **must** be closed up in the direction of normal rotation.
>
> **Note · Примечание**
> Three guide bolts equally spaced in front of the crankshaft will help rotate the engine.
>
> Turn the crankshaft in the direction of normal rotation while observing both of the timing tool plungers. Both plungers will begin moving upward when the cylinder is on the compression stroke.
>
> Assuming all the gear index marks were aligned when the injection timing process was started, the crankshaft will have to be rotated approximately three-quarters of a revolution to get to the compression stroke for the Number 3 cylinder.
>
> If both plungers are **not** moving upward (one upward and one downward), the engine is on the exhaust stroke. Rotate the crankshaft one revolution to get to the compression stroke.
>
> Establish TDC by slowly rotating the crankshaft in the direction of normal rotation while observing the piston plunger (10). The plunger will move upward, STOP, then begin to move downward. The STOP point of the plunger is TDC. Rotate the engine opposite the direction of normal rotation until the plunger begins to move downward. The cylinder is now before TDC slightly.
>
> Turn the indicator so the stem is touching the plunger. Carefully move the indicator downward until the needle has turned a minimum of five revolutions \[0.500 inch\]. LOCK the indicator in position.
>
> Slowly turn the crankshaft in the direction of normal rotation until the indicator needle STOPS turning **clockwise** (TDC). Move the indicator downward until there is **only** one revolution \[0.100 inch\] of travel remaining until the indicator bottoms out.
>
> Adjust the indicator to ZERO.
>
> Turn the push rod indicator so that the stem touches the plunger.
>
> Carefully lower the indicator until it bottoms out. Raise the indicator when the needle has turned a minimum of three revolutions \[0.300 inch\].
>
> Slowly turn the crankshaft in the direction of normal rotation until the push rod indicator STOPS (1), momentarily reverses direction (2) (this is the crush nose on the camshaft), and STOPS again (3). The cam follower is now on the outer base circle of the camshaft. The piston is now approximately 45 degrees after TDC.
>
> It is important to record the amount of travel remaining in the push rod travel indicator for later reference.
>
> Carefully lower the push rod travel indicator until it bottoms out. Raise the indicator approximately one-half of a revolution \[0.050 inch\]. LOCK the indicator in position.
>
> Set the indicator at ZERO.
>
> Set the piston at \[0.2032 inch\] before TDC
>
> Observe the piston travel indicator as you slowly rotate the crankshaft opposite the direction of normal rotation.
>
> Stop rotating the crankshaft when the piston travel indicator indicates the piston is at TDC (ZERO).
>
> The crankshaft **must** be turned slowly to accurately count the indicator revolutions.
>
> Turn the crankshaft opposite the direction of normal rotation until the indicator needle moves two and one-half revolutions \[0.250 inch\].
>
> The piston is now \[0.250 inch\] before TDC.
>
> **Only** move the piston to \[0.2032 inch\] before TDC by turning the crankshaft in the direction of normal rotation. If you accidently turn the crankshaft too far, you **must** turn the crankshaft opposite the direction of normal rotation more than \[0.2032 inch\] before TDC. Then very slowly turn the crankshaft in the direction of normal rotation until the indicator indicates that the piston is \[0.2032 inch\] before TDC.
>
> **Note · Примечание**
> Remember that all QSK19 injection timing specifications are more than one indicator revolution \[0.100 inch\].
>
> Read the push rod travel indicator **counterclockwise** from zero. This is the injection timing measurement to compare to the specification. An example of \[0.118 inch\] is shown.
>
> If **not** sure of the number of push rod indicator revolutions, check by:
>
> - Carefully lifting the indicator stem until the indicator has bottomed out
> - Lower the stem the amount of excess travel you set in the third preceding step
> - Lower the stem to the plunger.
> - Read the indicator.
>
> If the injection timing is within specification and you are using a slipper-fit gear, install the standard gear. [[20-001-012-tr — Camshaft Gear (Camshaft Installed)|Refer to Procedure 001-012 in Section]]. Repeat the injection timing procedure after the camshaft gear has cooled.
>
> If the injection timing is **not** within specification, repeat the measurement procedure to check the tool setup and the ZERO settings.
>
> If the timing is still **not** within specification, the camshaft key **must** be changed. [[20-001-012-tr — Camshaft Gear (Camshaft Installed)|Refer to Procedure 001-012 in Section]] for instructions to remove the camshaft gear.
>
> Record the orientation of any offset of the key. Use the following worksheet to determine an alternate key.
>
> You **must** confirm the timing measurement after changing the key.
>
> ### Finishing Steps
>
> with Mechanically Actuated Injector
>
> - Install the injector from cylinder Number 3. [[20-006-026-tr — Injector|Refer to Procedure 006-026 in Section 6.]]
> - Install the rocker lever assembly from cylinder Number 3. [[20-003-009-tr — Rocker Lever Assembly|Refer to Procedure 003-009 in Section 3.]]
> - Install the rocker lever cover. [[20-003-011-tr — Rocker Lever Cover|Refer to Procedure 003-011 in Section 3.]]
> - Operate the engine and check for leaks.
