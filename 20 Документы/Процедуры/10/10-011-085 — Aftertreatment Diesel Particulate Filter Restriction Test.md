---
type: "Процедура"
doc: "10-011-085"
title_en: "Aftertreatment Diesel Particulate Filter Restriction Test"
modified: "2016-09-21"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
manuals:
  - "3666239"
figures: 22
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-011-085.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-011-085.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSX15"
  - "группа/10"
  - "перевод/машинный"
---

# Aftertreatment Diesel Particulate Filter Restriction Test

> [!abstract] Процедура · `10-011-085`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Входит в руководства:** [[3666239 — Signature™, ISX, and QSX15 Service Manual|3666239]]
> **Секции:** Section 11 - Exhaust System · Section 11 - Exhaust System - Group 11
> **Даты:** изменён 2016-09-21
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-011-085.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-011-085.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Приложения

![[00c00069.png]]

Эта процедура применяется к двигателям ISX15 CM871 с 2-й, 3-й и 4-й фазами дизельных фильтров твердых частиц (DPF):

| DPF Part Number (Часовой номер) |  |  |  |
|---|---|---|---|
| Фаза 1 | Фаза 2 | Фаза 3 | Фаза 4 |
| 4969702 | 5283669 | 5297522 | 4388409 |
| 4969701 | 5283778 | 5297990 | 4388410 |
| 4969701 | 5283799 | 5297989 | 4388411 |

Введение

Испытание на ограничитель дизельного фильтра для твердых частиц после обработки может быть использовано для оценки ограничения фильтра для твердых частиц дизельного топлива (DPF) после обработки, без использования специализированного оборудования. Испытание может использоваться во время устранения неполадок для кодов неисправностей, связанных с системой последующей обработки, для определения того, был ли достигнут интервал обслуживания после обработки (очистка или обмен) или если датчик дифференциального давления DPF после обработки неисправен.

Тест на ограничение фильтра дизельных частиц после обработки поможет в оценке DPF после обработки для определения следующего:

- Необходимо очистить или обменять, чтобы удалить сажу, пепел или посторонние вещества
- Соответствует критериям повторного использования для ограничения после мероприятия по очистке.

Накопление сажи в послеочистном DPF является нормальной функцией работы двигателя. Однако накопление избыточной сажи может вызвать частые регенерации после обработки и обычно вызвано проблемами топливной системы или системы обработки воздуха.

Накопление пепла является результатом сбора негорючих продуктов в послеоперационном DPF. Чрезмерное накопление золы в послеоперационном DPF может быть вызвано потреблением моторного масла, потреблением охлаждающей жидкости, загрязненным топливом и другими проблемами.

Инородный материал в послеочистном DPF является **не** нормальным и может быть вызван такими проблемами, как ухудшение компонентов выхлопной системы, утечки выхлопных газов или повреждение двигателя или других компонентов.

> [!note] Примечание
> Проверьте активные коды неисправностей перед выполнением теста на ограничение фильтра дизельных частиц после обработки. Если присутствуют активные коды неисправностей, перед завершением этого теста обратитесь к соответствующему дереву устранения неисправностей кода неисправностей, если только вы не направлены на выполнение этого теста в дереве устранения неисправностей.

> [!note] Примечание
> Испытание на ограничитель дизельного фильтра для твердых частиц после обработки должно проводиться сразу после успешного завершения регенерации фильтра дизельных частиц после обработки, за исключением случаев, отмеченных в этой процедуре. Регенерация дизельного фильтра твердых частиц после обработки выполняется с использованием электронного инструментария INSITETM.

Выполнение регенерации фильтра для дизельных твердых частиц после обработки гарантирует, что любой остаток выхлопных газов или сажа удаляются из DPF после обработки, что приводит к измерению ограничения, которое относится к содержанию золы, за исключением случаев, когда посторонний материал вошел в DPF после обработки. Выполнение послеочистки дизельного фильтра твердых частиц стационарной регенерации также гарантирует, что температура после обработки DPF повышена до уровня, который обеспечивает максимальный расход выхлопных газов во время испытания на ограничение и что любая влага также была удалена.

![[11c00245.png]]

### Подготовительные операции

Проверка выпускных выпусков

Проверить выпуск выхлопной системы.

Проверка выпускной отверстия выхлопной системы может помочь в определении состояния после обработки DPF. Выход выхлопной системы должен выглядеть чистым с небольшим или нулевым остатком выхлопных газов или накоплением сажи.

> [!note] Примечание
> Некоторое накопление остатков выхлопных газов или сажи является нормальным и не указывает на проблему с послеобработкой DPF.

Тяжелое накопление остатков выхлопных газов или сажи на выпускной розетке выхлопной системы является результатом проблемы с послеочисткой DPF. Выполните тест ускорения Snap - после лечения подключено.

![[14d00033.png]]

Ускорение Snap - после лечения подключено

Откройте инструмент для электронного обслуживания INSITETM, но не подключайтесь к модулю управления двигателем (ECM).

Перейдите к Инструменты \> Варианты \> Единицы измерения.

В выпадающем меню в меню Единицы измерения выберите Метрику. Выберите кнопку Apply, а затем выберите кнопку OK.

