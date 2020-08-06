
public class Tile
{
    public static final char EMPTY_TILE = ' ';
    public int X;
    public int Y;
    public char Symbol= EMPTY_TILE;

    Tile(int rowNumber, int columnNumber) {
        X = rowNumber;
        Y = columnNumber;
    }

    public void SetSymbol(char NewSymbol) {
        Symbol = NewSymbol;
    }

}