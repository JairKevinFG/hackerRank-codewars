const alphabetPosition = (text)  => {
    const lower = text.toLowerCase()
    alphabet = ['a', 'b', 'c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
    let array=[]
    for(i=0;i<lower.length;i++){
        for(j=0;j<alphabet.length;j++){
            if (lower[i] === alphabet[j]){
                array.push(j+1)
            }               
        }
    }
    let result = array.join(' ')
    return result
}


alphabetPosition("THE sunset sets at twelve o' clock.")
