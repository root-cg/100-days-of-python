import colorgram

rgb_colors = []
colors = colorgram.extract("100-days-of-python\Day 18\angela\image.jpg", 30)
for color in colors:
    rgb_colors.append(color.rgb)

print(rgb_colors)   