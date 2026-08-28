---
type: "Процедура"
doc: "101-101-048"
title_en: "Engine Indicator Lamps"
modified: "2009-09-24"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
manuals:
  - "3666251"
  - "4960314"
figures: 13
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/101/101-101-048.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/101-101-048.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSX15"
  - "группа/101"
  - "перевод/машинный"
---

# Engine Indicator Lamps

> [!abstract] Процедура · `101-101-048`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Входит в руководства:** [[3666251 — Signature and ISX Operation and Maintenance Manual|3666251]], [[4960314 — ISX Owners Manual|4960314]]
> **Секции:** Section 1 - Operating Instructions
> **Даты:** изменён 2009-09-24
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/101/101-101-048.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/101-101-048.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Следующие индикаторные лампы двигателя охватывают **только **лампы, управляемые ECM двигателя. Производитель автомобиля может предоставить дополнительные индикаторные лампы. Пожалуйста, обратитесь к руководству для владельцев автомобиля для получения дополнительной информации о лампе.

1. Проверить двигатель
2. Проверить двигатель
3. После обработки дизельным фильтром твердых частиц
4. Остановить двигатель
5. После обработки выхлопной жидкости дизельного топлива
6. Выхлопная высокая температура

![[ck800wa.png]]

Работа двигателя

#### лампа с индикатором неисправности (MIL)

- Для двигателей ISX15 CM2250, оснащенных бортовой диагностикой (OBD), система контроля выбросов отслеживает и сообщает о неисправностях, которые могут привести к увеличению уровня выбросов выхлопных газов. Если система OBD обнаруживает такую неисправность, бортовая диагностическая система освещает MALFUNCTION INDICATOR LAMP (MIL), чтобы указать, что двигатель должен обслуживаться при первой доступной возможности.

> [!note] Примечание
> **Для диагностики на борту используются только сертифицированные продукты**.

ИНДИКАТОР МОЛФУНКЦИИ ЛАМП (MIL) является янтарным и может выглядеть так:

- Символ двигателя, похожий на иллюстрацию.
- Символ потока выхлопных газов с восклицательным знаком, похожим на иллюстрацию.

MALFUNCTION INDICATOR LAMP (MIL) может быть освещен вместе с любым из индикаторов двигателя. Он не используется для указания требуемого состояния защиты двигателя или технического обслуживания.

![[00c00178.png]]

Проверить лампу двигателя

Лампа CHECK ENGINE загорается, когда двигатель должен быть обслуживаем при первой доступной возможности.

Лампа CHECK ENGINE является янтарной и может выглядеть так:

- Слова «предупреждение» или «проверка» Энжин
- Символ двигателя, похожий на иллюстрацию.

Еще одна функция лампы CHECK ENGINE - мигать в течение 30 секунд при включении клавиши, чтобы указать состояние обслуживания. Эта функция мигания называется лампой MAINTENANCE. Лампа MAINTENANCE может мигать по следующим причинам:

- Требуется техническое обслуживание (если включен монитор технического обслуживания)
- Вода в топливе обнаружена
- Уровень охлаждения низкий.

![[00c00181.png]]

Остановить лампу двигателя

Лампа STOP ENGINE указывает при освещении на необходимость остановки двигателя, как только это можно сделать безопасно. Двигатель должен быть отключен до тех пор, пока двигатель не будет отремонтирован.

Для двигателей с включенной функцией защиты двигателя, если лампа STOP ENGINE начинает мигать, двигатель автоматически выключается через 30 секунд. Мгновенная лампа двигателя STOP предупреждает оператора о предстоящем отключении.

Лампа STOP ENGINE имеет красный цвет и может выглядеть так:

- Слова «стоп» или «стоп» Энжин
- Символ двигателя с восклицательной точкой в центре, похожий на иллюстрацию.
- Символ знака остановки с контуром двигателя в центре, похожий на иллюстрацию

![[00c00179.png]]

После обработки лампой фильтра дизельных частиц

Лампа ПАРТИКУЛЬТАТНЫЙ ПРИМЕНЕННЫЙ ФИЛЬТЕР указывает при освещении или мигании, что фильтр для твердых частиц дизельного топлива после обработки требует регенерации.

Освещенная лампа накаливания указывает на то, что фильтр для дизельных частиц после обработки должен быть восстановлен при следующей возможной возможности. Этого можно достичь путем:

