---
aliases:
  - "Цепь электромагнита форсунки"
type: "Процедура"
doc: "82-019-058"
title_en: "Injector Solenoid Circuit"
title_ru: "Цепь электромагнита форсунки"
modified: "2005-01-28"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 38
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-058.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-058.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Injector Solenoid Circuit
**Цепь электромагнита форсунки**

> [!abstract] Процедура · `82-019-058`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2005-01-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-058.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-058.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

> [!danger] ОПАСНО
> На электромагниты форсунок при работающем двигателе подаётся высокое напряжение. Чтобы уменьшить вероятность получения травмы или смерти от поражения электрическим током, не носите ювелирные изделия или сырую одежду, и не прикасайтесь к соленоидам форсунки или соленоидным проводам при работе двигателя.

> [!warning] ОСТОРОЖНО
> Не используйте щупы или провода, отличные от Части № 3822758. Разъём будет повреждён. Лиды должны плотно помещаться в разъеме без расширения контактов разъема.

Осмотрите соленоидную схему форсунки цилиндра, указанную на зарегистрированном коде неисправности. См. прилагаемый график для штифтов схемы форсунки проблемного цилиндра. Цилиндр No1 будет использоваться в этом примере.

![[19200339.png]]

Штифты цепей следующие:

| Контакты с поставщиками | обратный контакт |  |  |  |  |  |
|---|---|---|---|---|---|---|
| Кайл. № | ECM Конн. | 15-пин Конн. | Индж. Пин | ECM Конн. | 15-пин Конн. | Индж. Пин |
| 1 | 10 | 01 | А. | 09 | 02 | B |
| 2 | 08 | 03 | А. | 07 | 04 | B |
| 3 | 06 | 05 | А. | 16 | 06 | B |
| 4 | 26 | 07 | А. | 36 | 08 | B |
| 5 | 04 | 09 | А. | 03 | 10 | B |
| 6 | 02 | 11 | А. | 01 | 12 | B |

![[19200333.png]]

Переключатель зажигания транспортного средства в положение выключения.

Отсоедините разъем электропроводки привода от ECM.

Вставьте испытательный щуп в контакт поставки (контакт 10 в этом примере) разъёма проводов привода. Вставьте другой свинец в обратный контакт (контакт 09 в этом примере) разъёма проводов привода. Подключите аллигаторы к многометровым зондам.

![[19200338.png]]

Измерьте сопротивление. Вычтите значение сопротивления многометрового испытательного щупа из этого значения, чтобы определить истинное значение сопротивления цепи форсунки. Сопротивление **должно быть от 0,5 до 1,5 Ом. Если значение сопротивления **не** правильно, то следует перейти к следующим разделам: Если сопротивление правильное, схема **должна все еще проверяться на короткое замыкание на землю и короткое замыкание от пин-кодов до пин-кодов.

> [!note] Примечание
> Если измерение сопротивления составляет менее 10 Ом, схема приемлема, если сопротивление соленоида форсунки находится в пределах 0,5-1,5 Ом (см. Значение сопротивления выше спецификации).

![[oi801k07.png]]

Значение сопротивления ниже спецификаций

Снять клапанную крышку сборки.

Осмотрите форсунку соленоидных проводов для коротких замыканий между проводами. Если провода повреждены, замените провода. См. процедуру[[82-019-057 — Injector Solenoid|019-057]].

![[ee2coka.png]]

Отсоедините форсунку питания и возвратные провода от соленоида проблемного цилиндра.

Используйте небольшую отвертку, чтобы удалить защитную крышку из соленоида.

Удалите сборку гайки из форсунки соленоида.

![[ee2cokh.png]]

Измерьте сопротивление между двумя столбами или соединением соленоида форсунки. Вычтите сопротивление мультиметра. Истинное сопротивление соленоидов форсунки **должно быть от 0,5 до 1,5 Ом. Если значение сопротивления **не правильно, замените форсунку. См. процедуру 006-026 в Руководстве по устранению неполадок и ремонту, Двигатели ISM и QSM11, Вестник [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]].

![[fi2cnka.png]]

Если значение сопротивления соленоида форсунки правильное, проблема заключается во внутренней или внешней проводах привода. Изолируйте проблему, проверяя каждую проводку отдельно.

![[19200339.png]]

Отсоедините разъем внутри головы.

