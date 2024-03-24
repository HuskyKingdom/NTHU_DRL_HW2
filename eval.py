from xml.etree import ElementTree as ET

# retrive submission meta info

xml_file_path = 'meta.xml'

tree = ET.parse(xml_file_path)
root = tree.getroot()

sub_name = ""

for book in root.findall('info'):
    sub_name =  book.find('name').text

print(sub_name)