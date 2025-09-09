create database deneme;
use deneme
create table deneme1 ( id int primary key, name varchar(250))
insert into deneme1 values (0,'abc');
select name from deneme1 where id=0;
create user 'denemeu'@'%' identified with mysql_native_password by 'denemep';
grant all on deneme.* to 'denemeu'@'%';


