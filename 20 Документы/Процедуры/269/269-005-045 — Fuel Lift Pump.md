---
aliases:
  - "Топливоподкачивающий насос"
type: "Процедура"
doc: "269-005-045"
title_en: "Fuel Lift Pump"
title_ru: "Топливоподкачивающий насос"
modified: "2023-02-22"
engines:
  - "93948840"
families:
  - "QSZ13"
manuals:
  - "4358369"
figures: 9
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/269/269-005-045.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/269-005-045.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSZ13"
  - "группа/269"
  - "перевод/машинный"
---

# Fuel Lift Pump
**Топливоподкачивающий насос**

> [!abstract] Процедура · `269-005-045`
> **Двигатели:** [[93948840 — QSZ13 CM2150 Z102 CPL 4858|93948840]]
> **Семейство:** QSZ13
> **Входит в руководства:** [[4358369 — QSZ13 CM2150 Z102 Service Manual|4358369]]
> **Секции:** Section 5 - Fuel System - Group 05
> **Даты:** изменён 2023-02-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/269/269-005-045.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/269-005-045.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Выбор сервисного инструмента

#### Рекомендованный сервисный инструмент Cummins®

- Инструмент для удаления, номер детали 4918878
- Диагностическая топливная линия, номер детали 4918895
- Трубопровод для диагностики ориффицированного топлива, номер детали 3164621

#### Дополнительные сервисные позиции

- отвертка
- Контейнер, пригодный для топлива.

### Первичная проверка

Неисправный насос для подъёма электрического топлива может вызвать медленные запуски двигателя или привести к неисправности двигателя. Насос для подъёма топлива может быть очищен и отремонтирован в ограниченной степени.

Насос для подъёма топлива будет работать от 30 до 60 секунд при включении ключа. Насос для подъёма топлива также будет работать, пока двигатель работает.

![[05900327.png]]

Насос для подъёма топлива установлен на задней панели охлаждающей пластины модуля управления двигателем (ECM).

Проверочный клапан в охлаждающей пластине ECM гарантирует, что система запускается насосом топливного подъемника. Этот контрольный клапан открывается под вакуумом, создаваемым передаточным насосом после запуска двигателя. Высокий вакуум, измеренный между насосом для подъёма электрического топлива и насосом для передачи, может указывать на то, что этот контрольный клапан заглушен.

Клапан проверки охлаждающей пластины ECM является интегралом с нижней (выходной) установкой охлаждающей пластины ECM.

![[05d00792.png]]

#### Испытание насосного потока на подъёмнике топлива

- Удалите зажим из топливной стойки. Это позволит топливным линиям двигаться, чтобы испытательное оборудование могло быть установлено должным образом.

![[06d00248.png]]

- Отсоедините линию подачи топлива в стиле быстрого отключения от входного отверстия переключателя, нажав в запирающих тангах по обе стороны быстроразъемной фитинги.
- Чтобы помочь в удалении быстроразъединенных топливных линий, инструмент для удаления слайдов, номер детали 4918878, над запирающимися тангами. Проверьте, чтобы инструмент был удален из топливной линии как можно скорее после отключения линии.
- Непреднамеренное оставление инструмента на месте может привести к утечке топлива.

![[06d00489.png]]

- Для облегчения удаления между концом топливной линии и быстро отсоединяемой внешней резьбой может быть вставлена отвертка. После нажатия противостоящих запирающих тангов, скручивание плоского лезвия отвертки помогает снять топливную линию.

![[06d00249.png]]

- Установите диагностическую топливную линию, номер детали 4918895, между передаточным насосом, подающим топливо, и входным отверстием передаточного насоса.
- Подключите перфорированную диагностическую топливную линию, Номер детали 3164621, к установке CompuchekTM на диагностической топливной линии, Номер детали 4918895, и запустите шланг в устройство сбора.

![[05d01044.png]]

> [!note] Примечание
> При первоначальном включении клавиши насос топливного подъемника будет работать в течение 30 секунд, а затем остановится.

Включите переключатель зажигания в положение Включения и позвольте топливу течь в устройство сбора в течение 10 секунд (или до тех пор, пока поток топлива не будет непрерывным).

> [!note] Примечание
> Для непрерывного потока топлива в течение первого цикла включения ключа может потребоваться более 10 секунд из-за воздуха в диагностических топливных линиях.

После того, как поток топлива будет непрерывным, переведите орифицированную диагностическую топливную линию в четкий градуированный цилиндр и позвольте топливу течь в градуированный цилиндр в течение 10 секунд.

Удалите перфорированную диагностическую топливную линию из градуированного цилиндра через 10 секунд и переключите зажигание в положение выключения.

Зафиксировать объем топлива, собранного за 10 секунд.

