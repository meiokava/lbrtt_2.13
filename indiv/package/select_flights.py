#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

def select_flights(flights, t):
    """
    selecting flights that are appropriate
    """
    result = []
    for flight in flights:
        if t in str(flight.values()):
            result.append(flight)
    return result