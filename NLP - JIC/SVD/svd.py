# -*- coding: utf-8 -*-

import numpy as np

#-------------------------------------------------------------------------------------
# Função calculate_svd() - Calcula o SVD com a matriz term X doc e retorna a posição espacial de cada musica
# - matrix: term X doc                                                                
# - k: tamanho do corte do SVD                                                        
#-------------------------------------------------------------------------------------
def calculate_svd(matrix, k):
        S, sigma, UT = np.linalg.svd(matrix, full_matrices=False)
        S = S[:,:k]
        sigma = np.diag(sigma)[:k,:k]
        UT = UT[:k,:]
        
        #doc_vectors = np.dot(sigma, UT)
        #term_vectors = np.dot(S, sigma) 
        
        return S, sigma, UT