Повторите этот тест три раза и возьмите среднюю скорость потока.

| Измерения |  |  |
|---|---|---|
|  | млечный | фл-оз |
| Минимальный объем топлива в течение 10 секунд испытания на расход насоса топливного лифта | 100 | 3.4 |

> [!note] Примечание
> Если поток насоса топливного лифта низкий, пока работает насос топливного лифта, убедитесь, что клапан проверки охлаждающей пластины ECM **не **заблокирован. Также проверьте, что ограничение входного впуска оригинального оборудования производителя (OEM) находится в пределах спецификации.

> [!note] Примечание
> Если поток насоса топливного лифта низкий, пока работает насос топливного лифта, проверьте, заряжено ли топливо. Например, после замены топливного фильтра, заправьте насос топливного лифта три или четыре раза, прежде чем воздух будет очищен.

![[05d01045.png]]

### Подготовительные операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

> [!danger] ОПАСНО
> При работе с пароочистителем надевайте защитные очки или щиток и защитную одежду. Горячий пар может привести к тяжёлой травме.

> [!danger] ОПАСНО
> Топливный насос, топливные линии высокого давления и топливный рельс содержат топливо очень высокого давления. Не растягивайте ни одну фитингу, пока двигатель работает. Подождите не менее 10 минут после выключения двигателя, прежде чем ослаблять любую фитинги в топливной системе высокого давления, чтобы снизить давление до более низкого уровня.

Перед обслуживанием любых компонентов топливной системы (таких как топливные линии, топливный насос, топливный форсунок и т. Д.), Которые могут подвергать топливную систему или внутренний компонент двигателя потенциальным загрязнителям перед разборкой, очистите фитинги, монтажное оборудование и область вокруг компонента, который должен быть удален. Грязь или загрязняющие вещества могут быть введены в топливную систему и двигатель, если окружающие области не очищены, что приводит к повреждению топливной системы и двигателя.

- Отсоедините аккумуляторные батареи. См. сервисную документацию изготовителя оборудования.
- очищать паром компоненты топливной системы (такие как топливные линии, топливный насос, форсунка и т. Д.).[[99-000-009 — Engine Cleaning|См. процедуру 000-009 в разделе 0.]]
- Отсоедините электротопливный насос от электропроводки двигателя.
- Удалите линии подачи топлива. См. процедуру 006-024 в разделе 6.
- Удалите охлаждающую пластину ECM. См. процедуру 006-006 в разделе 6.

### Снятие

Удалите насос для подъёма электрического топлива из охлаждающей пластины ECM.

![[05d00797.png]]

### Установка

Установите насос для подъёма электрического топлива на охлаждающую пластину ECM.

Затягивайте крепежные болты.

> [!tip] Момент затяжки
> 10 Н·м [89 фунт-дюйм]

Клапан проверки охлаждающей пластины ECM должен быть свободен от мусора и установлен в нижний порт охлаждающей пластины ECM (выходной порт).

Держите топливные линии, как показано, чтобы они не вступали в контакт друг с другом или блоком цилиндров.

![[05d00797.png]]

### Завершающие операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Установите охлаждающую пластину ECM на блок цилиндров. См. процедуру 006-006 в разделе 6.
- Установите все линии подачи топлива. См. процедуру 006-024 в разделе 6.
- Подсоедините аккумуляторные батареи. См. сервисную документацию изготовителя оборудования.
- Запустите двигатель и проверьте на отсутствие утечек.


