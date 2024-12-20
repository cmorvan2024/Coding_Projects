$(function () {
    var squares = $(".cell"), 
        SIZE = 3,
        EMPTY = "",
        score,
        moves,
        turn = "X",

    wins = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ],

    /*
     * Resets the game state and clears the board.
     */
    startNewGame = function () {
        turn = "X";
        score = {"X": [], "O": []};
        moves = 0;
        squares.each(function () {
            $(this).text(EMPTY).removeClass("winner");
        });
        $("#message").text("Player X's turn");
    },

    /*
     * Checks whether the current player's moves match a winning combination.
     */
    win = function (currentPlayerMoves) {
        return wins.some(function (combo) {
            return combo.every(function (index) {
                return currentPlayerMoves.includes(index);
            });
        });
    },

    /*
     * Handles the logic when a cell is clicked.
     */
    set = function () {
        var $this = $(this);
        var cellIndex = $this.data("cell");

        if ($this.text() !== EMPTY) {
            return; // Ignore clicks on already-filled cells
        }

        $this.text(turn); // Mark the cell
        score[turn].push(cellIndex); // Track the move
        moves += 1;

        if (win(score[turn])) {
            $("#message").text(`Player ${turn} wins!`);
            score[turn].forEach(function (index) {
                squares.eq(index).addClass("winner");
            });
        } else if (moves === SIZE * SIZE) {
            $("#message").text("It's a tie!");
        } else {
            turn = turn === "X" ? "O" : "X";
            $("#message").text(`Player ${turn}'s turn`);
        }
    };

    /*
     * Attach click events to each cell and initialize the game.
     */
    squares.each(function () {
        $(this).on("click", set);
    });

    /*
     * Reset button functionality.
     */
    $("#resetButton").on("click", function () {
        startNewGame();
    });

    startNewGame();
});
