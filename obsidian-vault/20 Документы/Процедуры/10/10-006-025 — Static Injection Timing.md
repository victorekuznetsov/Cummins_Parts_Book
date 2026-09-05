---
aliases:
  - "Статическая установка угла опережения впрыска"
type: "Процедура"
doc: "10-006-025"
title_en: "Static Injection Timing"
title_ru: "Статическая установка угла опережения впрыска"
modified: "2011-11-02"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
manuals:
  - "3666239"
figures: 34
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-006-025.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-006-025.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSX15"
  - "группа/10"
  - "перевод/машинный"
---

# Static Injection Timing
**Статическая установка угла опережения впрыска**

> [!abstract] Процедура · `10-006-025`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Входит в руководства:** [[3666239 — Signature™, ISX, and QSX15 Service Manual|3666239]]
> **Секции:** Section 6 - Injectors and Fuel Lines - Group 06
> **Даты:** изменён 2011-11-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-006-025.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-006-025.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Статическая мера времени - это количество пробега впрыска на доли распределительного вала форсунки, остающейся, когда поршень составляет 5,161 мм \[0,2032-в\], или 17,5 градусов перед верхним мертвым центром (TDC) на ходе сжатия.

![[06a00126.png]]

Статический код времени появляется на табличке данных двигателя. Коды перечислены в степенях клина, используемых для установки распределительного вала форсунки.

Спецификации можно найти в таблице Control Parts List (CPL). Используйте следующую процедуру для статических значений времени ISX, QSX. См. процедуру 850-029 в разделе V.

![[06a00127.png]]

Расширенное время (1) означает, что топливо впрыскивается ранее в цилиндр во время такта сжатия. Замедленное время (2) означает, что впрыск топлива происходит ближе к TDC в цилиндре.

![[cg100wc.png]]

Количество проезда кулачков форсунки определяет сроки впрыска топлива по отношению к положению поршня.

**низкое** числовое значение оставшегося проезда кулачков форсунки указывает на большую степень ускорения (1) или быстрое время.

**Высокая** числовая величина оставшегося проезда кулачков форсунки указывает на большую степень замедления (2) или замедления времени.

![[06a00128.png]]

> [!warning] ОСТОРОЖНО
> Продление времени впрыска сверх номинального значения времени двигателя может привести к повреждению двигателя и или после обработки.

Изменения времени впрыска осуществляются путем **продвижения** или **замедления** действия кулачкового вала форсунки по отношению к положению поршня.

Это достигается путем изменения ориентации доли распределительного вала на рычаг качения топливного форсунка с использованием различных клиньев.

![[06a00129.png]]

### Настройка

Сроки впрыска - это измерение, которое определяет оставшуюся долю форсунки в распределительном вале по отношению к путешествию поршня. Требуются инструменты для впрыска, Номер детали 3824942 и Номер детали 2892426.

![[06a00130.png]]

Удалите разъём масляной трубки из нижней крышки передач. См. процедуру 007-065 в разделе 7.

Вставьте 19 мм 3/4-дюймовый приводной скоб и удлинитель в привод воздушного компрессора.

![[17c00091.png]]

Снимите крышку коромысел. См. процедуру 003-011 в разделе 3.

![[03c00002.png]]

Удалите передний форсунка и клапан клапана качального рычага сборки **только**.[[10-003-009-tr — Rocker Lever Assembly|См. процедуру 003-009 в разделе 3.]]

![[03a00075.png]]

Удалите форсунка из цилиндра № 3.[[10-006-026-tr — Injector|См. процедуру 006-026 в разделе 6.]]

> [!note] Примечание
> Если топливо или охлаждающая жидкость вошли в цилиндр № 3, эти жидкости должны быть эвакуированы до начала работы.

![[06a00131.png]]

> [!note] Примечание
> Инструмент синхронизации форсунки, Номер детали 3824982, может быть установлена без удаления передней вентиляции и рычагов форсунки. Если **не** уже завершено, удалите передний клапан и топливный клапанный клапан качального рычага.[[10-003-009-tr — Rocker Lever Assembly|См. процедуру 003-009 в разделе 3.]]

Установите адаптер цилиндра цилиндра форсунки ISX, номер детали 3163304, найденную в комплекте для обработки, номер детали 2892426, в цилиндр № 3 цилиндра форсунки топлива, который находится в головке цилиндра.

![[06a00132.png]]

