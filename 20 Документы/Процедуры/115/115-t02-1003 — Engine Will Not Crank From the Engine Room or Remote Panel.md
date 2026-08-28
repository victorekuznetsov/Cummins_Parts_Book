---
aliases:
  - "Двигатель не проворачивается ни из МО, ни с дистанционного пульта"
type: "Процедура"
doc: "115-t02-1003"
title_en: "Engine Will Not Crank From the Engine Room or Remote Panel"
title_ru: "Двигатель не проворачивается ни из МО, ни с дистанционного пульта"
modified: "2007-01-08"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021587"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1003.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1003.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/115"
  - "перевод/машинный"
---

# Engine Will Not Crank From the Engine Room or Remote Panel
**Двигатель не проворачивается ни из МО, ни с дистанционного пульта**

> [!abstract] Процедура · `115-t02-1003`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]]
> **Секции:** Section TT — Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2007-01-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1003.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1003.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Двигатель будет **не** проворачивать, когда кнопка запуска нажимается на панель машинного отделения.

- Двигатель **не** будет сворачиваться, когда кнопка запуска нажимается на удаленную панель.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения симптомов запуска двигателя. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Для запуска коленчатого механизма двигателя с панели машинного отделения должны быть соблюдены следующие параметры панели:

- Выключатель питания панели машинного отделения на освещенной лампе.

- Двигатель остановлен.

Для запуска коленчатого механизма двигателя с удаленной панели должны быть соблюдены следующие параметры панели:

- Удалённая панель питания лампы освещалась.

- Локальная стартовая **только** лампа **не** освещена

- Двигатель остановлен.

Перед началом процедуры устранения неполадок должны быть активны следующие условия :

1. Все выключатели в окне интерфейса клиента должны быть закрыты.

2. Выключатель остановки двигателя должен быть отключен.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте конфигурацию панели машинного отделения |  |
|  | **ШАГ 1А** Проверить питание панели | Включается выключатель питания и лампа подсвечивается? |
|  | **ШАГ 1В** Проверьте Локальный запуск только лампы | Локальный старт **только** лампа подсвечивается? |
| ШАГ 2. | Проверьте конфигурацию удаленной панели |  |
|  | **ШАГ 2А** Проверить питание панели | Локальный старт **только** лампа подсвечивается? |
|  | **ШАГ 2В** Проверьте Локальный запуск только лампы | Подсвечивается ли лампа локального запуска с удаленной панели **только**? |
| ШАГ 3. | Проверить панель двигателя Пуск кнопки |  |
|  | **STEP 3A.** Проверьте вход кнопки запуска в блок логики интерфейса клиента | Светильник с кривошипом? |
|  | **STEP 3B** Проверить работу кнопки запуска | Сопротивление менее 10 Ом? |
| ШАГ 4. | Проверить кнопку Пуск удаленной панели |  |
|  | **STEP 4A.** Проверьте вход кнопки запуска в блок логики интерфейса клиента | Светильник с кривошипом? |
|  | **STEP 4B** Проверить работу кнопки запуска | Сопротивление менее 10 Ом? |
| ШАГ 5. | Проверить Panel Wiring |  |
|  | **STEP 5A** Проверить проводку панели машинного отделения | Сопротивление менее 10 Ом? |
|  | **STEP 5A-1.** Проверьте питание коммутатора двигателя | Сопротивление менее 10 Ом? |
|  | **STEP 5A-2.** Проверить пуско-наладочный провод в машинном отделении | Сопротивление менее 10 Ом? |
| ШАГ 6. | Проверьте кабели Панельной системы |  |
|  | **STEP 6A.** Проверить кабель панели машинного отделения | Сопротивление менее 10 Ом? |
|  | **STEP 6B.** Проверьте кабель дистанционной панели | Сопротивление менее 10 Ом? |
|  | **STEP 6C.** Проверить стартовый кабель на наличие сигнала прелюбуляции | Сопротивление менее 10 Ом? |
|  | **STEP 6C-1.** Проверьте стартовую систему смазки кабеля | Менее 10 Ом сопротивления? |
|  | **STEP 6C-2.** Проверить кабельные провода | Менее 10 Ом сопротивления? |
| ШАГ 7. | Проверка проводки интерфейсной коробки заказчика |  |
|  | **STEP 7A.** Проверьте панель пускового провода в машинном отделении | Сопротивление менее 10 Ом? |
|  | **STEP 7B.** Проверьте проволоку для запуска удаленной панели | Сопротивление менее 10 Ом? |
|  | **STEP 7C.** Проверьте логику интерфейса клиента в блоке предварительной активации сигнала | Сопротивление менее 10 Ом? |
|  | **STEP 7D** Проверьте интерфейс клиента Логика Прелюбия Полная проволока сигнала | Сопротивление менее 10 Ом? |
|  | **STEP 7E** Проверьте интерфейс клиента Box Logic Unit Starter Switch Signal Wire | Сопротивление менее 10 Ом? |
|  | **STEP 7F.** Проверьте интерфейс клиента Box Logic Unit Starter Relay Wire | Сопротивление менее 10 Ом? |
| ШАГ 8. | Проверьте стартовый сигнал для двигателя |  |
|  | **STEP 8A.** Проверьте сигналы кабеля Starter Cable Starter Relay Switch | Сопротивление менее 10 Ом? |
| ШАГ 9. | Проверьте клиентский интерфейс Box Logic |  |
|  | **STEP 9A.** Проверьте логическую единицу интерфейса клиента из панели машинного отделения | 24 ВДЦ? |
|  | **STEP 9B.** Проверьте блок логики интерфейса клиента с удаленной панели | 24 ВДЦ? |
| ШАГ 10. | Проверить панель машинного отделения |  |
|  | **STEP 10A.** Проверить стартовый сигнал с панели машинного отделения или удаленной панели | 24 ВДЦ? |

