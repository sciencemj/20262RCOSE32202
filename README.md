# 20262RCOSE32202 — Game of Life (CLI)

터미널에서 실행되는 Conway's Game of Life 시뮬레이션. Python 3 표준 라이브러리만 사용.

## 실행

```bash
python3 -m life                  # 기본 프리셋(glider)
python3 -m life gosper-gun -W 50 -H 25
python3 -m life pulsar -d 0.2
python3 -m life --list           # 프리셋 목록
```

`Ctrl+C`로 종료.

## 옵션

| 옵션 | 설명 | 기본값 |
| --- | --- | --- |
| `preset` | 시작 패턴 | `glider` |
| `-W, --width` | 격자 너비 | 40 |
| `-H, --height` | 격자 높이 | 20 |
| `-d, --delay` | 세대 간 간격(초) | 0.1 |
| `-g, --generations` | N세대 후 정지 (0 = 무한) | 0 |
| `--no-wrap` | 가장자리를 감싸지 않음 | off |
| `--ascii` | 블록 문자 대신 `#` 사용 | off |
| `-l, --list` | 프리셋 목록 출력 | |

## 프리셋

blinker, glider, toad, beacon, pulsar, lwss, r-pentomino, diehard, acorn, gosper-gun

## 테스트

```bash
python3 -m unittest discover -s tests -t .
```
