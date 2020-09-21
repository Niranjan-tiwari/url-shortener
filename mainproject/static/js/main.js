function Urlshortener(){
    let copy = document.getElementById('short_url');
    copy.select();
    document.exeCommand('copy')
    alert('url copied:' + copy.value);



}