### ШАГ 1. Проверьте конфигурацию панели машинного отделения

#### ШАГ 1A. Проверьте панель питания

| **Условия:** Расположение панели машинного отделения. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте включен выключатель питания и лампа подсвечивается. | Включается выключатель питания и лампа подсвечивается? *Да | 1В |
| Включается выключатель питания и лампа подсвечивается? **NORepair:** Включите выключатель питания и проверьте, что лампа освещена. Если лампа питания **не** по ссылке на Систему **Не** Начнется после выключения Устранение неполадок Симптомное дерево. | Ремонт завершён. |  |

#### ШАГ 1B. Проверьте локальный запуск только лампы

| **Условия:** Найдите панель двигателя, включите выключатель питания и подсветите лампу. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте, что подсвечивается только лампа локального запуска. | Локальный старт **только** лампа подсвечивается? *Да | 2А |
| Локальный старт **только** лампа подсвечивается? **NORepair:** Нажмите кнопку локального запуска **только** и проверьте, что лампа освещена. Если лампа не освещается, обратитесь к панели машинного отделения Local/Remote Switch Fails to Switch to Local Troubleshooting Symptom Tree. | Ремонт завершён. |  |

### ШАГ 2. Проверьте конфигурацию удаленной панели

#### ШАГ 2A. Проверьте панель питания

| **Условия:** Расположение удаленной панели. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить, что лампа питания подсвечивается. | Локальный старт **только** лампа подсвечивается? *Да | 2В |
| Локальный старт **только** лампа подсвечивается? **NORepair:** Если лампа не освещается, обратитесь к Системе не будет запуска после выключения, устраняющего неполадки. | Ремонт завершён. |  |

#### ШАГ 2B. Проверьте локальный запуск только лампы

| **Условия:** Светильник с дистанционным питанием. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте, что подсвечивается только лампа локального запуска. | Подсвечивается ли лампа локального запуска с удаленной панели **только**? **YESRepair:** Нажмите кнопку локального запуска **только** и убедитесь, что лампа удаленной панели **не** освещена. Если лампа все еще освещена, обратитесь к удаленной панели, которая не переключается на удаленное дерево с симптомами. | 3А |
| Подсвечивается ли лампа локального запуска с удаленной панели **только**? **NORepair:** См. Дистанционную панель не удалось перейти на локальное дерево-симптом. | Ремонт завершён. |  |

### ШАГ 3. Проверить панель двигателя Пуск кнопки

#### ШАГ 3A. Проверьте вход кнопки Пуск в блок логики интерфейса клиента

| **Условия:** Расположение панели машинного отделения Панельная панель двигателя с подсветкой Панель машинного отделения только с локальным пуском лампы не подсвечивается Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте ввод кнопки запуска двигателя в логический блок клиентского интерфейса. Нажмите кнопку запуска. Проверьте лампу коленчатого включения, освещенную на логическом блоке клиентского интерфейса. | Светильник с кривошипом? *Да | 7Е |
| Светильник с кривошипом? **НЕТ** | 3B |  |

#### ШАГ 3B. Проверить пусковую кнопку

| **Условия:** Открытая панель машинного отделения Отключить панель управления разъемом Х4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте работу кнопки запуска. Поместите один испытательный щуп на терминал питания переключателя питания машинного отделения разъёма панели управления X4. Поместите другой испытательный щуп на панель машинного отделения пускового терминала питания разъёма панели управления X4. Нажмите кнопку запуска. | Сопротивление менее 10 Ом? *Да | 4А |
| Сопротивление менее 10 Ом? **NORepair:** Заменить панель управления. См. процедуру[[115-015-024 — Engine Room Panel\|015-024]]. | Ремонт завершён. |  |

### ШАГ 4. Проверить кнопку Пуск удаленной панели

#### ШАГ 4A. Проверьте вход кнопки Пуск в блок логики интерфейса клиента

| **Условия:** Расположение пульта дистанционного управления Светодиодная панель питания подсветила Open клиентский интерфейс коробки. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте ввод кнопки запуска двигателя в логический блок клиентского интерфейса. Нажмите кнопку запуска. Проверьте лампу коленчатого включения, освещенную на логическом блоке клиентского интерфейса. | Светильник с кривошипом? *Да | 7Е |
| Светильник с кривошипом? **НЕТ** | 4B |  |

