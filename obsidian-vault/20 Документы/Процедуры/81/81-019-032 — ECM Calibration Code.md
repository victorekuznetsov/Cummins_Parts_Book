---
aliases:
  - "Калибровочный код ЭБУ"
type: "Процедура"
doc: "81-019-032"
title_en: "ECM Calibration Code"
title_ru: "Калибровочный код ЭБУ"
modified: "2003-08-26"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
manuals:
  - "3666410"
figures: 4
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-019-032.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-019-032.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/81"
  - "перевод/машинный"
---

# ECM Calibration Code
**Калибровочный код ЭБУ**

> [!abstract] Процедура · `81-019-032`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[3666410 — QSK45 and QSK60 CENSE™ Electronic Control System Troubleshooting and Repair Manual|3666410]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-08-26
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-019-032.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-019-032.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Первичная проверка

Для перекалибровки ECM необходимо загрузить указанную калибровку для модели двигателя.

С выключателем зажигания подключите инструмент электронного сервиса и запустите ESDN. Окно, которое появится, спросит, включен ли переключатель зажигания. Выберите "нет".

Нажмите на кнопку Recalibrate в ESDN и выберите соответствующий номер детали ECM и калибровку, которую вы хотите загрузить. Перенесите калибровку в ECM.

![[19400359.png]]

Появится окно состояния связи, которое подсчитывает прошедшее время, когда модуль пытался установить связь. Поскольку переключатель зажигания отключен, связь может **не** быть установлена. Подождите, пока попытка связи не закончится, или нажмите кнопку Отменить.

В этот момент появится еще одно окно с сообщением о том, что INSITETM для CENSETM не удалось подключиться к модулю. Вам будет предложено выбрать, продолжать или отменить процесс. Выберите OK, чтобы продолжить.

![[19a00042.png]]

Включите замок зажигания.

Процесс калибровки должен проходить через обычные этапы.

![[19a00474.png]]

Поскольку перекалибровка перезаписывает существующую калибровку в модуле, информация о табличке данных также перезаписывается, как только загрузка завершена.

Используйте INSITETM для CENSETM, чтобы добавить информацию о табличке.

![[19a00042.png]]


> [!quote]- Original (English) · английский оригинал
> ### Initial Check
>
> In order to recalibrate the ECM, the specified calibration for the engine model **must** be downloaded.
>
> With the keyswitch OFF, connect the electronic service tool and start ESDN. The window that will appear will ask if the keyswitch is ON. Select No.
>
> Click on the Recalibrate button in ESDN and choose the appropriate ECM part number and calibration you wish to download. Transfer the calibration to the ECM.
>
> A communication status window will appear that counts the elapsed time the module has tried to establish communication. Because the keyswitch is OFF, communication can **not** be established. Wait until the communication attempt times out, or press the Cancel button.
>
> At this point, another window will appear with the message that INSITE™ for CENSE™ was unable to connect to the module. You will be prompted to choose whether to continue or cancel the process. Select OK to continue.
>
> Turn the keyswitch ON.
>
> The calibration process should cycle through the normal steps.
>
> Because the recalibration overwrites the existing calibration in the module, the dataplate information is overwritten as well, once the download is completed.
>
> Use INSITE™ for CENSE™ to add the dataplate information.
