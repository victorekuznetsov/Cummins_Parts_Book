---
aliases:
  - "Цепь датчика положения педали или рычага подачи"
type: "Процедура"
doc: "87-019-086"
title_en: "Accelerator Pedal or Lever Position Sensor Circuit"
title_ru: "Цепь датчика положения педали или рычага подачи"
modified: "2018-08-09"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 20
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-086.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-019-086.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Accelerator Pedal or Lever Position Sensor Circuit
**Цепь датчика положения педали или рычага подачи**

> [!abstract] Процедура · `87-019-086`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2018-08-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-086.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-019-086.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Первичная проверка

> [!warning] ОСТОРОЖНО
> Не используйте щупы или испытательные щупы, кроме Части № 3822758. Разъём будет повреждён. Лиды должны плотно помещаться в разъеме без расширения штифтов в разъеме.

Если INSITETM доступен, контролируйте схему датчика положения ускорителя для правильной работы. Если **не**, следуйте процедурам устранения неполадок в этом разделе.

![[19900524.png]]

### Проверка сопротивления

> [!warning] ОСТОРОЖНО
> Не используйте щупы или испытательные щупы, кроме Части № 3822758. Разъём будет повреждён. Лиды должны плотно помещаться в разъеме без расширения штифтов в разъеме.

Отсоедините разъем OEM-интерфейса от ECM. Убедитесь, что датчик подключен к OEM-проводах.

Вставьте один из выводов в контакт 29 (+5-VDC питания) интерфейса OEM-проводов жгута разъема. Вставьте другой испытательный щуп в контакт 19 (возврат) разъема.

![[19900638.png]]

Подключите зажимы аллигатора к мультиметровым проводам. Измерьте сопротивление. Мультиметр ** должен ** показывать от 2000 до 3000 Ом, когда педаль акселератора находится вверх или вниз. Если сопротивление ** не** в пределах спецификации, то в проводе OEM-интерфейса, при условии, что датчик положения ускорителя был предварительно проверен, возникает проблема с проводом 19 или проводом 29. Ремонт OEM интерфейса проводов жгута.[[99-019-199 — Connector, Butt Splice|Процедура 019-199]]. Ремонт проводной упряжки OEM в соответствии с инструкциями производителя транспортного средства.

![[19900639.png]]

Удалите свинец из контакта 19 (возврат) разъёма проводов OEM-интерфейса и вставьте его в контакт 30 (сигнал) разъёма.

Убедитесь, что педаль стопы находится в освобожденном (пустом) положении.

Измерьте сопротивление. Мультиметр ** должен ** показывать от 1500 до 3000 Ом.

![[19a00717.png]]

Ударьте педалью стопы (полное топливо) и снова измерьте сопротивление. Мультиметр ** должен ** показывать от 200 до 1500 Ом. Это значение сопротивления ** должно быть по меньшей мере на 1000 Ом ниже значения сопротивления положения, высвобожденного дроссельной заслонки (низкое холостое), измеренного в вышеприведенной проверке. Если значения сопротивления ** не** в пределах спецификации, существует проблема с проводом 29 (+5-VDC питания) или проводом 30 (сигнал) в электропроводке OEM. Ремонт OEM интерфейса проводов жгута. Если значения сопротивления в двух предыдущих проверках находятся в пределах спецификации, провода 19, 29 и 30 ** должны быть проверены на короткое замыкание на землю, короткое замыкание от штифта до штифта и короткое замыкание до подачи батареи.

> [!note] Примечание
> При проверке проводной упряжки OEM изучите разъем переборки и другие разъемы в цепи на предмет коррозии или повреждения клемм проводов датчика положения ускорителя.

![[19900641.png]]

### Проверка на замыкание на массу

> [!warning] ОСТОРОЖНО
> Не используйте щупы или испытательные щупы, кроме Части № 3822758. Разъём будет повреждён. Лиды должны плотно помещаться в разъеме без расширения штифтов разъема.

Отсоедините разъем OEM-интерфейса от ECM. Отсоедините датчик положения ускорителя от электропроводки OEM у педалей стопы.

![[tl8swkb.png]]

Вставьте испытательный щуп в контакт 29 (+5-VDC питания) разъёма OEM интерфейса проводов жгута. Подключите аллигаторный клип к многометровому положительному (+) щупу. Прикоснитесь к многометровому отрицательному (-) щупу блока двигателя и измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

![[19900642.png]]

Удалите свинец из контакта 29 интерфейса OEM проводов жгута разъема и вставьте его в контакт 19 (возврат) разъема. Прикоснитесь к многометровому отрицательному (-) щупу блока двигателя и измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

![[19900643.png]]

