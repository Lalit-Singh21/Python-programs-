#XML parsing Programming

try:
    from lxml import etree
except:
    from xml.etree import ElementTree as etree

#build xml
root=etree.Element("root") #to build xml root
#print "Element",root,"Tag:",root.tag
#print etree.tostring(root)


child=etree.SubElement(root,"child") # to build xml child
#print etree.tostring(root)

child.set("property_1", "abc") #to set property of child tag
#child.text="Hello"
#print etree.tostring(root)

child2=etree.SubElement(child,"child_2") # to build xml child
#child2.text="Hello"
#print etree.tostring(root)

br=etree.SubElement(child2,"br") # to build xml child
br.text="Hello"
#print etree.tostring(root,pretty_print=True)
br.tail = "Python!"
print etree.tostring(root,pretty_print=True)


texts=["a","e","i","o","u",]

for text in texts:
    c=etree.SubElement(root,"child")
    c.text=text
print etree.tostring(root,pretty_print=True)


##printing memory
##for c in root:
##    print c

#print root[0]

##root.append(etree.Element("newchild"))
##print etree.tostring(root)


#parent and siblings
##child2=etree.SubElement(root, "child")
##print child.getparent(), child2.getparent()
##print child.getnext(),child2.getnext()
##



###basic xpath
print child2.xpath("string()")
#print child2.xpath("\\text()")
print etree.tostring(root)
print "element", root.xpath("./child")
for c in root.xpath(".//child2/br"):
    print c,c.tag


#iterating    
for elem in root.iter():
    print "%s - %s - %s" % (elem,elem.text,elem.tail)

xml1='''<root>
<child property_1="abc">
<child_2>
<br>Hello</br>Python!</child_2>
</child>
<child>a</child>
<child>e</child>
<child>i</child>
<child>o</child>
<child>u</child>
</root>'''
xml_obj=etree.xml(xml1)
print etree.tostring(xml_obj)
print xml_obj.xpath(".//child2")

####Iterations









