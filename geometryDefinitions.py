from units import *
import numpy as np
import openseespy.opensees as ops
DBeam = 457*mm  #key
DCol = 406*mm   #key
beamPlasticHingeLength = DBeam/2  #originally divide by 2
# beamPlasticHingeLength = DBeam #originally divide by 2
columnPlasticHingeLength = DCol/2 #originally divide by 2



ops.node(1,0,0)     #center node of the subassembles


# These nodes also have been commented out for external joint 
# ops.node(2,-DCol/4,0)  #left end of the rigid link
# ops.node(200, -DCol/4 - beamPlasticHingeLength,0) #end of plastic hinge


# ops.node(3,-848*mm,0)  #left end of the beam where gravity load is applied
# ops.node(4,-2119*mm,0)  #extreme left end

#right beam
#500-5 plastic hinge->heavy section discretization
ops.node(5,DCol/4,0*mm)  #right rigid link
ops.node(500, +DCol/4 + beamPlasticHingeLength,0) #end of plastic hinge
ops.node(6,848*mm,0*mm)  #right beam where gravity load is applied
ops.node(7,2119*mm,0*mm)  #right extreme beam



#top column 8-800 rigid link
ops.node(8,0,DBeam/4*mm) #column top rigid link
ops.node(800,0,DBeam/4*mm + columnPlasticHingeLength) #column top rigid link
ops.node(9,0,1236*mm) #column top extreme->lateral displacement node

#bottom column
ops.node(10,0,-DBeam/4) #column bottom rigid link
ops.node(1000,0,-DBeam/4-columnPlasticHingeLength) #end of plastic hinge
ops.node(11,0,-1236*mm) #column bottom extreme



differenceColumn = -DBeam/4-DCol/2 + 1236  #length of the column excluding plastic hinge length and rigid link lengths
numEleCol = 2
lengthEleCol = differenceColumn/numEleCol

[ops.node(51+i, 0, -DBeam/4 - columnPlasticHingeLength - i*lengthEleCol) for i in range(1,numEleCol)]   #for the bottom column

[ops.node(501+i, 0, +DBeam/4 + columnPlasticHingeLength + i*lengthEleCol) for i in range(1,numEleCol)] #for the top column



# ########################## Here we define the nodes for the beams ##############################
# lengthof the beam on eigher side is 2119 mm from the joint center
differenceBeam1 = -DCol/4 - DBeam/2 + 848 #this is the length of the beam upto the gravity loading point excluding pH length on either side
differenceBeam2 = -848 + 2119 #This is the length of the beam from the gravity load point to the extreme end

numEleBeam1 = 2
numEleBeam2 = 2
lengthEleBeam1 = differenceBeam1/numEleBeam1
lengthEleBeam2 = differenceBeam2/numEleBeam2  #These were used previously to discretize the beam when all the elements were modeled with distributed plasticity
# lengthEleBeam1 is for the elements right next to the plastic hinge zone
# lengthEleBeam3 is for the elements right next to the  nodes with gravity loads


#for the beam to the right of the joint
[ops.node(6001+i, +DCol/4 + beamPlasticHingeLength + i*lengthEleBeam1, 0) for i in range(1,numEleBeam1)]  
[ops.node(6051+i, +848 + i*lengthEleBeam2, 0) for i in range(1,numEleBeam2)]



# section Tags and geometrical transformations
#here we give section definitions using fiber sections, could have used RCSection2d as well!!
#two different sections have been defined for each columns and beams
#one heavily discretized section for plastic hinge regions and one lightly discretized section for the rest of the member length
# 1->plastic hinge section for beam
# 2->sections other than plastic hinge section for beam
# 3->plastic hinge section for column
# 1->sections other than plastic hinge section for column
transfTag = 1
ops.geomTransf("PDelta",transfTag)


secTagBeamAtPlasticHinges = 1
secTagBeam = 2
secTagColumnAtPlasticHinges = 3
secTagColumn = 4