---
type: "Сервисный бюллетень"
doc: "6643906"
title_en: "Engine Control Module (ECM) Calibration Download with Cummins® Electronic Service Tools"
released: "2025-07-22"
modified: "2025-08-08"
engines:
  - "77804793"
  - "77804810"
families:
  - "15N"
  - "A8.5"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/6643906.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/bulletin/6643906.pdf"
tags:
  - "документ/бюллетень"
  - "двигатель/15N"
  - "двигатель/A8.5"
  - "перевод/машинный"
---

# Engine Control Module (ECM) Calibration Download with Cummins® Electronic Service Tools

> [!abstract] Сервисный бюллетень · `6643906`
> **Двигатели:** [[77804793 — A8.5 CM2670 L153B CPL 6235|77804793]], [[77804810 — 15N CM2380 M104B CPL 5977|77804810]]
> **Семейство:** 15N, A8.5
> **Даты:** выпущен 2025-07-22 · изменён 2025-08-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/6643906.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/bulletin/6643906.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Модуль управления двигателем (ECM) Калибровка Скачать с помощью Cummins® Electronic Service Tools

**Затронутая продукция**

- Двигатели с управляемыми калибровочными передачами будут идентифицированы сервисной оснасткой

**Введение**

В настоящем документе внесены изменения в калибровочные передачи модуля управления двигателем (ECM) с помощью электронных средств обслуживания Cummins® для продуктов, которые осуществляют калибровочные передачи в процессе управления калибровкой службы (SCM).

**Обзор**

Начиная с мобильной версии 7.3/Windows версии 3.3 и электронной сервисной оснастки INSITETM версии 9.2, которая запланирована к выпуску в августе 2025 года, управление калибровкой службы (SCM) начнет управлять калибровочными установками в ECM. SCM - это процесс, который использует электронный сервисный инструмент Cummins® для определения правильной калибровки и предоставляет разрешение на калибровочную установку в ECM. SCM использует различные источники данных для определения правильной калибровки ECM для конкретного серийного номера двигателя (ESN) см. Рисунок 1.

![[00r01911.png]]

Рисунок 1, Схема потока SCM.

1. Dataplate Uprate

2. Полевой тест

3. SCM

4. Производственный завод

5. Полевое действие

Инструменты для электронных услуг Cummins® потребуют подключения к Интернету, а также ESN, чтобы SCM мог предоставить разрешение на установку калибровки ECM. Если подключение к Интернету **не** доступно на рабочем месте, то доступен офлайн-процесс, однако SCM должен предоставить авторизацию при подключении к Интернету до прибытия на рабочее место для установки калибровки ECM на ECM. Обновление базового кода ECM будет всегда разрешено независимо от подключения к Интернету. Инструменты электронного обслуживания Cummins® собирают данные для каждой передачи калибровки ECM в ECM.

Большинство переводов калибровки ECM в ECM являются обновлениями для пересмотра базового кода ECM. Для ремонта, который требует изменения базового кода ECM, необходимо ввести причину изменения. Причины изменения базового кода ECM:

- Кампания
- Практика временного ремонта (TRP)
- Охват команды аккаунта (ATC)
- повышать
- Бюллетени технического обслуживания (TSB)
- Новый/отредактированный модуль

При получении разрешения SCM для Кампании, TRP, ATC или TSB письмо будет предварительно заполнено только номером Должен быть введен.

Если проводится процедура модификации продукта 111-513-007 Модификация продукта должна быть выполнена с учетом запроса на новую табличку с данными двигателя. SCM будет разрешать передачу калибровки ECM только после завершения этих этапов.

Fleetcount или CalAssists больше не требуются при изменении базового кода ECM.

Для обеспечения дополнительной подготовки и информации по калибровочным установкам СКМ и ЕКМ были созданы или обновлены следующие элементы:

- Курс 1629 – Cummins Service Calibration Management был создан для предоставления дополнительной информации о SCM.
- Cummins Electronic Service Tools - Calibration Download Changes (недоступная ссылка)

> [!note] Примечание
> [https://quickserve.cummins.com/qs3/qsol/news/back\_office\_changes.html](https://quickserve.cummins.com/qs3/qsol/news/back_office_changes.html)

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## Engine Control Module (ECM) Calibration Download with Cummins ® Electronic Service Tools
>
> **Product Affected**
>
> - Engines with managed calibration transfers will be identified by the service tool
>
> **Introduction**
>
> This document introduces changes to engine control module (ECM) calibration transfers with Cummins® electronic service tools for products that calibration transfers are managed by the service calibration management (SCM) process.
>
> **Overview**
>
> Beginning with Guidanz Diagnostic Tool Kit (DTK) mobile version 7.3/Windows version 3.3 and INSITE™ electronic service tool version 9.2 which is scheduled for release in August 2025, the service calibration management (SCM) will begin to manage calibration installs to the ECM. The SCM is a process the Cummins® electronic service tool uses to determine the correct calibration and provides the authorization for the calibration install to the ECM. The SCM uses various sources of data to determine the correct ECM calibration for a particular engine serial number (ESN) see Figure 1.
>
> Figure 1, SCM Flow Schematic.
>
> 1. Dataplate Uprate
>
> 2. Field Test
>
> 3. SCM
>
> 4. Manufacturing Plant
>
> 5. Field Action
>
> The Cummins® electronic service tool will require internet connection as well as the ESN to allow SCM to provide authorization for the ECM calibration install. If internet connection is **not** available at the job site, an offline process is available, however the SCM **must** provide authorization while connected to the internet before arriving at the job site to install the ECM calibration to the ECM. A revision update to the ECM base code will **always** be authorized regardless of internet connection. The Cummins® electronic service tool collects data for every ECM calibration transfer to the ECM.
>
> Most ECM calibration transfers to the ECM are ECM base code revision updates. For the repairs that require an ECM base code change the reason for the change **must** be entered. Causes for ECM base code changes are:
>
> - Campaign
> - Temporary Repair Practices (TRP)
> - Account Team Coverage (ATC)
> - Uprate
> - Technical Service Bulletins (TSBs)
> - New/SEEDED Module
>
> When obtaining SCM authorization for Campaign, TRP, ATC or TSB the letter will be prepopulated only the number **must** be entered.
>
> If an uprate is being performed product modification procedure 111-513-007 Product Modification **must** be followed including request for a new engine dataplate. SCM will only authorize the ECM calibration transfer after these steps are completed.
>
> Fleetcount or CalAssists are no longer required when changing the ECM base code.
>
> The following items have been created or updated to provide additional training and information on SCM and ECM calibration installs:
>
> - Training course 1629 – Cummins Service Calibration Management has been created to provide further detail on SCM.
> - News article Cummins Electronic Service Tools – Calibration Download Changes
>
> **Note · Примечание**
> [https://quickserve.cummins.com/qs3/qsol/news/back\_office\_changes.html](https://quickserve.cummins.com/qs3/qsol/news/back_office_changes.html)
>
> ### Document History
