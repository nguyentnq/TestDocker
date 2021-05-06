
import json


def get_pathFile_fromJson():
    ''' This function is for reading JSON file
    and return the path of the input file
    '''

    infoFileName = './info_inputFile.json'
    
    path_File = [];   

    with open(infoFileName) as json_file:
        data = json.load(json_file)

        for temp in data['dataFile']:
            path_File = temp['path']

        for temp in data['outputFolder']:
            path_outputFolder = temp['path']
    
    return path_File, path_outputFolder