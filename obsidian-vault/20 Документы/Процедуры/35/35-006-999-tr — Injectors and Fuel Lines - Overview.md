---
aliases:
  - "Форсунки и топливные магистрали — обзор"
type: "Процедура"
doc: "35-006-999-tr"
title_en: "Injectors and Fuel Lines - Overview"
title_ru: "Форсунки и топливные магистрали — обзор"
modified: "2008-11-17"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
figures: 20
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-006-999-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-006-999-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/35"
  - "перевод/машинный"
---

# Injectors and Fuel Lines - Overview
**Форсунки и топливные магистрали — обзор**

> [!abstract] Процедура · `35-006-999-tr`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section F - Familiarization
> **Даты:** изменён 2008-11-17
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-006-999-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-006-999-tr.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Теория операции

Гидромеханическая подсистема

Двигатель ISM 2002 года использует другой форсунка, чем предыдущий двигатель ISM, с изменениями характеристик потока и повышенной надежностью. Форсунка специально разработан для максимизации преимущества охлажденного EGR и снижения уровня выбросов.

Топливный насос расположен в том же месте, что и топливный насос CELECTTM Plus.

![[gr8hsha.png]]

Топливный насос является типом переключения передач насоса. Сборка включает регулятор давления, пульсационный демпфер и соленоидный клапан.

1. Регулятор давления
2. пульсационный демпфер
3. Электромагнитный клапан.

![[fp800pi.png]]

ECM устанавливается на охлаждающую пластину. Во время работы двигателя топливо циркулирует через охлаждающую пластину для поглощения тепла, генерируемого ECM.

![[06200011.png]]

На двигателях CM876 топливо течет от топливной винты в задней части двигателя к запорному клапану после обработки. Затем он поступает в форсунка для топлива после обработки.

Когда топливо **не** поступает в форсунка, топливо, оставшееся между запорным клапаном после обработки № 1 и форсункой после обработки топлива, проходит через запорный клапан после обработки № 2 и идет в слив.

![[06200059.png]]

В сборку форсунки входит соленоидный клапан, который контролирует конец учета топлива и начало впрыска. Соленоидный клапан обычно открыт. Электронный сигнал от ECM закрывает клапан по мере необходимости.

![[fi8vaga.png]]

Топливная система использует распредвал для создания адекватного давления для впрыска.

![[fi200gk.png]]

Проиллюстрирован отсеченный вид электронно управляемого форсунки с идентифицированными внутренними компонентами.

![[fi800gb.png]]

Цикл инъекций

В начале измерения, измерительный плунжер и плунжер времени находятся на нижних границах их путешествия. Клапан управления топливным форсункой закрыт.

![[fi800gn.png]]

По мере вращения распределительного вала, возвращаемая пружина вынуждает плунжер времени вверх.

Топливо течет мимо контрольного контрольного шара и в камеру учета. Этот поток продолжается до тех пор, пока плунжер синхронизации движется вверх, а клапан управления топливным форсункой закрыт.

Давление подачи, воздействуя на дно дозирующего поршня, вынуждает его поддерживать контакт с плунжером времени.

![[fi800gd.png]]

ECM определяет конец измерения, сигнализируя о том, что клапан управления топливным форсункой открыт.

![[fi800ge.png]]

Топливо при давлении подачи затем поступает в камеру синхронизации, тем самым останавливая движение поршня.

В течение этого времени пружина смещения гарантирует, что дозирующий плунжер остается неподвижным; что он **не **дрейфует вверх по мере движения плунжера синхронизации вверх. Эта же сила против измерительного плунжера приводит к достаточному давлению топлива ниже поршня, чтобы держать контрольный мяч измерения сидящим.

Точно измеренное количество топлива теперь находится в камере учета. Это определяет количество топлива, которое будет впрыскиваться.

![[fi800gh.png]]

Временный плунжер продолжает двигаться вверх, а камера синхронизации заполняется топливом.

![[fi800gf.png]]

Время плунжер начинает свое нисходящее путешествие. Первоначально клапан управления топливным форсункой остается открытым, позволяя топливу течь из камеры синхронизации через клапан управления топливным форсункой и в проход подачи топлива.

![[fi800gh.png]]

В соответствующее время, как определено ECM, клапан управления топливным форсункой закрывается, улавливая топливо в камере синхронизации. Это захваченное топливо создает прочную гидравлическую связь между плунжером синхронизации и плунжером учета.

![[fi800gi.png]]

В результате дозирующий плунжер вынужден двигаться вниз с помощью плунжера времени.

Поскольку топливо захвачено, сила снижения на плунжере времени передается на плунжер учета, тем самым увеличивая давление в камере учета.

![[fi800gj.png]]

Когда это давление достигает примерно 34 474 кПа[5000 psi], игловой клапан начинает прижиматься вверх.

Продолжающееся движение по нисходящей линии таймингового плунжера и дозирующего плунжера приводит к неуклонному увеличению давления топлива. В результате топливо проталкивается через игловой клапан, через распылительные отверстия и в камеру сгорания.

![[fi800gk.png]]

Инъекция продолжается до тех пор, пока пропуск разлива измерительного плунжера не пройдет через порт разлива измерительного.

