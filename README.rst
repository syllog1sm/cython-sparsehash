====================================================
Cython headers for Google Sparsehash, and MurmurHash
====================================================

This library provides Cython .pxd files for Google's Sparsehash library. 
Currently only dense_hash_map is implemented.
As yet it's only intended for use directly from Cython. I doubt it'll be of any use
to pure Python programs --- the built-in dict is better.

.pxd files are also provided for MurmurHash2 and MurmurHash3
