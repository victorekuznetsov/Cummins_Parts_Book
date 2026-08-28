---
aliases:
  - "Выключатель регулировки холостого хода"
type: "Процедура"
doc: "99-019-052"
title_en: "Idle Adjust Switch"
title_ru: "Выключатель регулировки холостого хода"
modified: "2015-06-29"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "37292556"
  - "37295879"
  - "41343322"
  - "41370103"
  - "85017333"
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
  - "NT/NTA855 · ISM/QSM11"
  - "QSK23"
  - "QSK60"
  - "QST30"
manuals:
  - "3666113"
  - "3666214"
  - "3666266"
  - "4021442"
figures: 12
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-052.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-052.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "двигатель/NT/NTA855"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "двигатель/QST30"
  - "группа/99"
  - "перевод/машинный"
---

# Idle Adjust Switch
**Выключатель регулировки холостого хода**

> [!abstract] Процедура · `99-019-052`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]], [[85017333 — QSK23 CM500 CPL 2858|85017333]], [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3, NT/NTA855 · ISM/QSM11, QSK23, QSK60, QST30
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]], [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]], [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]], [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section 19 - Electronic Engine Controls · Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2015-06-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-052.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-052.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Функция регулировки холостого хода является частью многофункционального коммутатора круиз-контроля / резюме. Перемещение переключателя в заданное положение увеличивает низкую скорость холостого хода, а перемещение переключателя в положение резюме уменьшает низкую скорость холостого хода.

![[19c00894.png]]

В зависимости от того, как настроен переключатель, перемещение переключателя в одном направлении увеличит низкую скорость холостого хода.

![[19c00895.png]]

Нажмите диагностический переключатель на положение ON или установите шортинг-розетку. После того, как первый активный код неисправности вспыхнул, нажмите на кнопку положительного (+) переключения настройки холостого хода, чтобы перейти к следующему активному коду неисправности. Нажмите переключатель снова, пока не будут записаны все активные коды неисправностей.

![[19c00896.png]]

Схема переключателя регулирования холостого хода состоит из сигнала приращения холостого хода/диагностики, сигнала принижения холостого хода/диагностики, обратного провода и двухпозиционного переключателя, расположенного в транспортном средстве.

![[19c01180.png]]

### Проверка сопротивления

Если доступна электронная инструментальная система обслуживания, следите за выключателем настройки холостого хода для правильной работы. Если **не,** следуйте процедурам устранения неполадок в этом разделе.

Удалите три электрических разъема из коммутатора. Нанесите на провода метки с указанием местоположения переключателя и названия схемы.

![[19c00898.png]]

Прикоснитесь одним щупом мультиметра к центральному терминалу переключателя.

Прикоснитесь к другому щупу к терминалу сигнала коммутатора круиз-контроля / PTO resume / Accelerate switch.

![[ee8swkn.png]]

Держите выключатель регулирования холостого хода в положительном (+) положении приращения. Мультиметр **должен** показывать открытую схему (100к Ом или более), когда переключатель удерживается в положительном (+) положении приращения и после его выпуска. Если схема не открыта, выключатель не работает.

См. руководство по устранению неполадок и ремонту OEM для процедур замены.

![[ee8swkz.png]]

Держите переключатель в отрицательном (-) положении декремента. Мультиметр **должен** показывать замкнутую цепь (10 Ом или меньше), когда переключатель удерживается в отрицательном (-) положении декремента.

Когда выключатель выпущен, он должен показывать открытую схему (100k Ом или более). Если мультиметр показывает **не** правильные значения, переключатель не работает.

См. руководство по устранению неполадок и ремонту OEM для процедур замены.

![[ee8swk01.png]]

Переместить электрический привод от терминала сигнала коммутатора круиз-контроля / PTO resume / Accelerate на терминал сигнала коммутатора круиз-контроля / PTO set / Coastt.

Держите выключатель регулирования холостого хода в положительном (+) положении приращения. Мультиметр **должен** показывать замкнутую цепь (10 Ом или меньше), в то время как переключатель удерживается в положительном (+) положении приращения.

Когда выключатель выпущен, мультиметр **должен** показать открытую схему (100k Ом или более). Если мультиметр показывает **не** правильные значения, переключатель не работает.

См. руководство по устранению неполадок и ремонту OEM для процедур замены.

![[ee8swk03.png]]

Переместить переключатель регулировки холостого хода в положение отрицательного (-) декремента. Мультиметр **должен** показывать открытую схему (100км и более), когда переключатель удерживается в отрицательном (-) положении декремента и когда он высвобождается. Если схема не открыта, выключатель не работает.

См. руководство по устранению неполадок и ремонту OEM для процедур замены.

Если значение сопротивления правильное, переключатель должен быть проверен на короткое замыкание на землю.

![[ee8swk04.png]]

### Проверка на замыкание на массу

Прикоснитесь к одному многометровому щупу, чтобы установить PTO круиз-контроля / поперечный выключатель сигнала выключателя и коснитесь другого многометрового щупа до земли шасси. Переместите переключатель настройки холостого хода в положение отрицательного (-) декремента, затем в положение положительного (+) приращения. Измерьте сопротивление. Мультиметр **должен** показывать открытую схему (100к Ом или более), когда переключатель находится во всех положениях. Если схема не открыта, выключатель не работает. См. руководство по устранению неполадок и ремонту OEM для процедур замены.

![[ee8swk05.png]]

Проверьте короткое замыкание на землю. Удалите многометровый щуп из терминала сигнала круиз-контроля / PTO set / Coast switch и прикоснитесь к нему в терминал сигнала круиз-контроля / PTO resume / Accelerate switch. Держите другой многометровый касающийся земли шасси. Переместите переключатель в положение положительного (+) приращения, затем в положение отрицательного (-) приращения. Измерьте сопротивление. Мультиметр **должен** показывать открытую схему (100к Ом или более), когда переключатель находится во всех положениях. Если схема **не открыта, выключатель не работает. См. руководство по устранению неполадок и ремонту OEM для процедур замены. Если выключатель проходит все предыдущие проверки, схема переключателя** должна быть проверена.

![[ee8swk02.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The idle adjustment feature is a part of the cruise control set/resume multi-functionality switch. Moving the switch to the set position increases the low idle speed and moving the switch to the resume position decreases the low idle speed.
>
> Depending on how the switch is configured, moving the switch in one direction will increase the low idle speed.
>
> Push the diagnostic switch to the ON position or install the shorting plug. After the first active fault code has flashed out, push the idle adjust switch positive (+) up to advance to the next active fault code. Push the switch again until all of the active fault codes have been recorded.
>
> The idle adjust switch circuit consists of the idle/diagnostics increment signal, the idle/diagnostics decrement signal, the return wire, and the two-position switch located in the vehicle.
>
> ### Resistance Check
>
> If an electronic service tool is available, monitor the idle adjust switch for proper operation. If **not,** follow the troubleshooting procedures in this section.
>
> Remove the three electrical connectors from the switch. Label the wires with the switch location and the circuit name.
>
> Touch one probe of the multimeter to the center terminal of the switch.
>
> Touch the other probe to the cruise control/PTO resume/accelerate switch signal terminal of the switch.
>
> Hold the idle adjust switch in the positive (+) increment position. The multimeter **must** show an open circuit (100k ohms or more) when the switch is held in the positive (+) increment position and after it is released. If the circuit is **not** open, the switch has failed.
>
> Refer to the OEM troubleshooting and repair manual for the replacement procedures.
>
> Hold the switch in the negative (-) decrement position. The multimeter **must** show a closed circuit (10 ohms or less) when the switch is held in the negative (-) decrement position.
>
> When the switch is released, it **must** show an open circuit (100k ohms or more). If the multimeter does **not** show the correct values, the switch has failed.
>
> Refer to the OEM troubleshooting and repair manual for the replacement procedures.
>
> Move the electrical lead from the cruise control/PTO resume/accelerate switch signal terminal to the cruise control/PTO set/coast switch signal terminal.
>
> Hold the idle adjust switch in the positive (+) increment position. The multimeter **must** show a closed circuit (10 ohms or less) while the switch is held in the positive (+) increment position.
>
> When the switch is released, the multimeter **must** show an open circuit (100k ohms or more). If the multimeter does **not** show the correct values, the switch has failed.
>
> Refer to the OEM troubleshooting and repair manual for the replacement procedures.
>
> Move the idle adjust switch to the negative (-) decrement position. The multimeter **must** show an open circuit (100k ohms or more) when the switch is held in the negative (-) decrement position and when it is released. If the circuit is **not** open, the switch has failed.
>
> Refer to the OEM troubleshooting and repair manual for the replacement procedures.
>
> If the resistance value is correct, the switch **must** still be checked for a short circuit to ground.
>
> ### Check for Short Circuit to Ground
>
> Touch one multimeter probe to the cruise control PTO set/coast switch signal terminal of the switch and touch the other multimeter probe to chassis ground. Move the idle adjust switch to the negative (-) decrement position then to the positive (+) increment position. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more) when the switch is in all positions. If the circuit is **not** open, the switch has failed. Refer to the OEM troubleshooting and repair manual for the replacement procedures.
>
> Check for a short circuit to ground. Remove the multimeter probe from the cruise control/PTO set/coast switch signal terminal and touch it to the cruise control/PTO resume/accelerate switch signal terminal of the switch. Keep the other multimeter touching chassis ground. Move the switch to the positive (+) increment position then to the negative (-) decrement position. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more) when the switch is in all positions. If the circuit is **not** open, the switch has failed. Refer to the OEM troubleshooting and repair manual for the replacement procedures. If the switch passes all of the previous checks, the switch circuit **must** be checked.
