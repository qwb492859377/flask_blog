DROP TABLE IF EXISTS `date_tip`;
CREATE TABLE `date_tip`(
  `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `date_name` VARCHAR(32) NOT NULL,
  PRIMARY KEY (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `article_date_edge`;
CREATE TABLE `article_date_edge`(
  `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `date_id` INT(11) UNSIGNED NOT NULL,
  `article_id` INT(11) UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_dateid_articleid`(`date_id`, `article_id`),
  KEY `idx_articleid`(`article_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;