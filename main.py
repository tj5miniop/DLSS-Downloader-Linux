import os
import sys
import time

def main():
    print("Welcome to the DLSS Downloader!")
    version = input("Please enter the version of the DLSS you wish to replace with. You can choose from the following options: 2, 3, or 4: ")
    
    if version.isdigit():
        version = int(version)
        if version >= 2 and version <= 4:
            print("Using DLSS Version " + str(version))
            directory(version)
        else:
            print("Please enter a valid version number.")
            main()
    else:
        print("Please enter numbers only.")
        main()

def directory(dlss_version):
    print("Please enter the directory you wish to download the new version of DLSS to: ")
    directory = input().strip()  # Using strip() to avoid leading/trailing spaces.
    
    # Construct the command
    cmd = "cp -r DLSS_VERSIONS/" + str(dlss_version) + "/" + "nvngx_dlss.dll" + " " + directory
    print(cmd)
    os.system(cmd)
    print("DLSS Added to " + directory)

main()
