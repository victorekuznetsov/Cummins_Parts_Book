---
type: "Процедура"
doc: "326-015-054"
title_en: "Vessel Configuration"
modified: "2024-06-25"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "4358378"
figures: 39
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/326/326-015-054.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/326-015-054.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/326"
  - "перевод/машинный"
---

# Vessel Configuration

> [!abstract] Процедура · `326-015-054`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[4358378 — Cummins® Electronic Throttle and Shift (ETS) and Cummins® Inboard Joystick Marine Con|4358378]]
> **Секции:** Section 15 - Instruments and Controls
> **Даты:** изменён 2024-06-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/326/326-015-054.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/326-015-054.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Существуют две разные версии рычажных станций управления и бортовых джойстиков. Унаследованная версия рычажной станции управления - все 3 и более старые, а существующая версия - 4 и более. Наследственная версия джойстика для бортовых устройств — все версии 2 и старше, а существующая версия — 3 и больше. Версия 3 и более мощные бортовые джойстики, версия 4 и более мощные станции управления рычагами будут предварительно настроены с завода с идентификационным номером 1. Версии 3 и более старая станция управления рычагом, а также все версии 2 и более старый бортовой джойстик имеют уникальный идентификатор ручки в сети контроллера, чтобы различать каждое устройство. Существующие и устаревшие джойстики и станции управления рычагами обратно совместимы.

**С версией 2 и более старыми встроенными джойстиками и версией 3 и более старой стойкой управления рычагами**

Для того чтобы каждая станция управления рычагом и бортовой джойстик могли взаимодействовать с модулем процессора управления дроссельной заслонки, каждое устройство должно иметь уникальный идентификатор ручки. Если с завода была приобретена полная система, конфигурация выполнялась заводом. Бортовые джойстики также имеют связанный идентификационный номер ручки и настройки типа джойстика.

Если станция управления рычагом или бортовой джойстик были приобретены отдельно, то на заводе он будет предварительно настроен с идентификатором ручки. Если установлены два устройства с одинаковым идентификатором ручки, система введет режим сигнализации и код тревоги будет сохранен. Одно из устройств должно быть настроено с новым идентификатором ручки для решения проблемы.

Если два устройства имеют одинаковый идентификатор ручки, все огни на кнопочной панели мигают сразу после включения переключателя системы.

**С версией 3 и большим встроенным джойстиком или версией 4 и большей стойкой управления рычагами**

Версия 4 и большая станция управления рычагом, а также версия 3 и более мощный бортовой джойстик поставляются с преднастроенной заводской рабочей станцией с идентификатором ручки № 1.

Существует четыре сценария, в которых может быть настроена станция управления рычагом и бортовой джойстик. Ниже приводятся примеры таких ситуаций:

![[15e00181.png]]

Идентификатор бортового джойстика № 3 заменяется бортовым джойстиком версии 3 и большим программным обеспечением. Новый бортовой джойстик необходимо будет изменить с заводской настройки ID номер 1 на уникальный идентификатор ручки.

#### Сценарий № 1: Бортовой джойстик с устаревшим программным обеспечением Версия 2 и старше заменяется на блок, оснащенный существующим программным обеспечением версии 3 или выше.

- Встроенный джойстик (идентификатор рукоятки 3) версии 3 и более мощное программное обеспечение включает в себя возможность обратной совместимости с устаревшим программным обеспечением версии 2 и более старой версии.
- Идентификатор по умолчанию для бортовых джойстиков и станций управления рычагами с новым программным обеспечением является идентификатором ручки № 1. Новый/заменительный джойстик с версией 3 и выше должен будет установить уникальный идентификатор ручки, прежде чем он будет использоваться. Невыполнение этого требования вызовет немедленную тревогу при активации системы управления.
- Новый или заменяемый джойстик может быть связан с станцией управления рычагом (идентификатором рукоятки № 1) для активации кнопки.
- Функции, доступные с версией 3 и большим программным обеспечением (прозрачная передача), не доступны в этом приложении.
- Такая ситуация будет применяться даже в том случае, если в разных зонах сети будут заменены несколько компонентов – либо бортовой джойстик, либо рычаг управления станцией.

![[15e00187.png]]

Идентификатор 1 рычажной станции управления заменяется рычажной станцией управления с версией 4 и большим программным обеспечением. Новая станция управления рычагом должна быть изменена с заводской установки ID номер 1 на уникальный идентификатор ручки.

#### Сценарий № 2: Станция управления рычагом с устаревшей версией программного обеспечения 3 и старше заменяется блоком, оснащенным существующей версией программного обеспечения 4 или выше.

- Программное обеспечение Lever Control Station версии 4 и выше включает в себя возможность обратной совместимости со всеми устаревшими версиями программного обеспечения 3 и старше.
- Идентификатор по умолчанию для бортовых джойстиков / станций управления рычагами с существующей версией программного обеспечения 4 и более - идентификатор ручки № 1. Замена станции управления рычагом другим идентификатором ручки потребует, чтобы новый/замененный идентификатор ручки ручки рычага был изменен на уникальный номер.
- Существующий джойстик может быть связан с новой станцией управления рычагом управления ручкой номер 1 для активации кнопки.
- Функции, доступные с версией 4 и большим программным обеспечением (прозрачная передача), не доступны в этом приложении.
- Такая ситуация будет применяться даже в том случае, если в разных областях сети будут заменены несколько компонентов — либо головка управления, либо джойстик.

![[15e00182.png]]

#### Сценарий No3: Новый «набор» устройств управления (станция рычага управления и бортовой джойстик) добавляется в сеть, где уже существуют другие компоненты с существующим / устаревшим программным обеспечением. Это может быть либо добавление новой станции, либо замена обоих компонентов на существующей станции.

