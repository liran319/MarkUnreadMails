# -*- conding: utf-8 -*-

import imaplib
# import sys

USERNAME = raw_input('Please input your email address: ')
PASSWORD = raw_input('Please input your passward: ')
M = imaplib.IMAP4_SSL('imap.gmail.com')
print M.login(USERNAME, PASSWORD)
M.list()
M.select('inbox')
typ, data = M.search(None, 'UNSEEN')
for num in data[0].split():
    typ, data = M.fetch(num, '(BODY.PEEK[])')
    M.store(num, '+FLAGS', '\Seen')
    # print 'Message %s\n%s\n' % (num, repr(data))
print "Done!"
M.close()
M.logout()
