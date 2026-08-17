import xml.etree.ElementTree as ET
import sys, copy
from struct import pack
from os import path
from dataclasses import dataclass, field

BOM = "big"
ENCODING_STRING = "utf-16be"
ENCODING_NAME = "utf-8"
MAGIC = b"\x58\x4D\x53\x47\x20\x10\x05\x03"

@dataclass
class message:
    name: str = ""
    type: str = ""
    text: str = ""
    exp_index: int = 0

#misnomer: styles
@dataclass
class expr:
    color: str = ""
    outline: str = ""
    width: int = 0
    height: int = 0
    horziontal_spacing: int = 0
    vertical_spacing: int = 0
    #size 3: start, middle, end
    states: list[int] = field(default_factory=list)

@dataclass
class XMSG:
    magic: bytes = MAGIC
    num_messages: int = 0
    messages: list[message] = field(default_factory=list)
    exp_start: int = 0
    #misnomer: styles of text
    expressions: list[expr] = field(default_factory=list)

def sortchildrenby(parent, attr) -> None:
    parent[:] = sorted(parent, key=lambda child: child.get(attr))

#reads full UTF-8 string data from an offset (until null terminator)
def get_message_name(mess: bytearray, offset: int) -> str:
    null_char_pos = mess[offset:].index(b"\x00") + offset
    return mess[offset:null_char_pos].decode(ENCODING_NAME)

#reads full UTF-16 string data from an offset (until null terminator)
def get_message_string(mess: bytearray, offset: int) -> str:
    null_char_pos = offset
    while mess[null_char_pos:null_char_pos+2] != b"\x00\x00":
        null_char_pos += 2
    return mess[offset:null_char_pos].decode(ENCODING_STRING)

#returns the start of the style section. It is the first offset to it in the message data.
def get_expression_section_start(mess: bytearray, NUM_MESSAGES: int) -> int:
    return min((int.from_bytes(mess[16*i + 24:16*i + 28], BOM) for i in range(NUM_MESSAGES)))

