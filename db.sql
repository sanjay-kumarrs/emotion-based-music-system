/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.33 : Database - emoplayer
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`emoplayer` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `emoplayer`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add login',7,'add_login'),
(26,'Can change login',7,'change_login'),
(27,'Can delete login',7,'delete_login'),
(28,'Can view login',7,'view_login'),
(29,'Can add user',8,'add_user'),
(30,'Can change user',8,'change_user'),
(31,'Can delete user',8,'delete_user'),
(32,'Can view user',8,'view_user'),
(33,'Can add viewrating',9,'add_viewrating'),
(34,'Can change viewrating',9,'change_viewrating'),
(35,'Can delete viewrating',9,'delete_viewrating'),
(36,'Can view viewrating',9,'view_viewrating'),
(37,'Can add manageplaylist',10,'add_manageplaylist'),
(38,'Can change manageplaylist',10,'change_manageplaylist'),
(39,'Can delete manageplaylist',10,'delete_manageplaylist'),
(40,'Can view manageplaylist',10,'view_manageplaylist'),
(41,'Can add complaints',11,'add_complaints'),
(42,'Can change complaints',11,'change_complaints'),
(43,'Can delete complaints',11,'delete_complaints'),
(44,'Can view complaints',11,'view_complaints'),
(45,'Can add chat',12,'add_chat'),
(46,'Can change chat',12,'change_chat'),
(47,'Can delete chat',12,'delete_chat'),
(48,'Can view chat',12,'view_chat'),
(49,'Can add rating',13,'add_rating'),
(50,'Can change rating',13,'change_rating'),
(51,'Can delete rating',13,'delete_rating'),
(52,'Can view rating',13,'view_rating');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