Проверьте внутреннюю проводку привода. Измерьте сопротивление между двумя пленными узлами гайки или соединением соленоидной проволоки форсунки, которая была удалена из соленоида форсунки. Сопротивление **должно быть открытым контуром (более 100k Ом). Если сопротивление меньше 100k Ом, замените внутреннюю проводку привода. См. процедуру 019-063. **Не ремонтировать внутреннюю проводку привода.

Подключите 15-контактный разъем, когда ремонт будет завершен.

![[ee2coke.png]]

Проверьте внешний привод проводов жгута. Убедитесь, что 15-контактный разъем все еще отключен. Вставьте испытательный щуп в контакт питания (контакт 10 в этом примере) разъёма проводов привода. Вставьте штифт другого свинца в обратный контакт (контакт 09 в этом примере) разъема проводов привода. Подключите аллигаторы к многометровым зондам.

![[19200338.png]]

Измерьте сопротивление. Сопротивление должно быть открытым контуром (более 100k Ом). Если сопротивление меньше 100k Ом, отремонтируйте или замените внешний привод проводов ремня. См. процедуру[[82-019-043-tr — Engine Wiring Harness|019-043]].

Подключите 15-контактный разъем, когда ремонт будет завершен.

![[19200338.png]]

Значение сопротивления выше спецификации

Снять клапанную крышку сборки.

Проверьте форсунку соленоидных проводов на наличие сломанных проводов. Если провода повреждены, замените провода. См. процедуру[[82-019-057 — Injector Solenoid|019-057]]. Не надо чинить провода.

![[ee2coka.png]]

Проверьте 2-контактный разъем топливных форсуночных соленоидных проводов для правильного подключения.

Используйте небольшую отвертку, чтобы удалить защитную крышку из соленоида.

Используйте дюймовый гаечный ключ, номер детали 3823208 и гнездо отвертки, номер детали 3823209, чтобы проверить сборку гайки для правильного крутящего момента.

> [!tip] Момент затяжки
> 1.6 Н·м [14 фунт-дюйм]

![[ee2cokf.png]]

Проверьте пропускной разъем для плотного соединения. Проверьте наличие открытой цепи в соленоиде форсунки. Используйте небольшую отвертку, чтобы удалить защитную крышку из соленоида.

Удалите сборку гайки из форсунки соленоида.

![[ee2cokh.png]]

Измерьте сопротивление между столбами или соединением соленоида форсунки. Вычтите сопротивление мультиметра. Истинное сопротивление соленоидов форсунки **должно быть от 0,5 до 1,5 Ом. Если сопротивление **не правильно, замените форсунку. См. процедуру 006-026 в Руководстве по устранению неполадок и ремонту, Двигатели ISM и QSM11, Вестник [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]].

![[fi2cnka.png]]

Если сопротивление правильное, проверьте соленоидные провода на открытую схему.

Отсоедините 2-контактный разъем топливных форсуночных соленоидных проводов.

![[fi8coad.png]]

> [!warning] ОСТОРОЖНО
> Не используйте щупы или провода, отличные от соединительного разъема. Разъём будет повреждён. Лиды должны плотно помещаться в разъеме без расширения контактов разъема.

Подключите соединительный разъем с короткими свинцовыми расширениями к стороне форсунки 2-контактного разъема.

![[ee2cokb.png]]

Прикоснитесь к одному многометровому щупу до конца короткого отводного удлинения. Прикоснитесь к другому многометровому щупу к пленному ореховому сбору форсунки соленоидной проволоки. Измерьте сопротивление. Повторите процедуру для другого провода форсунки. Сопротивление для обеих этих проверок должно быть менее 10 Ом. Если сопротивление превышает 10 Ом, замените форсунку соленоидными проводами. См. процедуру[[82-019-057 — Injector Solenoid|019-057]]. Не надо чинить провода.

![[ee2cokc.png]]

Отсоедините 15-контактный разъем, чтобы отделить внутреннюю и внешнюю проводку привода.

![[ea200hf.png]]

См. прилагаемый график в начале этого раздела для штифтов схемы форсунки проблемного цилиндра.

Цилиндр No1 будет использоваться в этом примере. Проверьте провод подачи. Прикоснитесь одним многометровым щупом к контакту подачи (контакту А) на топливном форсунке 2-контактного разъёма, внутренней проводах привода упряжки.

![[19200340.png]]

