---
aliases:
  - "Шины данных двигателя"
type: "Процедура"
doc: "105-019-428"
title_en: "Engine Datalinks"
title_ru: "Шины данных двигателя"
modified: "2023-02-28"
engines:
  - "37292556"
  - "37295879"
  - "41343322"
  - "93058669"
families:
  - "C8.3 · 6C8.3"
  - "NT/NTA855 · ISM/QSM11"
  - "QST30"
manuals:
  - "3666214"
  - "3666266"
  - "4021442"
figures: 31
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/105/105-019-428.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/105-019-428.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "двигатель/NT/NTA855"
  - "двигатель/QST30"
  - "группа/105"
  - "перевод/машинный"
---

# Engine Datalinks
**Шины данных двигателя**

> [!abstract] Процедура · `105-019-428`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3, NT/NTA855 · ISM/QSM11, QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]], [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]], [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section 19 - Electronic Engine Controls · Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2023-02-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/105/105-019-428.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/105-019-428.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Выбор сервисного инструмента

#### Рекомендованный сервисный инструмент Cummins®

- Цифровой мультиметр, номер детали 3164489

#### Дополнительные сервисные позиции

- Соответствующий испытательный щуп(ы)

### Общие сведения

> [!warning] ОСТОРОЖНО
> Правильные провода и/или одобренный Cummins® инструмент для тестирования цепи должны использоваться при работе с электрическими разъемами для предотвращения расширения штифта и повреждения разъема.

Шина данных CAN двигателя состоит из схемы, расположенной в ремне проводов двигателя, которая передает цифровую информацию между модулем управления двигателем (ECM) и другими устройствами на двигателе и шасси. На старых двигателях схема шины данных CAN поддерживает протокол J1587/J1708. На новых двигателях схема шины данных CAN поддерживает протокол J1939.

Шина данных CAN двигателя обеспечивает точку доступа для инструментария обслуживания, такого как рекомендуемый инструмент электронного обслуживания Cummins® или эквивалент, для связи с ECM. Сервисная инструментальная система может взаимодействовать с ECM на шине данных CAN двигателя, свободной от трафика шины данных CAN с других электронных устройств, которые могут присутствовать на шине данных OEM CAN.

Сеть шины данных CAN 2016 модельного года и новые двигатели могут работать по 250K baud или 500K baud. Скорость Бод относится к скорости, с которой информация транслируется в сети шины данных CAN. Только один уровень baud может быть установлен для любой сети шины данных CAN. По умолчанию ставка baud для модельного года 2016 и более новых двигателей составляет 500 К. baud. По умолчанию показатель baud для моделей 2015 года и более старых двигателей составляет 250 КБ.

Приложения, оснащенные сетями шины данных CAN, способными поддерживать скорости шины данных CAN 500K, дифференцируются по шаблону ключа на 9-контактном разъеме шины данных CAN. Этот разъем также отличается от 9 разъемов, которые поддерживают только 250K скорости шины данных baud CAN. Инструмент адаптера, номер детали 5299126, доступен для подключения к приложениям, оснащенным сетями шины данных 500K baud CAN через 9-контактный разъем.

SAE J1939 Обратная проводка Упряжка Обзор:

SAE J1939 имеет строгие правила, которые должны соблюдаться для успешного общения. Понимание некоторых фундаментальных принципов SAE J1939 поможет проверить, соблюдаются ли эти руководящие принципы.

Основным компонентом системы SAE J1939 является магистральная проводка. Проводная упряжка может быть до 40 м[131 фута] в длину. Стержневой проводной упряжкой на каждом конце оканчивают резисторы 120 Ом.

Максимально 30 различных устройств могут быть подключены к магистрали SAE J1939 одновременно. Каждое устройство, такое как адаптер шины данных CAN, соединено с магистралью через заглушку, которая может быть длиной до 1 м [3,2 фута ]. Разъем заглушки представляет собой 3-контактную вилку.

![[19802395.png]]

Концевые резисторы (1) ** должны быть на месте на розетках магистральной проводов OEM (2) для поддержания надлежащей связи. Каждый резистор составляет 120 Ом и расположен в съемной крышке. Это сопротивление требуется при общении с рекомендованным электронным сервисным оборудованием Cummins® или эквивалентом через шину данных J1939 CAN.

![[19802397.png]]

Некоторые ремни для проводов двигателя включают в себя полный ремень магистральной проводов SAE J1939. Если эта магистральная проводка поставляется, подключение к рекомендуемой электронной сервисной оснастке Cummins® или эквиваленту осуществляется либо 9-контактным разъемом шины данных CAN (1), Частью № 4918416, либо 3-контактным сосудом (2), Частью № 3165141.

Чтобы проверить хребет J1939, переключатель зажигания переключателя в положение выключения. Измерить сопротивление от шины данных SAE J1939 CAN положительного (+) штифта к шине данных SAE J1939 CAN отрицательного (-) штифта 3-контактного разъема DeutschTM.

Мультиметр покажет 60 Ом, когда жгут проводов двигателя обеспечил основу на шине данных CAN.

![[19802614.png]]

Если жгут для проводов двигателя не поставляет ремень магистральной проводов J1939, а разъем шины данных CAN является 3-контактным сосудом, придется добавить мини-ремень проводов.

![[19802394.png]]

Двигатель CAN Data Bus Connectors

Разъем шины данных CAN, доступный на ремне электропроводки двигателя, будет зависеть от схемы шины данных CAN в ремне электропроводки двигателя и винтажа двигателя. Разъемы шины данных CAN для двигателей Cummins® кратко изложены в таблице ниже.

| Тип подключения | Поддерживаемые протоколы шины данных CAN |
|---|---|
| 2 PIN Weather PackTM | J1587/J1708 |
| 3 pin DeutschTM | 1939 год |
| 6 pin DeutschTM | J1587/J1708 |
| 9 pin DeutschTM | J1587/J1708, J1939 |

![[nobox.png]]

Каждый тип разъема более подробно описан в следующей информации.

Разъем 9 pin DeutschTM может обеспечивать связь SAE J1587/SAE 1708 и SAE J1939 со скоростью шины передачи данных 250k baud и напряжением батареи. Ниже приведены вырезы для 9-контактного разъема:

| Тип I (250k) |  |
|---|---|
| Пин | сигнал |
| А. | земля |
| B | Незакрученная батарея |
| C | J1939 CAN Data Bus (+) (недоступная ссылка) |
| D | J1939 CAN Data Bus (-) (недоступная ссылка) |
| Е | J1939 CAN Data Bus (щит) (**не** применим для морских судов) |
| F | J1708 CAN Data Bus (+) |
| GGG | J1708 CAN Data Bus (-) (недоступная ссылка) |
| Hе | Открыть |
| Джей | Открыть |

![[19400739.png]]

Аналогичный 9-контактный разъем DeutschTM также может обеспечивать связь SAE J1939 со скоростью шины передачи данных 500 КБ и напряжением батареи. Ниже приведены вырезы для 9-контактного разъема:

| Зеленый тип II (500К) |  |
|---|---|
| Пин | сигнал |
| А. | земля |
| B | Незакрученная батарея |
| C | J1939 CAN Data Bus (+) (недоступная ссылка) |
| D | J1939 CAN Data Bus (-) (недоступная ссылка) |
| Е | J1939 CAN Data Bus (щит) (**не** применим для морских судов) |
| F | J1708 CAN Data Bus (+) |
| GGG | J1708 CAN Data Bus (-) (недоступная ссылка) |
| Hе | Открыть |
| Джей | Открыть |

![[19r99337.png]]

6-контактный разъем DeutschTM, номер детали 3824805, установлен на некоторых двигателях. Этот разъем поставляет SAE J1587/J1708, а также напряжение батареи. Ниже приведены вырезы для 6-контактного разъема:

| Пин | сигнал |
|---|---|
| А. | J1708 CAN Data Bus (+) |
| B | J1708 CAN Data Bus (-) (недоступная ссылка) |
| C | Незакрученная батарея (+) |
| D | Открыть |
| Е | земля |
| F | Открыть |

![[19400740.png]]

> [!note] Примечание
> Для двигателей CELECT PlusTM, не используйте 6-контактный разъем шины данных CAN в кабине для калибровки ECM. Используйте разъем шины данных CAN, найденный на двигателе.

![[19400418.png]]

3-контактные разъемы SAE J1939 DeutschTM также установлены на некоторых ремнях электропроводки двигателя Cummins®. Могут присутствовать два возможных типа 3-контактных разъемов: 3-контактная пробка (1), номер детали 3824288; и 3-контактная емкость (2), номер детали 3824290. Ниже приведены вырезы для 3-контактного разъема:

| Пин | сигнал |
|---|---|
| А. | J1939 CAN Data Bus (+) (недоступная ссылка) |
| B | J1939 CAN Data Bus (-) (недоступная ссылка) |
| C | J1939 CAN Data Bus (щитовой) |

3-контактный разъем **только ** поддерживает шину данных SAE J1939 CAN.

Для соответствия стандарту SAE J1939 разъём сосуда с 3 штифтами ** должен быть в пределах 0,66 м \[2,16 фута \] от ECM. Использование микро-костной электропроводки J1939, номер детали 3163096, может потребоваться для надлежащего сопротивления прерыванию. Мини-магистраль проводов жгут требуется, когда **no** магистраль предоставляется на шине данных CAN. Гендерный кабель, номер детали 3163597, может потребоваться для подключения мини-магистральной проводов к электропроводке двигателя или кабелю для инструментальной обработки.

> [!note] Примечание
> Если между контактами A и B 3-контактного разъема измеряется сопротивление 60 Ом, то на шине данных CAN находится магистраль.

![[19802392.png]]

2-контактный разъем установлен на многих старых двигателях, и только он обеспечивает поддержку SAE J1587 / J1708 (без питания от батареи). Ниже приведены вырезы для 2-контактного разъема:

| Пин | сигнал |
|---|---|
| А. | J1587/J1708 CAN шина данных (+) |
| B | J1587/1708 CAN шина данных (-) |

![[19400406.png]]

Некоторые двигатели имеют 2-контактный сервисный инструмент питания Weather PackTM, расположенный в ремне электропроводки двигателя. Разъем может быть использован для питания любого сервисного инструментального устройства.

| Пин | сигнал |
|---|---|
| А. | Незакрученная батарея (+) |
| B | Земля (-) |

![[ee8coge.png]]

### Проверка сопротивления

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

> [!warning] ОСТОРОЖНО
> Для шины данных CAN двигателя J1939 используйте испытательный щуп, номер детали 3822758, на разъеме ECM, чтобы избежать повреждения контактов разъема. Используйте измерительный щуп, номер детали 3824811, для 9-контактного разъема DeutschTM. Используйте пробный щуп, номер детали 3823993 для контактного сосуда 3-контактного разъема DeutschTM или испытательного щупа, номер детали 3823994 для разъема 3-контактного DeutschTM.

> [!warning] ОСТОРОЖНО
> Для шины данных CAN двигателя J1587/J1708 используйте испытательный щуп, номер детали 3622758, на разъеме ECM, чтобы уменьшить возможность повреждения контактов разъема. Используйте измерительный щуп 3824800 для 6-контактного разъема DeutschTM. Используйте измерительный щуп 3823995 для разъема 2 pin PackardTM.

Определить тип шины данных CAN двигателя, доступной на двигателе, J1939 или J1587/J1708. Следуйте инструкциям, предоставленным для измерения сопротивления для типа идентифицированной шины данных CAN двигателя.

![[19802614.png]]

J1939 Двигатель МОЖЕТ ставить шину данных

- Отсоедините аккумуляторные батареи.
- Отсоедините разъем жгута проводов двигателя от ECM. Переведите замок зажигания в положение OFF.

![[19c01212.png]]

Вставьте измерительный щуп в шину данных SAE J1939 CAN положительного (+) штифта проводов двигателя с помощью разъема ECM и соедините испытательный щуп с многометровым щупом. Вставьте другой измерительный щуп в шину данных SAE J1939 CAN положительного (+) штифта 3-х штифтового или 9-ти штифтового разъема DeutschTM и соедините испытательный щуп с мультиметром.

Измерьте сопротивление. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

Если цепь ** не** закрыта, отремонтируйте или замените электропроводку двигателя.

См. руководство по устранению неполадок и ремонту для получения дополнительной информации.

![[nobox.png]]

Вставьте многометровый свинец в шину данных SAE J1939 CAN отрицательного (-) разъема ECM электропроводки двигателя. Прикосновение к другому приводит к отрицательному (-) значку шины данных SAE J1939 разъема 3-х или 9-ти контактов DeutschTM. Измерьте сопротивление. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

Если цепь ** не** закрыта, отремонтируйте или замените электропроводку двигателя.

См. руководство по устранению неполадок и ремонту для получения дополнительной информации.

![[nobox.png]]

Если значения верны, схема ** должна быть проверена на короткое замыкание на землю и короткое замыкание от контакта к контакту.

Удалите измерительный щуп из шины данных SAE J1939 CAN отрицательного (-) штифта разъема ECM проводов двигателя и вставьте измерительный щуп в штифт шины данных SAE J1939 CAN (щитовой) штифт. Прикосновение к отрицательному мультиметру приводит к шине данных SAE J1939 CAN (щитовой) разъема 3-х или 9-ти штифтов DeutschTM. Измерьте сопротивление.

Мультиметр **должен** показать замкнутую цепь (10 Ом и менее). Если в любом из этих этапов измеряется более 10 Ом, может быть открытая цепь в шине данных SAE J1939 CAN (щитовой) штифт, шине данных SAE J1939 CAN отрицательный (-) штифт или шине данных SAE J1939 CAN положительный (+) штифт, или полярность ** не** правильная.

![[19c01212.png]]

J1587/J1708 Двигатель CAN шина данных

Переведите замок зажигания в положение OFF. Отсоедините электропроводку двигателя от ECM.

Вставьте измерительный щуп в шину данных SAE J1587 CAN положительного (+) штифта проводов двигателя упряжки ECM разъема и соедините испытательный щуп с многометровым щупом. Вставьте другой измерительный щуп в шину данных SAE J1587 CAN положительного (+) штифта 2-х штифтового или 6-ти штифтового разъема и соедините испытательный щуп с другим многометровым щупом. Измерьте сопротивление. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

Если цепь ** не** закрыта, отремонтируйте или замените электропроводку двигателя.

См. руководство по устранению неполадок и ремонту для получения дополнительной информации.

![[19c01188.png]]

Удалите пробный щуп из шины данных SAE J1587 CAN положительного (+) штифта и вставьте пробный щуп в шину данных SAE J1587 CAN отрицательного (-) штифта разъема ECM. Удалите другой измерительный щуп из шины данных SAE J1587 CAN положительный (+) штифт и вставьте измерительный щуп в шину данных SAE J1587 CAN отрицательный (-) штифт 2 штифта или 6 штифтового разъема. Измерьте сопротивление. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

Если цепь ** не** закрыта, отремонтируйте или замените электропроводку двигателя.

См. руководство по устранению неполадок и ремонту для получения дополнительной информации.

![[nobox.png]]

Удалите пробный щуп из шины данных SAE J1587 CAN с отрицательным (-) штифтом и вставьте пробный щуп в отрицательный (-) штифт батареи 6-пинного разъема DeutschTM. Удалите измерительный щуп из шины данных SAE J1587 CAN отрицательного (-) штифта разъема двигателя и отсоедините испытательный щуп от многометрового щупа. Прикоснитесь к многометровому щупу, чтобы заземлить двигатель. Измерьте сопротивление. Мультиметр должен показывать замкнутую цепь (10 Ом или меньше).

Если цепь не закрыта, отремонтируйте или замените электропроводку двигателя.

См. руководство по устранению неполадок и ремонту для получения дополнительной информации.

![[nobox.png]]

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

> [!warning] ОСТОРОЖНО
> Используйте измерительный щуп, номер детали 3824811, для 6-контактного разъема DeutschTM.

Отсоедините аккумуляторные батареи.

Измерьте сопротивление от положительного (+) к положительному (+) аккумулятору 6-контактного разъема DeutschTM. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

Если цепь ** не** закрыта, отремонтируйте или замените электропроводку двигателя.

См. руководство по устранению неполадок и ремонту для получения дополнительной информации.

Если значения верны, схема ** должна быть проверена на короткое замыкание на землю и короткое замыкание от контакта к контакту.

![[19c01191.png]]

### Проверка на замыкание на массу

> [!warning] ОСТОРОЖНО
> Для шины данных CAN двигателя J1939 используйте испытательный щуп, номер детали 3822758, на разъеме ECM, чтобы избежать повреждения контактов разъема.

> [!warning] ОСТОРОЖНО
> Для шины данных CAN двигателя J1587/J1708 используйте испытательный щуп, номер детали 3822758, на разъеме ECM, чтобы избежать повреждения контактов разъема.

Определить тип шины данных CAN двигателя, доступной на двигателе, J1939 или J1587/J1708. Следуйте инструкциям, предусмотренным для короткого замыкания, чтобы проверить тип шины данных CAN двигателя.

J1939 Двигатель МОЖЕТ ставить шину данных

Отсоедините разъем жгута проводов двигателя от ECM. Вставьте измерительный щуп в шину данных SAE J1939 CAN положительного (+) штифта проводов двигателя упряжки разъема ECM и соедините испытательный щуп с многометровым щупом. Прикоснитесь к другому многометровому щупу, чтобы блокировать двигатель.

Измерьте сопротивление. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема ** не** открыта, отремонтируйте или замените электропроводку двигателя.

См. руководство по устранению неполадок и ремонту для получения дополнительной информации.

![[19c01270.png]]

Удалите пробный щуп из шины данных SAE J1939 CAN положительного (+) штифта и вставьте пробный щуп в шину данных SAE J1939 CAN отрицательного (-) штифта разъема ECM. Измерить сопротивление от SAE J1939 CAN данных шины отрицательного (-) штифта проводов двигателя упряжка разъема ECM к заземлению блока двигателя. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема ** не** открыта, отремонтируйте или замените электропроводку двигателя.

См. руководство по устранению неполадок и ремонту для получения дополнительной информации.

Если на любом из предыдущих этапов измеряется менее 100k Ом, то есть короткий путь к заземлению. Ремонт или замена ремня электропроводки двигателя.

См. руководство по устранению неполадок и ремонту для получения дополнительной информации.

![[19c01270.png]]

J1587/J1708 Двигатель CAN шина данных

Отсоедините разъем жгута проводов двигателя от ECM.

Вставьте измерительный щуп в шину данных SAE J1587 CAN положительного (+) штифта проводов двигателя упряжки ECM разъема и соедините испытательный щуп с многометровым щупом. Прикоснитесь к другому многометровому щупу к заземлению блока двигателя. Измерьте сопротивление. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема ** не** открыта, отремонтируйте или замените электропроводку двигателя.

См. руководство по устранению неполадок и ремонту для получения дополнительной информации.

![[19202568.png]]

Удалите пробный щуп из шины данных SAE J1587 CAN положительный (+) штифт и вставьте пробный щуп в шину данных SAE J1587 CAN отрицательный (-) штифт разъема ECM проводов двигателя. Прикоснитесь к другому многометровому щупу к заземлению блока двигателя. Измерить сопротивление от SAE J1587 CAN данных шины отрицательного (-) штифта проводов двигателя упряжка разъема ECM к заземлению блока двигателя. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема ** не** открыта, отремонтируйте или замените электропроводку двигателя.

См. руководство по устранению неполадок и ремонту для получения дополнительной информации.

![[nobox.png]]

### Проверьте короткое замыкание от контакта к контакту

> [!warning] ОСТОРОЖНО
> Для шины данных CAN двигателя J1939 используйте испытательный щуп, номер детали 3822758, на разъеме ECM, чтобы избежать повреждения контактов разъема.

> [!warning] ОСТОРОЖНО
> Для шины данных CAN двигателя J1587/J1708 используйте испытательный щуп, номер детали 3822758, на разъеме ECM, чтобы избежать повреждения контактов разъема.

J1939 Двигатель МОЖЕТ ставить шину данных

Отсоедините разъем жгута проводов двигателя от ECM.

Вставьте измерительный щуп в шину данных SAE J1939 CAN положительного (+) штифта проводов двигателя упряжки разъема ECM и соедините испытательный щуп с многометровым щупом. Вставьте другой испытательный щуп в другой штифт в разъеме проводов двигателя разъема ECM и соедините испытательный щуп с другим многометровым щупом.

Измерьте сопротивление от шин данных SAE J1939 CAN положительного (+) штифта к первому штифту в разъеме. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема ** не** открыта, отремонтируйте или замените электропроводку двигателя.

См. руководство по устранению неполадок и ремонту для получения дополнительной информации.

![[19c01272.png]]

Удалите свинец из первого штифта в разъеме и измерьте сопротивление от шины данных SAE J1939 CAN положительного (+) штифта проводов двигателя упряжки ECM разъема ко всем другим штифтам в разъеме, по одному за раз. Мультиметр ** должен** показывать открытую схему (100к Ом или более) на всех штифтах.

Если схема ** не** открыта, отремонтируйте или замените электропроводку двигателя.

См. руководство по устранению неполадок и ремонту для получения дополнительной информации.

![[nobox.png]]

Удалите пробный щуп из шины данных J1939 CAN положительного (+) штифта и вставьте пробный щуп в шину данных J1939 CAN (щитовой) штифт разъема ECM проводов двигателя. Вставьте другой испытательный щуп в другой штифт в разъеме. Измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема ** не** открыта, отремонтируйте или замените электропроводку двигателя.

См. руководство по устранению неполадок и ремонту для получения дополнительной информации.

Измерьте сопротивление от штифта шины данных SAE J1939 CAN (щитовой) к всем другим штифтам в разъеме, по одному за раз. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема ** не** открыта, отремонтируйте или замените электропроводку двигателя.

См. руководство по устранению неполадок и ремонту для получения дополнительной информации.

![[nobox.png]]

Удалите пробный щуп из шины данных SAE J1939 CAN (щитовой) штифт и вставьте пробный щуп в шину данных SAE J1939 CAN отрицательный (-) штифт разъема ECM проводов двигателя. Вставьте другой испытательный щуп в другой штифт в разъеме. Измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема ** не** открыта, отремонтируйте или замените электропроводку двигателя.

См. руководство по устранению неполадок и ремонту для получения дополнительной информации.

Измерить сопротивление от SAE J1939 CAN шины данных отрицательный (-) штифт разъема жгута двигателя ко всем другим штифтам в разъеме, по одному за раз. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема ** не** открыта, отремонтируйте или замените электропроводку двигателя.

См. руководство по устранению неполадок и ремонту для получения дополнительной информации.

![[nobox.png]]

J1587/J1708 Двигатель CAN шина данных

Отсоедините разъем жгута проводов двигателя от ECM.

Вставьте измерительный щуп в шину данных SAE J1587 CAN положительного (+) штифта проводов двигателя упряжки ECM разъема и соедините испытательный щуп с многометровым щупом. Вставьте другой измерительный щуп в другой многометровый щуп. Измерьте сопротивление. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема ** не** открыта, отремонтируйте или замените электропроводку двигателя.

См. руководство по устранению неполадок и ремонту для получения дополнительной информации.

![[nobox.png]]

Удалите свинец из первого штифта в разъеме и протестируйте все другие штифты в разъеме. Измерьте сопротивление от шины данных SAE J1587 CAN положительного (+) штифта проводов двигателя, жгута ECM разъёма ко всем другим штифтам в разъеме, по одному за раз. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Удалите пробный щуп из шины данных SAE J1587 CAN положительного (+) штифта проводов двигателя упряжки разъема ECM и вставьте пробный щуп в шину данных SAE J1587 CAN отрицательного (-) штифта.

Измерить сопротивление от шины данных SAE J1587 CAN отрицательного (-) штифта ко всем другим штифтам в разъеме. Мультиметр ** должен** показывать открытую схему (100к Ом или более) на всех штифтах.

Если схема ** не** открыта, отремонтируйте или замените электропроводку двигателя.

См. руководство по устранению неполадок и ремонту для получения дополнительной информации.

![[19c01272.png]]


> [!quote]- Original (English) · английский оригинал
> ### Select Service Tools
>
> #### Recommended Cummins® Service Tools
>
> - Digital multimeter, Part Number 3164489
>
> #### Additional Service Items
>
> - Appropriate test lead(s)
>
> ### General Information
>
> **CAUTION · Осторожно**
> Proper leads and/or a Cummins® approved circuit testing tool must be used when working with electrical connectors to prevent pin expansion and damage to the connector.
>
> The engine data link consists of circuitry located in the engine wiring harness which transmits digital information between the engine control module (ECM) and other devices on the engine and chassis. On older engines, the engine data link circuitry supports J1587/J1708 protocol. On newer engines, the engine data link circuitry supports J1939 protocol.
>
> The engine data link provides an access point for a service tool, such as a recommended Cummins® electronic service tool or equivalent, to communicate with the ECM. A service tool can communicate with the ECM on the engine data link free from data link traffic from other electronic devices that can be present on the OEM data link.
>
> The data link network on model year 2016 and newer engines can operate at either 250K baud or 500K baud rates. Baud rate refers to the speed at which information is broadcasted on a data link network. Only one baud rate can be set for any data link network. The default baud rate for model year 2016 and newer engines is 500K baud. The default baud rate for model year 2015 and older engines is 250K baud.
>
> Applications equipped with data link networks capable of supporting 500K baud data link speeds are differentiated by the key pattern on the 9 pin data link connector. This connector is also a different color from the 9 pin connectors that support only 250K baud data link speeds. An adapter tool, Part Number 5299126, is available in order to connect to applications equipped with 500K baud data link networks through the 9 pin connector.
>
> SAE J1939 Backbone Harness Overview:
>
> SAE J1939 has strict guidelines that **must** be followed for successful communication. Understanding some fundamentals about SAE J1939 will help verify these guidelines are followed.
>
> The main component of an SAE J1939 system is a backbone harness. The harness can be up to 40 m \[ 131 feet \] long. The backbone harness is terminated at each end with 120 ohm resistors.
>
> A maximum of 30 different devices can be attached to the SAE J1939 backbone at once. Each device, such as the data link adapter, is connected to the backbone through a stub which can be up to 1 m \[ 3.2 feet \] in length. The stub connector is a 3-pin plug.
>
> The terminating resistor caps (1) **must** be in place on the OEM backbone harness plugs (2) to maintain proper communication. Each resistor is 120 ohms and is located in a removable cap. This resistance is required when communicating with a recommended Cummins® electronic service tool or equivalent over the J1939 data link.
>
> Some engine harnesses include a complete SAE J1939 backbone harness. If this backbone harness is supplied, connection to a recommended Cummins® electronic service tool or equivalent is accomplished either by a 9-pin data link connector (1), Part Number 4918416, or a 3-pin receptacle (2), Part Number 3165141.
>
> To check for the J1939 backbone, turn the keyswitch to the OFF position. Measure the resistance from the SAE J1939 data link positive (+) pin to the SAE J1939 data link negative (-) pin of the 3-pin Deutsch™ connector.
>
> The multimeter will show 60 ohms when the engine harness has provided a backbone on the data link bus.
>
> If the engine harness does **not** supply the J1939 backbone harness and the data link connector is a 3-pin receptacle, a mini-backbone harness will have to be added.
>
> Engine Data Link Connectors
>
> The engine data link connector available on the engine harness will depend upon the data link circuitry in the engine harness and the vintage of the engine. Engine data link connectors available on Cummins® engines are summarized in the table below.
>
> | Connector Type | Data Link Protocols Supported |
> |---|---|
> | 2 pin Weather Pack™ | J1587/J1708 |
> | 3 pin Deutsch™ | J1939 |
> | 6 pin Deutsch™ | J1587/J1708 |
> | 9 pin Deutsch™ | J1587/J1708, J1939 |
>
> Each connector type is described in more detail in the following information.
>
> The 9 pin Deutsch™ connector can supply SAE J1587/SAE 1708 and SAE J1939 communications at 250k baud data link speed, and battery voltage. The following are pin-outs for the 9 pin connector:
>
> | Type I (250k) |  |
> |---|---|
> | Pin | Signal |
> | A | Ground |
> | B | Unswitched Battery |
> | C | J1939 data link (+) |
> | D | J1939 data link (-) |
> | E | J1939 data link (shield) (**not** applicable for Marine) |
> | F | J1708 data link (+) |
> | G | J1708 data link (-) |
> | H | Open |
> | J | Open |
>
> A similar 9 pin Deutsch™ connector can also supply SAE J1939 communications at 500K baud data link speed, and battery voltage. The following are pin-outs for the 9 pin connector:
>
> | Type II Green (500K) |  |
> |---|---|
> | Pin | Signal |
> | A | Ground |
> | B | Unswitched Battery |
> | C | J1939 data link (+) |
> | D | J1939 data link (-) |
> | E | J1939 data link (shield) (**not** applicable for Marine) |
> | F | J1708 data link (+) |
> | G | J1708 data link (-) |
> | H | Open |
> | J | Open |
>
> The 6 pin Deutsch™ connector, Part Number 3824805, is found on some engines. This connector supplies SAE J1587/J1708, as well as the battery voltage. The following are pin-outs for the 6 pin connector:
>
> | Pin | Signal |
> |---|---|
> | A | J1708 data link (+) |
> | B | J1708 data link (-) |
> | C | Unswitched battery (+) |
> | D | Open |
> | E | Ground |
> | F | Open |
>
> **Note · Примечание**
> For CELECT Plus™ engines, do **not** use the in-cab 6-pin data link connector to calibrate the ECM. Use the data link connector found on the engine.
>
> The 3 pin SAE J1939 Deutsch™ connectors are also found on some Cummins® engine harnesses. Two possible types of 3 pin connectors can be present: A 3 pin plug (1), Part Number 3824288; and a 3 pin receptacle (2), Part Number 3824290. The following are the pin-outs for the 3 pin connector:
>
> | Pin | Signal |
> |---|---|
> | A | J1939 data link (+) |
> | B | J1939 data link (-) |
> | C | J1939 data link (shield) |
>
> The 3-pin connector **only** supports the SAE J1939 data link.
>
> To meet the SAE J1939 standard, the 3 pin receptacle connector **must** be within 0.66 m \[ 2.16 feet \] of the ECM. Use of the J1939 mini-backbone harness, Part Number 3163096, may be required for proper termination resistance. The mini-backbone harness is required when **no** backbone is provided on the data link. Gender changer cable, Part Number 3163597, may be required to connect the mini-backbone harness to the engine harness or service tool cable.
>
> **Note · Примечание**
> If there is 60 ohm resistance measured between pins A and B of the 3 pin connector, a backbone is on the data link.
>
> The 2 pin connector is on many older engines, and **only** supplies SAE J1587/J1708 support (no battery voltage supply). The following are the pin-outs for the 2 pin connector:
>
> | Pin | Signal |
> |---|---|
> | A | J1587/J1708 data link (+) |
> | B | J1587/1708 data link (-) |
>
> Some engines have a 2 pin service tool power supply Weather Pack™ receptacle located in the engine harness. The connector can be used to power up any service tool device.
>
> | Pin | Signal |
> |---|---|
> | A | Unswitched battery (+) |
> | B | Ground (-) |
>
> ### Resistance Check
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> **CAUTION · Осторожно**
> For the J1939 engine data link, use test lead, Part Number 3822758, on the ECM connector to avoid damage to the connector pins. Use test lead, Part Number 3824811, for the 9 pin Deutsch™ connector. Use test lead, Part Number 3823993 for the 3 pin Deutsch™ connector pin receptacle or test lead, Part Number 3823994 for the 3 pin Deutsch™ connector.
>
> **CAUTION · Осторожно**
> For the J1587/J1708 engine data link, use test lead, Part Number 3622758, on the ECM connector to reduce the possibility of damage to the connector pins. Use test lead 3824800 for the 6 pin Deutsch™ connector. Use test lead 3823995 for the 2 pin Packard™ connector.
>
> Determine the type of engine data link available on the engine, either J1939 or J1587/J1708. Follow the instructions provided to measure the resistance for the type of engine data link identified.
>
> J1939 Engine Data Link
>
> - Disconnect the batteries.
> - Disconnect the engine harness connector from the ECM. Turn the keyswitch to the OFF position.
>
> Insert a test lead into the SAE J1939 data link positive (+) pin of the engine harness ECM connector, and connect the test lead to the multimeter probe. Insert the other test lead into the SAE J1939 data link positive (+) pin of the 3 pin or 9 pin Deutsch™ connector, and connect the test lead to the multimeter.
>
> Measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less).
>
> If the circuit is **not** closed, repair or replace the engine harness.
>
> See the Troubleshooting and Repair manual for additional information.
>
> Insert the multimeter lead into the SAE J1939 data link negative (-) of the engine harness ECM connector. Touch the other lead to the SAE J1939 data link negative (-) pin of the 3 pin or 9 pin Deutsch™ connector. Measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less).
>
> If the circuit is **not** closed, repair or replace the engine harness.
>
> See the Troubleshooting and Repair manual for additional information.
>
> If the values are correct, the circuit **must** still be checked for a short circuit to ground and a short circuit from pin-to-pin.
>
> Remove the test lead from the SAE J1939 data link negative (-) pin of the engine harness ECM connector and insert the test lead into the SAE J1939 data link (shield) pin. Touch the negative multimeter lead to the SAE J1939 data link (shield) pin of the 3 pin or 9 pin Deutsch™ connector. Measure the resistance.
>
> The multimeter **must** show a closed circuit (10 ohms or less). If more than 10 ohms are measured in any of these steps, there could be an open circuit in the SAE J1939 data link (shield) pin, the SAE J1939 data link negative (-) pin, or the SAE J1939 data link positive (+) pin, or the polarity is **not** correct.
>
> J1587/J1708 Engine Data Link
>
> Turn the keyswitch to the OFF position. Disconnect the engine harness from the ECM.
>
> Insert a test lead into the SAE J1587 data link positive (+) pin of the engine harness ECM connector and connect the test lead to a multimeter probe. Insert the other test lead into the SAE J1587 data link positive (+) pin of the 2 pin or 6 pin connector and connect the test lead to the other multimeter probe. Measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less).
>
> If the circuit is **not** closed, repair or replace the engine harness.
>
> See the Troubleshooting and Repair manual for additional information.
>
> Remove the test lead from the SAE J1587 data link positive (+) pin and insert the test lead into the SAE J1587 data link negative (-) pin of the ECM connector. Remove the other test lead from the SAE J1587 data link positive (+) pin and insert the test lead into the SAE J1587 data link negative (-) pin of the 2 pin or 6 pin connector. Measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less).
>
> If the circuit is **not** closed, repair or replace the engine harness.
>
> See the Troubleshooting and Repair manual for additional information.
>
> Remove the test lead from the SAE J1587 data link negative (-) pin and insert the test lead into the battery negative (-) pin of the 6 pin Deutsch™ connector. Remove the test lead from the SAE J1587 data link negative (-) pin of the engine connector and disconnect the test lead from the multimeter probe. Touch the multimeter probe to the engine block ground. Measure the resistance. The multimeter should show a closed circuit (10 ohms or less).
>
> If the circuit is not closed, repair or replace the engine harness.
>
> See the Troubleshooting and Repair manual for additional information.
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> **CAUTION · Осторожно**
> Use test lead, Part Number 3824811, for the 6 pin Deutsch™ connector.
>
> Disconnect the batteries.
>
> Measure the resistance from the positive (+) battery terminal to battery positive (+) of the 6-pin Deutsch™ connector. The multimeter **must** show a closed circuit (10 ohms or less).
>
> If the circuit is **not** closed, repair or replace the engine harness.
>
> See the Troubleshooting and Repair manual for additional information.
>
> If the values are correct, the circuit **must** still be checked for a short circuit to ground and a short circuit from pin-to-pin.
>
> ### Check for Short Circuit to Ground
>
> **CAUTION · Осторожно**
> For the J1939 engine data link, use test lead, Part Number 3822758, on the ECM connector to avoid damage to the connector pins.
>
> **CAUTION · Осторожно**
> For the J1587/J1708 engine data link, use test lead, Part Number 3822758, on the ECM connector to avoid damage to the connector pins.
>
> Determine the type of engine data link available on the engine, either J1939 or J1587/J1708. Follow the instructions provided for short circuit to ground check for the type of engine data link identified.
>
> J1939 Engine Data Link
>
> Disconnect the engine harness connector from the ECM. Insert a test lead into SAE J1939 data link positive (+) pin of the engine harness ECM connector and connect the test lead to a multimeter probe. Touch the other multimeter probe to engine block ground.
>
> Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the engine harness.
>
> See the Troubleshooting and Repair manual for additional information.
>
> Remove the test lead from the SAE J1939 data link positive (+) pin and insert the test lead into the SAE J1939 data link negative (-) pin of the ECM connector. Measure the resistance from the SAE J1939 data link negative (-) pin of the engine harness ECM connector to the engine block ground. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the engine harness.
>
> See the Troubleshooting and Repair manual for additional information.
>
> If less than 100k ohms is measured in any of the previous steps, there is a short to circuit to ground. Repair or replace the engine harness.
>
> See the Troubleshooting and Repair manual for additional information.
>
> J1587/J1708 Engine Data Link
>
> Disconnect the engine harness connector from the ECM.
>
> Insert a test lead into the SAE J1587 data link positive (+) pin of the engine harness ECM connector and connect the test lead to a multimeter probe. Touch the other multimeter probe to the engine block ground. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the engine harness.
>
> See the Troubleshooting and Repair manual for additional information.
>
> Remove the test lead from the SAE J1587 data link positive (+) pin and insert the test lead into the SAE J1587 data link negative (-) pin of the engine harness ECM connector. Touch the other multimeter probe to the engine block ground. Measure the resistance from the SAE J1587 data link negative (-) pin of the engine harness ECM connector to the engine block ground. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the engine harness.
>
> See the Troubleshooting and Repair manual for additional information.
>
> ### Check for Short Circuit from Pin-to-Pin
>
> **CAUTION · Осторожно**
> For the J1939 engine data link, use test lead, Part Number 3822758, on the ECM connector to avoid damage to the connector pins.
>
> **CAUTION · Осторожно**
> For the J1587/J1708 engine data link, use test lead, Part Number 3822758, on the ECM connector to avoid damage to the connector pins.
>
> J1939 Engine Data Link
>
> Disconnect the engine harness connector from the ECM.
>
> Insert a test lead into the SAE J1939 data link positive (+) pin of the engine harness ECM connector and connect the test lead to the multimeter probe. Insert the other test lead into another pin in the connector of the engine harness ECM connector and connect the test lead to the other multimeter probe.
>
> Measure the resistance from the SAE J1939 data link positive (+) pin to the first pin in the connector. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the engine harness.
>
> See the Troubleshooting and Repair manual for additional information.
>
> Remove the lead from the first pin in the connector and measure the resistance from the SAE J1939 data link positive (+) pin of the engine harness ECM connector to all other pins in the connector, one at a time. The multimeter **must** show an open circuit (100k ohms or more) at all pins.
>
> If the circuit is **not** open, repair or replace the engine harness.
>
> See the Troubleshooting and Repair manual for additional information.
>
> Remove the test lead from the J1939 data link positive (+) pin and insert the test lead into the J1939 data link (shield) pin of the engine harness ECM connector. Insert the other test lead into another pin in the connector. Measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the engine harness.
>
> See the Troubleshooting and Repair manual for additional information.
>
> Measure the resistance from the SAE J1939 data link (shield) pin to all other pins in the connector, one at a time. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the engine harness.
>
> See the Troubleshooting and Repair manual for additional information.
>
> Remove the test lead from the SAE J1939 data link (shield) pin and insert the test lead into the SAE J1939 data link negative (-) pin of the engine harness ECM connector. Insert the other test lead into another pin in the connector. Measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the engine harness.
>
> See the Troubleshooting and Repair manual for additional information.
>
> Measure the resistance from the SAE J1939 data link negative (-) pin of the engine harness connector to all other pins in the connector, one at a time. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the engine harness.
>
> See the Troubleshooting and Repair manual for additional information.
>
> J1587/J1708 Engine Data Link
>
> Disconnect the engine harness connector from the ECM.
>
> Insert a test lead into the SAE J1587 data link positive (+) pin of the engine harness ECM connector and connect the test lead to the multimeter probe. Insert the other test lead into another multimeter probe. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the engine harness.
>
> See the Troubleshooting and Repair manual for additional information.
>
> Remove the lead from the first pin in the connector and test all other pins in the connector. Measure the resistance from the SAE J1587 data link positive (+) pin of the engine harness ECM connector to all other pins in the connector, one at a time. The multimeter **must** show an open circuit (100k ohms or more).
>
> Remove the test lead from the SAE J1587 data link positive (+) pin of the engine harness ECM connector and insert the test lead into the SAE J1587 data link negative (-) pin.
>
> Measure the resistance from the SAE J1587 data link negative (-) pin to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more) at all pins.
>
> If the circuit is **not** open, repair or replace the engine harness.
>
> See the Troubleshooting and Repair manual for additional information.
