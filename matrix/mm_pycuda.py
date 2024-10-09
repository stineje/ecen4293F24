import pycuda.autoinit
import pycuda.driver as drv
import numpy as np
from pycuda.compiler import SourceModule

# CUDA kernel for matrix multiplication
mod = SourceModule("""
__global__ void multiply_them(float *dest, float *a, float *b)
{
    const int i = threadIdx.x;
    dest[i] = a[i] * b[i];
}
""")

multiply_them = mod.get_function("multiply_them")

# Initialize input arrays
a = np.random.randn(256).astype(np.float32)
b = np.random.randn(256).astype(np.float32)
dest = np.zeros_like(a)

# Call the CUDA kernel
multiply_them(drv.Out(dest), drv.In(a), drv.In(b), block=(256, 1, 1))

print(dest)
