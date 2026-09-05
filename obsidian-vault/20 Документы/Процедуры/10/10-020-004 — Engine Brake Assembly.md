---
type: "Процедура"
doc: "10-020-004"
title_en: "Engine Brake Assembly"
modified: "2008-10-27"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
manuals:
  - "3666251"
figures: 34
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-020-004.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-020-004.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSX15"
  - "группа/10"
  - "перевод/машинный"
---

# Engine Brake Assembly

> [!abstract] Процедура · `10-020-004`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Входит в руководства:** [[3666251 — Signature and ISX Operation and Maintenance Manual|3666251]]
> **Секции:** Section 11 - Maintenance Procedures at 800,000 Kilometers [500,000 Miles], 10,000 Hours, or 5 Years
> **Даты:** изменён 2008-10-27
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-020-004.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-020-004.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

> [!warning] ОСТОРОЖНО
> Не подключайте проводку двигателя к ветке провода к разъему ремня. Подключение проводов тормозной ветки двигателя к проводной ветке двигателя даст ложное считывание при проверке сопротивления.

Отсоедините разъём ремня электропроводки двигателя от проходящего через разъем головки цилиндра.

Подключите один конец проводов тормозной системы двигателя, номер детали 3163150, к разъёму цилиндра.

![[20c00007.png]]

> [!note] Примечание
> Черный измерительный порт на проводах тормозной ветки двигателя, ветвь кабельной коробки, является общей основой для всех трех соленоидов. Белые испытательные порты (1, 2 и 3) используются для проверки сопротивления соответствующих соленоидов тормоза (1, 2 и 3).

![[20c00022.png]]

> [!note] Примечание
> Ключ зажигания **должен быть** в положении **OFF**.

Проверьте сопротивление каждого соленоида.

- **Холодный двигатель** - от 8 до 10 Ом
- **Горячий двигатель** - от 16 до 20 Ом.

- **Холодный двигатель** - от 32 до 40 Ом
- **Горячий двигатель** - от 60 до 80 Ом.

> [!note] Примечание
> Если **не** в пределах спецификации, с использованием ветки ремня тормозной проводов двигателя, ремень тормозной проводов двигателя и соленоиды должны быть проверены отдельно для идентификации неисправного компонента.[[10-020-012 — Engine Brake Solenoid Valve|См. процедуру 020-012 (Двигатель тормоза соленоидного клапана) в разделе 20.]] [[10-020-015 — Engine Brake Wiring Harness|См. процедуру 020-015 (Применение электропроводки двигателя) в разделе 20.]]

![[20c00023.png]]

### Проверка напряжения

Отсоедините разъём ремня электропроводки двигателя от проходящего через разъем головки цилиндра.

Подключите один конец проводов тормозной системы двигателя к ветке жгута проводов, номер детали 3163150, к проходящему через цилиндр разъему, а другой конец к разъему ремня электропроводки двигателя.

![[20c00026.png]]

Подключите красный аллигаторный зажим проводов тормоза двигателя к ветвящему кабелю к напряжению батареи и черный аллигаторный зажим к земле.

![[20c00005.png]]

> [!note] Примечание
> Черный измерительный порт на проводах тормозной ветки двигателя, ветвь кабельной коробки, является общей основой для всех трех соленоидов. Белые испытательные порты (1, 2 и 3) используются для считывания напряжения соответствующих тормозных соленоидов 1, 2 и 3.

![[20c00022.png]]

> [!note] Примечание
> Ключ зажигания **должен** находиться в положении **ON**.

Проверьте напряжение каждого соленоида.

Напряжение должно быть 12-VDC для каждого соленоида.

> [!note] Примечание
> Если **не** в пределах спецификации, с использованием ветки ремня тормозной проводов двигателя, ремень тормозной проводов двигателя и соленоиды должны быть проверены отдельно для идентификации неисправного компонента.[[10-020-012 — Engine Brake Solenoid Valve|См. процедуру 020-012 (Двигатель тормоза соленоидного клапана) в разделе 20.]] [[10-020-015 — Engine Brake Wiring Harness|См. процедуру 020-015 (Применение электропроводки двигателя) в разделе 20.]]

