# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 11:28:37 2025

@author: hanan
"""

import random
import string
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def generate_pro_captcha(text_length=6, width=250, height=100, font_size=45):
    # Générer le texte du captcha
    characters = string.ascii_letters + string.digits
    captcha_text = ''.join(random.choices(characters, k=text_length))

    # Créer une image avec fond aléatoire
    bg_color = (random.randint(180, 255), random.randint(180, 255), random.randint(180, 255))
    image = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(image)

    # Charger la police (vous pouvez changer le chemin de la police)
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()

    # Dessiner le texte avec rotation aléatoire pour chaque lettre
    for i, char in enumerate(captcha_text):
        x = 20 + i * (font_size - 5)
        y = random.randint(10, height - font_size - 10)
        char_image = Image.new('RGBA', (font_size, font_size), (0,0,0,0))
        char_draw = ImageDraw.Draw(char_image)
        char_draw.text((0,0), char, font=font, fill=(random.randint(0,120), random.randint(0,120), random.randint(0,120)))
        rotated_char = char_image.rotate(random.randint(-30,30), expand=1)
        image.paste(rotated_char, (x, y), rotated_char)

    # Ajouter des lignes aléatoires
    for _ in range(random.randint(5, 10)):
        start = (random.randint(0, width), random.randint(0, height))
        end = (random.randint(0, width), random.randint(0, height))
        draw.line([start, end], fill=(random.randint(50,150), random.randint(50,150), random.randint(50,150)), width=2)

    # Ajouter du bruit
    for _ in range(random.randint(300, 600)):
        x = random.randint(0, width-1)
        y = random.randint(0, height-1)
        draw.point((x, y), fill=(random.randint(0,255), random.randint(0,255), random.randint(0,255)))

    # Ajouter des courbes sinus pour complexifier le captcha
    for i in range(random.randint(1,3)):
        amplitude = random.randint(5, 15)
        frequency = random.uniform(0.05, 0.15)
        phase = random.uniform(0, 2*math.pi)
        for x in range(width):
            y = int((height/2) + amplitude * math.sin(frequency * x + phase))
            if 0 <= y < height:
                draw.point((x, y), fill=(random.randint(50,150), random.randint(50,150), random.randint(50,150)))

    # Appliquer un léger flou
    image = image.filter(ImageFilter.GaussianBlur(1))

    # Sauvegarder le captcha
    image.save("pro_captcha.png")
    print("Captcha généré :", captcha_text)

# Générer un captcha professionnel
generate_pro_captcha()
