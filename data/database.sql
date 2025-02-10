create database if not exists `agenda`;
use agenda;

create table if not exists `tarefa`(
    `id` int not null `auto_increment` primary key,
    `titulo` varchar(60) not null,
    `data_conclusao` datetime null
)
