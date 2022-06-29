-- creates a table second_table in the database All_weather_repartition in your MySQL server and add multiples rows.
-- cat Create_table_all_w.sql | mysql -hlocalhost -uroot -p Portfoladvice_data
CREATE TABLE IF NOT EXISTS `All_weather_info` (`name` VARCHAR(256), `code isin` VARCHAR(256), `frais annuels` REAL, `repartition` REAL, `value` REAL);
INSERT INTO `All_weather_repartition` (`name`, `code isin`, `frais annuels`, `repartition`, `localisation`) VALUES ("Lyxor S&P 500 UCITS ETF - Dist (EUR)", "LU0496786574", 0.09, 4, 38.1678);
INSERT INTO `All_weather_repartition` (`name`, `code isin`, `frais annuels`, `repartition`, `localisation`) VALUES ("Amundi Russell 2000 UCITS ETF EUR (C)", "LU1681038672", 0.35, 4, 241.18);
INSERT INTO `All_weather_repartition` (`name`, `code isin`, `frais annuels`, `repartition`, `localisation`) VALUES ("BNP Paribas Easy Low Carbon 100 Europe PAB", "LU1377382368", 0.30, 4, 199.48);
INSERT INTO `All_weather_repartition` (`name`, `code isin`, `frais annuels`, `repartition`, `localisation`) VALUES ("Lyxor MSCI EMU Small Cap (DR) UCITS ETF - Dist", "LU1598689153", 0.40, 4, 320.78);
INSERT INTO `All_weather_repartition` (`name`, `percent`) VALUES ("Gold", 7.5);
