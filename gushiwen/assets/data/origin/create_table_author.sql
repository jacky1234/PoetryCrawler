CREATE TABLE IF NOT EXISTS `poetdb`.`author`  (
id varchar(32) PRIMARY KEY,
name varchar(64),
chaodai varchar(32),
src varchar(64),
shiCount INTEGER,
content text
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;
