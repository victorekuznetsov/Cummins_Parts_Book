---
aliases:
  - "Цепь датчика положения педали или рычага подачи"
type: "Процедура"
doc: "07-019-086"
title_en: "Accelerator Pedal or Lever Position Sensor Circuit"
title_ru: "Цепь датчика положения педали или рычага подачи"
modified: "2003-12-02"
engines:
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "4021442"
figures: 16
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-019-086.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-019-086.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
  - "перевод/машинный"
---

# Accelerator Pedal or Lever Position Sensor Circuit
**Цепь датчика положения педали или рычага подачи**

> [!abstract] Процедура · `07-019-086`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-12-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-019-086.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-019-086.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Первичная проверка

> [!warning] ОСТОРОЖНО
> Не используйте щупы или испытательные щупы, кроме Части 3822758, иначе разъем будет поврежден. Испытательный щуп должен плотно помещаться в разъеме без расширения штифтов в разъеме.

Если электронный сервисный инструмент INSITETM доступен, проверьте схему датчика положения ускорителя для правильной работы.

Если **не**, следуйте процедурам устранения неполадок в этом разделе.

![[19900524.png]]

### Проверка сопротивления

> [!warning] ОСТОРОЖНО
> Не используйте щупы или испытательные щупы, кроме Части 3822758, иначе разъем будет поврежден. Испытательный щуп должен плотно помещаться в разъеме без расширения штифтов в разъеме.

Отсоедините разъем интерфейса проводов упряжки оригинального производителя оборудования (OEM) от электронного модуля управления (ECM).

Убедитесь, что датчик подключен к OEM-проводах.

Включить один из испытательных щупов в рычаг питания ускорителя контакт подключения разъёма OEM интерфейса проводов.

Вставьте другой испытательный щуп в рычаг ускорителя обратного контакта разъема.

![[19901376.png]]

Подключите аллигаторы к многометровому испытательному щупу.

Измерьте сопротивление.

Мультиметр **должен **показывать от 2000 до 3000 Ом, когда рычаг акселератора находится в холостом или полном положении топлива.

Если сопротивление **не** в пределах спецификации, возникает проблема с возвратным проводом рычага акселератора или проводом подачи рычага акселератора в ремне проводов интерфейса OEM при условии проверки датчика положения ускорителя. Ремонт OEM интерфейса проводов жгута разъема. См. процедуру[[99-019-204 — Deutsch DRC Connector Series|019-204]].

Ремонт проводной упряжки OEM в соответствии с инструкциями производителя транспортного средства.

![[19901377.png]]

Удалите пробный щуп из рычага ускорителя обратного контакта разъёма проводов интерфейса OEM и вставьте его в контакт сигнала рычага ускорителя разъёма.

Убедитесь, что рычаг акселератора находится в положении холостого хода.

Измерьте сопротивление.

Мультиметр **должен **показывать от 1500 до 3000 Ом.

![[19901378.png]]

Переместите рычаг ускорителя в полное положение топлива и снова измерьте сопротивление.

Мультиметр **должен **показывать от 200 до 1500 Ом.

Это значение сопротивления должно быть по меньшей мере на 1000 Ом ниже значения сопротивления в положении с низким уровнем холостого хода, измеренного в вышеприведенной проверке.

Если значения сопротивления **не** в пределах спецификации, существует проблема с проводом питания рычага акселератора или сигнальным проводом рычага акселератора в электропроводке OEM. Ремонт OEM интерфейса проводов жгута.

Если значения сопротивления в двух предыдущих проверках находятся в пределах спецификации, возврат рычага акселератора, сигнал рычага акселератора и провода подачи рычага акселератора должны быть все еще проверены на короткое замыкание на землю, короткое замыкание от штифта до штифта и короткое замыкание до подачи батареи.

Исследуйте переборки разъема и других разъемов в цепи для коррозии или повреждения ускорителя положения датчика провода терминалов.

![[19901379.png]]

### Проверка на замыкание на массу

