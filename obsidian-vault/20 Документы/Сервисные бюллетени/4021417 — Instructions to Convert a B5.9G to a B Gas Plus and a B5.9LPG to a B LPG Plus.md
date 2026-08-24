---
aliases:
  - "Инструкции по переоборудованию B5.9G в B Gas Plus и B5.9LPG в B LPG Plus"
type: "Сервисный бюллетень"
doc: "4021417"
title_en: "Instructions to Convert a B5.9G to a B Gas Plus and a B5.9LPG to a B LPG Plus"
title_ru: "Инструкции по переоборудованию B5.9G в B Gas Plus и B5.9LPG в B LPG Plus"
released: "2003-01-01"
modified: "2017-04-04"
group: "00 - Complete Engine / Troubleshooting"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
parts:
  - "3617958"
  - "3617959"
  - "3900589"
  - "3900629"
  - "3900630"
  - "3900631"
  - "3900632"
  - "3900678"
  - "3901445"
  - "3902460"
  - "3906216"
  - "3909025"
  - "3939258"
figures: 22
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/4021417.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/bulletin/4021417.pdf"
tags:
  - "документ/бюллетень"
  - "двигатель/NT/NTA855"
  - "перевод/машинный"
  - "тема/complete-engine-troubleshooting"
---

# Instructions to Convert a B5.9G to a B Gas Plus and a B5.9LPG to a B LPG Plus
**Инструкции по переоборудованию B5.9G в B Gas Plus и B5.9LPG в B LPG Plus**

> [!abstract] Сервисный бюллетень · `4021417`
> **Раздел Cummins:** 00 - Complete Engine / Troubleshooting
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Даты:** выпущен 2003-01-01 · изменён 2017-04-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/4021417.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/bulletin/4021417.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Инструкции по переоборудованию B5.9G в B Gas Plus и B5.9LPG в B LPG Plus

**Подготовительные мероприятия**

Двигатели B Gas Plus и B LPG Plus требуют использования блока цилиндров ISB (STORM). Двигатели B5.9G и B5.9LPG, построенные после марта 1997 года, были построены с этим блоком цилиндров. Тип установки в масляной винтовке может идентифицировать блок цилиндров. Правильная фитинговая установка - прямое ниточное кольцо M14. Старый блок имеет резьбу трубы.

После завершения этого обновления, табличка с данными двигателя ** должна быть проштампована новой CPL. Об этой модификации двигателя *** необходимо сообщить в Cummins Warranty с использованием формы Cummins Form 1877 (Уведомление об изменении двигателя), которое можно найти в руководстве по управлению гарантиями.

Удалите следующие компоненты:

- Турбокомпрессор и выхлопной адаптер
- Взятие коллектора крышки и сборка дросселя
- Корпус узла управления подачей топлива
- Электронный модуль управления (ECM)
- Модуль управления зажиганием (ICM)
- Жгут проводов двигателя.

![[05900762.png]]

** ECM**

Прикрепите ECM, номер детали 3937299, к блоку цилиндров с помощью прокладок, номер детали 3936236, под левым и правым ушами. Центральная вкладка и левое ухо удерживаются болтами, номер детали[[3900631]]. Правое ухо удерживается болтами, номер детали[[3909025]].

> [!note] Примечание
> Правые болты уха являются общими с кронштейном модуля управления зажиганием (ICM).

Заменить шпиль в блоке подъемного насоса на пластину с болтами M8x20, номер детали[[3900630]](природный газ** только**).

Для B LPG Plus установите блок-офф лифтового насоса, номер детали 3948083 и прокладку, номер детали[[3939258]]. Гора с двумя болтами M8x20, номер детали[[3900630]].

См. процедуру 019-031 в Руководстве по устранению неполадок и ремонту - Электроника, Газ Плюс Двигатели, Вестник 4021317.

![[05900763.png]]

**Давление масла/температурный датчик**

Вставьте датчик давления/температуры масла, часть 3417195, в резьбовое отверстие ниже ECM и слева от подъемного насоса блокировать пластину.

См. процедуру 019-155 в Руководстве по устранению неполадок и ремонту - Электроника, Газ Плюс Двигатели, Вестник 4021317.

![[05900764.png]]

** Корпус управления топливом**

Удалите датчик потока газа и клапан отключения топлива (природный газ только **) из первоначального корпуса.

Установите новый экранный блок, Номер детали 3929159, и запорный клапан (только природный газ) или крышку, Номер детали 3964363 (только СНГ) в основании нового корпуса управления топливом, Номер детали 3938872.

Установите 45-градусный разъем, номер детали 200293, в впускном порту топлива (2).

Корпус датчика потока газа удерживается на месте с четырьмя болтами M5, Номер детали 3253888, сверху, а не с помощью сквозного болта.

Заменить 90-градусное топливное соединение, установленное на верхней части адаптера датчика потока газовой массы, на прямое фитинговое устройство, номер детали 129866.

См. процедуру 005-009 в Руководстве по устранению неполадок и ремонту, серия В - Природный газ, Вестник 3666164.

![[05900734.png]]

Установите новое кольцо на корпус управления топливом.

Прикрепите корпус управления топливом с теми же гайками.

См. процедуру 005-009 в Руководстве по устранению неполадок и ремонту, серия В - Природный газ, Вестник 3666164.

![[05900765.png]]

**Кронштейн модуля зажигания**

