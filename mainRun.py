#importation
import sys
import pandas
import utilities.importFile as importFile
import matplotlib.pyplot as plt


def run():

    path_outputFolder = ''
    path_File, path_outputFolder = importFile.get_pathFile_fromJson()

    #Import my data points
    datapoints = pandas.read_csv(path_File)  

    print(datapoints.keys())
    
    plt.figure()
    #Plot my data
    datapoints.plot.scatter(x='x', y='y')
    plt.title('Plot of points')
    #plt.show()
    plt.savefig( path_outputFolder + "plot_of_data.pdf", bbox_inches='tight')




if __name__ == '__main__':
    
    #run the main function
    run()
    pass