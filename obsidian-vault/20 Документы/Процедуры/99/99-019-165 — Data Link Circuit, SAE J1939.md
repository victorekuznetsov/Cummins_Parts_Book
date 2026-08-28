---
aliases:
  - "Цепь шины данных SAE J1939"
type: "Процедура"
doc: "99-019-165"
title_en: "Data Link Circuit, SAE J1939"
title_ru: "Цепь шины данных SAE J1939"
modified: "2015-06-25"
engines:
  - "41343322"
  - "41370103"
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
  - "4021442"
figures: 13
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-165.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-165.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "двигатель/NT/NTA855"
  - "группа/99"
  - "перевод/машинный"
---

# Data Link Circuit, SAE J1939
**Цепь шины данных SAE J1939**

> [!abstract] Процедура · `99-019-165`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]], [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3, NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]], [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section 19 - Electronic Engine Controls · Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2015-06-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-165.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-165.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Схема шины данных OEM J1939 CAN расположена в электропроводке OEM.

Цель этой шины данных CAN заключается в том, чтобы обеспечить связь с системами управления транспортным средством, такими как контроллеры передачи, система управления тягой и т. Д.

Традиционная схема шины данных OEM J1939 CAN описывается как экранированная витая пара и включает провода, подключенные к штифту положительной шины данных J1939 CAN (+), штифту отрицательной шины данных J1939 CAN (-) и штифту J1939 (щитовой) в штифте проводов OEM.

На новых транспортных средствах и оборудовании OEM-производители могут использовать схему шины данных OEM J1939 CAN, которая описывается как неэкранированная витая пара (UTP). Неэкранированная витая пара (UTP) J1939 шина данных CAN включает в себя J1939 (щитовой) штифт и **только** включает в себя штифт данных J1939 CAN положительный (+) штифт и штифт данных J1939 CAN отрицательный (-) штифт в проводной упряжке OEM.

С переключателем зажигания в положении ON сообщения шины данных CAN будут транслироваться на шине данных OEM J1939 CAN. Трансляция прекращается, когда переключатель зажигания поворачивается в положение выключения.

![[19803969.png]]

Общество автомобильных инженеров (SAE) J1939 имеет строгие правила, которые должны соблюдаться для успешного общения. Понимание некоторых фундаментальных принципов SAE J1939 поможет убедиться в том, что эти рекомендации соблюдаются.

Основным компонентом системы SAE J1939 является магистральная проводка. Длина проводной ремни может достигать 40 метров[131 фут]. Стержневой проводной упряжкой на каждом конце завершается резистор 120 Ом.

Максимально тридцать различных устройств могут быть подключены к магистрали SAE J1939 одновременно. Каждое устройство, такое как адаптер шины данных CAN, соединено с магистралью через заглушку, которая может быть длиной до 1 метра \[3.3 фута \]. Разъем заглушки представляет собой 3-контактную вилку.

![[19802395.png]]

Концевые резисторы (1) должны быть на месте на розетках магистральной проводов OEM (2) для поддержания надлежащей связи. Каждый резистор имеет размер 120 Ом и может быть расположен в съемной крышке.

![[19802397.png]]

Некоторые производители предпочтут предоставить полный комплект магистральной проводов SAE J1939. Если это предусмотрено, подключение к инструменту электронного обслуживания осуществляется 9-контактным разъемом шины данных CAN (1), Номер детали 3162848.

> [!note] Примечание
> Некоторые OEM-производители устанавливают 9-контактный разъем в кабине, но не подключают все контакты для поддержки протокола J1939.

Чтобы проверить хребет OEM J1939, переключатель зажигания переключателя зажигания в положение выключения. Измерить сопротивление от шины данных SAE J1939 CAN положительного (+) штифта к шине данных SAE J1939 CAN отрицательного (-) штифта 9-контактного разъема DeutschTM.

Мультиметр **должен** читать от 50 до 65 Ом для того, чтобы электронный сервис мог устанавливать связь.

Если OEM-производитель не подает магистральную проводку J1939 на 9-контактный разъем, единственный способ установить связь J1939 - это либо установка связи на испытательном стенде, либо модуль управления двигателем через установку связи двигателя.[[00-022-999 — Service Tools and Hardware - Overview|См. процедуру 022-999]].

> [!note] Примечание
> Типичный разъем SAE J1939 будет 9-контактным.

![[19c01495.png]]

| Пин | сигнал |
|---|---|
| А. | земля |
| B | Незакрученная батарея |
| C | J1939 CAN Data Bus (+) (недоступная ссылка) |
| D | J1939 CAN Data Bus (-) (недоступная ссылка) |
| Е | J1939 CAN Data Bus (щит) (если есть) |
| F | J1708 CAN Data Bus (+) |
| GGG | J1708 CAN Data Bus (-) (недоступная ссылка) |
| Hе | Открыть |
| Джей | Открыть |

![[19400739.png]]

### Проверка сопротивления

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

> [!warning] ОСТОРОЖНО
> Правильные провода и/или одобренный Cummins® инструмент для тестирования цепи должны использоваться при работе с электрическими разъемами для предотвращения расширения штифта и повреждения разъема.

Переведите замок зажигания в положение OFF.

Отсоедините аккумуляторные батареи.

Отсоедините разъем OEM-проводов от ECU.

Вставьте измерительный щуп в шину данных SAE J1939 CAN положительного (+) штифта разъема проводов OEM-производителя и соедините его с многометровым щупом. Вставьте другой измерительный щуп в шину данных SAE J1939 CAN положительного (+) штифта 9-контактного разъема DeutschTM и соедините его с мультиметром.

Измерьте сопротивление. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

Если цепь **не** закрыта, отремонтируйте или замените электропроводку OEM. См. руководство по устранению неполадок и ремонту OEM для процедур.

Вставьте многометровый свинец в шину данных SAE J1939 CAN отрицательной (-) разъёма проводов OEM-приемника. Прикосновение к другому приводит к отрицательному (-) значку шины данных SAE J1939 разъема DeutschTM с 9-контактным разъемом. Измерьте сопротивление. Мультиметр **должен** показывать замкнутую цепь (10 Ом или меньше)

Если цепь **не** закрыта, отремонтируйте или замените электропроводку OEM. См. руководство по устранению неполадок и ремонту OEM для процедур.

Если значения верны, схема **должна *** все еще проверяться на короткое замыкание на землю и короткое замыкание от пин-кодов до пин-кодов.

Удалите свинец из шины данных SAE J1939 CAN отрицательного (-) штифта разъема проводов OEM и вставьте его в штифт шины данных SAE J1939 CAN (щитовой) штифт, если штифт экрана доступен.

Если цепь шины данных J1939 CAN представляет собой неэкранированную витую пару (UTP), то штифт экрана будет **не**.

Если щитовой штифт предусмотрен, измерьте сопротивление от штифта шины данных SAE J1939 CAN (щитовой) штифта разъема проводов OEM к штифту данных шины (щитовой) шины данных SAE J1939 DeutschTM разъема 9-контактного штифта.

Мультиметр **должен** показать замкнутую цепь (10 Ом и менее). Если цепь **не** закрыта, отремонтируйте или замените электропроводку OEM. См. руководство по устранению неполадок и ремонту OEM для процедур.

Если (щитовой) штифт предусмотрен, измерьте сопротивление от штифта шины данных SAE J1939 CAN (щитовой) штифта 9-контактного разъема DeutschTM к блоку двигателя или заземлению шасси. Щит шины данных SAE J1939 CAN** должен быть заземлен до заземления аккумулятора автомобиля. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее). Если схема **не закрыта, обратитесь к руководству по устранению неполадок и ремонту OEM для инструкции по ремонту.

