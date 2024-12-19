import  pymupdf
from io import StringIO

input = "fliegende-fetzen.pdf"
output = "fliegende-fetzen_full.txt"

pdf = pymupdf.Document(input)
pages = pdf.page_count

def getTextFromPage(number):
    page = pdf.load_page(number)
    return page.get_text("text").replace("\n", "").replace(" " + str(number),"").replace("\"","\\\"").replace("!","\!")
content = StringIO()

for x in range(1, pages):
    content.write(getTextFromPage(x))

fileOut = open(output, "w")
fileOut.write(content.getvalue().replace("\n", "").replace("- ", "").replace("  ", " "))
fileOut.close()

print(output + " witten")


