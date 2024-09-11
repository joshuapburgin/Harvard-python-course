from fpdf import FPDF


def main():
    name=input("Name: ")
    #name="Joshua Burgin"

    create_pdf(name)

def create_pdf(name):
    pdf= FPDF(orientation="P",  format="A4")
    pdf.add_page()
    image_width = pdf.w / 2  # Set the image width to half of the page width
    image_height = pdf.h / 2  # Set the image height to half of the page height

    # Calculate the x coordinate to center the image horizontally
    x = (pdf.w - image_width) / 2

    # Calculate the y coordinate to center the image vertically
    y = (pdf.h - image_height) / 2

    pdf.image("shirtificate.png", x=x, y=y, w=image_width, h=image_height)

    pdf.set_font('helvetica', 'B', 20)





    pdf.set_y(10)

    pdf.cell(0, 10, 'CS50 Shirtificate', align='C')

    pdf.set_text_color(r=255, g=255, b=255)


    vertical_position = pdf.h/2

    # Set the vertical position
    pdf.set_y(vertical_position)

    pdf.cell(0,10, f"{name} took CS50",align='C')

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
