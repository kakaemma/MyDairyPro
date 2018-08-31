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
        display_results='<tr><td>Diary name</td><td>Description</td></tr>';
        response.forEach(entry=>{
            display_results += "<tr><td><h5>"+entry.name+"</h5></td><td><h5>"+ entry.Description +"</h5></td></tr>";

        });
        document.getElementById('diary-display').innerHTML =display_results;

        console.log(response);
    }
})


