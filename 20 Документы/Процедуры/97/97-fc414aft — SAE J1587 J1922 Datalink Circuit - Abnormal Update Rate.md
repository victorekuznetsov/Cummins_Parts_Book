---
type: "Процедура"
doc: "97-fc414aft"
title_en: "SAE J1587/J1922 Datalink Circuit - Abnormal Update Rate"
modified: "2004-10-15"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
  - "80141463"
  - "80248213"
families:
  - "QSM11"
  - "QSX15"
manuals:
  - "3666415"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc414aft.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc414aft.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
  - "перевод/машинный"
---

# SAE J1587/J1922 Datalink Circuit - Abnormal Update Rate

> [!abstract] Процедура · `97-fc414aft`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-10-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc414aft.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc414aft.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 414 (Послепродажное и OEM)

### SAE J1587/J1922 CAN Data Bus Circuit - Abnormal Update Rate (необычный уровень обновления)

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 414 PID(P): СПН: ФМИ: Лампа: СТО: | SAE J1587/J1922 CAN data bus Circuit - Abnormal Update Rate (ненормальный уровень обновления). Информация шины данных J1587 CAN была **не** получена модулем управления ICONTM в течение указанного времени. | Система ICONTM будет отключена. Двигатель запускается нормально. |

![[19802968.png]]

### Описание цепи

Шина данных J1587 CAN обеспечивает связь между двигателем ECM и модулем управления холостым ходом ICONTM. Вышеупомянутая схема может варьироваться, например, разъем или штифты, в зависимости от марки или модели транспортного средства. Установки OEM могут обеспечить взаимодействие между модулем управления холостым ходом и другими устройствами ICONTM.

### Расположение компонента

Шина данных J1587 CAN расположена в электропроводке OEM. Модуль управления ICONTM обычно подключается к проводной ремне J1587 за разъемом службы шины данных CAN в кабине. Модуль ICONTM может быть расположен в другом месте в зависимости от применения транспортного средства.

### Практические замечания

Эта неисправность устанавливается, когда информация, требуемая неработающим модулем управления ICONTM, **не** получена от двигателя ECM на шине данных J1587 CAN. Обычно он указывает на открытую схему на шине данных J1587 CAN. Проверьте двигатель ECM на наличие активных неисправностей и устраните их в первую очередь.

Система ICONTM может отображать только текущий активный код неисправности. Если одновременно активируется более одного кода неисправности, система ICONTM выдает наиболее приоритетную ошибку. После того, как ошибка была исправлена, будет выброшена следующая активная ошибка.

**Примечание:** Проблема может возникнуть с проводкой транспортного средства для шины данных J1708 CAN.

**Примечание:** Электронная система ICONTM может отображать более одного активного и неактивного кода неисправности одновременно.

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
>

**Для уменьшения возможности повреждения нового модуля управления бездействия ICONTM необходимо изучить все другие коды активных неисправностей до замены модуля управления бездействия ICONTM**.

> [!warning] ОСТОРОЖНО
>

