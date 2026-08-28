---
type: "TSB"
doc: "tsb130142"
title_en: "CENSE™ CM530 Obsoleted and Replaced by Next Generation CENSE™ CM2330"
modified: "2018-10-16"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
parts:
  - "4323412"
  - "4326926"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2013/tsb130142.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb130142.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QSK60"
  - "перевод/машинный"
---

# CENSE™ CM530 Obsoleted and Replaced by Next Generation CENSE™ CM2330

> [!abstract] TSB · `tsb130142`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Даты:** изменён 2018-10-16
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2013/tsb130142.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb130142.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## CENSETM CM530, вышедший из эксплуатации и замененный CENSETM CM2330 следующего поколения

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### Содержание

В документе сообщается, что модуль CENSETM CM530 устареет в сентябре 2013 года. Модуль CENSETM CM2330 следующего поколения заменит существующий CENSETM.

Калибровки для модуля CENSETM CM2330 следующего поколения будут доступны через QuickServe Online и INCALTM CD. История калибровки ECM для продукта CM2330 также будет доступна через QSOL. Полный список старых vs. Новые варианты EI и коды модуля управления двигателем (ECM) для платформ двигателей на дизельном топливе и природном газе можно найти ближе к концу этой связи.

Модуль CENSETM CM2330 следующего поколения будет поддерживаться электронным сервисным оборудованием INSITETM CENSETM. Полевой персонал должен использовать базовый инструмент для электронного обслуживания INSITETM (версия 7.6.2 или выше) для связи с любым двигателем, оснащенным новым модулем CENSETM CM2330. TSB был опубликован, чтобы показать, как можно собирать расширенные данные ECM через INSITETM. Журналы трендов, журналы защиты двигателя, журналы расширенных снимков ошибок и журналы запуска-остановки должны загружаться каждый раз, когда собирается рабочий заказ. Ссылка [[tsb130149 — Next Generation CENSE™ CM2330 - INSITE™ Electronic Service Tool, Image Trend Log Co\|TSB130149]] для получения дополнительной информации.

Модуль CENSETM CM2330 следующего поколения не требует регулярного удаления журналов трендов. После того, как он достигнет полной емкости, новый модуль начнет создавать пространство для новых данных, удаляя самые старые точки данных в памяти.

В следующем поколении CENSETM CM2330 будет семнадцать новых кодов неисправностей. Они заменят существующие коды ошибок CM530. Все оборудование заказчика, собирающее информацию о коде неисправности из модуля CENSETM**, должно** обновлять свой список, чтобы отразить эти изменения. Ссылка [[tsb130148 — Next Generation CENSE™ Fault Code List Changes\|TSB130148]] для получения дополнительной информации.

Также был выпущен новый загрузочный кабель ROM для модуля CENSETM CM2330 следующего поколения, который доступен для использования на местах. Номер детали этого инструмента можно найти в сводной таблице ниже.

Переход на CENSETM CM2330 следующего поколения приведет к потере поддержки интерфейсов RS422 и RS232. Любое оборудование, используемое производителем оригинального оборудования (OEM) или клиентом, использующим эти интерфейсы, должно быть обновлено до оборудования, совместимого с J1939.

В рамках перехода на новый модуль CENSETM CM2330 была принята стандартная система нумерации для датчиков температуры выхлопных газов (EGT), температуры впускного коллектора (IMT) и давления впускного коллектора (IMP). Подробный старый vs. Новая информация будет показана в конце этого сообщения.

Хотя все двигатели, которые в настоящее время находятся в эксплуатации, в конечном итоге будут оснащены модулем CENSETM CM2330 следующего поколения, в конце этого сообщения можно найти информацию о серийном номере двигателя (ESN) для двигателей QSK / QSV / KV, оснащенных новым модулем. Все последующие ESN будут оснащены CENSETM CM2330 следующего поколения.

> [!note] Примечание
> Чтобы избежать путаницы в этой области и ложных некоммуникационных проблем, Cummins Inc. Рекомендуется удалить все точки соединения RS232 из кабины двигателя и/или грузовика, как только будет установлен CENSETM CM2330 следующего поколения.

> [!note] Примечание
> После модернизации до модуля CENSETM CM2330 следующего поколения персонал на местах может не иметь возможности связаться с новым модулем из кабины, если порт J1939 уже установлен в кабине. Чтобы поддерживать связь с модулем CENSETM CM2330 из кабины, убедитесь, что соединение шины данных J1939 CAN из ремня электропроводки двигателя правильно расширено. Свяжитесь с местным инженером-прикладником для получения инструкций по расширению соединения.

| Устаревшие номера частей |  |
|---|---|
| Название части | Номер детали |
| Электронный блок управления двигателем | 3098771 |
| K38 Моторная проводка жгут | 3643114 |
| K38 Моторная проводка жгут | 3643115 |
| К50 Моторная проводка жгут | 3644538 |
| К50 Моторная проводка жгут | 3644539 |

| Новые номера частей |  |
|---|---|
| Название части | Номер детали |
| Электронный блок управления двигателем | [[4326926]] |
| K38 Моторная проводка жгут | 4328451 |
| К50 Моторная проводка жгут | 4323226 |
| J1939 Upfit Jumper Wiring Grupp (англ.)русск. | 4328522 |
| 9-Pin Service Connector L-Bracket | 3649861 |
| CM2330 ROM Boot Cable (Кабель для загрузки) | 5298707 |

