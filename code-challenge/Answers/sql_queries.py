table1_sql_insert = """
    INSERT INTO table1(
                    t1id,
                    value
                )
    VALUES (%s, %s)
    """

table2_sql_insert = """
    INSERT INTO table2(
                    t2id,
                    value
                )
    VALUES (%s, %s)
    """

table3_sql_insert = """
    INSERT INTO table3(
                    t3id,
                    ModifiedDTS,
                    value
                )
    VALUES (%s, %s, %s)
    """

table4_sql_insert = """
     INSERT INTO table4(
                    t4id,
                    createdDTS,
                    metric,
                    value
                )
    VALUES (%s, %s, %s, %s)
    """

etherscan_sql_insert = """
     INSERT INTO etherscan(
                    `blockNumber`,
                    `timeStamp`,
                    `hash`,
                    `nonce`,
                    `blockHash`,
                    `from`,
                    `contractAddress`,
                    `to`,
                    `value`,
                    `tokenName`,
                    `tokenSymbol`,
                    `tokenDecimal`,
                    `transactionIndex`,
                    `gas`,
                    `gasPrice`,
                    `gasUsed`,
                    `cumulativeGasUsed`,
                    `input`,
                    `confirmations`
                )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """


sql_strings = {
    'table1_sql_insert': table1_sql_insert,
    'table2_sql_insert': table2_sql_insert,
    'table3_sql_insert': table3_sql_insert,
    'table4_sql_insert': table4_sql_insert,
    'etherscan_sql_insert': etherscan_sql_insert
}