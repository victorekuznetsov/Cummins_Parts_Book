---
aliases:
  - "Диагностика мультиплексирования"
type: "Сервисный бюллетень"
doc: "4021378"
title_en: "Multiplexing Troubleshooting"
title_ru: "Диагностика мультиплексирования"
released: "2011-04-25"
modified: "2019-05-07"
group: "19 - Electronic Engine Controls"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "33224404"
  - "33239746"
  - "33239899"
  - "35354607"
  - "35373113"
  - "41340468"
  - "41349633"
  - "41353297"
  - "71156161"
  - "77804793"
  - "77804810"
  - "80141463"
  - "80248213"
  - "82099327"
  - "85017333"
  - "93948840"
families:
  - "15N"
  - "A8.5"
  - "K38/K50 · QSK38, QSK50"
  - "QSB6.7"
  - "QSK19"
  - "QSK23"
  - "QSK50"
  - "QSK60"
  - "QSK60 CM2150 MCRS"
  - "QSM11"
  - "QSX15"
  - "QSZ13"
figures: 2
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/4021378.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/bulletin/4021378.pdf"
tags:
  - "документ/бюллетень"
  - "двигатель/15N"
  - "двигатель/A8.5"
  - "двигатель/K38/K50"
  - "двигатель/QSB6.7"
  - "двигатель/QSK19"
  - "двигатель/QSK23"
  - "двигатель/QSK50"
  - "двигатель/QSK60"
  - "двигатель/QSK60CM2150MCRS"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "двигатель/QSZ13"
  - "перевод/машинный"
  - "тема/electronic-engine-controls"
---

# Multiplexing Troubleshooting
**Диагностика мультиплексирования**

> [!abstract] Сервисный бюллетень · `4021378`
> **Раздел Cummins:** 19 - Electronic Engine Controls
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[33224404 — QSK50 CM2150 MCRS CPL 3391|33224404]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[41340468 — QSK50 CM2150 MCRS CPL 3728|41340468]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[77804793 — A8.5 CM2670 L153B CPL 6235|77804793]], [[77804810 — 15N CM2380 M104B CPL 5977|77804810]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]], [[82099327 — QSB6.7 CM2150 B109 CPL 4375|82099327]], [[85017333 — QSK23 CM500 CPL 2858|85017333]], [[93948840 — QSZ13 CM2150 Z102 CPL 4858|93948840]]
> **Семейство:** 15N, A8.5, K38/K50 · QSK38, QSK50, QSB6.7, QSK19, QSK23, QSK50, QSK60, QSK60 CM2150 MCRS, QSM11, QSX15, QSZ13
> **Даты:** выпущен 2011-04-25 · изменён 2019-05-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/4021378.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/bulletin/4021378.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Диагностика мультиплексирования

## Введение

Этот бюллетень службы вводит функцию мультиплексирования и предоставляет:

- Введение в новую функцию мультиплексирования SAE J1939
- Функции и параметры мультиплексирования SAE J1939 с использованием инструментария электронных услуг INSITETM
- Информация кода ошибки, связанная с функцией мультиплексирования и общими рекомендациями по устранению неполадок.

## многослойный

Обычные системы двигателей имеют проводные соединения с отдельными переключателями, датчиками и дросселями для целей управления и обратной связи. С введением в автомобильной промышленности сети мультиплексирования SAE J1939 многочисленные кабели и проводные ремни были сокращены до нескольких точек подключения. Уменьшенная проводка транспортного средства возможна в мультиплексированной системе из-за передачи и приема нескольких сигналов по одной и той же шине сигнала (или шине данных CAN) между модулями, которые традиционно выполняются отдельными проводами.

## Многоуровневые функции и параметры настройки

Процесс настройки функции мультиплексирования объясняется в двух частях:

## Часть 1: J1939 Многоуровневые функции и параметры с помощью инструментария электронного обслуживания INSITETM

Следуйте инструкциям ниже, чтобы настроить функции и параметры мультиплексирования J1939 с помощью инструментария электронного обслуживания INSITETM.

1. В меню View (текущий вид) выберите Функции и Параметры или нажмите на значок Функции и Параметры в левой части окна инструментов электронного сервиса INSITETM.
2. Найдите и расширьте значок SAE J1939 Multiplexing из списка «Особенности и параметры».
3. Для каждого параметра установите значение ECM для включения/отключения в соответствии с соответствующими настройками OEM.
4. Для каждого включенного параметра установите адрес источника в соответствии с соответствующей установкой OEM.