> [!note] Примечание
> Часть служебной оснастки, номер детали 3824942, которая измеряет движение проталкивающей трубки, не будет использоваться при измерении времени впрыска на двигателе ISX или QSX.

Установите **только** поршневую часть инструмента синхронизации форсунки, номер детали 3824942, в цилиндр № 3 с болтами, предоставленными в сервисной оснастке, номер детали 2892426.

Ориентируйте служебную оснастку так, чтобы инструмент соответствовал оси коленчатого вала, а часть инструмента, которая удерживает проездной штепсель трубки, вытянута над цилиндром № 4.

> [!note] Примечание
> Неправильное затягивание этих болтов вызовет погрешность измерения. Используйте 13-мм поворот, чтобы затянуть болты. После затягивания болтов проверьте, чтобы убедиться, что поршневой плунжер имеет свободное движение вверх и вниз. Если поршневой плунжерный прут **не** свободно перемещается, инструмент должен быть скорректирован для получения свободного перемещения.

Затяните болт.

> [!tip] Момент затяжки
> 47 Н·м [35 фунт-фут]

![[06a00133.png]]

### Измерение

Поверните двигатель **по часовой стрелке**, как видно из передней части двигателя, пока метка В на демпфере двигателя не выровняется с метки на нижней крышке корпуса зубчатой коробки, а впускной и выпускной клапаны закрыты на цилиндре № 4.

Рычаги коромысла на цилиндре № 4 **должны быть свободными. Если они не являются**, поверните двигатель на 360 градусов и снова проверьте рычаги качения, чтобы убедиться, что впускной и выпускной клапаны закрыты на цилиндре № 4. Оба набора клапанов закрыты, когда рычаги коромысла свободны.

![[06a00134.png]]

Установите индикатор (1) и адаптер (2) поворотного циферблата поршня на служебную оснастку, установленную в цилиндре № 3.

Адаптер **должен** коснуться инструмента индикатором, обращенным к оператору. Закрутите винт большого пальца.

Индикатор циферблата должен быть также полностью вставлен в адаптер. Закрутите винт большого пальца.

![[06a00135.png]]

Используйте следующую процедуру, чтобы найти TDC двигателя на цилиндре № 3.

Вращайте двигатель **по часовой стрелке** до тех пор, пока поршневой плунжерный стержень не достигнет своего полного верхнего положения.

Вращайте двигатель **против часовой стрелки** и **против часовой стрелки** при наблюдении за движением иглы индикатора циферблата.

Вращайте двигатель **по часовой стрелке** до тех пор, пока не прекратится движение иглы.

Нулевой индикатор циферблата, регулируя внешнее кольцо и запирая его на место. Повторите этот шаг несколько раз, чтобы убедиться в точности TDC.

> [!note] Примечание
> Всегда устанавливайте индикатор циферблата на TDC до «0» (ноль), при этом коленчатый вал только что был повернут в направлении нормального вращения **(по часовой стрелке)**, чтобы уменьшить любые ошибки времени из-за обратной реакции передачи.

![[06a00136.png]]

Вращайте двигатель **против часовой стрелки** до 6,35 мм \[0,250 дюйма\] перед верхним мертвым центром (BTDC). Большая игла на индикаторе циферблата сделает 2-1/2 оборота и будет двигаться в движении против часовой стрелки.

![[06a00137.png]]

> [!note] Примечание
> Поршень должен быть расположен на 5,161 мм \[0,2032 в \] BTDC, чтобы избежать ошибки измерения времени.

Вращайте двигатель **по часовой стрелке** до тех пор, пока индикатор циферблата не прочтет 5,161 мм \[0,2032 в\] BTDC. Игла индикатора будет двигаться по часовой стрелке.

![[06a00138.png]]

> [!note] Примечание
> Этот шаг должен быть выполнен для предотвращения ошибки в измерении.

Разрежьте цилиндр № 4 форсунки, регулирующего винтовой шлюзовый гайка, и полностью втягивайте регулирующий винт, чтобы не было нагрузки на форсунка. Рычаг форсунки **должен **свободно раскачиваться взад и вперед.

Затягивайте винт регулировки форсунки до той точки, когда рычаг форсунки больше не будет качать.

Закрутите регулирующий винт на один дополнительный виток (360 градусов). Рукоять затягивать гайку, следя за тем, чтобы регулировочный винт не поворачивался.

Затяните корректирующий винтовой локон.

> [!tip] Момент затяжки
> 47 Н·м [35 фунт-фут]

