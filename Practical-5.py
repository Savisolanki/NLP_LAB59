'''Name:Savi Solanki
Batch:B3
Roll no:59
Pract no 5: Implement Regular Expression function to find PRN,Mobile No,DOB in textual data using libraries..'''

import re

def find_entities(text):

    result = {
        'PRN': re.findall(r'[A-Z]{3}[0-9]{2}[A-Z]{1}[0-9]{4}', text),
        'Mobile No': re.findall(r'([0-9]{10})', text),
        'Date oF Birth': re.findall(r'([0-9]{2}[A-Z]{3}[0-9]{4})', text),
    }
    return result

# Example usage:
sample_text = """
First Dataset
PRN: UIT20F1061
Mobile No : Contact to - 9881235104
Date: MY DOB is 12NOV2002


Second Dataset
PRN: UIT20F1046
Mobile No :Call on this no - 7972273450
Date: MY Friends DOB is 23JAN2003

"""

result = find_entities(sample_text)

for entity_type, entities in result.items():
    print(f"{entity_type}: {entities}")


"""

Output:
PRN: ['UIT20F1061', 'UIT20F1046']
Mobile No: ['9881235104', '7972273450']
Date oF Birth: ['12NOV2002', '23JAN2003']

"""