![[20c00024.png]]

### Первичная проверка

Электромагнит моторного тормоза

Отсоедините разъём ремня электропроводки двигателя от проходящего через разъем головки цилиндра.

Подключите один конец проводов тормозной системы двигателя к ветке жгута проводов, номер детали 3163150, к проходящему через цилиндр разъему, а другой конец к разъему ремня электропроводки двигателя.

![[20c00007.png]]

> [!note] Примечание
> Ключ зажигания должен быть в положении выключения.

- Кнопка "Нет". 1 актуирует соленоид No. 1 и тормоз № 1.
- Кнопка "Нет". 2 активирует соленоид No. 2 и тормоза № 2 и 3.
- Кнопка "Нет". 3 активирует соленоид No. 3 и тормоза № 4, 5 и 6.

![[20c00032.png]]

Нажмите на кнопку ветвления кабельной коробки (1, 2 или 3) для активации соответствующего соленоида (1, 2 или 3) тормоза двигателя.

Слушайте щелчок при активации соленоида тормоза. Если при нажатии кнопки не слышен щелчок, соответствующий соленоидный клапан и ремень тормозной проводов двигателя должны быть проверены отдельно для идентификации неисправного компонента.[[10-020-012 — Engine Brake Solenoid Valve|См. процедуру 020-012 (Двигатель тормоза соленоидного клапана) в разделе 20.]] [[10-020-015 — Engine Brake Wiring Harness|См. процедуру 020-015 (Применение электропроводки двигателя) в разделе 20.]]

![[20c00008.png]]

Рука качения клапана тормозного клапана

Снимите крышку коромысел. См. процедуру 003-011 (клапанная крышка для качения клапанов) в разделе 3.

![[03c00002.png]]

Установите брызговик, номер детали 3163092, чтобы уменьшить количество масла, выбрасываемого приводом топливного насоса.

Запускай двигатель.

![[20c00009.png]]

Нажмите на кнопку ветвления кабельной коробки (1, 2 или 3) для активации соответствующего соленоида (1, 2 или 3) тормоза двигателя.

Проверьте соответствующий рычаг(ы) тормоза двигателя и соленоид на предмет:

- Развертывание поршневого тормоза двигателя
- Утечка из верхних уплотнения соленоида.

Замените детали по мере необходимости.[[10-020-012 — Engine Brake Solenoid Valve|См. процедуру 020-012 (Двигатель тормоза соленоидного клапана).]]См. процедуру 020-017 (клапан управления тормозами двигателя). См. процедуру 020-019 (Тормозной поршень двигателя) в разделе 20.

![[20c00010.png]]

### Регулировка

Все регулировки накладных расходов должны быть сделаны, когда двигатель холодный (любая стабилизированная температура охлаждающей жидкости при 60°C \[140°F\] или ниже).

![[03c00102.png]]

> [!warning] ОСТОРОЖНО
> Не используйте растворитель для очистки прокладки крышки скалолаза. Растворитель может повредить прокладочный материал и вызвать его набухание.

Удалите крышку рычага клапанного клапана и прокладку. См. процедуру 003-011 (клапанная крышка для качения клапанов) в разделе 3.

![[03c00002.png]]

> [!note] Примечание
> Ранние вибрационные амортизаторы двигателя отмечены BRAKE SET 1-6, BRAKE SET 2-5 или BRAKE SET 3-4. Тормоза двигателя **должны быть установлены на соответствующих отметках на этих двигателях. Новые вибрационные амортизаторы двигателя помечены **только A, B или C и регулируются клапанами и топливным форсункой на том же цилиндре.

Найдите знаки клапана на внешней стороне вибрационного демпфера.

Назначения A, B и C:

Настроен на маркировку А для регулировки цилиндра 1 или 6.

Набор для маркировки B для регулировки цилиндра 2 или 5.

Настроен на маркировку C для регулировки цилиндра 3 или 4.