![[06a00139.png]]

Установите кронштейн индикатора впрыска, Номер детали 2892427, на служебную оснастку, установленную в цилиндре № 3. Кронштейн **должен** растягиваться над цилиндром № 4.

Рукоять крепеж кронштейна.

![[06a00140.png]]

Соберите индикаторный щуп на индикаторе форсуночного проездного циферблата.

![[06a00141.png]]

Установите индикатор перемещения инъекций и адаптер на скобку, номер детали 2892427. Адаптер **должен** располагаться на 9,5 мм \[0,375 дюйма\] над скобкой.

Закрутите винт большого пальца.

Индикатор циферблата должен быть обращен к оператору.

![[06a00142.png]]

> [!note] Примечание
> Некоторые топливные форсунки верхних пружинных фиксаторах имеют ступень, где находится измерительный щуп, поэтому обратите пристальное внимание, чтобы щуп не проскальзывал во время стадии измерения впрыска. Если щуп проскользнет, произойдут ошибки во времени.

Измерительный щуп **должен** быть ориентирован таким образом, чтобы он соприкасался с верхним пружинным фиксатором форсунки как можно ближе к центральной линии коленчатого вала. Будьте особенно осторожны, чтобы убедиться, что щуп не контактирует с рычагом топливного форсунка или клапанным мостом. Щуп **должен** располагаться на центральной линии коленчатого вала, чтобы избежать ошибок измерения.

![[06a00143.png]]

Рукоять затягивать щуп локона с 6,35 мм \[1/4 в\] гаечный ключ.

Нулевой индикатор перемещения инъекции, отрегулировав внешнее кольцо и заблокировав его на место. Убедитесь, что все винты большого пальца плотные, а индикатор остается на нуле (0).

Проверьте, что индикатор движения поршня по-прежнему читает 5,161 мм \[0,2032 в\] BTDC.

![[06a00144.png]]

> [!note] Примечание
> **не** смотреть индикатор поворота поршня. На данном этапе процедуры движение индикатора больше не требуется.

Вращайте двигатель **по часовой стрелке**, наблюдая за большой иглой на индикаторе движения впрыска на цилиндре № 4, пока игла не перестанет двигаться. Обратите внимание, что игла будет двигаться **против часовой стрелки**.

Когда игла перестает двигаться, запишите показания индикатора перемещения инъекции. Обратите пристальное внимание на количество оборотов, которые совершает индикатор. Каждая полная революция составляет 2,54 мм \[0,100 дюйма \].

![[06a00145.png]]

> [!note] Примечание
> Индикатор движения инъекций считывается в направлении **против часовой стрелки** от "0" (ноль). Общая сумма проезда представляет собой значение времени инъекции.

Сравните показания индикатора проезда впрыска с спецификацией, указанной для CPL двигателя, найденной в таблице «Список критических частей» (CPL). Используйте следующую процедуру для значений статического хребта ISX, QSX. См. процедуру 850-029 в разделе V.

Эту таблицу также можно найти, введя серийный номер двигателя (ESN) в QuickServiceTM Online, а затем выбрав вкладку Гарантия. Под Warranty Tab выберите Engine Dataplate. На экране таблички с данными двигателя нажмите на номер CPL двигателя, и он приведет вас к экрану списка критических частей. Выберите ссылку под названием ISX QSX Static Timing Wedge. Найдите CPL для двигателя, над которым вы работаете. Запишите номинальное значение времени впрыска для правильного CPL. Сравните номинальное значение CPL с значением времени впрыска, которое вы только что измерили на двигателе. Переходим к следующему шагу.

Двигатель CPL можно найти на табличке с данными двигателя, расположенной на крышке рычага качения клапанного клапана.

![[cg1uaje.png]]

Если время впрыска **не** в пределах спецификации, проверьте следующее:

- Правильно ли установлен инструмент синхронизации?
- Правильно ли корректируются индикаторы циферблата?
- Повернут ли коленчатый вал в правильном направлении и последовательности времени?

Если эти шаги были проверены на правильность и двигатель вышел из строя, выполните следующий шаг, чтобы определить, является ли время впрыска замедленным или расширенным.

![[06a00146.png]]

Если показания индикатора выше номинальной спецификации, то сроки замедляются.

Если показания индикатора ниже номинальной спецификации, то время увеличивается.

![[nobox.png]]

