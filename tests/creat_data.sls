-- MySQL Script generated by MySQL Workbench
-- Sat Jun  2 21:21:44 2018
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema wnba_test
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema wnba_test
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `wnba_test` DEFAULT CHARACTER SET latin1 ;
-- -----------------------------------------------------
-- Schema new_schema1
-- -----------------------------------------------------
USE `wnba_test` ;

-- -----------------------------------------------------
-- Table `wnba_test`.`player_reference`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `wnba_test`.`player_reference` (
  `playerID` INT(11) NOT NULL AUTO_INCREMENT,
  `bbrefID` TEXT NULL DEFAULT NULL,
  `rotogrindersID` INT(11) NULL DEFAULT NULL,
  `fanduelID` TEXT NULL DEFAULT NULL,
  `draftkingsID` INT(11) NULL DEFAULT NULL,
  `rotowireID` INT(11) NULL DEFAULT NULL,
  `firstName` VARCHAR(100) NULL DEFAULT NULL,
  `lastName` VARCHAR(100) NULL DEFAULT NULL,
  `playerName` VARCHAR(100) NULL DEFAULT NULL,
  `team` VARCHAR(45) NULL DEFAULT NULL,
  `nickName` VARCHAR(150) NULL DEFAULT NULL,
  `rotoguruID` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`playerID`),
  UNIQUE INDEX `playerid_UNIQUE` (`playerID` ASC))
ENGINE = InnoDB
AUTO_INCREMENT = 0
DEFAULT CHARACTER SET = latin1;

USE `wnba_test` ;

-- -----------------------------------------------------
-- Placeholder table for view `wnba_test`.`view1`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `wnba_test`.`view1` (`id` INT);

-- -----------------------------------------------------
--  routine1
-- -----------------------------------------------------

DELIMITER $$
USE `wnba_test`$$
$$

DELIMITER ;

-- -----------------------------------------------------
-- View `wnba_test`.`view1`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `wnba_test`.`view1`;
USE `wnba_test`;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

