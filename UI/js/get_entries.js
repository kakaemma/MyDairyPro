/**
 * Created by Administrator on 8/29/2018.
 */

function get_all_entries() {

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
        alert('No entries')
    }
    else{
        alert('entries')

        console.log(response)
    }
})

}
