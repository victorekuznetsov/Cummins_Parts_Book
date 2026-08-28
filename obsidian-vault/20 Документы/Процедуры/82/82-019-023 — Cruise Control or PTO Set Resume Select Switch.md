---
aliases:
  - "Выключатель круиз-контроля или отбора мощности (Set/Resume)"
type: "Процедура"
doc: "82-019-023"
title_en: "Cruise Control or PTO Set/Resume Select Switch"
title_ru: "Выключатель круиз-контроля или отбора мощности (Set/Resume)"
modified: "2003-10-09"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 15
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-023.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-023.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Cruise Control or PTO Set/Resume Select Switch
**Выключатель круиз-контроля или отбора мощности (Set/Resume)**

> [!abstract] Процедура · `82-019-023`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2003-10-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-023.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-023.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Переключатель выбора круиз-контроля имеет две позиции: СТАТЬЯ/КОАСТ И РЕЗУМЕ/УСТАНОВЛЕНИЕ.

Переключатель может использоваться для:

- Круз Контрол: СТАТЬЯ/АССТОЯНИЕ И РЕЗУМЕ/КОАСТ
- ПТО: РЕКРЕМЕНТ/ДЕКРЕМЕНТ
- Идл: РЕКРЕМЕНТ/ДЕКРЕМЕНТ
- Дорога быстрой управляемости: РЕКРЕМЕНТ/ДЕКРЕМЕНТ
- Диагностический фаулит: РЕКРЕМЕНТ/ДЕКРЕМЕНТ

Дополнительную информацию см. в разделе F.

![[gp8swgh.png]]

Оператор может установить крейсерскую скорость транспортного средства, когда переключатель находится в положении SET/COAST. Положение SET/COAST также может быть использовано для снижения крейсерской скорости транспортного средства. Держите переключатель в положении SET / COAST, и автомобиль будет двигаться на более низкой скорости. Когда выключатель будет выпущен, крейсерская скорость будет сброшена.

> [!note] Примечание
> Некоторые производители имеют коммутаторы с меткой SET/ACCEL и RESUME/COAST.

![[gp8swgh.png]]

Оператор может возобновить круиз-контроль после сцепления или торможения, переместив переключатель на РЕЗУМ/АКСЕЛЕРАТОР. Скорость автомобиля вернется к последней установленной миле в час.

Положение RESUME/ACCELERATE также может быть использовано для увеличения скорости движения транспортного средства. Держите выключатель в положении RESUME/ACCELERATE, и автомобиль будет увеличивать скорость. Когда выключатель будет выпущен, крейсерская скорость будет сброшена.

![[gp8swgk.png]]

Схема выбора круиз-контроля представляет собой общую основу, контакт 14 (сигнал SET/COAST), контакт 24 (сигнал RESUME/ACCELERATE) и двухпозиционный выключатель выбора, расположенный в транспортном средстве.

![[19c00179.png]]

### Проверка сопротивления

Если INSITETM доступен, проверьте выключатель круиз-контроля для правильной работы. Если **не**, следуйте процедурам устранения неполадок в этом разделе.

Пометьте провода с местоположением на выключателе или номером провода. Удалите три электрических разъема из коммутатора.

![[19c00180.png]]

Настройте мультиметр для измерения сопротивления.

Прикоснитесь к одному многометровому щупу к центральному терминалу переключателя.

Прикоснитесь к другому многометровому щупу к верхнему терминалу переключателя.

![[ee8swkh.png]]

Держите переключатель в положении SET/COAST. Мультиметр **должен** показывать открытую схему (100к Ом или более), когда переключатель удерживается в положении SET/COAST и после его выпуска. Если схема не открыта, выключатель не работает. См. руководство по устранению неполадок и ремонту OEM для процедур замены.

![[19900504.png]]

Держите переключатель в положении РЕЗУМЕНТ/УСТАВЛЕННОСТЬ. Мультиметр **должен** показывать замкнутую цепь (10 Ом или меньше), когда переключатель удерживается в положении РЕЗУМЕНТ/УСТАВЛЕННОЕ.

![[ee8swkj.png]]

Когда выключатель выпущен, мультиметр **должен** показать открытую схему (100k Ом или более). Если мультиметр показывает **не** правильные значения в любом из измерительн, переключатель не работает. См. руководство по устранению неполадок и ремонту OEM для процедур замены.

Если значение сопротивления правильное, переключатель должен быть проверен на короткое замыкание на землю.

![[ee8swkk.png]]

Прикоснитесь к одному многометровому щупу к центральному терминалу переключателя. Прикоснитесь к другому многометровому щупу до нижнего конца переключателя.

![[wr8swkb.png]]

Держите переключатель в положении SET/COAST. Мультиметр **должен** показывать замкнутую цепь (10 Ом или меньше), в то время как переключатель удерживается в положении SET/COAST.

![[wr8swkb.png]]

Когда выключатель выпущен, мультиметр **должен** показать открытую схему (100k Ом или более). Если мультиметр показывает **не** правильные значения в любом из измерительн, переключатель не работает. См. руководство по устранению неполадок и ремонту OEM для процедур замены.

![[ee8swko.png]]

Переключитесь на позицию ПОДДЕРЖАНИЯ/УСТАВЛЕНИЯ. Мультиметр **должен **показывать открытую схему (100к Ом или более), когда выключатель включен и когда он выпущен. Если схема не открыта, выключатель не работает. См. руководство по устранению неполадок и ремонту OEM для процедур замены.

