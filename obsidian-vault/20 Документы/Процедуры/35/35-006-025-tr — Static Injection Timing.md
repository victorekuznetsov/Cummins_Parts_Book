---
aliases:
  - "Статическая установка угла опережения впрыска"
type: "Процедура"
doc: "35-006-025-tr"
title_en: "Static Injection Timing"
title_ru: "Статическая установка угла опережения впрыска"
modified: "2020-02-04"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
figures: 22
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-006-025-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-006-025-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/35"
  - "перевод/машинный"
---

# Static Injection Timing
**Статическая установка угла опережения впрыска**

> [!abstract] Процедура · `35-006-025-tr`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 6 - Injectors and Fuel Lines - Group 06 · Section 6- Injectors and Fuel Lines - Group 06
> **Даты:** изменён 2020-02-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-006-025-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-006-025-tr.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Настройка

- Снимите крышку коромысел.[[35-003-011-tr — Rocker Lever Cover|См. процедуру 003-011 в разделе 3.]]
- Удалите форсунка из цилиндра номер один. См. процедуру 006-026 в разделе 6.

> [!note] Примечание
> не обязательно удалять весь форсунка; однако вращение двигателя будет легче при удалении всего форсунки.

![[fi200md.png]]

Средство синхронизации, часть 3824942, может быть установлено без удаления обсадного кожуха.

Установите поршневой плунжер (1) в цилиндр форсунки цилиндра номер один.

![[it200jr.png]]

Выровнять поворотную кронштейн (2) с помощью форсунки с удерживающим болтом.

Установите болты, номер детали 3823600, через поворотную кронштейн. Болты включены в комплект инструментов для определения времени.

![[it200js.png]]

> [!warning] ОСТОРОЖНО
> Не затягивайте болты слишком плотно. Болты могут быть повреждены.

Затягивайте болты (3) достаточно, чтобы жестко удерживать фиксатор времени.

![[it200jt.png]]

Поместите инструмент тайминга толкающую трубку плунжерную кронштейн (4) на задней стороне центральной кронштейн (5).

![[it200ju.png]]

Используйте инструмент выравнивания (6), Номер детали 3824947, чтобы выровнять толкатель плунжер (7).

Обязательно затяните ручку (8) зажима после выравнивания плунжерного стержня и удалите инструмент выравнивания.

![[it200jv.png]]

Установите топливный форсунок (9) между топливным форсуном распределительного вала и плунжерным стержнем.

Толчок (9) **должен быть вертикально выровнен с плунжерным стержнем. Если это **не**, то в результате будут получены неправильные значения времени. Будьте осторожны **не, чтобы сбросить толкатель в двигатель.

![[it200jw.png]]

### Измерение

> [!warning] ОСТОРОЖНО
> Используйте вспомогательный вал привода для вращения коленчатого вала. Если используется другой метод, то время впрыска не будет правильным, или двигатель может быть поврежден.

Определить центр поршня сверху мертвым (TDC) по ходу сжатия путем поворота вспомогательного вала привода **по часовой стрелке**.

Поршень находится на сжатии, когда оба плунжера движутся в направлении вверх одновременно. TDC обозначается максимальным **по часовой стрелке** положением указателя индикатора движения поршня.

![[it200jx.png]]

> [!warning] ОСТОРОЖНО
> Оба индикатора должны иметь диапазон перемещения не менее 6,35 мм \[0,250-в\], иначе индикаторы будут повреждены.

Поместите контактный наконечник измерительной стрелки в центр плунжерного стержня и опустите измерительный стрелок в пределах 0,63 мм \[0,025-в\] полностью сжатого положения.

![[it200jy.png]]

Установите индикатор циферблата на поршневой плунжерный стержень до нуля «0», когда поршневой плунжерный стержень достиг максимального движения вверх на TDC.

![[it200jz.png]]

Поверните дополнительный вал взад и вперед, до и после нулевого значения индикатора «0», примерно на 3 градуса, чтобы убедиться, что поршень находится на TDC.

![[it200jd.png]]

Поверните дополнительный вал привода **по часовой стрелке** до 90 градусов после TDC.

Поршневой плунжер будет на отметке «L10 90 градусов» на временном креплении.

