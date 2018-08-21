document.getElementById("register-Form").addEventListener("submit",register);
function register(event){
    event.preventDefault();

    first_name = document.getElementById('fname').value;
    last_name = document.getElementById('lname').value;
    user_email = document.getElementById('email').value
    user_password = document.getElementById('password');

    fetch('https://diary-2018.herokuapp.com/api/v1/auth/signup',{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        mode:'no-cors',
        body:JSON.stringify({
            name: first_name,
            email: user_email,
            password: user_password

        })


    }).then((response) => {
        response.json()
    }).catch(error =>
        alert("please check your internet connection")
    ).then((response) => {
        if(response.status_code !=201){
            document.getElementById("error-msg").innerHTML = response['Error']
        }
        else{
            window.location = './index.html'
            alert('Account created please login')
        }
    }).catch(error =>
        alert("Failed to fetch request")
    )

}
