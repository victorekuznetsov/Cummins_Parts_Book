---
aliases:
  - "Электронный блок управления двигателем"
type: "Процедура"
doc: "123-019-031"
title_en: "Engine Control Module"
title_ru: "Электронный блок управления двигателем"
modified: "2014-04-17"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4022094"
figures: 6
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-019-031.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/123-019-031.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
  - "перевод/машинный"
---

# Engine Control Module
**Электронный блок управления двигателем**

> [!abstract] Процедура · `123-019-031`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section 19 - Electronic Controls
> **Даты:** изменён 2014-04-17
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-019-031.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/123-019-031.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Первичная проверка

Включите переключатель зажигания в положение Включения при мониторинге неисправных огней. Неисправность лампы **должны** освещаться в течение 2 - 3 секунд.

Если лампы не освещаются, проверьте наличие выгоревших ламп.

![[gp8swkb.png]]

Переведите замок зажигания в положение OFF.

Подключите электронный инструмент к шине данных CAN транспортного средства.

Переведите замок зажигания в положение ON.

С помощью инструментария электронного обслуживания INSITETM выберите подходящее соединение для используемой шины данных CAN и попробуйте подключиться к ECM. Электронная сервисная оснастка **должна** иметь возможность связи с модулем управления двигателем (ECM). Если ECM будет **не** общаться с инструментами обслуживания, обратитесь к ошибке связи - электронному инструменту обслуживания или дереву симптомов устройства управления.

![[19c01217.png]]

### Снятие

> [!warning] ОСТОРОЖНО
> Записывайте все программируемые параметры, функции и информацию о калибровке со старого ECM, прежде чем отсоединять разъёмы жгута проводов. Эта информация будет необходима для программирования нового ECM.

Удалите наземный ремешок ECM из ECM на морских двигателях.

Отсоедините 4-контактный разъем питания и оба 60-контактных разъема от ECM, если они уже удалены.

![[19c01218.png]]

Удалите болты, которые обеспечивают ECM, в двигатель.

![[19600713.png]]

### Установка

> [!warning] ОСТОРОЖНО
> Не рисуйте заднюю сторону ECM. Убедитесь, что между ECM и охлаждающей пластиной нет смазки или грязи. Неспособность сделать это может привести к повреждению ЭКМ.

Установите новый ECM на охлаждающую пластину.

Затяните болты.

> [!tip] Момент затяжки
> 18 Н·м [159 фунт-дюйм]

![[19600713.png]]

> [!warning] ОСТОРОЖНО
> Не выдувайте сжатый воздух в порты или разъемы ECM. Сжатый воздух может содержать влагу из-за конденсации.

> [!note] Примечание
> При замене ECM необходимо откалибрование нового ECM. См. процедуру 019-032.

Подключите наземный ремешок ECM к ECM для применения в двигателях морской пехоты.

Используйте быстросушливый электрический контактный очиститель, Номер детали 3824510 или эквивалент, чтобы удалить всю грязь и влагу из портов разъемов ECM и разъёмов проводной ремни. Подключите все проводные разъёмы.

Подключите 4-контактный разъем питания и оба 60-контактных разъема к ECM.

Затягивайте болты разъема к ECM.

Используйте крутящий момент в дюйме, номер детали 3376592, с 4 мм \[5/32 в \] шестиглавый адаптер для затягивания разъема винта.

> [!tip] Момент затяжки
> 2.8 Н·м [25 фунт-дюйм]

> [!note] Примечание
> Не делайте -переворот разъема, как повреждение может произойти.

![[19900518.png]]


> [!quote]- Original (English) · английский оригинал
> ### Initial Check
>
> Turn the keyswitch to the ON position while monitoring the fault lamps. The fault lamps **must** illuminate for 2 to 3 seconds.
>
> If the lamps do **not** illuminate, check for burned-out bulbs.
>
> Turn the keyswitch to the OFF position.
>
> Connect an electronic service tool to the vehicle data link.
>
> Turn the keyswitch to the ON position.
>
> With INSITE™ electronic service tool, select the appropriate connection for the data link being used and attempt to connect to the ECM. The electronic service tool **must** be able to communicate with engine control module (ECM). If the ECM will **not** communicate with the service tool, refer to the Communication Error - Electronic Service Tool or Control Device symptom tree.
>
> ### Remove
>
> **CAUTION · Осторожно**
> Record all programmable parameters, features, and calibration information from the old ECM before disconnecting the harness connectors. This information will be needed to program the new ECM.
>
> Remove the ECM ground strap from the ECM on Marine engine applications.
>
> Disconnect the 4-pin power connector and both 60-pin connectors from the ECM, if they are **not** already removed.
>
> Remove the capscrews that secure the ECM to the engine.
>
> ### Install
>
> **CAUTION · Осторожно**
> Do not paint the back side of the ECM. Make sure no grease or dirt is between the ECM and the cooling plate. Failure to do so can result in ECM damage.
>
> Install the new ECM to the cooling plate.
>
> Tighten the capscrews.
>
> **Момент затяжки · Torque Value**
> 18 n•m [159 in-lb]
>
> **CAUTION · Осторожно**
> Do not blow compressed air into the ECM ports or connectors. Compressed air can contain moisture due to condensation.
>
> **Note · Примечание**
> When an ECM is replaced, the new ECM **must** be calibrated. Refer to Procedure 019-032.
>
> Connect the ECM ground strap to the ECM on Marine engine applications.
>
> Use quick-dry electrical contact cleaner, Part Number 3824510, or equivalent, to remove all dirt and moisture from the ECM connector ports and the harness connectors. Connect all harness connectors.
>
> Connect the 4-pin power connector and both 60-pin connectors to the ECM.
>
> Tighten the connector capscrews to the ECM.
>
> Use an inch-pound torque wrench, Part Number 3376592, with 4 mm \[5/32 in\] hex head adapter to tighten the connector jackscrew.
>
> **Момент затяжки · Torque Value**
> 2.8 n•m [25 in-lb]
>
> **Note · Примечание**
> Do **not** over-torque connector as damage can occur.
