import socket, os, datetime
import xml.etree.ElementTree as ET

tree = ET.parse('C:\Luminar\TS_Automation\Results\Tests_Evaluation_Report[05 56 08 p. m.][05 08 2021].xml')
root = tree.getroot()

UUTResult_dict =	{
    "UUTResult": "",
    "FailCode": None,
    "FailDescription": "",
    "Exectime": None
}
       
def main_uut():
    UUTResult_dict["UUTResult"] = (root.find("./Report/[@Type='UUT']")).attrib.get("UUTResult")
    

            
main_uut()