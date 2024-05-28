#!/usr/bin/env python3
"""Module that serialize and deserialize data to xml/from xml"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize and save data to the file data"""
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Load and deserialize data from the argument file"""
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text
    return dictionary
