---
type: "Процедура"
doc: "40-005-058"
title_en: "Speed Droop Governor"
modified: "2003-09-23"
engines:
  - "93047320"
families:
  - "6B5.9"
manuals:
  - "3666087"
figures: 2
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-005-058.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-005-058.pdf"
tags:
  - "документ/процедура"
  - "двигатель/6B5.9"
  - "группа/40"
  - "перевод/машинный"
---

# Speed Droop Governor

> [!abstract] Процедура · `40-005-058`
> **Двигатели:** [[93047320 — 6B5.9 CPL 3111|93047320]]
> **Семейство:** 6B5.9
> **Входит в руководства:** [[3666087 — B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual|3666087]]
> **Секции:** Section 5 - Fuel System - Group 05
> **Даты:** изменён 2003-09-23
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-005-058.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-005-058.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Регулировка

Станадин

Stanadyne DB4 (Generator Application) — губернатор скоростного спуска

Регулирование губернатора от 3 до 5 процентов может быть достигнуто с помощью губернатора с пониженной скоростью. Точный контроль над губернаторским регулированием осуществляется путем уменьшения или увеличения эффективной длины губернаторского пружины; это также уменьшает или увеличивает весенний весенний коэффициент контроля. Рессор управления губернатора втиснут в сборку регулируемой колпачки и называется сборкой управляющего стержня. Повернув регулировочный колпачок в направлении **часовой стрелки**, как видно из конца перекачки топлива, пружина управляющего стержня укорачивается и становится менее чувствительной, тем самым увеличивая регулирование регулятора. Поворот регулировочного колпачка в направлении **против часовой стрелки** увеличивает длину и чувствительность пружины управления, что снизит регулирование губернатора.

Винт регулировки внешнего скоростного сужения, расположенный в задней части корпуса насоса впрыска топлива, контролирует чувствительность регулятора. Корректировка винта свисания изменяет регулирование губернатора, изменяя эффективную весеннюю ставку. Эта настройка повлияет как на полную, так и на частоту без нагрузки, и может потребовать сброса высокоскоростного стоп-винта.

Корректировка скорости **должна быть сделана во время работы двигателя. После каждой регулировки винта сбрасывания двигатель **должен быть выключен на короткое время, чтобы позволить пружине-губернатору разгрузиться, а механизм регулировки искать свое окончательное положение пружиной. Вращение винта сокращает пружину управления, делая ее менее чувствительной и увеличивая скорость свисания. Включение регулировочного винта имеет противоположный эффект. Скорость сбрасывания - это способность впрыска топлива реагировать на изменение нагрузки двигателя.

![[05900604.png]]

Скорость Droop регулировка

> [!note] Примечание
> Если в период разминки происходит серьезный подъём, поверните винт регулировки скорости **по часовой стрелке** до остановки подъёма.

> [!note] Примечание
> Когда вносятся регулировки скорости сбрасывания, необходимо регулировать положение дроссельной заслонки.

Изменить губернатора следующим образом:

1. Работайте с двигателем до тех пор, пока не будет достигнута нормальная рабочая температура 91°C[195°F].
2. Когда двигатель достигает рабочей температуры, поместите дросселя, чтобы достичь номинальной скорости, и приложите 100-процентную нагрузку. Отрегулируйте положение дроссельной заслонки по мере необходимости, чтобы получить 100-процентную производительность.
3. Снимите нагрузку и проверьте наличие указанной незагруженности или, в случае генераторной установки, обратите внимание на частоту. Если скорость без нагрузки неверна, ослабьте запирающую крышку и отрегулируйте винт регулировки скорости сбрасывания (**по часовой стрелке** для увеличенного сбрасывания, **против часовой стрелки** для меньшего сбрасывания). Если при снятии нагрузки происходит подъём, поверните регулировочную крышку **по часовой стрелке**, чтобы исключить подъём. Закрепите запирающую крышку, чтобы закрепить регулирующий винт.
4. Проверьте 100-процентную нагрузку и производительность без нагрузки снова и внесите коррективы по мере необходимости.

![[05900604.png]]


> [!quote]- Original (English) · английский оригинал
> ### Adjust
>
> Stanadyne
>
> Stanadyne DB4 (Generator Application) Speed Droop Governor
>
> Governor regulation of 3 percent to 5 percent can be attained with the speed droop governor. Precise control of governor regulation is done by decreasing or increasing the effective length of the governor control spring; this also decreases or increases the spring control spring rate. The governor control spring is threaded into an adjusting cap assembly and is referred to as the control rod assembly. By turning the adjusting cap in the **clockwise** direction, as viewed from the fuel transfer pump end, the control rod spring shortens and becomes less sensitive, thereby increasing governor regulation. Turning the adjusting cap in the **counterclockwise** direction increases the control rod spring length and sensitivity, which will decrease governor regulation.
>
> The external speed droop adjustment screw, located at the rear of the fuel injection pump housing, controls the governor sensitivity. The droop screw adjustment varies the governor regulation by changing the effective spring rate. This adjustment will affect both full-load and no-load frequency settings and can require the high-speed stop screw be reset.
>
> Speed droop adjustments **must** be made while the engine is operating. After each adjustment of the droop screw, the engine **must** be shutdown briefly in order to allow the governor spring to unload and the adjusting mechanism to seek its final position in the spring. Turning the screw in shortens the control spring, making it less sensitive and increasing speed droop. Turning the adjusting screw out has the opposite effect. Speed droop is the fuel injection pump's ability to respond to changing engine loads.
>
> Speed Droop Adjustment
>
> **Note · Примечание**
> If serious surging occurs during the warm-up period, turn the speed droop adjusting screw **clockwise** until the surging stops.
>
> **Note · Примечание**
> When the speed droop adjustments are made, it is necessary to adjust the throttle position.
>
> Adjust the governor as follows:
>
> 1. Operate the engine until normal operating temperature is obtained 91°C \[195°F\].
> 2. When the engine reaches operating temperature, position the throttle to attain rated speed, and apply 100-percent load. Adjust the throttle position as necessary to obtain 100 percent performance.
> 3. Remove the load, and check for the specified no-load or, in the case of a generator set, note the frequency. If the no-load speed is incorrect, loosen the locking cap, and adjust the speed droop adjusting screw (**clockwise** for increased droop, **counterclockwise** for less droop). If surging occurs when the load is removed, turn the adjusting cap **clockwise** to eliminate the surge. Tighten the locking cap to secure the adjusting screw.
> 4. Check the 100-percent load and no-load performance again, and make adjustments as necessary.
