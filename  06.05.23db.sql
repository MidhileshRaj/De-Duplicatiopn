/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 5.6.12-log : Database - deduplication
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`deduplication` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `deduplication`;

/*Table structure for table `assignment&seminar` */

DROP TABLE IF EXISTS `assignment&seminar`;

CREATE TABLE `assignment&seminar` (
  `assignment_id` int(11) NOT NULL AUTO_INCREMENT,
  `teacher_id` int(11) DEFAULT NULL,
  `student_id` int(11) DEFAULT NULL,
  `date` int(30) DEFAULT NULL,
  `content` varchar(100) DEFAULT NULL,
  `last_date` int(30) DEFAULT NULL,
  `subject` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`assignment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `assignment&seminar` */

/*Table structure for table `complaints` */

DROP TABLE IF EXISTS `complaints`;

CREATE TABLE `complaints` (
  `complaints_id` int(11) NOT NULL AUTO_INCREMENT,
  `complaints` varchar(80) DEFAULT NULL,
  `user_id` int(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `reply` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`complaints_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `complaints` */

insert  into `complaints`(`complaints_id`,`complaints`,`user_id`,`date`,`reply`,`status`) values 
(1,'not working',2,'2023-01-11','will get back to  you soon','replied'),
(2,'',0,'0000-00-00','',''),
(3,'iojjf',8,'2023-04-29','pending','pending');

/*Table structure for table `course` */

DROP TABLE IF EXISTS `course`;

CREATE TABLE `course` (
  `course_id` int(11) NOT NULL AUTO_INCREMENT,
  `course` varchar(50) DEFAULT NULL,
  `department_id` int(11) DEFAULT NULL,
  `total_semester` int(50) DEFAULT NULL,
  PRIMARY KEY (`course_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `course` */

insert  into `course`(`course_id`,`course`,`department_id`,`total_semester`) values 
(3,'bcom',2,2),
(4,'ai',3,2),
(5,'ai',3,4),
(6,'biotechnology',6,2),
(7,'ai',3,4);

/*Table structure for table `department` */

DROP TABLE IF EXISTS `department`;

CREATE TABLE `department` (
  `department_id` int(11) NOT NULL AUTO_INCREMENT,
  `department` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`department_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `department` */

insert  into `department`(`department_id`,`department`) values 
(1,'\"++\"'),
(2,'ite'),
(3,'bca'),
(4,'bca'),
(5,'bca'),
(6,'science'),
(7,'bca'),
(8,'bca');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `feedback` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `action` varchar(50) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`feedback`,`date`,`action`,`user_id`) values 
(1,'we will take action','2023-04-11','fdgfh',2);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`type`) values 
(1,'samih@gmail.com','123456','admin'),
(2,'shezin','2002','student'),
(3,'','',''),
(8,'fathih@gmail.com','123456789','teacher'),
(9,'','','teacher'),
(10,'mishal@gmail.com','1234567890','teacher');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `notification_id` int(11) NOT NULL AUTO_INCREMENT,
  `notification` varchar(100) DEFAULT NULL,
  `date` int(30) DEFAULT NULL,
  PRIMARY KEY (`notification_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `student_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `pin` int(30) DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL,
  `phone_number` int(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `gender` varchar(30) DEFAULT NULL,
  `photo` varchar(50) DEFAULT NULL,
  `semester` int(30) DEFAULT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `student` */

insert  into `student`(`student_id`,`login_id`,`name`,`place`,`post`,`pin`,`course_id`,`phone_number`,`email`,`gender`,`photo`,`semester`) values 
(1,2,'samih','azhiyoor','mahe',673310,3,2147483647,'SAMIH234@gmail.com','male','/static/student/download.jpg',3),
(2,NULL,'shezin','monthal','mahe',673310,3,2147483647,'shezin@gmail.com','male','/static/student/download.jpg',4);

/*Table structure for table `student_upload` */

DROP TABLE IF EXISTS `student_upload`;

CREATE TABLE `student_upload` (
  `upload_id` int(11) NOT NULL AUTO_INCREMENT,
  `assignment_id` int(11) DEFAULT NULL,
  `file_name` varchar(50) DEFAULT NULL,
  `date` int(30) DEFAULT NULL,
  `student_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`upload_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `student_upload` */

/*Table structure for table `subject` */

DROP TABLE IF EXISTS `subject`;

CREATE TABLE `subject` (
  `subject_id` int(11) NOT NULL AUTO_INCREMENT,
  `subject` varchar(50) DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL,
  `semester` int(11) DEFAULT NULL,
  PRIMARY KEY (`subject_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `subject` */

insert  into `subject`(`subject_id`,`subject`,`course_id`,`semester`) values 
(1,'',0,2),
(2,'introduction to ai',0,2),
(4,'elct',0,5),
(5,'gf',0,5),
(6,'h',0,3),
(7,'dsd',2,1),
(8,'introduction to ai',2,5),
(9,'introduction to ai',2,0),
(11,'it',4,4);

/*Table structure for table `teacher` */

DROP TABLE IF EXISTS `teacher`;

CREATE TABLE `teacher` (
  `teacher_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `phone_number` bigint(20) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `pin` int(11) DEFAULT NULL,
  `email` varchar(80) DEFAULT NULL,
  `photo` varchar(50) DEFAULT NULL,
  `department_id` int(11) DEFAULT NULL,
  `status` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`teacher_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `teacher` */

insert  into `teacher`(`teacher_id`,`login_id`,`name`,`gender`,`phone_number`,`place`,`post`,`pin`,`email`,`photo`,`department_id`,`status`) values 
(1,1,'shezin','male',8976546787,'kannur','kannur',673325,'sdfgh90@gmail.com','/static/teacher/download.jpg',2,NULL),
(2,0,'\"++\"','\"++\"',0,'\"++\"','\"++\"',0,'\"++\"','\"++\"',0,''),
(3,0,'\"++\"','\"++\"',0,'\"++\"','\"++\"',0,'\"++\"','\"++\"',0,''),
(4,0,'\"++\"','\"++\"',0,'\"++\"','\"++\"',0,'\"++\"','\"++\"',0,'pending'),
(5,8,'fathih','male',8794551214,'kunjipalli','vadakara',670363,'fathih@gmail.com','/static/teacher/20230429-114532.jpg',1,'pending'),
(6,9,'','',0,'','',0,'','/static/teacher/20230429-112401.jpg',3,'pending'),
(7,10,'mishaal','male',9638521470,'kanjaram','chokli',670673,'mishal@gmail.com','/static/teacher/20230505-161425.jpg',3,'pending');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
