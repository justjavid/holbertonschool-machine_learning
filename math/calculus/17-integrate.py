def poly_integral(poly, C=0):
    if not isinstance(poly, list) or \
    not all(isinstance(x, int) for x in poly) or poly == []:
        return None
    poly.insert(0, C)
    for x in range(1, len(poly)):
        poly[x] = poly[x] / x
    return poly
