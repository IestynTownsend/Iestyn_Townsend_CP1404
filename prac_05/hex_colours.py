color_codes = {
    "lightgray": "#d3d3d3",
    "ivory": "#fffff0",
    "aqua": "#00ffff",
    "black": "#000000",
    "blue": "#0000ff",
    "gold": "#ffd700",
    "crimson": "#dc143c",
    "darkgreen": "#006400",
    "indigo": "#4b0082",
    "magenta": "#ff00ff",
    "orange": "#ffa500",
    "pink": "#ffc0cb",
    "purple": "#800080",
    "salmon": "#fa8072",
    "teal": "#008080",
    "yellow": "#ffff00"
}

# Main loop to allow the user to look up color codes
while True:
    user_input = input("Enter a color name (or blank to exit): ").strip().lower()

    if not user_input:
        # If the user enters a blank line, exit the loop
        break

    color_code = color_codes.get(user_input, "Unknown color")
    print(f"The hexadecimal color code for {user_input} is {color_code}")
