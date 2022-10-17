'''
    Question 4 (Open Ended):
    
    Augur is a decentralized prediction market platform built on the Ethereum blockchain. 
    We’d like to scrape their blockchain data to gain insights into wallet addresses that have Augur.

    They have two contract addresses (augur_contract, augur_contract_v1 in code snippet below). 
    REP ICO was in 2015 and launched in 2018. REPV2 launched in 2020.

    Etherscan is a block explorer and analytics platform that allows access to details on any Ethereum blockchain. 
    They have an API that can be reached to extract information (docs). The below code snippet is an example of how to get a response from the below endpoint in Python.

    Objective:
    Write a script that extracts Augur’s historical token transfer events. Get a large enough sample size to use the results for analysis. 
'''

import pandas as pd
import requests
import os

from etherscan import Etherscan
from utils import *
from sql_queries import sql_strings


eth_key = "7U3C64WMQWE9TVUHWG8FMRXIGGAB1NR5AT"
eth = Etherscan(eth_key) # key in quotation marks

# augur contract addresses
augur_contract = "0x221657776846890989a759BA2973e427DfF5C9bB"
augur_contract_v1 = "0x1985365e9f78359a9B6AD760e32412f4a445E862"

# example of getting a response from etherscan ipo endpoint to get ERC20 - Token Transfer Events’ by address (&module=account&action=tokentx)
def fetchEthERC20TransfersFromWalletOrContract(wallet='', page_num=1, contract=augur_contract):
    response = requests.get(f"https://api.etherscan.io/api?module=account&action=tokentx&contractaddress={contract}&page={page_num}&offset=0&startblock=0&endblock=14731209&sort=desc&apikey={eth_key}")
    response_code = response.status_code

    if response_code == 200:
        return response.json()
    else:
        print(f"Check Response Code: {response_code}")


def exportDataFrameToCsv(path, df, contract, **kwargs):
    try:
        # create csv file if not exists
        if os.path.isfile(path):
            open(path, 'a')

        print("Exporting Data Frame to %s with Contract Address %s" % (path, contract))
        
        # export dataframe to csv file
        df.to_csv(path, encoding = 'utf-8', index = False, **kwargs)

        print("Export finished successfully with %s rows\n" % len(df))

        return
    
    except Error as e:
        print("UNEXPECTED ERROR: ", e)


def exportDataFrameToMysqlDb(path):
    try:
        # import csv files 
        csv_data = csv_parse(path)
    
        # create database schema and tables if not yet exist.
        db_create_schema()

        # insert csv data into database tables
        print("Inserting rows into etherscan mysql table")
        db_insert(sql_strings.get('etherscan_sql_insert'), csv_data)

        # df_transformed = df.set_index(['contractAddress', 'timeStamp', 'metric'])['value', 'gasUsed'].unstack()

        return

    except Error as e:
        print("UNEXPECTED ERROR: ", e)


def analyzeData():
    # query data by contractAddress, tokenSymbol, month
    sql_string = """ 
            SELECT 
                ContractAddress,
                DATE_FORMAT(from_unixtime(timestamp), '%Y-%m') AS `month`,
                tokenSymbol,
                COUNT(DISTINCT blockNumber) blockNumberUniqueCount
            FROM 
                etherscan
            GROUP BY contractAddress, tokenSymbol, `month`;
        """
        
    result = db_send_query(sql_string)
    df = pd.DataFrame(result)
    df.rename(columns=df.iloc[0], inplace = True)
    df.drop([0], inplace = True)

    df_transformed = df.set_index(['month', 'ContractAddress', 'tokenSymbol'])['blockNumberUniqueCount'].unstack(level=0)

    print('\n', df)
    print('\n\n', df_transformed)
    print('\n\n')

    return


if __name__ == "__main__":
    # set csv file name
    path = '../Data/etherscan.csv'

    # load dataframe from ether api json response
    pages = 5
    for page_num in range(pages+1):
        augur_contract_df = pd.DataFrame(fetchEthERC20TransfersFromWalletOrContract(wallet='', page_num=page_num, contract=augur_contract)['result'])
        augur_contract_v1_df = pd.DataFrame(fetchEthERC20TransfersFromWalletOrContract(wallet='', page_num=page_num, contract=augur_contract_v1)['result'])

        # export augur contracts dataframe to csv file
        print("Page %s of %s" % (page_num, pages))
        if page_num == 0:
            exportDataFrameToCsv(path, augur_contract_df, augur_contract)
        else:
            exportDataFrameToCsv(path, augur_contract_df, augur_contract, header=False, mode='a')
        
        exportDataFrameToCsv(path, augur_contract_v1_df, augur_contract_v1, header=False, mode='a')

    
    exportDataFrameToMysqlDb(path)
    analyzeData()