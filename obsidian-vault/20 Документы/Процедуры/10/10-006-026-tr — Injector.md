---
aliases:
  - "Форсунка"
type: "Процедура"
doc: "10-006-026-tr"
title_en: "Injector"
title_ru: "Форсунка"
modified: "2014-11-07"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
manuals:
  - "3666239"
figures: 51
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-006-026-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-006-026-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSX15"
  - "группа/10"
  - "перевод/машинный"
---

# Injector
**Форсунка**

> [!abstract] Процедура · `10-006-026-tr`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Входит в руководства:** [[3666239 — Signature™, ISX, and QSX15 Service Manual|3666239]]
> **Секции:** Section 06 - Injectors and Fuel Lines · Section 6 - Injector and Fuel Lines - Group 06 · Section 6 - Injectors and Fuel Lines · Section 6 - Injectors and Fuel Lines - Group 06
> **Даты:** изменён 2014-11-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-006-026-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-006-026-tr.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Тест на утечку

Этот тест проверяет утечку газа сгорания обратно через контрольный клапан форсунки или другие условия, которые позволят утечке газа через форсунка в топливном рельсе.

Когда двигатель перекрыт, обратное давление создается против топливного форсунка поршнем, поднимающимся на ход сжатия.

Во время испытания, если протекает клапан проверки рельсов, воздух проталкивается через контрольный клапан рельсов и в топливный рельс. Давление ощущается на испытательном стенде, который находится на месте дозирующего привода. Если к испытательному приспособлению подключен манометр, давление будет измеряться по мере выхода воздуха через протекающий клапан проверки рельсов. Если вместо манометра используется емкость с водой, пузырьки будут рассматриваться как воздушные выходы через протекающий клапан проверки рельсов.

Накладные отметки на демпфере используются для определения того, какой цилиндр находится на ходу сжатия, и, следовательно, какая форсунка неисправна, если наблюдается изменение давления манометра или пузырьков.

Закройте двигатель.

![[00c00077.png]]

Приводы для учета топлива представляют собой приводы, расположенные на каждом конце блока.

Для двигателей, оснащенных CM871, удалите привод для учета топлива для передних трех цилиндров. Используйте руководство по устранению неполадок и ремонту электронной системы управления SignatureTM ISX и QSX15, Bulletin 3666259. См. процедуру 019-110 в разделе 19.

Для двигателей, оснащенных CM870, удалите привод учета топлива для передних трех цилиндров. Используйте руководство по устранению неполадок и ремонту электронной системы управления SignatureTM ISX CM870, Bulletin 4021334. См. процедуру 019-110 в разделе 19.

Установите форсунку Leak Test Kit, номер детали 3164001, вместо привода для измерения расхода топлива.

> [!tip] Момент затяжки
> 15.3 Н·м [135 фунт-дюйм]

Подключите гибкую трубку к шлангу, установленному на монтажной пластине.

Поместите гибкую трубку в контейнер с водой.

![[00c00078.png]]

> [!warning] ОСТОРОЖНО
> Не запускайте двигатель более 20 секунд и не допускайте 2 минут между циклами запуска для охлаждения стартера. Неспособность сделать это может привести к началу повреждения моторных компонентов.

Удалите 4-контактный разъем питания из модуля управления двигателем (ECM), а затем прокрутите двигатель. Отключение 4-контактного разъема питания предотвратит запуск двигателя.

> [!note] Примечание
> Для двигателей без 4-контактных разъемов питания на ECM отсоедините отключающий соленоидный провод подачи топлива от отключающего соленоида топлива, а затем прокрутите двигатель. Отключение отключения топлива соленоидной проволоки питания предотвратит запуск двигателя.

Если в контейнере не наблюдается пузырьков, то в переднем берегу происходит утечка. Продолжить проверку трех задних цилиндров, описанную в нижеследующей процедуре.

Если в контейнере наблюдаются пузырьки, продолжайте перекрывать двигатель, чтобы определить, какая форсунка протекает.

Заблокируйте двигатель, наблюдая за пузырьками в контейнере. Если в контейнере не наблюдается пузырьков при замыкании двигателя, это **не **указывает на отсутствие утечки. Продолжайте перекрывать двигатель, чтобы создать достаточное обратное давление, чтобы определить, какая форсунка протекает.

Двигатель должен быть заблокирован в течение трех полных оборотов для оценки каждого банка.

Могут наблюдаться несколько пузырьков непосредственно перед достижением отметки времени. Индикатор утечки - это если пузырьки возникают в течение длительного периода между временными метками.

![[08c00214.png]]

Обратите внимание, между которыми два момента означают, что пузырьки возникают. Определить утечку форсунки, следуя диаграмме.

Если пузырьки возникают между:

- A и B (утечка топлива № 3)
- B и C (утечка форсунки № 1)
- C и A (форсунка № 2 протекает).

