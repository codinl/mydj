# ************************************************************
# Sequel Pro SQL dump
# Version 4135
#
# http://www.sequelpro.com/
# http://code.google.com/p/sequel-pro/
#
# Host: 127.0.0.1 (MySQL 5.5.34)
# Database: haodiao
# Generation Time: 2015-04-11 06:31:41 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table account_admin
# ------------------------------------------------------------

DROP TABLE IF EXISTS `account_admin`;

CREATE TABLE `account_admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `login_times` int(11) NOT NULL,
  `last_login_time` datetime NOT NULL,
  `last_login_ip` char(15) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `account_admin` WRITE;
/*!40000 ALTER TABLE `account_admin` DISABLE KEYS */;

INSERT INTO `account_admin` (`id`, `name`, `password`, `login_times`, `last_login_time`, `last_login_ip`, `is_active`)
VALUES
	(1,'admin','pbkdf2_sha256$10000$vxFc7YtbS3zN$4XhRjsPqELxT0trMzqBrvhRHWFVw+VMIDkz75hXM35w=',5,'2015-04-11 11:58:42','::1',1);

/*!40000 ALTER TABLE `account_admin` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table admin_node
# ------------------------------------------------------------

DROP TABLE IF EXISTS `admin_node`;

CREATE TABLE `admin_node` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `level` smallint(5) unsigned NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `sort` smallint(5) unsigned NOT NULL,
  `is_often` tinyint(1) NOT NULL,
  `is_show` tinyint(1) NOT NULL,
  `descr` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `admin_node_52094d6e` (`name`),
  KEY `admin_node_63f17a16` (`parent_id`),
  CONSTRAINT `parent_id_refs_id_e029f399` FOREIGN KEY (`parent_id`) REFERENCES `admin_node` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `admin_node` WRITE;
/*!40000 ALTER TABLE `admin_node` DISABLE KEYS */;

INSERT INTO `admin_node` (`id`, `url`, `name`, `level`, `parent_id`, `sort`, `is_often`, `is_show`, `descr`)
VALUES
	(1,'node/list','菜单管理',1,NULL,20,1,1,'菜单设置'),
	(2,'node/list','菜单管理',2,1,1,1,1,'菜单管理 2'),
	(3,'node/list/1','菜单列表',3,2,1,1,1,'菜单列表'),
	(4,'','系统用户管理',1,NULL,19,1,1,'系统用户管理'),
	(5,'','系统用户管理',3,4,1,1,1,'系统用户管理2'),
	(6,'admin/list/1','系统用户列表',3,5,1,1,1,'系统用户列表'),
	(7,'','DNS服务器',1,NULL,3,1,1,'DNS服务器'),
	(8,'','DNS服务器',2,7,3,1,1,'DNS服务器'),
	(9,'dns/list/1','DNS列表',3,8,1,1,1,'DNS服务器'),
	(10,'','站点管理',1,NULL,1,1,1,'站点管理'),
	(11,'','站点列表',2,10,1,1,1,'站点列表'),
	(12,'site/list/1','站点列表',3,11,1,1,1,'站点列表'),
	(13,'','广告管理',1,NULL,1,1,1,'广告管理'),
	(16,'adurl/list','广告URL',2,13,1,1,1,'广告URL'),
	(17,'adurl/list/1','广告URL列表',3,16,1,1,1,'广告URL列表');

/*!40000 ALTER TABLE `admin_node` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
