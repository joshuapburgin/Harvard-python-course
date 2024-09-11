import sys
import json
import requests
import pyfiglet



available_fonts= pyfiglet.FigletFont.getFonts()




if len(sys.argv) != 3 or (sys.argv[1] not in ["--font", "-f"]):
    sys.exit("Usage: python script.py --font [FONT_NAME]")
if sys.argv[2] not in available_fonts:
    sys.exit("font not found")

chosen_font = sys.argv[2]

string_word= input("Input: ")
object_font= pyfiglet.Figlet(font=chosen_font)
print(object_font.renderText(string_word))
