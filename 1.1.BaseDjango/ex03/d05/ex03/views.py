from django.shortcuts import render

# Create your views here.

from django import http


def adjust_color_hex(hex_color, adjust_value=2, color='r'):
    hex_color = hex_color.lstrip('#')

    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    # On garde les valeurs entre 0 et 255
    color = max(0, min(255, color + adjust_value))

    r_hex = format(r, '02x')
    g_hex = format(g, '02x')
    b_hex = format(b, '02x')

    # Convertir à nouveau en hexadécimal
    if color == 'r':
        r_hex = format(color, '02x')  # Format en hex (2 caractères)

    elif color == 'g':
        g_hex = format(color, '02x')
    elif color == 'b':
        b_hex = format(color, '02x')

    # Retourner la couleur ajustée en hex
    return f"#{r_hex}{g_hex}{b_hex}"


def create_shader(hex_color, steps=50):
    start = ['r', 'g', 'b']
    colors = []
    for i in range(steps):
        colors.append(adjust_color_hex(hex_color, i * 2, 'r'))
    return colors


def test(request):
    colors = []
    start = ['#ff0000', '#00ff00', '#0000ff', '#ffff00']

    for i in range(4):
        colors.append(create_shader(start[i]))

    print(colors)

    return render(request, 'bic.html', context={'cols': range(4),
                                                'rows': range(50)})
