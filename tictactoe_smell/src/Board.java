import java.util.ArrayList;
import java.util.List;

public class Board
{
    private List<Tile> tiles = new ArrayList<>();

    public Board()
    {
        for (int rowNumber = 0; rowNumber < 3; rowNumber++)
        {
            InitRow(rowNumber);
        }
    }

    private void InitRow(int rowNumber) {
        for (int columnNumber = 0; columnNumber < 3; columnNumber++)
        {
            tiles.add(new Tile(rowNumber, columnNumber));
        }
    }

    public Tile TileAt(int x, int y)
    {
        for (Tile ATile : tiles) {
            if (ATile.X == x && ATile.Y == y){
                return ATile;
            }
        }
        return null;
    }

    public void UpdateTileAt(char symbol, int x, int y)
            //introduire NewSymbol
    {
        TileAt(x,y).SetSymbol(symbol);
    }
}