Давление в измерительной камере быстро падает, что позволяет игловому клапану резко закрываться. Это действие приводит к положительному концу инъекции. Положительный конец инъекции предотвращает дриблинг и приводит к более чистому горению.

Именно в этот момент клапан сброса давления «отключается», тем самым уменьшая эффекты «шика» высокого давления, который возникает во время разлива дозирования.

![[fi800gl.png]]

Сразу после открытия порта дозирования разлива верхний край дозирующего плунжера проходит порт разлива синхронизации.

![[fi800gm.png]]

Это действие позволяет топливу в камере синхронизации разливаться обратно в слив топлива, когда плунжер синхронизации завершает свое нисходящее движение.

Это завершает цикл инъекции.

![[fi800gn.png]]

![[fi100gr.png]]

форсунка Drivetrain

1. Форсунка
2. форсунка
3. Коромысло клапана
4. Штанга толкателя
5. Толкатель
6. Распределительный вал.


> [!quote]- Original (English) · английский оригинал
> ### Theory of Operation
>
> Hydromechanical Subsystem
>
> The 2002 ISM engine utilizes a different injector than the previous ISM engine, with flow characteristic changes and improved reliability. The injector is specially designed to maximize the benefit of cooled EGR and lower the emission levels.
>
> The fuel pump is located in the same location as a CELECT™ Plus fuel pump.
>
> The fuel pump is a gear type of pump. The assembly includes a pressure regulator, pulsation damper, and solenoid valve.
>
> 1. Pressure regulator
> 2. Pulsation damper
> 3. Solenoid valve.
>
> The ECM mounts on a cooling plate. During engine operation, fuel circulates through the cooling plate to absorb heat generated by the ECM.
>
> On CM876 engines, fuel flows from the fuel rifle at the rear of the engine to the aftertreatment shutoff valve. It then flows to the aftertreatment fuel injector.
>
> When fuel is **not** flowing to the injector, fuel remaining between the aftertreatment shutoff valve number 1 and aftertreatment fuel injector passes through the aftertreatment shutoff valve number 2 and goes to drain.
>
> The injector assembly includes a solenoid valve, which controls the end of the fuel metering and the beginning of injection. The solenoid valve is normally open. An electronic signal from the ECM closes the valve as required.
>
> The fuel system uses the camshaft to create adequate pressure for injection.
>
> A cutaway view of the electronically controlled injector with the internal components identified is illustrated.
>
> Injection Cycle
>
> At the start of metering, the metering plunger and the timing plunger are at the lower limits of their travel. The injector control valve is closed.
>
> As the camshaft rotates, the timing plunger return spring forces the timing plunger upward.
>
> Fuel flows past the metering check ball and into the metering chamber. This flow continues as long as the timing plunger is moving upward, and the injector control valve is closed.
>
> Supply pressure, acting on the bottom of the metering piston, forces it to maintain contact with the timing plunger.
>
> The ECM determines the end of metering by signaling the injector control valve to open.
>
> Fuel at supply pressure then flows into the timing chamber, thereby stopping metering piston travel.
>
> During this time, the bias spring makes sure the metering plunger remains stationary; that it does **not** drift upward as the timing plunger moves upward. This same force against the metering plunger results in enough fuel pressure below the piston to keep the metering check ball seated.
>
> A precisely metered quantity of fuel is now trapped in the metering chamber. This determines the quantity of fuel that will be injected.
>
> The timing plunger continues to move upward, and the timing chamber fills with fuel.
>
> The timing plunger begins its downward travel. Initially, the injector control valve remains open, allowing fuel to flow from the timing chamber, through the injector control valve, and into the fuel supply passage.
>
> At the appropriate time, as determined by the ECM, the injector control valve closes, trapping fuel in the timing chamber. This trapped fuel creates a solid hydraulic link between the timing plunger and the metering plunger.
>
> As a result, the metering plunger is forced to move downward with the timing plunger.
>
> Because the fuel is trapped, the downward force on the timing plunger is transferred to the metering plunger, thereby increasing pressure in the metering chamber.
>
> When this pressure reaches approximately 34,474 kPa \[5000 psi\], the needle valve begins to be forced upward.
>
> Continued downward movement of the timing plunger and metering plunger results in steadily increasing fuel pressure. The result is that fuel is forced past the needle valve, through the spray holes, and into the combustion chamber.
>
> Injection continues until the spill passage of the metering plunger passes the metering spill port.
>
> Metering chamber pressure drops rapidly, allowing the needle valve to close abruptly. This action results in a positive end of injection. The positive end of injection prevents dribble and results in cleaner burning.
>
> It is also at this point that the pressure relief valve "pops off”, thereby reducing the effects of the high-pressure "spike" that occurs at the time of the metering spill.
>
> Immediately after the metering spill port is opened, the upper edge of the metering plunger passes the timing spill port.
>
> This action allows the fuel in the timing chamber to be spilled back to the fuel drain as the timing plunger completes its downward movement.
>
> This completes the injection cycle.
>
> Injector Drivetrain
>
> 1. Injector
> 2. Injector link
> 3. Rocker lever
> 4. Push rod
> 5. Cam follower
> 6. Camshaft.
