---
aliases:
  - "Электронный блок управления двигателем"
type: "Процедура"
doc: "19-019-031"
title_en: "Engine Control Module"
title_ru: "Электронный блок управления двигателем"
modified: "2014-04-23"
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
figures: 7
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-031.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-031.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Engine Control Module
**Электронный блок управления двигателем**

> [!abstract] Процедура · `19-019-031`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2014-04-23
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-031.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-031.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Снятие

> [!note] Примечание
> Записывайте все программируемые параметры, функции и информацию о калибровке из старого модуля управления двигателем (ECM) для программирования нового ECM.

Отсоедините проводку интерфейса производителя исходного оборудования (OEM) от электропроводки ECM.

![[19400299.png]]

Удалите болты, которые удерживают ECM, в корпус управляющего клапана.

Удалите ECM из корпуса управляющего клапана.

![[19400294.png]]

### Установка

> [!warning] ОСТОРОЖНО
> Не выдувайте сжатый воздух в порты или разъемы ECM. Сжатый воздух может содержать влагу из-за конденсации.

Используйте быстросушливый электрический контактный очиститель, номер детали 3824510, для удаления всей грязи и влаги из портов разъемов ECM и разъёмов проводной упряжки.

![[19400296.png]]

> [!note] Примечание
> Убедитесь, что между ECM и корпусом клапана управления нет смазки или грязи.

Установите новый ECM на корпус управляющего клапана. Затяните шесть болтов.

> [!tip] Момент затяжки
> 8 Н·м [71 фунт-дюйм]

![[19400295.png]]

> [!warning] ОСТОРОЖНО
> Используйте только рекомендованную Cummins смазку DS-ES, номер детали 3822934. Другие смазочные материалы, такие как моторное масло или смазка, в разъемах могут вызвать повреждение ECM, плохую производительность двигателя или преждевременный контактный износ разъема.

Нанесите тонкое покрытие смазки на соединительный носовой кусок.

![[19400297.png]]

Распространяйте смазку через носовой части разъема, чтобы она проникала в каждое отверстие штифта и смазывала контакты.

Смазка не должна быть видна на поверхности носа.

![[19400298.png]]

Подключите OEM-разъемы и разъёмы жгута для проводов двигателя к ECM. Затягивайте болты разъема.

Используйте крутящий момент в дюйме, номер детали 3376592, с 4 мм \]5/32 в \] шестиголовый адаптер для подтягивания разъема винта.

> [!tip] Момент затяжки
> 2.8 Н·м [25 фунт-дюйм]

> [!note] Примечание
> Не делайте крутящего момента, так как может произойти повреждение разъема.

> [!note] Примечание
> При замене ECM необходимо откалибрование нового ECM. Используйте INSITETM, номер 3824801, для калибровки ECM.

См. процедуру 019-032 в разделе 19 для калибровки нового ECM.

![[19400299.png]]


> [!quote]- Original (English) · английский оригинал
> ### Remove
>
> **Note · Примечание**
> Record all of the programmable parameters, features, and calibration information from the old engine control module (ECM) for programming the new ECM.
>
> Disconnect the originl equipment manufacturer (OEM) interface harness and engine harness from the ECM.
>
> Remove the capscrews that hold the ECM to the control valve body.
>
> Remove the ECM from the control valve body.
>
> ### Install
>
> **CAUTION · Осторожно**
> Do not blow compressed air into the ECM ports or connectors. Compressed air can contain moisture due to condensation.
>
> Use quick-dry electrical contact cleaner, Part Number 3824510, to remove all dirt and moisture from the ECM connector ports and the harness connectors.
>
> **Note · Примечание**
> Make sure there is no grease or dirt between the ECM and the control valve body.
>
> Install the new ECM to the control valve body. Tighten the six capscrews.
>
> **Момент затяжки · Torque Value**
> 8 n•m [71 in-lb]
>
> **CAUTION · Осторожно**
> Use only Cummins-recommended lubricant DS-ES, Part Number 3822934. Other lubricants, such as lubricating oil or grease, in the connectors can cause ECM damage, poor engine performance, or premature connector pin wear.
>
> Apply a thin coating of lubricant to the connector nose piece.
>
> Spread the lubricant across the connector nosepiece so it enters every pin hole and lubricates the contacts.
>
> Lubricant **must not** be visible on the surface of the nose piece.
>
> Connect the OEM and engine harness connectors to the ECM. Tighten the connector capscrews.
>
> Use an inch-pound torque wrench, Part Number 3376592, with 4 mm \]5/32 in\] hex head adapter to tighten the connector jackscrew.
>
> **Момент затяжки · Torque Value**
> 2.8 n•m [25 in-lb]
>
> **Note · Примечание**
> Do **not** over-torque as connector damage can occur.
>
> **Note · Примечание**
> When an ECM is replaced, the new ECM **must** be calibrated. Use INSITE™, Part Number 3824801, to calibrate the ECM.
>
> Refer to Procedure 019-032 in Section 19 to calibrate the new ECM.
