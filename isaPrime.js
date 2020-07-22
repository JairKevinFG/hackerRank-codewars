function isPrime(num){
    let valor = true
    if(num == 2){
        valor= true 
    }
    else if (num <2 || num % 2 == 0 ){
        valor = false
    } 
    for(let i = 3 ; i<=num**0.5; i++){
        if(num % i == 0){
            valor = false
            break
        }
    }
    return valor

}

console.log(isPrime(2))