> [!note] Примечание
> Сроки впрыска могут быть изменены с помощью различных клиньев, поставляемых в сервисную оснастку, номер детали 2892426. Каждый клин 1/4-градусной степени изменит время приблизительно на 0,1016 мм \[0,004 в\].

- 4,25° клин - предварительное время на 0,1016 мм \[0,004 в\]
- 4.50 Degree Wedge - Предварительное время на 0.2032 мм \[0.008 in\]
- 4,75° клин - Предварительное время на 0,3048 мм \[0,012 в\]

![[nobox.png]]

Выберите подходящий клин и выполните процедуру определения времени базового двигателя.[[10-001-088-tr — Engine Base Timing|См. процедуру 001-088 в разделе 1.]]Используйте коленчатый вал и выбранный клин, чтобы изменить время впрыска, чтобы привести его в спецификацию. После того, как основное время двигателя было завершено, повторите эту процедуру и снова измерьте время впрыска, чтобы убедиться, что время впрыска теперь находится в пределах спецификации.

Обновите табличку с данными двигателя, чтобы отразить степень клина, используемого для получения номинального времени двигателя.

![[nobox.png]]

Удалите инструмент синхронизации впрыска и адаптер цилиндра цилиндра форсунки.

![[06a00147.png]]

Используйте новые кольца и установите форсунку цилиндра № 3.[[10-006-026-tr — Injector|См. процедуру 006-026 в разделе 6.]]

![[06a00131.png]]

Установите мосты клапанных клапанов.

Установите клапанные клапанные качели на рычагах.[[10-003-009-tr — Rocker Lever Assembly|См. процедуру 003-009 в разделе 3.]]

![[03c00129.png]]

Регулируйте клапаны и форсунка.[[10-003-004-tr — Overhead Set|См. процедуру 003-004 в разделе 3.]]

![[03c00088.png]]

Установите крышку коромысел. См. процедуру 003-011 в разделе 3.

Удалите запорное устройство и установите масляную трубку. См. процедуру 007-065 в разделе 7.

