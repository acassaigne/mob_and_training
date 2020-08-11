public class Game {
    public static final char FREE_TILE = ' ';
    public static final char O_PLAYER_SYMBOL = 'O';
    private char _lastSymbol = FREE_TILE;
    private NewSymbol _lastNewSymbol = NewSymbol.EMPTY;
    private Board _board = new Board();

    public void Play(char symbol, int x, int y) throws Exception {
        raiseIfFirstPlayerIsO(symbol);
        raiseIfSamePlayerPlaysTwice(symbol);
        RaiseIfTriesToPlayOnTakenTile(x, y);

        _lastSymbol = symbol;
        NewSymbol newSymbol = _board.convertToNewSymbol(symbol);
        _lastNewSymbol = newSymbol;
        _board.UpdateTileAt(symbol, x, y);
    }

    private void RaiseIfTriesToPlayOnTakenTile(int x, int y) throws Exception {
        if (_board.TileAt(x, y).newSymbol != NewSymbol.EMPTY) {
            throw new Exception("Invalid position");
        }
    }

    private void raiseIfSamePlayerPlaysTwice(char symbol) throws Exception {
        NewSymbol newSymbol = _board.convertToNewSymbol(symbol);
        if (newSymbol == _lastNewSymbol) {
            throw new Exception("Invalid next player");
        }
    }

    private void raiseIfFirstPlayerIsO(char symbol) throws Exception {
        if (_lastSymbol == FREE_TILE) {
            if (symbol == O_PLAYER_SYMBOL) {
                throw new Exception("Invalid first player");
            }
        }
    }

    private boolean isFullRow(int x) {
    return  _board.TileAt(x, 0).Symbol != FREE_TILE &&
            _board.TileAt(x, 1).Symbol != FREE_TILE &&
            _board.TileAt(x, 2).Symbol != FREE_TILE;
    }

    private boolean rowHasNonEmptyTile(int x) {
        return  _board.TileAt(x, 0).Symbol != FREE_TILE;
    }

    private boolean isTheSameSymbolForTheRow(int x) {
        return _board.TileAt(x, 0).Symbol == _board.TileAt(x, 1).Symbol &&
                _board.TileAt(x, 2).Symbol == _board.TileAt(x, 1).Symbol;
    }

    private char winnerSymbolForTheRow(int x) {
        if (isTheSameSymbolForTheRow(0)) {
            if (rowHasNonEmptyTile(0)) {
                return _board.TileAt(0, 0).Symbol;
            }
        }
        return FREE_TILE;
    }

    public char Winner() {
        char result;
        result = winnerSymbolForTheRow(0);

        if (isFullRow(1)) {
            if (isTheSameSymbolForTheRow(1)) {
                return _board.TileAt(1, 0).Symbol;
            }
        }

        if (isFullRow(2)) {
            if (isTheSameSymbolForTheRow(2)) {
                return _board.TileAt(2, 0).Symbol;
            }
        }

        return result;
    }
}