![[06c00110.png]]

Для двигателей, оснащенных CM871, удалите монтажную пластину, соединенную с портом для передних трех цилиндров. Установите ранее снятый привод учета топлива. Используйте руководство по устранению неполадок и ремонту электронной системы управления SignatureTM ISX и QSX15, Bulletin 3666259. См. процедуру 019-110 в разделе 19.

Для двигателей, оснащенных CM870, удалите монтажную пластину, соединенную с портом для передних трех цилиндров. Установите ранее снятый привод учета топлива. Используйте руководство по устранению неполадок и ремонту электронной системы управления SignatureTM ISX CM870, Bulletin 4021334. См. процедуру 019-110 в разделе 19.

Удалите привод для учета топлива для задних трех цилиндров.

Установите форсунку Leak Test Kit, номер детали 3164001, вместо заднего привода для учета топлива.

> [!tip] Момент затяжки
> 15.3 Н·м [135 фунт-дюйм]

Поместите гибкую трубку в контейнер с водой.

Повторите вышеупомянутую процедуру для трех задних цилиндров.

![[05c00122.png]]

Перекройте двигатель и обратите внимание, между которыми происходят два момента.

Если пузырьки возникают между:

- A и B (утечка топлива 4)
- B и C (утечка топлива 6)
- C и A (форсунка номер 5 протекает).

![[06c00109.png]]

Заменить протекающий форсунка (форсунки). Перейдите в раздел Удалить в этой процедуре.

![[02c00024.png]]

### Подготовительные операции

> [!danger] ОПАСНО
> Не снимайте пробку радиатора с горячего двигателя. Снимайте пробку радиатора только после того, как температура охлаждающей жидкости опустится ниже 50 °C \[120 °F\]. Струя горячей охлаждающей жидкости или пар могут привести к травме.

> [!danger] ОПАСНО
> Охлаждающая жидкость токсична. Хранить в недоступном для детей и животных месте. Если деталь не используется повторно, утилизируйте её по местным природоохранным требованиям.

- Охладитель опускайте ниже уровня головки цилиндра.[[10-008-018-tr — Cooling System|См. процедуру 008-018 в разделе 8.]]
- Снимите крышку коромысел. См. процедуру 003-011 в разделе 3.
- Отключите тормоз двигателя соленоидной проводкой упряжки.[[10-020-015 — Engine Brake Wiring Harness|См. процедуру 020-015 в разделе 20.]]

![[ck800wa.png]]

### Снятие

> [!warning] ОСТОРОЖНО
> Не добавляйте корректирующие винты. Повреждение двигателя может произойти, если регулировочные винты снизу.

Удалить **только **вал топливного форсунка, в котором расположена валка качения для топливных форсунок (форсунок), подлежащих удалению.

Ослабьте топливный форсунок клапана клапана коромысла рычага регулирования винтов.

Удалите шесть болтов и вал топливного клапана клапана качения.

Не позволяйте рычагам коромысла сойти с вала во время удаления.

![[03c00006.png]]

Поверните двигатель на заданный клапаном знак для снимаемого топливного форсунка.[[10-003-004-tr — Overhead Set|См. процедуру 003-004 в разделе 3.]]

![[17c00091.png]]

Разблокируйте и поверните винты регулировки ресниц клапана **против часовой стрелки**, чтобы позволить снять мосты впускного и выпускного клапанов.

Удалите впускной клапанный мостик.

Отметьте клапанные мосты, чтобы убедиться, что они установлены в одном и том же положении.

![[03c00087.png]]

Поместите мост клапана выхлопного клапана к стороне выхлопа двигателя, чтобы позволить форсунка быть удаленным.

![[06c00003.png]]

Устранить зажимные болты форсунки.

Используйте небольшой магнит, чтобы удалить зажимные болты форсунки.

Удалите зажим форсунки.

![[06c00002.png]]

> [!warning] ОСТОРОЖНО
> Не используйте пятку, чтобы вырвать форсунка из головки цилиндра. Повреждения форсунки могут произойти.

Используйте топливный форсунок, номер детали 3823579, чтобы удалить топливный форсунок.

Если пружина форсунки действительно выходит из пружинного удерживающего устройства, ее можно собрать повторно, используя отвертку для сжатия пружины под удерживающим устройством.

![[06c00096.png]]

### Проверка при повторном использовании

Осмотрите форсунку на наличие отсутствующих или поврежденных колец. Замените кольца по мере необходимости.

![[06c00099.png]]

Проверьте форсунку для отсутствующих шариков. Замените форсунку, если это необходимо.

![[06c00100.png]]

### Разборка

Масляные уплотнения, Roll pin сохранили кольцо нагрузки

Тщательно очищайте масло и грязь снаружи топливного форсунка.

Поместите форсунка в крепеж для удерживания форсунки.

