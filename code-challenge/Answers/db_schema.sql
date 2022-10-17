CREATE SCHEMA IF NOT EXISTS `%s`;

USE `%s`;

CREATE TABLE IF NOT EXISTS `table1` (
    `t1id` BIGINT NOT NULL,
    `value` SMALLINT DEFAULT NULL,

    PRIMARY KEY (`t1id`)
);

CREATE TABLE IF NOT EXISTS `table2` (
    `t2id` BIGINT NOT NULL,
    `value` SMALLINT DEFAULT NULL,

    PRIMARY KEY (`t2id`)
);

CREATE TABLE IF NOT EXISTS `table3` (
    `t3id` BIGINT NOT NULL,
    `ModifiedDTS` DATE DEFAULT NULL,
    `value` SMALLINT DEFAULT NULL

);

CREATE TABLE IF NOT EXISTS `table4` (
    `t4id` BIGINT NOT NULL,
    `createdDTS` DATE DEFAULT NULL,
    `metric` CHAR(5) DEFAULT NULL,
    `value` SMALLINT DEFAULT NULL

);

DROP TABLE IF EXISTS `etherscan`;
CREATE TABLE IF NOT EXISTS `etherscan` (
    `blockNumber` BIGINT DEFAULT NULL,
    `timeStamp` BIGINT DEFAULT NULL,
    `hash` CHAR(100) DEFAULT NULL,
    `nonce` VARCHAR(20) DEFAULT NULL,
    `blockHash` CHAR(100) DEFAULT NULL,
    `from` CHAR(100) DEFAULT NULL,
    `contractAddress` CHAR(100) DEFAULT NULL,
    `to` CHAR(100) DEFAULT NULL,
    `value` VARCHAR(100) DEFAULT NULL,
    `tokenName` CHAR(20) DEFAULT NULL,
    `tokenSymbol` CHAR(20) DEFAULT NULL,
    `tokenDecimal` SMALLINT DEFAULT NULL,
    `transactionIndex` SMALLINT DEFAULT NULL,
    `gas`  BIGINT DEFAULT NULL,
    `gasPrice`  BIGINT DEFAULT NULL,
    `gasUsed`  BIGINT DEFAULT NULL,
    `cumulativeGasUsed`  BIGINT DEFAULT NULL,
    `input` CHAR(20) DEFAULT NULL,
    `confirmations`  BIGINT DEFAULT NULL

);