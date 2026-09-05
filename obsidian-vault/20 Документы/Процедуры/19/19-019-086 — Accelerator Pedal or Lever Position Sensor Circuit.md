---
aliases:
  - "Цепь датчика положения педали или рычага подачи"
type: "Процедура"
doc: "19-019-086"
title_en: "Accelerator Pedal or Lever Position Sensor Circuit"
title_ru: "Цепь датчика положения педали или рычага подачи"
modified: "2002-08-20"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 23
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-086.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-086.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Accelerator Pedal or Lever Position Sensor Circuit
**Цепь датчика положения педали или рычага подачи**

> [!abstract] Процедура · `19-019-086`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2002-08-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-086.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-086.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Первичная проверка

> [!warning] ОСТОРОЖНО
> Чтобы уменьшить вероятность повреждения разъема, не используйте щупы или провода, отличные от Части № 3822758. Разъём будет повреждён. Лиды должны плотно помещаться в разъеме без расширения штифтов в разъеме.

Если имеется InsiteTM, часть 3824801, то для правильной работы необходимо контролировать схему датчика положения ускорителя. Если **не**, следуйте процедурам устранения неполадок в этом разделе.

![[19400357.png]]

### Проверка сопротивления

Отключите проводку OEM-интерфейса от ECM. Убедитесь, что датчик подключен к OEM-проводах.

Вставьте один из выводов в контакт 26 (+5-VDC питания) интерфейса OEM-проводов жгута разъема. Вставьте другой свинец в контакт 11 (возврат) разъема.

![[19800922.png]]

Подключите зажимы аллигатора к мультиметровым проводам. Измерьте сопротивление. Мультиметр **должен **показывать от 2000 до 3000 Ом, когда педаль акселератора находится вверх или вниз. Если сопротивление **не** в пределах спецификации, возникает проблема с проводом, подключенным к контакту 11 или контакту 26 в проводной ремне OEM-интерфейса, при условии, что датчик положения ускорителя был ранее проверен. Ремонт OEM интерфейса проводов жгута. См. процедуру 019-240. Ремонт проводной упряжки OEM в соответствии с инструкциями производителя транспортного средства.

![[19800926.png]]

Удалите штифт свинца из контакта 11 (возврат) и вставьте его в контакт 29 (сигнал) разъёма проводов OEM-интерфейса.

Убедитесь, что педаль стопы находится в освобожденном (пустом) положении.

Измеряйте сопротивление от контакта 26 до контакта 29. Мультиметр **должен **показывать от 1500 до 3000 Ом.

![[19800927.png]]

Ударьте педалью стопы (полностью заправляемой) и снова измерьте сопротивление. Мультиметр **должен **показывать от 200 до 1500 Ом. Это значение сопротивления **должно быть по меньшей мере на 1000 Ом ниже значения сопротивления 1500-3000 Ом, измеренного в вышеупомянутой проверке. Если значения сопротивления **не** в пределах спецификации, возникает проблема с проводом, подключенным к контакту 26 (+5-VDC питания) или контакту 29 (сигнал) в электропроводке OEM. Ремонт OEM интерфейса проводов жгута. Если значения сопротивления в двух предыдущих проверках находятся в пределах спецификации, контакты 11, 26 и 29 **должны быть проверены на короткое замыкание на землю, короткое замыкание от пин-кодов до пин-кодов и короткое замыкание до подачи батареи.

> [!note] Примечание
> При проверке проводной упряжки OEM изучите разъем переборки и другие разъемы в цепи на предмет коррозии или повреждения клемм проводов датчика положения ускорителя.

![[19800928.png]]

### Проверка на замыкание на массу

Отсоедините датчик положения ускорителя от электропроводки OEM у педалей стопы.

![[tl8swkb.png]]

Включить испытательный щуп в контакт 26 (+5-VDC). Подключите клип к многометровому положительному (+) щупу. Прикоснитесь к многометровому отрицательному (-) щупу блока двигателя и измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

![[19800929.png]]

Удалите свинец из контакта 26 и вставьте его в контакт 11 (возврат). Прикосновение к многометровому отрицательному (-) приводу приводит к блоку двигателя и измеряет сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

![[19800930.png]]

Удалите свинец из контакта 11 и вставьте его в контакт 29 (сигнал). Прикосновение к многометровому отрицательному (-) приводу приводит к блоку двигателя и измеряет сопротивление. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если **любой из этих трех измерений сопротивления **не открыт, между проводами, подключенными к контактам 26, 29 или 11, есть короткое замыкание на землю. Ремонт OEM интерфейса проводов жгута. См. процедуру 019-240. Ремонт проводной упряжки OEM в соответствии с инструкциями производителя транспортного средства.

