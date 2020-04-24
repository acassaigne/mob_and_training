 wc -l test_tictactoe.py                                                                                                                                                                                                                                                   
247 test_tictactoe.py                                                                                                                                                                                                                                                                                                         

Avant refacto SetofSetMarks
 wc -l test_tictactoe_calisthenics.py tictactoe_other.py                                                                                                                                                                                                                   
 219 test_tictactoe_calisthenics.py                                                                                                                                                                                                                                                                                           
  50 tictactoe_other.py                                                                                                                                                                                                                                                                                                       
 269 total                 
 
 Après refacto 
  258 test_tictactoe_calisthenics.py
  50 tictactoe_other.py
 308 total

 
 # TODO
 Finir refacto SetofSetofMarks for Row and Columns in Board Class                                                                                                
 
 # Game of Life
 «The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, 
 each of which is in one of two possible states: alive or dead (or populated and unpopulated, respectively). 
 Every cell interacts with its eight neighbors, which are the cells that are horizontally, 
 vertically or diagonally adjacent. At each step in time, the following transitions occur:
 
 - Any live cell with fewer than two live neighbors dies, as if by under population.
 - Any live cell with two or three live neighbors lives on to the next generation.
 - Any live cell with more than three live neighbors dies, as if by overpopulation.
 - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
 