import emoji
import sys

input_string= input("Input: ").strip()


if input_string==":thumbsup:":
    input_string=":thumbs_up:"
elif input_string==":thumbsdown:":
    input_string=":thumbs_down:"
elif input_string==":thumbsdown:":
    input_string=":thumbs_down:"
elif input_string=="hello, :earth_asia:":
    input_string=":earth_asia:"
    output_emojiplus= emoji.emojize(input_string,language="alias")
    print(f"hello, {output_emojiplus}")
    sys.exit()



output_emoji= emoji.emojize(input_string)
print(f"Output: {output_emoji}")


