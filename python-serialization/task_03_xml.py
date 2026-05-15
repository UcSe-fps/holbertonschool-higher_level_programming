#!/usr/bin/python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serializes a dictionary into an XML file.
    """
    # Create the root element <data>
    root = ET.Element("data")

    # Iterate through dictionary and create child elements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # XML only stores text/strings

    # Create the tree and write to file
    tree = ET.ElementTree(root)
    try:
        # encoding='utf-8' and xml_declaration=True are best practices
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        return True
    except Exception as e:
        print(f"Error writing XML: {e}")
        return False

def deserialize_from_xml(filename):
    """
    Reads an XML file and reconstructs it into a dictionary.
    """
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()

        # Reconstruct the dictionary from child elements
        deserialized_dict = {}
        for child in root:
            deserialized_dict[child.tag] = child.text

        return deserialized_dict

    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None
    except ET.ParseError:
        print(f"Error parsing XML file.")
        return None
