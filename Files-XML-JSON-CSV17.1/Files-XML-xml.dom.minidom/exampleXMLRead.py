from xml.dom import minidom

# Parse an XML file
doc = minidom.parse('Files-XML-xml.dom.minidom\\example.xml')

# Access elements and attributes
books = doc.getElementsByTagName('book')
for book in books:
	title = book.getElementsByTagName('title')[0].firstChild.nodeValue
	author = book.getElementsByTagName('author')[0].getElementsByTagName('name')[0].firstChild.nodeValue
	print(f"Title: {title}, Author: {author}")
