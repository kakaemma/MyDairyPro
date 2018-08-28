/**
 * Created by Emmanuel Kakaire on 8/27/2018.
 */

document.getElementById("add-entry-form").addEventListener('submit', add_entry);

function add_entry(event) {
    event.preventDefault()
    diary_name = document.getElementById('add_entry_name').value;
    description = document.getElementById('add_entry_desc').value;

    fetch('https://diary-2018.herokuapp.com/api/v1/entries',{
        method:'POST',
        headers:{
            'Content-Type': 'application/json',
            'Authorization':window.localStorage.getItem('token')
        },
        body:JSON.stringify({
            name:diary_name,
            desc:description
        })

    }).then((response)=>{
        
    })

}
