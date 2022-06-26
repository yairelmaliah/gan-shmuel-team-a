CREATE DATABASE IF NOT EXISTS `weight`;

USE weight;

CREATE TABLE IF NOT EXISTS `containers_registered` (
  `container_id` varchar(15) NOT NULL,
  `weight` int(12) DEFAULT NULL,
  `unit` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`container_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10001 ;


CREATE TABLE IF NOT EXISTS `transactions` (
  `id` int(12) NOT NULL AUTO_INCREMENT,
  `datetime` datetime DEFAULT NULL,
  `direction` varchar(10) DEFAULT NULL,
  `truck` varchar(50) DEFAULT NULL,
  `containers` varchar(10000) DEFAULT NULL,
  `bruto` int(12) DEFAULT NULL,
  `truckTara` int(12) DEFAULT NULL,
  --   "neto": <int> or "na" // na if some of containers unknown
  `neto` int(12) DEFAULT NULL,
  `produce` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=10001 ;


INSERT INTO transactions (datetime, direction, truck, containers, bruto, produce) VALUES(20220622190746, 'in', '155-34-443', 'C-1', 5000, 'Blood');
INSERT INTO transactions (datetime, direction, truck, containers, produce, neto, truckTara) VALUES(20220622190746, 'out','155-34-443', '', 'Blood', 3000, 1200);
INSERT INTO transactions (datetime, direction, truck, containers, bruto, produce) VALUES(20220622190746, 'in', '165-34-443', 'C-2,C-3', 8777, 'Mandarin');
INSERT INTO transactions (datetime, direction, truck, containers, produce, neto, truckTara) VALUES(20220622190746, 'out', '165-34-443', 'C-2', 'Mandarin',4500, 3000);
INSERT INTO transactions (datetime, direction, truck, containers, bruto, produce) VALUES(20220622190746, 'in', '195-37-443', 'C-4', 3000, 'Navel');
INSERT INTO transactions (datetime, direction, truck, containers, produce, neto, truckTara) VALUES(20220622190746, 'out', '195-37-443', '', 'Navel', 2000, 800);
INSERT INTO transactions (datetime, direction, truck, containers, bruto, produce) VALUES(20220622190746, 'in', '200-32-443', 'C-5,C-6', 4444, 'Tangerine');
INSERT INTO transactions (datetime, direction, truck, containers, produce, neto, truckTara) VALUES(20220622160746, 'out', '200-32-443', 'C-6', 'Tangerine', 3000, 1300);
