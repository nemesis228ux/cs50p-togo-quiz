from fpdf import FPDF


def main():
  name = input("Name: ")

  pdf = FPDF(orientation="P", format="A4")

  pdf.add_page()
  pdf.set_font(family="Helvetica", style="B", size=26)
  pdf.set_text_color(0, 0, 0)
  pdf.set_y(20)
  pdf.cell(w=0, h=10, text="CS50 Shirtificate", align="C")
  pdf.image("shirtificate.png", x=10, y=50, w=190)
  pdf.set_font(family="Helvetica", style="B", size=24)
  pdf.set_text_color(255, 255, 255)
  pdf.set_y(170)
  pdf.cell(0, 10, f"{name} took CS50", align="C")
  pdf.output("shirtificate.pdf")


if __name__ == "__main__":
  main()