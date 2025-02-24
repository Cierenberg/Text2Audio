import  pymupdf
from io import StringIO
import string

input = "mummenschanz.pdf"
output = "mummenschanz_full.txt"
optimize_line_breaks = False
optimize_chapter = True
remove_exclamation_marks = False
remove_asteriks = False
remove_gt_lt = False
ensure_on_line = False
remove_multi_spaces = True
remove_multi_dots = False
break_after_sentences = False
min_line_length = 0
min_line_lengt_for_break = 2


pdf = pymupdf.Document(input)
pages = pdf.page_count

def getTextFromPage(number):
    global optimize_line_breaks
    global optimize_chapter
    global remove_exclamation_marks
    global remove_asteriks
    global remove_gt_lt
    global ensure_on_line
    global remove_multi_spaces
    global remove_multi_dots
    global break_after_sentences
    global min_line_length
    global pdf
    page = pdf.load_page(number)
    page_text = page.get_text("text")
    
    
    

    # for two paget pdf format
    num_min = 2*number + 4
    num_max = num_min + 1
    num_text_v1 = "\n" + str(num_max) + " \n" + str(num_min) + " \n"
    num_text_v2 = "\n" + str(num_min) + " \n" + str(num_max) + " \n"

    if num_text_v1 in page_text:
        page_text = page_text.replace(num_text_v1, "")
    if num_text_v2 in page_text:
        page_text = page_text.replace(num_text_v2, "")

    while page_text.endswith("\n"):
        page_text = page_text[:-1]
    while page_text.startswith("\n") or page_text.startswith(" "):
        page_text = page_text[1:]
        

    # for two paget pdf format
    num_min = 2*number + 4
    num_max = num_min + 1
    num_text_p1 = "\n" + str(num_max)
    num_text_p2 = str(num_min) + " "


    page_text = page_text.replace(str(number),"").replace("\"","'").replace("»","\"").replace("«","\"")
    page_text = page_text.replace(" - ", "").replace(" -", "").replace("- ", "").replace("-\n", "").replace("-", "")
    page_text = page_text.replace(num_text_p1, "").replace(num_text_p2, "")

    
    if "man nur schwer le" in page_text:
        print(">>" + page_text + "<<")
    

    if optimize_line_breaks: 
        page_text = page_text.replace(".\n","#END.#").replace("!\n","#END!#").replace("?\n","#END?#")
        page_text = page_text.replace("\n"," ")
        page_text = page_text.replace("#END.#",".\n" ).replace("#END!#","!\n").replace("#END?#","!\n")
    
  
              

    if ensure_on_line:
        page_text = page_text.replace("\n", " ")
    if remove_exclamation_marks:
        page_text = page_text.replace("!",".")
    if remove_asteriks:
        page_text = page_text.replace("*14","-")
    if remove_gt_lt:
        page_text = page_text.replace("<", " ").replace(">", " ")
    if remove_multi_dots:
        while ".." in page_text:
            page_text = page_text.replace("..", ".")
    if break_after_sentences:
        page_text = page_text.replace(". ", ".\n").replace("! ", ".\n").replace("? ", ".\n")
        min_line_length = 40
    if min_line_length > 0:
        min_length = min_line_length
        new_text = ""
        tmp_list = page_text.split("\n")
        offset = 0
        for line in tmp_list:
            new_text = new_text + line
            if len(line) + offset < min_length:
                offset = offset + len(line)
                new_text = new_text + " "
            else:
                offset = 0
                new_text = new_text + "\n"
        page_text = new_text


    return page_text

content = StringIO()

for x in range(1, pages):
    content.write(getTextFromPage(x))

content_string = content.getvalue()

if optimize_chapter:
    count = 0
    new_text = "<p>"
    tmp_list = content_string.split("\n")
    for line in tmp_list:
        if len(line) < min_line_lengt_for_break:
            if count == 0:
                new_text = new_text + line + "</p><br/><p>"
            else:
                new_text = new_text + line
            count += 1
        else:

            new_text = new_text + line
            count = 0
    content_string = new_text.replace("\n"," ").replace("\r"," ")
    content_string = content_string + "</p>"
    while "</p><br/><p></p><br/><p>" in content_string:
        print("*")
        content_string = content_string.replace("</p><br/><p></p><br/><p>", "</p><br/><p>") 
    while "</p><br/><p></p><p></p><br/><p>" in content_string:
            print(".")
            content_string = content_string.replace("</p><br/><p></p><p></p><br/><p>", "</p><br/><p>") 
if remove_multi_spaces:
    while "  " in content_string:
        content_string = content_string.replace("  ", " ")


fileOut = open(output, "w")
fileOut.write(content_string)
fileOut.close()

print(output + " witten")