Поместите форсунка, удерживающий фиксатор, в бирку. Затяните фиксатор, чтобы он был на месте.

Выровнять кронштейн затворов кольца нагрузки вырезом в фиксирующей пластине.

![[22c00182.png]]

Используйте привод T45 TorxTM (длинная версия) для ослабления болтов удерживающего устройства для форсунки форсунки.

![[22c00183.png]]

Убедитесь, что форсунка остается вертикальной. Это позволит предотвратить выпадение нижнего плунжера и пружины.

Снимите болты и скобки.

Удалите верхнюю плунжерную/сцепную сборку и соединительную пружину.

Некоторые части топливных форсунок не являются взаимозаменяемыми.

Поместите каждую из отдельных частей сборки топливного форсунка вместе на ткань без вязания.

![[22c00184.png]]

Удалите пружинный клип из кольца нагрузки.

Бурение кольца нагрузки предназначено для удаления и установки штифта крена только в одном направлении. Удалите в указанном направлении.

Используйте 5/32-дюймовый удар, чтобы слегка нажать на штифт рулона и удалить его из кольца нагрузки.

Отбросьте булавку.

![[22c00203.png]]

Удалите кольцо нагрузки из корпуса форсунки.

![[22c00186.png]]

Установите соединительную/разгрузочную установку в цилиндр корпуса форсунки, чтобы предотвратить попадание мусора в цилиндрический отсек.

![[22c00187.png]]

Основа масляного уплотнения видна через четыре обработанных отверстия в боковой части корпуса форсунки.

![[22c00188.png]]

> [!warning] ОСТОРОЖНО
> Очень важно, чтобы был использован 3/32-дюймовый удар, чтобы ствол не был поврежден во время удаления масляного уплотнения.

Используйте 3/32 дюймовый удар. Поместите удар под углом вверх, как показано на иллюстрации, к основанию масляного уплотнения.

Используйте молоток, чтобы мягко нажать удар на основание масляного уплотнения. Чтобы предотвратить повреждение цилиндра уплотнения, пробитого в стволе, чередуйте между четырьмя отверстиями в стволе, чтобы уплотнение вышло равномерно и не забивало ствол.

![[22c00189.png]]

> [!danger] ОПАСНО
> При работе со сжатым воздухом применяйте защиту глаз и лица. Разлетающиеся частицы и грязь могут привести к травме.

Скользите маслом, запечатайте плунжер.

Используйте консервную банку растворителя для выдувания мусора из области масляного уплотнения перед удалением плунжера.

![[22c00190.png]]

Убедитесь, что форсунка остается вертикальной.

Удалите масляную уплотнитель и плунжерную сборку из топливного форсунка.

Удалите старый масляной уплотнитель из плунжера.

Удалите форсунка, удерживающий фиксацию, и форсунка из вис.

Поместите крепеж и форсунка на пресс-стол беседки.

![[22c00191.png]]

Масляные уплотнения, Clip сохранили зарядное кольцо

Тщательно очищайте масло и грязь снаружи топливного форсунка.

Поместите чистое, без ворсинок полотенце магазина, сложенное в кварталах, на край стенда для тестирования работы.

При крепком удерживании форсунки в одной руке поместите верхний плунжер на внешний край испытательного стенда с нагрузочным кольцом чуть выше рабочей поверхности испытательного стенда.

Наклонитесь на форсунка, чтобы частично сжать верхнюю пружину и плунжер. Используйте осторожность **не**, чтобы войти в контакт с соплом форсунки.

![[06c00136.png]]

Используйте кирку для удаления зажима удерживающего кольца нагрузки форсунки.

![[06c00137.png]]

Медленно снимите давление с топливного форсунка, выпуская верхнюю пружину.

Встаньте форсунка вертикально и удалите кольцо нагрузки, верхний плунжер / сборку соединения и пружину.

> [!note] Примечание
> Некоторые части форсунки являются **не** взаимозаменяемыми.

Поместите каждую из отдельных частей сборки топливного форсунка вместе на ткань без вязания.

![[06c00138.png]]

Поместите форсунка в удерживающий крепеж, установленный в измерительном стенде.

![[06c00156.png]]

Найдите внешний край верхней уплотнения.

Используйте удар, удерживаемый под небольшим углом, как показано на иллюстрации, чтобы тщательно сложить край уплотнения внутрь и вниз.

Сложите край уплотнения на 180 градусов от первой складки.

Используйте осторожность **не**, чтобы повредить корпус форсунки.

![[06c00139.png]]

Когда уплотнение начинает вращаться в цилиндре корпуса форсунки, осторожно вставьте небольшую штангу в центр уплотнения.

Тщательно вытаскивайте уплотнение из цилиндра корпуса форсунки.

Используйте осторожность **не**, чтобы повредить корпус форсунки.

