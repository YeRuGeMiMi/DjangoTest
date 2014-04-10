/*
SQLyog 企业版 - MySQL GUI v8.14 
MySQL - 5.5.25 : Database - yfl_dev
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`yfl_dev` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `yfl_dev`;

/*Table structure for table `qa_qlist` */

DROP TABLE IF EXISTS `qa_qlist`;

CREATE TABLE `qa_qlist` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `question` varchar(255) NOT NULL COMMENT '问题',
  `answer` varchar(255) NOT NULL COMMENT '回答',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

/*Data for the table `qa_qlist` */

insert  into `qa_qlist`(`id`,`question`,`answer`) values (1,'1+1等于几？','二'),(2,'我想和你好好的','去你丫的'),(3,'你妹叫什么名字？','叫你妹'),(4,'今天你打卡了吗？','打你妹呀'),(5,'你就会你妹呀？','哈哈'),(6,'你当我是傻逼啊？','你就是个傻逼'),(7,'——————','傻逼'),(8,'哈希表','hashTable'),(9,'涂雯雯','打错了'),(10,'涂雯雯','打错了'),(11,'呵呵','女神的微笑'),(12,'呵呵','女神微笑'),(13,'呵呵是什么','女神的微笑'),(14,'女神是什么','女神经病的简称');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