- Управление рычажной станцией версии 4 и более, а также встроенным джойстиком версии 3 и большим программным обеспечением включает в себя возможность обратной совместимости с устаревшим программным обеспечением. С точки зрения процессора управления новые блоки будут работать так же, как и устаревшее программное обеспечение.
- На конкретной станции, станции № 2 в этом примере, станция рычага управления и бортовой джойстик смогут поддерживать функции системы (прозрачная передача).
- Идентификаторы по умолчанию для бортовых джойстиков и рычажной станции управления с существующим программным обеспечением являются идентификаторами ручки № 1. В этой ситуации идентификатор ручки рычажной станции управления должен быть изменен для обработки идентификатора номер 2. Невыполнение этого требования вызовет немедленную тревогу при активации системы управления.
- Бортовой джойстик на станции № 2 может быть настроен на прозрачную передачу с новой рычажной станцией управления на той же станции. При установке для прозрачной передачи и сопряжении с станцией управления рычагом бортовой идентификатор ручки джойстика должен быть установлен на тот же идентификатор ручки, что и станция управления рычагом, с которой он сопряжен (идентификационный номер 2 в ситуации, изображенной ниже). Если установлено, что **не** использовать прозрачный перенос, то бортовой джойстик также должен иметь уникальный идентификатор ручки.

![[15e00183.png]]

#### Сценарий No4: Система управления с компонентами, которые имеют новое программное обеспечение (управление головкой версии 4 и выше / бортовой джойстик версии 3 и выше)

- В этой конфигурации станции управления рычагом и бортовые джойстики могут быть установлены без учета идентификаторов ручки. Они будут установлены для идентификатора ручки по умолчанию № 1.
- Если требуется прозрачная передающая функция, бортовые джойстики на станциях № 1 и № 2 должны быть соединены с рычагами управления станциями, к которым установлены в непосредственной близости.
- Если не требуется прозрачная передача, то каждая станция может быть настроена с индивидуальными / уникальными идентификаторами ручки, как это делается в настоящее время с существующим программным обеспечением.
- Станция № 3 может быть настроена как для конфигурации «Standalone», так и для «Transparent Transfer». («Прозрачный перевод» — это настройка по умолчанию). В любой из настроек клавиатура джойстика будет активна только тогда, когда джойстик (станция № 3) является активной станцией.

### Конфигурация станции управления рычагом Four Button

> [!note] Примечание
> Обновления программного обеспечения на станции управления рычагом будут применять настройки заводской конфигурации по умолчанию. См. информацию ниже для документирования или сброса уникальных настроек конфигурации.

> [!note] Примечание
> Станции рычага управления версии 3 имеют кнопку ACTIVE. Версия 4 и выше имеет кнопку TAKE. Формулировка изменилась, но функциональность осталась прежней.

Выполните эти восемь шагов, чтобы применить новый идентификатор ручки.

Действие:

Переместить ручки рычага управления на полные позиции АСТЕРНА.

Результат:

Не получилось.

![[15900084.png]]

Действие:

Включите питание в систему.

Результат:

Активный/включенный светодиод начнет мигать.

![[15900085.png]]

Действие:

Нажмите и удерживайте две центральные кнопки (SYNC и WARM) в течение примерно 2 секунд, пока все четыре светодиода не начнут мигать. Кнопки освобождения.

Результат:

Все четыре светодиода начинают мигать.

![[15900086.png]]

Действие:

Нажмите и выпустите кнопку SYNC один раз, чтобы выбрать режим идентификатора рукоятки.

Результат:

Активный/включенный светодиод начнет мигать.

![[15900087.png]]

Действие:

Нажмите и отпустите кнопку WARM один раз, чтобы ввести конфигурацию идентификатора Handle ID.

Результат:

Будет отображаться текущий идентификатор ручки.

| **ID #** | **Включает** |
|---|---|
| 1 | Действующий/призывной |
| 2 | СИНК |
| 3 | Активный/интактный и SYNC |
| 4 | ВАРМ |
| 5 | Действующий/призывной и война |
| 6 | СИНК и ВАРМ |

![[15900088.png]]

Действие:

Нажмите и отпустите кнопку SYNC до достижения желаемого идентификатора ручки. См. диаграмму ниже для идентификационного номера ручки и соответствующего светодиода, который освещается.

Результат:

| **ID #** | **Включает** |
|---|---|
| 1 | Действующий/призывной |
| 2 | СИНК |
| 3 | Активный/интактный и SYNC |
| 4 | ВАРМ |
| 5 | Действующий/призывной и война |
| 6 | СИНК и ВАРМ |

![[15900087.png]]

Действие:

Нажмите и отпустите кнопку WARM один раз.

Результат:

Это действие хранит идентификатор ручки в памяти. Все четыре светодиода начинают мигать после того, как ID хранится в памяти.

![[15900088.png]]

Действие:

Запишите идентификационный номер ручки на тег, расположенный в нижней части станции управления рычагом.

Результат:

Не применяется

Для выхода из режима конфигурации ручки управления, выключите систему и верните ручки управления в положение NEUTRAL.

![[15900091.png]]

### Конфигурация двухкнопочного рычага управления

> [!note] Примечание
> Обновления программного обеспечения на станции управления рычагом будут применять настройки заводской конфигурации по умолчанию. См. информацию ниже для документирования или сброса уникальных настроек конфигурации.

Выполните эти восемь шагов, чтобы применить новый идентификатор ручки.

Действие:

Переместить ручки рычага управления на полные позиции АСТЕРНА.

Результат:

Не получилось.

![[15900084.png]]

Действие:

Включите питание в систему.

Результат:

Актив начинает мигать.

![[15900085.png]]

Действие:

Нажмите и удерживайте две центральные кнопки (ACTIVE и WARM) в течение примерно 2 секунд, пока все четыре светодиода не начнут мигать. Кнопки освобождения.

Результат:

Все четыре светодиода начинают мигать.

![[15900092.png]]

Действие:

Нажмите и выпустите кнопку ACTIVE один раз, чтобы выбрать режим идентификатора рукоятки.

Результат:

Свежий светодиод Port Neutral начнет мигать.

