# Evangelos Kontopantelis, David A Springate, David Reeves, Darren M. Aschroff, Martin Rutter, Iain Buchan, Tim Doran, Matthias Pierce, Darren M. Ashcroft, 2023.

import sys, csv, re

codes = [{"code":"1455","system":"gprdproduct"},{"code":"25047","system":"gprdproduct"},{"code":"26237","system":"gprdproduct"},{"code":"4111","system":"gprdproduct"},{"code":"41651","system":"gprdproduct"},{"code":"41652","system":"gprdproduct"},{"code":"43547","system":"gprdproduct"},{"code":"445","system":"gprdproduct"},{"code":"6008","system":"gprdproduct"},{"code":"7056","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('alpha-blockers-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["alpha-blockers-400microgram---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["alpha-blockers-400microgram---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["alpha-blockers-400microgram---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
