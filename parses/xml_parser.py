import xml.dom.minidom

def main ():
    doc = xml.dom.minidom.parse("samplexml.xml")
    print(doc.nodeName)
    print(doc.firstChild.tagName)

    skills = doc.getElementsByTagName("skill")
    print("%d skills: " % skills.length)

    for skill in skills:
        print(skill.getAttribute("name"))

    newSkill = doc.createElement("skill")
    newSkill.setAttribute("name", "jquery")

    doc.firstChild.appendChild(newSkill)

    skills = doc.getElementsByTagName("skill")
    print("%d skills: " % skills.length)

    for skill in skills:
        print(skill.getAttribute("name"))
main()