- Изменение рабочего цикла за счет увеличения паразитов двигателя, включая активацию огня вождения автомобиля и фар, активацию вентилятора двигателя (если оборудован переключатель приборной панели), активацию кондиционера (или дефростера), вождение и поддержание скорости дороги 50 миль в час или более до тех пор, пока не отключится лампа AFTERTREATMENT DIESEL PARTICULATE FILTER. Продолжайте движение в течение дополнительных 20 минут, чтобы обеспечить адекватную регенерацию фильтра с твердыми частицами дизельного топлива после обработки.
- Выполняет стационарную регенерацию. Следуйте инструкциям в Уникальных эксплуатационных характеристиках двигателя с последующей обработкой, в разделе 1.

> [!note] Примечание
> Стационарная регенерация считается обычной практикой технического обслуживания и не покрывается компанией Cummins Inc. Гарантия.

![[11c00108.png]]

Вспышка на фильтре с дополнительными элементами указывает на то, что фильтр для твердых частиц дизельного топлива после обработки должен быть восстановлен при следующей возможной возможности. Мощность двигателя может быть уменьшена автоматически.

При мигании этой лампы оператор должен:

- Измените рабочий цикл, увеличив паразитирование двигателя, включая активацию вентилятора двигателя (если оснащен переключатель прибора), активацию кондиционера (или дефростера), управление и поддержание скорости дороги 50 миль в час или больше, пока не отключится лампа AFTERTREATMENT DIESEL PARTICULATE FILTER. Продолжайте движение в течение дополнительных 20 минут, чтобы обеспечить достаточную регенерацию дизельного фильтра твердых частиц.
- Выполняют стационарную регенерацию. Следуйте инструкциям в Уникальных эксплуатационных характеристиках двигателя с последующей обработкой, в разделе 1.

> [!note] Примечание
> Стационарная регенерация считается обычной практикой технического обслуживания и не покрывается компанией Cummins Inc. Гарантия.

![[00c00180.png]]

Вспышка светодиодной лампы в сочетании с освещенной лампой предупреждения или CHECK ENGINE указывает на то, что после обработки дизельный фильтр для твердых частиц должен быть немедленно регенерирован. Мощность двигателя будет автоматически снижена.

При освещении этих ламп требуется стационарная регенерация.

- Следуйте инструкциям в Уникальных эксплуатационных характеристиках двигателя с последующей обработкой, в разделе 1.

> [!note] Примечание
> Если неподвижная регенерация не выполняется, лампа STOP ENGINE будет освещаться, и транспортное средство должно быть доставлено в авторизованное место ремонта Cummins®.

> [!note] Примечание
> Стационарная регенерация считается обычной практикой технического обслуживания и не покрывается компанией Cummins Inc. Гарантия.

![[00c00182.png]]

Высокотемпературная лампа системы выхлопа

Высокая ЭКСПОЛЬЗОВАТЕЛЬНАЯ СИСТЕМА ТЕМПЕРАТуры при освещении указывает на то, что температура выхлопных газов высока из-за регенерации фильтра для твердых частиц дизельного топлива после обработки. Эта лампа может освещаться во время нормальной работы двигателя или при стационарной регенерации.

> [!note] Примечание
> OEM определяет, установлена ли лампа высокой экзавст-системы на транспортном средстве или нет. OEM также определяет температуры, скорости транспортного средства и другие условия, при которых лампа освещается. См. руководство по обслуживанию OEM для получения дополнительной информации об этой лампе.

При освещении этой лампы убедитесь, что выпуск выхлопной трубы **не** направлен на любую поверхность или материал, который может расплавиться, сгореть или взорваться.

> [!danger] ОПАСНО
> При освещении этой лампы температура выхлопных газов может достигать 800 ° C \[1500 ° F \], что достаточно жарко, чтобы воспламенить или расплавить обычные материалы и сжечь людей.

- Держите выхлопную трубу подальше от людей и всего, что может гореть, таять или взрываться.
- Ничего в пределах 0,6 м \[2 фута \] от выпускного отверстия выхлопных газов
- Ничто не может сгореть, расплавиться или взорваться в пределах 1,5 м[5 футов] (например, бензин, дерево, бумага, пластмассы, ткань, контейнеры сжатого газа и гидравлические линии).
- В экстренной ситуации выключите двигатель, чтобы остановить поток выхлопных газов.

> [!note] Примечание
> Светильник высокой экшоустной системы не означает необходимости какого-либо обслуживания транспортного средства или двигателя; он просто предупреждает оператора транспортного средства о высоких температурах выхлопных газов. Лампа высокой экшоуст системы будет обычно включаться и выключаться во время нормальной работы автомобиля, когда двигатель завершает регенерацию.