![[19800931.png]]

### Проверка на замыкание между контактами

Отсоедините датчик положения ускорителя от электропроводки OEM у педалей стопы.

![[tl8swkb.png]]

Вставьте один из испытательных щупов для контакта 26 (+5-VDC питания) разъёма OEM-интерфейса проводов жгута. Вставьте другой вывод для контакта 1 разъема. Подключите клипсы к многометровым зондам и измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

![[19800932.png]]

Удалите свинец из контакта 1 и вставьте его в контакт 2, затем свяжитесь с 3, пока все штифты не будут проверены.

Мультиметр **должен** показывать открытую схему (100к Ом или более) на всех штифтах.

Если мультиметр показывает замкнутую цепь на любом штифте, между контактом 26 и любым другим штифтом, который измерял замкнутую цепь, существует короткое замыкание. Ремонт OEM интерфейса проводов жгута. См. процедуру 019-240. Ремонт проводной упряжки OEM в соответствии с инструкциями производителя транспортного средства.

![[19800933.png]]

Удалите свинец из контакта 26 и вставьте его в контакт 29 (возврат) разъёма проводов OEM-интерфейса. Вставьте другой свинец в контакт 1 и измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

![[19800934.png]]

Удалите свинец из контакта 1 и вставьте его в контакт 2, затем свяжитесь с 3, пока все штифты не будут проверены.

Мультиметр **должен** показывать открытую схему (100к Ом или более) на всех штифтах.

Если мультиметр показывает замкнутую цепь на любом штифте, между контактом 29 и любым другим штифтом, который измерял замкнутую цепь, есть короткое замыкание. Ремонт OEM интерфейса проводов жгута. См. процедуру 019-240. Ремонт проводной упряжки OEM в соответствии с инструкциями производителя транспортного средства.

![[19800935.png]]

Удалите свинец из контакта 29 и вставьте его в контакт 11 (возврат) разъёма проводов OEM-интерфейса. Вставьте другой свинец в контакт 1 и измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

![[19400485.png]]

Удалите свинец из контакта 1 и вставьте его в контакт 2, затем свяжитесь с 3, пока все штифты не будут проверены.

Мультиметр **должен** показывать открытую схему (100к Ом или более) на всех штифтах.

Если мультиметр показывает замкнутую цепь на любом штифте, между контактом 11 и любым другим штифтом, который измерял замкнутую цепь, есть короткое замыкание. Ремонт OEM интерфейса проводов жгута. См. процедуру 019-240. Ремонт проводной упряжки OEM в соответствии с инструкциями производителя транспортного средства.

![[19400486.png]]

### Проверьте короткое замыкание на источнике внешнего напряжения

Отсоедините датчик положения ускорителя от электропроводки OEM у педалей стопы.

![[tl8swkb.png]]

Переключатель зажигания транспортного средства в положение Включения. Установите мультиметр для измерения VDC. Вставьте один из выводов в контакт 26 (+5-VDC питания) интерфейса OEM-проводов жгута разъема. Подключите клип к многометровому положительному (+) щупу. Подключите многометровый отрицательный (-) щуп к блоку двигателя и измерьте напряжение.

Напряжение должно быть 1.5 VDC или меньше.

![[19800923.png]]

Удалите свинец из контакта 26 и вставьте его в контакт 11 (возврат) разъёма проводов OEM-интерфейса. Прикоснитесь к многометровому отрицательному (-) щупу к блоку двигателя и измерьте напряжение.

Напряжение должно быть 1.5 VDC или меньше.

![[19800924.png]]

Удалите свинец из контакта 11 и вставьте его в контакт 29 (сигнал) разъёма проводов OEM-интерфейса. Прикоснитесь к блоку двигателя многометровым отрицательным (+) щупом и измерьте напряжение.

Напряжение должно быть 1.5 VDC или меньше.

Если измеряется более 1,5 VDC при любой точке, то происходит короткое замыкание от контакта 26, 11 или 29 до провода, несущего мощность. Ремонт OEM интерфейса проводов жгута. См. процедуру 019-240. Ремонт проводной упряжки OEM в соответствии с инструкциями производителя транспортного средства.

> [!note] Примечание
> Источник внешнего напряжения - это **любой** провод в электропроводке, который несет напряжение.

![[19800925.png]]

Подключите зажимы аллигатора к мультиметровым проводам. Измерьте сопротивление. Мультиметр **должен **показывать от 2000 до 3000 Ом, когда педаль акселератора находится вверх или вниз. Если сопротивление **не** в пределах спецификации, то в проводах OEM-интерфейса возникает проблема с контактом 11 или 26 при условии, что датчик положения ускорителя был предварительно проверен. Ремонт OEM интерфейса проводов жгута. См. процедуру 019-240. Ремонт проводной упряжки OEM в соответствии с инструкциями производителя транспортного средства.