| Платформа | Старый код ECM | Новый код ECM | Старый номер файла | Новый номер файла | FR Вариант | Примечание |
|---|---|---|---|---|---|---|
| NTC-400 | G10002 | Не применяется | 4922482 | Не применяется | FR01288 | Устаревший |
| QST30 | G50043 | EP80004 | 4998247 | 4328553 | FR05134 |  |
| QST30 | G50041 | EP80008 | 3092440 | 4308662 | FR05150 |  |
| QST30 | G50034 | EP80001 | 3092882 | 4328554 | FR05151 |  |
| QST30 |  | EP80005 |  | 4308655 | FR05144 |  |
| QST30 | G50031 | EP80006 | 3092208 | 4328555 | FR05227 |  |
| QST30 | G50037 | Не применяется | 4068125 | 4328556 | FR05232 | Устаревший |
| QST30 | G50042 | EP80003 | 4295355 | 4328557 | FR05233 |  |
| К50 | G60082 | EP60024 | 3099310 | 4328558 | FR06075 |  |
| К50 | G60320 | EP60051.00 | 3098393 | 4335183 | FR06097 |  |
| К50 | G60321 | Не применяется | 3098392 | FR06097 | Устаревший |  |
| K38 | G60322 | EP60023 | 3098997 | 4328559 | FR06101 | Устаревший |
| K38 | G60083 | EP60023 | 3099305 | FR06101 |  |  |
| K38 | G60342 | EP60036 | 2873437 | 4335184 | FR06142 |  |
| К50 | G60001 | EP60037 | 3098391 | 4335185 | FR06145 |  |
| К50 | G60323 | EP60037 | 3098390 | FR06145 | Устаревший |  |
| К50 | G60349 | EP60037 | 3099306 | FR06145 | Устаревший |  |
| К50 | G60242 | EP60037 | 3099496 | FR06145 | Устаревший |  |
| К50 | G60338 | EP60037 | 4971018 | FR06145 | Устаревший |  |
| К50 | G60014 | EP60027 | 3099081 | 4328560 | FR06147 | Устаревший |
| К50 | G60300 | EP60027 | 3099309 | FR06147 |  |  |
| К50 | G60334 | EP60028 | 4968511 | 4328561 | FR06202 |  |
| К50 | G60324 | EP60029 | 3098731 | 4328562 | FR06215 | Устаревший |
| К50 | G60087 | EP60029 | 3099311 | FR06215 |  |  |
| K38 | G60088 | EP60030 | 3099304 | 4328563 | FR06233 |  |
| К50 | G60004 | EP60038 | 3098737 | 4335186 | FR06237 | Устаревший |
| К50 | G60333 | EP60038 | 3099308 | FR06237 |  |  |
| QSK45 | G60304 | EP60010 | 4065692 | 4328564 | FR06268 |  |
| К50 | G60305 | EP60031 | 3098779 | 4328565 | FR06276 | Устаревший |
| К50 | G60301 | EP60031 | 3099307 | FR06276 |  |  |
| QSK45 | G60307 | EP60044 | 4065694 | 4357403 | FR06289 |  |
| QSK45 | G60329 | EP60002 | 3636700 | 4328566 | FR06289 |  |
| QSK45 | G60308 | EP60045 | 4065691 | 4357404 | FR06291 |  |
| QSK45 | G60309 | EP60003 | 4080316 | 4328567 | FR06291 |  |
| QSK78 | G60327 | EP60020 | 4080432 | 4328568 | FR06302 |  |
| QSK78 | G60330 | EP60020 | 3637688 | FR06302 | Устаревший |  |
| QSK45 | G60310 | EP60004 | 4065693 | 4328570 | FR06305 |  |
| QSK60 | G60098 | EP60011 | 4016601 | 4328571 | FR06325 |  |
| QSK60 | G60225 | EP60012 | 4016600 | 4328572 | FR06327 |  |
| QSK60 | G60099 | EP60046 | 4080312 | 4357405 | FR06329 |  |
| QSK60 | G60100 | EP60046 | 4080311 | FR06329 | Устаревший |  |
| QSK60 | G60101 | EP60039 | 4080313 | 4335187 | FR06329 |  |
| QSK60 | G60129 | EP60013 | 4086033 | 4328573 | FR06330 |  |
| QSK60 | G60102 | EP60014 | 4086351 | 4328574 | FR06331 | Устаревший |
| QSK60 | G60178 | EP60014 | FR06331 |  |  |  |
| QSK60 | G60254 | EP60015 | 4080314 | 4328575 | FR06339 | Устаревший |
| QSK60 | G60255 | EP60015 | 4080308 | FR06339 | Устаревший |  |
| QSK60 | G60256 | EP60015 | 4065680 | FR06339 |  |  |
| QSK60 | G60257 | EP60015 | 4080310 | FR06339 | Устаревший |  |
| QSK60 | G60233 | EP60015 | 4100583 | FR06339 | Устаревший |  |
| QSK60 | G60296 | EP60016 | 4080318 | 4328576 | FR06340 | Устаревший |
| QSK60 | G60297 | EP60016 | 4080319 | FR06340 | Устаревший |  |
| QSK60 | G60298 | EP60016 | 4065696 | FR06340 |  |  |
| QSK60 | G60260 | EP60016 |  | FR06340 | Устаревший |  |
| QSK60 | G60325 | EP60016 | 4101155 | FR06340 | Устаревший |  |
| QSK60 | G60245 | EP60017 | 4065687 | 4328577 | FR06359 |  |
| K38 | G60339 | EP60047 | 2866989 | 4357406 | FR06367 |  |
| K38 | G60350 | EP60047 | 3637829 | FR06367 | Устаревший |  |
| К50 | G60340 | EP60040 | 2866990 | 4335188 | FR06367 |  |
| QSK60 | G60289 | EP60041 | 4065688 | 4335189 | FR06378 |  |
| QSK60 | G60292 | EP60018 | 4101145 | 4328578 | FR06378 | Устаревший |
| QSK60 | G60331 | EP60018 | 3637682 | FR06378 |  |  |
| QSK60 | G60312 | EP60042 | 4080315 | 4335190 | FR06379 |  |
| QSK60 | G60314 | EP60019 | 4065681 | 4328579 | FR06379 |  |
| К50 | G60299 | EP60032 | 3099306 | 4328580 | FR06389 |  |
| К50 | G60337 | EP60032 | 4971017 | FR06389 | Устаревший |  |
| QSK45 | G60140 | EP60005 | 4085912 | 4328581 | FR06404 |  |
| QSK45 | G60142 | EP60048 | 4085914 | 4357407 | FR06406 |  |
| QSK45 | G60143 | EP60006 | 4085915 | 4328582 | FR06406 |  |
| К50 | G60345 | EP60033 | 2896429 | 4328583 | FR06426 |  |
| QSK45 | G60336 | EP60009 | 4101300 | 4328584 | FR06443 |  |
| QSK60 | G60227 | EP60043 | 4016521 | 4335191 | FR06458 |  |
| QSK60 | G60130 | EP60001.01 | 4065689 | [[4323412]] | FR06554 |  |
| QSK45 | G60302 | EP60049 | 4065695 | 4357408 | FR06640 |  |
| QSK60 | G60123 | EP60025 | 4085921 | 4328586 | FR06687 |  |
| QSK78 | G60328 | EP60022 | 4101100 | 4328587 | FR06704 |  |
| QSK45 | G60341 | EP60007 | 3635475 | 4328588 | FR06707 |  |
| QSK60 | G60335 | EP60026 | 3636051 | 4328589 | FR06714 |  |
| QSK78 | G60344 | EP60021 | 2886091 | 4328569 | FR06725 |  |
| K38 | G60332 | EP60034 | 3637829 | 4328590 | FR06819 |  |
| QSK45 | G60311 | EP60008 | 4065690 | 4328591 | FR06979 |  |
| QST30 |  | EP80007 | 4067824 | 4328592 |  |  |
| К50 | G60348 | EP60035 | 3099306 | 4335177 | FR06356 |  |
| QSK60 - Газ |  | EP60050 |  |  | FR6056 |  |
| QSK60 - Газ |  | EP60050 |  |  | FR6587 |  |
| QSK60 - Газ |  | EP60050 |  |  | FR6802 |  |
| QSK60 - Газ |  | EP60050 |  |  | FR6803 |  |
| QSK60 - Газ |  | EP60050 |  |  | FR6804 |  |
| QSK60 - Газ |  | EP60050 |  |  | FR6805 |  |
| QSK60 - Газ |  | EP60050 |  |  | FR6806 |  |
| QSK60 - Газ |  | EP60050 |  |  | FR6911 |  |
| QSK60 - Газ |  | EP60050 |  |  | FR6912 |  |
| Фаза 1 QSV91 |  | EP80010 |  |  | FR7309 |  |
| Фаза 1 QSV91 |  | EP80010 |  |  | FR7310 |  |
| Фаза 1 QSV91 |  | EP80010 |  |  | FR7311 |  |
| Фаза 1 QSV91 |  | EP80010 |  |  | FR7312 |  |
| Фаза 1 QSV91 |  | EP80010 |  |  | FR7313 |  |
| Фаза 1 QSV91 |  | EP80010 |  |  | FR7314 |  |
| Фаза 1 QSV91 |  | EP80010 |  |  | FR7315 |  |
| Фаза 1 QSV91 |  | EP80010 |  |  | FR7316 |  |
| Фаза 1 QSV91 |  | EP80010 |  |  | FR7317 |  |
| Фаза 1 QSV91 |  | EP80010 |  |  | FR7318 |  |
| Фаза 1 QSV91 |  | EP80010 |  |  | FR7319 |  |
| Фаза 1 QSV91 |  | EP80010 |  |  | FR7320 |  |
| Фаза 1 QSV91 |  | EP80010 |  |  | FR7321 |  |
| Фаза 1 QSV91 |  | EP80010 |  |  | FR7322 |  |
| Фаза 1 QSV91 |  | EP80010 |  |  | FR7323 |  |
| Фаза 1 QSV91 |  | EP80010 |  |  | FR7324 |  |
| Фаза 1 QSV91 |  | EP80010 |  |  | FR7325 |  |
| Фаза 1 QSV91 |  | EP80010 |  |  | FR7385 |  |
| Фаза 2 QSV91 |  | EP80009 |  |  | FR07276 |  |
| Фаза 2 QSV91 |  | EP80009 |  |  | FR07281 |  |
| Фаза 2 QSV91 |  | EP80009 |  |  | FR07296 |  |
| Фаза 2 QSV91 |  | EP80009 |  |  | FR07297 |  |
| Фаза 2 QSV91 |  | EP80009 |  |  | FR07303 |  |
| Фаза 2 QSV91 |  | EP80009 |  |  | FR07306 |  |
| Фаза 2 QSV91 |  | EP80009 |  |  | FR07328 |  |
| Фаза 2 QSV91 |  | EP80009 |  |  | FR07329 |  |
| Фаза 2 QSV91 |  | EP80009 |  |  | FR07332 |  |
| Фаза 2 QSV91 |  | EP80009 |  |  | FR07335 |  |
| Фаза 2 QSV91 |  | EP80009 |  |  | FR07336 |  |
| Фаза 2 QSV91 |  | EP80009 |  |  | FR07339 |  |
| Фаза 2 QSV91 |  | EP80009 |  |  | FR07340 |  |
| Фаза 2 QSV91 |  | EP80009 |  |  | FR07343 |  |
| Фаза 2 QSV91 |  | EP80009 |  |  | FR07344 |  |
| Фаза 2 QSV91 |  | EP80009 |  |  | FR07347 |  |
| Фаза 2 QSV91 |  | EP80009 |  |  | FR07348 |  |
| Фаза 2 QSV91 |  | EP80009 |  |  | FR07349 |  |
| Фаза 2 QSV91 |  | EP80009 |  |  | FR07350 |  |
| Фаза 2 QSV91 |  | EP80009 |  |  | FR07351 |  |
| Фаза 2 QSV91 |  | EP80009 |  |  | FR07352 |  |
| Фаза 2 QSV91 |  | EP80009 |  |  | FR07355 |  |
| Фаза 2 QSV91 |  | EP80009 |  |  | FR07356 |  |
| Фаза 2 QSV91 |  | EP80009 |  |  | FR07359 |  |
| Фаза 2 QSV91 |  | EP80009 |  |  | FR07360 |  |
| Фаза 2 QSV91 |  | EP80009 |  |  | FR07361 |  |
| Фаза 2 QSV91 |  | EP80009 |  |  | FR07362 |  |
| Фаза 2 QSV91 |  | EP80009 |  |  | FR07377 |  |
| Фаза 2 QSV91 |  | EP80009 |  |  | FR07378 |  |
| QSK38 - Газ |  | EP60052 |  |  | FR6691 |  |
| QSV91 TVAB |  | EP80011 |  |  | FR7257 |  |