![[it200je.png]]

Поместите указатель контакта с наконечником индикатора push-rod в центре плунжерного стержня и опустите калибр в пределах 0,63 мм \[0,025 в\] полностью сжатого положения.

Установите индикатор push-rod dial на ноль «0».

Вращайте дополнительный вал привода **против часовой стрелки** в TDC.

![[it200jf.png]]

Продолжайте вращать вспомогательный вал **против часовой стрелки **до тех пор, пока коленчатый вал не достигнет 45 градусов перед TDC. Этот шаг необходим для удаления обратной реакции передачи в двигателе.

![[it200jg.png]]

Поверните дополнительный вал привода **по часовой стрелке**, медленно, пока измеритель перемещения поршня не достигнет 5,160 мм \[0,2032-в\] перед TDC.

Если коленчатый вал вращается за пределами 5,160-мм \[0,2032-в\] перед положением TDC, коленчатый вал **должен** вращаться против часовой стрелки, обратно к 45 градусам перед отметкой TDC.

![[it200jh.png]]

Прочтите измеритель движения толкателя **против часовой стрелки** от нуля "0". Это путешествие представляет собой значение времени впрыска. В показанном примере значение составляет 1,98 мм \[0,078-в\].

![[it200ji.png]]

Чтобы проверить правильное время впрыска для конкретного двигателя, проверьте код времени впрыска форсунки на табличке данных двигателя.[[35-100-001-tr — Engine Identification|См. процедуру 100-001 в разделе Е для определения местоположения таблички с данными двигателя]]. Сроки кодов перечислены как два алфавитных символа, которые относятся к числовой спецификации.

Спецификации можно найти в таблице статических временных кодов в руководстве по контрольной части (CPL), бюллетене 4021327 или 4021328.

![[06a00163.png]]

Если показания индикатора ниже спецификации, то время увеличивается.

Если показания индикатора выше, чем спецификация, то время задержки.

Толчок должен быть вертикально выровнен с плунжером, или в результате будут получены неправильные значения времени. Повторите процедуру, если есть сомнения.

![[it200jj.png]]

Сроки впрыска можно изменить, удалив распределительную передачу и установив смещенную клавишу.[[35-001-012-tr — Camshaft Gear (Camshaft Installed)|См. процедуру 001-012 в разделе 1.]]

![[it200jk.png]]

В прилагаемой таблице перечислены смещенные ключи по номеру части и степени смещения.

Никогда не продвигайте сроки впрыска сверх пределов спецификации. Долговечность двигателя будет снижена.

![[lt200nb.png]]

Если стрелка на ключе указывает на двигатель, время замедляется.

Если стрелка указывает в сторону от двигателя, время увеличивается.

После установки нового ключа времени **всегда** перепроверяйте время, чтобы убедиться, что оно соответствует спецификациям.

![[cg2kegc.png]]

- Установите форсунку (форсунки).[[35-006-026-tr — Injector|См. процедуру 006-026 в разделе 6.]]
- Установите крышку коромысел.[[35-003-011-tr — Rocker Lever Cover|См. процедуру 003-011 в разделе 3.]]

![[fi2bdhg.png]]


