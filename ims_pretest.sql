/*
SQLyog Ultimate v12.5.1 (64 bit)
MySQL - 10.4.22-MariaDB : Database - ims_pretest
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`ims_pretest` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `ims_pretest`;

/*Table structure for table `tb_pertandingan` */

DROP TABLE IF EXISTS `tb_pertandingan`;

CREATE TABLE `tb_pertandingan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_peserta_a` int(11) DEFAULT NULL,
  `id_peserta_b` int(11) DEFAULT NULL,
  `hasil` enum('Peserta 1 Menang','Peserta 2 Menang','Draw') DEFAULT NULL,
  `mulai` datetime DEFAULT NULL,
  `selesai` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_peserta_a` (`id_peserta_a`),
  KEY `id_peserta_b` (`id_peserta_b`),
  CONSTRAINT `tb_pertandingan_ibfk_1` FOREIGN KEY (`id_peserta_a`) REFERENCES `tb_peserta` (`id`),
  CONSTRAINT `tb_pertandingan_ibfk_2` FOREIGN KEY (`id_peserta_b`) REFERENCES `tb_peserta` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

/*Data for the table `tb_pertandingan` */

insert  into `tb_pertandingan`(`id`,`id_peserta_a`,`id_peserta_b`,`hasil`,`mulai`,`selesai`) values 
(3,1,2,'Draw','2022-03-01 15:20:12','2022-03-01 15:20:12');

/*Table structure for table `tb_peserta` */

DROP TABLE IF EXISTS `tb_peserta`;

CREATE TABLE `tb_peserta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nama_depan` varchar(255) DEFAULT NULL,
  `nama_belakang` varchar(255) DEFAULT NULL,
  `alamat` varchar(255) DEFAULT NULL,
  `no_telp` varchar(255) DEFAULT NULL,
  `poin` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_rank` (`poin`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

/*Data for the table `tb_peserta` */

insert  into `tb_peserta`(`id`,`nama_depan`,`nama_belakang`,`alamat`,`no_telp`,`poin`) values 
(1,'Halo','Ngab','Klungkung','911',0.5),
(2,'Tes','Ngab','Gianyar','200',0.5),
(4,'Neng','Pei','Badung','211',0);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
