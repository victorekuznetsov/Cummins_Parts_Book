---
aliases:
  - "Цепь общедоступной шины данных"
type: "Процедура"
doc: "98-019-026"
title_en: "Data Link Circuit, Public"
title_ru: "Цепь общедоступной шины данных"
modified: "2012-11-14"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 14
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-026.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-026.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Data Link Circuit, Public
**Цепь общедоступной шины данных**

> [!abstract] Процедура · `98-019-026`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2012-11-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-026.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-026.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Эта схема используется для электронных средств обслуживания CompulinkTM, EchekTM или INSITETM для связи с модулем управления двигателем (ECM). Схема состоит из проводов, соединенных с контактом 6 и контактом 8 главного разъёма проводов двигателя. Есть два разъема шины данных CAN. Один расположен в непосредственной близости от приборной панели (обычно под ней), а другой расположен на главной проводах двигателя вблизи разъема ECM.

> [!note] Примечание
> Проверьте оригинальную часть схемы производителя оборудования (OEM).[[99-019-071 — OEM Wiring Harness|См. процедуру 019-071 в разделе 19.]]

![[19801719.png]]

### Осмотр

Отключите разъем ECM.

Промыть и очистить контакты разъема с помощью контактного очистителя, номер детали 3824510.

Осмотрите штифты в главном разъеме проводов двигателя для поврежденных контактов.

Если какой-либо из штифтов поврежден, отремонтируйте или замените основную проводку двигателя.

- См. процедуру 019-228 в разделе 19.
- [[98-019-043 — Engine Wiring Harness|См. процедуру 019-043 в разделе 19.]]

![[19801724.png]]

### Проверка сопротивления

Отключите разъем ECM.

Отключите разъем C6.

Выберите функцию сопротивления на мультиметре.

Прикосновение к одному из мультиметров приводит к контакту 6 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к контакту J разъема C6.

