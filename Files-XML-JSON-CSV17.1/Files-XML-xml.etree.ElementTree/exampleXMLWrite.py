import xml.etree.ElementTree as ET

# Create an XML document
root = ET.Element('library')

book1 = ET.SubElement(root, 'book', id='1')
title1 = ET.SubElement(book1, 'title')
title1.text = 'Introduction to XML'

book2 = ET.SubElement(root, 'book', id='2')
title2 = ET.SubElement(book2, 'title')
title2.text = 'Data Structures in Python'

# Create an ElementTree object
tree = ET.ElementTree(root)

# Write to a file
tree.write('Files-XML-xml.etree.ElementTree\\library.xml')
