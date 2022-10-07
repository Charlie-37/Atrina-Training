
//*-------Function--------*//
let x = document.getElementById('Calc')

x.addEventListener('click',Calculete)

function Calculete(){
    
    let a = document.getElementById('no1').value
    a = parseInt(a)
    let b = document.getElementById('no2').value
    b = parseInt(b)
    let opt = document.getElementById('opert').value
    let res = 0
    switch (opt){

        case '+':
        res = a + b
        document.getElementById('answer').innerHTML =  res
        break;

        case '+':
        res = a + b
        document.getElementById('answer').innerHTML =  res
        break;

        case '-':
        res = a - b
        document.getElementById('answer').innerHTML =  res
        break;

        case '*':
        res = a * b
        document.getElementById('answer').innerHTML =  res
        break;

        case '/':
        res = a / b
        document.getElementById('answer').innerHTML =  res
        break;

        case '%':
        res = a % b
        document.getElementById('answer').innerHTML =  res
        break;

        case '**':
        res = a ** b
        document.getElementById('answer').innerHTML =  res
        break;

        case '//':
        res = a // b
        document.getElementById('answer').innerHTML =  res
        break;
        

    }
}

let multi_btn = document.getElementById('mul_Table')
multi_btn.addEventListener('click',Multiplication_tab)

function Multiplication_tab(){
    let a = document.getElementById('multitab').value
    a = parseInt(a)
    res = ''
    let i = 1
    
    while (i<11){
        res += a*i+'<br>'
        i++
        
    }
    document.getElementById('mult_ans').innerHTML =  res
    
}

//*----- Stack Method----*//
const stack_array = [];

let arr_push1 = document.getElementById('arr_push')
let arr_pop = document.getElementById('arr_pop')
let arr_traverse = document.getElementById('arr_traver')
arr_push1.addEventListener('click', function(){arrInsert(stack_array)})
arr_pop.addEventListener('click',function(){arrPop(stack_array)})
arr_traverse.addEventListener('click',function(){arrTraverse(stack_array)})

function arrInsert(stack_array) { 
    let a = document.getElementById('ent_arr').value
    stack_array.push(a)
    console.log(stack_array)
    
    return document.getElementById('arr_disp').innerHTML =  stack_array
    
}

function arrPop(stack_array){
    stack_array.pop()
    return document.getElementById('arr_disp').innerHTML =  stack_array
}

function arrTraverse(stack_array){
    let traverse_arr = []
    let i = stack_array.length-1
    for(i;i>=0;i-=1){
        traverse_arr.push(stack_array[i])
        
    }
    stack_array = traverse_arr
    document.getElementById('arr_disp').innerHTML =  stack_array

    return stack_array
}