Прикоснитесь к другому многометровому щупу к контакту подачи (контакт 01) на 15-контактном разъёме, внутренней стороне проводов привода. Измерьте сопротивление. Сопротивление **должно быть менее 10 Ом. Если измеряется более 10 Ом, замените внутреннюю проводку привода. См. процедуру 019-063. **Не ремонтируйте провода.

Подключите 15-контактный разъем, когда ремонт будет завершен.

![[19200340.png]]

Проверьте обратный провод на открытую цепь. Прикоснитесь одним многометровым щупом к обратному контакту (контакту В) у форсунки 2-контактного разъёма, внутренней проводов привода упряжки. Прикоснитесь к другому многометровому щупу на обратном контакте (контакт 02) 15-контактного разъема, внутренней проводов привода упряжки.

![[19200341.png]]

Измерьте сопротивление. Сопротивление должно быть менее 10 Ом. Если измеряется более 10 Ом, замените внутреннюю проводку привода. См. процедуру 019-063. Не надо чинить провода.

Подключите 15-контактный разъем, когда ремонт будет завершен.

![[19200341.png]]

Проверьте внешний привод проводов жгута для открытой цепи. Смотрите сопровождающую диаграмму в начале этого раздела для требуемых значков.

Цилиндр No1 будет использоваться в качестве примера. Вставьте штифт свинца в контакт с подачей (контакт 10 в этом примере) проводов привода. Подключите аллигатор к многометровому щупу.

![[19200342.png]]

Вставьте другой многометровый щуп на контакт подачи (контакт 01) на 15-контактном разъёме, внешней стороне проводов привода. Измерьте сопротивление. Сопротивление должно быть менее 10 Ом. Если измеряется более 10 Ом, отремонтируйте провод или замените электропроводку привода. См. процедуру[[82-019-043-tr — Engine Wiring Harness|019-043]].

Подключите 15-контактный разъем, когда ремонт будет завершен.

![[19200342.png]]

Вставьте штифт свинца в обратный контакт (контакт 09 в этом примере) разъёма проводов привода. Поместите другой многометровый щуп на обратный контакт (контакт 02) на 15-контактный разъем, внешнюю проводку с ремнями безопасности.

![[19200343.png]]

Измерьте сопротивление. Сопротивление должно быть менее 10 Ом. Если измеряется более 10 Ом, отремонтируйте обратный провод или замените электропроводку привода. См. процедуру[[82-019-043-tr — Engine Wiring Harness|019-043]].

Подключите 15-контактный разъем, когда ремонт будет завершен.

![[19200343.png]]

Значение сопротивления в пределах спецификации

Если значение сопротивления находится в пределах спецификации, схема **должна** все еще проверяться на короткое замыкание на землю и короткое замыкание от пин-кодов до пин-кодов.

![[19200344.png]]

### Проверка на замыкание на массу

> [!danger] ОПАСНО
> На электромагниты форсунок при работающем двигателе подаётся высокое напряжение. Чтобы уменьшить вероятность получения травмы или смерти от поражения электрическим током, не носите ювелирные изделия или сырую одежду, и не прикасайтесь к соленоидам форсунки или соленоидным проводам при работе двигателя.

Проверьте короткое замыкание для заземления во внешней проводах привода. Смотрите сопровождающую диаграмму для булавок, чтобы проверить. Цилиндр No1 будет использоваться в этом примере.

![[19200339.png]]

Штифты цепей следующие:

| Контакты с поставщиками | обратный контакт |  |  |  |  |  |
|---|---|---|---|---|---|---|
| Кайл. № | ECM Конн. | 15-пин Конн. | Индж. Пин | ECM Конн. | 15-пин Конн. | Индж. Пин |
| 1 | 10 | 01 | А. | 09 | 02 | B |
| 2 | 08 | 03 | А. | 07 | 04 | B |
| 3 | 06 | 05 | А. | 16 | 06 | B |
| 4 | 26 | 07 | А. | 36 | 08 | B |
| 5 | 04 | 09 | А. | 03 | 10 | B |
| 6 | 02 | 11 | А. | 01 | 12 | B |

![[19200333.png]]

Переключатель зажигания транспортного средства в положение выключения. Отсоедините разъем электропроводки привода от ECM.

Вставьте измерительный щуп в контакт 10 разъема электропроводки привода и соедините его с многометровым щупом. Прикоснитесь к другому многометровому щупу, чтобы блокировать двигатель. Измерьте сопротивление.

Схема **должна быть открыта (100к Ом или более). Если он **не открыт, изолируйте короткое к внешней или внутренней проводах привода.