![[11c00107.png]]

После обработки дизельной выхлопной жидкости лампа

Светодиодная лампа с ДИЗЕЛЬНЫМ СРЕДСТВОМ указывает при освещении или мигании, что уровень выхлопной жидкости дизельного топлива низкий.

Освещенная лампа DIESEL EXHAUST FLUID указывает на то, что уровень выхлопной жидкости дизельного топлива упал ниже первоначального уровня предупреждения. Это можно исправить, заполнив бак с выхлопной жидкостью дизельного топлива выхлопной жидкостью дизельного топлива.

> [!note] Примечание
> Рекомендуется, чтобы резервуар с выхлопной жидкостью дизельного топлива был заполнен полностью, чтобы исправить любые условия неисправности.

![[00c00200.png]]

Проблесковая лампа с РЕЗУЛЬТАТНЫМ СРЕДСТВОМ указывает на то, что уровень выхлопной жидкости дизельного топлива упал ниже критического уровня предупреждения. Это можно исправить, заполнив бак с выхлопной жидкостью дизельного топлива выхлопной жидкостью дизельного топлива.

> [!note] Примечание
> Рекомендуется, чтобы резервуар с выхлопной жидкостью дизельного топлива был заполнен полностью, чтобы исправить любые условия неисправности.

![[00c00185.png]]

Проблесковая лампа с светодиодным усилителем в сочетании с освещенной лампой предупреждения или CHECK ENGINE указывает на то, что уровень выхлопной жидкости дизельного топлива упал ниже первоначального уровня выхлопа. Мощность двигателя будет ограничена автоматически. Это можно исправить, заполнив бак с выхлопной жидкостью дизельного топлива выхлопной жидкостью дизельного топлива.

> [!note] Примечание
> Рекомендуется, чтобы резервуар с выхлопной жидкостью дизельного топлива был заполнен полностью, чтобы исправить любые условия неисправности.

![[00c00203.png]]

Позволяя баку выхлопной жидкости дизельного топлива стать пустым, система дозирования выхлопной жидкости дизельного топлива после обработки потеряет простоту. Потеря основного состояния может привести к активации кодов неисправностей.

> [!note] Примечание
> На бортовых диагностических сертифицированных продуктах MIL может быть освещен для потери основного состояния.

> [!note] Примечание
> Рекомендуется, чтобы резервуар с выхлопной жидкостью дизельного топлива был заполнен полностью, чтобы исправить любые условия неисправности.

![[00c00203.png]]

Если двигатель был выключен или работал в режиме холостого хода в течение 20 часов после опорожнения резервуара, лампа STOP ENGINE также будет освещена вместе с мигающей лампой DIESEL EXHAUST FLUID и лампой CHECK ENGINE. Мощность двигателя будет ограничена автоматически. Также будет ограничено ограничение скорости 5 миль в час (MPH).

> [!note] Примечание
> Для того, чтобы снять ограничение скорости 5 МпГ, резервуар с выхлопной жидкостью дизельного топлива должен быть заполнен, по крайней мере, до 10 процентов объема резервуара.

> [!note] Примечание
> Рекомендуется, чтобы резервуар с выхлопной жидкостью дизельного топлива был заполнен полностью, чтобы исправить любые условия неисправности.

> [!note] Примечание
> На бортовых диагностических сертифицированных продуктах также может быть освещена MALFUNCTION INDICATOR LAMP (MIL).