| Старая нумерация CENSETM для датчиков температуры выхлопных газов (EGT) | Новая нумерация CENSETM CM2330 для датчиков температуры выхлопных газов (EGT) |
|---|---|
| Цилиндр № 1 Левый берег | Цилиндр № 1 (А1) |
| Цилиндр No1 Правый Банк | Цилиндровый номер 2 (В1) |
| Цилиндр номер 2 Левый берег | Цилиндровый номер 3 (А2) |
| Цилиндр No2 Правый берег | Цилиндровый номер 4 (В2) |
| Цилиндр № 3 Левый берег | Цилиндровый номер 5 (А3) |
| Цилиндр № 3 Правый берег | Цилиндр № 6 (В3) |
| Цилиндр № 4 Левый берег | Цилиндр № 7 (А4) |
| Цилиндр № 4 Правый берег | Цилиндр № 8 (В4) |
| Цилиндр № 5 Левый берег | Цилиндр № 9 (А5) |
| Цилиндр № 5 Правый берег | Цилиндр № 10 (B5) |
| Цилиндр номер 6 Левый берег | Цилиндровый номер 11 (А6) |
| Цилиндр № 6 Правый берег | Цилиндр № 12 (В6) |
| Цилиндр № 7 Левый берег | Цилиндр № 13 (А7) |
| Цилиндр № 7 Правый берег | Цилиндр № 14 (B7) |
| Цилиндр № 8 Левый берег | Цилиндр № 15 (А8) |
| Цилиндр № 8 Правый берег | Цилиндр № 16 (B8) |
| Цилиндр № 9 Левый берег | Цилиндр № 17 (А9) |
| Цилиндр № 9 Правый берег | Цилиндр № 18 (B9) |