Прикрепить модуль зажигания, номер детали 3938875.

Кронштейн удерживается одним болтом M8x55 (1), номер детали[[3909025]], один болт M8x80 (2), номер детали 3902112, два болта M8x35 (3), номер детали[[3900632]]и один стад M8xM6 (4), номер детали 3923022.

> [!note] Примечание
> Студ, номер детали[[3909025]], является общим с правильной вкладкой крепления ECM.

> [!note] Примечание
> болты, номер детали 3923022, установлены в левом нижнем углу скобки ICM. Шпилька используется для крепления наземного терминала проводов двигателя. Используйте орех M6, номер детали[[3906216]].

> [!note] Примечание
> Если левый боковой стартер используется с стартерным соленоидом сверху, может возникнуть проблема помех с регулятором низкого давления или испарителем. Первый вариант необходимо будет изменить.

![[05900766.png]]

** Корпус регулятора давления (только природный газ)**

Корпус регулятора давления, номер детали 3938679, крепится к скобке с болтами 1-M10x95, номер детали 3908226 и 3-M10x25, номер детали[[3902460]].

Направьте корпус регулятора давления так, чтобы фитинги были обращены влево (вперед).

> [!note] Примечание
> Возможно, потребуется заменить топливный выпускной фитинг (нижний) на 90-градусный фитинг, часть 129859, если он уже установлен.

> [!note] Примечание
> Первичный датчик давления топлива, часть 3330527, включен в сборку регулятора давления.

См. процедуру 005-047 в Руководстве по устранению неполадок и ремонту, серия B - Природный газ, Вестник 3666164.

![[05900767.png]]

**Сборка испарителя топлива (только для СНГ)**

Сборка испарителя, номер детали 3964356, крепится к кронштейну модуля зажигания с болтами 4-M10x25, номер детали[[3902460]].

> [!note] Примечание
> Первичный датчик давления топлива, часть 3330527, включен в сборку испарителя.

Замените две трубки охлаждающей жидкости номерами 3967820 и 3967822.

См. процедуру 005-094 в Руководстве по устранению неполадок и ремонту, серия B - Природный газ, Вестник 3666164.

> [!note] Примечание
> Линия охлаждающей жидкости, которая соединена в корпусе термостата, соединяется с бортовой установкой на испарителе.

![[05900769.png]]

** Модуль зажигания/OEM-подключатель**

Прикрепить модуль зажигания к кронштейну модуля зажигания. Модуль должен быть ориентирован с двумя разъемами для катушек зажигания с левой стороны (вперед). Разъем OEM, номер детали 3938921, установлена за двумя верхними крепежными болтами ICM.

4-M8x40, номер детали[[3900678]]- Болты.

См. процедуру 019-105 в Руководстве по устранению неполадок и ремонту - Электроника, Газ Плюс Двигатели, Вестник 4021317.

![[05900767.png]]

** Железнодорожная проводка**

Установите жгут для проводов двигателя, номер детали 3938919. Разъемы ECM закодированы для обеспечения правильной ориентации.

Установите OEM-разъемы в кронштейне OEM-разъема. Используйте стиральные машины, часть Номер[[3617959]], и орехи, часть номер[[3617958]]Для обеспечения безопасности разъемов.

Подключите наземный терминал к нижней левой кронштейнной шпильке ICM с гайкой M6, номер детали[[3906216]].

Соедините два p-клипа. Передний р-затвор крепится к верхнему наружному болту топливного корпуса. Второй крепится к блоку за воздушным компрессором с болтами, номер детали[[3900629]]. Он установлен в верхнем монтажном отверстии.

Подключите жгут проводов двигателя к датчикам и исполнительным механизмам, когда они установлены на двигателе.

См. процедуру 019-043 в Руководстве по устранению неполадок и ремонту - Электроника, Газ Плюс Двигатели, Вестник 4021317.

![[19901339.png]]

**Склады для подачи топлива**

Подсоедините шланг подачи топлива к корпусу регулятора низкого давления или испарителю и корпусу управления топливом, номер детали 3930037.

> [!note] Примечание
> 90-градусный конец шланга соединяется с корпусом регулятора низкого давления.

![[05900770.png]]

**Взять крышку коллектора**

Сборка дроссельной заслонки может быть прикреплена к крышке впускного коллектора на двигателе или вне его.

Вставьте резьбовые стержни, Номер детали 3992127, в крышку впускного коллектора, Номер детали 3938881.

> [!note] Примечание
> Установите четыре кольца, часть 145582, между каждой спаривающейся поверхностью.

Прикрепить привод дроссельной заслонки, номер детали 3992126, к впускному коллектору.

Прикрепите опорную кронштейн дроссельной заслонки, Номер детали 3992124, к приводу дроссельной заслонки и крышке впускного коллектора; используйте три конических болта, Номер детали 3284216.

![[10900296.png]]

Сдвиньте корпус смесителя, номер детали 3938871, на резьбовые стержни.

Установите четыре ореха, номер детали[[3900589]].

Установите впускной локоть, номер детали 3938918, используя оригинальное оборудование впускного локоть.

Новый впускной локоть имеет резерв для датчика влажности. Локтел может быть ориентирован прямо вверх или прямо наружу.

См. процедуру 005-052 в Руководстве по устранению неполадок и ремонту, серия B - Природный газ, Вестник 3666164.

