---
type: "Процедура"
doc: "35-010-119-tr"
title_en: "Turbocharger Control Valve Air Line"
modified: "2009-01-23"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
figures: 5
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-010-119-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-010-119-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/35"
  - "перевод/машинный"
---

# Turbocharger Control Valve Air Line

> [!abstract] Процедура · `35-010-119-tr`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 10 - Air Intake System - Group 10
> **Даты:** изменён 2009-01-23
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-010-119-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-010-119-tr.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Введен новый клапан управления турбокомпрессором, чтобы максимизировать производительность двигателя без воздействия на уровень выбросов.

Новый клапан управления турбокомпрессором с высоким креплением расположен на стороне топливного насоса двигателя, установленного на головке цилиндра. Новый клапан управления турбокомпрессором высокого крепления выполняет двойные функции, заменяя клапан управления турбокомпрессором низкого крепления и сборку отключения фильтра воздухоочистителя, как ранее использовалось на двигателе ISM CM870. Новый клапан управления турбокомпрессором **не требует фильтра для очистки воздуха. Однако транспортное средство **должно быть оснащено воздушной сушилкой для удовлетворения требований к установке двигателя.

Воздух транспортного средства будет подаваться непосредственно в клапан управления турбокомпрессором на высоком креплении во входном порту, определенном как порт 1. Порт для выпуска турбокомпрессора к турбокомпрессору VGT идентифицируется как порт 2. Эта информация расположена на этикетке клапана управления турбокомпрессором высокого крепления.

Как и в предыдущих двигателях ISM CM870, электронный модуль управления (ECM) посылает модулированный сигнал шириной импульса (PWM) в клапан управления турбокомпрессором для управления приводом переменной геометрии путем модуляции давления воздуха. По мере увеличения сигнала к приводу с изменяемой геометрией прикладывается большее давление воздуха.

Два новых кода неисправностей связаны с новым клапаном управления турбокомпрессором с высоким креплением.

- Код 2384 - VGT Actuator - напряжение ниже нормального или короткое до низкого источника
- Код 2385 - VGT Actuator - напряжение выше нормального или короткое к высокому источнику

### Подготовительные операции

- Переведите замок зажигания в положение OFF.

![[ck800wa.png]]

### Снятие

> [!warning] ОСТОРОЖНО
> Клапан управления турбокомпрессором очень чувствителен к загрязнению. Неспособность предотвратить попадание загрязнения в управляющий клапан турбокомпрессора линии сжатого воздуха приведет к повреждению управляющего клапана турбокомпрессора.

Отсоедините линию сжатого воздуха на клапане управления турбокомпрессором.

Используйте маскирующую ленту, чтобы покрыть конец линии сжатого воздуха и клапан управления турбокомпрессором, чтобы предотвратить загрязнение.

Удалите P-затворы, удерживающие линию сжатого воздуха к двигателю.

Отсоедините линию сжатого воздуха на клапане отключения управления турбокомпрессором.

Используйте маскирующую ленту, чтобы покрыть конец линии сжатого воздуха и клапан управления турбокомпрессором для предотвращения загрязнения.

Удалите линию подачи воздуха в турбокомпрессорный клапан.

![[19202572.png]]

### Проверка при повторном использовании

Осмотрите соединения сжатых воздушных линий на предмет повреждений или трещин.

Осмотрите линию сжатого воздуха на предмет износа или повреждения.

Осмотрите кольца на наличие признаков повреждения или искажения. Заменить, если обнаружен ущерб.

![[10c00120.png]]

### Установка

> [!warning] ОСТОРОЖНО
> Клапан управления турбокомпрессором очень чувствителен к загрязнению. Неспособность предотвратить попадание загрязнения в управляющий клапан турбокомпрессора линии сжатого воздуха приведет к повреждению управляющего клапана турбокомпрессора.

> [!warning] ОСТОРОЖНО
> Не используйте герметик. Использование герметика резьбы приведет к повреждению клапана управления турбокомпрессором.

Удалите маскирующую ленту с концов линий подачи воздуха турбокомпрессора перед установкой.