![[06c00141.png]]

### Сборка

Масляные уплотнения, Roll pin сохранили кольцо нагрузки

> [!warning] ОСТОРОЖНО
> Не устанавливайте масляную уплотнение вверх ногами. Несоблюдение правильной установки уплотнения приведет к повреждению масляного уплотнения.

Масляная уплотнение плотно поместится на инструменте, если установлена правильно. Пружинная сторона масляного уплотнения, как показано, обращена вверх при установке в топливном форсунке.

Установите новый масляный уплотнитель на инструмент установки.

![[22c00192.png]]

С новым масляным уплотнением, расположенным на инструменте, поместите инструмент над цилиндром уплотнения.

Используйте пресс беседки, чтобы мягко поместить давление на инструмент установки до тех пор, пока наружная сторона диаметра инструмента не свяжется с корпусом форсунки.

При правильной установке высота уплотнения **не** будет промываться корпусом форсунки. Высота будет приблизительно 0,5 мм \[0,020 дюйма \] над топливным форсункой.

![[22c00193.png]]

Поместите форсунка с удерживающим креплением с топливным форсункой в форсуну. Затяните фиксатор, чтобы он был на месте.

Установите на форсунка кольцо нагрузки. Выровнять отверстие затворов кольца нагрузки с вырезом на топливном форсунке.

![[22c00186.png]]

Установите новый штифт в кольцо нагрузки. По конструкции отверстия для штифта рулона имеют разные размеры с каждой стороны, поэтому штифт рулона должен быть установлен в правильном направлении, как показано на рисунке.

Используйте 5/32-дюймовый удар, чтобы мягко нажать на штифт рулона в оба отверстия в кольце нагрузки. Продолжайте движение рулонного штифта в нагрузочное кольцо, пока штифт не будет равномерно центрирован в обоих отверстиях и не будет находиться на равном расстоянии от обеих сторон.

![[22c00204.png]]

Осмотрите масляный уплотнитель и цилиндр плунжера, несущие мусор. Если присутствуют обломки, чистите с помощью безвязочной ткани.

Очистить пружину форсунки с помощью безлитражной ткани. Соберите пружину на грузовое кольцо.

Очистить плунжер и соединительную сборку с помощью безлипкой ткани.

![[22c00197.png]]

Смазать плунжер чистой калибровочной жидкостью.

![[22c00198.png]]

Немного под углом и поверните верхний плунжер при установке плунжер в масляную уплотнение.

Держите плунжер вертикально и вращайтесь при установке плунжера в цилиндр форсунки.

![[22c00199.png]]

Используйте фонарик для просмотра через соединительную пружину. Проверить масляную уплотнение, чтобы проверить подвязочный пружин (1), все еще находится в правильном месте вокруг уплотнения.

![[22c00200.png]]

Установите пружинную брекет-резервную кронштейн.

Затяните болты для крепления.

> [!tip] Момент затяжки
> 30 Н·м [22 фунт-фут]

Установите новые топливные форсунки.

![[22c00201.png]]

Масляные уплотнения, Clip сохранили зарядное кольцо

> [!warning] ОСТОРОЖНО
> Не устанавливайте масляную уплотнение вверх ногами. Несоблюдение правильной установки уплотнения приведет к повреждению масляного уплотнения.

Масляная уплотнение плотно поместится на инструменте, если установлена правильно. Пружинная сторона масляного уплотнения, как показано, обращена вверх при установке в топливном форсунке.

Установите новый масляный уплотнитель на инструмент установки.

![[22c00192.png]]

С новым масляным уплотнением, расположенным на инструменте, поместите инструмент над цилиндром уплотнения.

Используйте пресс беседки, чтобы мягко поместить давление на инструмент установки до тех пор, пока наружная сторона диаметра инструмента не свяжется с корпусом форсунки.

При правильной установке высота уплотнения **не** будет промываться корпусом форсунки. Высота будет приблизительно 0,5 мм \[0,020 дюйма \] над топливным форсункой.

![[06c00157.png]]

Смазать плунжер чистой калибровочной жидкостью.

Тщательно установите пружинное и нагрузочное кольцо на верхний плунжер.

![[22c00198.png]]

Держа форсунка вертикально в одной руке, слегка под углом и вращайте верхний плунжер при установке плунжера в масляную уплотнитель.

Держите плунжер вертикально и вращайтесь при установке плунжера в цилиндр форсунки.

![[06c00143.png]]

Используйте фонарик для просмотра через соединительную пружину. Проверьте масляную уплотнение, чтобы убедиться, что подвязочный пружина все еще находится в правильном месте вокруг уплотнения.

![[06c00144.png]]

Поместите чистое, без ворсинок полотенце магазина, сложенное в кварталах, на край стенда для тестирования работы.

