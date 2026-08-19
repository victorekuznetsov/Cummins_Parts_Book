---
aliases:
  - "Процедуры и методы поиска неисправностей"
type: "Процедура"
doc: "99-t00-001-tr"
title_en: "Troubleshooting Procedures and Techniques"
title_ru: "Процедуры и методы поиска неисправностей"
modified: "2013-09-18"
engines:
  - "37292556"
  - "37295879"
  - "41343322"
  - "41349633"
  - "93058669"
families:
  - "C8.3 · 6C8.3"
  - "NT/NTA855 · ISM/QSM11"
  - "QSK19"
  - "QST30"
manuals:
  - "3666003"
  - "3666121"
  - "3666184"
  - "3666214"
  - "3666231"
  - "3666266"
  - "4021419"
  - "4021442"
  - "4021592"
  - "4021674"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-t00-001-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-t00-001-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "двигатель/NT/NTA855"
  - "двигатель/QSK19"
  - "двигатель/QST30"
  - "группа/99"
  - "перевод/машинный"
---

# Troubleshooting Procedures and Techniques
**Процедуры и методы поиска неисправностей**

> [!abstract] Процедура · `99-t00-001-tr`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3, NT/NTA855 · ISM/QSM11, QSK19, QST30
> **Входит в руководства:** [[3666003 — C Troubleshooting and Repair Manual|3666003]], [[3666121 — Holset® Air Compressors Master Repair Manual|3666121]], [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]], [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]], [[3666231 — Centinel™ Master Repair Manual|3666231]], [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]], [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]], [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]], [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual|4021592]], [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TS - Troubleshooting Symptoms · Section TS — Troubleshooting Symptoms
> **Даты:** изменён 2013-09-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-t00-001-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-t00-001-tr.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Тщательный анализ жалобы клиента является ключом к успешному устранению неполадок. Чем больше информации известно о жалобе, тем быстрее и проще можно решить проблему.

Симптомы устранения неполадок организованы таким образом, чтобы проблема могла быть обнаружена и исправлена, сначала выполнив самые простые и логичные действия. Заполните все шаги в последовательности, показанной сверху вниз.

Невозможно включить все решения проблем, которые могут возникнуть; однако эти диаграммы предназначены для стимулирования мыслительного процесса, который приведет к причине и исправлению проблемы.

Следуйте этим основным шагам устранения неполадок:

- Получить все факты, касающиеся жалобы
- Проанализируйте проблему тщательно
- Относитесь к симптомам основных систем двигателя и компонентов
- Рассмотрите любые недавние действия по техническому обслуживанию или ремонту, которые могут относиться к жалобе.
- Двойная проверка перед началом любой разборки
- Решите проблему, используя диаграммы симптомов и сначала сделайте самые простые вещи.
- Определите причину проблемы и сделайте тщательный ремонт
- После того, как был сделан ремонт, используйте двигатель, чтобы убедиться, что причина жалобы была исправлена.


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> A thorough analysis of the customer's complaint is the key to successful troubleshooting. The more information known about a complaint, the faster and easier the problem can be solved.
>
> The Troubleshooting Symptom Charts are organized so that a problem can be located and corrected by doing the easiest and most logical things first. Complete all steps in the sequence shown from top to bottom.
>
> It is **not** possible to include all the solutions to problems that can occur; however, these charts are designed to stimulate a thought process that will lead to the cause and correction of the problem.
>
> Follow these basic troubleshooting steps:
>
> - Get all the facts concerning the complaint
> - Analyze the problem thoroughly
> - Relate the symptoms to the basic engine systems and components
> - Consider any recent maintenance or repair action that can relate to the complaint
> - Double-check before beginning any disassembly
> - Solve the problem by using the symptom charts and doing the easiest things first
> - Determine the cause of the problem and make a thorough repair
> - After repairs have been made, operate the engine to make sure the cause of the complaint has been corrected
