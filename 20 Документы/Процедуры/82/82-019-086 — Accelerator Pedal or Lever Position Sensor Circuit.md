---
aliases:
  - "Цепь датчика положения педали или рычага подачи"
type: "Процедура"
doc: "82-019-086"
title_en: "Accelerator Pedal or Lever Position Sensor Circuit"
title_ru: "Цепь датчика положения педали или рычага подачи"
modified: "2002-06-03"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 21
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-086.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-086.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Accelerator Pedal or Lever Position Sensor Circuit
**Цепь датчика положения педали или рычага подачи**

> [!abstract] Процедура · `82-019-086`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2002-06-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-086.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-086.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Первичная проверка

> [!warning] ОСТОРОЖНО
> Не используйте ни пробы, ни зацепки, кроме Части Нет. 3822758. Разъем OEM будет поврежден. Лиды должны плотно помещаться в разъеме без расширения контактов разъема.

Если INSITETM доступен, контролируйте схему датчика положения ускорителя для правильной работы. Если **не**, следуйте процедурам устранения неполадок в этом разделе. Отсоедините разъём OEM-проводов от ECM. Убедитесь, что датчик положения ускорителя подключен к OEM-проводах.

![[19c00691.png]]

### Проверка сопротивления

Включить испытательный щуп в контакт 48 (положение ускорителя (+) 5-VDC питания) разъёма проводов OEM-приемника. Вставьте другой свинец в контакт 49 (возврат) разъема.

Подключите испытательный щуп к многометровым зондам. При подавлении педали акселератора измеряйте сопротивление. Мультиметр **должен **показывать от 2000 до 3000 Ом, когда педаль акселератора находится вниз (или вверх). Если сопротивление **не** в пределах спецификации, то в электропроводке OEM-приемника возникает проблема с проводом 48 или проводом 49 при условии, что датчик положения ускорителя был предварительно проверен. Ремонт проводной упряжки OEM в соответствии с процедурами производителя.

![[19200229.png]]

Повторите проверку педалью акселератора в освобожденном положении. Измерьте сопротивление. Мультиметр **должен **показывать от 2000 до 3000 Ом, когда педаль акселератора находится вверх (или вниз). Если сопротивление **не** в пределах спецификации, то в электропроводке OEM-приемника возникает проблема с проводом 48 или проводом 49 при условии, что датчик положения ускорителя был предварительно проверен.

Ремонт проводной упряжки OEM в соответствии с процедурами производителя.

![[19200230.png]]

Удалите пробный щуп из контакта 49 (возвращение положения ускорителя) и вставьте его в контакт 47 (сигнал положения ускорителя).

Убедитесь, что педаль стопы находится в освобожденном (пустом) положении.

Измерьте сопротивление. Мультиметр **должен **показывать от 1500 до 3000 Ом.

![[19c00889.png]]

Ударьте педалью стопы (полностью заправляемой) и снова измерьте сопротивление.

Мультиметр **должен **показывать от 200 до 1500 Ом. Это значение сопротивления **должно быть по меньшей мере на 1000 Ом ниже значения сопротивления 1500-3000 Ом, измеренного в вышеупомянутой проверке. Если значения сопротивления **не в пределах спецификации, то в проводе OEM-проводов возникает проблема с проводом 48 (положение ускорителя (+) 5-VDC питания) или проводом 47 (сигнал положения ускорителя).

![[19200232.png]]

Ремонт проводной упряжки OEM в соответствии с процедурами производителя. Если значения сопротивления в двух предыдущих проверках находятся в пределах спецификации, провод 48, 49 и 47 должен быть все еще проверен на короткое замыкание на землю, короткое замыкание от штифта до штифта и короткое замыкание до подачи батареи.

> [!note] Примечание
> При проверке проводной упряжки OEM проверьте разъем переборки и другие разъемы в цепи на предмет коррозии или повреждения клемм проводов датчика положения ускорителя.

![[19200232.png]]

### Проверка на замыкание на массу

Отсоедините датчик положения ускорителя от электропроводки OEM у педалей стопы.

![[tl8swkb.png]]

Вставьте измерительный щуп в контакт 48 (+5-VDC питания) разъёма проводов OEM-приемника и соедините его с многометровым (+) положительным щупом. Прикоснитесь к блоку двигателя многометровым (-) отрицательным щупом и измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

![[19200233.png]]

Удалите свинец из контакта 48 и вставьте его в контакт 49 (возвратный грунт). Прикоснитесь к многометровому (-) отрицательному щупу к заземлению блока двигателя и измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

![[19200234.png]]

Удалите свинец из контакта 49 и вставьте его в контакт 47 (возврат сигнала). Прикоснитесь к многометровому (-) отрицательному щупу к заземлению блока двигателя и измерьте сопротивление. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если **любой из этих трех измерений сопротивления **не открыт, между проводами, подключенными к контактам 48, 49 и/или 47, есть короткое замыкание на землю. Ремонт проводной упряжки OEM в соответствии с процедурами производителя транспортного средства.