**Для уменьшения возможности повреждения штифта и проводов жгута проводов используйте при проведении измерений следующий испытательный щуп: Номер детали 3822917 - розеточный пробный щуп типа Deutsch/AMP/Metri-Pack**

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Подтвердите статус вины. |  |
|  | **STEP 1A.** Проверьте модуль управления неработающим двигателем ICONTM на наличие активных кодов неисправностей. | Шина данных CAN работает правильно |
| ШАГ 2. | Проверьте электропроводку двигателя ICONTM. |  |
|  | **STEP 2A.** Проверить коннекторы соединительного устройства двигателя ICONTM и коннектора модуля управления ICONTM. | Никаких поврежденных контактов |
|  | **STEP 2B.** Проверьте полную проводку ремня для короткого замыкания от пин-кодов до пин-кодов. | Более 100 тыс. ом |
|  | **STEP 2B-1.** Определите, является ли система ICONTM послепродажным или OEM-производителем. | Система ICONTM является системой Aftermarket. |
|  | **STEP 2B-2.** Проверьте электропроводку кабины на короткое замыкание от пин-кодов до пин-кодов. | Более 100 тыс. ом |
|  | **STEP 2C.** Проверьте полную проводку ремня для короткого замыкания к батарее. | Контакт 7: 2.5-5.0 VDC; контакт 8: 0.0-2.5 VDC |
|  | **STEP 2C-1.** Определите, является ли система ICONTM послепродажным или OEM-производителем. | Система ICONTM является системой Aftermarket. |
|  | **STEP 2C-2.** Проверьте электропроводку двигателя на короткое замыкание к батарее. | Менее 1 VDC |
|  | **STEP 2D.** Проверьте полную проводку ремня для короткого замыкания на землю. | Более 100 тыс. ом |
|  | **STEP 2D-1.** Определите, является ли система ICONTM послепродажным или OEM-производителем. | Система ICONTM является системой Aftermarket. |
|  | **STEP 2D-2.** Проверьте упряжку электропроводки двигателя для короткого замыкания на землю. | Более 100 тыс. ом |
|  | **ШАГ 2E.** Проверьте полную проводку ремня для открытой цепи. | Менее 10 Ом |
|  | **STEP 2E-1.** Определите, является ли система ICONTM послепродажным или OEM-производителем. | Система ICONTM является системой Aftermarket. |
|  | **ШАГ 2Е-3.** Проверьте упряжку для проводов двигателя на открытом контуре. | Менее 10 Ом |
|  | **STEP 2F.** Проверьте наличие открытой цепи в электропроводке двигателя ECM. | Менее 10 Ом |
| ШАГ 3. | Проверьте устройство J1587. |  |
|  | **STEP 3A.** Проверить наличие неисправного устройства шины данных J1587 CAN. | Положительный провод к земле шасси (только J1587): 2.5-5.0 VDC, отрицательный провод на землю шасси (только J1587): 0.0-2.5 VDC |
| ШАГ 4. | Очистите код ошибки. |  |
|  | **STEP 4A.** Отключить код ошибки. | Код 414 ошибки обезврежен |

### ШАГ 1. Подтвердите статус вины.

#### ШАГ 1A. Проверьте модуль управления неработающим двигателем ICONTM на наличие активных кодов неисправностей.

| **Условия:** Включить переключатель зажигания. Подключите электронный сервис ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Инициировать кнопку CAN Data Bus Test с помощью инструментария службы, чтобы определить, работает ли шина данных CAN должным образом. | Шина данных CAN работает должным образом см. Неактивный или прерывистый код ошибки, процедура[[99-019-362 — Inactive or Intermittent Fault Code\|019-362]] | 4А |
|  | 2А |  |

### ШАГ 2. Проверьте электропроводку двигателя ICONTM.

#### ШАГ 2A. Осмотрите контактные линзы разъема для проводов двигателя ICONTM и коннектора модуля управления ICONTM.

| **Условия:** Выключите замок зажигания. Отсоедините разъем B модуля управления ICONTM от модуля управления ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Корродированные штифты Бент или сломанные штифты Отталкивание назад или расширенные штифты Проводная изоляция Повреждение Влажность в или на разъем Пропавшие или поврежденные соединительные штифты Коннекторная оболочка разбитая Грязь или мусор в или на разъемных контактах. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 2В |
| Ремонт поврежденных контактов Смывать грязь, мусор или влагу из контактов разъема с помощью электрического контактного очистителя, Номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт ремня электропроводки двигателя ICONTM. См. процедуру 019-206. Заменить электропроводку двигателя ICONTM. См. процедуру 019-043. Заменить модуль управления ICONTM idle. См. процедуру 019-358. По мере необходимости ремонтировать или заменять электропроводку OEM. | 4А |  |

#### ШАГ 2B. Проверьте полную проводку ремня для короткого замыкания от пин-кодов до пин-кодов.

| **Условия:** Выключите замок зажигания. Отсоедините разъемы ICONTM Idle Control Module A и B от модуля ICONTM idle Control. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление контакта 7 в неработающем модуле управления ICONTM разъем B-проводов жгута проводов ко всем другим штифтам в разъемах A- и B-проводов, за исключением контакта 8 в разъеме жгута проводов B-проводов. Измерьте сопротивление от контакта 8 в неработающем модуле управления ICONTM разъем B-проводов жгута проводов ко всем другим штифтам в разъемах A- и B-проводов, за исключением контакта 7 в разъеме жгута проводов B-проводов. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 100 тыс. ом | 2C |
|  | 2В-1-1 |  |

