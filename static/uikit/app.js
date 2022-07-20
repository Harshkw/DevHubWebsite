// Invoke Functions Call on Document Loaded
document.addEventListener('DOMContentLoaded', function(){
  hljs.highlightAll();
});

if(alertWrapper){
  for (let i = 0; i < alertClose.length; i++) {
   alertClose[i].addEventListener('click', ()=>{
     alertWrapper[i].style.display = 'none'});
     }
}