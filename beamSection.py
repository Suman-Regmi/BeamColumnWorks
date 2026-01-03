
import openseespy.opensees as ops
import opsvis
from units import *
import numpy as np
import matplotlib.pyplot as plt
from geometryDefinitions import  *
from materialDefinitions import  *  #for confined and unconfined concrete material definitions 
# ################################### For beam:  ##########################
#defining these parameters so that elements outside of the plastic hinge length can be modeled as elastic beam column elements
#These are to be changed while defining sections, hence key parameters for the research work
# Section definitions

# let's encapsulate the section definitions into a function
# sectionDimensions is a dictionary or an object with the beamDepth, beamWidth, cover, information about arrangement of bars
# unconfinedConcrete stores info on the properties of unconfined concrete
# confinedConcrete stores info on the properties of confined concrete
# steel stores the info on the properties of the steel 

# def beamSection(sectionDimensions, steel, unconfinedConcrete, confinedConcrete):
Bbeam = 229*mm  #key
Hbeam = 457*mm  #key

#may be i would benefit from using the elastic section for the elastic beam column elements
#  as i have already defined the fiber section layout here
Ibeam = 0.35 * Bbeam*Hbeam**3/12
Abeam = Bbeam*Hbeam
c = 42*mm  # cover  #consistent

y1col = Hbeam/2.0
z1col = Bbeam/2.0
separation_between_bars = 33*mm
y2col = y1col - c - separation_between_bars

nFibZCoverTopBottom = 3
nFibZCoverLeftRight = 2
nFibZCore = 7
nFib = 7
nFibCover, nFibCore = 2, 20
As9 = np.pi*16**2/4  #6 #9 bars for compression and tension face  #key
Fy = 294 * N/mm**2  #done   #key



# uniaxialMaterial('Concrete02', matTag, fpc, epsc0, fpcu, epsU, lambda, ft, Ets)
# ops.uniaxialMaterial("Concrete02", 2, -39*MPa, -0.002,-0.2*39*MPa,-0.004,0.3,2*MPa,3.6e3)  #unconfined concrete
# ops.uniaxialMaterial("Concrete02", 2, -39*MPa, -0.002,0*MPa,-0.004,0.3,2*MPa,3.6e3)  #unconfined concrete

# # ops.uniaxialMaterial("Concrete02", 3, -48*MPa, -0.003,-0.2*48*MPa,-0.01,0.3,2*MPa,3.6e3)   #confined concrete
# ops.uniaxialMaterial("Concrete02", 3, -48*MPa, -0.003,0*MPa,-0.01,0.3,2*MPa,3.6e3)   #confined concrete

# uniaxialMaterial('Steel02', matTag, Fy, E0, b, *params, a1=a2*Fy/E0, a2=1.0, a3=a4*Fy/E0, a4=1.0, sigInit=0.0)
# R0=between 10 and 20, cR1=0.925, cR2=0.15
# D16 Rebar - Beam
# uniaxialMaterial     Steel02     2002     295000000.00000     210000000000.00000     0.00400     20.00000     0.92500     0.15000
fyBeamRebar = 295*MPa
# EBeamRebar =  0.35*210e3*MPa
EBeamRebar =  210e3*MPa
# ops.uniaxialMaterial('Steel02', 4, fyBeamRebar,EBeamRebar , 0.004, 20,0.925,0.15) #material for rebar
# ops.uniaxialMaterial("Steel02",3,2500)  #material for unconfined concrete
# ops.uniaxialMaterial("Elastic",3,2500)  #material for confined concrete
# ops.uniaxialMaterial("Elastic",4,2500)   #material for rebar


beamSectionAtPlasticHinges = [['section', 'Fiber', secTagBeamAtPlasticHinges, '-GJ', 1.0e6],
            ['patch', 'rect', 3, nFibCore, nFibZCore, c-y1col, c-z1col, y1col-c, z1col-c],
            ['patch', 'rect', 2, nFib, nFibZCoverLeftRight, -y1col, -z1col, y1col, c-z1col],
            ['patch', 'rect', 2, nFib, nFibZCoverLeftRight, -y1col, z1col-c, y1col, z1col],
            ['patch', 'rect', 2, nFibCover, nFibZCoverTopBottom, -y1col, c-z1col, c-y1col, z1col-c],
            ['patch', 'rect', 2, nFibCover, nFibZCoverTopBottom, y1col-c, c-z1col, y1col, z1col-c],
            ['layer', 'straight', 4, 3, As9, y1col-c, z1col-c, y1col-c, c-z1col],
            #  ['layer', 'straight', 4, 2, As9, y2col, z1col-c, y2col, c-z1col],
            ['layer', 'straight', 4, 2, As9, c-y1col, z1col-c, c-y1col, c-z1col]]


opsvis.fib_sec_list_to_cmds(beamSectionAtPlasticHinges)

nFibZCoverTopBottom = 3
nFibZCoverLeftRight = 2
nFibZCore = 5
nFib = 5
nFibCover, nFibCore = 2, 4

beamSection = [['section', 'Fiber', secTagBeam, '-GJ', 1.0e6],
            ['patch', 'rect', 2, nFibCore, nFibZCore, c-y1col, c-z1col, y1col-c, z1col-c],
            ['patch', 'rect', 2, nFib, nFibZCoverLeftRight, -y1col, -z1col, y1col, c-z1col],
            ['patch', 'rect', 2, nFib, nFibZCoverLeftRight, -y1col, z1col-c, y1col, z1col],
            ['patch', 'rect', 2, nFibCover, nFibZCoverTopBottom, -y1col, c-z1col, c-y1col, z1col-c],
            ['patch', 'rect', 2, nFibCover, nFibZCoverTopBottom, y1col-c, c-z1col, y1col, z1col-c],
            ['layer', 'straight', 4, 3, As9, y1col-c, z1col-c, y1col-c, c-z1col],
            #  ['layer', 'straight', 4, 2, As9, y2col, z1col-c, y2col, c-z1col],
            ['layer', 'straight', 4, 2, As9, c-y1col, z1col-c, c-y1col, c-z1col]
            ]
# our beam wil have only two layers of rebar on tension and compression side collectively

opsvis.fib_sec_list_to_cmds(beamSection)

matcolor = ['r', 'lightgrey', 'gold', 'w', 'w', 'w']
opsvis.plot_fiber_section(beamSectionAtPlasticHinges, matcolor=matcolor)
plt.axis('equal')


matcolor = ['r', 'lightgrey', 'gold', 'w', 'w', 'w']
opsvis.plot_fiber_section(beamSection, matcolor=matcolor)
plt.axis('equal')
plt.show()