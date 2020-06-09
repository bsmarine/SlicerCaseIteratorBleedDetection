import os
class RapidReview():
    def __init__(self):
        self.counter = -1
        #self.dire = "/Users/brettmarinelli/Desktop/LargePatches"
        self.dire = '/Users/brettmarinelli/Dropbox/IR_Work/Bleed_Studies/InitialBatch_092619'
    def load_study(self,k):
        studies = [i for i in os.listdir(self.dire) if 'DS_Store' not in i]
        slicer.mrmlScene.Clear(0)
        a,venNode = slicer.util.loadVolume(os.path.join(self.dire,studies[k],'venous.nii.gz'),returnNode=True)
        b,artNode = slicer.util.loadVolume(os.path.join(self.dire,studies[k],'arterial.nii.gz'),returnNode=True)
        c,nonconNode = slicer.util.loadVolume(os.path.join(self.dire,studies[k],'non-con.nii.gz'),returnNode=True)
        #d,maskNode = slicer.util.loadLabelVolume(os.path.join(self.dire,studies[k],'mask.nii.gz'), returnNode=True)
        d,fidNode = slicer.util.loadMarkupsFiducialList(os.path.join(self.dire,studies[k],'BoxFiducials_JT.fcsv'),returnNode=True)
        ##Make Display Nodes
        artDisplay = artNode.GetDisplayNode()
        venDisplay = venNode.GetDisplayNode()
        ncDisplay = nonconNode.GetDisplayNode()
        ##Change Window Levels
        for displayNode in [artDisplay,venDisplay,ncDisplay]:
            displayNode.AutoWindowLevelOff()
            displayNode.SetWindow(350)
            displayNode.SetLevel(40)
        #Grab Slice Window Logics
        red_logic = slicer.app.layoutManager().sliceWidget('Red').sliceLogic().GetSliceCompositeNode()
        green_logic = slicer.app.layoutManager().sliceWidget('Green').sliceLogic().GetSliceCompositeNode()
        yellow_logic = slicer.app.layoutManager().sliceWidget('Yellow').sliceLogic().GetSliceCompositeNode()
        slice4_logic = slicer.app.layoutManager().sliceWidget('Slice4').sliceLogic().GetSliceCompositeNode()
        # Set Background Nodes
        red_logic.SetBackgroundVolumeID(artNode.GetID())
        green_logic.SetBackgroundVolumeID(venNode.GetID())
        yellow_logic.SetBackgroundVolumeID(nonconNode.GetID())
        # Set Label Opacity
        red_logic.SetLabelOpacity(0.3)
        green_logic.SetLabelOpacity(0.3)
        yellow_logic.SetLabelOpacity(0.3)
        slice4_logic.SetLabelOpacity(0.3)
        # Change Foreground Opacity
        red_logic.SetLabelOpacity(0.3)       
        ##Set Orientations to Coronal
        sliceNodes = slicer.util.getNodesByClass('vtkMRMLSliceNode')
        for i in sliceNodes:
            i.SetOrientation("Coronal")
        print (os.path.join(self.dire,studies[k]))
    
    ### TODO: Unable to get this method to work, where each time it's called
    ### the next index study is loaded and viewed....
    def next_study(self):
        self.counter += 1
        print (self.counter)
        return self.load_study(self.counter)