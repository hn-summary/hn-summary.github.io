document.addEventListener("DOMContentLoaded", function(event) {
    for (const element of document.getElementsByClassName("is-active")){
        setTimeout(function(){
            element.parentElement.parentElement.scrollTo({left: element.offsetLeft, behavior: 'auto'})
        }, 300);
    }
});
