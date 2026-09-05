---
aliases:
  - "Электронный блок управления двигателем"
type: "Процедура"
doc: "98-019-031"
title_en: "Engine Control Module"
title_ru: "Электронный блок управления двигателем"
modified: "2024-09-23"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 15
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-031.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-031.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Engine Control Module
**Электронный блок управления двигателем**

> [!abstract] Процедура · `98-019-031`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Controls - Group 19 · Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2024-09-23
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-031.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-031.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Осмотр

Проверьте джек-разъёмы ECM для свободных или отсутствующих джеков.

Промыть и очистить контакты разъема с помощью контактного очистителя, номер детали. 3824510. Проверить разъем ECM на наличие сгоревших штифтов и повреждения корпуса ECM.

Если присутствует какое-либо из вышеперечисленных условий, замените ECM.

![[19801120.png]]

### Снятие

> [!note] Примечание
> Все коды активных ошибок должны быть исследованы до замены ECM.

Запись программируемых параметров клиента. См. соответствующее руководство по электронному обслуживанию.

![[19800109.png]]

> [!warning] ОСТОРОЖНО
> Не крутите, не изгибайте и не тяните за главный двигатель проводов ремня.

Удалите три крепежных болта, удерживающих ECM, в модуль EFC.

Тщательно отведите ECM от топливного насоса.

![[19801900.png]]

> [!warning] ОСТОРОЖНО
> Свободный или отсутствующий пост разъема ECM может привести к тому, что двигатель будет работать беспорядочно, резко расти или неожиданно гибнуть, а также к регистрации любого количества различных кодов неисправностей. Используйте 1/4-дюймовый разъем с открытым концом, чтобы удерживать джек-пост, ослабляя основные болты разъема ECM.

![[19801121.png]]

Удалите два удерживающих болта из главного разъёма проводов двигателя.

Тщательно вытащите разъем из ECM.

![[19801896.png]]

### Установка

> [!warning] ОСТОРОЖНО
> Используйте только рекомендованную Cummins смазку DS-ES, номер детали. 3822934. Другие смазочные материалы, такие как моторное масло или смазка, в разъемах могут вызвать повреждение ECM, плохую производительность двигателя или преждевременный износ штифта.

Нанести смазку на поверхность сосуда ECM.

![[19801885.png]]

Распространите смазку по поверхности сосуда, чтобы убедиться, что она попадает в каждую пин-полость разъема.

![[19801879.png]]

Установите главный разъём ремней электропроводки двигателя в сосуд ECM. Тщательно выровняйте соединительные направляющие слоты с гнездами направляющих в ECM и вставьте разъем.

![[19801855.png]]

> [!warning] ОСТОРОЖНО
> Не перегружайте болты разъема; это может привести к тому, что болты сломаются и повредят ECM.

Тщательно выровняйте и запустите каждый соединительный крепеж вручную. Используйте крутящий момент в дюйме, номер детали. 3376592, затягивать каждый болт по одному повороту до тех пор, пока разъём не будет установлен в сосуде.

> [!tip] Момент затяжки
> 0.7 Н·м [6 фунт-дюйм]

> [!note] Примечание
> Затворы будут **не** внизу.

![[19801841.png]]

> [!warning] ОСТОРОЖНО
> Убедитесь, что задние крепежные болты ECM являются частью No. 3067583. ECM может быть поврежден внутри, если установлены более длинные болты.

Поместите ECM над лицевой стороной модуля EFC и вставьте три крепежных болта.

Затяните болты.

> [!tip] Момент затяжки
> 14 Н·м [124 фунт-дюйм]

![[19801900.png]]

Программируйте программируемые клиентом параметры.

> [!note] Примечание
> При замене ECM необходимо откалибрование нового ECM. Используйте инструмент электронного сервиса для калибровки ECM. См. соответствующее руководство по электронному обслуживанию.

![[19800109.png]]

### калибровать

Для перекалибровки ECM необходимо загрузить указанную калибровку для модели двигателя.

С выключателем зажигания подключите инструмент электронного сервиса и запустите ESDN. Окно, которое появится, спросит, включен ли переключатель зажигания. Выберите "нет".

Нажмите на кнопку Recalibrate в ESDN и выберите соответствующий номер детали ECM и калибровку, которую вы хотите загрузить. Перенесите калибровку в ECM.

![[19400359.png]]

Появится окно состояния связи, которое подсчитывает прошедшее время, когда модуль пытался установить связь. Поскольку переключатель зажигания отключен, связь может **не** быть установлена. Подождите, пока попытка связи не закончится, или нажмите кнопку Отменить.

