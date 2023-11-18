// function exibirPopup(id) {
//     var popup = document.getElementById("popup_" + id);
//     if (popup){
//     popup.style.display = "block";


//     }
// }

function fecharPopup(id) {
    var popup = document.getElementById("popup_" + id);
    popup.style.display = "none";
}

document.querySelectorAll('.image-container img').forEach(function (img) {
    img.addEventListener('click', function () {
        var id = this.parentElement.dataset.id;
        exibirPopup(id);
    });
});
var popupAberto = null;
function exibirPopup(id) {
    var popup = document.getElementById("popup_" + id);
    
    if (popup.style.display === "block") {
        popup.style.display = "none";
    } else {
        popup.style.display = "block";
        return popupAberto = true;
    }
}
if (popupAberto == true){
    document.addEventListener('click', function(event) {
        var popups = document.querySelectorAll('.popup'); // Substitua 'seu-classe-de-popup' pela classe real do seu popup
        
        var clicouDentroDoPopup = false;

        popups.forEach(function(popup) {
            if (popup.contains(event.target)) {
                clicouDentroDoPopup = true;
            }
        });

        if (!clicouDentroDoPopup) {
            popups.forEach(function(popup) {
                popup.style.display = "none";
            });
        }
    });
    }
