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
    else{
        alert('entries')

        console.log(response)
    }
})