В этот момент появится еще одно окно с сообщением о том, что INSITETM для CENTRYTM не удалось подключиться к модулю. Вам будет предложено выбрать, продолжать или отменить процесс. Выберите OK, чтобы продолжить.

![[19a00042.png]]

Включите замок зажигания.

Процесс калибровки должен проходить через обычные этапы.

![[19a00474.png]]

Поскольку перекалибровка перезаписывает существующую калибровку в модуле, информация о табличке данных также перезаписывается, как только загрузка завершена.

Используйте INSITETM для CENTRYTM для добавления информации о табличках.

![[19a00042.png]]


> [!quote]- Original (English) · английский оригинал
> ### Inspect
>
> Inspect the ECM connector jack posts for loose or missing jacks.
>
> Flush and clean the connector pins using contact cleaner, Part No. 3824510. Inspect the ECM connector for burnt pins and damage to the ECM housing.
>
> If any of the above conditions are present, replace the ECM.
>
> ### Remove
>
> **Note · Примечание**
> All active fault codes **must** be investigated prior to ECM replacement.
>
> Record the customer's programmable parameters. Refer to the appropriate electronic service tool manual.
>
> **CAUTION · Осторожно**
> Do not twist, bend, or pull on the main engine harness.
>
> Remove the three mounting capscrews holding the ECM to the EFC module.
>
> Carefully move the ECM away from the fuel pump.
>
> **CAUTION · Осторожно**
> A loose or missing ECM jack post can cause the engine to run erratically, surge, or die unexpectedly, as well as to log any number of different fault codes. Use a 1/4-inch open-end wrench to hold the jack post while loosening the main engine harness ECM connector capscrews.
>
> Remove the two hold-down capscrews from the main engine harness connector.
>
> Carefully pull the connector from the ECM.
>
> ### Install
>
> **CAUTION · Осторожно**
> Use only Cummins-recommended lubricant DS-ES, Part No. 3822934. Other lubricants, such as lubricating oil or grease, in the connectors can cause ECM damage, poor engine performance, or premature pin wear.
>
> Apply lubricant to the face of the ECM receptacle.
>
> Spread the lubricant across the face of the receptacle to make sure it gets into every pin cavity of the connector.
>
> Install the main engine harness connector into the ECM receptacle. Carefully align the connector guide slots with the receptacle guide slots in the ECM and insert the connector.
>
> **CAUTION · Осторожно**
> Do not overtighten the connector capscrews; this can cause the capscrews to break and damage the ECM.
>
> Carefully align and start each connector mounting capscrew by hand. Use inch-pound torque wrench, Part No. 3376592, to tighten each capscrew one turn each until the connector is seated in the receptacle.
>
> **Момент затяжки · Torque Value**
> 0.7 n•m [6 in-lb]
>
> **Note · Примечание**
> The capscrews will **not** bottom out.
>
> **CAUTION · Осторожно**
> Make sure the rear ECM mounting capscrew is Part No. 3067583. The ECM can be internally damaged if a longer capscrew is installed.
>
> Place the ECM over the face of the EFC module, and insert the three mounting capscrews.
>
> Tighten the capscrews.
>
> **Момент затяжки · Torque Value**
> 14 n•m [124 in-lb]
>
> Program the customer-programmable parameters.
>
> **Note · Примечание**
> When an ECM is replaced, the new ECM **must** be calibrated. Use an electronic service tool to calibrate the ECM. Refer to the appropriate electronic service tool manual.
>
> ### Calibrate
>
> In order to recalibrate the ECM, the specified calibration for the engine model **must** be downloaded.
>
> With the keyswitch OFF, connect the electronic service tool and start ESDN. The window that will appear will ask if the keyswitch is ON. Select No.
>
> Click on the Recalibrate button in ESDN and choose the appropriate ECM part number and calibration you wish to download. Transfer the calibration to the ECM.
>
> A communication status window will appear that counts the elapsed time the module has tried to establish communication. Because the keyswitch is OFF, communication can **not** be established. Wait until the communication attempt times out, or press the Cancel button.
>
> At this point, another window will appear with the message that INSITE™ for CENTRY™ was unable to connect to the module. You will be prompted to choose whether to continue or cancel the process. Select OK to continue.
>
> Turn the keyswitch ON.
>
> The calibration process should cycle through the normal steps.
>
> Because the recalibration overwrites the existing calibration in the module, the dataplate information is overwritten as well, once the download is completed.
>
> Use INSITE™ for CENTRY™ to add the dataplate information.
