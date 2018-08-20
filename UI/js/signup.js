document.getElementById("register-Form").addEventListener("submit",register)
function register(event){
    event.preventDefault()

    first_name = document.getElementById('fname').value;
    last_name = document.getElementById('lname').value;
    user_email = document.getElementById('email').value
    user_password = document.getElementById('password');

    uri = 'https://diary-2018.herokuapp.com/api/v1/auth/signup'
    headers = new Headers(
        {
            'Content-Type': 'application/json'
        }
    )
    fetch(uri,{
        method: 'POST',
        body:JSON.stringify({
            name: first_name,
            email: user_email,
            password: user_password

        })


    }).then((response)=>{
        if(respose.status_code == 201){
            window.location='./index.html'
            alert('Account successfully created created')

    }
    else {
            alert()
    }
    })

}
