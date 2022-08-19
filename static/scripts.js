/* 
$("#list a").click(function(event){
    event.preventDefault(); //Essa linha vc coloca caso queira anular o evento do click da tag <a>;
    console.log("O elemento clicado foi: " + $(this).text();
});
 */


window.onload = function () {
    //var el = document.getElementById("title-div");
    var el = document.querySelectorAll(".click")
    el.style.cursor = "pointer";
    el.onclick = verify;
}


function verify(){
    console.log('teste!')

    let descendentes = document.querySelectorAll(".link-td");
    let item;

    for (let i = 0; i < descendentes.length; i++) {
        descendentes[i].addEventListener("click", function (e) {
            item = this.innerHTML
            //alert('O elemento clicado foi o ' + this.innerHTML);
            var r=confirm("Tem certeza que deseja deletar esse item?");
            if (r==true)
                {
                    console.log('FOI!')
                    window.location.assign('http://127.0.0.1:5000/del_data/' + item);
                }
            else
                {
                    console.log('OK!')
                    window.location.assign('http://127.0.0.1:5000/lista_pac');
                }
        })
    }


/*     var r=confirm("Tem certeza que deseja deletar esse item?");
    if (r==true)
        {
            console.log('FOI!') //window.location.assign("http://127.0.0.1:5000/"); //del_data/1
            document.getElementById("xx").click();
        }
    else
        {
            console.log('OK!') //window.location.assign("http://127.0.0.1:5000/lista_pac");
        } */
}


var descendentes = document.querySelectorAll("#list a");
for (var i = 0; i < descendentes.length; i++) {
    descendentes[i].addEventListener("click", function (e) {
        alert('O elemento clicado foi o ' + this.innerHTML);
    })
}












//     var botoes = document.getElementsByTagName("button");
//     for (var i = 0; i < botoes.length; i++) {
//     if (botoes[i].className === "MINHA-CASSE") {
//         botoes[i].click();
//     }
//  }



//     console.log('teste!')
//     var r=confirm("Tem certeza que deseja deletar esse item?");
//     if (r==true)
//         {
//             window.location.assign("http://127.0.0.1:5000/"); //del_data/1
//         }
//     else
//         {
//         window.location.assign("http://127.0.0.1:5000/lista_pac");
//         }
    //document.getElementById("demo").innerHTML=x;

//window.location.href = "http://pt.stackoverflow.com";
// ou uma variante com o mesmo efeito
//window.location.assign("http://pt.stackoverflow.com");
