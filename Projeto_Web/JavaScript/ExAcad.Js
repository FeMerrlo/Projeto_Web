const calcular = document.getElementById('calcular');

calcular.addEventListener('click', function() {
  const peso = document.getElementById('peso').value;
  const altura = document.getElementById('altura').value;

  const imc = peso / (altura ** 2);

  let resultado = '';
  if (imc < 18.5) {
    resultado = 'Abaixo do peso';
  } else if (imc >= 18.5 && imc < 25) {
    resultado = 'Peso normal';
  } else if (imc >= 25 && imc < 30) {
    resultado = 'Acima do peso';
  } else {
    resultado = 'Obesidade';
  }

  document.getElementById('resultado').innerHTML = `Seu IMC é: ${imc.toFixed(2)} - ${resultado}`;
});
