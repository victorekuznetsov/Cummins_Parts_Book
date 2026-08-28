---
type: "Процедура"
doc: "19-019-186"
title_en: "In-Range Pressure Sensor"
modified: "2002-08-20"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 9
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-186.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-186.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# In-Range Pressure Sensor

> [!abstract] Процедура · `19-019-186`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2002-08-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-186.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-186.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Испытание на давление

Выключи двигатель.

Снять давление в топливной системе, открыв топливные линии или вытащив датчики давления или исполнительные механизмы.

![[19400307.png]]

Подключите INSITETM к шине данных CAN.

![[19a00042.png]]

Переведите замок зажигания в положение ON.

> [!note] Примечание
> Железнодорожное и временное давление отображаются в единицах psia. Давление окружающего воздуха отображается в единицах in-Hg. Чтобы преобразовать из psia в in-Hg, умножьте значение psia на два (15 psia = 30 in-Hg, например).

Используйте INSITETM для мониторинга давления в рельсах, давления во времени, давления окружающего воздуха, давления насоса и давления впускного коллектора в английских единицах.

- Давление в Железной дороге, давление временных рамок и давление в насосе должны быть одинаковыми.
- Давление рельса, времени и насоса должно быть равно давлению окружающего воздуха.
- Давление впуска многообразия должно быть равно нулю.

> [!note] Примечание
> Вышеуказанные меры должны быть точными в пределах ±4 psia или ±8 in-Hg.

![[19800978.png]]

Если давление рельса, время и насос равны, но не равны давлению окружающего воздуха, то обратитесь к кодам поломок 221, 222 и 318.

Если давление впускного коллектора превышает 0,5 in-Hg, то обратитесь к кодам 122 и 123.

![[19800978.png]]

Если давление рельса, время и насоса не равны, сравните каждое с давлением окружающего воздуха.

- Если давление на рельсах не соответствует давлению окружающего воздуха, обратитесь к кодам 451 и 452.
- Если временное давление **не** равно давлению окружающего воздуха, обратитесь к кодам 116 и 117.
- Если давление насоса **не** равно давлению окружающего воздуха, обратитесь к коду 316 по умолчанию.

![[19800978.png]]

Если какие-либо датчики были удалены, установите их обратно в электронный клапанный узел.

Запустите двигатель и запускайте его на холостом ходу.

Измерьте давление в рельсах, давление временных рамок, давление окружающего воздуха, давление насоса и давление впускного коллектора.

- Если давление окружающего воздуха не соответствует давлению окружающего воздуха с выключенным двигателем, обратитесь к кодам 221 и 222 по умолчанию.
- Если давление впускного коллектора превышает 1 рт.ст., обратитесь к кодам 122 и 123 по умолчанию.

![[19800979.png]]

Подключите датчик измерения давления к быстрому отключению топливной рельсы.

- Если измерительное давление не совпадает с электронным измерением, обратитесь к кодам 451 и 452.

![[19400633.png]]

Подсоедините датчик измерения давления к быстрому отключению рельса синхронизации.

- Если измерительное давление не совпадает с электронным измерением, обратитесь к кодам 116 и 117.

![[19400633.png]]

Подключите датчик измерения давления к выходу топливного насоса быстро отсоединяйтесь.

- Если измерительное давление не совпадает с электронным измерением, обратитесь к коду 316 по умолчанию.

![[19400633.png]]


> [!quote]- Original (English) · английский оригинал
> ### Pressure Test
>
> Turn the engine off.
>
> Relieve the pressure in the fuel system by opening the fuel lines or pulling out the pressure sensors or actuators.
>
> Connect INSITE™ to the vehicle datalink.
>
> Turn the keyswitch to the ON position.
>
> **Note · Примечание**
> Rail and timing pressure are displayed in units of psia. Ambient air pressure is displayed in units of in-Hg. To convert from psia to in-Hg, multiply the psia reading by two (15 psia = 30 in-Hg, for example).
>
> Use INSITE™ to monitor the rail pressure, timing pressure, ambient air pressure, pump pressure, and intake manifold pressure in English units.
>
> - Rail pressure, timing pressure, and pump pressure should all be the same.
> - Rail, timing, and pump pressure should be equal to the ambient air pressure.
> - Intake manifold pressure should be equal to zero.
>
> **Note · Примечание**
> The above measures should be accurate to within ±4 psia or ±8 in-Hg.
>
> If the rail, timing, and pump pressures are equal, but are **not** equal to the ambient air pressure, then refer to Fault Codes 221, 222, and 318.
>
> If the intake manifold pressure is greater than 0.5 in-Hg, then refer to Fault Codes 122 and 123.
>
> If the rail, timing, and pump pressures are **not** equal, compare each to the ambient air pressure.
>
> - If the rail pressure is **not** equal to the ambient air pressure, refer to Fault Codes 451 and 452.
> - If the timing pressure is **not** equal to the ambient air pressure, refer to Fault Codes 116 and 117.
> - If the pump pressure is **not** equal to the ambient air pressure, refer to Fault Code 316.
>
> If any sensors were removed, install them back into the electronic control valve assembly.
>
> Start the engine and let it idle.
>
> Measure the rail pressure, timing pressure, ambient air pressure, pump pressure, and intake manifold pressure.
>
> - If the ambient air pressure does **not** equal the ambient air pressure with the engine off, refer to Fault Codes 221 and 222.
> - If the intake manifold pressure is greater than 1 in-Hg, refer to Fault Codes 122 and 123.
>
> Connect a pressure gauge to the fuel rail quick-disconnect.
>
> - If the gauge pressure is **not** the same as the electronic measurement, refer to Fault Codes 451 and 452.
>
> Connect a pressure gauge to the timing rail quick-disconnect.
>
> - If the gauge pressure is **not** the same as the electronic measurement, refer to Fault Codes 116 and 117.
>
> Connect a pressure gauge to the fuel pump outlet quick-disconnect.
>
> - If the gauge pressure is **not** the same as the electronic measurement, refer to Fault Code 316.