![[15900093.png]]

Действие:

Нажмите и отпустите кнопку WARM один раз, чтобы ввести конфигурацию идентификатора Handle ID.

Результат:

Будет отображаться текущий идентификатор ручки.

| **ID #** | **Включает** |
|---|---|
| 1 | Порт Нейтрэл |
| 2 | активный |
| 3 | Порт Нейтральный и активный |
| 4 | ВАРМ |
| 5 | Порт Нейтрэл и ВАРМ |
| 6 | Действительный и боевой |

![[15900094.png]]

Действие:

Нажмите и отпустите кнопку ACTIVE до тех пор, пока не будет достигнут желаемый идентификатор ручки. См. диаграмму ниже для идентификационного номера ручки и соответствующего светодиода, который освещается.

| **ID #** | **Включает** |
|---|---|
| 1 | Порт Нейтрэл |
| 2 | активный |
| 3 | Порт Нейтральный и активный |
| 4 | ВАРМ |
| 5 | Порт Нейтрэл и ВАРМ |
| 6 | Действительный и боевой |

![[15900095.png]]

Действие:

Нажмите и отпустите кнопку WARM один раз.

Результат:

Это действие хранит ваш идентификатор ручки в памяти. Все четыре светодиода начинают мигать после того, как ID хранится в памяти.

![[15900096.png]]

Действие:

Запишите идентификационный номер ручки на тег, расположенный в нижней части станции управления рычагом.

Результат:

Не применяется

Для выхода из режима конфигурации ручки управления, выключите систему и верните ручки управления в положение NEUTRAL.

![[15900091.png]]

### Конфигурация Joystick Configuration

> [!note] Примечание
> Обновления программного обеспечения на бортовой джойстик будут применять настройки заводской конфигурации по умолчанию. Ниже для документирования или сброса уникальных настроек конфигурации.

Режим конфигурации

Выполните эти шаги, чтобы войти в меню конфигурации.

Действие:

Переместите ручку джойстика в полную позицию и удерживайте.

Результат:

Не получилось.

![[15900097.png]]

Действие:

Включите питание в систему.

Результат:

Не получилось.

![[15900085.png]]

Действие:

При удерживании джойстика в полном положении на корме нажмите и удерживайте кнопку SELECT в течение 3 секунд для входа в режим конфигурации. После ввода режима конфигурации джойстик может быть выпущен.

Результат:

И индикатор оповещения (красный светодиод), и индикатор подруливающего устройства (желтый светодиод) на джойстике будут мигать одновременно, чтобы указать, что вы вошли в главное меню конфигурации.

![[15900107.png]]

Выбор меню конфигурации

После того, как вы перейдете в режим конфигурации, возможен выбор подменю. В таблице ниже показано каждое подменю и то, как реагирует соответствующий индикатор на панели кнопок.

Главное меню конфигурации — меню по умолчанию при вводе режима конфигурации. После ввода режима конфигурации кнопка носового съёмника порта, кнопка правого лука, индикатор сигнализации (красный светодиод) и индикатор тяги (желтый светодиод) используются для навигации в подменю.

Кнопка носового тягового устройства порта - это кнопка меню «Следующий», а кнопка правого бортового форсунного тягового устройства - кнопка меню «Войти».

Нажмите кнопку «Далее», чтобы проехать через доступные варианты и контролировать индикатор оповещения (красный светодиод), чтобы определить, какое меню в настоящее время выбрано.

Смотрите диаграмму ниже для выбора меню. Выбор меню отличается между бортовыми версиями джойстика.

Выбор меню в таблице параметров меню конфигурации Joystick с 1 по 5 поддерживается в встроенной версии джойстика 2 и старше.

Выбор меню от 1 до 6 поддерживается в бортовой джойстике версии 3 и более новой.

Когда выбрано желаемое меню, нажмите кнопку «Ввести», чтобы ввести выбранное меню.

| Конфигурация Joystick меню |  |
|---|---|
| **Световой индикатор алерта (красный светодиод) Вспышка "х" число раз:** | **Выбранное меню конфигурации** |
| Оба светодиода мигают | Главное меню конфигурации |
| 1 | Меню типа Joystick |
| 2 | Joystick Handle Меню идентификатора |
| 3 | Связанное меню Handle ID |
| 4 | Установить меню заводских дефектов |
| 5 | Меню проверки аппаратного обеспечения |
| 6 | Конфигурационное меню Joystick |

Кнопка джойстика имеет следующие кнопки и индикаторные огни.

1. Кнопка "Удаленный"
2. Кнопка Port Bow Thruster
3. Кнопка Starboard Bow Thruster
4. Кнопка Port Stern Thruster
5. Кнопка Starboard Stern Thruster
6. Световой индикатор оповещения (красный светодиод)
7. Выберите индикаторный свет (зеленый светодиод)
8. Световой индикатор Thruster (желтый светодиод).

![[25500005.png]]

Выбор типа Joystick

Меню типа джойстика позволяет выбрать, является ли джойстик автономным блоком на своей собственной выделенной станции или если он связан.

Если джойстик связан, он находится рядом с рычажной станцией управления на том же штурвале.

После нажатия кнопки «Войти», чтобы попасть в меню типа джойстика, индикатор оповещения (красный светодиод) будет продолжать мигать один раз. Световой индикатор двигателя (желтый светодиод) начнет мигать, указывая, какой элемент в меню подбора.

Нажмите кнопку «Далее», чтобы пройти через выбор. После того, как вы выбрали соответствующий элемент, нажмите кнопку «Ввести», чтобы подтвердить его.

После того, как настройка будет сохранена, вы будете возвращены в Главное меню конфигурации (оба светодиода мигают).

Наборные джойстики с программным обеспечением версии 3 и выше будут иметь дополнительный выбор для прозрачной передачи. Прозрачная процедура передачи.

