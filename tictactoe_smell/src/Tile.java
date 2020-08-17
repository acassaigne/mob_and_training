
public class Tile
{
    public static final char EMPTY_TILE = ' ';
    public int X;
    public int Y;
    public NewSymbol newSymbol = NewSymbol.EMPTY;

    Tile(int rowNumber, int columnNumber) {
        X = rowNumber;
        Y = columnNumber;
    }


    public void SetNewSymbol(NewSymbol newSymbol) {
        this.newSymbol = newSymbol;
    }

}