![[19200235.png]]

### Проверка на замыкание между контактами

Отсоедините датчик положения ускорителя от электропроводки OEM у педалей стопы.

![[tl8swkb.png]]

Включить испытательный щуп в контакт 48 (+5-VDC питания) разъёма проводов OEM-привязи. Вставьте другой свинец в контакт 6 разъема. Подключите провода к многометровым зондам и измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

![[19200236.png]]

Проверьте все булавки. Удалите свинец из контакта 6 и измерьте сопротивление от контакта 48 ко всем другим штифтам в разъеме, по одному за раз.

Мультиметр **должен** показывать открытую схему (100к Ом или более) на всех штифтах.

Если мультиметр показывает замкнутую цепь на любом штифте, между проводом № есть короткое замыкание. 48 и любой другой провод, измеряющий замкнутую цепь.

Ремонт проводной упряжки OEM в соответствии с процедурами производителя транспортного средства.

![[19200237.png]]

Удалите свинец из контакта 48 и вставьте его в контакт 49 (возвратный грунт). Вставьте другой свинец в контакт 6 и измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

![[19200238.png]]

Удалите свинец из контакта 6 и проверьте все контакты. Измерьте сопротивление от контакта 49 до всех других контактов в разъеме, по одному за раз.

Мультиметр **должен** показывать открытую схему (100к Ом или более) на всех штифтах.

![[19200239.png]]

Удалите свинец из контакта 49 и вставьте его в контакт 47 (возврат сигнала). Вставьте другой свинец в контакт 1 и измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

![[19200240.png]]

Удалите свинец из контакта 1 и проверьте все контакты.

Мультиметр **должен** показывать открытую схему (100к Ом или более) во всех штифтах.

Если мультиметр показал замкнутую цепь на любом штифте, то между проводом № есть короткое замыкание. 47 и любой другой провод, измеряющий замкнутую цепь. Ремонт проводной упряжки OEM в соответствии с процедурами производителя транспортного средства.

![[19200241.png]]

### Проверьте короткое замыкание на источнике внешнего напряжения

Отсоедините датчик положения ускорителя от электропроводки OEM у педалей стопы.

![[tl8swkb.png]]

Переключатель зажигания транспортного средства в положение Включения. Установите мультиметр для измерения VDC. Включить испытательный щуп в контакт 48 (+5-VDC). Подключите его к многометровому (+) положительному щупу. Прикоснитесь к многометровому (−) отрицательному щупу к заземлению блока двигателя и измерьте напряжение.

Напряжение должно быть 1.5 VDC или меньше.

![[19200242.png]]

Удалите свинец из контакта 48 и вставьте его в контакт 49 (возвратный грунт). Прикоснитесь к многометровому (−) отрицательному щупу к заземлению блока двигателя и измерьте напряжение.

Напряжение должно быть 1.5 VDC или меньше.

![[19200243.png]]

Удалите свинец из контакта 49 и вставьте его в контакт 47 (возврат сигнала). Прикоснитесь к многометровому (−) отрицательному щупу к заземлению блока двигателя и измерьте напряжение.

Напряжение должно быть 1.5 VDC или меньше.

Если на любом штифте измеряется более 1,5 VDC, то происходит короткое замыкание от провода No. 48, 49 или 47 на внешний источник напряжения. Ремонт проводной упряжки OEM в соответствии с процедурами производителя транспортного средства.

> [!note] Примечание
> Внешний источник напряжения - это любой провод в OEM-проводах, который несет напряжение.

После ремонта подсоедините все компоненты.

![[19200244.png]]


