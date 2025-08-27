#!/usr/bin/env python3
def poly_integral(poly, C=0):
    if not isinstance(poly, list) or \
    not all(isinstance(x, int) for x in poly) or poly == []:
        return None
    if poly == [0]:
        return [C]
    poly.insert(0, C)
    for x in range(1, len(poly)):
        poly[x] = poly[x] / x
        if int(poly[x]) == poly[x]:
            poly[x] = int(poly[x])
    return poly

print(poly_integral([5], None))
