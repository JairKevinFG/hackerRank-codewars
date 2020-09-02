// Move the first letter of each word to the end of it, 
// then add "ay" to the end of the word. Leave punctuation marks untouched.
// pigIt('Pig latin is cool'); // igPay atinlay siay oolcay
// pigIt('Hello world !');     // elloHay orldway !
// Pig! => igPay! 

function pigIt(str) {
    newstr = ''
    for(let i of str.split(' ')){
        newlist = i.split('')
        newlist.push(newlist.shift())
        if (newlist[0] != '!' &&  newlist[0] != '?') {
            nstr = newlist.join('').concat('ay')
        }else{
            nstr = newlist.join('')
        }
        newstr = newstr + ' '+ nstr
    }
    return newstr.trim()
}
console.log(pigIt("Hello world !"))

