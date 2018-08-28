/**
 * *
 * Created by Emmanuel Kakaire on 8/27/2018.
 * *
 */

function logged_in() {
    token = localStorage.getItem('token')
    if(token ==''){
        window.location="../index.html"
    }
}

function logout(){
    localStorage.removeItem('token')
    window.location="../index.html"
}