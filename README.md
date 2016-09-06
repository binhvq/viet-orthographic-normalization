# viet-orthographic-normalization
Vietnamese orthographic normalization for preprocessing.

## Vietnamese Orthographic Variation Dictionary
A file `variant_dic/variants_without_wrong.tsv` is a Vietnamese orthographic variation dictionary.
I pick it up from [VNTQcorpus(big).txt](https://dl.dropboxusercontent.com/u/2152477/SNOW-Vietnamese/VNTQcorpus-big.txt) using `pick_variant_from_corpus.py` python script.

This file formats are
- Row of odd number:syllable
- Row of even number:left syllable's frequency in the corpus

# Acknowledgement
A part of scripts are borrowed from Luu Tuan Anh.
