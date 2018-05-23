from PIL import Image
from numpy import *

def pca(X):
    """ Principal Component Analysis
     input: X, matrix with training data stored as flattened arrays in rows
     return: projection matrix (with important dimensions first), variance and means
    """
    """
      PCA is a useful technique for dimensionality reduction
      Images have alot of dimensional space so need dimension reduction
      The projection matrix resulting from PCA can be seen as a change
       of coordinates to a coordinate system where the coordinates are in
       descending order of importance
      Use NumPy's flatten() method
    """
    """
      Flatten images are collected in a single matrix by stacking them (row = image)
      The rows are centered relative to the mean before the
        computation of the dominant directions
      To find principal components, singular value decomposition (SVD) is used
      If high dim() there is a trick b/c SVD is slow
    """

    # get dimensions
    num_data,dim = X.shape

    # center data
    mean_X = X.mean(axis=0)
    X = X - mean_X

    if dim>num_data:
        # PCA - compact trick used
        M = dot(X,X.T) # covariance matrix
        e,EV = linalg.eigh(M) # eigenvalues and eigenvectors
        tmp = dot(X.T,EV).T # this is the compact trick
        V = tmp[::-1] # reverse since last eigenvecotrs are the ones we want
        S = sqrt(e)[::-1] # reverse since eigenvalues are in increasing order
        for i in range(V.shape[1]):
            V[:,i] /= S
    else:
        # PCA - SVD used =
        U,S,V = linalg.svd(X)
        V = V[:num_data] # only makes sense to return the first num_data

    # return the projection matrix, the variance and the means
    return V,S, mean_X
    
