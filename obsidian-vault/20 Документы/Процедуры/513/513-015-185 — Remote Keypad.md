---
type: "Процедура"
doc: "513-015-185"
title_en: "Remote Keypad"
modified: "2025-06-10"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "5411480"
figures: 3
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-015-185.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-015-185.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
  - "перевод/машинный"
---

# Remote Keypad

> [!abstract] Процедура · `513-015-185`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section 15 - Instruments and Controls - Group 15
> **Даты:** изменён 2025-06-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-015-185.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-015-185.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Судно может быть оснащено удаленной клавиатурой для управления работой дисплея. Удалённая клавиатура обычно является дополнительным компонентом для взаимодействия с дисплеем ED-5/ED-7 через шину данных SAE J1939 CAN. Удалённая клавиатура обеспечит возможность управления сенсорной функцией дисплея.

Шпильки для установки и подключения интерфейса устройства находятся на нижней части устройства, используемого для интерфейса с адаптерной проводкой дисплея.

![[15e00197.png]]

Рисунок 1 Передняя часть удаленной клавиатуры

![[15e00198.png]]

Рисунок 2, Задняя часть удаленной клавиатуры

Удалённая клавиатура поставляется предварительно запрограммированной программным обеспечением и конфигурационным файлом и требует выбора из меню дисплея. Удалённая клавиатура также имеет внутренние светодиоды подсветки, которыми можно управлять через меню дисплея. Удалённое программирование на клавиатуре не поддерживается.

![[15e00199.png]]

Рисунок 3, Выбор ключа на удаленной клавиатуре

1. Ключ 1 (Up) - Нажмите клавишу 1 для прокрутки вверх.
2. Ключ 2 (слева) - Нажмите клавишу 2, чтобы прокрутить влево или отрегулировать значения в меню.
3. Ключ 3 (введите / выберите)
4. Ключ 4 (Down) - нажмите клавишу 4, чтобы прокрутить вниз.
5. Ключ 5 (справа) - Нажмите клавишу 5, чтобы прокрутить правильно или отрегулировать значения в меню.
6. Ключ 6 (Возвращение/Выход)

Другая операция, поддерживаемая с удаленной клавиатуры, заключается в нажатии и удерживании клавиш 1 и 4 для доступа к мягким клавишам «Menu» (I), «Backlight» (II), «Alarm» (III). Когда функция мягкой клавиши на экране дисплея выделена желтым ящиком, нажмите клавишу 3 (Enter/Select) для выбора функции кнопки.

Удалённая клавиатура после установки нуждается в идентификации на дисплее, удалённая идентификация клавиатуры может быть выполнена настройками в меню.

Действие:

- Выберите «NMEA Switch Bank» с помощью сенсорного экрана.
- Выберите «Кипа по умолчанию» с помощью сенсорного экрана.
- Выберите «PKU2300M» с помощью сенсорного экрана.
- Выберите «Идентифицировать», чтобы подтвердить, что дисплей взаимодействует с удаленной клавиатурой. Удалённая клавиатура начнет мигать светодиодами, если связь активна.

Когда закончите:

- Прокрутите слева направо или используйте мягкий ключ «Назад» (IV) на экране, чтобы выйти.

Удалённая клавиатура имеет светодиоды подсветки, настраиваемые с различным режимом освещения, доступные как:

- Вон! Светодиоды остаются выключенными все время.
- На: Светодиоды остаются на все время.
- При низкой яркости: Светодиоды **только **загораются, когда подсветка дисплея ниже 20 процентов или равна 20 процентам.
- При высокой яркости: Светодиоды **только **загораются, когда подсветка дисплея выше 20 процентов.
- Не контролируется: Светодиоды остаются выключенными все время и не контролируются уровнем подсветки дисплея.

Действие:

- Выберите «Меню».
- Выберите «Безопасность», введите действительный PIN-код безопасности.
- Выберите «Назад» (IV) мягкий ключ на экране, чтобы выйти.
- Выберите «Setup».
- Выберите «NMEA Switch Bank».
- Выберите «Default Keypad».
- Выберите «PKU2300M».
- Чтобы усовершенствовать порог освещения для дистанционного управления светодиодами подсветки клавиатуры, установите «Порог освещения» для желаемого процента уровня подсветки дисплея.
- Выберите «Режим освещения».
- Выберите режим в соответствии с потребностями приложения.

Когда закончите:

- Прокрутите слева направо или «Назад» (IV) мягкий ключ для выхода из страницы.

