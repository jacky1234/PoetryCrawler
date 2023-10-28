CREATE TABLE IF NOT EXISTS `poetdb`.`poet`  (
id INT AUTO_INCREMENT PRIMARY KEY,
name varchar(64),
dynasty varchar(32),
author varchar(32),
content text,
tag text,
fanyi text,
zhushi text,
cankao text,
shangxi text
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;