Подключите линию подачи воздуха к клапану управления турбокомпрессором.

> [!tip] Момент затяжки
> 16 Н·м [142 фунт-дюйм]

Подключите p-клип к двигателю.

> [!tip] Момент затяжки
> 20 Н·м [177 фунт-дюйм]

Подключите линию подачи воздуха к клапану отключения управления турбокомпрессором.

> [!tip] Момент затяжки
> 16 Н·м [142 фунт-дюйм]

![[19202572.png]]

### Завершающие операции

- Переведите замок зажигания в положение ON.
- Запустите и запустите двигатель.
- Проверить правильность операции.
- Проверьте коды неисправностей и утечки воздуха.

![[ck800wa.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> A new turbocharger control valve has been introduced to maximize the performance of the engine without impacting the emissions level.
>
> The new high mount turbocharger control valve is located on the fuel pump side of the engine mounted to the cylinder head. The new high mount turbocharger control valve serves dual roles, replacing the low mount turbocharger control valve and the air filter shutoff assembly as previously utilized on the ISM CM870 engine. The new turbocharger control valve will **not** require an air filter. However, the vehicle **must** be equipped with an air dryer to meet engine installation requirements.
>
> The vehicle air supply will be plumbed directly to the high mount turbocharger control valve at the inlet port identified as port 1. The turbocharger control valve outlet port to the VGT turbocharger is identified as port 2. This information is located on the high mount turbocharger control valve label.
>
> As with previous ISM CM870 engines, the electronic control module (ECM) sends a pulse width modulated (PWM) signal to the turbocharger control valve to control the variable geometry actuator by modulating air pressure. As the signal increases, more air pressure is applied to the variable geometry actuator.
>
> Two new fault codes are associated with the new high mount turbocharger control valve.
>
> - Fault Code 2384 - VGT Actuator - Voltage Below Normal, or Shorted to Low Source
> - Fault Code 2385 - VGT Actuator - Voltage Above Normal, or Shorted to High Source
>
> ### Preparatory Steps
>
> - Turn the keyswitch to the OFF position.
>
> ### Remove
>
> **CAUTION · Осторожно**
> The turbocharger control valve is very sensitive to contamination. Failure to prevent contamination from entering the turbocharger control valve air lines will cause damage to the turbocharger control valve.
>
> Disconnect the air line at the turbocharger control valve.
>
> Use masking tape to cover the end of the air line and turbocharger control valve to prevent contamination.
>
> Remove the P-clips holding the air line to the engine.
>
> Disconnect the air line at the turbocharger control shutoff valve.
>
> Use masking tape to cover the end of the air line and the turbocharger control shutoff valve to prevent contamination.
>
> Remove the turbocharger control valve air supply line.
>
> ### Inspect for Reuse
>
> Inspect the air line connections for damage or cracks.
>
> Inspect the air line for wear or damage.
>
> Inspect the o-rings for signs of damage or distortion. Replace if damage is found.
>
> ### Install
>
> **CAUTION · Осторожно**
> The turbocharger control valve is very sensitive to contamination. Failure to prevent contamination from entering the turbocharger control valve air lines will cause damage to the turbocharger control valve.
>
> **CAUTION · Осторожно**
> Do not use thread sealant. Use of thread sealant will cause damage to the turbocharger control valve.
>
> Remove the masking tape from the ends of the turbocharger control valve air supply lines before installing.
>
> Connect the air supply line to the turbocharger control valve.
>
> **Момент затяжки · Torque Value**
> 16 n•m [142 in-lb]
>
> Connect the p-clip to the engine.
>
> **Момент затяжки · Torque Value**
> 20 n•m [177 in-lb]
>
> Connect the air supply line to the turbocharger control shutoff valve.
>
> **Момент затяжки · Torque Value**
> 16 n•m [142 in-lb]
>
> ### Finishing Steps
>
> - Turn the keyswitch to the ON position.
> - Start and run the engine.
> - Verify proper operation.
> - Check for fault codes and air leaks.
