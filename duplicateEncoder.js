function duplicateEncode(word){
    let count = {}
    const letters = word.toLowerCase().split('')
    console.log(letters)
    letters.forEach(el => {
        return count[el] = (count[el] || 0 ) + 1
    })
    const str = letters.map(el => {
        return count[el] === 1 ?  '(' : ')'
    }).join('')
    return str

}

console.log(duplicateEncode("holaMundo"))