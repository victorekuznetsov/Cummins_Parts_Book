---
type: "Процедура"
doc: "98-fc254"
title_en: "Auxiliary Shutdown Circuit - Voltage Below Normal or Shorted to Low Source"
modified: "2021-09-15"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc254.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc254.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Auxiliary Shutdown Circuit - Voltage Below Normal or Shorted to Low Source

> [!abstract] Процедура · `98-fc254`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2021-09-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc254.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc254.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 254

### Вспомогательная цепь отключения - напряжение ниже нормального или короткое до низкого источника

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 254 PID(P): S17 SPN: ФМИ: 4 лампы: На SRT: 00-629 | Низкое напряжение на вспомогательном выключателе/срабатывающей цепи драйвера крутящего момента при включенном вспомогательном выключении. | Двигатель может **не** завестись. Двигатель может отключиться. Возможно снижение производительности двигателя. |

![[19802304.png]]

Вспомогательная схема отключения

### Описание цепи

Вспомогательный драйвер выключения/вывода крутящего момента в системе CENTRYTM может использоваться для питания вспомогательных устройств выключения, таких как клапаны воздухозаборника. Драйвер вывода крутящего момента/ауксиллярного выключения имеет один контур; драйвер вывода крутящего момента/ауксиллярного выключения. ECM обеспечивает переключенное напряжение батареи на вспомогательный выключатель соленоида.

### Расположение компонента

Вспомогательные выключения соленоидов могут варьироваться и зависят от OEM.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда переключатель зажигания находится в положении Включения.

### Условия установки кодов неисправностей

Модуль управления двигателем (ECM) обнаружил, что вспомогательное выключение / выходное напряжение драйвера крутящего момента было вне диапазона низкого.

### Действия системы при активном коде неисправности

- ECM освещает красную лампу STOP ENGINE сразу же после запуска и отказа диагностического устройства.

Для приложений генерации электроэнергии:

- Контроллер генераторной установки отображает неисправность сразу же, когда диагностика работает и выходит из строя.

### Условия сброса кода неисправности

- Выключите замок зажигания. Позвольте ECM полностью выключить питание и включить переключатель зажигания.

- Состояние кода ошибки, отображаемого рекомендованным электронным сервисным инструментом Cummins® или его эквивалентом, будет изменено на INACTIVE сразу после диагностических запусков и проходов.

- ECM выключит красную лампу STOP ENGINE сразу после диагностических прогонов и проходов.

- Команда «Сбросить все ошибки» в рекомендуемой электронной сервисной оснастке Cummins® или эквиваленте может использоваться для устранения активных и неактивных ошибок.

Для приложений генерации электроэнергии:

- Чтобы проверить результат ремонта, запустите двигатель и дайте ему поработать 1 минуту без нагрузки.

- Контроллер генераторной установки выключит индикатор сразу после того, как пользователь нажмет сброс.

- Для сброса активных неисправностей можно воспользоваться командой «Reset All Faults» в рекомендованной программе Cummins® или её аналоге.

### Практические замечания

Возможные причины этого кода неисправности:

- Неисправный или повреждённый жгут проводов двигателя.

- Неисправность или повреждение OEM-проводов.

- Поврежденные или рыхлые разъемы.

- Неисправность или повреждение вспомогательного отключения соленоида.

См. Код устранения неполадок t05-254


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 254
>
> ### Auxiliary Shutdown Circuit - Voltage Below Normal or Shorted to Low Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 254 PID(P): S17 SPN: FMI: 4 Lamp: On SRT: 00-629 | Low voltage on the auxiliary shutdown/torque output driver circuit when the auxiliary shutdown is on. | Engine may **not** start. Engine may shut down. Possible reduced engine performance. |
>
> Auxiliary Shutdown Circuit
>
> ### Circuit Description
>
> The auxiliary shutdown/ torque output driver in the CENTRY™ system can be used to power auxiliary shutdown devices such as air intake flaps. The auxillary shutdown/ torque output driver has a single circuit; auxillary shutdown/ torque output driver. The ECM provides switched battery voltage to the auxiliary shutdown solenoid.
>
> ### Component Location
>
> The auxiliary shutdown solenoid location may vary and is OEM dependent.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the keyswitch is in the ON position.
>
> ### Conditions For Setting The Fault Codes
>
> The Engine Control Module (ECM) detected the auxiliary shutdown/ torque output driver voltage was out of range low.
>
> ### Action Taken When The Fault Code Is Active
>
> - The ECM illuminates the red STOP ENGINE lamp immediately when the diagnostic runs and fails.
>
> For Power Generation Applications:
>
> - The generator set controller displays the fault immediately when the diagnostics runs and fails.
>
> ### Conditions For Clearing The Fault Code
>
> - Turn the keyswitch OFF. Allow the ECM to completely power down and turn the keyswitch ON.
>
> - The fault code status displayed by the recommended Cummins® electronic service tool or equivalent will change to INACTIVE immediately after the diagnostic runs and passes.
>
> - The ECM will turn off the red STOP ENGINE lamp immediately after the diagnostic runs and passes.
>
> - The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active and inactive faults.
>
> For Power Generation Applications:
>
> - To validate the repair, start the engine and let it run for 1 minute at no load.
>
> - The generator set controller will turn off the indicator immediately after the user presses reset.
>
> - The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.
>
> ### Shoptalk
>
> Possible causes of this fault code include:
>
> - Malfunctioning or damaged engine wiring harness.
>
> - Malfunctioning or damaged OEM wiring harness.
>
> - Damaged or loose connectors.
>
> - Malfunctioning or damaged auxiliary shutdown solenoid.
>
> Refer to Troubleshooting Fault Code t05-254
