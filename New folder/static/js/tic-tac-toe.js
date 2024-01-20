//restart game button
var restart = document.querySelector("#ng");

// grabs all the squares
var squares = document.querySelectorAll('td');
//clear all the squares
function clearBoard(){
    for (var i = 0; i < squares.length; i++){
        squares[i].textContent = '';
        squares[i].style.color = ''; // Reset the color
    }
}
restart.addEventListener('click',clearBoard);

//for loop to add event listeners to all the squares
for (var i = 0; i < squares.length; i++) {
    squares[i].addEventListener('click', function() {
        if (this.textContent === '') {
            this.textContent = 'X';
        } else if (this.textContent === 'X') {
            this.textContent = 'O';
        }
        else {
            this.textContent = '';
        }
        checkWin(); // Check for a win after each move
    });
}

function checkWin() {
    // Define winning combinations
    var winningCombinations = [
        [0, 1, 2], // Top row
        [3, 4, 5], // Middle row
        [6, 7, 8], // Bottom row
        [0, 3, 6], // Left column
        [1, 4, 7], // Middle column
        [2, 5, 8], // Right column
        [0, 4, 8], // Diagonal from top-left to bottom-right
        [2, 4, 6]  // Diagonal from top-right to bottom-left
    ];

    // Check for a win
    for (var i = 0; i < winningCombinations.length; i++) {
        var combination = winningCombinations[i];
        var a = squares[combination[0]].textContent;
        var b = squares[combination[1]].textContent;
        var c = squares[combination[2]].textContent;

        if (a === b && b === c && a !== '') {
            // Set the color to green for all squares in the winning combination
            for (var j = 0; j < combination.length; j++) {
                squares[combination[j]].style.color = 'green';
            }
        } else {
            // Set the color to red for the unmatched squares
            for (var j = 0; j < combination.length; j++) {
                squares[combination[j]].style.color = 'red';
            }
        }
    }
}
