import xml.etree.ElementTree as ET

# Reading the XML File (Importing data from file)
try:
    tree = ET.parse('vehicle.xml')
    root = tree.getroot()
    print(f"Root tag: {root.tag}")  # This will display 'motorvehicles'
except FileNotFoundError:
    print("Error: The file 'vehicle.xml' was not found.")

print("-" * 30)

# Iterating through the XML using a loop (Iterating children)
print("All vehicle types and their attributes:")
for child in root:
    print(child.tag, child.attrib)

print("-" * 30)

# Accessing data by Index
# root[0] refers to the first vehicle, [1] refers to its second sub-element (make)
make_of_first = root[0][1].text
print(f"Make of the first vehicle: {make_of_first}")

print("-" * 30)

# Searching for specific tags (Using iter)
print("List of Registration Numbers (using iter):")
for element in root.iter(tag='registration_no'):
    print(element.text)

print("-" * 30)

# Searching using the findall() function
print("Vehicle information using findall():")
for element in root.findall('vehicle'):
    regno = element.find('registration_no').text
    make = element.find('make').text
    print(f"Reg No: {regno}, Make: {make}")

print("-" * 30)

# Modifying XML data and writing to a new file
for element in root.iter(tag='make'):
    element.text = 'Nissan'  # Changes all 'make' tags to 'Nissan'

tree.write('output.xml')
print("XML successfully modified and saved as 'output.xml'.")