#### ШАГ 2B-1. Определите, является ли система ICONTM послепродажным или OEM-производителем.

| **Условия: **Ни одно |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| См. процедуру[[97-209-017 — ICON™ Idle Control System\|209-017]]. | Система ICONTM является системой Aftermarket. | 2В-2-2 |
| Проверьте штифт OEM-проводов, чтобы зажать короткое время в цепи шины данных CAN. | 4А |  |

#### ШАГ 2B-2. Проверьте электропроводку кабины для короткого замыкания от пин-кодов до пин-кодов.

| **Условия:** Выключите замок зажигания. Отключите 14-контактный проходной разъем. Отсоедините разъемы ICONTM Idle Control Module A и B от модуля ICONTM idle Control. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта G 14-контактной кабины проводов ремня, кабины проводов ремня, ко всем другим штифтам в разъеме, кроме контакта H. Измерьте сопротивление от контакта H 14-контактной кабины проводов, кабины проводов упряжки, ко всем другим штифтам в разъеме, кроме контакта G. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 100 000 Ом Ремонт или замена ремня электропроводки двигателя ICONTM Ремонт ремня электропроводки двигателя ICONTM. См. процедуру 019-206 или 019-207. Заменить электропроводку двигателя ICONTM. См. процедуру 019-043. | 4А |
| Ремонт или замена кабины ICONTM ремень проводов кабины. См. процедуру 019-207. Замените проводку кабины. См. процедуру 019-305. | 4А |  |

#### ШАГ 2C. Проверьте полную проводку ремня для короткого замыкания к батарее.

| **Условия:** Отсоединить разъем B модуля управления ICONTM от модуля управления ICONTM. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте напряжение от контакта 7 в неработающем модуле управления ICONTM B проводов ремня разъема к блоку двигателя. Измерьте напряжение от контакта 8 в неработающем модуле управления ICONTM B проводов ремня разъема к заземлению блока двигателя. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для многометровых методов использования, обратитесь к процедуре[[99-019-359 — Multimeter Usage\|019-359]]. | Контакт 7: 2.5-5.0 Контакты VDC 8: 0.0-2.5 VDC | 2D |
|  | 2С-1 |  |

#### ШАГ 2C-1. Определите, является ли система ICONTM послепродажным или OEM-производителем.

| **Условия: **Ни одно |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| См. процедуру[[97-209-017 — ICON™ Idle Control System\|209-017]]. | Система ICONTM является системой Aftermarket. | 2С-2 |
| Проверьте OEM-проводку, используя короткую батарею в цепи шины данных CAN. | 4А |  |

#### ШАГ 2C-2. Проверьте электропроводку двигателя для короткого замыкания к батарее.

| **Условия:** Включить переключатель зажигания. Отключите 14-контактный разъем. Отсоедините разъем B модуля управления ICONTM от модуля управления ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте напряжение от контакта 7 в неработающем модуле управления ICONTM B проводов ремня разъема к блоку двигателя. Измерьте напряжение от контакта 8 в неработающем модуле управления ICONTM B проводов ремня разъема к заземлению блока двигателя. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для многометровых методов использования, обратитесь к процедуре[[99-019-359 — Multimeter Usage\|019-359]]. | Менее 1 устранения неполадок VDC в соответствии с процедурой 019-166 или процедурой устранения неполадок OEM. | 4А |
| Ремонт или замена упряжки для проводов двигателя ICONTM Ремонт упряжки для проводов двигателя ICONTM. См. процедуру 019-206 или 019-207. Заменить электропроводку двигателя ICONTM. См. процедуру 019-043. | 4А |  |

#### ШАГ 2D. Проверьте полную проводку ремня для короткого замыкания на землю.

| **Условия:** Выключите замок зажигания. Отсоедините разъемы ICONTM Idle Control Module A и B от модуля ICONTM idle Control. Отсоедините разъем ECM OEM двигателя (содержащий выходной провод шины данных CAN). |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта 7 в неработающем модуле управления ICONTM B проводов ремня разъема к заземлению блока двигателя. Измерьте сопротивление от контакта 8 в неработающем модуле управления ICONTM B проводов ремня разъема к заземлению блока двигателя. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 100 тыс. ом | 2Е |
|  | 2D-1 |  |

#### ШАГ 2D-1. Определите, является ли система ICONTM послепродажным или OEM-производителем.

