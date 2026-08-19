---
aliases:
  - "Ошибка теста насоса DEF: ЭБУ не допускает выполнение теста"
type: "TSB"
doc: "tsb120182"
title_en: "DEF Pump Override Test Error - The engine control module has detected a condition that would not let the DEF Override Test run"
title_ru: "Ошибка теста насоса DEF: ЭБУ не допускает выполнение теста"
released: "2013-02-12"
modified: "2013-02-12"
group: "22 - Service Tools"
engines:
  - "41349633"
families:
  - "QSK19"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2012/tsb120182.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb120182.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QSK19"
  - "год/2013"
  - "перевод/машинный"
  - "тема/service-tools"
---

# DEF Pump Override Test Error - The engine control module has detected a condition that would not let the DEF Override Test run
**Ошибка теста насоса DEF: ЭБУ не допускает выполнение теста**

> [!abstract] TSB · `tsb120182`
> **Раздел Cummins:** 22 - Service Tools
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Даты:** выпущен 2013-02-12 · изменён 2013-02-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2012/tsb120182.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb120182.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Ошибка теста насоса DEF: ЭБУ не допускает выполнение теста

### Суть проблемы

Пользователи не могут запустить тест на перегрузку дизельного выхлопа (DEF) в электронном сервисе INSITETM. В сообщении, которое отображается в поле состояния в рамках теста, говорится: «ECM обнаружил условие, которое не позволит DEF перепроверить тест». Инструменты электронного обслуживания INSITETM ** не** предоставляют информацию о том, что такое условие, поэтому техник не знает, что исправить для запуска теста.

### Подтверждение

Пользователи могут увидеть ошибку, когда они пытаются запустить тест DEF Pump Override.

### Решение

**************************************************************************************************************************************************************************************************************************************************************** Если есть активные коды неисправностей, устраните их соответствующим образом. После того, как все коды неисправностей будут устранены и потребуется тест DEF Pump Override Test, следуйте инструкциям ниже:

- Отключите инструмент электронного сервиса INSITETM
- Замок зажигания
- Подождите 90 секунд (время для выключения всех устройств)
- Включите переключатель зажигания (подождите от 90 секунд до 2 минут, чтобы убедиться, что все запущено и готово к работе).
- Подключите инструмент электронного сервиса INSITETM и запустите тест DEF Pump Override Test.

Для постоянного решения этой проблемы была добавлена 90-секундная задержка, чтобы отложить начало испытания на перегрузку выхлопных газов дизельного топлива (DEF) после выбора кнопки «Пуск». Эта 90-секундная задержка позволит двигателю достичь начального состояния запуска, а затем позволит начать испытание. Данное исправление включено в инструмент электронного сервиса INSITETM версии 7.6, который был выпущен 23 октября 2012 года.

Кроме того, было реализовано уведомление для оповещения пользователя о состоянии недостающего состояния двигателя, обнаруженного с помощью инструментария электронного обслуживания INSITETM. Данное исправление доступно в электронном сервисе INSITETM версии 7.6.1, который был выпущен 30 января 2013 года.

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## DEF Pump Override Test Error - The engine control module has detected a condition that would not let the DEF Override Test run
>
> ### Core Issue
>
> Users are unable to run the Diesel Exhaust Fluid (DEF) Pump Override Test in INSITE™ electronic service tool. The message, which is displayed in the status box within the test, states “ECM detected a condition that would not let the DEF override test run”. INSITE™ electronic service tool does **not** provide information on what the condition is, therefore the technician does **not** know what to fix for the test to run.
>
> ### Confirmation
>
> Users may see the error when they try to run the DEF Pump Override Test.
>
> ### Resolution
>
> Verify there are **no** active fault codes. If there are active fault codes, troubleshoot those accordingly. After all fault codes are addressed and the DEF Pump Override Test is required, follow the directions below:
>
> - Disconnect INSITE™ electronic service tool
> - Turn keyswitch OFF
> - Wait 90 seconds (time for all devices to shut down)
> - Turn keyswitch ON (wait between 90 seconds and 2 minutes to make sure everything is started and ready for operation.)
> - Connect INSITE­™ electronic service tool and run the DEF Pump Override Test.
>
> To permanently address this issue; a 90 second delay was added to delay the start of the Diesel Exhaust Fluid (DEF) Pump Override Test after the “Start” button is selected. This 90 second delay will allow the engine to reach its prime start condition and will then allow the test to begin. This fix is included in INSITE™ electronic service tool, version 7.6, which was released on 23 October 2012.
>
> Also, a notification was implemented to alert the user of missing engine states status' detected by INSITE™ electronic service tool. This fix is available in INSITE™ electronic service tool, version 7.6.1,which was released on 30 January 2013.
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Document History
