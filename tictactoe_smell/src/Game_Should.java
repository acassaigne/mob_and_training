import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class Game_Should {
    private Game game;

    @Before
    public void InitializeGame(){
        game = new Game();
    }

    @Test(expected=Exception.class)
    public void NotAllowPlayerOToPlayFirst() throws Exception {
        game.PlayNewSymbol(NewSymbol.PLAYER_O, 0, 0);
    }

    @Test(expected=Exception.class)
    public void NotAllowPlayerXToPlayTwiceInARow() throws Exception
    {
        game.PlayNewSymbol(NewSymbol.PLAYER_X, 0, 0);
        game.PlayNewSymbol(NewSymbol.PLAYER_X, 1, 0);
    }

    @Test(expected=Exception.class)
    public void NotAllowPlayerToPlayInLastPlayedPosition() throws Exception
    {
        game.PlayNewSymbol(NewSymbol.PLAYER_X, 0, 0);
        game.PlayNewSymbol(NewSymbol.PLAYER_O, 0, 0);

    }

    @Test(expected=Exception.class)
    public void NotAllowPlayerToPlayInAnyPlayedPosition() throws Exception
    {
        game.PlayNewSymbol(NewSymbol.PLAYER_X, 0, 0);
        game.PlayNewSymbol(NewSymbol.PLAYER_O, 1, 0);
        game.PlayNewSymbol(NewSymbol.PLAYER_X, 0, 0);
    }

    @Test
    public void DeclarePlayerXAsAWinnerIfThreeInTopRow() throws Exception
    {
        game.PlayNewSymbol(NewSymbol.PLAYER_X, 0, 0);
        game.PlayNewSymbol(NewSymbol.PLAYER_O, 1, 0);
        game.PlayNewSymbol(NewSymbol.PLAYER_X, 0, 1);

        game.PlayNewSymbol(NewSymbol.PLAYER_O, 1, 1);
        game.PlayNewSymbol(NewSymbol.PLAYER_X, 0, 2);
        NewSymbol winner_2 = game.Winner_2();
        assertEquals(NewSymbol.PLAYER_X, winner_2);

//        game.Play('X', 0, 0);
//        game.Play('O', 1, 0);
//        game.Play('X', 0, 1);
//
//        game.Play('O', 1, 1);
//        game.Play('X', 0, 2);

        //char winner = game.Winner();

       // assertEquals('X', winner);
    }


//    @Test
//    public void bugTracking() throws Exception {
//        game.PlayNewSymbol(NewSymbol.PLAYER_X, 0, 0);
//        game.PlayNewSymbol(NewSymbol.PLAYER_O, 1, 0);
//        assertEquals(game._board, winner);
//    }

    @Test
    public void DeclarePlayerOAsAWinnerIfThreeInTopRow() throws Exception
    {
        game.Play('X', 2, 2);
        game.Play('O', 0, 0);
        game.Play('X', 1, 0);
        game.Play('O', 0, 1);
        game.Play('X', 1, 1);
        game.Play('O', 0, 2);

        char winner = game.Winner();

        assertEquals('O', winner);
    }

    @Test
    public void DeclarePlayerXAsAWinnerIfThreeInMiddleRow() throws Exception
    {
        game.Play('X', 1, 0);
        game.Play('O', 0, 0);
        game.Play('X', 1, 1);
        game.Play('O', 0, 1);
        game.Play('X', 1, 2);

        char winner = game.Winner();

        assertEquals('X', winner);
    }

    @Test
    public void DeclarePlayerOAsAWinnerIfThreeInMiddleRow() throws Exception
    {
        game.Play('X', 0, 0);
        game.Play('O', 1, 0);
        game.Play('X', 2, 0);
        game.Play('O', 1, 1);
        game.Play('X', 2, 1);
        game.Play('O', 1, 2);

        char winner = game.Winner();

        assertEquals('O', winner);
    }

    @Test
    public void DeclarePlayerXAsAWinnerIfThreeInBottomRow() throws Exception
    {
        game.Play('X', 2, 0);
        game.Play('O', 0, 0);
        game.Play('X', 2, 1);
        game.Play('O', 0, 1);
        game.Play('X', 2, 2);

        char winner = game.Winner();

        assertEquals('X', winner);
    }

    @Test
    public void DeclarePlayerOAsAWinnerIfThreeInBottomRow() throws Exception
    {
        game.Play('X', 0, 0);
        game.Play('O', 2, 0);
        game.Play('X', 1, 0);
        game.Play('O', 2, 1);
        game.Play('X', 1, 1);
        game.Play('O', 2, 2);

        char winner = game.Winner();

        assertEquals('O', winner);
    }
}
