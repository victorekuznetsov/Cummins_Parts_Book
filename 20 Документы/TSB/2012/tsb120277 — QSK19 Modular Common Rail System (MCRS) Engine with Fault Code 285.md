---
aliases:
  - "QSK19 MCRS с кодом неисправности 285"
type: "TSB"
doc: "tsb120277"
title_en: "QSK19 Modular Common Rail System (MCRS) Engine with Fault Code 285"
title_ru: "QSK19 MCRS с кодом неисправности 285"
released: "2012-10-23"
modified: "2012-10-23"
group: "19 - Electronic Engine Controls"
engines:
  - "41349633"
families:
  - "QSK19"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2012/tsb120277.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb120277.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QSK19"
  - "год/2012"
  - "перевод/машинный"
  - "тема/electronic-engine-controls"
---

# QSK19 Modular Common Rail System (MCRS) Engine with Fault Code 285
**QSK19 MCRS с кодом неисправности 285**

> [!abstract] TSB · `tsb120277`
> **Раздел Cummins:** 19 - Electronic Engine Controls
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Даты:** выпущен 2012-10-23 · изменён 2012-10-23
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2012/tsb120277.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb120277.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## QSK19 MCRS с кодом неисправности 285

### Суть проблемы

Поступила жалоба от клиента на то, что код 285 ошибки является активным или его количество неактивно. На некоторых калибровках была допущена ошибка калибровки, которая установила показатель Mux\_Timeout\_Fault\_Count до 500 миллисекунд \[.50 секунд], который равен скорости передачи и вызывает ложные коды неисправностей.

Эта проблема была замечена на Фазе 18 программного обеспечения для двигателей CM850 и Фазе 25 для двигателей CM2150.

### Подтверждение

- Проверить, что J1939 Multiplexing включен.
- Убедитесь, что счетчик Mux\_Timeout\_Fault\_Count установлен на 500 миллисекунд \[.50 секунд] с использованием Calterm. Если он установлен на более чем 2000 миллисекунд \[2.0 секунды\], то проигнорируйте этот документ и продолжайте с обычными шагами устранения неисправностей кода.

### Решение

Модуль управления двигателем (ECM) ** должен быть откалиброван с помощью последней калибровки, доступной на диске INCALTM. Это должно изменить Mux\_Timeout\_Fault\_Count, который должен быть установлен на более чем 2000 миллисекунд \[2.0 секунды\]. Если он все еще установлен на 500 миллисекунд или все еще происходит неисправность, следуйте обычному процессу эскалации для Cummins, Inc.

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## QSK19 Modular Common Rail System (MCRS) Engine with Fault Code 285
>
> ### Core Issue
>
> A customer complaint has been received for Fault Code 285 being active or high counts of it inactive. A calibration error was made on some calibrations, which set Mux\_Timeout\_Fault\_Count to 500 milliseconds \[.50 seconds\] which equals the transmit rate and causes false fault codes.
>
> This issue has been seen on Phase 18 software for CM850 engines and Phase 25 for CM2150 engines.
>
> ### Confirmation
>
> - Verify that the J1939 Multiplexing is enabled.
> - Verify that the Mux\_Timeout\_Fault\_Count is set to 500 milliseconds \[.50 seconds\] using Calterm. If it is set to greater than 2,000 milliseconds \[2.0 seconds\] then disregard this document and continue with normal fault code troubleshooting steps.
>
> ### Resolution
>
> The engine control module (ECM) **must** be calibrated with the latest calibration available on the INCAL™ disc. This should change the Mux\_Timeout\_Fault\_Count to be set to greater than 2,000 milliseconds \[2.0 seconds\]. If it is still set to 500 milliseconds \[.50 seconds\] or a fault still occurs, follow the factory normal escalation process for Cummins, Inc.
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Document History
