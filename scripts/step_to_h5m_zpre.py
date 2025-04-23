###############################################################################
# Converting step files to h5m file to be read by openmc
###############################################################################
import numpy as np
import os
import CAD_to_OpenMC.assembly as ab
###############################################################################

# inputs
step_filepath = "./step_files/zpre.step"
#step_filepath = "test_blocks.step"
#step_filepath = "loop6.1_b26.6.step"
h5m_out_filepath = os.getcwd() + '/h5m_files/zpre.h5m'

# mesher config
ab.mesher_config['mesh_algorithm'] = 2
ab.mesher_config['threads'] = 1
ab.mesher_config['curve_samples'] = 50
ab.mesher_config['angular_tolerance'] = 0.20
ab.mesher_config['tolerance'] = 0.3

# output
a=ab.Assembly()
a.verbose=2
a.stp_files=[step_filepath]
a.import_stp_files()
a.merge_all()
a.solids_to_h5m(backend='gmsh',h5m_filename=h5m_out_filepath)
