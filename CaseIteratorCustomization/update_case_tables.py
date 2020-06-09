import os
import json
import csv
import fnmatch

def remove_irr_files(folder):	
	# Get a list of all files in directory
    for rootDir, subdirs, filenames in os.walk(folder):
        for pattern in ['*[Dd][Ss]*[Ss]tore*','*Icon*']:

		# Find the files that matches the given pattern
            for filename in fnmatch.filter(filenames, pattern):
                try:
				#print (os.path.join(rootDir,filename))
                    os.remove(os.path.join(rootDir, filename))
                except OSError:
                    print("Error while deleting file")

def make_folder_if_absent(acc_folder):
	if os.path.exists(acc_folder) == True:
	  pass
	else:
	  os.mkdir(acc_folder)

def make_case_csv(folder,initials,data_dir,casetable_folder):
    header = ['subID','path','arterial','box','non-contrast','venous']
    filename = os.path.join(casetable_folder,str(folder+'_'+initials+'.csv'))
    print (filename)
    if os.path.exists(filename) == True:
        pass
    else:
        case_list = os.listdir(os.path.join(data_dir,folder))
        cases_for_csv = [[case,os.path.join(data_dir,folder,case),'arterial.nii.gz','','non-con.nii.gz','venous.nii.gz'] for case in case_list]
        cases_for_csv.sort(key=lambda x:(len(x[0]),x[0]))
        cases_for_csv.insert(0,header)

        with open(filename, 'w') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',')
            csvwriter.writerows(cases_for_csv)

def make_tables(config):
    with open(config, 'r') as f:
        config = json.load(f)

    data_dir = config['data_dir']
    initials = config['initials']
    casetables = config['case_tables']

    remove_irr_files(data_dir)

    for i in [i for i in os.listdir(data_dir) if not i.startswith('Icon')]:
        make_case_csv(i,initials,data_dir,casetables)


if __name__ == '__main__':

    make_tables("./caseiterator_config.json")