![[19803894.png]]

1. SAE J1939 Мультиплексорная функция
2. Включить/отключить для функции мультиплексирования J1939
3. Выбор адреса источника для функции «Enabled» J1939 Multiplexing.

## Использование инструментария электронного сервиса INSITETM для устранения неполадок в кодах 285, 286, 427 или 6338

Используйте инструмент электронного сервиса INSITETM SAE J1939 Multiplexed Fault Data, расположенный в данных Advanced ECM, чтобы определить, какой компонент вызывает неисправность. Эта функция в инструменте электронного обслуживания INSITETM будет указывать, какой мультиплексный компонент **не** настроен правильно. Если столбец состояния указывает «Активный» для мультиплексированного компонента, проверьте, что мультиплексированный компонент ECM двигателя включает и адреса источника соответствуют мультиплексному компоненту OEM VECU. Параметры конфигурации мультиплексирования можно найти в разделе SAE J1939 Multiplexing в разделе «Особенности и параметры электронного инструментария обслуживания INSITETM».

![[19r00017.png]]

1. SAE J1939 Многослойные данные об ошибках
2. Неисправности, показывающие параметры, которые в настоящее время установлены неправильно. Параметры, которые в настоящее время показаны как «Активные», имеют неверную информацию об адресе источника или были неправильно установлены для включения или отключения.

## Часть 2: OEM Specific SAE J1939 Многослойная конфигурация функций

Различные OEM-производители имеют различные конфигурации мультиплексирования, для которых компоненты или переключатели могут быть включены для мультиплексирования в Cummins® ECM. Для возможности мультиплексирования должны быть выполнены следующие условия:

1. Электронный блок OEM-автомобиля и ECM Cummins® должны иметь одинаковые компоненты, включенные для мультиплексирования.
2. Адрес источника каждого включенного компонента должен быть установлен на соответствующее значение для включенного компонента или переключателя.

> [!note] Примечание
> Процедура установки мультиплексирования для электронного блока управления OEM-автомобилем выходит за рамки настоящего Бюллетеня по обслуживанию. Свяжитесь с соответствующим OEM для получения необходимой информации.

## Устранение общих неполадок

Предоставляется список кодов ошибок мультиплексирования, описания, причины кода ошибок и краткая процедура устранения неполадок. Для подробного описания проверьте код неисправности в соответствующем руководстве по устранению неполадок и ремонту.

## Код ошибки 285 или 427 - Ошибка многократного тайм-аута SAE J1939 - аномальная скорость обновления (медленная или отсутствие связи)

Этот код неисправности возникает, когда переключатель или компонент включен и адресован в ECM, но сообщение от электронного блока управления OEM-автомобиля **не** получено ECM по одной или всем следующим причинам:

- Мультиплексное сообщение для конкретного переключателя **не** транслируется из электронного блока управления транспортного средства в ECM. Это может быть связано с аппаратным сбоем электронного блока управления транспортного средства или проблемой установки программного обеспечения электронного блока управления транспортного средства. Эта неисправность может быть вызвана проблемой установки электронного блока управления OEM-устройством транспортного средства **только**, если все компоненты и параметры для конкретного сообщения групп имен параметров SAE J1939 отключены в электронном блоке управления OEM-транспортного средства. В противном случае будет создан код ошибки 286 или 6338.
- Между электронным блоком управления OEM-автомобилем и ECM Cummins® существует проблема шины данных CAN, которая **не** позволяет передавать любые сообщения SAE J1939 (названия групп параметров) из электронного блока управления OEM-автомобилем в ECM Cummins®.
- Cummins ECM включает переключатель или компонент, который правильно включен в программное обеспечение электронного блока управления OEM-автомобиля, но является источником, адресованным неправильному электронному блоку управления OEM-автомобиля. Этот режим неисправности может возникнуть, когда ECM заменен и изображение работы было **не** взято или сохранен шаблон, чтобы определить, какие компоненты **должны быть включены для мультиплексирования и как должен быть установлен источник электронного блока управления OEM-производителя транспортного средства**.
- Cummins ECM включил переключатель или компонент, который включен неправильно в программном обеспечении электронного блока управления OEM-автомобиля и является источником, адресованным неправильному электронному блоку управления OEM-автомобиля (электронный блок управления OEM-автомобиля поддерживает мультиплексирование компонента). Этот режим неисправности может возникнуть, когда заменяется ECM и используется правильный шаблон **не**.

