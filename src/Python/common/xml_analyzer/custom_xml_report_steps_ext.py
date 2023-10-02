import socket, os, datetime
import xml.etree.ElementTree as ET

xml_1 = 'C:\Luminar\TS_Automation\Results\Tests_Evaluation_Report[05 56 08 p. m.][05 08 2021].xml'
xml_2 = 'C:\Luminar\TS_Automation\Results\Tests_Evaluation_Report[08 05 10 p. m.][07 08 2021].xml'
tree = ET.parse(xml_2)
root = tree.getroot()
        
        
def main_steps(element,StepID):
    global step_count, param_dict_list
    steps_param = ["Id","StepName","StepType","StepStatus","StepResult","SequenceName","SequencePath","Exectime","StringLimit","StringResult","NumericLimitHigh","NumericLimitLow","NumericUnit","NumericResult","FailCode","FailDescription"]
    for values in element.findall("Value"):     
        # print(values.attrib)
        if values.attrib.get("ID") == "["+str(StepID)+"]":
            print(values.attrib.get("ID"))
        
            param_dict = dict.fromkeys(steps_param)
            
            #param generic for all step types
            param_dict["Id"] = StepID + 1
            param_dict["StepName"] = (values.find("./Prop/[@Type='TEResult']/Prop/[@Name='TS']/Prop/[@Name='StepName']")).find('Value').text
            param_dict["StepType"] = (values.find("./Prop/[@Type='TEResult']/Prop/[@Name='TS']/Prop/[@Name='StepType']")).find('Value').text
            param_dict["StepStatus"] = (values.find("./Prop/[@Type='TEResult']/Prop/[@Name='Status']")).find('Value').text
            # param_dict["StepResult"] = 
            param_dict["SequenceName"] = (values.find("./Prop/[@Type='TEResult']/Prop/[@Name='TS']/Prop/[@Name='StepGroup']")).find('Value').text
            param_dict["SequencePath"] = repr(str(sequence_file_name) + "\\" + str(param_dict.get("SequenceName")))
            param_dict["Exectime"] = (values.find("./Prop/[@Type='TEResult']/Prop/[@Name='TS']/Prop/[@Name='TotalTime']")).find('Value').text
            
            ##Verify steptype 
            if param_dict.get("StepType") == "NumericLimitTest":
                param_dict["NumericLimitHigh"] = (values.find("./Prop/[@Type='TEResult']/Prop/[@Name='Limits']/Prop/[@Name='High']")).find('Value').text
                param_dict["NumericLimitLow"] = (values.find("./Prop/[@Type='TEResult']/Prop/[@Name='Limits']/Prop/[@Name='Low']")).find('Value').text
                param_dict["NumericResult"] = (values.find("./Prop/[@Type='TEResult']/Prop/[@Name='Numeric']")).find('Value').text
                param_dict["NumericUnit"] = (values.find("./Prop/[@Type='TEResult']/Prop/[@Name='Units']")).find('Value').text
                
            if param_dict.get("StepType") == "StringValueTest":
                param_dict["StringLimit"] = (values.find("./Prop/[@Type='TEResult']/Prop/[@Name='Limits']/Prop/[@Name='String']")).find('Value').text
                param_dict["StringResult"] = (values.find("./Prop/[@Type='TEResult']/Prop/[@Name='String']")).find('Value').text
            
            if param_dict.get("StepStatus") == "Failed":
                param_dict["FailCode"] = (values.find("./Prop/[@Type='TEResult']/Prop/[@Name='Error']/Prop/[@Name='Code']")).find('Value').text
                param_dict["FailDescription"] = (values.find("./Prop/[@Type='TEResult']/Prop/[@Name='Error']/Prop/[@Name='Msg']")).find('Value').text
            
            param_dict_list[StepID].append(param_dict)





def main():
    global sequence_file_name_path, sequence_file_name, step_count, param_dict_list
    
    sequence_file_name_path = root.find("./Report/Prop/[@Type='TEResult']/Prop/[@Name='TS']/Prop/[@Name='SequenceCall']/Prop/[@Name='SequenceFile']")
    sequence_file_name = os.path.splitext((os.path.basename(sequence_file_name_path.find('Value').text)))[0]
    
    step_count = 0
    for result_list in root.findall("./Report/Prop/[@Type='TEResult']/Prop/[@Name='TS']/Prop/[@Name='SequenceCall']/Prop/[@Name='ResultList']/Value/..."):
        steps = len(result_list.findall("Value"))
        print(steps)
        
        param_dict_list = [[] for i in range(steps)]
        for values in result_list.findall("Value"):     
            StepType = (values.find("./Prop/[@Type='TEResult']/Prop/[@Name='TS']/Prop/[@Name='StepType']")).find('Value').text
            print(StepType)
            if StepType == "SequenceCall":
                print("Make sublist and call main_steps()")
                print(values.attrib)
                main_steps(result_list, step_count)
                step_count += 1
            
            
            
            else:
                main_steps(result_list, step_count)
         
                step_count += 1  

# main_steps()
main()
'''
Id
StepName
StepType
StepStatus
StepResult
SequenceName
SequencePath
Exectime
StringLimit
StringResult
NumericLimitHigh
NumericLimitLow
NumericUnit
NumericResult
FailCode	
FailDescription	
'''            