Удалите свинец из контакта 19 интерфейса OEM проводов жгута разъема и вставьте его в контакт 30 (сигнал) разъема. Прикоснитесь к многометровому отрицательному (-) щупу блока двигателя и измерьте сопротивление. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если ** любой из этих трех измерений сопротивления ** не открыт, между проводом, подключенным к контакту 29, 19 или 30, есть короткое замыкание на землю. Ремонт OEM интерфейса проводов жгута.[[87-019-250 — Connector, 50-Pin|См. процедуру 019-250]]. Ремонт проводной упряжки OEM в соответствии с инструкциями производителя транспортного средства.

Подключите датчик положения ускорителя после завершения ремонта.

![[19900644.png]]

### Проверьте короткое замыкание от контакта к контакту

> [!warning] ОСТОРОЖНО
> Не используйте щупы или испытательные щупы, кроме Части № 3822758. Разъём будет повреждён. Лиды должны плотно помещаться в разъеме без расширения штифтов разъема.

Отсоедините датчик положения ускорителя от электропроводки OEM у педалей стопы. Отсоедините разъем жгута проводов двигателя и разъем жгута OEM-интерфейса от ECM.

![[tl8swkb.png]]

Вставьте испытательный щуп в контакт 29 (+5-VDC питания) разъёма OEM интерфейса проводов жгута. Вставьте другой свинец в контакт 1 разъёма. Подключите клипсы к многометровым зондам и измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

![[19900645.png]]

Удалите свинец из контакта 1 и протестируйте все другие штифты разъема.

Затем повторите проверку контакта с контактом от контакта 29 интерфейса OEM-проводов жгута проводов разъёма ко всем штифтам разъема жгута проводов двигателя.

Мультиметр ** должен** показывать открытую схему (100к Ом или более) на всех штифтах.

Если мультиметр показывает замкнутую цепь на любом штифте, между проводом 29 и любым другим проводом, который измерял замкнутую цепь, есть короткое замыкание. Ремонт OEM интерфейса проводов жгута.[[87-019-250 — Connector, 50-Pin|См. процедуру 019-250]]. Ремонт проводной упряжки OEM в соответствии с инструкциями производителя транспортного средства.

![[19a00718.png]]

Удалите свинец из контакта 29 интерфейса OEM-проводов ремня разъема и вставьте его в контакт 19 (возврат). Вставьте другой свинец в контакт 1 и измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

![[19900647.png]]

Удалите свинец из контакта 1 и протестируйте все другие штифты разъема.

Затем повторите проверку контакта с контактом от контакта 19 интерфейса OEM-проводов разъёма жгута проводов ко всем штифтам разъема ремня электропроводки двигателя.

Мультиметр ** должен** показывать открытую схему (100к Ом или более) на всех штифтах.

Если мультиметр показывает замкнутую цепь на любом штифте, между проводом 19 и любым другим проводом есть короткое замыкание, которое измеряет замкнутую цепь. Ремонт OEM интерфейса проводов жгута.[[87-019-250 — Connector, 50-Pin|См. процедуру 019-250]]. Ремонт проводной упряжки OEM в соответствии с инструкциями производителя транспортного средства.

![[19a00719.png]]

Удалите свинец из контакта 19 интерфейса OEM-проводов и вставьте его в контакт 30 (сигнал). Вставьте другой свинец в контакт 1 и измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

![[19900649.png]]

Удалите свинец из контакта 1 и протестируйте все другие штифты разъема.

Затем повторите проверку контакта с контактом от контакта 30 разъёма OEM-интерфейса проводов жгута проводов ко всем штифтам разъема ремня электропроводки двигателя.

Мультиметр ** должен** показывать открытую схему (100к Ом или более) на всех штифтах.

Если мультиметр показывает замкнутую цепь на любом штифте, между проводом 30 и любым другим проводом есть короткое замыкание, которое измеряет замкнутую цепь. Ремонт OEM интерфейса проводов жгута.[[87-019-250 — Connector, 50-Pin|См. процедуру 019-250]]. Ремонт проводной упряжки OEM в соответствии с инструкциями производителя транспортного средства.

Подключите датчик положения ускорителя после завершения ремонта.

![[19a00720.png]]

### Проверьте короткое замыкание на источнике внешнего напряжения

> [!warning] ОСТОРОЖНО
> Не используйте щупы или испытательные щупы, кроме Части № 3822758. Разъём будет повреждён. Лиды должны плотно помещаться в разъеме без расширения штифтов разъема.

> [!note] Примечание
> Внешний источник напряжения - это ** любой ** провод в электропроводке, который несет напряжение.

