# -*- conding: utf-8 -*-

import imaplib
import getpass
# import sys

M = imaplib.IMAP4_SSL('imap.gmail.com')


def account_login():
    """
    """
    USERNAME = raw_input('Please input your email address: ')
    PASSWORD = getpass.getpass('Please input your passward: ')
    try:
        status = M.login(USERNAME, PASSWORD)
    except Exception as e:
        print e
        status = ['Fail']
    print status
    if status[0] == 'OK':
        return True
    else:
        return False

while 1:
    if account_login():
        M.list()
        M.select('inbox')
        typ, data = M.search(None, 'UNSEEN')
        for num in data[0].split():
            typ, data = M.fetch(num, '(BODY.PEEK[])')
            M.store(num, '+FLAGS', '\Seen')
            print 'Message %s\n' % num
        print "Done!"
        M.close()
        M.logout()
        anykey = raw_input('Press any to continue...')
        break
    else:
        pass
