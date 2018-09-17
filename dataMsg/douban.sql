-- douban_comment
CREATE TABLE `douban_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `movieRank` varchar(20) DEFAULT NULL,
  `movieName` varchar(50) DEFAULT NULL,
  `movieForName` varchar(50) DEFAULT NULL,
  `movieAlias` varchar(100) DEFAULT NULL,
  `directorName` varchar(50) DEFAULT NULL,
  `showYear` varchar(50) DEFAULT NULL,
  `makeCounty` varchar(100) DEFAULT NULL,
  `movieType` varchar(100) DEFAULT NULL,
  `movieScore` varchar(10) DEFAULT NULL,
  `scoreNum` varchar(20) DEFAULT NULL,
  `shortFilm` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