Если на любом из этих этапов измерено более 10 Ом, то в шине данных SAE J1939 CAN может быть открытая цепь с положительным (+) штифтом, шине данных SAE J1939 CAN с отрицательным (-) штифтом или штифте SAE J1939 (щитовой) штифт, или полярность **не** правильная. Также может быть открытая схема от штифта шины данных CAN (щитовой) до заземления аккумулятора автомобиля.

Если значения верны, шина данных SAE J1939 CAN положительный (+) штифт и шина данных CAN отрицательный (-) штифт **должны быть проверены на короткое замыкание на землю. Шина данных SAE J1939 CAN положительная (+) штифт, шина данных CAN отрицательная (-) штифт, и штифт данных CAN (щит)** должны быть проверены на короткое замыкание от штифта до штифта.

![[19c01496.png]]

### Проверка на замыкание на массу

> [!warning] ОСТОРОЖНО
> Правильные провода и/или одобренный Cummins® инструмент для тестирования цепи должны использоваться при работе с электрическими разъемами для предотвращения расширения штифта и повреждения разъема.

Отключите разъем интерфейса оригинального производителя оборудования (OEM) проводов жгута проводов двигателя. Чтобы определить местоположение разъема, см. соответствующую схему проводов двигателя.Вставьте измерительный щуп в шину данных SAE J1939 CAN положительного (+) штифта разъема проводов OEM-производителя и соедините его с многометровым щупом. Прикоснитесь к другому многометровому щупу к блоку двигателя или земле шасси.

