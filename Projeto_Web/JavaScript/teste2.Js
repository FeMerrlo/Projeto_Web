const form = document.querySelector("#login-form");

form.addEventListener("submit", function(event) {
  event.preventDefault();

  const username = form.elements.username.value;
  const password = form.elements.password.value;

  console.log("Nome ou CPF: ", username);
  console.log("Senha: ", password);

  const nome = form.elements.nome.value;
  const telefone = form.elements.telefone.value;
  const email = form.elements.email.value;
  const mensagem = `${nome} Entraremos em contato pelo ${telefone} e ${email} obrigado pela preferência.`;
  alert(mensagem);

});
