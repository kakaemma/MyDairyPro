document.getElementById("register-Form").addEventListener("submit",register)
function register(event){
    event.preventDefault()

    first_name = document.getElementById('fname').value;
    last_name = document.getElementById('lname').value;
    email = document.getElementById('email').value
    password = document.getElementById('password');

    uri = 'https://diary-2018.herokuapp.com/api/v1/auth/signup'
    headers = new Headers(
        {
            'Content-Type': 'application/json'
        }
    )
    fetch(uri,{
        method: 'POST',


    })

}