#### ШАГ 4B. Проверить пусковую кнопку

| **Условия:** Открытая удаленная панель Отключить панель управления разъемом Х4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте работу кнопки запуска. Поместите один испытательный щуп на удаленную панель пускового терминала питания разъёма панели управления X4. Поместите другой испытательный щуп на терминал питания пульта дистанционного питания панели разъема управления X4. Нажмите кнопку запуска. | Сопротивление менее 10 Ом? *Да | 5а |
| Сопротивление менее 10 Ом? **NORepair:** Заменить панель управления. См. процедуру[[115-015-025 — Remote Panel\|015-025]]. | Ремонт завершён. |  |

### ШАГ 5. Проверить Panel Wiring

#### ШАГ 5A. Проверка проводов панели Engine Room

| **Условия:** Найдите панель машинного отделения Открытая дверь панели машинного отделения. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте проводку панели машинного отделения. Отсоедините кабель C14 от панели машинного отделения. Поместите один испытательный щуп на контакт питания переключателя в машинном отделении на разъеме C14. Поместите другой испытательный щуп на панель машинного отделения, чтобы начать контакт с подачей на разъеме C14. Нажмите кнопку запуска. | Сопротивление менее 10 Ом? *Да | 6А |
| Сопротивление менее 10 Ом? **НЕТ** | 5А-1-1 |  |

#### ШАГ 5A-1. Проверьте двигатель комнаты питание коммутатор провод

| **Условия:** Найдите панель машинного отделения Открытая дверь панели машинного отделения. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте проводку панели машинного отделения. Отсоедините кабель C14 от панели машинного отделения. Подключите на испытательном щупе на двигателе коммутатор питания контакт на панели двигателя C14 разъем. Поместите другой испытательный щуп на контакт питания переключателя в машинном отделении на разъем панели управления. | Сопротивление менее 10 Ом? *Да | 5А-2 |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-024 — Engine Room Panel\|015-024]]. | Ремонт завершён. |  |

#### ШАГ 5A-2. Проверить панель машинного отделения Start Supply Wire

| **Условия:** Найдите панель машинного отделения Открытая дверь панели машинного отделения. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте проводку панели машинного отделения. Отсоедините кабель C14 от панели машинного отделения. Подключите один испытательный щуп на панели машинного отделения, начните контакт питания на панели машинного отделения C14 разъема. Поместите другой испытательный щуп на панель машинного отделения, начните контакт питания на разъем панели управления. | Сопротивление менее 10 Ом? *Да | 6А |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-024 — Engine Room Panel\|015-024]]. | Ремонт завершён. |  |

### ШАГ 6. Проверьте кабели Панельной системы

#### ШАГ 6A. Проверить панель кабеля машинного отделения

| **Условия:** Отсоединить кабельный разъём С14 от панели машинного отделения Отключить кабельный разъём С7 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте кабель панели машинного отделения. Установите перемычку между контактом питания переключателя двигателя и панелью двигателя, чтобы начать контакт питания в разъеме C14. Поместите один испытательный щуп в контакт питания переключателя в разъеме C7. Поместите другой испытательный щуп в панель машинного отделения, начните контактную подачу в разъеме С7. | Сопротивление менее 10 Ом? *Да | 6B |
| Сопротивление менее 10 Ом? **Заменить кабель.** | Ремонт завершён. |  |

#### ШАГ 6B. Проверьте удаленный панельный кабель

| **Условия:** Найти и открыть окно клиентского интерфейса Найти и открыть пульт дистанционного подключения Отключить кабель удаленной панели от окна клиентского интерфейса X4 разъема. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте кабель удаленной панели. Установите перемычку между терминалом питания удаленного переключателя питания и терминалом питания дистанционного пуска панели на панели дистанционного управления разъемом X4. Поместите один измерительный щуп на терминал питания пульта дистанционного управления в разъеме клиентского интерфейса X4. Поместите другой измерительный щуп на удаленную панель пускового терминала в разъем клиентского интерфейса X4. | Сопротивление менее 10 Ом? *Да | 6C |
| Сопротивление менее 10 Ом? **Заменить кабель.** | Ремонт завершён. |  |

#### ШАГ 6C. Проверить Стартовый кабель Prelubrication Signals

| **Условия:** Отсоедините кабельный разъем С1 от окна интерфейса клиента Проверьте, что на месте прыгун системы предварительной смазки. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте стартовый кабель. Поместите один испытательный щуп на контакт сигнала прелюбрикационной активации в разъём С1. Поместите другой испытательный щуп на прелюбрикационный полный контакт сигнала в разъём С1. | Сопротивление менее 10 Ом? *Да | 7А |
| Сопротивление менее 10 Ом? **НЕТ** | 6С-1-1 |  |

#### ШАГ 6C-1. Стартовая кабельная система прелюбрикации Jumper

