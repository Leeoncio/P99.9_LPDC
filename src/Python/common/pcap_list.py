import os


def pcap_list(path, index):
    pcaps = []
    for file in os.listdir(path):
        if file.endswith(".pcap"):
            #print(os.path.join(path, file))
            #pcaps.append(os.path.join(path, file))
            pcaps.append(file)
    print("\n"+ str(len(os.listdir(path))))
    return pcaps
            

#pcaps = pcap_list("C:\\temp\\302_POD", 3)
#print(pcaps[0])