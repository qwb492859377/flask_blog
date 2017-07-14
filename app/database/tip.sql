DROP TABLE IF EXISTS `article_tip`;
CREATE TABLE `article_tip`(
  `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `tip_name` VARCHAR(32) NOT NULL,
  PRIMARY KEY (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `article_tip_edge`;
CREATE TABLE `article_tip_edge`(
  `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `tip_id` INT(11) UNSIGNED NOT NULL,
  `article_id` INT(11) UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_tipid_articleid`(`tip_id`, `article_id`),
  KEY `idx_articleid`(`article_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