При крепком удерживании форсунки в одной руке поместите верхний плунжер на внешний край испытательного стенда с нагрузочным кольцом чуть выше рабочей поверхности испытательного стенда.

Наклонитесь на форсунка, чтобы частично сжать верхнюю пружину и плунжер. Используйте осторожность **не**, чтобы войти в контакт с соплом форсунки.

![[06c00145.png]]

Установите зажим на кольцо нагрузки форсунки.

Медленно снимите давление с форсунки, отпустив верхнюю пружину к нагрузочному кольцу.

Установите новые топливные форсунки.

![[06c00146.png]]

### Установка

Используйте чистое моторное масло 15W-40 для смазки колец.

![[06c00097.png]]

> [!warning] ОСТОРОЖНО
> Убедитесь, что форсунка удерживает зажим правильно выровнен перед затягиванием болтов. Зажим может контактировать с близлежащим выступом и приводить к низкой нагрузке на зажим.

Установите форсунку в головку цилиндра. Установите зажим и болты форсунки.

Затяните болт.

> [!tip] Момент затяжки
> 80 Н·м [59 фунт-фут]

Установите клапанные мосты.

![[06c00098.png]]

### Завершающие операции

- Установите и установите топливный форсунок клапана клапана коромысленного рычага и клапан клапана клапана коромысленного рычага сборки.[[10-003-009-tr — Rocker Lever Assembly|См. процедуру 003-009 в разделе 3.]]
- Подключите тормоз двигателя соленоидной проводкой упряжки, если она оборудована.[[10-020-015 — Engine Brake Wiring Harness|См. процедуру 020-015 в разделе 15.]]
- По мере необходимости отрегулируйте накладные расходы.[[10-003-004-tr — Overhead Set|См. процедуру 003-004 в разделе 3.]]
- Установите крышку коромысел. См. процедуру 003-011 в разделе 3.
- Заправьте систему охлаждения.[[10-008-018-tr — Cooling System|См. процедуру 008-018 в разделе 8.]]
- Управляйте двигателем до нормальной рабочей температуры и проверяйте наличие утечек.

> [!note] Примечание
> Если повреждение привело к попаданию масла, чрезмерного топлива или черного дыма в выхлопную систему, необходимо проверить систему последующей обработки. Ссылка на Руководство по повторному использованию дизельного окислительного катализатора и дизельного фильтра для твердых частиц после обработки, Вестник 4021600.

> [!note] Примечание
> Если топливные форсунки заменяются из-за внутренней утечки охлаждающей жидкости, то элемент капканного передатчика должен быть изменен.[[101-003-019-tr — Crankcase Breather Element|См. процедуру 003-019 в разделе 3.]]

> [!note] Примечание
> Если повреждение привело к попаданию охлаждающей жидкости в выхлопную систему, система последующей обработки может быть восстановлена.[[101-014-013-tr — Aftertreatment Testing|См. процедуру 014-013 в разделе 14.]]

![[ck800wa.png]]


