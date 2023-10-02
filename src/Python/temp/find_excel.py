import os


def find_excel(file_name):
    TTL_wd = str(os.getcwd() + '\TTL')
    TTL_files = os.listdir(TTL_wd)
    TTL_file_ = ""
    for file in TTL_files:
        if file_name in file:
            TTL_file_ = file

    return TTL_file_

#print(find_excel("PM0003658_16"))