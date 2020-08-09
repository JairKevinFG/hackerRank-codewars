
function isSolved(board){
    for(let j = 0 ; j<board.length ; j++){
        if( board[j][0] == board[j][1] && board[j][0] == board[j][2] ) {
            if(board[j][0] !== 0){
                return board[j][0] 
            }
        }
        if( board[0][j] == board[1][j] && board[0][j] == board[2][j] ) {
            if( board[0][j] !== 0){
                return board[0][j]
            }
        }
    }   
    
    if(board[0][0] == board[1][1] && board[1][1] == board[2][2] ){
        if( board[0][0]  !== 0){
            return board[0][0]
        }
    }

    if(board[2][0] == board[1][1] && board[1][1] == board[0][2]){
        if( board[2][0] !== 0){
            return board[2][0]
        }
    }
    for (let i = 0 ; i< board.length ; i++){
        for(let k = 0 ; k<board.length ; k++){
            if(board[i][k] == 0){
                return -1
            }
        }
    }
    return 0
}

console.log(isSolved([[1,1,1],
                      [0,2,2],
                      [0,0,0]]))