### Подготовительные операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Отсоедините аккумуляторные батареи. См. сервисную документацию изготовителя оборудования.

### Снятие

Удалите адаптер дисплея удаленного интерфейса клавиатуры, с нижней части удаленной клавиатуры.

Удалите грецкие гайки, которые обеспечивают удаленную клавиатуру к рулю.

Удалите клавиатуру.

### Установка

Установите удаленную клавиатуру к рулю.

Установите грецкие гайки, которые обеспечивают удаленную клавиатуру к рулю. Подтягивай вручную.

Подключите адаптер дисплея к интерфейсу удаленной клавиатуры к адаптеру на нижней части удаленной клавиатуры.

### Завершающие операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Подсоедините аккумуляторные батареи. См. сервисную документацию изготовителя оборудования.


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The vessel can be equipped with a remote keypad to control the operations of the display. The remote keypad is typically an optional component for interfacing with the display ED-5/ED-7 through SAE J1939 data link. The remote keypad will provide the ability to control touchscreen function of the display.
>
> The mounting studs for installation and device interface connections are on the bottom of the device used to interface with display adapter harness.
>
> Figure 1, Front of the Remote Keypad
>
> Figure 2, Rear of the Remote Keypad
>
> The remote keypad comes pre-programmed with software and configuration file and requires selection from the display menu. The remote keypad also has internal backlight LEDs that can be controlled through the display menu. The remote keypad field programming is **not** supported.
>
> Figure 3, Key Selection on Remote Keypad
>
> 1. Key 1 (Up) - Press key 1 to scroll up.
> 2. Key 2 (Left) - Press key 2 to scroll left or adjust the values in the menu options.
> 3. Key 3 (Enter / Select) –
> 4. Key 4 (Down) - Press key 4 to scroll down.
> 5. Key 5 (Right) - Press key 5 to scroll right or adjust the values in the menu options.
> 6. Key 6 (Return / Exit) –
>
> The other operation supported from remote keypad is by press and hold key 1 and key 4 to access the soft keys “Menu”(I), “Backlight” (II), “Alarm”(III). When the soft key function on the display screen is highlighted with a yellow box, press key 3 (Enter / Select) to select the button function.
>
> The remote keypad once installed needs identification on the display, the remote keypad identification can be done by settings in the menu.
>
> Action:
>
> - Select “NMEA Switch Bank” using the touch screen.
> - Select “Default Keypad” using the touch screen.
> - Select “PKU2300M” using the touch screen.
> - Select “Identify” to confirm the display is communicating with the remote keypad. The remote keypad will start blinking LEDs if communication is active.
>
> When finished:
>
> - Swipe left to right or use “Back”(IV) soft key on the screen to exit.
>
> The remote keypad has backlight LEDs configurable with different lighting mode available as:
>
> - Off: LEDs remain off all the time.
> - On: LEDs remain on all the time.
> - On at low brightness: LEDs **only** light up when display backlight is lower than 20 percent or equal to 20 percent.
> - On at high brightness: LEDs **only** light up when display backlight is above 20 percent.
> - **Not** controlled: LEDs remain off all the time and is **not** controlled by the display backlight level.
>
> Action:
>
> - Select “Menu”.
> - Select “Security”, enter valid security PIN.
> - Select “Back”(IV) soft key on the screen to exit.
> - Select “Setup”.
> - Select “NMEA Switch Bank”.
> - Select “Default Keypad”.
> - Select “PKU2300M”.
> - To adiust the lighting threshold for remote keypad backlight LEDs control, set the "Lighting Threshold" to desired display backlight level percentage.
> - Select “Lighting Mode”.
> - Select the mode per the application needs.
>
> When finished:
>
> - Swipe left to right or “Back”(IV) soft key to exit the page.
>
> ### Preparatory Steps
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Disconnect the batteries. See equipment manufacturer service information.
>
> ### Remove
>
> Remove the display adapter remote keypad interface, from the bottom of the remote keypad.
>
> Remove the wingnuts that secure the remote keypad to the helm.
>
> Remove the keypad.
>
> ### Install
>
> Install the remote keypad to the helm.
>
> Install the wingnuts that secure the remote keypad to the helm. Tighten by hand.
>
> Connect the display adapter harness remote keypad interface to the adapter on the bottom of the remote keypad.
>
> ### Finishing Steps
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Connect the batteries. See equipment manufacturer service information.
