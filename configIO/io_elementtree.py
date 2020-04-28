import xml.etree.ElementTree as ET

# Saving Parameters
root = ET.Element("root")
default = ET.SubElement(root, "DEFAULT")
user = ET.SubElement(root, "User")

ET.SubElement(default, "param", name="scale").text = "1"
ET.SubElement(default, "param", name="x0").text = "2"
ET.SubElement(default, "param", name="y0").text = "3"
ET.SubElement(user, "param", name="Name").text = "yuangreg"

tree = ET.ElementTree(root)
tree.write("params.xml")


# Loading Parameters
tree = ET.parse('params.xml')
root = tree.getroot()

for item in root.iter():
    print(item)

param_list = {}
for item in root.iter('param'):
    param_list[item.attrib['name']] = item.text

print(param_list)