import java.util.ArrayList;
import java.util.List;

public class Board
{
    private List<Tile> _plays = new ArrayList<>();

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
            Tile tile = new Tile();
            tile.X = rowNumber;
            tile.Y = columnNumber;
            _plays.add(tile);
        }
    }

    public Tile TileAt(int x, int y)
    {
        for (Tile t : _plays) {
            if (t.X == x && t.Y == y){
                return t;
            }
        }
        return null;
    }

    public void UpdateTileAt(char symbol, int x, int y)
    {
        
        TileAt(x,y).Symbol = symbol;
    }
}