| **Условия: **Ни одно |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| См. процедуру[[97-209-017 — ICON™ Idle Control System\|209-017]]. | Система ICONTM является системой Aftermarket. | 2D-2 |
| Проверьте OEM-проводку, чтобы заземлиться в цепи шины данных CAN. | 4А |  |

#### ШАГ 2D-2. Проверьте упряжку проводов двигателя для короткого замыкания на землю.

| **Условия:** Выключите замок зажигания. Отсоедините разъем B модуля управления ICONTM от модуля управления ICONTM. Отключите 14-контактный проходной разъем. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта 7 в неработающем модуле управления ICONTM B проводов ремня разъема к заземлению блока двигателя. Измерьте сопротивление от контакта 8 в неработающем модуле управления ICONTM B проводов ремня разъема к заземлению блока двигателя. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Устранение неполадок более 100k Ом в соответствии с процедурой 019-166 или процедурой устранения неполадок OEM. | 4А |
| Ремонт или замена упряжки для проводов двигателя ICONTM Ремонт упряжки для проводов двигателя ICONTM. См. процедуру 019-206. Заменить электропроводку двигателя ICONTM. См. процедуру 019-043. | 4А |  |

#### ШАГ 2E. Проверьте полную проводку ремня для открытой цепи.

| **Условия:** Выключите замок зажигания. Отсоедините разъем B модуля управления ICONTM от модуля управления ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта 7 в неработающем модуле управления ICONTM B проводов жгута разъема к положительному (+) контакту A разъема шины данных J1587 CAN (для 6-контактного разъема Deutsch) или контакту F (для 9-контактного разъема Deutsch). Измерить сопротивление от контакта 8 в ICONTM неработающего модуля управления B проводов жгута разъема к отрицательному (-) контакту B разъема шины данных J1587 CAN (для 6-контактного разъема Deutsch) или контакту G (для 9-контактного разъема Deutsch). **Примечание:** Вышеупомянутые шины данных CAN, положительные и отрицательные соединения типичны для 6-контактных и 9-контактных разъемов Deutsch. См. руководство по OEM для соответствующих номеров шины данных CAN с положительным и отрицательным значениями, если ваш автомобиль настроен по-другому. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Менее 10 Ом | 2F |
|  | 2Е-1 |  |

#### ШАГ 2E-1. Определите, является ли система ICONTM послепродажным или OEM-производителем.

| **Условия: **Ни одно |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| См. процедуру[[97-209-017 — ICON™ Idle Control System\|209-017]]. | Система ICONTM является системой Aftermarket. | 2Е-2 |
| Проверьте OEM-проводку для открытия в цепи шины данных CAN. | 4А |  |

#### ШАГ 2E-2. Проверьте наличие открытой цепи в ремне электропроводки двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините разъемы ICONTM Idle Control Module A и B от модуля ICONTM idle Control. Отсоедините 14-контактный проходной разъем на переборке транспортного средства. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление от контакта 7 в ICONTM холостого модуля управления B проводов жгута разъёма к контакту G кабины проводов жгута разъёма, двигателя проводов жгута стороны. Измерить сопротивление от контакта 8 в ICONTM холостого модуля управления B проводов жгута разъёма к контакту H кабины проводов жгута разъёма, двигателя проводов жгута стороны. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Устранение неполадок менее 10 Ом в соответствии с процедурой 019-166 или процедурой устранения неполадок OEM. | 4А |
| Ремонт или замена ремня электропроводки двигателя ICONTM. Ремонт ремня электропроводки двигателя ICONTM. См. процедуру 019-206 или 019-207. Заменить электропроводку двигателя ICONTM. См. процедуру 019-043. | 4А |  |

#### ШАГ 2F. Проверьте наличие открытой цепи в электропроводке двигателя ECM.

