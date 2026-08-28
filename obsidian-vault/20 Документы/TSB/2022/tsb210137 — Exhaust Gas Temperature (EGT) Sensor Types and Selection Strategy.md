---
aliases:
  - "Типы датчиков температуры ОГ (EGT) и порядок их выбора"
type: "TSB"
doc: "tsb210137"
title_en: "Exhaust Gas Temperature (EGT) Sensor Types and Selection Strategy"
title_ru: "Типы датчиков температуры ОГ (EGT) и порядок их выбора"
released: "2022-06-27"
modified: "2022-06-27"
group: "19 - Electronic Engine Controls"
engines:
  - "33224404"
  - "33239746"
  - "33239899"
  - "41340468"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSK50"
figures: 8
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2021/tsb210137.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb210137.pdf"
tags:
  - "документ/tsb"
  - "двигатель/K38/K50"
  - "двигатель/QSK50"
  - "год/2022"
  - "перевод/машинный"
  - "тема/electronic-engine-controls"
---

# Exhaust Gas Temperature (EGT) Sensor Types and Selection Strategy
**Типы датчиков температуры ОГ (EGT) и порядок их выбора**

> [!abstract] TSB · `tsb210137`
> **Раздел Cummins:** 19 - Electronic Engine Controls
> **Двигатели:** [[33224404 — QSK50 CM2150 MCRS CPL 3391|33224404]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[41340468 — QSK50 CM2150 MCRS CPL 3728|41340468]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60, QSK50
> **Даты:** выпущен 2022-06-27 · изменён 2022-06-27
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2021/tsb210137.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb210137.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Типы датчиков температуры ОГ (EGT) и порядок их выбора

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### Содержание

**Затронутая продукция**

- QSK50 CM2150 K107
- QSK50 CM2150 MCRS
- QSK50 DF CM850/CM2150
- QSK60 CM2150 MCRS

**Описание изменения**

В этом документе анонсированы новые калибровки модуля управления двигателем (ECM), которые позволяют обнаруживать, выбирать и поддерживать один из двух различных типов датчиков температуры выхлопных газов (EGT). Термисторы и термопары.

**Причина изменения**

- Недавно были выпущены термопары EGT в качестве более надежной альтернативы существующим терморезисторным датчикам EGT.
- Для получения подробной информации о внедрении более надежных термопарных датчиков EGT:

**Клиентская коммуникация**

- Новые промышленные двигатели (за исключением двигателей для нефтегазовых установок) будут иметь датчики типа EGT по умолчанию, установленные на «Thermocouple» в калибровках ECM. Это связано с тем, что новые промышленные двигатели будут оснащены термопарными датчиками EGT.
- Для двигателей в полевых условиях с терморезисторными датчиками EGT тип выбора «Термистор EGTS» будет по-прежнему использоваться при загрузке нового калибровочного кода ECM.
- Для двигателей в полевых условиях с термопарными датчиками EGT тип выбора «Thermocouple EGTS» будет по-прежнему использоваться при загрузке нового калибровочного кода ECM.
- Для двигателей в полевых условиях без датчиков EGT датчики EGT будут по-прежнему отключаться при загрузке нового калибровочного кода ECM.

**Указания по обслуживанию**

- Инструменты для электронного обслуживания Cummins INSITETM также могут использоваться для настройки типа выбора датчиков EGT среди термопар, терморезисторов или без них (для двигателей без датчиков EGT).
- Только в электронной версии 8.7.1 для инструментов обслуживания INSITETM и более поздней версии эта функция может быть использована. Подтвердите, что инструмент является версией 8.7.1 и более поздней.

**Изменение выбора типа датчика EGT с помощью инструментария INSITE Electronic Service:**

1. Перейдите на «Особенности и параметры» =\> CM2150E\[1\]\[Второй 1\] =\> «Выбор типа датчика EGT» и выберите тип датчика EGT, который установлен на двигателе. См. рисунки 1 и 2 ниже.

![[19r99747.png]]

Рисунок 1 - Навигация по типу датчика EGT.

![[19r99748.png]]

Рисунок 2, Выберите подходящий тип датчика EGT.

> [!note] Примечание
> Логика выбора «Автодетектив» в настоящее время не реализована в программном обеспечении. Если будет сделан выбор «Автодетектив», то для обработки EGT будет использоваться тип датчика Thermistor EGT.

2. Выберите выделенный значок «Отправить в ECM» или щелкните правой кнопкой мыши, выберите «Отправить в», «ECM» и выберите «ОК». См. рисунок 3 ниже.

![[19r99749.png]]

Рисунок 3, Выберите «Отправить в ECM».

3. Выберите «ОК» для подтверждения настройки ECM. См. рисунок 4 ниже.

![[19r99750.png]]

Рисунок 4, Подтверждаем корректировку ECM.

4. Переключите зажигание в положение выключения и выберите «ОК» См. рисунок 5 ниже.

![[19r99751.png]]

Рис. 5, замок зажигания.

5. Переключите зажигание в положение ON и выберите «ОК». См. рисунок 6 ниже.

![[19r99752.png]]

Рис. 6, включена замок зажигания.

6. Следуйте за подсказкой и выберите «ОК». Сенсорный тип EGT будет успешно сохранен. См. рисунок 7 ниже.

![[19r99753.png]]

Рисунок 7, ECM Write Succeeded.

**Мониторинг типа датчика ЭГТ:**

Этот экран используется для мониторинга типа датчика EGT, используемого ECM для обработки ввода EGT.

1. Перейдите в раздел «Монитор данных/Logger» =\> CM2150E\[1\]\[Второй пункт 1\] =\> «Обнаружен тип датчика EGT».Нажмите «Данные журнала» или «Начало/Обзор» для мониторинга обнаруженного типа датчика EGT и используемого для обработки EGT в программном обеспечении. См. Рисунок 8 ниже.

![[19r99754.png]]

Рисунок 8, Мониторинг обнаруженного типа датчика EGT.

**Идентификация детали**

Для запуска новейшего программного обеспечения с функцией выбора типа датчика EGT, проверьте, что калибровки ECM, установленные на двигателе, перечислены в таблицах ниже. Все коды калибровки ECM, выпущенные до этого выпуска программного обеспечения, будут **не** поддерживать функцию выбора типа датчика EGT.

| Таблица 1, Фаза программного обеспечения |  |
|---|---|
| Двигательная платформа | Фаза программного обеспечения |
| QSK50 CM2150 | 25.02.01.20 |
| QSK50 CM2150 (KOMNET) | 25.02.30.18 |
| QSK60 CM2150 | 25.02.01.20 |

| Таблица 2, QSK50 CM2150 |  |  |  |  |  |
|---|---|---|---|---|---|
| SC Option | Семейство двигателей | Делай выбор | FR Вариант | PP Вариант | Калибровочный код ЭБУ |
| SC60621 | QSKTA50-CE | ДО06765 | FR06734 | PP43379 | AQ60217.28 |
| SC60623 | QSKTA50-CE | 66767 | FR06736 | PP43391 | AQ60220.25 |
| SC60707 | QSKTA50-CE | ДО06853 | FR06782 | PP43548 | AQ60287.19 |
| SC60720 | QSKTA50-CE | ДО06866 | FR06790 | PP43548 | AQ60288.19 |
| SC60724 | QSKTA50-CE | ДО 66870 | FR06794 | PP43905 | AQ60421.17 |
| SC60725 | QSKTA50-CE | ДО06871 | FR06795 | PP43548 | AQ60289.22 |
| SC60776 | QSKTA50-CE | ДО06928 | FR06734 | PP43379 | AQ60252.21 |
| SC60823 | QSKTA50-CE | ДО06976 | FR06734 | PP43379 | AQ60296.18 |
| SC60824 | QSKTA50-CE | ДО06977 | FR06856 | PP43548 | AQ60292.17 |
| SC60825 | QSKTA50-CE | ДО06978 | FR06857 | PP43391 | AQ60293.16 |
| SC60826 | QSKTA50-CE | ДО06979 | FR06858 | PP43548 | AQ60294.17 |
| SC60827 | QSKTA50-CE | ДО 66980 | FR06859 | PP43669 | AQ60297.16 |
| SC60828 | QSKTA50-CE | ДО06981 | FR06860 | PP43669 | AQ60309.20 |
| SC60829 | QSKTA50-CE | ДО06982 | FR06861 | PP43669 | AQ60310.20 |
| SC60833 | QSKTA50-CE | ДО 6988 | FR06974 | PP43548 | AQ60301.19 |
| SC60861 | QSKTA50-CE | ДО 60018 | FR06734 | PP43379 | AQ60320.19 |
| SC60869 | QSKTA50-CE | ДО 60026 | FR06901 | PP43905 | AQ60429.17 |
| SC60881 | QSKTA50-CE | ДОКТО 60038 | FR06905 | PP43379 | AQ60401.19 |
| SC60924 | QSKTA50-CE | 60081 | FR06736 | PP43391 | AQ60338.22 |
| SC60987 | QSKTA50-CE | ДО 60148 | FR06905 | PP43379 | AQ60399.23 |
| SC61043 | QSKTA50-CE | ДО60202 | FR06795 | PP43548 | AQ60417.17 |
| SC61045 | QSKTA50-CE | ДО60204 | FR06975 | PP43379 | AQ60420.15 |
| SC61056 | QSKTA50-CE | ДО 60215 | FR06861 | PP43669 | AQ60444.17 |
| SC61210 | QSKTA50-CE | ДО60371 | FR06858 | PP43548 | AQ60458.15 |
| SC61069 | QSKTA50-CE | ДО 60228 | FR06990 | PP43976 | AQ60463.16 |
| SC61070 | QSKTA50-CE | ДО 60229 | FR06991 | PP43976 | AQ60464.17 |
| SC61227 | QSKTA50-CE | ДО 60388 | FR60014 | PP43548 | AQ60989.02 |
| SC61244 | QSKTA50-CE | ДО 60405 | FR06734 | PP43379 | AQ60479.16 |
| SC61245 | QSKTA50-CE | ДО 60406 | FR06790 | PP43548 | AQ60480.15 |
| SC61246 | QSKTA50-CE | ДО60407 | FR06795 | PP43548 | AQ60481.16 |
| SC61247 | QSKTA50-CE | ДО 60408 | FR06736 | PP43391 | AQ60490.19 |
| SC61248 | QSKTA50-CE | ДО 60409 | FR06782 | PP43548 | AQ60491.15 |
| SC61249 | QSKTA50-CE | ДО 60410 | FR06974 | PP43548 | AQ60492.15 |
| SC61250 | QSKTA50-CE | ДО 60411 | FR06794 | PP43905 | AQ60493.16 |
| SC61255 | QSKTA50-CE | ДО 60230 | FR06858 | PP43548 | AQ60489.12 |
| SC61259 | QSKTA50-CE | ДО 60418 | FR06734 | PP43379 | AQ60484.15 |
| SC61286 | QSKTA50-CE | ДО 60445 | FR06794 | PP43905 | AQ60498.16 |
| SC61287 | QSKTA50-CE | ДО 60446 | FR06901 | PP43905 | AQ60500.16 |
| SC61288 | QSKTA50-CE | ДО 60447 | FR06734 | PP43379 | AQ60504.15 |
| SC61585 | QSKTA50-CE | ДО60747 | FR06734 | PP43379 | AQ60701.13 |
| SC61687 | QSKTA50-CE | ДО 60848 | FR60457 | PP43669 | AQ60805.06 |
| SC61704 | QSKTA50-CE | ДО 60870 | FR06736 | PP43391 | AQ60756.05 |
| SC61716 | QSKTA50-CE | ДО60882 | FR60048 | PP43548 | AQ60765.08 |
| SC61719 | QSKTA50-CE | ДО60885 | FR60350 | PP43391 | AQ60803.03 |
| SC61774 | QSKTA50-CE | ДО 60940 | FR06736 | PP43391 | AQ60769.09 |
| SC61803 | QSKTA50-CE | ДО 60969 | FR06860 | PP43669 | AQ60775.07 |
| SC61804 | QSKTA50-CE | ДО 60970 | FR06861 | PP43669 | AQ60776.07 |
| SC61810 | QSKTA50-CE | ДО60976 | FR06859 | PP43669 | AQ60800.06 |
| SC61813 | QSKTA50-CE | ДО 60979 | FR06794 | PP43905 | AQ60785.06 |
| SC61814 | QSKTA50-CE | ДО 60980 | FR06901 | PP43905 | AQ60786.06 |
| SC61844 | QSKTA50-CE | ДО 61010 | FR60457 | PP43669 | AQ60796.06 |
| SC61864 | QSKTA50-CE | ДО 61028 | FR60457 | PP43669 | AQ60807.07 |
| SC61878 | QSKTA50-CE | ДО 61042 | FR06734 | PP43379 | AQ60809.06 |
| SC61918 | QSKTA50-CE | ДО 61084 | FR06858 | PP43548 | AQ60889.03 |
| SC61928 | QSKTA50-CE | ДО 61094 | FR06790 | PP43548 | AQ60888.03 |
| SC61929 | QSKTA50-CE | ДО 61095 | FR60048 | PP43548 | AQ60882.03 |
| SC61981 | QSKTA50-CE | 61147 | FR60457 | PP43669 | AQ60874.03 |
| SC61985 | QSKTA50-CE | 61160 | FR60522 | PP43669 | AQ60883.03 |
| SC61993 | QSKTA50-CE | 61159 | FR60522 | PP43669 | AQ60884.03 |
| SC62006 | QSKTA50-CE | 61180 | FR60457 | PP43669 | AQ60892.03 |
| SC62022 | QSKTA50-CE | ДО61182 | FR06794 | PP43905 | AQ60941.03 |
| SC62023 | QSKTA50-CE | 61183 | FR06901 | PP43905 | AQ60942.03 |
| SC62024 | QSKTA50-CE | 61184 | FR06859 | PP43669 | AQ60939.02 |
| SC62025 | QSKTA50-CE | ДО 61185 | FR06859 | PP43669 | AQ60940.02 |
| SC62030 | QSKTA50-CE | ДО 61190 | FR06858 | PP43548 | AQ60911.02 |
| SC62031 | QSKTA50-CE | Do61191 | FR06858 | PP43548 | AQ60912.02 |
| SC62039 | QSKTA50-CE | 61199 | FR06856 | PP43548 | AQ60934.02 |
| SC62040 | QSKTA50-CE | 612200 | FR06857 | PP43391 | AQ60935.02 |
| SC62041 | QSKTA50-CE | ДО61201 | FR60351 | PP43391 | AQ60936.03 |
| SC62042 | QSKTA50-CE | ДО61202 | FR06858 | PP43548 | AQ60937.02 |
| SC62043 | QSKTA50-CE | ДО61203 | FR06858 | PP43548 | AQ60938.02 |
| SC62044 | QSKTA50-CE | 6124 | FR06905 | PP43379 | AQ60901.02 |
| SC62045 | QSKTA50-CE | 6125 | FR06905 | PP43379 | AQ60902.03 |
| SC62046 | QSKTA50-CE | 6206 | FR06901 | PP43905 | AQ60903.02 |
| SC62047 | QSKTA50-CE | 6207 | FR06901 | PP43905 | AQ60904.02 |
| SC62129 | QSKTA50-CE | ДО 61306 | FR06901 | PP43905 | AQ60979.01 |
| SC62130 | QSKTA50-CE | ДО61307 | FR06790 | PP43548 | AQ60980.01 |
| SC60853 | QSKTA50-CE | ДО 60010 | FR06888 | PP43728 | AQ60359.21 |
| SC60854 | QSKTA50-CE | ДО 60011 | FR06889 | PP43728 | AQ60360.19 |
| SC60855 | QSKTA50-CE | ДО 60012 | FR06890 | PP43728 | AQ60361.19 |
| SC60856 | QSKTA50-CE | ДО 60013 | FR06888 | PP43728 | AQ60362.22 |
| SC60936 | QSKTA50-CE | 60096 | FR06890 | PP43728 | AQ60363.21 |
| SC60937 | QSKTA50-CE | ДО 60097 | FR06890 | PP43728 | AQ60364.19 |
| SC60938 | QSKTA50-CE | 60098 | FR06890 | PP43728 | AQ60365.20 |
| SC60939 | QSKTA50-CE | ДО 60099 | FR06888 | PP43728 | AQ60366.19 |
| SC60940 | QSKTA50-CE | ДО 60100 | FR06888 | PP43728 | AQ60378.20 |
| SC60941 | QSKTA50-CE | ДО 60101 | FR06888 | PP43728 | AQ60379.20 |
| SC60942 | QSKTA50-CE | ДО 60102 | FR06888 | PP43728 | AQ60380.19 |
| SC60943 | QSKTA50-CE | ДО 60103 | FR06888 | PP43728 | AQ60386.21 |
| SC60944 | QSKTA50-CE | ДО60104 | FR06888 | PP43728 | AQ60381.19 |
| SC60957 | QSKTA50-CE | ДО 60118 | FR06888 | PP43728 | AQ60373.21 |
| SC60958 | QSKTA50-CE | 60119 | FR06888 | PP43728 | AQ60374.20 |
| SC60959 | QSKTA50-CE | ДО 60120 | FR06888 | PP43728 | AQ60375.21 |
| SC60960 | QSKTA50-CE | ДО 60121 | FR06888 | PP43728 | AQ60376.18 |
| SC60961 | QSKTA50-CE | ДО 60122 | FR06888 | PP43728 | AQ60377.20 |
| SC60962 | QSKTA50-CE | ДО 60123 | FR06889 | PP43728 | AQ60367.19 |
| SC60963 | QSKTA50-CE | ДО 60124 | FR06889 | PP43728 | AQ60368.19 |
| SC60964 | QSKTA50-CE | ДО 60125 | FR06889 | PP43728 | AQ60369.19 |
| SC60965 | QSKTA50-CE | ДО 60126 | FR06889 | PP43728 | AQ60370.19 |
| SC60966 | QSKTA50-CE | ДО 60127 | FR06889 | PP43728 | AQ60371.19 |
| SC60967 | QSKTA50-CE | ДО 60128 | FR06890 | PP43728 | AQ60387.22 |
| SC60968 | QSKTA50-CE | ДО 60129 | FR06890 | PP43728 | AQ60388.21 |
| SC60969 | QSKTA50-CE | ДО 60130 | FR06890 | PP43728 | AQ60389.19 |
| SC60970 | QSKTA50-CE | ДО 60131 | FR06890 | PP43728 | AQ60390.19 |
| SC60971 | QSKTA50-CE | ДО 60132 | FR06888 | PP43728 | AQ60395.20 |
| SC60972 | QSKTA50-CE | ДО 60133 | FR06890 | PP43728 | AQ60391.21 |
| SC60973 | QSKTA50-CE | ДО 60134 | FR06890 | PP43728 | AQ60392.17 |
| SC60974 | QSKTA50-CE | 60135 | FR06890 | PP43728 | AQ60402.19 |
| SC60993 | QSKTA50-CE | ДО60154 | FR06888 | PP43728 | AQ60404.20 |
| SC60996 | QSKTA50-CE | ДО 60157 | FR06890 | PP43728 | AQ60397.19 |
| SC61013 | QSKTA50-CE | ДО 60173 | FR06890 | PP43728 | AQ60410.18 |
| SC61031 | QSKTA50-CE | ДО60191 | FR06889 | PP43728 | AQ60441.18 |
| SC61035 | QSKTA50-CE | ДО 60195 | FR06889 | PP43728 | AQ60416.16 |
| SC61037 | QSKTA50-CE | ДО 60197 | FR06890 | PP43728 | AQ60442.16 |
| SC61046 | QSKTA50-CE | ДО 60205 | FR06890 | PP43728 | AQ60443.22 |
| SC61055 | QSKTA50-CE | ДО 60213 | FR06890 | PP43728 | AQ60440.18 |
| SC61076 | QSKTA50-CE | ДО 60236 | FR06888 | PP43728 | AQ60445.16 |
| SC61207 | QSKTA50-CE | ДО 60368 | FR06888 | PP43728 | AQ60453.19 |
| SC61208 | QSKTA50-CE | 60369 | FR06889 | PP43728 | AQ60454.19 |
| SC61209 | QSKTA50-CE | ДО 60370 | FR06890 | PP43728 | AQ60455.19 |
| SC61214 | QSKTA50-CE | ДО 60375 | FR06890 | PP43728 | AQ60456.17 |
| SC61216 | QSKTA50-CE | ДО 60377 | FR06890 | PP43728 | AQ60475.17 |
| SC61222 | QSKTA50-CE | ДО60383 | FR06888 | PP43728 | AQ60476.16 |
| SC61284 | QSKTA50-CE | ДО60443 | FR06890 | PP43728 | AQ60499.16 |
| SC61468 | QSKTA50-CE | ДО 60629 | FR06888 | PP43728 | AQ60690.11 |
| SC61485 | QSKTA50-CE | ДО 60646 | FR06890 | PP43728 | AQ60694.12 |
| SC61516 | QSKTA50-CE | ДО60677 | FR06890 | PP43728 | AQ60677.13 |
| SC61550 | QSKTA50-CE | ДО 60711 | FR06890 | PP43728 | AQ60691.14 |
| SC61575 | QSKTA50-CE | ДО 60737 | FR06888 | PP43728 | AQ60695.12 |
| SC61577 | QSKTA50-CE | ДО 60739 | FR06888 | PP43728 | AQ60696.12 |
| SC61579 | QSKTA50-CE | ДО60741 | FR06888 | PP43728 | AQ60700.14 |
| SC61682 | QSKTA50-CE | ДО 60849 | FR06888 | PP43728 | AQ60751.09 |
| SC61773 | QSKTA50-CE | ДО 60939 | FR06888 | PP43728 | AQ60770.07 |
| SC61783 | QSKTA50-CE | ДО 60949 | FR06890 | PP43728 | AQ60773.07 |
| SC61860 | QSKTA50-CE | ДО 61026 | FR06890 | PP43728 | AQ60811.06 |
| SC61893 | QSKTA50-CE | ДО 61059 | FR06890 | PP43728 | AQ60824.05 |
| SC61900 | QSKTA50-CE | ДО 61066 | FR06890 | PP43728 | AQ60825.05 |
| SC61978 | QSKTA50-CE | 6144 | FR06890 | PP43728 | AQ60876.03 |
| SC61998 | QSKTA50-CE | 6165 | FR06889 | PP43728 | AQ60890.03 |
| SC61999 | QSKTA50-CE | ДО 6166 | FR06890 | PP43728 | AQ60886.03 |
| SC62019 | QSKTA50-CE | 61178 | FR06890 | PP43728 | AQ60891.03 |

| Таблица 3, QSK60 CM2150 |  |  |  |  |  |
|---|---|---|---|---|---|
| SC Option | Семейство двигателей | Делай выбор | FR Вариант | PP Вариант | Калибровочный код ЭБУ |
| SC60620 | QSKTA60-CE | ДО06764 | FR06733 | PP43416 | AQ60218.26 |
| SC60648 | QSKTA60-CE | ДО06792 | FR06746 | PP43451 | AQ60221.24 |
| SC60659 | QSKTA60-CE | ДО06803 | FR06751 | PP43416 | AQ60236.23 |
| SC60660 | QSKTA60-CE | ДО06804 | FR06751 | PP43416 | AQ60237.24 |
| SC60693 | QSKTTA60-CE | 66839 | FR06773 | PP43501 | AQ60238.23 |
| SC60706 | QSKTA60-CE | ДО06852 | FR06781 | PP43416 | AQ60317.19 |
| SC60721 | QSKTA60-CE | 66867 | FR06791 | PP43451 | AQ60337.19 |
| SC60722 | QSKTA60-CE | ДО06868 | FR06792 | PP43451 | AQ60302.18 |
| SC60723 | QSKTA60-CE | ДО06869 | FR06793 | PP43451 | AQ60305.23 |
| SC60726 | QSKTA60-CE | ДО06872 | FR06796 | PP43451 | AQ60303.25 |
| SC60777 | QSKTA60-CE | ДО 66929 | FR06746 | PP43451 | AQ60253.24 |
| SC60779 | QSKTA60-CE | ДО06931 | FR06829 | PP43378 | AQ60255.17 |
| SC60780 | QSKTA60-CE | ДО06932 | FR06830 | PP43378 | AQ60285.16 |
| SC60781 | QSKTA60-CE | ДО06933 | FR06831 | PP43451 | AQ60254.27 |
| SC60822 | QSKTA60-CE | ДО06975 | FR06746 | PP43451 | AQ60295.15 |
| SC60834 | QSKTA60-CE | ДО 6989 | FR06792 | PP43451 | AQ60304.21 |
| SC60842 | QSKTA60-CE | ДО 6997 | FR06781 | PP43416 | AQ60318.15 |
| SC60846 | QSKTA60-CE | ДО 60002 | FR06792 | PP43451 | AQ60314.19 |
| SC60847 | QSKTA60-CE | ДО 60003 | FR06751 | PP43416 | AQ60312.18 |
| SC60848 | QSKTA60-CE | ДО 60004 | FR06733 | PP43416 | AQ60313.17 |
| SC60849 | QSKTA60-CE | ДО 60005 | FR06792 | PP43451 | AQ60315.17 |
| SC60850 | QSKTA60-CE | 60006 | FR06792 | PP43451 | AQ60316.18 |
| SC60863 | QSKTA60-CE | ДО60020 | FR06895 | PP43451 | AQ60326.21 |
| SC60864 | QSKTA60-CE | ДОКТО 60021 | FR06896 | PP43451 | AQ60327.23 |
| SC60865 | QSKTA60-CE | ДО 60022 | FR06897 | PP43416 | AQ60328.26 |
| SC60866 | QSKTA60-CE | ДО 60023 | FR06898 | PP43451 | AQ60329.22 |
| SC60867 | QSKTA60-CE | ДО 60024 | FR06899 | PP43416 | AQ60330.19 |
| SC60868 | QSKTA60-CE | ДОК 60025 | FR06900 | PP43451 | AQ60451.14 |
| SC60880 | QSKTA60-CE | ДО 60037 | FR06895 | PP43451 | AQ60325.17 |
| SC60882 | QSKTA60-CE | ДО 60039 | FR06906 | PP43451 | AQ60331.18 |
| SC60883 | QSKTA60-CE | ДО60040 | FR06907 | PP43451 | AQ60341.22 |
| SC60885 | QSKTA60-CE | ДОК 60042 | FR06908 | PP43451 | AQ60342.19 |
| SC60891 | QSKTA60-CE | ДО 60048 | FR06898 | PP43451 | AQ60335.17 |
| SC60911 | QSKTA60-CE | ДОК 60068 | FR06863 | PP43451 | AQ60343.18 |
| SC60912 | QSKTA60-CE | 60069 | FR06864 | PP43451 | AQ60344.16 |
| SC60913 | QSKTA60-CE | ДО 60070 | FR06865 | PP43451 | AQ60345.16 |
| SC60951 | QSKTA60-CE | 60111 | FR06746 | PP43451 | AQ60352.18 |
| SC60986 | QSKTTA60-CE | ДО 60147 | FR06938 | PP43501 | AQ60398.20 |
| SC61014 | QSKTA60-CE | ДО60174 | FR06866 | PP43451 | AQ60412.13 |
| SC61015 | QSKTA60-CE | 60175 | FR06867 | PP43451 | AQ60413.14 |
| SC61039 | QSKTTA60-CE | ДО 60198 | FR06773 | PP43501 | AQ60415.14 |
| SC61040 | QSKTTA60-CE | 60199 | FR06938 | PP43501 | AQ60433.14 |
| SC61044 | QSKTA60-CE | ДО60203 | FR06831 | PP43451 | AQ60431.16 |
| SC61073 | QSKTA60-CE | ДО60233 | FR06863 | PP43451 | AQ60446.19 |
| SC61224 | QSKTA60-CE | ДО 60385 | FR06906 | PP43451 | AQ60477.13 |
| SC61254 | QSKTA60-CE | ДО 60227 | FR06746 | PP43451 | AQ60482.14 |
| SC61264 | QSKTA60-CE | ДО 60423 | FR06831 | PP43451 | AQ60509.16 |
| SC61265 | QSKTA60-CE | ДО 60424 | FR06781 | PP43416 | AQ60510.13 |
| SC61266 | QSKTTA60-CE | ДО 60425 | FR06773 | PP43501 | AQ60511.16 |
| SC61267 | QSKTA60-CE | ДО 60426 | FR06796 | PP43451 | AQ60512.16 |
| SC61268 | QSKTA60-CE | ДО 60427 | FR06792 | PP43451 | AQ60506.13 |
| SC61269 | QSKTA60-CE | ДО 60428 | FR06733 | PP43416 | AQ60507.13 |
| SC61270 | QSKTA60-CE | ДО 60429 | FR06906 | PP43451 | AQ60508.14 |
| SC61272 | QSKTA60-CE | ДО60431 | FR06751 | PP43416 | AQ60501.14 |
| SC61273 | QSKTA60-CE | ДО60432 | FR06791 | PP43451 | AQ60502.13 |
| SC61274 | QSKTA60-CE | ДО60433 | FR06793 | PP43451 | AQ60503.13 |
| SC61279 | QSKTA60-CE | ДО 60438 | FR60369 | PP43451 | AQ60793.05 |
| SC61315 | QSKTA60-CE | 60475 | FR06751 | PP43416 | AQ60528.13 |
| SC61318 | QSKTA60-CE | 60478 | FR06746 | PP43451 | AQ60530.13 |
| SC61319 | QSKTA60-CE | 60479 | FR06898 | PP43451 | AQ60531.13 |
| SC61323 | QSKTA60-CE | ДО60843 | FR60088 | PP43416 | AQ60534.10 |
| SC61514 | QSKTA60-CE | ДО60884 | FR06898 | PP43451 | AQ60759.10 |
| SC61595 | QSKTA60-CE | ДО 60760 | FR06791 | PP43451 | AQ60717.11 |
| SC61596 | QSKTA60-CE | ДО60761 | FR06908 | PP43451 | AQ60716.11 |
| SC61612 | QSKTTA60-CE | ДО 60775 | FR06773 | PP43501 | AQ60724.11 |
| SC61664 | QSKTA60-CE | ДО 60827 | FR60323 | PP43416 | AQ60748.09 |
| SC61665 | QSKTA60-CE | ДО 60828 | FR60323 | PP43416 | AQ60749.10 |
| SC61673 | QSKTA60-CE | ДО 60836 | FR06897 | PP43416 | AQ60750.15 |
| SC61710 | QSKTA60-CE | ДО60876 | FR06751 | PP43416 | AQ60761.12 |
| SC61711 | QSKTTA60-CE | ДО60877 | FR06773 | PP43501 | AQ60762.10 |
| SC61712 | QSKTTA60-CE | DO60878 | FR06938 | PP43501 | AQ60763.10 |
| SC61764 | QSKTA60-CE | ДО 60930 | FR60407 | PP43416 | AQ60801.05 |
| SC61765 | QSKTA60-CE | ДО60931 | FR60408 | PP43416 | AQ60804.05 |
| SC61794 | QSKTA60-CE | ДО 60960 | FR60429 | PP44768 | AQ60789.06 |
| SC61795 | QSKTTA60-CE | ДО60961 | FR60444 | PP44828 | AQ60792.06 |
| SC61796 | QSKTA60-CE | ДО60962 | FR60431 | PP44768 | AQ60790.06 |
| SC61805 | QSKTA60-CE | ДО60971 | FR06867 | PP43451 | AQ60777.05 |
| SC61806 | QSKTA60-CE | ДО60972 | FR06865 | PP43451 | AQ60778.06 |
| SC61807 | QSKTA60-CE | ДО60973 | FR06864 | PP43451 | AQ60779.06 |
| SC61808 | QSKTA60-CE | ДО60974 | FR06863 | PP43451 | AQ60780.06 |
| SC61809 | QSKTA60-CE | ДО60975 | FR06866 | PP43451 | AQ60781.05 |
| SC61819 | QSKTA60-CE | ДО 60985 | FR60430 | PP44768 | AQ60791.06 |
| SC61848 | QSKTA60-CE | ДО 61014 | FR06746 | PP43451 | AQ60799.04 |
| SC61858 | QSKTA60-CE | ДО 61025 | FR06906 | PP43451 | AQ60808.05 |
| SC61894 | QSKTA60-CE | ДО 61060 | FR06796 | PP43451 | AQ60946.02 |
| SC61913 | QSKTTA60-CE | ДО 61079 | FR60444 | PP44828 | AQ60881.03 |
| SC61914 | QSKTA60-CE | ДО 61080 | FR06896 | PP43451 | AQ60947.02 |
| SC61980 | QSKTA60-CE | 6146 | FR06733 | PP43416 | AQ60879.03 |
| SC61987 | QSKTA60-CE | 6152 | FR06746 | PP43451 | AQ60880.03 |
| SC61989 | QSKTA60-CE | 6155 | FR06831 | PP43451 | AQ60877.03 |
| SC61996 | QSKTA60-CE | ДО 6163 | FR06830 | PP43378 | AQ60949.01 |
| SC61997 | QSKTA60-CE | ДО61164 | FR06896 | PP43451 | AQ60948.01 |
| SC62032 | QSKTA60-CE | 6192 | FR06896 | PP43451 | AQ60913.03 |
| SC62048 | QSKTA60-CE | ДО61208 | FR06830 | PP43378 | AQ60915.02 |
| SC62049 | QSKTA60-CE | 61209 | FR06895 | PP43451 | AQ60916.02 |
| SC62050 | QSKTA60-CE | ДО 61210 | FR06895 | PP43451 | AQ60917.02 |
| SC62051 | QSKTA60-CE | 61211 | FR06897 | PP43416 | AQ60918.04 |
| SC62052 | QSKTA60-CE | 6121212 | FR06897 | PP43416 | AQ60919.03 |
| SC62053 | QSKTA60-CE | ДО 61213 | FR06907 | PP43451 | AQ60920.02 |
| SC62054 | QSKTA60-CE | ДО 61214 | FR06898 | PP43451 | AQ60921.03 |
| SC62055 | QSKTA60-CE | 61215 | FR06898 | PP43451 | AQ60922.02 |
| SC62056 | QSKTA60-CE | ДО 61216 | FR06898 | PP43451 | AQ60923.02 |
| SC62057 | QSKTA60-CE | 61217 | FR06898 | PP43451 | AQ60924.03 |
| SC62058 | QSKTA60-CE | ДО 61218 | FR06908 | PP43451 | AQ60925.03 |
| SC62059 | QSKTA60-CE | ДО 61219 | FR06908 | PP43451 | AQ60926.02 |
| SC62060 | QSKTA60-CE | ДО 61220 | FR06899 | PP43416 | AQ60927.02 |
| SC62061 | QSKTA60-CE | ДО 61221 | FR06900 | PP43451 | AQ60928.02 |
| SC62062 | QSKTTA60-CE | ДО 61222 | FR06938 | PP43501 | AQ60929.02 |
| SC62063 | QSKTTA60-CE | ДО 61223 | FR06938 | PP43501 | AQ60930.03 |
| SC62064 | QSKTA60-CE | ДО 61224 | FR60323 | PP43416 | AQ60931.03 |
| SC62065 | QSKTA60-CE | ДО 61225 | FR60323 | PP43416 | AQ60932.03 |
| SC62066 | QSKTA60-CE | ДО 61226 | FR60408 | PP43416 | AQ60933.02 |
| SC62082 | QSKTA60-CE | ДО61244 | FR06831 | PP43451 | AQ60914.02 |
| SC62131 | QSKTA60-CE | ДО61308 | FR06792 | PP43451 | AQ60981.01 |
| SC62132 | QSKTA60-CE | ДО 6309 | FR06791 | PP43451 | AQ60982.01 |
| SC62133 | QSKTA60-CE | ДО 61310 | FR06796 | PP43451 | AQ60983.01 |
| SC62163 | QSKTTA60-CE | ДО 61337 | FR06773 | PP43501 | AQ60994.01 |
| SC62164 | QSKTA60-CE | ДО 61338 | FR06831 | PP43451 | AQ60995.01 |

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## Exhaust Gas Temperature (EGT) Sensor Types and Selection Strategy
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Contents
>
> **Product Affected**
>
> - QSK50 CM2150 K107
> - QSK50 CM2150 MCRS
> - QSK50 DF CM850/CM2150
> - QSK60 CM2150 MCRS
>
> **Description of Change**
>
> This document announces the new engine control module (ECM) calibrations which allow for detection, selection, and support of one of the two different types of exhaust gas temperature (EGT) sensor technologies available: Thermistors and Thermocouples.
>
> **Reason for Change**
>
> - Thermocouples EGT sensors were recently released as a more robust alternative to the existing thermistor EGT sensors.
> - For details on the introduction of the more robust thermocouple EGT sensors:
>
> **Customer Communication**
>
> - Newly built Industrial engines (except for engines in Oil and Gas applications) from the manufacturing plants will have the default EGT sensors type set to “Thermocouple” in the ECM calibrations. This is because new Industrial engines will be upfitted with thermocouple EGT sensors.
> - For engines in the field with thermistor EGT sensors, “Thermistor EGTS” selection type will continue to be used whenever a new ECM calibration code is downloaded.
> - For engines in the field with thermocouple EGT sensors, “Thermocouple EGTS” selection type will continue to be used whenever a new ECM calibration code is downloaded.
> - For engines in the field without EGT sensors, the EGT sensors will continue to be disabled whenever a new ECM calibration code is downloaded.
>
> **Service Instructions**
>
> - The Cummins INSITE™ Electronic Service tool can also be used to adjust the EGT sensors selection type among Thermocouples, Thermistors, or None (for engines without EGT sensors).
> - **Only** INSITE™ electronic service tool version 8.7.1 and later can support this selection feature. Confirm the tool is version 8.7.1 and later.
>
> **Changing the EGT sensor type selection using INSITE Electronic Service Tool:**
>
> 1. Navigate to "Features and Parameters" =\> CM2150E\[1\]\[Secondary 1\] =\> "EGT Sensor Type Selection" and select the EGT sensor type that is installed on the engine. See Figures 1 and 2 below.
>
> Figure 1, EGT Sensor Type Navigation.
>
> Figure 2, Select Appropriate EGT Sensor Type.
>
> **Note · Примечание**
> The “Autodetection” selection logic is **not** currently implemented in the software. If the “Autodetection” selection is made, then Thermistor EGT sensor type will be used for EGT processing.
>
> 2. Select the highlighted “Send to ECM” icon or Right click, select "Send To", "ECM" and select "OK". See Figure 3 below.
>
> Figure 3, Select “Send to ECM”.
>
> 3. Select “OK” to confirm ECM Adjustment. See Figure 4 below.
>
> Figure 4, Confirm ECM Adjustment.
>
> 4. Turn Key Switch to OFF position and select "OK" See Figure 5 below.
>
> Figure 5, Key Switch Off.
>
> 5. Turn Key Switch to ON position and select "OK". See Figure 6 below.
>
> Figure 6, Key Switch On.
>
> 6. Follow the prompt and select "OK". EGT Sensor Type will be successfully saved. See Figure 7 below.
>
> Figure 7, ECM Write Succeeded.
>
> **EGT Sensor Type Monitoring:**
>
> This screen is used to monitor EGT sensor type used by the ECM for EGT input processing.
>
> 1. Navigate to "Data Monitor/Logger" =\> CM2150E\[1\]\[Secondary 1\] =\> "EGT Sensor Type Detected".Click “Log Data” or “Start/Resume” to monitor the EGT Sensor Type Detected and used for EGT processing in the software. See Figure 8 below.
>
> Figure 8, Monitoring EGT Sensor Type Detected.
>
> **Part Identification**
>
> To run the latest software with the EGT sensor selection type functionality, verify the ECM calibrations installed on the engine are listed in the tables below. All ECM calibration codes released prior to this software release will **not** support the EGT sensor selection type functionality.
>
> | Table 1, Software Phase |  |
> |---|---|
> | Engine Platform | Software Phase |
> | QSK50 CM2150 | 25.02.01.20 |
> | QSK50 CM2150 (KOMNET) | 25.02.30.18 |
> | QSK60 CM2150 | 25.02.01.20 |
>
> | Table 2, QSK50 CM2150 |  |  |  |  |  |
> |---|---|---|---|---|---|
> | SC Option | Engine Family | DO Option | FR Option | PP Option | ECM Calibration Code |
> | SC60621 | QSKTA50-CE | DO06765 | FR06734 | PP43379 | AQ60217.28 |
> | SC60623 | QSKTA50-CE | DO06767 | FR06736 | PP43391 | AQ60220.25 |
> | SC60707 | QSKTA50-CE | DO06853 | FR06782 | PP43548 | AQ60287.19 |
> | SC60720 | QSKTA50-CE | DO06866 | FR06790 | PP43548 | AQ60288.19 |
> | SC60724 | QSKTA50-CE | DO06870 | FR06794 | PP43905 | AQ60421.17 |
> | SC60725 | QSKTA50-CE | DO06871 | FR06795 | PP43548 | AQ60289.22 |
> | SC60776 | QSKTA50-CE | DO06928 | FR06734 | PP43379 | AQ60252.21 |
> | SC60823 | QSKTA50-CE | DO06976 | FR06734 | PP43379 | AQ60296.18 |
> | SC60824 | QSKTA50-CE | DO06977 | FR06856 | PP43548 | AQ60292.17 |
> | SC60825 | QSKTA50-CE | DO06978 | FR06857 | PP43391 | AQ60293.16 |
> | SC60826 | QSKTA50-CE | DO06979 | FR06858 | PP43548 | AQ60294.17 |
> | SC60827 | QSKTA50-CE | DO06980 | FR06859 | PP43669 | AQ60297.16 |
> | SC60828 | QSKTA50-CE | DO06981 | FR06860 | PP43669 | AQ60309.20 |
> | SC60829 | QSKTA50-CE | DO06982 | FR06861 | PP43669 | AQ60310.20 |
> | SC60833 | QSKTA50-CE | DO06988 | FR06974 | PP43548 | AQ60301.19 |
> | SC60861 | QSKTA50-CE | DO60018 | FR06734 | PP43379 | AQ60320.19 |
> | SC60869 | QSKTA50-CE | DO60026 | FR06901 | PP43905 | AQ60429.17 |
> | SC60881 | QSKTA50-CE | DO60038 | FR06905 | PP43379 | AQ60401.19 |
> | SC60924 | QSKTA50-CE | DO60081 | FR06736 | PP43391 | AQ60338.22 |
> | SC60987 | QSKTA50-CE | DO60148 | FR06905 | PP43379 | AQ60399.23 |
> | SC61043 | QSKTA50-CE | DO60202 | FR06795 | PP43548 | AQ60417.17 |
> | SC61045 | QSKTA50-CE | DO60204 | FR06975 | PP43379 | AQ60420.15 |
> | SC61056 | QSKTA50-CE | DO60215 | FR06861 | PP43669 | AQ60444.17 |
> | SC61210 | QSKTA50-CE | DO60371 | FR06858 | PP43548 | AQ60458.15 |
> | SC61069 | QSKTA50-CE | DO60228 | FR06990 | PP43976 | AQ60463.16 |
> | SC61070 | QSKTA50-CE | DO60229 | FR06991 | PP43976 | AQ60464.17 |
> | SC61227 | QSKTA50-CE | DO60388 | FR60014 | PP43548 | AQ60989.02 |
> | SC61244 | QSKTA50-CE | DO60405 | FR06734 | PP43379 | AQ60479.16 |
> | SC61245 | QSKTA50-CE | DO60406 | FR06790 | PP43548 | AQ60480.15 |
> | SC61246 | QSKTA50-CE | DO60407 | FR06795 | PP43548 | AQ60481.16 |
> | SC61247 | QSKTA50-CE | DO60408 | FR06736 | PP43391 | AQ60490.19 |
> | SC61248 | QSKTA50-CE | DO60409 | FR06782 | PP43548 | AQ60491.15 |
> | SC61249 | QSKTA50-CE | DO60410 | FR06974 | PP43548 | AQ60492.15 |
> | SC61250 | QSKTA50-CE | DO60411 | FR06794 | PP43905 | AQ60493.16 |
> | SC61255 | QSKTA50-CE | DO60230 | FR06858 | PP43548 | AQ60489.12 |
> | SC61259 | QSKTA50-CE | DO60418 | FR06734 | PP43379 | AQ60484.15 |
> | SC61286 | QSKTA50-CE | DO60445 | FR06794 | PP43905 | AQ60498.16 |
> | SC61287 | QSKTA50-CE | DO60446 | FR06901 | PP43905 | AQ60500.16 |
> | SC61288 | QSKTA50-CE | DO60447 | FR06734 | PP43379 | AQ60504.15 |
> | SC61585 | QSKTA50-CE | DO60747 | FR06734 | PP43379 | AQ60701.13 |
> | SC61687 | QSKTA50-CE | DO60848 | FR60457 | PP43669 | AQ60805.06 |
> | SC61704 | QSKTA50-CE | DO60870 | FR06736 | PP43391 | AQ60756.05 |
> | SC61716 | QSKTA50-CE | DO60882 | FR60048 | PP43548 | AQ60765.08 |
> | SC61719 | QSKTA50-CE | DO60885 | FR60350 | PP43391 | AQ60803.03 |
> | SC61774 | QSKTA50-CE | DO60940 | FR06736 | PP43391 | AQ60769.09 |
> | SC61803 | QSKTA50-CE | DO60969 | FR06860 | PP43669 | AQ60775.07 |
> | SC61804 | QSKTA50-CE | DO60970 | FR06861 | PP43669 | AQ60776.07 |
> | SC61810 | QSKTA50-CE | DO60976 | FR06859 | PP43669 | AQ60800.06 |
> | SC61813 | QSKTA50-CE | DO60979 | FR06794 | PP43905 | AQ60785.06 |
> | SC61814 | QSKTA50-CE | DO60980 | FR06901 | PP43905 | AQ60786.06 |
> | SC61844 | QSKTA50-CE | DO61010 | FR60457 | PP43669 | AQ60796.06 |
> | SC61864 | QSKTA50-CE | DO61028 | FR60457 | PP43669 | AQ60807.07 |
> | SC61878 | QSKTA50-CE | DO61042 | FR06734 | PP43379 | AQ60809.06 |
> | SC61918 | QSKTA50-CE | DO61084 | FR06858 | PP43548 | AQ60889.03 |
> | SC61928 | QSKTA50-CE | DO61094 | FR06790 | PP43548 | AQ60888.03 |
> | SC61929 | QSKTA50-CE | DO61095 | FR60048 | PP43548 | AQ60882.03 |
> | SC61981 | QSKTA50-CE | DO61147 | FR60457 | PP43669 | AQ60874.03 |
> | SC61985 | QSKTA50-CE | DO61160 | FR60522 | PP43669 | AQ60883.03 |
> | SC61993 | QSKTA50-CE | DO61159 | FR60522 | PP43669 | AQ60884.03 |
> | SC62006 | QSKTA50-CE | DO61180 | FR60457 | PP43669 | AQ60892.03 |
> | SC62022 | QSKTA50-CE | DO61182 | FR06794 | PP43905 | AQ60941.03 |
> | SC62023 | QSKTA50-CE | DO61183 | FR06901 | PP43905 | AQ60942.03 |
> | SC62024 | QSKTA50-CE | DO61184 | FR06859 | PP43669 | AQ60939.02 |
> | SC62025 | QSKTA50-CE | DO61185 | FR06859 | PP43669 | AQ60940.02 |
> | SC62030 | QSKTA50-CE | DO61190 | FR06858 | PP43548 | AQ60911.02 |
> | SC62031 | QSKTA50-CE | DO61191 | FR06858 | PP43548 | AQ60912.02 |
> | SC62039 | QSKTA50-CE | DO61199 | FR06856 | PP43548 | AQ60934.02 |
> | SC62040 | QSKTA50-CE | DO61200 | FR06857 | PP43391 | AQ60935.02 |
> | SC62041 | QSKTA50-CE | DO61201 | FR60351 | PP43391 | AQ60936.03 |
> | SC62042 | QSKTA50-CE | DO61202 | FR06858 | PP43548 | AQ60937.02 |
> | SC62043 | QSKTA50-CE | DO61203 | FR06858 | PP43548 | AQ60938.02 |
> | SC62044 | QSKTA50-CE | DO61204 | FR06905 | PP43379 | AQ60901.02 |
> | SC62045 | QSKTA50-CE | DO61205 | FR06905 | PP43379 | AQ60902.03 |
> | SC62046 | QSKTA50-CE | DO61206 | FR06901 | PP43905 | AQ60903.02 |
> | SC62047 | QSKTA50-CE | DO61207 | FR06901 | PP43905 | AQ60904.02 |
> | SC62129 | QSKTA50-CE | DO61306 | FR06901 | PP43905 | AQ60979.01 |
> | SC62130 | QSKTA50-CE | DO61307 | FR06790 | PP43548 | AQ60980.01 |
> | SC60853 | QSKTA50-CE | DO60010 | FR06888 | PP43728 | AQ60359.21 |
> | SC60854 | QSKTA50-CE | DO60011 | FR06889 | PP43728 | AQ60360.19 |
> | SC60855 | QSKTA50-CE | DO60012 | FR06890 | PP43728 | AQ60361.19 |
> | SC60856 | QSKTA50-CE | DO60013 | FR06888 | PP43728 | AQ60362.22 |
> | SC60936 | QSKTA50-CE | DO60096 | FR06890 | PP43728 | AQ60363.21 |
> | SC60937 | QSKTA50-CE | DO60097 | FR06890 | PP43728 | AQ60364.19 |
> | SC60938 | QSKTA50-CE | DO60098 | FR06890 | PP43728 | AQ60365.20 |
> | SC60939 | QSKTA50-CE | DO60099 | FR06888 | PP43728 | AQ60366.19 |
> | SC60940 | QSKTA50-CE | DO60100 | FR06888 | PP43728 | AQ60378.20 |
> | SC60941 | QSKTA50-CE | DO60101 | FR06888 | PP43728 | AQ60379.20 |
> | SC60942 | QSKTA50-CE | DO60102 | FR06888 | PP43728 | AQ60380.19 |
> | SC60943 | QSKTA50-CE | DO60103 | FR06888 | PP43728 | AQ60386.21 |
> | SC60944 | QSKTA50-CE | DO60104 | FR06888 | PP43728 | AQ60381.19 |
> | SC60957 | QSKTA50-CE | DO60118 | FR06888 | PP43728 | AQ60373.21 |
> | SC60958 | QSKTA50-CE | DO60119 | FR06888 | PP43728 | AQ60374.20 |
> | SC60959 | QSKTA50-CE | DO60120 | FR06888 | PP43728 | AQ60375.21 |
> | SC60960 | QSKTA50-CE | DO60121 | FR06888 | PP43728 | AQ60376.18 |
> | SC60961 | QSKTA50-CE | DO60122 | FR06888 | PP43728 | AQ60377.20 |
> | SC60962 | QSKTA50-CE | DO60123 | FR06889 | PP43728 | AQ60367.19 |
> | SC60963 | QSKTA50-CE | DO60124 | FR06889 | PP43728 | AQ60368.19 |
> | SC60964 | QSKTA50-CE | DO60125 | FR06889 | PP43728 | AQ60369.19 |
> | SC60965 | QSKTA50-CE | DO60126 | FR06889 | PP43728 | AQ60370.19 |
> | SC60966 | QSKTA50-CE | DO60127 | FR06889 | PP43728 | AQ60371.19 |
> | SC60967 | QSKTA50-CE | DO60128 | FR06890 | PP43728 | AQ60387.22 |
> | SC60968 | QSKTA50-CE | DO60129 | FR06890 | PP43728 | AQ60388.21 |
> | SC60969 | QSKTA50-CE | DO60130 | FR06890 | PP43728 | AQ60389.19 |
> | SC60970 | QSKTA50-CE | DO60131 | FR06890 | PP43728 | AQ60390.19 |
> | SC60971 | QSKTA50-CE | DO60132 | FR06888 | PP43728 | AQ60395.20 |
> | SC60972 | QSKTA50-CE | DO60133 | FR06890 | PP43728 | AQ60391.21 |
> | SC60973 | QSKTA50-CE | DO60134 | FR06890 | PP43728 | AQ60392.17 |
> | SC60974 | QSKTA50-CE | DO60135 | FR06890 | PP43728 | AQ60402.19 |
> | SC60993 | QSKTA50-CE | DO60154 | FR06888 | PP43728 | AQ60404.20 |
> | SC60996 | QSKTA50-CE | DO60157 | FR06890 | PP43728 | AQ60397.19 |
> | SC61013 | QSKTA50-CE | DO60173 | FR06890 | PP43728 | AQ60410.18 |
> | SC61031 | QSKTA50-CE | DO60191 | FR06889 | PP43728 | AQ60441.18 |
> | SC61035 | QSKTA50-CE | DO60195 | FR06889 | PP43728 | AQ60416.16 |
> | SC61037 | QSKTA50-CE | DO60197 | FR06890 | PP43728 | AQ60442.16 |
> | SC61046 | QSKTA50-CE | DO60205 | FR06890 | PP43728 | AQ60443.22 |
> | SC61055 | QSKTA50-CE | DO60213 | FR06890 | PP43728 | AQ60440.18 |
> | SC61076 | QSKTA50-CE | DO60236 | FR06888 | PP43728 | AQ60445.16 |
> | SC61207 | QSKTA50-CE | DO60368 | FR06888 | PP43728 | AQ60453.19 |
> | SC61208 | QSKTA50-CE | DO60369 | FR06889 | PP43728 | AQ60454.19 |
> | SC61209 | QSKTA50-CE | DO60370 | FR06890 | PP43728 | AQ60455.19 |
> | SC61214 | QSKTA50-CE | DO60375 | FR06890 | PP43728 | AQ60456.17 |
> | SC61216 | QSKTA50-CE | DO60377 | FR06890 | PP43728 | AQ60475.17 |
> | SC61222 | QSKTA50-CE | DO60383 | FR06888 | PP43728 | AQ60476.16 |
> | SC61284 | QSKTA50-CE | DO60443 | FR06890 | PP43728 | AQ60499.16 |
> | SC61468 | QSKTA50-CE | DO60629 | FR06888 | PP43728 | AQ60690.11 |
> | SC61485 | QSKTA50-CE | DO60646 | FR06890 | PP43728 | AQ60694.12 |
> | SC61516 | QSKTA50-CE | DO60677 | FR06890 | PP43728 | AQ60677.13 |
> | SC61550 | QSKTA50-CE | DO60711 | FR06890 | PP43728 | AQ60691.14 |
> | SC61575 | QSKTA50-CE | DO60737 | FR06888 | PP43728 | AQ60695.12 |
> | SC61577 | QSKTA50-CE | DO60739 | FR06888 | PP43728 | AQ60696.12 |
> | SC61579 | QSKTA50-CE | DO60741 | FR06888 | PP43728 | AQ60700.14 |
> | SC61682 | QSKTA50-CE | DO60849 | FR06888 | PP43728 | AQ60751.09 |
> | SC61773 | QSKTA50-CE | DO60939 | FR06888 | PP43728 | AQ60770.07 |
> | SC61783 | QSKTA50-CE | DO60949 | FR06890 | PP43728 | AQ60773.07 |
> | SC61860 | QSKTA50-CE | DO61026 | FR06890 | PP43728 | AQ60811.06 |
> | SC61893 | QSKTA50-CE | DO61059 | FR06890 | PP43728 | AQ60824.05 |
> | SC61900 | QSKTA50-CE | DO61066 | FR06890 | PP43728 | AQ60825.05 |
> | SC61978 | QSKTA50-CE | DO61144 | FR06890 | PP43728 | AQ60876.03 |
> | SC61998 | QSKTA50-CE | DO61165 | FR06889 | PP43728 | AQ60890.03 |
> | SC61999 | QSKTA50-CE | DO61166 | FR06890 | PP43728 | AQ60886.03 |
> | SC62019 | QSKTA50-CE | DO61178 | FR06890 | PP43728 | AQ60891.03 |
>
> | Table 3, QSK60 CM2150 |  |  |  |  |  |
> |---|---|---|---|---|---|
> | SC Option | Engine Family | DO Option | FR Option | PP Option | ECM Calibration Code |
> | SC60620 | QSKTA60-CE | DO06764 | FR06733 | PP43416 | AQ60218.26 |
> | SC60648 | QSKTA60-CE | DO06792 | FR06746 | PP43451 | AQ60221.24 |
> | SC60659 | QSKTA60-CE | DO06803 | FR06751 | PP43416 | AQ60236.23 |
> | SC60660 | QSKTA60-CE | DO06804 | FR06751 | PP43416 | AQ60237.24 |
> | SC60693 | QSKTTA60-CE | DO06839 | FR06773 | PP43501 | AQ60238.23 |
> | SC60706 | QSKTA60-CE | DO06852 | FR06781 | PP43416 | AQ60317.19 |
> | SC60721 | QSKTA60-CE | DO06867 | FR06791 | PP43451 | AQ60337.19 |
> | SC60722 | QSKTA60-CE | DO06868 | FR06792 | PP43451 | AQ60302.18 |
> | SC60723 | QSKTA60-CE | DO06869 | FR06793 | PP43451 | AQ60305.23 |
> | SC60726 | QSKTA60-CE | DO06872 | FR06796 | PP43451 | AQ60303.25 |
> | SC60777 | QSKTA60-CE | DO06929 | FR06746 | PP43451 | AQ60253.24 |
> | SC60779 | QSKTA60-CE | DO06931 | FR06829 | PP43378 | AQ60255.17 |
> | SC60780 | QSKTA60-CE | DO06932 | FR06830 | PP43378 | AQ60285.16 |
> | SC60781 | QSKTA60-CE | DO06933 | FR06831 | PP43451 | AQ60254.27 |
> | SC60822 | QSKTA60-CE | DO06975 | FR06746 | PP43451 | AQ60295.15 |
> | SC60834 | QSKTA60-CE | DO06989 | FR06792 | PP43451 | AQ60304.21 |
> | SC60842 | QSKTA60-CE | DO06997 | FR06781 | PP43416 | AQ60318.15 |
> | SC60846 | QSKTA60-CE | DO60002 | FR06792 | PP43451 | AQ60314.19 |
> | SC60847 | QSKTA60-CE | DO60003 | FR06751 | PP43416 | AQ60312.18 |
> | SC60848 | QSKTA60-CE | DO60004 | FR06733 | PP43416 | AQ60313.17 |
> | SC60849 | QSKTA60-CE | DO60005 | FR06792 | PP43451 | AQ60315.17 |
> | SC60850 | QSKTA60-CE | DO60006 | FR06792 | PP43451 | AQ60316.18 |
> | SC60863 | QSKTA60-CE | DO60020 | FR06895 | PP43451 | AQ60326.21 |
> | SC60864 | QSKTA60-CE | DO60021 | FR06896 | PP43451 | AQ60327.23 |
> | SC60865 | QSKTA60-CE | DO60022 | FR06897 | PP43416 | AQ60328.26 |
> | SC60866 | QSKTA60-CE | DO60023 | FR06898 | PP43451 | AQ60329.22 |
> | SC60867 | QSKTA60-CE | DO60024 | FR06899 | PP43416 | AQ60330.19 |
> | SC60868 | QSKTA60-CE | DO60025 | FR06900 | PP43451 | AQ60451.14 |
> | SC60880 | QSKTA60-CE | DO60037 | FR06895 | PP43451 | AQ60325.17 |
> | SC60882 | QSKTA60-CE | DO60039 | FR06906 | PP43451 | AQ60331.18 |
> | SC60883 | QSKTA60-CE | DO60040 | FR06907 | PP43451 | AQ60341.22 |
> | SC60885 | QSKTA60-CE | DO60042 | FR06908 | PP43451 | AQ60342.19 |
> | SC60891 | QSKTA60-CE | DO60048 | FR06898 | PP43451 | AQ60335.17 |
> | SC60911 | QSKTA60-CE | DO60068 | FR06863 | PP43451 | AQ60343.18 |
> | SC60912 | QSKTA60-CE | DO60069 | FR06864 | PP43451 | AQ60344.16 |
> | SC60913 | QSKTA60-CE | DO60070 | FR06865 | PP43451 | AQ60345.16 |
> | SC60951 | QSKTA60-CE | DO60111 | FR06746 | PP43451 | AQ60352.18 |
> | SC60986 | QSKTTA60-CE | DO60147 | FR06938 | PP43501 | AQ60398.20 |
> | SC61014 | QSKTA60-CE | DO60174 | FR06866 | PP43451 | AQ60412.13 |
> | SC61015 | QSKTA60-CE | DO60175 | FR06867 | PP43451 | AQ60413.14 |
> | SC61039 | QSKTTA60-CE | DO60198 | FR06773 | PP43501 | AQ60415.14 |
> | SC61040 | QSKTTA60-CE | DO60199 | FR06938 | PP43501 | AQ60433.14 |
> | SC61044 | QSKTA60-CE | DO60203 | FR06831 | PP43451 | AQ60431.16 |
> | SC61073 | QSKTA60-CE | DO60233 | FR06863 | PP43451 | AQ60446.19 |
> | SC61224 | QSKTA60-CE | DO60385 | FR06906 | PP43451 | AQ60477.13 |
> | SC61254 | QSKTA60-CE | DO60227 | FR06746 | PP43451 | AQ60482.14 |
> | SC61264 | QSKTA60-CE | DO60423 | FR06831 | PP43451 | AQ60509.16 |
> | SC61265 | QSKTA60-CE | DO60424 | FR06781 | PP43416 | AQ60510.13 |
> | SC61266 | QSKTTA60-CE | DO60425 | FR06773 | PP43501 | AQ60511.16 |
> | SC61267 | QSKTA60-CE | DO60426 | FR06796 | PP43451 | AQ60512.16 |
> | SC61268 | QSKTA60-CE | DO60427 | FR06792 | PP43451 | AQ60506.13 |
> | SC61269 | QSKTA60-CE | DO60428 | FR06733 | PP43416 | AQ60507.13 |
> | SC61270 | QSKTA60-CE | DO60429 | FR06906 | PP43451 | AQ60508.14 |
> | SC61272 | QSKTA60-CE | DO60431 | FR06751 | PP43416 | AQ60501.14 |
> | SC61273 | QSKTA60-CE | DO60432 | FR06791 | PP43451 | AQ60502.13 |
> | SC61274 | QSKTA60-CE | DO60433 | FR06793 | PP43451 | AQ60503.13 |
> | SC61279 | QSKTA60-CE | DO60438 | FR60369 | PP43451 | AQ60793.05 |
> | SC61315 | QSKTA60-CE | DO60475 | FR06751 | PP43416 | AQ60528.13 |
> | SC61318 | QSKTA60-CE | DO60478 | FR06746 | PP43451 | AQ60530.13 |
> | SC61319 | QSKTA60-CE | DO60479 | FR06898 | PP43451 | AQ60531.13 |
> | SC61323 | QSKTA60-CE | DO60843 | FR60088 | PP43416 | AQ60534.10 |
> | SC61514 | QSKTA60-CE | DO60884 | FR06898 | PP43451 | AQ60759.10 |
> | SC61595 | QSKTA60-CE | DO60760 | FR06791 | PP43451 | AQ60717.11 |
> | SC61596 | QSKTA60-CE | DO60761 | FR06908 | PP43451 | AQ60716.11 |
> | SC61612 | QSKTTA60-CE | DO60775 | FR06773 | PP43501 | AQ60724.11 |
> | SC61664 | QSKTA60-CE | DO60827 | FR60323 | PP43416 | AQ60748.09 |
> | SC61665 | QSKTA60-CE | DO60828 | FR60323 | PP43416 | AQ60749.10 |
> | SC61673 | QSKTA60-CE | DO60836 | FR06897 | PP43416 | AQ60750.15 |
> | SC61710 | QSKTA60-CE | DO60876 | FR06751 | PP43416 | AQ60761.12 |
> | SC61711 | QSKTTA60-CE | DO60877 | FR06773 | PP43501 | AQ60762.10 |
> | SC61712 | QSKTTA60-CE | DO60878 | FR06938 | PP43501 | AQ60763.10 |
> | SC61764 | QSKTA60-CE | DO60930 | FR60407 | PP43416 | AQ60801.05 |
> | SC61765 | QSKTA60-CE | DO60931 | FR60408 | PP43416 | AQ60804.05 |
> | SC61794 | QSKTA60-CE | DO60960 | FR60429 | PP44768 | AQ60789.06 |
> | SC61795 | QSKTTA60-CE | DO60961 | FR60444 | PP44828 | AQ60792.06 |
> | SC61796 | QSKTA60-CE | DO60962 | FR60431 | PP44768 | AQ60790.06 |
> | SC61805 | QSKTA60-CE | DO60971 | FR06867 | PP43451 | AQ60777.05 |
> | SC61806 | QSKTA60-CE | DO60972 | FR06865 | PP43451 | AQ60778.06 |
> | SC61807 | QSKTA60-CE | DO60973 | FR06864 | PP43451 | AQ60779.06 |
> | SC61808 | QSKTA60-CE | DO60974 | FR06863 | PP43451 | AQ60780.06 |
> | SC61809 | QSKTA60-CE | DO60975 | FR06866 | PP43451 | AQ60781.05 |
> | SC61819 | QSKTA60-CE | DO60985 | FR60430 | PP44768 | AQ60791.06 |
> | SC61848 | QSKTA60-CE | DO61014 | FR06746 | PP43451 | AQ60799.04 |
> | SC61858 | QSKTA60-CE | DO61025 | FR06906 | PP43451 | AQ60808.05 |
> | SC61894 | QSKTA60-CE | DO61060 | FR06796 | PP43451 | AQ60946.02 |
> | SC61913 | QSKTTA60-CE | DO61079 | FR60444 | PP44828 | AQ60881.03 |
> | SC61914 | QSKTA60-CE | DO61080 | FR06896 | PP43451 | AQ60947.02 |
> | SC61980 | QSKTA60-CE | DO61146 | FR06733 | PP43416 | AQ60879.03 |
> | SC61987 | QSKTA60-CE | DO61152 | FR06746 | PP43451 | AQ60880.03 |
> | SC61989 | QSKTA60-CE | DO61155 | FR06831 | PP43451 | AQ60877.03 |
> | SC61996 | QSKTA60-CE | DO61163 | FR06830 | PP43378 | AQ60949.01 |
> | SC61997 | QSKTA60-CE | DO61164 | FR06896 | PP43451 | AQ60948.01 |
> | SC62032 | QSKTA60-CE | DO61192 | FR06896 | PP43451 | AQ60913.03 |
> | SC62048 | QSKTA60-CE | DO61208 | FR06830 | PP43378 | AQ60915.02 |
> | SC62049 | QSKTA60-CE | DO61209 | FR06895 | PP43451 | AQ60916.02 |
> | SC62050 | QSKTA60-CE | DO61210 | FR06895 | PP43451 | AQ60917.02 |
> | SC62051 | QSKTA60-CE | DO61211 | FR06897 | PP43416 | AQ60918.04 |
> | SC62052 | QSKTA60-CE | DO61212 | FR06897 | PP43416 | AQ60919.03 |
> | SC62053 | QSKTA60-CE | DO61213 | FR06907 | PP43451 | AQ60920.02 |
> | SC62054 | QSKTA60-CE | DO61214 | FR06898 | PP43451 | AQ60921.03 |
> | SC62055 | QSKTA60-CE | DO61215 | FR06898 | PP43451 | AQ60922.02 |
> | SC62056 | QSKTA60-CE | DO61216 | FR06898 | PP43451 | AQ60923.02 |
> | SC62057 | QSKTA60-CE | DO61217 | FR06898 | PP43451 | AQ60924.03 |
> | SC62058 | QSKTA60-CE | DO61218 | FR06908 | PP43451 | AQ60925.03 |
> | SC62059 | QSKTA60-CE | DO61219 | FR06908 | PP43451 | AQ60926.02 |
> | SC62060 | QSKTA60-CE | DO61220 | FR06899 | PP43416 | AQ60927.02 |
> | SC62061 | QSKTA60-CE | DO61221 | FR06900 | PP43451 | AQ60928.02 |
> | SC62062 | QSKTTA60-CE | DO61222 | FR06938 | PP43501 | AQ60929.02 |
> | SC62063 | QSKTTA60-CE | DO61223 | FR06938 | PP43501 | AQ60930.03 |
> | SC62064 | QSKTA60-CE | DO61224 | FR60323 | PP43416 | AQ60931.03 |
> | SC62065 | QSKTA60-CE | DO61225 | FR60323 | PP43416 | AQ60932.03 |
> | SC62066 | QSKTA60-CE | DO61226 | FR60408 | PP43416 | AQ60933.02 |
> | SC62082 | QSKTA60-CE | DO61244 | FR06831 | PP43451 | AQ60914.02 |
> | SC62131 | QSKTA60-CE | DO61308 | FR06792 | PP43451 | AQ60981.01 |
> | SC62132 | QSKTA60-CE | DO61309 | FR06791 | PP43451 | AQ60982.01 |
> | SC62133 | QSKTA60-CE | DO61310 | FR06796 | PP43451 | AQ60983.01 |
> | SC62163 | QSKTTA60-CE | DO61337 | FR06773 | PP43501 | AQ60994.01 |
> | SC62164 | QSKTA60-CE | DO61338 | FR06831 | PP43451 | AQ60995.01 |
>
> ### Document History
