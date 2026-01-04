
import openseespy.opensees as ops
import opsvis
from units import *
import numpy as np
import matplotlib.pyplot as plt
from geometryDefinitions import  *
from materialDefinitions import  *  #for confined and unconfined concrete material definitions 
# ############################################## For column: #######################################

#defining these parameters so that elements outside of the plastic hinge length can be modeled as elastic beam column elements
Bcol = 305*mm
Hcol = 406*mm



# L_RL_beam = Hcol/4
# L_RL_col = Hbeam/4

c = 43*mm  # cover

y1col = Hcol/2.0
z1col = Bcol/2.0

fyColumnRebar = 500*MPa
# fyColumnRebar = 295*MPa
# EColumnRebar = 0.7*210e3*MPa
EColumnRebar = 200e3*MPa

# nFibZ = 1  #do separate discretization for the core and the cover later
# nFib = 20
nFibCover,nFibCover2, nFibCore = 4,2, 16
nFibZCoverTopBottom = 3
nFibZCoverLeftRight = 2
nFibZCore = 7
nFib = 7
nFibCover, nFibCore = 2, 20
columnSteelRebarTag = 5
# As9 = 1*mm*mm  #four #9 bars cover is 2.5 mmes
As9 = np.pi*16**2/4
# commenting the following lines as they are already defined in materialDefinitions.py
# uniaxialMaterial('Concrete02', matTag, fpc, epsc0, fpcu, epsU, lambda, ft, Ets)
# ops.uniaxialMaterial("Concrete02", 5, -39*MPa, -0.002,-0.2*39*MPa,-0.004,0.3,2*MPa,3.6e3)  #unconfined concrete
# ops.uniaxialMaterial("Concrete02", 6, -48*MPa, -0.003,-0.2*48*MPa,-0.01,0.3,2*MPa,3.6e3)  #confined concrete
# # ops.uniaxialMaterial("Elastic",6,2500)  #material for unconfined concrete
# # ops.uniaxialMaterial("Elastic",7,2500)   #material for rebar
# # ops.uniaxialMaterial('Steel02', 7, fyColumnRebar, EColumnRebar, 0.004, 20,0.925,0.15)
ops.uniaxialMaterial('Steel02', columnSteelRebarTag, fyColumnRebar, EColumnRebar, 0.004, 20,0.925,0.15) #material for rebar

#5,6,7->materialtags
# 5->unconfined concrete
# 6->confined concrete
# 7->steel rebar


columnSectionAtPlasticHinges = [['section', 'Fiber', secTagColumnAtPlasticHinges, '-GJ', 1.0e6],
             ['patch', 'rect', confinedConcreteTag, nFibCore, nFibCore, c-y1col, c-z1col, y1col-c, z1col-c],
             ['patch', 'rect', unconfinedConcreteTag, nFibCover, nFibZCoverLeftRight, -y1col, -z1col, y1col, c-z1col],
             ['patch', 'rect', unconfinedConcreteTag, nFibCover, nFibZCoverLeftRight, -y1col, z1col-c, y1col, z1col],
             ['patch', 'rect', unconfinedConcreteTag, nFibCover2, nFibZCoverTopBottom, -y1col, c-z1col, c-y1col, z1col-c],
             ['patch', 'rect', unconfinedConcreteTag, nFibCover2, nFibZCoverTopBottom, y1col-c, c-z1col, y1col, z1col-c],
             ['layer', 'straight', columnSteelRebarTag, 3, As9, y1col-c, z1col-c, y1col-c, c-z1col],
             ['layer', 'straight', columnSteelRebarTag, 2, As9, 0, z1col-c, 0, c-z1col],
             ['layer', 'straight', columnSteelRebarTag, 3, As9, c-y1col, z1col-c, c-y1col, c-z1col]]


opsvis.fib_sec_list_to_cmds(columnSectionAtPlasticHinges)

#column section at places other than plastic hinges
nFibCover,nFibCover2, nFibCore = 4,2, 8 #at sections other than plastic hinges
columnSection = [['section', 'Fiber', secTagColumn, '-GJ', 1.0e6],
             ['patch', 'rect', confinedConcreteTag, nFibCore, nFibCore, c-y1col, c-z1col, y1col-c, z1col-c],
             ['patch', 'rect', unconfinedConcreteTag, nFibCover, nFibZCoverLeftRight, -y1col, -z1col, y1col, c-z1col],
             ['patch', 'rect', unconfinedConcreteTag, nFibCover, nFibZCoverLeftRight, -y1col, z1col-c, y1col, z1col],
             ['patch', 'rect', unconfinedConcreteTag, nFibCover2, nFibZCoverTopBottom, -y1col, c-z1col, c-y1col, z1col-c],
             ['patch', 'rect', unconfinedConcreteTag, nFibCover2, nFibZCoverTopBottom, y1col-c, c-z1col, y1col, z1col-c],
             ['layer', 'straight', columnSteelRebarTag, 3, As9, y1col-c, z1col-c, y1col-c, c-z1col],
             ['layer', 'straight', columnSteelRebarTag, 2, As9, 0, z1col-c, 0, c-z1col],
             ['layer', 'straight', columnSteelRebarTag, 3, As9, c-y1col, z1col-c, c-y1col, c-z1col]]


opsvis.fib_sec_list_to_cmds(columnSection)


matcolor = ['r', 'lightgrey', 'gold', 'w', 'w', 'w']
opsvis.plot_fiber_section(columnSectionAtPlasticHinges, matcolor=matcolor)
plt.axis('equal')
plt.show()
matcolor = ['r', 'lightgrey', 'gold', 'w', 'w', 'w']
opsvis.plot_fiber_section(columnSection, matcolor=matcolor)
plt.axis('equal')
plt.show()

# matcolor = ['r', 'lightgrey', 'gold', 'w', 'lightgrey', 'gold','w']
# opsvis.plot_fiber_section(columnSection, matcolor=matcolor)
# plt.axis('equal')

# # element('elasticBeamColumn', eleTag, *eleNodes, secTag, transfTag, <'-mass', mass>, <'-cMass'>, <'-release', releaseCode>)
# # ops.element("elasticBeamColumn",1,1,2,secTagColumn,transfTag)
# # ops.element("elasticBeamColumn",2,2,3,secTagColumn,transfTag)
# # ops.element("elasticBeamColumn",3,2,4,secTagBeam,transfTag)