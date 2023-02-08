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
 (cd_fun number(3) constraint fun_cd_pk1 primaru key,
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