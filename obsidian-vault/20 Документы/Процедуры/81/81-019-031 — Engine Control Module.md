---
aliases:
  - "Электронный блок управления двигателем"
type: "Процедура"
doc: "81-019-031"
title_en: "Engine Control Module"
title_ru: "Электронный блок управления двигателем"
modified: "2014-04-17"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
manuals:
  - "3666410"
figures: 7
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-019-031.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-019-031.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/81"
  - "перевод/машинный"
---

# Engine Control Module
**Электронный блок управления двигателем**

> [!abstract] Процедура · `81-019-031`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[3666410 — QSK45 and QSK60 CENSE™ Electronic Control System Troubleshooting and Repair Manual|3666410]]
> **Секции:** Section 19 - Electronic Controls · Section 19 - Electronic Engine Controls · Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2014-04-17
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-019-031.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-019-031.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Снятие

> [!warning] ОСТОРОЖНО
> Записывайте все программируемые параметры, функции и информацию о калибровке со старого ECM, прежде чем отсоединять разъёмы жгута проводов. Эта информация будет необходима для программирования нового ECM.

Справка об инструменте электронного обслуживания INSITETM для Руководства пользователя CENSETM под названием «Сохранить как шаблон» для получения информации о том, как в электронном виде сохранить и восстановить параметры ECM.

Отключите 40-контактные разъемы модуля управления двигателем A и B (ECM).

![[19800828.png]]

> [!note] Примечание
> Перед снятием болтов обратите внимание на положения кольцевых оконечностей под болтами, и установите их в тех же положениях, из которых они были удалены.

Удалите шесть болтов, которые обеспечивают ECM, на монтажную пластину.

Удалите ECM с монтажной пластины.

![[19800829.png]]

### Установка

> [!warning] ОСТОРОЖНО
> Не выдувайте сжатый воздух в порты или разъемы ECM. Сжатый воздух может содержать влагу из-за конденсации.

Используйте быстросушливый электрический контактный очиститель, номер детали 3824510, для удаления всей грязи и влаги из портов разъемов ECM и разъёмов проводной упряжки.

![[19800830.png]]

> [!warning] ОСТОРОЖНО
> Убедитесь, что между ECM и монтажной пластиной нет смазки или грязи.

> [!note] Примечание
> Установите кольцевые терминалы под болтами в тех же положениях, из которых они были сняты.

Установите новый ECM. Затяните шесть болтов.

> [!tip] Момент затяжки
> 8 Н·м [72 фунт-дюйм]

![[19800831.png]]

> [!warning] ОСТОРОЖНО
> Используйте только Cummins, Inc., рекомендованную смазку DS-ES, номер детали. 3822934. Другие смазочные материалы, такие как моторное масло или смазка, в разъеме могут вызвать повреждение ECM, плохую производительность двигателя или преждевременный износ разъема.

Нанесите тонкое покрытие смазки на поверхность 40-контактных разъемов DeutschTM.

![[19400297.png]]

Распространяйте смазку по поверхности 40-контактных разъемов DeutschTM. Убедитесь, что смазка попадает в каждую пин-полость разъема.

Смазка не должна быть видна на поверхности носового платка.

![[19400298.png]]

Включить 40-контактные разъёмы DeutschTM в сосуды ECM. Тщательно выровните разъемы направляющего в ECM и вставьте ECM и разъем.

Тщательно выровняйте и запустите соединительные крепежные болты вручную. Используйте крутящий момент в дюйме, номер детали 3376592, чтобы затянуть болты.

Используйте крутящий момент в дюйме, номер детали 3376592, с 4 мм \[5/32 в \] шестиглавый адаптер для затягивания разъема винта.

> [!tip] Момент затяжки
> 2.8 Н·м [25 фунт-дюйм]

> [!note] Примечание
> Не делайте крутящего момента, так как может произойти повреждение разъема.

> [!note] Примечание
> При замене ECM необходимо откалибрование нового ECM. Используйте инструмент для электронных услуг INSITETM для CENSETM с испытательным стендом верхнего жгута проводов, Номер детали 3163064 или кабель шины данных CAN, Номер детали 3885817, для калибровки ECM.

![[19400299.png]]


> [!quote]- Original (English) · английский оригинал
> ### Remove
>
> **CAUTION · Осторожно**
> Record all programmable parameters, features, and calibration information from the old ECM before disconnecting the harness connectors. This information will be needed to program the new ECM.
>
> Reference INSITE™ electronic service tool for CENSE™ User's Manual under “Save as a Template” for information on how to electronically save and restore ECM parameters.
>
> Disconnect the 40-pin A and B engine control module (ECM) connectors.
>
> **Note · Примечание**
> Before removing the capscrews, note the positions of the ring terminals under the capscrews, and install them at the same positions from which they were removed.
>
> Remove the six capscrews that secure the ECM to the mounting plate.
>
> Remove the ECM from the mounting plate.
>
> ### Install
>
> **CAUTION · Осторожно**
> Do not blow compressed air into the ECM ports or connectors. Compressed air can contain moisture due to condensation.
>
> Use quick-dry electrical contact cleaner, Part Number 3824510, to remove all dirt and moisture from the ECM connector ports and the harness connectors.
>
> **CAUTION · Осторожно**
> Make sure there is no grease or dirt between the ECM and the mounting plate.
>
> **Note · Примечание**
> Install the ring terminals under the capscrews at the same positions from which they were removed.
>
> Install the new ECM. Tighten the six capscrews.
>
> **Момент затяжки · Torque Value**
> 8 n•m [72 in-lb]
>
> **CAUTION · Осторожно**
> Use only Cummins, Inc.,-recommended lubricant DS-ES, Part No. 3822934. Other lubricants, such as lubricating oil or grease, in the connector can cause ECM damage, poor engine performance, or premature connector wear.
>
> Apply a thin coating of lubricant to the face of the 40-pin Deutsch™ connectors.
>
> Spread the lubricant across the face of the 40-pin Deutsch™ connectors. Make sure that the lubricant gets into every pin cavity of the connector.
>
> Lubricant **must not** be visible on the surface of the nosepiece.
>
> Insert the 40-pin Deutsch™ connectors into the ECM receptacles. Carefully align the connector guide slots in the ECM, and insert the ECM and the connector.
>
> Carefully align and start the connector mounting capscrews by hand. Use an inch-pound torque wrench, Part Number 3376592, to tighten the capscrews.
>
> Use an inch-pound torque wrench, Part Number 3376592, with 4 mm \[5/32 in\] hex head adapter to tighten the connector jackscrew.
>
> **Момент затяжки · Torque Value**
> 2.8 n•m [25 in-lb]
>
> **Note · Примечание**
> Do **not** over-torque as connector damage can occur.
>
> **Note · Примечание**
> When an ECM is replaced, the new ECM **must** be calibrated. Use INSITE™ electronic service tool for CENSE™ with bench top harness, Part Number 3163064, or data link cable, Part Number 3885817, to calibrate the ECM.
