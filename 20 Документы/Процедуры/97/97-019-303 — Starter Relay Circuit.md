---
aliases:
  - "Цепь реле стартера"
type: "Процедура"
doc: "97-019-303"
title_en: "Starter Relay Circuit"
title_ru: "Цепь реле стартера"
modified: "2003-06-13"
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
figures: 29
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-303.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-303.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
  - "перевод/машинный"
---

# Starter Relay Circuit
**Цепь реле стартера**

> [!abstract] Процедура · `97-019-303`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-06-13
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-303.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-303.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

Общие сведения

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы избежать травм, всегда проветривайте моторное отделение перед обслуживанием батарей. Чтобы избежать дуги, сначала удалите отрицательный (-) кабель батареи и прикрепите отрицательный (-) кабель батареи последним.

Переведите замок зажигания в положение OFF.

Отсоедините кабели аккумулятора автомобиля от батареи.

> [!note] Примечание
> Отключение аккумуляторных батарей автомобиля может потребовать сброса часов ECM в режиме реального времени с помощью INSITETM.

![[ea8coha.png]]

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте пробный щуп, номер детали 3822758 и 3822917, при проведении измерения.

Отсоедините стартовую реле от ремня электропроводки двигателя ICONTM.

Установите мультиметр для измерения сопротивления.

![[19802877.png]]

> [!note] Примечание
> Стартерная реле обычно открытая реле.

Прикосновение к одному из мультиметров приводит к контакту 87 стартера релейной проводов ремня разъема.

Прикосновение к другому мультиметру приводит к посту терминала батареи в сборке переключателя зажигания.

Считайте показания мультиметра.

![[19802878.png]]

Мультиметр **должен **отображать значение менее 10 Ом, что является замкнутой схемой.

Если цепь **не** закрыта, проверьте упряжку электропроводки двигателя ICONTM и части электропроводки кабины.

![[19801619.png]]

ICONTM двигательная проводка Side Check

Отсоедините 14-контактный проходной разъем на брандмауэре автомобиля.

Прикосновение к одному из мультиметров приводит к контакту 87 стартера релейной проводов ремня разъема. Прикосновение к другому мультиметру приводит к контакту L 14-контактного пропускного разъема, проводов двигателя с ремнями безопасности. Считайте показания мультиметра.

Мультиметр **должен **показывать показания менее 10 Ом, что является замкнутой схемой. Если схема **не** закрыта, отремонтируйте или замените электропроводку двигателя ICONTM. См. процедуру 019-204, 019-200 или[[97-019-043 — Engine Wiring Harness|019-043]].

![[19802879.png]]

Затем касание одного из мультиметров приводит к контакту 30 стартера релейной проводов с разъемом ремня. Прикосновение к другому мультиметру приводит к контакту N 14-контактного пропускного разъема, проводов двигателя с ремнями безопасности. Считайте показания мультиметра.

Мультиметр **должен **показывать показания менее 10 Ом, что является замкнутой схемой. Если схема **не** закрыта, отремонтируйте или замените электропроводку двигателя ICONTM. См. процедуру 019-204, 019-200 или[[97-019-043 — Engine Wiring Harness|019-043]].

![[19802879.png]]

Отсоедините 50-контактный разъем OEM-проводов от двигателя ECM (на двигателях Signature, ISX и ISM). Если ваше приложение является двигателем CELECTTM Plus, отсоедините 21-контактный OEM-разъем. Отсоедините разъем B модуля управления ICONTM от модуля управления ICONTM.

Прикосновение к одному из мультиметров приводит к контакту 85 стартера релейной проводов с ремнем разъема. Прикосновение к другому мультиметру приводит к контакту 5 с неработающим модулем управления ICONTM B проводов ремня разъема. Считайте показания мультиметра.

Затем касание одного из мультиметров приводит к контакту 86 стартера релейной проводов с разъемом ремня. Прикосновение к другому мультиметру приводит к контакту 6 с неработающим модулем управления ICONTM B проводов ремня разъема. Считайте показания мультиметра.

