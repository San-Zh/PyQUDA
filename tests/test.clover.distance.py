import os
import sys
import numpy as np
import cupy as cp

test_dir = os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0, os.path.join(test_dir, ".."))
from pyquda import core, mpi
from pyquda.field import Nc, Ns, LatticePropagator
from pyquda.utils import gauge_utils, source

os.environ["QUDA_RESOURCE_PATH"] = ".cache"

latt_size = [4, 4, 4, 8]
Lx, Ly, Lz, Lt = latt_size
Vol = Lx * Ly * Lz * Lt

xi_0, nu = 2.464, 0.95
kappa = 0.115
coeff = 1.17
coeff_r, coeff_t = 0.91, 1.07
alpha = 0.4
source_time = 0

mass = 1 / (2 * kappa) - 4

from pyquda.enum_quda import QudaResidualType

dslash = core.getDslash(latt_size, mass, 1e-9, 1000, xi_0, nu, coeff_t, coeff_r, multigrid=False)
dslash.invert_param.residual_type = QudaResidualType.QUDA_L2_ABSOLUTE_RESIDUAL
dslash.invert_param.alpha = alpha
dslash.invert_param.source_time = source_time
gauge = gauge_utils.readIldg(os.path.join(test_dir, "weak_field.lime"))

mpi.init()

dslash.loadGauge(gauge)

propagator = LatticePropagator(latt_size)
data = propagator.data.reshape(Vol, Ns, Ns, Nc, Nc)
for spin in range(Ns):
    for color in range(Nc):
        b = source.source(latt_size, "point", [0, 0, 0, source_time], spin, color)
        b.data /= cp.cosh(alpha * cp.arange(source_time - Lt / 2, source_time + Lt / 2)).reshape(-1, 1, 1, 1, 1, 1)
        x = dslash.invert(b)
        x.data *= cp.cosh(alpha * cp.arange(source_time - Lt / 2, source_time + Lt / 2)).reshape(-1, 1, 1, 1, 1, 1)
        data[:, :, spin, :, color] = x.data.reshape(Vol, Ns, Nc)

dslash.destroy()

propagator_chroma = cp.array(np.fromfile("pt_prop_1", ">c16", offset=8).astype("<c16")).reshape(Vol, Ns, Ns, Nc, Nc)
print(cp.linalg.norm(propagator.data.reshape(Vol, Ns, Ns, Nc, Nc) - propagator_chroma.transpose(0, 2, 1, 4, 3)))
