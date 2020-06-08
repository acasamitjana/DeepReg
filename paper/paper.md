title: 'DeepReg: A deep-learning toolkit for medical image registration'
tags:
  - Python
  - TensorFlow
  - medical image registration
  - image fusion
  - deep learning
  - neural networks
authors:
  - name: Yunguan Fu
    orcid: 0000-0002-1184-7421
    affiliation: "1, 2, 3" # (Multiple affiliations must be quoted)
  - name: Qianye Yang
    orcid: 0000-0000-0000-0000
    affiliation: "1, 2"
  - name: Yipeng Hu
    orcid: 0000-0003-4902-0486
    affiliation: "1, 2"
affiliations:
 - name: Wellcome/EPSRC Centre for Surgical and Interventional Sciences, University College London
   index: 1
 - name: Centre for Medical Image Computing, University College London
   index: 2
 - name: InstaDeep
   index: 3
date: 13 August 2017
bibliography: paper.bib


---

# Summary

Medical image registration has a important role in the fields of medical image analysis and computer assisted intervetnion

`DeepReg` is a Python package to implement a number of deep learning algorithms for medical image registration.

`DeepReg` was designed to be used by researchers, engineers and scientists. 

# Mathematics

Single dollars ($) are required for inline mathematics e.g. $f(x) = e^{\pi/x}$

Double dollars make self-standing equations:

$$\Theta(x) = \left\{\begin{array}{l}
0\textrm{ if } x < 0\cr
1\textrm{ else}
\end{array}\right.$$

You can also use plain \LaTeX for equations
\begin{equation}\label{eq:fourier}
\hat f(\omega) = \int_{-\infty}^{\infty} f(x) e^{i\omega x} dx
\end{equation}
and refer to \autoref{eq:fourier} from text.

# Citations

Citations to entries in paper.bib should be in
[rMarkdown](http://rmarkdown.rstudio.com/authoring_bibliographies_and_citations.html)
format.

If you want to cite a software repository URL (e.g. something on GitHub without a preferred
citation) then you can do it with the example BibTeX entry below for @fidgit.

For a quick reference, the following citation commands can be used:
- `@author:2001`  ->  "Author et al. (2001)"
- `[@author:2001]` -> "(Author et al., 2001)"
- `[@author1:2001; @author2:2001]` -> "(Author1 et al., 2001; Author2 et al., 2002)"

# Figures

Figures can be included like this:
![Caption for example figure.\label{fig:example}](figure.png)
and referenced from text using \autoref{fig:example}.

Fenced code blocks are rendered with syntax highlighting:
```python
for n in range(10):
    yield f(n)
```	

# Acknowledgements

This work is supported by the Wellcome/EPSRC Centre for Interventional and Surgical Sciences (203145Z/16/Z).

# References