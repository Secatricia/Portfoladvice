-- creates a table second_table in the database All_weather_info in your MySQL server and add multiples rows.
-- cat Create_table_all_w.sql | mysql -hlocalhost -uroot -p Portfoladvice_data
CREATE TABLE IF NOT EXISTS `All_weather_info` (`name` VARCHAR(256), `code_isin` VARCHAR(256), `frais_annuels` REAL, `repartition` REAL, `value` REAL);
INSERT INTO `All_weather_info` (`name`, `code_isin`, `frais_annuels`, `repartition`, `value`) VALUES ("Lyxor S&P 500 UCITS ETF - Dist (EUR)", "LU0496786574", 0.09, 4, 38.1678);
INSERT INTO `All_weather_info` (`name`, `code_isin`, `frais_annuels`, `repartition`, `value`) VALUES ("Amundi Russell 2000 UCITS ETF EUR (C)", "LU1681038672", 0.35, 4, 241.18);
INSERT INTO `All_weather_info` (`name`, `code_isin`, `frais_annuels`, `repartition`, `value`) VALUES ("BNP Paribas Easy Low Carbon 100 Europe PAB", "LU1377382368", 0.30, 4, 199.48);
INSERT INTO `All_weather_info` (`name`, `code_isin`, `frais_annuels`, `repartition`, `value`) VALUES ("Lyxor MSCI EMU Small Cap (DR) UCITS ETF - Dist", "LU1598689153", 0.40, 4, 320.78);
INSERT INTO `All_weather_info` (`name`, `code_isin`, `frais_annuels`, `repartition`, `value`) VALUES ("Lyxor MSCI Japan ESG Learders Extra (DR) UCITS ETF -Acc", "LU1646359452", 0.15, 3, 154.1255);
INSERT INTO `All_weather_info` (`name`, `code_isin`, `frais_annuels`, `repartition`, `value`) VALUES ("Lyxor FTSE EPRA/NAREIT Global Developed UCITS ETF - Dist (EUR)", "LU1832418773", 0.45, 4, 43.9386);
INSERT INTO `All_weather_info` (`name`, `code_isin`, `frais_annuels`, `repartition`, `value`) VALUES ("Amundi MSCI Emerging Markets UCITS ETF EUR (C)", "LU1681045370", 0.20, 7, 4.5400);
INSERT INTO `All_weather_info` (`name`, `code_isin`, `frais_annuels`, `repartition`, `value`) VALUES ("Lyxor Euro Government Bond 7-10Y (DR) UCITS ETF - Acc", "LU1287023185", 0.17, 15, 162.1708);
INSERT INTO `All_weather_info` (`name`, `code_isin`, `frais_annuels`, `repartition`, `value`) VALUES ("Lyxor Euro Government Bond 25+Y (DR) UCITS ETF - Acc", "LU1686832194", 0.07, 25, 89.3515);
INSERT INTO `All_weather_info` (`name`, `code_isin`, `frais_annuels`, `repartition`, `value`) VALUES ("Lyxor US Treasury 10+Y (DR) UCITS ETF - Dist", "LU1407890620", 0.07, 15, 115.818);
INSERT INTO `All_weather_info` (`name`, `code_isin`, `frais_annuels`, `repartition`, `value`) VALUES ("Certificat 100% Or", "NL0006454928", 0.75, 7.5, 156.370);
INSERT INTO `All_weather_info` (`name`, `code_isin`, `frais_annuels`, `repartition`, `value`) VALUES ("Lyxor Commodities Refinity/CoreCommodity CRB Ex-Energy", "LU1829218582", 0.35, 7.5, 24.6072);
