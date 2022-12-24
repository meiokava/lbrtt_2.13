#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from printmsg_md import print_msg as pm

if __name__ == '__main__':
    d = "dear {f} {n} you have done a great job"
    another = pm(d)
    print(another("Gloria", "Labron"))
