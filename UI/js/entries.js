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
                '<a href="#" class="button button_dash" id="modalbtn" onclick="return pop_edit_modal()">Edit</a>'+
                '</td></tr>'+
                '        <div class="modal" id="editModal" style="left: 0px">'+
                '<div class="modal_content">'+
                    '<div class="modal_header">'+
                        '<span class="close"><a href="">&times;</a></span>'+
                        '<h2>Update Diary</h2>'+
                    '</div>'+
                    '<div class="modal_body" style="padding-top: 20px;">'+
                        '<form action="" name="editentry" id="modify-entry" method="PUT">'+
                            '<div class="form-group" style="margin-bottom: 20px">'+
                                '<input type="text" name="name" class="formField" placeholder="New Diary name " />'+
                            '</div>'+
                            '<div class="form-group">'+
                                '<input type="text" name="desc" class="formField" placeholder="Diary description " />'+
                            '</div>'+
                            '<button class="button button_dash" name="entry_btn" type="submit" onclick="return modify_entry('+entry.id+')">Update</button>'+
                        '</form>'+
                    '</div>'+
                '</div>'+
            '</div>';

        });
        document.getElementById('diary-display').innerHTML =display_results;

        console.log(response);
    }
})



function pop_edit_modal () {

    document.getElementById('editModal').style.display = "block";

}

function modify_entry(entry_id) {
    alert(entry_id)
}