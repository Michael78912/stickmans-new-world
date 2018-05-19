"""
bugreport.py
this module takes any exception, the app name,
and any other info, and reports it to my email.
"""

import io
import os
import smtplib
from cryptography.fernet import Fernet
import sys
import threading
import traceback
import platform
import socket

FYUKYFVKFYVHUFL = b'gAAAAABavaf20Qc-jiOnPXzOsBfr-yhJiVbuBEiyK4cJA3r82f0wXAp5gdgPQ43UxZB7H9O9RgiTCHDb0ngh9CNCRPi03nQssg=='
HIUEFWILEIURFHE = b'_qJoI0kXZlQuHI0-U8BSSKuKQ_Zpp3vQMZGrPKMk8lI='
TMP = os.path.join('/tmp/',
                   'stderr.tmp') if os.name == 'posix' else os.path.join(
                       os.getenv('TMP'), 'stderr.tmp')
ERROR = 'whoops, a critical error occured. it should be reported.\nif you gave your email address, I will try and get back to you.\nfor more details, you can look at the file: ' + TMP
EMAILFILE = os.path.join((os.environ['USERPROFILE']
                          if os.name == 'nt' else os.environ['HOME']),
                         '.stickman_new_world', 'useremail')

if platform.system() == 'Linux':
    import pwd
    # os.getlogin sometimes fails on Linux machines
    os.getlogin = lambda: pwd.getpwuid(os.getuid())[0]


def error(arg1, arg2):
    import tkinter.messagebox
    try:
        root = tkinter.Tk()
        root.withdraw()
    except:
        pass
    tkinter.messagebox.showerror(arg1, arg2)


def mainwithmessage(*args):
    # show without the root window

    threading.Thread(target=lambda: error('Error :(', ERROR)).start()
    main(*args + (get_email(), ))


def get_email():
    if os.path.exists(EMAILFILE):
        return 'email address: ' + open(EMAILFILE).read()
    return ''


def main(project_name, exception, *other_info):
    """
    main function for sending mail.
    """

    exception.args = [str(arg) for arg in exception.args]
    print(exception.args)
    exception_traceback_details, exception_message = get_details(exception)

    with open(TMP, 'w') as stderr:
        stderr.write(repr(exception_traceback_details))

    email = build_message(project_name, exception_message,
                          exception_traceback_details, *other_info)
    send_message(email)


def send_message(message):
    """
    sends message to the bug report address
    """
    server = smtplib.SMTP_SSL('smtp.mail.com', 465)
    # i dont want random people just emailing me!!
    decrypter = Fernet(HIUEFWILEIURFHE)
    data = decrypter.decrypt(FYUKYFVKFYVHUFL).decode()
    print(data)
    try:
        print(server.login('bugreporter.smr@mail.com', 'bugreport'))
        server.sendmail('bugreporter.smr@mail.com',
                        ['bugreporter.smr@mail.com'], message)
    except Exception as e:
        print(e)
        threading.Thread(
            target=
            lambda: error('Another Error', 'an error accured when trying to send the email.\n please contact me at <michaelveenstra12@gmail.com>')
        )
    server.close()


def build_message(project, tbmessage, details, *args):
    """
    build and return a email that contains the 
    traceback.
    """
    args = [repr(arg) for arg in args]

    bottomline = ',\n'.join(args) if len(args) > 0 else 'Nope'
    sender = reciever = 'bugreporter.smr@mail.com'
    reciever = ['bugreporter.smr@mail.com']
    name = os.name
    uname = os.getlogin()
    hostname = socket.gethostname()
    build = platform.platform()
    email_string = """From: {sender}
To: {reciever}
Subject: bug in {project} on a {name} system :(

    
    platform:
        {build}

    machine name:
        {hostname}

    user name:
        {uname}
    
    details (traceback):
        {details}

    the message (even though it showed up before):
        {tbmessage}

    any extra things?
    
    {bottomline}


    sincerely, automatic message that has no heart :)""".format(**locals())
    print('hi')

    return email_string


def get_details(exception):
    """
    return the details of the traceback
    """

    tbstring = ''.join(
        traceback.format_exception(
            type(exception), exception, exception.__traceback__))
    tbargs = ', '.join(exception.args)
    return tbstring, tbargs


def default_smr(exception, *args):
    main('stickman\'s new world', exception, get_email(), *args)


if __name__ == '__main__':
    try:
        raise SyntaxError('this is a test message')

    except BaseException as e:
        mainwithmessage('test', e, get_email())
