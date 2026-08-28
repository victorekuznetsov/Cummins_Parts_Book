---
aliases:
  - "Электронный блок управления двигателем"
type: "Процедура"
doc: "01-019-031"
title_en: "Engine Control Module"
title_ru: "Электронный блок управления двигателем"
modified: "2015-10-14"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 7
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-031.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-031.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Engine Control Module
**Электронный блок управления двигателем**

> [!abstract] Процедура · `01-019-031`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section 19 - Electronic Controls · Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2015-10-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-031.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-031.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Первичная проверка

Включите Run/Stop переключатель в положение Run при мониторинге неисправностей ламп. Неисправные лампы должны освещаться в течение 2-3 секунд.

Если лампы не освещаются, проверьте выгоревшие лампы.

![[19802542.png]]

Переключатель Run/Stop переключается в положение Stop.

Подключите электронный инструмент к шине данных CAN.

Выберите режим монитора на инструменте электронного сервиса. Электронная сервисная оснастка **должна** иметь возможность связи с модулем управления двигателем (ECM). Если ECM будет **не** общаться с инструментами обслуживания, обратитесь к ошибке связи - электронному инструменту обслуживания или дереву симптомов устройства управления.

![[19800902.png]]

### Снятие

Записывайте все программируемые параметры, функции и информацию о калибровке со старого ECM, прежде чем отсоединять разъёмы жгута проводов. Эта информация будет необходима для программирования нового ECM. См. руководство INPOWERTM под заголовком «Сохранить как шаблон» для получения информации о том, как сохранить и восстановить эти параметры ECM в электронном виде.

Отсоедините разъемы удлинительной проводов и разъемы управляющей проводов генератора от ECM, если они **не** уже удалены.

![[19802544.png]]

Удалите болты, которые удерживают ECM, в его установленное местоположение.

См. информацию об услугах производителя оборудования для установки местоположения ECM.

![[19802545.png]]

### Установка

**Не рисуйте** * Убедитесь, что между ECM и монтажной поверхностью нет смазки или грязи.

Установите новый ECM.

Установите и затяните крепежные болты.

> [!tip] Момент затяжки
> 20 Н·м [15 фунт-фут]

![[19802545.png]]

> [!warning] ОСТОРОЖНО
> Не выдувайте сжатый воздух в порты или разъемы ECM. Сжатый воздух может содержать влагу, которая может повредить компоненты.

Используйте быстросушливый электрический контактный очиститель, номер детали 3824510, для удаления всей грязи и влаги из портов разъемов ECM и разъёмов проводной упряжки.

> [!missing]- Иллюстрация `19802490.png` не извлечена — смотрите PDF-оригинал документа

Подключите разъемы удлинительной проводов и разъемы управляющей проводов генератора к ECM. Затягивайте болты разъема к ECM.

> [!tip] Момент затяжки
> 2.8 Н·м [25 фунт-дюйм]

> [!note] Примечание
> Не делайте крутящего момента, так как может произойти повреждение разъема.

При замене ECM необходимо откалибрование нового ECM *.[[01-019-032 — ECM Calibration Code|См. процедуру 019-032]].

![[19802544.png]]


> [!quote]- Original (English) · английский оригинал
> ### Initial Check
>
> Turn the Run/Stop switch to the Run position while monitoring the fault lamps. The fault lamps **must** illuminate for 2 to 3seconds.
>
> If lamps do **not** illuminate, check for burned-out bulbs.
>
> Turn the Run/Stop switch to the Stop position.
>
> Connect an electronic service tool to the data link.
>
> Select the monitor mode on the electronic service tool. The electronic service tool **must** be able to communicate with the engine control module (ECM). If the ECM will **not** communicate with the service tool, refer to the Communication Error - Electronic Service Tool or Control Device symptom tree.
>
> ### Remove
>
> Record all programmable parameters, features, and calibration information from the old ECM before disconnecting the harness connectors. This information will be needed to program the new ECM. Refer to the INPOWER™ manual under “Save as a Template” for information on how to save and restore these ECM parameters electronically.
>
> Disconnect the extension harness connectors and the generator control harness connectors from the ECM, if they are **not** already removed.
>
> Remove the capscrews that hold the ECM to its mounted location.
>
> See the equipment manufacturer service information for mounting location of the ECM.
>
> ### Install
>
> Do **not** paint the ECM. Make sure no grease or dirt is between the ECM and the mounting surface.
>
> Install the new ECM.
>
> Install and tighten the mounting capscrews.
>
> **Момент затяжки · Torque Value**
> 20 n•m [15 ft-lb]
>
> **CAUTION · Осторожно**
> Do not blow compressed air into the ECM ports or connectors. Compressed air can contain moisture that may damage the components.
>
> Use quick-dry electrical contact cleaner, Part Number 3824510, to remove all dirt and moisture from the ECM connector ports and the harness connectors.
>
> Connect the extension harness connectors and generator control harness connectors to the ECM. Tighten the connector capscrews to the ECM.
>
> **Момент затяжки · Torque Value**
> 2.8 n•m [25 in-lb]
>
> **Note · Примечание**
> Do **not** over-torque as connector damage can occur.
>
> When an ECM is replaced, the new ECM **must** be calibrated. [[01-019-032 — ECM Calibration Code|Refer to Procedure 019-032]].