| **Условия:** Выключите замок зажигания. Отключите разъем ECM OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление контакта 27 на разъеме CELECTTM Plus ECM OEM и контакте А 6-контактного или контактного F 9-контактного разъема. Измерить сопротивление от контакта 8 на разъеме CELECTTM Plus ECM OEM и контакт B 6-контактного или контактного G 9-контактного разъема. Измерьте сопротивление от контакта 26 на разъеме ISM или ISX ECM OEM и контакте А 6-контакта или контакта F 9-контактного разъема. Измерить сопротивление от контакта 27 на ISM или ISX ECM OEM разъеме и контакт B 6-контактного или контакт G 9-контактного разъема. Измерьте сопротивление контакта 10 на разъеме ISM CM870, ISM CM875 или ISX CM870 ECM OEM и контакте А 6-контакта или контакта F 9-контактного разъема. Измерить сопротивление от контакта 20 на разъеме ISM CM870, ISM CM875 или ISX CM870 ECM OEM и контакте B 6-контакта или контакта G 9-контактного разъема. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Менее 10 Ом | 3А |
| Ремонт или замена OEM проводов жгута. См. руководство по устранению неполадок OEM. | 4А |  |

### ШАГ 3. Проверьте устройство J1587.

#### ШАГ 3A. Проверьте наличие неисправного устройства шины данных J1587 CAN.

