create table if not exists users (
    id INT auto_increment primary key,
    username VARCHAR(50) not null unique,
    pass VARCHAR(10) not null,
    created_at TIMESTAMP default CURRENT_TIMESTAMP
);

insert into users (username, pass) values('user1','password1');
insert into users (username, pass) values('user2','password2');
insert into users (username, pass) values('user3','password3');
select * from users u