> [!warning] ОСТОРОЖНО
> Не используйте щупы или испытательные щупы, кроме Части 3822758, иначе разъем будет поврежден. Испытательный щуп должен плотно помещаться в разъеме без расширения штифтов в разъеме.

Отсоедините разъем OEM-интерфейса от ECM.

Отсоедините датчик положения ускорителя от электропроводки OEM на рычажке акселератора.

![[19901368.png]]

Включить испытательный щуп в рычаг питания ускорителя контактного соединения разъёма проводов OEM-интерфейса.

Подключите аллигаторный клип к многометровому положительному (+) щупу.

Прикоснитесь к многометровому отрицательному (-) щупу блока двигателя и измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Удалите пробный щуп из рычага акселератора, обеспечивающего контакт подключения интерфейса OEM-проводов, и вставьте его в обратный контакт акселератора разъема.

Прикоснитесь к многометровому отрицательному (-) щупу блока двигателя и измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Удалите пробный щуп из рычага ускорителя обратного контакта разъёма проводов интерфейса OEM и вставьте его в контакт сигнала ускорителя разъёма.

Прикоснитесь к многометровому отрицательному (-) щупу блока двигателя и измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если **любой из этих трех измерений сопротивления **не открыт, между проводом, подключенным к возврату рычага акселератора, сигналом рычага акселератора или контактом подачи рычага акселератора, есть короткое замыкание на землю. Ремонт OEM интерфейса проводов жгута разъема. См. процедуру[[99-019-204 — Deutsch DRC Connector Series|019-204]].

Ремонт проводной упряжки OEM в соответствии с инструкциями производителя транспортного средства.

Подключите датчик положения ускорителя после завершения ремонта.

![[19901407.png]]

### Проверка на замыкание между контактами

> [!warning] ОСТОРОЖНО
> Не используйте щупы или испытательные щупы, кроме Части 3822758, иначе разъем будет поврежден. Испытательный щуп должен плотно помещаться в разъеме без расширения штифтов в разъеме.

Отсоедините датчик положения ускорителя от электропроводки OEM на рычажке акселератора.

Отсоедините разъем жгута проводов двигателя и разъем жгута OEM-интерфейса от ECM.

![[19901368.png]]

Включить испытательный щуп в рычаг питания ускорителя контактного соединения разъёма проводов OEM-интерфейса.

Вставить другой испытательный щуп в штифт стоп-сигнала разъёма.

Подключите клипсы к многометровым зондам и измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

![[19901408.png]]

Удалите пробоотборник из стоп-сигнала лампы и проверьте все другие штифты разъема.

Повторите проверку контакта с контактом от контакта питания рычага акселератора разъёма OEM-интерфейса с ремнём проводов ко всем штифтам разъема ремня электропроводки двигателя.

Мультиметр **должен** показывать открытую схему (100к Ом или более) на всех штифтах.

Если мультиметр показывает замкнутую цепь на любом штифте, между подводящим проводом рычага ускорителя и любым другим проводом, который измерял замкнутую цепь, есть короткое замыкание. Ремонт OEM интерфейса проводов жгута разъема. См. процедуру[[99-019-204 — Deutsch DRC Connector Series|019-204]].

Ремонт проводной упряжки OEM в соответствии с инструкциями производителя транспортного средства.

![[19901415.png]]

Удалите пробный щуп из рычага акселератора, обеспечивающего контакт подключения интерфейса OEM-проводов, и вставьте его в обратный контакт рычага акселератора.

Вставьте другой испытательный щуп в штифт стоп-сигнала и измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

![[19901408.png]]

Удалите пробный щуп из стоп-сигнала лампы и проверьте все другие штифты в разъеме.

Повторите проверку контакта с контактом с рычага акселератора обратного контакта разъёма OEM-интерфейса проводов жгута проводов со всеми штифтами разъема ремня электропроводки двигателя.

Мультиметр **должен** показывать открытую схему (100к Ом или более) на всех штифтах.

Если мультиметр показывает замкнутую цепь на любом штифте, между обратным проводом рычага ускорителя и любым другим проводом, который измерял замкнутую цепь, есть короткое замыкание. Ремонт OEM интерфейса проводов жгута разъема. См. процедуру[[99-019-204 — Deutsch DRC Connector Series|019-204]].

