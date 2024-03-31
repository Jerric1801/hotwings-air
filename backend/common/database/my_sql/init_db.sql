
CREATE DATABASE IF NOT EXISTS `prices`;


GRANT ALL PRIVILEGES ON prices.* TO 'root'@'%' IDENTIFIED BY 'strong_password'; 
FLUSH PRIVILEGES;


USE `prices`;


DROP TABLE IF EXISTS `flight_pricing`; 


CREATE TABLE IF NOT EXISTS `flight_pricing` (
`pricing_id` int(11) NOT NULL AUTO_INCREMENT,
`flight_number` varchar(15) NOT NULL, 
`seat_class` varchar(15) NOT NULL,
`price` float(10) NOT NULL,
`created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
`modified` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (`pricing_id`),
INDEX (`flight_number`) -- Add an index on flight_id
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;



INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW916', 'First', 1167.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW916', 'Business', 817.25); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW916', 'Premium Economy', 574.41); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW916', 'Economy', 467.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW390', 'First', 390.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW390', 'Business', 273.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW390', 'Premium Economy', 191.88); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW390', 'Economy', 156.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW122', 'First', 790.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW122', 'Business', 553.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW122', 'Premium Economy', 388.68); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW122', 'Economy', 316.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW946', 'First', 1042.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW946', 'Business', 729.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW946', 'Premium Economy', 512.91); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW946', 'Economy', 417.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW841', 'First', 2352.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW841', 'Business', 1646.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW841', 'Premium Economy', 1157.43); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW841', 'Economy', 941.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW713', 'First', 1597.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW713', 'Business', 1118.25); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW713', 'Premium Economy', 785.97); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW713', 'Economy', 639.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW878', 'First', 437.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW878', 'Business', 306.25); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW878', 'Premium Economy', 215.25); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW878', 'Economy', 175.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW674', 'First', 255.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW674', 'Business', 178.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW674', 'Premium Economy', 125.46); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW674', 'Economy', 102.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW611', 'First', 697.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW611', 'Business', 488.25); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW611', 'Premium Economy', 343.17); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW611', 'Economy', 279.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW865', 'First', 1362.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW865', 'Business', 953.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW865', 'Premium Economy', 670.35); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW865', 'Economy', 545.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW833', 'First', 1565.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW833', 'Business', 1095.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW833', 'Premium Economy', 769.98); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW833', 'Economy', 626.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW888', 'First', 2472.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW888', 'Business', 1730.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW888', 'Premium Economy', 1216.47); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW888', 'Economy', 989.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW733', 'First', 1495.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW733', 'Business', 1046.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW733', 'Premium Economy', 735.54); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW733', 'Economy', 598.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW729', 'First', 1102.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW729', 'Business', 771.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW729', 'Premium Economy', 542.43); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW729', 'Economy', 441.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW595', 'First', 1185.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW595', 'Business', 829.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW595', 'Premium Economy', 583.02); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW595', 'Economy', 474.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW574', 'First', 490.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW574', 'Business', 343.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW574', 'Premium Economy', 241.08); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW574', 'Economy', 196.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW242', 'First', 2105.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW242', 'Business', 1473.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW242', 'Premium Economy', 1035.66); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW242', 'Economy', 842.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW589', 'First', 1610.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW589', 'Business', 1127.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW589', 'Premium Economy', 792.12); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW589', 'Economy', 644.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW420', 'First', 885.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW420', 'Business', 619.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW420', 'Premium Economy', 435.42); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW420', 'Economy', 354.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW454', 'First', 905.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW454', 'Business', 633.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW454', 'Premium Economy', 445.26); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW454', 'Economy', 362.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW181', 'First', 1210.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW181', 'Business', 847.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW181', 'Premium Economy', 595.32); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW181', 'Economy', 484.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW842', 'First', 1685.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW842', 'Business', 1179.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW842', 'Premium Economy', 829.02); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW842', 'Economy', 674.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW210', 'First', 2380.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW210', 'Business', 1666.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW210', 'Premium Economy', 1170.96); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW210', 'Economy', 952.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW631', 'First', 1560.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW631', 'Business', 1092.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW631', 'Premium Economy', 767.52); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW631', 'Economy', 624.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW669', 'First', 585.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW669', 'Business', 409.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW669', 'Premium Economy', 287.82); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW669', 'Economy', 234.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW601', 'First', 1182.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW601', 'Business', 827.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW601', 'Premium Economy', 581.79); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW601', 'Economy', 473.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW358', 'First', 752.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW358', 'Business', 526.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW358', 'Premium Economy', 370.23); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW358', 'Economy', 301.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW197', 'First', 1412.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW197', 'Business', 988.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW197', 'Premium Economy', 694.95); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW197', 'Economy', 565.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW983', 'First', 1820.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW983', 'Business', 1274.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW983', 'Premium Economy', 895.44); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW983', 'Economy', 728.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW763', 'First', 2235.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW763', 'Business', 1564.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW763', 'Premium Economy', 1099.62); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW763', 'Economy', 894.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW745', 'First', 612.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW745', 'Business', 428.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW745', 'Premium Economy', 301.35); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW745', 'Economy', 245.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW850', 'First', 337.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW850', 'Business', 236.25); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW850', 'Premium Economy', 166.05); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW850', 'Economy', 135.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW516', 'First', 340.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW516', 'Business', 238.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW516', 'Premium Economy', 167.28); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW516', 'Economy', 136.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW515', 'First', 982.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW515', 'Business', 687.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW515', 'Premium Economy', 483.39); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW515', 'Economy', 393.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW922', 'First', 1802.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW922', 'Business', 1261.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW922', 'Premium Economy', 886.83); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW922', 'Economy', 721.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW327', 'First', 2200.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW327', 'Business', 1540.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW327', 'Premium Economy', 1082.4); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW327', 'Economy', 880.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW768', 'First', 1360.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW768', 'Business', 952.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW768', 'Premium Economy', 669.12); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW768', 'Economy', 544.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW292', 'First', 1125.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW292', 'Business', 787.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW292', 'Premium Economy', 553.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW292', 'Economy', 450.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW598', 'First', 905.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW598', 'Business', 633.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW598', 'Premium Economy', 445.26); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW598', 'Economy', 362.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW446', 'First', 1175.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW446', 'Business', 822.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW446', 'Premium Economy', 578.1); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW446', 'Economy', 470.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW592', 'First', 2220.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW592', 'Business', 1554.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW592', 'Premium Economy', 1092.24); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW592', 'Economy', 888.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW560', 'First', 982.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW560', 'Business', 687.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW560', 'Premium Economy', 483.39); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW560', 'Economy', 393.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW401', 'First', 1265.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW401', 'Business', 885.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW401', 'Premium Economy', 622.38); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW401', 'Economy', 506.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW409', 'First', 782.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW409', 'Business', 547.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW409', 'Premium Economy', 384.99); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW409', 'Economy', 313.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW996', 'First', 1442.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW996', 'Business', 1009.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW996', 'Premium Economy', 709.71); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW996', 'Economy', 577.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW948', 'First', 1812.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW948', 'Business', 1268.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW948', 'Premium Economy', 891.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW948', 'Economy', 725.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW369', 'First', 1555.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW369', 'Business', 1088.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW369', 'Premium Economy', 765.06); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW369', 'Economy', 622.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW615', 'First', 1145.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW615', 'Business', 801.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW615', 'Premium Economy', 563.34); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW615', 'Economy', 458.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW257', 'First', 1422.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW257', 'Business', 995.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW257', 'Premium Economy', 699.87); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW257', 'Economy', 569.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW872', 'First', 540.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW872', 'Business', 378.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW872', 'Premium Economy', 265.68); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW872', 'Economy', 216.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW749', 'First', 1300.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW749', 'Business', 910.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW749', 'Premium Economy', 639.6); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW749', 'Economy', 520.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW800', 'First', 1177.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW800', 'Business', 824.25); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW800', 'Premium Economy', 579.33); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW800', 'Economy', 471.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW352', 'First', 1752.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW352', 'Business', 1226.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW352', 'Premium Economy', 862.23); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW352', 'Economy', 701.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW742', 'First', 2490.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW742', 'Business', 1743.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW742', 'Premium Economy', 1225.08); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW742', 'Economy', 996.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW829', 'First', 970.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW829', 'Business', 679.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW829', 'Premium Economy', 477.24); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW829', 'Economy', 388.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW356', 'First', 970.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW356', 'Business', 679.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW356', 'Premium Economy', 477.24); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW356', 'Economy', 388.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW254', 'First', 812.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW254', 'Business', 568.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW254', 'Premium Economy', 399.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW254', 'Economy', 325.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW303', 'First', 2152.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW303', 'Business', 1506.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW303', 'Premium Economy', 1059.03); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW303', 'Economy', 861.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW721', 'First', 2082.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW721', 'Business', 1457.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW721', 'Premium Economy', 1024.59); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW721', 'Economy', 833.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW679', 'First', 1742.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW679', 'Business', 1219.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW679', 'Premium Economy', 857.31); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW679', 'Economy', 697.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW279', 'First', 2307.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW279', 'Business', 1615.25); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW279', 'Premium Economy', 1135.29); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW279', 'Economy', 923.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW740', 'First', 2215.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW740', 'Business', 1550.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW740', 'Premium Economy', 1089.78); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW740', 'Economy', 886.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW398', 'First', 1655.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW398', 'Business', 1158.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW398', 'Premium Economy', 814.26); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW398', 'Economy', 662.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW314', 'First', 1925.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW314', 'Business', 1347.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW314', 'Premium Economy', 947.1); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW314', 'Economy', 770.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW331', 'First', 2347.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW331', 'Business', 1643.25); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW331', 'Premium Economy', 1154.97); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW331', 'Economy', 939.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW994', 'First', 1415.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW994', 'Business', 990.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW994', 'Premium Economy', 696.18); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW994', 'Economy', 566.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW337', 'First', 2322.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW337', 'Business', 1625.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW337', 'Premium Economy', 1142.67); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW337', 'Economy', 929.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW377', 'First', 1810.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW377', 'Business', 1267.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW377', 'Premium Economy', 890.52); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW377', 'Economy', 724.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW306', 'First', 2352.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW306', 'Business', 1646.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW306', 'Premium Economy', 1157.43); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW306', 'Economy', 941.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW250', 'First', 1042.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW250', 'Business', 729.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW250', 'Premium Economy', 512.91); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW250', 'Economy', 417.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW779', 'First', 485.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW779', 'Business', 339.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW779', 'Premium Economy', 238.62); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW779', 'Economy', 194.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW542', 'First', 1390.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW542', 'Business', 973.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW542', 'Premium Economy', 683.88); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW542', 'Economy', 556.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW391', 'First', 1535.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW391', 'Business', 1074.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW391', 'Premium Economy', 755.22); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW391', 'Economy', 614.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW495', 'First', 1877.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW495', 'Business', 1314.25); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW495', 'Premium Economy', 923.73); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW495', 'Economy', 751.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW422', 'First', 2332.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW422', 'Business', 1632.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW422', 'Premium Economy', 1147.59); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW422', 'Economy', 933.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW774', 'First', 1162.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW774', 'Business', 813.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW774', 'Premium Economy', 571.95); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW774', 'Economy', 465.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW384', 'First', 2217.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW384', 'Business', 1552.25); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW384', 'Premium Economy', 1091.01); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW384', 'Economy', 887.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW147', 'First', 1190.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW147', 'Business', 833.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW147', 'Premium Economy', 585.48); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW147', 'Economy', 476.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW546', 'First', 2465.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW546', 'Business', 1725.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW546', 'Premium Economy', 1212.78); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW546', 'Economy', 986.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW474', 'First', 2115.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW474', 'Business', 1480.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW474', 'Premium Economy', 1040.58); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW474', 'Economy', 846.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW232', 'First', 1742.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW232', 'Business', 1219.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW232', 'Premium Economy', 857.31); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW232', 'Economy', 697.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW693', 'First', 1767.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW693', 'Business', 1237.25); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW693', 'Premium Economy', 869.61); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW693', 'Economy', 707.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW642', 'First', 1225.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW642', 'Business', 857.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW642', 'Premium Economy', 602.7); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW642', 'Economy', 490.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW830', 'First', 720.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW830', 'Business', 504.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW830', 'Premium Economy', 354.24); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW830', 'Economy', 288.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW626', 'First', 362.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW626', 'Business', 253.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW626', 'Premium Economy', 178.35); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW626', 'Economy', 145.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW346', 'First', 1377.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW346', 'Business', 964.25); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW346', 'Premium Economy', 677.73); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW346', 'Economy', 551.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW646', 'First', 380.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW646', 'Business', 266.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW646', 'Premium Economy', 186.96); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW646', 'Economy', 152.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW362', 'First', 947.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW362', 'Business', 663.25); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW362', 'Premium Economy', 466.17); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW362', 'Economy', 379.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW614', 'First', 845.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW614', 'Business', 591.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW614', 'Premium Economy', 415.74); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW614', 'Economy', 338.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW997', 'First', 2147.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW997', 'Business', 1503.25); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW997', 'Premium Economy', 1056.57); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW997', 'Economy', 859.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW470', 'First', 1850.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW470', 'Business', 1295.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW470', 'Premium Economy', 910.2); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW470', 'Economy', 740.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW955', 'First', 302.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW955', 'Business', 211.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW955', 'Premium Economy', 148.83); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW955', 'Economy', 121.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW773', 'First', 552.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW773', 'Business', 386.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW773', 'Premium Economy', 271.83); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW773', 'Economy', 221.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW436', 'First', 1090.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW436', 'Business', 763.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW436', 'Premium Economy', 536.28); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW436', 'Economy', 436.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW123', 'First', 1570.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW123', 'Business', 1099.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW123', 'Premium Economy', 772.44); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW123', 'Economy', 628.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW239', 'First', 1702.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW239', 'Business', 1191.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW239', 'Premium Economy', 837.63); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW239', 'Economy', 681.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW222', 'First', 420.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW222', 'Business', 294.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW222', 'Premium Economy', 206.64); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW222', 'Economy', 168.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW330', 'First', 922.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW330', 'Business', 645.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW330', 'Premium Economy', 453.87); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW330', 'Economy', 369.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW698', 'First', 337.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW698', 'Business', 236.25); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW698', 'Premium Economy', 166.05); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW698', 'Economy', 135.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW672', 'First', 795.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW672', 'Business', 556.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW672', 'Premium Economy', 391.14); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW672', 'Economy', 318.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW790', 'First', 1052.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW790', 'Business', 736.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW790', 'Premium Economy', 517.83); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW790', 'Economy', 421.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW610', 'First', 1512.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW610', 'Business', 1058.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW610', 'Premium Economy', 744.15); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW610', 'Economy', 605.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW968', 'First', 2092.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW968', 'Business', 1464.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW968', 'Premium Economy', 1029.51); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW968', 'Economy', 837.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW429', 'First', 590.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW429', 'Business', 413.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW429', 'Premium Economy', 290.28); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW429', 'Economy', 236.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW333', 'First', 350.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW333', 'Business', 245.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW333', 'Premium Economy', 172.2); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW333', 'Economy', 140.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW797', 'First', 860.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW797', 'Business', 602.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW797', 'Premium Economy', 423.12); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW797', 'Economy', 344.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW896', 'First', 1582.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW896', 'Business', 1107.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW896', 'Premium Economy', 778.59); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW896', 'Economy', 633.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW838', 'First', 2265.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW838', 'Business', 1585.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW838', 'Premium Economy', 1114.38); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW838', 'Economy', 906.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW537', 'First', 640.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW537', 'Business', 448.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW537', 'Premium Economy', 314.88); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW537', 'Economy', 256.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW359', 'First', 1117.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW359', 'Business', 782.25); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW359', 'Premium Economy', 549.81); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW359', 'Economy', 447.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW478', 'First', 300.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW478', 'Business', 210.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW478', 'Premium Economy', 147.6); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW478', 'Economy', 120.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW295', 'First', 1107.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW295', 'Business', 775.25); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW295', 'Premium Economy', 544.89); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW295', 'Economy', 443.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW607', 'First', 1075.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW607', 'Business', 752.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW607', 'Premium Economy', 528.9); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW607', 'Economy', 430.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW266', 'First', 2417.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW266', 'Business', 1692.25); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW266', 'Premium Economy', 1189.41); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW266', 'Economy', 967.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW259', 'First', 1942.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW259', 'Business', 1359.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW259', 'Premium Economy', 955.71); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW259', 'Economy', 777.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW588', 'First', 725.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW588', 'Business', 507.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW588', 'Premium Economy', 356.7); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW588', 'Economy', 290.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW244', 'First', 665.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW244', 'Business', 465.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW244', 'Premium Economy', 327.18); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW244', 'Economy', 266.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW756', 'First', 902.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW756', 'Business', 631.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW756', 'Premium Economy', 444.03); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW756', 'Economy', 361.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW203', 'First', 2410.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW203', 'Business', 1687.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW203', 'Premium Economy', 1185.72); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW203', 'Economy', 964.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW754', 'First', 1805.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW754', 'Business', 1263.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW754', 'Premium Economy', 888.06); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW754', 'Economy', 722.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW184', 'First', 817.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW184', 'Business', 572.25); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW184', 'Premium Economy', 402.21); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW184', 'Economy', 327.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW937', 'First', 2327.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW937', 'Business', 1629.25); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW937', 'Premium Economy', 1145.13); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW937', 'Economy', 931.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW904', 'First', 1482.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW904', 'Business', 1037.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW904', 'Premium Economy', 729.39); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW904', 'Economy', 593.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW929', 'First', 2395.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW929', 'Business', 1676.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW929', 'Premium Economy', 1178.34); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW929', 'Economy', 958.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW117', 'First', 1812.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW117', 'Business', 1268.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW117', 'Premium Economy', 891.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW117', 'Economy', 725.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW682', 'First', 1130.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW682', 'Business', 791.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW682', 'Premium Economy', 555.96); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW682', 'Economy', 452.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW858', 'First', 1882.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW858', 'Business', 1317.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW858', 'Premium Economy', 926.19); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW858', 'Economy', 753.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW452', 'First', 982.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW452', 'Business', 687.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW452', 'Premium Economy', 483.39); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW452', 'Economy', 393.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW624', 'First', 1275.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW624', 'Business', 892.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW624', 'Premium Economy', 627.3); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW624', 'Economy', 510.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW293', 'First', 860.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW293', 'Business', 602.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW293', 'Premium Economy', 423.12); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW293', 'Economy', 344.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW225', 'First', 1262.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW225', 'Business', 883.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW225', 'Premium Economy', 621.15); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW225', 'Economy', 505.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW144', 'First', 2195.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW144', 'Business', 1536.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW144', 'Premium Economy', 1079.94); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW144', 'Economy', 878.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW373', 'First', 1912.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW373', 'Business', 1338.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW373', 'Premium Economy', 940.95); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW373', 'Economy', 765.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW664', 'First', 1990.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW664', 'Business', 1393.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW664', 'Premium Economy', 979.08); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW664', 'Economy', 796.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW481', 'First', 1615.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW481', 'Business', 1130.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW481', 'Premium Economy', 794.58); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW481', 'Economy', 646.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW726', 'First', 1647.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW726', 'Business', 1153.25); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW726', 'Premium Economy', 810.57); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW726', 'Economy', 659.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW758', 'First', 1812.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW758', 'Business', 1268.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW758', 'Premium Economy', 891.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW758', 'Economy', 725.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW518', 'First', 610.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW518', 'Business', 427.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW518', 'Premium Economy', 300.12); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW518', 'Economy', 244.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW402', 'First', 1110.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW402', 'Business', 777.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW402', 'Premium Economy', 546.12); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW402', 'Economy', 444.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW597', 'First', 1745.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW597', 'Business', 1221.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW597', 'Premium Economy', 858.54); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW597', 'Economy', 698.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW441', 'First', 1842.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW441', 'Business', 1289.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW441', 'Premium Economy', 906.51); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW441', 'Economy', 737.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW284', 'First', 1800.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW284', 'Business', 1260.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW284', 'Premium Economy', 885.6); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW284', 'Economy', 720.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW317', 'First', 805.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW317', 'Business', 563.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW317', 'Premium Economy', 396.06); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW317', 'Economy', 322.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW707', 'First', 950.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW707', 'Business', 665.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW707', 'Premium Economy', 467.4); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW707', 'Economy', 380.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW473', 'First', 2425.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW473', 'Business', 1697.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW473', 'Premium Economy', 1193.1); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW473', 'Economy', 970.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW348', 'First', 1552.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW348', 'Business', 1086.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW348', 'Premium Economy', 763.83); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW348', 'Economy', 621.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW979', 'First', 1655.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW979', 'Business', 1158.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW979', 'Premium Economy', 814.26); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW979', 'Economy', 662.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW688', 'First', 1130.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW688', 'Business', 791.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW688', 'Premium Economy', 555.96); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW688', 'Economy', 452.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW313', 'First', 2002.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW313', 'Business', 1401.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW313', 'Premium Economy', 985.23); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW313', 'Economy', 801.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW146', 'First', 1432.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW146', 'Business', 1002.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW146', 'Premium Economy', 704.79); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW146', 'Economy', 573.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW455', 'First', 657.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW455', 'Business', 460.25); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW455', 'Premium Economy', 323.49); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW455', 'Economy', 263.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW462', 'First', 2037.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW462', 'Business', 1426.25); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW462', 'Premium Economy', 1002.45); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW462', 'Economy', 815.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW288', 'First', 2090.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW288', 'Business', 1463.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW288', 'Premium Economy', 1028.28); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW288', 'Economy', 836.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW992', 'First', 2232.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW992', 'Business', 1562.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW992', 'Premium Economy', 1098.39); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW992', 'Economy', 893.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW999', 'First', 1927.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW999', 'Business', 1349.25); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW999', 'Premium Economy', 948.33); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW999', 'Economy', 771.0); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW586', 'First', 1492.5); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW586', 'Business', 1044.75); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW586', 'Premium Economy', 734.31); 
    

INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('HW586', 'Economy', 597.0); 
    