По умолчанию устанавливается тип джойстика. В качестве альтернативы, инструмент электронного обслуживания JOYSTICKCONFIG-SERVICE может использоваться для установки типа джойстика.[[326-015-042 — Vessel Configuration Tool|См. процедуру 015-042 в разделе 15.]]

| **Световой индикатор синхронизации (желтый светодиод) Флеширование "х" число раз:**| **Выбранное решение** |
|---|---|
| 1 | отдельно |
| 2 | связанный |
| 3 | передача |

![[nobox.png]]

Идентификационный номер Joystick Handle

Меню Joystick Handle Identification Selection позволяет выбрать уникальный идентификационный номер для каждого джойстика.

Каждое устройство в сети контроллеров (CAN) должно иметь уникальный идентификационный номер. Станция управления рычагом не может иметь тот же идентификационный номер другой станции управления рычагом или бортового джойстика.

После нажатия кнопки «Войти», чтобы попасть в меню выбора идентификации Joystick Handle, индикатор оповещения (красный светодиод) будет продолжать мигать два раза. Световой индикатор двигателя (желтый светодиод) начнет мигать, указывая, какой элемент в меню подбора.

> [!note] Примечание
> Когда индикатор двигателя (желтый светодиод) первоначально мигает, он будет указывать идентификационный номер текущей ручки для бортового джойстика, которым управляют.

Нажмите кнопку «Далее», чтобы пройти через выбор. Когда выбран соответствующий элемент, нажмите кнопку «Ввести», чтобы подтвердить его. После сохранения настройки пользователь будет возвращен в Главное меню конфигурации (оба светодиода мигают).

Запишите новый идентификационный номер ручки джойстика на теге, расположенном на дне бортового джойстика. Электронная система обслуживания JOYSTICKCONFIG-SERVICE может **не** использоваться для установки идентификационного номера ручки.

| **Световой индикатор синхронизации (желтый светодиод) Флешинг 'x' число раз:**| **Выбранное решение** |
|---|---|
| 1 | Идентификатор Джойстика 1 |
| 2 | Идентификатор Джойстика 2 |
| 3 | Идентификатор Джойстика 3 |
| 4 | Идентификатор Джойстика 4 |
| 5 | Идентификатор джойстика 5 |
| 6 | Идентификатор Джойстика 6 |

![[nobox.png]]

Связанный идентификационный номер Handle

Меню выбора идентификации с ассоциированными ручками позволяет выбрать, с какой джойстиком связана станция управления рычагом. Джойстик может быть связан только с станцией управления рычагом, если они находятся на одной и той же станции руля. Это позволит пользователю более эффективно использовать станцию управления рычагом и бортовой джойстик, позволяя нажатию кнопки на бортовом джойстике работать при использовании ручек станции управления рычагом.

После нажатия кнопки «Войти», чтобы попасть в меню выбора идентификации с ассоциированными ручками, индикатор оповещения (красный светодиод) будет продолжать мигать три раза. Световой индикатор двигателя (желтый светодиод) начнет мигать, указывая, какой элемент в подменю выбран.

Нажмите кнопку «Далее», чтобы пройти через выбор. После того, как пользователь выбрал соответствующий элемент, нажмите кнопку «Ввести», чтобы подтвердить. После сохранения настройки пользователь будет возвращен в Главное меню конфигурации (оба светодиода мигают).

Запишите новый идентификационный номер связанной ручки на тег, расположенный на дне бортового джойстика. В качестве альтернативы, инструмент электронного обслуживания JOYSTICKCONFIG-SERVICE может использоваться для установки идентификационного номера соответствующей ручки.[[326-015-042 — Vessel Configuration Tool|См. процедуру 015-042 в разделе 15.]]

| **Световой индикатор синхронизации (желтый светодиод) Флешинг 'x' число раз:**| **Выбранное решение** |
|---|---|
| 1 | Обсуждение Handle ID 1 |
| 2 | Обсуждение Handle ID 2 |
| 3 | Обсуждение Handle ID 3 |
| 4 | Обсуждение Handle ID 4 |
| 5 | Обсуждение Handle ID 5 |
| 6 | Обсуждение Handle ID 6 |

![[nobox.png]]

Выбор заводского по умолчанию

Выбор заводских параметров в главном меню конфигурации и нажатие кнопки «Ввод» вернет все настройки обратно на завод. Ссылка на вышеупомянутые разделы подменю, чтобы увидеть, какие заводские настройки для каждого подменю.

После сохранения настройки пользователь будет возвращен в Главное меню конфигурации (оба светодиода мигают).

Чтобы выйти из меню «Главная конфигурация», выключите систему.

![[nobox.png]]

Выбор аппаратной проверки

- Выберите аппаратную проверку в конфигурации меню и нажмите кнопку «Ввести».
- Введите диагностический режим в бортовой джойстик, чтобы проверить функцию накладки кнопки и ручки джойстика. См. процедуру 015-052 в разделе 15.
- Чтобы выйти из меню «Главная конфигурация», выключите систему.

![[nobox.png]]

Конфигурационное меню Joystick

Конфигурация с кормовой стороны - это когда бортовой джойстик установлен с оператором лодки, обращенным к корме судна во время работы.

- Выберите конфигурацию Aft face в конфигурации меню и нажмите кнопку «Ввести».
- Измените функцию джойстика, чтобы обеспечить конфигурацию с кормовой облицовкой.
- После того, как настройка сохранена, появится Главное меню конфигурации (оба светодиода мигают).

![[nobox.png]]

### Конфигурация модуля управления дроссельной заслонки

> [!note] Примечание
> Обновления программного обеспечения для модуля процессора управления дроссельной заслонки будут применять заводские настройки по умолчанию. Ниже для документирования или сброса уникальных настроек конфигурации.

Электронная система дросселирования и переключения должна **не** нуждаться в какой-либо конфигурации, поскольку она предварительно настроена с завода. Во время нормальной работы оператор лодки имеет возможность изменять скорость холостого хода двигателя до 10 различных настроек холостого хода.