![[19800926.png]]

Удалите свинец из контакта 11 (возврат) и вставьте его в контакт 29 (сигнал) разъёма проводов OEM-приемника.

Убедитесь, что педаль стопы находится в освобожденном (пустом) положении.

Измерьте сопротивление от контакта 26 до контакта 29 разъёма OEM-интерфейса. Мультиметр **должен **показывать от 1500 до 3000 Ом.

![[19800927.png]]

Ударьте педалью стопы (полностью заправляемой) и снова измерьте сопротивление. Мультиметр **должен **показывать от 200 до 1500 Ом. Это значение сопротивления **должно быть по меньшей мере на 1000 Ом ниже значения сопротивления 1500-3000 Ом, измеренного в вышеупомянутой проверке. Если значения сопротивления **не** в пределах спецификации, существует проблема с контактом 26 (+5-VDC) или контактом 29 (сигнал) в электропроводке OEM. Ремонт OEM интерфейса проводов жгута. Если значения сопротивления в двух предыдущих проверках находятся в пределах спецификации, контакты 11, 26 и 29 **должны быть проверены на короткое замыкание на землю, короткое замыкание от пин-кодов до пин-кодов и короткое замыкание до подачи батареи.

> [!note] Примечание
> При проверке проводной упряжки OEM изучите разъем переборки и другие разъемы в цепи на предмет коррозии или повреждения клемм проводов датчика положения ускорителя.

![[19800928.png]]