## Общий процедура устранения неполадок код 285 или 427

- Проверить связь между электронным сервисным оборудованием и Cummins® ECM можно. Если это невозможно, устраните неисправности в подключении шины данных службы CAN к шине данных SAE J1939 CAN и соединении ECM с шиной данных SAE J1939 CAN. Это достигается путем проверки того, что при измерении сопротивления между шиной данных SAE J1939 CAN (+) проводом и шиной данных SAE J1939 CAN (-) проводом на разъеме шины данных CAN службы и разъемом шины данных Cummins® ECM CAN существует значение сопротивления между 50 и 70 Ом.
- Если связь возможна, определите, позволяет ли мультиплексный компонент и адреса источника электронного блока управления OEM-устройством транспортного средства правильно установлены в ECM Cummins®. Это может быть достигнуто с помощью изображений и шаблонов работы, которые, как известно, являются правильными, или с помощью информации, предоставляемой соответствующим OEM. Это также может быть достигнуто путем проверки наличия проводов, установленных на соответствующем разъеме Cummins® ECM для рассматриваемых компонентов.
- Если проблема **не найдена с шиной данных CAN или разъемами, проблема **должна быть с компонентом OEM, аппаратным обеспечением электронного блока управления транспортного средства, программным обеспечением электронного блока управления транспортного средства или подключением электронного блока управления транспортного средства к шине данных CAN.

## Код ошибки 286 или 6338 - Ошибка многослойной конфигурации SAE J1939 - Вне калибровки

Этот код неисправности будет иметь место, когда включен коммутатор или компонент и адресован источник для мультиплексирования в Cummins® ECM, но сообщение от электронного блока управления OEM-автомобиля **не** получено Cummins® ECM по одной или всем следующим причинам:

- Cummins ECM включил и источник адресовал коммутатор или компонент правильно, что **должен** быть включен в электронный блок управления OEM-устройством транспортного средства в соответствии с предоставленной OEM-производителем информацией, но **не** включен в программное обеспечение электронного блока управления OEM-устройством транспортного средства правильно. Электронный блок управления OEM-автомобиля передает сообщение компонента как **не** доступное, но компонент должен быть включен и доступен в электронном блоке управления OEM-производителя.
- Cummins ECM включил компонент, который **не** доступен для мультиплексирования из электронного блока управления OEM-транспортного средства, и имеет выбранное устройство, которое является правильным для всех других мультиплексированных компонентов из электронного блока управления OEM-транспортного средства. Сигнал передается как «Недоступен».

## Общий процедура устранения неполадок Код 286 или 6338

- Если проблема **не** обнаружена с шиной данных CAN или разъемами, проблема должна быть с компонентом OEM, аппаратным обеспечением электронного блока управления транспортного средства, программным обеспечением электронного блока управления транспортного средства или электронным блоком управления транспортного средства с подключением шины данных CAN.
- Если связь возможна, определите, правильно ли включены мультиплексированные компоненты и правильно установлены адреса источника электронного блока управления OEM-устройством в ECM Cummins®. Это может быть достигнуто с помощью изображений работы и шаблонов, которые, как известно, являются правильными, или с помощью информации, предоставляемой соответствующим OEM. Это также может быть достигнуто путем проверки наличия проводов, установленных на соответствующем разъеме Cummins® ECM для местоположения компонента.

## Код ошибки 287 - SAE J1939 Многоплексный ускоритель Педаль или ошибка системы датчика рычага - Ошибка получения сетевых данных

Код неисправности генерируется, когда присутствует условие ошибки на ускорителе или выключателе проверки бездействия. Этот код ошибки будет происходить по одной или всем следующим причинам:

- Когда ускоритель находится в депрессии, и ECM считывает положение ускорителя как более 0 процентов, но переключатель проверки бездействия передает сообщение, которое показывает, что ускоритель находится в депрессии.
- Когда ускоритель высвобождается, ECM считывает положение ускорителя как 0 процентов, но переключатель проверки бездействия передает сообщение, которое показывает, что ускоритель находится в депрессии.
- Сигнальная линия ускорителя закорочена высоко или закорочена низко. Когда любой из компонентов имеет ошибку, Cummins ECM будет использовать алгоритм «ухоженный дом», чтобы позволить транспортному средству перемещаться в безопасное место.