| **Условия:** Отсоединить прыгун системы прелюбрикации от стартового кабеля. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте смывную систему прыгуна. Поместите один испытательный щуп на контакт сигнала активации прелюбрикации в прыгуне системы прелюбрикации. Поместите другой испытательный щуп на прелюбрикационный полный контакт сигнала в прыгун прелюбрикационной системы. | Менее 10 Ом сопротивления? *Да | 6С-2 |
| Менее 10 Ом сопротивления? **Норэпэр:** Замените прыгуна. | Ремонт завершён. |  |

#### ШАГ 6C-2. Проверить кабельную систему прелюбрикации Starter

| **Условия:** Отсоединить кабельный разъем С1 от окна интерфейса клиента Отключить прелюбрикационный системный перемычек от стартового кабеля. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте стартовый кабель. Установите перемычку между контактом сигнала активации прелюбрикации и полным контактом сигнала прелюбрики в разъеме системы прелюбрикации. Поместите один испытательный щуп на контакт сигнала прелюбрикационной активации в разъём С1. Поместите другой испытательный щуп на прелюбрикационный полный контакт сигнала в разъём С1. | Менее 10 Ом сопротивления? *Да | 7А |
| Менее 10 Ом сопротивления? **Норэпэр:** Замените прыгуна. | Ремонт завершён. |  |

### ШАГ 7. Проверка проводки интерфейсной коробки заказчика

#### ШАГ 7A. Проверьте панель машинного отделения Start Supply Wire

| **Условия:** Откройте окно интерфейса клиента Отключите кабель машинного отделения на разъеме C7 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод питания в машинном отделении. Поместите один испытательный щуп на панель машинного отделения, начните контакт подачи в разъеме С7. Поместите другой испытательный щуп на панель машинного отделения, запустите терминал питания на логическом блоке клиентского интерфейса. | Сопротивление менее 10 Ом? *Да | 7B |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

#### ШАГ 7B. Проверьте проволоку для запуска удаленной панели

| **Условия:** Откройте окно интерфейса клиента Отключите кабель удаленной панели на разъеме X4 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод питания пульта дистанционного управления. Поместите один измерительный щуп на удаленную панель запуска проводного терминала в клиентский интерфейсный ящик X4 разъема. Поместите другой измерительный щуп на удаленную панель запуска проводного терминала питания на логический блок окна интерфейса клиента. | Сопротивление менее 10 Ом? *Да | 7C |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

#### ШАГ 7C. Проверьте клиентский интерфейс Box Logic Unit Prelube

| **Условия:** Откройте окно интерфейса клиента Отключить кабель C1 от соединительного окна интерфейса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод сигнала активации прелюбия. Поместите один измерительный щуп на терминал сигнала активации прелюбия на блок логики окна интерфейса клиента. Поместите другой испытательный щуп в контакт сигнала активации прелюбы в разъеме C1. | Сопротивление менее 10 Ом? *Да | 7D |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

#### ШАГ 7D. Проверьте интерфейс клиента Box Logic Prelube Полная проволока сигнала

| **Условия:** Откройте окно интерфейса клиента Отключите разъем кабеля C1 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте прелюбию полного сигнала провода. Поместите один измерительный щуп на терминал полного сигнала прелюбия на блок логики окна интерфейса клиента. Поместите другой испытательный щуп в прелюбию полного контакта сигнала в разъем С1. | Сопротивление менее 10 Ом? *Да | 7Е |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

#### ШАГ 7E. Проверьте интерфейс клиента Box Logic Unit Starter Switch Signal Wire

| **Условия:** Откройте окно интерфейса клиента Отключите разъем кабеля C1 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнальный провод стартового реле. Поместите один измерительный щуп на стартовый терминал ретранслятора сигналов на логический блок окна интерфейса клиента. Поместите другой испытательный щуп в контакт сигнала стартового реле переключателя в разъем С1. | Сопротивление менее 10 Ом? *Да | 7F |
| Сопротивление менее 10 Ом? **NORepair:** Заменить логический блок клиентского интерфейса. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

#### ШАГ 7F. Проверьте клиентский интерфейс Box Logic Unit Starter Relay Wire

| **Условия:** Откройте окно интерфейса клиента Отключите разъем кабеля C1 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод ретранслятора стартера. Поместите один измерительный щуп на стартовый релейный терминал возврата на блок логики клиентского интерфейса. Поместите другой испытательный щуп в стартовый реле обратного контакта в разъем С1. | Сопротивление менее 10 Ом? *Да | 8а |
| Сопротивление менее 10 Ом? **NORepair:** Заменить логический блок клиентского интерфейса. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

### ШАГ 8. Проверьте стартовый сигнал для двигателя

#### ШАГ 8A. Стартовый кабель Starter Relay Switch Signals

| **Условия:** Отсоединить кабельный разъем С1 от окна интерфейса клиента Отключить кабельные кольцевые терминалы от стартового ретранслятора. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте стартовый кабель. Установите перемычку между контактом сигнала стартового реле-переключателя и обратным контактом стартера-ретранслятора в разъёме C1. Поместите один испытательный щуп на стартовый сигнальный терминал ретранслятора. Поместите другой испытательный щуп на терминал возвратного кольца реле стартера. | Сопротивление менее 10 Ом? *Да | 9а |
| Сопротивление менее 10 Ом? **Заменить кабель.** | Ремонт завершён. |  |

