import sys
import fnmatch
import json
import os
import slicer

from update_case_tables import make_tables

def start_up(config_file):

    current = os.getcwd()

    print (current)

    customization_folder = '/Users/brettmarinelli/Dropbox/IR_Work/BodyBleeds/Code/CaseIteratorCustomization'
    sys.path.append(customization_folder)
    sys.path.append(current)
    #config = os.path.join(customization_folder,'caseiterator_config_BM.json')
    config = os.path.abspath(config_file)

    with open(config, 'r') as f:
        config_f = json.load(f)

        data_dir = config_f['data_dir']
        initials = config_f['initials']
        casetables = config_f['case_tables']

    make_tables(config)

    # Go to SlicerCaseIterator on StartUp
    slicer.util.selectModule("SlicerCaseIterator")

    # For Bleed Case Iterator Load All Data Folders

    folder = casetables
    print (folder)
    for rootDir, subdirs, filenames in os.walk(folder):
        for pattern in ['*'+initials+'*']:

    #        Find the files that matches the given pattern
                for filename in fnmatch.filter(filenames, pattern):
                        path = os.path.join(folder,filename)
                        logic = slicer.modules.tables.logic()
                        newTable = logic.AddTable(path)
                        csv_sciw = slicer.modules.slicercaseiterator.widgetRepresentation().self().inputWidget
                        csv_sciw.batchTableSelector.setCurrentNode(newTable)
                        csv_sciw.batchTableView.setMRMLTableNode(newTable)


    sciw = slicer.modules.slicercaseiterator.widgetRepresentation().self()
    sciw.txtReaderName.text = initials

    sciw.onReset()

if __name__ == '__main__':

    start_up("./caseiterator_config_BM.json")