![[19200344.png]]

Отсоедините 15-контактный проходной разъем от электропроводки привода.

Вставьте испытательный щуп в контакт 01 15-контактного разъёма, внутренней проводов с ремнями безопасности. Прикоснитесь к другому многометровому щупу, чтобы блокировать двигатель. Измерьте сопротивление.

Схема **должна быть открыта (100к Ом или более). Если он **не открыт, короткое замыкание находится на внутренней стороне проводов. Заменить внутреннюю проводку привода. См. процедуру 019-063. Если цепь открыта, отремонтируйте или замените внешний привод проводов жгута.

![[19200409.png]]

### Проверка на замыкание между контактами

> [!danger] ОПАСНО
> На электромагниты форсунок при работающем двигателе подаётся высокое напряжение. Чтобы уменьшить вероятность получения травмы или смерти от поражения электрическим током, не носите ювелирные изделия или сырую одежду, и не прикасайтесь к соленоидам форсунки или соленоидным проводам при работе двигателя.

Проверьте короткое замыкание от пин-кодов до пин-кодов. Смотрите сопроводительную диаграмму для требуемых значков. Цилиндр No1 будет использоваться в качестве примера.

![[19200339.png]]

Штифты цепей следующие:

| Контакты с поставщиками | обратный контакт |  |  |  |  |  |
|---|---|---|---|---|---|---|
| Кайл. № | ECM Конн. | 15-пин Конн. | Индж. Пин | ECM Конн. | 15-пин Конн. | Индж. Пин |
| 1 | 10 | 01 | А. | 09 | 02 | B |
| 2 | 08 | 03 | А. | 07 | 04 | B |
| 3 | 06 | 05 | А. | 16 | 06 | B |
| 4 | 26 | 07 | А. | 36 | 08 | B |
| 5 | 04 | 09 | А. | 03 | 10 | B |
| 6 | 02 | 11 | А. | 01 | 12 | B |

![[19200333.png]]

Переключатель зажигания транспортного средства в положение выключения. Отсоедините исполнительный механизм и разъёмы проводов датчика от ECM. Отсоедините проводку привода от 15-контактного пропускного разъема.

Включить испытательный щуп в контакт 10 разъёма проводов привода. Вставьте другой испытательный щуп во все другие штифты разъёма проводов привода, по одному за раз. Измерьте сопротивление.

Повторите ту же проверку, что и в предыдущем контакте 9. Схема должна быть открыта (100к Ом или более) на всех штифтах. Если цепь не открыта, отремонтируйте или замените электропроводку привода. См. процедуру[[82-019-043-tr — Engine Wiring Harness|019-043]].

![[19200410.png]]

Включить испытательный щуп в контакт 10 разъёма проводов привода. Вставьте другой измерительный щуп во все другие штифты разъёма проводов датчика, по одному за раз. Измерьте сопротивление.

Повторите ту же проверку, что и в предыдущем контакте 9. Схема **должна быть открыта (100к Ом или более) на всех штифтах. Если схема **не открыта, отремонтируйте или замените привод или датчик проводов ремня. См. процедуру[[82-019-043-tr — Engine Wiring Harness|019-043]].

![[19200411.png]]

Проверьте короткое замыкание от пин-кодов до пин-кодов в 15-контактном проходном разъеме. Отсоедините внутреннюю проводку от форсунки соленоида.

Вставьте пробный щуп в контакт 01 15-контактного пропускного разъема, внутренней проводов с ремнями безопасности. Вставьте другой измерительный щуп во все другие штифты проходящего разъема, по одному за раз. Измерьте сопротивление.

Схема **должна быть открыта (100к Ом или более). Если он **не открыт, замените внутреннюю проводку привода. См. процедуру 019-063.

![[19200412.png]]

Вставьте пробный щуп в контакт 02 15-контактного пропускного разъема, внутренней проводов с ремнями безопасности. Вставьте другой измерительный щуп во все другие штифты проходящего разъема, по одному за раз. Измерьте сопротивление.

Схема **должна быть открыта (100к Ом или более). Если он **не открыт, замените внутреннюю проводку привода. См. процедуру 019-063.

После ремонта подсоедините все компоненты.

