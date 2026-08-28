---
aliases:
  - "Воздух в топливе"
type: "Процедура"
doc: "89-006-003"
title_en: "Air in Fuel"
title_ru: "Воздух в топливе"
modified: "2023-01-27"
engines:
  - "85017333"
families:
  - "QSK23"
manuals:
  - "4021375"
figures: 10
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/89/89-006-003.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/89-006-003.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "группа/89"
  - "перевод/машинный"
---

# Air in Fuel
**Воздух в топливе**

> [!abstract] Процедура · `89-006-003`
> **Двигатели:** [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23
> **Входит в руководства:** [[4021375 — QSK23 Troubleshooting and Repair Manual|4021375]]
> **Секции:** Section 6 - Injectors and Fuel Lines - Group 06
> **Даты:** изменён 2023-01-27
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/89/89-006-003.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/89-006-003.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

> [!warning] ОСТОРОЖНО
> Топливо огнеопасно. Держите все сигареты, пламя, пилотные огни, дуговое оборудование и выключатели из рабочей зоны и областей, разделяющих вентиляцию, чтобы уменьшить вероятность серьезных травм или смерти при работе на топливной системе.

Существует два способа проверки наличия воздуха в топливе.

- Метод визуального стекла
- Метод слива насоса.

![[06400183.png]]

### Проверка

Метод визуального стекла

Удалите впускную линию топлива, соединяющую головку крепления топливного фильтра с топливным насосом.

Заменить топливный трубопровод на прицельное стекло, номер детали 3164387, и адаптерный шланг, номер детали 3165146 или эквивалент.

Работайте с двигателем на высоком холостом ходу без нагрузки.

> [!note] Примечание
> Небольшая утечка воздуха будет иметь «молочный» вид.

> [!note] Примечание
> Большая утечка воздуха будет выглядеть как пузырьки в топливе.

> [!note] Примечание
> Если приложение включает в себя дневной бак или топливную систему с положительной головкой (PHFS), рекомендуется нанести прицельное стекло перед этим аксессуаром, поскольку эти устройства могут маскировать присутствие воздуха в топливе вверх по течению.

![[06400184.png]]

Если обнаружена утечка воздуха, выполните следующее:

- Систематически проверяйте всю маршрутизацию подачи топлива для источников проникновения воздуха, начиная с топливного бака, за которым следуют все соединительные соединения шлангов / трубок, оборудование для фильтрации топлива и дневной бак / ПХФС, если предусмотрено. Затягивайте любые свободные связи по мере необходимости.
- Проверьте капельную трубку в топливном баке на предмет повреждения.
- Проверьте возврат топлива в бак и убедитесь, что трубка находится как выше уровня топлива, так и на минимальном расстоянии 305 мм [12 в ] от соединения подачи топлива.
- Проверьте топливные кольца для подачи топлива на предмет повреждения.

![[ft8hssa.png]]

Продолжайте тестировать и искать источник воздуха, пока не появятся пузырьки воздуха.

Удалите стекло зрения.

Затяните впускной шланг.

> [!tip] Момент затяжки
> 88 Н·м [65 фунт-фут]

Повторное испытание двигателя, дублирующего условия эксплуатации, когда жалоба на эксплуатационные характеристики подтвердила наличие воздуха в топливной коррекции. Это особенно важно для резервных приложений генератора с нечастыми запусками и может потребовать тестирования после длительного периода отдыха.

![[06400185.png]]

Метод вытяжки грушевого насоса

> [!danger] ОПАСНО
>

Для проведения испытания на топливо с использованием бокового воздуха под давлением используйте следующие элементы:

- Быстрая подборка для отключения, номер детали 3376859
- шланг высокого давления
- Клапан давления (способен работать с 2758 кПа \[400 psi\])
- Чистая трубка
- Чистый контейнер.

![[06400034.png]]

Подключите оборудование к быстрому соединению, установленному на выходе топливного насоса.

Положите конец прозрачного шланга в чистый контейнер.

Закройте клапан давления.

![[06400186.png]]

Работайте с двигателем на высоком холостом ходу без нагрузки.

Медленно открывайте клапан, пока не будет виден постоянный поток топлива.

![[06400036.png]]

Положите конец шланга под поверхность топлива.

Если будет утечка воздуха, будут видны пузырьки.

> [!note] Примечание
> Если приложение включает в себя дневной бак или топливную систему с положительной головкой, рекомендуется использовать метод стекла, размещенный перед этим аксессуаром, поскольку эти устройства могут маскировать присутствие воздуха в топливе вверх по течению.

![[06400187.png]]

Если обнаружена утечка воздуха, выполните следующее:

- Систематически проверяйте всю маршрутизацию подачи топлива для источников проникновения воздуха, начиная с топливного бака, за которым следуют все соединительные соединения шлангов / трубок, оборудование для фильтрации топлива и дневной бак / ПХФС, если предусмотрено. Затягивайте любые свободные связи по мере необходимости.
- Проверьте капельную трубку в топливном баке на предмет повреждения.
- Проверьте возврат топлива в бак и убедитесь, что трубка находится как выше уровня топлива, так и на минимальном расстоянии 305 мм [12 в ] от соединения подачи топлива.
- Проверьте подачу топлива, устанавливающего кольца для повреждений.

![[ft8hssa.png]]

Продолжайте тестировать и искать утечки воздуха, пока не появятся пузырьки.

Удалите испытательное оборудование.

Затяните впускной шланг.

> [!tip] Момент затяжки
> 120 Н·м [89 фунт-фут]

Повторное испытание двигателя, дублирующего условия эксплуатации, когда жалоба на эксплуатационные характеристики подтвердила наличие воздуха в топливной коррекции. Это особенно важно для резервных приложений генератора с нечастыми запусками и может потребовать тестирования после длительного периода отдыха.

![[06400186.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> **CAUTION · Осторожно**
> Fuel is flammable. Keep all cigarettes, flames, pilot lights, arcing equipment, and switches out of the work area and areas sharing ventilation to reduce the possibility of severe personal injury or death when working on the fuel system.
>
> There are two good methods to check for air in the fuel.
>
> - Sight glass method
> - Gear pump drain method.
>
> ### Test
>
> Sight Glass Method
>
> Remove the fuel inlet line connecting the fuel filter head to the fuel pump.
>
> Replace the fuel line with the fuel sight glass, Part Number 3164387, and adapter hose, Part Number 3165146, or equivalent.
>
> Operate the engine at high idle with no load.
>
> **Note · Примечание**
> A small air leak will have a “milky” appearance.
>
> **Note · Примечание**
> A large air leak will look like bubbles in the fuel.
>
> **Note · Примечание**
> If the application incorporates a Day tank or a Positive Head Fuel System (PHFS) it is recommended to apply a sight glass before this accessory as these devices may mask the presence of air in fuel upstream.
>
> If an air leak is found, perform the following:
>
> - Systematically inspect the entire fuel supply routing for sources of air ingress starting at the fuel tank followed by all hose/tube interconnections, fuel filtration hardware and day tank/PHFS if provisioned. Tighten any loose connections as needed.
> - Check the drop tube in the fuel tank for damage.
> - Check the fuel return to tank and ensure the tube is both above fuel level and at a minimum distance of 305 mm \[ 12 in \] from the fuel supply connection.
> - Check the fuel fitting supply o-rings for damage.
>
> Continue to test and look for a source of air until no air bubbles are visible.
>
> Remove the sight glass.
>
> Tighten the fuel inlet hose.
>
> **Момент затяжки · Torque Value**
> 88 n•m [65 ft-lb]
>
> Retest engine duplicating the operating conditions when performance complaint occurred to confirm air in fuel correction. This is especially important for standby Generator applications with infrequent starts and may require testing after an extended rest period.
>
> Gear Pump Drain Method
>
> **WARNING · Опасно**
>
> To perform a pressure side air in fuel test, use the following items:
>
> - Quick disconnect fitting, Part Number 3376859
> - High pressure hose
> - Pressure valve (capable of 2758 kPa \[400 psi\])
> - Clean tubing
> - Clean container.
>
> Connect the equipment to the quick-connect fitting at the fuel pump outlet.
>
> Put the end of the clear hose in the clean container.
>
> Close the pressure valve.
>
> Operate the engine at high idle with no load.
>
> Slowly open the valve until a steady stream of fuel is visible.
>
> Put the end of the hose below the surface of the fuel.
>
> If there is an air leak, bubbles will be visible.
>
> **Note · Примечание**
> If the application incorporates a Day tank or a Positive Head Fuel System it is recommended to use the Sight Glass Method placed before this accessory as these devices may mask the presence of air in fuel upstream.
>
> If an air leak is found, perform the following:
>
> - Systematically inspect the entire fuel supply routing for sources of air ingress starting at the fuel tank followed by all hose/tube interconnections, fuel filtration hardware and day tank/PHFS if provisioned. Tighten any loose connections as needed.
> - Check the drop tube in the fuel tank for damage.
> - Check the fuel return to tank and ensure the tube is both above fuel level and at a minimum distance of 305 mm \[ 12 in \] from the fuel supply connection.
> - Check the fuel supply fitting o-rings for damage.
>
> Continue to test and look for air leaks until there are no bubbles visible.
>
> Remove the test equipment.
>
> Tighten the fuel inlet hose.
>
> **Момент затяжки · Torque Value**
> 120 n•m [89 ft-lb]
>
> Retest engine duplicating the operating conditions when performance complaint occurred to confirm air in fuel correction. This is especially important for standby Generator applications with infrequent starts and may require testing after an extended rest period.
