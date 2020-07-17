// Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence,
// which is the number of times you must multiply the digits in num until you reach a single digit.
const persistence =  (num) => {
    let count = 0
     let product = 1
     let newNum = num.toString()
     if (num <10){
         return 0
     }else{
         for(i=0;i<newNum.length;i++){
             let number = newNum[i]
             product = number*product
         } 
         count =count + 1
     }
     if (product >= 10){
         const newcount = persistence(product)
         count = count + newcount   
     }
     return count
 }
 
console.log(persistence(39))




