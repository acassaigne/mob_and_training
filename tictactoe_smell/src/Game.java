public class Game {
    public static final char O_PLAYER_SYMBOL = 'O';
    private Symbol _lastSymbol = Symbol.EMPTY;
    private Board _board = new Board();

    public void Play(char symbol, int x, int y) throws Exception {
        raiseIfFirstPlayerIsO(symbol);
        raiseIfSamePlayerPlaysTwice(symbol);
        RaiseIfTriesToPlayOnTakenTile(x, y);

        Symbol newSymbol = _board.convertToNewSymbol(symbol);
        _lastSymbol = newSymbol;
        _board.UpdateTileAt(symbol, x, y);
    }


    private void RaiseIfTriesToPlayOnTakenTile(int x, int y) throws Exception {
        if (_board.TileAt(x, y).symbol != Symbol.EMPTY) {
            throw new Exception("Invalid position");
        }
    }

    private void raiseIfSamePlayerPlaysTwice(char symbol) throws Exception {
        Symbol newSymbol = _board.convertToNewSymbol(symbol);
        if (newSymbol == _lastSymbol) {
            throw new Exception("Invalid next player");
        }
    }

    private void raiseIfFirstPlayerIsO(char symbol) throws Exception {
        if (_lastSymbol == Symbol.EMPTY) {
            if (symbol == O_PLAYER_SYMBOL) {
                throw new Exception("Invalid first player");
            }
        }
    }


    private boolean isFullRow_2(int x) {
        return  _board.TileAt(x, 0).symbol != Symbol.EMPTY &&
                _board.TileAt(x, 1).symbol != Symbol.EMPTY &&
                _board.TileAt(x, 2).symbol != Symbol.EMPTY;
    }

    private boolean rowHasNonEmptyTile(int x) {
        return  _board.TileAt(x, 0).symbol != Symbol.EMPTY;
    }


    private boolean isTheSameSymbolForTheRow(int x) {
        return _board.TileAt(x, 0).symbol == _board.TileAt(x, 1).symbol &&
                _board.TileAt(x, 2).symbol == _board.TileAt(x, 1).symbol;
    }



    private Symbol winnerSymbolForTheRow(int x) {
        if (isTheSameSymbolForTheRow(0)) {
            if (rowHasNonEmptyTile(0)) {
                return _board.TileAt(0, 0).symbol;
            }
        }
        return Symbol.EMPTY;
    }

    public char Winner() {
        return Winner_2();
    }


    public char Winner_2() {
        Symbol result;
        result = winnerSymbolForTheRow(0);

        if (isFullRow_2(1)) {
            if (isTheSameSymbolForTheRow(1)) {
                return _board.convertNewSymbolToChar(_board.TileAt(1, 0).symbol);
            }
        }

        if (isFullRow_2(2)) {
            if (isTheSameSymbolForTheRow(2)) {
                return _board.convertNewSymbolToChar(_board.TileAt(2, 0).symbol);
            }
        }

        return _board.convertNewSymbolToChar(result);
    }
}
