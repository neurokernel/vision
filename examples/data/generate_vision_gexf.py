#!/usr/bin/env pythpn

import numpy as np

from neurokernel.LPU.LPU import LPU
import vision_configuration as vc

np.random.seed(10000)

lamina = vc.Lamina(24, 32, 'neuron_types_lamina.csv', 'synapse_lamina.csv', None)
lamina.create_cartridges()
lamina.connect_cartridges()
lamina.create_non_columnar_neurons()
lamina.connect_composition_II()
lamina.connect_composition_I()
lamina.add_selectors()
g_lam = lamina.export_to_gexf('lamina.gexf.gz')
n_dict_lam, s_dict_lam = LPU.graph_to_dicts(g_lam)

medulla = vc.Medulla(24, 32, 'neuron_types_medulla.csv', 'synapse_medulla.csv', 'synapse_medulla_other.csv')
medulla.create_cartridges()
medulla.connect_cartridges()
medulla.create_non_columnar_neurons()
medulla.connect_composition_I()
medulla.connect_composition_II()
medulla.connect_composition_III()
medulla.add_selectors()
g_med = medulla.export_to_gexf('medulla.gexf.gz')
n_dict_med, s_dict_med = LPU.graph_to_dicts(g_med)

vc.create_pattern(n_dict_lam, n_dict_med, 'lam_med.gexf.gz')
