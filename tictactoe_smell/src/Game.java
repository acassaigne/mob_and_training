public class Game {
    private char _lastSymbol = ' ';
    private Board _board = new Board();

    public void Play(char symbol, int x, int y) throws Exception {
        raiseIfFirstPlayerIsO(symbol);
        raiseIfSamePlayerPlaysTwice(symbol);
        RaiseIfTriesToPlayOnTakenTile(x, y);

        _lastSymbol = symbol;
        _board.UpdateTileAt(symbol, x, y);
    }

    private void RaiseIfTriesToPlayOnTakenTile(int x, int y) throws Exception {
        if (_board.TileAt(x, y).Symbol != ' ') {
            throw new Exception("Invalid position");
        }
    }

    private void raiseIfSamePlayerPlaysTwice(char symbol) throws Exception {
        if (symbol == _lastSymbol) {
            throw new Exception("Invalid next player");
        }
    }

    private void raiseIfFirstPlayerIsO(char symbol) throws Exception {
        if (_lastSymbol == ' ') {
            if (symbol == 'O') {
                throw new Exception("Invalid first player");
            }
        }
    }

    public char Winner() {
        //if the positions in first row are taken
        if (_board.TileAt(0, 0).Symbol != ' ' &&
                _board.TileAt(0, 1).Symbol != ' ' &&
                _board.TileAt(0, 2).Symbol != ' ') {
            //if first row is full with same symbol
            if (_board.TileAt(0, 0).Symbol ==
                    _board.TileAt(0, 1).Symbol &&
                    _board.TileAt(0, 2).Symbol == _board.TileAt(0, 1).Symbol) {
                return _board.TileAt(0, 0).Symbol;
            }
        }

        //if the positions in first row are taken
        if (_board.TileAt(1, 0).Symbol != ' ' &&
                _board.TileAt(1, 1).Symbol != ' ' &&
                _board.TileAt(1, 2).Symbol != ' ') {
            //if middle row is full with same symbol
            if (_board.TileAt(1, 0).Symbol ==
                    _board.TileAt(1, 1).Symbol &&
                    _board.TileAt(1, 2).Symbol ==
                            _board.TileAt(1, 1).Symbol) {
                return _board.TileAt(1, 0).Symbol;
            }
        }

        //if the positions in first row are taken
        if (_board.TileAt(2, 0).Symbol != ' ' &&
                _board.TileAt(2, 1).Symbol != ' ' &&
                _board.TileAt(2, 2).Symbol != ' ') {
            //if middle row is full with same symbol
            if (_board.TileAt(2, 0).Symbol ==
                    _board.TileAt(2, 1).Symbol &&
                    _board.TileAt(2, 2).Symbol ==
                            _board.TileAt(2, 1).Symbol) {
                return _board.TileAt(2, 0).Symbol;
            }
        }

        return ' ';
    }
}

