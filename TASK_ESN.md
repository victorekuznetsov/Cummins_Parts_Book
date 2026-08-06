# Задача: каталоги Cummins по списку машин

Полный список из задания (модель · VIN · серийный номер ДВС · доступность в EPC).
Каталог качается **по одному ESN на CPL** (`tools/check_esn.py esn_list.txt`).

Серийники с буквами (SG21-C6, BHL4CX, SE420LCW) регуляркой `check_esn.py`
не разбираются — проверять их отдельным запросом к API по полному ESN.

| Модель | VIN | Серийный ДВС | EPC |
|---|---|---|---|
| SG21-C6 AWD | CHSGA21APRC001781 | 1024E008268 | Да |
| SG21-C6 AWD | CHSGA21APRC002008 | 1024H015347 | Да |
| SD90-C5 | CHSDA90ANRC000035 | 37292556 | Только PDF |
| SD90-C5 | CHSDA90ANRC000042 | 37292733 | Да |
| SD90-C5 | CHSDA90ANRC000026 | 37290615 | Да |
| SD90-C5 | CHSDA90ANRC000027 | 37290487 | Да |
| SD90-C5 | CHSDA90ANRC000050 | 37293376 | Да |
| SD90-C5 | CHSDA90ANRC000045 | 37293549 | Да |
| SD90-C5 | CHSDA90ANRC000043 | 37292731 | Да |
| SD90-C5 | CHSDA90ANRC000049 | 37293377 | Да |
| SD90-C5 | CHSDA90ANRC000048 | 37293410 | Да |
| SD90-C5 | CHSDA90ANRC000044 | 37293592 | Да |
| SD60-C5 | CHSDA60ALPC000163 | 41349704 | Да |
| SD60-C5 | CHSDA60ACRC000252 | 41353297 | Да |
| SD60-C5 | CHSDA60ACRC000257 | 41369708 | Да |
| SD60-C5 | CHSDA60AHRC000250 | 41351859 | Да |
| SD34-B3 | CHSDA34AVPB009067 | 41354422 | Да |
| BHL4CX | SBH388H20251278 | 4P25J004736 | Только PDF |
| SE420LCW | 66SE42EWNR0000159 | 7524A001078 | Только PDF |
| SG21A-3 | CHSGA21AVNB001320 | 93058669 | Только PDF |
| SG21A-3 | CHSGA21AHNB001337 | 93065419 | Только PDF |
| SG21A-3 | CHSGA21AENB001338 | 93087701 | Только PDF |
| DH46C3 RS | CHSDH46HNPC000021 | 85201236 | Только PDF |
| DH46C3 RS | CHSDH46HNPC000019 | 80201235 | Только PDF |
| SD32 | CHSD32AAJP1008576 | 41343322 | Только PDF |
| SE420LCW | 66SE42EWNR0000219 | 7524A001060 | Только PDF |
| SD60-C5 | CHSDA60AERC000220 | 41349633 | Да |
| SD60-C5 | CHSDA60AERC000203 | 41356585 | Да |
| SD60-C5 | CHSDA60ATRC000186 | 41348302 | Да |
| SD60-C5 | CHSDA60AVRC000227 | 41353280 | Да |
| SD60-C5 | CHSDA60AESC000322 | 41384184 | Да |
| SD60-C5 | CHSDA60AVSC000346 | 41383427 | Да |
| SD34-B3 | CHSDA34APRB009728 | 41370103 | Да |
| SD34-B3 | CHSDA34AJRB009585 | 41365967 | Да |
| SD34-B3 | CHSDA34ATRB009582 | 41364976 | Да |
| SD34-B3 | CHSDA34AHRB009612 | 41365979 | Да |
| SD34-B3 | CHSDA34ALRB009740 | 41370102 | Да |
| SD34-B3 | CHSDA34AVRB009606 | 41365971 | Да |
| SD34-B3 | CHSDA34AARB009655 | 41367668 | Да |
| SD34-B3 | CHSDA34ACRB009645 | 41367681 | Да |
| SD34-B3 | CHSDA34APRB009633 | 41365996 | Да |
| SD34-B3 | CHSDA34AARB009638 | 41365012 | Да |
| SD34-B3 | CHSDA34ALRB009723 | 41365025 | Да |
| SD34-B3 | CHSDA34AERB009613 | 41366000 | Да |
| SD60-C5 | CHSDA60APPC000137 | 41348289 | Да |
| SD60-C5 | CHSDA60AKPC000138 | 41348295 | Да |
| SD60-C5 | CHSDA60ATPC000136 | 41348156 | Да |
| SD60-C5 | CHSDA60APPC000140 | 41348307 | Да |
| SD60-C5 | CHSDA60AJRC000239 | 41351021 | Да |
| SD60-C5 | CHSDA60AKRC000210 | 41353290 | Да |
| SD60-C5 | CHSDA60AEPC000182 | 41349698 | Только PDF |

## Серийники с буквами (проверять отдельно)

```
1024E008268  1024H015347  4P25J004736  7524A001078  7524A001060
```

## Статус выгрузки

- `37292556` (SD90-C5 / QST30) — уже выгружен в прошлой сессии.
- `33239899` (QSK50 / NTE200) — уже выгружен в прошлой сессии.
- Остальные — ждут открытия сетевого доступа к `parts.cummins.com`
  (в текущем окружении egress-политика отвечает 403 на CONNECT к этому хосту).

## После открытия доступа

```
python tools/check_esn.py esn_list.txt          # группировка по CPL
# затем по каждому представителю CPL:
python crawler.py <ESN>
python crawl_details.py <ESN> --workers 8
python tools/build_catalog.py <ESN> --machine <машина> --fleet-from esn_report.json
```
