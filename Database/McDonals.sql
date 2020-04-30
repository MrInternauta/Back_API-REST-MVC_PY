
-- -----------------------------------------------------
-- Schema McDonals
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `McDonals` DEFAULT CHARACTER SET utf8 ;
USE `McDonals` ;

-- -----------------------------------------------------
-- Table `McDonals`.`Rol`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `McDonals`.`Rol` (
  `idRol` INT NOT NULL AUTO_INCREMENT,
  `nombreRol` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idRol`));


-- -----------------------------------------------------
-- Table `McDonals`.`Usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `McDonals`.`Usuario` (
  `idUsuario` INT NOT NULL AUTO_INCREMENT,
  `nombreUsuario` VARCHAR(45) NOT NULL,
  `apellidoUsuario` VARCHAR(45) NULL,
  `emailUsuario` VARCHAR(45) NOT NULL UNIQUE ,
  `passwordUsuario` VARCHAR(250) NOT NULL,
  `idRol` INT NULL,
  PRIMARY KEY (`idUsuario`));

  ALTER TABLE `McDonals`.`Usuario` 
    ADD CONSTRAINT `UsuarioRol`
    FOREIGN KEY (`idRol`)
    REFERENCES `McDonals`.`Rol` (`idRol`)
    ON DELETE SET NULL
    ON UPDATE NO ACTION;

-- -----------------------------------------------------
-- Table `McDonals`.`Categoria`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `McDonals`.`Categoria` (
  `idCategoria` INT NOT NULL AUTO_INCREMENT,
  `nombreCategoria` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idCategoria`));


-- -----------------------------------------------------
-- Table `McDonals`.`Producto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `McDonals`.`Producto` (
  `idProducto` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `stock` INT NULL,
  `idCategoria` INT NULL,
  PRIMARY KEY (`idProducto`));
  
  ALTER TABLE `McDonals`.`Producto` ADD 
  CONSTRAINT `Producto_Categoria`
    FOREIGN KEY (`idCategoria`)
    REFERENCES `McDonals`.`Categoria` (`idCategoria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION;


-- -----------------------------------------------------
-- Table `McDonals`.`Venta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `McDonals`.`Venta` (
  `idVenta` INT NOT NULL AUTO_INCREMENT,
  `idCliente` INT NULL,
  `idVendedor` INT NULL,
  `fecha` DATETIME NULL,
  PRIMARY KEY (`idVenta`));

  ALTER TABLE `McDonals`.`Venta` ADD
  CONSTRAINT `Venta_Cliente`
    FOREIGN KEY (`idCliente`)
    REFERENCES `McDonals`.`Usuario` (`idUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION;

  ALTER TABLE `McDonals`.`Venta` ADD
  CONSTRAINT `Venta_Vendedor`
    FOREIGN KEY (`idVendedor`)
    REFERENCES `McDonals`.`Usuario` (`idUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION;

-- -----------------------------------------------------
-- Table `McDonals`.`VentaDetalle`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `McDonals`.`VentaDetalle` (
  `idVentaDetalle` INT NOT NULL AUTO_INCREMENT,
  `idProducto` INT NULL,
  `contidad_vendida` FLOAT NULL,
  `descuento` FLOAT NULL,
  `idVenta` INT NULL,
  PRIMARY KEY (`idVentaDetalle`));


ALTER  TABLE `McDonals`.`VentaDetalle` ADD
  CONSTRAINT `Venta_Producto`
    FOREIGN KEY (`idProducto`)
    REFERENCES `McDonals`.`Producto` (`idProducto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION;

ALTER  TABLE `McDonals`.`VentaDetalle` ADD
  CONSTRAINT `VentaDetalle_Venta`
    FOREIGN KEY (`idVenta`)
    REFERENCES `McDonals`.`Venta` (`idVenta`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION;


-- -----------------------------------------------------
-- Table `McDonals`.`Extras`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `McDonals`.`Extras` (
  `idExtras` INT NOT NULL AUTO_INCREMENT,
  `nombreExra` VARCHAR(45) NULL,
  `PrecioExtra` FLOAT NULL,
  PRIMARY KEY (`idExtras`));


-- -----------------------------------------------------
-- Table `McDonals`.`ExtrasProductos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `McDonals`.`ExtrasProductos` (
  `idExtras` INT NOT NULL,
  `idProducto` INT NOT NULL,
  PRIMARY KEY (`idExtras`, `idProducto`));


ALTER TABLE `McDonals`.`ExtrasProductos` ADD
  CONSTRAINT `ExtraProducto_Producto`
    FOREIGN KEY (`idProducto`)
    REFERENCES `McDonals`.`Producto` (`idProducto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION;

ALTER TABLE `McDonals`.`ExtrasProductos` ADD
  CONSTRAINT `ExtraProducto_Extras`
    FOREIGN KEY (`idExtras`)
    REFERENCES `McDonals`.`Extras` (`idExtras`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION;