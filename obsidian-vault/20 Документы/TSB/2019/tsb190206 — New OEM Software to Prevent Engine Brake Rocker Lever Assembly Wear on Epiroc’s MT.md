---
type: "TSB"
doc: "tsb190206"
title_en: "New OEM Software to Prevent Engine Brake Rocker Lever Assembly Wear on Epiroc’s MT-42 Unit"
modified: "2019-12-09"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
figures: 4
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2019/tsb190206.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb190206.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QSX15"
  - "перевод/машинный"
---

# New OEM Software to Prevent Engine Brake Rocker Lever Assembly Wear on Epiroc’s MT-42 Unit

> [!abstract] TSB · `tsb190206`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Даты:** изменён 2019-12-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2019/tsb190206.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb190206.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Новое OEM-программное обеспечение для предотвращения торможения двигателя клапана клапана качели сборка носить на Epiroc MT-42 единицы

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

Только информация - OEM-связанный вопрос, не охватываемый Cummins® - Контактный соответствующий OEM-дилер или представитель OEM для дополнительной информации

### Содержание

**Затронутая продукция**

Двигатель:

- QSX15 CM570

Производитель оригинального оборудования (OEM):

- эпиротик

Шасси:

- Горнодобывающий грузовик МТ-42

**Проблема**

Симптом:

- Установки могут испытывать шум или вибрацию, исходящую от двигателя.
- Части тормозов двигателя, включая углубление вала, пружины управляющего клапана и крышки управляющего клапана, будут выглядеть изношенными и высвободятся из их сборки.

Первопричина:

- TSC1 Torque Control сообщение от OEM-программы, поступающее на шину данных J1939 CAN, настроено неправильно. Неправильная конфигурация заставляет сообщения управления крутящим моментом приводить к чрезмерному срабатыванию тормозов двигателя в несколько раз большему, чем номинальные срабатывания, наблюдаемые в этих приложениях.

**Подтверждение**

- Проверьте заднюю часть переключателя тормоза двигателя на приборной панели для любой ненормальной проводов. Все провода должны быть направлены в соответствующие порты. См. сервисную документацию изготовителя оборудования.
- Выполните полный осмотр накладных тормозных частей двигателя. Разберите клапанную качалку рычага/вала и проверьте следующее:

![[20f00001.png]]

![[20f00002.png]]

![[20f00003.png]]

![[20f00004.png]]

Рисунок 1 Дыра-детанта тормозного вала двигателя.

Рисунок 2, Двигатель управления тормозом клапан Spring.

Рисунок 3, привод двигателя тормоза Пистон.

Рисунок 4, контактный мостик с торможением двигателя.

**Решение**

- Свяжитесь с OEM для получения дальнейших инструкций о том, как устранить этот тип сбоя.

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## New OEM Software to Prevent Engine Brake Rocker Lever Assembly Wear on Epiroc's MT-42 Unit
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> Information Only - OEM Related Matter Not Covered By Cummins® - Contact Appropriate OEM Dealer or OEM Representative For Additional Information
>
> ### Contents
>
> **Product Affected**
>
> Engine:
>
> - QSX15 CM570
>
> Original Equipment Manufacturer (OEM):
>
> - Epiroc
>
> Chassis:
>
> - MT-42 Mining Truck
>
> **Issue**
>
> Symptom:
>
> - Units may experience noise or vibration coming from the engine.
> - Engine brake parts, including shaft detent, control valve springs and control valve covers will appear worn out and become loose from their assembly.
>
> Root Cause:
>
> - TSC1 Torque Control message from OEM software arriving on the J1939 datalink configured incorrectly. The incorrect configuration causes the Torque Control messages to drive excessive engine brake activations up to several times the nominal activations seen on these applications.
>
> **Confirmation**
>
> - Inspect the back of the engine brake switch in the dashboard for any abnormal wiring. All wires should be directed to their respective ports. See equipment manufacturer service information.
> - Perform a complete overhead inspection of the engine brake parts. Take apart the rocker lever/shaft assembly and inspect the following:
>
> Figure 1, Engine Brake Shaft Detent Hole.
>
> Figure 2, Engine Brake Control Valve Spring.
>
> Figure 3, Engine Brake Actuator Piston.
>
> Figure 4, Engine Brake Contact Bridge Pin.
>
> **Resolution**
>
> - Contact the OEM for further instructions on how to address this type of failure.
>
> ### Document History
