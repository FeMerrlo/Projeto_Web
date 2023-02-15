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
 
 desc cargo
 create table funcionaio
 (cd_fun number(3) constraint fun_cd_pk1 primary key,
 nm_fun varchar(30) constraint fun_nm_nn1 not null,
 dt_adm date constraint fun dt_nn1 not null,
 uf_fun char(2) constraint fun_uf_nn1 not null,
 cargo_fk number(3) constraint fun_cargo_fk references cargo)
 
 desc funcionaio
 
 Criação das tabelas: n_fiscal e produto
 create table N_Fiscal
(cd_cargo number(3),
nm_cargo varchar2(25),
salaio number(8,2));

--Ex 1--

create table cliente
(Cod_Cli number(4) constraint Cli_Cod_pk1 primary key,
Prenome varchar(50) constraint Cli_Prenome_nnl not null,
Sobrenome varchar(50),
Endereco varchar(70),
Telefone varchar(20));

desc cliente


create table DVD 
(Num_DVD number(4) constraint DVD_Num_pk1 primary key,
Tipo char(1));

desc DVD


create table Filme
(Num_Filme number(4) constraint Filme_Num_pk1 primary key,
Tipo char(1));

desc Filme


create table Ator
(Num_Codator number(4) constraint Cotador_Num_pk1 primary key,
Nome_Popular varchar(50) constraint Popular_Nome_nnl not null,
Nome_Artistico varchar(50),
Datanasc date);

desc Ator


insert into cliente values (1,'João','Silva','Rua da Cruz sem Pé',4444-1111);
insert into cliente values (2,'Antônio','Ferreira','Av. da Vila Velha',6660-9333);
insert into cliente values (3,'Fabio','Dias','Rua Antonio Vieira',2337-0393);
insert into cliente values (4,'Andreia','Melo','Rua da Praia Bonita',8989-7777);
insert into cliente values (5,'Murilo','Fontes','Av. dos Autonomistas',9090-9090);
select * from cliente

insert into Filme values (1,'Sai pra lá',1);
insert into Filme values (2,'Ajuda Eterna',2);
insert into Filme values (3,'Anjos Malditos',2);

