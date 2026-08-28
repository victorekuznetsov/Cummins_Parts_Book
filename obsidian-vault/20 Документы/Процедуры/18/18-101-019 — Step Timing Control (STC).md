---
aliases:
  - "Ступенчатое управление опережением впрыска (STC)"
type: "Процедура"
doc: "18-101-019"
title_en: "Step Timing Control (STC)"
title_ru: "Ступенчатое управление опережением впрыска (STC)"
modified: "2006-07-28"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "33239746"
  - "33239899"
  - "37269910"
  - "37280605"
  - "41349633"
  - "41353297"
  - "85017333"
families:
  - "K19"
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSK19"
  - "QSK23"
  - "QSK60"
manuals:
  - "3666013"
  - "3666120"
  - "3810497"
  - "4021375"
  - "4021530"
figures: 3
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/18/18-101-019.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/18-101-019.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "двигатель/K38/K50"
  - "двигатель/QSK19"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/18"
  - "перевод/машинный"
---

# Step Timing Control (STC)
**Ступенчатое управление опережением впрыска (STC)**

> [!abstract] Процедура · `18-101-019`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** K19, K38/K50 · QSK38, QSK50, QSK60, QSK19, QSK23, QSK60
> **Входит в руководства:** [[3666013 — K19 Industrial and Marine Operation and Maintenance Manual|3666013]], [[3666120 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Operation and Maintenance Manual|3666120]], [[3810497 — K38, K50, QSK38 and QSK50 Operation and Maintenance Manual|3810497]], [[4021375 — QSK23 Troubleshooting and Repair Manual|4021375]], [[4021530 — QSK45 and QSK60 Service Manual|4021530]]
> **Секции:** Section 1 - Operating Instructions
> **Даты:** изменён 2006-07-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/18/18-101-019.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/18-101-019.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Некоторые модели двигателей оснащены системой управления временем шага (STC). Контроль времени шага позволяет двигателю работать в расширенном режиме впрыска сразу после запуска и условий нагрузки двигателя легкой службы, а также вернуться к нормальному времени в условиях средней и высокой нагрузки двигателя.

К числу преимуществ относятся:

- Улучшенные характеристики холостого хода
- Сниженный холодный белый дым
- Улучшенная экономия топлива при легкой нагрузке.

**Не** пытаться обойти или иным образом подделать клапан управления маслом или сантехнику STC. Это приведет к потере как экономии топлива, так и долговечности двигателя. Правильная работа клапана необходима для поддержания приемлемых давлений и температур цилиндров и обеспечения оптимальной экономии топлива во время работы с высокой нагрузкой. Правильная работа также необходима для контроля белого дыма на холостом ходу.

![[bp4vaub.png]]

При работе в продвинутом режиме можно отметить легкий тикающий шум на верхних сиденьях. Этот звук является нормальным и вызван приведением в действие гидравлических кранов STC во время каждого цикла инъекции.

![[ew400ki.png]]

Для оптимального управления белым дымом на двигателях, оснащенных STC, не увеличивайте скорость двигателя выше холостого хода во время запуска двигателя, пока достаточное давление масла не достигнет кранов STC и не переключит весь форсунка в расширенный режим времени.

![[bp4vauc.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> Some engine models are equipped with step timing control (STC). Step timing control allows the engine to operate in advanced injection timing immediately after start-up and light duty engine load conditions, and to return to normal timing during medium and high engine load conditions.
>
> Benefits include:
>
> - Improved cold weather idling characteristics
> - Reduced cold weather white smoke
> - Improved light load fuel economy.
>
> Do **not** attempt to bypass or otherwise tamper with the STC oil control valve or plumbing. This will result in the loss of both fuel economy and engine durability. Correct valve operation is necessary to maintain acceptable cylinder pressures and temperatures, and to yield optimal fuel economy during high-load operation. Correct operation is also necessary to control white smoke at idle.
>
> When operating in the advanced mode, a light ticking noise can be noted at the overhead. This sound is normal, and is caused by the actuation of the STC hydraulic tappets during each injection cycle.
>
> For optimal white smoke control on STC-equipped engines, do not increase engine speed above idle during engine start-up until sufficient oil pressure reaches the STC tappets and shifts all injectors into the advanced timing mode.
