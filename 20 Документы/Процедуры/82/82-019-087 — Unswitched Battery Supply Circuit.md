---
aliases:
  - "Цепь постоянного питания от АКБ"
type: "Процедура"
doc: "82-019-087"
title_en: "Unswitched Battery Supply Circuit"
title_ru: "Цепь постоянного питания от АКБ"
modified: "2002-06-27"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 8
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-087.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-087.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Unswitched Battery Supply Circuit
**Цепь постоянного питания от АКБ**

> [!abstract] Процедура · `82-019-087`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2002-06-27
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-087.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-087.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

ECM получает постоянное напряжение от батарей через непереключенные провода батареи, которые подключены непосредственно к (+) положительному заряду батареи. В каждом из непереключенных проводов батареи есть два встроенных 15-амперных предохранителя для защиты ECM. ECM принимает вводимую аккумуляторную батарею через провод переключателя зажигания транспортного средства, когда переключатель зажигания транспортного средства включен. Провода возврата аккумулятора соединены непосредственно с (-) отрицательным столбом батареи.

![[ee8cos31.png]]

Непереключенные провода батареи и провода возврата батареи находятся в ремне проводов OEM.

** Всегда** проверяйте непереключенные предохранители питания аккумулятора при устранении неполадок в цепях ECM и питания.

Проверьте напряжение батареи. См. процедуру 019-008.

![[ee8cos31.png]]

### Проверка сопротивления

Отсоедините проводку OEM от ECM.

![[19c00295.png]]

Настройте мультиметр для измерения сопротивления.

Вставьте один испытательный щуп в контакт 29 разъёма проводов OEM-проводов и соедините его с многометровым щупом. Прикоснитесь к другому многометровому щупу, чтобы заземлить блок двигателя и измерить сопротивление. Мультиметр ** должен** показывать замкнутую цепь размером 10 Ом или менее.

Измерительные контакты 29, 30, 39, 40 и 50 одинаковым образом.

![[19c00182.png]]

Если значение сопротивления ** не** правильно, проверьте батареи, кабели и кабельные соединения.

Ремонт или замена деталей по мере необходимости.

![[ee8cos38.png]]

Когда проверки будут завершены, подключите разъём OEM-проводов к ECM.

![[19c00295.png]]

Проверьте провода возврата батареи в OEM-проводнике для правильного заземления. Отсоедините проводную упряжку от ECM. Проверьте наличие поврежденных контактов в ECM и проводах.

![[19c00178.png]]

### Проверка напряжения

Проверьте подачу напряжения батареи на 50-контактном разъёме OEM-проводов.

Переведите замок зажигания в положение OFF. Отсоедините 50-контактный разъём OEM-проводов от ECM. Установите мультиметр для измерения VDC.

Измерьте напряжение от контакта 7 разъёма проводов OEM-проводов с землей. Повторите проверку напряжения от контакта 8, 17, 18 и 28.

Напряжение ** должно** считывать напряжение батареи при контакте 7, 8, 17, 18 и 28.

> [!missing]- Иллюстрация `19c00718.png` не извлечена — смотрите PDF-оригинал документа


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The ECM receives constant voltage from the batteries through the unswitched battery wires that are connected directly to the (+) positive battery post. There are two in-line 15-amp fuses in each of the unswitched battery wires to protect the ECM. The ECM receives switched battery input through the vehicle keyswitch wire when the vehicle keyswitch is turned on. The battery return wires are connected directly to the (-) negative battery post.
>
> The unswitched battery wires and the battery return wires are in the OEM harness.
>
> **Always** check the unswitched battery supply fuses when troubleshooting the ECM and power supply circuits.
>
> Check the battery voltage. Refer to Procedure 019-008.
>
> ### Resistance Check
>
> Disconnect the OEM harness from the ECM.
>
> Adjust the multimeter to measure resistance.
>
> Insert one test lead into pin 29 of the OEM harness connector and connect it to the multimeter probe. Touch the other multimeter probe to the engine block ground and measure the resistance. The multimeter **must** show a closed circuit of 10 ohms or less.
>
> Test pins 29, 30, 39, 40, and 50 in the same manner.
>
> If the resistance value is **not** correct, check the batteries, cables, and cable connections.
>
> Repair or replace the parts as required.
>
> When the checks have been completed, connect the OEM harness connector to the ECM.
>
> Check the battery return wires in the OEM harness for proper grounding. Disconnect the harness from the ECM. Check for damaged pins in the ECM and the harness.
>
> ### Voltage Check
>
> Check the battery voltage supply at the 50-pin OEM harness connector.
>
> Turn the keyswitch to the OFF position. Disconnect the 50-pin OEM harness connector from the ECM. Set the multimeter to measure VDC.
>
> Measure the voltage from pin 7 of the OEM harness connector to ground. Repeat the voltage check from pin 8, 17, 18, and 28.
>
> The voltage **must** read battery voltage at pin 7, 8, 17, 18, and 28.