> [!quote]- Original (English) · английский оригинал
> ### Select Service Tools
>
> #### Recommended Cummins® Service Tools
>
> - Removal tool, Part Number 4918878
> - Diagnostic fuel line, Part Number 4918895
> - Orificed diagnostic fuel line, Part Number 3164621
>
> #### Additional Service Items
>
> - Screwdriver
> - Container suitable for fuel.
>
> ### Initial Check
>
> A malfunctioning electric fuel lift pump can cause slow engine starts or can result in an engine failing to start. The fuel lift pump can be cleaned and repaired to a limited extent.
>
> The fuel lift pump will operate for 30 to 60 seconds when the key is switched ON. The fuel lift pump will also operate while the engine is cranking.
>
> A fuel lift pump is mounted to the back of the Engine Control Module (ECM) cooling plate.
>
> A bypass check valve in the ECM cooling plate makes sure the system is primed by the fuel lift pump. This check valve opens under vacuum created by the gear pump once the engine is started. High vacuum measured between the electric fuel lift pump and the gear pump can indicate this check valve has become plugged.
>
> The ECM cooling plate check valve is integral with the lower (outlet) fitting of the ECM cooling plate.
>
> #### Fuel Lift Pump Flow Test Setup
>
> - Remove the clasp from the fuel line brace. This will allow the fuel lines to move so that test equipment can be installed properly.
>
> - Disconnect the quick-disconnect style fuel line from the gear pump inlet by pressing in the locking tangs on both sides of the quick-disconnect fitting.
> - To aid in the removal of quick-disconnect style fuel lines, slide removal tool, Part Number 4918878, over the locking tangs. Verify the tool is removed from the fuel line as soon as possible after the line has been disconnected.
> - Inadvertently leaving the tool in place can result in fuel leaks.
>
> - To aid in removal, a screwdriver may be inserted between the fuel line end and quick-disconnect male union. After pressing the opposing locking tangs, twisting the flat blade of the screwdriver helps to remove the fuel line.
>
> - Install diagnostic fuel line, Part Number 4918895, between the gear pump fuel supply line and the gear pump inlet.
> - Connect orificed diagnostic fuel line, Part Number 3164621, to the Compuchek™ fitting on the diagnostic fuel line, Part Number 4918895, and run hose into a collection device.
>
> **Note · Примечание**
> At initial key-ON, the fuel lift pump will run for 30 seconds and then stop.
>
> Turn keyswitch to the ON position and allow fuel to flow into a collection device for 10 seconds (or until fuel stream is continuous).
>
> **Note · Примечание**
> It may take longer than 10 seconds for fuel stream to flow continuously during the first key-ON cycle because of air in the diagnostic fuel lines.
>
> Once fuel flow is continuous, transfer the orificed diagnostic fuel line to a clear graduated cylinder and allow fuel to flow into the graduated cylinder for 10 seconds.
>
> Remove the orificed diagnostic fuel line from graduated cylinder after 10 seconds and turn keyswitch to the OFF position.
>
> Record the volume of fuel collected over 10 seconds.
>
> Repeat this test three times and take an average of the flow rates.
>
> | Measurements |  |  |
> |---|---|---|
> |  | ml | fl-oz |
> | Minimum volume of fuel during 10 second fuel lift pump flow test | 100 | 3.4 |
>
> **Note · Примечание**
> If the fuel lift pump flow is low while the fuel lift pump runs, verify the ECM cooling plate check valve is **not** blocked open. Also, verify the original equipment manufacturer (OEM) connection inlet restriction is within specification.
>
> **Note · Примечание**
> If the fuel lift pump flow is low while the fuel lift pump runs, verify fuel is primed. For example, following fuel filter replacement, cycle the fuel lift pump three or four times before the air is purged.
>
> ### Preparatory Steps
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> **WARNING · Опасно**
> When using a steam cleaner, wear safety glasses or a face shield, as well as protective clothing. Hot steam can cause serious personal injury.
>
> **WARNING · Опасно**
> The fuel pump, high-pressure fuel lines, and fuel rail contain very high-pressure fuel. Do not loosen any fittings while the engine is running. Wait at least 10 minutes after shutting down the engine before loosening any fittings in the high-pressure fuel system to allow pressure to decrease to a lower level.
>
> Before servicing any fuel system components (such as fuel lines, fuel pump, injectors, and so forth), which can expose the fuel system or internal engine component to potential contaminants prior to disassembly, clean the fittings, mounting hardware, and the area around the component to be removed. Dirt or contaminants can be introduced into the fuel system and engine if the surrounding areas are **not** cleaned, resulting in damage to the fuel system and engine.
>
> - Disconnect the batteries. See equipment manufacturer service information.
> - Steam clean the fuel system components (such as fuel lines, fuel pump, injectors, and so forth). [[99-000-009 — Engine Cleaning|Refer to Procedure 000-009 in Section 0.]]
> - Disconnect the electric fuel priming pump from the engine wiring harness.
> - Remove the fuel supply lines. Refer to Procedure 006-024 in Section 6.
> - Remove the ECM cooling plate. Refer to Procedure 006-006 in Section 6.
>
> ### Remove
>
> Remove the electric fuel lift pump from the ECM cooling plate.
>
> ### Install
>
> Install the electric fuel lift pump to the ECM cooling plate.
>
> Tighten the mounting capscrews.
>
> **Момент затяжки · Torque Value**
> 10 n•m [89 in-lb]
>
> The ECM cooling plate check valve **must** be free of debris and installed into the lower ECM cooling plate port (outlet port).
>
> Hold the fuel lines, as illustrated, so they do **not** come into contact with each other or the cylinder block.
>
> ### Finishing Steps
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Install the ECM cooling plate to the cylinder block. Refer to Procedure 006-006 in Section 6.
> - Install all fuel supply lines. Refer to Procedure 006-024 in Section 6.
> - Connect the batteries. See equipment manufacturer service information.
> - Operate the engine and check for leaks.