![[00c00184.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The following engine indicator lamps cover **only** the lamps controlled by the engine's ECM. The vehicle manufacturer can provide additional indicator lamps. Please refer to the vehicle's owners manual for additional lamp information.
>
> 1. Check engine
> 2. Check engine
> 3. Aftertreatment diesel particulate filter
> 4. Stop engine
> 5. Aftertreatment diesel exhaust fluid
> 6. Exhaust high temperature
>
> Engine Operation
>
> #### Malfunction Indicator Lamp (MIL)
>
> - For ISX15 CM2250 engines equipped with On Board Diagnostics (OBD), the emissions control system monitors and reports malfunctions that could cause an increase in exhaust emissions levels. If the OBD system detects such a malfunction, the on-board diagnostic system illuminates the MALFUNCTION INDICATOR LAMP (MIL) to indicate that the engine needs to be serviced at the first available opportunity.
>
> **Note · Примечание**
> **The MALFUNCTION INDICATOR LAMP (MIL) is only used on on-board diagnostic certified products**.
>
> The MALFUNCTION INDICATOR LAMP (MIL) is amber, and can look like:
>
> - A symbol of an engine, similar to the illustration.
> - A symbol of exhaust flow featuring an exclamation point, similar to the illustration.
>
> The MALFUNCTION INDICATOR LAMP (MIL) can be illuminated along with any of the engine indicator lamps. It is not used to indicate an engine protection or maintenance required condition.
>
> Check Engine Lamp
>
> The CHECK ENGINE lamp illuminates when the engine needs to be serviced at the first available opportunity.
>
> The CHECK ENGINE lamp is amber, and can look like:
>
> - The words WARNING or CHECK ENGINE spelled out
> - A symbol of an engine, similar to the illustration.
>
> Another function of the CHECK ENGINE lamp is to flash for 30 seconds at key ON to indicate a maintenance condition. This flashing function is referred to as the MAINTENANCE lamp. The MAINTENANCE lamp could flash for and of the following reasons:
>
> - Maintenance required (if the Maintenance Monitor is enabled)
> - Water-in-fuel is detected
> - Coolant level is low.
>
> Stop Engine Lamp
>
> The STOP ENGINE lamp indicates, when illuminated, the need to stop the engine as soon as it can be safely done. The engine **must** remain shut down until the engine can be repaired.
>
> For engines with the Engine Protection Shutdown feature enabled, if the STOP ENGINE lamp begins to flash, the engine will automatically shut down after 30 seconds. The flashing STOP engine lamp alerts the operator to the impending shutdown.
>
> The STOP ENGINE lamp is red in color, and can look like:
>
> - The words STOP or STOP ENGINE spelled out
> - A symbol of an engine with an exclamation point in the center, similar to the illustration.
> - A symbol of a stop sign with an engine outline in the center, similar to the illustration
>
> Aftertreatment Diesel Particulate Filter Lamp
>
> The AFTERTREATMENT DIESEL PARTICULATE FILTER lamp indicates, when illuminated or flashing, that the aftertreatment diesel particulate filter requires regeneration.
>
> An illuminated AFTERTREATMENT DIESEL PARTICULATE FILTER lamp indicates that the aftertreatment diesel particulate filter needs to be regenerated at the next possible opportunity. This can be accomplished by:
>
> - Changing the duty cycle by increasing the engine parasitics, including activating the vehicle's driving lights and head lights, activating the engine fan (if dash switch equipped),activating the air conditioner (or defroster), driving and maintaining a road speed of 50 mph or greater until the AFTERTREATMENT DIESEL PARTICULATE FILTER lamp deactivates. Continue driving for an additional 20 minutes to provide for adequate aftertreatment diesel particulate filter regeneration.
> - Performing a stationary regeneration. Follow the instructions in Unique Operating Characteristics of an Engine with Aftertreatment, in Section 1.
>
> **Note · Примечание**
> Stationary regeneration is considered a normal maintenance practice and is **not** covered by Cummins Inc. warranty.
>
> A flashing AFTERTREATMENT DIESEL PARTICULATE FILTER lamp indicates that the aftertreatment diesel particulate filter needs to be regenerated at the next possible opportunity. Engine power may be reduced automatically.
>
> When this lamp is flashing, the operator should:
>
> - Change the duty cycle by increasing the engine parasitics, including activating the vehicle's driving and head lights,activating the engine fan (if dash switch equipped), activating the air conditioner (or defroster), driving and maintaining a road speed of 50 mph or greater until the AFTERTREATMENT DIESEL PARTICULATE FILTER lamp deactivates. Continue driving for an additional 20 minutes to provide for adequate diesel particulate filter regeneration.
> - Perform a stationary regeneration. Follow the instructions in Unique Operating Characteristics of an Engine with Aftertreatment, in Section 1.
>
> **Note · Примечание**
> Stationary regeneration is considered a normal maintenance practice and is **not** covered by Cummins Inc. warranty.
>
> A flashing AFTERTREATMENT DIESEL PARTICULATE FILTER lamp combined with an illuminated WARNING or CHECK ENGINE lamp indicates that the aftertreatment diesel particulate filter needs be regenerated immediately. Engine power will be reduced automatically.
>
> When these lamps are illuminated, a stationary regeneration is required.
>
> - Follow the instructions in Unique Operating Characteristics of an Engine with Aftertreatment, in Section 1.
>
> **Note · Примечание**
> If a stationary regeneration is **not** performed, the STOP ENGINE lamp will illuminate and the vehicle will need to be taken to a Cummins® Authorized Repair Location.
>
> **Note · Примечание**
> Stationary regeneration is considered a normal maintenance practice and is **not** covered by Cummins Inc. warranty.
>
> High Exhaust System Temperature Lamp
>
> The HIGH EXHAUST SYSTEM TEMPERATURE lamp indicates, when illuminated, that exhaust temperatures are high due to regeneration of the aftertreatment diesel particulate filter. This lamp can illuminate during normal engine operation or during stationary regeneration.
>
> **Note · Примечание**
> The OEM determines whether or **not** the HIGH EXHAUST SYSTEM TEMPERATURE lamp is installed on the vehicle. The OEM also specifies the temperatures, vehicle speeds, and other conditions at which the lamp illuminates. Refer to the OEM service manual for additional information regarding this lamp.
>
> When this lamp is illuminated, make sure that the exhaust pipe outlet is **not** directed at any surface or material that can melt, burn, or explode.
>
> **WARNING · Опасно**
> When this lamp is illuminated, the exhaust gas temperature could reach 800°C \[1500°F\], which is hot enough to ignite or melt common materials, and to burn people.
>
> - Keep the exhaust outlet away from people and anything that can burn, melt, or explode.
> - Nothing within 0.6 m \[2 ft\] of the exhaust outlet
> - Nothing that can burn, melt, or explode within 1.5 m \[5 ft \] (such as gasoline, wood, paper, plastics, fabric, compressed gas containers, and hydraulic lines).
> - In an emergency, turn off the engine to stop the flow of exhaust.
>
> **Note · Примечание**
> The HIGH EXHAUST SYSTEM TEMPERATURE lamp does **not** signify the need for any kind of vehicle or engine service; it merely alerts the vehicle operator to high exhaust temperatures. It will be common for the HIGH EXHAUST SYSTEM TEMPERATURE lamp to illuminate on and off during normal vehicle operation as the engine completes regeneration.
>
> Aftertreatment Diesel Exhaust Fluid Lamp
>
> The DIESEL EXHAUST FLUID lamp indicates, when illuminated or flashing, that the diesel exhaust fluid level is low.
>
> An illuminated DIESEL EXHAUST FLUID lamp indicates that the diesel exhaust fluid level has fallen below the initial warning level. This can be corrected by filling the diesel exhaust fluid tank with diesel exhaust fluid.
>
> **Note · Примечание**
> It is recommended that the diesel exhaust fluid tank be filled completely full of diesel exhaust fluid in order to correct any fault conditions.
>
> A flashing DIESEL EXHAUST FLUID lamp indicates that the diesel exhaust fluid level has fallen below the critical warning level. This can be corrected by filling the diesel exhaust fluid tank with diesel exhaust fluid.
>
> **Note · Примечание**
> It is recommended that the diesel exhaust fluid tank be filled completely full of diesel exhaust fluid in order to correct any fault conditions.
>
> A flashing DIESEL EXHAUST FLUID lamp combined with an illuminated WARNING or CHECK ENGINE lamp indicates that the diesel exhaust fluid level has fallen below the initial derate level. The engine power will be limited automatically. This can be corrected by filling the diesel exhaust fluid tank with diesel exhaust fluid.
>
> **Note · Примечание**
> It is recommended that the diesel exhaust fluid tank be filled completely full of diesel exhaust fluid in order to correct any fault conditions.
>
> Allowing the diesel exhaust fluid tank to become empty will cause the aftertreatment diesel exhaust fluid dosing system to lose prime. A loss of prime condition may cause fault codes to become active.
>
> **Note · Примечание**
> On on-board diagnostic certified products, the MIL may become illuminated for a loss of prime condition.
>
> **Note · Примечание**
> It is recommended that the diesel exhaust fluid tank be filled completely full of diesel exhaust fluid in order to correct any fault conditions.
>
> If the engine has been shut down or has idled for 20 hours after the tank has been emptied, the STOP ENGINE lamp will also be illuminated along with the flashing DIESEL EXHAUST FLUID lamp and illuminated CHECK ENGINE lamp. The engine power will continue to be limited automatically. The vehicle will also be limited to a 5 Mile per Hour (MPH) speed limit.
>
> **Note · Примечание**
> In order to remove the 5 MPH speed limit, the diesel exhaust fluid tank must be filled to at least 10 percent volume of the tank.
>
> **Note · Примечание**
> It is recommended that the diesel exhaust fluid tank be filled completely full of diesel exhaust fluid in order to correct any fault conditions.
>
> **Note · Примечание**
> On on-board diagnostic certified products, the MALFUNCTION INDICATOR LAMP (MIL) may also be illuminated.
