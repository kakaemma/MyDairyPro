/**
 * Created by Emmanuel Kakaire/2018.
 */

document.getElementById("login-form").addEventListener('submit', login);
function login(event) {
    event.preventDefault();

    user_email = document.getElementById("email").value;
    user_password = document.getElementById("password").value;

    fetch('https://diary-2018.herokuapp.com/api/v1/auth/login',{
        method:'POST',
        headers:{
            'Content-Type': 'application/json'
        },
        mode:'cors',
        body:JSON.stringify({
            email:user_email,
            password:user_password
        })

    }).then((response) =>{
        status_code = response.status
        return response.json()
    }).then((resp)=>{
        if(status_code !=200){
            document.getElementById("error-msg").innerHTML= resp['Error']
        }
        else{
            alert(resp['status'])
        }

    })
    
}
