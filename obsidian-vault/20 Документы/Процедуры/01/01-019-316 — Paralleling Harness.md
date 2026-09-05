---
aliases:
  - "Жгут параллельной работы"
type: "Процедура"
doc: "01-019-316"
title_en: "Paralleling Harness"
title_ru: "Жгут параллельной работы"
modified: "2003-06-30"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 13
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-316.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-316.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Paralleling Harness
**Жгут параллельной работы**

> [!abstract] Процедура · `01-019-316`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-06-30
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-316.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-316.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Параллельная проводка используется, когда генераторный набор находится в параллельном приложении с другими генераторными установками. Параллельная проводка соединяет параллельную плату с платой PT/CT, PT-модулем шины, модулем распределения мощности и несколькими терминальными блоками в TB3 для подключения клиентов.

![[19802742.png]]

### Снятие

Отсоедините 50-контактный разъем D-sub 04 от параллельной платы в карточной клетке.

![[19802661.png]]

> [!note] Примечание
> Некоторые генераторные установки QSK60 не будут иметь этот модуль питания и разъем.

Отсоедините 4-контактный AMP-разъем 27 от силового модуля в блоке управления.

![[19802819.png]]

Отсоедините 23-контактный разъем AMP 08 от платы PT/CT.

Также будет еще один 23-контактный разъем AMP 08 от ремня управления генератором, который останется неиспользованным.

![[19802834.png]]

Удалите проводку с параллельной проводкой из модуля PT шины в TB2.

Удалите каждый из шести проводов, ослабив соответствующий винт на PT-модуле шины.

![[19802826.png]]

Удалите проводку клиента в TB3 из терминальных блоков 21-32.

Удалите терминалы TB3 блоков 21-32.

Удалите винт в нижнем зажиме, который удерживает нижние оконечные блоки на месте. Удалите клип.

![[19802823.png]]

Скользите с терминала и спуститесь с железнодорожного терминала. Удалить только те блоки, которые являются частью параллельной проводов.

Удалите все проводов, поддерживающие ремни.

Убедитесь, что все соединения, сделанные параллельной проводкой, отключены и распутаны.

Медленно вытащите из коробки управления проводящую проводку, убедившись, что нет связывания или запутывания.

![[19802824.png]]

### Установка

Замените любые поддерживающие скобки жгута проводов.

Маршрутируйте электропроводку через необходимые опоры и места маршрутизации.

Установите терминалы TB3 блоков 21-32.

Скользите с терминала и на железнодорожный вокзал.

![[19802824.png]]

Установите нижнюю зажимку и затяните винт, чтобы удерживать терминальные блоки на месте.

Установите клиентскую проводку на соответствующие терминальные блоки на TB3.

![[19802823.png]]

Установите проводку параллельной проводов на модуль PT шины в TB2.

Установите каждый из шести проводов, затянув соответствующий винт на PT-модуле шины.

![[19802826.png]]

Подключите 23-контактный разъем AMP 08 к плате PT/CT.

Будьте осторожны **не**, чтобы подключить идентичный 23-контактный разъем AMP 08 от электропроводки управления генератором. Этот разъем **не будет **использоваться при использовании параллельной проводов.

![[19802834.png]]

> [!note] Примечание
> Некоторые генераторные установки QSK 60 будут иметь этот модуль питания и разъем.

Подключите 4-контактный AMP-разъем 27 к модулю питания в блоке управления.

![[19802819.png]]

Подключите 50-контактный разъем D-sub 04 к параллельной плате в карточной клетке. Затягивай джек-круки.

Дважды проверьте, что все параллельные соединения с проводкой управления безопасны.

Подключите инструмент электронного сервиса и проверьте наличие кодов неисправностей.

![[19802661.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The paralleling harness is used when the generator set is in a paralleling application with other generator sets. The paralleling harness connects the parallel board with the PT/CT board, the bus PT module, power distribution module, and several terminal blocks at TB3 for customer connections.
>
> ### Remove
>
> Disconnect the 50-pin D-sub connector 04 from the parallel board in the card cage.
>
> **Note · Примечание**
> Some QSK60 generator sets will **not** have this power module and connector.
>
> Disconnect the 4-pin AMP connector 27 from the power module in the controls box.
>
> Disconnect the 23-pin AMP connector 08 from the PT/CT board.
>
> There will also be another 23-pin AMP connector 08 from the generator control harness that will remain unused.
>
> Remove the paralleling harness wiring from the bus PT module at TB2.
>
> Remove each of the six wires by loosening the corresponding screw on the bus PT module.
>
> Remove customer wiring to TB3 from terminal blocks 21 to 32.
>
> Remove TB3 terminal blocks 21 to 32.
>
> Remove the screw in the lower clip that holds the lower terminal blocks in place. Remove the clip.
>
> Slide the terminal blocks down and off the terminal rail. **Only** remove terminal blocks that are part of the paralleling harness.
>
> Remove any harness supports.
>
> Make sure that all connections made by the paralleling harness are disconnected and untangled.
>
> Slowly pull the paralleling harness out of the controls box, making sure that there is no binding or tangling.
>
> ### Install
>
> Replace any harness support brackets.
>
> Route the harness through the necessary supports and routing locations.
>
> Install TB3 terminal blocks 21 to 32.
>
> Slide the terminal blocks up and onto the terminal rail.
>
> Install the lower clip and tighten the screw to hold the terminal blocks in place.
>
> Install customer wiring to appropriate terminal blocks on TB3.
>
> Install the paralleling harness wiring to the bus PT module at TB2.
>
> Install each of the six wires by tightening down the corresponding screw on the bus PT module.
>
> Connect the 23-pin AMP connector 08 to the PT/CT board.
>
> Be careful **not** to connect the identical 23-pin AMP connector 08 from the generator control harness. This connector will **not** be used when the paralleling harness is being used.
>
> **Note · Примечание**
> Some QSK 60 generator sets will **not** have this power module and connector.
>
> Connect the 4-pin AMP connector 27 to the power module in the controls box.
>
> Connect the 50-pin D-sub connector 04 to the parallel board in the card cage. Tighten down jackscrews.
>
> Double-check that all paralleling control harness connections are secure.
>
> Connect the electronic service tool and check for any fault codes.