Ремонт проводной упряжки OEM в соответствии с инструкциями производителя транспортного средства.

![[19901415.png]]

Удалите пробный щуп из рычага ускорителя обратного контакта разъёма проводов интерфейса OEM и вставьте его в контакт сигнала рычага ускорителя.

Вставьте другой испытательный щуп в штифт стоп-сигнала и измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

![[19901408.png]]

Удалите пробоотборник из стоп-сигнала лампы и проверьте все другие штифты разъема.

Повторите проверку контакта с контактом от контакта рычага акселератора с интерфейсом OEM-проводов разъема жгута ко всем штифтам разъема жгута проводов двигателя.

Мультиметр **должен** показывать открытую схему (100к Ом или более) на всех штифтах.

Если мультиметр показывает замкнутую цепь на любом штифте, между сигнальным проводом рычага ускорителя и любым другим проводом, который измерял замкнутую цепь, есть короткое замыкание. Ремонт OEM интерфейса проводов жгута разъема. См. процедуру[[99-019-204 — Deutsch DRC Connector Series|019-204]].

Ремонт проводной упряжки OEM в соответствии с инструкциями производителя транспортного средства.

![[19901415.png]]

### Проверьте короткое замыкание на источнике внешнего напряжения

> [!warning] ОСТОРОЖНО
> Не используйте щупы или испытательные щупы, кроме Части 3822758, иначе разъем будет поврежден. Испытательный щуп должен плотно помещаться в разъеме без расширения штифтов в разъеме.

Отсоедините разъем OEM-интерфейса от ECM.

Отсоедините датчик положения ускорителя от электропроводки OEM на рычажке акселератора.

![[19901368.png]]

Переключатель зажигания транспортного средства в положение Включения.

Поверните многометровый циферблат для измерения VDC.

Включить один из испытательных щупов в рычаг питания ускорителя контакт подключения разъёма OEM интерфейса проводов.

Подключите клип к многометровому положительному (+) щупу.

Прикоснитесь к многометровому отрицательному (-) щупу к блоку двигателя и измерьте напряжение.

Напряжение должно быть 1.5 VDC или меньше.

Удалите пробный щуп из рычага акселератора, обеспечивающего контакт подключения интерфейса OEM-проводов, и вставьте его в рычаг акселератора, возвращающий контакт разъема.

Прикоснитесь к многометровому отрицательному (-) щупу к блоку двигателя и измерьте напряжение.

Напряжение должно быть 1.5 VDC или меньше.

Удалите пробный щуп из рычага ускорителя обратного контакта разъёма проводов интерфейса OEM и вставьте его в контакт сигнала рычага ускорителя разъёма.

Прикоснитесь к многометровому отрицательному (-) щупу к блоку двигателя и измерьте напряжение.

Напряжение должно быть 1.5 VDC или меньше.

Если на любом штифте измеряется более 1,5 VDC, то происходит короткое замыкание от рычага акселератора, возвращающего сигнал или подающего провода к проводу, несущему мощность. Ремонт OEM интерфейса проводов жгута разъема. См. процедуру[[99-019-204 — Deutsch DRC Connector Series|019-204]].

Ремонт проводной упряжки OEM в соответствии с инструкциями производителя транспортного средства.

Подключите датчик положения ускорителя после завершения ремонта.

![[19901416.png]]


