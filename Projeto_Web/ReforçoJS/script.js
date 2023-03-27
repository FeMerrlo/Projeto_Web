// funaõ tradicional 

function soma(num1,num2){
    return num1 * num2
}
console.log(soma(2,3));

// arrow funcion

const soma1=(num3,num4)=>{
    return num3 * num4
}
console.log(soma(5,9))

//function tradicional

const texto ="Ola Mundo"
function sepaTexto(texto){
    return texto.split('')
}
console.log(sepaTexto(texto))

//arrow function 
const texto1 = 'Ola Mundo'
const sepaTexto1=(texto1) =>{
    return texto1.split('')
}
console.log(sepaTexto(texto1))


//arrow function com array

const usuarios=[
    {id: 1, nome: "Felipe"},
    {id: 2, nome: "Carlos"},
    {id: 3, nome: "Guilherme"},

]
const user=usuarios.find(user =>user.id ===3)

document.write (`O usuário é: ${user.nome}`);

// exemplo com filter, map e reduce

const funcionarios =[
    {nome: 'Gustavo', salario:1500, dataNascimento:2003},
    {nome: 'Vitão', salario:150000, dataNascimento:2002},
    {nome: 'Felipe', salario:1200, dataNascimento:2001},
    {nome: 'Natan', salario:2000, dataNascimento:1930},
]

const salario = funcionarios.filter(funcionarios =>(
    funcionarios.salario >= 2000))
    console.log(salario);

const exibeInfo = funcionarios.map( funcionarios => `${funcionarios.nome}`+' nasceu em '+ `${funcionarios.dataNascimento})`);
console.log(exibeInfo)

const total = funcionarios.reduce((resultado,valorTotal)=>{
    return (resultado + valorTotal.salario)
},0)
console.log(total)
