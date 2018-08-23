document.getElementById("register-Form").addEventListener("submit",register);
function register(event){
    event.preventDefault();

    first_name = document.getElementById('fname').value;
    last_name = document.getElementById('lname').value;
    user_email = document.getElementById('email').value
    user_password = document.getElementById('password').value;

    fetch('https://diary-2018.herokuapp.com/api/v1/auth/signup',{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        mode:'cors',
        body:JSON.stringify({
            name: first_name,
            email: user_email,
            password: user_password

        })


    }).then((response) => {
        status_code = response.status
        return response.json()
    }).catch(error =>
        alert(error)
    ).then((response) => {
        if(status_code !=201){
            alert(response['Error'])
            document.getElementById("error-msg").innerHTML = response['Error']
        }
        else{
            window.location = '../index.html'
            alert('Account created please login')
        }
    }).catch(error =>
        alert("Failed to fetch request")
    )

}
