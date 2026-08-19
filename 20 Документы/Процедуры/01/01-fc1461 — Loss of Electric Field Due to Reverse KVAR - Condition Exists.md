---
aliases:
  - "Потеря возбуждения из-за обратной реактивной мощности — условие возникло"
type: "Процедура"
doc: "01-fc1461"
title_en: "Loss of Electric Field Due to Reverse KVAR - Condition Exists"
title_ru: "Потеря возбуждения из-за обратной реактивной мощности — условие возникло"
modified: "2012-05-08"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1461.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1461.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Loss of Electric Field Due to Reverse KVAR - Condition Exists
**Потеря возбуждения из-за обратной реактивной мощности — условие возникло**

> [!abstract] Процедура · `01-fc1461`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1461.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1461.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1461

### Потеря возбуждения из-за обратной реактивной мощности — условие возникло

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1461 P(P): СПН: ФМИ: Лампа: Отключение SRT: | Потеря поля (электрического) из-за обратного кВАР. | Генератор будет отключен. |

![[19802905.png]]

Схема генератора

### Описание цепи

В обычных условиях эксплуатации генераторная установка подключается к шине. Генераторная установка вырабатывает энергию, и когда она подключается к шине, к основной электрической шине добавляется мощность. Когда происходят некоторые события, может возникнуть состояние, когда генераторная установка больше не производит энергию для электрической шины, а вместо этого потребляет энергию от электрической шины. Это состояние называется обратным сокращением киловольта-ампера (kVAR). Иногда состояние обратного кВАР может привести к потере генератором электрического поля.

Этот код неисправности используется модулем управления двигателем, чтобы сообщить оператору, что модуль управления двигателем обнаружил потерю электрического поля в генераторе из-за обратного состояния kVAR.

### Расположение компонента

Справочный раздел E для определения местоположения карточной клетки модуля управления двигателем.

Справочная клиентская/факультативно-установочная документация для определения местоположения генераторного набора выключателя и интерфейса с электрической шиной.

### Практические замечания

Возможный режим отказа, возможно, обусловлен конденсаторами коррекции коэффициента мощности или другими источниками питания, подавающими кВАР в генераторную установку.

За пределами определенного порога обратный kVAR может привести к нестабильности выходного напряжения и скольжению полюсов из-за того, что генератор становится самовоспаленным.

Проверьте линии разделения нагрузки для правильного подключения.

См. Код устранения неполадок t05-1461.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1461
>
> ### Loss of Electric Field Due to Reverse KVAR - Condition Exists
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1461 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Loss of field (electric) due to reverse kVAR. | Generator set will shut down. |
>
> Generator Circuit
>
> ### Circuit Description
>
> Under normal operating conditions, the generator set connects to the bus. The generator set is producing power, and when it connects to the bus, power is added to the main electric bus. When some events occur, a condition can occur when the generator set is no longer producing power for the electric bus, but rather is drawing power from the electric bus. This condition is called reverse kilovolt-ampere reduction (kVAR). Sometimes a reverse kVAR condition can cause the alternator to lose its electric field.
>
> This fault code is used by the engine control module to tell the operator that the engine control module has detected a loss of electric field in the alternator due to a reverse kVAR condition.
>
> ### Component Location
>
> Reference Section E for location of the engine control module card cage.
>
> Reference customer/facility/installation documentation for the location of the generator set circuit breaker and interface with the electric bus.
>
> ### Shoptalk
>
> The possible failure mode is perhaps due to power factor correction capacitors or other power sources feeding kVAR into the generator set.
>
> Beyond a certain threshold, reverse kVAR can lead to voltage output instability and pole slipping due to the fact that the alternator becomes self-excited.
>
> Check load-sharing lines for proper connection.
>
> Refer to Troubleshooting Fault Code t05-1461.