Закройте меню опций электронного сервиса INSITETM.

![[ck800wa.png]]

Подключите инструмент электронного сервиса INSITETM к шине данных сервиса CAN.[[105-019-428 — Engine Datalinks|См. процедуру 019-428 в разделе 19.]]

Захват рабочего заказа (изображение работы) с помощью инструментария электронного обслуживания INSITETM.

![[19803969.png]]

Используйте инструмент электронного обслуживания INSITETM для настройки диагностического теста ECM для динамометра.

> [!note] Примечание
> Необходимо активировать этот тест, чтобы позволить скорости двигателя достичь требуемого уровня без необходимости изменения параметров и параметров клиента (т.е. Максимальная скорость автомобиля без VSS, управление скоростью на основе нагрузки и т. Д.

> [!note] Примечание
> Настройку для диагностического теста ECM динамометра можно найти в разделе диагностических измерительн ECM в инструменте электронного обслуживания INSITETM.

![[19803969.png]]

- Трансмиссия транспортного средства должна быть в Нейтрале.
- При этом необходимо использовать стояночный тормоз.
- Автомобильный капот должен быть закрыт.
- Ручной вентиляторный переключатель, если он оборудован, и система кондиционирования воздуха транспортного средства должны быть отключены, чтобы предотвратить работу вентилятора охлаждения двигателя во время этого испытания.
- Двигатель **должен** иметь нормальную рабочую температуру (выше 82°C \[180°F\] температуры охлаждающей жидкости).

Запускай двигатель.

Позволяет двигателю стабилизироваться при низком холостом режиме в течение 30 секунд.

Удерживайте педаль акселератора, чтобы убедиться, что двигатель может достичь высокого холостого хода (обычно 1800-2000 об/мин).

Отпустите педаль акселератора и позвольте двигателю стабилизироваться при низком холостом режиме в течение 30 секунд.

Быстро нажимайте педаль акселератора с 0 до 100 процентов и удерживайте двигатель на высоком холостом ходу (обычно 1800 - 2000 об/мин) в течение 5 секунд.

Отпустите педаль акселератора и позвольте двигателю стабилизироваться при низком холостом режиме в течение 30 секунд.

Повторите тест на ускорение Snap - После обработки подключается по мере необходимости, чтобы позволить визуальную проверку дыма на выходе выхлопной системы, поскольку двигатель ускоряется от низкого до высокого холостого хода.

> [!note] Примечание
> Визуальная проверка может быть выполнена с помощью другого техника, в зависимости от конфигурации выхлопных газов автомобиля.

![[14c00079.png]]

Во время испытания на ускорение Snap - После обработки подключите, проверьте наличие черного дыма, выходящего из выпускной системы, так как двигатель ускоряется от низкого холостого хода до высокого холостого хода.

> [!note] Примечание
> В некоторых случаях тест на ускорение Snap может **не** обеспечить условия, необходимые для выявления неисправности после обработки DPF. Если на выпускном отверстии выхлопных газов происходит сильное накопление остатка/сажи выхлопных газов, и ускорение с помощью защелки **не** показывает состояние, изложенное в следующих шагах, может потребоваться выполнить короткий разгон при частичной до полной нагрузке или выполнить испытание на остановку. См. процедуру 014-008 в разделе 14.

Если во время этих испытаний в выпускной трубе выхлопной системы обнаружен черный дым, обратитесь к рекомендациям по повторному использованию дизельного окислительного катализатора и дизельного фильтра для твердых частиц после обработки, бюллетеню 4021600, и проверьте последующую обработку DPF на предмет повреждения.

**не использовать после обработки дизельных твердых частиц фильтра Ограничение тест для оценки поврежденной после обработки DPF. Неверные результаты теста **будут.

![[11c00246.png]]

Если присутствует серый дым или слабый черный дым, обратитесь к Катализатору окисления дизельного топлива и Рекомендациям по повторному использованию фильтра дизельных частиц после обработки, Бюллетень 4021600, и проверьте последующую обработку DPF на предмет повреждения. Белый дым во время испытания на ускорение Snap - после обработки может указывать на неисправность. В это время не требуется никаких дополнительных устранений неполадок или ремонта.

![[11c00247.png]]

Если черный или серый дым **не **найден на выходе выхлопной системы, перейдите к тесту напряжения сигнала датчика в этом разделе.

![[11o00085.png]]

Датчик сигнала тест на напряжение

В инструменте электронного обслуживания INSITETM добавьте следующие параметры на экран монитора данных / сканера:

1. Скорость двигателя (rpm)
2. Скорость потока выхлопных газов (м 3/с)
3. После обработки DPF дифференциальное давление (кПа)
4. После обработки DPF дифференциального давления датчик сигнала напряжения (VDC).

![[19803969.png]]

Убедитесь, что параметр после обработки DPF дифференциального давления датчика сигнала напряжения считывает 0,69 VDC (± 0,22 VDC при 25°C \[77°F\] и ниже или ± 0,14 VDC при 26°C \[78°F\] или выше) при включении переключателя зажигания, выключении двигателя.

> [!note] Примечание
> Если напряжение сигнала датчика дифференциального давления DPF после обработки считывается **не** в пределах спецификации, проверьте датчик дифференциального давления DPF после обработки и связанную с ним проводку. Используйте следующую процедуру в электронных системах управления CM871 и CM876, двигателях ISX и ISM, бюллетене 4021560. См. процедуру 019-443 в разделе 19.

![[19803969.png]]

Отсоедините разъем DPF-датчика дифференциального давления после обработки.

Используйте инструмент для проверки работоспособности кодов 1881 и 3134.

> [!note] Примечание
> Если код ошибки 1881 не активировался, проверьте датчик дифференциального давления DPF после обработки и связанную с ним проводку. Используйте следующую процедуру в электронных системах управления CM871 и CM876, двигателях ISX и ISM, бюллетене 4021560. См. процедуру 019-443 в разделе 19.

![[19c01637.png]]

Используйте штыревой испытательный щуп FramatomeTM, номер детали 3164596 или эквивалент, чтобы сократить датчик дифференциального давления DPF после обработки 5 VDC SUPPLY (контакт 4 разъёма жгута проводов) до датчика дифференциального давления DPF после обработки SIGNAL (контакт 2 разъёма жгута проводов).

Используйте инструмент электронного сервиса INSITETM для проверки активности кода ошибки 1879.

> [!note] Примечание
> Если коды поломок 1879 года не активировались, сигнал датчика перепада давления DPF после обработки и сигнал датчика давления в розетке дизельного фильтра с твердыми частицами могут быть неправильно маршрутизированы. См. руководство по обслуживанию производителя оригинального оборудования (OEM).

> [!note] Примечание
> Если коды ошибок 1881 не активировались, проверьте датчик дифференциального давления DPF после обработки и связанную с ним проводку. Используйте следующую процедуру в электронных системах управления CM871 и CM876, двигателях ISX и ISM, бюллетене 4021560. См. процедуру 019-443 в разделе 19.

![[11y00001.png]]

Проверить, что проблемы с датчиком перепада давления DPF после обработки и связанной с ним проводкой были исправлены путем повторения предыдущих шагов, если это необходимо.

Подключите после обработки DPF датчик дифференциального давления проводкой жгута разъема.

![[ck800wa.png]]

Используйте инструмент электронного обслуживания INSITETM для очистки неактивных кодов неисправностей от испытания (испытаний) датчика (датчиков) дифференциального давления DPF после обработки.

![[19803969.png]]

### Проверка

Убедитесь, что выполнены следующие условия:

1. Автомобиль припаркован в соответствующем месте, на поверхности, которая будет **не** гореть или плавиться при высоких температурах (например, чистый бетон или гравий, **не** трава или асфальт) и вдали от всего, что может гореть, плавиться или взрываться.
2. Автомобиль надежно припаркован.
3. Установите безопасную зону выхлопа.
4. Проверьте поверхности выхлопной системы.
5. Готовьтесь к изменениям скорости двигателя во время регенерации.
6. Убедитесь, что автомобиль и окружающие его участки находятся под контролем во время регенерации. Если возникнут какие-либо небезопасные условия, будьте готовы немедленно выключить двигатель.

![[ck800wa.png]]

> [!danger] ОПАСНО
> Во время регенерации температура выхлопных газов может достигать 800 ° C \[1500 ° F \], а температура поверхности выхлопной системы может превышать 700° C \[1300° F \], которая достаточно горячая, чтобы воспламенить или расплавить обычные материалы и вызвать серьезные ожоговые травмы. Выхлопные и выхлопные компоненты могут оставаться горячими после того, как транспортное средство перестало двигаться. Чтобы избежать риска пожара, повреждения имущества, ожогов или других серьезных личных травм, убедитесь, что горючие материалы не находятся там, где они могут вступать в контакт с горячими выхлопными газами или выхлопными компонентами.

Выполняйте регенерацию DPF после обработки с использованием инструментария электронного обслуживания INSITETM.

> [!note] Примечание
> Необязательно допускать регенерацию ДПФ после лечения в течение этого раздела процедуры (рекомендуется минимум 30 минут).

> [!note] Примечание
> Регенерацию после лечения DPF можно найти в меню диагностики ECM в электронном сервисном инструменте INSITETM.

> [!note] Примечание
> Скорость двигателя будет увеличиваться, и турбокомпрессор может громко свистеть во время послеоперационного испытания на регенерацию DPF.

Чтобы остановить регенерацию DPF после обработки, включите сцепление, рабочий тормоз и педаль акселератора; или выключите двигатель.

После завершения регенерации температура выхлопных газов и поверхности выхлопных газов будет оставаться повышенной в течение 3-5 минут.

![[19803969.png]]

> [!danger] ОПАСНО
> Вентилятор охлаждения двигателя должен быть полностью включен и заблокирован в положении Включения перед проведением испытания на ограничение фильтра дизельных твердых частиц после обработки. Несоблюдение режима блокировки вентилятора охлаждения двигателя в положении Включения может привести к повреждению сцепления вентилятора, двигателя или других компонентов.

Закройте двигатель.

Установите вентилятор охлаждения двигателя в положение Включено, Заполнено или Закрыто.

> [!note] Примечание
> Не используйте инструмент электронного обслуживания INSITETM для изменения настроек функций и параметров для изменения работы вентилятора охлаждения двигателя. Большинство вентиляторов охлаждения двигателя предназначены для работы по умолчанию в положении ON, ENGAGED или LOCKED с потерей давления воздуха или электрического тока. Для того, чтобы изменить работу вентилятора охлаждения двигателя, может потребоваться отключить воздух или электропитание. Ссылка на информацию об услугах производителя оборудования.

Запускай двигатель.

Убедитесь, что вентилятор охлаждения двигателя будет поддерживать положение ON, ENGAGED или LOCKED. Ссылка на информацию об услугах производителя оборудования.

Закройте двигатель.

![[ck800wa.png]]

Используйте инструмент электронного обслуживания INSITETM для настройки диагностического теста ECM для динамометра.

> [!note] Примечание
> Необходимо активировать это испытание, чтобы позволить скорости двигателя достичь требуемого уровня без необходимости изменения параметров и параметров клиента (т.е. Максимальная скорость автомобиля без VSS, управление скоростью на основе нагрузки и т. Д.

> [!note] Примечание
> Настройку для диагностического теста ECM можно найти в разделе диагностического теста ECM в инструменте электронного обслуживания INSITETM.

![[19803969.png]]

> [!note] Примечание
> Эта процедура требует, чтобы двигатель работал на высоком холостом ходу в течение тридцати (30) секунд. Сделайте **не** попытку выполнить тест ускорения Snap - после лечения, подключенного в этом разделе процедуры. Произойдут неправильные результаты испытаний.

Выполните следующие шаги:

1. Запускай двигатель.
2. Позволяет двигателю стабилизироваться при низком холостом режиме в течение 30 секунд.
3. Усильте ускоритель с 0 до 100 процентов и удерживайте двигатель на высоком холостом ходу (обычно от 1800 до 2000 об/мин).
4. Используйте инструмент InsiteTM Data Monitor/Logger для регистрации этих параметров.
5. Наблюдайте за параметром объемного расхода выхлопных газов в электронном сервисе INSITETM Data Monitor/Logger.
6. Убедитесь, что объемный расход выхлопных газов достигает 0,3 м 3/с или выше.
7. Остановите электронный сервис INSITETM, используя Data Monitor/Logger через 30 секунд и сохраните полученный файл журнала, используя имя файла ESN\_After\_Cleaning\_Run\_1.log.csv, где ESN является серийным номером двигателя тестируемого транспортного средства. Сохраните файл журнала в подходящем месте, где его будет легко найти. Используйте ESN в качестве имени папки.
8. Отпустите педаль акселератора и позвольте двигателю стабилизироваться при низком холостом режиме в течение 30 секунд.
9. Повторите соответствующий шаг (2-8) еще четыре раза, сохранив файл журнала Data Monitor/Logger с использованием имен файлов ESN\_After\_Cleaning\_Run\_2.log.csv, ESN\_After\_Cleaning\_3.log.csv, ESN\_After\_Cleaning\_4.log.csv и ESN\_After\_Cleaning\__Run\_5.log.csv, где ESN - серийный номер двигателя испытываемого транспортного средства. Сохраните файлы журнала в подходящем месте, где их будет легко найти. Используйте ESN в качестве имени папки.

![[19803969.png]]

### Анализ данных

Найдите файл(ы) журнала, взятый с помощью электронного инструментария InsiteTM Data Monitor/Logger во время раздела «Тест» этой процедуры.

> [!note] Примечание
> Файлы журналов будут храниться в папке C:\\Intelect\\Insite\\Logs по умолчанию, где C: представляет собой букву диска жесткого диска, на котором установлена электронная инструментальная система обслуживания INSITETM.

| DPF Part Number (Часовой номер) |  |  |  |
|---|---|---|---|
| Фаза 1 | Фаза 2 | Фаза 3 | Фаза 4 |
| 4969702 | 5283669 | 5297522 | 4388409 |
| 4969701 | 5283778 | 5297990 | 4388410 |
| 4969701 | 5283799 | 5297989 | 4388411 |

Просмотрите файлы журналов из электронного инструментария обслуживания INSITETM, взятые во время раздела «Тест» этой процедуры.

Получить после обработки DPF дифференциальное давление (кПа) при 0,3 м3/с или больше объемного потока выхлопных газов после того, как двигатель достиг высокого холостого хода и стабилизирован.

Дифференциальное давление DPF после обработки должно быть ниже максимального - после спецификации регенерации для заданного объема потока выхлопных газов, как показано в таблице ниже:

| Дифференциальное давление DPF (фаза 2 или 3 DPF) |  |
|---|---|
| Скорость объемного потока выхлопных газов (м 3 /с) | Максимальный (кПа) |
| 0.30 | 1.75 |
| 0.35 | 2.15 |
| 0.40 | 2.55 |
| 0.45 | 3.00 |
| 0.50 | 3.40 |
| 0.55 | 3.80 |
| 0.60 | 4.20 |
| 0.65 | 4.60 |
| 0.70 | 5.00 |
| 0.75 | 5.45 |
| 0.80 | 5.85 |

Если после обработки DPF дифференциальное давление **не **ниже максимального - после спецификации регенерации выше, после обработки DPF должен быть заменен.[[101-011-041-tr — Aftertreatment Diesel Particulate Filter|См. процедуру 011-041 в разделе 11.]]

| Дифференциальное давление DPF (Фаза 4 DPF) |  |
|---|---|
| Скорость объемного потока выхлопных газов (м 3 /с) | Максимальный (кПа) |
| 0.30 | 2.25 |
| 0.35 | 2.65 |
| 0.40 | 3.05 |
| 0.45 | 3.50 |
| 0.50 | 3.90 |
| 0.55 | 4.30 |
| 0.60 | 4.70 |
| 0.65 | 5.10 |
| 0.70 | 5.50 |
| 0.75 | 5.95 |
| 0.80 | 6.30 |

Если после обработки DPF дифференциальное давление **не **ниже максимального - после спецификации регенерации выше, после обработки DPF должен быть заменен.[[101-011-041-tr — Aftertreatment Diesel Particulate Filter|См. процедуру 011-041 в разделе 11.]].

### Завершающие операции

Используйте инструмент электронного сервиса INSITETM для проверки любых активных кодов неисправностей. Если присутствуют какие-либо активные коды неисправностей, обратитесь к соответствующему дереву устранения неисправностей кода неисправностей в разделе TS.

Используйте инструмент электронного сервиса INSITETM для очистки всех кодов неактивных ошибок.

Используйте инструмент электронного обслуживания INSITETM для выполнения процедуры установки фильтра после обработки и восстановления всех элементов.

> [!note] Примечание
> Процедуру установки фильтра после обработки можно найти в инструменте электронного обслуживания INSITETM в разделе Advanced ECM Data в разделе «Поддержание после обработки».

![[19803969.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> Applications
>
> This procedure applies to ISX15 CM871 engines with Phase 2, 3, and 4 diesel particulate filters (DPF):
>
> | DPF Part Number |  |  |  |
> |---|---|---|---|
> | Phase 1 | Phase 2 | Phase 3 | Phase 4 |
> | 4969702 | 5283669 | 5297522 | 4388409 |
> | 4969701 | 5283778 | 5297990 | 4388410 |
> | 4969701 | 5283799 | 5297989 | 4388411 |
>
> Introduction
>
> The Aftertreatment Diesel Particulate Filter Restriction Test can be used to evaluate the aftertreatment diesel particulate filter (DPF) restriction, without requiring the use of specialized equipment. The test may be used during troubleshooting for aftertreatment system related fault codes, to determine if an aftertreatment maintenance (cleaning or exchange) interval has been reached or if the aftertreatment DPF differential pressure sensor is malfunctioning.
>
> The Aftertreatment Diesel Particulate Filter Restriction Test will aid in the evaluation of aftertreatment DPFs to determine the following:
>
> - Needs to be cleaned or exchanged to remove soot, ash, or foreign matter
> - Meets reuse criteria for restriction after a cleaning event.
>
> Soot accumulation in the aftertreatment DPF is a normal function of engine operation. However, the accumulation of excessive soot can cause frequent aftertreatment regenerations and is normally caused by fuel system or air handling system issues.
>
> Ash accumulation is the result of non-combustible products collecting in the aftertreatment DPF. Excessive ash accumulation in the aftertreatment DPF can be caused by lubricating oil consumption, coolant consumption, contaminated fuel, and other issues.
>
> Foreign material in the aftertreatment DPF is **not** normal and can be caused by issues such as degraded exhaust system components, exhaust leaks, or damage to engine or other components.
>
> **Note · Примечание**
> Check for active fault codes prior to performing the Aftertreatment Diesel Particulate Filter Restriction Test. If active fault codes are present, reference the appropriate fault code troubleshooting tree before completing this test, unless you are directed to perform this test in a troubleshooting tree.
>
> **Note · Примечание**
> The Aftertreatment Diesel Particulate Filter Restriction Test **must** be performed immediately after the successful completion of an aftertreatment diesel particulate filter regeneration, except where noted in this procedure. The aftertreatment diesel particulate filter regeneration is performed using INSITE™ electronic service tool.
>
> Performing the aftertreatment diesel particulate filter regeneration makes sure that any exhaust residue or soot is removed from the aftertreatment DPF, resulting in a restriction measurement that is attributable to ash content, except where foreign material has entered the aftertreatment DPF. Performing the aftertreatment diesel particulate filter stationary regeneration also makes sure that the aftertreatment DPF temperature is raised to a level that provides maximum exhaust gas flow rate during the restriction test and that any moisture present has also been removed.
>
> ### Preparatory Steps
>
> Exhaust Outlet Inspection
>
> Inspect the exhaust system outlet.
>
> Inspection of the exhaust system outlet can aid in determining the condition of the aftertreatment DPF. The exhaust system outlet should appear clean with little to no exhaust residue or soot buildup.
>
> **Note · Примечание**
> Some accumulation of exhaust residue or soot is normal, and does **not** indicate an issue with the aftertreatment DPF.
>
> A heavy buildup of exhaust residue or soot accumulation on the exhaust system outlet is the result of an issue with the aftertreatment DPF. Perform the Snap Acceleration Test - Aftertreatment Connected.
>
> Snap Acceleration - Aftertreatment Connected
>
> Open INSITE™ electronic service tool, but do **not** connect to the engine control module (ECM).
>
> Go to Tools \> Options \> Units of Measure.
>
> In the drop down menu in the Units of Measure menu, select Metric. Select the Apply button and then select the OK button.
>
> Close INSITE™ electronic service tool Options menu.
>
> Connect INSITE™ electronic service tool to the service data link. [[105-019-428 — Engine Datalinks|Refer to Procedure 019-428 in Section 19.]]
>
> Capture a work order (job image) with INSITE™ electronic service tool.
>
> Use INSITE™ electronic service tool to enable the Setup for Dynamometer ECM Diagnostic Test.
>
> **Note · Примечание**
> It is necessary to activate this test to allow the engine speed to reach the required level without requiring a change to Customer Feature and Parameter Settings (i.e. Maximum Vehicle Speed Without VSS, Load Based Speed Control, etc.)
>
> **Note · Примечание**
> The setup for the Dynamometer ECM Diagnostic Test can be found in the ECM Diagnostic Tests section of INSITE™ electronic service tool.
>
> - The vehicle transmission **must** be in NEUTRAL.
> - The vehicle parking brake **must** be applied.
> - The vehicle hood **must** be closed.
> - The manual fan switch, if equipped, and vehicle air conditioning system **must** be turned OFF to prevent engine cooling fan operation during this test.
> - The engine **must** be at normal operating temperature (above 82°C \[180°F\] coolant temperature).
>
> Start the engine.
>
> Allow the engine to stabilize at low idle for 30 seconds.
>
> Depress and hold the accelerator pedal to verify that the engine can reach high idle (normally 1800-2000 rpm).
>
> Release the accelerator pedal and allow the engine to stabilize at low idle for 30 seconds.
>
> Quickly depress the accelerator pedal from 0 percent to 100 percent and hold the engine at high idle (normally 1800 - 2000 rpm) for 5 seconds.
>
> Release the accelerator pedal and allow the engine to stabilize at low idle for 30 seconds.
>
> Repeat the Snap Acceleration Test - Aftertreatment Connected as needed to allow a visual check for smoke at the exhaust system outlet to be completed as the engine is accelerated from low idle to high idle.
>
> **Note · Примечание**
> The visual check may need to be performed with the aid of another technician, depending on the vehicle's exhaust configuration.
>
> During the Snap Acceleration Test - Aftertreatment Connected, check for black smoke exiting the exhaust system outlet, as the engine is accelerated from low idle to high idle.
>
> **Note · Примечание**
> In some applications, a Snap Acceleration Test may **not** provide the conditions necessary to reveal a malfunctioning aftertreatment DPF. If there is a heavy buildup of exhaust residue/soot on the exhaust outlet and a snap acceleration does **not** reveal a condition outlined in the following steps, it can be necessary to perform a brief acceleration run under partial to full load or to perform a stall test. Refer to Procedure 014-008 in Section 14.
>
> If black smoke is found at the exhaust system outlet during these tests, reference the Aftertreatment Diesel Oxidation Catalyst and Aftertreatment Diesel Particulate Filter Reuse Guidelines, Bulletin 4021600, and inspect the aftertreatment DPF for damage.
>
> Do **not** use the Aftertreatment Diesel Particulate Filter Restriction Test to evaluate a damaged aftertreatment DPF. Incorrect test results **will** occur.
>
> If gray smoke or faint black smoke is present, reference the Aftertreatment Diesel Oxidation Catalyst and Aftertreatment Diesel Particulate Filter Reuse Guidelines, Bulletin 4021600, and inspect the aftertreatment DPF for damage. White smoke during the Snap Acceleration Test - Aftertreatment Connected may **not** indicate a malfunction. No additional troubleshooting or repair is necessary at this time.
>
> If black or gray smoke is **not** found at the exhaust system outlet, proceed to the Sensor Signal Voltage Test in this section.
>
> Sensor Signal Voltage Test
>
> In INSITE™ electronic service tool, add the following parameters to the Data Monitor/Logger screen:
>
> 1. Engine speed (rpm)
> 2. Exhaust volumetric flow rate (m 3 /s)
> 3. Aftertreatment DPF differential pressure (kPa)
> 4. Aftertreatment DPF differential pressure sensor signal voltage (VDC).
>
> Verify that the parameter aftertreatment DPF differential pressure sensor signal voltage reads 0.69 VDC (± 0.22 VDC at 25°C \[77°F\] and below or ± 0.14 VDC at 26°C \[78°F\] or greater) at keyswitch ON, engine OFF.
>
> **Note · Примечание**
> If the aftertreatment DPF differential pressure sensor signal voltage does **not** read within specification, inspect the aftertreatment DPF differential pressure sensor and associated wiring. Use the following procedure in the CM871 and CM876 Electronic Control Systems, ISX and ISM Engines, Bulletin 4021560. Refer to Procedure 019-443 in Section 19.
>
> Disconnect the aftertreatment DPF differential pressure sensor wiring harness connector.
>
> Use INSITE™ electronic service tool to verify that Fault Codes 1881 and 3134 are active.
>
> **Note · Примечание**
> If Fault Code 1881 did **not** become active, inspect the aftertreatment DPF differential pressure sensor and associated wiring. Use the following procedure in the CM871 and CM876 Electronic Control Systems, ISX and ISM Engines, Bulletin 4021560. Refer to Procedure 019-443 in Section 19.
>
> Use the Framatome™ male test lead, Part Number 3164596, or equivalent, to short the aftertreatment DPF differential pressure sensor 5 VDC SUPPLY (pin 4 of the wiring harness connector) to the aftertreatment DPF differential pressure sensor SIGNAL (pin 2 of the wiring harness connector).
>
> Use INSITE™ electronic service tool to verify that Fault Code 1879 is active.
>
> **Note · Примечание**
> If Fault Codes 1879 did **not** become active, the aftertreatment DPF differential pressure sensor signal and aftertreament diesel particulate filter outlet pressure sensor signal could be incorrectly routed. Refer to the original equipment manufacturer (OEM) service manual.
>
> **Note · Примечание**
> If Fault Codes 1881 did **not** become active, inspect the aftertreatment DPF differential pressure sensor and associated wiring. Use the following procedure in the CM871 and CM876 Electronic Control Systems, ISX and ISM Engines, Bulletin 4021560. Refer to Procedure 019-443 in Section 19.
>
> Verify that issues with the aftertreatment DPF differential pressure sensor and associated wiring have been corrected by repeating the previous steps, if necessary.
>
> Connect the aftertreatment DPF differential pressure sensor wiring harness connector.
>
> Use INSITE™ electronic service tool to clear the inactive fault codes from the aftertreatment DPF differential pressure sensor test(s).
>
> ### Test
>
> Verify that the following conditions have been met:
>
> 1. The vehicle is parked in an appropriate location, on a surface that will **not** burn or melt under high temperatures (such as clean concrete or gravel, **not** grass or asphalt) and away from anything that can burn, melt, or explode.
> 2. The vehicle is parked securely.
> 3. Set up a safe exhaust area.
> 4. Check the exhaust system surfaces.
> 5. Prepare for engine speed changes during regeneration.
> 6. Make sure that the vehicle and surrounding areas are monitored during regeneration. If any unsafe condition occurs, be prepared to shut the engine OFF immediately.
>
> **WARNING · Опасно**
> During regeneration, exhaust gas temperature could reach 800°C \[1500°F\] and exhaust system surface temperature can exceed 700°C \[1300°F\], which is hot enough to ignite or melt common materials, and cause severe burn injuries. The exhaust and exhaust components can remain hot after the vehicle stopped moving. To avoid the risk of fire, property damage, burns, or other serious personal injury, make sure that no combustible materials are located where they are likely to come in contact with hot exhaust or exhaust components.
>
> Perform the aftertreatment DPF regeneration using INSITE™ electronic service tool.
>
> **Note · Примечание**
> It is **not** necessary to allow the aftertreatment DPF regeneration to fully complete during this section of the procedure (a minimum of 30 minutes is recommended).
>
> **Note · Примечание**
> The aftertreatment DPF regeneration can be found under the ECM Diagnostic Test menu in INSITE™ electronic service tool.
>
> **Note · Примечание**
> Engine speed will increase and the turbocharger can whistle loudly during the aftertreatment DPF Regeneration Test.
>
> To stop the aftertreatment DPF regeneration, engage the clutch, service brake, and accelerator pedal; or shut the engine OFF.
>
> Once regeneration is complete, exhaust gas and exhaust surface temperatures will remain elevated for 3 to 5 minutes.
>
> **WARNING · Опасно**
> The engine cooling fan must be fully engaged and locked in the ON position before conducting the Aftertreatment Diesel Particulate Filter Restriction Test. Failure to lock the engine cooling fan in the ON position may result in damage to the fan clutch, engine or other components.
>
> Shut the engine OFF.
>
> Set the engine cooling fan to the ON, ENGAGED, or LOCKED position.
>
> **Note · Примечание**
> Do **not** use INSITE™ electronic service tool to change feature and parameter settings to alter the operation of the engine cooling fan. Most engine cooling fans are designed to default to the ON, ENGAGED, or LOCKED position with a loss of air pressure or electrical current. In order to alter engine cooling fan operation, it may be necessary to disconnect the air or electrical supply. Reference the equipment manufacturer service information.
>
> Start the engine.
>
> Verify that the engine cooling fan will maintain the ON, ENGAGED, or LOCKED position. Reference the equipment manufacturer service information.
>
> Shut the engine OFF.
>
> Use INSITE™ electronic service tool to enable the Setup for Dynamometer ECM Diagnostic Test.
>
> **Note · Примечание**
> It is necessary to activate this test to allow the engine speed to reach the required level without requiring a change to customer feature and parameter settings (i.e. Maximum Vehicle Speed Without VSS, Load Based Speed Control, etc.).
>
> **Note · Примечание**
> The setup for Dynamometer ECM Diagnostic Test can be found in the ECM Diagnostic Test section of INSITE™ electronic service tool.
>
> **Note · Примечание**
> This procedure requires that the engine be operated at high idle for thirty (30) seconds. Do **not** attempt to perform a Snap Acceleration Test - Aftertreatment Connected during this section of the procedure. Incorrect test results will occur.
>
> Perform the following steps:
>
> 1. Start the engine.
> 2. Allow the engine to stabilize at low idle for 30 seconds.
> 3. Depress the accelerator from 0 percent to 100 percent and hold the engine at high idle (normally 1800 to 2000 rpm)
> 4. Use INSITE™ electronic service tool Data Monitor/Logger to log these parameters.
> 5. Observe the parameter exhaust volumetric flow rate in INSITE™ electronic service tool Data Monitor/Logger.
> 6. Verify that the exhaust volumetric flow rate reaches 0.3 m 3 /s or higher.
> 7. Stop INSITE™ electronic service tool Data Monitor/Logger after 30 seconds and save the resulting log file using the file name ESN\_After\_Cleaning\_Run\_1.log.csv where ESN is the engine serial number of the vehicle being tested. Save the log file in a suitable location where it will be easy to locate. Use the ESN as the folder name.
> 8. Release the accelerator pedal and allow the engine to stabilize at low idle for 30 seconds.
> 9. Repeat the applicable step (2-8) four more times, saving the Data Monitor/Logger log file using the file names ESN\_After\_Cleaning\_Run\_2.log.csv, ESN\_After\_Cleaning\_Run\_3.log.csv, ESN\_After\_Cleaning\_Run\_4.log.csv, and ESN\_After\_Cleaning\_Run\_5.log.csv, where ESN is the engine serial number of the vehicle being tested. Save the log files in a suitable location where they will be easy to locate. Use the ESN as the folder name.
>
> ### Analyzing the Data
>
> Locate the log file(s) taken with INSITE™ electronic service tool Data Monitor/Logger during the Test section of this procedure.
>
> **Note · Примечание**
> The log files will be stored in the folder C:\\Intelect\\Insite\\Logs by default where C: represents the drive letter of the hard drive on which INSITE™ electronic service tool is installed.
>
> | DPF Part Number |  |  |  |
> |---|---|---|---|
> | Phase 1 | Phase 2 | Phase 3 | Phase 4 |
> | 4969702 | 5283669 | 5297522 | 4388409 |
> | 4969701 | 5283778 | 5297990 | 4388410 |
> | 4969701 | 5283799 | 5297989 | 4388411 |
>
> Review the log files from INSITE™ electronic service tool taken during the Test section of this procedure.
>
> Obtain the aftertreatment DPF differential pressure (kPa) at 0.3 m3/s or greater of exhaust volumetric flow once the engine reached high idle and stabilized.
>
> The aftertreatment DPF differential pressure should be below the Maximum - After Regeneration specification for a given exhaust volumetric flow rate, as shown in the table below:
>
> | Aftertreatment DPF Differential Pressure (Phase 2 or 3 DPF) |  |
> |---|---|
> | Exhaust Volumetric Flow Rate (m 3 /s) | Maximum (kPa) |
> | 0.30 | 1.75 |
> | 0.35 | 2.15 |
> | 0.40 | 2.55 |
> | 0.45 | 3.00 |
> | 0.50 | 3.40 |
> | 0.55 | 3.80 |
> | 0.60 | 4.20 |
> | 0.65 | 4.60 |
> | 0.70 | 5.00 |
> | 0.75 | 5.45 |
> | 0.80 | 5.85 |
>
> If the aftertreatment DPF differential pressure is **not** below the Maximum - After Regeneration specification above, the aftertreatment DPF **must** be replaced. [[101-011-041-tr — Aftertreatment Diesel Particulate Filter|Refer to Procedure 011-041 in Section 11.]]
>
> | Aftertreatment DPF Differential Pressure (Phase 4 DPF) |  |
> |---|---|
> | Exhaust Volumetric Flow Rate (m 3 /s) | Maximum (kPa) |
> | 0.30 | 2.25 |
> | 0.35 | 2.65 |
> | 0.40 | 3.05 |
> | 0.45 | 3.50 |
> | 0.50 | 3.90 |
> | 0.55 | 4.30 |
> | 0.60 | 4.70 |
> | 0.65 | 5.10 |
> | 0.70 | 5.50 |
> | 0.75 | 5.95 |
> | 0.80 | 6.30 |
>
> If the aftertreatment DPF differential pressure is **not** below the Maximum - After Regeneration specification above, the aftertreatment DPF **must** be replaced. [[101-011-041-tr — Aftertreatment Diesel Particulate Filter|Refer to Procedure 011-041 in Section 11]].
>
> ### Finishing Steps
>
> Use INSITE™ electronic service tool to check for any active fault codes. If any active fault codes are present, reference the appropriate fault code troubleshooting tree in Section TS.
>
> Use INSITE™ electronic service tool to clear all inactive fault codes.
>
> Use INSITE™ electronic service tool to perform an Aftertreatment Maintenance Reset All and Aftertreatment Filter Installation procedure.
>
> **Note · Примечание**
> The Aftertreatment Maintenance Reset All and Aftertreatment Filter Installation procedure can be found in INSITE™ electronic service tool in the Advanced ECM Data section, under Aftertreatment Maintenance.
