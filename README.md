# SlicerCaseIteratorBleedDetection

Adaptation of SlicerCaseIterator, a scripted module extension for 3D slicer to streamline the annotation of CT angiography with fiducials datasets by handling
loading and saving.

## Usage

## Edit caseiterator_config.json file in CaseIteratorCustomization folder

``` json
{"initials":"BM",

"data_dir":"/Users/brettmarinelli/Dropbox/IR_Work/Bleed_Studies/",

"case_tables":"/Users/brettmarinelli/Dropbox/IR_Work/BodyBleeds/Code/CaseIteratorCustomization/CaseTables"

}
```

## Add Following to .slicerrc To Call Case Iterator Customization Script

``` Python
import sys
sys.path.append('/Users/brettmarinelli/Bleed_Code/CaseIteratorCustomization/')
from bodybleed_startup_script import start_up
start_up('/Users/brettmarinelli/Bleed_Code/CaseIteratorCustomization/caseiterator_config_BM.json')
```

## This Customization Automates The Following:

The input for SlicerCaseIterator is a csv-file containing the file locations of the images
and/or labelmaps that have to be annotated. The first row should be a header row, with
each subsequent row representing one case.

By providing column names in the module interface, columns containing (absolute or relative)
paths to the images/boxes. The main image is loaded last and set as background image.

If you already processed some part of the batch or need to start at a specific case, you can
do so by specifying the number at the `Start postion` parameter (with 1 representing the first case).

When input data is valid, press `Start Batch` and start annotating!

### Case Navigation

When a batch is loaded, the users can navigate between cases using the `Previous Case` and `Next Case`
buttons that are then visible on the module interface.

In addition to the buttons, navigation also be controlled using 2 keyboard shortcuts:
- `Ctrl + N`: Go to next case
- `Ctrl + P`: Go to previous case (in case the first case is active, nothing happens)

When the last case is selected and the user moves to the next case, the current case is closed
and a message indicating the batch is done is shown (navigation is then disabled).

Exiting the navigation prior to reaching is possible using the `Reset` button,
which exits the navigation (the case is not saved and not closed).

### Console Output

On the python console SlicerCaseIterator prints information about the current case.
Output can contain the following:
- The case number that is loaded. If the table contains a column `patient` or `ID`, the value
  of this cell for the current row is added to this message, e.g. `Loading next patient (3/5): breast1...` 
- An info messages when the case is closed.
- For each new file that is saved, the full path location of the new file is printed.
- Errors and warnings about invalid or missing input.

### Invalid input

When the input is invalid (e.g. unknown column, incorrect path), error messages
detailing the error are shown.

### Output Customization

The following customization is available when processing a batch of cases:
- `Reader name`: Any string specified here gets appended to filenames used to save labelmaps
  (both new labelmaps and labelmaps that were specified in the input file). This can help to
  prevent inadvertently overwriting files and to keep track of who made the labelmaps.
- `Go to Editor`: Check this to automatically switch to the editor module whenever a new case is loaded.
