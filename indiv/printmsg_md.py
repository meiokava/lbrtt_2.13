#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def print_msg(ms):

    def printer(nm, fm):
        data = ms.format(n=nm, f=fm)
        return data
    return printer