> [!note] Примечание
> Для установки всех клапанов, тормозов двигателя и форсунки требуется два полных оборота.

![[17c00090.png]]

С воздушным компрессором:

Удалите масляный разъем из нижней крышки коробки передач.

Вставьте 3/4-дюймовый приводной скоб и удлинитель в привод воздушного компрессора.

Вращайте привод воздушного компрессора **по часовой стрелке**, как видно с передней части двигателя.

![[17c00091.png]]

> [!danger] ОПАСНО
> Не тяните и не потянитесь на вентилятор, чтобы вручную вращать двигатель. Это может повредить лопасти вентилятора. Поврежденные лопасти вентилятора могут вызвать преждевременные сбои вентилятора, которые могут привести к серьезным травмам или имущественному ущербу.

Вращение коленчатого вала происходит по часовой стрелке, как видно из передней части двигателя.

Цилиндры пронумерованы спереди двигателя (1-2-3-4-5-6).

Заказ на стрельбу двигателя составляет 1-5-3-6-2-4.

![[17c00092.png]]

Без воздушного компрессора:

Освободите болты и поверните крышку или удалите масляную трубку, если она оборудована.

![[00c00060.png]]

Используйте 1 1/2-дюймовую розетку, толкайте двигатель, превращающий передачу в сетку передач и барный двигатель по **против часовой стрелки**.

> [!note] Примечание
> Скачайте заграждающее устройство туда и обратно, пока оно не отключится.

![[00c00061.png]]

Каждый цилиндр имеет четыре рычага:

- Рука качения клапана выпускного клапана (1)
- Рука винта форсунки (2)
- Рука впускного клапана клапана качения (3)
- Рука качения клапана тормозного клапана двигателя (4).

> [!note] Примечание
> Впускной клапан клапана рычага качения **всегда **длинный рычаг на клапан клапана качели вала качения.

![[17c00093.png]]

> [!note] Примечание
> Ранние вибрационные амортизаторы двигателя отмечены BRAKE SET 1-6, BRAKE SET 2-5 или BRAKE SET 3-4. Тормоза двигателя **должны быть установлены на соответствующих отметках на этих двигателях. Новые вибрационные амортизаторы двигателя помечены **только A, B или C и регулируются клапанами и топливным форсункой на том же цилиндре.

Клапаны, тормоза и форсунка на одном цилиндре регулируются с одинаковым индексным знаком на вибрационном демпфере.

| Подпись, ISX и QSX15 |  |  |
|---|---|---|
| Последовательность торможения |  |  |
| Барный двигатель в направлении вращения | Позиция Пулли | тормоз |
| Начинать | А. | 1 |
| Продвижение к | B | 5 |
| Продвижение к | C | 3 |
| Продвижение к | А. | 6 |
| Продвижение к | B | 2 |
| Продвижение к | C | 4 |
| Приказ об обстреле: 1-5-3-6-2-4 |  |  |

![[nobox.png]]

Вращайте привод компрессора или заграждающее устройство в направлении вращения двигателя, **по часовой стрелке**. Нанести знак А на вибрационный демпфер с указателем на крышке передач.

> [!note] Примечание
> Для иллюстративных целей позиция А показана в качестве первого шага. необязательно начинать с позиции А, если соблюдена правильная последовательность.

![[17c00095.png]]

Проверьте рычаги качения клапана на данном цилиндре, чтобы увидеть, закрыты ли впускные и выпускные клапаны.

> [!note] Примечание
> Оба комплекта клапанов закрываются, когда рычаги качения и рычаг тормоза свободны. Если оба комплекта клапанов **не** закрыты, поверните приводную передачу компрессора на один полный оборот и снова выровните отметку А на переднем демпфере с указателем.

![[17c00096.png]]

> [!warning] ОСТОРОЖНО
> Для достижения максимальной эффективности работы тормоза и предотвращения повреждения двигателя необходимо следовать инструкциям по регулировке тормозов.

Для старых двигателей найдите отметки тормозов двигателя на внешней стороне вибрационного демпфера.