![[05900737.png]]

** Купельный джампер Хосе**

Установите 90-градусный фитинг, номер детали 129859, в корпус топливного смесителя.

Установите клапан управления топливом, номер детали 3938841-природный газ или номер детали 3938870-LPG, в корпус топливного смесителя.

Подключите дом топливных перемычек, номер детали 3938932, к 90-градусной установке на корпусе смесителя. Если впускной/дроссельной сборки собирается на двигателе, подсоедините шланг к адаптеру датчика потока газа. В противном случае, сделать соединение после того, как впускной коллектор сборки установлен на двигателе.

Установите катушки зажигания после того, как впускной коллектор установлен на двигателе. См. процедуру 013-012 в Руководстве по устранению неполадок и ремонту, серия В - Природный газ, Вестник 3666164.

См. процедуру 005-052 в Руководстве по устранению неполадок и ремонту, серия B - Природный газ, Вестник 3666164.

![[05900771.png]]

**Тепловое давление/температурный датчик, вторичный**

Установите датчик давления/температуры топлива, номер детали 3417195, в корпус смесителя.

См. процедуру 019-053 в Руководстве по устранению неполадок и ремонту - Электроника, Газ Плюс Двигатели, Вестник 4021317.

![[19901340.png]]

** Давление на коллекторе впуска/температурный датчик**

Установите датчик давления/температуры впускного коллектора, номер детали 4009913.

Установите пробку в оставшиеся два отверстия в впускном коллекторе.

См. процедуру 019-099 в Руководстве по устранению неполадок и ремонту - Электроника, Газ Плюс Двигатели, Вестник 4021317.

![[19901341.png]]

**Стучать датчики**

Двигатель оснащен двумя датчиками детонации, номер детали 3607945.

Передний датчик расположен на верхней части крышки впускного коллектора и имеет крепежный болт с передним внутренним болтом. Для установки датчика требуется более длинный болт, M8x45, часть Номер[[3901445]].

Задний датчик расположен ниже кронштейна модуля зажигания. На двигателе есть начальник с двумя резьбовыми отверстиями. Датчик расположен в нижней дыре и установлен с использованием шпильки датчика детонации, номер детали 3992125 и гайка M8, номер детали.[[3900589]].

См. процедуру 019-346 в Руководстве по устранению неполадок и ремонту - Электроника, Газ Плюс Двигатели, Вестник 4021317.

![[19901342.png]]

** Датчик обратного давления**

Датчик обратного давления выхлопных газов, номер детали 3348579, установлен на верхней части впускного коллектора в адаптере датчика, номер детали 3938873. Сенсорная кронштейна установлена с болтами, часть номер 3937181.

Датчик подключается к адаптеру выхлопных газов через трубку из нержавеющей стали. Номер детали трубки варьируется в зависимости от конфигурации турбокомпрессора.

Смотрите раздел турбокомпрессора для деталей выбора трубки.

См. процедуру 019-347 в Руководстве по устранению неполадок и ремонту - Электроника, Газ Плюс Двигатели, Вестник 4021317.

![[19901343.png]]

** Зажигательная проводка**

Подсоедините жгут зажигания, номер детали 3938920, к модулю зажигания и к обоим катушкам зажигания.

См. процедуру 013-037 в Руководстве по устранению неполадок и ремонту, серия В - Природный газ, Вестник 3666164.

![[19901344.png]]

** Турбокомпрессор**

B Gas Plus имеет несколько вариантов конфигурации турбокомпрессора. Турбокомпрессор и адаптер выхлопных газов необходимо будет заменить вместе с установкой трубки датчика обратного давления выхлопных газов.

Смотрите следующую диаграмму для деталей опциона.

| Диаграмма совместимости трубок давления выхлопа |  |  |  |  |
|---|---|---|---|---|
|  | Адаптер выхлопа |  |  |  |
|  | 90-градусный локоть | 90-градусный локоть (Rotatable) | Прямо из |  |
| Выпускной коллектор | XS 9260 | XS 9266 | XS 9259 |  |
| LMRO | ТБ 9795 | Не применяется | PH 9051 | PH 9843 |
| LMFO | ТБ 97003 | PH 9844 | Не применяется | Не применяется |

| Вариант Часть Номер Список |  |  |  |
|---|---|---|---|
| Номер опции | Вариант Часть Номер | Требуемая фитинг | Турбокомпрессор |
| XS 9260 | 3992179 | 68138 | Не применяется |
| XS 9266 | 3992179 | 3992178 | Не применяется |
| XS 9259 | 3938917 | 68138 | Не применяется |
| PH 9844 | 3938929 | Не применяется | Не применяется |
| PH 9051 | 3992224 | Не применяется | Не применяется |
| PH 9843 | 3938926 | Не применяется | Не применяется |
| ТБ 9795 | Не применяется | Не применяется | 3599492 |
| ТБ 97003 | Не применяется | Не применяется | 3599493 |

![[10900297.png]]

## Список частей конверсии

