

header_dict = {'SerialNumber': '001', 'Family': 'Iris Slim', 'PartNumber': '1234', 'Revision': 'R001', 'Process': 'Bring Up', 'Station': 'LAPTOP-RQS41FNE', 'Operator': 'MBE', 'Fixture': 'TCU_001', 'Socket': 'NA', 'SequenceName': 'Tests_Evaluation', 'StartTime': '17:56:08', 'EndTime': '17:56:37'}
UUTResult_dict = {'UUTResult': 'Failed', 'FailCode': None, 'FailDescription': None, 'Exectime': None}
param_dict_list = [[{'Id': 1, 'StepName': 'Sensor_Info', 'StepType': 'Action', 'StepStatus': 'Skipped', 'StepResult': None, 'SequenceName': 'Main', 'SequencePath': "'Tests_Evaluation\\\\Main'", 'Exectime': '9e-06', 'StringLimit': None, 'StringResult': None, 'NumericLimitHigh': None, 'NumericLimitLow': None, 'NumericUnit': None, 'NumericResult': None, 'FailCode': None, 'FailDescription': None}], [{'Id': 2, 'StepName': 'Evaluate Statement', 'StepType': 'Statement', 'StepStatus': 'Done', 'StepResult': None, 'SequenceName': 'Main', 'SequencePath': "'Tests_Evaluation\\\\Main'", 'Exectime': '4.49e-05', 'StringLimit': None, 'StringResult': None, 'NumericLimitHigh': None, 'NumericLimitLow': None, 'NumericUnit': None, 'NumericResult': None, 'FailCode': None, 'FailDescription': None}], [{'Id': 3, 'StepName': 'Evaluate String', 'StepType': 'StringValueTest', 'StepStatus': 'Passed', 'StepResult': None, 'SequenceName': 'Main', 'SequencePath': "'Tests_Evaluation\\\\Main'", 'Exectime': '4.78e-05', 'StringLimit': 'Legion Connected', 'StringResult': 'Legion Connected', 'NumericLimitHigh': None, 'NumericLimitLow': None, 'NumericUnit': None, 'NumericResult': None, 'FailCode': None, 'FailDescription': None}], [{'Id': 4, 'StepName': 'Evaluate Number', 'StepType': 'NumericLimitTest', 'StepStatus': 'Failed', 'StepResult': None, 'SequenceName': 'Main', 'SequencePath': "'Tests_Evaluation\\\\Main'", 'Exectime': '6.77e-05', 'StringLimit': None, 'StringResult': None, 'NumericLimitHigh': '20', 'NumericLimitLow': '10', 'NumericUnit': 'KM', 'NumericResult': '7', 'FailCode': '0', 'FailDescription': None}], [{'Id': 5, 'StepName': 'Subsequence_call', 'StepType': 'SequenceCall', 'StepStatus': 'Failed', 'StepResult': None, 'SequenceName': 'Main', 'SequencePath': "'Tests_Evaluation\\\\Main'", 'Exectime': '0.0132732', 'StringLimit': None, 'StringResult': None, 'NumericLimitHigh': None, 'NumericLimitLow': None, 'NumericUnit': None, 'NumericResult': None, 'FailCode': '0', 'FailDescription': None}], [{'Id': 6, 'StepName': 'Evaluate Boolean', 'StepType': 'PassFailTest', 'StepStatus': 'Passed', 'StepResult': None, 'SequenceName': 'Main', 'SequencePath': "'Tests_Evaluation\\\\Main'", 'Exectime': '4.04e-05', 'StringLimit': None, 'StringResult': None, 'NumericLimitHigh': None, 'NumericLimitLow': None, 'NumericUnit': None, 'NumericResult': None, 'FailCode': None, 'FailDescription': None}]]
report_file = open('report_sample.xml', 'a')

def write_header():
    global report_file
    report_file.write('<?xml version="1.0" encoding="iso-8859-1" ?>\n\n')
    report_file.write('<header>\n')
    
    header_list = list(header_dict.keys()) 
    for header_element in header_list:
        report_file.write('\t'+'<'+header_element+'><Value>'+str(header_dict.get(header_element))+'</Value></'+header_element+'>\n')
    report_file.write('</header>\n')


def write_uutResult():
    global report_file
    report_file.write('<UUTResult>\n')
    
    UUTResult_list = list(UUTResult_dict.keys())
    for uut_element in UUTResult_list:
        report_file.write('\t'+'<'+uut_element+'><Value>'+str(UUTResult_dict.get(uut_element))+'</Value></'+uut_element+'>\n')
    report_file.write('</UUTResult>\n')


def write_stepResults():
    global report_file
    
    report_file.write("<StepResults StepCount='"+str(len(param_dict_list))+"'>\n")
    for stepArray in range(len(param_dict_list)):
        report_file.write("\t<StepArray id='"+str(stepArray+1)+"'>\n")
        temp_param_dict = param_dict_list[stepArray][0]
        temp_stepResults_list = list(temp_param_dict.keys()) 
        for step_element in temp_stepResults_list:
            report_file.write('\t\t'+'<'+step_element+'><Value>'+str(temp_param_dict.get(step_element))+'</Value></'+step_element+'>\n')
        report_file.write('\t</StepArray>\n')
    report_file.write('</StepResults>\n')

write_header()
write_uutResult()
write_stepResults()
report_file.close()