> [!quote]- Original (English) · английский оригинал
> ### Leak Test
>
> This test checks for combustion gas leaks back through the injector rail check valve or other conditions that will allow gas leakage through the injector into the fuel rail.
>
> When the engine is barred over, backpressure is created against the injector by the piston coming up on the compression stroke.
>
> During the test, if the rail check valve is leaking, air is pushed through the rail check valve and into the fuel rail. Pressure is sensed at the test fixture, which is in place of the metering actuator. If a manometer is connected to the test fixture, pressure will be measured as air escapes through the leaking rail check valve. If a container of water is used instead of a manometer, bubbles will be seen as air escapes through the leaking rail check valve.
>
> The overhead set marks on the damper are used to identify which cylinder is on the compression stroke, and therefore which injector has malfunctioned, if a change in manometer pressure or bubbles are seen.
>
> Shut the engine OFF.
>
> The fuel-metering actuators are the actuators located on each end of the unit.
>
> For engines equipped with the CM871, remove the fuel-metering actuator for the front three cylinders. Use the Signature™ ISX and QSX15 Electronic Control System Troubleshooting and Repair Manual, Bulletin 3666259. Refer to Procedure 019-110 in Section 19.
>
> For engines equipped with the CM870, remove the fuel-metering actuator for the front three cylinders. Use the Signature™ ISX CM870 Electronic Control System Troubleshooting and Repair Manual, Bulletin 4021334. Refer to Procedure 019-110 in Section 19.
>
> Install the Injector Leak Test Kit, Part Number 3164001, in place of the fuel-metering actuator.
>
> **Момент затяжки · Torque Value**
> 15.3 n•m [135 in-lb]
>
> Connect the flexible tubing to the hose fitting on the mounting plate.
>
> Place the flexible tubing into a container of water.
>
> **CAUTION · Осторожно**
> Do not crank the engine for more than 20 seconds and allow 2 minutes between crank cycles for the starter to cool. Failure to do so can result in starting motor component damage.
>
> Remove the 4-pin power connector from the engine control module (ECM) and then crank the engine. Disconnecting the 4-pin power connector will prevent the engine from starting.
>
> **Note · Примечание**
> For engines without 4-pin power connectors on the ECM, disconnect the fuel shutoff solenoid supply wire from the fuel shutoff solenoid and then crank the engine. Disconnecting the fuel shutoff solenoid supply wire will prevent the engine from starting.
>
> If no bubbles are observed in the container, there is **not** a leak in the front bank. Continue on to the checks for the rear three cylinders outlined in the procedure below.
>
> If bubbles are observed in the container, proceed with barring over the engine to determine which injector is leaking.
>
> Bar the engine over while watching for bubbles in the container. If no bubbles are observed in the container while barring the engine, it does **not** indicate that there is no leak. Continue to bar the engine over to build sufficient backpressure to determine which injector is leaking.
>
> The engine will need to be barred over three complete revolutions to evaluate each bank.
>
> There can be a few bubbles observed immediately before reaching a timing mark. The leak indicator is if bubbles occur for an extended period between the timing marks.
>
> Note between which two timing marks the bubbles occur. Determine the leaking injector by following the diagram.
>
> If bubbles occur between:
>
> - A and B (number 3 injector is leaking)
> - B and C (number 1 injector is leaking)
> - C and A (number 2 injector is leaking).
>
> For engines equipped with the CM871, remove the mounting plate connected to the port for the front three cylinders. Install the fuel-metering actuator removed previously. Use the Signature™ ISX and QSX15 Electronic Control System Troubleshooting and Repair Manual, Bulletin 3666259. Refer to Procedure 019-110 in Section 19.
>
> For engines equipped with the CM870, remove the mounting plate connected to the port for the front three cylinders. Install the fuel-metering actuator removed previously. Use the Signature™ ISX CM870 Electronic Control System Troubleshooting and Repair Manual, Bulletin 4021334. Refer to Procedure 019-110 in Section 19.
>
> Remove the fuel-metering actuator for the rear three cylinders.
>
> Install the Injector Leak Test Kit, Part Number 3164001, in place of the rear fuel-metering actuator.
>
> **Момент затяжки · Torque Value**
> 15.3 n•m [135 in-lb]
>
> Place the flexible tubing into a container of water.
>
> Repeat the above procedure for the rear three cylinders.
>
> Bar the engine over and note between which two timing marks the bubbles occur.
>
> If the bubbles occur between:
>
> - A and B (number 4 injector is leaking)
> - B and C (number 6 injector is leaking)
> - C and A (number 5 injector is leaking).
>
> Replace the leaking injector(s). Go to the Remove section in this procedure.
>
> ### Preparatory Steps
>
> **WARNING · Опасно**
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.
>
> **WARNING · Опасно**
> Coolant is toxic. Keep away from children and pets. If not reused, dispose of in accordance with local environmental regulations.
>
> - Drain the coolant to below the cylinder head level. [[10-008-018-tr — Cooling System|Refer to Procedure 008-018 in Section 8.]]
> - Remove the rocker lever cover. Refer to Procedure 003-011 in Section 3.
> - Disconnect the engine brake solenoid wiring harness. [[10-020-015 — Engine Brake Wiring Harness|Refer to Procedure 020-015 in Section 20.]]
>
> ### Remove
>
> **CAUTION · Осторожно**
> Do not bottom out adjusting screws. Engine damage can occur if adjusting screws are bottomed out.
>
> Remove **only** the injector rocker lever shaft for the injector(s) being removed.
>
> Loosen the injector rocker lever adjusting screws.
>
> Remove the six capscrews and injector rocker lever shaft.
>
> Do **not** let the rocker levers come off the shaft during removal.
>
> Rotate the engine to the valve set mark for the injector being removed. [[10-003-004-tr — Overhead Set|Refer to Procedure 003-004 in Section 3.]]
>
> Loosen and turn the valve lash adjusting screws **counterclockwise** to allow the intake and exhaust valve crossheads to be removed.
>
> Remove the intake crosshead.
>
> Mark the crossheads to make certain they are installed in the same position.
>
> Position the exhaust valve crosshead toward the exhaust side of the engine to allow the injector to be removed.
>
> Loosen the injector clamp capscrew.
>
> Use a small magnet to remove the injector clamp capscrew.
>
> Remove the injector clamp.
>
> **CAUTION · Осторожно**
> Do not use a heel bar to pry the injector loose from the cylinder head. Damage to the injector can occur.
>
> Use injector puller, Part Number 3823579, to remove the injectors.
>
> If the injector spring does come loose from the spring retainer, it can be reassembled by using a screwdriver to compress the spring back under the retainer.
>
> ### Inspect for Reuse
>
> Inspect the injector for missing or damaged o-rings. Replace o-rings as necessary.
>
> Inspect the injector cup for missing plug balls. Replace the injector, if necessary.
>
> ### Disassemble
>
> Oil Seals, Roll pin retained load ring
>
> Thoroughly clean the oil and dirt from the outside of the injector.
>
> Place the injector into the injector holding fixture.
>
> Place the injector holding fixture into a vise. Tighten the vise to hold the fixture in place.
>
> Align the load ring capscrew bracket with the cutout in the fixture plate.
>
> Use a T45 Torx™ drive (long version) to loosen the injector coupling retainer capscrew.
>
> Make certain the injector remains upright. This will prevent the lower plunger and spring from falling out.
>
> Remove the retainer capscrew and bracket.
>
> Remove the upper plunger/coupling assembly and coupling spring.
>
> Some injector parts are **not** interchangeable.
>
> Place each of the individual injector assembly parts together on a lint-free cloth.
>
> Remove the spring clip from the load ring.
>
> The load ring drilling is designed to remove and install the roll pin in **only** one direction. Remove in the direction shown.
>
> Use a 5/32 inch punch to lightly tap the roll pin loose and remove it from the load ring.
>
> Discard the roll pin.
>
> Remove the load ring from the injector body.
>
> Install the coupling/plunger assembly into the injector body bore to prevent debris from entering the bore.
>
> The base of the oil seal is visible through the four machined holes in the side of the injector body.
>
> **CAUTION · Осторожно**
> Its very important that a 3/32 inch punch be used so the barrel is not damaged during oil seal removal.
>
> Use a 3/32 inch punch. Place the punch at an upward angle, as shown in the illustration, against the base of the oil seal.
>
> Use a hammer to gently tap the punch against the base of the oil seal. To prevent damage to the seal bore in the barrel, alternate between the four holes in the barrel so that the seal comes out evenly and does **not** score the barrel.
>
> **WARNING · Опасно**
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.
>
> Slide the oil seal up the plunger.
>
> Use a can of safety solvent to blow debris away from the oil seal area before removing the plunger.
>
> Make certain the injector remains upright.
>
> Remove the oil seal and plunger assembly from the injector.
>
> Remove the old oil seal from the plunger.
>
> Remove the injector holding fixture and the injector from the vise.
>
> Place the fixture and injector onto the arbor press table.
>
> Oil Seals, Clip retained load ring
>
> Thoroughly clean the oil and dirt from the outside of the injector.
>
> Place a clean, lint-free shop towel folded in quarters over the edge of a work bench.
>
> While holding the injector firmly in one hand, place the upper plunger against the outer edge of the work bench with the load ring just above the working surface of the bench.
>
> Lean in on the injector to partially compress the upper spring and plunger. Use care **not** to come in contact with the nozzle of the injector.
>
> Use a pick to remove the injector load ring retaining clip.
>
> Slowly remove pressure from the injector, releasing the upper spring.
>
> Stand the injector upright and remove the load ring, the upper plunger/coupling assembly, and the spring.
>
> **Note · Примечание**
> Some of the injector parts are **not** interchangeable.
>
> Place each of the individual injector assembly parts together on a lint-free cloth.
>
> Place the injector in the holding fixture, mounted in a bench vise.
>
> Locate the outer edge of the upper seal.
>
> Use a punch, held at a slight angle, as shown in the illustration, to carefully fold the edge of the seal in and down.
>
> Fold the edge of the seal in, 180 degrees from the first fold.
>
> Use care **not** to damage the injector body.
>
> When the seal begins to rotate in the bore of the injector body, carefully insert a small pry bar into the center of the seal.
>
> Carefully pry the seal out of the injector body bore.
>
> Use care **not** to damage the injector body.
>
> ### Assemble
>
> Oil Seals, Roll pin retained load ring
>
> **CAUTION · Осторожно**
> Do not install the oil seal upside down. Failure to install the seal correctly will cause damage to the oil seal.
>
> The oil seal will fit on the tool tightly if installed correctly. The spring side of the oil seal, as shown, faces up when installed in the injector.
>
> Install a new oil seal onto the installation tool.
>
> With the new oil seal positioned on the tool, position the tool over the seal bore.
>
> Use the arbor press to gently place pressure onto the installation tool until the outer diameter face of the tool contacts the injector body.
>
> When properly installed, the seal height will **not** be flush with the injector body. The height will be approximately 0.5 mm \[0.020 in\] above the injector.
>
> Place the injector holding fixture with injector into the vise. Tighten the vise to hold the fixture in place.
>
> Install the load ring on the injector. Align the load ring capscrew hole end with the cutout on the injector fixture.
>
> Install a new roll pin into the load ring. By design, the roll pin holes are a different size on each side, so the roll pin **must** be installed in the correct direction, as illustrated.
>
> Use a 5/32 inch punch to gently tap the roll pin into both holes in the load ring. Continue driving the roll pin into the load ring until the pin is centered evenly in both holes and is an equal distance from both sides.
>
> Inspect the oil seal and plunger bore for debris. If debris is present, clean with a lint-free cloth.
>
> Clean the injector coupling spring with a lint-free cloth. Assemble the spring onto the load ring.
>
> Clean the plunger and coupling assembly with a lint-free cloth.
>
> Lubricate the plunger with clean calibration fluid.
>
> Slightly angle and rotate the upper plunger while installing the plunger into the oil seal.
>
> Hold the plunger vertically and rotate while installing the plunger into the injector bore.
>
> Use a flashlight to view through the coupling spring. Inspect the oil seal to verify the garter spring (1) is still in the correct location around the seal.
>
> Install the spring retainer bracket.
>
> Tighten the retainer capscrew.
>
> **Момент затяжки · Torque Value**
> 30 n•m [22 ft-lb]
>
> Install new injector o-rings.
>
> Oil Seals, Clip retained load ring
>
> **CAUTION · Осторожно**
> Do not install the oil seal upside down. Failure to install the seal correctly will cause damage to the oil seal.
>
> The oil seal will fit on the tool tightly, if installed correctly. The spring side of the oil seal, as shown, faces up when installed in the injector.
>
> Install a new oil seal onto the installation tool.
>
> With the new oil seal positioned on the tool, position the tool over the seal bore.
>
> Use the arbor press to gently place pressure onto the installation tool until the outer diameter face of the tool contacts the injector body.
>
> When properly installed, the seal height will **not** be flush with the injector body. The height will be approximately 0.5 mm \[0.020 in\] above the injector.
>
> Lubricate the plunger with clean calibration fluid.
>
> Carefully install the spring and load ring on the upper plunger.
>
> Holding the injector upright in one hand, slightly angle and rotate the upper plunger while installing the plunger into the oil seal.
>
> Hold the plunger vertically and rotate while installing the plunger into the injector bore.
>
> Use a flashlight to view through the coupling spring. Inspect the oil seal to verify the garter spring is still in the correct location around the seal.
>
> Place a clean, lint-free shop towel folded in quarters over the edge of a work bench.
>
> While holding the injector firmly in one hand, place the upper plunger against the outer edge of the work bench with the load ring just above the working surface of the bench.
>
> Lean in on the injector to partially compress the upper spring and plunger. Use care **not** to come in contact with the nozzle of the injector.
>
> Install the clip onto the injector load ring.
>
> Slowly, remove pressure from the injector, releasing the upper spring against the load ring.
>
> Install new injector o-rings.
>
> ### Install
>
> Use clean 15W-40 lubricating oil to lubricate the o-rings.
>
> **CAUTION · Осторожно**
> Make sure the injector hold down clamp is properly aligned before tightening the capscrew. It is possible for the clamp to contact a nearby ledge, and result in low clamp load.
>
> Install the injector into the cylinder head. Install the injector clamp and capscrew.
>
> Tighten the capscrew.
>
> **Момент затяжки · Torque Value**
> 80 n•m [59 ft-lb]
>
> Install the crossheads.
>
> ### Finishing Steps
>
> - Install and set the injector rocker lever and valve rocker lever assemblies. [[10-003-009-tr — Rocker Lever Assembly|Refer to Procedure 003-009 in Section 3.]]
> - Connect the engine brake solenoid wiring harness, if equipped. [[10-020-015 — Engine Brake Wiring Harness|Refer to Procedure 020-015 in Section 15.]]
> - Adjust the overhead set as needed. [[10-003-004-tr — Overhead Set|Refer to Procedure 003-004 in Section 3.]]
> - Install the rocker lever cover. Refer to Procedure 003-011 in Section 3.
> - Fill the cooling system. [[10-008-018-tr — Cooling System|Refer to Procedure 008-018 in Section 8.]]
> - Operate the engine to normal operating temperature and check for leaks.
>
> **Note · Примечание**
> If damage resulted in oil, excessive fuel, or excessive black smoke entering the exhaust system, the aftertreatment system **must** be inspected. Reference the Aftertreatment Diesel Oxidation Catalyst and Aftertreatment Diesel Particulate Filter Reuse Guidelines, Bulletin 4021600.
>
> **Note · Примечание**
> If the injector o-rings are being replaced due to an internal coolant leak, the crankcase breather element **must** be changed. [[101-003-019-tr — Crankcase Breather Element|Refer to Procedure 003-019 in Section 3.]]
>
> **Note · Примечание**
> If damage resulted in coolant entering the exhaust system, the aftertreatment system can be recovered. [[101-014-013-tr — Aftertreatment Testing|Refer to Procedure 014-013 in Section 14.]]
