function zeros(n) {
    let zs = 0 
    while(n>0){
        n = Math.floor(n/5)
        zs = n + zs
    }

    return zs
}


console.log(zeros(8))