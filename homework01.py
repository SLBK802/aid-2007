"""
2. 创建一个数据库 books 使用utf8
          该数据库下创建数据表 book
          id  书名  作者 出版  价格  备注


          字段类型和约束自己设计
          在该表中插入若干数据  （>=8条）
          价格 --》  30  --120
"""
"""
create table book(id tinyint primary key auto_increment,name varchar(30) not null,writer varchar(20) not null,press char(20) not null,price decimal(5,2) unsigned default 0.00 ,remark text);

"""