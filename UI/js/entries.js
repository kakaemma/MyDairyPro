/**
 * Created by Administrator on 8/29/2018.
 */


    fetch('https://diary-2018.herokuapp.com/api/v1/entries',{
    method:'GET',
    headers:{
        'Authorization':localStorage.getItem('token')
    }
}).then((response)=>{
    status_code = response.status
    return response.json()
}).then((response)=>{
    if(status_code == 404){
        document.getElementById('diary-display').innerHTML = "You have no entries added"
    }
    if(status_code == 401){
        alert('Your session has expired. please login again');
        window.location='../index.html'
    }
    else{
        display_results="<tr><td>Diary name</td><td>Description</td><td>#</td></tr>";
        response.forEach(entry=>{
            modal = 'myModal'
            display_results += '<tr><td><h5>'+entry.name
                +'</h5></td><td><h5>'+ entry.Description
                +'</h5></td><td>'+
                '<a href="#" class="button button_dash" id="modalbtn" onclick="return edit_modal('+entry.id+')">Edit</a>'+
                '</td></tr>';

        });
        document.getElementById('diary-display').innerHTML =display_results;

        console.log(response);
    }
})



function edit_modal (entry_id) {

    document.getElementById('editModal').style.display = "block";

    alert(entry_id)
document.getElementById('modify-entry').addEventListener('submit', modify);
function modify(event){
    event.preventDefault();
alert(entry_id)
    new_name = document.getElementById('new_name').value;
    new_description = document.getElementById('new_desc').value;

    fetch('https://diary-2018.herokuapp.com/api/v1/entries/'+parseInt(entry_id),{
        method:'PUT',
        headers:{
            'Content-Type': 'application/json',
            'Authorization': localStorage.getItem('token')
        },
        body:JSON.stringify({
            name:new_name,
            desc:new_description
        })
    }).then(response=>{
            status_code = response.status
            return response.json()
        }).then(response=>{
            if(status_code !=200){
                alert(response['Error'])
            }
            if(status_code == 401){
                alert('Your session has expired. please login again');
                window.location='../index.html'
            }
            if(status_code == 200){
                alert('Entry successfully modified')
                window.location='dashboard.html'
            }
        })

}

}

function modify_entry(entry_id) {


}