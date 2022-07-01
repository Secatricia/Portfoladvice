-- creates a table second_table in the database All_weather_repartition in your MySQL server and add multiples rows.
-- cat Create_table_all_w_repartition.sql | mysql -hlocalhost -uroot -p Portfoladvice_data
CREATE TABLE IF NOT EXISTS `All_weather_repartition` (`name` VARCHAR(256), `percent` REAL);
INSERT INTO `All_weather_repartition` (`name`, `percent`) VALUES ("Total Stock Market", 30);
INSERT INTO `All_weather_repartition` (`name`, `percent`) VALUES ("Long Term Bonds", 40);
INSERT INTO `All_weather_repartition` (`name`, `percent`) VALUES ("Intermediate Bonds", 15);
INSERT INTO `All_weather_repartition` (`name`, `percent`) VALUES ("Commodities", 7.5);
INSERT INTO `All_weather_repartition` (`name`, `percent`) VALUES ("Gold", 7.5);
