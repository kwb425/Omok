[![tag][a]][1]
[![release][b]][2]
[![download][c]][3]
# Table of Contents <a name="anchor_main"></a>
---
1. [omok.py](#anchor_1) <br></br>
2. [Static Variables](#anchor_2) <br></br>
3. [Calculation Functions](#anchor_3) <br></br>
4. [Play Functions](#anchor_4) <br></br>
5. [References](#anchor_5) <br></br>

## omok.py <a name="anchor_1"></a> [top](#anchor_main)
* Wrapper, below will cover contents of it.

## Static Variables <a name="anchor_2"></a> [top](#anchor_main)
* Static vaiables (value fixed) <-> Dynamic variables (value changes, thus feeded into the functions as their arguments)
* Stones part; Allocating stones to each player
* Board size & Total number of spaces in that board part; Literally...
* Rows & Columns & Diagonals part; Names & Indices of the rows, columns, and diagonals are verified.

## Calculation Functions <a name="anchor_3"></a> [top](#anchor_main)
* Coordinates control part; Transitioning user input (e.g., A1, B4, C8, ...) into computational unit (e.g., 1, 2, 3, 4, 5, 6, ...)
* The weighting part; Calculating the weights so that the computer can put a best defensive stone in collaboration with Surrounding indices part
* Surrounding indices part; This function returns a box that wraps a point where the user has put his (her) stone lately. The boxing can be single fenced, or double fenced (see code for detail.).
* Human -> Computer part; One round

## Play Functions <a name="anchor_4"></a> [top](#anchor_main)
* Displays part; Displaying current state of the board.
* Win & Lose & Draw part; Keeping the game until a winner (loser) comes up (or just a draw)
* Main part; Diplay -> Initialization & Play -> Win? -> Display -> Initialization & Play -> Win? -> Display -> Initialization & Play -> Win? -> ...

## References <a name="anchor_5"></a> [top](#anchor_main)
Please check Git repo for [latest update][4]

Please send any questions to: <kwb425@icloud.com>

<!--Links to addresses, reference Markdowns-->
[1]: https://github.com/kwb425/Omok/tags
[2]: https://github.com/kwb425/Omok/releases
[3]: https://github.com/kwb425/Omok/releases
[4]: https://github.com/kwb425/Omok.git
<!--Links to images, reference Markdowns-->
[a]: https://img.shields.io/badge/Tag-v1.3-red.svg?style=plastic
[b]: https://img.shields.io/badge/Release-v1.3-green.svg?style=plastic
[c]: https://img.shields.io/badge/Download-Click-blue.svg?style=plastic