| Номер детали | Часть описание | Количество | НГ | сжиженный газ |
|---|---|---|---|---|
| 68183 | 3/8 дюйма до 1/4 дюйма NPT | 1 | Да | Да |
| 129859 | 90-градусная арматура | 1 | Да | Нет |
| 129866 | прямая подгонка | 1 | Да | Да |
| 145582 | Throttle/mixer o-rings (4) | 4 | Да | Да |
| 200293 | 45-градусная арматура | 1 | Да | Да |
| 3253888 | 3.2.1.3 Установочные болты GMFS M5 | 4 | Да | Да |
| 3284216 | Винты с приводом/смешивателем кронштейнов | 3 | Да | Да |
| 3348579 | Датчик давления | 1 | Да | Да |
| 3417195 | Датчик давления топлива в масле комбинированный | 2 | Да | Да |
| 3599492 | Турбокомпрессор LMRO | 1 из 2 | Да | Да |
| 3599493 | Турбокомпрессор LMFO | 1 из 2 | Да | Да |
| 3607945 | Стучать датчик | 2 | Да | Да |
| [[3617959]] | ОЭМ соединительная стиральная машина | 2 | Да | Да |
| [[3900589]] | Орехи - топливный смеситель М8 | 5 | Да | Да |
| 3925883 | движок шнурка p-clip | 1 | Да | Да |
| [[3900631]] | Холдс-холдс ECM - M8x25 | 4 | Да | Да |
| [[3900632]] | Удерживающие кронштейны IM - M8x35 | 2 | Да | Да |
| [[3900678]] | Холдс-холдс IM - M8x40 | 4 | Да | Да |
| [[3901445]] | Затворы M8x45 | 1 | Да | Да |
| 3902112 | Удерживающие кронштейны IM - M8x80 | 1 | Да | Да |
| [[3902460]] | Регулятор давления болтов M10x25 | 3 | Да | Нет |
| [[3902460]] | болты M10x25 - установка испарителя | 4 | Нет | Да |
| [[3906216]] | Nut - двигательная проводка упряжка грунта М6 | 1 | Да | Да |
| 3908226 | Регулятор давления M10x95 | 1 | Да | Нет |
| [[3909025]] | Удерживающая петля ECM/IM скобка M8x55 | 1 | Да | Да |
| 3923022 | Штука - ICM крепление/моторная проводка упряжка грунта | 1 | Да | Да |
| 3929159 | Экранный пакет | 1 | Да | Да |
| 3930037 | Топливный шланг (регулятор давления для корпуса управления топливом) | 1 | Да | Нет |
| 3936236 | держатели ECM | 2 | Да | Да |
| 3937181 | болты - крепление под давлением выхлопных газов | 2 | Да | Да |
| 3937299 | ЭКМ | 1 | Да | Да |
| 3938679 | Сборка регулятора давления | 1 | Да | Нет |
| 3938836 | Клапан управления топливом | 1 | Нет | Да |
| 3938841 | Клапан управления топливом | 1 | Да | Нет |
| 3938871 | Смеситель воздушного топлива | 1 | Да | Да |
| 3938872 | Корпус узла управления подачей топлива | 1 | Да | Да |
| 3938873 | Держатель датчика обратного давления | 1 | Да | Да |
| 3938875 | 5.2.1 Кронштейн модуля зажигания | 1 | Да | Да |
| 3938881 | Крышка впускного коллектора | 1 | Да | Да |
| 3938917 | Выхлопной адаптер, прямой | 1 из 2 | Да | Да |
| 3938918 | локтевой воздухозаборник | 1 | Да | Да |
| 3938919 | Жгут проводов двигателя | 1 | Да | Да |
| 3938920 | Система зажигания проводка ремня | 1 | Да | Да |
| 3938921 | Кронштейн разъема OEM | 1 | Да | Да |
| 3938926 | 4.2.1.1 Считывающая трубка LMRO с прямым давлением | 1 из 3 | Да | Да |
| 3938929 | Считывающая трубка давления выхлопных газов BBUK | 1 из 3 | Да | Да |
| 3938932 | Топливный шланг (топливный корпус для микшера) | 1 | Да | Да |
| 3964356 | Сборка испарителей | 1 | Нет | Да |
| 3964363 | 5.2.1 Запорный клапан топливного клапана, закрывающий монтажную пластину | 1 | Нет | Да |
| 3992124 | 3.2.1.1 Поддержка дроссельной заслонки | 1 | Да | Да |
| 3992125 | Стук датчика | 1 | Да | Да |
| 3992126 | Вудворд дроссельной заслонки | 1 | Да | Да |
| 3992127 | Длинные шпильки топливной системы | 4 | Да | Да |
| 3992178 | Задний адаптер для локтя | 1 | Да | Да |
| 3992179 | Выхлопной адаптер, 90-градусный локоть | 1 из 2 | Да | Да |
| 3992224 | Труба-LMRO 90 с датчиком давления | 1 из 3 | Да | Да |
| 4001675 | НТК датчик кислорода с подогревом | 1 | Да | Да |
| 4009913 | Сенсор комбинированного впуска коллектора | 1 | Да | Да |
| [[3617958]] | ОЭМ соединительный орех | 2 | Да | Да |
| 4062315 | Датчик влажности | 1 | Да | Да |
| 3967820 | Трубка для охлаждения испарителя сжиженного газа | 1 | Нет | Да |
| 3967822 | Трубка для охлаждения испарителя сжиженного газа | 1 | Нет | Да |

## OEM-установка Wiring Diagram

> [!note] Примечание
> Вы также можете обратиться к сервисной схеме проводов, Бюллетень 4021276.

![[19901345.png]]

![[19901346.png]]

## Справочная документация

