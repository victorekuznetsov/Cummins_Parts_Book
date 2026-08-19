---
aliases:
  - "Воздух в топливе"
type: "Процедура"
doc: "20-006-003"
title_en: "Air in Fuel"
title_ru: "Воздух в топливе"
modified: "2023-01-02"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021592"
figures: 12
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-006-003.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/20-006-003.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/20"
  - "перевод/машинный"
---

# Air in Fuel
**Воздух в топливе**

> [!abstract] Процедура · `20-006-003`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual|4021592]]
> **Секции:** Section 6 - Injectors and Fuel Lines - Group 06
> **Даты:** изменён 2023-01-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-006-003.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/20-006-003.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

с форсункой механического управления

> [!danger] ОПАСНО
> Топливо огнеопасно. Не допускать сигарет, пламени, искр, дуговых выключателей или оборудования, пилотных огней или других источников зажигания вблизи топливной системы.

Существует два хороших способа проверки наличия воздуха в топливе на топливной системе с механически приводимым в действие топливным форсункой:

- Метод визуального стекла
- Метод высыхания грушевого насоса.

![[fp8tbka.png]]

с форсункой электронного управления

Для двигателей с топливным форсункой с электронным приводом используйте процедуру Prime (Стадия 1) для проверки наличия воздуха в топливной системе и удаления всего воздуха из топливной системы.[[20-006-075-tr — Fuel Filter (Stage 1)|См. процедуру 006-075 в разделе 6.]]

![[06k00007.png]]

> [!danger] ОПАСНО
> Топливо огнеопасно. Не допускать сигарет, пламени, искр, дуговых выключателей или оборудования, пилотных огней или других источников зажигания вблизи топливной системы.

Если воздух все еще виден после завершения предыдущей процедуры, проверьте линии подачи топлива на наличие свободных соединений или поврежденных колец.[[20-006-024-tr — Fuel Supply Lines|См. процедуру 006-024 в разделе 6.]]

![[06k00008.png]]

### Проверка

с форсункой механического управления

> [!danger] ОПАСНО
> Топливо огнеопасно. Не допускать сигарет, пламени, искр, дуговых выключателей или оборудования, пилотных огней или других источников зажигания вблизи топливной системы.

#### Метод визуального стекла

- Удалить линию впуска топлива
- Установите прицельное стекло, номер детали 3163270, на входе топливного насоса.
- Работайте с двигателем на высоком холостом ходу без нагрузки.

Небольшая утечка воздуха будет иметь «молочный» вид.

Большая утечка воздуха будет выглядеть как пузырьки в топливе.

> [!note] Примечание
> Если приложение включает в себя дневной бак или топливную систему с положительной головкой, рекомендуется нанести прицельное стекло перед этим аксессуаром, поскольку эти устройства могут маскировать присутствие воздуха в топливе вверх по течению.

![[06400061.png]]

Если обнаружена утечка воздуха, выполните следующее.

- Систематически проверяйте всю маршрутизацию подачи топлива для источников проникновения воздуха, начиная с топливного бака, за которым следуют все соединительные соединения шлангов / трубок, оборудование для фильтрации топлива и система дневного бака / положительной головки топлива, если она предусмотрена. Затягивайте любые свободные связи по мере необходимости.
- Проверьте капельную трубку в топливном баке на предмет повреждения.
- Проверьте возврат топлива в бак и убедитесь, что трубка находится как выше уровня топлива, так и на минимальном расстоянии 305 мм [12 в ] от соединения подачи топлива.
- Проверьте кольца на предмет повреждений.

![[ft8hssa.png]]

Продолжайте тестировать и искать источник воздуха, пока не будут видны пузырьки воздуха.

Удалите стекло зрения.

Установите и затяните впускной шланг топлива.

> [!tip] Момент затяжки
> 88 Н·м [65 фунт-фут]

Повторно проверить двигатель, дублирующий условия эксплуатации, когда жалоба на производительность подтвердила наличие воздуха в топливной коррекции. Это особенно важно для резервных приложений генератора с нечастыми запусками и может потребовать тестирования после длительного периода отдыха.

![[06400033.png]]

Метод вытяжки грушевого насоса

Для проведения испытания топлива на боковой воздух под давлением используйте следующие элементы.

- Быстрое отключение, номер детали. 3376859
- Хранилище высокого давления
- Клапан давления (способен работать с 2758 кПа \[400 psi\])
- Чистая трубка
- Чистый контейнер

![[06400034.png]]

Подключите оборудование к быстрому соединению, установленному на выходе топливного насоса.

Поместите конец прозрачного шланга в чистый контейнер.

![[06400035.png]]

Работайте с двигателем на высоком холостом ходу без нагрузки. ** Медленно откройте клапан, пока не будет виден постоянный поток топлива.

![[06400036.png]]

Поместите конец шланга под поверхностью топлива.

Если будет утечка воздуха, будут видны пузырьки.

> [!note] Примечание
> Если приложение включает в себя дневной бак или топливную систему с положительной головкой, рекомендуется использовать метод стекла, размещенный перед этим аксессуаром, поскольку эти устройства могут маскировать присутствие воздуха в топливе вверх по течению.

![[06400062.png]]

Если обнаружена утечка воздуха, выполните следующее.

