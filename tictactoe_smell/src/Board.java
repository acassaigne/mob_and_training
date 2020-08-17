import java.util.ArrayList;
import java.util.List;

public class Board {
    private List<Tile> tiles = new ArrayList<>();

    public Board() {
        for (int rowNumber = 0; rowNumber < 3; rowNumber++) {
            InitRow(rowNumber);
        }
    }

    private void InitRow(int rowNumber) {
        for (int columnNumber = 0; columnNumber < 3; columnNumber++) {
            tiles.add(new Tile(rowNumber, columnNumber));
        }
    }

    public Tile TileAt(int x, int y) {
        for (Tile ATile : tiles) {
            if (ATile.X == x && ATile.Y == y) {
                return ATile;
            }
        }
        return null;
    }

    public void UpdateTileAt(char symbol, int x, int y)
    {
        Symbol newSymbol = convertToNewSymbol(symbol);
        TileAt(x, y).SetNewSymbol(newSymbol);
    }


    public Symbol convertToNewSymbol(char symbol) {
        Symbol newSymbol = Symbol.EMPTY;
        if (symbol == 'O') {
            newSymbol = Symbol.PLAYER_O;
        }
        if (symbol == 'X') {
            newSymbol = Symbol.PLAYER_X;
        }
        return newSymbol;
    }

    public char convertNewSymbolToChar(Symbol symbol) {
        if (symbol == Symbol.PLAYER_O) {
            return 'O';
        }
        if (symbol == Symbol.PLAYER_X) {
            return 'X';
        }
        return ' ';
    }

}