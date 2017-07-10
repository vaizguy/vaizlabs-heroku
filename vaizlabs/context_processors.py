'''
Created on Nov 26, 2012

@author: vaizguy
'''

import datetime
import subprocess

def get_git_revision_hash():
    return subprocess.check_output(['git', 'rev-parse', 'HEAD'])

def get_git_revision_short_hash():
    return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'])

def home_static(request):
    """A context processor that provides static site attributes
    for site under construction."""

    return {
    ## Static variables
   'HOME_TITLE'            : '[vaizlabs engineering]',
   'HOME_HEADER'           : 'Vaizlabs Portal',
   'SECTION_HOME'          : 'HOME',
   'SECTION_BLOG'          : 'BLOG',
   'SECTION_CONTACT'       : 'CONTACT',
   'AUTHOR'                : 'arun vaidya',
   ## Dynamic variables
   'TIME'                  : datetime.datetime.now(),
   'IP_ADDRESS'            : request.META['REMOTE_ADDR'],
    ## CSS Files
    'HOME_CSS'   : 'home.css',
    'FOOTER_CSS' : 'footer.css',
    ## Contact variables
    #'MY_PGP_KEY_FP' : "498F 1806 393A 95BB BCCB 81D4 2E5A 3718 F4AB A2A9",
    'MY_PGP_KEY_FP' : "9DAC 3BE7 AA80 B9D5 CAFC 3BF0 0BB8 4490 C52A 6453",
    'SHOW_PGP'      : True,
    'EMAIL_TITLE'   : "vaizguy@gmail",
    'EMAIL_LINK'    : "vaizguy@gmail.com",
    'TWITTER_TITLE' : "vaizguy@twitter",
    'TWITTER_LINK'  : "https://www.twitter.com/vaizguy",
    'MY_IRC_CHANNEL_INFO' : "#vaizlabs@irc.freenode.net",
    'SHOW_IRC_CHANNEL' : True,
    'IRC_CHANNEL_LOCKED' : True,
    'GIT_REV' : get_git_revision_short_hash(),
    'GIT_REV_FULL' : get_git_revision_hash()
    }
