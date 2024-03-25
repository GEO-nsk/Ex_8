import json
import xml.etree.ElementTree as ET
import yaml

def to_format(output_type):
    def logger(func):
        def wrapped(*args):

            if output_type == 'JSON':
                func_ans = func(*args)
                result = json.dumps(func_ans)

            elif output_type == 'XML':
                func_ans = func(*args)
                xml = ET.Element('xml')
                for itr in func_ans:
                    ET.SubElement(xml, 'tag').text = itr
                xml_str = ET.tostring(xml)
                result = xml_str

            elif output_type == 'YAML':
                func_ans = func(*args)
                result = yaml.dump(func_ans)

            else:
                func_ans = func(*args)
                result = json.dumps(func_ans)


            return result
        return wrapped
    return logger

out_type = str(input())
ptr = str(input())

@to_format(output_type=out_type)
def data(ptr):
    return ptr.split()

print(data(ptr))
