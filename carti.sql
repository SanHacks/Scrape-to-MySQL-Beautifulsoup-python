
CREATE TABLE IF NOT EXISTS `products`(
`ID` int(11) DEFAULT NOT NULL AUTO_INCREMENT,
`PRODUCT` varchar(500) DEFAULT NULL,
`PRICE` varchar() DEFAULT NULL,
`BRAND` varchar() DEFAULT NULL,
`SHOP` varchar() DEFAULT NULL,
`IMAGE` varchar() DEFAULT NULL,
`TIMESTAMP` int(11) DEAFAULT NULL
PRIMARY KEY(`ID`)
);
