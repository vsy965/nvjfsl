import  xml.etree.ElementTree as ET

mytree = ET.parse("x1.xml")
myroot = mytree.getroot()

for prices in myroot.iter('price'):
    prices.text = str(float((prices.text).lstrip('$'))+10)
    prices.set('newprices', 'yes')

ET.SubElement(myroot[0], "tasty")
for temp in myroot.iter('tasty'):
    temp.text = str("YES")
mytree.write('modified.xml')


# import xml.etree.ElementTree as ET
# mytree = ET.parse("x1.xml")
# myroot = mytree.getroot()
# for prices in myroot.iter('price'):
#     prices.text = str(float(prices.text)+10)
#     prices.set('newprices', 'yes')
# ET.SubElement(myroot[0], "tasty")
# for temp in myroot.iter('tasty'):
#     temp.text = str("YES")
# # poping the element
# print(myroot[2][0].attrib.pop('name'))
# # Delete
# print(myroot.remove(myroot[2]))
# mytree.write('modified.xml')