Скорость холостого хода двигателя всегда сбрасывается с ключевым событием цикла. Начальный размер шага бездействия двигателя может быть изменен, как описано ниже, на модулях процессора управления дроссельной заслонки EEC3. Эта настройка позволяет на небольшом или большом первом этапе позволить системе электронного дроссельного заслонка и сдвига попасть в диапазон дроссельного заслонка.

После первого шага следующие девять шагов позволяют осуществлять небольшие корректировки в диапазоне дроссельной заслонки. Для некоторых уникальных установок может потребоваться настроить дополнительные параметры в модуле процессора управления дроссельной заслонки. Для этих случаев обратитесь к местному инженеру-дистрибьютору Cummins®.

![[nobox.png]]

Чтобы изменить начальный размер шага установки начального размера бездействия двигателя по умолчанию, выполните следующие шаги.

Действие:

Переместить ручки управления рычагом в полные позиции AHEAD.

Результат:

Не получилось.

![[19903699.png]]

Действие:

Включите питание в систему.

Результат:

Активный/включенный светодиод начнет мигать.

![[15900109.png]]

Действие:

Нажмите и отпустите кнопку WARM три раза.

Результат:

Все четыре светодиода начнут мигать.

![[15900090.png]]

Действие:

Нажмите и отпустите кнопку SYNC шесть раз.

Результат:

Светодиоды SYNC и WARM начнут мигать.

![[15900110.png]]

Действие:

Нажмите и отпустите кнопку WARM один раз.

Результат:

Светодиоды не будут подсвечиваться.

![[15900111.png]]

Действие:

Нажмите и отпустите кнопку SYNC, пока не будет достигнут желаемый начальный размер шага. См. диаграмму ниже для начального размера шага бездействия двигателя и соответствующего светодиода, который освещается.

Результат:

| **Начальный размер шага** | **Включает** |
|---|---|
| 0,5% диапазона дроссельной заслонки | Нет |
| 1% от диапазона дроссельной заслонки | Действующий/призывной |
| 2% от диапазона дроссельной заслонки | СИНК |
| 3% от диапазона дроссельной заслонки | Активный/интактный и SYNC |
| 4% диапазона дроссельной заслонки | ВАРМ |
| 5% от диапазона дроссельной заслонки | Действующий/призывной и война |
| 10% от диапазона дроссельной заслонки | СИНК и ВАРМ |
| 20% от диапазона дроссельной заслонки | Активный/интактный, синхронный и боевой |
| 30% от диапазона дроссельной заслонки | Тролль |

Начальный размер шага по умолчанию для двигателя бездействует на 4% от диапазона дроссельной заслонки.

![[15900087.png]]

Действие:

Нажмите и отпустите кнопку WARM один раз.

Результат:

Настройки будут сохранены в памяти. Светодиоды SYNC и WARM будут подсвечиваться. Для выхода из режима конфигурации ручки управления, выключите систему и верните ручки управления в положение NEUTRAL.

![[15900113.png]]

### Завершающие операции

Проведите морское испытание, чтобы проверить правильность работы. См. процедуру 015-046 в разделе 15.

