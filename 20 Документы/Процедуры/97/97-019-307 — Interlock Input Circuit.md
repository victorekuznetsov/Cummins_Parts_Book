---
aliases:
  - "Цепь входа блокировки"
type: "Процедура"
doc: "97-019-307"
title_en: "Interlock Input Circuit"
title_ru: "Цепь входа блокировки"
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
figures: 67
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-307.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-307.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
  - "перевод/машинный"
---

# Interlock Input Circuit
**Цепь входа блокировки**

> [!abstract] Процедура · `97-019-307`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-06-13
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-307.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-307.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы избежать травм, всегда проветривайте моторное отделение перед обслуживанием батарей. Чтобы избежать дуги, сначала удалите отрицательный (-) кабель батареи и прикрепите отрицательный (-) кабель батареи последним.

Переведите замок зажигания в положение OFF. Отсоедините кабели аккумулятора автомобиля от батареи. Отсоедините разъемы ICONTM от батареи.

> [!note] Примечание
> Отключение аккумуляторных батарей автомобиля может потребовать сброса часов ECM в режиме реального времени с помощью INSITETM.

![[ea8coha.png]]

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте пробный щуп, номер детали 3822758 и 3822917, при проведении измерения.

Отключите разъемы ICONTM idle Control module A и B.

Отключите выключатель стояночного тормоза от электропроводки кабины.

Отсоедините лампу ICONTM от электропроводки кабины.

Установите мультиметр для измерения сопротивления.

![[19802893.png]]

Проверьте выходную цепь блокировки.

Прикосновение к одному из мультиметров приводит к контакту 5 с неработающим модулем управления ICONTM Разъем проводов жгута. Прикоснитесь к другому мультиметру, приведите к контакту В разъема жгута парковочного тормоза.

Считайте показания мультиметра.

Удалите свинец от контакта В разъема жгута жгута парковочного тормоза. Прикосновение к мультиметру приводит к контакту В разъема ламповой проводов ICONTM.

Считайте показания мультиметра.

![[19802894.png]]

Наконец, касание одного из мультиметров приводит к контакту 6 с неработающим модулем управления ICONTM Разъем жгута проводов.

Прикосновение к другому мультиметру приводит к контакту А разъема ламповой проводов ICONTM.

Считайте показания мультиметра.

![[19802894.png]]

Для всех трех проверок пин-кодов мультиметр должен отображать показания менее 10 Ом, что является замкнутой схемой.

Если какая-либо из цепей **не** закрыта, изолируйте проблему от проводов кабины или от проводов двигателя ICONTM. Если цепь закрыта, проверьте цепь ввода блокировки.

![[19801619.png]]

Проверьте схему входного блока.

Убедитесь, что выключатели наклона капота и нейтрального положения закрыты.

Прикосновение к одному из мультиметров приводит к контакту 3 с неработающим модулем управления ICONTM Разъем проводной упряжки.

Прикосновение к другому мультиметру приводит к контакту А разъема жгута парковочного тормоза.

Считайте показания мультиметра.

![[19802894.png]]

Затем, при одном свинце, все еще касающемся контакта А разъема проводов жгута проводов стояночного тормоза, коснитесь другого мультиметрового провода, чтобы связаться 2 с неработающим модулем управления ICONTM B разъемом жгута проводов проводов.

Считайте показания мультиметра.

![[19802895.png]]

Для обеих проверок пин-кодов мультиметр **должен **отображать значение менее 10 Ом, что является замкнутой схемой.

Если либо схема **не** закрыта, изолируйте проблему от проводов кабины или от проводов двигателя ICONTM.

![[19801619.png]]

Проверьте выходной провод на стороне проводов кабины.

Отсоедините 14-контактный проходной разъем на брандмауэре автомобиля.

Прикосновение к одному из мультиметров приводит к контакту J с 14-контактным проходным разъемом, проводкой кабины с ремнями безопасности. Прикоснитесь к другому мультиметру, приведите к контакту В разъема жгута парковочного тормоза.

Считайте показания мультиметра.

![[19c00931.png]]

Затем, с одним свинцом, все еще касающимся контакта J 14-контактного разъема, стороны проводов кабины, коснитесь второго многометрового свинца, чтобы связаться с B разъема ламповой проводов ICONTM.

Считайте показания мультиметра.

![[19c00931.png]]

Для обеих проверок пин-кодов мультиметр **должен **отображать значение менее 10 Ом, что является замкнутой схемой.

Если цепь **не **закрыта, отремонтируйте или замените проводку кабины. См. процедуру 019-202, 019-200 или[[97-019-305 — Cab Wiring Harness|019-305]].

