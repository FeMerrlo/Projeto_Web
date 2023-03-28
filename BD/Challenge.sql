Introdução a linguagem SQL
DDL - Linguagem de definição de dados - Estrutura
Criando tabelas
Sintaxe:
    create table nome_tabela
    (nome_coluna1 tipo_dados(tamanho) [regra],
    ......,
    nome_colunaN tipo_dados(tamanho) [regra]);
    
Tipo de dados: char(n), campo alfanumérico de tamanho fixo (Caractere)
               varchar(n), campo alfanumérico de tamanho variavel
               number(x,y), campo numérico inteiro ou real
               date, campo tipo data
n = tamanho
x = parte inteira
y = parte real, casas decimais

Regras/Constraints
Pk - primary key, campo unico, preenchimento obrigatório, relacionamento
FK - foreign key, relacionamento lado n da cardinalidade, recebe dados
     previamente cadastrados na Pk
Nn - not null, campo de preenchimento obrigatorio
Uk - unique, campo com restriçao a dados repetidos
Ck - check, campo com lista de dados para validação

Exemplificando 

1- criando uma tabela sem regras:

create table cargo10
(cd_cargo number(3),
nm_cargo varchar2(25),
salario number(8,2));

visualizando a estrutura de uma tabela
desc nome_tabela
exemplo: desc cargo10

deletando uma tabela
drop table nome_tabela
exemplo: drop table cargo10

2- criando uma tabela com regras, sem personalização:
create table cargo10
(cd_cargo number(3) primary key,
nm_cargo varchar2(25)not null unique,
salario number(8,2));

desc cargo10

visualizando constraints
select constraint_name, constraint_type from user_constraints
where table_name = 'CARGO10'

2- criando uma tabela com regras, com personalização:

drop table cargo10

create table cargo10
(cd_cargo number(3) constraint cargo_cd_pk primary key,
nm_cargo varchar2(25)constraint cargo_nome_nn not null 
                     constraint cargo_nome_uk unique,
salario number(8,2));

desc cargo10

visualizando constraints
select constraint_name, constraint_type from user_constraints
where table_name = 'CARGO10'

criando o relacionamento

1 - 1 - Pk + FK_Uk
1 - N - Pk + FK
N - N - não existe em código sql

desc cargo10
create table funcionario10
(cd_fun number(3) constraint fun_cd_pk primary key,
nm_fun varchar(30) constraint fun_nm_nn not null,
dt_adm date constraint fun_dt_nn not null,
uf_fun char(2) constraint fun_uf_nn not null,
cargo_fk number(3) constraint fun_cargo_fk references cargo)

desc funcionario10

create table funcionario11
(cd_fun number(3) constraint fun_cd_pk1 primary key,
nm_fun varchar(30) constraint fun_nm_nn1 not null,
dt_adm date constraint fun_dt_nn1 not null,
uf_fun char(2) constraint fun_uf_nn1 not null,
cargo_fk references cargo)

Criação das tabelas: n_fiscal e produto

15/02/2023

create table n_fiscal
(n_nf number(5) primary key,
dt_nf date not null,
total_nf number(10,2));

desc n_fiscal
select constraint_name from user_constraints where table_name = 'N_FISCAL'

desc n_fiscal

create table produto
(cd_pro number(5) constraint prod_cd_pk primary key,
nm_prod varchar2(30) constraint prod_mn_nn not null
constraint prod_nm_uk unique,
preco number(10,2))

select constraint_name from user_constraints where table_name = 'PRODUTO'

create table tem
(fk_nota number(5) constraint tem_nf_fk references n_fiscal,
fk_prod number(5) constraint tem_prod_fk references produto)

Inserindo dados
Comando DML - Data Manipulation Language
Novas linhas:
insert into nome_tabela values
(valor1, valor2,...., valorN)

Obs: campos: char, varchar ou varchar2 e date precisam de apóstrofe

Exemplo 1
conhecendo ou visualizando a estrutura
desc n_fiscal
inserindo uma linha
insert into n_fiscal values (1,'10-Jan-00',5000);
insert into n_fiscal values (2,'10-dec-00',5000);
verificando a inserção
select * from n_fiscal
descobrindo o padrão da data
select sysdate from dual
gravando dados fisicamente
commit;

Aula 03 - 01/03/2023

Ainda trabalhando com estrutura das tabelas

DDL

Create - Ok

Alterando ou corrigindo uma estrutura
alter table nome_tabela
opções
add column      - nova coluna
add constraint  - nova regra
modify          - modifica tipo e/ou tamanho de uma coluna
drop column     - elimina uma coluna
drop constraint - elimina uma regra

create table tb_teste
(codigo number(2),
nome number(10));

incluindo uma nova coluna
alter table tb_teste add dt_nasc date
incluindo uma coluna com regra
alter table tb_teste add cep char(8) not null
incluindo a pk na coluna codigo
alter table tb_teste add constraint pk_cod primary key (codigo)

modificando apenas o tipo de dados
alter table tb_teste modify nome varchar(10)

modificando apenas o tamanho da coluna
alter table tb_teste modify nome varchar(50)

modificando tamanho e tipo ao mesmo tempo
alter table tb_teste modify nome number(10)

eliminando uma regra
alter table tb_teste drop constraint pk_cod

desc tb_teste
desc user_constraints
select constraint_name from user_constraints where table_name = 'TB_TESTE'
eliminando uma coluna
alter table tb_teste drop column nome
renomeando uma coluna
alter table tb_teste rename column codigo to cod_cliente
renomeando uma constraint
alter table tb_teste rename constraint sys_c003509437 to fiap
eliminando uma tabela
drop table nome_tabela
drop table tb_teste

