function zeros(n) {
    let total = 1
    for (i=1 ; i<=n; i++){
        total = total * i
    }
    console.log(total)
    let newtotal = total.toLocaleString().split('')
    return  newtotal
}


console.log(zeros(100))