Отсоедините разъем OEM-интерфейса от ECM. Отсоедините датчик положения ускорителя от электропроводки OEM у педалей стопы.

![[tl8swkb.png]]

Переключатель зажигания транспортного средства в положение Включения. Поверните многометровый циферблат для измерения VDC. Вставьте один из выводов в контакт 29 (+5-VDC питания) интерфейса OEM-проводов жгута разъема. Подключите клип к многометровому положительному (+) щупу. Прикоснитесь к многометровому отрицательному (-) щупу к блоку двигателя и измерьте напряжение.

Напряжение ** должно быть 1.5 VDC или меньше.

![[19900651.png]]

Удалите свинец из контакта 29 интерфейса OEM проводов жгута разъема и вставьте его в контакт 19 (возврат) разъема. Прикоснитесь к многометровому отрицательному (-) щупу к блоку двигателя и измерьте напряжение.

Напряжение ** должно быть 1.5 VDC или меньше.

![[19900652.png]]

Удалите свинец из контакта 19 интерфейса OEM проводов жгута разъема и вставьте его в контакт 30 (сигнал) разъема. Прикоснитесь к многометровому отрицательному (-) щупу к блоку двигателя и измерьте напряжение.

Напряжение ** должно быть 1.5 VDC или меньше.

Если на любом штифте измеряется более 1,5 VDC, то происходит короткое замыкание от провода 19, 29 или 30 до провода, несущего мощность. Ремонт OEM интерфейса проводов жгута.[[87-019-250 — Connector, 50-Pin|См. процедуру 019-250]]. Ремонт проводной упряжки OEM в соответствии с инструкциями производителя транспортного средства. Подключите датчик положения ускорителя после завершения ремонта.

![[19900653.png]]


