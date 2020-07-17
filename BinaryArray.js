// arreglo de binario a decimal
const binaryArrayToNumber = arr => {
  decimal = 0
  for (i=0;i<arr.length;i++){
    numero = arr[i]
    newnumero = numero*(2**(arr.length-i-1))
    decimal= newnumero + decimal
  }
  console.log(decimal)
}

binaryArrayToNumber([1, 1, 1, 1])
