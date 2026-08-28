---
aliases:
  - "Выключатель положения педали тормоза"
type: "Процедура"
doc: "99-019-088"
title_en: "Brake Pedal Position Switch"
title_ru: "Выключатель положения педали тормоза"
modified: "2015-06-29"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 9
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-088.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-088.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/99"
  - "перевод/машинный"
---

# Brake Pedal Position Switch
**Выключатель положения педали тормоза**

> [!abstract] Процедура · `99-019-088`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2015-06-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-088.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-088.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

> [!warning] ОСТОРОЖНО
> При устранении неполадок в цепи переключателя тормозной линии убедитесь, что переключатель давления тормоза идентифицирован. Переключатель давления тормозного света транспортного средства, который не является частью системы Signature, обычно ошибочно принимают за переключатель тормозной линии, используемый в системе Signature.

Переключатель положения педали тормоза определяет положение педали рабочего тормоза. Некоторые функции, такие как круиз-контроль и PTO, реагируют на состояние переключателя положения педали тормоза и отключаются при нажатии тормозов. Схема имеет обычно закрытый переключатель, обратный провод переключателя и сигнальный провод переключения положения педали тормоза провода проводов OEM. Переключатель положения педали тормоза установлен в стороне низкого давления пневматической тормозной системы транспортного средства. При нажатии на тормоза транспортного средства обычно закрытый переключатель открывает и отключает работу круиз-контроля.

![[19c01261.png]]

### Снятие

> [!danger] ОПАСНО
> Чтобы избежать травм или смерти, не применяйте тормоза транспортного средства, когда выключатель снят с фитинга тормозной линии.

Отсоедините проводку OEM от переключателя положения педали тормоза.

Удалите выключатель положения педали тормоза из фитинга.

![[eb8swha.png]]

### Установка

Установите новый переключатель положения педали тормоза в фитинг в соответствии с процедурами изготовителя транспортного средства.

![[eb8swhb.png]]

Подключите два проводных разъёма к переключателю положения педали тормоза.

![[eb8swhc.png]]

### Проверка сопротивления

Если имеется электронный инструмент, следите за переключателем положения педали тормоза для правильной работы. Если **не**, следуйте процедурам устранения неполадок в этом разделе.

Переключатель (1) положения педали тормоза будет расположен в тормозной линии (2) транспортного средства. Месторасположение будет зависеть от процедур установки OEM.

![[eb8swka.png]]

Отсоедините два проводных разъёма от переключателя положения педали тормоза.

![[eb8swkb.png]]

Подключите датчики мультиметра к клеммам переключателя положения педали тормоза.

Измерьте сопротивление.

Мультиметр **должен **показывать замкнутую цепь (10 Ом или меньше), когда тормоза **не **применяются. Если цепь **не** закрыта, замените выключатель положения педали тормоза.

![[eb8swkc.png]]

> [!warning] ОСТОРОЖНО
> Автомобиль должен иметь достаточное давление воздуха для активации тормозов.

Ударить педалью тормоза транспортного средства. Мультиметр **должен **показывать открытую схему (100к Ом или более), когда применяются тормоза. Если цепь **не** открыта, замените выключатель положения педали тормоза.

Если значение сопротивления правильное, переключатель должен быть проверен на короткое замыкание на землю.

![[eb8swkd.png]]

### Проверка на замыкание на массу

Прикоснитесь одним многометровым щупом к одному из терминалов переключателя положения педали тормоза. Прикоснитесь к другому многометровому щупу на земле шасси. Измерьте сопротивление. Мультиметр **должен **показывать открытую схему (100км или более), когда педаль тормоза выпущена. Если цепь **не** открыта, замените выключатель положения педали тормоза.

Если выключатель положения педали тормоза прошел все предыдущие проверки, подключите выключатель к проводах ремня. Схема переключения положения педали тормоза должна быть проверена.

![[eb8swke.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> **CAUTION · Осторожно**
> When troubleshooting the brake line switch circuit, make sure the brake pressure switch is identified. The vehicle brake light pressure switch, which is not a part of the Signature system, is commonly mistaken for the brake line switch used in the Signature system.
>
> The brake pedal position switch detects the position of the service brake pedal. Certain features such as cruise control and PTO respond to the state of the brake pedal position switch and disengage when the brakes are applied. The circuit has a normally-closed switch, switch return wire, and brake pedal position switch signal wire of the OEM harness. The brake pedal position switch is mounted in the low pressure side of the vehicle pneumatic brake system. When the vehicle brakes are applied, the normally-closed switch opens and disables the cruise control operation.
>
> ### Remove
>
> **WARNING · Опасно**
> To avoid personal injury or death, do not apply the vehicle brakes when the switch is removed from the brake line fitting.
>
> Disconnect the OEM harness from the brake pedal position switch.
>
> Remove the brake pedal position switch from the fitting.
>
> ### Install
>
> Install the new brake pedal position switch into the fitting according to the vehicle manufacturer's procedures.
>
> Connect the two wire connectors to the brake pedal position switch.
>
> ### Resistance Check
>
> If an electronic service tool is available, monitor the brake pedal position switch for proper operation. If **not**, follow the troubleshooting procedures in this section.
>
> The brake pedal position switch (1) will be located in the vehicle brake line (2). The location will depend on the OEM installation procedures.
>
> Disconnect the two wire connectors from the brake pedal position switch.
>
> Connect the probes of the multimeter to the brake pedal position switch terminals.
>
> Measure the resistance.
>
> The multimeter **must** show a closed circuit (10 ohms or less) when the brakes are **not** applied. If the circuit is **not** closed, replace the brake pedal position switch.
>
> **CAUTION · Осторожно**
> The vehicle must have enough air pressure to activate the brakes.
>
> Depress the vehicle brake pedal. The multimeter **must** show an open circuit (100k ohms or more) when the brakes are applied. If the circuit is **not** open, replace the brake pedal position switch.
>
> If the resistance value is correct, the switch **must** still be checked for a short circuit to ground.
>
> ### Check for Short Circuit to Ground
>
> Touch one multimeter probe to one of the brake pedal position switch terminals. Touch the other multimeter probe to chassis ground. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more) when the brake pedal is released. If the circuit is **not** open, replace the brake pedal position switch.
>
> If the brake pedal position switch passed all the previous checks, connect the switch to the wiring harness. The brake pedal position switch circuit **must** still be checked.