### ШАГ 9. Проверьте клиентский интерфейс Box Logic

#### ШАГ 9A. Проверьте блок логики интерфейса клиента из панели машинного отделения

| **Условия:** Откройте окно интерфейса клиента Отключите разъем кабеля C1 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод питания в машинном отделении. Поместите положительный измерительный щуп на стартовый терминал ретранслятора сигналов на логический блок клиентского интерфейса. Поместите отрицательный измерительный щуп на стартовый терминал возврата ретранслятора реле на логический блок окна интерфейса клиента. Нажмите кнопку запуска на панели машинного отделения. | 24 ВДЦ? *Да | 9В |
| 24 ВДЦ? **NORepair:** Заменить логический блок клиентского интерфейса. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

#### ШАГ 9B. Проверьте блок логики интерфейса клиента из удаленной панели

| **Условия:** Открыть окно интерфейса клиента Базовая система сконфигурирована для запуска с удаленной панели (локальный пуск только лампы не освещается) Отключить кабель C1 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод питания пульта дистанционного управления. Поместите положительный измерительный щуп на стартовый терминал ретранслятора сигналов на логический блок клиентского интерфейса. Поместите отрицательный измерительный щуп на стартовый терминал возврата ретранслятора реле на логический блок окна интерфейса клиента. Нажмите кнопку запуска на удаленной панели. | 24 ВДЦ? *Да | 10А |
| 24 ВДЦ? **NORepair:** Заменить логический блок клиентского интерфейса. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

### ШАГ 10. Проверить панель машинного отделения

#### ШАГ 10A. Проверьте стартовый сигнал с панели машинного отделения или удаленной панели

