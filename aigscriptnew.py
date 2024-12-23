from genericpath import exists
import os
import shutil
import time
import webbrowser

githubFolderPath = "C:\\Users\\samue\\Documents\\GitHub\\AIG-ModelMatching-For-MSFS\\Community\\"
comFolderPathMain = "F:\MSFS\Addons\AI Traffic\\"
#names of the folders/files inside the aig main folder that we will copy
componentFolderNames = ["Effects", "SimObjects", "Sound", "Texture", "Traffic Files", "BritishAvgeeks-AIG-MSFS-Vatsim-Rules.vmr", "layout.json", "manifest.json"]

def clearGithubDir(): #clears the github folder of all files and remakes it empty
    print("Clearing Github Folder")
    if exists(githubFolderPath):
        shutil.rmtree(githubFolderPath)
        print("Github Folder Cleared")
    os.makedirs(githubFolderPath) #folder doesnt already exist - make it 
    os.mkdir(githubFolderPath + "aig-aitraffic-oci-beta")
    print("Blank Community Folder Made At " + githubFolderPath)
    print("#############################################################################")

def copyFiles():
    #copy to github
    shutil.move(comFolderPathMain + "aig-aitraffic-effects\\", githubFolderPath) #copy aig-aitraffic-effects
    shutil.move(comFolderPathMain + "aig-aitraffic-modelbehavior\\", githubFolderPath) #copy aig-aitraffic-modelbehavior

    for name in componentFolderNames:
        print("moving " + comFolderPathMain + "aig-aitraffic-oci-beta\\" + name + " to " + githubFolderPath + "aig-aitraffic-oci-beta\\" + name )
        shutil.move(comFolderPathMain + "aig-aitraffic-oci-beta\\" + name, githubFolderPath + "aig-aitraffic-oci-beta")
        print("moved " + comFolderPathMain + "aig-aitraffic-oci-beta\\" + name + " to " + githubFolderPath + "aig-aitraffic-oci-beta\\" + name )
    print("################")

    os.startfile(os.getenv('LOCALAPPDATA') + "\\GitHubDesktop\\GitHubDesktop.exe")
    
    input("push changes to github or ZIP then press enter to continue")
    print("################")

    #copy back to commnunity
    print("moving files back to " + comFolderPathMain)
    shutil.move(githubFolderPath + "aig-aitraffic-effects\\", comFolderPathMain)
    shutil.move(githubFolderPath + "aig-aitraffic-modelbehavior\\", comFolderPathMain)
    #DOESNT WORK FOR NOW - shutil.move(githubFolderPath + "aig-aitraffic-oci-beta\\", comFolderPathMain)
    print("moved files back to " + comFolderPathMain)
    print("#############################################################################")


def start(): #main function
    clearGithubDir()
    copyFiles()

#######################################

start()