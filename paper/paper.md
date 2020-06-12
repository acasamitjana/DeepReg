title: 'DeepReg: A deep-learning toolkit for medical image registration'
tags:
  - Python
  - TensorFlow
  - medical image registration
  - logitudinal image registration
  - image fusion
  - deep learning
  - neural networks
authors:
  - name: Yunguan Fu
    orcid: 0000-0002-1184-7421
    affiliation: "1, 2, 3" # (Multiple affiliations must be quoted)
  - name: Nina Montana Brown
    orcid: 0000-0000-0000-0000
    affiliation: "1, 2"
  - name: Qianye Yang
    orcid: 0000-0000-0000-0000
    affiliation: "1, 2"

    ... many other ;)

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

<<<<<<< HEAD
Medical image registration has an important role in the fields of medical image analysis and computer assisted intervetnion
=======
Medical image registration has a important role in the fields of medical image analysis and computer assisted intervetnion
>>>>>>> 975783ffcded003e6ac8dba862cef903bba0747e

`DeepReg` is a Python package to implement a number of deep learning algorithms for medical image registration.

`DeepReg` was designed to be used by researchers, engineers and scientists. 

<<<<<<< HEAD
# Methodology
=======
# Algorithms
>>>>>>> 975783ffcded003e6ac8dba862cef903bba0747e
## Unsupervised learning
## Weakly-supervised learning
## Unsupervised learning with weak supervision
## Conditional segmentation

<<<<<<< HEAD
# Data IO
## Network (inference) input
Compusory: moving image and fixed image
Optional: moving label(s) and/or fixed label(s)

## Loss input
Warped moving image and fixed image
Warped moving label(s) and fixed image label(s)

## Data loader - a superset of val / test data
Training data loader requires a union of 'network input' and 'loss input'
Val / test data loader requires a union of 'network input' and 'loss input'

## Training sampling methods
### Sampling for multiple labels
In any case when corresponding labels are available and there are multiple types of labels, e.g. the segmentation of different organs in a CT image, two options are available:

During one epoch, each image would be sampled only once and when there are multiple labels, we will randomly sample one label at a time. (Default)
During one epoch, each image would be paired with each available label. So if an image has four types of labels, it will be sampled for four times and each time corresponds to a different label.
When using multiple labels, it is the user's responsibility to ensure the labels are ordered, such that label_idx are the corresponding types in (width, height, depth, label_idx)

### Sampling for multiple subjects each with multiple images
When multiple subjects each with multiple images are available, multiple different sampling methods are supported:

Inter-subject, one image is sampled from subject A as moving image, and another one image is sampled from a different subject B as fixed image.
Intra-subject, two images are sampled from the same subject. In this case, we can specify:
a) moving image always has a smaller index, e.g. at an earlier time;
b) moving image always has a larger index, e.g. at a later time; or
c) no constraint on the order.
For the first two options, the intra-subject images will be ascending-sorted by name to represent ordered sequential images, such as time-series data
*Multiple label sampling is also supported once image pair is sampled; In case there are no consistent label types defined between subjects, an option is available to turned off label contribution to the loss for those inter-subject image pairs.

(see the Supported Data Loaders)

## Network (inference) output
Opt 1: dense displacement field (DDF), with dense velocity field (DFV) if enabled
Opt 2 (conditional segmentation): warped moving labels 


# Supported application scenarios
Unpaired images (e.g. single-modality inter-subject registration)
Case 1-1 multiple independent images.
Case 1-2 multiple independent images and corresponding labels.
Grouped unpaired images (e.g. single-modality intra-subject registration)
Case 2-1 multiple subjects each with multiple images.
Case 2-2 multiple subjects each with multiple images and corresponding labels.
Paired images (e.g. two-modality intra-subject registration)
Case 3-1 multiple paired images.
Case 3-2 multiple paired images and corresponding labels.


# Example applications (Demos)
=======
# Example applications
>>>>>>> 975783ffcded003e6ac8dba862cef903bba0747e
## Inter-subject registration
### Neural MR (unsupervised +/- supervision)
### 3D ultrasound fetal?

<<<<<<< HEAD
## Intra-subject registration
### Lung 4DCT (unsupervised +/- supervision with inter-subject sampling)
### Prostate logitudinal MR (unsupervised +/- supervision with inter-subject sampling)

=======
>>>>>>> 975783ffcded003e6ac8dba862cef903bba0747e
## Multimodal registration
### Prostate (weakly with multiple labels, conditional reg.)
### Neurosurgery (unsupervised with supervision)

<<<<<<< HEAD

=======
## Intra-subject registration with logitudinal data
### Lung 4DCT (unsupervised +/- supervision with inter-subject sampling)
### Prostate MR (unsupervised +/- supervision with inter-subject sampling)
>>>>>>> 975783ffcded003e6ac8dba862cef903bba0747e

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