Наборы обозначены как BRAKE SET 1-6, BRAKE SET 2-5 и BRAKE SET 3-4.

**BRAKE SET 1-6:** Цилиндр 1 или 6 регулировка

**BRAKE SET 2-5:** Цилиндр 2 или 5 регулировка

**BRAKE SET 3-4:** Цилиндр 3 или 4 регулировка

![[20c00003.png]]

Вращайте привод компрессора или заграждающее устройство в направлении вращения двигателя, **по часовой стрелке**. Нанести знак А на вибрационный демпфер с указателем на крышке передач.

> [!note] Примечание
> Для иллюстративных целей позиция А показана в качестве первого шага. необязательно начинать с позиции А, если соблюдена правильная последовательность.

![[17c00095.png]]

Проверьте рычаги качения клапана на данном цилиндре, чтобы увидеть, закрыты ли впускные и выпускные клапаны.

> [!note] Примечание
> Оба комплекта клапанов закрываются, когда рычаги качения и рычаг тормоза свободны. Если оба комплекта клапанов **не** закрыты, поверните приводную передачу компрессора на один полный оборот и снова выровните отметку А на переднем демпфере с указателем.

![[17c00096.png]]

Нажмите на рычаг тормоза двигателя, чтобы убедиться, что распределитель распределительного вала находится в контакте с распределительным валом.

![[20c00012.png]]

Освободите гайку на тормозном рычаге, регулирующем винт, и выйдите из регулирующего винта на один оборот.

Вставьте калибр для щупальца, номер детали 3163530, между нижней частью поршня тормоза двигателя и верхней частью штифта выхлопного клапана на мостике клапана выхлопного клапана.

| мм |  | в |
|---|---|---|
| 7.00 | НМ | 0.276 |

![[20c00013.png]]

Затягивайте регулирующий винт до тех пор, пока не прощупывается нащупывающий измеритель. Правильное сопротивление означает, что нет движения рычага тормоза, который следует за распределительным валом, против доли кулачка.

![[20c00018.png]]

Держите рычаг регулировки тормоза двигателя винтом, и затяните канат.

> [!tip] Момент затяжки
> 20 Н·м [177 фунт-дюйм]

Удалите калибр для щупальца.

![[03c00079.png]]

> [!warning] ОСТОРОЖНО
> Повреждение двигателя может произойти, если эксплуатационный зазор не входит в спецификации.

Проверьте рабочий зазор:

1. Поверните рычаг качения клапана тормозного клапана двигателя в детентное (нейтральное) положение.
2. Проверьте зазор (1) между поршнем привода рычага тормоза двигателя и направляющим штифтом клапанного моста.

| мм |  | в |
|---|---|---|
| 0.635 | Мин | 0.025 |
| 2.790 | Макс | 0.110 |

Если рабочий зазор **не** попадает в заданные спецификации, ослабьте клапанный клапанный вал качения и слегка поверните клапанный клапанный вал качения качения в направлении, необходимом для приведения рабочего зазора в пределах спецификаций.

Перепроверить тормозной зазор.

> [!note] Примечание
> Ручные валы клапанного клапана должны быть отрегулированы таким образом, чтобы все три рычага тормоза двигателя попадали в заданную спецификацию рабочего зазора.

![[03c00076.png]]

Повторите процесс для регулировки всех тормозов двигателя в соответствии с графиком, показанным ранее в этой процедуре.

![[nobox.png]]

Установите крышку рычага клапанного клапана и прокладку. См. процедуру 003-011 (клапанная крышка для качения клапанов) в разделе 3.

Если в результате отказа охлаждающая жидкость, масло, чрезмерное топливо или чрезмерный черный дым попадают в выхлопную систему, система последующей обработки должна быть проверена.[[101-014-013-tr — Aftertreatment Testing|См. процедуру 014-013 (Тестирование после лечения) в разделе 14.]]