| K38, K50 только двигатели |  |  |
|---|---|---|
| CENSETM CM530 для датчиков температуры впускного коллектора (IMT) | Новая нумерация CENSETM CM2330 для датчиков температуры коллектора впуска (IMT) | Код ошибки в новом CM2330 |
| Левобережье Фронт Взятие Многообразная Температура | Температура воздуха в коллекторе \#1 | 154 |
| Right Bank Front - температура коллектора | Температура воздуха в коллекторе \#3 | 161 |
| Температура заднего входа левого берега | Температура воздуха в коллекторе \#2 | 157 |
| Температура заднего входа в правом банке | Температура воздуха в коллекторе \#4 | 164 |

| QSK45 и QSK60 только для двигателей |  |  |
|---|---|---|
| CENSETM CM530 для датчиков температуры впускного коллектора (IMT) | Новая нумерация CENSETM CM2330 для датчиков температуры коллектора впуска (IMT) | Код ошибки в новом CM2330 |
| Левобережье Фронт Взятие Многообразная Температура | Температура воздуха в коллекторе \#1 | Удаленная (CM500) |
| Right Bank Front - температура коллектора | Температура воздуха в коллекторе \#3 | 161 |
| Температура заднего входа левого берега | Температура воздуха в коллекторе \#2 | 157 |
| Температура заднего входа в правом банке | Температура воздуха в коллекторе \#4 | 164 |

| Только двигатели QSK78 |  |  |
|---|---|---|
| CENSETM CM530 для датчиков температуры впускного коллектора (IMT) | Новая нумерация CENSETM CM2330 для датчиков температуры коллектора впуска (IMT) | Код ошибки в новом CM2330 |
| Левобережье Фронт Взятие Многообразная Температура | Температура воздуха в коллекторе \#1 | Удаленная (CM500) |
| Right Bank Front - температура коллектора | Температура воздуха в коллекторе \#3 | 161 |
| Средний уровень потребления левобережья | Температура воздуха в коллекторе \#5 | 2243 |
| Средняя температура в среднем потреблении Right Bank | Температура воздуха в коллекторе \#6 | 2247 |
| Температура заднего входа левого берега | Температура воздуха в коллекторе \#2 | 157 |
| Температура заднего входа в правом банке | Температура воздуха в коллекторе \#4 | 164 |

| Старая нумерация CENSETM для датчиков давления впускного коллектора (IMP) | CENSETM CM2330 Номер для датчиков давления впускного коллектора (IMP) |
|---|---|
| Левый берег под давлением многообразия | Давление в коллекторе \#1 |
| Правый банк подвергается многообразному давлению | Давление в коллекторе \#2 |