> [!quote]- Original (English) · английский оригинал
> ### Setup
>
> - Remove the rocker lever cover. [[35-003-011-tr — Rocker Lever Cover|Refer to Procedure 003-011 in Section 3.]]
> - Remove the injector from cylinder number one. Refer to Procedure 006-026 in Section 6.
>
> **Note · Примечание**
> It is **not** necessary to remove all injectors; however, engine rotation will be easier with all injectors removed.
>
> The timing tool, Part Number 3824942, can be installed without removing the rocker housing.
>
> Install the piston plunger rod (1) in the injector bore of number one cylinder.
>
> Align the swivel bracket (2) with the injector hold-down capscrew hole.
>
> Install capscrew, Part Number 3823600, through the swivel bracket. The capscrew is included with the timing tool kit.
>
> **CAUTION · Осторожно**
> Do not tighten the capscrew too tightly. The capscrew can be damaged.
>
> Tighten the capscrew (3) enough to hold the timing fixture rigidly.
>
> Position the timing tool push tube plunger bracket (4) on the backside of the center bracket (5).
>
> Use the alignment tool (6), Part Number 3824947, to align the push rod plunger rod (7).
>
> Be sure to tighten the clamp handle (8) after the plunger rod is aligned, and remove the alignment tool.
>
> Install the injector push rod (9) between the injector camshaft follower and the plunger rod.
>
> The push rod (9) **must** be vertically aligned with the plunger rod. If it is **not**, incorrect timing values will result. Be careful **not** to drop the push rod into the engine.
>
> ### Measure
>
> **CAUTION · Осторожно**
> Use the accessory driveshaft to rotate the crankshaft. If another method is used, the injection timing will not be correct, or the engine can be damaged.
>
> Determine the piston top dead center (TDC) on the compression stroke by rotating the accessory driveshaft **clockwise**.
>
> The piston is on the compression stroke when both plungers move in an upward direction at the same time. TDC is indicated by the maximum **clockwise** indicator position of the piston travel indicator pointer.
>
> **CAUTION · Осторожно**
> Both indicators must have a travel range of at least 6.35-mm \[0.250-in\], or the indicators will be damaged.
>
> Position the gauge contact tip in the center of the plunger rod, and lower the gauge to within 0.63-mm \[0.025-in\] of the fully compressed position.
>
> Set the dial indicator over the piston plunger rod to zero "0" when the piston plunger rod has reached maximum upward movement at TDC.
>
> Rotate the accessory driveshaft back and forth, before and after the zero "0" indicator reading, for approximately 3 degrees, to be sure the piston is at TDC.
>
> Rotate the accessory driveshaft **clockwise** to 90-degrees after TDC.
>
> The piston plunger will be at the "L10 90 degree" mark on the timing fixture.
>
> Position the push rod dial indicator contact tip in the center of the plunger rod, and lower the gauge to within 0.63 mm \[0.025 in\] of the fully compressed position.
>
> Set the push rod dial indicator to zero "0."
>
> Rotate the accessory driveshaft **counterclockwise** to TDC.
>
> Continue to rotate the accessory driveshaft **counterclockwise** until the crankshaft is at 45-degrees before TDC. This step is necessary to remove gear backlash in the engine.
>
> Rotate the accessory driveshaft **clockwise**, slowly, until the piston travel gauge is at 5.160-mm \[0.2032-in\] before TDC.
>
> If the crankshaft is rotated beyond the 5.160-mm \[0.2032- in\] before TDC position, the crankshaft **must** be rotated **counterclockwise**, back to the 45-degrees before TDC mark.
>
> Read the push rod travel gauge **counterclockwise** from zero "0." This travel represents the injection timing value. In the example shown, the value is 1.98-mm \[0.078-in\].
>
> To verify the correct injection timing for a particular engine, check the injector timing code on the engine dataplate. [[35-100-001-tr — Engine Identification|Refer to Procedure 100-001 in Section E for the engine dataplate location]]. Timing codes are listed as two alphabetical characters that relate to a numberical specification.
>
> Specifications can be found in the Static Timing Codes chart in the Control Part List (CPL) Manual, Bulletin 4021327 or 4021328.
>
> If the indicator reading is lower than the specification, the timing is advanced.
>
> If the indicator reading is higher than the specification, the timing is retarded.
>
> The push rod **must** be vertically aligned with the plunger, or incorrect timing values will result. Repeat the procedure if in doubt.
>
> Injection timing can be changed by removing the camshaft gear and installing an offset key. [[35-001-012-tr — Camshaft Gear (Camshaft Installed)|Refer to Procedure 001-012 in Section 1.]]
>
> The accompanying table lists offset keys by part number and degree of offset.
>
> **Never** advance injection timing beyond the specification limits. The engine's durability will be diminished.
>
> If the arrow on the key is pointing toward the engine, the timing is retarded.
>
> If the arrow is pointing away from the engine, the timing is advanced.
>
> After installing a new timing key, **always** recheck the timing to be sure it is within the specifications.
>
> - Install the injector(s). [[35-006-026-tr — Injector|Refer to Procedure 006-026 in Section 6.]]
> - Install the rocker lever cover. [[35-003-011-tr — Rocker Lever Cover|Refer to Procedure 003-011 in Section 3.]]
