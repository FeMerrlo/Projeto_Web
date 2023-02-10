function nome_funcao(){
    let nr1 = document.getElementById("txtNumero1").value;
    let nr2 = document.getElementById("txtNumero2").value;
    let resultado = "";
    if(nr1==nr2)
        resultado ="Número" + nr1  + "é igual ao nr" + nr2+ "!"
    if(nr1>nr2)
        resultado = ("Número" + nr1  + "é o maior do que o nr: " + nr2+ "!");
    else
        resultado = ("Número" + nr2  + "é o maior do que o nr: " + nr1+ "!");
    document.getElementById("idResultado").innerHTML = resultado;
}