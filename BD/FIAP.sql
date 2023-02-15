-- Introdução a linguagem SQL 

-- É uma linuagem estruturada de tarefas
-- problema é a crrigir problemas
-- DDL - Linguagem de definição de dados, vai significar estrutura

-- Criadno tabela
-- Sintaxe:
   create table nome_tabela (
   nome_coluna1 tipo_dados(tamanho)  [regra],
   ......,
   nome_colunaN tipo_dados(tamanho)  [regra]);

Tipo de dados: char(n), campo alfanumérico de tamanho fixo
               varchar(n), campo alfanumérico de tamanho variavel
               number(x, y), campo numérico inteiro ou real
               date, campo tipo data
n = tamanho
x = parte interira
y = parte real, casas decimais

regras/Constraints
Pk - primary key, campo unico, preencimento obrigatório, relacionament
FK - foreign key, relacionamento lado n da cardinalidade, recebe dados previamente cadastrados na Pk
Nn - not null, campo de preenchimento obrigatorio
Uk - unique, campo com restriçao a dados repetidos
Ck - check, campo com lista de dados para vaidaçao

Exemplificando

1 - criando uma tabela:

create table cargo
(cd_cargo number(3),
nm_cargo varchar2(25),
salaio number(8,2));

visuaizando a estrutura de uma tabela 
desc cargo

--select object_name from user_objects where object_type = 'TABLE'; Vai trazer todos os arquivos da area 
 1- deletando uma tabela
ex: drop nome_tabela
drop table cargo

 2- criando uma tabela com regras, sem personalização: 
 create
 
 criando o relacionamento
 1 - 1 - Pk + FK_Uk
 1 - N - Pk + FK
 N - N - não existe em código sql
 
 
 15/02/2023
 
 -- tem que ser exatamente com o nome da entidade
 create table n_fiscal
 (n_nf number(5) primary key,
 dt_nf date not null,
 total_nf number(10,2)); 
 
 select constraint_name from user_constraints where table_name = 'N_FISCAL'
 
 desc n_fiscal
 
 create table produto
 (cd_pro number(5) constraint prod_cd_pk primary key,
 nm_prod varchar2(30) constraint prod_mn_nm not nul
 constraint prod_nm_uk unique,
 preco number(10,2))
 
 select constraint_name from user_constraints where table_name = 'PRODUTO'
 
 create table tem
 (fk_nota number(5) constraint tem_nf_fk references n_fiscal,
 fk_prod number(5) constraint tem_prod_fk references produto)
 
 Inserindo dados
 Comando DML -Data Manipulation Language
 Novas linhas
 insert into nome_tabela values
 (Valor1, Valor2,...., ValorN)
 
 Obs: campos: char,varchar ou varchar2 e date precisam de apóstrofe
 
 Exemplo 1
 conhecendo ou visualizando a estrutura
 desc n_fiscal
 inserido uma linha
 insert into n_discal values (1,'10-Jan-00', 5000);
 insert into n_discal values (1,'10-Jan-00', 5000);
 verificando a inserção
 select * from n_fiscal
 
 descobrindo o padrão de data
 select sysdate from dual
 gravando dados físicamene
 commit;