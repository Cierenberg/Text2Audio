import  pymupdf
from io import StringIO

input = "heisse-huepfer.pdf"
output = "heisse-huepfer_full.txt"
remove_exclamation_marks = False

pdf = pymupdf.Document(input)
pages = pdf.page_count

def getTextFromPage(number):
    page = pdf.load_page(number)
    
    # for two paget pdf format
    num_min = 2*number + 4
    num_max = num_min + 1
    num_text = str(num_max) + " " + str(num_min)

    page_text = page.get_text("text").replace("\n", "").replace(" " + str(number),"").replace("\"","\\\"").replace("\n", "").replace("- ", "").replace("<", " ").replace(">", " ").replace(num_text, "").replace("»","\"").replace("«","\"").replace("*","-").replace("-", "")
    
    if remove_exclamation_marks:
        page_text = page_text.replace("!",".")
    while "  " in page_text:
        page_text = page_text.replace("  ", " ")
    while ".." in page_text:
        page_text = page_text.replace("..", ".")

    #print("[DEBUG] Seite (" + str(number) + ") ;\n" + page_text)
    return page_text
content = StringIO()

for x in range(1, pages):
    content.write(getTextFromPage(x))

fileOut = open(output, "w")
fileOut.write(content.getvalue().replace("  ", " "))
fileOut.close()

print(output + " witten")


