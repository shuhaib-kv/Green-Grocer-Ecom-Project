/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - green grocer
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`green grocer` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `green grocer`;

/*Table structure for table `bill table` */

DROP TABLE IF EXISTS `bill table`;

CREATE TABLE `bill table` (
  `billid` int(11) NOT NULL AUTO_INCREMENT,
  `userloginid` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `totalamount` varchar(40) DEFAULT NULL,
  `status` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`billid`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `bill table` */

insert  into `bill table`(`billid`,`userloginid`,`date`,`totalamount`,`status`) values 
(12,5,'2021-08-27','2000','paid'),
(13,NULL,NULL,NULL,NULL);

/*Table structure for table `farmers` */

DROP TABLE IF EXISTS `farmers`;

CREATE TABLE `farmers` (
  `farmerid` int(11) NOT NULL AUTO_INCREMENT,
  `farmerloginid` int(11) DEFAULT NULL,
  `firstname` varchar(40) DEFAULT NULL,
  `lastname` varchar(40) DEFAULT NULL,
  `place` varchar(40) DEFAULT NULL,
  `post` varchar(40) DEFAULT NULL,
  `pin` int(11) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`farmerid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `farmers` */

insert  into `farmers`(`farmerid`,`farmerloginid`,`firstname`,`lastname`,`place`,`post`,`pin`,`phone`) values 
(1,2,'shamshad','ali','amkd','tkd',999999,7894561230);

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedbackid` int(11) NOT NULL AUTO_INCREMENT,
  `userloginid` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `rating` varchar(40) DEFAULT NULL,
  `feedback` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`feedbackid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedbackid`,`userloginid`,`date`,`rating`,`feedback`) values 
(1,5,'2021-09-17','10','good app for farmers'),
(2,6,'2021-09-16','10','very good bbbhhgdkjssjju');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(40) DEFAULT NULL,
  `password` varchar(40) DEFAULT NULL,
  `type` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`id`,`username`,`password`,`type`) values 
(1,'shuhaib','123','admin'),
(2,'shamshad','321','farmer'),
(3,'sarath','147','user');

/*Table structure for table `order` */

DROP TABLE IF EXISTS `order`;

CREATE TABLE `order` (
  `orderid` int(11) NOT NULL AUTO_INCREMENT,
  `billid` int(11) DEFAULT NULL,
  `userid` int(11) DEFAULT NULL,
  `itemid` int(11) DEFAULT NULL,
  `quandity` varchar(40) DEFAULT NULL,
  `amount` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`orderid`)
) ENGINE=InnoDB AUTO_INCREMENT=133 DEFAULT CHARSET=latin1;

/*Data for the table `order` */

insert  into `order`(`orderid`,`billid`,`userid`,`itemid`,`quandity`,`amount`) values 
(8,12,9,7,'12','88'),
(12,12,5,8,'45','96'),
(132,13,2,5,'22','200');

/*Table structure for table `payments` */

DROP TABLE IF EXISTS `payments`;

CREATE TABLE `payments` (
  `bankid` int(11) NOT NULL AUTO_INCREMENT,
  `bank` varchar(40) DEFAULT NULL,
  `ifccode` int(11) DEFAULT NULL,
  `accountnumber` varchar(40) DEFAULT NULL,
  `key` int(11) DEFAULT NULL,
  `amount` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`bankid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `payments` */

insert  into `payments`(`bankid`,`bank`,`ifccode`,`accountnumber`,`key`,`amount`) values 
(1,NULL,NULL,NULL,0,NULL);

/*Table structure for table `products` */

DROP TABLE IF EXISTS `products`;

CREATE TABLE `products` (
  `productid` int(11) NOT NULL AUTO_INCREMENT,
  `productname` varchar(40) DEFAULT NULL,
  `description` varchar(40) DEFAULT NULL,
  `image` varchar(40) DEFAULT NULL,
  `wholesaleprice` float DEFAULT NULL,
  `retailprice` float DEFAULT NULL,
  `quandity` varchar(40) DEFAULT NULL,
  `type` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`productid`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

/*Data for the table `products` */

insert  into `products`(`productid`,`productname`,`description`,`image`,`wholesaleprice`,`retailprice`,`quandity`,`type`) values 
(8,'mango','FRUITS','good',0,25,'35','SEEDS');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `userid` int(11) NOT NULL AUTO_INCREMENT,
  `userloginid` int(11) DEFAULT NULL,
  `firstname` varchar(40) DEFAULT NULL,
  `lastname` varchar(40) DEFAULT NULL,
  `place` varchar(40) DEFAULT NULL,
  `post` varchar(40) DEFAULT NULL,
  `pin` int(11) DEFAULT NULL,
  `email` varchar(40) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`userid`,`userloginid`,`firstname`,`lastname`,`place`,`post`,`pin`,`email`,`phone`) values 
(1,5,'muthasir','hafi','pod','ius',852,'dhsjahsjh',99613886),
(2,6,'fais','mhdd','aws','ssd',6665,'sdsasd',56465656),
(9,12,'shau','hj','jjhdj','jhdj',55,'hjd',5464465);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