![[19802880.png]]

Для обеих проверок мультиметр **должен** отображать показания менее 10 Ом, что является замкнутой схемой.

Если схема **не** закрыта, отремонтируйте или замените электропроводку двигателя ICONTM. См. процедуру 019-204, 019-208 или[[97-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

Прикосновение к одному из мультиметров приводит к контакту 85 стартера релейной проводов с ремнем разъема. Прикосновение к другому мультиметру приводит к контакту 38 двигателя ECM с 50-контактным разъёмом проводов жгута (двигатели Signature, ISX и ISM).

Если ваше приложение является двигателем CELECTTM Plus, коснитесь другого многометрового привода, чтобы связаться с A 21-контактного разъема OEM-проводов. Считайте показания мультиметра.

![[19802881.png]]

Мультиметр **должен **отображать значение менее 10 Ом, что является замкнутой схемой.

Если схема **не** закрыта, отремонтируйте или замените электропроводку двигателя ICONTM. См. процедуру 019-204 или[[97-019-043 — Engine Wiring Harness|019-043]].

Или, отремонтировать или заменить двигатель OEM разъемом. Смотрите соответствующее руководство по устранению неполадок и ремонту базового двигателя.

![[19801619.png]]

ICONTM Cab Wiring Sweet Side Check (недоступная ссылка)

Прикосновение к одному из мультиметров приводит к контакту L 14-контактного пропускного разъема, проводов кабины с ремнями безопасности. Прикосновение к другому мультиметру приводит к посту терминала батареи в сборке переключателя зажигания. Считайте показания мультиметра.

Мультиметр **должен **показывать показания менее 10 Ом, что является замкнутой схемой. Если цепь **не** закрыта, отремонтируйте или замените проводку кабины. См. процедуру 019-200, 019-197 или[[97-019-305 — Cab Wiring Harness|019-305]].

![[19802882.png]]

Прикосновение к одному из мультиметров приводит к контакту N 14-контактного пропускного разъема, проводов кабины с ремнями безопасности. Прикоснитесь к другому мультиметру, который ведет к магнитному переключателю провода терминала (переключатель расположен на стартере). Считайте показания мультиметра.

Мультиметр **должен **показывать показания менее 10 Ом, что является замкнутой схемой.

Если цепь **не** закрыта, проверьте целостность сплайса прикладного магнитного переключателя провода на проводку кабины ICONTM с магнитным переключателем силового провода (провода № 017). Если сплайс приклада хорош, отремонтируйте или замените проводку кабины. См. процедуру 019-200 или[[97-019-305 — Cab Wiring Harness|019-305]].

После ремонта подсоедините все компоненты.

![[19802883.png]]

### Проверка на замыкание на массу

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы избежать травм, всегда проветривайте моторное отделение перед обслуживанием батарей. Чтобы избежать дуги, сначала удалите отрицательный (-) кабель батареи и прикрепите отрицательный (-) кабель батареи последним.

Переведите замок зажигания в положение OFF. Отсоедините кабели аккумулятора автомобиля и разъемы для проводов аккумулятора ICONTM от батареи.

> [!note] Примечание
> Отключение аккумуляторных батарей автомобиля может потребовать сброса часов ECM в режиме реального времени с помощью INSITETM.

![[ea8coha.png]]

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте пробный щуп, номер детали 3822758, при проведении измерения.

Установите мультиметр для измерения сопротивления.

Прикосновение к одному из мультиметров приводит к посту терминала батареи в сборке переключателя зажигания.

Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

![[19802884.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если схема **не **открыта, есть короткое замыкание на землю.

Изолируйте короткую кабину проводов ремня или ICONTM двигатель проводов ремня часть цепи.

![[19801621.png]]

Отсоедините 14-контактный проходной разъем на брандмауэре автомобиля.

Прикосновение к одному из мультиметров приводит к контакту L 14-контактного пропускного разъема, проводов двигателя с ремнями безопасности. Прикоснитесь к другому мультиметру, который ведет на землю. Считайте показания мультиметра.

Затем повторите проверку от контакта N 14-контактного пропускного разъема, стороны ремня электропроводки двигателя, до заземления блока двигателя. Считайте показания мультиметра.

![[19c00940.png]]

Для обеих проверок с помощью штифта на землю мультиметр **должен **отображать показания более 100k ом, что является открытой схемой.

Если цепь открыта, короткое замыкание находится на стороне проводов кабины. Ремонт или замена кабины проводов ремня. См. процедуру 019-197, 019-200 или[[97-019-305 — Cab Wiring Harness|019-305]].

Если схема **не** открыта, отремонтируйте или замените электропроводку двигателя ICONTM. См. процедуру 019-200 или[[97-019-043 — Engine Wiring Harness|019-043]].

После ремонта подсоедините все компоненты.

![[19801621.png]]

### Проверка на замыкание между контактами

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы избежать травм, всегда проветривайте моторное отделение перед обслуживанием батарей. Чтобы избежать дуги, сначала удалите отрицательный (-) кабель батареи и прикрепите отрицательный (-) кабель батареи последним.

Переведите замок зажигания в положение OFF. Отсоедините кабели аккумулятора автомобиля и разъемы для проводов аккумулятора ICONTM от батареи.

> [!note] Примечание
> Отключение аккумуляторных батарей автомобиля может потребовать сброса часов ECM в режиме реального времени с помощью INSITETM.

![[ea8coha.png]]

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте пробный щуп, номер детали 3822758 и 3822917, при проведении измерения.

Отключите 14-контактный проходной разъем на брандмауэре автомобиля.

Установите мультиметр для измерения сопротивления.

![[15800040.png]]

Прикосновение к одному из мультиметров приводит к контакту L 14-контактного пропускного разъема, проводов кабины с ремнями безопасности. Прикосновение к другому мультиметру приводит ко всем другим штифтам в разъеме, по одному за раз. Прочитайте значение, отображаемое на мультиметре для каждой проверки контакта с контактом.

Затем повторите проверку контакта с контактом от контакта N 14-контактного проходного разъема, стороны проводов кабины, ко всем другим штифтам в разъеме. Прочитайте значение, отображаемое на мультиметре для каждой проверки контакта с контактом.

![[19c00935.png]]

Для каждой проверки контакта с контактом мультиметр **должен отображать показания более 100k Ом, что является открытой схемой. Если какая-либо схема **не открыта, то имеется короткое замыкание от контакта L (или контакта N) до любого другого штифта в разъеме, который зарегистрировал замкнутую схему.

Ремонт или замена кабины проводов ремня. См. процедуру 019-200 или[[97-019-305 — Cab Wiring Harness|019-305]].

Проверьте проводку двигателя на стороне разъема.

![[19801621.png]]

Прикосновение к одному из мультиметров приводит к контакту L 14-контактного пропускного разъема, проводов двигателя с ремнями безопасности. Прикосновение к другому мультиметру приводит ко всем другим штифтам в разъеме, по одному за раз. Прочитайте значение, отображаемое на мультиметре для каждой проверки контакта с контактом.

Затем повторите проверку контакта с контактом от контакта N 14-контактного пропускного разъема, стороны проводов двигателя, до всех других контактов в разъеме. Прочитайте значение, отображаемое на мультиметре для каждой проверки контакта с контактом.

![[19c00942.png]]

Для каждой проверки контакта с контактом мультиметр **должен отображать показания более 100k Ом, что является открытой схемой. Если какая-либо схема **не открыта, то имеется короткое замыкание от контакта L (или контакта N) до любого другого штифта в разъеме, который зарегистрировал замкнутую схему.

Ремонт или замена ремня электропроводки двигателя ICONTM. См. процедуру 019-200 или[[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Отсоедините стартовую реле от жгута проводов двигателя.

Прикосновение к одному из мультиметров приводит к контакту 87 релейной проводов ремня разъема.

Прикосновение к другому мультиметру приводит ко всем другим штифтам в разъеме, по одному за раз.

Считайте показания мультиметра.

![[19802885.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой. Если схема **не** открыта, то в разъеме есть короткое замыкание от контакта 87 до любого другого штифта, который зарегистрировал замкнутую цепь.

Ремонт или замена реле-коннектора или реле-коннектора.

См. процедуру 019-204 или[[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Повторите проверку контакта с контактами 85, 86 и 30 разъёма реле стартера для подключения к другим штифтам в разъеме. Прочитайте значение, отображаемое на мультиметре для каждой проверки контакта с контактом.

Для каждой проверки контакта с контактом мультиметр **должен отображать показания более 100k Ом, что является открытой схемой. Если какая-либо схема **не открыта, то в разъеме имеется короткое замыкание от контакта 85 (или 86 или 30) до любого другого штифта, который зарегистрировал замкнутую схему.

Ремонт или замена реле-коннектора или реле-коннектора. См. процедуру 019-204 или[[97-019-043 — Engine Wiring Harness|019-043]].

После ремонта подсоедините все компоненты.

![[19802885.png]]

### Проверка напряжения

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте пробный щуп, номер детали 3822917, при проведении измерения.

Отсоедините 14-контактный проходной разъем на брандмауэре автомобиля.

Установите мультиметр для измерения VDC.

Переведите замок зажигания в положение ON.

![[15800040.png]]

Прикосновение к одному из мультиметров приводит к контакту L 14-контактного пропускного разъема, проводов кабины с ремнями безопасности. Прикоснитесь к другому мультиметру, который ведет на землю. Считайте показания мультиметра.

Затем повторите проверку напряжения от контакта N 14-контактного пропускного разъема, стороны проводов кабины, до заземления блока двигателя. Считайте показания мультиметра.

![[19c00933.png]]

Для проверки от контакта L до земли мультиметр **должен **отображать показания более 12 VDC. Для проверки от контакта N до земли мультиметр **должен** отображать показания 0 VDC.

Если показания напряжения **не** являются правильными для каждого штифта, отремонтируйте или замените проводку кабины. См. процедуру 019-197, 019-200 или[[97-019-305 — Cab Wiring Harness|019-305]].

После ремонта подсоедините все компоненты.

![[19802886.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> General Information
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first, and attach the negative (-) battery cable last.
>
> Turn the keyswitch to the OFF position.
>
> Disconnect the vehicle battery cables from the battery.
>
> **Note · Примечание**
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset using INSITE™.
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.
>
> Disconnect the starter relay from the ICON™ engine harness.
>
> Set the multimeter to measure resistance.
>
> **Note · Примечание**
> The starter relay is a normally open relay.
>
> Touch one of the multimeter leads to pin 87 of the starter relay harness connector.
>
> Touch the other multimeter lead to the battery terminal post in the keyswitch assembly.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.
>
> If the circuit is **not** closed, check the ICON™ engine harness and cab harness portions of the circuit.
>
> ICON™ Engine Harness Side Check
>
> Disconnect the 14-pin pass-through connector at the vehicle's firewall.
>
> Touch one of the multimeter leads to pin 87 of the starter relay harness connector. Touch the other multimeter lead to pin L of the 14-pin pass-through connector, engine harness side. Read the value displayed on the multimeter.
>
> The multimeter **must** show a reading of less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, repair or replace the ICON™ engine harness. Refer to Procedure 019-204, 019-200, or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Then, touch one of the multimeter leads to pin 30 of the starter relay harness connector. Touch the other multimeter lead to pin N of the 14-pin pass-through connector, engine harness side. Read the value displayed on the multimeter.
>
> The multimeter **must** show a reading of less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, repair or replace the ICON™ engine harness. Refer to Procedure 019-204, 019-200, or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Disconnect the engine ECM 50-pin OEM harness connector from the engine ECM (on Signature, ISX, and ISM engines). If your application is a CELECT™ Plus engine, disconnect the engine 21-pin OEM connector. Disconnect the ICON™ idle control module B connector from the ICON™ idle control module.
>
> Touch one of the multimeter leads to pin 85 of the starter relay harness connector. Touch the other multimeter lead to pin 5 of the ICON™ idle control module B harness connector. Read the value displayed on the multimeter.
>
> Then, touch one of the multimeter leads to pin 86 of the starter relay harness connector. Touch the other multimeter lead to pin 6 of the ICON™ idle control module B harness connector. Read the value displayed on the multimeter.
>
> For both checks, the multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.
>
> If the circuit is **not** closed, repair or replace the ICON™ engine harness. Refer to Procedure 019-204, 019-208, or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Touch one of the multimeter leads to pin 85 of the starter relay harness connector. Touch the other multimeter lead to pin 38 of the engine ECM 50-pin harness connector (Signature, ISX, and ISM engines).
>
> If your application is a CELECT™ Plus engine, touch the other multimeter lead to pin A of the 21-pin OEM harness connector. Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.
>
> If the circuit is **not** closed, repair or replace the ICON™ engine harness. Refer to Procedure 019-204 or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Or, repair or replace the engine OEM connector. Refer to the appropriate base engine troubleshooting and repair manual.
>
> ICON™ Cab Harness Side Check
>
> Touch one of the multimeter leads to pin L of the 14-pin pass-through connector, cab harness side. Touch the other multimeter lead to the battery terminal post in the keyswitch assembly. Read the value displayed on the multimeter.
>
> The multimeter **must** show a reading of less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, repair or replace the cab harness. Refer to Procedure 019-200, 019-197, or [[97-019-305 — Cab Wiring Harness|019-305]].
>
> Touch one of the multimeter leads to pin N of the 14-pin pass-through connector, cab harness side. Touch the other multimeter lead to the magnetic switch wire terminal post (switch is located on the starter). Read the value displayed on the multimeter.
>
> The multimeter **must** show a reading of less than 10 ohms, which is a closed circuit.
>
> If the circuit is **not** closed, check the integrity of the butt splice of the starter magnetic switch wire to the ICON™ cab harness magnetic switch power wire (wire Number 017). If the butt splice is good, repair or replace the cab harness. Refer to Procedure 019-200 or [[97-019-305 — Cab Wiring Harness|019-305]].
>
> Connect all components after completing the repair.
>
> ### Check for Short Circuit to Ground
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> Turn the keyswitch to the OFF position. Disconnect the vehicle battery cables and ICON™ battery harness connectors from the battery.
>
> **Note · Примечание**
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset using INSITE™.
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use test lead, Part Number 3822758, when taking a measurement.
>
> Set the multimeter to measure resistance.
>
> Touch one of the multimeter leads to the battery terminal post in the keyswitch assembly.
>
> Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, there is a short circuit to ground.
>
> Isolate the short to the cab harness or ICON™ engine harness portion of the circuit.
>
> Disconnect the 14-pin pass-through connector at the vehicle's firewall.
>
> Touch one of the multimeter leads to pin L of the 14-pin pass-through connector, engine harness side. Touch the other multimeter lead to ground. Read the value displayed on the multimeter.
>
> Then, repeat the short-to-ground check from pin N of the 14-pin pass-through connector, engine harness side, to engine block ground. Read the value displayed on the multimeter.
>
> For both pin-to-ground checks, the multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is open, the short circuit is on the cab harness side of the circuit. Repair or replace the cab harness. Refer to Procedure 019-197, 019-200, or [[97-019-305 — Cab Wiring Harness|019-305]].
>
> If the circuit is **not** open, repair or replace the ICON™ engine harness. Refer to Procedure 019-200 or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Connect all components after completing the repair.
>
> ### Check for Short Circuit from Pin to Pin
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> Turn the keyswitch to the OFF position. Disconnect the vehicle battery cables and ICON™ battery harness connectors from the battery.
>
> **Note · Примечание**
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset using INSITE™.
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.
>
> Disconnect the 14-pin pass-through connector on the vehicle's firewall.
>
> Set the multimeter to measure resistance.
>
> Touch one of the multimeter leads to pin L of the 14-pin pass-through connector, cab harness side. Touch the other multimeter lead to all other pins in the connector, one at a time. Read the value displayed on the multimeter for each pin-to-pin check.
>
> Then, repeat the pin-to-pin check from pin N of the 14-pin pass-through connector, cab harness side, to all other pins in the connector. Read the value displayed on the multimeter for each pin-to-pin check.
>
> For each pin-to-pin check, the multimeter **must** display a reading of more than 100k ohms, which is an open circuit. If any circuit is **not** open, there is a short circuit from pin L (or pin N) to any other pin in the connector that registered a closed circuit.
>
> Repair or replace the cab harness. Refer to Procedure 019-200 or [[97-019-305 — Cab Wiring Harness|019-305]].
>
> Check the engine harness side of the connector.
>
> Touch one of the multimeter leads to pin L of the 14-pin pass-through connector, engine harness side. Touch the other multimeter lead to all other pins in the connector, one at a time. Read the value displayed on the multimeter for each pin-to-pin check.
>
> Then, repeat the pin-to-pin check from pin N of the 14-pin pass-through connector, engine harness side, to all other pins in the connector. Read the value displayed on the multimeter for each pin-to-pin check.
>
> For each pin-to-pin check, the multimeter **must** display a reading of more than 100k ohms, which is an open circuit. If any circuit is **not** open, there is a short circuit from pin L (or pin N) to any other pin in the connector that registered a closed circuit.
>
> Repair or replace the ICON™ engine harness. Refer to Procedure 019-200 or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Disconnect the starter relay from the engine harness.
>
> Touch one of the multimeter leads to pin 87 of the relay harness connector.
>
> Touch the other multimeter lead to all other pins in the connector, one at a time.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short circuit from pin 87 to any other pin in the connector that registered a closed circuit.
>
> Repair or replace the engine harness or relay connector.
>
> Refer to Procedure 019-204 or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Repeat the pin-to-pin check from pins 85, 86, and 30 of the starter relay harness connector to all other pins in the connector. Read the value displayed on the multimeter for each pin-to-pin check.
>
> For each pin-to-pin check, the multimeter **must** display a reading of more than 100k ohms, which is an open circuit. If any circuit is **not** open, there is a short circuit from pin 85 (or 86 or 30) to any other pin in the connector that registered a closed circuit.
>
> Repair or replace the engine harness or relay connector. Refer to Procedure 019-204 or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Connect all components after completing the repair.
>
> ### Voltage Check
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use test lead, Part Number 3822917, when taking a measurement.
>
> Disconnect the 14-pin pass-through connector at the vehicle's firewall.
>
> Set the multimeter to measure VDC.
>
> Turn the keyswitch to the ON position.
>
> Touch one of the multimeter leads to pin L of the 14-pin pass-through connector, cab harness side. Touch the other multimeter lead to ground. Read the value displayed on the multimeter.
>
> Then, repeat the voltage check from pin N of the 14-pin pass-through connector, cab harness side, to engine block ground. Read the value displayed on the multimeter.
>
> For the check from pin L to ground, the multimeter **must** display a reading of greater than 12 VDC. For the check from pin N to ground, the multimeter **must** display a reading of 0 VDC.
>
> If the voltage readings are **not** the correct VDC for each pin, repair or replace the cab harness. Refer to Procedure 019-197, 019-200, or [[97-019-305 — Cab Wiring Harness|019-305]].
>
> Connect all components after completing the repair.