| Номер бюллетеня | Наименование |
|---|---|
| 4021390 | B5.9G, B5.9LPG, B Gas Plus и B LPG Plus Руководство для владельцев |
| 3666164 | Руководство по устранению неполадок и ремонту, двигатели B5.9G (природный газ) и B5.9LPG (сжиженный нефтяной газ) |
| 4056515 | B Газ плюс Части Каталог |
| 4021317 | Руководство по устранению неполадок и ремонту - Электроника, Газ Плюс Двигатели |
| 4021276 | Газ плюс схема проводов |
| 3666119 | B5.9G/B5.9LPG Схема проводов |

Для получения дополнительной информации об установке свяжитесь с местным авторизованным ремонтным центром Cummins.

### История изменений документа

## Детали, упомянутые в документе

| Артикул | Наименование | Русское название |
|---|---|---|
| [[3617958]] | REGULAR HEXAGON NUT | Гайка шестигранная |
| [[3617959]] | LOCK WASHER | Стопорная шайба |
| [[3900589]] | HEXAGON FLANGE NUT | Гайка шестигранная с фланцем |
| [[3900629]] | HEXAGON FLANGE HEAD CAP SCREW | Болт с шестигранной головкой и фланцем |
| [[3900630]] | HEXAGON FLANGE HEAD CAP SCREW | Болт с шестигранной головкой и фланцем |
| [[3900631]] | HEXAGON FLANGE HEAD CAP SCREW | Болт с шестигранной головкой и фланцем |
| [[3900632]] | HEXAGON FLANGE HEAD CAP SCREW | Болт с шестигранной головкой и фланцем |
| [[3900678]] | HEXAGON FLANGE HEAD CAP SCREW | Болт с шестигранной головкой и фланцем |
| [[3901445]] | HEXAGON FLANGE HEAD CAP SCREW | Болт с шестигранной головкой и фланцем |
| [[3902460]] | HEXAGON FLANGE HEAD CAP SCREW | Болт с шестигранной головкой и фланцем |
| [[3906216]] | HEXAGON FLANGE NUT | Гайка шестигранная с фланцем |
| [[3909025]] | HEXAGON FLANGE HEAD CAP SCREW | Болт с шестигранной головкой и фланцем |
| [[3939258]] | COVER PLATE GASKET | Прокладка крышки-пластины |

