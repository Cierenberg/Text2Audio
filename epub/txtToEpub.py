#import pypub
from io import StringIO
from epub import Epub

display_name = "Heiße Hüpfer"
name = "heisse-huepfer"
author = "Terry Pratchet"
cover = "hh.png"
intro = "ein neuer Geniestreich von <i>Terry Pratchett</i>, dem erfolgreichsten englischen Autor der Gegenwart.<hr /><br />"
intro = intro + "<b>Zusammenfassung:</b> Irgendwo am Ende der Scheibenwelt gibt es einen Kontinent, der nur als mißratene Schöpfung bezeichnet werden kann. Dort ist es heiß und trocken, und alles, was nicht sowieso giftig ist, kann tödlich wirken. Also das glatte Gegenteil vom schönsten Ort auf der ganzen Welt, und es droht mit ihm endgültig zur Neige zu gehen. Als Retter kommt nur ein Mann mit Hut in Frage, der dort durch die rote Wüste wandert. Ein Zauberer, der nicht einmal weiß, wie <i>Zauberer</i> geschrieben wird. Rincewind, der letzte Held…"


input = name + ".txt"
tmp_html = name + ".html"
output = name + ".epub"

pre = "<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.1//EN\" \"http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd\">\n<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"de\">\n\t<head>\n\t\t<title>" + display_name + "</title>\n\t</head>\n\t<body>\n\t\t<p>\n"
post = "\n\t\t</p>\n\t</body>\n</html>"

content = StringIO()

file = open("../" + input, "r")
file_content = file.read()
file.close()

'''
#file_content = file_content.replace("ä","&auml;").replace("Ä","&Auml;")
#file_content = file_content.replace("ö","&ouml;").replace("Ö","&Ouml;")
#file_content = file_content.replace("ü","&uuml;").replace("Ü","&Uuml;")

content.write(pre)
content.write(file_content)
content.write(post)

fileOut = open(tmp_html, "w")
fileOut.write(content.getvalue())
fileOut.close()
'''

epub = Epub(name) # the file name to save without suffix, such as mybook
epub.set_title(display_name)
epub.add_author(author)
epub.add_intro(intro)
epub.add_cover(cover)
epub.set_language("en-en")
epub.create_chapter(1, display_name, file_content, False)
epub.create()

'''
epub = pypub.Epub(display_name)
chapter = pypub.create_chapter_from_file(tmp_html, name)
epub.add_chapter(chapter)
epub.create(output)
'''