create table tb_teste1
(codigo number(1) primary key)
create table tb_teste2
(codigo number(1) references tb_teste1)
insert into tb_teste1 values(1)
insert into tb_teste2 values(1)
drop table tb_teste1 cascade constraints
uso do cascade permite eliminar o relacionamento e depois dropar a tabela

Atualizando dados

Update 

operadores: aritméticos: + - * / ()
            relacionais: > >= < <= = != ou <>
            lógicos: and or not
            
update nome_tabela set nome_coluna = novo_valor

update nome_tabela set nome_coluna = novo_valor
where condição


create table produto_tb 
(cod_prod number(4) constraint prod_cod_pk primary key, 
unidade varchar2(3),descricao varchar2(20),val_unit number(10,2))

insert into produto_tb values ('25','KG','Queijo','0.97');
insert into produto_tb values ('31','BAR','Chocolate','0.87');
insert into produto_tb values ('78','L','Vinho','2.00');
insert into produto_tb values ('22','M','Linho','0.11');
insert into produto_tb values ('30','SAC','Acucar','0.30');
insert into produto_tb values ('53','M','Linha','1.80');
insert into produto_tb values ('13','G','Ouro','6.18');
insert into produto_tb values ('45','M','Madeira','0.25');
insert into produto_tb values ('87','M','Cano','1.97');
insert into produto_tb values ('77','M','Papel','1.05');
commit;

select * from produto_tb

atualizando os dados do preço do produto para R$1,00
update produto_tb set val_unit = 1

atualizando os dados do preço do produto para R$1,5
apenas dos produtos de unidade de medida igual a metro
update produto_tb set val_unit = 1.5
where unidade = 'M'
select * from produto_tb order by 1

atualizar em 15% o preço dos produtos de código maior que 30.
update produto_tb set val_unit * 1,15
where cod_prod > 30


atualizar o nome do produto queijo para queijo de minas.
update produto_tb set descricao = 'Queijo De Minas'
where descricao = 'Queijo'


para os produtos Açucar, madeira e Linha zerar o seu preço.
update produto_tb set val_unit = 0
where descricao = 'Acucar' or descricao = 'Madeira' or descricao = 'Linha'
desc produto_tb


commit

Eliminando linhas (s)
todas 
delete from nome_tabela
algumas


ex01 - Cidade

create table cidade_tb

(Codigo_Cidade number(4) constraint Cid_Cod_pk primary key, 
Nome_da_Cidade varchar2(30) constraint cid_nome_nn not null)

create table social_tb

(Cod_cpf char(11) constraint soc_cpf_pk primary key, 
Cod_nome varchar2(20) constraint soc_nome_nn not null,
Cod_DaNas date,
Cod_rg varchar2(15),
Cod_Cid_fk number(4));

ex3
alter table cidade_tb add Uf char(2) not null
select * from cidade_tb

ex5
alter table social_tb modify Cod_nome char(25)

commit

ex4

Aula 5 - Correção de exercicios

create table cidade (codigo number(4) constraint pk_cid_cd primary key,
nome varchar(30) constraint nn_cid_nome not null);
desc cidade -- exibindo estrutura
insert into cidade values(1,'São Paulo','SP');
insert into cidade values(2,'Curitiba','CU');
commit; -- validação de dados
select * from cidade; -- exibindo dados

 

create table socio (cpf char(11) constraint pk_soc_cpf primary key,
nome varchar(20) constraint nn_soc_nome not null,
datanasc date constraint nnt_soc_dtnasc not null,
rg varchar(15) constraint nn_soc_rg not null,
cidade number(4) constraint fk_soc_cid references cidade)
desc socio -- exibindo estrutura
insert into socio values ('11111111111','Joana','04-may-1997','11111111111111',
1,'1111111111','F',10);
insert into socio values ('21111111111','Claudio','14-dec-00','21111111111111',
2,'2111111111','M',20);
commit; -- validação de dados

 

alter table cidade add uf char(2) constraint nn_cid_uf not null

 

alter table socio add (fone varchar(10),
sexo char(1) constraint nn_soc_sx not null)

 

alter table socio modify nome varchar(35)

 

create table setor (codigo number (3) constraint pk_set_cd primary key,
setnome varchar2(30) constraint nm_set_nome not null);
alter table setor rename column setnome to nome;
desc setor
insert into setor values (10,'Financeiro');
insert into setor values (20,'Informática');
commit;

 

alter table socio add setor number(3) not null references setor

 

create table dependente (socio char(11) not null references socio,
numero number(4) primary key,
nome varchar(30) not null,
datanasc date not null)
desc dependente
insert into dependente values('11111111111',100,'Gustavo','26-feb-00');
insert into dependente values('21111111111',101,'Mariana','06-mar-10');
commit;
-- exibindo o nome das constraints
select constRaint_name, constraint_type from user_constraints
where table_name = 'CIDADE'

 

select * from cidade;
select * from socio;
select * from setor;
select * from dependente;


--- Bateria 2 ---

create table empregado
(nome varchar2(50) constraint nm_emp_cd not null,
rua varchar2(100) constraint nm_rua_cd not null,
cidade varchar2(30),
estado_civil varchar(15));

alter table empregado add salario numeber(11) not null
select * from empregado


create table questao
id_questão number (5) constraint questao_id_pk primary key,
pergunta varchar2(5000) not null,
resposta varchar2(5000) not null,
id_aula number (5) constraint aula_id_fk references aula

create table aula 
id_aula number (5) constraint 
desc questao