> [!quote]- Original (English) · английский оригинал
> ### Initial Check
>
> **CAUTION · Осторожно**
> To reduce the possibility of connector damage, do not use probes or leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins in the connector.
>
> If INSITE™, Part Number 3824801, is available, monitor the accelerator position sensor circuit for proper operation. If **not**, follow the troubleshooting procedures in this section.
>
> ### Resistance Check
>
> Disconnect the OEM interface harness from the ECM. Make sure the sensor is connected to the OEM harness.
>
> Insert one of the leads into pin 26 (+5-VDC supply) of the OEM interface harness connector. Insert the other lead into pin 11 (return) of the connector.
>
> Connect the alligator clips to the multimeter leads. Measure the resistance. The multimeter **must** show 2000 to 3000 ohms when the accelerator pedal is up or down. If the resistance is **not** within the specification, there is a problem with the wire connected to pin 11 or pin 26 in the OEM interface harness, provided the accelerator position sensor has been previously checked. Repair the OEM interface harness. Refer to Procedure 019-240. Repair the OEM harness according to the vehicle manufacturer's instructions.
>
> Remove the pin of the lead from pin 11 (return) and insert it into pin 29 (signal) of the OEM interface harness connector.
>
> Make sure the foot pedal is in the released (idle) position.
>
> Measure the resistance from pin 26 to pin 29. The multimeter **must** show 1500 to 3000 ohms.
>
> Depress the foot pedal (full-fuel) and measure the resistance again. The multimeter **must** show 200 to 1500 ohms. This resistance value **must** be at least 1000 ohms lower than the resistance value of 1500 to 3000 ohms measured in the above check. If the resistance values are **not** within the specification, there is a problem with the wire connected to pin 26 (+5-VDC supply) or pin 29 (signal) in the OEM harness. Repair the OEM interface harness. If the resistance values in the two previous checks are within the specification, pins 11, 26, and 29 **must** still be checked for a short circuit to ground, a short circuit from pin to pin, and a short circuit to battery supply.
>
> **Note · Примечание**
> When checking the OEM harness, examine the bulkhead connector and other connectors in the circuit for corrosion or damage to the accelerator position sensor wire terminals.
>
> ### Check for Short Circuit to Ground
>
> Disconnect the accelerator position sensor from the OEM harness at the foot pedal assembly.
>
> Insert the test lead into pin 26 (+5-VDC supply). Connect the clip to the multimeter positive (+) probe. Touch the multimeter negative (-) probe to the engine block and measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> Remove the lead from pin 26 and insert it into pin 11 (return). Touch the multimeter negative (-) lead to the engine block and measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> Remove the lead from pin 11 and insert it into pin 29 (signal). Touch the multimeter negative (-) lead to the engine block and measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).
>
> If **any** of these three resistance measurements are **not** open, there is a short circuit to ground between the wires connected to pins 26, 29, or 11. Repair the OEM interface harness. Refer to Procedure 019-240. Repair the OEM harness according to the vehicle manufacturer's instructions.
>
> ### Check for Short Circuit from Pin to Pin
>
> Disconnect the accelerator position sensor from the OEM harness at the foot pedal assembly.
>
> Insert one of the test leads to pin 26 (+5-VDC supply) of the OEM interface harness connector. Insert the other lead to pin 1 of the connector. Connect the clips to the multimeter probes and measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> Remove the lead from pin 1 and insert it into pin 2, then pin 3, until all pins are tested.
>
> The multimeter **must** show an open circuit (100k ohms or more) at all pins.
>
> If the multimeter shows a closed circuit at any pin, there is a short circuit between pin 26 and any other pin that measured a closed circuit. Repair the OEM interface harness. Refer to Procedure 019-240. Repair the OEM harness according to the vehicle manufacturer's instructions.
>
> Remove the lead from pin 26 and insert it into pin 29 (return) of the OEM interface harness connector. Insert the other lead into pin 1 and measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> Remove the lead from pin 1 and insert it into pin 2, then pin 3, until all pins are tested.
>
> The multimeter **must** show an open circuit (100k ohms or more) at all pins.
>
> If the multimeter shows a closed circuit at any pin, there is a short circuit between pin 29 and any other pin that measured a closed circuit. Repair the OEM interface harness. Refer to Procedure 019-240. Repair the OEM harness according to the vehicle manufacturer's instructions.
>
> Remove the lead from pin 29 and insert it into pin 11 (return) of the OEM interface harness connector. Insert the other lead into pin 1 and measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> Remove the lead from pin 1 and insert it into pin 2, then pin 3, until all pins are tested.
>
> The multimeter **must** show an open circuit (100k ohms or more) at all pins.
>
> If the multimeter shows a closed circuit at any pin, there is a short circuit between pin 11 and any other pin that measured a closed circuit. Repair the OEM interface harness. Refer to Procedure 019-240. Repair the OEM harness according to the vehicle manufacturer's instructions.
>
> ### Check for Short Circuit to External Voltage Source
>
> Disconnect the accelerator position sensor from the OEM harness at the foot pedal assembly.
>
> Turn the vehicle keyswitch to the ON position. Set the multimeter to measure VDC. Insert one of the leads into pin 26 (+5-VDC supply) of the OEM interface harness connector. Connect the clip to the multimeter positive (+) probe. Connect the multimeter negative (-) probe to the engine block and measure the voltage.
>
> The voltage **must** be 1.5 VDC or less.
>
> Remove the lead from pin 26 and insert it into pin 11 (return) of the OEM interface harness connector. Touch the multimeter negative (-) probe to the engine block and measure the voltage.
>
> The voltage **must** be 1.5 VDC or less.
>
> Remove the lead from pin 11 and insert it into pin 29 (signal) of the OEM interface harness connector. Touch the multimeter negative (+) probe to the engine block and measure the voltage.
>
> The voltage **must** be 1.5 VDC or less.
>
> If more than 1.5 VDC is measured at **any** pin, there is a short circuit from pin 26, 11, or 29 to a wire carrying power. Repair the OEM interface harness. Refer to Procedure 019-240. Repair the OEM harness according to the vehicle manufacturer's instructions.
>
> **Note · Примечание**
> The external voltage source is **any** wire in the harness that carries voltage.
>
> Connect the alligator clips to the multimeter leads. Measure the resistance. The multimeter **must** show 2000 to 3000 ohms when the accelerator pedal is up or down. If the resistance is **not** within the specification, there is a problem with pin 11 or 26 in the OEM interface harness, provided the accelerator position sensor has been previously checked. Repair the OEM interface harness. Refer to Procedure 019-240. Repair the OEM harness according to the vehicle manufacturer's instructions.
>
> Remove the lead from pin 11 (return) and insert it into pin 29 (signal) of the OEM harness connector.
>
> Make sure the foot pedal is in the released (idle) position.
>
> Measure the resistance from pin 26 to pin 29 of the OEM interface harness connector. The multimeter **must** show 1500 to 3000 ohms.
>
> Depress the foot pedal (full-fuel) and measure the resistance again. The multimeter **must** show 200 to 1500 ohms. This resistance value **must** be at least 1000 ohms lower than the resistance value of 1500 to 3000 ohms measured in the above check. If the resistance values are **not** within the specification, there is a problem with pin 26 (+5-VDC supply) or pin 29 (signal) in the OEM harness. Repair the OEM interface harness. If the resistance values in the two previous checks are within the specification, pins 11, 26, and 29 **must** still be checked for a short circuit to ground, a short circuit from pin to pin, and a short circuit to battery supply.
>
> **Note · Примечание**
> When checking the OEM harness, examine the bulkhead connector and other connectors in the circuit for corrosion or damage to the accelerator position sensor wire terminals.
