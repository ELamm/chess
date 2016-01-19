# chess
code to represent and analyze chess games and players

run python script with args:
1 fileName.pgn (name of pgn file)
2 gameNumber (game index in the pgn file that you want, starting at 0)
3 moveNumber (move of game to look at)
4 sideToMove ('W' or 'B' for white or black)

program will print a crude chess board to standard output of the game board

example:
python importPGNs.py testPGN.pgn 1 20 B

prints the second game in the pgn file testPGN.pgn immediately after black's move 20 (Qa5+)
(Here Capablanca, playing black, has put Alekhine in check with his queen)