> [!note] Примечание
> Может быть педаль акселератора или время ожидания переключателя проверки, что приведет к активации кода 285 или 427 ошибки. Код 287 по умолчанию **только для истинных отказов схемы переключателя ускорителя или холостого валидирования. Двигатель будет работать в режиме холостого хода, когда педаль акселератора или выключатель валидации холостого хода получат сообщение от электронного блока управления транспортного средства OEM, которое показывает педаль акселератора или выключатель проверки холостого хода как находящиеся в состоянии **не (код ошибки 286 или 6338). Алгоритм «ухоженного дома» будет включен, когда произойдет отключение времени сообщения (код ошибки 285 или 427) или когда педаль акселератора или переключатель проверки бездействия имеют ошибку (код ошибки 287).

## Общий процедура устранения неполадок Кодекс 287

- Определить, включены ли мультиплексированные компоненты и правильно ли установлены адреса источника электронного блока управления OEM-устройством в ECM Cummins®. Это может быть достигнуто с помощью изображений работы и шаблонов, которые, как известно, являются правильными, или с помощью информации, предоставляемой соответствующим OEM. Это также может быть достигнуто путем проверки наличия проводов, установленных на соответствующем разъеме Cummins® ECM для рассматриваемых компонентов.
- Если с настройками функций существует проблема **not**, проблема может быть связана с компонентом OEM, аппаратным обеспечением электронного блока управления транспортного средства, программным обеспечением электронного блока управления транспортного средства или подключением электронного блока транспортного средства к шине данных CAN.
- Проверьте соединения педали акселератора и холостого валидационного выключателя и проследите за состоянием с помощью инструментария электронного обслуживания INSITETM, чтобы убедиться, что параметры получены правильно с помощью ECM Cummins®.

## Код ошибки 288 - SAE J1939 Удалённая ошибка данных дроссельной загрузки

Этот код ошибок обнаруживает ошибки в удаленном дросселе, но не обнаруживает ошибки тайм-аута (код ошибки 285 или 427). Этот код ошибки будет происходить по одной или всем следующим причинам:

- При удаленном ускорителе имеется закороченная высокая или закороченная низкая ошибка, обнаруженная электронным блоком управления транспортным средством. Этот статус неисправности передается в ECM на шине данных SAE J1939 CAN, что приводит к возникновению неисправности в ECM.
- Когда выключатель с дистанционным дроссельным заслоном имеет закороченную высокую или закороченную низкую ошибку, обнаруженную электронным блоком управления транспортным средством, состояние неисправности передается в ECM на шине данных SAE J1939 CAN, что приводит к активации кода неисправности в ECM. Большинство OEM-производителей **не** включают обнаружение неисправностей на коммутаторе. Код неисправности генерируется, когда присутствует условие ошибки в цепи удаленного дроссельного заслонка, но **не**, когда присутствует ошибка в цепи переключателя холостого валидационного переключателя, потому что удаленные дроссельные заслонки **не** имеют переключатель холостого валидационного заслонка.

## Общий процедура устранения неполадок Кодекс 288

- Определить, включены ли мультиплексированные компоненты и правильно ли установлены адреса источника электронного блока управления OEM-устройством в ECM Cummins®. Это может быть достигнуто с помощью изображений работы и шаблонов, которые, как известно, являются правильными, или с помощью информации, предоставляемой соответствующим OEM. Это также может быть достигнуто путем проверки наличия проводов, установленных на соответствующем разъеме Cummins® ECM для рассматриваемых компонентов.
- Если с настройками функций обнаружена проблема **not**, проблема должна быть связана с компонентом OEM, аппаратным обеспечением электронного блока управления транспортного средства, программным обеспечением электронного блока управления транспортного средства или подключением электронного блока управления транспортного средства к шине данных CAN.

## General SAE J1939 Многослойная процедура устранения неполадок на основе симптома

> [!note] Примечание
> Этот процесс предполагает, что транспортное средство будет использовать функцию мультиплексирования.

Следующий общий процесс **должен быть использован для устранения симптомов на транспортном средстве, которое поддерживает функцию мультиплексирования SAE J1939, когда коды неисправностей **не присутствуют. Эти симптомы будут связаны только с компонентами, которые могут быть мультиплексированы в конкретном приложении. Следующие шаги будут действовать как руководство по процедуре устранения неполадок на основе симптомов и позволят выделить проблему в проблему датчика, проблему электронного блока управления транспортным средством, проблему шины данных CAN, проблему ECM Cummins или их комбинацию.

