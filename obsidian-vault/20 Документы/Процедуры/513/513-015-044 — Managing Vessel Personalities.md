---
type: "Процедура"
doc: "513-015-044"
title_en: "Managing Vessel Personalities"
modified: "2025-05-12"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "5411480"
figures: 17
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-015-044.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-015-044.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
  - "перевод/машинный"
---

# Managing Vessel Personalities

> [!abstract] Процедура · `513-015-044`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section 15 - Instruments and Controls - Group 15
> **Даты:** изменён 2025-05-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-015-044.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-015-044.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Выбор сервисного инструмента

ЭД-4

#### Рекомендованный сервисный инструмент Cummins®

- Универсальный удлинитель шины (USB), номер детали 5394862 (при необходимости для доступа).

#### Дополнительные сервисные позиции

- USB-накопитель

ED-5 и ED-7

#### Рекомендованный сервисный инструмент Cummins®

- Универсальный удлинитель шины (USB), номер детали 5394862 (при необходимости для доступа).

#### Дополнительные сервисные позиции

- USB-накопитель

### Общие сведения

ЭД-4

Дисплей Cummins® C Command Connect и Connect Premier Marine Panel System ED-4 предварительно загружены программным обеспечением с завода. Программное обеспечение для отображения Cummins® ED-4 и VPF должны быть обновлены и настроены до надлежащей работы дисплея.

> [!note] Примечание
> Обычно метка находится в C.I.B. для ссылки на программное обеспечение и файл VPF, загруженный во главе и C.I.B. ЭД-4 при первоначальной установке системы у изготовителя оригинального оборудования (ОЭМ). Этот тег должен быть обновлен после модификации программного обеспечения ED-4 или VPF.

Система **должна быть установлена для судна, в котором она установлена для максимальной производительности. Дисплеи ED-4** должны быть обновлены с помощью VPF, который специфичен для OEM-производителя и модели судна. Необходимо загрузить наиболее актуальный для судна ВПФ. Если вы меняете VPF по другим причинам, рассмотрите множество факторов, которые могут способствовать производительности, таких как:

- Датчики судов
- ED-4 display location (C.I.B. или шлем
- Количество двигателей
- Количество станций рулевого управления.

Веб-страница Cummins® QuickServe® Online содержит таблицу отслеживания и файлы. После ввода серийного номера двигателя или поиска модели двигателя веб-страницу можно найти, нажав на следующие ссылки: Сервис, связанная с ним информация, обновления прошивки для морских панелей и ED-4.

Cummins® QuickServe® Online webpage; Marine Panel Firmware Updates – ED-4, содержит файлы и таблицу отслеживания с информацией о каждом файле, которая помогает выбрать правильный уровень файла и уровня редактирования для компонента.

> [!note] Примечание
> Группа Cummins® Marine Application Engineering создает файлы личности судна и обновляет «Справочник отслеживания личных файлов судна Cummins ED-4» с именем файла, версией и описанием судна, приложения, оборудования и информации датчика судна.

Формат имени файла ниже является примером. Смотрите таблицу отслеживания для конкретной информации.

Формат имени VPF: "0000 ACSOPOS1 44DXXX.zip"

Где:

000 = ED-4 Display VPF Version (000 - шестнадцатеричный индекс для VPF)

0 = Пересмотр ВПФ

Стратегия адреса источника

C = Тип приложения

SO = Устройство 1

PO = устройство 2

S1 = Специальный

44DXXX = OEM описание

«.zip» — расширение файла

> [!note] Примечание
> «Cummins ED-4 Display Vessel Personality File Tracking Sheet» содержит вкладку «VPF file name key», которая содержит информацию для расшифровки формата имени файла VPF.

Файл VPF.zip должен быть сохранен в папке с именем «VPF» на USB-накопителе. Файл не должен быть расшифрован, так как ED-4 может обнаружить и загрузить файл как a.zip.

После настройки ED-4, VPF может быть сохранен, экспортирован и импортирован в другие VPF на судне.

Пример типичной структуры файла/папки USB-накопителя для программного обеспечения ED-4 и VPF.

![[15e00090.png]]

> [!note] Примечание
> Файлы в папках с именем «VPF» и «LOGS» должны быть удалены на USB-накопителе до сохранения файлов с веб-страницы Cummins® QuickServe® Online.

> [!note] Примечание
> Несколько файлов VPF можно сохранить в папке «VPF» на USB-накопителе.

ED-5 и ED-7

Дисплей Cummins® C Command Connect и Connect Premier Marine Panel System ED-5/ED-7 предварительно загружены программным обеспечением с завода. Дисплей Cummins® ED-5/ED-7 VPF должен быть сконфигурирован до надлежащей работы дисплея в соответствии с потребностями, характерными для OEM-производителя и модели судна.

Если необходимо обновить программное обеспечение отображения ED-5/ED-7 в полевых условиях, веб-страница Cummins® QuickServe® Online содержит лист отслеживания и файлы. После ввода серийного номера двигателя или поиска модели двигателя веб-страницу можно найти, нажав на следующие ссылки: Сервис, связанная с ним информация, обновления прошивки для морских панелей и ED-5 / ED-7.

Cummins® QuickServe® Online webpage; Marine Panel Firmware Updates – ED-5/ED-7, содержит файлы и таблицу отслеживания с информацией о темах/конфигурации, доступной в программном пакете, что помогает выбрать правильную тему для удовлетворения потребностей приложения.

### Подготовительные операции

ЭД-4

> [!danger] ОПАСНО
> Для уменьшения возможности получения травм или повреждения оборудования, эта процедура должна выполняться только квалифицированными специалистами по обслуживанию.

> [!warning] ОСТОРОЖНО
> Перед обновлением программного обеспечения или VPF в любом компоненте системы управления убедитесь, что система управления судном полностью работоспособна. Также важно проверить и задокументировать настройки конфигурации и индивидуальность сосуда компонента.

![[15e00155.png]]

Программное обеспечение и VPF-информацию дисплея ED-4 можно просмотреть, нажав клавишу 5 или «Меню» на странице экрана данных.

Действие:

- Нажмите клавишу 5 или «Меню».
- Выберите «О нас» и нажмите клавишу 4 или «Войти».
- Нажмите клавишу 3 или «VPF» для информации о VPF.
- Нажмите клавишу 4 или «Информация» для информации о программном обеспечении.

Важная информация на странице, которая жестко закодирована в VPF.

- Идентифицирующая информация, хранящаяся в VPF, будет отображаться в верхней части экрана.
- Версия - версия и доработка VPF.
- Модифицированный по - ED-4 программный серийный номер, на котором был изменен ВПФ.
- Краткое описание - имя файла VPF.
- Формат имени файла VPF и информация о возможностях VPF, таких как количество двигателей, датчиков судна и местоположение ED-4, для которого должен использоваться VPF.

> [!note] Примечание
> После изменения настроек и настроек конфигурации ED-4 информация в кратком и длинном описании может перестать быть действительной.

Когда закончите:

Нажмите клавишу 5 или «Назад», чтобы выйти из страницы.

Нажмите клавишу 5 или «Выход» для возврата на страницу экрана данных.

Перед загрузкой VPF документируйте и понимайте характеристики судна и коды аварийной сигнализации / неисправности. Следуйте коду тревоги / ошибки или соответствующему дереву симптомов устранения неполадок, чтобы понять проблемы. Ссылка на следующие процедуры для тестирования и настройки конфигурации информации:

- Проверить правильность функции.[[513-015-047 — Final Verification|См. процедуру 015-047 в разделе 15.]].
- Загрузите файлы журналов с дисплея ED-4 для будущего использования.[[513-015-035 — Display(s) and Instrumentation|См. процедуру 015-035 в разделе 15.]].
- Документируйте программное обеспечение отображения ED-4, VPF, адрес(ы) источника и настройки конфигурации.[[513-015-108 — Display Configuration|См. процедуру 015-108 в разделе 15.]].
- При необходимости экспортируйте существующие ВПФ, используемые ЭД-4. См. раздел Экспорт ниже.
- Используйте следующую процедуру для поиска и выбора программного обеспечения ED-4, когда требуется обновление.[[513-015-107 — Display Software|См. процедуру 015-107 в разделе 15.]].

ED-5 и ED-7

> [!danger] ОПАСНО
> Для уменьшения возможности получения травм или повреждения оборудования, эта процедура должна выполняться только квалифицированными специалистами по обслуживанию.

> [!warning] ОСТОРОЖНО
> Перед обновлением программного обеспечения или VPF в любом компоненте системы управления убедитесь, что система управления судном полностью работоспособна. Также важно проверить и задокументировать настройки конфигурации и индивидуальность сосуда компонента.

![[00e00314.png]]

![[00e00315.png]]

Программное обеспечение и информация о теме/конфигурации дисплея ED-5/ED-7 можно просматривать, зайдя в меню с дисплея.

Действие:

- Нажмите и удерживайте в середине экрана или выберите значок «Menu» (I) с экрана или нажмите и удерживайте кнопку выбора на удаленной клавиатуре, если она установлена.
- Выберите «О» для идентификации программного обеспечения.
- Выберите «Конфигурация» для информации VPF.

Важная информация на странице:

- Версия конфигурации – будет отображать установленную конфигурацию программного обеспечения. Программный пакет, выпущенный на Cummins® QuickServe® Online Marine Firmware, будет идентифицирован с этой информацией.
- Текущая тема - будет отображать тему, которая в настоящее время активна на дисплее ED-5 / ED-7.

Когда закончите:

- Прокрутите слева направо на экране или используйте, когда в структуре меню, чтобы вернуться на последнюю страницу или выйти из меню.

### Настройка информации

ЭД-4

Доступ к USB-порту на задней панели дисплея ED-4 путем удаления порта уплотнения.

Для Си Би. ED-4 дисплеи, используйте следующую процедуру для получения информации о доступе к ED-4 дисплею USB порта. См. процедуру 015-023 в разделе 15.

> [!note] Примечание
> Важно проверить, правильно ли установлен резиновый порт USB-уплотнения после обновления программного обеспечения или VPF. Если ED-4 не находится в состоянии покоя, то он может подвергаться воздействию окружающей среды и вызывать внутренние повреждения.

![[15e00095.png]]

ED-5 и ED-7

Доступ к USB-порту на задней панели дисплея ED-5/ED-7 путем удаления порта уплотнения.

> [!note] Примечание
> Важно проверить, правильно ли установлен резиновый порт USB-уплотнения после обновления программного обеспечения. Если ED-5/ED-7 не подвергается воздействию окружающей среды и может привести к внутреннему повреждению.

![[00e00316.png]]

### экспорт

ЭД-4

VPF может быть экспортирован, если ED-4 заменяется на событие обслуживания или конфигурация может быть использована в других местах ED-4 на судне.

Процесс экспорта активного VPF, используемого дисплеем ED-4, заключается в следующем.

> [!note] Примечание
> Рекомендуется очистить папку VPF перед экспортом VPF на USB-накопитель.

1. Включите систему, включите включение питания переключателя, выключите двигатель и проверьте, включен ли экран дисплея ED-4.
2. Подключите USB-накопитель к порту ED-4 USB.

После того, как USB-накопитель будет обнаружен ED-4, будут показаны следующие параметры:

1. Загрузить VPF
2. Сохранить текущий VPF
3. Экспортный журнал(ы)
4. Выполняйте обновление программного обеспечения.

Действие:

- Нажмите клавишу 2 или «Down», чтобы прокрутить «Сохранить текущий VPF».
- Нажмите клавишу 4 или «Сохранить».

Прочитайте подсказки на экране ED-4 во время процесса экспорта.

**Не** Удалите питание на ED-4 или USB-накопитель во время процесса экспорта.

> [!note] Примечание
> Если сообщение с сигналом тревоги появляется во время установки USB-накопителя, нажмите клавишу 5 или «Закрыть», чтобы подтвердить и удалить сообщение. Затем нажмите клавишу 5 или «Menu», чтобы вернуться к параметрам USB-накопителя.

> [!note] Примечание
> Потребуется около 1 минуты, чтобы экспортировать VPF с ED-4 на USB-накопитель.

Файл будет сохранен в папке «VPF» на USB-накопителе. Имя файла будет включать в себя серийный номер программного обеспечения дисплея ED-4.

Пример: экспортный VPF\_33403.zip

Экспорт VPF с ED-4 с тем же программным серийным номером перезапишет существующий VPF, сохраненный на USB-накопителе.

После сохранения на USB-накопитель рекомендуется переименовать файл перед его использованием в других ED-4(ах). См. формат, показанный в разделе «Общая информация» выше.

![[15e00122.png]]

ED-5 и ED-7

Конфигурация может быть экспортирована из ED-5/ED-7, поэтому конфигурация может быть использована в других местах ED-5/ED-7 на судне.

Процесс экспорта конфигурации, используемой дисплеем ED-5/ED-7, заключается в следующем.

1. Включите систему, включите включение питания переключателя, выключите двигатель и проверьте, включен ли экран дисплея ED-5/ED-7.
2. Подключите USB-накопитель к порту ED-5/ED-7 USB.
3. После того, как USB-накопитель будет обнаружен ED-5/ED-7, будут показаны следующие параметры:

![[00e00317.png]]

Действие:

- Скролл к «Загрузить файлы конфигурации».
- Прокрутите слева направо, чтобы выбросить USB.

Прочитайте подсказки на экране ED-5/ED-7 во время процесса экспорта. В ED-5/ED-7 будут показаны подсказки "Конфигурация загрузки. Полная копия. Выкинуть USB перед удалением".

**Не** Удалите питание на ED-5/ED-7 или удалите USB-накопитель во время процесса экспорта.

Конфигурационные файлы будут сохранены в папке 1536-software serial number_config на USB-накопителе. Название папки будет включать в себя программный серийный номер дисплея ED-5/ED-7.

Пример экспортируемой папки конфигурации: 1536-459434\_config

Экспорт конфигурационных файлов с ED-5/ED-7 с тем же программным серийным номером перезапишет существующую конфигурацию, сохраненную на USB-накопителе.

После сохранения на USB-накопитель файлы конфигурации могут быть упакованы с поддержкой инженерии клиента, прежде чем они будут использованы в других дисплеях ED-5/ED-7.

![[00e00318.png]]

### импортировать

ЭД-4

> [!note] Примечание
> Перед обновлением VPF документируйте адрес (адреса) источника (источников) ED-4 и настройки конфигурации. См. раздел подготовительные шаги выше.

> [!note] Примечание
> Каждый дисплей ED-4 на судне имеет собственное USB-соединение, и VPF должен быть обновлен отдельно для каждого.

Процесс загрузки VPF на дисплей ED-4 выглядит следующим образом.

1. Включите систему, включите включение питания переключателя, выключите двигатель и проверьте, включен ли экран дисплея ED-4.
2. Подключите USB-накопитель к порту ED-4 USB.

После того, как USB-накопитель будет обнаружен ED-4, будут показаны следующие параметры:

1. Загрузить ВПФ.
2. Сохранить текущий VPF.
3. Экспортный журнал(ы).
4. Выполняйте обновление программного обеспечения.

Действие:

- Нажмите клавишу 2 или «Вниз», чтобы прокрутить «Загрузить VPF».
- Нажмите клавишу 4 или «Выбрать».

Прочитайте подсказки на экране ED-4 во время импорта.

> [!note] Примечание
> **Не** Удалите питание на ED-4 или USB-накопитель во время импорта.

> [!note] Примечание
> Если сообщение с сигналом тревоги появляется во время установки USB-накопителя, нажмите клавишу 5 или «Закрыть», чтобы подтвердить и удалить сообщение. Затем нажмите клавишу 5 или «Menu», чтобы вернуться к параметрам USB-накопителя.

![[15e00123.png]]

Выберите VPF для загрузки.

Действие:

- Нажмите клавишу 2 или «Вниз», чтобы выделить VPF.
- Нажмите клавишу 4 или «Загрузка».

На следующем экране:

- Нажмите клавишу 1 или «Fav», чтобы сохранить в качестве любимого во внутренней памяти ED-4.
- Нажмите клавишу 3 или «Да», чтобы продолжить выбор.
- Нажатие клавиши 5 или «Нет» вернется на главный экран выбора.

Прочитайте подсказки на экране ED-4 во время импорта.

> [!note] Примечание
> **Не** Удалите питание на ED-4 или USB-накопитель во время импорта.

> [!note] Примечание
> Для импорта VPF с USB-накопителя на ED-4 требуется около 5 минут.

> [!note] Примечание
> Нажатие клавиши 1 или «Fav» сохранит выбранный VPF в качестве Фаворита во внутренней памяти ED-4. См. Загрузка библиотеки ниже для доступа и информации.

![[15e00156.png]]

ED-4 будет циклично использовать свою мощность и возобновлять работу после импорта VPF.

> [!note] Примечание
> Не удаляйте USB-накопитель из ED-4, если не указано это сделать.

Действие:

- Нажмите клавишу 5 или «Выбросить», чтобы завершить интерфейс ED-4 с USB-накопителем.

Прочитайте подсказки на экране ED-4 и удалите USB-накопитель, когда вам это будет предложено.

Проверьте, что ED-4 использует импортную VPF, перейдя на страницу «О нас». См. подготовительные шаги выше.

![[15e00125.png]]

### Библиотека Загрузка

ЭД-4

ED-4 может иметь VPF, хранящиеся локально.

Процесс доступа к библиотеке VPF на ЭД-4 выглядит следующим образом.

Включите систему, включите включение питания переключателя, выключите двигатель и проверьте, включен ли экран дисплея ED-4.

Действие:

- Нажмите клавишу 5 или «Меню».
- Нажмите клавишу 2 или «Вниз», чтобы прокрутить до «Конфигурация». Нажмите клавишу 4 или «Войти».
- Нажмите клавишу 1 или «Принять».
- Нажмите клавишу 2 или «Down», чтобы прокрутить до «VPF». Нажмите клавишу 4 или «Войти».
- Просмотрите VPF, доступные на экране ED-4. Нажмите клавишу 2 или «Вниз», чтобы прокрутить до нужного «VPF». Нажмите клавишу 4 или «Загрузка».

![[15e00126.png]]

Действие:

- Нажмите клавишу 3 или «Да», чтобы продолжить.
- Нажмите клавишу 5 или «Нет», чтобы отменить, которая возвращается на предыдущий экран выбора.

Если VPF был выбран в качестве «Любимого» при загрузке с USB-накопителя, это будет активный VPF, используемый ED-4. Изменения настройки и настройки ED-4 сохраняются во внутренней памяти ED-4. Чтобы обновить локально сохраненный VPF, VPF должен быть экспортирован на USB-накопитель, а затем импортирован обратно в ED-4 и сохранен как «любимое».

> [!note] Примечание
> Во время импорта VPF нажмите клавишу 1 или «Fav», чтобы сохранить выделенный VPF в качестве фаворита в ED-4. Обычно это делается после изменения настроек конфигурации в ED-4.

> [!note] Примечание
> Для загрузки VPF из памяти ED-4 требуется около 5 минут.

> [!note] Примечание
> **Не** Удалите питание на ЭД-4 во время процесса нагрузки ВПФ.

![[15e00156.png]]

ED-5 и ED-7

ED-5/ED-7 имеет VPF/темы, хранящиеся локально.

Процесс доступа к темам на ED-5/ED-7 выглядит следующим образом.

Включите систему, включите включение питания переключателя, выключите двигатель и проверьте, включен ли экран дисплея ED-5/ED-7.

Действие:

- Выберите «Setup».
- Выберите «Темы».

![[15e00200.png]]

Действие:

- Выберите «Настройка» с помощью сенсорного экрана или удаленной клавиатуры.
- Выберите «Темы» с помощью сенсорного экрана или удаленной клавиатуры.
- Выберите «Тема» с помощью сенсорного экрана или удаленной клавиатуры.
- Выберите файл личности сосуда с экрана «Выбрать тему», чтобы использовать его на дисплее.

![[15e00201.png]]

Когда закончите:

- Прокрутите слева направо или используйте мягкий ключ «Назад» (IV) на экране, чтобы выйти или нажать клавишу «Возвращение / Выход» на удаленной клавиатуре, чтобы сохранить настройку.

![[15e00202.png]]

### устранение неполадок

ЭД-4

USB ошибка

После подключения USB-накопителя к ED-4 сообщение об ошибке USB может быть замечено при подключении к компьютеру. Это нормально из-за совместимости операционной системы между средой разработки (Linux), используемой для создания и запуска программного обеспечения ED-4 с компьютером, работающим на другой операционной системе (WindowsTM). Это не функциональная проблема, а то, как ведет себя система.

Если вы не можете перенести файл с компьютера на USB-накопитель, попробуйте следующее:

Получите новый файл, сохраните его на USB-накопитель и попробуйте снова. Файл может быть поврежден или изменен. Файлы, измененные из несанкционированного источника, будут **не** читаться правильно и могут **не** загружаться.

Если есть проблема, которая не позволяет ED-4 VPF загружаться, попробуйте следующее:

1. Проверьте, используется ли правильный USB-накопитель. Если необходимо, попробуйте использовать другой USB-накопитель.
2. Проверьте, существует ли папка «VPF» на USB-накопителе.
3. Проверьте, включен ли переключатель системы, и включен дисплей ED-4.
4. Проверьте, что USB и кабель расширения (если используется) подключены надежно.
5. После установки USB-накопителя оставьте USB-накопитель подключенным к дисплею в течение 1 минуты, чтобы дать время для распознавания USB-накопителя.
6. После установки USB-накопителя, питание цикла на ED-4 с помощью системы включает переключатель.
7. Попробуйте снова процесс загрузки.

Если ED-4 не распознает USB-накопитель после его подключения, питание цикла к ED-4 с помощью системы включает переключатель.

> [!note] Примечание
> Если USB-накопитель удален без нажатия клавиши 5 или «выброс», ED-4 будет **не** распознавать USB-накопитель снова, пока питание на ED-4 не будет циклично.

Если выключатель системы включен или питание прервано на ED-4 до завершения загрузки VPF, VPF будет **не** обновляться в ED-4. Если ошибка произошла, попробуйте следующее:

- Установите USB-накопитель и попробуйте снова.

> [!note] Примечание
> Система включения цикла переключения OFF-ON может быть выполнена для перезагрузки ED-4 с предыдущей установленной версией VPF.

Связанные с файлами сбои:

- Если в пакете VPF имеются ошибки или несовместимая версия, то на ED-4 отображается сообщение "Проблема с VPF. Описание в журнале событий
- Если файл VPF неполный на USB-накопителе, ED-4 **не** предоставит ключ «Да» для начала загрузки ключа VPF или «Fav» для установки любимого VPF.

Если ошибка произошла, попробуйте следующее:

- Получите новый файл, сохраните его на USB-накопитель и попробуйте снова.

> [!note] Примечание
> Система включения OFF-ON может быть выполнена для перезагрузки ED-4 с предыдущей установленной версией VPF.

Неисправности, связанные с процессом, требующие восстановления ЭД-4:

Если USB-накопитель удаляется до завершения загрузки VPF, ED-4 застрянет на сообщении «Установка VPF» на экране с последующим красным экраном. После включения системы OFF-ON ED-4 будет застревать на сером экране.

Если ошибка возникает, этапы восстановления для ED-4:

1. Включите выключатель System Enable OFF.
2. Загрузите правильный пакет программного обеспечения ED-4 на USB-накопитель.
3. Установите USB-накопитель.
4. Держите ключ 1 и ключ 5.
5. Включите системный включатель.
6. ED-4 начнет загрузку программного обеспечения для восстановления из промежуточного нефункционального состояния, в котором находился блок ED-4.

ED-5 и ED-7

USB ошибка

После подключения USB-накопителя к ED-5/ED-7 сообщение об ошибке USB может быть замечено при подключении к компьютеру. Это нормально из-за совместимости операционной системы между средой разработки (Linux), используемой для создания и запуска программного обеспечения ED-5 / ED-7 с компьютером, работающим на другой операционной системе (Windows TM). Это не функциональная проблема и как ведет себя система.

Если вы не можете перенести файл с компьютера на USB-накопитель, попробуйте следующее:

Получите новый файл, сохраните его на USB-накопитель и попробуйте снова. Файл может быть поврежден или изменен. Файлы, измененные из несанкционированного источника, будут **не** читаться правильно и могут **не** загружаться.

Если ED-5/ED-7 не распознает USB-накопитель после его подключения, то питание цикла ED-5/ED-7 с помощью системы включает переключатель и снова пробует.

> [!note] Примечание
> Если USB-накопитель удален без выбора опции Eject USB, ED-5/ED-7 будет **не** распознавать USB-накопитель снова, пока питание ED-5/ED-7 не будет циклично.

> [!note] Примечание
> Система включения переключателя цикла OFF-ON может быть выполнена для перезагрузки ED-5/ED-7 с предыдущей установленной версией VPF.

Обновление загрузчика в программном обеспечении потребует выполнения этапов восстановления ED-5/ED-7.

Неисправности, связанные с процессом, требующие восстановления ED-5/ED-7:

Если USB-накопитель удален до того, как ED-5/ED-7 завершит обновление программного обеспечения, или при попытке загрузить обновление программного обеспечения продолжает показывать сообщение «Успешный отказ от USB».

Если ошибка возникает, этапы восстановления для ED-5/ED-7:

1. Включите выключатель System Enable OFF.
2. Загрузите правильный пакет программного обеспечения ED-5 / ED-7 на USB-накопитель.
3. Установите USB-накопитель.
4. Используя небольшой отвертку нажмите и удерживайте красную кнопку рядом с портом USB.
5. Включите системный включатель.
6. ED-5/ED-7 начнет загрузку программного обеспечения для восстановления из промежуточного нефункционального состояния, в котором находился блок ED-5/ED-7.

### Завершающие операции

ЭД-4

> [!warning] ОСТОРОЖНО
> После обновления программного обеспечения или VPF в любом компоненте системы управления убедитесь, что система управления судном полностью работоспособна. Также важно проверить и обновить настройки конфигурации и индивидуальность сосуда компонента.

После обновления VPF дисплея ED-4 обратитесь к следующим процедурам для настройки конфигурации и тестирования:

- Для настройки используйте следующую процедуру.[[513-015-108 — Display Configuration|См. процедуру 015-108 в разделе 15.]]. Дисплей ED-4 может быть настроен по-разному в зависимости от его местоположения.
- Для настройки используйте следующую процедуру.[[513-101-013 — General Operating Instructions|См. процедуру 101-013 в разделе]]1.
- Все функции управления Cummins® Marine Controls должны быть протестированы перед выходом из дока после служебного мероприятия.[[513-015-047 — Final Verification|См. процедуру 015-047 в разделе 15.]].

После обновления VPF, если есть новый код тревоги или жалоба на производительность, следуйте коду тревоги или соответствующему дереву симптомов устранения неполадок, чтобы понять, работает ли личность должным образом и является ли она подходящей личностью для приложения.

Если есть подозрение, что файл личности судна работает некорректно, убедитесь, что соответствующий файл был загружен для двигателя, оборудования и приложения.

> [!note] Примечание
> На веб-странице Cummins® QuickServe® Online «Сборник личных файлов судна Cummins ED-4 Display» представлена информация об изменениях, внесенных в файл личности судна. Эта информация может быть использована для установления, существует ли общность между изменениями, внесенными в личность, и наблюдаемыми симптомами.

ED-5 и ED-7

> [!warning] ОСТОРОЖНО
> После обновления программного обеспечения или VPF в любом компоненте системы управления убедитесь, что система управления судном полностью работоспособна. Также важно проверить и обновить настройки конфигурации и индивидуальность сосуда компонента.

После обновления конфигурации дисплея ED-5/ED-7 обратитесь к следующим процедурам для информации о настройке конфигурации и тестирования:

- Для настройки используйте следующую процедуру.[[513-015-108 — Display Configuration|См. процедуру 015-108 в разделе 15.]]Дисплей ED-5/ED-7 может быть настроен по-разному в зависимости от его местоположения.
- Все функции управления Cummins® Marine Controls должны быть протестированы перед выходом из дока после служебного мероприятия.[[513-015-047 — Final Verification|См. процедуру 015-047 в разделе 15.]]


> [!quote]- Original (English) · английский оригинал
> ### Select Service Tools
>
> ED-4
>
> #### Recommended Cummins® Service Tools
>
> - Universal serial bus (USB) extension cable, Part Number 5394862 (if needed for access).
>
> #### Additional Service Items
>
> - USB drive
>
> ED-5 and ED-7
>
> #### Recommended Cummins® Service Tools
>
> - Universal serial bus (USB) extension cable, Part Number 5394862 (if needed for access).
>
> #### Additional Service Items
>
> - USB drive
>
> ### General Information
>
> ED-4
>
> The Cummins® C Command Connect and Connect Premier Marine Panel System ED-4 display(s) are preloaded with software from the factory. The Cummins® ED-4 display software and VPF **must** be updated and configured prior to proper operation of the display.
>
> **Note · Примечание**
> A tag is typically located in the C.I.B. for referencing the software and VPF file loaded in the helm and C.I.B. ED-4s during initial system installation at the original equipment manufacturer (OEM). This tag should be updated after ED-4 software or VPF modification.
>
> The system **must** be set up for the vessel in which it is installed in for maximum performance. ED-4 displays **must** be updated with a VPF that is specific to the vessel OEM and model. It is necessary to load the most current VPF for the vessel. If changing a VPF for other reasons, consider the many factors that can contribute to performance such as the following:
>
> - Vessel sensors
> - ED-4 display location (C.I.B. or Helm)
> - Number of engines
> - Number of helm stations.
>
> The Cummins® QuickServe® Online webpage contains a tracking sheet and files. After entering the engine serial number or engine model search, the webpage can be found by clicking the following links: Service, Related Information, Marine Panel Firmware Updates, and ED-4.
>
> Cummins® QuickServe® Online webpage; Marine Panel Firmware Updates – ED-4, contains files and a tracking sheet with information about each file, which helps select the correct file and revision level for the component.
>
> **Note · Примечание**
> The Cummins® Marine Application Engineering group creates the vessel personality files and updates the “Cummins ED-4 Display Vessel Personality File Tracking Sheet” with file name, version, and description of the vessel, application, equipment, and vessel sensor information.
>
> The file name format below is an example. Refer to the tracking sheet for specific information.
>
> The VPF name format: “0000 ACSOPOS1 44DXXX.zip”
>
> Where:
>
> 000 = ED-4 Display VPF Version (000 - Hexadecimal Index for VPF)
>
> 0 = VPF Revision
>
> A = Source Address Strategy
>
> C = Application Type
>
> SO = Device 1
>
> PO = Device 2
>
> S1 = Special Feature
>
> 44DXXX = OEM Description
>
> “.zip” = File Extension
>
> **Note · Примечание**
> The “Cummins ED-4 Display Vessel Personality File Tracking Sheet” contains a tab called “VPF file name key” which contains information to decipher the VPF file name format.
>
> The VPF.zip file **must** be saved to a folder named “VPF” on the USB drive. The file does **not** need to be unzipped since the ED-4 can detect and load the file as a.zip.
>
> Once the ED-4 is configured, the VPF can be saved, exported, and imported to other VPFs on the vessel.
>
> Example of a typical file / folder structure of the USB drive for ED-4 software and VPF.
>
> **Note · Примечание**
> The files in the folders named “VPF” and “LOGS” should be cleared on the USB drive prior to saving files from the Cummins® QuickServe® Online webpage.
>
> **Note · Примечание**
> Multiple VPF files can be saved in the “VPF” folder on the USB drive.
>
> ED-5 and ED-7
>
> The Cummins® C Command Connect and Connect Premier Marine Panel System ED-5/ED-7 display(s) are preloaded with software from the factory. The Cummins® ED-5/ED-7 display VPF **must** be configured prior to proper operation of the display according to needs specific to the vessel OEM and model.
>
> If it is necessary to update the ED-5/ED-7 display software in field the Cummins® QuickServe® Online webpage contains a tracking sheet and files. After entering the engine serial number or engine model search, the webpage can be found by clicking the following links: Service, Related Information, Marine Panel Firmware Updates, and ED-5/ED-7.
>
> Cummins® QuickServe® Online webpage; Marine Panel Firmware Updates – ED-5/ED-7, contains files and a tracking sheet with information about themes/configuration available in the software package, which helps select the correct theme to meet application need.
>
> ### Preparatory Steps
>
> ED-4
>
> **WARNING · Опасно**
> To reduce the possibility of personal injury or equipment damage, this procedure must only be performed by suitably qualified service technicians.
>
> **CAUTION · Осторожно**
> Before updating the software or VPF in any control system component, verify that the Vessel Control System is completely operational. It is also important to test and document the configuration settings and vessel personality of the component.
>
> The software and VPF information of the ED-4 display can be viewed by pressing key 5 or “Menu” on the data screen page.
>
> Action:
>
> - Press key 5 or “Menu”.
> - Select “About” and press key 4 or “Enter”.
> - Press key 3 or “VPF” for VPF information.
> - Press key 4 or “Info” for software information.
>
> Important information on the page, which is hard coded in the VPF.
>
> - The identification information stored in the VPF will display across the top of the screen.
> - Version - VPF version and revision.
> - Modified By - ED-4 software serial number on which the VPF was modified.
> - Short Description - VPF file name.
> - Long Description - VPF file name format and information about the VPF capability, such as number of engines, vessel sensors, and ED-4 location for which the VPF should be used.
>
> **Note · Примечание**
> Once the ED-4 setup and configuration settings are modified, the information in the short and long description may no longer be valid.
>
> When finished:
>
> Press key 5 or “Back” to exit the page.
>
> Press key 5 or “Exit” to return to the data screen page.
>
> Prior to VPF download, document and understand the vessel performance and alarm/fault codes. Follow the alarm/fault code or the appropriate troubleshooting symptom tree to understand issues. Reference the following procedures for testing and configuration setup information:
>
> - Verify proper function. [[513-015-047 — Final Verification|Refer to Procedure 015-047 in Section 15]].
> - Download log files from the ED-4 display for future use. [[513-015-035 — Display(s) and Instrumentation|Refer to Procedure 015-035 in Section 15]].
> - Document the ED-4 display software, VPF, source address(s), and configuration settings. [[513-015-108 — Display Configuration|Refer to Procedure 015-108 in Section 15]].
> - If needed, export the existing VPF used by the ED-4. See Export section below.
> - Use the following procedure to find and select ED-4 software when updates are required. [[513-015-107 — Display Software|Refer to Procedure 015-107 in Section 15]].
>
> ED-5 and ED-7
>
> **WARNING · Опасно**
> To reduce the possibility of personal injury or equipment damage, this procedure must only be performed by suitably qualified service technicians.
>
> **CAUTION · Осторожно**
> Before updating the software or VPF in any control system component, verify that the Vessel Control System is completely operational. It is also important to test and document the configuration settings and vessel personality of the component.
>
> The software and theme/configuration information of the ED-5/ED-7 display can be viewed by accessing Menu from the display.
>
> Action:
>
> - Press and hold in the middle of screen or select “Menu”(I)” icon from the screen or press and hold on the select button on remote keypad if installed.
> - Select “About” for software identification.
> - Select “Config” for VPF information.
>
> Important information on the page:
>
> - Configuration Version – will display the software configuration installed. The software package released on Cummins® QuickServe® Online Marine Firmware will be identified with this information.
> - Current Theme – will display theme currently active on the ED-5/ED-7 display.
>
> When finished:
>
> - Swipe from left to right on the screen or use when in the Menu structure to return to last page or exit the menu.
>
> ### Setup Information
>
> ED-4
>
> Access the USB port on the rear of the ED-4 display by removing the seal port.
>
> For C.I.B. mounted ED-4 displays, use the following procedure for information on accessing the ED-4 display USB port. Refer to Procedure 015-023 in Section 15
>
> **Note · Примечание**
> It is important to verify the rubber USB seal port is properly installed afterward a software or VPF update. If **not**, the ED-4 may be exposed to the environment and result in internal damage.
>
> ED-5 and ED-7
>
> Access the USB port on the rear of the ED-5/ED-7 display by removing the seal port.
>
> **Note · Примечание**
> It is important to verify the rubber USB seal port is properly installed afterward a software update. If **not**, the ED-5/ED-7 may be exposed to the environment and result in internal damage.
>
> ### Exporting
>
> ED-4
>
> The VPF can be exported if an ED-4 is being replaced for a service event or the configuration can be used in other ED-4 locations on the vessel.
>
> The process of exporting the active VPF being used by the ED-4 display is as follows.
>
> **Note · Примечание**
> It is recommended that the VPF folder be cleared prior to exporting a VPF to the USB drive.
>
> 1. Turn the system enable switch power ON, engine OFF, and verify the ED-4 display screen is on.
> 2. Connect the USB drive to the ED-4 USB port.
>
> Once the USB drive is detected by the ED-4, the following options will be shown:
>
> 1. Load VPF
> 2. Save current VPF
> 3. Export log(s)
> 4. Perform software update.
>
> Action:
>
> - Press key 2 or “Down” to scroll to “Save current VPF”.
> - Press key 4 or “Save”.
>
> Read the prompts on the ED-4 screen during the exporting process.
>
> Do **not** remove power to the ED-4 or remove the USB drive during the export process.
>
> **Note · Примечание**
> If an alarm pop up message occurs while the USB drive is installed, press key 5 or “Close” to acknowledge and remove the message. Then, press key 5 or “Menu” to return to the USB drive options.
>
> **Note · Примечание**
> It takes approximately 1 minute to export a VPF from the ED-4 to the USB drive.
>
> The file will be saved to the “VPF” folder on the USB drive. The file name will include the software serial number of the ED-4 display.
>
> Example: exportedVPF\_33403.zip
>
> Exporting a VPF from an ED-4 with the same software serial number will overwrite the existing VPF saved on the USB drive.
>
> Once saved to the USB drive, it is recommended to rename the file before it is used in other ED-4(s). Refer to the format shown in the General Information section above.
>
> ED-5 and ED-7
>
> The configuration can be exported from an ED-5/ED-7 so the configuration can be used in other ED-5/ED-7 locations on the vessel.
>
> The process of exporting the configuration being used by the ED-5/ED-7 display is as follows.
>
> 1. Turn the system enable switch power ON, engine OFF, and verify the ED-5/ED-7 display screen is on.
> 2. Connect the USB drive to the ED-5/ED-7 USB port.
> 3. Once the USB drive is detected by the ED-5/ED-7, the following options will be shown:
>
> Action:
>
> - Scroll to “Offload Config Files”.
> - Swipe left to right to eject USB.
>
> Read the prompts on the ED-5/ED-7 screen during the exporting process. The ED-5/ED-7 will show prompts “Config Offload. Copy Complete. Eject USB before removing.”
>
> Do **not** remove power to the ED-5/ED-7 or remove the USB drive during the export process.
>
> The configuration files will be saved to the “1536-software serial number\_config” folder on the USB drive. The folder name will include the software serial number of the ED-5/ED-7 display.
>
> Example of exported configuration folder: 1536-459434\_config
>
> Exporting configuration files from an ED-5/ED-7 with the same software serial number will overwrite the existing configuration saved on the USB drive.
>
> Once saved to the USB drive, the configuration files can be packaged with support of customer engineering before it is used in other ED-5/ ED-7 displays.
>
> ### Importing
>
> ED-4
>
> **Note · Примечание**
> Prior to VPF update, document the ED-4 display(s) source address(s) and configuration settings. See the Preparatory Steps section above.
>
> **Note · Примечание**
> Each ED-4 display on the vessel has its own USB connection and the VPF **must** be updated separately to each.
>
> The process of loading a VPF to the ED-4 display is as follows.
>
> 1. Turn the system enable switch power ON, engine OFF, and verify the ED-4 display screen is on.
> 2. Connect the USB drive to the ED-4 USB port.
>
> Once the USB drive is detected by the ED-4, the following options will be shown:
>
> 1. Load VPF.
> 2. Save current VPF.
> 3. Export log(s).
> 4. Perform software update.
>
> Action:
>
> - Press key 2 or “Down” to scroll to “Load VPF”.
> - Press key 4 or “Choose”.
>
> Read the prompts on the ED-4 screen during the importing process.
>
> **Note · Примечание**
> Do **not** remove power to the ED-4 or remove the USB drive during the import process.
>
> **Note · Примечание**
> If an alarm pop up message occurs while the USB drive is installed, press key 5 or “Close” to acknowledge and remove the message. Then, press key 5 or “Menu” to return to the USB drive options.
>
> Select the VPF to load.
>
> Action:
>
> - Press key 2 or “Down” to highlight the VPF.
> - Press key 4 or “Load”.
>
> On the next screen:
>
> - Press key 1 or “Fav” to save as the favorite in the ED-4 internal memory.
> - Press key 3 or “Yes” to continue with the selection.
> - Pressing key 5 or “No” will return to main selection screen.
>
> Read the prompts on the ED-4 screen during the importing process.
>
> **Note · Примечание**
> Do **not** remove power to the ED-4 or remove the USB drive during the import process.
>
> **Note · Примечание**
> It takes approximately 5 minutes to import a VPF from the USB drive to the ED-4.
>
> **Note · Примечание**
> Pressing key 1 or “Fav” will save the selected VPF as the Favorite in the ED-4 internal memory. See Library Loading below for access and information.
>
> The ED-4 will cycle its power and restart after a VPF is imported.
>
> **Note · Примечание**
> Do **not** remove the USB drive from the ED-4 unless instructed to do so.
>
> Action:
>
> - Press key 5 or “Eject” to end ED-4 interface with the USB drive.
>
> Read the prompts on the ED-4 screen, and remove the USB drive when prompted to do so.
>
> Verify the ED-4 is using the imported VPF by accessing the “About” page. See Preparatory Steps above.
>
> ### Library Loading
>
> ED-4
>
> The ED-4 may have VPFs stored locally.
>
> The process of accessing the VPF library on the ED-4 is as follows.
>
> Turn the system enable switch power ON, engine OFF, and verify the ED-4 display screen is on.
>
> Action:
>
> - Press key 5 or “Menu”.
> - Press key 2 or “Down” to scroll to “Configuration”. Press Key 4 or “Enter”.
> - Press Key 1 or “Accept”.
> - Press key 2 or “Down” to scroll to “VPF”. Press Key 4 or “Enter”.
> - Review the VPFs available on the ED-4 screen. Press key 2 or “Down” to scroll to the desired “VPF”. Press Key 4 or “Load”.
>
> Action:
>
> - Press key 3 or “Yes” to continue.
> - Press key 5 or “No” to cancel which returns to the previous selection screen.
>
> If a VPF was selected as a “Favorite” while loading from a USB drive, it will be the active VPF used by the ED-4. ED-4 setup and configuration setting changes are saved to the internal memory of the ED-4. To update the locally stored VPF, the VPF **must** be exported to USB drive and then imported back into the ED-4 and saved as a “favorite”.
>
> **Note · Примечание**
> During the VPF importing, press key 1 or “Fav” to save the highlighted VPF as the favorite in the ED-4. This is typically done after configuration settings have been changed in the ED-4.
>
> **Note · Примечание**
> It takes approximately 5 minutes to load a VPF from the ED-4 memory.
>
> **Note · Примечание**
> Do **not** remove power to the ED-4 during the VPF load process.
>
> ED-5 and ED-7
>
> The ED-5/ED-7 have VPFs/Themes stored locally.
>
> The process of accessing the themes on the ED-5/ED-7 is as follows.
>
> Turn the system enable switch power ON, engine OFF, and verify the ED-5/ED-7 display screen is on.
>
> Action:
>
> - Select “Setup”.
> - Select “Themes”.
>
> Action:
>
> - Select “Setup” using touchscreen or remote keypad.
> - Select “Themes” using touch screen or remote keypad.
> - Select “Theme” using touch screen or remote keypad.
> - Select the vessel personality file from “Choose Theme” screen to use on the display.
>
> When finished:
>
> - Swipe left to right or use “Back”(IV) soft key on the screen to exit or press “Return/Exit” key on remote keypad to save the setting.
>
> ### Troubleshooting
>
> ED-4
>
> USB Error Message
>
> After a USB drive is connected to an ED-4, a USB error message may be noticed when plugged into a computer. This is normal due to the operating system interoperability between development environment (Linux) used to create and run the ED-4 software with the computer running on a different operating system (Windows™). It is **not** a functional issue, and is how the system behaves.
>
> If unable to transfer a file from the computer to the USB drive, try the following:
>
> Get a new file, save it to the USB drive, and try again. The file may have become corrupt or may have been modified. Files modified from an unauthorized source will **not** read correctly and can **not** be downloaded.
>
> If there is an issue that keeps the ED-4 VPF from loading, try the following:
>
> 1. Verify a proper USB drive is being used. If needed, try using a different USB drive.
> 2. Verify the folder “VPF” exists on the USB drive.
> 3. Verify the system enable switch is ON and ED-4 display is powered up.
> 4. Verify the USB and extension cable (if used) is plugged in securely.
> 5. After installing the USB drive, leave the USB drive plugged into the display for 1 minute to allow time to recognize the USB drive.
> 6. After installing the USB drive, cycle power to the ED-4 using the system enable switch.
> 7. Try the load process again.
>
> If the ED-4 does **not** recognize the USB drive after it is plugged in, cycle power to the ED-4 using the system enable switch.
>
> **Note · Примечание**
> If the USB drive is removed without pressing key 5 or “eject”, the ED-4 will **not** recognize the USB drive again until the power to the ED-4 is cycled.
>
> If the system enable switch is pushed OFF or power is interrupted to the ED-4 before the VPF download completes, the VPF will **not** be updated in the ED-4. If error occurs, try the following:
>
> - Install the USB drive and try again.
>
> **Note · Примечание**
> System enable switch cycle OFF-ON can be done to reboot ED-4 with previous installed version of VPF.
>
> File related failures:
>
> - If the VPF file package has errors or an incompatible version, the ED-4 shows the message "Problem with VPF. Description in Event Log"
> - If the VPF file is incomplete on the USB drive, the ED-4 will **not** provide the key “Yes” to start the upload of the VPF or “Fav” key to set the favorite VPF.
>
> If error occurs, try the following:
>
> - Get a new file, save it to the USB drive, and try again.
>
> **Note · Примечание**
> System enable OFF-ON can be done to reboot ED-4 with previous installed version of VPF.
>
> Process related failures requiring an ED-4 recovery:
>
> If the USB drive is removed before the VPF download completes, the ED-4 will get stuck at the message "Installing VPF" on screen followed by a red screen. After a system enable OFF-ON, the ED-4 will be stuck at gray screen.
>
> If an error occurs, recovery steps for ED-4 are:
>
> 1. Turn System Enable switch OFF.
> 2. Load the correct ED-4 software package on the USB drive.
> 3. Install the USB drive.
> 4. Hold Key 1 and Key 5.
> 5. Turn System Enable switch ON.
> 6. ED-4 will start loading the software to recover from the intermediate non-functional state the ED-4 unit had been in.
>
> ED-5 and ED-7
>
> USB Error Message
>
> After a USB drive is connected to an ED-5/ED-7, a USB error message may be noticed when plugged into a computer. This is normal due to the operating system interoperability between development environment (Linux) used to create and run the ED-5/ED-7 software with the computer running on a different operating system (Windows™). It is **not** a functional issue and is how the system behaves.
>
> If unable to transfer a file from the computer to the USB drive, try the following:
>
> Get a new file, save it to the USB drive, and try again. The file may have become corrupt or may have been modified. Files modified from an unauthorized source will **not** read correctly and can **not** be downloaded.
>
> If the ED-5/ED-7 does **not** recognize the USB drive after it is plugged in, cycle power to the ED-5/ED-7 using the system enable switch and try again.
>
> **Note · Примечание**
> If the USB drive is removed without selecting Eject USB option, the ED-5/ED-7 will **not** recognize the USB drive again until the power to the ED-5/ED-7 is cycled.
>
> **Note · Примечание**
> System enable switch cycle OFF-ON can be done to reboot ED-5/ED-7 with previous installed version of VPF.
>
> Boot loader update in the software will require the ED-5/ED-7 recovery steps to be performed.
>
> Process related failures requiring an ED-5/ED-7 recovery:
>
> If the USB drive is removed before the ED-5/ED-7 completed the software update or keeps showing “Eject USB Successful” message when attempting to load the software update.
>
> If an error occurs, recovery steps for ED-5/ED-7 are:
>
> 1. Turn System Enable switch OFF.
> 2. Load the correct ED-5/ED-7 software package on the USB drive.
> 3. Install the USB drive.
> 4. Using a small screwdriver press and hold the red button beside the USB port.
> 5. Turn System Enable switch ON.
> 6. ED-5/ED-7 will start loading the software to recover from the intermediate non-functional state the ED-5/ED-7 unit had been in.
>
> ### Finishing Steps
>
> ED-4
>
> **CAUTION · Осторожно**
> After updating the software or VPF in any control system component, verify that the Vessel Control System is completely operational. It is also important to test and update the configuration settings and vessel personality of the component.
>
> After ED-4 display VPF update, refer to the following procedures for configuration setup information and testing:
>
> - For configuration, use the following procedure. [[513-015-108 — Display Configuration|Refer to Procedure 015-108 in Section 15]]. The ED-4 display may need to be set up differently based on its location.
> - For setup, use the following procedure. [[513-101-013 — General Operating Instructions|Refer to Procedure 101-013 in Section]] 1.
> - All control functionality of the Cummins® Marine Controls **must** be tested before leaving the dock after a service event. [[513-015-047 — Final Verification|Refer to Procedure 015-047 in Section 15]].
>
> Following a VPF update, if there is a new alarm code or performance complaint, follow the alarm code or the appropriate troubleshooting symptom tree in order to understand if the personality is working properly and is the appropriate personality for the application.
>
> If it is suspected that the vessel personality file is **not** working correctly, be sure that the appropriate file was loaded for the engine, equipment, and application.
>
> **Note · Примечание**
> The “Cummins ED-4 Display Vessel Personality File Tracking Sheet” in the Cummins® QuickServe® Online webpage provides information relating to changes made to a vessel personality file. This information can be used to establish if there is a commonality between changes made to the personality and the symptoms being observed.
>
> ED-5 and ED-7
>
> **CAUTION · Осторожно**
> After updating the software or VPF in any control system component, verify that the Vessel Control System is completely operational. It is also important to test and update the configuration settings and vessel personality of the component.
>
> After ED-5/ED-7 display configuration update, refer to the following procedures for configuration setup information and testing:
>
> - For configuration, use the following procedure. [[513-015-108 — Display Configuration|Refer to Procedure 015-108 in Section 15.]] The ED-5/ED-7 display may need to be set up differently based on its location.
> - All control functionality of the Cummins® Marine Controls **must** be tested before leaving the dock after a service event. [[513-015-047 — Final Verification|Refer to Procedure 015-047 in Section 15.]]