![[ee8swkp.png]]

### Проверка на замыкание на массу

Настройте мультиметр для измерения сопротивления.

Прикоснитесь к одному многометровому щупу к верхнему терминалу переключателя. Прикоснитесь к другому многометровому щупу к земле шасси. Переместите переключатель в положение SET/COAST, затем в положение RESUME/ACCELERATE. Измерьте сопротивление. Мультиметр **должен** показывать открытую схему (100к Ом или более), когда переключатель находится во всех положениях. Если схема не открыта, выключатель не работает. См. руководство по устранению неполадок и ремонту OEM для процедур замены.

> [!missing]- Иллюстрация `ee8swkl.png` не извлечена — смотрите PDF-оригинал документа

Прикоснитесь одним многометровым щупом к нижнему терминалу переключателя. Прикоснитесь к другому многометровому щупу на земле шасси. Переместите переключатель в положение RESUME/ACCELERATE, затем в положение SET/COAST. Измерьте сопротивление. Мультиметр **должен** показывать открытую схему (100к Ом или более), когда переключатель находится во всех положениях. Если схема не открыта, выключатель не работает. См. руководство по устранению неполадок и ремонту OEM для процедур замены.

> [!missing]- Иллюстрация `ee8swkq.png` не извлечена — смотрите PDF-оригинал документа


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The cruise control select switch has two positions: SET/COAST and RESUME/ACCELERATE.
>
> The switch can be used for:
>
> - CRUISE CONTROL: SET/ACCEL and RESUME/COAST
> - PTO: INCREMENT/DECREMENT
> - IDLE: INCREMENT/DECREMENT
> - ROAD SPEED GOVERNOR: INCREMENT/DECREMENT
> - DIAGNOSTIC FAULT CODE: INCREMENT/DECREMENT
>
> For additional information, see Section F.
>
> The operator can set the vehicle cruising speed when the switch is in the SET/COAST position. The SET/COAST position can also be used to reduce the vehicle cruising speed. Hold the switch in the SET/COAST position and the vehicle will coast down to a lower speed. When the select switch is released, the cruising speed will be reset.
>
> **Note · Примечание**
> Some OEMs have switches labeled SET/ACCEL and RESUME/COAST.
>
> The operator can resume cruise control, after clutching or braking, by moving the switch to RESUME/ACCELERATE. The vehicle speed will return to the last set mph.
>
> The RESUME/ACCELERATE position can also be used to increase the vehicle cruising speed. Hold the select switch in the RESUME/ACCELERATE position and the vehicle will increase in speed. When the switch is released, the cruising speed will be reset.
>
> The cruise control select switch circuit is the common ground, pin 14 (SET/COAST signal), pin 24 (RESUME/ACCELERATE signal), and the two-position select switch located in the vehicle.
>
> ### Resistance Check
>
> If INSITE™ is available, monitor the cruise control select switch for proper operation. If **not**, follow the troubleshooting procedures in this section.
>
> Label the wires with the location on the switch or the wire number. Remove the three electrical connectors from the switch.
>
> Adjust the multimeter to measure resistance.
>
> Touch one multimeter probe to the center terminal of the switch.
>
> Touch the other multimeter probe to the top terminal of the switch.
>
> Hold the switch in the SET/COAST position. The multimeter **must** show an open circuit (100k ohms or more) when the switch is held in the SET/COAST position and after it is released. If the circuit is **not** open, the switch has failed. Refer to the OEM troubleshooting and repair manual for replacement procedures.
>
> Hold the switch in the RESUME/ACCELERATE position. The multimeter **must** show a closed circuit (10 ohms or less) when the switch is held in the RESUME/ACCELERATE position.
>
> When the switch is released, the multimeter **must** show an open circuit (100k ohms or more). If the multimeter does **not** show the correct values in either test, the switch has failed. Refer to the OEM troubleshooting and repair manual for replacement procedures.
>
> If the resistance value is correct, the switch **must** still be checked for a short circuit to ground.
>
> Touch one multimeter probe to the center terminal of the switch. Touch the other multimeter probe to the bottom terminal of the switch.
>
> Hold the switch in the SET/COAST position. The multimeter **must** show a closed circuit (10 ohms or less) while the switch is held on to the SET/COAST position.
>
> When the switch is released, the multimeter **must** show an open circuit (100k ohms or more). If the multimeter does **not** show the correct values in either test, the switch has failed. Refer to the OEM troubleshooting and repair manual for replacement procedures.
>
> Move the switch to the RESUME/ACCELERATE position. The multimeter **must** show an open circuit (100k ohms or more) when the switch is held on and when it is released. If the circuit is **not** open, the switch has failed. Refer to the OEM troubleshooting and repair manual for replacement procedures.
>
> ### Check for Short Circuit to Ground
>
> Adjust the multimeter to measure resistance.
>
> Touch one multimeter probe to the top terminal of the switch. Touch the other multimeter probe to the chassis ground. Move the switch to the SET/COAST position then to the RESUME/ACCELERATE position. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more) when the switch is in all positions. If the circuit is **not** open, the switch has failed. Refer to the OEM troubleshooting and repair manual for replacement procedures.
>
> Touch one multimeter probe to the bottom terminal of the switch. Touch the other multimeter probe to chassis ground. Move the switch to the RESUME/ACCELERATE position, then to the SET/COAST position. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more) when the switch is in all positions. If the circuit is **not** open, the switch has failed. Refer to the OEM troubleshooting and repair manual for replacement procedures.