- Систематически проверяйте всю маршрутизацию подачи топлива для источников проникновения воздуха, начиная с топливного бака, за которым следуют все соединительные соединения шлангов / трубок, оборудование для фильтрации топлива и система дневного бака / положительной головки топлива, если она предусмотрена. Затягивайте любые свободные связи по мере необходимости.
- Проверьте капельную трубку в топливном баке на предмет повреждения.
- Проверьте возврат топлива в бак и убедитесь, что трубка находится как выше уровня топлива, так и на минимальном расстоянии 305 мм [12 в ] от соединения подачи топлива.
- Проверьте кольца на предмет повреждений.

![[ft8hssa.png]]

Продолжайте тестировать и искать утечки воздуха, пока не появятся пузыри.

Удалите испытательное оборудование.

Повторное испытание двигателя, дублирующего условия эксплуатации, когда жалоба на эксплуатационные характеристики подтвердила наличие воздуха в топливной коррекции. Это особенно важно для резервных приложений генератора с нечастыми запусками и может потребовать тестирования после длительного периода отдыха.

Установите и затяните впускной шланг топлива.

> [!tip] Момент затяжки
> 88 Н·м [65 фунт-фут]

![[06400035.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> with Mechanically Actuated Injector
>
> **WARNING · Опасно**
> Fuel is flammable. Do not allow cigarettes, flames, sparks, arcing switches or equipment, pilot lights or other ignition sources near the fuel system.
>
> There are two good methods to check for air in the fuel on a fuel system with mechanically actuated injectors:
>
> - Sight Glass Method
> - Gear Pump Drain Method.
>
> with Electronically Actuated Injector
>
> For engines with electronically actuated injectors, use the Prime section of the Fuel Filter (Stage 1) procedure to check for air in the fuel system and to remove all the air from the fuel system. [[20-006-075-tr — Fuel Filter (Stage 1)|Refer to Procedure 006-075 in Section 6.]]
>
> **WARNING · Опасно**
> Fuel is flammable. Do not allow cigarettes, flames, sparks, arcing switches or equipment, pilot lights or other ignition sources near the fuel system.
>
> If air is still seen after completing the previous procedure, check the fuel supply lines for loose connections or damaged o-rings. [[20-006-024-tr — Fuel Supply Lines|Refer to Procedure 006-024 in Section 6.]]
>
> ### Test
>
> with Mechanically Actuated Injector
>
> **WARNING · Опасно**
> Fuel is flammable. Do not allow cigarettes, flames, sparks, arcing switches or equipment, pilot lights or other ignition sources near the fuel system.
>
> #### Sight Glass Method
>
> - Remove the fuel inlet line
> - Install a sight glass, Part Number 3163270, at the inlet of the fuel pump.
> - Operate the engine at high idle with no load.
>
> A small air leak will have a "milky" appearance.
>
> A large air leak will look like bubbles in the fuel.
>
> **Note · Примечание**
> If the application incorporates a Day tank or a Positive Head Fuel System it is recommended to apply a sight glass before this accessory as these devices may mask the presence of air in fuel upstream.
>
> If an air leak is found, perform the following.
>
> - Systematically inspect the entire fuel supply routing for sources of air ingress starting at the fuel tank followed by all hose/tube interconnections, fuel filtration hardware and day tank/positive head fuel system, if provisioned. Tighten any loose connections as needed.
> - Check the drop tube in the fuel tank for damage.
> - Check the fuel return to tank and ensure the tube is both above fuel level and at a minimum distance of 305 mm \[ 12 in \] from the fuel supply connection.
> - Check the o-rings for damage.
>
> Continue to test and look for the source of the air until **no** air bubbles are visible.
>
> Remove the sight glass.
>
> Install and tighten the fuel inlet hose.
>
> **Момент затяжки · Torque Value**
> 88 n•m [65 ft-lb]
>
> Retest the engine duplicating the operating conditions when performance complaint occurred to confirm air in fuel correction. This is especially important for standby Generator applications with infrequent starts and may require testing after an extended rest period.
>
> Gear Pump Drain Method
>
> To perform a pressure side air in fuel test, use the following items.
>
> - Quick disconnect fitting, Part No. 3376859
> - High pressure Hose
> - Pressure valve (capable of 2758 kPa \[400 psi\])
> - Clean tubing
> - Clean container
>
> Connect the equipment to the quick-connect fitting at the fuel pump outlet.
>
> Place the end of the clear hose in the clean container.
>
> Operate the engine at high idle with no load. **Slowly** open the valve until a steady stream of fuel is visible.
>
> Place the end of the hose below the surface of the fuel.
>
> If there is an air leak, bubbles will be visible.
>
> **Note · Примечание**
> If the application incorporates a Day tank or a Positive Head Fuel System it is recommended to use the Sight Glass Method placed before this accessory as these devices may mask the presence of air in fuel upstream.
>
> If an air leak is found, perform the following.
>
> - Systematically inspect the entire fuel supply routing for sources of air ingress starting at the fuel tank followed by all hose/tube interconnections, fuel filtration hardware and day tank/positive head fuel system, if provisioned. Tighten any loose connections as needed.
> - Check the drop tube in the fuel tank for damage.
> - Check the fuel return to tank and ensure the tube is both above fuel level and at a minimum distance of 305 mm \[ 12 in \] from the fuel supply connection.
> - Check the o-rings for damage.
>
> Continue to test and look for air leaks until there are **no** bubbles visible.
>
> Remove the test equipment.
>
> Retest engine duplicating the operating conditions when performance complaint occurred to confirm air in fuel correction. This is especially important for standby Generator applications with infrequent starts and may require testing after an extended rest period.
>
> Install and tighten the fuel inlet hose.
>
> **Момент затяжки · Torque Value**
> 88 n•m [65 ft-lb]
