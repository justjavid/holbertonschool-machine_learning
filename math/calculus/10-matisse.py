#!/usr/bin/env python3
def poly_derivative(poly):
    if not isinstance(poly, list) or \
    not all(isinstance(x, int) for x in poly):
        return None
    poly.remove(poly[0])
    for x in range(len(poly)):
        poly[x] = poly[x] * (x + 1)
    return poly
