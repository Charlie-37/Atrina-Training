
// Register A id

function registerId(){
    let name = document.getElementById('UserName').value
    let user_id = document.getElementById('UserId').value
    let email = document.getElementById('UserEmail').value
    let passw = document.getElementById('UserPassw').value
    let phNumber = document.getElementById('UserNumber').value
    let city = document.getElementById('UserCity').value

    let obj_id = user_id
    user_obj = {
        User_id : user_id,
        User_name : name,
        User_email : email,
        User_passw : passw,
        User_number : phNumber,
        User_city : city
    }
    // console.log(user_id)

    localStorage.setItem( obj_id,JSON.stringify(user_obj))

    // let gotobj = localStorage.getItem('user_id')

    // let parseobj = JSON.parse(gotobj)

    // console.log(parseobj)

    alert("Registration Sucessfull")

    // return location.reload()
    return window.location.href = 'index.html';
}

//*-----------Login--------------*//

function userLogin(){
    entered_userId = document.getElementById('userId').value
    entered_userPassw = document.getElementById('userPassw').value

    let checkId = localStorage.getItem(entered_userId)

    let gotId = JSON.parse(checkId)

    if(gotId != null){

        if(entered_userPassw == gotId['User_passw'] ){
            let u_id = gotId

            window.location.href = 'user.html';
            sessionStorage.setItem(JSON.stringify(u_id['User_id']),JSON.stringify(gotId))
            alert("Login Sucessful")
        
            return SessionUser()
        }
        else{
            alert("Invalid UserId and Password")
            window.location.href = 'index.html';
        }
    }
    else{
        console.log("notgot")
    }
}

var objInfo = Object.keys(sessionStorage)
// console.log(objInfo)


function SessionUser(){
    let user = Object.keys(sessionStorage)
    let user_id = sessionStorage.getItem(user)
    alert(user)  

var el = document.getElementsByClassName('hr');
el.innerHTML = 'hello world'
}




function logOut(){
    sessionStorage.clear()
    return window.location.href = 'index.html';
}




