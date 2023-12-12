/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - lifeline
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`lifeline` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `lifeline`;

/*Table structure for table `assign` */

DROP TABLE IF EXISTS `assign`;

CREATE TABLE `assign` (
  `Assign_id` int(10) NOT NULL AUTO_INCREMENT,
  `Login_id` int(10) NOT NULL,
  `Agent_id` int(11) NOT NULL,
  `Request_id` int(10) NOT NULL,
  `Status` varchar(200) NOT NULL,
  PRIMARY KEY (`Assign_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `assign` */

insert  into `assign`(`Assign_id`,`Login_id`,`Agent_id`,`Request_id`,`Status`) values 
(1,2,5,2,'delivered'),
(2,2,5,4,'delivered'),
(3,2,5,2,'delivered');

/*Table structure for table `deliveryagent` */

DROP TABLE IF EXISTS `deliveryagent`;

CREATE TABLE `deliveryagent` (
  `Agent_id` int(10) NOT NULL AUTO_INCREMENT,
  `Login_id` int(10) NOT NULL,
  `First_Name` varchar(50) NOT NULL,
  `Last_Name` varchar(50) NOT NULL,
  `Gender` char(10) NOT NULL,
  `Date` date DEFAULT NULL,
  `Place` varchar(50) NOT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `Phone` bigint(10) NOT NULL,
  PRIMARY KEY (`Agent_id`),
  UNIQUE KEY `Email` (`Email`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `deliveryagent` */

insert  into `deliveryagent`(`Agent_id`,`Login_id`,`First_Name`,`Last_Name`,`Gender`,`Date`,`Place`,`Email`,`Phone`) values 
(1,3,'ashwanth','sidu','Male','2019-12-05','nlmbr','shareef3533@gmail.com',9564741254),
(3,5,'first','agent','Male','2019-11-28','qwert','keytechno@gmail.com',9864645455);

/*Table structure for table `donor` */

DROP TABLE IF EXISTS `donor`;

CREATE TABLE `donor` (
  `Donor_id` int(10) NOT NULL AUTO_INCREMENT,
  `Login_id` int(10) DEFAULT NULL,
  `First_Name` varchar(50) NOT NULL,
  `Last_Name` varchar(50) NOT NULL,
  `gender` varchar(15) DEFAULT NULL,
  `DOB` date NOT NULL,
  `Place` varchar(50) NOT NULL,
  `Post` varchar(50) NOT NULL,
  `Pin` int(10) NOT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `Phone` bigint(10) NOT NULL,
  PRIMARY KEY (`Donor_id`),
  UNIQUE KEY `Email` (`Email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `donor` */

insert  into `donor`(`Donor_id`,`Login_id`,`First_Name`,`Last_Name`,`gender`,`DOB`,`Place`,`Post`,`Pin`,`Email`,`Phone`) values 
(1,2,'shafeen','shaz','MALE','2019-11-28','PMNA','vlr',653366,'shafeen@gmail.com',7034665325),
(2,8,'donor','donor','MALE','2019-12-11','qwerty','asdfg',123456,'basictechno01@gmail.com',7834455176);

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `Feedback_id` int(10) NOT NULL AUTO_INCREMENT,
  `Login_id` int(10) NOT NULL,
  `Feedback` varchar(200) NOT NULL,
  `Date` date NOT NULL,
  PRIMARY KEY (`Feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`Feedback_id`,`Login_id`,`Feedback`,`Date`) values 
(2,6,'fxhxhxjcv','2021-09-01');

/*Table structure for table `item` */

DROP TABLE IF EXISTS `item`;

CREATE TABLE `item` (
  `Item_id` int(10) NOT NULL AUTO_INCREMENT,
  `Login_id` int(10) NOT NULL,
  `Item_type` varchar(60) NOT NULL,
  `Item_name` varchar(100) NOT NULL,
  `Quantity` int(11) NOT NULL,
  PRIMARY KEY (`Item_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `item` */

insert  into `item`(`Item_id`,`Login_id`,`Item_type`,`Item_name`,`Quantity`) values 
(1,2,'Food','meals',12),
(2,2,'Medicine','paracetamol',500),
(4,2,'Cloths','shirt',10);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `Login_id` int(10) NOT NULL AUTO_INCREMENT,
  `Username` varchar(50) NOT NULL,
  `Password` varchar(50) NOT NULL,
  `User_Type` varchar(50) NOT NULL,
  PRIMARY KEY (`Login_id`),
  UNIQUE KEY `Username` (`Username`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`Login_id`,`Username`,`Password`,`User_Type`) values 
(1,'admin','admin','Admin'),
(2,'donorshafeen','donor','Donor'),
(3,'agent1','donor','deliver_agent'),
(5,'new','new','deliver_agent'),
(6,'user1','user','user'),
(7,'user2','user','user'),
(8,'donor','donor','Donor');

/*Table structure for table `report` */

DROP TABLE IF EXISTS `report`;

CREATE TABLE `report` (
  `Report_id` int(10) NOT NULL AUTO_INCREMENT,
  `Login_id` int(10) NOT NULL,
  `Date` date NOT NULL,
  `Report` varchar(200) NOT NULL,
  PRIMARY KEY (`Report_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `report` */

insert  into `report`(`Report_id`,`Login_id`,`Date`,`Report`) values 
(1,2,'2021-09-01','file');

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `Request_id` int(10) NOT NULL AUTO_INCREMENT,
  `Login_id` int(10) NOT NULL,
  `Item_id` int(10) NOT NULL,
  `Description` varchar(200) NOT NULL,
  `Donor_id` int(11) NOT NULL,
  `Status` varchar(200) NOT NULL,
  `Date` date NOT NULL,
  PRIMARY KEY (`Request_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `request` */

insert  into `request`(`Request_id`,`Login_id`,`Item_id`,`Description`,`Donor_id`,`Status`,`Date`) values 
(2,6,1,'needddss',2,'pending','2021-09-01'),
(3,6,2,'needs',2,'pending','2021-09-01'),
(4,7,4,'needed',2,'pending','2021-09-01');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `User_id` int(10) NOT NULL AUTO_INCREMENT,
  `Login_id` int(10) NOT NULL,
  `First_Name` varchar(50) NOT NULL,
  `Last_Name` varchar(50) NOT NULL,
  `Place` varchar(50) NOT NULL,
  `Post` varchar(50) NOT NULL,
  `Pin` int(10) NOT NULL,
  `District` varchar(50) NOT NULL,
  `Phone` bigint(10) NOT NULL,
  `Email` varchar(50) NOT NULL,
  PRIMARY KEY (`User_id`),
  UNIQUE KEY `Email` (`Email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`User_id`,`Login_id`,`First_Name`,`Last_Name`,`Place`,`Post`,`Pin`,`District`,`Phone`,`Email`) values 
(1,6,'user','mon','pmna','pmnas',147852,'mlpm',7043465892,'user@gmail.com'),
(2,7,'krishnajith','k','pmna','pmnas',369852,'mlpm',7034655855,'user2@gmail.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
