---
aliases:
  - "Электронный блок управления двигателем"
type: "Процедура"
doc: "82-019-031"
title_en: "Engine Control Module"
title_ru: "Электронный блок управления двигателем"
modified: "2024-09-24"
engines:
  - "35354607"
  - "35373113"
  - "41343322"
  - "41370103"
  - "71156161"
families:
  - "NT/NTA855 · ISM/QSM11"
  - "QSM11"
manuals:
  - "3666266"
  - "3666322"
figures: 10
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-031.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-031.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "двигатель/QSM11"
  - "группа/82"
  - "перевод/машинный"
---

# Engine Control Module
**Электронный блок управления двигателем**

> [!abstract] Процедура · `82-019-031`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** NT/NTA855 · ISM/QSM11, QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]], [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 19 - Electronic Controls - Group 19 · Section 19 - Electronic Engine Controls · Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2024-09-24
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-031.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-031.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Первичная проверка

Включите переключатель зажигания в положение Включения при мониторинге неисправных огней. Неисправность лампы **должны** освещаться в течение 2 - 3 секунд.

Если лампы не освещаются, проверьте выгоревшие лампы.

![[gp8swkb.png]]

Переведите замок зажигания в положение OFF.

Подключите электронный инструмент к шине данных CAN транспортного средства.

Переведите замок зажигания в положение ON.

Выберите режим монитора на инструменте электронного сервиса. Электронная система обслуживания должна быть в состоянии общаться с ECM. Если ECM не будет общаться с инструментами обслуживания, см. Ошибка связи - Электронное инструментальное средство обслуживания или дерево симптомов устройства управления.

![[19c00691.png]]

### Снятие

> [!warning] ОСТОРОЖНО
> Записывайте все программируемые параметры, функции и информацию о калибровке со старого ECM, прежде чем отсоединять разъёмы жгута проводов. Эта информация будет необходима для программирования нового ECM.

См. руководство INSITETM в разделе «Сохранить как шаблон» для получения информации о том, как в электронном виде сохранить и восстановить параметры ECM.

Отсоедините исполнительный механизм, датчик и OEM-разъемы проводов от ECM, если они уже удалены.

![[17c00003.png]]

Удалите метрические болты, которые обеспечивают ECM, на охлаждающую пластину на блоке двигателя.

Удалите ECM из охлаждающей пластины.

![[19200336.png]]

### Установка

Убедитесь, что звездная шайба находится на месте верхнего левого монтажного отверстия ECM.

Звездная шайба должна быть свободна от трещин или повреждений, которые предотвратят правильное наземное соединение с блоком двигателя.

![[19c01035.png]]

> [!warning] ОСТОРОЖНО
> Не рисуйте заднюю сторону ECM. Убедитесь, что между ECM и блоком двигателя нет смазки или грязи.

Установите новый ECM на охлаждающую пластину.

Затяните болты.

> [!tip] Момент затяжки
> 20 Н·м [177 фунт-дюйм]

![[17c00065.png]]

> [!warning] ОСТОРОЖНО
> Не выдувайте сжатый воздух в порты или разъемы ECM. Сжатый воздух может содержать влагу из-за конденсации.

Используйте быстросушливый электрический контактный очиститель, номер детали 3824510, для удаления всей грязи и влаги из портов разъемов ECM и разъёмов проводной упряжки.

![[19900518.png]]

> [!warning] ОСТОРОЖНО
> Используйте только рекомендованную Cummins смазку DS-ES, номер детали 3822934. Другие смазочные материалы, такие как моторное масло или смазка, в разъемах могут вызвать повреждение ECM, плохую производительность двигателя или преждевременный износ разъема.

Нанесите тонкое покрытие смазки на носовой части разъемов.

![[19900606.png]]

Распространяйте смазку по носу, чтобы она проникала в каждое отверстие штифта и смазывала контакты.

Смазка не должна быть видна на поверхности носа.

![[19900520.png]]

Подключите исполнительный механизм, датчик и OEM-проводку к портам ECM.

Затягивайте болты разъема к ECM.

> [!tip] Момент затяжки
> 2.8 Н·м [25 фунт-дюйм]

> [!note] Примечание
> При замене ECM необходимо откалибрование нового ECM. См. процедуру[[105-019-032 — Engine Control Module Calibration Code|См. процедуру 019-032]].

![[19200336.png]]


> [!quote]- Original (English) · английский оригинал
> ### Initial Check
>
> Turn the keyswitch to the ON position while monitoring the fault lamps. The fault lamps **must** illuminate for 2 to 3 seconds.
>
> If lamps do **not** illuminate, check for burned-out bulbs.
>
> Turn the keyswitch to the OFF position.
>
> Connect an electronic service tool to the vehicle datalink.
>
> Turn the keyswitch to the ON position.
>
> Select the monitor mode on the electronic service tool. The electronic service tool **must** be able to communicate with ECM. If the ECM will **not** communicate with the service tool, see the Communication Error - Electronic Service Tool or Control Device symptom tree.
>
> ### Remove
>
> **CAUTION · Осторожно**
> Record all programmable parameters, features, and calibration information from the old ECM before disconnecting the harness connectors. This information will be needed to program the new ECM.
>
> See the INSITE™ Manual under 'Save as a Template' for information on how to electronically save and restore ECM parameters.
>
> Disconnect the actuator, sensor, and OEM harness connectors from the ECM, if they are **not** already removed.
>
> Remove the metric capscrews that secure the ECM to the cooling plate on the engine block.
>
> Remove the ECM from the cooling plate.
>
> ### Install
>
> Make certain that the star washer is in place on the ECM upper-left mounting hole.
>
> The star washer **must** be free of cracks or damage that will prevent a proper ground connection to the engine block.
>
> **CAUTION · Осторожно**
> Do not paint the backside of the ECM. Make sure no grease or dirt is between the ECM and the engine block.
>
> Install the new ECM to the cooling plate.
>
> Tighten the capscrews.
>
> **Момент затяжки · Torque Value**
> 20 n•m [177 in-lb]
>
> **CAUTION · Осторожно**
> Do not blow compressed air into the ECM ports or connectors. Compressed air can contain moisture due to condensation.
>
> Use quick-dry electrical contact cleaner, Part Number 3824510, to remove all dirt and moisture from the ECM connector ports and the harness connectors.
>
> **CAUTION · Осторожно**
> Use only Cummins-recommended lubricant DS-ES, Part Number 3822934. Other lubricants, such as lubricating oil or grease, in the connectors can cause ECM damage, poor engine performance, or premature connector wear.
>
> Apply a thin coating of lubricant to the nosepiece of the connectors.
>
> Spread the lubricant across the nosepiece so it enters every pin hole and lubricates the contacts.
>
> Lubricant **must not** be visible on the surface of the nose piece.
>
> Connect the actuator, sensor, and OEM harness connectors to the ECM ports.
>
> Tighten the connector capscrews to the ECM.
>
> **Момент затяжки · Torque Value**
> 2.8 n•m [25 in-lb]
>
> **Note · Примечание**
> When an ECM is replaced, the new ECM **must** be calibrated. Refer to Procedure [[105-019-032 — Engine Control Module Calibration Code|Refer to Procedure 019-032]].
