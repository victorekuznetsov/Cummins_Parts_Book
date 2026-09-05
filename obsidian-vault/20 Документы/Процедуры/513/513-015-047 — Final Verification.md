---
type: "Процедура"
doc: "513-015-047"
title_en: "Final Verification"
modified: "2025-04-21"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "5411480"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-015-047.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-015-047.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
  - "перевод/машинный"
---

# Final Verification

> [!abstract] Процедура · `513-015-047`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section 15 - Instruments and Controls - Group 15
> **Даты:** изменён 2025-04-21
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-015-047.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-015-047.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Выбор сервисного инструмента

#### Рекомендованный сервисный инструмент Cummins®

- Не рекомендуется использовать инструменты Cummins®.

#### Дополнительные сервисные позиции

- Никаких дополнительных предметов обслуживания не требуется.

### Общие сведения

Функциональность системы командной связи C Command Connect и системы управления морскими панелями Connect Premier должна быть проверена перед выходом из дока после служебного события системы.

Проверьте следующее для правильной работы каждого двигателя индивидуально, чтобы подтвердить работу физического переключателя и функциональность отображения.

- Для каждого двигателя включите систему, включите переключатель (переключатели). Проверьте включение питания дисплея (дисплеев), просматривая информацию о данных на экране.
- С включением переключателя (переключателей) системы, проверьте внешние звуки сигнализации, поместив дисплей ED-4 в режим DEMO. После подтверждения внешних звуков сигнализации отключите режим DEMO дисплея ED-4.
- С включением переключателя (переключателей) системы, убедитесь, что сенсорный экран дисплея ED-5 / ED-7 функционирует, прокручивая экран данных, получая доступ к информации тревоги с помощью кнопки мягких сигналов тревоги на экране данных.
- Для приложения с использованием удаленной клавиатуры с включенным переключателем (переключателями) системы убедитесь, что клавиатура функциональна, используя клавиши Up, Down, Left, Right для прокрутки экрана данных, доступа к информации тревоги, доступа к мягким кнопкам для открытия меню и управления подсветкой.
- С системой включения переключателя (переключателей) ON, включите диммер (если он оборудован), чтобы проверить, что яркость дисплея (дисплеев) регулируется.
- С системой включите переключатель(ы). Нажмите на стартовый выключатель для каждого двигателя, чтобы проверить запуск двигателя.
- При работе двигателя в нейтральном режиме и холостом режиме, убедитесь, что дисплей(ы) функционирует должным образом для этого двигателя, и на дисплее(ах) нет активных неисправностей. Например, проверьте напряжение батареи, давление масла в двигателе и то, что температура охлаждающей жидкости двигателя увеличивается по мере того, как двигатель работает. Также важно проверить информацию датчика судна, отображаемую на ED-4/ED-5/ED-7; например, давление и температуру масла передач, угол руля и уровень топлива. Если он оборудован, проверьте правильное напряжение генератора во время работы.
- С двигателем в нейтральном режиме и холостом ходу проверьте работу всех систем, включающих переключатели, включая любые переключатели E-stop, переключатели остановки двигателя, переключатели lanyard, переключатели ключей двигателя и любые другие устройства, предназначенные для выключения двигателя, если они оборудованы. После тестирования каждого двигателя индивидуально, запустите все двигатели и выполните отключение системы с помощью переключателей.
- Хотя **не** часть C Command Connect и Connect Premier Marine Panel System, с работающим двигателем (двигателями), проверьте дроссель и правильное управление передачей двигателя (двигателей).
- Используйте следующую процедуру для получения дополнительной информации.[[513-101-013 — General Operating Instructions|См. процедуру 101-013 в разделе 1.]]


> [!quote]- Original (English) · английский оригинал
> ### Select Service Tools
>
> #### Recommended Cummins® Service Tools
>
> - No recommended Cummins® service tools.
>
> #### Additional Service Items
>
> - No additional service items required.
>
> ### General Information
>
> Functionality of the C Command Connect and Connect Premier Marine Panel System **must** be tested before leaving the dock after a service event of the system.
>
> Check the following for proper operation of each engine individually to confirm physical switch operation and display functionality.
>
> - For each engine, turn ON the system enable switch(s). Verify the display(s) power ON by viewing data information on the screen.
> - With the system enable switch(s) ON, verify external alarm horn sounds by placing an ED-4 display into DEMO mode. After confirming the external alarm horn sounds, disable the ED-4 display DEMO mode.
> - With the system enable switch(s) ON, verify the ED-5/ED-7 display touchscreen is functional by scrolling through data screen, accessing alarm information by alarm soft button on the data screen.
> - For application using the Remote Keypad, with the system enabled switch(s) ON, verify the keypad is functional by using the Up, Down, Left, Right keys to scroll through data screen, accessing alarm information, accessing soft buttons to open menu and backlight controls.
> - With the system enable switch(s) ON, turn the dimmer (if equipped) to verify the display(s) brightness is adjustable.
> - With the system enable switch(s) ON. Press the start switch for each engine to verify the engine starts.
> - With the engine in neutral and idling, verify the display(s) function properly for that engine and there are no active faults on the display(s). For example, check the battery voltage, engine oil pressure, and that the engine coolant temperature increases as the engine idles. It is also important to check the vessel sensor information displayed on the ED-4/ED-5/ED-7; such as transmission gear oil pressure and temperature, rudder angle, and fuel level. If equipped, verify proper generator voltage while running.
> - With the engine in neutral and idling, check the operation of all system enable switches, including any E-stop switches, engine stop switches, lanyard switches, engine key switches, and any other devices intended to shut down the engine, if equipped. After testing each engine individually, start all engines and perform a system shutdown using the switches.
> - Although **not** part of the C Command Connect and Connect Premier Marine Panel System, with the engine(s) running, verify throttle and correct gear control of engine(s).
> - Use the following procedure for additional information. [[513-101-013 — General Operating Instructions|Refer to Procedure 101-013 in Section 1.]]