| Платформа | ESN First |
|---|---|
| QSK78 HPI | 66302969 |
| QSK60 HPI | 33199842 |
| К50 | 33199574 |
| QSK60 - Газ | 33199692 |
| QSV91 - Газ | 66302996 |

### История изменений документа

## Детали, упомянутые в документе

| Артикул | Наименование | Русское название |
|---|---|---|
| [[4323412]] | CALIBRATION SOFTWARE |  |
| [[4326926]] | ELECTRONIC CONTROL MODULE | Электронный блок управления |

> [!quote]- Original (English) · английский оригинал
> ## CENSE™ CM530 Obsoleted and Replaced by Next Generation CENSE™ CM2330
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Contents
>
> This document announces that the CENSE™ CM530 module will be obsoleted in September 2013. The Next Generation CENSE™ CM2330 module will be superseding the existing CENSE™.
>
> Calibrations for the Next Generation CENSE™ CM2330 module will be available through QuickServe™ Online and the INCAL™ CD. ECM Calibration Revision History for the CM2330 product will also be available through QSOL. A full list of old vs. new EI options and engine control module (ECM) codes for diesel and natural gas engine platforms can be found toward the end of this communication.
>
> The Next Generation CENSE™ CM2330 module will **not** be supported by the INSITE™ CENSE™ electronic service tool. Field personnel **must** use base INSITE™ electronic service tool (Version 7.6.2 or higher) to communicate with any engine equipped with the new CENSE™ CM2330 module. A TSB has been published to show how advanced ECM data can be collected via INSITE™. Trend logs, Engine Protection logs, Enhanced Fault Snapshot logs, and Start-Stop logs should be downloaded every time a work order is collected. Reference [[tsb130149 — Next Generation CENSE™ CM2330 - INSITE™ Electronic Service Tool, Image Trend Log Co\|TSB130149]] for more information.
>
> The Next Generation CENSE™ CM2330 module does **not** require the trend logs to be cleared out regularly. Once it has reached full capacity, the new module will start making space for new data by deleting the oldest data points in the memory.
>
> There will be seventeen new fault codes for the Next Generation CENSE™ CM2330 product. They will be replacing existing CM530 fault codes. All customer equipment collecting fault code information from the CENSE™ module **must** update their list to reflect these changes. Reference [[tsb130148 — Next Generation CENSE™ Fault Code List Changes\|TSB130148]] for more information.
>
> A new ROM boot cable for the Next Generation CENSE™ CM2330 module has also been released and is available to the field. The part number for this tool can be found in a summary table below.
>
> Changing to the Next Generation CENSE™ CM2330 module will result in the loss of RS422 and RS232 interface support. Any original equipment manufacturer (OEM) or customer equipment utilizing these interfaces will need to upgrade to J1939-capable equipment.
>
> As part of the migration to the new CENSE™ CM2330 module, a standard numbering system for exhaust gas temperature (EGT), intake manifold temperature (IMT), and intake manifold pressure (IMP) sensors has been adopted. Detailed old vs. new information is shown toward the end of this communication.
>
> Although all engines that are currently in service will eventually be upfitted with the Next Generation CENSE™ CM2330 module, first engine serial number (ESN) information for QSK/QSV/KV engines equipped with the new module can be found at the end of this communication. All subsequent ESNs will be equipped with the Next Generation CENSE™ CM2330 from the plant.
>
> **Note · Примечание**
> To avoid confusion in the field and false non-communication issues, Cummins Inc. recommends removing all RS232 connection points from the engine and/or truck cab as soon as the Next Generation CENSE™ CM2330 is installed.
>
> **Note · Примечание**
> After upgrading to the Next Generation CENSE™ CM2330 module, field personnel might **not** be able to communicate to the new module from the cab if a J1939 port is **not** already installed in the cab. To support communication with the CENSE™ CM2330 module from the cab, be sure that a J1939 data link connection from the engine harness is properly extended. Contact a local application engineer for instructions to extend the connection.
>
> | Obsoleted Part Numbers |  |
> |---|---|
> | Part Name | Part Number |
> | Engine Control Module | 3098771 |
> | K38 Engine Harness | 3643114 |
> | K38 Engine Harness | 3643115 |
> | K50 Engine Harness | 3644538 |
> | K50 Engine Harness | 3644539 |
>
> | New Part Numbers |  |
> |---|---|
> | Part Name | Part Number |
> | Engine Control Module | [[4326926]] |
> | K38 Engine Harness | 4328451 |
> | K50 Engine Harness | 4323226 |
> | J1939 Upfit Jumper Harness | 4328522 |
> | 9-Pin Service Connector L-Bracket | 3649861 |
> | CM2330 ROM Boot Cable | 5298707 |
>
> | Platform | Old ECM Code | New ECM Code | Old File Number | New File Number | FR Option | Note |
> |---|---|---|---|---|---|---|
> | NTC-400 | G10002 | N/A | 4922482 | N/A | FR01288 | Obsoleted |
> | QST30 | G50043 | EP80004 | 4998247 | 4328553 | FR05134 |  |
> | QST30 | G50041 | EP80008 | 3092440 | 4308662 | FR05150 |  |
> | QST30 | G50034 | EP80001 | 3092882 | 4328554 | FR05151 |  |
> | QST30 |  | EP80005 |  | 4308655 | FR05144 |  |
> | QST30 | G50031 | EP80006 | 3092208 | 4328555 | FR05227 |  |
> | QST30 | G50037 | N/A | 4068125 | 4328556 | FR05232 | Obsoleted |
> | QST30 | G50042 | EP80003 | 4295355 | 4328557 | FR05233 |  |
> | K50 | G60082 | EP60024 | 3099310 | 4328558 | FR06075 |  |
> | K50 | G60320 | EP60051.00 | 3098393 | 4335183 | FR06097 |  |
> | K50 | G60321 | N/A | 3098392 | FR06097 | Obsoleted |  |
> | K38 | G60322 | EP60023 | 3098997 | 4328559 | FR06101 | Obsoleted |
> | K38 | G60083 | EP60023 | 3099305 | FR06101 |  |  |
> | K38 | G60342 | EP60036 | 2873437 | 4335184 | FR06142 |  |
> | K50 | G60001 | EP60037 | 3098391 | 4335185 | FR06145 |  |
> | K50 | G60323 | EP60037 | 3098390 | FR06145 | Obsoleted |  |
> | K50 | G60349 | EP60037 | 3099306 | FR06145 | Obsoleted |  |
> | K50 | G60242 | EP60037 | 3099496 | FR06145 | Obsoleted |  |
> | K50 | G60338 | EP60037 | 4971018 | FR06145 | Obsoleted |  |
> | K50 | G60014 | EP60027 | 3099081 | 4328560 | FR06147 | Obsoleted |
> | K50 | G60300 | EP60027 | 3099309 | FR06147 |  |  |
> | K50 | G60334 | EP60028 | 4968511 | 4328561 | FR06202 |  |
> | K50 | G60324 | EP60029 | 3098731 | 4328562 | FR06215 | Obsoleted |
> | K50 | G60087 | EP60029 | 3099311 | FR06215 |  |  |
> | K38 | G60088 | EP60030 | 3099304 | 4328563 | FR06233 |  |
> | K50 | G60004 | EP60038 | 3098737 | 4335186 | FR06237 | Obsoleted |
> | K50 | G60333 | EP60038 | 3099308 | FR06237 |  |  |
> | QSK45 | G60304 | EP60010 | 4065692 | 4328564 | FR06268 |  |
> | K50 | G60305 | EP60031 | 3098779 | 4328565 | FR06276 | Obsoleted |
> | K50 | G60301 | EP60031 | 3099307 | FR06276 |  |  |
> | QSK45 | G60307 | EP60044 | 4065694 | 4357403 | FR06289 |  |
> | QSK45 | G60329 | EP60002 | 3636700 | 4328566 | FR06289 |  |
> | QSK45 | G60308 | EP60045 | 4065691 | 4357404 | FR06291 |  |
> | QSK45 | G60309 | EP60003 | 4080316 | 4328567 | FR06291 |  |
> | QSK78 | G60327 | EP60020 | 4080432 | 4328568 | FR06302 |  |
> | QSK78 | G60330 | EP60020 | 3637688 | FR06302 | Obsoleted |  |
> | QSK45 | G60310 | EP60004 | 4065693 | 4328570 | FR06305 |  |
> | QSK60 | G60098 | EP60011 | 4016601 | 4328571 | FR06325 |  |
> | QSK60 | G60225 | EP60012 | 4016600 | 4328572 | FR06327 |  |
> | QSK60 | G60099 | EP60046 | 4080312 | 4357405 | FR06329 |  |
> | QSK60 | G60100 | EP60046 | 4080311 | FR06329 | Obsoleted |  |
> | QSK60 | G60101 | EP60039 | 4080313 | 4335187 | FR06329 |  |
> | QSK60 | G60129 | EP60013 | 4086033 | 4328573 | FR06330 |  |
> | QSK60 | G60102 | EP60014 | 4086351 | 4328574 | FR06331 | Obsoleted |
> | QSK60 | G60178 | EP60014 | FR06331 |  |  |  |
> | QSK60 | G60254 | EP60015 | 4080314 | 4328575 | FR06339 | Obsoleted |
> | QSK60 | G60255 | EP60015 | 4080308 | FR06339 | Obsoleted |  |
> | QSK60 | G60256 | EP60015 | 4065680 | FR06339 |  |  |
> | QSK60 | G60257 | EP60015 | 4080310 | FR06339 | Obsoleted |  |
> | QSK60 | G60233 | EP60015 | 4100583 | FR06339 | Obsoleted |  |
> | QSK60 | G60296 | EP60016 | 4080318 | 4328576 | FR06340 | Obsoleted |
> | QSK60 | G60297 | EP60016 | 4080319 | FR06340 | Obsoleted |  |
> | QSK60 | G60298 | EP60016 | 4065696 | FR06340 |  |  |
> | QSK60 | G60260 | EP60016 |  | FR06340 | Obsoleted |  |
> | QSK60 | G60325 | EP60016 | 4101155 | FR06340 | Obsoleted |  |
> | QSK60 | G60245 | EP60017 | 4065687 | 4328577 | FR06359 |  |
> | K38 | G60339 | EP60047 | 2866989 | 4357406 | FR06367 |  |
> | K38 | G60350 | EP60047 | 3637829 | FR06367 | Obsoleted |  |
> | K50 | G60340 | EP60040 | 2866990 | 4335188 | FR06367 |  |
> | QSK60 | G60289 | EP60041 | 4065688 | 4335189 | FR06378 |  |
> | QSK60 | G60292 | EP60018 | 4101145 | 4328578 | FR06378 | Obsoleted |
> | QSK60 | G60331 | EP60018 | 3637682 | FR06378 |  |  |
> | QSK60 | G60312 | EP60042 | 4080315 | 4335190 | FR06379 |  |
> | QSK60 | G60314 | EP60019 | 4065681 | 4328579 | FR06379 |  |
> | K50 | G60299 | EP60032 | 3099306 | 4328580 | FR06389 |  |
> | K50 | G60337 | EP60032 | 4971017 | FR06389 | Obsoleted |  |
> | QSK45 | G60140 | EP60005 | 4085912 | 4328581 | FR06404 |  |
> | QSK45 | G60142 | EP60048 | 4085914 | 4357407 | FR06406 |  |
> | QSK45 | G60143 | EP60006 | 4085915 | 4328582 | FR06406 |  |
> | K50 | G60345 | EP60033 | 2896429 | 4328583 | FR06426 |  |
> | QSK45 | G60336 | EP60009 | 4101300 | 4328584 | FR06443 |  |
> | QSK60 | G60227 | EP60043 | 4016521 | 4335191 | FR06458 |  |
> | QSK60 | G60130 | EP60001.01 | 4065689 | [[4323412]] | FR06554 |  |
> | QSK45 | G60302 | EP60049 | 4065695 | 4357408 | FR06640 |  |
> | QSK60 | G60123 | EP60025 | 4085921 | 4328586 | FR06687 |  |
> | QSK78 | G60328 | EP60022 | 4101100 | 4328587 | FR06704 |  |
> | QSK45 | G60341 | EP60007 | 3635475 | 4328588 | FR06707 |  |
> | QSK60 | G60335 | EP60026 | 3636051 | 4328589 | FR06714 |  |
> | QSK78 | G60344 | EP60021 | 2886091 | 4328569 | FR06725 |  |
> | K38 | G60332 | EP60034 | 3637829 | 4328590 | FR06819 |  |
> | QSK45 | G60311 | EP60008 | 4065690 | 4328591 | FR06979 |  |
> | QST30 |  | EP80007 | 4067824 | 4328592 |  |  |
> | K50 | G60348 | EP60035 | 3099306 | 4335177 | FR06356 |  |
> | QSK60 - Gas |  | EP60050 |  |  | FR6056 |  |
> | QSK60 - Gas |  | EP60050 |  |  | FR6587 |  |
> | QSK60 - Gas |  | EP60050 |  |  | FR6802 |  |
> | QSK60 - Gas |  | EP60050 |  |  | FR6803 |  |
> | QSK60 - Gas |  | EP60050 |  |  | FR6804 |  |
> | QSK60 - Gas |  | EP60050 |  |  | FR6805 |  |
> | QSK60 - Gas |  | EP60050 |  |  | FR6806 |  |
> | QSK60 - Gas |  | EP60050 |  |  | FR6911 |  |
> | QSK60 - Gas |  | EP60050 |  |  | FR6912 |  |
> | QSV91 Phase 1 |  | EP80010 |  |  | FR7309 |  |
> | QSV91 Phase 1 |  | EP80010 |  |  | FR7310 |  |
> | QSV91 Phase 1 |  | EP80010 |  |  | FR7311 |  |
> | QSV91 Phase 1 |  | EP80010 |  |  | FR7312 |  |
> | QSV91 Phase 1 |  | EP80010 |  |  | FR7313 |  |
> | QSV91 Phase 1 |  | EP80010 |  |  | FR7314 |  |
> | QSV91 Phase 1 |  | EP80010 |  |  | FR7315 |  |
> | QSV91 Phase 1 |  | EP80010 |  |  | FR7316 |  |
> | QSV91 Phase 1 |  | EP80010 |  |  | FR7317 |  |
> | QSV91 Phase 1 |  | EP80010 |  |  | FR7318 |  |
> | QSV91 Phase 1 |  | EP80010 |  |  | FR7319 |  |
> | QSV91 Phase 1 |  | EP80010 |  |  | FR7320 |  |
> | QSV91 Phase 1 |  | EP80010 |  |  | FR7321 |  |
> | QSV91 Phase 1 |  | EP80010 |  |  | FR7322 |  |
> | QSV91 Phase 1 |  | EP80010 |  |  | FR7323 |  |
> | QSV91 Phase 1 |  | EP80010 |  |  | FR7324 |  |
> | QSV91 Phase 1 |  | EP80010 |  |  | FR7325 |  |
> | QSV91 Phase 1 |  | EP80010 |  |  | FR7385 |  |
> | QSV91 Phase 2 |  | EP80009 |  |  | FR07276 |  |
> | QSV91 Phase 2 |  | EP80009 |  |  | FR07281 |  |
> | QSV91 Phase 2 |  | EP80009 |  |  | FR07296 |  |
> | QSV91 Phase 2 |  | EP80009 |  |  | FR07297 |  |
> | QSV91 Phase 2 |  | EP80009 |  |  | FR07303 |  |
> | QSV91 Phase 2 |  | EP80009 |  |  | FR07306 |  |
> | QSV91 Phase 2 |  | EP80009 |  |  | FR07328 |  |
> | QSV91 Phase 2 |  | EP80009 |  |  | FR07329 |  |
> | QSV91 Phase 2 |  | EP80009 |  |  | FR07332 |  |
> | QSV91 Phase 2 |  | EP80009 |  |  | FR07335 |  |
> | QSV91 Phase 2 |  | EP80009 |  |  | FR07336 |  |
> | QSV91 Phase 2 |  | EP80009 |  |  | FR07339 |  |
> | QSV91 Phase 2 |  | EP80009 |  |  | FR07340 |  |
> | QSV91 Phase 2 |  | EP80009 |  |  | FR07343 |  |
> | QSV91 Phase 2 |  | EP80009 |  |  | FR07344 |  |
> | QSV91 Phase 2 |  | EP80009 |  |  | FR07347 |  |
> | QSV91 Phase 2 |  | EP80009 |  |  | FR07348 |  |
> | QSV91 Phase 2 |  | EP80009 |  |  | FR07349 |  |
> | QSV91 Phase 2 |  | EP80009 |  |  | FR07350 |  |
> | QSV91 Phase 2 |  | EP80009 |  |  | FR07351 |  |
> | QSV91 Phase 2 |  | EP80009 |  |  | FR07352 |  |
> | QSV91 Phase 2 |  | EP80009 |  |  | FR07355 |  |
> | QSV91 Phase 2 |  | EP80009 |  |  | FR07356 |  |
> | QSV91 Phase 2 |  | EP80009 |  |  | FR07359 |  |
> | QSV91 Phase 2 |  | EP80009 |  |  | FR07360 |  |
> | QSV91 Phase 2 |  | EP80009 |  |  | FR07361 |  |
> | QSV91 Phase 2 |  | EP80009 |  |  | FR07362 |  |
> | QSV91 Phase 2 |  | EP80009 |  |  | FR07377 |  |
> | QSV91 Phase 2 |  | EP80009 |  |  | FR07378 |  |
> | QSK38 - Gas |  | EP60052 |  |  | FR6691 |  |
> | QSV91 TVAB |  | EP80011 |  |  | FR7257 |  |
>
> | Old CENSE™ Numbering for Exhaust Gas Temperature (EGT) Sensors | New CENSE™ CM2330 Numbering for Exhaust Gas Temperature (EGT) Sensors |
> |---|---|
> | Cylinder Number 1 Left Bank | Cylinder Number 1 (A1) |
> | Cylinder Number 1 Right Bank | Cylinder Number 2 (B1) |
> | Cylinder Number 2 Left Bank | Cylinder Number 3 (A2) |
> | Cylinder Number 2 Right Bank | Cylinder Number 4 (B2) |
> | Cylinder Number 3 Left Bank | Cylinder Number 5 (A3) |
> | Cylinder Number 3 Right Bank | Cylinder Number 6 (B3) |
> | Cylinder Number 4 Left Bank | Cylinder Number 7 (A4) |
> | Cylinder Number 4 Right Bank | Cylinder Number 8 (B4) |
> | Cylinder Number 5 Left Bank | Cylinder Number 9 (A5) |
> | Cylinder Number 5 Right Bank | Cylinder Number 10 (B5) |
> | Cylinder Number 6 Left Bank | Cylinder Number 11 (A6) |
> | Cylinder Number 6 Right Bank | Cylinder Number 12 (B6) |
> | Cylinder Number 7 Left Bank | Cylinder Number 13 (A7) |
> | Cylinder Number 7 Right Bank | Cylinder Number 14 (B7) |
> | Cylinder Number 8 Left Bank | Cylinder Number 15 (A8) |
> | Cylinder Number 8 Right Bank | Cylinder Number 16 (B8) |
> | Cylinder Number 9 Left Bank | Cylinder Number 17 (A9) |
> | Cylinder Number 9 Right Bank | Cylinder Number 18 (B9) |
>
> | K38, K50 Engines Only |  |  |
> |---|---|---|
> | Old CENSE™ CM530 Numbering for Intake Manifold Temperature (IMT) Sensors | New CENSE™ CM2330 Numbering for Intake Manifold Temperature (IMT) Sensors | Fault Code Associated in New CM2330 |
> | Left Bank Front Intake Manifold Temperature | Intake Manifold Air Temperature \#1 | 154 |
> | Right Bank Front Intake Manifold Temperature | Intake Manifold Air Temperature \#3 | 161 |
> | Left Bank Rear Intake Manifold Temperature | Intake Manifold Air Temperature \#2 | 157 |
> | Right Bank Rear Intake Manifold Temperature | Intake Manifold Air Temperature \#4 | 164 |
>
> | QSK45, QSK60 Engines Only |  |  |
> |---|---|---|
> | Old CENSE™ CM530 Numbering for Intake Manifold Temperature (IMT) Sensors | New CENSE™ CM2330 Numbering for Intake Manifold Temperature (IMT) Sensors | Fault Code Associated in New CM2330 |
> | Left Bank Front Intake Manifold Temperature | Intake Manifold Air Temperature \#1 | Remote (CM500) |
> | Right Bank Front Intake Manifold Temperature | Intake Manifold Air Temperature \#3 | 161 |
> | Left Bank Rear Intake Manifold Temperature | Intake Manifold Air Temperature \#2 | 157 |
> | Right Bank Rear Intake Manifold Temperature | Intake Manifold Air Temperature \#4 | 164 |
>
> | QSK78 Engines Only |  |  |
> |---|---|---|
> | Old CENSE™ CM530 Numbering for Intake Manifold Temperature (IMT) Sensors | New CENSE™ CM2330 Numbering for Intake Manifold Temperature (IMT) Sensors | Fault Code Associated in New CM2330 |
> | Left Bank Front Intake Manifold Temperature | Intake Manifold Air Temperature \#1 | Remote (CM500) |
> | Right Bank Front Intake Manifold Temperature | Intake Manifold Air Temperature \#3 | 161 |
> | Left Bank Middle Intake Manifold Temperature | Intake Manifold Air Temperature \#5 | 2243 |
> | Right Bank Middle Intake Manifold Temperature | Intake Manifold Air Temperature \#6 | 2247 |
> | Left Bank Rear Intake Manifold Temperature | Intake Manifold Air Temperature \#2 | 157 |
> | Right Bank Rear Intake Manifold Temperature | Intake Manifold Air Temperature \#4 | 164 |
>
> | Old CENSE™ Numbering for Intake Manifold Pressure (IMP) Sensors | New CENSE™ CM2330 Numbering for Intake Manifold Pressure (IMP) Sensors |
> |---|---|
> | Left Bank Intake Manifold Pressure | Intake Manifold Pressure \#1 |
> | Right Bank Intake Manifold Pressure | Intake Manifold Pressure \#2 |
>
> | Platform | ESN First |
> |---|---|
> | QSK78 HPI | 66302969 |
> | QSK60 HPI | 33199842 |
> | K50 | 33199574 |
> | QSK60 - Gas | 33199692 |
> | QSV91 - Gas | 66302996 |
>
> ### Document History
