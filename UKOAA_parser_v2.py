
import re
import csv
import sys
import os
from pathlib import Path

def main():

    target_file = sys.argv[1]

    # Extracting file path, extension and name
    file_nameAndPath, file_ext = os.path.splitext(target_file) 
    file_name = os.path.basename(os.path.normpath(file_nameAndPath))
    output_f = file_nameAndPath+".csv"

    print(f"FULL PATH:\t{target_file}\n")
    print(f"FILE NAME:\t{file_name}{file_ext}\n")
    print(f"OUTPUT PATH:\t{output_f}\n")

    header_count = 0
    data_count = 0
    line_count = 0
    EOF_count = 0
    emptyLine_count = 0
    EOF_location = []
    emptyLine_location = []

    with open(target_file, 'r') as file:
        with open(output_f, 'w', newline='') as output_file:
            for line in file:
                line_count += 1

                stripped_line = line.strip()
                # print(stripped_line)
                if stripped_line.startswith("H"):
                    header_count += 1
                    print(line_count, stripped_line)
                elif stripped_line.startswith("S"):
                    data_count += 1
                    emptySpacesSplit = re.split(r'\s+', stripped_line)
                    # print(emptySpacesSplit)

                    recordID = emptySpacesSplit[0][0]
                    lineName = emptySpacesSplit[0][1:]
                    flag1 = emptySpacesSplit[2]
                    flag2 = emptySpacesSplit[3]

                    SP_coordinates = list(filter(None, re.split(r'([NSEW])', emptySpacesSplit[1]))) # Split (and keep) by N, S, E and/or W. Added a filter to remove empty elements and saved it in a list
                    # print(SP_coordinates)

                    LAT_sec = SP_coordinates[0][-5:]
                    LAT_min = SP_coordinates[0][-7:-5]
                    LAT_deg = SP_coordinates[0][-9:-7]
                    SP = SP_coordinates[0][:-9]
                    N_S = SP_coordinates[1]
                    LON_sec = SP_coordinates[2][-5:]
                    LON_min = SP_coordinates[2][-7:-5]
                    LON_deg = SP_coordinates[2][-9:-7]
                    E_W = SP_coordinates[3]

                    LATITUDE = LAT_deg+" "+LAT_min+" "+LAT_sec

                    LONGITUDE = LON_deg+" "+LON_min+" "+LON_sec

                    if N_S == 'S':
                        LATITUDE = "-"+LATITUDE

                    if E_W == 'W':
                        LONGITUDE = "-"+LONGITUDE

                    writer = csv.writer(output_file)
                    writer.writerow([recordID, lineName, SP, LAT_deg, LAT_min, LAT_sec, N_S, LON_deg, LON_min, LON_sec, E_W, LATITUDE, LONGITUDE])
                    print(f"{line_count}\t{recordID}\t{lineName}\t{SP}\t{LAT_deg}\t{LAT_min}\t{LAT_sec}\t{N_S}\t{LON_deg}\t{LON_min}\t{LON_sec}\t{E_W}\t{LATITUDE}\t{LONGITUDE}")
                    
                elif stripped_line.startswith("EOF"):
                    EOF_count += 1
                    EOF_location.append(line_count)
                    print(f"EOF reached in line {EOF_location}")

                else:
                    emptyLine_count += 1
                    emptyLine_location.append(line_count)
                    print(f"Empty line in {line_count}")

    print(f'''
    SUMMARY:
        Total number of lines: {line_count}
        Number of Header Rows: {header_count}
        Number of Data Rows:   {data_count}
        Number of EOF lines:   {EOF_count} in {EOF_location}
        Number of Empty lines: {emptyLine_count} in {emptyLine_location}
    ''')

    if line_count == header_count+data_count+EOF_count:
        print("===> SUM CHECK PASSED, ALL GOOD :) <=== \n\n")
    else:
        print("===> SUM CHECK FAILED. REVIEW INPUT AND OUTPUT FILE <=== \n\n")

if __name__ == "__main__":
    main()