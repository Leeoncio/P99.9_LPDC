import socket, os, datetime
import xml.etree.ElementTree as ET


tree = ET.parse('C:\Luminar\TS_Automation\Results\Tests_Evaluation_Report[05 56 08 p. m.][05 08 2021].xml')
root = tree.getroot()

header_dict =	{
    "SerialNumber": "",
    "Family": "",
    "PartNumber": "",
    "Revision": "",
    "Process": "",
    "Station": "",
    "Operator": "",
    "Fixture": "",
    "Socket": "",
    "SequenceName": "",
    "StartTime": None,
    "EndTime": None
}

def main_header():
    for result_list in root.findall("./Report/Prop/[@Type='TEResult']/Prop/[@Name='TS']/Prop/[@Name='SequenceCall']/Prop/[@Name='ResultList']/Value/..."):
        for values in result_list.findall("Value"):   
            if values.attrib.get('ID') == '[0]':     
                for additional_results in values.findall("./Prop/[@Type='TEResult']/Prop/[@Name='AdditionalResults']/Value/Prop/[@Name='Parameters']"):
                    for parameters in additional_results:
                        for parameters_values in parameters:
                            # print(parameters_values.attrib)
                            if parameters_values.attrib.get('Name') == 'Operator out [Out]':
                                header_dict["Operator"] = str(parameters_values.find('Value').text)
                            if parameters_values.attrib.get('Name') == 'Serial Number out [Out]':
                                header_dict["SerialNumber"] = str(parameters_values.find('Value').text)
                            if parameters_values.attrib.get('Name') == 'Family out [Out]':
                                header_dict["Family"] = str(parameters_values.find('Value').text)
                            if parameters_values.attrib.get('Name') == 'Part Number out [Out]':
                                header_dict["PartNumber"] = str(parameters_values.find('Value').text)
                            if parameters_values.attrib.get('Name') == 'Revision out [Out]':
                                header_dict["Revision"] = str(parameters_values.find('Value').text)
                            if parameters_values.attrib.get('Name') == 'Process out [Out]':
                                header_dict["Process"] = str(parameters_values.find('Value').text)
                            if parameters_values.attrib.get('Name') == 'Fixture out [Out]':
                                header_dict["Fixture"] = str(parameters_values.find('Value').text)
                            
    header_dict["Station"] = str(socket.gethostname())
    header_dict["Socket"] = "NA"        
    
    sequence_file_name_path = root.find("./Report/Prop/[@Type='TEResult']/Prop/[@Name='TS']/Prop/[@Name='SequenceCall']/Prop/[@Name='SequenceFile']")
    sequence_file_name = os.path.splitext((os.path.basename(sequence_file_name_path.find('Value').text)))[0]
    header_dict["SequenceName"] = sequence_file_name
    
       
    StartTime_hours = int((root.find("./Report/Prop/[@Name='StartTime']/Prop/[@Name='Hours']")).find('Value').text)
    StartTime_minutes = int((root.find("./Report/Prop/[@Name='StartTime']/Prop/[@Name='Minutes']")).find('Value').text)
    StartTime_seconds = int((root.find("./Report/Prop/[@Name='StartTime']/Prop/[@Name='Seconds']")).find('Value').text)
    StartTime = datetime.datetime(100,1,1,StartTime_hours,StartTime_minutes,StartTime_seconds)
    header_dict["StartTime"] = str((StartTime).time())      
    
    TotalTime = (root.find("./Report/Prop/[@Type='TEResult']/Prop/[@Name='TS']/Prop/[@Name='TotalTime']")).find('Value').text
    EndTime = (StartTime + datetime.timedelta(seconds = int(float(str(TotalTime))))).time()
    header_dict["EndTime"] = str(EndTime)


main_header()


