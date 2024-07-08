import xml.etree.ElementTree as ET

# Parse an XML file
tree = ET.parse('Files-XML-xml.etree.ElementTree\\example.xml')
root = tree.getroot()

# Access elements and attributes
for book in root.findall('.//book'):
	title = book.find('title').text
	author = book.find('author/name').text
	print(f"Title: {title}, Author: {author}")
