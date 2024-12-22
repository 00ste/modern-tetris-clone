# Wall Kicks

SRS has super wallkicks. Unlike most rotation systems with super kicks, these wall kicks are relatively modest. When the player attempts to rotate a tetromino, but the position it would normally occupy after basic rotation is obstructed, (either by the wall or floor of the playfield, or by the stack), the game will attempt to "kick" the tetromino into an alternative position nearby. Some points to note:

- When a rotation is attempted, 5 positions are sequentially tested (inclusive of basic rotation); if none are available, the rotation fails completely.

- Which positions are tested is determined by the initial rotation state, and the desired final rotation state. Because it is possible to rotate both clockwise and counter-clockwise, for each of the 4 initial states there are 2 final states. Therefore there are a total of 8 possible rotations for each tetromino and 8 sets of wall kick data need to be described.
    
- The positions are commonly described as a sequence of (x, y) kick values representing translations relative to basic rotation; a convention of positive x rightwards, positive y upwards is used, e.g. (-1, 2) would indicate a kick of 1 cell left and 2 cells up.
    
- The J, L, T, S, and Z tetrominoes all share the same kick values, the I tetromino has its own set of kick values, and the O tetromino does not kick.
    
- Several different conventions are commonly used for the naming of the rotation states. On this page, the following convention will be used:
    - 0 = spawn state
    - 1 = state resulting from a clockwise rotation ("right") from spawn
    - 2 = state resulting from 2 successive rotations in either direction from spawn.
    - 3 = state resulting from a counter-clockwise ("left") rotation from spawn


J, L, T, S, Z Tetromino Wall Kick Data

        Test 1 	        Test 2 	        Test 3 	        Test 4 	        Test 5
0>>1    basic rotation 	(-1, 0) 	(-1, 1) 	( 0,-2)¹ 	(-1,-2)
1>>0 	basic rotation 	( 1, 0) 	( 1,-1) 	( 0, 2) 	( 1, 2)
1>>2 	basic rotation 	( 1, 0) 	( 1,-1) 	( 0, 2) 	( 1, 2)
2>>1 	basic rotation 	(-1, 0) 	(-1, 1)¹ 	( 0,-2) 	(-1,-2)
2>>3 	basic rotation 	( 1, 0) 	( 1, 1)¹ 	( 0,-2) 	( 1,-2)
3>>2 	basic rotation 	(-1, 0) 	(-1,-1) 	( 0, 2) 	(-1, 2)
3>>0 	basic rotation 	(-1, 0) 	(-1,-1) 	( 0, 2) 	(-1, 2)
0>>3 	basic rotation 	( 1, 0) 	( 1, 1) 	( 0,-2)¹ 	( 1,-2)

J, L, T, S, Z Tetromino Wall Kick Data (project)

        Test 1 	        Test 2 	        Test 3 	        Test 4 	        Test 5
0>>3    basic rotation 	(-1, 0) 	(-1,-1) 	( 0, 2)¹ 	(-1, 2)
3>>0 	basic rotation 	( 1, 0) 	( 1, 1) 	( 0,-2) 	( 1,-2)
3>>2 	basic rotation 	( 1, 0) 	( 1, 1) 	( 0,-2) 	( 1,-2)
2>>3 	basic rotation 	(-1, 0) 	(-1,-1)¹ 	( 0, 2) 	(-1, 2)
2>>1 	basic rotation 	( 1, 0) 	( 1,-1)¹ 	( 0, 2) 	( 1, 2)
1>>2 	basic rotation 	(-1, 0) 	(-1, 1) 	( 0,-2) 	(-1,-2)
1>>0 	basic rotation 	(-1, 0) 	(-1, 1) 	( 0,-2) 	(-1,-2)
0>>1 	basic rotation 	( 1, 0) 	( 1,-1) 	( 0, 2)¹ 	( 1, 2)


I Tetromino Wall Kick Data
        Test 1 	        Test 2 	        Test 3 	        Test 4 	        Test 5
0>>1 	basic rotation 	(-2, 0) 	( 1, 0) 	(-2,-1) 	( 1, 2)
1>>0 	basic rotation 	( 2, 0) 	(-1, 0) 	( 2, 1) 	(-1,-2)
1>>2 	basic rotation 	(-1, 0) 	( 2, 0) 	(-1, 2) 	( 2,-1)
2>>1 	basic rotation 	( 1, 0) 	(-2, 0) 	( 1,-2) 	(-2, 1)
2>>3 	basic rotation 	( 2, 0) 	(-1, 0) 	( 2, 1) 	(-1,-2)
3>>2 	basic rotation 	(-2, 0) 	( 1, 0) 	(-2,-1) 	( 1, 2)
3>>0 	basic rotation 	( 1, 0) 	(-2, 0) 	( 1,-2) 	(-2, 1)
0>>3 	basic rotation 	(-1, 0) 	( 2, 0) 	(-1, 2) 	( 2,-1)

¹ This kick is impossible with the t-tetrimino because if it fits, basic rotation fits too, so basic rotation is used. 

[text](https://www.four.lol/srs/kicks-overview)
