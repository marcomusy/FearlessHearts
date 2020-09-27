
![](https://user-images.githubusercontent.com/32848391/94369891-ad9d9680-00ec-11eb-8efc-960416a5a0d0.png)

# Fearless Hearts

Create a continuous timecourse for the heart development starting from a limited number of samples acquired at different timepoints.

The algorithm is completely general and can be applied to any dataset.


## Datasets

Download them from server: `/g/sharpeba/scratch/marco/FearlessHearts/data`


## Pipeline

Follow the pipeline steps below to reproduce the analysis results.


#### `python 0__compress_data.py`
- _Description:_ can be skipped as data is ready for use. Only here for reference.

![](https://user-images.githubusercontent.com/32848391/94371727-f2c7c580-00f8-11eb-8175-98cd60b0d0cd.png)


---
#### `python 1__manually_align.py`
- _Description:_ manually adjust alignment of different heart samples to a common frame

![](https://user-images.githubusercontent.com/32848391/94369906-c0b06680-00ec-11eb-916a-29e0556bc937.png)


---
#### `python 2a_make_histos.py`
- _Description:_ make some histograms of the scalar along some ray

![image](https://user-images.githubusercontent.com/32848391/94369915-c9a13800-00ec-11eb-86e0-0429198c392a.png)

![image](https://user-images.githubusercontent.com/32848391/94370309-86949400-00ef-11eb-9b21-d4163de78c8f.png)

---
#### `python 2b_probe_vol.py`
- _Description:_ more visualizations of the volume probing

![image](https://user-images.githubusercontent.com/32848391/94370391-11758e80-00f0-11eb-84b9-828b9d523a9d.png)


---
#### `python 3__generate_rays.py`
- _Description:_ probe volume and save a polydata which is a cloud of point. Files are produced to the local path. They can be visualized with command e.g.:
`vedo -n -p 5 -a 0.02 -c w -x1 *2425*.vtk`. If all looks OK move files to `data/wt` or `data/ko`.

![image](https://user-images.githubusercontent.com/32848391/94370678-a2009e80-00f1-11eb-99a7-7dcf8b7582ef.png)


---
#### `python 4a_expand_plot.py`
- _Description:_ plot scalar values on a specific radius shell for test:

![image](https://user-images.githubusercontent.com/32848391/94370795-569ac000-00f2-11eb-94ea-506aa02bd978.png)


---
#### `python 4b_clm_plot.py`
- _Description:_ plot the spherical harmonics expansion for the above test:

![image](https://user-images.githubusercontent.com/32848391/94369921-d756bd80-00ec-11eb-9ba3-69464ed5dc7a.png)


---
#### `python 5__write_clm.py`
- _Description:_ generate and save a numpy array `clm_data.npy` with the `Clm` spherical harmonic coefficients for all the time points

![step5](https://user-images.githubusercontent.com/32848391/94371848-bc3e7a80-00f9-11eb-8f07-16075893844e.gif)


---
#### `python 6__plot_splined_clm.py`
- _Description:_ make 50 plots of the spherical harm coefficients visualizing the time variable for each one. Pressing return takes to the next radial shell.

![step6](https://user-images.githubusercontent.com/32848391/94371751-1ee34680-00f9-11eb-9aaf-ce93ca54efc4.gif)


---
#### `python 7a_plot_six_clouds.py`
- _Description:_ plot now for each time point the reconstructed point clouds (using the sph coefficients) with a threshold to cut off points that are below some value

![image](https://user-images.githubusercontent.com/32848391/94371614-14747d00-00f8-11eb-8760-1e1c288df60e.png)


---
#### `python 7b_interp_clouds.py`
- _Description:_ interpolate the above time points to generate a continous (small stepped) time course. Interpolation is done by splining all the `Clm` coefficients.

![step7b](https://user-images.githubusercontent.com/32848391/94372187-00327f00-00fc-11eb-88b2-dd8f5dbdff51.gif)


---
#### `python 8a_write_volumes.py`
- _Description:_ generate as many volumes as the nr of interpolated point clouds. Points in space are spatially interpolated onto the regular grid of a Volume object (made of voxels). Isosurfaces are also generated (for 3 different thresholds):

![image](https://user-images.githubusercontent.com/32848391/94372279-88b11f80-00fc-11eb-859f-ba25085c87eb.png)


---
#### `python 8b_write_scaled_isos.py`
- _Description:_ build isosurfaces for all the generated volumes using some threshold value. The absolute size is also recovered from a fit of the original sizes, to take into account the biological growth of the tissues

![h_timecourse_wt](https://user-images.githubusercontent.com/32848391/94372352-f4938800-00fc-11eb-84e8-9804aae3c27c.gif)

![](https://user-images.githubusercontent.com/32848391/94369930-e5a4d980-00ec-11eb-980c-9b012cc821c4.png)


## References

Ten years ago, a population of cardiac progenitor cells was identified
in pharyngeal mesoderm that gives rise to a major part of the amniote heart.
These multipotent progenitor cells, termed the second heart field (SHF),
contribute progressively to the poles of the elongating heart tube during
looping morphogenesis, giving rise to myocardium, smooth muscle, and endothelial cells.

_Arid3b_, a member of the conserved ARID family of transcription
factors, is essential for mouse embryonic development but its precise
roles are poorly understood.
_Arid3b_ is expressed in the myocardium of the tubular heart and in second heart field
progenitors.

_Arid3b_-deficient embryos show cardiac abnormalities,
including a notable shortening of the poles, absence of myocardial
differentiation and altered patterning of the atrioventricular canal,
which also lacks epithelial-to-mesenchymal transition.
Proliferation and death of progenitors as well as early patterning of the heart
appear normal.

_Arid3b_ is thus required for heart development by regulating
the motility and differentiation of heart progenitors. These findings
identify Arid3b as a candidate gene involved in the aetiology of human
congenital malformations.

- _[“Arid3b is essential for second heart field cell deployment and heart patterning”](https://dev.biologists.org/content/141/21/4168)_, J.J. Sanz-Esquerro et al., Development (2014) 141, 4168-4181 doi:10.1242/dev.109918
- [The second heart field](https://pubmed.ncbi.nlm.nih.gov/22449840/)
- [Heart Development (wikipedia)](https://en.wikipedia.org/wiki/Heart_development).


[![vedo_powered](https://user-images.githubusercontent.com/32848391/94372929-13e0e400-0102-11eb-938c-bc0274d57108.png)](https://github.com/marcomusy/vedo)

![embl](https://user-images.githubusercontent.com/32848391/94371851-c3658880-00f9-11eb-9c2a-d418adb93d59.gif)



