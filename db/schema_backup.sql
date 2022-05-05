drop table if exists entries;

create table messages (
  id integer primary key autoincrement,
  'text' text not null
);