![[19801725.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать менее 10 Ом, что является замкнутой схемой. Если схема **не** закрыта, то ремонтируйте или заменяйте основную проводку двигателя.

- См. процедуру 019-228 в разделе 19.
- [[98-019-043 — Engine Wiring Harness|См. процедуру 019-043 в разделе 19.]]

![[19801619.png]]

Прикосновение к одному из мультиметров приводит к контакту 8 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к контакту Н разъема С6.

Измерьте сопротивление.

Мультиметр **должен **показывать менее 10 Ом. Если схема **не** менее 10 Ом, отремонтируйте или замените основную проводку двигателя.

- См. процедуру 019-228 в разделе 19.
- [[98-019-043 — Engine Wiring Harness|См. процедуру 019-043 в разделе 19.]]

![[19801727.png]]

### Проверка на замыкание на массу

Отключите разъем ECM.

Отключите разъемы C5 и C6.

Промыть и очистить контакты разъема с помощью контактного очистителя, номер детали 3824510. Проверьте разъемы на наличие поврежденных контактов.

Прикосновение к одному из мультиметров приводит к контакту 6 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к хорошей чистой поверхности на блоке двигателя.

![[19801728.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом, что является открытой схемой. Если схема **не** открыта, то между проводом, подключенным к контакту 6, и заземлением блока двигателя имеется короткое замыкание.

Ремонт или замена основного двигателя проводов жгута.

- См. процедуру 019-228 в разделе 19.
- [[98-019-043 — Engine Wiring Harness|См. процедуру 019-043 в разделе 19.]]

![[19801621.png]]

Прикосновение к одному из мультиметров приводит к контакту 8 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к контакту Н разъема С6.

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом. Если схема **не** более 100k Ом, отремонтируйте или замените основную проводку двигателя.

- См. процедуру 019-228 в разделе 19.
- [[98-019-043 — Engine Wiring Harness|См. процедуру 019-043 в разделе 19.]]

![[19801730.png]]

### Проверка на замыкание между контактами

Отключите разъемы ECM, C5 и C6.

Смой и очисти контакты разъема.

Проверьте разъемы на наличие поврежденных контактов.

Проверьте короткое замыкание между контактом 6 главного разъёма проводов двигателя и всеми другими штифтами в разъеме, кроме контакта 8.

Прикосновение к одному из мультиметров приводит к контакту 6 разъема. Прикосновение к другому мультиметру приводит ко всем другим штифтам в разъеме, кроме контакта 8, по одному за раз.

![[19801731.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом, что является открытой схемой. Если схема **не** открыта, то между проводом, подключенным к контакту 6 главного разъёма проводов двигателя, и любым другим штифтом, который измеряется менее 100k Ом.

Ремонт или замена основного двигателя проводов жгута.

- См. процедуру 019-228 в разделе 19.
- [[98-019-043 — Engine Wiring Harness|См. процедуру 019-043 в разделе 19.]]

![[19801621.png]]

Прикосновение к одному из мультиметров приводит к контакту 8 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит ко всем другим штифтам в разъеме, кроме контакта 6, по одному за раз.

Измерьте сопротивление.

Мультиметр должен измерять более 100k ом. Если измеренные сопротивления **не **больше 100k Ом, то отремонтируйте или замените основную проводку двигателя.

- См. процедуру 019-228 в разделе 19.
- [[98-019-043 — Engine Wiring Harness|См. процедуру 019-043 в разделе 19.]]

![[19802406.png]]

### Проверка полярности

Найдите разъем шины данных CAN основной проводов двигателя. Провода шины данных CAN 6 и 8 находятся в 2-контактном разъеме Weather-PackTM.

![[19801720.png]]

Прикосновение к мультиметру положительного (+) приводит к контакту B разъема шины данных CAN. Прикоснитесь к отрицательному (-) мультиметру, который ведет к заземлению блока двигателя. Измерьте напряжение.Мультиметр **должен **показывать от 0 до 1 VDC.

![[19801772.png]]

Если напряжение при контакте В измеряется от 4 до 5 ВДК, штифты в 2-контактном разъеме Weather-PackTM неправильно установлены и должны быть отменены.

Если напряжение и полярность верны, схему необходимо проверить на короткое замыкание на землю и короткое замыкание от контакта к контакту.

![[19801723.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> This circuit is used for the Compulink™, Echek™, or INSITE™ electronic service tool to communicate with the engine control module (ECM). The circuit consists of the wires connected to pin 6 and pin 8 of the main engine harness connector. There are two datalink connectors. One is located in the vicinity of the dash (usually under it) and the other is located on the main engine harness near the ECM connector.
>
> **Note · Примечание**
> Check the original equipment manufacturer (OEM) portion of this circuit. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071 in Section 19.]]
>
> ### Inspect
>
> Disconnect the ECM connector.
>
> Flush and clean the connector pins using contact cleaner, Part Number 3824510.
>
> Inspect the pins in the main engine harness connector for damaged pins.
>
> If any of the pins are damaged, repair or replace the main engine harness.
>
> - Refer to Procedure 019-228 in Section 19.
> - [[98-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 in Section 19.]]
>
> ### Resistance Check
>
> Disconnect the ECM connector.
>
> Disconnect the C6 connector.
>
> Select the resistance function on the multimeter.
>
> Touch one of the multimeter leads to pin 6 of the main engine harness connector. Touch the other multimeter lead to pin J of the C6 connector.
>
> Measure the resistance.
>
> The multimeter **must** show less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, then repair or replace the main engine harness.
>
> - Refer to Procedure 019-228 in Section 19.
> - [[98-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 in Section 19.]]
>
> Touch one of the multimeter leads to pin 8 of the main engine harness connector. Touch the other multimeter lead to pin H of the C6 connector.
>
> Measure the resistance.
>
> The multimeter **must** show less than 10 ohms. If the circuit is **not** less than 10 ohms, repair or replace the main engine harness.
>
> - Refer to Procedure 019-228 in Section 19.
> - [[98-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 in Section 19.]]
>
> ### Check for Short Circuit to Ground
>
> Disconnect the ECM connector.
>
> Disconnect the C5 and C6 connectors.
>
> Flush and clean the connector pins using contact cleaner, Part Number 3824510. Inspect the connectors for damaged pins.
>
> Touch one of the multimeter leads to pin 6 of the main engine harness connector. Touch the other multimeter lead to a good clean surface on the engine block.
>
> Measure the resistance.
>
> The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short circuit between the wire connected to pin 6 and engine block ground.
>
> Repair or replace the main engine harness.
>
> - Refer to Procedure 019-228 in Section 19.
> - [[98-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 in Section 19.]]
>
> Touch one of the multimeter leads to pin 8 of the main engine harness connector. Touch the other multimeter lead to pin H of the C6 connector.
>
> Measure the resistance.
>
> The multimeter **must** show more than 100k ohms. If the circuit is **not** more than 100k ohms, repair or replace the main engine harness.
>
> - Refer to Procedure 019-228 in Section 19.
> - [[98-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 in Section 19.]]
>
> ### Check for Short Circuit from Pin to Pin
>
> Disconnect the ECM, C5, and C6 connectors.
>
> Flush and clean the connector pins.
>
> Inspect the connectors for damaged pins.
>
> Check for a short circuit between pin 6 of the main engine harness connector and all other pins in the connector, except pin 8.
>
> Touch one of the multimeter leads to pin 6 of the connector. Touch the other multimeter lead to all other pins in the connector except for pin 8, one at a time.
>
> Measure the resistance.
>
> The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short between the wire connected to pin 6 of the main engine harness connector and any other pin that measured less than 100k ohms.
>
> Repair or replace the main engine harness.
>
> - Refer to Procedure 019-228 in Section 19.
> - [[98-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 in Section 19.]]
>
> Touch one of the multimeter leads to pin 8 of the main engine harness connector. Touch the other multimeter lead to all other pins in the connector, except pin 6, one at a time.
>
> Measure the resistance.
>
> The multimeter should measure more than 100k ohms. If the measured resistances are **not** greater than 100k ohms, then repair or replace the main engine harness.
>
> - Refer to Procedure 019-228 in Section 19.
> - [[98-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 in Section 19.]]
>
> ### Polarity Check
>
> Locate the datalink connector of the main engine harness. The data link wires nunber 6 and number 8 are in the 2-pin Weather-Pack™ connector.
>
> Touch the multimeter positive (+) lead to pin B of the datalink connector. Touch the negative (-) multimeter lead to the engine block ground. Measure the voltage.The multimeter **must** show 0 to 1 VDC.
>
> If the voltage at pin B measures 4 to 5 VDC, the pins in the 2-pin Weather-Pack™ connector are improperly installed and **must** be reversed.
>
> If the voltage and polarity are correct, the circuit **must** be checked for short circuit to ground and short circuits from pin-to-pin.