| **Условия:** Включить переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| **Примечание:** Это устройство может быть автоматической коробкой передач, автоматической тормозной системой или электронным прибором. Найдите предохранитель питания для устройства (устройств) J1587. Вытаскивайте предохранители по одному за раз. Когда предохранитель вытягивается из держателя предохранителя, измеряйте напряжение от положительного (+) контакта А разъема шины данных J1587 CAN, стороны кабины (для 6-контактного разъема Deutsch) или контакта F (для 9-контактного разъема Deutsch) с землей шасси. Когда предохранитель вытягивается из держателя предохранителя, измеряйте напряжение от отрицательного (-) контакта B разъема шины данных J1587 CAN, стороны кабины (для 6-контактного разъема Deutsch) или контакта G (для 9-контактного разъема Deutsch) с землей шасси. **Примечание: **Устройство J1587, которое обычно вызывает проблему, представляет собой электронный прибор. Вышеупомянутые шины данных CAN, положительные и отрицательные соединения типичны для 6-контактных и 9-контактных разъемов Deutsch. См. руководство по OEM для соответствующих номеров шины данных CAN с положительным и отрицательным значениями, если ваш автомобиль настроен по-другому. | Положительный провод к земле шасси (только J1587): 2.5-5.0 VDC Отрицательный провод на земле шасси (только J1587): От 0,0 до 2,5 VDC Заменить модуль управления холостым режимом ICONTM. См. процедуру[[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Ремонт завершён |
| Устройство шины данных CAN нестандартно или неисправно ремонтируется или заменяется по мере необходимости. См. руководство по устранению неполадок OEM. | 4А |  |

### ШАГ 4. Очистите код ошибки.

#### ШАГ 4A. Отключите код неисправности.

| **Условия: **Соединить все компоненты. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Цикл переключателя зажигания для проверки кода неисправности неактивен. | Код 414 ошибки обезврежен | Ремонт завершён |
| Устранение неполадок с оставшимися активными кодами неисправностей. | Соответствующие диаграммы устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 414 (Aftermarket and OEM)
>
> ### SAE J1587/J1922 Datalink Circuit - Abnormal Update Rate
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 414 PID(P): SPN: FMI: Lamp: SRT: | SAE J1587/J1922 Datalink Circuit - Abnormal Update Rate. J1587 datalink information was **not** received by the ICON™ idle control module within the specified time. | The ICON™ system will be disabled. Engine will start normally. |
>
> ### Circuit Description
>
> The J1587 datalink provides communication between the engine ECM and the ICON™ idle control module. The above circuit diagram can vary, such as connector or pins, depending on the vehicle make or model. OEM installations can possibly provide the harnessing between the idle control module and other ICON™ devices.
>
> ### Component Location
>
> The J1587 datalink is located in the OEM wiring harness. The ICON™ idle control module typically connects into the J1587 wiring harness behind the in-cab datalink service connector. The ICON™ module can be located in a different location depending on the vehicle application.
>
> ### Shoptalk
>
> This fault is set when information that is required by the ICON™ idle control module is **not** received from the engine ECM on the J1587 datalink. It typically indicates an open circuit on the J1587 datalink. Check the engine ECM for active faults and troubleshoot those first.
>
> The ICON™ system can display **only** the present active fault code. If more than one fault code is active at the same time, the ICON™ system flashes out the highest priority fault. After the fault has been corrected then the next active fault will be flashed out.
>
> **NOTE:** A problem can exist with the vehicle wiring for the J1708 datalink.
>
> **NOTE:** The ICON™ electronic service tool can display more than one active and or inactive fault codes at the same time.
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
>
> **To reduce the possibility of damaging a new ICON™ idle control module, all other active fault codes must be investigated prior to replacing the ICON™ idle control module.**
>
> **CAUTION · Осторожно**
>
> **To reduce the possibility of pin and harness damage, use the following test lead when taking a measurement: Part Number 3822917 - female Deutsch/AMP/Metri-Pack test lead.**
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Confirm the fault status. |  |
> |  | **STEP 1A.** Check the engine ICON™ idle control module for active fault codes. | Datalink operating properly |
> | STEP 2. | Check the ICON™ engine harness. |  |
> |  | **STEP 2A.** Inspect the ICON™ engine harness and ICON™ idle control module connector pins. | No damaged pins |
> |  | **STEP 2B.** Check the complete harness for a short circuit from pin to pin. | More than 100k ohms |
> |  | **STEP 2B-1.** Identify whether the ICON™ system is an Aftermarket or an OEM. | ICON™ system is Aftermarket |
> |  | **STEP 2B-2.** Check the cab harness for a short circuit from pin to pin. | More than 100k ohms |
> |  | **STEP 2C.** Check the complete harness for a short circuit to the battery. | Pin 7: 2.5 to 5.0 VDC; Pin 8: 0.0 to 2.5 VDC |
> |  | **STEP 2C-1.** Identify whether the ICON™ system is an Aftermarket or an OEM. | ICON™ system is Aftermarket |
> |  | **STEP 2C-2.** Check the engine harness for a short circuit to the battery. | Less than 1 VDC |
> |  | **STEP 2D.** Check the complete harness for a short circuit to ground. | More than 100k ohms |
> |  | **STEP 2D-1.** Identify whether the ICON™ system is an Aftermarket or an OEM. | ICON™ system is Aftermarket |
> |  | **STEP 2D-2.** Check the engine harness for a short circuit to ground. | More than 100k ohms |
> |  | **STEP 2E.** Check the complete harness for an open circuit. | Less than 10 ohms |
> |  | **STEP 2E-1.** Identify whether the ICON™ system is an Aftermarket or an OEM. | ICON™ system is Aftermarket |
> |  | **STEP 2E-3.** Check the engine harness for an open circuit. | Less than 10 ohms |
> |  | **STEP 2F.** Check for an open circuit in the engine ECM harness. | Less than 10 ohms |
> | STEP 3. | Check the J1587 device. |  |
> |  | **STEP 3A.** Check for a malfunctioning J1587 datalink device. | Positive wire to chassis ground (J1587 only): 2.5 to 5.0 VDC, negative wire to chassis ground (J1587 only): 0.0 to 2.5 VDC |
> | STEP 4. | Clear the fault code. |  |
> |  | **STEP 4A.** Disable the fault code. | Fault Code 414 cleared |
>
> ### STEP 1. Confirm the fault status.
>
> #### STEP 1A. Check the engine ICON™ idle control module for active fault codes.
>
> | **Conditions:** Turn keyswitch ON. Connect the ICON™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Initiate the Datalink Test button with the service tool to determine if the datalink is operating properly. | Datalink operating properly Refer to Inactive or Intermittent Fault Code, Procedure [[99-019-362 — Inactive or Intermittent Fault Code\|019-362]] | 4A |
> |  | 2A |  |
>
> ### STEP 2. Check the ICON™ engine harness.
>
> #### STEP 2A. Inspect the ICON™ engine harness and ICON™ idle control module connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module B connector from the ICON™ idle control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 2B |
> | Repair the damaged pins Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the ICON™ engine harness. Refer to Procedure 019-206. Replace the ICON™ engine harness. Refer to Procedure 019-043. Replace the ICON™ idle control module. Refer to Procedure 019-358. Repair or replace the OEM wiring harness as necessary. | 4A |  |
>
> #### STEP 2B. Check the complete harness for a short circuit from pin to pin.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module A and B connectors from the ICON™ idle control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 7 in the ICON™ idle control module B harness connector to all other pins in the A and B harness connectors, except pin 8 in the B harness connector. Measure the resistance from pin 8 in the ICON™ idle control module B harness connector to all other pins in the A and B harness connectors, except pin 7 in the B harness connector. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 2C |
> |  | 2B-1 |  |
>
> #### STEP 2B-1. Identify whether the ICON™ system is an Aftermarket or an OEM.
>
> | **Conditions:** None |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Refer to Procedure [[97-209-017 — ICON™ Idle Control System\|209-017]]. | ICON™ system is Aftermarket | 2B-2 |
> | Check the OEM wiring harness pin to pin for a short in the datalink circuit. | 4A |  |
>
> #### STEP 2B-2. Check the cab harness for a short circuit from pin to pin.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the 14-pin pass-through connector. Disconnect the ICON™ idle control module A and B connectors from the ICON™ idle control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin G of the 14-pin cab harness, cab harness side, to all other pins in the connector except pin H. Measure the resistance from pin H of the 14-pin cab harness, cab harness side, to all other pins in the connector except pin G. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms Repair or replace the ICON™ engine harness Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. | 4A |
> | Repair or replace the ICON™ cab harness Repair the cab harness. Refer to Procedure 019-207. Replace the cab harness. Refer to Procedure 019-305. | 4A |  |
>
> #### STEP 2C. Check the complete harness for a short circuit to the battery.
>
> | **Conditions:** Disconnect the ICON™ idle control module B connector from the ICON™ idle control module. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the voltage from pin 7 in the ICON™ idle control module B harness connector to engine block ground. Measure the voltage from pin 8 in the ICON™ idle control module B harness connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For multimeter usage techniques, refer to Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | Pin 7: 2.5 to 5.0 VDC Pin 8: 0.0 to 2.5 VDC | 2D |
> |  | 2C-1 |  |
>
> #### STEP 2C-1. Identify whether the ICON™ system is an Aftermarket or an OEM.
>
> | **Conditions:** None |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Refer to Procedure [[97-209-017 — ICON™ Idle Control System\|209-017]]. | ICON™ system is Aftermarket | 2C-2 |
> | Check the OEM wiring harness a short to battery in the datalink circuit. | 4A |  |
>
> #### STEP 2C-2. Check the engine harness for a short circuit to the battery.
>
> | **Conditions:** Turn keyswitch ON. Disconnect the 14-pin connector. Disconnect the ICON™ idle control module B connector from the ICON™ idle control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the voltage from pin 7 in the ICON™ idle control module B harness connector to engine block ground. Measure the voltage from pin 8 in the ICON™ idle control module B harness connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For multimeter usage techniques, refer to Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | Less than 1 VDC Troubleshoot per Procedure 019-166 or the OEM troubleshooting procedure. | 4A |
> | Repair or replace the ICON™ engine harness Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. | 4A |  |
>
> #### STEP 2D. Check the complete harness for a short circuit to ground.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module A and B connectors from the ICON™ idle control module. Disconnect the engine ECM OEM connector (containing the datalink output wire). |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 7 in the ICON™ idle control module B harness connector to engine block ground. Measure the resistance from pin 8 in the ICON™ idle control module B harness connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 2E |
> |  | 2D-1 |  |
>
> #### STEP 2D-1. Identify whether the ICON™ system is an Aftermarket or an OEM.
>
> | **Conditions:** None |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Refer to Procedure [[97-209-017 — ICON™ Idle Control System\|209-017]]. | ICON™ system is Aftermarket | 2D-2 |
> | Check the OEM wiring harness short to ground in the datalink circuit. | 4A |  |
>
> #### STEP 2D-2. Check the engine harness for a short circuit to ground.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module B connector from the ICON™ idle control module. Disconnect the 14-pin pass-through connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 7 in the ICON™ idle control module B harness connector to engine block ground. Measure the resistance from pin 8 in the ICON™ idle control module B harness connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms Troubleshoot per Procedure 019-166 or the OEM troubleshooting procedure. | 4A |
> | Repair or replace the ICON™ engine harness Repair the ICON™ engine harness. Refer to Procedure 019-206. Replace the ICON™ engine harness. Refer to Procedure 019-043. | 4A |  |
>
> #### STEP 2E. Check the complete harness for an open circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module B connector from the ICON™ idle control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 7 in the ICON™ idle control module B harness connector to positive (+) pin A of the J1587 datalink connector (for the 6-pin Deutsch connector), or pin F (for the 9-pin Deutsch connector). Measure the resistance from pin 8 in the ICON™ idle control module B harness connector to negative (-) pin B of the J1587 datalink connector (for the 6-pin Deutsch connector), or pin G (for the 9-pin Deutsch connector). **NOTE:** The above-mentioned datalink positive and negative connections are typical for the 6-pin and 9-pin Deutsch connectors. Refer to the OEM manual for the appropriate datalink positive and negative pin numbers if your vehicle is configured differently. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 10 ohms | 2F |
> |  | 2E-1 |  |
>
> #### STEP 2E-1. Identify whether the ICON™ system is an Aftermarket or an OEM.
>
> | **Conditions:** None |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Refer to Procedure [[97-209-017 — ICON™ Idle Control System\|209-017]]. | ICON™ system is Aftermarket | 2E-2 |
> | Check the OEM wiring harness for an open in the datalink circuit. | 4A |  |
>
> #### STEP 2E-2. Check for an open circuit in the engine harness.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module A and B connectors from the ICON™ idle control module. Disconnect the 14-pin pass-through connector at the vehicle bulkhead. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 7 in the ICON™ idle control module B harness connector to pin G of the cab harness connector, engine harness side. Measure the resistance from pin 8 in the ICON™ idle control module B harness connector to pin H of the cab harness connector, engine harness side. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 10 ohms Troubleshoot per Procedure 019-166 or the OEM troubleshooting procedure. | 4A |
> | Repair or replace the ICON™ engine harness. Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. | 4A |  |
>
> #### STEP 2F. Check for an open circuit in the engine ECM harness.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ECM OEM connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 27 on a CELECT™ Plus ECM OEM connector and pin A of the 6-pin or pin F of the 9-pin connector. Measure the resistance from pin 8 on a CELECT™ Plus ECM OEM connector and pin B of the 6-pin or pin G of the 9-pin connector. Measure the resistance from pin 26 on an ISM or ISX ECM OEM connector and pin A of the 6-pin or pin F of the 9-pin connector. Measure the resistance from pin 27 on an ISM or ISX ECM OEM connector and pin B of the 6-pin or pin G of the 9-pin connector. Measure the resistance from pin 10 on an ISM CM870, ISM CM875, or ISX CM870 ECM OEM connector and pin A of the 6-pin or pin F of the 9-pin connector. Measure the resistance from pin 20 on an ISM CM870, ISM CM875, or ISX CM870 ECM OEM connector and pin B of the 6-pin or pin G of the 9-pin connector. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 10 ohms | 3A |
> | Repair or replace the OEM harness. Refer to the OEM troubleshooting manual. | 4A |  |
>
> ### STEP 3. Check the J1587 device.
>
> #### STEP 3A. Check for a malfunctioning J1587 datalink device.
>
> | **Conditions:** Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | **NOTE:** This device can be an automatic transmission, automatic braking system, or electronic dash. Locate the power fuse for the J1587 device(s). Pull out the fuses one at a time. As the fuse is pulled from the fuse-holder, measure the voltage from positive (+) pin A of the J1587 datalink connector, cab side (for the 6-pin Deutsch connector), or pin F (for the 9-pin Deutsch connector) to chassis ground. As the fuse is pulled from the fuse-holder, measure the voltage from negative (-) pin B of the J1587 datalink connector, cab side (for the 6-pin Deutsch connector), or pin G (for the 9-pin Deutsch connector) to chassis ground. **NOTE:** The J1587 device that typically will cause a problem is an electronic dash. The above-mentioned datalink positive and negative connections are typical for the 6-pin and 9-pin Deutsch connectors. Refer to the OEM manual for the appropriate datalink positive and negative pin numbers if your vehicle is configured differently. | Positive wire to chassis ground (J1587 only): 2.5 to 5.0 VDC Negative wire to chassis ground (J1587 only): 0.0 to 2.5 VDC Replace the ICON™ idle control module. Refer to Procedure [[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Repair Complete |
> | Datalink device is nonstandard or defective Repair or replace as necessary. Refer to the OEM troubleshooting manual. | 4A |  |
>
> ### STEP 4. Clear the fault code.
>
> #### STEP 4A. Disable the fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Cycle the keyswitch to verify the fault code is inactive. | Fault Code 414 cleared | Repair complete |
> | Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