Если обе цепи закрыты, отремонтируйте или замените электропроводку двигателя ICONTM. См. процедуру 019-202, 019-208 или[[97-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

Прикосновение одного мультиметра приводит к контакту D 14-контактного пропускного разъема, кабины проводов упряжки.

Прикосновение к другому мультиметру приводит к контакту А разъема ламповой проводов ICONTM.

Считайте показания мультиметра.

![[19c00931.png]]

Мультиметр **должен **отображать значение менее 10 Ом, что является замкнутой схемой.

Если цепь **не** закрыта, отремонтируйте или замените проводку кабины. См. процедуру 019-202, 019-200 или[[97-019-305 — Cab Wiring Harness|019-305]].

Если цепь закрыта, отремонтируйте или замените электропроводку двигателя ICONTM. См. процедуру 019-202, 019-208 или[[97-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

Проверьте входной провод на стороне проводов кабины.

Прикосновение к одному из мультиметров приводит к контакту К 14-контактного пропускного разъема, кабины проводов упряжки борта.

Прикосновение к другому мультиметру приводит к контакту А разъема жгута парковочного тормоза.

Считайте показания мультиметра.

![[19c00931.png]]

Мультиметр **должен **отображать значение менее 10 Ом, что является замкнутой схемой.

Если цепь **не** закрыта, отремонтируйте или замените проводку кабины. См. процедуру 019-202, 019-200 или[[97-019-305 — Cab Wiring Harness|019-305]].

Если цепь закрыта, изолируйте проблему до правильной части проводов двигателя ICONTM.

![[19801619.png]]

Прикосновение к одному из мультиметров приводит к контакту К 14-контактного пропускного разъема, проводов двигателя с ремнями безопасности.

Прикосновение к другому мультиметру приводит к контакту 3 с неработающим модулем управления ICONTM Разъем проводов жгута.

Считайте показания мультиметра.

![[19c00930.png]]

Затем, оставив первый вывод на месте на контакте К 14-контактного разъема, коснитесь второго многометрового вывода для контакта 2 неработающего модуля управления ICONTM B проводов ремня разъема.

Считайте показания мультиметра.

![[19802896.png]]

Для обеих проверок пин-кодов мультиметр должен отображать показания менее 10 Ом (замкнутая схема).

Если цепь **не** закрыта, проверьте часть схемы на нейтральный выключатель положения.

![[19801619.png]]

Во-первых, убедитесь, что нейтральный переключатель позиции хорош. Замените нейтральный переключатель по мере необходимости.

Отключите нейтральный переключатель положения от электропроводки двигателя ICONTM.

Прикосновение к одному из мультиметров приводит к контакту К 14-контактного пропускного разъема, проводов двигателя с ремнями безопасности. Прикосновение к другому мультиметру приводит к контакту В нейтрального положения коммутатора проводов ремня разъема.

Считайте показания мультиметра.

![[19802897.png]]

Мультиметр **должен** отображать показания менее 10 Ом (замкнутая схема).

Если схема **не** закрыта, отремонтируйте или замените электропроводку двигателя ICONTM.

См. процедуру 019-202 или[[97-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

Отсоедините переключатель наклона капота от электропроводки двигателя ICONTM.

Прикосновение к одному из мультиметров приводит к контакту А с разъемом нейтрального положения проводов жгута.

Прикосновение к другому мультиметру приводит к контакту В вытяжного переключателя наклона проводов жгута разъема.

Считайте показания мультиметра.

![[19802898.png]]

Мультиметр **должен** отображать показания менее 10 Ом (замкнутая схема).

Если схема **не** закрыта, отремонтируйте или замените электропроводку двигателя ICONTM.

См. процедуру 019-202 или[[97-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

Убедитесь, что переключатель наклона капота хорош.

Прикосновение одного из мультиметров приводит к контакту А переключателя наклона капота с проводкой ремня разъема.

Прикосновение к другому мультиметру приводит к контакту 3 с неработающим модулем управления ICONTM Разъем проводов жгута.

Считайте показания мультиметра.

![[19802894.png]]

Мультиметр **должен** отображать показания менее 10 Ом (замкнутая схема).

Если схема **не** закрыта, отремонтируйте или замените электропроводку двигателя ICONTM.

См. процедуру 019-202 или[[97-019-043 — Engine Wiring Harness|019-043]].

После ремонта подсоедините все компоненты.

![[19801619.png]]

### Проверка на замыкание на массу

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы избежать травм, всегда проветривайте моторное отделение перед обслуживанием батарей. Чтобы избежать дуги, сначала удалите отрицательный (-) кабель батареи и прикрепите отрицательный (-) кабель батареи последним.

Переведите замок зажигания в положение OFF. Отсоедините кабели аккумулятора автомобиля от батареи. Отсоедините разъемы ICONTM от батареи.

> [!note] Примечание
> Отключение аккумуляторных батарей автомобиля может потребовать сброса часов ECM в режиме реального времени с помощью INSITETM.

![[ea8coha.png]]

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте пробный щуп, номер детали 3822758 и 3822917, при проведении измерения.

Отключите разъемы ICONTM idle Control module A и B.

Отсоедините 14-контактный проходной разъем на брандмауэре автомобиля.

Отсоедините выключатель стояночного тормоза и лампу ICONTM от электропроводки кабины.

Отсоедините нейтральный переключатель положения и переключатель наклона капота от электропроводки двигателя ICONTM.

Установите мультиметр для измерения сопротивления.

![[19802893.png]]

Прикосновение к одному из мультиметров приводит к контакту В разъема ламповой проводов ICONTM. Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

Затем касание одного из мультиметров приводит к контакту А разъема ламповой проводов ICONTM. Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

![[19802899.png]]

Для обеих проверок с помощью штифта на землю мультиметр **должен **отображать показания более 100k ом, что является открытой схемой.

Если схема **не **открыта, есть короткое замыкание на землю.

Изолируйте короткую кабину проводов упряжкой или двигатель проводов упряжкой части схемы.

![[19801621.png]]

Прикосновение одного из мультиметров приводит к контакту В разъема жгута парковочного тормоза. Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

Затем касание одного из мультиметров приводит к контакту А разъема жгута парковочного тормоза. Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

![[19802899.png]]

Для обеих проверок с помощью штифта на землю мультиметр **должен **отображать показания более 100k ом, что является открытой схемой.

Если схема **не **открыта, есть короткое замыкание на землю.

Изолируйте короткую кабину проводов упряжкой или двигатель проводов упряжкой части схемы.

![[19801621.png]]

Прикосновение к одному из мультиметров приводит к контакту J с 14-контактным проходным разъемом, проводкой двигателя с ремнями безопасности. Прикоснитесь к другому мультиметру, который ведет на землю. Считайте показания мультиметра.

Затем касание одного из мультиметров приводит к контакту D 14-контактного пропускного разъема, проводов двигателя с жгутом проводов. Прикоснитесь к другому мультиметру, который ведет на землю. Считайте показания мультиметра.

![[19c00940.png]]

Для обеих проверок с помощью штифта на землю мультиметр **должен **отображать показания более 100k ом, что является открытой схемой. Если любая из цепей **не** открыта, проверьте короткое замыкание от соответствующего контакта с коннектором соединительного устройства проводов модуля управления холостым ходом.

Если цепь открыта, отремонтируйте или замените проводку кабины. См. процедуру 019-202, 019-200 или[[97-019-305 — Cab Wiring Harness|019-305]].

![[19801621.png]]

Прикосновение к одному из мультиметров приводит к контакту К 14-контактного пропускного разъема, проводов двигателя с ремнями безопасности.

Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

![[19c00940.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой. Если схема **не** открыта, изолируйте короткий к любому неработающему разъему модуля управления.

Если цепь открыта, отремонтируйте или замените проводку кабины. См. процедуру 019-202, 019-200 или[[97-019-305 — Cab Wiring Harness|019-305]].

![[19801621.png]]

Прикосновение к одному из мультиметров приводит к контакту 5 с неработающим модулем управления ICONTM Разъем проводов жгута. Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

Затем касание одного из мультиметров приводит к контакту 6 с неработающим модулем управления ICONTM Разъем проводной упряжки. Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

![[19c00932.png]]

Для обеих проверок с помощью штифта на землю мультиметр **должен **отображать показания более 100k ом, что является открытой схемой.

Если схема **не** открыта, отремонтируйте или замените электропроводку двигателя ICONTM.

См. процедуру 019-208 или[[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Прикосновение к одному из мультиметров приводит к контакту 2 с неработающим модулем управления ICONTM B проводов жгута разъема.

Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

![[19802900.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если схема **не** открыта, отремонтируйте или замените электропроводку двигателя ICONTM.

См. процедуру 019-208 или[[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Прикосновение к одному из мультиметров приводит к контакту А с разъемом нейтрального положения проводов жгута. Прикоснитесь к другому мультиметру, который ведет на землю. Считайте показания мультиметра.

Затем касание одного из мультиметров приводит к контакту В с нейтральным положением коммутатора проводов ремня разъема. Прикоснитесь к другому мультиметру, который ведет на землю. Считайте показания мультиметра.

![[19802899.png]]

Для обеих проверок с помощью штифта на землю мультиметр **должен **отображать показания более 100k ом, что является открытой схемой.

Если схема **не** открыта, отремонтируйте или замените электропроводку двигателя ICONTM. См. процедуру 019-202 или[[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Прикосновение одного из мультиметров приводит к контакту А переключателя наклона капота с проводкой ремня разъема. Прикоснитесь к другому мультиметру, который ведет на землю. Считайте показания мультиметра.

Затем касание одного из мультиметров приводит к контакту В вытяжного переключателя наклона проводов жгута разъема. Прикоснитесь к другому мультиметру, который ведет на землю. Считайте показания мультиметра.

![[19802899.png]]

Для обеих проверок с помощью штифта на землю мультиметр **должен **отображать показания более 100k ом, что является открытой схемой.

Если проверка **не** открыта, отремонтируйте или замените электропроводку двигателя ICONTM. См. процедуру 019-202 или[[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Прикосновение к одному из мультиметров приводит к контакту 3 с неработающим модулем управления ICONTM Разъем проводной упряжки.

Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

![[19c00932.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если схема **не** открыта, отремонтируйте или замените электропроводку двигателя ICONTM. См. процедуру 019-202 или[[97-019-043 — Engine Wiring Harness|019-043]].

После ремонта подсоедините все компоненты.

![[19801621.png]]

### Проверка на замыкание между контактами

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы избежать травм, всегда проветривайте моторное отделение перед обслуживанием батарей. Чтобы избежать дуги, сначала удалите отрицательный (-) кабель батареи и прикрепите отрицательный (-) кабель батареи последним.

Переведите замок зажигания в положение OFF. Отсоедините кабели аккумулятора автомобиля от батареи. Отсоедините разъемы ICONTM от батареи.

> [!note] Примечание
> Отключение аккумуляторных батарей автомобиля может потребовать сброса часов ECM в режиме реального времени с помощью INSITETM.

![[ea8coha.png]]

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте пробный щуп, номер детали 3822758 и 3822917, при проведении измерения.

Отключите разъемы ICONTM idle Control module A и B. Отсоедините 14-контактный проходной разъем на брандмауэре автомобиля.

Отсоедините выключатель стояночного тормоза и лампу ICONTM от электропроводки кабины.

Отсоедините нейтральный переключатель положения и переключатель наклона капота от электропроводки двигателя ICONTM.

Установите мультиметр для измерения сопротивления.

![[19802893.png]]

Прикосновение одного из мультиметров приводит к контакту А разъема жгута парковочного тормоза.

Прикосновение к другому мультиметру приводит к контакту В проводов ремня разъема.

Считайте показания мультиметра.

![[19802901.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой. Если схема не открыта, между контактом А и контактом В имеется короткое замыкание.

Ремонт или замена кабины проводов ремня. См. процедуру 019-202 или[[97-019-305 — Cab Wiring Harness|019-305]].

![[19801621.png]]

Прикосновение к одному из мультиметров приводит к контакту А разъема ламповой проводов ICONTM.

Прикосновение к другому мультиметру приводит к контакту В проводов ремня разъема.

Считайте показания мультиметра.

![[19802901.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой. Если схема не открыта, между контактом А и контактом В имеется короткое замыкание.

Ремонт или замена кабины проводов ремня. См. процедуру 019-202 или[[97-019-305 — Cab Wiring Harness|019-305]].

![[19801621.png]]

Прикосновение к одному из мультиметров приводит к контакту J с 14-контактным проходным разъемом, проводкой кабины с ремнями безопасности. Прикосновение к другому мультиметру приводит ко всем другим штифтам в разъеме, по одному за раз.

Повторите проверку контакта с контактом от контакта D 14-контактного разъема, стороны проводов кабины, до всех других контактов в разъеме и от контакта K до всех других контактов.

Считайте показания мультиметра.

![[19c00935.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой. Если схема **не** открыта, то имеется короткое замыкание от контакта J, контакта D или контакта K до любого другого штифта в разъеме, который зарегистрировал замкнутую цепь.

Ремонт или замена кабины проводов ремня. См. процедуру 019-200 или[[97-019-305 — Cab Wiring Harness|019-305]].

![[19801621.png]]

Прикосновение к одному из мультиметров приводит к контакту J с 14-контактным проходным разъемом, проводкой двигателя с ремнями безопасности. Прикосновение к другому мультиметру приводит ко всем другим штифтам в разъеме, по одному за раз.

Повторите проверку контакта с контактом от контакта D 14-контактного разъема, стороны проводов двигателя, до всех других контактов в разъеме и от контакта K до всех других контактов.

Считайте показания мультиметра.

![[19c00942.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если схема **не** открыта, то имеется короткое замыкание от контакта J, контакта D или контакта K в 14-контактном проходном разъеме к любому другому штифту в разъеме, который зарегистрировал замкнутую цепь.

Ремонт или замена ремня электропроводки двигателя ICONTM. См. процедуру 019-200 или[[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Прикосновение к одному из мультиметров приводит к контакту 3 с неработающим модулем управления ICONTM Разъем проводной упряжки. Прикосновение к другому мультиметру приводит ко всем другим штифтам в разъеме, по одному за раз.

Повторите проверку контакта с контактом от контакта 5 модуля управления ICONTM холостого хода Разъем проводов жгута ко всем другим штифтам в разъеме и от контакта 6 ко всем другим штифтам.

Считайте показания мультиметра.

![[19c00943.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если схема **не** открыта, то в модуле управления ICONTM idle имеется короткое замыкание от контакта 3, контакта 5 или контакта 6 к любому другому штифту в разъеме, который зарегистрировал замкнутую схему.

Ремонт или замена ремня электропроводки двигателя ICONTM. См. процедуру 019-208 или[[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Прикосновение к одному из мультиметров приводит к контакту 2 с неработающим модулем управления ICONTM B проводов жгута разъема.

Прикосновение к другому мультиметру приводит ко всем другим штифтам в разъеме, по одному за раз.

Считайте показания мультиметра.

![[19c00962.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если схема **не** открыта, то в коннекторе B модуля управления ICONTM холостого хода имеется короткое замыкание от контакта 2 к любому другому штифту в коннекторе, который зарегистрировал замкнутую цепь.

Ремонт или замена ремня электропроводки двигателя ICONTM. См. процедуру 019-208 или[[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Прикосновение к одному из мультиметров приводит к контакту А с разъемом нейтрального положения проводов жгута.

Прикосновение к другому мультиметру приводит к контакту B разъема.

Считайте показания мультиметра.

![[19802901.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если схема **не** открыта, то имеется короткое замыкание от контакта А до контакта В в нейтральном положении коммутатора проводов жгута разъема.

Ремонт или замена ремня электропроводки двигателя ICONTM. См. процедуру 019-202 или[[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Прикосновение одного из мультиметров приводит к контакту А переключателя наклона капота с проводкой ремня разъема.

Прикосновение к другому мультиметру приводит к контакту B разъема.

Считайте показания мультиметра.

![[19802901.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если схема **не** открыта, то имеется короткое замыкание от контакта А до контакта В в разъеме наклонной проводов вытяжки.

Ремонт или замена ремня электропроводки двигателя ICONTM. См. процедуру 019-202 или[[97-019-043 — Engine Wiring Harness|019-043]].

После ремонта подсоедините все компоненты.

![[19801621.png]]

### Проверьте короткое замыкание на источнике внешнего напряжения

Отключите разъемы ICONTM idle Control module A и B.

Отсоедините лампу ICONTM и выключатель стояночного тормоза от электропроводки кабины.

Установите мультиметр для измерения VDC.

Переведите замок зажигания в положение ON.

![[19802893.png]]

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте пробный щуп, номер детали 3822758, при проведении измерения.

Прикосновение к одному из мультиметров приводит к контакту А разъема ламповой проводов ICONTM. Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

Затем касание одного из мультиметров приводит к контакту В разъема ламповой проводов ICONTM. Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

![[19802899.png]]

Для обеих проверок с помощью пин-стопа мультиметр **должен отображать показания менее 0,5 VDC. Если напряжение **не меньше 0,5 ВДК, то происходит короткое замыкание к внешнему источнику напряжения.

> [!note] Примечание
> Внешним источником напряжения является любой провод в кабине или проводах двигателя, который несет напряжение.

Удалите внешний источник напряжения.

![[19c00963.png]]

Прикосновение одного из мультиметров приводит к контакту А разъема жгута парковочного тормоза. Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

Затем касание одного из мультиметров приводит к контакту В разъема жгута парковочного тормоза. Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

![[19802899.png]]

Для обеих проверок с помощью пин-стопа мультиметр **должен отображать показания менее 0,5 VDC. Если напряжение **не меньше 0,5 ВДК, то происходит короткое замыкание к внешнему источнику напряжения.

> [!note] Примечание
> Внешним источником напряжения является любой провод в кабине или проводах двигателя, который несет напряжение.

Удалите внешний источник напряжения.

После ремонта подсоедините все компоненты.

![[19c00963.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> Turn the keyswitch to the OFF position. Disconnect the vehicle battery cables from the battery. Disconnect the ICON™ battery harness connectors from the battery.
>
> **Note · Примечание**
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset using INSITE™.
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.
>
> Disconnect the ICON™ idle control module A and B connectors.
>
> Disconnect the parking brake switch from the cab harness.
>
> Disconnect the ICON™ lamp from the cab harness.
>
> Set the multimeter to measure resistance.
>
> Check the interlock output circuit.
>
> Touch one of the multimeter leads to pin 5 of the ICON™ idle control module A harness connector. Touch the other multimeter lead to pin B of the parking brake switch harness connector.
>
> Read the value displayed on the multimeter.
>
> Remove the lead from pin B of the parking brake switch harness connector. Touch the multimeter lead to pin B of the ICON™ lamp harness connector.
>
> Read the value displayed on the multimeter.
>
> Finally, touch one of the multimeter leads to pin 6 of the ICON™ idle control module A harness connector.
>
> Touch the other multimeter lead to pin A of the ICON™ lamp harness connector.
>
> Read the value displayed on the multimeter.
>
> For all three pin checks, the multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.
>
> If any of the circuits are **not** closed, isolate the problem to the cab harness or ICON™ engine harness side of the circuit. If the circuit is closed, check the interlock input circuit.
>
> Check the interlock input circuit.
>
> Make sure that the hood tilt and neutral position switches are closed.
>
> Touch one of the multimeter leads to pin 3 of the ICON™ idle control module A harness connector.
>
> Touch the other multimeter lead to pin A of the parking brake switch harness connector.
>
> Read the value displayed on the multimeter.
>
> Then, with one lead still touching pin A of the parking brake switch harness connector, touch the other multimeter lead to pin 2 of the ICON™ idle control module B harness connector.
>
> Read the value displayed on the multimeter.
>
> For both pin checks, the multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.
>
> If either circuit is **not** closed, isolate the problem to the cab harness or ICON™ engine harness side of the circuit.
>
> Check the output wire on the cab harness side.
>
> Disconnect the 14-pin pass-through connector at the vehicle's firewall.
>
> Touch one of the multimeter leads to pin J of the 14-pin pass-through connector, cab harness side. Touch the other multimeter lead to pin B of the parking brake switch harness connector.
>
> Read the value displayed on the multimeter.
>
> Then, with one lead still touching to pin J of the 14-pin connector, cab harness side, touch the second multimeter lead to pin B of the ICON™ lamp harness connector.
>
> Read the value displayed on the multimeter.
>
> For both pin checks, the multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.
>
> If either circuit is **not** closed, repair or replace the cab harness. Refer to Procedure 019-202, 019-200, or [[97-019-305 — Cab Wiring Harness|019-305]].
>
> If both circuits are closed, repair or replace the ICON™ engine harness. Refer to Procedure 019-202, 019-208, or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Touch one multimeter lead to pin D of the 14-pin pass-through connector, cab harness side.
>
> Touch the other multimeter lead to pin A of the ICON™ lamp harness connector.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.
>
> If the circuit is **not** closed, repair or replace the cab harness. Refer to Procedure 019-202, 019-200, or [[97-019-305 — Cab Wiring Harness|019-305]].
>
> If the circuit is closed, repair or replace the ICON™ engine harness. Refer to Procedure 019-202, 019-208, or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Check the input wire on the cab harness side.
>
> Touch one of the multimeter leads to pin K of the 14-pin pass-through connector, cab harness side.
>
> Touch the other multimeter lead to pin A of the parking brake switch harness connector.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.
>
> If the circuit is **not** closed, repair or replace the cab harness. Refer to Procedure 019-202, 019-200, or [[97-019-305 — Cab Wiring Harness|019-305]].
>
> If the circuit is closed, isolate the problem to the correct portion of the ICON™ engine harness.
>
> Touch one of the multimeter leads to pin K of the 14-pin pass-through connector, engine harness side.
>
> Touch the other multimeter lead to pin 3 of the ICON™ idle control module A harness connector.
>
> Read the value displayed on the multimeter.
>
> Then, leaving the first lead in place on pin K of the 14-pin connector, touch the second multimeter lead to pin 2 of the ICON™ idle control module B harness connector.
>
> Read the value displayed on the multimeter.
>
> For both pin checks, the multimeter **must** display a reading of less than 10 ohms (closed circuit).
>
> If the circuit is **not** closed, check the portion of the circuit to the neutral position switch.
>
> First, verify that the neutral position switch is good. Replace neutral position switch as required.
>
> Disconnect the neutral position switch from the ICON™ engine harness.
>
> Touch one of the multimeter leads to pin K of the 14-pin pass-through connector, engine harness side. Touch the other multimeter lead to pin B of the neutral position switch harness connector.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 10 ohms (closed circuit).
>
> If the circuit is **not** closed, repair or replace the ICON™ engine harness.
>
> Refer to Procedure 019-202 or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Disconnect the hood tilt switch from the ICON™ engine harness.
>
> Touch one of the multimeter leads to pin A of the neutral position switch harness connector.
>
> Touch the other multimeter lead to pin B of the hood tilt switch harness connector.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 10 ohms (closed circuit).
>
> If the circuit is **not** closed, repair or replace the ICON™ engine harness.
>
> Refer to Procedure 019-202 or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Verify that the hood tilt switch is good.
>
> Touch one of the multimeter leads to pin A of the hood tilt switch harness connector.
>
> Touch the other multimeter lead to pin 3 of the ICON™ idle control module A harness connector.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 10 ohms (closed circuit).
>
> If the circuit is **not** closed, repair or replace the ICON™ engine harness.
>
> Refer to Procedure 019-202 or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Connect all components after completing the repair.
>
> ### Check for Short Circuit to Ground
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> Turn the keyswitch to the OFF position. Disconnect the vehicle battery cables from the battery. Disconnect the ICON™ battery harness connectors from the battery.
>
> **Note · Примечание**
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset using INSITE™.
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use test leads, Part No 3822758 and 3822917, when taking a measurement.
>
> Disconnect the ICON™ idle control module A and B connectors.
>
> Disconnect the 14-pin pass-through connector at the vehicle's firewall.
>
> Disconnect the parking brake switch and the ICON™ lamp from the cab harness.
>
> Disconnect the neutral position switch and hood tilt switch from the ICON™ engine harness.
>
> Set the multimeter to measure resistance.
>
> Touch one of the multimeter leads to pin B of the ICON™ lamp harness connector. Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> Then, touch one of the multimeter leads to pin A of the ICON™ lamp harness connector. Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> For both pin-to-ground checks, the multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, there is a short circuit to ground.
>
> Isolate the short to the cab harness or engine harness portion of the circuit.
>
> Touch one of the multimeter leads to pin B of the parking brake switch harness connector. Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> Then, touch one of the multimeter leads to pin A of the parking brake switch harness connector. Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> For both pin-to-ground checks, the multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, there is a short circuit to ground.
>
> Isolate the short to the cab harness or engine harness portion of the circuit.
>
> Touch one of the multimeter leads to pin J of the 14-pin pass-through connector, engine harness side. Touch the other multimeter lead to ground. Read the value displayed on the multimeter.
>
> Then, touch one of the multimeter leads to pin D of the 14-pin pass-through connector, engine harness side. Touch the other multimeter lead to ground. Read the value displayed on the multimeter.
>
> For both pin-to-ground checks, the multimeter **must** display a reading of more than 100k ohms, which is an open circuit. If either circuit is **not** open, check for a short circuit from the appropriate idle control module harness connector pin.
>
> If either circuit is open, repair or replace the cab harness. Refer to Procedure 019-202, 019-200, or [[97-019-305 — Cab Wiring Harness|019-305]].
>
> Touch one of the multimeter leads to pin K of the 14-pin pass-through connector, engine harness side.
>
> Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit. If the circuit is **not** open, isolate the short to either idle control module connector.
>
> If the circuit is open, repair or replace the cab harness. Refer to Procedure 019-202, 019-200, or [[97-019-305 — Cab Wiring Harness|019-305]].
>
> Touch one of the multimeter leads to pin 5 of the ICON™ idle control module A harness connector. Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> Then, touch one of the multimeter leads to pin 6 of the ICON™ idle control module A harness connector. Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> For both pin-to-ground checks, the multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If either circuit is **not** open, repair or replace the ICON™ engine harness.
>
> Refer to Procedure 019-208 or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Touch one of the multimeter leads to pin 2 of the ICON™ idle control module B harness connector.
>
> Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, repair or replace the ICON™ engine harness.
>
> Refer to Procedure 019-208 or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Touch one of the multimeter leads to pin A of the neutral position switch harness connector. Touch the other multimeter lead to ground. Read the value displayed on the multimeter.
>
> Then, touch one of the multimeter leads to pin B of the neutral position switch harness connector. Touch the other multimeter lead to ground. Read the value displayed on the multimeter.
>
> For both pin-to-ground checks, the multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If either circuit is **not** open, repair or replace the ICON™ engine harness. Refer to Procedure 019-202 or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Touch one of the multimeter leads to pin A of the hood tilt switch harness connector. Touch the other multimeter lead to ground. Read the value displayed on the multimeter.
>
> Then, touch one of the multimeter leads to pin B of the hood tilt switch harness connector. Touch the other multimeter lead to ground. Read the value displayed on the multimeter.
>
> For both pin-to-ground checks, the multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If either check is **not** open, repair or replace the ICON™ engine harness. Refer to Procedure 019-202 or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Touch one of the multimeter leads to pin 3 of the ICON™ idle control module A harness connector.
>
> Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If either circuit is **not** open, repair or replace the ICON™ engine harness. Refer to Procedure 019-202 or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Connect all components after completing the repair.
>
> ### Check for Short Circuit from Pin to Pin
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> Turn the keyswitch to the OFF position. Disconnect the vehicle battery cables from the battery. Disconnect the ICON™ battery harness connectors from the battery.
>
> **Note · Примечание**
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset using INSITE™.
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use test leads, Part No 3822758 and 3822917, when taking a measurement.
>
> Disconnect the ICON™ idle control module A and B connectors. Disconnect the 14-pin pass-through connector at the vehicle's firewall.
>
> Disconnect the parking brake switch and the ICON™ lamp from the cab harness.
>
> Disconnect the neutral position switch and the hood tilt switch from the ICON™ engine harness.
>
> Set the multimeter to measure resistance.
>
> Touch one of the multimeter leads to pin A of the parking brake switch harness connector.
>
> Touch the other multimeter lead to pin B of the harness connector.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short circuit between pin A and pin B.
>
> Repair or replace the cab harness. Refer to Procedure 019-202 or [[97-019-305 — Cab Wiring Harness|019-305]].
>
> Touch one of the multimeter leads to pin A of the ICON™ lamp harness connector.
>
> Touch the other multimeter lead to pin B of the harness connector.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short circuit between pin A and pin B.
>
> Repair or replace the cab harness. Refer to Procedure 019-202 or [[97-019-305 — Cab Wiring Harness|019-305]].
>
> Touch one of the multimeter leads to pin J of the 14-pin pass-through connector, cab harness side. Touch the other multimeter lead to all other pins in the connector, one at a time.
>
> Repeat the pin-to-pin check from pin D of the 14-pin connector, cab harness side, to all other pins in the connector, and from pin K to all other pins.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short circuit from pin J, pin D, or pin K to any other pin in the connector that registered a closed circuit.
>
> Repair or replace the cab harness. Refer to Procedure 019-200 or [[97-019-305 — Cab Wiring Harness|019-305]].
>
> Touch one of the multimeter leads to pin J of the 14-pin pass-through connector, engine harness side. Touch the other multimeter lead to all other pins in the connector, one at a time.
>
> Repeat the pin-to-pin check from pin D of the 14-pin connector, engine harness side, to all other pins in the connector, and from pin K to all other pins.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, there is a short circuit from pin J, pin D, or pin K in the 14-pin pass-through connector to any other pin in the connector that registered a closed circuit.
>
> Repair or replace the ICON™ engine harness. Refer to Procedure 019-200 or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Touch one of the multimeter leads to pin 3 of the ICON™ idle control module A harness connector. Touch the other multimeter lead to all other pins in the connector, one at a time.
>
> Repeat the pin-to-pin check from pin 5 of the ICON™ idle control module A harness connector to all other pins in the connector, and from pin 6 to all other pins.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, there is a short circuit from pin 3, pin 5, or pin 6 in the ICON™ idle control module A connector to any other pin in the connector that registered a closed circuit.
>
> Repair or replace the ICON™ engine harness. Refer to Procedure 019-208 or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Touch one of the multimeter leads to pin 2 of the ICON™ idle control module B harness connector.
>
> Touch the other multimeter lead to all other pins in the connector, one at a time.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, there is a short circuit from pin 2 in the ICON™ idle control module B connector to any other pin in the connector that registered a closed circuit.
>
> Repair or replace the ICON™ engine harness. Refer to Procedure 019-208 or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Touch one of the multimeter leads to pin A of the neutral position switch harness connector.
>
> Touch the other multimeter lead to pin B of the connector.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, there is a short circuit from pin A to pin B in the neutral position switch harness connector.
>
> Repair or replace the ICON™ engine harness. Refer to Procedure 019-202 or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Touch one of the multimeter leads to pin A of the hood tilt switch harness connector.
>
> Touch the other multimeter lead to pin B of the connector.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, there is a short circuit from pin A to pin B in the hood tilt switch harness connector.
>
> Repair or replace the ICON™ engine harness. Refer to Procedure 019-202 or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Connect all components after completing the repair.
>
> ### Check for Short Circuit to External Voltage Source
>
> Disconnect the ICON™ idle control module A and B connectors.
>
> Disconnect the ICON™ lamp and the parking brake switch from the cab harness.
>
> Set the multimeter to measure VDC.
>
> Turn the keyswitch to the ON position.
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use test lead, Part Number 3822758, when taking a measurement.
>
> Touch one of the multimeter leads to pin A of the ICON™ lamp harness connector. Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> Then, touch one of the multimeter leads to pin B of the ICON™ lamp harness connector. Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> For both pin-to-ground checks, the multimeter **must** display a reading of less than 0.5 VDC. If the voltage is **not** less than 0.5 VDC, there is a short circuit to an external voltage source.
>
> **Note · Примечание**
> An external voltage source is any wire in the cab or engine harness wiring that carries voltage.
>
> Remove the external voltage source.
>
> Touch one of the multimeter leads to pin A of the parking brake switch harness connector. Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> Then, touch one of the multimeter leads to pin B of the parking brake switch harness connector. Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> For both pin-to-ground checks, the multimeter **must** display a reading of less than 0.5 VDC. If the voltage is **not** less than 0.5 VDC, there is a short circuit to an external voltage source.
>
> **Note · Примечание**
> An external voltage source is any wire in the cab or engine harness wiring that carries voltage.
>
> Remove the external voltage source.
>
> Connect all components after completing the repair.
