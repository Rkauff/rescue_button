# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 00:02:27 2018

@author: Ryan
"""

import os
from twilio.rest import Client


def handler(event, context):
    client = Client(
        os.environ['TWILIO_ACCOUNT'],
        os.environ['TWILIO_TOKEN'],
    )

    client.messages.create(
        to=os.environ['ALERT_PHONE'],
        body=os.environ['HELP_MSG'],
        from_=os.environ['TWILIO_PHONE'])