---
type: "Процедура"
doc: "97-019-300"
title_en: "Cab Thermostat"
modified: "2003-06-12"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
  - "80141463"
  - "80248213"
families:
  - "QSM11"
  - "QSX15"
manuals:
  - "3666415"
figures: 8
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-300.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-300.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
  - "перевод/машинный"
---

# Cab Thermostat

> [!abstract] Процедура · `97-019-300`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-06-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-300.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-300.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Снятие

Переведите замок зажигания в положение OFF.

Удалите винты, обеспечивающие термостат кабины, на стенку корпуса.

Отсоедините проводку термостата кабины и проводку датчика температуры от термостата кабины.

![[19802874.png]]

Удалите термостат кабины.

![[19802875.png]]

### Установка

Убедитесь, что переключатель зажигания повернут в положение выключения.

Поместите термостат кабины в подходящее место в зоне бункера.

Как правило, термостат устанавливается примерно на 2 фута над спальной зоной или на полпути между койкой и потолком из прямого потока воздуха от кондиционирования или отопления.

![[19802875.png]]

Установите винты, обеспечивающие термостат кабины, на стенку корпуса.

Подключите термостат кабины к проводах датчика температуры.

Подключите термостат кабины к электропроводке кабины.

![[19802874.png]]

### Регулировка

При устранении неполадок в системе ICONTM техник может «заставить» двигатель запускаться в режиме Cab Comfort термостата. Этот искусственно созданный запуск двигателя может быть выполнен с использованием тепловых пушек или холодного распыления.

Имейте в виду, что если этот метод используется для устранения неполадок и «принудительный» перезапуск двигателя происходит в течение 10 минут после предыдущего перезапуска по заказу ICONTM, термостат сгенерирует код неисправности E3.

![[15800001.png]]

Когда система ICONTM установлена в режиме Cab Comfort, термостат кабины играет важную роль в общении и позволяет системе ICONTM автоматически запускать двигатель автомобиля. Неправильно установленные регулировки термостата могут помешать системе ICONTM автоматически запустить двигатель. Исключите возможность неправильно установленного термостата кабины перед дальнейшим устранением неполадок.

Убедитесь, что режим охлаждения или нагрева термостата активен, проверив на слово «COOL» или «HEAT», отображаемое в нижнем левом углу термостата.

![[15800027.png]]

Если индикатор режима охлаждения или нагрева («COOL» или «HEAT», отображаемый в нижнем левом углу дисплея термостата) мигает, это означает, что термостат обнаружил температуру бункера выше точки охлаждения и значения диапазона (или ниже точки теплового набора и значения диапазона) и командует модулем управления холостым режимом ICONTM для запуска двигателя.

Также можно получить мигающий индикатор команды двигателя автозапуска термостата в ICONTM, когда двигатель уже работает.

Если двигатель не запускается, когда ему приказано сделать это термостатом, устраните неисправности кабины проводов, кабины термостата прыгуна проводов или ICONTM двигатель проводов ремня. Проверьте коды неисправностей.

![[15800023.png]]

Режим Cab Comfort системы ICONTM может работать с перерывами. Возможная причина этого заключается в том, что водитель **не **вручную выбирает режим тепла или охлаждения каждый раз, когда он хочет использовать режим комфорта Кабина ICONTM. Если режим охлаждения или нагрева **не** выбирается вручную каждый раз, когда включен режим Cab Comfort (путем включения термостата и выбора режима нагрева), термостат по умолчанию будет соответствовать настройкам автоматического охлаждения и автоматического нагрева, как это продиктовано настройками отделки термостата. Эти настройки отделки могут быть скорректированы в соответствии с личными предпопоказанийми водителя.

См. Cab Thermostat Operation и Thermostat Trim Settings в разделе F для получения более подробной информации о настройке режимов охлаждения и нагрева термостата, а также для настроек стола отделки, которые можно сбросить.

![[15800020.png]]


> [!quote]- Original (English) · английский оригинал
> ### Remove
>
> Turn the keyswitch to the OFF position.
>
> Remove the screws securing the cab thermostat to the bunk housing wall.
>
> Disconnect the cab thermostat jumper harness and the temperature sensor harness from the cab thermostat.
>
> Remove the cab thermostat.
>
> ### Install
>
> Make sure the keyswitch is turned to the OFF position.
>
> Position the cab thermostat in a suitable location in the bunk area.
>
> Typically, the thermostat is installed approximately 2 feet over the bunk sleeping area, or midway between the bunk and the ceiling, out of the direct flow of air from the air conditioning or heating.
>
> Install the screws securing the cab thermostat to the bunk housing wall.
>
> Connect the cab thermostat to the temperature sensor harness.
>
> Connect the cab thermostat to the cab thermostat harness.
>
> ### Adjust
>
> In troubleshooting the ICON™ system, the technician can “force” an engine start via the thermostat's Cab Comfort mode. This artificially created engine start can be accomplished using heat guns or cold spray.
>
> Be aware that, if this technique is being employed for troubleshooting purposes and the “forced” engine restart occurs within 10 minutes of the previous ICON™-ordered restart, the thermostat will generate an E3 fault code.
>
> When the ICON™ system is set to Cab Comfort mode, the cab thermostat is instrumental in communicating with and enabling the ICON™ system to autostart the vehicle's engine. Thermostat adjustments that are improperly set can prevent the ICON™ system from autostarting the engine. Rule out the possibility of an improperly set cab thermostat before troubleshooting further.
>
> Verify that the thermostat's cool or heat mode is active by checking for the word “COOL” or “HEAT” displayed in the thermostat's lower left corner.
>
> If the cool or heat mode indicator (“COOL” or “HEAT” displayed in lower left of thermostat display) is flashing, this means that the thermostat has detected the bunk temperature is above the cool set point and range value (or below the heat set point and range value) and is commanding the ICON™ idle control module to start the engine.
>
> It is also possible to get the flashing indication of the thermostat autostart engine command to ICON™ while the engine is already running.
>
> If the engine does **not** start when it is being commanded to do so by the thermostat, troubleshoot the cab harness, cab thermostat jumper harness, or ICON™ engine harness. Check for fault codes.
>
> The ICON™ system's Cab Comfort mode can seem to be working intermittently. A possible cause for this is that the driver is **not** manually choosing either heat or cool mode each time he desires to utilize ICON™'s Cab Comfort mode. If the cool or heat mode is **not** chosen manually each time Cab Comfort mode is enabled (by turning on the thermostat and choosing heat mode), the thermostat will default to the autocool and autoheat settings as dictated in the thermostat's trim settings. These trim settings can be readjusted according to the driver's personal preferences.
>
> Refer to Cab Thermostat Operation and the Thermostat Trim Settings in Section F for more details on adjusting the thermostat's cool and heat modes, and for the trim table settings, which can be reset.
