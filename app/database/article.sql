DROP TABLE IF EXISTS `article`;
CREATE TABLE `article`(
  `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(255) NOT NULL,
  `content` MEDIUMTEXT NOT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `is_hidden` TINYINT NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`),
  KEY `idx_ishidden_createdat`(`is_hidden`, `created_at`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;