![[19200413.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> **WARNING · Опасно**
> The injector solenoids receive high voltage when the engine is operating. To reduce the possibility of personal injury or death from electrical shock, do not wear jewelry or damp clothing, and do not touch the injector solenoids or the solenoid wires when the engine is operating.
>
> **CAUTION · Осторожно**
> Do not use probes or leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the connector pins.
>
> Inspect the injector solenoid circuit of the cylinder referenced on the recorded fault code. Refer to the accompanying chart for the pins of the injector circuit of the problem cylinder. Cylinder Number 1 will be used in this example.
>
> The pins of the circuits are as follows:
>
> | Supply Pin | Return Pin |  |  |  |  |  |
> |---|---|---|---|---|---|---|
> | Cyl. No. | ECM Conn. | 15-Pin Conn. | Inj. Pin | ECM Conn. | 15-Pin Conn. | Inj. Pin |
> | 1 | 10 | 01 | A | 09 | 02 | B |
> | 2 | 08 | 03 | A | 07 | 04 | B |
> | 3 | 06 | 05 | A | 16 | 06 | B |
> | 4 | 26 | 07 | A | 36 | 08 | B |
> | 5 | 04 | 09 | A | 03 | 10 | B |
> | 6 | 02 | 11 | A | 01 | 12 | B |
>
> Turn the vehicle keyswitch to the OFF position.
>
> Disconnect the actuator harness connector from the ECM.
>
> Insert a test lead into the supply pin (pin 10 in this example) of the actuator harness connector. Insert the other lead into the return pin (pin 09 in this example) of the actuator harness connector. Connect the alligator clips to the multimeter probes.
>
> Measure the resistance. Subtract the multimeter test lead resistance value from this value to determine the true injector circuit resistance value. The resistance **must** be 0.5 to 1.5 ohms. If the resistance value is **not** correct, proceed with the following sections. If the resistance is correct, the circuit **must** still be checked for a short circuit to ground and a short circuit from pin to pin.
>
> **Note · Примечание**
> If the resistance measurement is less than 10 ohms, the circuit is acceptable as long as the resistance of the injector solenoid is within 0.5 to 1.5 ohms (see Resistance Value Above Specification).
>
> Resistance Value Below Specifications
>
> Remove the valve cover.
>
> Inspect the injector solenoid wires for short circuits between the wires. If the wires are damaged, replace the wires. Refer to Procedure [[82-019-057 — Injector Solenoid|019-057]].
>
> Disconnect the injector supply and return wires from the solenoid of the problem cylinder.
>
> Use a small screwdriver to remove the protective cover from the solenoid.
>
> Remove the captive nut assembly from the injector solenoid.
>
> Measure the resistance between the two posts or the connection of the injector solenoid. Subtract the multimeter resistance. The true injector solenoid resistance **must** be 0.5 to 1.5 ohms. If the resistance value is **not** correct, replace the injector. Refer to Procedure 006-026 in the Troubleshooting and Repair Manual, ISM and QSM11 Engines, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]].
>
> If the resistance value of the injector solenoid is correct, the problem is in the internal or external actuator harness. Isolate the problem by checking each harness separately.
>
> Disconnect the connector inside the head.
>
> Check the internal actuator harness. Measure the resistance between the two captive nut assemblies, or the connection, of the injector solenoid wire that was removed from the injector solenoid. The resistance **must** be an open circuit (more than 100k ohms). If the resistance is less than 100k ohms, replace the internal actuator wiring harness. Refer to Procedure 019-063. Do **not** repair the internal actuator harness.
>
> Connect the 15-pin connector when the repair is completed.
>
> Check the external actuator harness. Make sure that the 15-pin connector is still disconnected. Insert the test lead into the supply pin (pin 10 in this example) of the actuator harness connector. Insert the pin of the other lead into the return pin (pin 09 in this example) of the actuator harness connector. Connect the alligator clips to the multimeter probes.
>
> Measure the resistance. The resistance **must** be an open circuit (more than 100k ohms). If the resistance is less than 100k ohms, repair or replace the external actuator harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].
>
> Connect the 15-pin connector when the repair is completed.
>
> Resistance Value Above Specification
>
> Remove the valve cover.
>
> Inspect the injector solenoid wires for broken wires. If the wires are damaged, replace the wires. Refer to Procedure [[82-019-057 — Injector Solenoid|019-057]]. Do **not** repair the wires.
>
> Check the 2-pin connector of the injector solenoid wires for proper connection.
>
> Use a small screwdriver to remove the protective cover from the solenoid.
>
> Use inch pound torque wrench, Part Number 3823208, and screwdriver socket, Part Number 3823209, to check the captive nut assembly for correct torque.
>
> **Момент затяжки · Torque Value**
> 1.6 n•m [14 in-lb]
>
> Check pass-through connector for a tight connection. Check for an open circuit in the injector solenoid. Use a small screwdriver to remove the protective cover from the solenoid.
>
> Remove the captive nut assembly from the injector solenoid.
>
> Measure the resistance between the posts or the connection of the injector solenoid. Subtract the multimeter resistance. The true injector solenoid resistance **must** be 0.5 to 1.5 ohms. If the resistance is **not** correct, replace the injector. Refer to Procedure 006-026 in the Troubleshooting and Repair Manual, ISM and QSM11 Engines, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]].
>
> If the resistance is correct, check the solenoid wires for an open circuit.
>
> Disconnect the 2-pin connector of the injector solenoid wires.
>
> **CAUTION · Осторожно**
> Do not use probes or leads other than the mating connector. The connector will be damaged. The leads must fit tightly in the connector without expanding the connector pins.
>
> Connect a mating connector with short lead extensions to the injector side of the 2-pin connector.
>
> Touch one multimeter probe to the end of the short lead extension. Touch the other multimeter probe to the captive nut assembly of the injector solenoid wire. Measure the resistance. Repeat the procedure for the other injector wire. The resistance for both of these checks **must** be less than 10 ohms. If the resistance is more than 10 ohms, replace the injector solenoid wires. Refer to Procedure [[82-019-057 — Injector Solenoid|019-057]]. Do **not** repair the wires.
>
> Disconnect the 15-pin connector to separate the internal and external actuator harness.
>
> Refer to the accompanying chart at the beginning of this section for the pins of the injector circuit of the problem cylinder.
>
> Cylinder Number 1 will be used in this example. Check the supply wire. Touch one multimeter probe to the supply pin (pin A) at the injector 2-pin connector, internal actuator harness side.
>
> Touch the other multimeter probe to the supply pin (pin 01) at the 15-pin connector, internal actuator harness side. Measure the resistance. The resistance **must** be less than 10 ohms. If more than 10 ohms are measured, replace the internal actuator harness. Refer to Procedure 019-063. Do **not** repair the wire.
>
> Connect the 15-pin connector when the repair is completed.
>
> Check the return wire for an open circuit. Touch one multimeter probe to the return pin (pin B) at the injector 2-pin connector, internal actuator harness side. Touch the other multimeter probe on the return pin (pin 02) of the 15-pin connector, internal actuator harness side.
>
> Measure the resistance. The resistance **must** be less than 10 ohms. If more than 10 ohms are measured, replace the internal actuator harness. Refer to Procedure 019-063. Do **not** repair the wires.
>
> Connect the 15-pin connector when the repair is completed.
>
> Check the external actuator harness for an open circuit. Refer to the accompanying chart at the beginning of this section for the pins required.
>
> Cylinder Number 1 will be used as an example. Insert the pin of the lead into the supply pin (pin 10 in this example) of the actuator harness. Connect the alligator clip to the multimeter probe.
>
> Insert the other multimeter probe on the supply pin (pin 01) at the 15-pin connector, external actuator harness side. Measure the resistance. The resistance **must** be less than 10 ohms. If more than 10 ohms are measured, repair the wire or replace the actuator harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].
>
> Connect the 15-pin connector when the repair is completed.
>
> Insert the pin of the lead in the return pin (pin 09 in this example) of the actuator harness connector. Place the other multimeter probe on the return pin (pin 02) at the 15-pin connector, external harness side.
>
> Measure the resistance. The resistance **must** be less than 10 ohms. If more than 10 ohms are measured, repair the return wire or replace the actuator harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].
>
> Connect the 15-pin connector when the repair is completed.
>
> Resistance Value Within Specification
>
> If the resistance value is within specification, the circuit **must** still be checked for a short circuit to ground and a short circuit from pin to pin.
>
> ### Check for Short Circuit to Ground
>
> **WARNING · Опасно**
> The injector solenoids receive high voltage when the engine is operating. To reduce the possibility of personal injury or death from electrical shock, do not wear jewelry or damp clothing, and do not touch the injector solenoids or the solenoid wires when the engine is operating.
>
> Check for a short circuit to ground in the external actuator harness. Refer to the accompanying chart for the pins to check. Cylinder Number 1 will be used for this example.
>
> The pins of the circuits are as follows:
>
> | Supply Pin | Return Pin |  |  |  |  |  |
> |---|---|---|---|---|---|---|
> | Cyl. No. | ECM Conn. | 15-Pin Conn. | Inj. Pin | ECM Conn. | 15-Pin Conn. | Inj. Pin |
> | 1 | 10 | 01 | A | 09 | 02 | B |
> | 2 | 08 | 03 | A | 07 | 04 | B |
> | 3 | 06 | 05 | A | 16 | 06 | B |
> | 4 | 26 | 07 | A | 36 | 08 | B |
> | 5 | 04 | 09 | A | 03 | 10 | B |
> | 6 | 02 | 11 | A | 01 | 12 | B |
>
> Turn the vehicle keyswitch to the OFF position. Disconnect the actuator harness connector from the ECM.
>
> Insert a test lead into pin 10 of the actuator harness connector, and connect it to a multimeter probe. Touch the other multimeter probe to engine block ground. Measure the resistance.
>
> The circuit **must** be open (100k ohms or more). If it is **not** open, isolate the short to the external or internal actuator harness.
>
> Disconnect the 15-pin pass-through connector from the actuator harness.
>
> Insert the test lead into pin 01 of the 15-pin connector, internal harness side. Touch the other multimeter probe to engine block ground. Measure the resistance.
>
> The circuit **must** be open (100k ohms or more). If it is **not** open, the short circuit is on the internal harness side. Replace the internal actuator harness. Refer to Procedure 019-063. If the circuit is open, repair or replace the external actuator harness.
>
> ### Check for Short Circuit from Pin to Pin
>
> **WARNING · Опасно**
> The injector solenoids receive high voltage when the engine is operating. To reduce the possibility of personal injury or death from electrical shock, do not wear jewelry or damp clothing, and do not touch the injector solenoids or the solenoid wires when the engine is operating.
>
> Check for a short circuit from pin to pin. Refer to the accompanying chart for the pins required. Cylinder Number 1 will be used as an example.
>
> The pins of the circuits are as follows:
>
> | Supply Pin | Return Pin |  |  |  |  |  |
> |---|---|---|---|---|---|---|
> | Cyl. No. | ECM Conn. | 15-Pin Conn. | Inj. Pin | ECM Conn. | 15-Pin Conn. | Inj. Pin |
> | 1 | 10 | 01 | A | 09 | 02 | B |
> | 2 | 08 | 03 | A | 07 | 04 | B |
> | 3 | 06 | 05 | A | 16 | 06 | B |
> | 4 | 26 | 07 | A | 36 | 08 | B |
> | 5 | 04 | 09 | A | 03 | 10 | B |
> | 6 | 02 | 11 | A | 01 | 12 | B |
>
> Turn the vehicle keyswitch to the OFF position. Disconnect the actuator and sensor harness connectors from the ECM. Disconnect the actuator harness from the 15-pin pass-through connector.
>
> Insert a test lead into pin 10 of the actuator harness connector. Insert the other test lead into all other pins of the actuator harness connector, one at a time. Measure the resistance.
>
> Repeat same check as previous from pin 9. The circuit **must** be open (100k ohms or more) at all pins. If the circuit is not open, repair or replace the actuator harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].
>
> Insert a test lead into pin 10 of the actuator harness connector. Insert the other test lead into all other pins of the sensor harness connector, one at a time. Measure the resistance.
>
> Repeat same check as previous from pin 9. The circuit **must** be open (100k ohms or more) at all pins. If the circuit is **not** open, repair or replace the actuator or sensor harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].
>
> Check for a short circuit from pin to pin in the 15-pin pass-through connector. Disconnect the internal harness from the injector solenoid.
>
> Insert a test lead into pin 01 of the 15-pin pass-through connector, internal harness side. Insert the other test lead into all other pins of the pass-through connector, one at a time. Measure the resistance.
>
> The circuit **must** be open (100k ohms or more). If it is **not** open, replace the internal actuator harness. Refer to Procedure 019-063.
>
> Insert a test lead into pin 02 of the 15-pin pass-through connector, internal harness side. Insert the other test lead into all other pins of the pass-through connector, one at a time. Measure the resistance.
>
> The circuit **must** be open (100k ohms or more). If it is **not** open, replace the internal actuator harness. Refer to Procedure 019-063.
>
> Connect all components after completing the repair.