> [!quote]- Original (English) · английский оригинал
> ## Instructions to Convert a B5.9G to a B Gas Plus and a B5.9LPG to a B LPG Plus
>
> **Preparatory Steps**
>
> The B Gas Plus and B LPG Plus engines require the use of an ISB (STORM) cylinder block. B5.9G and B5.9LPG engines built after March of 1997 were built with this cylinder block. The type of fitting in the oil rifle can identify the cylinder block. The correct fitting is a M14 straight thread o-ring. The older block has pipe threads.
>
> After the completion of this upfit, the engine dataplate **must** be stamped with the new CPL. This engine modification **must** be reported to Cummins Warranty using Cummins Form 1877 (Notice of Engine Modification), which can be found in the Warranty Administration Manual.
>
> Remove the following components:
>
> - Turbocharger and exhaust adaptor
> - Intake manifold cover and throttle assembly
> - Fuel control housing
> - Electronic control module (ECM)
> - Ignition control module (ICM)
> - Engine wiring harness.
>
> **ECM**
>
> Attach the ECM, Part Number 3937299, to the cylinder block using spacers, Part Number 3936236, under the left and right ears. The center tab and left ear are held down with capscrew, Part Number [[3900631]]. The right ear is held with capscrew, Part Number [[3909025]].
>
> **Note · Примечание**
> The right ear capscrew is common with the ignition control module (ICM) bracket.
>
> Replace the stud in the lift pump block off plate with an M8x20 capscrew, Part Number [[3900630]] (natural gas **only**).
>
> For B LPG Plus, install lift pump block-off plate, Part Number 3948083, and gasket, Part Number [[3939258]]. Mount with two M8x20 capscrews, Part Number [[3900630]].
>
> Refer to Procedure 019-031 in Troubleshooting and Repair Manual - Electronics, Gas Plus Engines, Bulletin 4021317.
>
> **Oil Pressure/Temperature Sensor**
>
> Insert the oil pressure/temperature sensor, Part Number 3417195, in the threaded hole below the ECM and to the left of the lift pump block off plate.
>
> Refer to Procedure 019-155 in Troubleshooting and Repair Manual - Electronics, Gas Plus Engines, Bulletin 4021317.
>
> **Fuel Control Housing**
>
> Remove the gas mass flow sensor and the fuel shutoff valve (natural gas **only**) from the original housing.
>
> Install a new screen pack, Part Number 3929159, and the shutoff valve (natural gas **only**) or cover plate, Part Number 3964363, (LPG **only**) in the base of the new fuel control housing, Part Number 3938872.
>
> Install a 45-degree connector, Part Number 200293, in the fuel inlet port (2).
>
> The gas mass flow sensor housing is held in place with four M5 capscrews, Part Number 3253888, from the top rather than through-bolted.
>
> Replace the 90-degree fuel connection fitting on the top of the gas mass flow sensor adaptor with a straight fitting, Part Number 129866.
>
> Refer to Procedure 005-009 in Troubleshooting and Repair Manual, B Series - Natural Gas, Bulletin 3666164.
>
> Install a new o-ring on the fuel control housing.
>
> Attach the fuel control housing with the same nuts.
>
> Refer to Procedure 005-009 in Troubleshooting and Repair Manual, B Series - Natural Gas, Bulletin 3666164.
>
> **Ignition Module Bracket**
>
> Attach the ignition module bracket, Part Number 3938875.
>
> The bracket is held with one M8x55 capscrew (1), Part Number [[3909025]], one M8x80 capscrew (2), Part Number 3902112, two M8x35 capscrews (3), Part Number [[3900632]], and one M8xM6 stud (4), Part Number 3923022.
>
> **Note · Примечание**
> Stud, Part Number [[3909025]], is common with the right ECM mounting tab.
>
> **Note · Примечание**
> Capscrew, Part Number 3923022, is mounted in the lower left corner of the ICM bracket. The stud is used to mount the engine wiring harness ground terminal. Use M6 nut, Part Number [[3906216]].
>
> **Note · Примечание**
> If a left side starter option is used with the starter solenoid on the top, there can be an interference problem with the low pressure regulator or evaporator. The starter option will need to be changed.
>
> **Fuel Pressure Regulator Housing (Natural Gas Only)**
>
> The pressure regulator housing, Part Number 3938679, attaches to the bracket with 1-M10x95 capscrew, Part Number 3908226, and 3-M10x25 capscrews, Part Number [[3902460]].
>
> Orient the pressure regulator housing so the fittings are facing to the left (forward).
>
> **Note · Примечание**
> The fuel outlet fitting (lower) may need to be replaced with a 90-degree fitting, Part Number 129859, if **not** already installed.
>
> **Note · Примечание**
> Fuel pressure sensor primary, Part Number 3330527, is included in the pressure regulator assembly.
>
> Refer to Procedure 005-047 in Troubleshooting and Repair Manual, B Series - Natural Gas, Bulletin 3666164.
>
> **Fuel Evaporator Assembly (LPG Only)**
>
> The evaporator assembly, Part Number 3964356, attaches to the ignition module bracket with 4-M10x25 capscrews, Part Number [[3902460]].
>
> **Note · Примечание**
> Fuel pressure sensor primary, Part Number 3330527, is included in the evaporator assembly.
>
> Replace the two coolant tubes with Part Numbers 3967820 and 3967822.
>
> Refer to Procedure 005-094 in Troubleshooting and Repair Manual, B Series - Natural Gas, Bulletin 3666164.
>
> **Note · Примечание**
> The coolant line that is connected at the thermostat housing connects to the inboard fitting on the evaporator.
>
> **Ignition Module/OEM Connector Bracket**
>
> Attach the ignition module to the ignition module bracket. The module should be oriented with the two connectors for the ignition coils on the left side (forward). The OEM connector bracket, Part Number 3938921, is mounted behind the top two ICM mounting bolts.
>
> Use 4-M8x40, Part Number [[3900678]], capscrews.
>
> Refer to Procedure 019-105 in Troubleshooting and Repair Manual - Electronics, Gas Plus Engines, Bulletin 4021317.
>
> **Engine Wiring Harness**
>
> Install the engine wiring harness, Part Number 3938919. The ECM connectors are keyed to allow for correct orientation.
>
> Mount the OEM connectors in the OEM connector bracket. Use washers, part Number [[3617959]], and nuts, Part Number [[3617958]], to secure the connectors.
>
> Connect the ground terminal to the lower left ICM bracket stud with a M6 nut, Part Number [[3906216]].
>
> Connect the two p-clips. The front p-clip is mounted to the upper outside fuel housing bolt. The second is mounted to the block behind the air compressor with capscrew, Part Number [[3900629]]. It is mounted in the upper mounting hole.
>
> Connect the engine wiring harness to the sensors and actuators as they are installed on the engine.
>
> Refer to Procedure 019-043 in Troubleshooting and Repair Manual - Electronics, Gas Plus Engines, Bulletin 4021317.
>
> **Fuel Supply Hose**
>
> Connect the fuel supply hose to the low pressure regulator housing or evaporator and the fuel control housing, Part Number 3930037.
>
> **Note · Примечание**
> The 90-degree end of the hose connects to the low pressure regulator housing.
>
> **Intake Manifold Cover**
>
> The throttle assembly can be attached to the intake manifold cover on or off the engine.
>
> Insert the threaded rods, Part Number 3992127, into the intake manifold cover, Part Number 3938881.
>
> **Note · Примечание**
> Install the four o-rings, Part Number 145582, between each mating surface.
>
> Attach the throttle actuator, Part Number 3992126, to the intake manifold.
>
> Attach the throttle support bracket, Part Number 3992124, to the throttle actuator and the intake manifold cover; use three tapered capscrews, Part Number 3284216.
>
> Slide the mixer housing, Part Number 3938871, onto the threaded rods.
>
> Install the four nuts, Part Number [[3900589]].
>
> Install intake elbow, Part Number 3938918, using the original intake elbow hardware.
>
> The new intake elbow has the provision for a humidity sensor. The elbow can be oriented straight up or straight out.
>
> Refer to Procedure 005-052 in Troubleshooting and Repair Manual, B Series - Natural Gas, Bulletin 3666164.
>
> **Fuel Jumper Hose**
>
> Install a 90-degree fitting, Part Number 129859, in the fuel mixer housing.
>
> Install fuel control valve, Part Number 3938841-natural gas or Part Number 3938870-LPG, into the fuel mixer housing.
>
> Connect the fuel jumper house, Part Number 3938932, to the 90-degree fitting on the mixer housing. If the intake/throttle assembly is being assembled on the engine, connect the hose to the gas mass flow sensor adaptor. Otherwise, make the connection after the intake manifold assembly is installed on the engine.
>
> Install the ignition coils after the intake manifold is installed on the engine. Refer to Procedure 013-012 in Troubleshooting and Repair Manual, B Series - Natural Gas, Bulletin 3666164.
>
> Refer to Procedure 005-052 in Troubleshooting and Repair Manual, B Series - Natural Gas, Bulletin 3666164.
>
> **Fuel Pressure/Temperature Sensor, Secondary**
>
> Install the fuel pressure/temperature sensor, Part Number 3417195, into the mixer housing.
>
> Refer to Procedure 019-053 in Troubleshooting and Repair Manual - Electronics, Gas Plus Engines, Bulletin 4021317.
>
> **Intake Manifold Pressure/Temperature Sensor**
>
> Install the intake manifold pressure/temperature sensor, Part Number 4009913, into the intake manifold.
>
> Install a plug in the remaining two holes in the intake manifold.
>
> Refer to Procedure 019-099 in Troubleshooting and Repair Manual - Electronics, Gas Plus Engines, Bulletin 4021317.
>
> **Knock Sensors**
>
> The engine is equipped with two knock sensors, Part Number 3607945.
>
> The front sensor is located on the top of the intake manifold cover and shares a mounting bolt with the front inner bolt. A longer capscrew is required to mount the sensor, M8x45, part Number [[3901445]].
>
> The rear sensor is located below the ignition module bracket. There is a boss on the engine with two threaded holes. The sensor is located in the lower hole and is mounted using knock sensor stud, Part Number 3992125, and M8 nut, Part Number [[3900589]].
>
> Refer to Procedure 019-346 in Troubleshooting and Repair Manual - Electronics, Gas Plus Engines, Bulletin 4021317.
>
> **Exhaust Back Pressure Sensor**
>
> The exhaust back pressure sensor, Part Number 3348579, is remote mounted on the top of the intake manifold in sensor adaptor, Part Number 3938873. The sensor bracket is mounted with capscrews, Part Number 3937181.
>
> The sensor connects to the exhaust adaptor through a stainless steel tube. The tube part number varies by turbocharger configuration.
>
> Refer to the turbocharger section for tube selection details.
>
> Refer to Procedure 019-347 in Troubleshooting and Repair Manual - Electronics, Gas Plus Engines, Bulletin 4021317.
>
> **Ignition Harness**
>
> Connect the ignition harness, Part Number 3938920, to the ignition module and to both ignition coils.
>
> Refer to Procedure 013-037 in Troubleshooting and Repair Manual, B Series - Natural Gas, Bulletin 3666164.
>
> **Turbocharger**
>
> The B Gas Plus has several turbocharger configuration options. The turbocharger and exhaust adaptor will need to be replaced along with the installation of the exhaust back pressure sensor tube.
>
> Refer to the following chart for option details.
>
> | Exhaust Back Pressure Tube Compatibility Chart |  |  |  |  |
> |---|---|---|---|---|
> |  | Exhaust Adaptor |  |  |  |
> |  | 90-Degree Elbow | 90-Degree Elbow (Rotatable) | Straight Out |  |
> | Exhaust Manifold | XS 9260 | XS 9266 | XS 9259 |  |
> | LMRO | TB 9795 | N/A | PH 9051 | PH 9843 |
> | LMFO | TB 97003 | PH 9844 | N/A | N/A |
>
> | Option Part Number List |  |  |  |
> |---|---|---|---|
> | Option Number | Option Part Number | Required Fitting | Turbocharger |
> | XS 9260 | 3992179 | 68138 | N/A |
> | XS 9266 | 3992179 | 3992178 | N/A |
> | XS 9259 | 3938917 | 68138 | N/A |
> | PH 9844 | 3938929 | N/A | N/A |
> | PH 9051 | 3992224 | N/A | N/A |
> | PH 9843 | 3938926 | N/A | N/A |
> | TB 9795 | N/A | N/A | 3599492 |
> | TB 97003 | N/A | N/A | 3599493 |
>
> ## Conversion Parts List
>
> | Part Number | Part Description | Quantity | NG | LPG |
> |---|---|---|---|---|
> | 68183 | 3/8 inch to 1/4 inch NPT | 1 | Yes | Yes |
> | 129859 | 90-degree fitting | 1 | Yes | No |
> | 129866 | Straight fitting | 1 | Yes | Yes |
> | 145582 | Throttle/mixer o-rings (4 total) | 4 | Yes | Yes |
> | 200293 | 45-degree fitting | 1 | Yes | Yes |
> | 3253888 | GMFS mounting bolts M5 | 4 | Yes | Yes |
> | 3284216 | Throttle actuator/mixer bracket screws | 3 | yes | Yes |
> | 3348579 | Back pressure sensor | 1 | Yes | Yes |
> | 3417195 | Fuel pressure oil pressure combo sensor | 2 | Yes | Yes |
> | 3599492 | Turbocharger LMRO | 1 of 2 | Yes | Yes |
> | 3599493 | Turbocharger LMFO | 1 of 2 | Yes | Yes |
> | 3607945 | Knock sensor | 2 | Yes | Yes |
> | [[3617959]] | OEM connector washer | 2 | Yes | Yes |
> | [[3900589]] | Nuts - fuel mixer M8 | 5 | Yes | Yes |
> | 3925883 | Engine harness p-clip | 1 | Yes | Yes |
> | [[3900631]] | Holds-holds ECM - M8x25 | 4 | Yes | Yes |
> | [[3900632]] | Holds-holds IM bracket - M8x35 | 2 | Yes | Yes |
> | [[3900678]] | Holds-holds IM - M8x40 | 4 | Yes | Yes |
> | [[3901445]] | Capscrew M8x45 | 1 | Yes | Yes |
> | 3902112 | Holds-holds IM bracket - M8x80 | 1 | Yes | Yes |
> | [[3902460]] | Capscrew-holds pressure regulator M10x25 | 3 | Yes | No |
> | [[3902460]] | Capscrew M10x25 - evaporator mount | 4 | No | Yes |
> | [[3906216]] | Nut - engine harness ground M6 | 1 | Yes | Yes |
> | 3908226 | Holds-holds pressure regulator M10x95 | 1 | Yes | No |
> | [[3909025]] | Holds-holds ECM/IM bracket M8x55 | 1 | Yes | Yes |
> | 3923022 | Stud - ICM mounting/engine harness ground | 1 | Yes | Yes |
> | 3929159 | Screen pack | 1 | Yes | Yes |
> | 3930037 | Fuel hose (pressure regulator to fuel control housing) | 1 | Yes | No |
> | 3936236 | ECM holders | 2 | Yes | Yes |
> | 3937181 | Capscrew - exhaust back pressure mounting | 2 | Yes | Yes |
> | 3937299 | ECM | 1 | Yes | Yes |
> | 3938679 | Pressure regulator assembly | 1 | Yes | No |
> | 3938836 | Fuel control valve | 1 | No | Yes |
> | 3938841 | Fuel control valve | 1 | Yes | No |
> | 3938871 | Air fuel mixer | 1 | Yes | Yes |
> | 3938872 | Fuel control housing | 1 | Yes | Yes |
> | 3938873 | Back pressure sensor holder | 1 | Yes | Yes |
> | 3938875 | Ignition module bracket | 1 | Yes | Yes |
> | 3938881 | Intake manifold cover | 1 | Yes | Yes |
> | 3938917 | Exhaust adaptor, straight | 1 of 2 | Yes | Yes |
> | 3938918 | Air intake elbow | 1 | Yes | Yes |
> | 3938919 | Engine wiring harness | 1 | Yes | Yes |
> | 3938920 | Ignition system wiring harness | 1 | Yes | Yes |
> | 3938921 | OEM connector bracket | 1 | Yes | Yes |
> | 3938926 | Exhaust pressure sensing tube-LMRO straight | 1 of 3 | Yes | Yes |
> | 3938929 | Exhaust pressure sensing tube-BBUK | 1 of 3 | Yes | Yes |
> | 3938932 | Fuel supply hose (fuel housing to mixer) | 1 | Yes | Yes |
> | 3964356 | Evaporator assembly | 1 | No | Yes |
> | 3964363 | Fuel shutoff valve cover plate | 1 | No | Yes |
> | 3992124 | Throttle support bracket | 1 | Yes | Yes |
> | 3992125 | Knock sensor stud | 1 | Yes | Yes |
> | 3992126 | Woodward throttle actuator | 1 | Yes | Yes |
> | 3992127 | Long fuel system studs | 4 | Yes | Yes |
> | 3992178 | Rear out adapter for elbow | 1 | Yes | Yes |
> | 3992179 | Exhaust adaptor, 90-degree elbow | 1 of 2 | Yes | Yes |
> | 3992224 | Pressure sensing tube-LMRO 90 rotatable | 1 of 3 | Yes | Yes |
> | 4001675 | NTK heated oxygen sensor | 1 | Yes | Yes |
> | 4009913 | Intake manifold combo sensor | 1 | Yes | Yes |
> | [[3617958]] | OEM connector nut | 2 | Yes | Yes |
> | 4062315 | Humidity sensor | 1 | Yes | Yes |
> | 3967820 | LPG Evaporator coolant tube | 1 | No | Yes |
> | 3967822 | LPG Evaporator coolant tube | 1 | No | Yes |
>
> ## OEM Installation Wiring Diagram
>
> **Note · Примечание**
> You can also reference service wiring diagram, Bulletin 4021276.
>
> ## Reference Documentation
>
> | Bulletin Number | Description |
> |---|---|
> | 4021390 | B5.9G, B5.9LPG, B Gas Plus, and B LPG Plus Owner's Manual |
> | 3666164 | Troubleshooting and Repair Manual, B5.9G (Natural Gas) and B5.9LPG (Liquefied Petroleum Gas) Engines |
> | 4056515 | B Gas Plus Parts Catalog |
> | 4021317 | Troubleshooting and Repair Manual - Electronics, Gas Plus Engines |
> | 4021276 | Gas Plus Wiring Diagram |
> | 3666119 | B5.9G/B5.9LPG Wiring Diagram |
>
> For additional installation information, contact your local Cummins Authorized Repair Facility.
>
> ### Document History
