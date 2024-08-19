# Basin-wide_rock_physics

Basin-wide rock physics modeling

Paper reference:

Liu, Y., J. H. Casado, M. El-Toukhy, and S. Tai, 2021, Basin-wide empirical rock-physics transform and its application in Campeche Basin, The Leading Edge, 40, 178-184.
(https://library.seg.org/doi/10.1190/tle40030178.1)

Liu, Y., M. Ellis, M. El-Toukhy, and J. Hernandez, 2021, Basin-wide rock-physics analysis in Campeche Basin, Gulf of Mexico - phase II: Reservoir rock and fluid properties, The Leading Edge, 40, 716-722.
(https://library.seg.org/doi/10.1190/tle40100716.1)

Notes:

All the .py files are python functions that will be called in the Jupyter notebook: [RPT_Well_1.ipynb](/RPT_Well_1.ipynb)

All .txt files are the input files.  

Description:

In the Jupyter notebook: RPT_Well_1.ipynb, we first build a density trend based on Traugott's equation: ro=rosfl+a*(zbml*3.2808/c)**b, where rosfl is the seafloor density, a, b, c are calibration coefficients. Then we convert the density trend into overburden stress. Next, we calculate the temperature trend and burial age trend based on thermal gradient and burial rate. Using the temperature trend and burial age trend, we calculate the diagenesis function Beta. Beta function is needed in the velocity to effective stress transformation based on Dutta's equation. 

Next We build a template of pore pressure gradients from 8.6 ppg and 9 ppg to 17 ppg with 1 ppg as increment, and convert them to effecrtive stress template, then we convert these effective stress template to P-wave velocity using Issler's equation. This velocity template is our so-called Rock Physics Template (RPT), which can be used to overlain with Sonic velocity or seismic velocity for QC purpose. The figure below shows RPT with velocity curves range from 8.6 ppg and 9 ppg to 17 ppg with 1 ppg as increment from right to left (background curves) and overlain with Sonic velocity (blue curve).

![image](https://github.com/user-attachments/assets/ed40a158-a123-4f72-bc4b-f2288fcf1e05)


In the shallow portion of the RPT, we corrected the P-wave velocity using Reuss equation, since these velocity are in a suspension mode that Issler's equation doesn't apply.

We can convert Sonic velocity to pore pressure using this RPT.

A modeled density from Sonic velocity is compared with Traugott's density trend.

A temperature modeling method from P-wave velocity is presented, where the seafloor temperature is also modeled based on water depth. 

Poisson ratio and Vp/Vs ratio are modeled using Castagna's Mud Rock Line and compared with measured data.

Next, using Raymer-Hunt-Gardner (RHG) equation, we modeled RPT for sandstone. In this sand RPT, porosity trend is based on Athy's equation, then Vp, Density, P-impedance, and Poisson ratio templates with clay content changing from 0-1 are computed and cross-plotted. The cross-plot between P-impedance and Poisson ratio or Vp/Vs ratio are displayed.

Next, we used Gassmann's equation to do fluid substitution and cross-plotted the new P-impedance vs Poisson ratio or Vp/Vs ratio for new fluid content that contains hydrocarbon. We overlain some data onto these cross-plots. In the figure below, tri-angles are data from hydrocarbon sands in Southern Gulf of Mexico (Liu et al., 2021).

![image](https://github.com/yjliu212/Basin-wide_rock_physics/assets/29761191/830edeff-45c8-4884-8f82-0956bf82c42a)

And we can further use these rock physics models for RPT-based AVO modeling. For example, for a given reservoir top and bottom depth and sand model, we could model the AVO response from such a reservoir. In this Python Notebook, we provided an example, in which the reservoir thickness is 50 m with reservoir top located at 2000 m, the picture below shows the modeled AVO curve at reservoir top, bottom and a deeper level with brine saturation. We can see a class III type of AVO anomaly at reservoir top and bottom.

![image](https://github.com/user-attachments/assets/b0c4c93c-baac-4596-9d0f-b0e6b049ecca)