Измерьте сопротивление. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, отремонтируйте или замените проводку OEM. См. руководство изготовителя машины по диагностике и ремонту.

Удалите пробный щуп из шины данных SAE J1939 CAN положительного (+) штифта и вставьте его в шину данных SAE J1939 CAN отрицательного (-) штифта. Измерить сопротивление от SAE J1939 CAN шины данных отрицательный (-) штифт OEM проводов ремня разъема к блоку двигателя или шасси земли. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, отремонтируйте или замените проводку OEM. См. руководство изготовителя машины по диагностике и ремонту.

![[19c01270.png]]

### Проверка на замыкание между контактами

> [!warning] ОСТОРОЖНО
> Правильные провода и/или одобренный Cummins® инструмент для тестирования цепи должны использоваться при работе с электрическими разъемами для предотвращения расширения штифта и повреждения разъема.

Отключите разъем интерфейса оригинального производителя оборудования (OEM) проводов жгута проводов двигателя. Чтобы определить местоположение разъема, см. соответствующую схему проводов двигателя.

Вставьте измерительный щуп в шину данных SAE J1939 CAN положительного (+) штифта разъема проводов OEM-производителя и соедините его с многометровым щупом. Вставьте другой испытательный щуп в другой штифт в разъем проводной упряжки OEM и соедините его с другим многометровым щупом.

Измерьте сопротивление от шин данных SAE J1939 CAN положительного (+) штифта к первому штифту в разъеме. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, отремонтируйте или замените проводку OEM. См. руководство изготовителя машины по диагностике и ремонту.

![[19c01271.png]]

Измерьте сопротивление от SAE J1939 CAN шины данных положительного (+) штифта OEM проводов жгута разъема ко всем другим штифтам в разъеме, по одному за раз. Мультиметр **должен** показывать открытую схему (100км или более) на всех штифтах, за исключением отрицательной шины данных J1939 CAN (-).

Если схема **не** открыта, отремонтируйте или замените проводку OEM. См. руководство изготовителя машины по диагностике и ремонту.

![[19c01215.png]]

Удалите пробный щуп из положительного (+) штифта шины данных J1939 CAN и вставьте его в штифт шины данных J1939 CAN (щитовой) штифт разъема проводов OEM, если штифт экрана доступен

> [!note] Примечание
> Если цепь шины данных J1939 CAN представляет собой неэкранированную витую пару (UTP), то штифт (щит) будет **не**. Если штифт экрана **не** предусмотрен, штифт отрицательной шины данных CAN * должен быть проверен на короткое замыкание к другим штифтам.

Вставьте другой испытательный щуп в другой штифт в разъеме. Измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, отремонтируйте или замените проводку OEM. См. руководство изготовителя машины по диагностике и ремонту.

![[19c01271.png]]

Измерьте сопротивление от штифта шины данных SAE J1939 CAN (щита), если таковой имеется, ко всем другим штифтам в разъеме, по одному за раз. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, отремонтируйте или замените проводку OEM. См. руководство изготовителя машины по диагностике и ремонту.

![[19c01215.png]]

Удалите пробный щуп из шины данных SAE J1939 CAN (щитовой) штифт и вставьте его в шину данных SAE J1939 CAN отрицательный (-) штифт разъема проводов OEM. Вставьте другой испытательный щуп в другой штифт в разъеме. Измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, отремонтируйте или замените проводку OEM. См. руководство изготовителя машины по диагностике и ремонту.

![[19c01271.png]]

Измерить сопротивление от SAE J1939 CAN шины данных отрицательного (-) штифта OEM проводов жгута разъёма ко всем другим штифтам в разъеме. Мультиметр **должен** показывать открытую схему (100к Ом или более) на всех штифтах, за исключением штифта положительной шины данных J1939 CAN (+).

Если схема **не** открыта, отремонтируйте или замените проводку OEM. См. руководство изготовителя машины по диагностике и ремонту.

Подключите все компоненты после завершения ремонта.

