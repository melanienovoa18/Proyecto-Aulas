-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema reservas_evento
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema reservas_evento
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `reservas_evento` DEFAULT CHARACTER SET utf8 ;
USE `reservas_evento` ;

-- -----------------------------------------------------
-- Table `reservas_evento`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `reservas_evento`.`usuario` (
  `ID_usuario` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre_usurario` VARCHAR(45) NOT NULL,
  `contraseña` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID_usuario`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `reservas_evento`.`información_tarjeta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `reservas_evento`.`información_tarjeta` (
  `ID_tarjeta` INT(11) NOT NULL AUTO_INCREMENT,
  `numero_tarjeta` INT(12) NOT NULL,
  `mes_vencimiento` INT(2) NOT NULL,
  `años_vencimeinto` INT(2) NOT NULL,
  `CCV` INT(3) NOT NULL,
  PRIMARY KEY (`ID_tarjeta`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `reservas_evento`.`tipo de pago`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `reservas_evento`.`tipo de pago` (
  `ID_tipo_de_pago` INT(11) NOT NULL AUTO_INCREMENT,
  `tipo_de_pago` VARCHAR(45) NOT NULL,
  `eventos_confirmados_ID_evento` INT(11) NOT NULL,
  PRIMARY KEY (`ID_tipo_de_pago`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `reservas_evento`.`registro_eventos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `reservas_evento`.`registro_eventos` (
  `ID_evento` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre_evento` VARCHAR(45) NOT NULL,
  `tipo_evento` VARCHAR(45) NOT NULL,
  `tipo_otros` VARCHAR(100) NULL DEFAULT NULL,
  `fecha_inico_evento` DATE NOT NULL,
  `fecha_final_evento` DATE NOT NULL,
  `hora_inicio_evento` VARCHAR(45) NOT NULL,
  `hora_final_evento` VARCHAR(45) NOT NULL,
  `fecha_registro` VARCHAR(45) NOT NULL,
  `encargado_empresa` VARCHAR(45) NOT NULL,
  `orador` MULTIPOINT NOT NULL,
  `nombre_empresa` VARCHAR(45) NOT NULL,
  `status` VARCHAR(45) NOT NULL,
  `cf_userID` INT(11) NOT NULL,
  `fk_tarjetaIDI` INT(11) NOT NULL,
  `tipo de pago_ID` INT(11) NOT NULL,
  PRIMARY KEY (`ID_evento`),
  INDEX `fk_registro_eventos_usuario1_idx` (`cf_userID` ASC) VISIBLE,
  INDEX `fk_registro_eventos_información_tarjeta1_idx` (`fk_tarjetaIDI` ASC) VISIBLE,
  INDEX `fk_registro_eventos_tipo de pago1_idx` (`tipo de pago_ID` ASC) VISIBLE,
  CONSTRAINT `fk_registro_eventos_usuario1`
    FOREIGN KEY (`cf_userID`)
    REFERENCES `reservas_evento`.`usuario` (`ID_usuario`),
  CONSTRAINT `fk_registro_eventos_información_tarjeta1`
    FOREIGN KEY (`fk_tarjetaIDI`)
    REFERENCES `reservas_evento`.`información_tarjeta` (`ID_tarjeta`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_registro_eventos_tipo de pago1`
    FOREIGN KEY (`tipo de pago_ID`)
    REFERENCES `reservas_evento`.`tipo de pago` (`ID_tipo_de_pago`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `reservas_evento`.`areas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `reservas_evento`.`areas` (
  `ID_areas` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `tipo` VARCHAR(45) NOT NULL,
  `capacidad` VARCHAR(45) NOT NULL,
  `registro_eventos_ID_evento` INT(11) NOT NULL,
  PRIMARY KEY (`ID_areas`),
  CONSTRAINT `fk_areas_registro_eventos1`
    FOREIGN KEY (`registro_eventos_ID_evento`)
    REFERENCES `reservas_evento`.`registro_eventos` (`ID_evento`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `reservas_evento`.`banquete`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `reservas_evento`.`banquete` (
  `ID_banquete` INT(11) NOT NULL AUTO_INCREMENT,
  `tipo` INT(1) NOT NULL,
  `registro_eventos_ID_evento` INT(11) NOT NULL,
  `eventos_confirmados_ID_evento` INT(11) NOT NULL,
  PRIMARY KEY (`ID_banquete`),
  INDEX `fk_banquete_registro_eventos1_idx` (`registro_eventos_ID_evento` ASC) VISIBLE,
  CONSTRAINT `fk_banquete_registro_eventos1`
    FOREIGN KEY (`registro_eventos_ID_evento`)
    REFERENCES `reservas_evento`.`registro_eventos` (`ID_evento`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `reservas_evento`.`extras`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `reservas_evento`.`extras` (
  `ID_extras` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `registro_eventos_ID_evento` INT(11) NOT NULL,
  PRIMARY KEY (`ID_extras`),
  CONSTRAINT `fk_extras_registro_eventos1`
    FOREIGN KEY (`registro_eventos_ID_evento`)
    REFERENCES `reservas_evento`.`registro_eventos` (`ID_evento`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `reservas_evento`.`registro_empresa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `reservas_evento`.`registro_empresa` (
  `ID_registro_empresa` INT(11) NOT NULL AUTO_INCREMENT,
  `usuario_ID_usuario` INT(11) NOT NULL,
  `nombre_empresa` VARCHAR(45) NOT NULL,
  `rubro_empresa` VARCHAR(45) NOT NULL,
  `NIT` INT(11) NOT NULL,
  `registro_empresa` INT(11) NOT NULL,
  `telefeno` INT(11) NOT NULL,
  `correo` VARCHAR(45) NOT NULL,
  `representante_legal` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID_registro_empresa`),
  INDEX `fk_registro_empresa_usuario1_idx` (`usuario_ID_usuario` ASC) VISIBLE,
  CONSTRAINT `fk_registro_empresa_usuario1`
    FOREIGN KEY (`usuario_ID_usuario`)
    REFERENCES `reservas_evento`.`usuario` (`ID_usuario`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