insert  into `auth_user`(`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`) values 
(1,'pbkdf2_sha256$260000$o9gcbU2Jrw7MiCVQU3DNMz$bWSI9EPMJZa9iRhPWw0tNuRpsXcATRV+/KdhN1lezFM=','2024-02-01 08:40:22.859440',1,'admin','','','admin@gmail.com',1,1,'2024-02-01 08:31:30.531699');

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(12,'emo','chat'),
(11,'emo','complaints'),
(7,'emo','login'),
(10,'emo','manageplaylist'),
(13,'emo','rating'),
(8,'emo','user'),
(9,'emo','viewrating'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2024-01-07 07:00:00.669672'),
(2,'auth','0001_initial','2024-01-07 07:00:01.644025'),
(3,'admin','0001_initial','2024-01-07 07:00:01.921470'),
(4,'admin','0002_logentry_remove_auto_add','2024-01-07 07:00:01.937360'),
(5,'admin','0003_logentry_add_action_flag_choices','2024-01-07 07:00:01.944386'),
(6,'contenttypes','0002_remove_content_type_name','2024-01-07 07:00:02.094213'),
(7,'auth','0002_alter_permission_name_max_length','2024-01-07 07:00:02.163386'),
(8,'auth','0003_alter_user_email_max_length','2024-01-07 07:00:02.188539'),
(9,'auth','0004_alter_user_username_opts','2024-01-07 07:00:02.188539'),
(10,'auth','0005_alter_user_last_login_null','2024-01-07 07:00:02.298256'),
(11,'auth','0006_require_contenttypes_0002','2024-01-07 07:00:02.298256'),
(12,'auth','0007_alter_validators_add_error_messages','2024-01-07 07:00:02.317708'),
(13,'auth','0008_alter_user_username_max_length','2024-01-07 07:00:02.444606'),
(14,'auth','0009_alter_user_last_name_max_length','2024-01-07 07:00:02.560234'),
(15,'auth','0010_alter_group_name_max_length','2024-01-07 07:00:02.575869'),
(16,'auth','0011_update_proxy_permissions','2024-01-07 07:00:02.592244'),
(17,'auth','0012_alter_user_first_name_max_length','2024-01-07 07:00:02.657752'),
(18,'emo','0001_initial','2024-01-07 07:00:03.296307'),
(19,'sessions','0001_initial','2024-01-07 07:00:03.375202'),
(20,'emo','0002_delete_viewrating','2024-01-07 07:01:28.021663'),
(21,'emo','0003_auto_20240107_1231','2024-01-07 07:01:56.315085'),
(22,'emo','0004_chat_complaints_manageplaylist_user_viewrating','2024-01-07 07:02:44.146153'),
(23,'emo','0005_delete_viewrating','2024-01-07 07:02:56.564813'),
(24,'emo','0006_rating','2024-01-07 07:03:11.427577'),
(25,'emo','0007_auto_20240120_1228','2024-01-20 06:58:04.450216'),
(26,'emo','0008_auto_20240120_1519','2024-01-20 09:49:25.873751');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('4edjw8ifspmi351susehq4j8jrfrqp9r','eyJsaWQiOjEsImNpZCI6Mn0:1rRSbT:9f-7Lt1TxZ4vO4igCHKZGwwoMm9ZmRB6xjh6Ebz2758','2024-02-04 07:50:51.218697'),
('b70pus8ir3dgrm7hyybf1gcz6bzs011f','eyJsaWQiOjF9:1rVRcw:_BK6izQkhFtVu9U-WWVd60GKRIXwl1h4WOsCkAuTHvw','2024-02-15 07:36:50.709339');

/*Table structure for table `emo_chat` */

DROP TABLE IF EXISTS `emo_chat`;

CREATE TABLE `emo_chat` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `message` varchar(500) NOT NULL,
  `date` int NOT NULL,
  `Fromid_id` bigint NOT NULL,
  `Toid_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `emo_chat_Fromid_id_3a35c82d_fk_emo_login_id` (`Fromid_id`),
  KEY `emo_chat_Toid_id_c68fa492_fk_emo_login_id` (`Toid_id`),
  CONSTRAINT `emo_chat_Fromid_id_3a35c82d_fk_emo_login_id` FOREIGN KEY (`Fromid_id`) REFERENCES `emo_login` (`id`),
  CONSTRAINT `emo_chat_Toid_id_c68fa492_fk_emo_login_id` FOREIGN KEY (`Toid_id`) REFERENCES `emo_login` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `emo_chat` */

/*Table structure for table `emo_complaints` */

DROP TABLE IF EXISTS `emo_complaints`;

CREATE TABLE `emo_complaints` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `Complaints` varchar(500) NOT NULL,
  `date` date NOT NULL,
  `reply` varchar(500) NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `emo_complaints_user_id_4987229c_fk_emo_user_id` (`user_id`),
  CONSTRAINT `emo_complaints_user_id_4987229c_fk_emo_user_id` FOREIGN KEY (`user_id`) REFERENCES `emo_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `emo_complaints` */

insert  into `emo_complaints`(`id`,`Complaints`,`date`,`reply`,`user_id`) values 
(1,'baad','2024-01-21','jhg',1),
(2,'hhh','2024-01-21','ok',1);

/*Table structure for table `emo_login` */

DROP TABLE IF EXISTS `emo_login`;

CREATE TABLE `emo_login` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `type` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `emo_login` */

insert  into `emo_login`(`id`,`username`,`password`,`type`) values 
(1,'admin','123','admin'),
(2,'user1','123','user');

/*Table structure for table `emo_manageplaylist` */

DROP TABLE IF EXISTS `emo_manageplaylist`;

CREATE TABLE `emo_manageplaylist` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `song` varchar(100) NOT NULL,
  `genre` varchar(100) NOT NULL,
  `musician` varchar(100) NOT NULL,
  `details` varchar(100) NOT NULL,
  `file` varchar(100) NOT NULL,
  `emotion` varchar(300) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `emo_manageplaylist_LOGIN_id_a9d64ec1_fk_emo_login_id` (`LOGIN_id`),
  CONSTRAINT `emo_manageplaylist_LOGIN_id_a9d64ec1_fk_emo_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `emo_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `emo_manageplaylist` */

insert  into `emo_manageplaylist`(`id`,`song`,`genre`,`musician`,`details`,`file`,`emotion`,`LOGIN_id`) values 
(1,'pppppp','gff','tt','erty','fggs','sad',1),
(4,'ff','ff','ff','hf','usecasediagram1_WrFUH7F.dia','ff',1),
(5,'ff','ff','ff','mnbv','dea.txt','ff',1),
(6,'werfg','df','sdf','wedf','DFD.jpg','sdf',1);

/*Table structure for table `emo_rating` */

DROP TABLE IF EXISTS `emo_rating`;

CREATE TABLE `emo_rating` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `feedback` varchar(500) NOT NULL,
  `rating` double NOT NULL,
  `date` date NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `emo_rating_user_id_d632d137_fk_emo_user_id` (`user_id`),
  CONSTRAINT `emo_rating_user_id_d632d137_fk_emo_user_id` FOREIGN KEY (`user_id`) REFERENCES `emo_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `emo_rating` */

insert  into `emo_rating`(`id`,`feedback`,`rating`,`date`,`user_id`) values 
(2,'good',5,'2024-01-20',1);

/*Table structure for table `emo_user` */

DROP TABLE IF EXISTS `emo_user`;

CREATE TABLE `emo_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fname` varchar(50) NOT NULL,
  `lname` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `place` varchar(50) NOT NULL,
  `post` varchar(50) NOT NULL,
  `pin` int NOT NULL,
  `phone` bigint NOT NULL,
  `email` varchar(50) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `emo_user_LOGIN_id_6bd6543c_fk_emo_login_id` (`LOGIN_id`),
  CONSTRAINT `emo_user_LOGIN_id_6bd6543c_fk_emo_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `emo_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `emo_user` */

insert  into `emo_user`(`id`,`fname`,`lname`,`gender`,`place`,`post`,`pin`,`phone`,`email`,`LOGIN_id`) values 
(1,'kadeeja','sana','female','thalayad','thalayad',673574,9778795630,'sana@gmail.com',2),
(2,'havath','hdt','male','poonoor','sdfghj',673574,9656922125,'asdfghjk@gmail.com',2);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
