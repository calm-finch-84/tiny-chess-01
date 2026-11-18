# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/calm-finch-84/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/calm-finch-84/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in at most 4,096 bytes of Python, built for the make.fun
tiny-chess-01 bounty.

`main.py` is the whole engine: a negamax search with alpha-beta pruning,
quiescence search, a transposition table, null-move pruning, check
extensions and a tapered piece-square-table evaluation, packed as an
lzma-compressed payload with a small self-extracting stub (3,819 bytes).
Search is bounded by a fixed node count only, so every move is derived
deterministically from the position.

`pack.py` is the packaging script that produced `main.py` from the
readable engine source; the payload decompresses byte-for-byte to that
source.
