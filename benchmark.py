import anndata as ad
import timeit
import numpy as np
import pandas as pd
import time
from resource import getrusage, RUSAGE_SELF
from scipy.sparse import csr_matrix 
import loompy as lp
import h5py
import scanpy as sc

@profile
def create_anndata_object():
    counts = csr_matrix(np.random.poisson(1, size=(2000, 2000)), dtype=np.float32)
    adata = ad.AnnData(counts)

@profile
def write_anndata_object():
    pass

@profile
def create_loom_object():
    filename = "test.loom"
    counts = csr_matrix(np.random.poisson(1, size=(2000,2000)), dtype=np.float32)
    row_attrs = {"RowAttr": np.arange(2000)}
    col_attrs = {"ColAttrs": np.arange(2000)}
    ldata = lp.create(filename, counts, row_attrs, col_attrs)

if __name__ == "__main__":

    # main()
    
    #print(getrusage(RUSAGE_SELF))
    
    print(timeit.Timer(create_anndata_object).timeit(number=3))
    print(timeit.Timer(create_loom_object).timeit(number=3))
    