#converts mess.bin into deserialized structure
def deserialize(mess: bytearray) -> XMSG:
    data = XMSG()
    data.num_messages = int.from_bytes(mess[0x8:0x0C], BOM)
    data.exp_start = get_expression_section_start(mess, data.num_messages)
    pos = 0xC
    for i in range(data.num_messages):
        message_entry = message()
        message_entry.name = get_message_name(mess, int.from_bytes(mess[pos:pos+4], BOM))
        message_entry.type = get_message_name(mess, int.from_bytes(mess[pos+8:pos+12], BOM))
        message_entry.text = get_message_string(mess, int.from_bytes(mess[pos + 4:pos + 8], BOM))
        message_entry.exp_index = (int.from_bytes(mess[pos + 12:pos + 16], BOM) - data.exp_start) // 16
        data.messages.append(message_entry)
        pos += 16
    pos = data.exp_start
    for i in range((len(mess) - data.exp_start) // 16):
        expression = expr()
        expression.color = str(mess[pos:pos+4].hex())
        expression.outline = str(mess[pos+4:pos+8].hex())
        expression.width = int.from_bytes(mess[pos+8:pos+9])
        expression.height = int.from_bytes(mess[pos+9:pos+10])
        expression.horizontal_spacing = int.from_bytes(mess[pos+10:pos+11])
        expression.vertical_spacing = int.from_bytes(mess[pos+11:pos+12])
        expression.states.append(int.from_bytes(mess[pos+13:pos+14]))
        expression.states.append(int.from_bytes(mess[pos+14:pos+15]))
        expression.states.append(int.from_bytes(mess[pos+15:pos+16]))
        data.expressions.append(expression)
        pos += 16
    return data

#converts XML into deserialized structure
def deserialize_xml(filepath: str) -> XMSG:
    data = XMSG()
    xmsg_xml = ET.parse(filepath)
    xmsg = xmsg_xml.getroot()
    data.num_messages = len(xmsg.findall('message'))
    for mess in xmsg.findall('message'):
        message_entry = message()
        message_entry.name = mess.get('name')
        message_entry.type = mess.get('type')
        message_entry.text = mess.find('text').text
        message_entry.exp_index = int(mess.find('text').get('style'))
        data.messages.append(message_entry)
    em = xmsg.find('styles')
    for exp in em.findall('style'):
        expression = expr()
        states = exp.find('states')
        expression.color = exp.find('color').text
        expression.outline = exp.find('outline').text
        expression.width = int(exp.find('width').text)
        expression.height = int(exp.find('height').text)
        expression.horizontal_spacing = int(exp.find('horizontal_spacing').text)
        expression.vertical_spacing = int(exp.find('vertical_spacing').text)
        expression.states.append(int(states.find('start').text))
        expression.states.append(int(states.find('middle').text))
        expression.states.append(int(states.find('end').text))
        data.expressions.append(expression)
    return data

#packs deserialized structure into mess.bin and writes to filepath
def serialize(deser_org: XMSG, filepath: str) -> None:
    #deep copy in the case that we are going to keep using the deserialized file,
    #and we want messages to stay in the same order
    deser = copy.deepcopy(deser_org)
    deser.messages = sorted(deser.messages, key=lambda m:m.name)
    data = bytearray(deser.magic)
    data.extend(pack(">l", deser.num_messages))
    #blank space for message entries
    data.extend(pack(f'>{deser.num_messages * 16}x'))

    #name and type banks are interweaved, and they each cannot have duplicates
    #but the same string can appear in both name_bank and type_bank
    name_bank = {}
    type_bank = {}
    strings = {}
    for mess in deser.messages:
        if mess.name not in name_bank:
            name_bank[mess.name] = len(data)
            data.extend((mess.name).encode(ENCODING_NAME) + b"\x00")
        if mess.type not in type_bank:
            type_bank[mess.type] = len(data)
            data.extend((mess.type).encode(ENCODING_NAME) + b"\x00")
        if mess.text not in strings:
            strings[mess.text] = -1

    for string in list(strings):
        strings[string] = len(data)
        data.extend(string.encode(ENCODING_STRING) + b"\x00\x00")

    EMOTIONS_OFFSET = len(data)
    for exp in deser.expressions:
        data.extend(bytearray.fromhex(exp.color)[:4]) #only get first 4 bytes, otherwise invalid size
        data.extend(bytearray.fromhex(exp.outline)[:4])
        data.extend(pack(">8b", exp.width,
                                exp.height,
                                exp.horizontal_spacing,
                                exp.vertical_spacing,
                                0, #padding
                                exp.states[0],
                                exp.states[1],
                                exp.states[2]))

    #write message data and pointers
    for i in range(deser.num_messages):
        data[(i*16)+12:(i*16)+16] = pack(">l", name_bank[deser.messages[i].name])
        data[(i*16)+16:(i*16)+20] = pack(">l", strings[deser.messages[i].text])
        data[(i*16)+20:(i*16)+24] = pack(">l", type_bank[deser.messages[i].type])
        data[(i*16)+24:(i*16)+28] = pack(">l", int(deser.messages[i].exp_index * 16 + EMOTIONS_OFFSET))

    with open(filepath, 'wb') as saved_file:
        saved_file.write(data)

#packs deserialized data into xml and writes to filepath
def serialize_to_xml(deser_org: XMSG, filepath: str) -> None:
    #deep copy in the case that we are going to keep using the deserialized file,
    #and we want messages to stay in the same order
    deser = copy.deepcopy(deser_org)
    deser.messages = sorted(deser.messages, key=lambda m:m.name)
    root = ET.Element('XMSG')
    tree = ET.ElementTree(root)
    for mess in deser.messages:
        elem = ET.SubElement(root, 'message')
        elem.set('name', mess.name)
        elem.set('type', mess.type)
        elemText = ET.SubElement(elem, 'text')
        elemText.text = mess.text
        elemText.set('style', str(mess.exp_index))
    expressions = ET.SubElement(root, 'styles')
    for i in range(len(deser.expressions)):
        elem = ET.SubElement(expressions, 'style')
        elem.set('id', str(i))
        elemTextColor = ET.SubElement(elem, 'color')
        elemTextColor.text = deser.expressions[i].color
        elemOutline = ET.SubElement(elem, 'outline')
        elemOutline.text = deser.expressions[i].outline
        elemWidth = ET.SubElement(elem, 'width')
        elemWidth.text = str(deser.expressions[i].width)
        elemHeight = ET.SubElement(elem, 'height')
        elemHeight.text = str(deser.expressions[i].height)
        elemHP = ET.SubElement(elem, 'horizontal_spacing')
        elemHP.text = str(deser.expressions[i].horizontal_spacing)
        elemVP = ET.SubElement(elem, 'vertical_spacing')
        elemVP.text = str(deser.expressions[i].vertical_spacing)
        elemState = ET.SubElement(elem, 'states')
        elemStart = ET.SubElement(elemState, 'start')
        elemStart.text = str(deser.expressions[i].states[0])
        elemMid = ET.SubElement(elemState, 'middle')
        elemMid.text = str(deser.expressions[i].states[1])
        elemEnd = ET.SubElement(elemState, 'end')
        elemEnd.text = str(deser.expressions[i].states[2])

    tree._setroot(root)
    ET.indent(tree, '  ')
    tree.write(filepath, encoding = "UTF-8", xml_declaration = True)

def main():
    if len(sys.argv) != 3:
        print("Usage: xmsg.py source dest\n")
        exit()

    root, extension = path.splitext(sys.argv[1])
    if extension == ".xml":
        data = deserialize_xml(sys.argv[1])
        serialize(data, sys.argv[2])
    else:
        try:
            #no defined file extension for XMSG, any could be valid
            with open(sys.argv[1], 'rb') as raw_mess:
                file_magic = raw_mess.read(8)
                if(file_magic == MAGIC):
                    raw_mess.seek(0)
                    mess = raw_mess.read()
                    mess = bytearray(mess)
                    data = deserialize(mess)
                    serialize_to_xml(data, sys.argv[2])
                else:
                    print("Invalid filetype.\n")
                    exit()
        except FileNotFoundError:
            print("Could not open file " + sys.argv[1] + ".\n")
            exit()

if __name__ == '__main__':
    main()
