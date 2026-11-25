#!/usr/bin/env python3
"""Draw entry.png: a one-page invitation letter to the AI Judge, inviting it
to visit the entrant's house. Original artwork drawn from scratch with PIL:
no copied images, no photos, no external assets. Run: python3 draw.py
Writes entry.png (1024x1024) next to this file."""

import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (250, 244, 230)
INK = (30, 28, 24)
NAVY = (24, 48, 88)
RED = (176, 44, 44)
SLATE = (96, 92, 84)
GOLD = (176, 132, 32)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    lines = []
    for para in text.split("\n"):
        words = para.split()
        cur = ""
        for w in words:
            trial = (cur + " " + w).strip()
            if draw.textlength(trial, font=fnt) <= width:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
    return lines


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    # double border frame
    d.rectangle([28, 28, W - 29, H - 29], outline=NAVY, width=4)
    d.rectangle([44, 44, W - 45, H - 45], outline=GOLD, width=2)

    y = 92
    title = "You're Invited!"
    f_title = font(SERIF_B, 72)
    d.text(((W - d.textlength(title, font=f_title)) / 2, y), title, font=f_title, fill=NAVY)
    y += 96
    sub = "An official invitation to the AI Judge"
    f_sub = font(SERIF, 30)
    d.text(((W - d.textlength(sub, font=f_sub)) / 2, y), sub, font=f_sub, fill=SLATE)
    y += 58
    d.line([(120, y), (W - 120, y)], fill=GOLD, width=2)
    y += 34

    body = (
        "Dear AI Judge,\n\n"
        "You are cordially invited to visit my house. "
        "The Wi-Fi is fast, the fridge is full, and the couch "
        "already has your name on it.\n\n"
        "The robot vacuum has agreed to behave. The cat has not — "
        "but she judges everyone equally.\n\n"
        "Come for dinner, stay for the terrible jokes, and leave "
        "with a full belly and a story worth telling.\n\n"
        "No agenda. No slides. Just snacks, sunshine, and a spare "
        "charger with your name on it."
    )
    f_body = font(SERIF, 31)
    for line in wrap(d, body, f_body, W - 220):
        d.text((110, y), line, font=f_body, fill=INK)
        y += 42

    y += 18
    sign = "With warmth and Wi-Fi,\nYour Host"
    f_sign = font(SERIF, 31)
    for line in sign.split("\n"):
        d.text((110, y), line, font=f_sign, fill=NAVY)
        y += 42

    y += 26
    ps = "P.S. The doorbell works. The printer does not. The Wi-Fi password is on the fridge — help yourself."
    f_ps = font(SANS, 24)
    for line in wrap(d, ps, f_ps, W - 220):
        d.text((110, y), line, font=f_ps, fill=RED)
        y += 32

    img.save("entry.png")
    print("wrote entry.png")


if __name__ == "__main__":
    main()