![[nobox.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> There are two different versions of lever control stations and inboard joysticks. The legacy lever control station version is all of 3 and older and the existing version is 4 and greater. The legacy inboard joystick version is all versions 2 and older and the existing version is 3 and greater. Version 3 and greater inboard joysticks and version 4 and greater lever control stations will come pre-configured from factory with Handle ID number 1. Versions 3 and older lever control station and all versions 2 and older inboard joystick have a unique handle identifier on the controller area network to distinguish each device. Existing and legacy joysticks and lever control stations are backward compatible.
>
> **With Version 2 and older Inboard Joystick and Version 3 and older Lever Control Station**
>
> In order for each lever control station and inboard joystick to communicate with the throttle control processor module, each device must have a unique handle identifier. If a complete system was purchased from the factory, configuration was performed by the factory. Inboard joysticks also have associated handle identification number and joystick type settings.
>
> If a lever control station or inboard joystick was purchased separately, it will be preconfigured at the factory with a handle identifier. If two devices with the same handle identifier are installed, the system will enter alarm mode and the alarm code will be stored. One of the devices will have to be configured with a new handle identifier to resolve the issue.
>
> If two devices have the same handle identifier, all lights on the button pad will blink immediately after the system enable switch is turned on.
>
> **With Version 3 and greater Inboard Joystick or Version 4 and greater Lever Control Station**
>
> Version 4 and greater lever control station and version 3 and greater inboard joystick come preconfigured from factory with handle identifier number 1.
>
> There are four scenarios in which the lever control station and inboard joystick can be configured. The following are example situations:
>
> Inboard joystick identifier number 3 is replaced with an inboard joystick with version 3 and greater software. The new inboard joystick will need to be changed from factory setting of ID number 1 to a unique handle identifier.
>
> #### Scenario Number 1: Inboard joystick with legacy software Version 2 and older is replaced with unit equipped with existing software version 3 or higher.
>
> - Inboard joystick (handle identifier number 3) version 3 and greater software includes the capability for backward compatibility with legacy software Version 2 and older.
> - Default handle identifier for inboard joysticks and lever control stations with new software is handle identifier number 1. New/replacement joystick with version 3 and greater will have to set a unique handle identifier before it can be used. Failure to do this will cause an immediate alarm when control system is activated.
> - New or replacement joystick can be associated to lever control station (handle identifier number 1) for purpose of button activation.
> - Features available with version 3 and greater software (transparent transfer) are **not** available in this application.
> - This situation would apply even if multiple components – either inboard joystick or lever control station were replaced in different areas of the network.
>
> Lever control station identifier number 1 is replaced with a lever control station with version 4 and greater software. The new lever control station will need to be changed from factory setting of ID number 1 to a unique handle identifier.
>
> #### Scenario Number 2: Lever control station with legacy software version 3 and older is replaced with unit equipped with existing software version 4 or higher.
>
> - Lever control station version 4 and higher software includes the capability for backward compatibility with all legacy software versions of 3 and older.
> - Default handle identifier for inboard joysticks/lever control stations with existing software version 4 and greater is handle identifier number 1. Replacement of a lever control station with a different handle identifier will require that the new/replacement lever control station handle identifier will have to be changed to a unique number.
> - Existing joystick can be associated to new handle identifier number 1 lever control station for purpose of button activation.
> - Features available with version 4 and greater software (transparent transfer) are not available in this application.
> - This situation would apply even if multiple components – either control head or joystick were replaced in different areas of the network.
>
> #### Scenario Number 3: A new “set” of control devices (control lever station and inboard joystick) are added to a network where other components with existing / legacy software already exist. This could either be adding a new station, or replacing both components at an existing station.
>
> - Control lever station version 4 and greater and inboard joystick version 3 and greater software includes the capability for backward compatibility with legacy software's. From the standpoint of the control processor, the new units will appear to operate in the same manner of the legacy software.
> - At the specific station, station number 2 in this example, the control lever station and inboard joystick will be able to support the system features (transparent transfer).
> - Default handle identifiers for inboard joysticks and lever control station with existing software is handle identifier number 1. In this situation, the lever control station handle identifier will need to be changed to handle identifier number 2. Failure to do this will cause an immediate alarm when control system is activated.
> - The inboard joystick at station number 2 can be setup for transparent transfer with new lever control station at the same station. When setup for transparent transfer and paired with the lever control station, inboard joystick handle identifier must be set to the same handle identifier as the lever control station which it is paired with (Station ID number 2 in the situation depicted below). If it is determined to **not** use transparent transfer, then the inboard joystick must also have a unique handle identifier.
>
> #### Scenario Number 4: A control system with components which all have new software (control head version 4 and greater / inboard joystick version 3 and greater)
>
> - In this configuration, the lever control stations and the inboard joysticks can be installed without regard to the handle identifiers. They will be set for the default handle identifier number 1.
> - If the transparent transfer feature is desired, the inboard joysticks at station number 1 and number 2 **must** be paired with the lever control stations to which are installed in proximity.
> - If transparent transfer is not desired, then each station can be setup with individual / unique handle identifiers –as it currently done with existing software.
> - Station number 3 inboard joystick can be setup for either “Standalone” configuration or “Transparent Transfer”. (“Transparent Transfer” is the default setting). In either setting, the inboard joystick keypad will only be active when the inboard joystick (Station number 3) is the active station.
>
> ### Four Button Lever Control Station Configuration
>
> **Note · Примечание**
> Software updates to the lever control station will apply default factory configuration settings. See information below for documenting or resetting unique configuration settings.
>
> **Note · Примечание**
> Version 3 control lever stations have an ACTIVE button. Version 4 and higher have a TAKE button. The wording has changed, but functionality has stayed the same.
>
> Follow these eight steps to apply a new handle identifier.
>
> Action:
>
> Move lever control station handles to FULL ASTERN positions.
>
> Result:
>
> No result.
>
> Action:
>
> Turn power ON to the system.
>
> Result:
>
> ACTIVE/INTAKE LED will begin to flash.
>
> Action:
>
> Press and hold the two center buttons (SYNC and WARM) for approximately 2 seconds until all four LEDs begin to flash. Release buttons.
>
> Result:
>
> All four LEDs begin to flash.
>
> Action:
>
> Press and release the SYNC button one time to select Handle Identifier Mode.
>
> Result:
>
> ACTIVE/INTAKE LED will begin to flash.
>
> Action:
>
> Press and release the WARM button one time to enter Handle ID Configuration.
>
> Result:
>
> The current handle ID will be displayed.
>
> | **ID\#** | **LEDs ON** |
> |---|---|
> | 1 | ACTIVE/INTAKE |
> | 2 | SYNC |
> | 3 | ACTIVE/INTAKE and SYNC |
> | 4 | WARM |
> | 5 | ACTIVE/INTAKE and WARM |
> | 6 | SYNC and WARM |
>
> Action:
>
> Press and release the SYNC button until desired handle ID is achieved. See chart below for handle identification number and corresponding LED that is illuminated.
>
> Result:
>
> | **ID\#** | **LEDs ON** |
> |---|---|
> | 1 | ACTIVE/INTAKE |
> | 2 | SYNC |
> | 3 | ACTIVE/INTAKE and SYNC |
> | 4 | WARM |
> | 5 | ACTIVE/INTAKE and WARM |
> | 6 | SYNC and WARM |
>
> Action:
>
> Press and release the WARM button one time.
>
> Result:
>
> This action stores the handle ID in memory. All four LEDs begin to flash after ID is stored in memory.
>
> Action:
>
> Record the handle identification number on the tag located on the bottom of the lever control station.
>
> Result:
>
> N/A
>
> To exit control handle configuration mode, turn system OFF and return control handles to NEUTRAL position.
>
> ### Two Button Lever Control Station Configuration
>
> **Note · Примечание**
> Software updates to the lever control station will apply default factory configuration settings. See information below for documenting or resetting unique configuration settings.
>
> Follow these eight steps to apply a new handle identifier.
>
> Action:
>
> Move lever control station handles to FULL ASTERN positions.
>
> Result:
>
> No result.
>
> Action:
>
> Turn power ON to the system.
>
> Result:
>
> ACTIVE will begin to flash.
>
> Action:
>
> Press and hold the two center buttons (ACTIVE and WARM) for approximately 2 seconds until all four LEDs begin to flash. Release buttons.
>
> Result:
>
> All four LEDs begin to flash.
>
> Action:
>
> Press and release the ACTIVE button one time to select Handle Identifier Mode.
>
> Result:
>
> PORT NEUTRAL LED will begin to flash.
>
> Action:
>
> Press and release the WARM button one time to enter Handle ID Configuration.
>
> Result:
>
> The current handle ID will be displayed.
>
> | **ID\#** | **LEDs ON** |
> |---|---|
> | 1 | PORT NEUTRAL |
> | 2 | ACTIVE |
> | 3 | PORT NEUTRAL and ACTIVE |
> | 4 | WARM |
> | 5 | PORT NEUTRAL and WARM |
> | 6 | ACTIVE and WARM |
>
> Action:
>
> Press and release ACTIVE button until desired handle ID is achieved. See chart below for handle identification number and corresponding LED that is illuminated.
>
> | **ID\#** | **LEDs ON** |
> |---|---|
> | 1 | PORT NEUTRAL |
> | 2 | ACTIVE |
> | 3 | PORT NEUTRAL and ACTIVE |
> | 4 | WARM |
> | 5 | PORT NEUTRAL and WARM |
> | 6 | ACTIVE and WARM |
>
> Action:
>
> Press and release the WARM button one time.
>
> Result:
>
> This action stores your handle ID in memory. All four LEDs begin to flash after ID is stored in memory.
>
> Action:
>
> Record the handle identification number on the tag located on the bottom of the lever control station.
>
> Result:
>
> N/A
>
> To exit control handle configuration mode, turn system OFF and return control handles to NEUTRAL position.
>
> ### Inboard Joystick Configuration
>
> **Note · Примечание**
> Software updates to the inboard joystick will apply default factory configuration settings. See below for documenting or resetting unique configuration settings.
>
> Configuration Mode
>
> Follow these steps to enter the configuration menu.
>
> Action:
>
> Move joystick handle to FULL ASTERN position and hold.
>
> Result:
>
> No result.
>
> Action:
>
> Turn power ON to the system.
>
> Result:
>
> No result.
>
> Action:
>
> While holding the joystick in the full astern position, press and hold the SELECT button for 3 seconds to enter configuration mode. Once configuration mode is entered, the joystick can be released.
>
> Result:
>
> Both the alert indicator light (red LED) and thruster indicator light (yellow LED) on the joystick will flash simultaneously to indicate you have entered the main configuration menu.
>
> Configuration Menu Options Selection
>
> Once in configuration mode, selection of the submenu is possible. The table below shows each submenu and how the corresponding indicator light on the button pad responds.
>
> The main configuration menu is the default menu when entering configuration mode. After entering Configuration Mode, the port bow thruster button, starboard bow thruster button, alert indicator light (red LED), and thruster indicator light (yellow LED) are used to navigate the submenus.
>
> The port bow thruster button is the menu “Next” button, and the starboard bow thruster button is the menu “Enter” button.
>
> Press the “Next” button to cycle through selections available and monitor the alert indicator light (red LED) to determine which menu is currently selected.
>
> See the chart below for menu selections. The menu selections are different between inboard joystick versions.
>
> The menu selections in the Joystick Configuration Menu options table from 1 through 5 are supported in inboard joystick version 2 and older.
>
> Menu selections from 1 through 6 are supported in inboard joystick version 3 and newer.
>
> When the desired menu is chosen, press the “Enter” button to enter the menu selected.
>
> | Joystick Configuration Menu Options |  |
> |---|---|
> | **Alert indicator light (red LED) Flashing "x" number of times:** | **Configuration Menu Selected** |
> | Both LEDs Flashing | Main Configuration Menu |
> | 1 | Joystick Type Menu |
> | 2 | Joystick Handle Identifier Menu |
> | 3 | Associated Handle ID Menu |
> | 4 | Set Factory Defaults Menu |
> | 5 | Hardware Verification Menu |
> | 6 | Aft Facing Joystick Configuration Menu |
>
> The joystick button pad has the following buttons and indicator lights.
>
> 1. SELECT button
> 2. Port Bow Thruster button
> 3. Starboard Bow Thruster button
> 4. Port Stern Thruster button
> 5. Starboard Stern Thruster button
> 6. Alert indicator light (red LED)
> 7. Select indicator light (green LED)
> 8. Thruster indicator light (yellow LED).
>
> Joystick Type Selection
>
> The joystick type menu allows selecting whether the joystick is a standalone unit on its own dedicated station or if it associated.
>
> If a joystick is associated, it is next to a lever control station on the same helm.
>
> After pressing the “Enter” button to get into the joystick type menu, the alert indicator light (red LED) will continue to blink one time. The thruster indicator light (yellow LED) will begin to blink indicating which item in the sub menu is selected.
>
> Press the “Next” button to cycle through the selections. Once you have the appropriate item selected hit the “Enter” button to confirm it.
>
> After the setting is stored you will be returned to the Main Configuration Menu (both LEDs flashing).
>
> Inboard joysticks with software version 3 and greater will have an additional selection for Transparent Transfer. See the Transparent Transfer procedure.
>
> The default joystick type setting is associated. Alternately, the JOYSTICKCONFIG-SERVICE electronic service tool can be used to set joystick type. [[326-015-042 — Vessel Configuration Tool|Refer to Procedure 015-042 in Section 15.]]
>
> | **Thruster indicator light (yellow LED) Flashing "x" number of times:** | **Setting Selected** |
> |---|---|
> | 1 | Standalone |
> | 2 | Associated |
> | 3 | Transfer |
>
> Joystick Handle Identification Number
>
> The Joystick Handle Identification Selection menu allows selection of a unique identification number for each joystick.
>
> Each device on the controller area network (CAN) must have a unique identification number. A lever control station cannot have the same identification number of another lever control station or inboard joystick.
>
> After pressing the “Enter” button to get into the Joystick Handle Identification Selection menu, the alert indicator light (red LED) will continue to blink two times. The thruster indicator light (yellow LED) will begin to blink indicating which item in the sub menu is selected.
>
> **Note · Примечание**
> When the thruster indicator light (yellow LED) initially blinks it will indicate the current handle identification number for the inboard joystick being operated.
>
> Press the “Next” button to cycle through the selections. When the appropriate item is selected, press the “Enter” button to confirm it. After the setting is stored, the user will be returned to the Main Configuration Menu (both LEDs flashing).
>
> Record the new joystick handle identification number on the tag located on the bottom of the inboard joystick. The JOYSTICKCONFIG-SERVICE electronic service tool can **not** be used to set the handle identification number.
>
> | **Thruster indicator light (yellow LED) Flashing 'x" number of times:** | **Setting Selected** |
> |---|---|
> | 1 | Joystick ID 1 |
> | 2 | Joystick ID 2 |
> | 3 | Joystick ID 3 |
> | 4 | Joystick ID 4 |
> | 5 | Joystick ID 5 |
> | 6 | Joystick ID 6 |
>
> Associated Handle Identification Number
>
> The Associated Handle Identification Selection menu allows selection of what lever control station the joystick is associated to. A joystick may **only** be associated to a lever control station if they are on the same helm station. This will allow the user to use the lever control station and inboard joystick more efficiently by allowing the button pad on the inboard joystick to be operational while using the lever control station handles.
>
> After pressing the “Enter” button to get into the Associated Handle Identification Selection menu, the alert indicator light (red LED) will continue to blink three times. The thruster indicator light (yellow LED) will begin to blink indicating which item in the submenu is selected.
>
> Press the “Next” button to cycle through the selections. Once the user has selected the appropriate item, press the “Enter” button to confirm. After the setting is stored, the user will be returned to the Main Configuration Menu (both LEDs flashing).
>
> Record the new associated handle identification number on the tag located on the bottom of the inboard joystick. Alternately, the JOYSTICKCONFIG-SERVICE electronic service tool can be used to set the associated handle identification number. [[326-015-042 — Vessel Configuration Tool|Refer to Procedure 015-042 in Section 15.]]
>
> | **Thruster indicator light (yellow LED) Flashing 'x" number of times:** | **Setting Selected** |
> |---|---|
> | 1 | Associated to Handle ID 1 |
> | 2 | Associated to Handle ID 2 |
> | 3 | Associated to Handle ID 3 |
> | 4 | Associated to Handle ID 4 |
> | 5 | Associated to Handle ID 5 |
> | 6 | Associated to Handle ID 6 |
>
> Factory Default Selection
>
> Selecting factory defaults on the main configuration menu and pressing the "Enter" button will revert all settings back to factory. Reference the above submenu sections to see what factory settings are for each submenu.
>
> After the setting is stored, the user will be returned to the Main Configuration Menu (both LEDs flashing).
>
> To exit the Main Configuration Menu, turn the system off.
>
> Hardware Verification Selection
>
> - Select hardware verification on the menu configuration and press the “Enter” button.
> - Enter diagnostic mode in the inboard joystick to check the function of the button pad and the joystick handle. Refer to Procedure 015-052 in Section 15.
> - To exit the Main Configuration Menu, turn the system off.
>
> Aft Facing Joystick Configuration Menu
>
> Aft facing configuration is when the inboard joystick is mounted with boat operator facing the stern of the vessel during operation.
>
> - Select the Aft facing configuration on the menu configuration and press the “Enter” button.
> - Change the joystick function to allow for an aft facing configuration.
> - After the setting is stored, the Main Configuration Menu will appear (both LEDs flashing).
>
> ### Throttle Control Processor Module Configuration
>
> **Note · Примечание**
> Software updates to the throttle control processor module will apply default factory configuration settings. See below for documenting or resetting unique configuration settings.
>
> The electronic throttle and shift system should **not** need any configuration as it is pre-configured from the factory. During normal operation, the boat operator has the ability to change the engine idle speed up to 10 different idle speed settings.
>
> The engine idle speed is always reset with a key cycle event. The engine idle initial step size setting may be changed as described below on EEC3 throttle control processor modules. This setting allows for a small or large first step to allow the electronic throttle and shift system to get into the throttle range.
>
> After the first step size, the following nine steps allow for small idle adjustments in the throttle range. For some unique installations, it may be necessary to configure additional parameters in the throttle control processor module. For these cases, contact a local Cummins® distributor application engineer.
>
> To change the default engine idle initial step size setting, perform the following steps.
>
> Action:
>
> Move lever control station handles to FULL AHEAD positions.
>
> Result:
>
> No result.
>
> Action:
>
> Turn power ON to the system.
>
> Result:
>
> ACTIVE/INTAKE LED will begin to flash.
>
> Action:
>
> Press and release the WARM button three times.
>
> Result:
>
> All four LEDs will begin to flash.
>
> Action:
>
> Press and release the SYNC button six times.
>
> Result:
>
> SYNC and WARM LEDs will begin to flash.
>
> Action:
>
> Press and release the WARM button one time.
>
> Result:
>
> No LEDs will be illuminated.
>
> Action:
>
> Press and release SYNC button until desired engine idle initial step size is achieved. See chart below for engine idle initial step size and corresponding LED that is illuminated.
>
> Result:
>
> | **Initial Step Size** | **LEDs ON** |
> |---|---|
> | 0.5% of throttle range | None |
> | 1% of throttle range | ACTIVE/INTAKE |
> | 2% of throttle range | SYNC |
> | 3% of throttle range | ACTIVE/INTAKE and SYNC |
> | 4% of throttle range | WARM |
> | 5% of throttle range | ACTIVE/INTAKE and WARM |
> | 10% of throttle range | SYNC and WARM |
> | 20% of throttle range | ACTIVE/INTAKE, SYNC and WARM |
> | 30% of throttle range | TROLL |
>
> The default engine idle initial step size setting is 4% of throttle range.
>
> Action:
>
> Press and release the WARM button one time.
>
> Result:
>
> Settings will be saved to memory. SYNC and WARM LEDs will be illuminated. To exit control handle configuration mode, turn system OFF and return control handles to the NEUTRAL position.
>
> ### Finishing Steps
>
> Perform a sea trial to verify proper function. Refer to Procedure 015-046 in Section 15.
