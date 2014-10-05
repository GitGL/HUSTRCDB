#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    
    import socket
    if socket.gethostname() == 'hustrc-desktop':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hustrcpro.settings")
    else:
        #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hustrcpro.settings_production")
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hustrcpro.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
