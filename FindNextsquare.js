const c = console.log
function findNextSquare(sq){
    const square = Math.sqrt(sq)
    if (square === Math.ceil(square)){
        const newSquare = square + 1 
        return Math.pow(newSquare,2)
    }else{
        return - 1
    }


}

c(findNextSquare(625))

