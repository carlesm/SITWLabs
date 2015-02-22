#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Simple web client, using URLLIB2
Created on 10/14/2014

@author: carlesm
'''

import urllib2


class Client(object):

    """Web Client, for www.udl.Created

    Downloads www.udl.cat main page to parse
    for agenda items"""

    def __init__(self):
        super(Client, self).__init__()

    def run(self):
        pass


if __name__ == "__main__":
    client = Client()
    client.run()
