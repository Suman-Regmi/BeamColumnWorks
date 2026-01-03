# beam and column materials Materials
from units import *
import openseespy.opensees as ops

# The defintions for concrete especially have to be generated using Mander model for various spacing later on!!

# definitions for concrete materials
unconfinedConcreteTag = 2
f_unconfined = -39*MPa  #key
eps_peak_unconfined = -0.002  #key
eps_max_unconfined = -0.004  #key
ops.uniaxialMaterial("Concrete02", unconfinedConcreteTag, f_unconfined, eps_peak_unconfined, 0*MPa, eps_max_unconfined, 0.3, 2*MPa, 3.6e3)  #unconfined concrete

confinedConcreteTag = 3
f_confined = -48*MPa  #key
eps_peak_confined = -0.003  #key
eps_max_confined = -0.01  #key
ops.uniaxialMaterial("Concrete02", confinedConcreteTag, f_confined, eps_peak_confined, 0*MPa, eps_max_confined, 0.3, 2*MPa, 3.6e3)   #confined concrete
# ops.uniaxialMaterial("Concrete02", 3, -48*MPa, -0.003,-0.2*48*MPa,-0.01,0.3,2*MPa,3.6e3)   #confined concrete


# definitions for steel rebar materials
steelRebarTag = 4
fyBeamRebar = 295*MPa
EBeamRebar =  210e3*MPa
ops.uniaxialMaterial('Steel02', steelRebarTag, fyBeamRebar,EBeamRebar , 0.004, 20,0.925,0.15) #material for rebar