| **Условия:** Настройка системы панели для запуска с удаленной панели или панели машинного отделения. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнал запуска с панели машинного отделения или удаленной панели. Поместите положительный пробный щуп на стартовый сигнальный терминал реле-переключателя. Поместите отрицательный пробный щуп на терминал возвратного кольца реле стартера. Нажмите кнопку запуска. | 24 ВДЦ? **Ремонт:** См. Руководство по эксплуатации, QSK19 и QSK19 CM850 Модульные двигатели серии Common Rail System, Бюллетень[[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. | Ремонт завершён. |
| 24 ВДЦ? **Заменить кабель.** | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - Engine will **not** crank when the start button is pushed at the engine room panel.
>
> - Engine will **not** crank when the start button is pushed at the remote panel.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot engine start symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> To initiate engine crank from the engine room panel, the following panel parameters **must** be met:
>
> - The engine room panel power switch on the lamp illuminated.
>
> - The engine is stopped.
>
> To initiate engine crank from the remote panel, the following panel parameters **must** be met:
>
> - The remote panel power lamp illuminated.
>
> - The local start **only** lamp is **not** illuminated
>
> - The engine is stopped.
>
> Prior to beginning the troubleshooting procedure, the following conditions **must** be active:
>
> 1. All circuit breakers in the customer interface box must be closed.
>
> 2. The engine stop switch **must** be disengaged.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check Engine Room Panel Configuration |  |
> |  | **STEP 1A.** Check Panel Power | Is the power switch on and lamp illuminated? |
> |  | **STEP 1B.** Check Local Start Only Lamp | Local start **only** lamp illuminated? |
> | STEP 2. | Check Remote Panel Configuration |  |
> |  | **STEP 2A.** Check Panel Power | Local start **only** lamp illuminated? |
> |  | **STEP 2B.** Check Local Start Only Lamp | Is remote panel local start **only** lamp illuminated? |
> | STEP 3. | Check Engine Room Panel Start Button |  |
> |  | **STEP 3A.** Check Start Button Input to Customer Interface Box Logic Unit | Crank lamp illuminated? |
> |  | **STEP 3B.** Check Start Button Operation | Less than 10 ohms resistance? |
> | STEP 4. | Check Remote Panel Start Button |  |
> |  | **STEP 4A.** Check Start Button Input to Customer Interface Box Logic Unit | Crank lamp illuminated? |
> |  | **STEP 4B.** Check Start Button Operation | Less than 10 ohms resistance? |
> | STEP 5. | Check Panel Wiring |  |
> |  | **STEP 5A.** Check Engine Room Panel Wiring | Less than 10 ohms resistance? |
> |  | **STEP 5A-1.** Check Engine Room Power Switch Supply Wire | Less than 10 ohms resistance? |
> |  | **STEP 5A-2.** Check Engine Room Panel Start Supply Wire | Less than 10 ohms resistance? |
> | STEP 6. | Check Panel System Cables |  |
> |  | **STEP 6A.** Check Engine Room Panel Cable | Less than 10 ohms resistance? |
> |  | **STEP 6B.** Check Remote Panel Cable | Less than 10 ohms resistance? |
> |  | **STEP 6C.** Check Starter Cable Prelubrication Signals | Less than 10 ohms resistance? |
> |  | **STEP 6C-1.** Check Starter Cable Prelubrication System Jumper | Less than 10 ohm resistance? |
> |  | **STEP 6C-2.** Check Starter Cable Prelubrication System Wires | Less than 10 ohm resistance? |
> | STEP 7. | Check Customer Interface Box Wiring |  |
> |  | **STEP 7A.** Check the Engine Room Panel Start Supply Wire | Less than 10 ohms resistance? |
> |  | **STEP 7B.** Check the Remote Panel Start Supply Wire | Less than 10 ohms resistance? |
> |  | **STEP 7C.** Check Customer Interface Box Logic Unit Prelube Activation Signal Wire | Less than 10 ohms resistance? |
> |  | **STEP 7D.** Check Customer Interface Box Logic Prelube Complete Signal Wire | Less than 10 ohms resistance? |
> |  | **STEP 7E.** Check Customer Interface Box Logic Unit Starter Relay Switch Signal Wire | Less than 10 ohms resistance? |
> |  | **STEP 7F.** Check Customer Interface Box Logic Unit Starter Relay Return Wire | Less than 10 ohms resistance? |
> | STEP 8. | Check Start Signal to Engine |  |
> |  | **STEP 8A.** Check Starter Cable Starter Relay Switch Signals | Less than 10 ohms resistance? |
> | STEP 9. | Check Customer Interface Box Logic Unit |  |
> |  | **STEP 9A.** Check Customer Interface Box Logic Unit From the Engine Room Panel | 24 VDC? |
> |  | **STEP 9B.** Check Customer Interface Box Logic Unit From the Remote Panel | 24 VDC? |
> | STEP 10. | Check Engine Room Panel |  |
> |  | **STEP 10A.** Check Start Signal from Engine Room Panel or Remote Panel | 24 VDC? |
>
> ### STEP 1. Check Engine Room Panel Configuration
>
> #### STEP 1A. Check Panel Power
>
> | **Conditions:** Locate engine room panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify power switch is on and lamp illuminated. | Is the power switch on and lamp illuminated? **YES** | 1B |
> | Is the power switch on and lamp illuminated? **NORepair:** Turn on power switch and verify lamp is illuminated. If the power lamp is **not** on refer to the System Will **Not** Start After Shutdown Troubleshooting Symptom Tree. | Repair complete. |  |
>
> #### STEP 1B. Check Local Start Only Lamp
>
> | **Conditions:** Locate engine room panel Power switch on and lamp illuminated. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify local start only lamp is illuminated. | Local start **only** lamp illuminated? **YES** | 2A |
> | Local start **only** lamp illuminated? **NORepair:** Push local start **only** button and verify lamp is illuminated. If the lamp did not illuminate refer to the Engine Room Panel Local/Remote Switch Fails to Switch to Local Troubleshooting Symptom Tree. | Repair complete. |  |
>
> ### STEP 2. Check Remote Panel Configuration
>
> #### STEP 2A. Check Panel Power
>
> | **Conditions:** Locate remote panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify power lamp is illumintated. | Local start **only** lamp illuminated? **YES** | 2B |
> | Local start **only** lamp illuminated? **NORepair:** If the lamp did **not** illuminate refer to the System Will Not Start After Shutdown Troubleshooting Symptom Tree. | Repair complete. |  |
>
> #### STEP 2B. Check Local Start Only Lamp
>
> | **Conditions:** Remote panel power lamp illuminated. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify remote panel local start only lamp is illuminated. | Is remote panel local start **only** lamp illuminated? **YESRepair:** Locate engine room panel and push local start **only** button and verify remote panel lamp is **not** illuminated. If the lamp is still illuminated refer to the Remote Panel Fails to Switch to Remote Troubleshooting Symptom Tree. | 3A |
> | Is remote panel local start **only** lamp illuminated? **NORepair:** Refer to the Remote Panel Fails to Switch to Local Troubleshooting Symptom Tree. | Repair complete. |  |
>
> ### STEP 3. Check Engine Room Panel Start Button
>
> #### STEP 3A. Check Start Button Input to Customer Interface Box Logic Unit
>
> | **Conditions:** Locate engine room panel Engine room panel power lamp illuminated Engine room panel local start only lamp not illuminated Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check engine start button input to customer interface box logic unit. Press the start button. Verify crank lamp illuminated on customer interface box logic unit. | Crank lamp illuminated? **YES** | 7E |
> | Crank lamp illuminated? **NO** | 3B |  |
>
> #### STEP 3B. Check Start Button Operation
>
> | **Conditions:** Open engine room panel Disconnect control panel X4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the start button operation. Place one test lead on the engine room power switch supply terminal of the control panel X4 connector. Place the other test lead on the engine room panel start supply terminal of the control panel X4 connector. Press the start button. | Less than 10 ohms resistance? **YES** | 4A |
> | Less than 10 ohms resistance? **NORepair:** Replace the control panel. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |
>
> ### STEP 4. Check Remote Panel Start Button
>
> #### STEP 4A. Check Start Button Input to Customer Interface Box Logic Unit
>
> | **Conditions:** Locate remote panel Remote panel power lamp illuminated Open customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine start button input to customer interface box logic unit. Press the start button. Verify the crank lamp illuminated on the customer interface box logic unit. | Crank lamp illuminated? **YES** | 7E |
> | Crank lamp illuminated? **NO** | 4B |  |
>
> #### STEP 4B. Check Start Button Operation
>
> | **Conditions:** Open remote panel Disconnect control panel X4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the start button operation. Place one test lead on the remote panel start supply terminal of the control panel X4 connector. Place the other test lead on the remote panel power switch supply terminal of the control panel X4 connector. Press the start button. | Less than 10 ohms resistance? **YES** | 5A |
> | Less than 10 ohms resistance? **NORepair:** Replace the control panel. Refer to Procedure [[115-015-025 — Remote Panel\|015-025]]. | Repair complete. |  |
>
> ### STEP 5. Check Panel Wiring
>
> #### STEP 5A. Check Engine Room Panel Wiring
>
> | **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check engine room panel wiring. Disconnect cable C14 from the engine room panel. Place one test lead to the engine room power switch supply pin at the C14 connector. Place the other test lead on the engine room panel start supply pin at the C14 connector. Press the start button. | Less than 10 ohms resistance? **YES** | 6A |
> | Less than 10 ohms resistance? **NO** | 5A-1 |  |
>
> #### STEP 5A-1. Check Engine Room Power Switch Supply Wire
>
> | **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check engine room panel wiring. Disconnect cable C14 from the engine room panel. Connect on test lead on the engine room power switch supply pin on the engine room panel C14 connector. Place the other test lead on the engine room power switch supply pin on the control panel connector. | Less than 10 ohms resistance? **YES** | 5A-2 |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |
>
> #### STEP 5A-2. Check Engine Room Panel Start Supply Wire
>
> | **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check engine room panel wiring. Disconnect cable C14 from the engine room panel. Connect one test lead on the engine room panel start supply pin on the engine room panel C14 connector. Place the other test lead on the engine room panel start supply pin on the control panel connector. | Less than 10 ohms resistance? **YES** | 6A |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |
>
> ### STEP 6. Check Panel System Cables
>
> #### STEP 6A. Check Engine Room Panel Cable
>
> | **Conditions:** Disconnect cable connector C14 from the engine room panel Disconnect cable connector C7 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine room panel cable. Install a jumper between engine room power switch supply pin and the engine room panel start supply pin in connector C14. Place one test lead in the engine room panel power switch supply pin in connector C7. Place the other test lead in the engine room panel start supply pin in connector C7. | Less than 10 ohms resistance? **YES** | 6B |
> | Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |
>
> #### STEP 6B. Check Remote Panel Cable
>
> | **Conditions:** Locate and open customer interface box Locate and open remote panel Disconnect remote panel cable from customer interface box X4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the remote panel cable. Install a jumper between the remote power switch supply terminal and the remote panel start supply terminal on the remote control panel X4 connector. Place one test lead on the remote panel power switch supply terminal in customer interface box X4 connector. Place the other test lead on the remote panel start supply terminal in the customer interface box X4 connector. | Less than 10 ohms resistance? **YES** | 6C |
> | Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |
>
> #### STEP 6C. Check Starter Cable Prelubrication Signals
>
> | **Conditions:** Disconnect cable connector C1 from the customer interface box Check that prelubrication system jumper is in place. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the starter cable. Place one test lead on the prelubrication activation signal pin in connector C1. Place the other test lead on the prelubrication complete signal pin in connector C1. | Less than 10 ohms resistance? **YES** | 7A |
> | Less than 10 ohms resistance? **NO** | 6C-1 |  |
>
> #### STEP 6C-1. Check Starter Cable Prelubrication System Jumper
>
> | **Conditions:** Disconnect the prelubrication system jumper from the starter cable. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the prelubrication system jumper. Place one test lead on the prelubrication activation signal pin in the prelubrication system jumper. Place the other test lead on the prelubrication complete signal pin in the prelubrication system jumper. | Less than 10 ohm resistance? **YES** | 6C-2 |
> | Less than 10 ohm resistance? **NORepair:** Replace the jumper. | Repair complete. |  |
>
> #### STEP 6C-2. Check Starter Cable Prelubrication System Wires
>
> | **Conditions:** Disconnect cable connector C1 from the customer interface box Disconnect the prelubrication system jumper from the starter cable. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the starter cable. Install a jumper between the prelubrication activation signal pin and the prelubrication complete signal pin in the prelubrication system connector. Place one test lead on the prelubrication activation signal pin in connector C1. Place the other test lead on the prelubrication complete signal pin in connector C1. | Less than 10 ohm resistance? **YES** | 7A |
> | Less than 10 ohm resistance? **NORepair:** Replace the jumper. | Repair complete. |  |
>
> ### STEP 7. Check Customer Interface Box Wiring
>
> #### STEP 7A. Check the Engine Room Panel Start Supply Wire
>
> | **Conditions:** Open the customer interface box Disconnect engine room cable at connector C7 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine room panel start supply wire. Place one test lead on the engine room panel start supply pin in connector C7. Place the other test lead on the engine room panel start supply terminal on the customer interface box logic unit. | Less than 10 ohms resistance? **YES** | 7B |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> #### STEP 7B. Check the Remote Panel Start Supply Wire
>
> | **Conditions:** Open the customer interface box Disconnect remote panel cable at connector X4 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the remote panel start supply wire. Place one test lead on the remote panel start supply wire terminal in customer interface box X4 connector. Place the other test lead on the remote panel start supply wire terminal on the customer interface box logic unit. | Less than 10 ohms resistance? **YES** | 7C |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> #### STEP 7C. Check Customer Interface Box Logic Unit Prelube Activation Signal Wire
>
> | **Conditions:** Open the customer interface box Disconnect cable C1 connector from the connector interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the prelube activation signal wire. Place one test lead on the prelube activation signal terminal on the customer interface box logic unit. Place the other test lead in the prelube activation signal pin in the C1 connector. | Less than 10 ohms resistance? **YES** | 7D |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> #### STEP 7D. Check Customer Interface Box Logic Prelube Complete Signal Wire
>
> | **Conditions:** Open the customer interface box Disconnect cable C1 connector from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the prelube complete signal wire. Place one test lead on the prelube complete signal terminal on the customer interface box logic unit. Place the other test lead in the prelube complete signal pin in the C1 connector. | Less than 10 ohms resistance? **YES** | 7E |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> #### STEP 7E. Check Customer Interface Box Logic Unit Starter Relay Switch Signal Wire
>
> | **Conditions:** Open the customer interface box Disconnect cable C1 connector from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the start relay switch signal wire. Place one test lead on the starter relay switch signal terminal on the customer interface box logic unit. Place the other test lead in the starter relay switch signal pin in the C1 connector. | Less than 10 ohms resistance? **YES** | 7F |
> | Less than 10 ohms resistance? **NORepair:** Replace the customer interface box logic unit. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> #### STEP 7F. Check Customer Interface Box Logic Unit Starter Relay Return Wire
>
> | **Conditions:** Open the customer interface box Disconnect cable C1 connector from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the starter relay return wire. Place one test lead on the starter relay return terminal on the customer interface box logic unit. Place the other test lead in the starter relay return pin in the C1 connector. | Less than 10 ohms resistance? **YES** | 8A |
> | Less than 10 ohms resistance? **NORepair:** Replace the customer interface box logic unit. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> ### STEP 8. Check Start Signal to Engine
>
> #### STEP 8A. Check Starter Cable Starter Relay Switch Signals
>
> | **Conditions:** Disconnect cable connector C1 from the customer interface box Disconnect cable ring terminals from the starter relay switch. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the starter cable. Install a jumper between the starter relay switch signal pin and the starter relay switch return pin in connector C1. Place one test lead on the starter relay switch signal ring terminal. Place the other test lead on the starter relay switch return ring terminal. | Less than 10 ohms resistance? **YES** | 9A |
> | Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |
>
> ### STEP 9. Check Customer Interface Box Logic Unit
>
> #### STEP 9A. Check Customer Interface Box Logic Unit From the Engine Room Panel
>
> | **Conditions:** Open the customer interface box Disconnect cable C1 connector from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine room panel start supply wire. Place the positive test lead on the starter relay switch signal terminal on the customer interface box logic unit. Place the negative test lead on the starter relay switch return terminal on the customer interface box logic unit. Press the start button at the engine room panel. | 24 VDC? **YES** | 9B |
> | 24 VDC? **NORepair:** Replace the customer interface box logic unit. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> #### STEP 9B. Check Customer Interface Box Logic Unit From the Remote Panel
>
> | **Conditions:** Open the customer interface box Basic system is configured for start from remote panel (local start only lamp is not illuminated) Disconnect cable C1 connector from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the remote panel start supply wire. Place the positive test lead on the starter relay switch signal terminal on the customer interface box logic unit. Place the negative test lead on the starter relay switch return terminal on the customer interface box logic unit. Press the start button at the remote panel. | 24 VDC? **YES** | 10A |
> | 24 VDC? **NORepair:** Replace the customer interface box logic unit. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> ### STEP 10. Check Engine Room Panel
>
> #### STEP 10A. Check Start Signal from Engine Room Panel or Remote Panel
>
> | **Conditions:** Configure panel system to start from remote or engine room panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check start signal from engine room panel or remote panel. Place the positive test lead on the starter relay switch signal ring terminal. Place the negative test lead on the starter relay switch return ring terminal. Press the start button. | 24 VDC? **YESRepair:** Refer to Service Manual, QSK19 and QSK19 CM850 Modular Common Rail System Series Engines, Bulletin [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. | Repair complete. |
> | 24 VDC? **NORepair:** Replace the cable. | Repair complete. |  |
