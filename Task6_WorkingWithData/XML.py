from xml.dom import minidom


def main():
    filepath = r'XML_Original.xml'
    xmldoc = minidom.parse(filepath)

    born = xmldoc.createElement("date_of_birth")
    born.setAttribute("val", "13.06.1962")
    xmldoc.firstChild.appendChild(born)

    xmldoc.getElementsByTagName("first_name")[0].childNodes[0].nodeValue = "Jerzy"
    xmldoc.getElementsByTagName("last_name")[0].childNodes[0].nodeValue = "Kiler"

    with open("XML_Modified.xml", "w") as fs:
        fs.write(xmldoc.toxml())
        fs.close()


if __name__ == '__main__':
    main()
