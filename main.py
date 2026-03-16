# drill 2
from pyscript import display, document


def area_triangle(base, height):
    return {'base' : base, 'height' : height}


def compute_area(e):
    
    base = float(document.getElementById("base").value)
    height = float(document.getElementById("height").value)

    area = area_triangle(base, height)

    output = f"""
    Base: {base} <br>
    Height: {height} <br>
    Area of Triangle: {area} <br>
    """

    document.getElementById("display").innerHTML = output