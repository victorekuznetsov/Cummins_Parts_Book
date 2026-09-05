---
aliases:
  - "Выключатель ступени моторного тормоза"
type: "Процедура"
doc: "82-019-036"
title_en: "Engine Brake Level Switch"
title_ru: "Выключатель ступени моторного тормоза"
modified: "2002-06-03"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 7
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-036.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-036.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Engine Brake Level Switch
**Выключатель ступени моторного тормоза**

> [!abstract] Процедура · `82-019-036`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2002-06-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-036.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-036.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Переключатель SELECTOR определяет, какой тормоз двигателя должен быть активирован. Переключатель ON/OFF тормоза двигателя должен быть включен, чтобы активировать тормозную систему двигателя.

![[19200290.png]]

### Проверка сопротивления

Если INSITETM доступен, проверьте переключатель тормозов двигателя на предмет правильной работы. Если **не**, следуйте процедурам устранения неполадок в этом разделе.

Пометьте провода с местоположением на выключателе или номером провода. Отсоедините три электрических разъема от переключателя.

![[19200297.png]]

Настройте мультиметр для измерения сопротивления.

Прикоснитесь к одному многометровому щупу к центральному терминалу переключателя. Прикоснитесь к другому многометровому щупу к верхнему терминалу переключателя, а затем к нижнему терминалу переключателя на каждом из следующих шагов.

![[19200298.png]]

Переместите селектор тормозов на No. 1 позиция. Мультиметр **должен** показывать замкнутую цепь на одном терминале, либо на верхнем терминале, либо на нижнем терминале (10 Ом или меньше), когда переключатель находится в точке No. 1 позиция. Если цепь **не** закрыта или если верхний и нижний терминалы показывают непрерывность, переключатель не работает.

См. руководство по устранению неполадок и ремонту OEM для процедур замены.

![[19200298.png]]

Снова прикоснитесь к верхнему терминалу. Переместите селектор тормозов на No. 2 позиции. Мультиметр **должен** показывать открытую схему (100к Ом или более), когда выключатель находится в No. 2 позиции.

Переведите щуп на нижний терминал. Мультиметр **должен** показать обрыв цепи (100 кОм и более). Если мультиметр показывает правильные значения в обоих тестах, переключатель не работает. См. руководство по устранению неполадок и ремонту OEM для процедур замены.

![[19200299.png]]

### Проверка на замыкание на массу

Настройте мультиметр для измерения сопротивления.

Прикоснитесь к одному многометровому щупу к верхнему терминалу переключателя. Прикоснитесь к другому многометровому щупу к земле шасси. Переключай на "Нет". 1 позиция, затем на позицию «нет». 2 позиции. Измерьте сопротивление. Мультиметр **должен** показывать открытую схему (100к Ом или более), когда переключатель находится во всех положениях. Если схема не открыта, выключатель не работает.

См. руководство по устранению неполадок и ремонту OEM для процедур замены.

![[19200300.png]]

Прикоснитесь одним многометровым щупом к нижнему терминалу переключателя. Прикоснитесь к другому многометровому щупу на земле шасси. Переключай на "Нет". 2 место, затем на "Нет". 1 позиция. Измерьте сопротивление. Мультиметр **должен** показывать открытую схему (100к Ом или более), когда переключатель находится во всех положениях. Если схема не открыта, выключатель не работает.

См. руководство по устранению неполадок и ремонту OEM для процедур замены.

![[19200301.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The engine brake SELECTOR switch determines which engine brake should be activated. The engine brake ON/OFF switch needs to be turned ON to activate the engine brake system.
>
> ### Resistance Check
>
> If INSITE™ is available, monitor the engine brake selector switch for proper operation. If **not**, follow the troubleshooting procedures for this section.
>
> Label the wires with the location on the switch or the wire number. Disconnect the three electrical connectors from the switch.
>
> Adjust the multimeter to measure resistance.
>
> Touch one multimeter probe to the center terminal of the switch. Touch the other multimeter probe to the top terminal of the switch and then to the bottom terminal of the switch in each of the following steps.
>
> Move the brake selector switch to the No. 1 position. The multimeter **must** show a closed circuit on one terminal, at either the top terminal or the bottom terminal (10 ohms or less) when the switch is in the No. 1 position. If the circuit is **not** closed or if both the top and the bottom terminals show continuity, the switch has failed.
>
> Refer to the OEM troubleshooting and repair manual for replacement procedures.
>
> Touch the probe to the top terminal again. Move the brake selector switch to the No. 2 position. The multimeter **must** show an open circuit (100k ohms or more) when the switch is in the No. 2 position.
>
> Move the probe to the bottom terminal. The multimeter **must** show an open circuit (100k ohms or more). If the multimeter does **not** show the correct values in both tests, the switch has failed. Refer to the OEM troubleshooting and repair manual for replacement procedures.
>
> ### Check for Short Circuit to Ground
>
> Adjust the multimeter to measure resistance.
>
> Touch one multimeter probe to the top terminal of the switch. Touch the other multimeter probe to the chassis ground. Move the switch to the No. 1 position, then to the No. 2 position. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more) when the switch is in all positions. If the circuit is **not** open, the switch has failed.
>
> Refer to the OEM troubleshooting and repair manual for replacement procedures.
>
> Touch one multimeter probe to the bottom terminal of the switch. Touch the other multimeter probe to chassis ground. Move the switch to the No. 2 position, then to the No. 1 position. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more) when the switch is in all positions. If the circuit is **not** open, the switch has failed.
>
> Refer to the OEM troubleshooting and repair manual for replacement procedures.