![[19c01215.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The OEM J1939 datalink circuit is located in the OEM wiring harness.
>
> The purpose of this datalink is to allow communication with vehicle control-operated systems such as transmission controllers, traction control system, etc.
>
> The traditional OEM J1939 datalink circuit is described as a shielded twisted pair and includes the wires connected to the J1939 datalink positive (+) pin, the J1939 datalink negative (-) pin, and the J1939 (shield) pin in the OEM harness.
>
> On newer vehicles and equipment, OEM's can utilize an OEM J1939 datalink circuit that is described as an unshielded twisted pair (UTP). The unshielded twisted pair (UTP) J1939 datalink does **not** include the J1939 (shield) pin and **only** includes the J1939 datalink positive (+) pin and the J1939 datalink negative (-) pin in the OEM harness.
>
> With the keyswitch in the ON position, public datalink messages will be broadcast on the OEM J1939 datalink. The broadcast will stop when the keyswitch is turned to the OFF position.
>
> The Society of Automotive Engineers (SAE) J1939 has strict guidelines that **must** be followed for successful communication. Understanding some fundamentals about SAE J1939 will help make sure these guidelines are followed.
>
> The main component of an SAE J1939 system is a backbone harness. The harness can be up to 40 meters \[131 feet\] in length. The backbone harness is terminated at each end with a 120 ohm resistor.
>
> A maximum of thirty different devices can be attached to the SAE J1939 backbone at once. Each device, such as the datalink adapter, is connected to the backbone through a stub, which can be up to 1 meter \[3.3 ft\] in length. The stub connector is a 3-pin plug.
>
> The terminating resistor caps (1) **must** be in place on the OEM backbone harness plugs (2) to maintain proper communication. Each resistor is 120 ohms and can be located in a removable cap.
>
> Some OEMs will choose to provide a complete SAE J1939 backbone harness. If this is supplied, connection to the electronic service tool is accomplished by a 9-pin datalink connector (1), Part Number 3162848.
>
> **Note · Примечание**
> Some OEM's place a 9-pin connector in the cab, but do **not** connect all of the pins to support J1939 protocol.
>
> To check for the OEM J1939 backbone, turn the keyswitch to the OFF position. Measure the resistance from the SAE J1939 datalink positive (+) pin to the SAE J1939 datalink negative (-) pin of the 9-pin Deutsch™ connector.
>
> The multimeter **must** read between 50 and 65 ohms for the electronic service tool to be able to establish communication.
>
> If the OEM does **not** supply the J1939 backbone harness to the 9-pin connector, the **only** way to establish J1939 communication is through either the bench communication setup or for the Engine Control Module through the engine communication setup. [[00-022-999 — Service Tools and Hardware - Overview|Refer to Procedure 022-999]].
>
> **Note · Примечание**
> The typical SAE J1939 connector will be a 9-pin connector.
>
> | Pin | Signal |
> |---|---|
> | A | Ground |
> | B | Unswitched Battery |
> | C | J1939 datalink (+) |
> | D | J1939 datalink (-) |
> | E | J1939 datalink (shield) (if available) |
> | F | J1708 datalink (+) |
> | G | J1708 datalink (-) |
> | H | Open |
> | J | Open |
>
> ### Resistance Check
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> **CAUTION · Осторожно**
> Proper leads and/or a Cummins® approved circuit testing tool must be used when working with electrical connectors to prevent pin expansion and damage to the connector.
>
> Turn the keyswitch to the OFF position.
>
> Disconnect the batteries.
>
> Disconnect the OEM harness connector from the ECU.
>
> Insert a test lead into the SAE J1939 datalink positive (+) pin of the OEM harness connector, and connect it to the multimeter probe. Insert the other test lead into the SAE J1939 datalink positive (+) pin of the 9-pin Deutsch™ connector, and connect it to the multimeter.
>
> Measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less).
>
> If the circuit is **not** closed, repair or replace the OEM harness. Refer to the OEM troubleshooting and repair manual for the procedures.
>
> Insert the multimeter lead into the SAE J1939 datalink negative (-) of the OEM harness connector. Touch the other lead to the SAE J1939 datalink negative (-) pin of the 9-pin Deutsch™ connector. Measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less)
>
> If the circuit is **not** closed, repair or replace the OEM harness. Refer to the OEM troubleshooting and repair manual for the procedures.
>
> If the values are correct, the circuit **must** still be checked for a short circuit to ground and a short circuit from pin to pin.
>
> Remove the lead from the SAE J1939 datalink negative (-) pin of the OEM harness connector and insert it into the SAE J1939 datalink (shield) pin, if the shield pin is available.
>
> If the J1939 datalink circuit is an unshielded twisted pair (UTP), the shield pin will **not** be provided.
>
> If the shield pin is provided, measure the resistance from the SAE J1939 datalink (shield) pin of the OEM harness connector to the SAE J1939 datalink (shield) pin of the 9-pin Deutsch™ connector.
>
> The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, repair or replace the OEM harness. Refer to the OEM troubleshooting and repair manual for the procedures.
>
> If the (shield) pin is provided, measure the resistance from the SAE J1939 datalink (shield) pin of the 9-pin Deutsch™ connector to the engine block or chassis ground. The SAE J1939 datalink shield **must** be grounded to the vehicle battery ground. The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, refer to the OEM troubleshooting and repair manual for repair instruction.
>
> If more than 10 ohms are measured in any of these steps, there can be an open circuit in the SAE J1939 datalink positive (+) pin, the SAE J1939 datalink negative (-) pin, or the SAE J1939 (shield) pin, or the polarity is **not** correct. There can also be an open circuit from the datalink (shield) pin to vehicle battery ground.
>
> If the values are correct, the SAE J1939 datalink positive (+) pin and the datalink negative (-) pin **must** still be checked for a short circuit to ground. The SAE J1939 datalink positive (+) pin, the datalink negative (-) pin, and the datalink (shield) pin **must** still be checked for a short circuit from pin to pin.
>
> ### Check for Short Circuit to Ground
>
> **CAUTION · Осторожно**
> Proper leads and/or a Cummins® approved circuit testing tool must be used when working with electrical connectors to prevent pin expansion and damage to the connector.
>
> Disconnect the original equipment manufacturer (OEM) harness engine interface connector. To determine the location of the connector, see the corresponding engine wiring diagram.Insert a test lead into the SAE J1939 datalink positive (+) pin of the OEM harness connector and connect it to a multimeter probe. Touch the other multimeter probe to the engine block or chassis ground.
>
> Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the OEM harness. Refer to the OEM troubleshooting and repair manual.
>
> Remove the test lead from the SAE J1939 datalink positive (+) pin and insert it into the SAE J1939 datalink negative (-) pin. Measure the resistance from the SAE J1939 datalink negative (-) pin of the OEM harness connector to the engine block or chassis ground. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the OEM harness. Refer to the OEM troubleshooting and repair manual.
>
> ### Check for Short Circuit from Pin to Pin
>
> **CAUTION · Осторожно**
> Proper leads and/or a Cummins® approved circuit testing tool must be used when working with electrical connectors to prevent pin expansion and damage to the connector.
>
> Disconnect the original equipment manufacturer (OEM) harness engine interface connector. To determine the location of the connector, see the corresponding engine wiring diagram.
>
> Insert a test lead into the SAE J1939 datalink positive (+) pin of the OEM harness connector and connect it to the multimeter probe. Insert the other test lead into another pin in the connector of the OEM harness and connect it to the other multimeter probe.
>
> Measure the resistance from the SAE J1939 datalink positive (+) pin to the first pin in the connector. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the OEM harness. Refer to the OEM troubleshooting and repair manual.
>
> Measure the resistance from the SAE J1939 datalink positive (+) pin of the OEM harness connector to all other pins in the connector, one at a time. The multimeter **must** show an open circuit (100k ohms or more) at all pins, except the J1939 datalink negative (-).
>
> If the circuit is **not** open, repair or replace the OEM harness. Refer to the OEM troubleshooting and repair manual.
>
> Remove the test lead from the J1939 datalink positive (+) pin and insert it into the J1939 datalink (shield) pin of the OEM harness connector, if the shield pin is available
>
> **Note · Примечание**
> If the J1939 datalink circuit is an unshielded twisted pair (UTP), the (shield) pin will **not** be provided. If the shield pin is **not** provided, the datalink negative (-) pin **must** still be checked for a short circuit to the other pins.
>
> Insert the other test lead into another pin in the connector. Measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the OEM harness. Refer to the OEM troubleshooting and repair manual.
>
> Measure the resistance from the SAE J1939 datalink (shield) pin, if available, to all other pins in the connector, one at a time. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the OEM harness. Refer to the OEM troubleshooting and repair manual.
>
> Remove the test lead from the SAE J1939 datalink (shield) pin and insert it into the SAE J1939 datalink negative (-) pin of the OEM harness connector. Insert the other test lead into another pin in the connector. Measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the OEM harness. Refer to the OEM troubleshooting and repair manual.
>
> Measure the resistance from the SAE J1939 datalink negative (-) pin of the OEM harness connector to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more) at all pins, except the J1939 datalink positive (+) pin.
>
> If the circuit is **not** open, repair or replace the OEM harness. Refer to the OEM troubleshooting and repair manual.
>
> Connect all the components after the repair is complete.
