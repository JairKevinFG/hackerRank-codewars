function validBraces(braces){
    let array = []
    let valid = {
        '(':')',
        '[':']',
        '{':'}'
    }
    for (let j = 0; j < braces.length; j++) {
        const char = braces[j];
        if(valid[char]){
            array.push(char)   
        }else{
            if(char != valid[array.pop()]){
                return false
            }
        }
    }
    return array.length === 0
}


console.log(validBraces("[]"))