> [!quote]- Original (English) · английский оригинал
> ### Initial Check
>
> **CAUTION · Осторожно**
> Do not use probes or test leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins in the connector.
>
> If INSITE™ is available, monitor the accelerator position sensor circuit for proper operation. If **not**, follow the troubleshooting procedures in this section.
>
> ### Resistance Check
>
> **CAUTION · Осторожно**
> Do not use probes or test leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins in the connector.
>
> Disconnect the OEM interface harness connector from the ECM. Make sure the sensor is connected to the OEM harness.
>
> Insert one of the leads into pin 29 (+5-VDC supply) of the OEM interface harness connector. Insert the other test lead into pin 19 (return) of the connector.
>
> Connect the alligator clips to the multimeter leads. Measure the resistance. The multimeter **must** show 2000 to 3000 ohms when the accelerator pedal is up or down. If the resistance is **not** within the specification, there is a problem with wire 19 or wire 29 in the OEM interface harness, provided the accelerator position sensor has been previously checked. Repair the OEM interface harness. [[99-019-199 — Connector, Butt Splice|Refer to Procedure 019-199]]. Repair the OEM harness according to the vehicle manufacturer's instructions.
>
> Remove the lead from pin 19 (return) of the OEM interface harness connector and insert it into pin 30 (signal) of the connector.
>
> Make sure the foot pedal is in the released (idle) position.
>
> Measure the resistance. The multimeter **must** show 1500 to 3000 ohms.
>
> Depress the foot pedal (full fuel) and measure the resistance again. The multimeter **must** show 200 to 1500 ohms. This resistance value **must** be at least 1000 ohms lower than the resistance value of the throttle-released (low-idle) position, measured in the above check. If the resistance values are **not** within the specification, there is a problem with wire 29 (+5-VDC supply) or wire 30 (signal) in the OEM harness. Repair the OEM interface harness. If the resistance values in the two previous checks are within the specification, wires 19, 29, and 30 **must** still be checked for a short circuit to ground, a short circuit from pin to pin, and a short circuit to battery supply.
>
> **Note · Примечание**
> When checking the OEM harness, examine the bulkhead connector and other connectors in the circuit for corrosion or damage to the accelerator position sensor wire terminals.
>
> ### Check for Short Circuit to Ground
>
> **CAUTION · Осторожно**
> Do not use probes or test leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins of the connector.
>
> Disconnect the OEM interface harness connector from the ECM. Disconnect the accelerator position sensor from the OEM harness at the foot pedal assembly.
>
> Insert the test lead into pin 29 (+5-VDC supply) of the OEM interface harness connector. Connect the alligator clip to the multimeter positive (+) probe. Touch the multimeter negative (-) probe to the engine block and measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> Remove the lead from pin 29 of the OEM interface harness connector and insert it into pin 19 (return) of the connector. Touch the multimeter negative (-) probe to the engine block and measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> Remove the lead from pin 19 of the OEM interface harness connector and insert it into pin 30 (signal) of the connector. Touch the multimeter negative (-) probe to the engine block and measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).
>
> If **any** of these three resistance measurements are **not** open, there is a short circuit to ground between the wire connected to pin 29, 19, or 30. Repair the OEM interface harness. [[87-019-250 — Connector, 50-Pin|Refer to Procedure 019-250]]. Repair the OEM harness according to the vehicle manufacturer's instructions.
>
> Connect the accelerator position sensor after completing the repair.
>
> ### Check for Short Circuit from Pin-to-Pin
>
> **CAUTION · Осторожно**
> Do not use probes or test leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins of the connector.
>
> Disconnect the accelerator position sensor from the OEM harness at the foot pedal assembly. Disconnect the engine harness connector and OEM interface harness connector from the ECM.
>
> Insert the test lead into pin 29 (+5-VDC supply) of the OEM interface harness connector. Insert the other lead into pin 1 of the connector. Connect the clips to the multimeter probes and measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> Remove the lead from pin 1 and test all other pins of the connector.
>
> Then, repeat the pin-to-pin check from pin 29 of the OEM interface harness connector to all pins of the engine harness connector.
>
> The multimeter **must** show an open circuit (100k ohms or more) at all pins.
>
> If the multimeter shows a closed circuit at any pin, there is a short circuit between wire 29 and any other wire that measured a closed circuit. Repair the OEM interface harness. [[87-019-250 — Connector, 50-Pin|Refer to Procedure 019-250]]. Repair the OEM harness according to the vehicle manufacturer's instructions.
>
> Remove the lead from pin 29 of the OEM interface harness connector and insert it into pin 19 (return). Insert the other lead into pin 1 and measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> Remove the lead from pin 1 and test all other pins of the connector.
>
> Then, repeat the pin-to-pin check from pin 19 of the OEM interface harness connector to all pins of the engine harness connector.
>
> The multimeter **must** show an open circuit (100k ohms or more) at all pins.
>
> If the multimeter shows a closed circuit at any pin, there is a short circuit between wire 19 and any other wire that measured a closed circuit. Repair the OEM interface harness. [[87-019-250 — Connector, 50-Pin|Refer to Procedure 019-250]]. Repair the OEM harness according to the vehicle manufacturer's instructions.
>
> Remove the lead from pin 19 of the OEM interface harness connector and insert it into pin 30 (signal). Insert the other lead into pin 1 and measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> Remove the lead from pin 1 and test all other pins of the connector.
>
> Then, repeat the pin-to-pin check from pin 30 of the OEM interface harness connector to all pins of the engine harness connector.
>
> The multimeter **must** show an open circuit (100k ohms or more) at all pins.
>
> If the multimeter shows a closed circuit at any pin, there is a short circuit between wire 30 and any other wire that measured a closed circuit. Repair the OEM interface harness. [[87-019-250 — Connector, 50-Pin|Refer to Procedure 019-250]]. Repair the OEM harness according to the vehicle manufacturer's instructions.
>
> Connect the accelerator position sensor after completing the repair.
>
> ### Check for Short Circuit to External Voltage Source
>
> **CAUTION · Осторожно**
> Do not use probes or test leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins of the connector.
>
> **Note · Примечание**
> An external voltage source is **any** wire in the harness that carries voltage.
>
> Disconnect the OEM interface harness connector from the ECM. Disconnect the accelerator position sensor from the OEM harness at the foot pedal assembly.
>
> Turn the vehicle keyswitch to the ON position. Turn the multimeter dial to measure VDC. Insert one of the leads into pin 29 (+5-VDC supply) of the OEM interface harness connector. Connect the clip to the multimeter positive (+) probe. Touch the multimeter negative (-) probe to the engine block and measure the voltage.
>
> The voltage **must** be 1.5 VDC or less.
>
> Remove the lead from pin 29 of the OEM interface harness connector and insert it into pin 19 (return) of the connector. Touch the multimeter negative (-) probe to the engine block and measure the voltage.
>
> The voltage **must** be 1.5 VDC or less.
>
> Remove the lead from pin 19 of the OEM interface harness connector and insert it into pin 30 (signal) of the connector. Touch the multimeter negative (-) probe to the engine block and measure the voltage.
>
> The voltage **must** be 1.5 VDC or less.
>
> If more than 1.5 VDC is measured at any pin, there is a short circuit from wire 19, 29, or 30 to a wire carrying power. Repair the OEM interface harness. [[87-019-250 — Connector, 50-Pin|Refer to Procedure 019-250]]. Repair the OEM harness according to the vehicle manufacturer's instructions. Connect the accelerator position sensor after completing the repair.
