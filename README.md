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

In the Jupyter notebook: RPT_Well_1.ipynb, we first build a density trend based on Traugott's equation: ro=rosfl+a*(zbml*3.2808/c)**b, where rosfl is the seafloor density, a, b, c are calibration coefficients, zbml is the depth below mudline in meter. This density trend is then converted into overburden stress. 

We also calculate the temperature and burial age trends based on thermal gradient and burial rate. Using these trends, we derive the diagenesis function, Beta, which is essential for the velocity-to-effective stress transformation using Dutta’s equation.

Next, we create a template of pore pressure gradients ranging from hydrostatic (8.6 ppg), and 9 ppg to 17 ppg in 1 ppg increments. These pore pressure templates are converted to effective stress and then transformed into P-wave velocity using Issler’s equation. This forms our Rock Physics Template (RPT), which can be used to overlay with sonic or seismic velocity for quality control (QC). The figure below shows the RPT velocity curves (from 8.6 to 17 ppg) overlaid with the sonic velocity (blue curve). In the shallow section, P-wave velocity is corrected using the Reuss equation due to suspension mode conditions, where Issler’s equation does not apply.

![image](https://github.com/user-attachments/assets/ed40a158-a123-4f72-bc4b-f2288fcf1e05)

The Sonic velocity can be converted to pore pressure using this RPT.

We also compare modeled density from the sonic velocity with Traugott’s density trend and present a method for temperature modeling from P-wave velocity, incorporating seafloor temperature based on water depth.

Poisson’s ratio and the Vp/Vs ratio are modeled using Castagna’s Mud Rock Line and compared to measured data.

Using the Raymer-Hunt-Gardner (RHG) equation, we then model the RPT for sandstone. The porosity trend is derived from Athy’s equation, and the Vp, density, P-impedance, and Poisson’s ratio templates are computed for varying clay content (0–100%). These results are cross-plotted, showing P-impedance vs Poisson’s ratio or Vp/Vs ratio.
Next, using Raymer-Hunt-Gardner (RHG) equation, we modeled RPT for sandstone. In this sand RPT, porosity trend is based on Athy's equation, then Vp, Density, P-impedance, and Poisson ratio templates with clay content changing from 0-1 are computed and cross-plotted. The cross-plot between P-impedance and Poisson ratio or Vp/Vs ratio are displayed.

Using Gassmann’s equation for fluid substitution, we generate cross-plots of P-impedance vs Poisson’s ratio or Vp/Vs ratio for hydrocarbon-bearing fluids, overlaying field data (triangles representing hydrocarbon sands in the Southern Gulf of Mexico, Liu et al., 2021).

![image](https://github.com/yjliu212/Basin-wide_rock_physics/assets/29761191/830edeff-45c8-4884-8f82-0956bf82c42a)

These rock physics models can be extended to RPT-based AVO modeling. For instance, given a reservoir top at 2000 m with a thickness of 50 m, we modeled the AVO response from a brine-saturated sand reservoir. The figure below shows the AVO curves at the reservoir’s top, bottom, and a deeper level, illustrating a Class III AVO anomaly at the reservoir's top and bottom.

![image](https://github.com/user-attachments/assets/b0c4c93c-baac-4596-9d0f-b0e6b049ecca)