![[03c00002.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The static timing measure is the amount of injection travel on the injector camshaft lobe remaining when the piston is 5.161 mm \[0.2032-in\], or 17.5 degrees before top dead center (TDC) on the compression stroke.
>
> The static timing code appears on the engine dataplate. Codes are listed in wedge degrees used to set the injector camshaft.
>
> Specifications can be found in the Control Parts List (CPL) table. Use the following procedure for ISX, QSX Static Timing Values. Refer to Procedure 850-029 in Section V.
>
> Advanced timing (1) means the fuel is injected earlier into the cylinder during the compression stroke. Retarded timing (2) means the fuel injection occurs closer to TDC in the cylinder.
>
> The amount of injector camshaft lobe travel determines the timing of fuel injection in relation to the piston position.
>
> A **low** numerical value of the injector camshaft lobe travel remaining indicates a greater degree of advanced (1) or fast timing.
>
> A **high** numerical value of the injector camshaft lobe travel remaining indicates a greater degree of retarded (2) or slow timing.
>
> **CAUTION · Осторожно**
> Advancing the injection timing beyond an engine's nominal timing value can cause engine and or aftertreatment damage.
>
> Injection timing changes are accomplished by **advancing** or **retarding** the injector camshaft lobe action in relation to the piston position.
>
> This is accomplished by changing the orientation of the camshaft lobe to the injector rocker lever using different wedges.
>
> ### Setup
>
> Injection timing is a measurement that determines the remaining injector camshaft lobe travel in relation to the piston travel. Injection timing tools, Part Number 3824942 and Part Number 2892426, are required.
>
> Remove the oil fill tube connector from the lower gear cover. Refer to Procedure 007-065 in Section 7.
>
> Insert a 19 mm 3/4-inch drive ratchet and extension into the air compressor drive.
>
> Remove the rocker lever cover. Refer to Procedure 003-011 in Section 3.
>
> Remove the front injector and valve rocker lever assembly **only**. [[10-003-009-tr — Rocker Lever Assembly|Refer to Procedure 003-009 in Section 3.]]
>
> Remove the injector from cylinder number 3. [[10-006-026-tr — Injector|Refer to Procedure 006-026 in Section 6]]
>
> **Note · Примечание**
> If fuel or coolant have entered cylinder number 3, these fluids **must** be evacuated before proceeding.
>
> **Note · Примечание**
> Injector timing tool, Part Number 3824982, can **not** be installed without removing the front valve and injector rocker levers. If **not** already completed, remove the front valve and injector rocker lever assembly. [[10-003-009-tr — Rocker Lever Assembly|Refer to Procedure 003-009 in Section 3.]]
>
> Install the ISX injector bore adapter, Part Number 3163304, found within service tool kit, Part Number 2892426, into cylinder number 3 injector bore in the cylinder head.
>
> **Note · Примечание**
> The portion of the service tool, Part Number 3824942, that measures push tube travel will **not** be used when measuring injection timing on an ISX or QSX engine.
>
> Install **only** the piston travel portion of injector timing tool, Part Number 3824942, into cylinder number 3 with the capscrew provided in service tool, Part Number 2892426.
>
> Orient the service tool so that the tool is in line with the crankshaft axis, and the portion of the tool that holds the push tube travel gage is extended over cylinder number 4.
>
> **Note · Примечание**
> Improper tightening of this capscrew will cause a measurement error. Use a 13 mm swivel to tighten the capscrew. After tighting the capscrew, check to make sure the piston plunger rod has free movement up and down. If the piston plunger rod does **not** move freely, the tool **must** be adjusted to obtain free travel.
>
> Tighten the capscrew.
>
> **Момент затяжки · Torque Value**
> 47 n•m [35 ft-lb]
>
> ### Measure
>
> Rotate the engine **clockwise**, as viewed from the front of the engine, until the B mark on the engine damper aligns with the mark on the lower gear housing cover, and the intake and exhaust valves are closed on cylinder number 4.
>
> The rocker levers on cylinder number 4 **must** be loose. If they are **not**, rotate the engine 360 degrees and check the rocker levers again to make sure the intake and exhaust valves are closed on cylinder number 4. Both sets of valves are closed when the rocker levers are loose.
>
> Install the piston travel dial indicator (1) and adapter (2) onto the service tool installed in cylinder number 3.
>
> The adapter **must** touch the tool with the indicator facing the operator. Tighten the thumb screw.
>
> The dial indicator **must** also be fully seated into the adapter. Tighten the thumb screw.
>
> Use the following procedure to locate engine TDC on cylinder number 3.
>
> Rotate the engine **clockwise** until the piston plunger rod reaches its full upper travel position.
>
> Rotate the engine **counterclockwise** and **clockwise** while observing the dial indicator needle movement.
>
> Rotate the engine **clockwise** until needle movement stops.
>
> Zero the dial indicator by adjusting the outer ring and locking it into place. Repeat this step several times to be sure of TDC accuracy.
>
> **Note · Примечание**
> Always set the dial indicator to "0" (zero) at TDC, with the crankshaft having just been rotated in the direction of normal rotation **(clockwise)** to reduce any timing errors due to gear backlash.
>
> Rotate engine **counterclockwise** to 6.35 mm \[0.250 in\] before top dead center (BTDC). The large needle on the dial indicator will make 2-1/2 revolutions and will move in a **counterclockwise** motion.
>
> **Note · Примечание**
> The piston **must** be positioned at 5.161 mm \[0.2032 in\] BTDC to avoid a timing measurement error.
>
> Rotate engine **clockwise** until the dial indicator reads 5.161 mm \[0.2032 in\] BTDC. The indicator needle will move in a **clockwise** motion.
>
> **Note · Примечание**
> This step **must** be performed to prevent an error in measurement.
>
> Loosen cylinder number 4 injector adjusting screw locknut and retract the adjusting screw completely, so there is no load on the injector link. The injector lever **must** rock back and forth freely.
>
> Tighten the injector adjusting screw until just to the point the injector lever will **not** rock any longer.
>
> Tighten the adjusting screw one additional turn (360 degrees). Hand-tighten the locknut while making sure the adjusting screw does **not** turn.
>
> Tighten the adjusting screw locknut.
>
> **Момент затяжки · Torque Value**
> 47 n•m [35 ft-lb]
>
> Install injection travel indicator bracket, Part Number 2892427, onto the service tool installed in cylinder number 3. The bracket **must** extend over cylinder number 4.
>
> Hand-tighten the bracket retainer.
>
> Assemble the indicator probe onto the injection travel dial indicator.
>
> Install the injection travel indicator and adapter onto the bracket, Part Number 2892427. The adapter **must** rest 9.5 mm \[0.375 in\] above the bracket.
>
> Tighten the thumb screw.
>
> The dial indicator **must** be facing toward the operator.
>
> **Note · Примечание**
> Some injector upper spring retainers have a step where the measurement probe sits, so pay close attention that the probe does **not** slip during the injection measurement step. If the probe slips, timing errors will occur.
>
> The measurement probe **must** be oriented so that it contacts the injector upper spring retainer as close to the crankshaft center line as possible. Take special care to make sure the probe does **not** contact the injector lever or crosshead. The probe **must** be positioned at the crankshaft centerline to avoid measurement errors.
>
> Hand-tighten the probe locknut with a 6.35 mm \[1/4 in\] wrench.
>
> Zero the injection travel indicator by adjusting the outer ring and locking it into place. Make sure all thumb screws are tight and the indicator remains at zero (0).
>
> Check that the piston travel indicator still reads 5.161 mm \[0.2032 in\] BTDC.
>
> **Note · Примечание**
> Do **not** watch the piston travel dial indicator. At this point in the procedure, that indicator movement is no longer needed.
>
> Rotate the engine **clockwise** while watching the large needle on the injection travel indicator on cylinder number 4, until the needle stops moving. Note the needle will move **counterclockwise**.
>
> When the needle stops moving, record the reading of the injection travel indicator. Pay close attention to the number of revolutions the indicator travels. Each full revolution is 2.54 mm \[0.100 in\].
>
> **Note · Примечание**
> The injection travel indicator is read in a **counterclockwise** direction from "0" (zero). The total amount of travel represents the injection timing value.
>
> Compare the reading of the injection travel indicator to the specification listed for the engine's CPL found in the Critical Parts List (CPL) table. Use the following procedure for ISX, QSX static timing wedge values. Refer to Procedure 850-029 in Section V.
>
> This table can also be found by typing in the engine serial number (ESN) into QuickService™ Online then selecting the Warranty Tab. Under the Warranty Tab select Engine Dataplate. On the engine dataplate screen click on the engine CPL number and it will take you to a Critical Parts List Screen. Select the link titled ISX QSX Static Timing Wedge. Find the engine CPL for the engine you are working on in the table. Record the nominal injection timing value for the correct CPL. Compare the nominal CPL value to the injection timing value you just measured on the engine. Proceed to the next step.
>
> The engine CPL can be found on the engine dataplate located on the rocker lever cover.
>
> If the injection timing is **not** within the specified limits, check the following:
>
> - Is the timing tool correctly installed?
> - Are the dial indicators correctly adjusted?
> - Has the crankshaft been rotated in the correct direction and timing sequence?
>
> If these steps have been verified to be correct and the engine is out of time, proceed with the next step to determine whether the injection timing is retarded or advanced.
>
> If the indicator reading is higher than the nominal specification, the timing is retarded.
>
> If the indicator reading is lower than the nominal specification, the timing is advanced.
>
> **Note · Примечание**
> The injection timing can be changed by using different wedges supplied in service tool, Part Number 2892426. Each 1/4-degree wedge will change timing by approximately 0.1016 mm \[0.004 in\].
>
> - 4.25 Degree Wedge – Advance Timing by 0.1016 mm \[0.004 in\]
> - 4.50 Degree Wedge – Advance Timing by 0.2032 mm \[0.008 in\]
> - 4.75 Degree Wedge – Advance Timing by 0.3048 mm \[0.012 in\]
>
> Select the appropriate wedge and perform the base engine timing procedure. [[10-001-088-tr — Engine Base Timing|Refer to Procedure 001-088 in Section 1.]] Use the crankshaft pin and selected wedge to change the injection timing to bring it into specification. Once the base engine timing has been completed, repeat this procedure and measure the injection timing again to make sure the injection timing is now within specification.
>
> Update the engine dataplate to reflect the degree wedge used to obtain nominal engine timing.
>
> Remove the injection timing tool and injector bore adapter.
>
> Use new o-rings and install cylinder number 3 injector. [[10-006-026-tr — Injector|Refer to Procedure 006-026 in Section 6.]]
>
> Install the valve crossheads.
>
> Install the rocker lever assemblies. [[10-003-009-tr — Rocker Lever Assembly|Refer to Procedure 003-009 in Section 3.]]
>
> Adjust the valves and injectors. [[10-003-004-tr — Overhead Set|Refer to Procedure 003-004 in Section 3.]]
>
> Install the rocker lever cover. Refer to Procedure 003-011 in Section 3.
>
> Remove the barring device and install the oil fill tube. Refer to Procedure 007-065 in Section 7.
