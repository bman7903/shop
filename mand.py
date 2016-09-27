#!/usr/bin/env python

import argparse
import logging
import mandrill
import socket
from ath import mdrill

api_key  = str( mdrill( 'akey' )() )

def post_mail(to, subj, msg, user, fname, **kwargs):
    msg = {
        'from_email': kwargs.get('from_email'),
        'from_name': fname,
        'html': '<h3>Thank you for joining! ' + user + ' </h3><p>{msg}</p><h6> Confirmation Required'
                'Please paste the above string into the confirmation box.</h6>'.format(msg=msg),
        'headers': {'Reply-To': kwargs.get('reply_to')},
        'subject': subj,
        'to': [
            {'email': to,
             'name': kwargs.get('recipient'),
             'type': 'to'
            }
        ]
    }
    mc = mandrill.Mandrill( api_key )
    try:
        res = mc.messages.send(msg, async=kwargs.get('async', False))
        if res and not res[0].get('status') == 'sent':
            logging.error('Could not send email to {to}; status: {status}, reason: {reason}'
                          .format(to=to, status=res.get('status', 'unknown'),
                                  reason=res.get('reject_reason')))
            exit(1)
    except mandrill.Error, e:
        logging.error('Error occurred: {} - {}'.format(e.__class__.__name__, e))
        exit(1)
    logging.info('Message sent to {to}'.format(to=to))

def read_api_key(filename):
    with open(filename, 'r') as key_file:
        api_key = key_file.readline().rstrip('\n')
    return api_key

def smail(to, subj, msg, user, femail, fname ):
    FORMAT   = '%(asctime)-15s [%(levelname)s] %(message)s'
    DATE_FMT = '%m/%d/%Y %H:%M:%S'
    loglevel = logging.DEBUG
    logging.basicConfig(format=FORMAT, datefmt=DATE_FMT, level=loglevel)
    logging.info('Mailer Auto Script starting...')
    logging.debug('API key: {}'.format(api_key))
    kwargs = {'api_key': api_key,
              'reply_to': femail,
              'recipient': 'Recipient',
              'from_email': femail
    }
    post_mail(to, subj, msg, user, fname, **kwargs)

#if __name__ == "__main__":
#    smail()
