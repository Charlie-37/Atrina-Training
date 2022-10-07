//*--------Variable --------------------*//


//*--------Comments--------------------*//
//*--------Data Type--------------------*//
//*--------Operators--------------------*//
//*--------Conditional statements--------------------*//
function points1(){
    let x = parseInt(document.getElementById('grade_check').value)

    if(x<100 && x>=90){
        return window.alert('Grade is : A+')
    }
    else if(x<90 && x>=75){
        return window.alert('Grade is : A')
    } 
    else if(x<75 && x>=60){
        return window.alert('Grade is : B')
    } 
    else if(x<60 && x>=45){
        return window.alert('Grade is : C')
    } 
    else if(x<45 && x>=32){
        return window.alert('Grade is : D')
    } 
    else if(x<32){
        return window.alert('Grade is : Fail')
    } 
    else{
        return window.alert('Invalid Number')

    }


}
//*--------Functions--------------------*//

function points2(){
    let x = parseInt(document.getElementById('add_num1').value)
    let y = parseInt(document.getElementById('add_num2').value)
    // window.alert(x+y)
    document.getElementById('add_is').innerHTML = 'Addition is : '+ (x+y)

}

//*--------For Loop andBreak statement--------------------*//

function num_break(){
    let x = document.getElementById('num_break').value
    let y = ''

    for(let i=0; i<=100; i++){
        if (i==x){

            break;
        }
        else{
            y+= i+'<br>'
            
        }

        document.getElementById('break_stat').innerHTML = y
    }
}

//*-------while loop--------------------*//
function fact(){
    let x = document.getElementById('fact').value
    
    let res = 1
    
    let i = 1
    while (i<= x){
        res*=i
        i++
    }
    
    document.getElementById('fact_num').innerHTML = res
}

//*-------Array--------------------*//

let x = document.getElementById('arrClick')
x.addEventListener('mouseover',arrayIn)
x.addEventListener('mouseout',arrayOut)

function arrayIn(){
    const fruits = ["Banana", "Orange", "Apple", "Mango"];
    fruits.up
    res = ''
    for (let i in fruits){
        res += fruits[i]+'<br>'
    }
    
    document.getElementById('arr_method').innerHTML=res
    document.getElementById('arr_method').innerHTML=fruits.join(' ')
    
}
function arrayOut(){
    document.getElementById('arr_method').innerHTML=''
    
}

//*-------JQUERY--------------------*//
$(document).ready(function(){
$('#fade_toggle').click(function(){
    $('#tog_para').fadeToggle('slow');
$('#tog_para2').slideToggle();
});

})

