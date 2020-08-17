
public class Tile
{
    public int X;
    public int Y;
    public Symbol symbol = Symbol.EMPTY;

    Tile(int rowNumber, int columnNumber) {
        X = rowNumber;
        Y = columnNumber;
    }


    public void SetNewSymbol(Symbol symbol) {
        this.symbol = symbol;
    }

}