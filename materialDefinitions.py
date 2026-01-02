# beam and column materials Materials
from units import *
import openseespy.opensees as ops
f_confined = -48*MPa  #key
f_unconfined = -39*MPa  #key

eps_peak_confined = -0.003  #key
eps_peak_unconfined = -0.002  #key

eps_max_confined = -0.01  #key
eps_max_unconfined = -0.004  #key
ops.uniaxialMaterial("Concrete02", 2, f_unconfined, eps_peak_unconfined, 0*MPa, eps_max_unconfined, 0.3, 2*MPa, 3.6e3)  #unconfined concrete

# ops.uniaxialMaterial("Concrete02", 3, -48*MPa, -0.003,-0.2*48*MPa,-0.01,0.3,2*MPa,3.6e3)   #confined concrete
ops.uniaxialMaterial("Concrete02", 3, -48*MPa, -0.003,0*MPa,-0.01,0.3,2*MPa,3.6e3)   #confined concrete