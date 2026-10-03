"""Original procedural illustration; no downloaded image, stock art, or model input."""
import math
import random
from PIL import Image, ImageDraw


def make_artwork(directory):
    directory.mkdir(parents=True, exist_ok=True)
    size = 1536
    canvas = Image.new('RGB', (size, size), '#172e32')
    draw = ImageDraw.Draw(canvas)
    cream, orange, dark = '#f3dfae', '#ff6841', '#172e32'
    random.seed(31)
    # A screen-print inspired botanical moon, constructed from original geometry.
    draw.ellipse((270, 130, 1266, 1126), fill=orange)
    draw.ellipse((435, 74, 1280, 925), fill=dark)
    for index in range(90):
        x, y = random.randrange(90, 1450), random.randrange(80, 1430)
        if 330 < x < 1260 and y < 1160:
            continue
        radius = random.choice([2, 3, 5])
        draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill=cream)
    # A large moth with mirrored curved wings and dense etched lines.
    cx, cy = 782, 763
    for side in (-1, 1):
        outer = []
        for index in range(161):
            t = index / 160 * math.pi
            x = cx + side * (48 + 505 * math.sin(t)**0.78)
            y = cy - 270 + 630 * (t/math.pi) + 52 * math.sin(3*t)
            outer.append((x, y))
        outer += [(cx + side*35, cy+305), (cx + side*38, cy-210)]
        draw.polygon(outer, fill=cream)
        draw.line(outer + [outer[0]], fill=dark, width=12, joint='curve')
        for index in range(17):
            angle = -1.15 + index * 0.131
            points = []
            for step in range(45):
                r = 42 + step * 10
                x = cx + side * (40 + r*math.cos(angle))
                y = cy + r*math.sin(angle) + 80*(r/490)**2
                points.append((x,y))
            draw.line(points, fill=dark, width=5, joint='curve')
        eye_x = cx + side*330
        draw.ellipse((eye_x-118,cy-130,eye_x+118,cy+106), fill=orange, outline=dark, width=12)
        draw.ellipse((eye_x-70,cy-85,eye_x+70,cy+55), fill=dark)
        draw.ellipse((eye_x-27,cy-63,eye_x+27,cy-9), fill=cream)
        # Leaf sprays below the moth.
        for index in range(6):
            y = 1060 + index*53
            x = 440 - index*31 if side == -1 else 1100 + index*31
            draw.line([(780,1465),(x,y)], fill=cream, width=7)
            draw.ellipse((x-55,y-27,x+55,y+27), fill=cream)
    draw.ellipse((748,526,818,1090), fill=dark, outline=orange, width=8)
    draw.ellipse((745,497,820,572), fill=cream)
    draw.arc((652,387,790,598),200,340,fill=cream,width=9)
    draw.arc((776,387,914,598),200,340,fill=cream,width=9)
    for y in range(605,1010,35):
        draw.line([(765,y),(800,y+4)],fill=cream,width=4)
    draw.arc((90,65,1445,1420),12,165,fill=cream,width=3)
    canvas.save(directory / 'source-artwork.png')
    # Keep the reduction controlled and explicit. The model never sees the master.
    small = canvas.resize((256,256),Image.Resampling.LANCZOS)
    small.save(directory / 'input.jpg', quality=48, subsampling=2, optimize=False)
    return canvas
