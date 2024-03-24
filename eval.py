from xml.etree import ElementTree as ET
import importlib
import sys
# retrive submission meta info

xml_file_path = 'meta.xml'

tree = ET.parse(xml_file_path)
root = tree.getroot()

sub_name = ""

for book in root.findall('info'):
    sub_name =  book.find('name').text


agent_path = sub_name + "_hw2_test.py"

module_name = agent_path.replace('/', '.').replace('.py', '')
spec = importlib.util.spec_from_file_location(module_name, agent_path)
module = importlib.util.module_from_spec(spec)
sys.modules[module_name] = module
spec.loader.exec_module(module)
Agent = getattr(module, 'Agent')

print(Agent)