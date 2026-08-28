---
aliases:
  - "Электронный блок управления двигателем"
type: "Процедура"
doc: "87-019-031"
title_en: "Engine Control Module"
title_ru: "Электронный блок управления двигателем"
modified: "2024-09-20"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 7
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-031.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-031.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Engine Control Module
**Электронный блок управления двигателем**

> [!abstract] Процедура · `87-019-031`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section 19 - Electronic Controls - Group 19 · Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2024-09-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-031.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-031.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Снятие

Отключите OEM-интерфейс проводов и разъёмы жгута проводов двигателя от ECM.

> [!note] Примечание
> Записывайте все программируемые параметры, функции и калибровочную информацию из старого ECM для программирования нового ECM.

![[19900515.png]]

Удалите три болта, которые удерживают ECM на двигателе.

Удалите ЭКМ из крепежной скобки.

![[19900516.png]]

### Установка

> [!warning] ОСТОРОЖНО
> Не выдувайте сжатый воздух в порты или разъемы ECM. Сжатый воздух может содержать влагу из-за конденсации.

Используйте быстросушливый электрический контактный очиститель, номер детали 3824510, для удаления всей грязи и влаги из портов разъемов ECM и разъёмов проводной упряжки.

![[19900518.png]]

> [!note] Примечание
> Убедитесь, что между ECM и монтажной скобкой нет смазки или грязи.

Установите новый ECM на двигатель. Затяните три болта.

> [!tip] Момент затяжки
> 8 Н·м [71 фунт-дюйм]

![[19900517.png]]

> [!warning] ОСТОРОЖНО
> Используйте только рекомендованную Cummins смазку DS-ES, номер детали 3822934. Другие смазочные материалы, такие как моторное масло или смазка, в разъемах могут вызвать повреждение ECM, плохую производительность двигателя или преждевременный контактный износ разъема.

Нанесите тонкое покрытие смазки на носовой части разъема.

![[19900606.png]]

Распространяйте смазку через носовой части разъема, чтобы она проникала в каждое отверстие штифта и смазывала контакты.

Смазка не должна быть видна на поверхности носового платка.

![[19900520.png]]

Подключите OEM-разъемы и разъёмы жгута для проводов двигателя к ECM. Затягивайте болты разъема.

> [!tip] Момент затяжки
> 3 Н·м [27 фунт-дюйм]

> [!note] Примечание
> При замене ECM, новый ECM должен быть откалиброван с использованием ESDNTM (Electronic Software and Database Network).

![[19900515.png]]


> [!quote]- Original (English) · английский оригинал
> ### Remove
>
> Disconnect the OEM interface harness and engine harness connectors from the ECM.
>
> **Note · Примечание**
> Record all of the programmable parameters, features, and calibration information from the old ECM for programming the new ECM.
>
> Remove the three capscrews that hold the ECM to the engine.
>
> Remove the ECM from the mounting bracket.
>
> ### Install
>
> **CAUTION · Осторожно**
> Do not blow compressed air into the ECM ports or connectors. Compressed air can contain moisture due to condensation.
>
> Use quick-dry electrical contact cleaner, Part Number 3824510, to remove all dirt and moisture from the ECM connector ports and the harness connectors.
>
> **Note · Примечание**
> Make sure there is no grease or dirt between the ECM and the mounting bracket.
>
> Install the new ECM onto the engine. Tighten the three capscrews.
>
> **Момент затяжки · Torque Value**
> 8 n•m [71 in-lb]
>
> **CAUTION · Осторожно**
> Use only Cummins-recommended lubricant DS-ES, Part Number 3822934. Other lubricants, such as lubricating oil or grease, in the connectors can cause ECM damage, poor engine performance, or premature connector pin wear.
>
> Apply a thin coating of lubricant to the connector nosepiece.
>
> Spread the lubricant across the connector nosepiece so it enters every pin hole and lubricates the contacts.
>
> Lubricant **must not** be visible on the surface of the nosepiece.
>
> Connect the OEM and engine harness connectors to the ECM. Tighten the connector capscrews.
>
> **Момент затяжки · Torque Value**
> 3 n•m [27 in-lb]
>
> **Note · Примечание**
> When an ECM is replaced, the new ECM **must** be calibrated using ESDN™ (Electronic Software and Database Network).