> [!quote]- Original (English) · английский оригинал
> ### Initial Check
>
> **CAUTION · Осторожно**
> Do not use probes or leads other than Part No. 3822758. The OEM connector will be damaged. The leads must fit tightly in the connector without expanding the connector pins.
>
> If INSITE™ is available, monitor the accelerator position sensor circuit for proper operation. If **not**, follow the troubleshooting procedures in this section. Disconnect the OEM harness connector from the ECM. Make sure the accelerator position sensor is connected to the OEM harness.
>
> ### Resistance Check
>
> Insert a test lead into pin 48 (accelerator position (+) 5-VDC supply) of the OEM harness connector. Insert the other lead into pin 49 (return) of the connector.
>
> Connect the test leads to the multimeter probes. With the accelerator pedal depressed, measure the resistance. The multimeter **must** show 2000 to 3000 ohms when the accelerator pedal is down (or up). If the resistance is **not** within the specification, there is a problem with wire 48 or wire 49 in the OEM harness, provided the accelerator position sensor has been previously checked. Repair the OEM harness according to the manufacturer's procedures.
>
> Repeat the check with the accelerator pedal in the released position. Measure the resistance. The multimeter **must** show 2000 to 3000 ohms when the accelerator pedal is up (or down). If the resistance is **not** within the specification, there is a problem with wire 48 or wire 49 in the OEM harness, provided the accelerator position sensor has been previously checked.
>
> Repair the OEM harness according to the manufacturer's procedures.
>
> Remove the test lead from pin 49 (accelerator position return) and insert it into pin 47 (accelerator position signal).
>
> Make sure the foot pedal is in the released (idle) position.
>
> Measure the resistance. The multimeter **must** show 1500 to 3000 ohms.
>
> Depress the foot pedal (full-fuel) and measure the resistance again.
>
> The multimeter **must** show 200 to 1500 ohms. This resistance value **must** be at least 1000 ohms lower than the resistance value of 1500 to 3000 ohms measured in the above check. If the resistance values are **not** within the specification, there is a problem with wire 48 (accelerator position (+) 5-VDC supply) or wire 47 (accelerator position signal) in the OEM harness.
>
> Repair the OEM harness according to the manufacturer's procedures. If the resistance values in the two previous checks are within the specification, wire 48, 49, and 47 **must** still be checked for a short circuit to ground, a short circuit from pin to pin, and a short circuit to battery supply.
>
> **Note · Примечание**
> When checking the OEM harness, inspect the bulkhead connector and other connectors in the circuit for corrosion or damage to the accelerator position sensor wire terminals.
>
> ### Check for Short Circuit to Ground
>
> Disconnect the accelerator position sensor from the OEM harness at the foot pedal assembly.
>
> Insert a test lead into pin 48 (+5-VDC supply) of the OEM harness connector, and connect it to the multimeter (+) positive probe. Touch the multimeter (-) negative probe to the engine block and measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> Remove the lead from pin 48 and insert it into pin 49 (return ground). Touch the multimeter (-) negative probe to the engine block ground and measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> Remove the lead from pin 49 and insert it into pin 47 (signal return). Touch the multimeter (-) negative probe to the engine block ground and measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).
>
> If **any** of these three resistance measurements are **not** open, there is a short circuit to ground between the wires connected to pins 48, 49, and/or 47. Repair the OEM harness according to the vehicle manufacturer's procedures.
>
> ### Check for Short Circuit from Pin to Pin
>
> Disconnect the accelerator position sensor from the OEM harness at the foot pedal assembly.
>
> Insert a test lead into pin 48 (+5-VDC supply) of the OEM harness connector. Insert the other lead into pin 6 of the connector. Connect the leads to the multimeter probes and measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> Test all pins. Remove the lead from pin 6, and measure the resistance from pin 48 to all other pins in the connector, one at a time.
>
> The multimeter **must** show an open circuit (100k ohms or more) at all pins.
>
> If the multimeter shows a closed circuit at any pin, there is a short circuit between wire No. 48 and any other wire that measured a closed circuit.
>
> Repair the OEM harness according to the vehicle manufacturer's procedures.
>
> Remove the lead from pin 48 and insert it into pin 49 (return ground). Insert the other lead into pin 6 and measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> Remove the lead from pin 6 and test all pins. Measure the resistance from pin 49 to all other pins in the connector, one at a time.
>
> The multimeter **must** show an open circuit (100k ohms or more) at all pins.
>
> Remove the lead from pin 49 and insert it into pin 47 (signal return). Insert the other lead into pin 1 and measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> Remove the lead from pin 1 and test all pins.
>
> The multimeter **must** show an open circuit (100k ohms or more) in all pins.
>
> If the multimeter showed a closed circuit at any pin, there is a short circuit between wire No. 47 and any other wire that measured a closed circuit. Repair the OEM harness according to the vehicle manufacturer's procedures.
>
> ### Check for Short Circuit to External Voltage Source
>
> Disconnect the accelerator position sensor from the OEM harness at the foot pedal assembly.
>
> Turn the vehicle keyswitch to the ON position. Set the multimeter to measure VDC. Insert a test lead into pin 48 (+5-VDC supply). Connect it to the multimeter (+) positive probe. Touch the multimeter (−) negative probe to the engine block ground and measure the voltage.
>
> The voltage **must** be 1.5 VDC or less.
>
> Remove the lead from pin 48 and insert it into pin 49 (return ground). Touch the multimeter (−) negative probe to the engine block ground and measure the voltage.
>
> The voltage **must** be 1.5 VDC or less.
>
> Remove the lead from pin 49 and insert it into pin 47 (signal return). Touch the multimeter (−) negative probe to the engine block ground and measure the voltage.
>
> The voltage **must** be 1.5 VDC or less.
>
> If more than 1.5 VDC is measured at any pin, there is a short circuit from wire No. 48, 49, or 47 to an external voltage source. Repair the OEM harness according to the vehicle manufacturer's procedures.
>
> **Note · Примечание**
> An external voltage source is any wire in the OEM harness that carries voltage.
>
> Connect all components after completing the repair.
