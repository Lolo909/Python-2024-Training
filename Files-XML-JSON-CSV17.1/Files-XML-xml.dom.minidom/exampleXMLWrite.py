from xml.dom import minidom

# Create an XML document
doc = minidom.Document()

library = doc.createElement('library')
doc.appendChild(library)

book1 = doc.createElement('book')
book1.setAttribute('id', '1')

title1 = doc.createElement('title')
title1.appendChild(doc.createTextNode('Introduction to XML'))
book1.appendChild(title1)

library.appendChild(book1)

# Write to a file
with open('Files-XML-xml.dom.minidom\\library.xml', 'w') as file:
	doc.writexml(file, indent='\t', addindent='\t', newl='\n')