> [!quote]- Original (English) · английский оригинал
> ### Initial Check
>
> **CAUTION · Осторожно**
> Do not use probes or test leads other than Part Number 3822758 or the connector will be damaged. The test leads must fit tightly in the connector without expanding the pins in the connector.
>
> If the INSITE™ electronic service tool is available, monitor the accelerator position sensor circuit for proper operation.
>
> If **not**, follow the troubleshooting procedures in this section.
>
> ### Resistance Check
>
> **CAUTION · Осторожно**
> Do not use probes or test leads other than Part Number 3822758 or the connector will be damaged. The test leads must fit tightly in the connector without expanding the pins in the connector.
>
> Disconnect the original equipment manufacturer (OEM) interface harness connector from the electronic control module (ECM).
>
> Make sure the sensor is connected to the OEM harness.
>
> Insert one of the test leads into the accelerator lever supply pin of the OEM interface harness connector.
>
> Insert the other test lead into the accelerator lever return pin of the connector.
>
> Connect the alligator clips to the multimeter test leads.
>
> Measure the resistance.
>
> The multimeter **must** show 2000 to 3000 ohms when the accelerator lever is at idle or full fuel position
>
> If the resistance is **not** within the specification, there is a problem with the accelerator lever return wire or the accelerator lever supply wire in the OEM interface harness, provided the accelerator position sensor has been checked. Repair the OEM interface harness connector. Refer to Procedure [[99-019-204 — Deutsch DRC Connector Series|019-204]].
>
> Repair the OEM harness according to the vehicle manufacturer's instructions.
>
> Remove the test lead from the accelerator lever return pin of the OEM interface harness connector and insert it into the accelerator lever signal pin of the connector.
>
> Make sure the accelerator lever is in the idle position.
>
> Measure the resistance.
>
> The multimeter **must** show 1500 to 3000 ohms.
>
> Move the accelerator lever to the full fuel position and measure the resistance again.
>
> The multimeter **must** show 200 to 1500 ohms.
>
> This resistance value **must** be at least 1000 ohms lower than the resistance value at the low-idle position, measured in the above check.
>
> If the resistance values are **not** within the specification, there is a problem with the accelerator lever supply wire or the accelerator lever signal wire in the OEM harness. Repair the OEM interface harness.
>
> If the resistance values in the two previous checks are within the specification, the accelerator lever return, accelerator lever signal, and accelerator lever supply wires **must** still be checked for a short circuit to ground, a short circuit from pin to pin, and a short circuit to battery supply.
>
> Examine the bulkhead connector and other connectors in the circuit for corrosion or damage to the accelerator position sensor wire terminals.
>
> ### Check for Short Circuit to Ground
>
> **CAUTION · Осторожно**
> Do not use probes or test leads other than Part Number 3822758 or the connector will be damaged. The test leads must fit tightly in the connector without expanding the pins in the connector.
>
> Disconnect the OEM interface harness connector from the ECM.
>
> Disconnect the accelerator position sensor from the OEM harness at the accelerator lever assembly.
>
> Insert the test lead into the accelerator lever supply pin of the OEM interface harness connector.
>
> Connect the alligator clip to the multimeter positive (+) probe.
>
> Touch the multimeter negative (-) probe to the engine block and measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> Remove the test lead from the accelerator lever supply pin of the OEM interface harness connector and insert it into the accelerator return pin of the connector.
>
> Touch the multimeter negative (-) probe to the engine block and measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> Remove the test lead from the accelerator lever return pin of the OEM interface harness connector and insert it into the accelerator signal pin of the connector.
>
> Touch the multimeter negative (-) probe to the engine block and measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> If **any** of these three resistance measurements are **not** open, there is a short circuit to ground between the wire connected to the accelerator lever return, accelerator lever signal, or accelerator lever supply pin. Repair the OEM interface harness connector. Refer to Procedure [[99-019-204 — Deutsch DRC Connector Series|019-204]].
>
> Repair the OEM harness according to the vehicle manufacturer's instructions.
>
> Connect the accelerator position sensor after completing the repair.
>
> ### Check for Short Circuit from Pin to Pin
>
> **CAUTION · Осторожно**
> Do not use probes or test leads other than Part Number 3822758 or the connector will be damaged. The test leads must fit tightly in the connector without expanding the pins in the connector.
>
> Disconnect the accelerator position sensor from the OEM harness at the accelerator lever assembly.
>
> Disconnect the engine harness connector and OEM interface harness connector from the ECM.
>
> Insert the test lead into the accelerator lever supply pin of the OEM interface harness connector.
>
> Insert the other test lead into the stop lamp pin of the connector.
>
> Connect the clips to the multimeter probes and measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> Remove the test lead from the stop lamp pin and test all other pins of the connector.
>
> Repeat the pin-to-pin check from the accelerator lever supply pin of the OEM interface harness connector to all pins of the engine harness connector.
>
> The multimeter **must** show an open circuit (100k ohms or more) at all pins.
>
> If the multimeter shows a closed circuit at any pin, there is a short circuit between the accelerator lever supply wire and any other wire that measured a closed circuit. Repair the OEM interface harness connector. Refer to Procedure [[99-019-204 — Deutsch DRC Connector Series|019-204]].
>
> Repair the OEM harness according to the vehicle manufacturer's instructions.
>
> Remove the test lead from the accelerator lever supply pin of the OEM interface harness connector and insert it into the accelerator lever return pin.
>
> Insert the other test lead into the stop lamp pin and measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> Remove the test lead from the stop lamp pin and test all other pins in the connector.
>
> Repeat the pin-to-pin check from the accelerator lever return pin of the OEM interface harness connector to all pins of the engine harness connector.
>
> The multimeter **must** show an open circuit (100k ohms or more) at all pins.
>
> If the multimeter shows a closed circuit at any pin, there is a short circuit between the accelerator lever return wire and any other wire that measured a closed circuit. Repair the OEM interface harness connector. Refer to Procedure [[99-019-204 — Deutsch DRC Connector Series|019-204]].
>
> Repair the OEM harness according to the vehicle manufacturer's instructions.
>
> Remove the test lead from the accelerator lever return pin of the OEM interface harness connector and insert it into the accelerator lever signal pin.
>
> Insert the other test lead into the stop lamp pin and measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> Remove the test lead from the stop lamp pin and test all other pins of the connector.
>
> Repeat the pin-to-pin check from the accelerator lever signal pin of the OEM interface harness connector to all pins of the engine harness connector.
>
> The multimeter **must** show an open circuit (100k ohms or more) at all pins.
>
> If the multimeter shows a closed circuit at any pin, there is a short circuit between the accelerator lever signal wire and any other wire that measured a closed circuit. Repair the OEM interface harness connector. Refer to Procedure [[99-019-204 — Deutsch DRC Connector Series|019-204]].
>
> Repair the OEM harness according to the vehicle manufacturer's instructions.
>
> ### Check for Short Circuit to External Voltage Source
>
> **CAUTION · Осторожно**
> Do not use probes or test leads other than Part Number 3822758 or the connector will be damaged. The test leads must fit tightly in the connector without expanding the pins in the connector.
>
> Disconnect the OEM interface harness connector from the ECM.
>
> Disconnect the accelerator position sensor from the OEM harness at the accelerator lever assembly.
>
> Turn the vehicle keyswitch to the ON position.
>
> Turn the multimeter dial to measure VDC.
>
> Insert one of the test leads into the accelerator lever supply pin of the OEM interface harness connector.
>
> Connect the clip to the multimeter positive (+) probe.
>
> Touch the multimeter negative (-) probe to the engine block and measure the voltage.
>
> The voltage **must** be 1.5 VDC or less.
>
> Remove the test lead from the accelerator lever supply pin of the OEM interface harness connector and insert it into the accelerator lever return pin of the connector.
>
> Touch the multimeter negative (-) probe to the engine block and measure the voltage.
>
> The voltage **must** be 1.5 VDC or less.
>
> Remove the test lead from the accelerator lever return pin of the OEM interface harness connector and insert it into the accelerator lever signal pin of the connector.
>
> Touch the multimeter negative (-) probe to the engine block and measure the voltage.
>
> The voltage **must** be 1.5 VDC or less.
>
> If more than 1.5 VDC is measured at any pin, there is a short circuit from the accelerator lever return, signal, or supply wire to a wire carrying power. Repair the OEM interface harness connector. Refer to Procedure [[99-019-204 — Deutsch DRC Connector Series|019-204]].
>
> Repair the OEM harness according to the vehicle manufacturer's instructions.
>
> Connect the accelerator position sensor after completing the repair.
