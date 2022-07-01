-- creates a table second_table in the database All_weather_info in your MySQL server and add multiples rows.
-- cat Create_table_list_etf.sql | mysql -hlocalhost -uroot -p Portfoladvice_data
CREATE TABLE IF NOT EXISTS `List_etf` (`name` VARCHAR(256), `code_isin` VARCHAR(256), `frais_annuels` REAL, `value` REAL);
INSERT INTO `List_etf` (`name`, `code_isin`, `frais_annuels`, `value`) VALUES ("Lyxor S&P 500 UCITS ETF - Dist (EUR)", "LU0496786574", 0.09, 38.1678);
INSERT INTO `List_etf` (`name`, `code_isin`, `frais_annuels`, `value`) VALUES ("Amundi Russell 2000 UCITS ETF EUR (C)", "LU1681038672", 0.35, 241.18);
INSERT INTO `List_etf` (`name`, `code_isin`, `frais_annuels`, `value`) VALUES ("BNP Paribas Easy Low Carbon 100 Europe PAB", "LU1377382368", 0.30, 199.48);
INSERT INTO `List_etf` (`name`, `code_isin`, `frais_annuels`, `value`) VALUES ("Lyxor MSCI EMU Small Cap (DR) UCITS ETF - Dist", "LU1598689153", 0.40, 320.78);
INSERT INTO `List_etf` (`name`, `code_isin`, `frais_annuels`, `value`) VALUES ("Lyxor MSCI Japan ESG Learders Extra (DR) UCITS ETF -Acc", "LU1646359452", 0.15, 154.1255);
INSERT INTO `List_etf` (`name`, `code_isin`, `frais_annuels`, `value`) VALUES ("Lyxor FTSE EPRA/NAREIT Global Developed UCITS ETF - Dist (EUR)", "LU1832418773", 0.45, 43.9386);
INSERT INTO `List_etf` (`name`, `code_isin`, `frais_annuels`, `value`) VALUES ("Amundi MSCI Emerging Markets UCITS ETF EUR (C)", "LU1681045370", 0.20, 4.5400);
INSERT INTO `List_etf` (`name`, `code_isin`, `frais_annuels`, `value`) VALUES ("Lyxor Euro Government Bond 7-10Y (DR) UCITS ETF - Acc", "LU1287023185", 0.17, 162.1708);
INSERT INTO `List_etf` (`name`, `code_isin`, `frais_annuels`, `value`) VALUES ("Lyxor Euro Government Bond 25+Y (DR) UCITS ETF - Acc", "LU1686832194", 0.07, 89.3515);
INSERT INTO `List_etf` (`name`, `code_isin`, `frais_annuels`, `value`) VALUES ("Lyxor US Treasury 10+Y (DR) UCITS ETF - Dist", "LU1407890620", 0.07, 115.818);
INSERT INTO `List_etf` (`name`, `code_isin`, `frais_annuels`, `value`) VALUES ("Certificat 100% Or", "NL0006454928", 0.75, 156.370);
INSERT INTO `List_etf` (`name`, `code_isin`, `frais_annuels`, `value`) VALUES ("Lyxor Commodities Refinity/CoreCommodity CRB Ex-Energy", "LU1829218582", 0.35, 24.6072);