![[03c00002.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> **CAUTION · Осторожно**
> Do not connect the engine breakout cable to the engine wiring harness connector. Connecting the engine brake breakout cable to the engine wiring harness will give a false reading when checking the resistance.
>
> Disconnect the engine wiring harness connector from the cylinder head pass-through connector.
>
> Connect one end of the engine brake breakout cable, Part Number 3163150, to the cylinder pass-through connector.
>
> **Note · Примечание**
> The black test port on the engine brake breakout cable box is the common ground for all three solenoids. The white test ports (1, 2, and 3) are used to test the resistance of the corresponding brake solenoids (1, 2, and 3).
>
> **Note · Примечание**
> The ignition key **must** be in the **OFF** position.
>
> Check the resistance of each solenoid.
>
> - **Cold engine** - 8 to 10 ohms
> - **Hot engine** - 16 to 20 ohms.
>
> - **Cold engine** - 32 to 40 ohms
> - **Hot engine** - 60 to 80 ohms.
>
> **Note · Примечание**
> If **not** within specification, using the engine brake breakout tool, the engine brake wiring harness and solenoids **must** be checked separately to identify the faulty component. [[10-020-012 — Engine Brake Solenoid Valve|Refer to Procedure 020-012 (Engine Brake Solenoid Valve) in Section 20.]] [[10-020-015 — Engine Brake Wiring Harness|Refer to Procedure 020-015 (Engine Brake Wiring Harness) in Section 20.]]
>
> ### Voltage Check
>
> Disconnect the engine wiring harness connector from the cylinder head pass-through connector.
>
> Connect one end of the engine brake breakout cable, Part Number 3163150, to the cylinder pass-through connector and the other end to the engine wiring harness connector.
>
> Connect the red alligator clip of the engine brake breakout cable to battery voltage and the black alligator clip to ground.
>
> **Note · Примечание**
> The black test port on the engine brake breakout cable box is the common ground for all three solenoids. The white test ports (1, 2, and 3) are used to read the voltage of the corresponding brake solenoids 1, 2, and 3.
>
> **Note · Примечание**
> The ignition key **must** be in the **ON** position.
>
> Check the voltage of each solenoid.
>
> The voltage should be 12-VDC for each solenoid.
>
> **Note · Примечание**
> If **not** within specification, using the engine brake breakout tool, the engine brake wiring harness and solenoids **must** be checked separately to identify the faulty component. [[10-020-012 — Engine Brake Solenoid Valve|Refer to Procedure 020-012 (Engine Brake Solenoid Valve) in Section 20.]] [[10-020-015 — Engine Brake Wiring Harness|Refer to Procedure 020-015 (Engine Brake Wiring Harness) in Section 20.]]
>
> ### Initial Check
>
> Engine Brake Solenoid
>
> Disconnect the engine wiring harness connector from the cylinder head pass-through connector.
>
> Connect one end of the engine brake breakout cable, Part Number 3163150, to the cylinder pass-through connector and the other end to the engine wiring harness connector.
>
> **Note · Примечание**
> The ignition key **must** be in the OFF position.
>
> - Button No. 1 actuates solenoid No. 1 and brake Number 1.
> - Button No. 2 actuates solenoid No. 2 and brakes Number 2 and 3.
> - Button No. 3 actuates solenoid No. 3 and brakes Number 4, 5, and 6.
>
> Press the engine brake breakout cable box button (1, 2, or 3) to activate the corresponding engine brake solenoid (1, 2, or 3).
>
> Listen for a clicking sound when activating the brake solenoid. If no clicking sound can be heard when the button is pressed, the corresponding solenoid valve and the engine brake wiring harness **must** be checked separately to identify the faulty component. [[10-020-012 — Engine Brake Solenoid Valve|Refer to Procedure 020-012 (Engine Brake Solenoid Valve) in Section 20.]] [[10-020-015 — Engine Brake Wiring Harness|Refer to Procedure 020-015 (Engine Brake Wiring Harness) in Section 20.]]
>
> Engine Brake Rocker Lever
>
> Remove the rocker lever cover. Refer to Procedure 003-011 (Rocker Lever Cover) in Section 3.
>
> Install the splash shield, Part Number 3163092, to reduce the amount of oil being thrown by the fuel pump drive gear.
>
> Start the engine.
>
> Press the engine brake breakout cable box button (1, 2, or 3) to activate the corresponding engine brake solenoid (1, 2, or 3).
>
> Check the corresponding engine brake lever(s) and solenoid for the following:
>
> - Engine brake piston deployment
> - Leakage from upper seals of solenoid.
>
> Replace parts as needed. [[10-020-012 — Engine Brake Solenoid Valve|Refer to Procedure 020-012 (Engine Brake Solenoid Valve).]] Refer to Procedure 020-017 (Engine Brake Control Valve). Refer to Procedure 020-019 (Engine Brake Piston) in Section 20.
>
> ### Adjust
>
> All overhead adjustments **must** be made when the engine is cold (any stabilized coolant temperature at 60°C \[140°F\] or below).
>
> **CAUTION · Осторожно**
> Do not use solvent to clean the rocker cover gasket. Solvent can damage the gasket material and cause it to swell.
>
> Remove the rocker lever cover and gasket. Refer to Procedure 003-011 (Rocker Lever Cover) in Section 3.
>
> **Note · Примечание**
> Early engine vibration dampers are marked with BRAKE SET 1-6, BRAKE SET 2-5, or BRAKE SET 3-4. The engine brakes **must** be set at the appropriate mark on these engines. Newer engine vibration dampers are marked with **only** A, B, or C, and are adjusted with the valves and injector on the same cylinder.
>
> Locate the valve set marks on the outside of the vibration damper.
>
> The set marks are A, B, and C:
>
> Set to mark A to adjust cylinder 1 or 6.
>
> Set to mark B to adjust cylinder 2 or 5.
>
> Set to mark C to adjust cylinder 3 or 4.
>
> **Note · Примечание**
> Two complete revolutions are required to set all valves, engine brakes, and injectors.
>
> With Air Compressor:
>
> Remove the oil fill connector from the lower gear case cover.
>
> Insert a 3/4-inch drive ratchet and extension into the air compressor drive.
>
> Rotate the air compressor drive **clockwise**, as viewed from the front of the engine.
>
> **WARNING · Опасно**
> Do not pull or pry on the fan to manually rotate the engine. To do so can damage the fan blades. Damaged fan blades can cause premature fan failures which can result in serious personal injury or property damage.
>
> The crankshaft rotation is **clockwise**, as viewed from the front of the engine.
>
> The cylinders are numbered from the front of the engine (1-2-3-4-5-6).
>
> The engine firing order is 1-5-3-6-2-4.
>
> Without Air Compressor:
>
> Loosen the capscrews and rotate the cover or remove the oil fill tube, if equipped.
>
> Use a 1 1/2-inch socket, push the barring gear into the gear mesh and bar engine over **counterclockwise**.
>
> **Note · Примечание**
> Rock the barring device back and forth until it disengages.
>
> Each cylinder has four rocker levers:
>
> - The exhaust valve rocker lever (1)
> - The injector rocker lever (2)
> - The intake valve rocker lever (3)
> - The engine brake rocker lever (4).
>
> **Note · Примечание**
> The intake valve rocker lever is **always** the long lever on the valve rocker lever shaft.
>
> **Note · Примечание**
> Early engine vibration dampers are marked with BRAKE SET 1-6, BRAKE SET 2-5, or BRAKE SET 3-4. The engine brakes **must** be set at the appropriate mark on these engines. Newer engine vibration dampers are marked with **only** A, B, or C, and are adjusted with the valves and injector on the same cylinder.
>
> The valves, brakes, and the injectors on the same cylinder are adjusted at the same index mark on the vibration damper.
>
> | Signature, ISX and QSX15 |  |  |
> |---|---|---|
> | Brake Adjustment Sequence |  |  |
> | Bar Engine in Direction of Rotation | Pulley Position | Brake |
> | Start | A | 1 |
> | Advance to | B | 5 |
> | Advance to | C | 3 |
> | Advance to | A | 6 |
> | Advance to | B | 2 |
> | Advance to | C | 4 |
> | Firing Order: 1-5-3-6-2-4 |  |  |
>
> Rotate the compressor drive or barring device in the direction of engine rotation, **clockwise**. Align the A mark on the vibration damper with the pointer on the gear cover.
>
> **Note · Примечание**
> For illustrative purposes, position A is shown as the first step. It is **not** necessary to start with position A, as long as the proper sequence is followed.
>
> Check the valve rocker levers on the given cylinder to see if both intake and exhaust valves are closed.
>
> **Note · Примечание**
> Both sets of valves are closed when the rocker levers and the brake lever are loose. If both sets of valves are **not** closed, rotate the compressor drive gear one complete revolution, and align the A mark on the front damper with the pointer again.
>
> **CAUTION · Осторожно**
> To get maximum brake operating efficiency and to prevent engine damage, the brake adjustment instructions must be followed.
>
> For older engines, locate the engine brake set marks on the outside of the vibration damper.
>
> The set marks are BRAKE SET 1-6, and BRAKE SET 2-5, and BRAKE SET 3-4.
>
> **BRAKE SET 1-6:** Cylinder 1 or 6 adjust
>
> **BRAKE SET 2-5:** Cylinder 2 or 5 adjust
>
> **BRAKE SET 3-4:** Cylinder 3 or 4 adjust
>
> Rotate the compressor drive or barring device in the direction of engine rotation, **clockwise**. Align the A mark on the vibration damper with the pointer on the gear cover.
>
> **Note · Примечание**
> For illustrative purposes, position A is shown as the first step. It is **not** necessary to start with position A, as long as the proper sequence is followed.
>
> Check the valve rocker levers on the given cylinder to see if both intake and exhaust valves are closed.
>
> **Note · Примечание**
> Both sets of valves are closed when the rocker levers and the brake lever are loose. If both sets of valves are **not** closed, rotate the compressor drive gear one complete revolution, and align the A mark on the front damper with the pointer again.
>
> Press the engine brake lever down to verify that the camshaft follower is in contact with the camshaft.
>
> Loosen the locknut on the brake lever adjusting screw, and back out the adjusting screw one turn.
>
> Insert the feeler gauge, Part Number 3163530, between the bottom of the engine brake piston and the top of exhaust valve pin on the exhaust valve crosshead.
>
> | mm |  | in |
> |---|---|---|
> | 7.00 | NOM | 0.276 |
>
> Tighten the adjusting screw until drag on the feeler gauge is felt. Proper drag means that there is no motion of the brake lever camshaft follower against the cam lobe.
>
> Hold the engine brake lever adjusting screw, and tighten the locknut.
>
> **Момент затяжки · Torque Value**
> 20 n•m [177 in-lb]
>
> Remove the feeler gauge.
>
> **CAUTION · Осторожно**
> Engine damage can occur if running clearance is not within specifications.
>
> Check the running clearance:
>
> 1. Rotate the engine brake rocker lever to the detent (neutral) position.
> 2. Check the clearance (1) between the engine brake lever actuator piston and the crosshead guide pin.
>
> | mm |  | in |
> |---|---|---|
> | 0.635 | MIN | 0.025 |
> | 2.790 | MAX | 0.110 |
>
> If the running clearance does **not** fall in the given specifications, loosen the rocker lever shaft and rotate the rocker lever shaft, slightly, in the direction required to bring the running clearance within specifications.
>
> Recheck the brake running clearance.
>
> **Note · Примечание**
> The rocker lever shafts **must** be adjusted so that all three engine brake levers fall within the given running clearance specification.
>
> Repeat the process to adjust all engine brakes according to the chart shown earlier in this procedure.
>
> Install the rocker lever cover and gasket. Refer to Procedure 003-011 (Rocker Lever Cover) in Section 3.
>
> If failure resulted in coolant, oil, excessive fuel or excessive black smoke entering the exhaust system, the aftertreatment system **must** be inspected. [[101-014-013-tr — Aftertreatment Testing|Refer to Procedure 014-013 (Aftertreatment Testing) in Section 14.]]
