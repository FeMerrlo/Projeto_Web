
import './App.css';
import escola from './img/lojacarros.jpg'
import ListaAlunos from './componentes/listaalunos';
export default App; function App() {

  //CODIGOJS COM A FUNÇAO ANTES DO RETURN

  const aluno = 'Felipe'
  const curso = 'ADS'
  const alunos = ['Joao','jose','maria']
  const valor = 10 * 3


  return (
    <>
    <h1>ESCOLA</h1>
    <img src={escola} className="App-logo" width= "200px" height="200px" alt='imagem escola'></img>
    <br></br>
    <p>aluno: <b>{aluno}</b></p>
    <p>curso: <b>{curso}</b></p>
    <p>alunos: <b>{alunos}</b></p>
    <p>vaor: <b>{valor}</b></p>

    <button onclick="clique()">
      Butão
    </button>
    <select>
      <option value="valor1">João</option>
      <option value="valor2">jose</option>
      <option value="valor3">Maria</option>

    </select>

    <ListaAlunos alunos={alunos} />
    </>
  );
}


