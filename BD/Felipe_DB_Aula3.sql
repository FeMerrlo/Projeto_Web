alter table nome_tabela
opções 
add column     - nova coluna
add constraint - nova regra
modi


eliminando uma tabela


drop table nome_tabela
drop table tb_teste

create table tb_teste1
(codigo number(1) primary key)
create table tb_teste2
(codigo number(1) references tb_teste1)
insert into tb_teste1 values(1)
insert into tb_teste1 values(2)
drop table tb_teste1 cascade constraints 
uso do cascade permite eliminar o relacionamento dpois dropar a tebela

Atualizando dados
Update

Para utilizar filtros de linha vamos trabalhar com os operadores:

Aritimeicos: + - * / ()
relacionais: > >= < <= = != ou <>
lóicos: and or not

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


update produto_tb set val_unit = (val_unit*1.15)
where cod_prod >30 ;
select * from produto_tb
commit;