1. Интервью оператора для определения конкретного симптома (примеры - переключатель сцепления **не** функционирует, круиз-контроль включения/выключения **не** работает, ручной переключатель управления вентилятором **не** работает и т.д.). Если описание симптома расплывчато, необходимо будет проверить симптомы с помощью дорожного теста.
2. Подключите электронный инструмент к Cummins® ECM и убедитесь, что связь с Cummins® ECM возможна.
3. Если связь с Cummins® ECM возможна, распечатайте изображение, чтобы получить копию функций Cummins® ECM и параметров настроек. Это будет стандартная процедура для всех транспортных средств, которые используют функцию мультиплексирования в двигателе Cummins®. Если ECM заменен или поврежден, а информация о настройке мультиплексирования была сохранена, будет трудно получить информацию от OEM.
4. Если связь с Cummins® ECM невозможна, проверьте соответствующее дерево устранения неполадок ECM для процедуры устранения неполадок симптома отсутствия связи. Некоторые из причин отсутствия связи между инструментами электронного обслуживания и ECM - это неисправность проводов шины данных SAE J1939 CAN или разъемы, переключаемые или непереключаемые батареи к адаптеру шины данных ECM или CAN, неисправность кабелей или разъемов адаптера шины данных CAN или неисправность калибровки или оборудования ECM.
5. Сначала прочитайте коды неисправностей и устраните любые активные коды неисправностей, используя соответствующую процедуру кода неисправности.[[99-019-362 — Inactive or Intermittent Fault Code|Если имеется большое количество кодов неактивных ошибок, 019-362 (Код неактивных или периодических ошибок) в разделе 19 соответствующего руководства по устранению неполадок и ремонту электронной системы управления.]]
6. Используйте инструмент электронного сервиса для мониторинга мультиплексированных компонентов или переключателей для изменения состояния или значения, которые могут способствовать симптому. Эта информация полезна для сужения того, какие компоненты способствуют симптому.
7. Эти компоненты могут быть включены и адресованы источнику мультиплексирования в соответствии с функцией мультиплексирования SAE J1939. Если какой-либо из компонентов **не** изменяет состояние, документируйте компонент и проверьте, включены ли компоненты и адресован ли источник мультиплексирования. Быстрая проверка для изучения того, является ли компонент мультиплексированным, заключается в проверке электропроводки, чтобы убедиться, что провода компонентов направляются в ECM Cummins®. Если провода **не** присутствуют для данного компонента, это указание на то, что компонент или переключатель не должны быть мультиплексированы. Свяжитесь с OEM для настроек мультиплексирования J1939.
8. Если есть **не** какие-либо проблемы с связью ECM, адаптером шины данных CAN, жгутом проводов или установкой для мультиплексирования, с OEM необходимо связаться, чтобы определить дальнейшие действия по устранению неполадок.

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## Multiplexing Troubleshooting
>
> ## Introduction
>
> This Service Bulletin introduces the multiplexing feature and provides:
>
> - Introduction to the new SAE J1939 multiplexing feature
> - SAE J1939 multiplexing features and parameters setup using INSITE™ electronic service tool
> - Fault code information associated with the multiplexing feature and general troubleshooting guidelines.
>
> ## Multiplexing
>
> Conventional engine systems have wired connections to individual switches, sensors, and throttles for control and feedback purposes. With the introduction of the SAE J1939 multiplexing network in the vehicle industry, the numerous cables and harnesses have been reduced to a few connection points. The reduced vehicle wiring is possible in a multiplexed system because of the transmission and reception of multiple signals over the same signal bus (or data link) between modules, which have been traditionally accomplished by individual wires.
>
> ## Multiplexing Features and Parameters Setup
>
> The multiplexing feature setup process is explained in two parts:
>
> ## Part 1: J1939 Multiplexing Features and Parameters Setup with INSITE™ Electronic Service Tool
>
> Follow the instructions below to set up the J1939 Multiplexing features and parameters using INSITE™ electronic service tool.
>
> 1. Under the View menu (current view), select Features and Parameters or click on the Features and Parameters icon on the left side of INSITE™ electronic service tool window.
> 2. Locate and expand the SAE J1939 Multiplexing icon from the Features and Parameters list.
> 3. For each parameter, set the ”ECM Value” to enable/disable, according to the appropriate OEM settings.
> 4. For each enabled parameter, set the source address according to the appropriate OEM setting.
>
> 1. SAE J1939 Multiplexing feature
> 2. Enable/Disable for J1939 Multiplexing feature
> 3. Source address selection for ”Enabled” J1939 Multiplexing feature.
>
> ## Using INSITE™ Electronic Service Tool to Troubleshoot Multiplexing Fault Codes 285, 286, 427, or 6338
>
> Use INSITE™ electronic service tool SAE J1939 Multiplexed Fault Data feature, located in Advanced ECM data, to determine which multiplexed component is causing the fault. This feature in INSITE™ electronic service tool will indicate which multiplexed component is **not** configured correctly. If the status column indicates “Active” for a multiplexed component, check that the engine ECM multiplexed component enables and source addresses match the OEM VECU multiplexed component. The multiplexing configuration settings can be found under SAE J1939 Multiplexing in Features and Parameters of the INSITE™ electronic service tool.
>
> 1. SAE J1939 Multiplexed Fault Data
> 2. Faults showing parameters that are currently set incorrectly. The parameters that are currently shown as “Active” have incorrect source address information, or have been improperly set to enable or disable.
>
> ## Part 2: OEM Specific SAE J1939 Multiplexing Feature Configuration
>
> Different OEMs have different multiplexing configurations for which components or switches can be enabled for multiplexing in the Cummins® ECM. For multiplexing to be possible, the following conditions **must** be met:
>
> 1. The OEM vehicle electronic unit and the Cummins® ECM **must** have the same components enabled for multiplexing.
> 2. The source address of each enabled component **must** be set to the proper value for the component or switch that was enabled.
>
> **Note · Примечание**
> The multiplexing setup procedure for the OEM vehicle electronic control unit is beyond the scope of this Service Bulletin. Contact the appropriate OEM for the required information.
>
> ## General Multiplexing Troubleshooting
>
> A list of multiplexing fault codes, descriptions, cause of the fault code, and a brief troubleshooting procedure is provided. For a detailed description, check the fault code in the appropriate troubleshooting and repair manual.
>
> ## Fault Code 285 or 427 - SAE J1939 Multiplexing PGN Timeout Error - Abnormal Update Rate (Slow or No Communication)
>
> This fault code occurs when a switch or component is enabled and addressed in the ECM, but the message from the OEM vehicle electronic control unit is **not** received by the ECM for one or all of the following reasons:
>
> - The multiplexed message for a particular switch is **not** broadcast from the vehicle electronic control unit to the ECM. This can be because of a vehicle electronic control unit hardware failure or vehicle electronic control unit software setup issue. This fault can be caused by an OEM vehicle electronic control unit setup issue **only** if all components and parameters for a specific SAE J1939 parameter group names message are disabled in the OEM vehicle electronic control unit. Otherwise Fault Code 286 or 6338will be generated.
> - There is a data link issue between the OEM vehicle electronic control unit and the Cummins® ECM which is **not** allowing any SAE J1939 messages (parameter group names) to be transmitted from the OEM vehicle electronic control unit to the Cummins® ECM.
> - The Cummins® ECM has enabled a switch or component that is enabled correctly in the OEM vehicle electronic control unit software, but is source addressed to the incorrect OEM vehicle electronic control unit. This fault mode can occur when an ECM is replaced and a job image was **not** taken or a template saved to identify which components **must** be enabled for multiplexing and how the OEM vehicle electronic control unit source **must** be set.
> - The Cummins® ECM has enabled a switch or component that is enabled incorrectly in the OEM vehicle electronic control unit software and is source addressed to the incorrect OEM vehicle electronic control unit (the OEM vehicle electronic control unit does **not** support multiplexing of the component). This fault mode can occur when an ECM is replaced and the correct template is **not** used.
>
> ## General Troubleshooting Procedure for Fault Code 285 or 427
>
> - Verify communication is possible between the electronic service tool and the Cummins® ECM. If it is **not** possible, troubleshoot the service data link connector connection to the SAE J1939 data link and the ECM connection to the SAE J1939 data link. This is accomplished by verifying that there is a resistance value between 50 and 70 ohms when measuring the resistance between the SAE J1939 data link (+) wire and the SAE J1939 data link (-) wire on the service data link connector and the Cummins® ECM data link connector.
> - If communication is possible, determine if the multiplexed component enables and the OEM vehicle electronic control unit source addresses are set correctly in the Cummins® ECM. This can be accomplished by using job images and templates that are known to be correct or by using information supplied by the appropriate OEM. This can also be accomplished by checking to see if there are wires installed on the appropriate Cummins® ECM connector for the components in question.
> - If an issue is **not** found with the data link or connectors, the issue **must** be with the OEM component, vehicle electronic control unit hardware, vehicle electronic control unit software, or the vehicle electronic control unit connection to the data link.
>
> ## Fault Code 286 or 6338 - SAE J1939 Multiplexing Configuration Error - Out of Calibration
>
> This fault code will occur when a switch or component is enabled and source addressed to be multiplexed in the Cummins® ECM, but the message from the OEM vehicle electronic control unit is **not** received by the Cummins® ECM for one or all of the following reasons:
>
> - The Cummins® ECM has enabled and source addressed a switch or component correctly that **must** be enabled in the OEM vehicle electronic control unit according to the OEM supplied information, but is **not** enabled in the OEM vehicle electronic control unit software correctly. The OEM vehicle electronic control unit transmits the component message as **not** available, but the component **must** be enabled and available in the OEM electronic control unit.
> - The Cummins® ECM has enabled a component that is **not** available to be a multiplexed component from the OEM vehicle electronic control unit, and has a device selected that is correct for all of the other multiplexed components from the OEM vehicle electronic control unit. The signal is being transmitted as ” **Not** available”.
>
> ## General Troubleshooting Procedure for Fault Code 286 or 6338
>
> - If an issue is **not** found with the data link or connectors, the issue **must** be with an OEM component, vehicle electronic control unit hardware, vehicle electronic control unit software, or vehicle electronic control unit to the data link connection.
> - If communication is possible, determine if the multiplexed components are enabled correctly and OEM vehicle electronic control unit source addresses are set correctly in the Cummins® ECM. This can be accomplished by using job images and templates that are known to be correct, or by using information supplied by the appropriate OEM. This also can be accomplished by checking to see if there are wires installed on the appropriate Cummins® ECM connector for the component's location.
>
> ## Fault Code 287 - SAE J1939 Multiplexing Accelerator Pedal or Lever Sensor System Error - Received Network Data Error
>
> The fault code is generated when an error condition on the accelerator or idle validation switch is present. This fault code will occur for one or all of the following reasons:
>
> - When the accelerator is depressed and the ECM reads accelerator position as greater than 0 percent, but the idle validation switch transmits a message that shows the accelerator is **not** depressed.
> - When the accelerator is released and the ECM reads accelerator position as 0 percent, but the idle validation switch transmits a message that shows the accelerator is depressed.
> - Accelerator signal line is shorted high or shorted low. When either component has an error, the Cummins® ECM will engage the limp home algorithm to allow the vehicle to be moved to a safe location.
>
> **Note · Примечание**
> There can be an accelerator pedal or idle validation switch message time out which will cause Fault Code 285 or 427 to become active. Fault Code 287 is **only** for true accelerator or idle validation switch circuit failures. The engine will go to idle when the accelerator pedal or the idle validation switch receives a message from the OEM vehicle electronic control unit that shows the accelerator pedal or idle validation switch as being in the **not** available state (Fault Code 286 or 6338). The limp home algorithm will be enabled when a message time out occurs (Fault Code 285 or 427) or when the accelerator pedal or the idle validation switch has an error (Fault Code 287).
>
> ## General Troubleshooting Procedure for Fault Code 287
>
> - Determine if the multiplexed components are enabled and the OEM vehicle electronic control unit source addresses are set correctly in the Cummins® ECM. This can be accomplished by using job images and templates that are known to be correct, or by using information supplied by the appropriate OEM. This can also be accomplished by checking to see if there are wires installed on the appropriate Cummins® ECM connector for the components in question.
> - If there is **not** an issue with the feature setups, the issue can be with the OEM component, vehicle electronic control unit hardware, vehicle electronic control unit software, or vehicle electronic unit connection to the data link.
> - Check the connections of the accelerator pedal and idle validation switch and monitor the status with INSITE™ electronic service tool to verify the parameters are received properly by the Cummins® ECM.
>
> ## Fault Code 288 - SAE J1939 Multiplexing Remote Throttle Data Error
>
> This fault code detects errors in the remote throttle, but does **not** detect message time out errors (Fault Code 285 or 427). This fault code will occur for one or all of the following reasons:
>
> - When the remote accelerator has a shorted high or shorted low error detected by the vehicle electronic control unit. This fault status is transmitted to the ECM on the SAE J1939 data link, which causes the fault to occur in the ECM.
> - When the remote throttle enable switch has a shorted high or shorted low error detected by the vehicle electronic control unit, the fault status is transmitted to the ECM on the SAE J1939 data link, which causes the fault code to activate in the ECM. Most OEMs will **not** incorporate fault detection on a switch. The fault code is generated when an error condition on the remote throttle circuit is present, but **not** when an error on the idle validation switch circuit is present, because remote throttles do **not** have an idle validation switch.
>
> ## General Troubleshooting Procedure for Fault Code 288
>
> - Determine if the multiplexed components are enabled and the OEM vehicle electronic control unit source addresses are set correctly in the Cummins® ECM. This can be accomplished by using job images and templates that are known to be correct, or by using information supplied by the appropriate OEM. This can also be accomplished by checking if there are wires installed on the appropriate Cummins® ECM connector for the components in question.
> - If there is **not** an issue found with the feature setups, the issue **must** be with an OEM component, vehicle electronic control unit hardware, vehicle electronic control unit software, or vehicle electronic control unit connection to the data link.
>
> ## General SAE J1939 Multiplexing Symptom Based Troubleshooting Procedure
>
> **Note · Примечание**
> This process assumes the vehicle will be using the multiplexing feature.
>
> The following general process **must** be used to troubleshoot symptoms on a vehicle that supports SAE J1939 multiplexing feature when fault codes are **not** present. These symptoms will **only** be related to the components that can be multiplexed in a particular application. The following steps will act as a guide through a symptom based troubleshooting procedure and allow the problem to be isolated to a sensor issue, vehicle electronic control unit issue, data link issue, Cummins® ECM issue, or a combination thereof.
>
> 1. Interview the operator to determine specific symptom (examples - clutch switch **not** functioning, cruise control on/off switch **not** working, manual fan control switch **not** working, etc.). If the symptom description is vague, it will be necessary to verify the symptoms with a road test.
> 2. Connect an electronic service tool to the Cummins® ECM and verify that communication with the Cummins® ECM is possible.
> 3. If communication with the Cummins® ECM is possible, print an image to get a copy of the Cummins® ECM features and parameter settings. This will be a standard procedure for all vehicles that use the multiplexing feature in a Cummins® engine. If an ECM is replaced or is damaged and the multiplexing setup information was **not** saved, it will be difficult to get the information from the OEM.
> 4. If communication with the Cummins® ECM is **not** possible, check the appropriate ECM Communication Troubleshooting Tree for procedure to troubleshoot a no communication symptom. Some of the causes of no communication between the electronic service tool and the ECM are SAE J1939 data link harness or connectors have malfunctioned, switched or unswitched battery power to the ECM or data link adapter is **not** available, the data link adapter cables or connectors have malfunctioned, or the ECM calibration or hardware has malfunctioned.
> 5. Read the fault codes and troubleshoot any active fault codes first, using the appropriate fault code procedure. [[99-019-362 — Inactive or Intermittent Fault Code|Refer to Procedure If there are high counts of inactive fault codes, 019-362 (Inactive or Intermittent Fault Code) in Section 19 of the appropriate Electronic Control System Troubleshooting and Repair Manual.]]
> 6. Use the electronic service tool to monitor the multiplexed components or switches for a change of state or value that can contribute to the symptom. This information is useful in narrowing down which components are contributing to the symptom.
> 7. These components can be enabled and source addressed for multiplexing under the SAE J1939 multiplexing feature. If any of the components are **not** changing state, document the component and verify the components are enabled and source addressed for multiplexing. A quick check to investigate if a component is multiplexed is to inspect the wiring harness to verify that the component wires are routed to the Cummins® ECM. If wires are **not** present for the component in question, it is an indication the component or switch **must not** be multiplexed. Contact the OEM for the J1939 multiplexing settings.
> 8. If there are **not** any issues with ECM communication, data link adapter, harness or setup for multiplexing, the OEM **must** be contacted to determine further troubleshooting actions.
>
> ### Document History
