#!/usr/bin/env python3.6

from password import Credential

def create_account(accountName, accountUsername, accountPassword):
    '''
    Function to creates a new account
    '''
    new_account = Credential(accountName, accountUsername, accountPassword)
    return new_account

def save_account(account):
    '''
    Function to save account
    '''
    account.save_account()

def find_account(accountUsername):
    '''
    Function that find an account by username and return the account
    '''
    return Credential.find_by_accountUsername(accountUsername)

def check_existing_account(accountUsername):
    '''
    Function that retur all the saved account
    '''
    return Credential.account_exist(accountUsername)

def display_accounts():
    '''
    Function that returns all saved accounts
    '''
    return Credential.display_accounts()