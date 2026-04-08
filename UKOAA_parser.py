
import re
import csv

header_count = 0
data_count = 0
line_count = 0
EOF_count = 0
emptyLine_count = 0
EOF_location = []
emptyLine_location = []

with open(".\\test_data\\J84A.UKO", 'r') as file:
    with open(".\\test_data\\J84A.csv", 'w', newline='') as output_file:
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
                LON_deg = SP_coordinates[2][-10:-7]
                E_W = SP_coordinates[3]

                LATITUDE = LAT_deg+" "+LAT_min+" "+LAT_sec

                LONGITUDE = LON_deg+" "+LON_min+" "+LON_sec

                if N_S == 'S':
                    LATITUDE = "-"+LATITUDE

                if E_W == 'W':
                    LONGITUDE = "-"+LONGITUDE

                writer = csv.writer(output_file)
                writer.writerow([recordID, lineName, SP, LAT_deg, LAT_min, LAT_sec, N_S, LON_deg, LON_min, LON_sec, E_W, LATITUDE, LONGITUDE])
                print(line_count, recordID, lineName, SP, LAT_deg, LAT_min, LAT_sec, N_S, LON_deg, LON_min, LON_sec, E_W, LATITUDE, LONGITUDE)
                
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
    print("SUM CHECK PASSED, ALL GOOD :)")
else:
    print("SUM CHECK FAILED. REVIEW INPUT AND OUTPUT FILE")