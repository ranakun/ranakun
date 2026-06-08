<!-- github.com/ranakun -->

<p align="center">
  <img src="hero.svg" alt="Live threshold signing ceremony. Of five key shares two are offline; the remaining three send partial signatures that combine, at a 3 of 5 quorum, into one signature that is then verified." width="100%">
</p>

<h2 align="center">Rana Singh Shashwat</h2>
<p align="center"><strong>Applied cryptography &amp; MPC</strong> · threshold signing &amp; HSM-backed custody infrastructure</p>

<p align="center">I build the signing layer for institutional digital-asset custody:<br>
threshold signature schemes, secure multiparty computation, and air-gapped HSM key management.</p>

---

#### The primitive I build around

$$
f(0) = \sum_{i \in Q} \lambda_i f(i) \qquad \lambda_i = \prod_{j \in Q, j \neq i} \frac{j}{j - i}
$$

<sub>Lagrange interpolation at 0 reconstructs one secret from any <i>t</i> of <i>n</i> shares (|Q| = t): the common core of every threshold scheme, independent of the underlying group (threshold ECDSA, EdDSA, BLS). No single party ever holds the key. (Shamir, <a href="https://web.mit.edu/6.857/OldStuff/Fall03/ref/Shamir-HowToShareASecret.pdf"><i>How to Share a Secret</i></a>, 1979.)</sub>

---

#### Reconstruct the secret · find the angle

<sub>A cloud of shards. Exactly one camera angle resolves it. Drag, or hit the viewer's auto-rotation and watch it pass through.</sub>

```stl
solid shards
  facet normal 0.000000e+00 -2.606377e-01 9.654367e-01
    outer loop
      vertex -2.407926e-01 1.009237e-01 -4.541320e-01
      vertex 3.847836e-02 1.009237e-01 -4.541320e-01
      vertex -1.454258e-01 1.707049e-01 -4.352932e-01
    endloop
  endfacet
  facet normal 2.887108e-01 5.491515e-01 7.842696e-01
    outer loop
      vertex 3.847836e-02 1.009237e-01 -4.541320e-01
      vertex 3.847836e-02 1.928055e-01 -5.184683e-01
      vertex -1.454258e-01 1.707049e-01 -4.352932e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.664642e-01 2.568012e-01
    outer loop
      vertex 3.847836e-02 1.928055e-01 -5.184683e-01
      vertex -2.863808e-01 1.928055e-01 -5.184683e-01
      vertex -1.454258e-01 1.707049e-01 -4.352932e-01
    endloop
  endfacet
  facet normal -3.661181e-01 5.337521e-01 7.622770e-01
    outer loop
      vertex -2.863808e-01 1.928055e-01 -5.184683e-01
      vertex -2.863808e-01 1.277974e-01 -4.729491e-01
      vertex -1.454258e-01 1.707049e-01 -4.352932e-01
    endloop
  endfacet
  facet normal -2.983754e-01 1.534572e-01 9.420313e-01
    outer loop
      vertex -2.863808e-01 1.277974e-01 -4.729491e-01
      vertex -2.407926e-01 1.009237e-01 -4.541320e-01
      vertex -1.454258e-01 1.707049e-01 -4.352932e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -2.441415e-01 7.041851e-02 -5.060185e-01
      vertex 3.901351e-02 1.635782e-01 -5.712496e-01
      vertex 3.901351e-02 7.041851e-02 -5.060185e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -2.441415e-01 7.041851e-02 -5.060185e-01
      vertex -2.903638e-01 1.635782e-01 -5.712496e-01
      vertex 3.901351e-02 1.635782e-01 -5.712496e-01
    endloop
  endfacet
  facet normal 2.332101e-16 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -2.441415e-01 7.041851e-02 -5.060185e-01
      vertex -2.903638e-01 9.766600e-02 -5.250974e-01
      vertex -2.903638e-01 1.635782e-01 -5.712496e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.620524e-01 -5.068191e-01
    outer loop
      vertex -2.407926e-01 1.009237e-01 -4.541320e-01
      vertex 3.847836e-02 1.009237e-01 -4.541320e-01
      vertex 3.901351e-02 7.041851e-02 -5.060185e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.620524e-01 -5.068191e-01
    outer loop
      vertex -2.407926e-01 1.009237e-01 -4.541320e-01
      vertex 3.901351e-02 7.041851e-02 -5.060185e-01
      vertex -2.441415e-01 7.041851e-02 -5.060185e-01
    endloop
  endfacet
  facet normal -9.999602e-01 -5.115626e-03 -7.305872e-03
    outer loop
      vertex 3.847836e-02 1.009237e-01 -4.541320e-01
      vertex 3.847836e-02 1.928055e-01 -5.184683e-01
      vertex 3.901351e-02 1.635782e-01 -5.712496e-01
    endloop
  endfacet
  facet normal -9.999602e-01 -5.115626e-03 -7.305872e-03
    outer loop
      vertex 3.847836e-02 1.009237e-01 -4.541320e-01
      vertex 3.901351e-02 1.635782e-01 -5.712496e-01
      vertex 3.901351e-02 7.041851e-02 -5.060185e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -8.748293e-01 4.844313e-01
    outer loop
      vertex 3.847836e-02 1.928055e-01 -5.184683e-01
      vertex -2.863808e-01 1.928055e-01 -5.184683e-01
      vertex -2.903638e-01 1.635782e-01 -5.712496e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -8.748293e-01 4.844313e-01
    outer loop
      vertex 3.847836e-02 1.928055e-01 -5.184683e-01
      vertex -2.903638e-01 1.635782e-01 -5.712496e-01
      vertex 3.901351e-02 1.635782e-01 -5.712496e-01
    endloop
  endfacet
  facet normal 9.978040e-01 -3.799170e-02 -5.425776e-02
    outer loop
      vertex -2.863808e-01 1.928055e-01 -5.184683e-01
      vertex -2.863808e-01 1.277974e-01 -4.729491e-01
      vertex -2.903638e-01 9.766600e-02 -5.250974e-01
    endloop
  endfacet
  facet normal 9.978040e-01 -3.799170e-02 -5.425776e-02
    outer loop
      vertex -2.863808e-01 1.928055e-01 -5.184683e-01
      vertex -2.903638e-01 9.766600e-02 -5.250974e-01
      vertex -2.903638e-01 1.635782e-01 -5.712496e-01
    endloop
  endfacet
  facet normal 5.838100e-01 6.828688e-01 -4.391539e-01
    outer loop
      vertex -2.863808e-01 1.277974e-01 -4.729491e-01
      vertex -2.407926e-01 1.009237e-01 -4.541320e-01
      vertex -2.441415e-01 7.041851e-02 -5.060185e-01
    endloop
  endfacet
  facet normal 5.838100e-01 6.828688e-01 -4.391539e-01
    outer loop
      vertex -2.863808e-01 1.277974e-01 -4.729491e-01
      vertex -2.441415e-01 7.041851e-02 -5.060185e-01
      vertex -2.903638e-01 9.766600e-02 -5.250974e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -2.191654e-01 9.756877e-01
    outer loop
      vertex 2.561680e-02 1.092611e-01 -4.396000e-01
      vertex 2.388885e-01 1.092611e-01 -4.396000e-01
      vertex 1.688530e-01 1.827323e-01 -4.230964e-01
    endloop
  endfacet
  facet normal 3.278429e-01 1.015290e-01 9.392608e-01
    outer loop
      vertex 2.388885e-01 1.092611e-01 -4.396000e-01
      vertex 3.941528e-01 2.007876e-01 -5.036875e-01
      vertex 1.688530e-01 1.827323e-01 -4.230964e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.758109e-01 2.186163e-01
    outer loop
      vertex 3.941528e-01 2.007876e-01 -5.036875e-01
      vertex 2.561680e-02 2.007876e-01 -5.036875e-01
      vertex 1.688530e-01 1.827323e-01 -4.230964e-01
    endloop
  endfacet
  facet normal -3.622049e-01 5.346297e-01 7.635304e-01
    outer loop
      vertex 2.561680e-02 2.007876e-01 -5.036875e-01
      vertex 2.561680e-02 1.092611e-01 -4.396000e-01
      vertex 1.688530e-01 1.827323e-01 -4.230964e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 2.597446e-02 7.875390e-02 -4.914850e-01
      vertex 3.996559e-01 1.715582e-01 -5.564673e-01
      vertex 2.422238e-01 7.875390e-02 -4.914850e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 2.597446e-02 7.875390e-02 -4.914850e-01
      vertex 2.597446e-02 1.715582e-01 -5.564673e-01
      vertex 3.996559e-01 1.715582e-01 -5.564673e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.620315e-01 -5.068546e-01
    outer loop
      vertex 2.561680e-02 1.092611e-01 -4.396000e-01
      vertex 2.388885e-01 1.092611e-01 -4.396000e-01
      vertex 2.422238e-01 7.875390e-02 -4.914850e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.620315e-01 -5.068546e-01
    outer loop
      vertex 2.561680e-02 1.092611e-01 -4.396000e-01
      vertex 2.422238e-01 7.875390e-02 -4.914850e-01
      vertex 2.597446e-02 7.875390e-02 -4.914850e-01
    endloop
  endfacet
  facet normal -5.838081e-01 6.829231e-01 -4.390719e-01
    outer loop
      vertex 2.388885e-01 1.092611e-01 -4.396000e-01
      vertex 3.941528e-01 2.007876e-01 -5.036875e-01
      vertex 3.996559e-01 1.715582e-01 -5.564673e-01
    endloop
  endfacet
  facet normal -5.838081e-01 6.829231e-01 -4.390719e-01
    outer loop
      vertex 2.388885e-01 1.092611e-01 -4.396000e-01
      vertex 3.996559e-01 1.715582e-01 -5.564673e-01
      vertex 2.422238e-01 7.875390e-02 -4.914850e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -8.748094e-01 4.844672e-01
    outer loop
      vertex 3.941528e-01 2.007876e-01 -5.036875e-01
      vertex 2.561680e-02 2.007876e-01 -5.036875e-01
      vertex 2.597446e-02 1.715582e-01 -5.564673e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -8.748094e-01 4.844672e-01
    outer loop
      vertex 3.941528e-01 2.007876e-01 -5.036875e-01
      vertex 2.597446e-02 1.715582e-01 -5.564673e-01
      vertex 3.996559e-01 1.715582e-01 -5.564673e-01
    endloop
  endfacet
  facet normal 9.999822e-01 3.419005e-03 4.882845e-03
    outer loop
      vertex 2.561680e-02 2.007876e-01 -5.036875e-01
      vertex 2.561680e-02 1.092611e-01 -4.396000e-01
      vertex 2.597446e-02 7.875390e-02 -4.914850e-01
    endloop
  endfacet
  facet normal 9.999822e-01 3.419005e-03 4.882845e-03
    outer loop
      vertex 2.561680e-02 2.007876e-01 -5.036875e-01
      vertex 2.597446e-02 7.875390e-02 -4.914850e-01
      vertex 2.597446e-02 1.715582e-01 -5.564673e-01
    endloop
  endfacet
  facet normal -0.000000e+00 1.364381e-04 1.000000e+00
    outer loop
      vertex -3.628473e-01 3.275786e-01 -2.664658e-01
      vertex -2.598213e-01 3.275786e-01 -2.664658e-01
      vertex -3.279703e-01 3.866743e-01 -2.664739e-01
    endloop
  endfacet
  facet normal 4.452659e-01 5.135794e-01 7.334674e-01
    outer loop
      vertex -2.598213e-01 3.275786e-01 -2.664658e-01
      vertex -2.598213e-01 4.134175e-01 -3.265709e-01
      vertex -3.279703e-01 3.866743e-01 -2.664739e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.136228e-01 4.065629e-01
    outer loop
      vertex -2.598213e-01 4.134175e-01 -3.265709e-01
      vertex -4.405157e-01 4.134175e-01 -3.265709e-01
      vertex -3.279703e-01 3.866743e-01 -2.664739e-01
    endloop
  endfacet
  facet normal -4.113809e-01 2.429082e-01 8.784995e-01
    outer loop
      vertex -4.405157e-01 4.134175e-01 -3.265709e-01
      vertex -3.628473e-01 3.275786e-01 -2.664658e-01
      vertex -3.279703e-01 3.866743e-01 -2.664739e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -3.682490e-01 2.983001e-01 -3.192113e-01
      vertex -2.636892e-01 3.854169e-01 -3.802111e-01
      vertex -2.636892e-01 2.983001e-01 -3.192113e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -3.682490e-01 2.983001e-01 -3.192113e-01
      vertex -4.470737e-01 3.854169e-01 -3.802111e-01
      vertex -2.636892e-01 3.854169e-01 -3.802111e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.743298e-01 -4.853323e-01
    outer loop
      vertex -3.628473e-01 3.275786e-01 -2.664658e-01
      vertex -2.598213e-01 3.275786e-01 -2.664658e-01
      vertex -2.636892e-01 2.983001e-01 -3.192113e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.743298e-01 -4.853323e-01
    outer loop
      vertex -3.628473e-01 3.275786e-01 -2.664658e-01
      vertex -2.636892e-01 2.983001e-01 -3.192113e-01
      vertex -3.682490e-01 2.983001e-01 -3.192113e-01
    endloop
  endfacet
  facet normal -9.979285e-01 3.689937e-02 5.269776e-02
    outer loop
      vertex -2.598213e-01 3.275786e-01 -2.664658e-01
      vertex -2.598213e-01 4.134175e-01 -3.265709e-01
      vertex -2.636892e-01 3.854169e-01 -3.802111e-01
    endloop
  endfacet
  facet normal -9.979285e-01 3.689937e-02 5.269776e-02
    outer loop
      vertex -2.598213e-01 3.275786e-01 -2.664658e-01
      vertex -2.636892e-01 3.854169e-01 -3.802111e-01
      vertex -2.636892e-01 2.983001e-01 -3.192113e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -8.864871e-01 4.627533e-01
    outer loop
      vertex -2.598213e-01 4.134175e-01 -3.265709e-01
      vertex -4.405157e-01 4.134175e-01 -3.265709e-01
      vertex -4.470737e-01 3.854169e-01 -3.802111e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -8.864871e-01 4.627533e-01
    outer loop
      vertex -2.598213e-01 4.134175e-01 -3.265709e-01
      vertex -4.470737e-01 3.854169e-01 -3.802111e-01
      vertex -2.636892e-01 3.854169e-01 -3.802111e-01
    endloop
  endfacet
  facet normal 8.033469e-01 4.819501e-01 -3.497970e-01
    outer loop
      vertex -4.405157e-01 4.134175e-01 -3.265709e-01
      vertex -3.628473e-01 3.275786e-01 -2.664658e-01
      vertex -3.682490e-01 2.983001e-01 -3.192113e-01
    endloop
  endfacet
  facet normal 8.033469e-01 4.819501e-01 -3.497970e-01
    outer loop
      vertex -4.405157e-01 4.134175e-01 -3.265709e-01
      vertex -3.682490e-01 2.983001e-01 -3.192113e-01
      vertex -4.470737e-01 3.854169e-01 -3.802111e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -3.556266e-01 9.346281e-01
    outer loop
      vertex -2.469525e-01 4.846414e-01 1.648392e-02
      vertex 3.230432e-02 4.846414e-01 1.648392e-02
      vertex -1.055719e-01 5.530327e-01 4.250688e-02
    endloop
  endfacet
  facet normal 4.020646e-01 5.251731e-01 7.500249e-01
    outer loop
      vertex 3.230432e-02 4.846414e-01 1.648392e-02
      vertex 3.230432e-02 5.636252e-01 -3.882116e-02
      vertex -1.055719e-01 5.530327e-01 4.250688e-02
    endloop
  endfacet
  facet normal 0.000000e+00 9.916247e-01 1.291531e-01
    outer loop
      vertex 3.230432e-02 5.636252e-01 -3.882116e-02
      vertex -2.469525e-01 5.636252e-01 -3.882116e-02
      vertex -1.055719e-01 5.530327e-01 4.250688e-02
    endloop
  endfacet
  facet normal -3.936598e-01 5.272637e-01 7.530106e-01
    outer loop
      vertex -2.469525e-01 5.636252e-01 -3.882116e-02
      vertex -2.469525e-01 4.846414e-01 1.648392e-02
      vertex -1.055719e-01 5.530327e-01 4.250688e-02
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -2.509479e-01 4.553628e-01 -3.626152e-02
      vertex 3.282697e-02 5.356246e-01 -9.246139e-02
      vertex 3.282697e-02 4.553628e-01 -3.626152e-02
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -2.509479e-01 4.553628e-01 -3.626152e-02
      vertex -2.509479e-01 5.356246e-01 -9.246139e-02
      vertex 3.282697e-02 5.356246e-01 -9.246139e-02
    endloop
  endfacet
  facet normal 0.000000e+00 8.743298e-01 -4.853323e-01
    outer loop
      vertex -2.469525e-01 4.846414e-01 1.648392e-02
      vertex 3.230432e-02 4.846414e-01 1.648392e-02
      vertex 3.282697e-02 4.553628e-01 -3.626152e-02
    endloop
  endfacet
  facet normal 0.000000e+00 8.743298e-01 -4.853323e-01
    outer loop
      vertex -2.469525e-01 4.846414e-01 1.648392e-02
      vertex 3.282697e-02 4.553628e-01 -3.626152e-02
      vertex -2.509479e-01 4.553628e-01 -3.626152e-02
    endloop
  endfacet
  facet normal -9.999621e-01 -4.996144e-03 -7.135234e-03
    outer loop
      vertex 3.230432e-02 4.846414e-01 1.648392e-02
      vertex 3.230432e-02 5.636252e-01 -3.882116e-02
      vertex 3.282697e-02 5.356246e-01 -9.246139e-02
    endloop
  endfacet
  facet normal -9.999621e-01 -4.996144e-03 -7.135234e-03
    outer loop
      vertex 3.230432e-02 4.846414e-01 1.648392e-02
      vertex 3.282697e-02 5.356246e-01 -9.246139e-02
      vertex 3.282697e-02 4.553628e-01 -3.626152e-02
    endloop
  endfacet
  facet normal 0.000000e+00 -8.864871e-01 4.627533e-01
    outer loop
      vertex 3.230432e-02 5.636252e-01 -3.882116e-02
      vertex -2.469525e-01 5.636252e-01 -3.882116e-02
      vertex -2.509479e-01 5.356246e-01 -9.246139e-02
    endloop
  endfacet
  facet normal 0.000000e+00 -8.864871e-01 4.627533e-01
    outer loop
      vertex 3.230432e-02 5.636252e-01 -3.882116e-02
      vertex -2.509479e-01 5.356246e-01 -9.246139e-02
      vertex 3.282697e-02 5.356246e-01 -9.246139e-02
    endloop
  endfacet
  facet normal 9.977902e-01 -3.811040e-02 -5.442730e-02
    outer loop
      vertex -2.469525e-01 5.636252e-01 -3.882116e-02
      vertex -2.469525e-01 4.846414e-01 1.648392e-02
      vertex -2.509479e-01 4.553628e-01 -3.626152e-02
    endloop
  endfacet
  facet normal 9.977902e-01 -3.811040e-02 -5.442730e-02
    outer loop
      vertex -2.469525e-01 5.636252e-01 -3.882116e-02
      vertex -2.509479e-01 4.553628e-01 -3.626152e-02
      vertex -2.509479e-01 5.356246e-01 -9.246139e-02
    endloop
  endfacet
  facet normal 0.000000e+00 -4.322769e-01 9.017409e-01
    outer loop
      vertex 2.256367e-02 2.105329e-01 -4.781959e-01
      vertex 3.888295e-01 2.105329e-01 -4.781959e-01
      vertex 2.386771e-01 2.783907e-01 -4.456662e-01
    endloop
  endfacet
  facet normal 3.355860e-01 3.173916e-01 8.869299e-01
    outer loop
      vertex 3.888295e-01 2.105329e-01 -4.781959e-01
      vertex 3.890176e-01 2.107407e-01 -4.783414e-01
      vertex 2.386771e-01 2.783907e-01 -4.456662e-01
    endloop
  endfacet
  facet normal 3.997666e-01 5.257499e-01 7.508487e-01
    outer loop
      vertex 3.890176e-01 2.107407e-01 -4.783414e-01
      vertex 3.890176e-01 3.014955e-01 -5.418886e-01
      vertex 2.386771e-01 2.783907e-01 -4.456662e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.723610e-01 2.334826e-01
    outer loop
      vertex 3.890176e-01 3.014955e-01 -5.418886e-01
      vertex 2.256367e-02 3.014955e-01 -5.418886e-01
      vertex 2.386771e-01 2.783907e-01 -4.456662e-01
    endloop
  endfacet
  facet normal -2.903298e-01 5.488706e-01 7.838684e-01
    outer loop
      vertex 2.256367e-02 3.014955e-01 -5.418886e-01
      vertex 2.256367e-02 2.105329e-01 -4.781959e-01
      vertex 2.386771e-01 2.783907e-01 -4.456662e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 2.288065e-02 1.812592e-01 -5.309447e-01
      vertex 3.944826e-01 1.814700e-01 -5.310923e-01
      vertex 3.942920e-01 1.812592e-01 -5.309447e-01
    endloop
  endfacet
  facet normal 4.138934e-18 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 2.288065e-02 1.812592e-01 -5.309447e-01
      vertex 3.944826e-01 2.734998e-01 -5.955323e-01
      vertex 3.944826e-01 1.814700e-01 -5.310923e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 2.288065e-02 1.812592e-01 -5.309447e-01
      vertex 2.288065e-02 2.734998e-01 -5.955323e-01
      vertex 3.944826e-01 2.734998e-01 -5.955323e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.743776e-01 -4.852462e-01
    outer loop
      vertex 2.256367e-02 2.105329e-01 -4.781959e-01
      vertex 3.888295e-01 2.105329e-01 -4.781959e-01
      vertex 3.942920e-01 1.812592e-01 -5.309447e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.743776e-01 -4.852462e-01
    outer loop
      vertex 2.256367e-02 2.105329e-01 -4.781959e-01
      vertex 3.942920e-01 1.812592e-01 -5.309447e-01
      vertex 2.288065e-02 1.812592e-01 -5.309447e-01
    endloop
  endfacet
  facet normal -8.033405e-01 4.815138e-01 -3.504119e-01
    outer loop
      vertex 3.888295e-01 2.105329e-01 -4.781959e-01
      vertex 3.890176e-01 2.107407e-01 -4.783414e-01
      vertex 3.944826e-01 1.814700e-01 -5.310923e-01
    endloop
  endfacet
  facet normal -8.033405e-01 4.815138e-01 -3.504119e-01
    outer loop
      vertex 3.888295e-01 2.105329e-01 -4.781959e-01
      vertex 3.944826e-01 1.814700e-01 -5.310923e-01
      vertex 3.942920e-01 1.812592e-01 -5.309447e-01
    endloop
  endfacet
  facet normal -9.958775e-01 -5.202847e-02 -7.430436e-02
    outer loop
      vertex 3.890176e-01 2.107407e-01 -4.783414e-01
      vertex 3.890176e-01 3.014955e-01 -5.418886e-01
      vertex 3.944826e-01 2.734998e-01 -5.955323e-01
    endloop
  endfacet
  facet normal -9.958775e-01 -5.202847e-02 -7.430436e-02
    outer loop
      vertex 3.890176e-01 2.107407e-01 -4.783414e-01
      vertex 3.944826e-01 2.734998e-01 -5.955323e-01
      vertex 3.944826e-01 1.814700e-01 -5.310923e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -8.865324e-01 4.626666e-01
    outer loop
      vertex 3.890176e-01 3.014955e-01 -5.418886e-01
      vertex 2.256367e-02 3.014955e-01 -5.418886e-01
      vertex 2.288065e-02 2.734998e-01 -5.955323e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -8.865324e-01 4.626666e-01
    outer loop
      vertex 3.890176e-01 3.014955e-01 -5.418886e-01
      vertex 2.288065e-02 2.734998e-01 -5.955323e-01
      vertex 3.944826e-01 2.734998e-01 -5.955323e-01
    endloop
  endfacet
  facet normal 9.999860e-01 3.030188e-03 4.327557e-03
    outer loop
      vertex 2.256367e-02 3.014955e-01 -5.418886e-01
      vertex 2.256367e-02 2.105329e-01 -4.781959e-01
      vertex 2.288065e-02 1.812592e-01 -5.309447e-01
    endloop
  endfacet
  facet normal 9.999860e-01 3.030188e-03 4.327557e-03
    outer loop
      vertex 2.256367e-02 3.014955e-01 -5.418886e-01
      vertex 2.288065e-02 1.812592e-01 -5.309447e-01
      vertex 2.288065e-02 2.734998e-01 -5.955323e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -4.822756e-01 8.760195e-01
    outer loop
      vertex -4.571584e-01 3.358292e-01 -4.688172e-01
      vertex -2.692447e-01 3.358292e-01 -4.688172e-01
      vertex -3.646679e-01 3.716888e-01 -4.490754e-01
    endloop
  endfacet
  facet normal 3.593065e-01 5.352728e-01 7.644487e-01
    outer loop
      vertex -2.692447e-01 3.358292e-01 -4.688172e-01
      vertex -2.692447e-01 3.735449e-01 -4.952260e-01
      vertex -3.646679e-01 3.716888e-01 -4.490754e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.991922e-01 4.018735e-02
    outer loop
      vertex -2.692447e-01 3.735449e-01 -4.952260e-01
      vertex -4.759229e-01 3.735449e-01 -4.952260e-01
      vertex -3.646679e-01 3.716888e-01 -4.490754e-01
    endloop
  endfacet
  facet normal -3.419538e-01 4.188794e-01 8.411942e-01
    outer loop
      vertex -4.759229e-01 3.735449e-01 -4.952260e-01
      vertex -4.571584e-01 3.358292e-01 -4.688172e-01
      vertex -3.646679e-01 3.716888e-01 -4.490754e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -4.637026e-01 3.077937e-01 -5.224330e-01
      vertex -2.730990e-01 3.460492e-01 -5.492198e-01
      vertex -2.730990e-01 3.077937e-01 -5.224330e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -4.637026e-01 3.077937e-01 -5.224330e-01
      vertex -4.827358e-01 3.460492e-01 -5.492198e-01
      vertex -2.730990e-01 3.460492e-01 -5.492198e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.861632e-01 -4.633732e-01
    outer loop
      vertex -4.571584e-01 3.358292e-01 -4.688172e-01
      vertex -2.692447e-01 3.358292e-01 -4.688172e-01
      vertex -2.730990e-01 3.077937e-01 -5.224330e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.861632e-01 -4.633732e-01
    outer loop
      vertex -4.571584e-01 3.358292e-01 -4.688172e-01
      vertex -2.730990e-01 3.077937e-01 -5.224330e-01
      vertex -4.637026e-01 3.077937e-01 -5.224330e-01
    endloop
  endfacet
  facet normal -9.979431e-01 3.676921e-02 5.251187e-02
    outer loop
      vertex -2.692447e-01 3.358292e-01 -4.688172e-01
      vertex -2.692447e-01 3.735449e-01 -4.952260e-01
      vertex -2.730990e-01 3.460492e-01 -5.492198e-01
    endloop
  endfacet
  facet normal -9.979431e-01 3.676921e-02 5.251187e-02
    outer loop
      vertex -2.692447e-01 3.358292e-01 -4.688172e-01
      vertex -2.730990e-01 3.460492e-01 -5.492198e-01
      vertex -2.730990e-01 3.077937e-01 -5.224330e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -8.911102e-01 4.537870e-01
    outer loop
      vertex -2.692447e-01 3.735449e-01 -4.952260e-01
      vertex -4.759229e-01 3.735449e-01 -4.952260e-01
      vertex -4.827358e-01 3.460492e-01 -5.492198e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -8.911102e-01 4.537870e-01
    outer loop
      vertex -2.692447e-01 3.735449e-01 -4.952260e-01
      vertex -4.827358e-01 3.460492e-01 -5.492198e-01
      vertex -2.730990e-01 3.460492e-01 -5.492198e-01
    endloop
  endfacet
  facet normal 9.247958e-01 2.789412e-01 -2.587364e-01
    outer loop
      vertex -4.759229e-01 3.735449e-01 -4.952260e-01
      vertex -4.571584e-01 3.358292e-01 -4.688172e-01
      vertex -4.637026e-01 3.077937e-01 -5.224330e-01
    endloop
  endfacet
  facet normal 9.247958e-01 2.789412e-01 -2.587364e-01
    outer loop
      vertex -4.759229e-01 3.735449e-01 -4.952260e-01
      vertex -4.637026e-01 3.077937e-01 -5.224330e-01
      vertex -4.827358e-01 3.460492e-01 -5.492198e-01
    endloop
  endfacet
  facet normal 3.908088e-01 5.279610e-01 7.540064e-01
    outer loop
      vertex -2.480792e-01 5.201420e-01 -2.031303e-01
      vertex -2.480792e-01 5.677176e-01 -2.364431e-01
      vertex -3.456229e-01 5.626707e-01 -1.823514e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.956756e-01 9.289791e-02
    outer loop
      vertex -2.480792e-01 5.677176e-01 -2.364431e-01
      vertex -4.624828e-01 5.677176e-01 -2.364431e-01
      vertex -3.456229e-01 5.626707e-01 -1.823514e-01
    endloop
  endfacet
  facet normal -3.702372e-01 4.021386e-01 8.373822e-01
    outer loop
      vertex -4.624828e-01 5.677176e-01 -2.364431e-01
      vertex -4.388127e-01 5.201420e-01 -2.031303e-01
      vertex -3.456229e-01 5.626707e-01 -1.823514e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -4.389893e-01 8.984923e-01
    outer loop
      vertex -4.388127e-01 5.201420e-01 -2.031303e-01
      vertex -2.480792e-01 5.201420e-01 -2.031303e-01
      vertex -3.456229e-01 5.626707e-01 -1.823514e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -2.519273e-01 4.926217e-01 -2.571069e-01
      vertex -4.696567e-01 5.409353e-01 -2.909364e-01
      vertex -2.519273e-01 5.409353e-01 -2.909364e-01
    endloop
  endfacet
  facet normal -0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -2.519273e-01 4.926217e-01 -2.571069e-01
      vertex -4.456194e-01 4.926217e-01 -2.571069e-01
      vertex -4.696567e-01 5.409353e-01 -2.909364e-01
    endloop
  endfacet
  facet normal -9.979496e-01 3.671113e-02 5.242893e-02
    outer loop
      vertex -2.480792e-01 5.201420e-01 -2.031303e-01
      vertex -2.480792e-01 5.677176e-01 -2.364431e-01
      vertex -2.519273e-01 5.409353e-01 -2.909364e-01
    endloop
  endfacet
  facet normal -9.979496e-01 3.671113e-02 5.242893e-02
    outer loop
      vertex -2.480792e-01 5.201420e-01 -2.031303e-01
      vertex -2.519273e-01 5.409353e-01 -2.909364e-01
      vertex -2.519273e-01 4.926217e-01 -2.571069e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -8.974655e-01 4.410847e-01
    outer loop
      vertex -2.480792e-01 5.677176e-01 -2.364431e-01
      vertex -4.624828e-01 5.677176e-01 -2.364431e-01
      vertex -4.696567e-01 5.409353e-01 -2.909364e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -8.974655e-01 4.410847e-01
    outer loop
      vertex -2.480792e-01 5.677176e-01 -2.364431e-01
      vertex -4.696567e-01 5.409353e-01 -2.909364e-01
      vertex -2.519273e-01 5.409353e-01 -2.909364e-01
    endloop
  endfacet
  facet normal 9.247913e-01 2.788858e-01 -2.588123e-01
    outer loop
      vertex -4.624828e-01 5.677176e-01 -2.364431e-01
      vertex -4.388127e-01 5.201420e-01 -2.031303e-01
      vertex -4.456194e-01 4.926217e-01 -2.571069e-01
    endloop
  endfacet
  facet normal 9.247913e-01 2.788858e-01 -2.588123e-01
    outer loop
      vertex -4.624828e-01 5.677176e-01 -2.364431e-01
      vertex -4.456194e-01 4.926217e-01 -2.571069e-01
      vertex -4.696567e-01 5.409353e-01 -2.909364e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.908876e-01 -4.542239e-01
    outer loop
      vertex -4.388127e-01 5.201420e-01 -2.031303e-01
      vertex -2.480792e-01 5.201420e-01 -2.031303e-01
      vertex -2.519273e-01 4.926217e-01 -2.571069e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.908876e-01 -4.542239e-01
    outer loop
      vertex -4.388127e-01 5.201420e-01 -2.031303e-01
      vertex -2.519273e-01 4.926217e-01 -2.571069e-01
      vertex -4.456194e-01 4.926217e-01 -2.571069e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -6.853733e-01 7.281919e-01
    outer loop
      vertex -2.405142e-01 6.066418e-01 4.908947e-02
      vertex 3.146211e-02 6.066418e-01 4.908947e-02
      vertex -1.028523e-01 6.496557e-01 8.957410e-02
    endloop
  endfacet
  facet normal 3.954874e-01 5.268136e-01 7.523677e-01
    outer loop
      vertex 3.146211e-02 6.066418e-01 4.908947e-02
      vertex 3.146211e-02 6.391422e-01 2.633240e-02
      vertex -1.028523e-01 6.496557e-01 8.957410e-02
    endloop
  endfacet
  facet normal 0.000000e+00 9.864617e-01 -1.639917e-01
    outer loop
      vertex 3.146211e-02 6.391422e-01 2.633240e-02
      vertex -2.405142e-01 6.391422e-01 2.633240e-02
      vertex -1.028523e-01 6.496557e-01 8.957410e-02
    endloop
  endfacet
  facet normal -3.873284e-01 5.288041e-01 7.552105e-01
    outer loop
      vertex -2.405142e-01 6.391422e-01 2.633240e-02
      vertex -2.405142e-01 6.066418e-01 4.908947e-02
      vertex -1.028523e-01 6.496557e-01 8.957410e-02
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -2.445096e-01 5.786062e-01 -4.526283e-03
      vertex 3.198476e-02 6.116465e-01 -2.766139e-02
      vertex 3.198476e-02 5.786062e-01 -4.526283e-03
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -2.445096e-01 5.786062e-01 -4.526283e-03
      vertex -2.445096e-01 6.116465e-01 -2.766139e-02
      vertex 3.198476e-02 6.116465e-01 -2.766139e-02
    endloop
  endfacet
  facet normal 0.000000e+00 8.861632e-01 -4.633732e-01
    outer loop
      vertex -2.405142e-01 6.066418e-01 4.908947e-02
      vertex 3.146211e-02 6.066418e-01 4.908947e-02
      vertex 3.198476e-02 5.786062e-01 -4.526283e-03
    endloop
  endfacet
  facet normal 0.000000e+00 8.861632e-01 -4.633732e-01
    outer loop
      vertex -2.405142e-01 6.066418e-01 4.908947e-02
      vertex 3.198476e-02 5.786062e-01 -4.526283e-03
      vertex -2.445096e-01 5.786062e-01 -4.526283e-03
    endloop
  endfacet
  facet normal -9.999621e-01 -4.996144e-03 -7.135234e-03
    outer loop
      vertex 3.146211e-02 6.066418e-01 4.908947e-02
      vertex 3.146211e-02 6.391422e-01 2.633240e-02
      vertex 3.198476e-02 6.116465e-01 -2.766139e-02
    endloop
  endfacet
  facet normal -9.999621e-01 -4.996144e-03 -7.135234e-03
    outer loop
      vertex 3.146211e-02 6.066418e-01 4.908947e-02
      vertex 3.198476e-02 6.116465e-01 -2.766139e-02
      vertex 3.198476e-02 5.786062e-01 -4.526283e-03
    endloop
  endfacet
  facet normal 0.000000e+00 -8.911102e-01 4.537870e-01
    outer loop
      vertex 3.146211e-02 6.391422e-01 2.633240e-02
      vertex -2.405142e-01 6.391422e-01 2.633240e-02
      vertex -2.445096e-01 6.116465e-01 -2.766139e-02
    endloop
  endfacet
  facet normal 0.000000e+00 -8.911102e-01 4.537870e-01
    outer loop
      vertex 3.146211e-02 6.391422e-01 2.633240e-02
      vertex -2.445096e-01 6.116465e-01 -2.766139e-02
      vertex 3.198476e-02 6.116465e-01 -2.766139e-02
    endloop
  endfacet
  facet normal 9.977902e-01 -3.811040e-02 -5.442730e-02
    outer loop
      vertex -2.405142e-01 6.391422e-01 2.633240e-02
      vertex -2.405142e-01 6.066418e-01 4.908947e-02
      vertex -2.445096e-01 5.786062e-01 -4.526283e-03
    endloop
  endfacet
  facet normal 9.977902e-01 -3.811040e-02 -5.442730e-02
    outer loop
      vertex -2.405142e-01 6.391422e-01 2.633240e-02
      vertex -2.445096e-01 5.786062e-01 -4.526283e-03
      vertex -2.445096e-01 6.116465e-01 -2.766139e-02
    endloop
  endfacet
  facet normal 3.723303e-01 5.323365e-01 7.602553e-01
    outer loop
      vertex 3.404474e-02 5.016739e-01 -2.393524e-01
      vertex 3.404474e-02 5.497448e-01 -2.730119e-01
      vertex -1.114175e-01 5.521166e-01 -2.034335e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.994195e-01 -3.406816e-02
    outer loop
      vertex 3.404474e-02 5.497448e-01 -2.730119e-01
      vertex -2.602573e-01 5.497448e-01 -2.730119e-01
      vertex -1.114175e-01 5.521166e-01 -2.034335e-01
    endloop
  endfacet
  facet normal -3.650180e-01 5.339999e-01 7.626309e-01
    outer loop
      vertex -2.602573e-01 5.497448e-01 -2.730119e-01
      vertex -2.602573e-01 5.016739e-01 -2.393524e-01
      vertex -1.114175e-01 5.521166e-01 -2.034335e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.800448e-01 8.145846e-01
    outer loop
      vertex -2.602573e-01 5.016739e-01 -2.393524e-01
      vertex 3.404474e-02 5.016739e-01 -2.393524e-01
      vertex -1.114175e-01 5.521166e-01 -2.034335e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 3.456739e-02 4.741537e-01 -2.933290e-01
      vertex -2.642527e-01 5.229625e-01 -3.275053e-01
      vertex 3.456739e-02 5.229625e-01 -3.275053e-01
    endloop
  endfacet
  facet normal -0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 3.456739e-02 4.741537e-01 -2.933290e-01
      vertex -2.642527e-01 4.741537e-01 -2.933290e-01
      vertex -2.642527e-01 5.229625e-01 -3.275053e-01
    endloop
  endfacet
  facet normal -9.999621e-01 -4.996144e-03 -7.135234e-03
    outer loop
      vertex 3.404474e-02 5.016739e-01 -2.393524e-01
      vertex 3.404474e-02 5.497448e-01 -2.730119e-01
      vertex 3.456739e-02 5.229625e-01 -3.275053e-01
    endloop
  endfacet
  facet normal -9.999621e-01 -4.996144e-03 -7.135234e-03
    outer loop
      vertex 3.404474e-02 5.016739e-01 -2.393524e-01
      vertex 3.456739e-02 5.229625e-01 -3.275053e-01
      vertex 3.456739e-02 4.741537e-01 -2.933290e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -8.974655e-01 4.410847e-01
    outer loop
      vertex 3.404474e-02 5.497448e-01 -2.730119e-01
      vertex -2.602573e-01 5.497448e-01 -2.730119e-01
      vertex -2.642527e-01 5.229625e-01 -3.275053e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -8.974655e-01 4.410847e-01
    outer loop
      vertex 3.404474e-02 5.497448e-01 -2.730119e-01
      vertex -2.642527e-01 5.229625e-01 -3.275053e-01
      vertex 3.456739e-02 5.229625e-01 -3.275053e-01
    endloop
  endfacet
  facet normal 9.977902e-01 -3.811040e-02 -5.442730e-02
    outer loop
      vertex -2.602573e-01 5.497448e-01 -2.730119e-01
      vertex -2.602573e-01 5.016739e-01 -2.393524e-01
      vertex -2.642527e-01 4.741537e-01 -2.933290e-01
    endloop
  endfacet
  facet normal 9.977902e-01 -3.811040e-02 -5.442730e-02
    outer loop
      vertex -2.602573e-01 5.497448e-01 -2.730119e-01
      vertex -2.642527e-01 4.741537e-01 -2.933290e-01
      vertex -2.642527e-01 5.229625e-01 -3.275053e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.908876e-01 -4.542239e-01
    outer loop
      vertex -2.602573e-01 5.016739e-01 -2.393524e-01
      vertex 3.404474e-02 5.016739e-01 -2.393524e-01
      vertex 3.456739e-02 4.741537e-01 -2.933290e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.908876e-01 -4.542239e-01
    outer loop
      vertex -2.602573e-01 5.016739e-01 -2.393524e-01
      vertex 3.456739e-02 4.741537e-01 -2.933290e-01
      vertex -2.642527e-01 4.741537e-01 -2.933290e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -6.884573e-01 7.252769e-01
    outer loop
      vertex 2.274639e-02 4.006630e-01 -3.448279e-01
      vertex 3.704696e-01 4.006630e-01 -3.448279e-01
      vertex 1.934187e-01 4.493191e-01 -2.986420e-01
    endloop
  endfacet
  facet normal 3.480910e-01 5.377054e-01 7.679229e-01
    outer loop
      vertex 3.704696e-01 4.006630e-01 -3.448279e-01
      vertex 3.704696e-01 4.371302e-01 -3.703625e-01
      vertex 1.934187e-01 4.493191e-01 -2.986420e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.858640e-01 -1.675475e-01
    outer loop
      vertex 3.704696e-01 4.371302e-01 -3.703625e-01
      vertex 2.274639e-02 4.371302e-01 -3.703625e-01
      vertex 1.934187e-01 4.493191e-01 -2.986420e-01
    endloop
  endfacet
  facet normal -3.594462e-01 5.352419e-01 7.644047e-01
    outer loop
      vertex 2.274639e-02 4.371302e-01 -3.703625e-01
      vertex 2.274639e-02 4.006630e-01 -3.448279e-01
      vertex 1.934187e-01 4.493191e-01 -2.986420e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 2.308315e-02 3.726275e-01 -3.984437e-01
      vertex 3.759545e-01 4.096345e-01 -4.243563e-01
      vertex 3.759545e-01 3.726275e-01 -3.984437e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 2.308315e-02 3.726275e-01 -3.984437e-01
      vertex 2.308315e-02 4.096345e-01 -4.243563e-01
      vertex 3.759545e-01 4.096345e-01 -4.243563e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.861632e-01 -4.633732e-01
    outer loop
      vertex 2.274639e-02 4.006630e-01 -3.448279e-01
      vertex 3.704696e-01 4.006630e-01 -3.448279e-01
      vertex 3.759545e-01 3.726275e-01 -3.984437e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.861632e-01 -4.633732e-01
    outer loop
      vertex 2.274639e-02 4.006630e-01 -3.448279e-01
      vertex 3.759545e-01 3.726275e-01 -3.984437e-01
      vertex 2.308315e-02 3.726275e-01 -3.984437e-01
    endloop
  endfacet
  facet normal -9.958477e-01 -5.221523e-02 -7.457107e-02
    outer loop
      vertex 3.704696e-01 4.006630e-01 -3.448279e-01
      vertex 3.704696e-01 4.371302e-01 -3.703625e-01
      vertex 3.759545e-01 4.096345e-01 -4.243563e-01
    endloop
  endfacet
  facet normal -9.958477e-01 -5.221523e-02 -7.457107e-02
    outer loop
      vertex 3.704696e-01 4.006630e-01 -3.448279e-01
      vertex 3.759545e-01 4.096345e-01 -4.243563e-01
      vertex 3.759545e-01 3.726275e-01 -3.984437e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -8.911102e-01 4.537870e-01
    outer loop
      vertex 3.704696e-01 4.371302e-01 -3.703625e-01
      vertex 2.274639e-02 4.371302e-01 -3.703625e-01
      vertex 2.308315e-02 4.096345e-01 -4.243563e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -8.911102e-01 4.537870e-01
    outer loop
      vertex 3.704696e-01 4.371302e-01 -3.703625e-01
      vertex 2.308315e-02 4.096345e-01 -4.243563e-01
      vertex 3.759545e-01 4.096345e-01 -4.243563e-01
    endloop
  endfacet
  facet normal 9.999842e-01 3.219269e-03 4.597592e-03
    outer loop
      vertex 2.274639e-02 4.371302e-01 -3.703625e-01
      vertex 2.274639e-02 4.006630e-01 -3.448279e-01
      vertex 2.308315e-02 3.726275e-01 -3.984437e-01
    endloop
  endfacet
  facet normal 9.999842e-01 3.219269e-03 4.597592e-03
    outer loop
      vertex 2.274639e-02 4.371302e-01 -3.703625e-01
      vertex 2.308315e-02 3.726275e-01 -3.984437e-01
      vertex 2.308315e-02 4.096345e-01 -4.243563e-01
    endloop
  endfacet
  facet normal 3.881472e-01 5.286065e-01 7.549284e-01
    outer loop
      vertex 3.280846e-01 6.481375e-01 4.791255e-02
      vertex 3.280846e-01 6.922808e-01 1.700308e-02
      vertex 1.709027e-01 7.001661e-01 9.229702e-02
    endloop
  endfacet
  facet normal 0.000000e+00 9.945609e-01 -1.041565e-01
    outer loop
      vertex 3.280846e-01 6.922808e-01 1.700308e-02
      vertex 2.014400e-02 6.922808e-01 1.700308e-02
      vertex 1.709027e-01 7.001661e-01 9.229702e-02
    endloop
  endfacet
  facet normal -4.020573e-01 5.251749e-01 7.500275e-01
    outer loop
      vertex 2.014400e-02 6.922808e-01 1.700308e-02
      vertex 2.014400e-02 6.481375e-01 4.791255e-02
      vertex 1.709027e-01 7.001661e-01 9.229702e-02
    endloop
  endfacet
  facet normal 0.000000e+00 -6.490075e-01 7.607820e-01
    outer loop
      vertex 2.014400e-02 6.481375e-01 4.791255e-02
      vertex 3.280846e-01 6.481375e-01 4.791255e-02
      vertex 1.709027e-01 7.001661e-01 9.229702e-02
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 3.335695e-01 6.206173e-01 -6.064031e-03
      vertex 2.048076e-02 6.654986e-01 -3.749024e-02
      vertex 3.335695e-01 6.654986e-01 -3.749024e-02
    endloop
  endfacet
  facet normal -0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 3.335695e-01 6.206173e-01 -6.064031e-03
      vertex 2.048076e-02 6.206173e-01 -6.064031e-03
      vertex 2.048076e-02 6.654986e-01 -3.749024e-02
    endloop
  endfacet
  facet normal -9.958477e-01 -5.221523e-02 -7.457107e-02
    outer loop
      vertex 3.280846e-01 6.481375e-01 4.791255e-02
      vertex 3.280846e-01 6.922808e-01 1.700308e-02
      vertex 3.335695e-01 6.654986e-01 -3.749024e-02
    endloop
  endfacet
  facet normal -9.958477e-01 -5.221523e-02 -7.457107e-02
    outer loop
      vertex 3.280846e-01 6.481375e-01 4.791255e-02
      vertex 3.335695e-01 6.654986e-01 -3.749024e-02
      vertex 3.335695e-01 6.206173e-01 -6.064031e-03
    endloop
  endfacet
  facet normal 0.000000e+00 -8.974655e-01 4.410847e-01
    outer loop
      vertex 3.280846e-01 6.922808e-01 1.700308e-02
      vertex 2.014400e-02 6.922808e-01 1.700308e-02
      vertex 2.048076e-02 6.654986e-01 -3.749024e-02
    endloop
  endfacet
  facet normal 0.000000e+00 -8.974655e-01 4.410847e-01
    outer loop
      vertex 3.280846e-01 6.922808e-01 1.700308e-02
      vertex 2.048076e-02 6.654986e-01 -3.749024e-02
      vertex 3.335695e-01 6.654986e-01 -3.749024e-02
    endloop
  endfacet
  facet normal 9.999842e-01 3.219269e-03 4.597592e-03
    outer loop
      vertex 2.014400e-02 6.922808e-01 1.700308e-02
      vertex 2.014400e-02 6.481375e-01 4.791255e-02
      vertex 2.048076e-02 6.206173e-01 -6.064031e-03
    endloop
  endfacet
  facet normal 9.999842e-01 3.219269e-03 4.597592e-03
    outer loop
      vertex 2.014400e-02 6.922808e-01 1.700308e-02
      vertex 2.048076e-02 6.206173e-01 -6.064031e-03
      vertex 2.048076e-02 6.654986e-01 -3.749024e-02
    endloop
  endfacet
  facet normal 0.000000e+00 8.908876e-01 -4.542239e-01
    outer loop
      vertex 2.014400e-02 6.481375e-01 4.791255e-02
      vertex 3.280846e-01 6.481375e-01 4.791255e-02
      vertex 3.335695e-01 6.206173e-01 -6.064031e-03
    endloop
  endfacet
  facet normal 0.000000e+00 8.908876e-01 -4.542239e-01
    outer loop
      vertex 2.014400e-02 6.481375e-01 4.791255e-02
      vertex 3.335695e-01 6.206173e-01 -6.064031e-03
      vertex 2.048076e-02 6.206173e-01 -6.064031e-03
    endloop
  endfacet
  facet normal 3.644661e-01 4.056099e-01 8.382393e-01
    outer loop
      vertex 4.893950e-01 3.070065e-01 -6.211613e-01
      vertex 5.159087e-01 3.602975e-01 -6.584761e-01
      vertex 4.422733e-01 3.442318e-01 -6.186855e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.272706e-01 3.743919e-01
    outer loop
      vertex 5.159087e-01 3.602975e-01 -6.584761e-01
      vertex 3.866936e-01 3.602975e-01 -6.584761e-01
      vertex 4.422733e-01 3.442318e-01 -6.186855e-01
    endloop
  endfacet
  facet normal -3.877424e-01 5.287043e-01 7.550680e-01
    outer loop
      vertex 3.866936e-01 3.602975e-01 -6.584761e-01
      vertex 3.866936e-01 3.070065e-01 -6.211613e-01
      vertex 4.422733e-01 3.442318e-01 -6.186855e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -6.636279e-02 9.977956e-01
    outer loop
      vertex 3.866936e-01 3.070065e-01 -6.211613e-01
      vertex 4.893950e-01 3.070065e-01 -6.211613e-01
      vertex 4.422733e-01 3.442318e-01 -6.186855e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 4.961722e-01 2.794863e-01 -6.751379e-01
      vertex 3.920486e-01 3.335153e-01 -7.129694e-01
      vertex 5.230530e-01 3.335153e-01 -7.129694e-01
    endloop
  endfacet
  facet normal -0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 4.961722e-01 2.794863e-01 -6.751379e-01
      vertex 3.920486e-01 2.794863e-01 -6.751379e-01
      vertex 3.920486e-01 3.335153e-01 -7.129694e-01
    endloop
  endfacet
  facet normal -9.248131e-01 2.791536e-01 -2.584454e-01
    outer loop
      vertex 4.893950e-01 3.070065e-01 -6.211613e-01
      vertex 5.159087e-01 3.602975e-01 -6.584761e-01
      vertex 5.230530e-01 3.335153e-01 -7.129694e-01
    endloop
  endfacet
  facet normal -9.248131e-01 2.791536e-01 -2.584454e-01
    outer loop
      vertex 4.893950e-01 3.070065e-01 -6.211613e-01
      vertex 5.230530e-01 3.335153e-01 -7.129694e-01
      vertex 4.961722e-01 2.794863e-01 -6.751379e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -8.974655e-01 4.410847e-01
    outer loop
      vertex 5.159087e-01 3.602975e-01 -6.584761e-01
      vertex 3.866936e-01 3.602975e-01 -6.584761e-01
      vertex 3.920486e-01 3.335153e-01 -7.129694e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -8.974655e-01 4.410847e-01
    outer loop
      vertex 5.159087e-01 3.602975e-01 -6.584761e-01
      vertex 3.920486e-01 3.335153e-01 -7.129694e-01
      vertex 5.230530e-01 3.335153e-01 -7.129694e-01
    endloop
  endfacet
  facet normal 9.960409e-01 5.098865e-02 7.281933e-02
    outer loop
      vertex 3.866936e-01 3.602975e-01 -6.584761e-01
      vertex 3.866936e-01 3.070065e-01 -6.211613e-01
      vertex 3.920486e-01 2.794863e-01 -6.751379e-01
    endloop
  endfacet
  facet normal 9.960409e-01 5.098865e-02 7.281933e-02
    outer loop
      vertex 3.866936e-01 3.602975e-01 -6.584761e-01
      vertex 3.920486e-01 2.794863e-01 -6.751379e-01
      vertex 3.920486e-01 3.335153e-01 -7.129694e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.908876e-01 -4.542239e-01
    outer loop
      vertex 3.866936e-01 3.070065e-01 -6.211613e-01
      vertex 4.893950e-01 3.070065e-01 -6.211613e-01
      vertex 4.961722e-01 2.794863e-01 -6.751379e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.908876e-01 -4.542239e-01
    outer loop
      vertex 3.866936e-01 3.070065e-01 -6.211613e-01
      vertex 4.961722e-01 2.794863e-01 -6.751379e-01
      vertex 3.920486e-01 2.794863e-01 -6.751379e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -3.666770e-01 9.303483e-01
    outer loop
      vertex -4.400340e-01 6.481415e-01 -6.712299e-02
      vertex -2.358752e-01 6.481415e-01 -6.712299e-02
      vertex -3.371215e-01 6.998359e-01 -4.674874e-02
    endloop
  endfacet
  facet normal 4.161778e-01 5.215434e-01 7.448412e-01
    outer loop
      vertex -2.358752e-01 6.481415e-01 -6.712299e-02
      vertex -2.358752e-01 7.108976e-01 -1.110653e-01
      vertex -3.371215e-01 6.998359e-01 -4.674874e-02
    endloop
  endfacet
  facet normal 0.000000e+00 9.855302e-01 1.694999e-01
    outer loop
      vertex -2.358752e-01 7.108976e-01 -1.110653e-01
      vertex -4.538837e-01 7.108976e-01 -1.110653e-01
      vertex -3.371215e-01 6.998359e-01 -4.674874e-02
    endloop
  endfacet
  facet normal -3.919256e-01 4.680826e-01 7.920183e-01
    outer loop
      vertex -4.538837e-01 7.108976e-01 -1.110653e-01
      vertex -4.400340e-01 6.481415e-01 -6.712299e-02
      vertex -3.371215e-01 6.998359e-01 -4.674874e-02
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -4.472022e-01 6.213254e-01 -1.215926e-01
      vertex -2.397177e-01 6.851038e-01 -1.662507e-01
      vertex -2.397177e-01 6.213254e-01 -1.215926e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -4.472022e-01 6.213254e-01 -1.215926e-01
      vertex -4.612775e-01 6.851038e-01 -1.662507e-01
      vertex -2.397177e-01 6.851038e-01 -1.662507e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.971686e-01 -4.416883e-01
    outer loop
      vertex -4.400340e-01 6.481415e-01 -6.712299e-02
      vertex -2.358752e-01 6.481415e-01 -6.712299e-02
      vertex -2.397177e-01 6.213254e-01 -1.215926e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.971686e-01 -4.416883e-01
    outer loop
      vertex -4.400340e-01 6.481415e-01 -6.712299e-02
      vertex -2.397177e-01 6.213254e-01 -1.215926e-01
      vertex -4.472022e-01 6.213254e-01 -1.215926e-01
    endloop
  endfacet
  facet normal -9.979557e-01 3.665698e-02 5.235159e-02
    outer loop
      vertex -2.358752e-01 6.481415e-01 -6.712299e-02
      vertex -2.358752e-01 7.108976e-01 -1.110653e-01
      vertex -2.397177e-01 6.851038e-01 -1.662507e-01
    endloop
  endfacet
  facet normal -9.979557e-01 3.665698e-02 5.235159e-02
    outer loop
      vertex -2.358752e-01 6.481415e-01 -6.712299e-02
      vertex -2.397177e-01 6.851038e-01 -1.662507e-01
      vertex -2.397177e-01 6.213254e-01 -1.215926e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.059274e-01 4.234330e-01
    outer loop
      vertex -2.358752e-01 7.108976e-01 -1.110653e-01
      vertex -4.538837e-01 7.108976e-01 -1.110653e-01
      vertex -4.612775e-01 6.851038e-01 -1.662507e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.059274e-01 4.234330e-01
    outer loop
      vertex -2.358752e-01 7.108976e-01 -1.110653e-01
      vertex -4.612775e-01 6.851038e-01 -1.662507e-01
      vertex -2.397177e-01 6.851038e-01 -1.662507e-01
    endloop
  endfacet
  facet normal 9.800826e-01 9.368763e-02 -1.751023e-01
    outer loop
      vertex -4.538837e-01 7.108976e-01 -1.110653e-01
      vertex -4.400340e-01 6.481415e-01 -6.712299e-02
      vertex -4.472022e-01 6.213254e-01 -1.215926e-01
    endloop
  endfacet
  facet normal 9.800826e-01 9.368763e-02 -1.751023e-01
    outer loop
      vertex -4.538837e-01 7.108976e-01 -1.110653e-01
      vertex -4.472022e-01 6.213254e-01 -1.215926e-01
      vertex -4.612775e-01 6.851038e-01 -1.662507e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -3.123511e-01 9.499667e-01
    outer loop
      vertex -2.742148e-01 4.447468e-01 -4.802635e-01
      vertex 6.148430e-03 4.447468e-01 -4.802635e-01
      vertex -1.519600e-01 5.006671e-01 -4.618769e-01
    endloop
  endfacet
  facet normal 3.339571e-01 7.616363e-01 5.553222e-01
    outer loop
      vertex 6.148430e-03 4.447468e-01 -4.802635e-01
      vertex -7.256178e-02 5.152569e-01 -5.296352e-01
      vertex -1.519600e-01 5.006671e-01 -4.618769e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.775945e-01 2.104970e-01
    outer loop
      vertex -7.256178e-02 5.152569e-01 -5.296352e-01
      vertex -2.742148e-01 5.152569e-01 -5.296352e-01
      vertex -1.519600e-01 5.006671e-01 -4.618769e-01
    endloop
  endfacet
  facet normal -3.597431e-01 5.351763e-01 7.643110e-01
    outer loop
      vertex -2.742148e-01 5.152569e-01 -5.296352e-01
      vertex -2.742148e-01 4.447468e-01 -4.802635e-01
      vertex -1.519600e-01 5.006671e-01 -4.618769e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -2.781906e-01 4.179307e-01 -5.347332e-01
      vertex -7.361383e-02 4.894631e-01 -5.848207e-01
      vertex 6.237574e-03 4.179307e-01 -5.347332e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -2.781906e-01 4.179307e-01 -5.347332e-01
      vertex -2.781906e-01 4.894631e-01 -5.848207e-01
      vertex -7.361383e-02 4.894631e-01 -5.848207e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.971686e-01 -4.416883e-01
    outer loop
      vertex -2.742148e-01 4.447468e-01 -4.802635e-01
      vertex 6.148430e-03 4.447468e-01 -4.802635e-01
      vertex 6.237574e-03 4.179307e-01 -5.347332e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.971686e-01 -4.416883e-01
    outer loop
      vertex -2.742148e-01 4.447468e-01 -4.802635e-01
      vertex 6.237574e-03 4.179307e-01 -5.347332e-01
      vertex -2.781906e-01 4.179307e-01 -5.347332e-01
    endloop
  endfacet
  facet normal -7.339133e-01 -6.098708e-01 2.990466e-01
    outer loop
      vertex 6.148430e-03 4.447468e-01 -4.802635e-01
      vertex -7.256178e-02 5.152569e-01 -5.296352e-01
      vertex -7.361383e-02 4.894631e-01 -5.848207e-01
    endloop
  endfacet
  facet normal -7.339133e-01 -6.098708e-01 2.990466e-01
    outer loop
      vertex 6.148430e-03 4.447468e-01 -4.802635e-01
      vertex -7.361383e-02 4.894631e-01 -5.848207e-01
      vertex 6.237574e-03 4.179307e-01 -5.347332e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.059274e-01 4.234330e-01
    outer loop
      vertex -7.256178e-02 5.152569e-01 -5.296352e-01
      vertex -2.742148e-01 5.152569e-01 -5.296352e-01
      vertex -2.781906e-01 4.894631e-01 -5.848207e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.059274e-01 4.234330e-01
    outer loop
      vertex -7.256178e-02 5.152569e-01 -5.296352e-01
      vertex -2.781906e-01 4.894631e-01 -5.848207e-01
      vertex -7.361383e-02 4.894631e-01 -5.848207e-01
    endloop
  endfacet
  facet normal 9.978118e-01 -3.792343e-02 -5.416027e-02
    outer loop
      vertex -2.742148e-01 5.152569e-01 -5.296352e-01
      vertex -2.742148e-01 4.447468e-01 -4.802635e-01
      vertex -2.781906e-01 4.179307e-01 -5.347332e-01
    endloop
  endfacet
  facet normal 9.978118e-01 -3.792343e-02 -5.416027e-02
    outer loop
      vertex -2.742148e-01 5.152569e-01 -5.296352e-01
      vertex -2.781906e-01 4.179307e-01 -5.347332e-01
      vertex -2.781906e-01 4.894631e-01 -5.848207e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -4.590111e-01 8.884305e-01
    outer loop
      vertex 2.490858e-02 3.928330e-01 -5.858689e-01
      vertex 3.899586e-01 3.928330e-01 -5.858689e-01
      vertex 1.780710e-01 4.546014e-01 -5.539560e-01
    endloop
  endfacet
  facet normal 2.790384e-01 5.507940e-01 7.866153e-01
    outer loop
      vertex 3.899586e-01 3.928330e-01 -5.858689e-01
      vertex 3.899586e-01 4.653244e-01 -6.366279e-01
      vertex 1.780710e-01 4.546014e-01 -5.539560e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.916929e-01 1.286281e-01
    outer loop
      vertex 3.899586e-01 4.653244e-01 -6.366279e-01
      vertex 7.369447e-02 4.653244e-01 -6.366279e-01
      vertex 1.780710e-01 4.546014e-01 -5.539560e-01
    endloop
  endfacet
  facet normal -3.484358e-01 7.666135e-01 5.393480e-01
    outer loop
      vertex 7.369447e-02 4.653244e-01 -6.366279e-01
      vertex 2.490858e-02 4.216211e-01 -6.060265e-01
      vertex 1.780710e-01 4.546014e-01 -5.539560e-01
    endloop
  endfacet
  facet normal -3.729850e-01 5.321856e-01 7.600399e-01
    outer loop
      vertex 2.490858e-02 4.216211e-01 -6.060265e-01
      vertex 2.490858e-02 3.928330e-01 -5.858689e-01
      vertex 1.780710e-01 4.546014e-01 -5.539560e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 2.525985e-02 3.660177e-01 -6.403391e-01
      vertex 3.954579e-01 4.395313e-01 -6.918139e-01
      vertex 3.954579e-01 3.660177e-01 -6.403391e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 2.525985e-02 3.660177e-01 -6.403391e-01
      vertex 7.473374e-02 4.395313e-01 -6.918139e-01
      vertex 3.954579e-01 4.395313e-01 -6.918139e-01
    endloop
  endfacet
  facet normal 1.598741e-15 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 2.525985e-02 3.660177e-01 -6.403391e-01
      vertex 2.525985e-02 3.952117e-01 -6.607809e-01
      vertex 7.473374e-02 4.395313e-01 -6.918139e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.971757e-01 -4.416738e-01
    outer loop
      vertex 2.490858e-02 3.928330e-01 -5.858689e-01
      vertex 3.899586e-01 3.928330e-01 -5.858689e-01
      vertex 3.954579e-01 3.660177e-01 -6.403391e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.971757e-01 -4.416738e-01
    outer loop
      vertex 2.490858e-02 3.928330e-01 -5.858689e-01
      vertex 3.954579e-01 3.660177e-01 -6.403391e-01
      vertex 2.525985e-02 3.660177e-01 -6.403391e-01
    endloop
  endfacet
  facet normal -9.958259e-01 -5.235219e-02 -7.476668e-02
    outer loop
      vertex 3.899586e-01 3.928330e-01 -5.858689e-01
      vertex 3.899586e-01 4.653244e-01 -6.366279e-01
      vertex 3.954579e-01 4.395313e-01 -6.918139e-01
    endloop
  endfacet
  facet normal -9.958259e-01 -5.235219e-02 -7.476668e-02
    outer loop
      vertex 3.899586e-01 3.928330e-01 -5.858689e-01
      vertex 3.954579e-01 4.395313e-01 -6.918139e-01
      vertex 3.954579e-01 3.660177e-01 -6.403391e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.059342e-01 4.234185e-01
    outer loop
      vertex 3.899586e-01 4.653244e-01 -6.366279e-01
      vertex 7.369447e-02 4.653244e-01 -6.366279e-01
      vertex 7.473374e-02 4.395313e-01 -6.918139e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.059342e-01 4.234185e-01
    outer loop
      vertex 3.899586e-01 4.653244e-01 -6.366279e-01
      vertex 7.473374e-02 4.395313e-01 -6.918139e-01
      vertex 3.954579e-01 4.395313e-01 -6.918139e-01
    endloop
  endfacet
  facet normal 7.339004e-01 -6.099561e-01 2.989042e-01
    outer loop
      vertex 7.369447e-02 4.653244e-01 -6.366279e-01
      vertex 2.490858e-02 4.216211e-01 -6.060265e-01
      vertex 2.525985e-02 3.952117e-01 -6.607809e-01
    endloop
  endfacet
  facet normal 7.339004e-01 -6.099561e-01 2.989042e-01
    outer loop
      vertex 7.369447e-02 4.653244e-01 -6.366279e-01
      vertex 2.525985e-02 3.952117e-01 -6.607809e-01
      vertex 7.473374e-02 4.395313e-01 -6.918139e-01
    endloop
  endfacet
  facet normal 9.999829e-01 3.357953e-03 4.795654e-03
    outer loop
      vertex 2.490858e-02 4.216211e-01 -6.060265e-01
      vertex 2.490858e-02 3.928330e-01 -5.858689e-01
      vertex 2.525985e-02 3.660177e-01 -6.403391e-01
    endloop
  endfacet
  facet normal 9.999829e-01 3.357953e-03 4.795654e-03
    outer loop
      vertex 2.490858e-02 4.216211e-01 -6.060265e-01
      vertex 2.525985e-02 3.660177e-01 -6.403391e-01
      vertex 2.525985e-02 3.952117e-01 -6.607809e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -1.725354e-02 9.998511e-01
    outer loop
      vertex 3.812031e-01 3.833139e-01 -6.050477e-01
      vertex 5.087192e-01 3.833139e-01 -6.050477e-01
      vertex 4.459524e-01 4.323833e-01 -6.042009e-01
    endloop
  endfacet
  facet normal 3.802724e-01 4.727058e-01 7.949479e-01
    outer loop
      vertex 5.087192e-01 3.833139e-01 -6.050477e-01
      vertex 5.247970e-01 4.561660e-01 -6.560592e-01
      vertex 4.459524e-01 4.323833e-01 -6.042009e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.089698e-01 4.168619e-01
    outer loop
      vertex 5.247970e-01 4.561660e-01 -6.560592e-01
      vertex 3.812031e-01 4.561660e-01 -6.560592e-01
      vertex 4.459524e-01 4.323833e-01 -6.042009e-01
    endloop
  endfacet
  facet normal -4.068592e-01 5.239568e-01 7.482879e-01
    outer loop
      vertex 3.812031e-01 4.561660e-01 -6.560592e-01
      vertex 3.812031e-01 3.833139e-01 -6.050477e-01
      vertex 4.459524e-01 4.323833e-01 -6.042009e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 3.865524e-01 3.564978e-01 -6.595173e-01
      vertex 5.321613e-01 4.303721e-01 -7.112447e-01
      vertex 5.158579e-01 3.564978e-01 -6.595173e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 3.865524e-01 3.564978e-01 -6.595173e-01
      vertex 3.865524e-01 4.303721e-01 -7.112447e-01
      vertex 5.321613e-01 4.303721e-01 -7.112447e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.971686e-01 -4.416883e-01
    outer loop
      vertex 3.812031e-01 3.833139e-01 -6.050477e-01
      vertex 5.087192e-01 3.833139e-01 -6.050477e-01
      vertex 5.158579e-01 3.564978e-01 -6.595173e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.971686e-01 -4.416883e-01
    outer loop
      vertex 3.812031e-01 3.833139e-01 -6.050477e-01
      vertex 5.158579e-01 3.564978e-01 -6.595173e-01
      vertex 3.865524e-01 3.564978e-01 -6.595173e-01
    endloop
  endfacet
  facet normal -9.801249e-01 9.396851e-02 -1.747145e-01
    outer loop
      vertex 5.087192e-01 3.833139e-01 -6.050477e-01
      vertex 5.247970e-01 4.561660e-01 -6.560592e-01
      vertex 5.321613e-01 4.303721e-01 -7.112447e-01
    endloop
  endfacet
  facet normal -9.801249e-01 9.396851e-02 -1.747145e-01
    outer loop
      vertex 5.087192e-01 3.833139e-01 -6.050477e-01
      vertex 5.321613e-01 4.303721e-01 -7.112447e-01
      vertex 5.158579e-01 3.564978e-01 -6.595173e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.059274e-01 4.234330e-01
    outer loop
      vertex 5.247970e-01 4.561660e-01 -6.560592e-01
      vertex 3.812031e-01 4.561660e-01 -6.560592e-01
      vertex 3.865524e-01 4.303721e-01 -7.112447e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.059274e-01 4.234330e-01
    outer loop
      vertex 5.247970e-01 4.561660e-01 -6.560592e-01
      vertex 3.865524e-01 4.303721e-01 -7.112447e-01
      vertex 5.321613e-01 4.303721e-01 -7.112447e-01
    endloop
  endfacet
  facet normal 9.960493e-01 5.093480e-02 7.274244e-02
    outer loop
      vertex 3.812031e-01 4.561660e-01 -6.560592e-01
      vertex 3.812031e-01 3.833139e-01 -6.050477e-01
      vertex 3.865524e-01 3.564978e-01 -6.595173e-01
    endloop
  endfacet
  facet normal 9.960493e-01 5.093480e-02 7.274244e-02
    outer loop
      vertex 3.812031e-01 4.561660e-01 -6.560592e-01
      vertex 3.865524e-01 3.564978e-01 -6.595173e-01
      vertex 3.865524e-01 4.303721e-01 -7.112447e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -2.737960e-01 9.617878e-01
    outer loop
      vertex -5.079649e-01 5.188766e-01 -5.137385e-01
      vertex -2.639136e-01 5.188766e-01 -5.137385e-01
      vertex -3.811545e-01 5.787200e-01 -4.967026e-01
    endloop
  endfacet
  facet normal 3.807773e-01 5.303671e-01 7.574427e-01
    outer loop
      vertex -2.639136e-01 5.188766e-01 -5.137385e-01
      vertex -2.639136e-01 5.979110e-01 -5.690790e-01
      vertex -3.811545e-01 5.787200e-01 -4.967026e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.665977e-01 2.562985e-01
    outer loop
      vertex -2.639136e-01 5.979110e-01 -5.690790e-01
      vertex -5.068898e-01 5.979110e-01 -5.690790e-01
      vertex -3.811545e-01 5.787200e-01 -4.967026e-01
    endloop
  endfacet
  facet normal -3.568811e-01 5.390590e-01 7.629229e-01
    outer loop
      vertex -5.068898e-01 5.979110e-01 -5.690790e-01
      vertex -5.079649e-01 5.188766e-01 -5.137385e-01
      vertex -3.811545e-01 5.787200e-01 -4.967026e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -5.153566e-01 4.930410e-01 -5.688947e-01
      vertex -2.677540e-01 5.732255e-01 -6.250405e-01
      vertex -2.677540e-01 4.930410e-01 -5.688947e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -5.153566e-01 4.930410e-01 -5.688947e-01
      vertex -5.142659e-01 5.732255e-01 -6.250405e-01
      vertex -2.677540e-01 5.732255e-01 -6.250405e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.055779e-01 -4.241800e-01
    outer loop
      vertex -5.079649e-01 5.188766e-01 -5.137385e-01
      vertex -2.639136e-01 5.188766e-01 -5.137385e-01
      vertex -2.677540e-01 4.930410e-01 -5.688947e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.055779e-01 -4.241800e-01
    outer loop
      vertex -5.079649e-01 5.188766e-01 -5.137385e-01
      vertex -2.677540e-01 4.930410e-01 -5.688947e-01
      vertex -5.153566e-01 4.930410e-01 -5.688947e-01
    endloop
  endfacet
  facet normal -9.979578e-01 3.663779e-02 5.232419e-02
    outer loop
      vertex -2.639136e-01 5.188766e-01 -5.137385e-01
      vertex -2.639136e-01 5.979110e-01 -5.690790e-01
      vertex -2.677540e-01 5.732255e-01 -6.250405e-01
    endloop
  endfacet
  facet normal -9.979578e-01 3.663779e-02 5.232419e-02
    outer loop
      vertex -2.639136e-01 5.188766e-01 -5.137385e-01
      vertex -2.677540e-01 5.732255e-01 -6.250405e-01
      vertex -2.677540e-01 4.930410e-01 -5.688947e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.149382e-01 4.035940e-01
    outer loop
      vertex -2.639136e-01 5.979110e-01 -5.690790e-01
      vertex -5.068898e-01 5.979110e-01 -5.690790e-01
      vertex -5.142659e-01 5.732255e-01 -6.250405e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.149382e-01 4.035940e-01
    outer loop
      vertex -2.639136e-01 5.979110e-01 -5.690790e-01
      vertex -5.142659e-01 5.732255e-01 -6.250405e-01
      vertex -2.677540e-01 5.732255e-01 -6.250405e-01
    endloop
  endfacet
  facet normal 9.922000e-01 -8.027470e-02 -9.536877e-02
    outer loop
      vertex -5.068898e-01 5.979110e-01 -5.690790e-01
      vertex -5.079649e-01 5.188766e-01 -5.137385e-01
      vertex -5.153566e-01 4.930410e-01 -5.688947e-01
    endloop
  endfacet
  facet normal 9.922000e-01 -8.027470e-02 -9.536877e-02
    outer loop
      vertex -5.068898e-01 5.979110e-01 -5.690790e-01
      vertex -5.153566e-01 4.930410e-01 -5.688947e-01
      vertex -5.142659e-01 5.732255e-01 -6.250405e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -1.954494e-01 9.807138e-01
    outer loop
      vertex -2.452979e-01 6.937473e-01 -1.404086e-01
      vertex -6.416990e-02 6.937473e-01 -1.404086e-01
      vertex -1.615510e-01 7.453935e-01 -1.301159e-01
    endloop
  endfacet
  facet normal 4.106782e-01 6.461447e-01 6.433043e-01
    outer loop
      vertex -6.416990e-02 6.937473e-01 -1.404086e-01
      vertex -9.812223e-02 7.649973e-01 -1.902984e-01
      vertex -1.615510e-01 7.453935e-01 -1.301159e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.508276e-01 3.097208e-01
    outer loop
      vertex -9.812223e-02 7.649973e-01 -1.902984e-01
      vertex -2.452979e-01 7.649973e-01 -1.902984e-01
      vertex -1.615510e-01 7.453935e-01 -1.301159e-01
    endloop
  endfacet
  facet normal -4.136910e-01 5.221939e-01 7.457702e-01
    outer loop
      vertex -2.452979e-01 7.649973e-01 -1.902984e-01
      vertex -2.452979e-01 6.937473e-01 -1.404086e-01
      vertex -1.615510e-01 7.453935e-01 -1.301159e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -2.492574e-01 6.679117e-01 -1.955648e-01
      vertex -9.970608e-02 7.403117e-01 -2.462599e-01
      vertex -6.520570e-02 6.679117e-01 -1.955648e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -2.492574e-01 6.679117e-01 -1.955648e-01
      vertex -2.492574e-01 7.403117e-01 -2.462599e-01
      vertex -9.970608e-02 7.403117e-01 -2.462599e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.055779e-01 -4.241800e-01
    outer loop
      vertex -2.452979e-01 6.937473e-01 -1.404086e-01
      vertex -6.416990e-02 6.937473e-01 -1.404086e-01
      vertex -6.520570e-02 6.679117e-01 -1.955648e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.055779e-01 -4.241800e-01
    outer loop
      vertex -2.452979e-01 6.937473e-01 -1.404086e-01
      vertex -6.520570e-02 6.679117e-01 -1.955648e-01
      vertex -2.492574e-01 6.679117e-01 -1.955648e-01
    endloop
  endfacet
  facet normal -9.305012e-01 -3.246810e-01 1.695576e-01
    outer loop
      vertex -6.416990e-02 6.937473e-01 -1.404086e-01
      vertex -9.812223e-02 7.649973e-01 -1.902984e-01
      vertex -9.970608e-02 7.403117e-01 -2.462599e-01
    endloop
  endfacet
  facet normal -9.305012e-01 -3.246810e-01 1.695576e-01
    outer loop
      vertex -6.416990e-02 6.937473e-01 -1.404086e-01
      vertex -9.970608e-02 7.403117e-01 -2.462599e-01
      vertex -6.520570e-02 6.679117e-01 -1.955648e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.149382e-01 4.035940e-01
    outer loop
      vertex -9.812223e-02 7.649973e-01 -1.902984e-01
      vertex -2.452979e-01 7.649973e-01 -1.902984e-01
      vertex -2.492574e-01 7.403117e-01 -2.462599e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.149382e-01 4.035940e-01
    outer loop
      vertex -9.812223e-02 7.649973e-01 -1.902984e-01
      vertex -2.492574e-01 7.403117e-01 -2.462599e-01
      vertex -9.970608e-02 7.403117e-01 -2.462599e-01
    endloop
  endfacet
  facet normal 9.978296e-01 -3.776917e-02 -5.393996e-02
    outer loop
      vertex -2.452979e-01 7.649973e-01 -1.902984e-01
      vertex -2.452979e-01 6.937473e-01 -1.404086e-01
      vertex -2.492574e-01 6.679117e-01 -1.955648e-01
    endloop
  endfacet
  facet normal 9.978296e-01 -3.776917e-02 -5.393996e-02
    outer loop
      vertex -2.452979e-01 7.649973e-01 -1.902984e-01
      vertex -2.492574e-01 6.679117e-01 -1.955648e-01
      vertex -2.492574e-01 7.403117e-01 -2.462599e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -3.438080e-01 9.390400e-01
    outer loop
      vertex 7.086452e-02 4.748681e-01 -6.076919e-01
      vertex 3.849598e-01 4.748681e-01 -6.076919e-01
      vertex 2.344155e-01 5.389196e-01 -5.842408e-01
    endloop
  endfacet
  facet normal 3.483613e-01 5.376478e-01 7.678406e-01
    outer loop
      vertex 3.849598e-01 4.748681e-01 -6.076919e-01
      vertex 3.849598e-01 5.558616e-01 -6.644041e-01
      vertex 2.344155e-01 5.389196e-01 -5.842408e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.783884e-01 2.067756e-01
    outer loop
      vertex 3.849598e-01 5.558616e-01 -6.644041e-01
      vertex 1.094599e-01 5.558616e-01 -6.644041e-01
      vertex 2.344155e-01 5.389196e-01 -5.842408e-01
    endloop
  endfacet
  facet normal -3.496349e-01 6.434402e-01 6.809847e-01
    outer loop
      vertex 1.094599e-01 5.558616e-01 -6.644041e-01
      vertex 7.086452e-02 4.748681e-01 -6.076919e-01
      vertex 2.344155e-01 5.389196e-01 -5.842408e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 7.187078e-02 4.490325e-01 -6.628480e-01
      vertex 3.904261e-01 5.311760e-01 -7.203656e-01
      vertex 3.904261e-01 4.490325e-01 -6.628480e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 7.187078e-02 4.490325e-01 -6.628480e-01
      vertex 1.110142e-01 5.311760e-01 -7.203656e-01
      vertex 3.904261e-01 5.311760e-01 -7.203656e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.055779e-01 -4.241800e-01
    outer loop
      vertex 7.086452e-02 4.748681e-01 -6.076919e-01
      vertex 3.849598e-01 4.748681e-01 -6.076919e-01
      vertex 3.904261e-01 4.490325e-01 -6.628480e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.055779e-01 -4.241800e-01
    outer loop
      vertex 7.086452e-02 4.748681e-01 -6.076919e-01
      vertex 3.904261e-01 4.490325e-01 -6.628480e-01
      vertex 7.187078e-02 4.490325e-01 -6.628480e-01
    endloop
  endfacet
  facet normal -9.958755e-01 -5.204056e-02 -7.432162e-02
    outer loop
      vertex 3.849598e-01 4.748681e-01 -6.076919e-01
      vertex 3.849598e-01 5.558616e-01 -6.644041e-01
      vertex 3.904261e-01 5.311760e-01 -7.203656e-01
    endloop
  endfacet
  facet normal -9.958755e-01 -5.204056e-02 -7.432162e-02
    outer loop
      vertex 3.849598e-01 4.748681e-01 -6.076919e-01
      vertex 3.904261e-01 5.311760e-01 -7.203656e-01
      vertex 3.904261e-01 4.490325e-01 -6.628480e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.149382e-01 4.035940e-01
    outer loop
      vertex 3.849598e-01 5.558616e-01 -6.644041e-01
      vertex 1.094599e-01 5.558616e-01 -6.644041e-01
      vertex 1.110142e-01 5.311760e-01 -7.203656e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.149382e-01 4.035940e-01
    outer loop
      vertex 3.849598e-01 5.558616e-01 -6.644041e-01
      vertex 1.110142e-01 5.311760e-01 -7.203656e-01
      vertex 3.904261e-01 5.311760e-01 -7.203656e-01
    endloop
  endfacet
  facet normal 9.304809e-01 -3.249367e-01 1.691785e-01
    outer loop
      vertex 1.094599e-01 5.558616e-01 -6.644041e-01
      vertex 7.086452e-02 4.748681e-01 -6.076919e-01
      vertex 7.187078e-02 4.490325e-01 -6.628480e-01
    endloop
  endfacet
  facet normal 9.304809e-01 -3.249367e-01 1.691785e-01
    outer loop
      vertex 1.094599e-01 5.558616e-01 -6.644041e-01
      vertex 7.187078e-02 4.490325e-01 -6.628480e-01
      vertex 1.110142e-01 5.311760e-01 -7.203656e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -4.997698e-02 9.987504e-01
    outer loop
      vertex 3.479913e-01 6.129590e-01 -3.128829e-01
      vertex 4.791243e-01 6.129590e-01 -3.128829e-01
      vertex 4.100192e-01 6.634447e-01 -3.103566e-01
    endloop
  endfacet
  facet normal 4.117906e-01 5.264399e-01 7.438343e-01
    outer loop
      vertex 4.791243e-01 6.129590e-01 -3.128829e-01
      vertex 4.781062e-01 6.878052e-01 -3.652909e-01
      vertex 4.100192e-01 6.634447e-01 -3.103566e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.141488e-01 4.053789e-01
    outer loop
      vertex 4.781062e-01 6.878052e-01 -3.652909e-01
      vertex 3.479913e-01 6.878052e-01 -3.652909e-01
      vertex 4.100192e-01 6.634447e-01 -3.103566e-01
    endloop
  endfacet
  facet normal -4.473624e-01 5.129797e-01 7.326109e-01
    outer loop
      vertex 3.479913e-01 6.878052e-01 -3.652909e-01
      vertex 3.479913e-01 6.129590e-01 -3.128829e-01
      vertex 4.100192e-01 6.634447e-01 -3.103566e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 3.533386e-01 5.871234e-01 -3.680391e-01
      vertex 4.854528e-01 6.631197e-01 -4.212523e-01
      vertex 4.864866e-01 5.871234e-01 -3.680391e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 3.533386e-01 5.871234e-01 -3.680391e-01
      vertex 3.533386e-01 6.631197e-01 -4.212523e-01
      vertex 4.854528e-01 6.631197e-01 -4.212523e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.055779e-01 -4.241800e-01
    outer loop
      vertex 3.479913e-01 6.129590e-01 -3.128829e-01
      vertex 4.791243e-01 6.129590e-01 -3.128829e-01
      vertex 4.864866e-01 5.871234e-01 -3.680391e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.055779e-01 -4.241800e-01
    outer loop
      vertex 3.479913e-01 6.129590e-01 -3.128829e-01
      vertex 4.864866e-01 5.871234e-01 -3.680391e-01
      vertex 3.533386e-01 5.871234e-01 -3.680391e-01
    endloop
  endfacet
  facet normal -9.922600e-01 -7.999930e-02 -9.497429e-02
    outer loop
      vertex 4.791243e-01 6.129590e-01 -3.128829e-01
      vertex 4.781062e-01 6.878052e-01 -3.652909e-01
      vertex 4.854528e-01 6.631197e-01 -4.212523e-01
    endloop
  endfacet
  facet normal -9.922600e-01 -7.999930e-02 -9.497429e-02
    outer loop
      vertex 4.791243e-01 6.129590e-01 -3.128829e-01
      vertex 4.854528e-01 6.631197e-01 -4.212523e-01
      vertex 4.864866e-01 5.871234e-01 -3.680391e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.149382e-01 4.035940e-01
    outer loop
      vertex 4.781062e-01 6.878052e-01 -3.652909e-01
      vertex 3.479913e-01 6.878052e-01 -3.652909e-01
      vertex 3.533386e-01 6.631197e-01 -4.212523e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.149382e-01 4.035940e-01
    outer loop
      vertex 4.781062e-01 6.878052e-01 -3.652909e-01
      vertex 3.533386e-01 6.631197e-01 -4.212523e-01
      vertex 4.854528e-01 6.631197e-01 -4.212523e-01
    endloop
  endfacet
  facet normal 9.960523e-01 5.091573e-02 7.271520e-02
    outer loop
      vertex 3.479913e-01 6.878052e-01 -3.652909e-01
      vertex 3.479913e-01 6.129590e-01 -3.128829e-01
      vertex 3.533386e-01 5.871234e-01 -3.680391e-01
    endloop
  endfacet
  facet normal 9.960523e-01 5.091573e-02 7.271520e-02
    outer loop
      vertex 3.479913e-01 6.878052e-01 -3.652909e-01
      vertex 3.533386e-01 5.871234e-01 -3.680391e-01
      vertex 3.533386e-01 6.631197e-01 -4.212523e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -3.027576e-01 9.530676e-01
    outer loop
      vertex -4.745898e-01 7.038245e-01 -3.205343e-01
      vertex -2.471911e-01 7.038245e-01 -3.205343e-01
      vertex -3.517264e-01 7.594949e-01 -3.028497e-01
    endloop
  endfacet
  facet normal 4.058287e-01 5.242197e-01 7.486633e-01
    outer loop
      vertex -2.471911e-01 7.038245e-01 -3.205343e-01
      vertex -2.471911e-01 7.777919e-01 -3.723269e-01
      vertex -3.517264e-01 7.594949e-01 -3.028497e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.670283e-01 2.546688e-01
    outer loop
      vertex -2.471911e-01 7.777919e-01 -3.723269e-01
      vertex -4.550629e-01 7.777919e-01 -3.723269e-01
      vertex -3.517264e-01 7.594949e-01 -3.028497e-01
    endloop
  endfacet
  facet normal -3.725315e-01 5.962718e-01 7.111120e-01
    outer loop
      vertex -4.550629e-01 7.777919e-01 -3.723269e-01
      vertex -4.745898e-01 7.038245e-01 -3.205343e-01
      vertex -3.517264e-01 7.594949e-01 -3.028497e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -4.819690e-01 6.790947e-01 -3.764648e-01
      vertex -2.510346e-01 7.542122e-01 -4.290627e-01
      vertex -2.510346e-01 6.790947e-01 -3.764648e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -4.819690e-01 6.790947e-01 -3.764648e-01
      vertex -4.621384e-01 7.542122e-01 -4.290627e-01
      vertex -2.510346e-01 7.542122e-01 -4.290627e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.145882e-01 -4.043864e-01
    outer loop
      vertex -4.745898e-01 7.038245e-01 -3.205343e-01
      vertex -2.471911e-01 7.038245e-01 -3.205343e-01
      vertex -2.510346e-01 6.790947e-01 -3.764648e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.145882e-01 -4.043864e-01
    outer loop
      vertex -4.745898e-01 7.038245e-01 -3.205343e-01
      vertex -2.510346e-01 6.790947e-01 -3.764648e-01
      vertex -4.819690e-01 6.790947e-01 -3.764648e-01
    endloop
  endfacet
  facet normal -9.979546e-01 3.666696e-02 5.236585e-02
    outer loop
      vertex -2.471911e-01 7.038245e-01 -3.205343e-01
      vertex -2.471911e-01 7.777919e-01 -3.723269e-01
      vertex -2.510346e-01 7.542122e-01 -4.290627e-01
    endloop
  endfacet
  facet normal -9.979546e-01 3.666696e-02 5.236585e-02
    outer loop
      vertex -2.471911e-01 7.038245e-01 -3.205343e-01
      vertex -2.510346e-01 7.542122e-01 -4.290627e-01
      vertex -2.510346e-01 6.790947e-01 -3.764648e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.234248e-01 3.837795e-01
    outer loop
      vertex -2.471911e-01 7.777919e-01 -3.723269e-01
      vertex -4.550629e-01 7.777919e-01 -3.723269e-01
      vertex -4.621384e-01 7.542122e-01 -4.290627e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.234248e-01 3.837795e-01
    outer loop
      vertex -2.471911e-01 7.777919e-01 -3.723269e-01
      vertex -4.621384e-01 7.542122e-01 -4.290627e-01
      vertex -2.510346e-01 7.542122e-01 -4.290627e-01
    endloop
  endfacet
  facet normal 9.648504e-01 -2.625607e-01 -1.120617e-02
    outer loop
      vertex -4.550629e-01 7.777919e-01 -3.723269e-01
      vertex -4.745898e-01 7.038245e-01 -3.205343e-01
      vertex -4.819690e-01 6.790947e-01 -3.764648e-01
    endloop
  endfacet
  facet normal 9.648504e-01 -2.625607e-01 -1.120617e-02
    outer loop
      vertex -4.550629e-01 7.777919e-01 -3.723269e-01
      vertex -4.819690e-01 6.790947e-01 -3.764648e-01
      vertex -4.621384e-01 7.542122e-01 -4.290627e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -6.410431e-02 9.979432e-01
    outer loop
      vertex -2.680815e-01 6.159462e-01 -5.192860e-01
      vertex -1.068505e-01 6.159462e-01 -5.192860e-01
      vertex -1.933059e-01 6.681280e-01 -5.159340e-01
    endloop
  endfacet
  facet normal 4.018312e-01 6.226259e-01 6.714676e-01
    outer loop
      vertex -1.068505e-01 6.159462e-01 -5.192860e-01
      vertex -1.364652e-01 6.940005e-01 -5.739402e-01
      vertex -1.933059e-01 6.681280e-01 -5.159340e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.132734e-01 4.073471e-01
    outer loop
      vertex -1.364652e-01 6.940005e-01 -5.739402e-01
      vertex -2.680815e-01 6.940005e-01 -5.739402e-01
      vertex -1.933059e-01 6.681280e-01 -5.159340e-01
    endloop
  endfacet
  facet normal -4.004253e-01 5.255849e-01 7.506131e-01
    outer loop
      vertex -2.680815e-01 6.940005e-01 -5.739402e-01
      vertex -2.680815e-01 6.159462e-01 -5.192860e-01
      vertex -1.933059e-01 6.681280e-01 -5.159340e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -2.720315e-01 5.912164e-01 -5.752165e-01
      vertex -1.384759e-01 6.704208e-01 -6.306760e-01
      vertex -1.084249e-01 5.912164e-01 -5.752165e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -2.720315e-01 5.912164e-01 -5.752165e-01
      vertex -2.720315e-01 6.704208e-01 -6.306760e-01
      vertex -1.384759e-01 6.704208e-01 -6.306760e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.145882e-01 -4.043864e-01
    outer loop
      vertex -2.680815e-01 6.159462e-01 -5.192860e-01
      vertex -1.068505e-01 6.159462e-01 -5.192860e-01
      vertex -1.084249e-01 5.912164e-01 -5.752165e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.145882e-01 -4.043864e-01
    outer loop
      vertex -2.680815e-01 6.159462e-01 -5.192860e-01
      vertex -1.084249e-01 5.912164e-01 -5.752165e-01
      vertex -2.720315e-01 5.912164e-01 -5.752165e-01
    endloop
  endfacet
  facet normal -9.544093e-01 -2.621430e-01 1.427725e-01
    outer loop
      vertex -1.068505e-01 6.159462e-01 -5.192860e-01
      vertex -1.364652e-01 6.940005e-01 -5.739402e-01
      vertex -1.384759e-01 6.704208e-01 -6.306760e-01
    endloop
  endfacet
  facet normal -9.544093e-01 -2.621430e-01 1.427725e-01
    outer loop
      vertex -1.068505e-01 6.159462e-01 -5.192860e-01
      vertex -1.384759e-01 6.704208e-01 -6.306760e-01
      vertex -1.084249e-01 5.912164e-01 -5.752165e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.234248e-01 3.837795e-01
    outer loop
      vertex -1.364652e-01 6.940005e-01 -5.739402e-01
      vertex -2.680815e-01 6.940005e-01 -5.739402e-01
      vertex -2.720315e-01 6.704208e-01 -6.306760e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.234248e-01 3.837795e-01
    outer loop
      vertex -1.364652e-01 6.940005e-01 -5.739402e-01
      vertex -2.720315e-01 6.704208e-01 -6.306760e-01
      vertex -1.384759e-01 6.704208e-01 -6.306760e-01
    endloop
  endfacet
  facet normal 9.978400e-01 -3.767927e-02 -5.381157e-02
    outer loop
      vertex -2.680815e-01 6.940005e-01 -5.739402e-01
      vertex -2.680815e-01 6.159462e-01 -5.192860e-01
      vertex -2.720315e-01 5.912164e-01 -5.752165e-01
    endloop
  endfacet
  facet normal 9.978400e-01 -3.767927e-02 -5.381157e-02
    outer loop
      vertex -2.680815e-01 6.940005e-01 -5.739402e-01
      vertex -2.720315e-01 5.912164e-01 -5.752165e-01
      vertex -2.720315e-01 6.704208e-01 -6.306760e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -3.359102e-01 9.418940e-01
    outer loop
      vertex 1.012335e-01 6.737633e-01 -3.885227e-01
      vertex 3.575895e-01 6.737633e-01 -3.885227e-01
      vertex 2.335474e-01 7.316048e-01 -3.678946e-01
    endloop
  endfacet
  facet normal 3.743356e-01 5.318736e-01 7.595942e-01
    outer loop
      vertex 3.575895e-01 6.737633e-01 -3.885227e-01
      vertex 3.575895e-01 7.491287e-01 -4.412942e-01
      vertex 2.335474e-01 7.316048e-01 -3.678946e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.726631e-01 2.322207e-01
    outer loop
      vertex 3.575895e-01 7.491287e-01 -4.412942e-01
      vertex 1.298280e-01 7.491287e-01 -4.412942e-01
      vertex 2.335474e-01 7.316048e-01 -3.678946e-01
    endloop
  endfacet
  facet normal -3.790133e-01 6.229573e-01 6.843048e-01
    outer loop
      vertex 1.298280e-01 7.491287e-01 -4.412942e-01
      vertex 1.012335e-01 6.737633e-01 -3.885227e-01
      vertex 2.335474e-01 7.316048e-01 -3.678946e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 1.027784e-01 6.490335e-01 -4.444532e-01
      vertex 3.630464e-01 7.255491e-01 -4.980300e-01
      vertex 3.630464e-01 6.490335e-01 -4.444532e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 1.027784e-01 6.490335e-01 -4.444532e-01
      vertex 1.318092e-01 7.255491e-01 -4.980300e-01
      vertex 3.630464e-01 7.255491e-01 -4.980300e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.145882e-01 -4.043864e-01
    outer loop
      vertex 1.012335e-01 6.737633e-01 -3.885227e-01
      vertex 3.575895e-01 6.737633e-01 -3.885227e-01
      vertex 3.630464e-01 6.490335e-01 -4.444532e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.145882e-01 -4.043864e-01
    outer loop
      vertex 1.012335e-01 6.737633e-01 -3.885227e-01
      vertex 3.630464e-01 6.490335e-01 -4.444532e-01
      vertex 1.027784e-01 6.490335e-01 -4.444532e-01
    endloop
  endfacet
  facet normal -9.958897e-01 -5.195118e-02 -7.419398e-02
    outer loop
      vertex 3.575895e-01 6.737633e-01 -3.885227e-01
      vertex 3.575895e-01 7.491287e-01 -4.412942e-01
      vertex 3.630464e-01 7.255491e-01 -4.980300e-01
    endloop
  endfacet
  facet normal -9.958897e-01 -5.195118e-02 -7.419398e-02
    outer loop
      vertex 3.575895e-01 6.737633e-01 -3.885227e-01
      vertex 3.630464e-01 7.255491e-01 -4.980300e-01
      vertex 3.630464e-01 6.490335e-01 -4.444532e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.234248e-01 3.837795e-01
    outer loop
      vertex 3.575895e-01 7.491287e-01 -4.412942e-01
      vertex 1.298280e-01 7.491287e-01 -4.412942e-01
      vertex 1.318092e-01 7.255491e-01 -4.980300e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.234248e-01 3.837795e-01
    outer loop
      vertex 3.575895e-01 7.491287e-01 -4.412942e-01
      vertex 1.318092e-01 7.255491e-01 -4.980300e-01
      vertex 3.630464e-01 7.255491e-01 -4.980300e-01
    endloop
  endfacet
  facet normal 9.543942e-01 -2.624085e-01 1.423853e-01
    outer loop
      vertex 1.298280e-01 7.491287e-01 -4.412942e-01
      vertex 1.012335e-01 6.737633e-01 -3.885227e-01
      vertex 1.027784e-01 6.490335e-01 -4.444532e-01
    endloop
  endfacet
  facet normal 9.543942e-01 -2.624085e-01 1.423853e-01
    outer loop
      vertex 1.298280e-01 7.491287e-01 -4.412942e-01
      vertex 1.027784e-01 6.490335e-01 -4.444532e-01
      vertex 1.318092e-01 7.255491e-01 -4.980300e-01
    endloop
  endfacet
  facet normal -0.000000e+00 2.532844e-02 9.996792e-01
    outer loop
      vertex 3.852018e-01 5.138589e-01 -7.501735e-01
      vertex 5.291471e-01 5.138589e-01 -7.501735e-01
      vertex 4.486313e-01 5.671115e-01 -7.515228e-01
    endloop
  endfacet
  facet normal 3.820966e-01 5.956172e-01 7.065709e-01
    outer loop
      vertex 5.291471e-01 5.138589e-01 -7.501735e-01
      vertex 5.072879e-01 5.966609e-01 -8.081521e-01
      vertex 4.486313e-01 5.671115e-01 -7.515228e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.865613e-01 4.626111e-01
    outer loop
      vertex 5.072879e-01 5.966609e-01 -8.081521e-01
      vertex 3.852018e-01 5.966609e-01 -8.081521e-01
      vertex 4.486313e-01 5.671115e-01 -7.515228e-01
    endloop
  endfacet
  facet normal -4.209914e-01 5.202709e-01 7.430238e-01
    outer loop
      vertex 3.852018e-01 5.966609e-01 -8.081521e-01
      vertex 3.852018e-01 5.138589e-01 -7.501735e-01
      vertex 4.486313e-01 5.671115e-01 -7.515228e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 3.905521e-01 4.891292e-01 -8.061041e-01
      vertex 5.143340e-01 5.730813e-01 -8.648879e-01
      vertex 5.364968e-01 4.891292e-01 -8.061041e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 3.905521e-01 4.891292e-01 -8.061041e-01
      vertex 3.905521e-01 5.730813e-01 -8.648879e-01
      vertex 5.143340e-01 5.730813e-01 -8.648879e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.145882e-01 -4.043864e-01
    outer loop
      vertex 3.852018e-01 5.138589e-01 -7.501735e-01
      vertex 5.291471e-01 5.138589e-01 -7.501735e-01
      vertex 5.364968e-01 4.891292e-01 -8.061041e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.145882e-01 -4.043864e-01
    outer loop
      vertex 3.852018e-01 5.138589e-01 -7.501735e-01
      vertex 5.364968e-01 4.891292e-01 -8.061041e-01
      vertex 3.905521e-01 4.891292e-01 -8.061041e-01
    endloop
  endfacet
  facet normal -9.649235e-01 -2.623081e-01 -1.081779e-02
    outer loop
      vertex 5.291471e-01 5.138589e-01 -7.501735e-01
      vertex 5.072879e-01 5.966609e-01 -8.081521e-01
      vertex 5.143340e-01 5.730813e-01 -8.648879e-01
    endloop
  endfacet
  facet normal -9.649235e-01 -2.623081e-01 -1.081779e-02
    outer loop
      vertex 5.291471e-01 5.138589e-01 -7.501735e-01
      vertex 5.143340e-01 5.730813e-01 -8.648879e-01
      vertex 5.364968e-01 4.891292e-01 -8.061041e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.234248e-01 3.837795e-01
    outer loop
      vertex 5.072879e-01 5.966609e-01 -8.081521e-01
      vertex 3.852018e-01 5.966609e-01 -8.081521e-01
      vertex 3.905521e-01 5.730813e-01 -8.648879e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.234248e-01 3.837795e-01
    outer loop
      vertex 5.072879e-01 5.966609e-01 -8.081521e-01
      vertex 3.905521e-01 5.730813e-01 -8.648879e-01
      vertex 5.143340e-01 5.730813e-01 -8.648879e-01
    endloop
  endfacet
  facet normal 9.960477e-01 5.094473e-02 7.275662e-02
    outer loop
      vertex 3.852018e-01 5.966609e-01 -8.081521e-01
      vertex 3.852018e-01 5.138589e-01 -7.501735e-01
      vertex 3.905521e-01 4.891292e-01 -8.061041e-01
    endloop
  endfacet
  facet normal 9.960477e-01 5.094473e-02 7.275662e-02
    outer loop
      vertex 3.852018e-01 5.966609e-01 -8.081521e-01
      vertex 3.905521e-01 4.891292e-01 -8.061041e-01
      vertex 3.905521e-01 5.730813e-01 -8.648879e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.312866e-01 8.471921e-01
    outer loop
      vertex -5.101572e-01 5.932507e-01 -8.088776e-01
      vertex -2.773201e-01 5.932507e-01 -8.088776e-01
      vertex -3.841544e-01 6.299334e-01 -7.858733e-01
    endloop
  endfacet
  facet normal 3.497505e-01 5.373510e-01 7.674168e-01
    outer loop
      vertex -2.773201e-01 5.932507e-01 -8.088776e-01
      vertex -2.773201e-01 6.356140e-01 -8.385406e-01
      vertex -3.841544e-01 6.299334e-01 -7.858733e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.942337e-01 1.072351e-01
    outer loop
      vertex -2.773201e-01 6.356140e-01 -8.385406e-01
      vertex -4.861315e-01 6.356140e-01 -8.385406e-01
      vertex -3.841544e-01 6.299334e-01 -7.858733e-01
    endloop
  endfacet
  facet normal -3.163141e-01 6.579323e-01 6.834255e-01
    outer loop
      vertex -4.861315e-01 6.356140e-01 -8.385406e-01
      vertex -5.101572e-01 5.932507e-01 -8.088776e-01
      vertex -3.841544e-01 6.299334e-01 -7.858733e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -5.172389e-01 5.696376e-01 -8.655900e-01
      vertex -2.811697e-01 6.125890e-01 -8.956648e-01
      vertex -2.811697e-01 5.696376e-01 -8.655900e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -5.172389e-01 5.696376e-01 -8.655900e-01
      vertex -4.928797e-01 6.125890e-01 -8.956648e-01
      vertex -2.811697e-01 6.125890e-01 -8.956648e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.231756e-01 -3.843784e-01
    outer loop
      vertex -5.101572e-01 5.932507e-01 -8.088776e-01
      vertex -2.773201e-01 5.932507e-01 -8.088776e-01
      vertex -2.811697e-01 5.696376e-01 -8.655900e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.231756e-01 -3.843784e-01
    outer loop
      vertex -5.101572e-01 5.932507e-01 -8.088776e-01
      vertex -2.811697e-01 5.696376e-01 -8.655900e-01
      vertex -5.172389e-01 5.696376e-01 -8.655900e-01
    endloop
  endfacet
  facet normal -9.979481e-01 3.672516e-02 5.244897e-02
    outer loop
      vertex -2.773201e-01 5.932507e-01 -8.088776e-01
      vertex -2.773201e-01 6.356140e-01 -8.385406e-01
      vertex -2.811697e-01 6.125890e-01 -8.956648e-01
    endloop
  endfacet
  facet normal -9.979481e-01 3.672516e-02 5.244897e-02
    outer loop
      vertex -2.773201e-01 5.932507e-01 -8.088776e-01
      vertex -2.811697e-01 6.125890e-01 -8.956648e-01
      vertex -2.811697e-01 5.696376e-01 -8.655900e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.274917e-01 3.738438e-01
    outer loop
      vertex -2.773201e-01 6.356140e-01 -8.385406e-01
      vertex -4.861315e-01 6.356140e-01 -8.385406e-01
      vertex -4.928797e-01 6.125890e-01 -8.956648e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.274917e-01 3.738438e-01
    outer loop
      vertex -2.773201e-01 6.356140e-01 -8.385406e-01
      vertex -4.928797e-01 6.125890e-01 -8.956648e-01
      vertex -2.811697e-01 6.125890e-01 -8.956648e-01
    endloop
  endfacet
  facet normal 8.893614e-01 -4.507396e-01 7.661725e-02
    outer loop
      vertex -4.861315e-01 6.356140e-01 -8.385406e-01
      vertex -5.101572e-01 5.932507e-01 -8.088776e-01
      vertex -5.172389e-01 5.696376e-01 -8.655900e-01
    endloop
  endfacet
  facet normal 8.893614e-01 -4.507396e-01 7.661725e-02
    outer loop
      vertex -4.861315e-01 6.356140e-01 -8.385406e-01
      vertex -5.172389e-01 5.696376e-01 -8.655900e-01
      vertex -4.928797e-01 6.125890e-01 -8.956648e-01
    endloop
  endfacet
  facet normal 3.646604e-01 5.340803e-01 7.627457e-01
    outer loop
      vertex -2.702962e-01 6.788234e-01 -7.258606e-01
      vertex -2.702962e-01 7.271706e-01 -7.597136e-01
      vertex -3.619048e-01 7.165731e-01 -7.084961e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.792574e-01 2.026201e-01
    outer loop
      vertex -2.702962e-01 7.271706e-01 -7.597136e-01
      vertex -4.460319e-01 7.271706e-01 -7.597136e-01
      vertex -3.619048e-01 7.165731e-01 -7.084961e-01
    endloop
  endfacet
  facet normal -3.284688e-01 6.596341e-01 6.760112e-01
    outer loop
      vertex -4.460319e-01 7.271706e-01 -7.597136e-01
      vertex -4.734512e-01 6.788234e-01 -7.258606e-01
      vertex -3.619048e-01 7.165731e-01 -7.084961e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -4.178983e-01 9.084938e-01
    outer loop
      vertex -4.734512e-01 6.788234e-01 -7.258606e-01
      vertex -2.702962e-01 6.788234e-01 -7.258606e-01
      vertex -3.619048e-01 7.165731e-01 -7.084961e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -2.741528e-01 6.557738e-01 -7.829675e-01
      vertex -4.523959e-01 7.048108e-01 -8.173036e-01
      vertex -2.741528e-01 7.048108e-01 -8.173036e-01
    endloop
  endfacet
  facet normal -0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -2.741528e-01 6.557738e-01 -7.829675e-01
      vertex -4.802064e-01 6.557738e-01 -7.829675e-01
      vertex -4.523959e-01 7.048108e-01 -8.173036e-01
    endloop
  endfacet
  facet normal -9.979407e-01 3.679137e-02 5.254352e-02
    outer loop
      vertex -2.702962e-01 6.788234e-01 -7.258606e-01
      vertex -2.702962e-01 7.271706e-01 -7.597136e-01
      vertex -2.741528e-01 7.048108e-01 -8.173036e-01
    endloop
  endfacet
  facet normal -9.979407e-01 3.679137e-02 5.254352e-02
    outer loop
      vertex -2.702962e-01 6.788234e-01 -7.258606e-01
      vertex -2.741528e-01 7.048108e-01 -8.173036e-01
      vertex -2.741528e-01 6.557738e-01 -7.829675e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.322031e-01 3.619355e-01
    outer loop
      vertex -2.702962e-01 7.271706e-01 -7.597136e-01
      vertex -4.460319e-01 7.271706e-01 -7.597136e-01
      vertex -4.523959e-01 7.048108e-01 -8.173036e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.322031e-01 3.619355e-01
    outer loop
      vertex -2.702962e-01 7.271706e-01 -7.597136e-01
      vertex -4.523959e-01 7.048108e-01 -8.173036e-01
      vertex -2.741528e-01 7.048108e-01 -8.173036e-01
    endloop
  endfacet
  facet normal 8.893794e-01 -4.506894e-01 7.670341e-02
    outer loop
      vertex -4.460319e-01 7.271706e-01 -7.597136e-01
      vertex -4.734512e-01 6.788234e-01 -7.258606e-01
      vertex -4.802064e-01 6.557738e-01 -7.829675e-01
    endloop
  endfacet
  facet normal 8.893794e-01 -4.506894e-01 7.670341e-02
    outer loop
      vertex -4.460319e-01 7.271706e-01 -7.597136e-01
      vertex -4.802064e-01 6.557738e-01 -7.829675e-01
      vertex -4.523959e-01 7.048108e-01 -8.173036e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.273142e-01 -3.742839e-01
    outer loop
      vertex -4.734512e-01 6.788234e-01 -7.258606e-01
      vertex -2.702962e-01 6.788234e-01 -7.258606e-01
      vertex -2.741528e-01 6.557738e-01 -7.829675e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.273142e-01 -3.742839e-01
    outer loop
      vertex -4.734512e-01 6.788234e-01 -7.258606e-01
      vertex -2.741528e-01 6.557738e-01 -7.829675e-01
      vertex -4.802064e-01 6.557738e-01 -7.829675e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -3.499089e-01 9.367837e-01
    outer loop
      vertex -2.514735e-01 7.887038e-01 -3.394509e-01
      vertex -1.278213e-01 7.887038e-01 -3.394509e-01
      vertex -1.914746e-01 8.171889e-01 -3.288111e-01
    endloop
  endfacet
  facet normal 3.886970e-01 6.109943e-01 6.896380e-01
    outer loop
      vertex -1.278213e-01 7.887038e-01 -3.394509e-01
      vertex -1.401789e-01 8.261994e-01 -3.657057e-01
      vertex -1.914746e-01 8.171889e-01 -3.288111e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.714481e-01 2.372521e-01
    outer loop
      vertex -1.401789e-01 8.261994e-01 -3.657057e-01
      vertex -2.514735e-01 8.261994e-01 -3.657057e-01
      vertex -1.914746e-01 8.171889e-01 -3.288111e-01
    endloop
  endfacet
  facet normal -3.853289e-01 5.292845e-01 7.558966e-01
    outer loop
      vertex -2.514735e-01 8.261994e-01 -3.657057e-01
      vertex -2.514735e-01 7.887038e-01 -3.394509e-01
      vertex -1.914746e-01 8.171889e-01 -3.288111e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -2.554175e-01 7.650907e-01 -3.961633e-01
      vertex -1.423774e-01 8.031744e-01 -4.228299e-01
      vertex -1.298260e-01 7.650907e-01 -3.961633e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -2.554175e-01 7.650907e-01 -3.961633e-01
      vertex -2.554175e-01 8.031744e-01 -4.228299e-01
      vertex -1.423774e-01 8.031744e-01 -4.228299e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.231756e-01 -3.843784e-01
    outer loop
      vertex -2.514735e-01 7.887038e-01 -3.394509e-01
      vertex -1.278213e-01 7.887038e-01 -3.394509e-01
      vertex -1.298260e-01 7.650907e-01 -3.961633e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.231756e-01 -3.843784e-01
    outer loop
      vertex -2.514735e-01 7.887038e-01 -3.394509e-01
      vertex -1.298260e-01 7.650907e-01 -3.961633e-01
      vertex -2.554175e-01 7.650907e-01 -3.961633e-01
    endloop
  endfacet
  facet normal -9.651338e-01 -2.277861e-01 1.289580e-01
    outer loop
      vertex -1.278213e-01 7.887038e-01 -3.394509e-01
      vertex -1.401789e-01 8.261994e-01 -3.657057e-01
      vertex -1.423774e-01 8.031744e-01 -4.228299e-01
    endloop
  endfacet
  facet normal -9.651338e-01 -2.277861e-01 1.289580e-01
    outer loop
      vertex -1.278213e-01 7.887038e-01 -3.394509e-01
      vertex -1.423774e-01 8.031744e-01 -4.228299e-01
      vertex -1.298260e-01 7.650907e-01 -3.961633e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.274917e-01 3.738438e-01
    outer loop
      vertex -1.401789e-01 8.261994e-01 -3.657057e-01
      vertex -2.514735e-01 8.261994e-01 -3.657057e-01
      vertex -2.554175e-01 8.031744e-01 -4.228299e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.274917e-01 3.738438e-01
    outer loop
      vertex -1.401789e-01 8.261994e-01 -3.657057e-01
      vertex -2.554175e-01 8.031744e-01 -4.228299e-01
      vertex -1.423774e-01 8.031744e-01 -4.228299e-01
    endloop
  endfacet
  facet normal 9.978466e-01 -3.762172e-02 -5.372938e-02
    outer loop
      vertex -2.514735e-01 8.261994e-01 -3.657057e-01
      vertex -2.514735e-01 7.887038e-01 -3.394509e-01
      vertex -2.554175e-01 7.650907e-01 -3.961633e-01
    endloop
  endfacet
  facet normal 9.978466e-01 -3.762172e-02 -5.372938e-02
    outer loop
      vertex -2.514735e-01 8.261994e-01 -3.657057e-01
      vertex -2.554175e-01 7.650907e-01 -3.961633e-01
      vertex -2.554175e-01 8.031744e-01 -4.228299e-01
    endloop
  endfacet
  facet normal 3.872859e-01 6.110502e-01 6.903819e-01
    outer loop
      vertex -1.473177e-01 7.469377e-01 -5.571029e-01
      vertex -1.625799e-01 7.932463e-01 -5.895286e-01
      vertex -2.085103e-01 7.789009e-01 -5.510659e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.369532e-01 3.494550e-01
    outer loop
      vertex -1.625799e-01 7.932463e-01 -5.895286e-01
      vertex -2.644959e-01 7.932463e-01 -5.895286e-01
      vertex -2.085103e-01 7.789009e-01 -5.510659e-01
    endloop
  endfacet
  facet normal -3.839309e-01 5.296186e-01 7.563737e-01
    outer loop
      vertex -2.644959e-01 7.932463e-01 -5.895286e-01
      vertex -2.644959e-01 7.469377e-01 -5.571029e-01
      vertex -2.085103e-01 7.789009e-01 -5.510659e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -1.855938e-01 9.826265e-01
    outer loop
      vertex -2.644959e-01 7.469377e-01 -5.571029e-01
      vertex -1.473177e-01 7.469377e-01 -5.571029e-01
      vertex -2.085103e-01 7.789009e-01 -5.510659e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -1.495121e-01 7.238881e-01 -6.142099e-01
      vertex -2.684358e-01 7.708865e-01 -6.471186e-01
      vertex -1.650016e-01 7.708865e-01 -6.471186e-01
    endloop
  endfacet
  facet normal -0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -1.495121e-01 7.238881e-01 -6.142099e-01
      vertex -2.684358e-01 7.238881e-01 -6.142099e-01
      vertex -2.684358e-01 7.708865e-01 -6.471186e-01
    endloop
  endfacet
  facet normal -9.651354e-01 -2.277491e-01 1.290116e-01
    outer loop
      vertex -1.473177e-01 7.469377e-01 -5.571029e-01
      vertex -1.625799e-01 7.932463e-01 -5.895286e-01
      vertex -1.650016e-01 7.708865e-01 -6.471186e-01
    endloop
  endfacet
  facet normal -9.651354e-01 -2.277491e-01 1.290116e-01
    outer loop
      vertex -1.473177e-01 7.469377e-01 -5.571029e-01
      vertex -1.650016e-01 7.708865e-01 -6.471186e-01
      vertex -1.495121e-01 7.238881e-01 -6.142099e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.322031e-01 3.619355e-01
    outer loop
      vertex -1.625799e-01 7.932463e-01 -5.895286e-01
      vertex -2.644959e-01 7.932463e-01 -5.895286e-01
      vertex -2.684358e-01 7.708865e-01 -6.471186e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.322031e-01 3.619355e-01
    outer loop
      vertex -1.625799e-01 7.932463e-01 -5.895286e-01
      vertex -2.684358e-01 7.708865e-01 -6.471186e-01
      vertex -1.650016e-01 7.708865e-01 -6.471186e-01
    endloop
  endfacet
  facet normal 9.978510e-01 -3.758326e-02 -5.367445e-02
    outer loop
      vertex -2.644959e-01 7.932463e-01 -5.895286e-01
      vertex -2.644959e-01 7.469377e-01 -5.571029e-01
      vertex -2.684358e-01 7.238881e-01 -6.142099e-01
    endloop
  endfacet
  facet normal 9.978510e-01 -3.758326e-02 -5.367445e-02
    outer loop
      vertex -2.644959e-01 7.932463e-01 -5.895286e-01
      vertex -2.684358e-01 7.238881e-01 -6.142099e-01
      vertex -2.684358e-01 7.708865e-01 -6.471186e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.273142e-01 -3.742839e-01
    outer loop
      vertex -2.644959e-01 7.469377e-01 -5.571029e-01
      vertex -1.473177e-01 7.469377e-01 -5.571029e-01
      vertex -1.495121e-01 7.238881e-01 -6.142099e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.273142e-01 -3.742839e-01
    outer loop
      vertex -2.644959e-01 7.469377e-01 -5.571029e-01
      vertex -1.495121e-01 7.238881e-01 -6.142099e-01
      vertex -2.684358e-01 7.238881e-01 -6.142099e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.928081e-01 8.053438e-01
    outer loop
      vertex 1.355828e-01 6.733923e-01 -6.163987e-01
      vertex 3.741698e-01 6.733923e-01 -6.163987e-01
      vertex 2.554593e-01 7.105813e-01 -5.890241e-01
    endloop
  endfacet
  facet normal 3.458392e-01 5.381832e-01 7.686053e-01
    outer loop
      vertex 3.741698e-01 6.733923e-01 -6.163987e-01
      vertex 3.741698e-01 7.137597e-01 -6.446642e-01
      vertex 2.554593e-01 7.105813e-01 -5.890241e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.983724e-01 5.703147e-02
    outer loop
      vertex 3.741698e-01 7.137597e-01 -6.446642e-01
      vertex 1.488868e-01 7.137597e-01 -6.446642e-01
      vertex 2.554593e-01 7.105813e-01 -5.890241e-01
    endloop
  endfacet
  facet normal -3.516187e-01 6.119417e-01 7.084431e-01
    outer loop
      vertex 1.488868e-01 7.137597e-01 -6.446642e-01
      vertex 1.355828e-01 6.733923e-01 -6.163987e-01
      vertex 2.554593e-01 7.105813e-01 -5.890241e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 1.375579e-01 6.497792e-01 -6.731111e-01
      vertex 3.796206e-01 6.907347e-01 -7.017884e-01
      vertex 3.796206e-01 6.497792e-01 -6.731111e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 1.375579e-01 6.497792e-01 -6.731111e-01
      vertex 1.510558e-01 6.907347e-01 -7.017884e-01
      vertex 3.796206e-01 6.907347e-01 -7.017884e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.231756e-01 -3.843784e-01
    outer loop
      vertex 1.355828e-01 6.733923e-01 -6.163987e-01
      vertex 3.741698e-01 6.733923e-01 -6.163987e-01
      vertex 3.796206e-01 6.497792e-01 -6.731111e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.231756e-01 -3.843784e-01
    outer loop
      vertex 1.355828e-01 6.733923e-01 -6.163987e-01
      vertex 3.796206e-01 6.497792e-01 -6.731111e-01
      vertex 1.375579e-01 6.497792e-01 -6.731111e-01
    endloop
  endfacet
  facet normal -9.958988e-01 -5.189397e-02 -7.411227e-02
    outer loop
      vertex 3.741698e-01 6.733923e-01 -6.163987e-01
      vertex 3.741698e-01 7.137597e-01 -6.446642e-01
      vertex 3.796206e-01 6.907347e-01 -7.017884e-01
    endloop
  endfacet
  facet normal -9.958988e-01 -5.189397e-02 -7.411227e-02
    outer loop
      vertex 3.741698e-01 6.733923e-01 -6.163987e-01
      vertex 3.796206e-01 6.907347e-01 -7.017884e-01
      vertex 3.796206e-01 6.497792e-01 -6.731111e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.274917e-01 3.738438e-01
    outer loop
      vertex 3.741698e-01 7.137597e-01 -6.446642e-01
      vertex 1.488868e-01 7.137597e-01 -6.446642e-01
      vertex 1.510558e-01 6.907347e-01 -7.017884e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.274917e-01 3.738438e-01
    outer loop
      vertex 3.741698e-01 7.137597e-01 -6.446642e-01
      vertex 1.510558e-01 6.907347e-01 -7.017884e-01
      vertex 3.796206e-01 6.907347e-01 -7.017884e-01
    endloop
  endfacet
  facet normal 9.651222e-01 -2.280560e-01 1.285672e-01
    outer loop
      vertex 1.488868e-01 7.137597e-01 -6.446642e-01
      vertex 1.355828e-01 6.733923e-01 -6.163987e-01
      vertex 1.375579e-01 6.497792e-01 -6.731111e-01
    endloop
  endfacet
  facet normal 9.651222e-01 -2.280560e-01 1.285672e-01
    outer loop
      vertex 1.488868e-01 7.137597e-01 -6.446642e-01
      vertex 1.375579e-01 6.497792e-01 -6.731111e-01
      vertex 1.510558e-01 6.907347e-01 -7.017884e-01
    endloop
  endfacet
  facet normal 3.657269e-01 5.338403e-01 7.624030e-01
    outer loop
      vertex 3.541807e-01 7.954861e-01 -4.368207e-01
      vertex 3.541807e-01 8.403419e-01 -4.682291e-01
      vertex 2.484999e-01 8.336284e-01 -4.128329e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.927363e-01 1.203103e-01
    outer loop
      vertex 3.541807e-01 8.403419e-01 -4.682291e-01
      vertex 1.555577e-01 8.403419e-01 -4.682291e-01
      vertex 2.484999e-01 8.336284e-01 -4.128329e-01
    endloop
  endfacet
  facet normal -3.720230e-01 6.115534e-01 6.982845e-01
    outer loop
      vertex 1.555577e-01 8.403419e-01 -4.682291e-01
      vertex 1.407744e-01 7.954861e-01 -4.368207e-01
      vertex 2.484999e-01 8.336284e-01 -4.128329e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.323743e-01 8.465091e-01
    outer loop
      vertex 1.407744e-01 7.954861e-01 -4.368207e-01
      vertex 3.541807e-01 7.954861e-01 -4.368207e-01
      vertex 2.484999e-01 8.336284e-01 -4.128329e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 3.596274e-01 7.724365e-01 -4.939277e-01
      vertex 1.579499e-01 8.179821e-01 -5.258191e-01
      vertex 3.596274e-01 8.179821e-01 -5.258191e-01
    endloop
  endfacet
  facet normal -0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 3.596274e-01 7.724365e-01 -4.939277e-01
      vertex 1.429393e-01 7.724365e-01 -4.939277e-01
      vertex 1.579499e-01 8.179821e-01 -5.258191e-01
    endloop
  endfacet
  facet normal -9.959048e-01 -5.185573e-02 -7.405766e-02
    outer loop
      vertex 3.541807e-01 7.954861e-01 -4.368207e-01
      vertex 3.541807e-01 8.403419e-01 -4.682291e-01
      vertex 3.596274e-01 8.179821e-01 -5.258191e-01
    endloop
  endfacet
  facet normal -9.959048e-01 -5.185573e-02 -7.405766e-02
    outer loop
      vertex 3.541807e-01 7.954861e-01 -4.368207e-01
      vertex 3.596274e-01 8.179821e-01 -5.258191e-01
      vertex 3.596274e-01 7.724365e-01 -4.939277e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.322031e-01 3.619355e-01
    outer loop
      vertex 3.541807e-01 8.403419e-01 -4.682291e-01
      vertex 1.555577e-01 8.403419e-01 -4.682291e-01
      vertex 1.579499e-01 8.179821e-01 -5.258191e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.322031e-01 3.619355e-01
    outer loop
      vertex 3.541807e-01 8.403419e-01 -4.682291e-01
      vertex 1.579499e-01 8.179821e-01 -5.258191e-01
      vertex 3.596274e-01 8.179821e-01 -5.258191e-01
    endloop
  endfacet
  facet normal 9.651238e-01 -2.280190e-01 1.286208e-01
    outer loop
      vertex 1.555577e-01 8.403419e-01 -4.682291e-01
      vertex 1.407744e-01 7.954861e-01 -4.368207e-01
      vertex 1.429393e-01 7.724365e-01 -4.939277e-01
    endloop
  endfacet
  facet normal 9.651238e-01 -2.280190e-01 1.286208e-01
    outer loop
      vertex 1.555577e-01 8.403419e-01 -4.682291e-01
      vertex 1.429393e-01 7.724365e-01 -4.939277e-01
      vertex 1.579499e-01 8.179821e-01 -5.258191e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.273142e-01 -3.742839e-01
    outer loop
      vertex 1.407744e-01 7.954861e-01 -4.368207e-01
      vertex 3.541807e-01 7.954861e-01 -4.368207e-01
      vertex 3.596274e-01 7.724365e-01 -4.939277e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.273142e-01 -3.742839e-01
    outer loop
      vertex 1.407744e-01 7.954861e-01 -4.368207e-01
      vertex 3.596274e-01 7.724365e-01 -4.939277e-01
      vertex 1.429393e-01 7.724365e-01 -4.939277e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -2.290856e-01 9.734063e-01
    outer loop
      vertex 3.577612e-01 7.171669e-01 -5.112635e-01
      vertex 4.710205e-01 7.171669e-01 -5.112635e-01
      vertex 4.066353e-01 7.451360e-01 -5.046811e-01
    endloop
  endfacet
  facet normal 3.553528e-01 6.629430e-01 6.589620e-01
    outer loop
      vertex 4.710205e-01 7.171669e-01 -5.112635e-01
      vertex 4.487451e-01 7.564442e-01 -5.387657e-01
      vertex 4.066353e-01 7.451360e-01 -5.046811e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.491285e-01 3.148890e-01
    outer loop
      vertex 4.487451e-01 7.564442e-01 -5.387657e-01
      vertex 3.577612e-01 7.564442e-01 -5.387657e-01
      vertex 4.066353e-01 7.451360e-01 -5.046811e-01
    endloop
  endfacet
  facet normal -4.016355e-01 5.252811e-01 7.501791e-01
    outer loop
      vertex 3.577612e-01 7.564442e-01 -5.387657e-01
      vertex 3.577612e-01 7.171669e-01 -5.112635e-01
      vertex 4.066353e-01 7.451360e-01 -5.046811e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 3.631176e-01 6.935538e-01 -5.679759e-01
      vertex 4.554637e-01 7.334191e-01 -5.958899e-01
      vertex 4.780727e-01 6.935538e-01 -5.679759e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 3.631176e-01 6.935538e-01 -5.679759e-01
      vertex 3.631176e-01 7.334191e-01 -5.958899e-01
      vertex 4.554637e-01 7.334191e-01 -5.958899e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.231756e-01 -3.843784e-01
    outer loop
      vertex 3.577612e-01 7.171669e-01 -5.112635e-01
      vertex 4.710205e-01 7.171669e-01 -5.112635e-01
      vertex 4.780727e-01 6.935538e-01 -5.679759e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.231756e-01 -3.843784e-01
    outer loop
      vertex 3.577612e-01 7.171669e-01 -5.112635e-01
      vertex 4.780727e-01 6.935538e-01 -5.679759e-01
      vertex 3.631176e-01 6.935538e-01 -5.679759e-01
    endloop
  endfacet
  facet normal -8.894375e-01 -4.505269e-01 7.698259e-02
    outer loop
      vertex 4.710205e-01 7.171669e-01 -5.112635e-01
      vertex 4.487451e-01 7.564442e-01 -5.387657e-01
      vertex 4.554637e-01 7.334191e-01 -5.958899e-01
    endloop
  endfacet
  facet normal -8.894375e-01 -4.505269e-01 7.698259e-02
    outer loop
      vertex 4.710205e-01 7.171669e-01 -5.112635e-01
      vertex 4.554637e-01 7.334191e-01 -5.958899e-01
      vertex 4.780727e-01 6.935538e-01 -5.679759e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.274917e-01 3.738438e-01
    outer loop
      vertex 4.487451e-01 7.564442e-01 -5.387657e-01
      vertex 3.577612e-01 7.564442e-01 -5.387657e-01
      vertex 3.631176e-01 7.334191e-01 -5.958899e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.274917e-01 3.738438e-01
    outer loop
      vertex 4.487451e-01 7.564442e-01 -5.387657e-01
      vertex 3.631176e-01 7.334191e-01 -5.958899e-01
      vertex 4.554637e-01 7.334191e-01 -5.958899e-01
    endloop
  endfacet
  facet normal 9.960387e-01 5.100260e-02 7.283926e-02
    outer loop
      vertex 3.577612e-01 7.564442e-01 -5.387657e-01
      vertex 3.577612e-01 7.171669e-01 -5.112635e-01
      vertex 3.631176e-01 6.935538e-01 -5.679759e-01
    endloop
  endfacet
  facet normal 9.960387e-01 5.100260e-02 7.283926e-02
    outer loop
      vertex 3.577612e-01 7.564442e-01 -5.387657e-01
      vertex 3.631176e-01 6.935538e-01 -5.679759e-01
      vertex 3.631176e-01 7.334191e-01 -5.958899e-01
    endloop
  endfacet
  facet normal 3.788086e-01 6.653020e-01 6.433330e-01
    outer loop
      vertex 4.629682e-01 7.076534e-01 -6.544325e-01
      vertex 4.360382e-01 7.551377e-01 -6.876814e-01
      vertex 4.075323e-01 7.383375e-01 -6.535226e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.973418e-01 4.413362e-01
    outer loop
      vertex 4.360382e-01 7.551377e-01 -6.876814e-01
      vertex 3.691978e-01 7.551377e-01 -6.876814e-01
      vertex 4.075323e-01 7.383375e-01 -6.535226e-01
    endloop
  endfacet
  facet normal -4.316694e-01 5.173842e-01 7.389013e-01
    outer loop
      vertex 3.691978e-01 7.551377e-01 -6.876814e-01
      vertex 3.691978e-01 7.076534e-01 -6.544325e-01
      vertex 4.075323e-01 7.383375e-01 -6.535226e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -2.964078e-02 9.995606e-01
    outer loop
      vertex 3.691978e-01 7.076534e-01 -6.544325e-01
      vertex 4.629682e-01 7.076534e-01 -6.544325e-01
      vertex 4.075323e-01 7.383375e-01 -6.535226e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 4.696938e-01 6.846038e-01 -7.115394e-01
      vertex 3.745612e-01 7.327779e-01 -7.452714e-01
      vertex 4.423726e-01 7.327779e-01 -7.452714e-01
    endloop
  endfacet
  facet normal -0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 4.696938e-01 6.846038e-01 -7.115394e-01
      vertex 3.745612e-01 6.846038e-01 -7.115394e-01
      vertex 3.745612e-01 7.327779e-01 -7.452714e-01
    endloop
  endfacet
  facet normal -8.894555e-01 -4.504768e-01 7.706877e-02
    outer loop
      vertex 4.629682e-01 7.076534e-01 -6.544325e-01
      vertex 4.360382e-01 7.551377e-01 -6.876814e-01
      vertex 4.423726e-01 7.327779e-01 -7.452714e-01
    endloop
  endfacet
  facet normal -8.894555e-01 -4.504768e-01 7.706877e-02
    outer loop
      vertex 4.629682e-01 7.076534e-01 -6.544325e-01
      vertex 4.423726e-01 7.327779e-01 -7.452714e-01
      vertex 4.696938e-01 6.846038e-01 -7.115394e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.322031e-01 3.619355e-01
    outer loop
      vertex 4.360382e-01 7.551377e-01 -6.876814e-01
      vertex 3.691978e-01 7.551377e-01 -6.876814e-01
      vertex 3.745612e-01 7.327779e-01 -7.452714e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.322031e-01 3.619355e-01
    outer loop
      vertex 4.360382e-01 7.551377e-01 -6.876814e-01
      vertex 3.745612e-01 7.327779e-01 -7.452714e-01
      vertex 4.423726e-01 7.327779e-01 -7.452714e-01
    endloop
  endfacet
  facet normal 9.960285e-01 5.106843e-02 7.293328e-02
    outer loop
      vertex 3.691978e-01 7.551377e-01 -6.876814e-01
      vertex 3.691978e-01 7.076534e-01 -6.544325e-01
      vertex 3.745612e-01 6.846038e-01 -7.115394e-01
    endloop
  endfacet
  facet normal 9.960285e-01 5.106843e-02 7.293328e-02
    outer loop
      vertex 3.691978e-01 7.551377e-01 -6.876814e-01
      vertex 3.745612e-01 6.846038e-01 -7.115394e-01
      vertex 3.745612e-01 7.327779e-01 -7.452714e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.273142e-01 -3.742839e-01
    outer loop
      vertex 3.691978e-01 7.076534e-01 -6.544325e-01
      vertex 4.629682e-01 7.076534e-01 -6.544325e-01
      vertex 4.696938e-01 6.846038e-01 -7.115394e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.273142e-01 -3.742839e-01
    outer loop
      vertex 3.691978e-01 7.076534e-01 -6.544325e-01
      vertex 4.696938e-01 6.846038e-01 -7.115394e-01
      vertex 3.745612e-01 6.846038e-01 -7.115394e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.595328e-02 9.984334e-01
    outer loop
      vertex -3.971118e-01 9.002415e-01 -3.062359e-01
      vertex -2.410481e-01 9.002415e-01 -3.062359e-01
      vertex -2.963909e-01 9.515328e-01 -3.033615e-01
    endloop
  endfacet
  facet normal 4.979047e-01 4.974237e-01 7.103947e-01
    outer loop
      vertex -2.410481e-01 9.002415e-01 -3.062359e-01
      vertex -2.410481e-01 9.797787e-01 -3.619284e-01
      vertex -2.963909e-01 9.515328e-01 -3.033615e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.007190e-01 4.344022e-01
    outer loop
      vertex -2.410481e-01 9.797787e-01 -3.619284e-01
      vertex -3.165293e-01 9.797787e-01 -3.619284e-01
      vertex -2.963909e-01 9.515328e-01 -3.033615e-01
    endloop
  endfacet
  facet normal -4.027691e-01 7.625482e-01 5.062582e-01
    outer loop
      vertex -3.165293e-01 9.797787e-01 -3.619284e-01
      vertex -3.971118e-01 9.002415e-01 -3.062359e-01
      vertex -2.963909e-01 9.515328e-01 -3.033615e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -4.034919e-01 8.778439e-01 -3.637994e-01
      vertex -2.449209e-01 9.586589e-01 -4.203866e-01
      vertex -2.449209e-01 8.778439e-01 -3.637994e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -4.034919e-01 8.778439e-01 -3.637994e-01
      vertex -3.216148e-01 9.586589e-01 -4.203866e-01
      vertex -2.449209e-01 9.586589e-01 -4.203866e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.319400e-01 -3.626125e-01
    outer loop
      vertex -3.971118e-01 9.002415e-01 -3.062359e-01
      vertex -2.410481e-01 9.002415e-01 -3.062359e-01
      vertex -2.449209e-01 8.778439e-01 -3.637994e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.319400e-01 -3.626125e-01
    outer loop
      vertex -3.971118e-01 9.002415e-01 -3.062359e-01
      vertex -2.449209e-01 8.778439e-01 -3.637994e-01
      vertex -4.034919e-01 8.778439e-01 -3.637994e-01
    endloop
  endfacet
  facet normal -9.979234e-01 3.694538e-02 5.276347e-02
    outer loop
      vertex -2.410481e-01 9.002415e-01 -3.062359e-01
      vertex -2.410481e-01 9.797787e-01 -3.619284e-01
      vertex -2.449209e-01 9.586589e-01 -4.203866e-01
    endloop
  endfacet
  facet normal -9.979234e-01 3.694538e-02 5.276347e-02
    outer loop
      vertex -2.410481e-01 9.002415e-01 -3.062359e-01
      vertex -2.449209e-01 9.586589e-01 -4.203866e-01
      vertex -2.449209e-01 8.778439e-01 -3.637994e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.405034e-01 3.397842e-01
    outer loop
      vertex -2.410481e-01 9.797787e-01 -3.619284e-01
      vertex -3.165293e-01 9.797787e-01 -3.619284e-01
      vertex -3.216148e-01 9.586589e-01 -4.203866e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.405034e-01 3.397842e-01
    outer loop
      vertex -2.410481e-01 9.797787e-01 -3.619284e-01
      vertex -3.216148e-01 9.586589e-01 -4.203866e-01
      vertex -2.449209e-01 9.586589e-01 -4.203866e-01
    endloop
  endfacet
  facet normal 7.486072e-01 -6.417118e-01 1.667130e-01
    outer loop
      vertex -3.165293e-01 9.797787e-01 -3.619284e-01
      vertex -3.971118e-01 9.002415e-01 -3.062359e-01
      vertex -4.034919e-01 8.778439e-01 -3.637994e-01
    endloop
  endfacet
  facet normal 7.486072e-01 -6.417118e-01 1.667130e-01
    outer loop
      vertex -3.165293e-01 9.797787e-01 -3.619284e-01
      vertex -4.034919e-01 8.778439e-01 -3.637994e-01
      vertex -3.216148e-01 9.586589e-01 -4.203866e-01
    endloop
  endfacet
  facet normal -0.000000e+00 6.372921e-02 9.979672e-01
    outer loop
      vertex -2.498680e-01 8.717562e-01 -3.794452e-01
      vertex -1.534457e-01 8.717562e-01 -3.794452e-01
      vertex -2.062575e-01 9.217968e-01 -3.826407e-01
    endloop
  endfacet
  facet normal 5.197783e-01 5.881321e-01 6.196218e-01
    outer loop
      vertex -1.534457e-01 8.717562e-01 -3.794452e-01
      vertex -1.775343e-01 9.529186e-01 -4.362756e-01
      vertex -2.062575e-01 9.217968e-01 -3.826407e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.649366e-01 5.018812e-01
    outer loop
      vertex -1.775343e-01 9.529186e-01 -4.362756e-01
      vertex -2.498680e-01 9.529186e-01 -4.362756e-01
      vertex -2.062575e-01 9.217968e-01 -3.826407e-01
    endloop
  endfacet
  facet normal -5.133106e-01 4.922450e-01 7.029987e-01
    outer loop
      vertex -2.498680e-01 9.529186e-01 -4.362756e-01
      vertex -2.498680e-01 8.717562e-01 -3.794452e-01
      vertex -2.062575e-01 9.217968e-01 -3.826407e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -2.538021e-01 8.493586e-01 -4.370086e-01
      vertex -1.803296e-01 9.317988e-01 -4.947339e-01
      vertex -1.558616e-01 8.493586e-01 -4.370086e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -2.538021e-01 8.493586e-01 -4.370086e-01
      vertex -2.538021e-01 9.317988e-01 -4.947339e-01
      vertex -1.803296e-01 9.317988e-01 -4.947339e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.319400e-01 -3.626125e-01
    outer loop
      vertex -2.498680e-01 8.717562e-01 -3.794452e-01
      vertex -1.534457e-01 8.717562e-01 -3.794452e-01
      vertex -1.558616e-01 8.493586e-01 -4.370086e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.319400e-01 -3.626125e-01
    outer loop
      vertex -2.498680e-01 8.717562e-01 -3.794452e-01
      vertex -1.558616e-01 8.493586e-01 -4.370086e-01
      vertex -2.538021e-01 8.493586e-01 -4.370086e-01
    endloop
  endfacet
  facet normal -9.715262e-01 -2.041689e-01 1.202162e-01
    outer loop
      vertex -1.534457e-01 8.717562e-01 -3.794452e-01
      vertex -1.775343e-01 9.529186e-01 -4.362756e-01
      vertex -1.803296e-01 9.317988e-01 -4.947339e-01
    endloop
  endfacet
  facet normal -9.715262e-01 -2.041689e-01 1.202162e-01
    outer loop
      vertex -1.534457e-01 8.717562e-01 -3.794452e-01
      vertex -1.803296e-01 9.317988e-01 -4.947339e-01
      vertex -1.558616e-01 8.493586e-01 -4.370086e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.405034e-01 3.397842e-01
    outer loop
      vertex -1.775343e-01 9.529186e-01 -4.362756e-01
      vertex -2.498680e-01 9.529186e-01 -4.362756e-01
      vertex -2.538021e-01 9.317988e-01 -4.947339e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.405034e-01 3.397842e-01
    outer loop
      vertex -1.775343e-01 9.529186e-01 -4.362756e-01
      vertex -2.538021e-01 9.317988e-01 -4.947339e-01
      vertex -1.803296e-01 9.317988e-01 -4.947339e-01
    endloop
  endfacet
  facet normal 9.978573e-01 -3.752786e-02 -5.359533e-02
    outer loop
      vertex -2.498680e-01 9.529186e-01 -4.362756e-01
      vertex -2.498680e-01 8.717562e-01 -3.794452e-01
      vertex -2.538021e-01 8.493586e-01 -4.370086e-01
    endloop
  endfacet
  facet normal 9.978573e-01 -3.752786e-02 -5.359533e-02
    outer loop
      vertex -2.498680e-01 9.529186e-01 -4.362756e-01
      vertex -2.538021e-01 8.493586e-01 -4.370086e-01
      vertex -2.538021e-01 9.317988e-01 -4.947339e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -4.206515e-02 9.991149e-01
    outer loop
      vertex 1.654500e-01 7.357368e-01 -7.284656e-01
      vertex 3.779798e-01 7.357368e-01 -7.284656e-01
      vertex 2.910596e-01 7.984229e-01 -7.258263e-01
    endloop
  endfacet
  facet normal 4.016115e-01 5.252871e-01 7.501877e-01
    outer loop
      vertex 3.779798e-01 7.357368e-01 -7.284656e-01
      vertex 3.779798e-01 8.024215e-01 -7.751588e-01
      vertex 2.910596e-01 7.984229e-01 -7.258263e-01
    endloop
  endfacet
  facet normal 3.086624e-01 7.352496e-01 6.034364e-01
    outer loop
      vertex 3.779798e-01 8.024215e-01 -7.751588e-01
      vertex 3.554594e-01 8.246498e-01 -7.907232e-01
      vertex 2.910596e-01 7.984229e-01 -7.258263e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.271498e-01 3.746909e-01
    outer loop
      vertex 3.554594e-01 8.246498e-01 -7.907232e-01
      vertex 1.918390e-01 8.246498e-01 -7.907232e-01
      vertex 2.910596e-01 7.984229e-01 -7.258263e-01
    endloop
  endfacet
  facet normal -3.174280e-01 6.053250e-01 7.299459e-01
    outer loop
      vertex 1.918390e-01 8.246498e-01 -7.907232e-01
      vertex 1.654500e-01 7.357368e-01 -7.284656e-01
      vertex 2.910596e-01 7.984229e-01 -7.258263e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 1.678279e-01 7.133367e-01 -7.860274e-01
      vertex 3.834122e-01 7.809799e-01 -8.333916e-01
      vertex 3.834122e-01 7.133367e-01 -7.860274e-01
    endloop
  endfacet
  facet normal 7.763598e-16 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 1.678279e-01 7.133367e-01 -7.860274e-01
      vertex 3.605681e-01 8.035276e-01 -8.491797e-01
      vertex 3.834122e-01 7.809799e-01 -8.333916e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 1.678279e-01 7.133367e-01 -7.860274e-01
      vertex 1.945962e-01 8.035276e-01 -8.491797e-01
      vertex 3.605681e-01 8.035276e-01 -8.491797e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.319229e-01 -3.626565e-01
    outer loop
      vertex 1.654500e-01 7.357368e-01 -7.284656e-01
      vertex 3.779798e-01 7.357368e-01 -7.284656e-01
      vertex 3.834122e-01 7.133367e-01 -7.860274e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.319229e-01 -3.626565e-01
    outer loop
      vertex 1.654500e-01 7.357368e-01 -7.284656e-01
      vertex 3.834122e-01 7.133367e-01 -7.860274e-01
      vertex 1.678279e-01 7.133367e-01 -7.860274e-01
    endloop
  endfacet
  facet normal -9.959263e-01 -5.172011e-02 -7.386398e-02
    outer loop
      vertex 3.779798e-01 7.357368e-01 -7.284656e-01
      vertex 3.779798e-01 8.024215e-01 -7.751588e-01
      vertex 3.834122e-01 7.809799e-01 -8.333916e-01
    endloop
  endfacet
  facet normal -9.959263e-01 -5.172011e-02 -7.386398e-02
    outer loop
      vertex 3.779798e-01 7.357368e-01 -7.284656e-01
      vertex 3.834122e-01 7.809799e-01 -8.333916e-01
      vertex 3.834122e-01 7.133367e-01 -7.860274e-01
    endloop
  endfacet
  facet normal -7.485623e-01 -6.418218e-01 1.664909e-01
    outer loop
      vertex 3.779798e-01 8.024215e-01 -7.751588e-01
      vertex 3.554594e-01 8.246498e-01 -7.907232e-01
      vertex 3.605681e-01 8.035276e-01 -8.491797e-01
    endloop
  endfacet
  facet normal -7.485623e-01 -6.418218e-01 1.664909e-01
    outer loop
      vertex 3.779798e-01 8.024215e-01 -7.751588e-01
      vertex 3.605681e-01 8.035276e-01 -8.491797e-01
      vertex 3.834122e-01 7.809799e-01 -8.333916e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.404876e-01 3.398280e-01
    outer loop
      vertex 3.554594e-01 8.246498e-01 -7.907232e-01
      vertex 1.918390e-01 8.246498e-01 -7.907232e-01
      vertex 1.945962e-01 8.035276e-01 -8.491797e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.404876e-01 3.398280e-01
    outer loop
      vertex 3.554594e-01 8.246498e-01 -7.907232e-01
      vertex 1.945962e-01 8.035276e-01 -8.491797e-01
      vertex 3.605681e-01 8.035276e-01 -8.491797e-01
    endloop
  endfacet
  facet normal 9.715151e-01 -2.045134e-01 1.197195e-01
    outer loop
      vertex 1.918390e-01 8.246498e-01 -7.907232e-01
      vertex 1.654500e-01 7.357368e-01 -7.284656e-01
      vertex 1.678279e-01 7.133367e-01 -7.860274e-01
    endloop
  endfacet
  facet normal 9.715151e-01 -2.045134e-01 1.197195e-01
    outer loop
      vertex 1.918390e-01 8.246498e-01 -7.907232e-01
      vertex 1.678279e-01 7.133367e-01 -7.860274e-01
      vertex 1.945962e-01 8.035276e-01 -8.491797e-01
    endloop
  endfacet
  facet normal -0.000000e+00 3.408006e-02 9.994191e-01
    outer loop
      vertex -2.571588e-01 9.146570e-01 -5.311428e-01
      vertex -1.829335e-01 9.146570e-01 -5.311428e-01
      vertex -1.928278e-01 9.652111e-01 -5.328667e-01
    endloop
  endfacet
  facet normal 5.085843e-01 1.285697e-01 8.513588e-01
    outer loop
      vertex -1.829335e-01 9.146570e-01 -5.311428e-01
      vertex -1.063671e-01 9.979418e-01 -5.894595e-01
      vertex -1.928278e-01 9.652111e-01 -5.328667e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.656488e-01 5.006517e-01
    outer loop
      vertex -1.063671e-01 9.979418e-01 -5.894595e-01
      vertex -1.673703e-01 9.979418e-01 -5.894595e-01
      vertex -1.928278e-01 9.652111e-01 -5.328667e-01
    endloop
  endfacet
  facet normal -3.049451e-01 8.774349e-01 3.702924e-01
    outer loop
      vertex -1.673703e-01 9.979418e-01 -5.894595e-01
      vertex -2.571588e-01 9.536477e-01 -5.584444e-01
      vertex -1.928278e-01 9.652111e-01 -5.328667e-01
    endloop
  endfacet
  facet normal -3.940897e-01 5.271580e-01 7.528597e-01
    outer loop
      vertex -2.571588e-01 9.536477e-01 -5.584444e-01
      vertex -2.571588e-01 9.146570e-01 -5.311428e-01
      vertex -1.928278e-01 9.652111e-01 -5.328667e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -2.611045e-01 8.934884e-01 -5.895669e-01
      vertex -1.079991e-01 9.780511e-01 -6.487783e-01
      vertex -1.857404e-01 8.934884e-01 -5.895669e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -2.611045e-01 8.934884e-01 -5.895669e-01
      vertex -1.699383e-01 9.780511e-01 -6.487783e-01
      vertex -1.079991e-01 9.780511e-01 -6.487783e-01
    endloop
  endfacet
  facet normal -2.067029e-15 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -2.611045e-01 8.934884e-01 -5.895669e-01
      vertex -2.611045e-01 9.330773e-01 -6.172873e-01
      vertex -1.699383e-01 9.780511e-01 -6.487783e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.401883e-01 -3.406551e-01
    outer loop
      vertex -2.571588e-01 9.146570e-01 -5.311428e-01
      vertex -1.829335e-01 9.146570e-01 -5.311428e-01
      vertex -1.857404e-01 8.934884e-01 -5.895669e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.401883e-01 -3.406551e-01
    outer loop
      vertex -2.571588e-01 9.146570e-01 -5.311428e-01
      vertex -1.857404e-01 8.934884e-01 -5.895669e-01
      vertex -2.611045e-01 8.934884e-01 -5.895669e-01
    endloop
  endfacet
  facet normal -7.833833e-01 5.954698e-01 -1.781188e-01
    outer loop
      vertex -1.829335e-01 9.146570e-01 -5.311428e-01
      vertex -1.063671e-01 9.979418e-01 -5.894595e-01
      vertex -1.079991e-01 9.780511e-01 -6.487783e-01
    endloop
  endfacet
  facet normal -7.833833e-01 5.954698e-01 -1.781188e-01
    outer loop
      vertex -1.829335e-01 9.146570e-01 -5.311428e-01
      vertex -1.079991e-01 9.780511e-01 -6.487783e-01
      vertex -1.857404e-01 8.934884e-01 -5.895669e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.481171e-01 3.179212e-01
    outer loop
      vertex -1.063671e-01 9.979418e-01 -5.894595e-01
      vertex -1.673703e-01 9.979418e-01 -5.894595e-01
      vertex -1.699383e-01 9.780511e-01 -6.487783e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.481171e-01 3.179212e-01
    outer loop
      vertex -1.063671e-01 9.979418e-01 -5.894595e-01
      vertex -1.699383e-01 9.780511e-01 -6.487783e-01
      vertex -1.079991e-01 9.780511e-01 -6.487783e-01
    endloop
  endfacet
  facet normal 4.974033e-01 -8.287730e-01 2.563693e-01
    outer loop
      vertex -1.673703e-01 9.979418e-01 -5.894595e-01
      vertex -2.571588e-01 9.536477e-01 -5.584444e-01
      vertex -2.611045e-01 9.330773e-01 -6.172873e-01
    endloop
  endfacet
  facet normal 4.974033e-01 -8.287730e-01 2.563693e-01
    outer loop
      vertex -1.673703e-01 9.979418e-01 -5.894595e-01
      vertex -2.611045e-01 9.330773e-01 -6.172873e-01
      vertex -1.699383e-01 9.780511e-01 -6.487783e-01
    endloop
  endfacet
  facet normal 9.978447e-01 -3.763810e-02 -5.375278e-02
    outer loop
      vertex -2.571588e-01 9.536477e-01 -5.584444e-01
      vertex -2.571588e-01 9.146570e-01 -5.311428e-01
      vertex -2.611045e-01 8.934884e-01 -5.895669e-01
    endloop
  endfacet
  facet normal 9.978447e-01 -3.763810e-02 -5.375278e-02
    outer loop
      vertex -2.571588e-01 9.536477e-01 -5.584444e-01
      vertex -2.611045e-01 8.934884e-01 -5.895669e-01
      vertex -2.611045e-01 9.330773e-01 -6.172873e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.751354e-02 9.952342e-01
    outer loop
      vertex 1.846197e-01 9.007421e-01 -5.694758e-01
      vertex 3.394263e-01 9.007421e-01 -5.694758e-01
      vertex 1.982626e-01 9.549260e-01 -5.641668e-01
    endloop
  endfacet
  facet normal 3.547220e-01 8.989720e-01 2.569469e-01
    outer loop
      vertex 3.394263e-01 9.007421e-01 -5.694758e-01
      vertex 1.688997e-01 9.848657e-01 -6.283797e-01
      vertex 1.982626e-01 9.549260e-01 -5.641668e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.063253e-01 4.225806e-01
    outer loop
      vertex 1.688997e-01 9.848657e-01 -6.283797e-01
      vertex 1.072822e-01 9.848657e-01 -6.283797e-01
      vertex 1.982626e-01 9.549260e-01 -5.641668e-01
    endloop
  endfacet
  facet normal -5.621509e-01 6.072890e-02 8.248020e-01
    outer loop
      vertex 1.072822e-01 9.848657e-01 -6.283797e-01
      vertex 1.846197e-01 9.007421e-01 -5.694758e-01
      vertex 1.982626e-01 9.549260e-01 -5.641668e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 1.874242e-01 8.795732e-01 -6.278996e-01
      vertex 1.714654e-01 9.649747e-01 -6.876984e-01
      vertex 3.445824e-01 8.795732e-01 -6.278996e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 1.874242e-01 8.795732e-01 -6.278996e-01
      vertex 1.089118e-01 9.649747e-01 -6.876984e-01
      vertex 1.714654e-01 9.649747e-01 -6.876984e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.401863e-01 -3.406607e-01
    outer loop
      vertex 1.846197e-01 9.007421e-01 -5.694758e-01
      vertex 3.394263e-01 9.007421e-01 -5.694758e-01
      vertex 3.445824e-01 8.795732e-01 -6.278996e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.401863e-01 -3.406607e-01
    outer loop
      vertex 1.846197e-01 9.007421e-01 -5.694758e-01
      vertex 3.445824e-01 8.795732e-01 -6.278996e-01
      vertex 1.874242e-01 8.795732e-01 -6.278996e-01
    endloop
  endfacet
  facet normal -4.974066e-01 -8.287642e-01 2.563914e-01
    outer loop
      vertex 3.394263e-01 9.007421e-01 -5.694758e-01
      vertex 1.688997e-01 9.848657e-01 -6.283797e-01
      vertex 1.714654e-01 9.649747e-01 -6.876984e-01
    endloop
  endfacet
  facet normal -4.974066e-01 -8.287642e-01 2.563914e-01
    outer loop
      vertex 3.394263e-01 9.007421e-01 -5.694758e-01
      vertex 1.714654e-01 9.649747e-01 -6.876984e-01
      vertex 3.445824e-01 8.795732e-01 -6.278996e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.481153e-01 3.179268e-01
    outer loop
      vertex 1.688997e-01 9.848657e-01 -6.283797e-01
      vertex 1.072822e-01 9.848657e-01 -6.283797e-01
      vertex 1.089118e-01 9.649747e-01 -6.876984e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -9.481153e-01 3.179268e-01
    outer loop
      vertex 1.688997e-01 9.848657e-01 -6.283797e-01
      vertex 1.089118e-01 9.649747e-01 -6.876984e-01
      vertex 1.714654e-01 9.649747e-01 -6.876984e-01
    endloop
  endfacet
  facet normal 7.833887e-01 5.954539e-01 -1.781485e-01
    outer loop
      vertex 1.072822e-01 9.848657e-01 -6.283797e-01
      vertex 1.846197e-01 9.007421e-01 -5.694758e-01
      vertex 1.874242e-01 8.795732e-01 -6.278996e-01
    endloop
  endfacet
  facet normal 7.833887e-01 5.954539e-01 -1.781485e-01
    outer loop
      vertex 1.072822e-01 9.848657e-01 -6.283797e-01
      vertex 1.874242e-01 8.795732e-01 -6.278996e-01
      vertex 1.089118e-01 9.649747e-01 -6.876984e-01
    endloop
  endfacet
  facet normal 3.420189e-01 -7.955516e-01 -5.001208e-01
    outer loop
      vertex -2.415005e-01 1.012476e+00 -3.059534e-01
      vertex -1.646229e-01 1.071514e+00 -3.472926e-01
      vertex -1.763600e-01 1.010585e+00 -2.583981e-01
    endloop
  endfacet
  facet normal -1.477473e-01 -8.065884e-01 -5.723512e-01
    outer loop
      vertex -1.646229e-01 1.071514e+00 -3.472926e-01
      vertex -7.874747e-02 1.040250e+00 -3.254010e-01
      vertex -1.763600e-01 1.010585e+00 -2.583981e-01
    endloop
  endfacet
  facet normal -5.084632e-01 -2.119548e-01 -8.345899e-01
    outer loop
      vertex -7.874747e-02 1.040250e+00 -3.254010e-01
      vertex -1.646229e-01 9.230083e-01 -2.433075e-01
      vertex -1.763600e-01 1.010585e+00 -2.583981e-01
    endloop
  endfacet
  facet normal 1.091491e-01 -1.545715e-01 -9.819339e-01
    outer loop
      vertex -1.646229e-01 9.230083e-01 -2.433075e-01
      vertex -2.415005e-01 9.387519e-01 -2.543313e-01
      vertex -1.763600e-01 1.010585e+00 -2.583981e-01
    endloop
  endfacet
  facet normal 5.026024e-01 -4.958670e-01 -7.081714e-01
    outer loop
      vertex -2.415005e-01 9.387519e-01 -2.543313e-01
      vertex -2.415005e-01 1.012476e+00 -3.059534e-01
      vertex -1.763600e-01 1.010585e+00 -2.583981e-01
    endloop
  endfacet
  facet normal 4.371681e-16 5.735764e-01 8.191520e-01
    outer loop
      vertex -2.454489e-01 9.915189e-01 -3.645256e-01
      vertex -8.003493e-02 1.019747e+00 -3.842912e-01
      vertex -1.673144e-01 1.051523e+00 -4.065407e-01
    endloop
  endfacet
  facet normal 5.664484e-16 5.735764e-01 8.191520e-01
    outer loop
      vertex -2.454489e-01 9.915189e-01 -3.645256e-01
      vertex -1.673144e-01 9.005886e-01 -3.008555e-01
      vertex -8.003493e-02 1.019747e+00 -3.842912e-01
    endloop
  endfacet
  facet normal -9.708675e-16 5.735764e-01 8.191520e-01
    outer loop
      vertex -2.454489e-01 9.915189e-01 -3.645256e-01
      vertex -2.454489e-01 9.165896e-01 -3.120595e-01
      vertex -1.673144e-01 9.005886e-01 -3.008555e-01
    endloop
  endfacet
  facet normal -6.643308e-01 7.168323e-01 -2.116979e-01
    outer loop
      vertex -2.415005e-01 1.012476e+00 -3.059534e-01
      vertex -1.646229e-01 1.071514e+00 -3.472926e-01
      vertex -1.673144e-01 1.051523e+00 -4.065407e-01
    endloop
  endfacet
  facet normal -6.643308e-01 7.168323e-01 -2.116979e-01
    outer loop
      vertex -2.415005e-01 1.012476e+00 -3.059534e-01
      vertex -1.673144e-01 1.051523e+00 -4.065407e-01
      vertex -2.454489e-01 9.915189e-01 -3.645256e-01
    endloop
  endfacet
  facet normal 3.940177e-01 8.652924e-01 -3.098695e-01
    outer loop
      vertex -1.646229e-01 1.071514e+00 -3.472926e-01
      vertex -7.874747e-02 1.040250e+00 -3.254010e-01
      vertex -8.003493e-02 1.019747e+00 -3.842912e-01
    endloop
  endfacet
  facet normal 3.940177e-01 8.652924e-01 -3.098695e-01
    outer loop
      vertex -1.646229e-01 1.071514e+00 -3.472926e-01
      vertex -8.003493e-02 1.019747e+00 -3.842912e-01
      vertex -1.673144e-01 1.051523e+00 -4.065407e-01
    endloop
  endfacet
  facet normal 8.461851e-01 -5.087346e-01 1.586189e-01
    outer loop
      vertex -7.874747e-02 1.040250e+00 -3.254010e-01
      vertex -1.646229e-01 9.230083e-01 -2.433075e-01
      vertex -1.673144e-01 9.005886e-01 -3.008555e-01
    endloop
  endfacet
  facet normal 8.461851e-01 -5.087346e-01 1.586189e-01
    outer loop
      vertex -7.874747e-02 1.040250e+00 -3.254010e-01
      vertex -1.673144e-01 9.005886e-01 -3.008555e-01
      vertex -8.003493e-02 1.019747e+00 -3.842912e-01
    endloop
  endfacet
  facet normal -2.365752e-01 -9.015423e-01 3.622895e-01
    outer loop
      vertex -1.646229e-01 9.230083e-01 -2.433075e-01
      vertex -2.415005e-01 9.387519e-01 -2.543313e-01
      vertex -2.454489e-01 9.165896e-01 -3.120595e-01
    endloop
  endfacet
  facet normal -2.365752e-01 -9.015423e-01 3.622895e-01
    outer loop
      vertex -1.646229e-01 9.230083e-01 -2.433075e-01
      vertex -2.454489e-01 9.165896e-01 -3.120595e-01
      vertex -1.673144e-01 9.005886e-01 -3.008555e-01
    endloop
  endfacet
  facet normal -9.978418e-01 3.766327e-02 5.378872e-02
    outer loop
      vertex -2.415005e-01 9.387519e-01 -2.543313e-01
      vertex -2.415005e-01 1.012476e+00 -3.059534e-01
      vertex -2.454489e-01 9.915189e-01 -3.645256e-01
    endloop
  endfacet
  facet normal -9.978418e-01 3.766327e-02 5.378872e-02
    outer loop
      vertex -2.415005e-01 9.387519e-01 -2.543313e-01
      vertex -2.454489e-01 9.915189e-01 -3.645256e-01
      vertex -2.454489e-01 9.165896e-01 -3.120595e-01
    endloop
  endfacet
  facet normal 5.534729e-01 -1.660698e-01 -8.161425e-01
    outer loop
      vertex 1.697273e-01 8.794542e-01 -3.550964e-01
      vertex 8.112456e-02 1.000419e+00 -4.397972e-01
      vertex 1.846790e-01 9.723619e-01 -3.638618e-01
    endloop
  endfacet
  facet normal 1.661319e-01 -8.295912e-01 -5.330841e-01
    outer loop
      vertex 8.112456e-02 1.000419e+00 -4.397972e-01
      vertex 1.697273e-01 1.032677e+00 -4.623841e-01
      vertex 1.846790e-01 9.723619e-01 -3.638618e-01
    endloop
  endfacet
  facet normal -3.875664e-01 -8.112377e-01 -4.378193e-01
    outer loop
      vertex 1.697273e-01 1.032677e+00 -4.623841e-01
      vertex 3.272434e-01 9.117116e-01 -3.776833e-01
      vertex 1.846790e-01 9.723619e-01 -3.638618e-01
    endloop
  endfacet
  facet normal -1.269199e-01 -7.290406e-02 -9.892302e-01
    outer loop
      vertex 3.272434e-01 9.117116e-01 -3.776833e-01
      vertex 1.697273e-01 8.794542e-01 -3.550964e-01
      vertex 1.846790e-01 9.723619e-01 -3.638618e-01
    endloop
  endfacet
  facet normal 1.420027e-15 5.735764e-01 8.191520e-01
    outer loop
      vertex 1.724168e-01 8.570344e-01 -4.126444e-01
      vertex 1.724168e-01 1.012685e+00 -5.216321e-01
      vertex 8.241006e-02 9.799165e-01 -4.986874e-01
    endloop
  endfacet
  facet normal -3.138007e-16 5.735764e-01 8.191520e-01
    outer loop
      vertex 1.724168e-01 8.570344e-01 -4.126444e-01
      vertex 3.324289e-01 8.898030e-01 -4.355892e-01
      vertex 1.724168e-01 1.012685e+00 -5.216321e-01
    endloop
  endfacet
  facet normal -8.461889e-01 -5.087208e-01 1.586426e-01
    outer loop
      vertex 1.697273e-01 8.794542e-01 -3.550964e-01
      vertex 8.112456e-02 1.000419e+00 -4.397972e-01
      vertex 8.241006e-02 9.799165e-01 -4.986874e-01
    endloop
  endfacet
  facet normal -8.461889e-01 -5.087208e-01 1.586426e-01
    outer loop
      vertex 1.697273e-01 8.794542e-01 -3.550964e-01
      vertex 8.241006e-02 9.799165e-01 -4.986874e-01
      vertex 1.724168e-01 8.570344e-01 -4.126444e-01
    endloop
  endfacet
  facet normal -3.940166e-01 8.652968e-01 -3.098586e-01
    outer loop
      vertex 8.112456e-02 1.000419e+00 -4.397972e-01
      vertex 1.697273e-01 1.032677e+00 -4.623841e-01
      vertex 1.724168e-01 1.012685e+00 -5.216321e-01
    endloop
  endfacet
  facet normal -3.940166e-01 8.652968e-01 -3.098586e-01
    outer loop
      vertex 8.112456e-02 1.000419e+00 -4.397972e-01
      vertex 1.724168e-01 1.012685e+00 -5.216321e-01
      vertex 8.241006e-02 9.799165e-01 -4.986874e-01
    endloop
  endfacet
  facet normal 6.643344e-01 7.168233e-01 -2.117173e-01
    outer loop
      vertex 1.697273e-01 1.032677e+00 -4.623841e-01
      vertex 3.272434e-01 9.117116e-01 -3.776833e-01
      vertex 3.324289e-01 8.898030e-01 -4.355892e-01
    endloop
  endfacet
  facet normal 6.643344e-01 7.168233e-01 -2.117173e-01
    outer loop
      vertex 1.697273e-01 1.032677e+00 -4.623841e-01
      vertex 3.324289e-01 8.898030e-01 -4.355892e-01
      vertex 1.724168e-01 1.012685e+00 -5.216321e-01
    endloop
  endfacet
  facet normal 2.365749e-01 -9.015449e-01 3.622832e-01
    outer loop
      vertex 3.272434e-01 9.117116e-01 -3.776833e-01
      vertex 1.697273e-01 8.794542e-01 -3.550964e-01
      vertex 1.724168e-01 8.570344e-01 -4.126444e-01
    endloop
  endfacet
  facet normal 2.365749e-01 -9.015449e-01 3.622832e-01
    outer loop
      vertex 3.272434e-01 9.117116e-01 -3.776833e-01
      vertex 1.724168e-01 8.570344e-01 -4.126444e-01
      vertex 3.324289e-01 8.898030e-01 -4.355892e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -3.647086e-01 9.311217e-01
    outer loop
      vertex -1.642210e-01 -7.588455e-01 3.608684e-01
      vertex 3.387472e-02 -7.588455e-01 3.608684e-01
      vertex -6.459188e-02 -7.175686e-01 3.770361e-01
    endloop
  endfacet
  facet normal 3.510758e-01 5.370666e-01 7.670106e-01
    outer loop
      vertex 3.387472e-02 -7.588455e-01 3.608684e-01
      vertex 3.387472e-02 -7.304975e-01 3.410190e-01
      vertex -6.459188e-02 -7.175686e-01 3.770361e-01
    endloop
  endfacet
  facet normal 6.221679e-16 9.411967e-01 -3.378592e-01
    outer loop
      vertex 3.387472e-02 -7.304975e-01 3.410190e-01
      vertex -1.642210e-01 -7.304975e-01 3.410190e-01
      vertex -6.459188e-02 -7.175686e-01 3.770361e-01
    endloop
  endfacet
  facet normal -3.474765e-01 5.378361e-01 7.681096e-01
    outer loop
      vertex -1.642210e-01 -7.304975e-01 3.410190e-01
      vertex -1.642210e-01 -7.588455e-01 3.608684e-01
      vertex -6.459188e-02 -7.175686e-01 3.770361e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -1.666012e-01 -8.030978e-01 3.186078e-01
      vertex 3.436570e-02 -7.743390e-01 2.984706e-01
      vertex 3.436570e-02 -8.030978e-01 3.186078e-01
    endloop
  endfacet
  facet normal 1.382998e-16 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -1.666012e-01 -8.030978e-01 3.186078e-01
      vertex -1.666012e-01 -7.743390e-01 2.984706e-01
      vertex 3.436570e-02 -7.743390e-01 2.984706e-01
    endloop
  endfacet
  facet normal 0.000000e+00 6.906453e-01 -7.231937e-01
    outer loop
      vertex -1.642210e-01 -7.588455e-01 3.608684e-01
      vertex 3.387472e-02 -7.588455e-01 3.608684e-01
      vertex 3.436570e-02 -8.030978e-01 3.186078e-01
    endloop
  endfacet
  facet normal 0.000000e+00 6.906453e-01 -7.231937e-01
    outer loop
      vertex -1.642210e-01 -7.588455e-01 3.608684e-01
      vertex 3.436570e-02 -8.030978e-01 3.186078e-01
      vertex -1.666012e-01 -8.030978e-01 3.186078e-01
    endloop
  endfacet
  facet normal -9.999665e-01 -4.693414e-03 -6.702891e-03
    outer loop
      vertex 3.387472e-02 -7.588455e-01 3.608684e-01
      vertex 3.387472e-02 -7.304975e-01 3.410190e-01
      vertex 3.436570e-02 -7.743390e-01 2.984706e-01
    endloop
  endfacet
  facet normal -9.999665e-01 -4.693414e-03 -6.702891e-03
    outer loop
      vertex 3.387472e-02 -7.588455e-01 3.608684e-01
      vertex 3.436570e-02 -7.743390e-01 2.984706e-01
      vertex 3.436570e-02 -8.030978e-01 3.186078e-01
    endloop
  endfacet
  facet normal -5.914126e-16 -6.964449e-01 7.176102e-01
    outer loop
      vertex 3.387472e-02 -7.304975e-01 3.410190e-01
      vertex -1.642210e-01 -7.304975e-01 3.410190e-01
      vertex -1.666012e-01 -7.743390e-01 2.984706e-01
    endloop
  endfacet
  facet normal -7.770918e-16 -6.964449e-01 7.176102e-01
    outer loop
      vertex 3.387472e-02 -7.304975e-01 3.410190e-01
      vertex -1.666012e-01 -7.743390e-01 2.984706e-01
      vertex 3.436570e-02 -7.743390e-01 2.984706e-01
    endloop
  endfacet
  facet normal 9.992141e-01 -2.273604e-02 -3.247043e-02
    outer loop
      vertex -1.642210e-01 -7.304975e-01 3.410190e-01
      vertex -1.642210e-01 -7.588455e-01 3.608684e-01
      vertex -1.666012e-01 -8.030978e-01 3.186078e-01
    endloop
  endfacet
  facet normal 9.992141e-01 -2.273604e-02 -3.247043e-02
    outer loop
      vertex -1.642210e-01 -7.304975e-01 3.410190e-01
      vertex -1.666012e-01 -8.030978e-01 3.186078e-01
      vertex -1.666012e-01 -7.743390e-01 2.984706e-01
    endloop
  endfacet
  facet normal 6.614259e-01 4.301884e-01 6.143727e-01
    outer loop
      vertex 2.934307e-02 -3.311644e-01 7.374552e-01
      vertex 2.934307e-02 -7.930009e-02 5.610980e-01
      vertex -5.527955e-02 -1.532127e-01 7.039558e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.881653e-01 4.595241e-01
    outer loop
      vertex 2.934307e-02 -7.930009e-02 5.610980e-01
      vertex -1.422520e-01 -7.930009e-02 5.610980e-01
      vertex -5.527955e-02 -1.532127e-01 7.039558e-01
    endloop
  endfacet
  facet normal -6.511933e-01 4.352940e-01 6.216642e-01
    outer loop
      vertex -1.422520e-01 -7.930009e-02 5.610980e-01
      vertex -1.422520e-01 -3.311644e-01 7.374552e-01
      vertex -5.527955e-02 -1.532127e-01 7.039558e-01
    endloop
  endfacet
  facet normal -5.161375e-16 1.850009e-01 9.827383e-01
    outer loop
      vertex -1.422520e-01 -3.311644e-01 7.374552e-01
      vertex 2.934307e-02 -3.311644e-01 7.374552e-01
      vertex -5.527955e-02 -1.532127e-01 7.039558e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 2.983405e-02 -3.750948e-01 6.949691e-01
      vertex -1.446322e-01 -1.190162e-01 5.156610e-01
      vertex 2.983405e-02 -1.190162e-01 5.156610e-01
    endloop
  endfacet
  facet normal -3.649977e-16 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 2.983405e-02 -3.750948e-01 6.949691e-01
      vertex -1.446322e-01 -3.750948e-01 6.949691e-01
      vertex -1.446322e-01 -1.190162e-01 5.156610e-01
    endloop
  endfacet
  facet normal -9.999665e-01 -4.693414e-03 -6.702891e-03
    outer loop
      vertex 2.934307e-02 -3.311644e-01 7.374552e-01
      vertex 2.934307e-02 -7.930009e-02 5.610980e-01
      vertex 2.983405e-02 -1.190162e-01 5.156610e-01
    endloop
  endfacet
  facet normal -9.999665e-01 -4.693414e-03 -6.702891e-03
    outer loop
      vertex 2.934307e-02 -3.311644e-01 7.374552e-01
      vertex 2.983405e-02 -1.190162e-01 5.156610e-01
      vertex 2.983405e-02 -3.750948e-01 6.949691e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -7.529154e-01 6.581173e-01
    outer loop
      vertex 2.934307e-02 -7.930009e-02 5.610980e-01
      vertex -1.422520e-01 -7.930009e-02 5.610980e-01
      vertex -1.446322e-01 -1.190162e-01 5.156610e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -7.529154e-01 6.581173e-01
    outer loop
      vertex 2.934307e-02 -7.930009e-02 5.610980e-01
      vertex -1.446322e-01 -1.190162e-01 5.156610e-01
      vertex 2.983405e-02 -1.190162e-01 5.156610e-01
    endloop
  endfacet
  facet normal 9.992141e-01 -2.273604e-02 -3.247043e-02
    outer loop
      vertex -1.422520e-01 -7.930009e-02 5.610980e-01
      vertex -1.422520e-01 -3.311644e-01 7.374552e-01
      vertex -1.446322e-01 -3.750948e-01 6.949691e-01
    endloop
  endfacet
  facet normal 9.992141e-01 -2.273604e-02 -3.247043e-02
    outer loop
      vertex -1.422520e-01 -7.930009e-02 5.610980e-01
      vertex -1.446322e-01 -3.750948e-01 6.949691e-01
      vertex -1.446322e-01 -1.190162e-01 5.156610e-01
    endloop
  endfacet
  facet normal 9.148709e-16 6.951917e-01 -7.188244e-01
    outer loop
      vertex -1.422520e-01 -3.311644e-01 7.374552e-01
      vertex 2.934307e-02 -3.311644e-01 7.374552e-01
      vertex 2.983405e-02 -3.750948e-01 6.949691e-01
    endloop
  endfacet
  facet normal 4.270768e-16 6.951917e-01 -7.188244e-01
    outer loop
      vertex -1.422520e-01 -3.311644e-01 7.374552e-01
      vertex 2.983405e-02 -3.750948e-01 6.949691e-01
      vertex -1.446322e-01 -3.750948e-01 6.949691e-01
    endloop
  endfacet
  facet normal 5.863222e-01 4.646416e-01 6.635770e-01
    outer loop
      vertex 3.498677e-02 -5.472339e-01 4.679608e-02
      vertex 3.498677e-02 -2.544396e-01 -1.582207e-01
      vertex -6.616007e-02 -3.546889e-01 1.345712e-03
    endloop
  endfacet
  facet normal 0.000000e+00 8.467552e-01 5.319828e-01
    outer loop
      vertex 3.498677e-02 -2.544396e-01 -1.582207e-01
      vertex -1.696121e-01 -2.544396e-01 -1.582207e-01
      vertex -6.616007e-02 -3.546889e-01 1.345712e-03
    endloop
  endfacet
  facet normal -5.776498e-01 4.682017e-01 6.686613e-01
    outer loop
      vertex -1.696121e-01 -2.544396e-01 -1.582207e-01
      vertex -1.696121e-01 -5.472339e-01 4.679608e-02
      vertex -6.616007e-02 -3.546889e-01 1.345712e-03
    endloop
  endfacet
  facet normal -0.000000e+00 2.297368e-01 9.732528e-01
    outer loop
      vertex -1.696121e-01 -5.472339e-01 4.679608e-02
      vertex 3.498677e-02 -5.472339e-01 4.679608e-02
      vertex -6.616007e-02 -3.546889e-01 1.345712e-03
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 3.547775e-02 -5.871101e-01 1.471186e-03
      vertex -1.719923e-01 -2.902068e-01 -2.064227e-01
      vertex 3.547775e-02 -2.902068e-01 -2.064227e-01
    endloop
  endfacet
  facet normal -0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 3.547775e-02 -5.871101e-01 1.471186e-03
      vertex -1.719923e-01 -5.871101e-01 1.471186e-03
      vertex -1.719923e-01 -2.902068e-01 -2.064227e-01
    endloop
  endfacet
  facet normal -9.999665e-01 -4.693414e-03 -6.702891e-03
    outer loop
      vertex 3.498677e-02 -5.472339e-01 4.679608e-02
      vertex 3.498677e-02 -2.544396e-01 -1.582207e-01
      vertex 3.547775e-02 -2.902068e-01 -2.064227e-01
    endloop
  endfacet
  facet normal -9.999665e-01 -4.693414e-03 -6.702891e-03
    outer loop
      vertex 3.498677e-02 -5.472339e-01 4.679608e-02
      vertex 3.547775e-02 -2.902068e-01 -2.064227e-01
      vertex 3.547775e-02 -5.871101e-01 1.471186e-03
    endloop
  endfacet
  facet normal 0.000000e+00 -8.030618e-01 5.958958e-01
    outer loop
      vertex 3.498677e-02 -2.544396e-01 -1.582207e-01
      vertex -1.696121e-01 -2.544396e-01 -1.582207e-01
      vertex -1.719923e-01 -2.902068e-01 -2.064227e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -8.030618e-01 5.958958e-01
    outer loop
      vertex 3.498677e-02 -2.544396e-01 -1.582207e-01
      vertex -1.719923e-01 -2.902068e-01 -2.064227e-01
      vertex 3.547775e-02 -2.902068e-01 -2.064227e-01
    endloop
  endfacet
  facet normal 9.992141e-01 -2.273604e-02 -3.247043e-02
    outer loop
      vertex -1.696121e-01 -2.544396e-01 -1.582207e-01
      vertex -1.696121e-01 -5.472339e-01 4.679608e-02
      vertex -1.719923e-01 -5.871101e-01 1.471186e-03
    endloop
  endfacet
  facet normal 9.992141e-01 -2.273604e-02 -3.247043e-02
    outer loop
      vertex -1.696121e-01 -2.544396e-01 -1.582207e-01
      vertex -1.719923e-01 -5.871101e-01 1.471186e-03
      vertex -1.719923e-01 -2.902068e-01 -2.064227e-01
    endloop
  endfacet
  facet normal 0.000000e+00 7.507936e-01 -6.605368e-01
    outer loop
      vertex -1.696121e-01 -5.472339e-01 4.679608e-02
      vertex 3.498677e-02 -5.472339e-01 4.679608e-02
      vertex 3.547775e-02 -5.871101e-01 1.471186e-03
    endloop
  endfacet
  facet normal 0.000000e+00 7.507936e-01 -6.605368e-01
    outer loop
      vertex -1.696121e-01 -5.472339e-01 4.679608e-02
      vertex 3.547775e-02 -5.871101e-01 1.471186e-03
      vertex -1.719923e-01 -5.871101e-01 1.471186e-03
    endloop
  endfacet
  facet normal 6.482733e-01 4.367255e-01 6.237087e-01
    outer loop
      vertex 3.302248e-02 -1.227231e-01 4.259204e-02
      vertex 3.302248e-02 1.926767e-01 -1.782533e-01
      vertex -6.225630e-02 8.039385e-02 -6.006865e-04
    endloop
  endfacet
  facet normal 0.000000e+00 8.453144e-01 5.342692e-01
    outer loop
      vertex 3.302248e-02 1.926767e-01 -1.782533e-01
      vertex -1.600894e-01 1.926767e-01 -1.782533e-01
      vertex -6.225630e-02 8.039385e-02 -6.006865e-04
    endloop
  endfacet
  facet normal -6.382978e-01 4.415331e-01 6.305747e-01
    outer loop
      vertex -1.600894e-01 1.926767e-01 -1.782533e-01
      vertex -1.600894e-01 -1.227231e-01 4.259204e-02
      vertex -6.225630e-02 8.039385e-02 -6.006865e-04
    endloop
  endfacet
  facet normal -8.079406e-17 2.079987e-01 9.781291e-01
    outer loop
      vertex -1.600894e-01 -1.227231e-01 4.259204e-02
      vertex 3.302248e-02 -1.227231e-01 4.259204e-02
      vertex -6.225630e-02 8.039385e-02 -6.006865e-04
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 3.351346e-02 -1.586596e-01 -5.491442e-03
      vertex -1.624696e-01 1.614296e-01 -2.296203e-01
      vertex 3.351346e-02 1.614296e-01 -2.296203e-01
    endloop
  endfacet
  facet normal 1.155287e-17 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 3.351346e-02 -1.586596e-01 -5.491442e-03
      vertex -1.624696e-01 -1.586596e-01 -5.491442e-03
      vertex -1.624696e-01 1.614296e-01 -2.296203e-01
    endloop
  endfacet
  facet normal -9.999665e-01 -4.693414e-03 -6.702891e-03
    outer loop
      vertex 3.302248e-02 -1.227231e-01 4.259204e-02
      vertex 3.302248e-02 1.926767e-01 -1.782533e-01
      vertex 3.351346e-02 1.614296e-01 -2.296203e-01
    endloop
  endfacet
  facet normal -9.999665e-01 -4.693414e-03 -6.702891e-03
    outer loop
      vertex 3.302248e-02 -1.227231e-01 4.259204e-02
      vertex 3.351346e-02 1.614296e-01 -2.296203e-01
      vertex 3.351346e-02 -1.586596e-01 -5.491442e-03
    endloop
  endfacet
  facet normal 0.000000e+00 -8.543446e-01 5.197069e-01
    outer loop
      vertex 3.302248e-02 1.926767e-01 -1.782533e-01
      vertex -1.600894e-01 1.926767e-01 -1.782533e-01
      vertex -1.624696e-01 1.614296e-01 -2.296203e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -8.543446e-01 5.197069e-01
    outer loop
      vertex 3.302248e-02 1.926767e-01 -1.782533e-01
      vertex -1.624696e-01 1.614296e-01 -2.296203e-01
      vertex 3.351346e-02 1.614296e-01 -2.296203e-01
    endloop
  endfacet
  facet normal 9.992141e-01 -2.273604e-02 -3.247043e-02
    outer loop
      vertex -1.600894e-01 1.926767e-01 -1.782533e-01
      vertex -1.600894e-01 -1.227231e-01 4.259204e-02
      vertex -1.624696e-01 -1.586596e-01 -5.491442e-03
    endloop
  endfacet
  facet normal 9.992141e-01 -2.273604e-02 -3.247043e-02
    outer loop
      vertex -1.600894e-01 1.926767e-01 -1.782533e-01
      vertex -1.624696e-01 -1.586596e-01 -5.491442e-03
      vertex -1.624696e-01 1.614296e-01 -2.296203e-01
    endloop
  endfacet
  facet normal 3.162977e-16 8.010074e-01 -5.986544e-01
    outer loop
      vertex -1.600894e-01 -1.227231e-01 4.259204e-02
      vertex 3.302248e-02 -1.227231e-01 4.259204e-02
      vertex 3.351346e-02 -1.586596e-01 -5.491442e-03
    endloop
  endfacet
  facet normal 3.501999e-16 8.010074e-01 -5.986544e-01
    outer loop
      vertex -1.600894e-01 -1.227231e-01 4.259204e-02
      vertex 3.351346e-02 -1.586596e-01 -5.491442e-03
      vertex -1.624696e-01 -1.586596e-01 -5.491442e-03
    endloop
  endfacet
  facet normal 3.929019e-01 5.274496e-01 7.532762e-01
    outer loop
      vertex 3.080313e-02 3.273452e-01 5.854252e-02
      vertex 3.080313e-02 3.750905e-01 2.511091e-02
      vertex -5.866175e-02 3.709492e-01 7.467474e-02
    endloop
  endfacet
  facet normal 0.000000e+00 9.965275e-01 8.326469e-02
    outer loop
      vertex 3.080313e-02 3.750905e-01 2.511091e-02
      vertex -1.493302e-01 3.750905e-01 2.511091e-02
      vertex -5.866175e-02 3.709492e-01 7.467474e-02
    endloop
  endfacet
  facet normal -3.884778e-01 5.285266e-01 7.548143e-01
    outer loop
      vertex -1.493302e-01 3.750905e-01 2.511091e-02
      vertex -1.493302e-01 3.273452e-01 5.854252e-02
      vertex -5.866175e-02 3.709492e-01 7.467474e-02
    endloop
  endfacet
  facet normal -2.890207e-16 -3.469851e-01 9.378707e-01
    outer loop
      vertex -1.493302e-01 3.273452e-01 5.854252e-02
      vertex 3.080313e-02 3.273452e-01 5.854252e-02
      vertex -5.866175e-02 3.709492e-01 7.467474e-02
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 3.129411e-02 2.959933e-01 7.248894e-03
      vertex -1.517104e-01 3.444996e-01 -2.671559e-02
      vertex 3.129411e-02 3.444996e-01 -2.671559e-02
    endloop
  endfacet
  facet normal 1.242375e-16 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 3.129411e-02 2.959933e-01 7.248894e-03
      vertex -1.517104e-01 2.959933e-01 7.248894e-03
      vertex -1.517104e-01 3.444996e-01 -2.671559e-02
    endloop
  endfacet
  facet normal -9.999665e-01 -4.693414e-03 -6.702891e-03
    outer loop
      vertex 3.080313e-02 3.273452e-01 5.854252e-02
      vertex 3.080313e-02 3.750905e-01 2.511091e-02
      vertex 3.129411e-02 3.444996e-01 -2.671559e-02
    endloop
  endfacet
  facet normal -9.999665e-01 -4.693414e-03 -6.702891e-03
    outer loop
      vertex 3.080313e-02 3.273452e-01 5.854252e-02
      vertex 3.129411e-02 3.444996e-01 -2.671559e-02
      vertex 3.129411e-02 2.959933e-01 7.248894e-03
    endloop
  endfacet
  facet normal 0.000000e+00 -8.611728e-01 5.083123e-01
    outer loop
      vertex 3.080313e-02 3.750905e-01 2.511091e-02
      vertex -1.493302e-01 3.750905e-01 2.511091e-02
      vertex -1.517104e-01 3.444996e-01 -2.671559e-02
    endloop
  endfacet
  facet normal 0.000000e+00 -8.611728e-01 5.083123e-01
    outer loop
      vertex 3.080313e-02 3.750905e-01 2.511091e-02
      vertex -1.517104e-01 3.444996e-01 -2.671559e-02
      vertex 3.129411e-02 3.444996e-01 -2.671559e-02
    endloop
  endfacet
  facet normal 9.992141e-01 -2.273604e-02 -3.247043e-02
    outer loop
      vertex -1.493302e-01 3.750905e-01 2.511091e-02
      vertex -1.493302e-01 3.273452e-01 5.854252e-02
      vertex -1.517104e-01 2.959933e-01 7.248894e-03
    endloop
  endfacet
  facet normal 9.992141e-01 -2.273604e-02 -3.247043e-02
    outer loop
      vertex -1.493302e-01 3.750905e-01 2.511091e-02
      vertex -1.517104e-01 2.959933e-01 7.248894e-03
      vertex -1.517104e-01 3.444996e-01 -2.671559e-02
    endloop
  endfacet
  facet normal 1.607154e-16 8.532388e-01 -5.215204e-01
    outer loop
      vertex -1.493302e-01 3.273452e-01 5.854252e-02
      vertex 3.080313e-02 3.273452e-01 5.854252e-02
      vertex 3.129411e-02 2.959933e-01 7.248894e-03
    endloop
  endfacet
  facet normal 7.883980e-17 8.532388e-01 -5.215204e-01
    outer loop
      vertex -1.493302e-01 3.273452e-01 5.854252e-02
      vertex 3.129411e-02 2.959933e-01 7.248894e-03
      vertex -1.517104e-01 2.959933e-01 7.248894e-03
    endloop
  endfacet
  facet normal 0.000000e+00 -2.320248e-01 9.727099e-01
    outer loop
      vertex 2.817969e-02 -8.390621e-01 2.842621e-01
      vertex 1.673014e-01 -8.390621e-01 2.842621e-01
      vertex 9.714961e-02 -8.056595e-01 2.922298e-01
    endloop
  endfacet
  facet normal 3.438225e-01 5.386082e-01 7.692122e-01
    outer loop
      vertex 1.673014e-01 -8.390621e-01 2.842621e-01
      vertex 1.673014e-01 -8.099693e-01 2.638911e-01
      vertex 9.714961e-02 -8.056595e-01 2.922298e-01
    endloop
  endfacet
  facet normal 7.889509e-16 9.886320e-01 -1.503555e-01
    outer loop
      vertex 1.673014e-01 -8.099693e-01 2.638911e-01
      vertex 2.817969e-02 -8.099693e-01 2.638911e-01
      vertex 9.714961e-02 -8.056595e-01 2.922298e-01
    endloop
  endfacet
  facet normal -3.490019e-01 5.375111e-01 7.676454e-01
    outer loop
      vertex 2.817969e-02 -8.099693e-01 2.638911e-01
      vertex 2.817969e-02 -8.390621e-01 2.842621e-01
      vertex 9.714961e-02 -8.056595e-01 2.922298e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 2.857767e-02 -8.833144e-01 2.420014e-01
      vertex 1.696642e-01 -8.538108e-01 2.213428e-01
      vertex 1.696642e-01 -8.833144e-01 2.420014e-01
    endloop
  endfacet
  facet normal -2.560324e-16 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 2.857767e-02 -8.833144e-01 2.420014e-01
      vertex 2.857767e-02 -8.538108e-01 2.213428e-01
      vertex 1.696642e-01 -8.538108e-01 2.213428e-01
    endloop
  endfacet
  facet normal 0.000000e+00 6.906453e-01 -7.231937e-01
    outer loop
      vertex 2.817969e-02 -8.390621e-01 2.842621e-01
      vertex 1.673014e-01 -8.390621e-01 2.842621e-01
      vertex 1.696642e-01 -8.833144e-01 2.420014e-01
    endloop
  endfacet
  facet normal 0.000000e+00 6.906453e-01 -7.231937e-01
    outer loop
      vertex 2.817969e-02 -8.390621e-01 2.842621e-01
      vertex 1.696642e-01 -8.833144e-01 2.420014e-01
      vertex 2.857767e-02 -8.833144e-01 2.420014e-01
    endloop
  endfacet
  facet normal -9.992255e-01 -2.256980e-02 -3.223302e-02
    outer loop
      vertex 1.673014e-01 -8.390621e-01 2.842621e-01
      vertex 1.673014e-01 -8.099693e-01 2.638911e-01
      vertex 1.696642e-01 -8.538108e-01 2.213428e-01
    endloop
  endfacet
  facet normal -9.992255e-01 -2.256980e-02 -3.223302e-02
    outer loop
      vertex 1.673014e-01 -8.390621e-01 2.842621e-01
      vertex 1.696642e-01 -8.538108e-01 2.213428e-01
      vertex 1.696642e-01 -8.833144e-01 2.420014e-01
    endloop
  endfacet
  facet normal -5.557790e-16 -6.964449e-01 7.176102e-01
    outer loop
      vertex 1.673014e-01 -8.099693e-01 2.638911e-01
      vertex 2.817969e-02 -8.099693e-01 2.638911e-01
      vertex 2.857767e-02 -8.538108e-01 2.213428e-01
    endloop
  endfacet
  facet normal -1.660361e-15 -6.964449e-01 7.176102e-01
    outer loop
      vertex 1.673014e-01 -8.099693e-01 2.638911e-01
      vertex 2.857767e-02 -8.538108e-01 2.213428e-01
      vertex 1.696642e-01 -8.538108e-01 2.213428e-01
    endloop
  endfacet
  facet normal 9.999780e-01 3.804444e-03 5.433310e-03
    outer loop
      vertex 2.817969e-02 -8.099693e-01 2.638911e-01
      vertex 2.817969e-02 -8.390621e-01 2.842621e-01
      vertex 2.857767e-02 -8.833144e-01 2.420014e-01
    endloop
  endfacet
  facet normal 9.999780e-01 3.804444e-03 5.433310e-03
    outer loop
      vertex 2.817969e-02 -8.099693e-01 2.638911e-01
      vertex 2.857767e-02 -8.833144e-01 2.420014e-01
      vertex 2.857767e-02 -8.538108e-01 2.213428e-01
    endloop
  endfacet
  facet normal 7.224982e-01 3.965551e-01 5.663394e-01
    outer loop
      vertex 1.566853e-01 -6.188860e-01 4.591930e-01
      vertex 1.566853e-01 -3.394202e-01 2.635090e-01
      vertex 8.993357e-02 -4.305288e-01 4.124613e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.530724e-01 5.217925e-01
    outer loop
      vertex 1.566853e-01 -3.394202e-01 2.635090e-01
      vertex 2.639155e-02 -3.394202e-01 2.635090e-01
      vertex 8.993357e-02 -4.305288e-01 4.124613e-01
    endloop
  endfacet
  facet normal -7.392715e-01 3.862507e-01 5.516231e-01
    outer loop
      vertex 2.639155e-02 -3.394202e-01 2.635090e-01
      vertex 2.639155e-02 -6.188860e-01 4.591930e-01
      vertex 8.993357e-02 -4.305288e-01 4.124613e-01
    endloop
  endfacet
  facet normal -8.270191e-16 2.408010e-01 9.705745e-01
    outer loop
      vertex 2.639155e-02 -6.188860e-01 4.591930e-01
      vertex 1.566853e-01 -6.188860e-01 4.591930e-01
      vertex 8.993357e-02 -4.305288e-01 4.124613e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 1.590481e-01 -6.628164e-01 4.167069e-01
      vertex 2.678953e-02 -3.791363e-01 2.180720e-01
      vertex 1.590481e-01 -3.791363e-01 2.180720e-01
    endloop
  endfacet
  facet normal 6.876239e-16 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 1.590481e-01 -6.628164e-01 4.167069e-01
      vertex 2.678953e-02 -6.628164e-01 4.167069e-01
      vertex 2.678953e-02 -3.791363e-01 2.180720e-01
    endloop
  endfacet
  facet normal -9.992255e-01 -2.256980e-02 -3.223302e-02
    outer loop
      vertex 1.566853e-01 -6.188860e-01 4.591930e-01
      vertex 1.566853e-01 -3.394202e-01 2.635090e-01
      vertex 1.590481e-01 -3.791363e-01 2.180720e-01
    endloop
  endfacet
  facet normal -9.992255e-01 -2.256980e-02 -3.223302e-02
    outer loop
      vertex 1.566853e-01 -6.188860e-01 4.591930e-01
      vertex 1.590481e-01 -3.791363e-01 2.180720e-01
      vertex 1.590481e-01 -6.628164e-01 4.167069e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -7.529154e-01 6.581173e-01
    outer loop
      vertex 1.566853e-01 -3.394202e-01 2.635090e-01
      vertex 2.639155e-02 -3.394202e-01 2.635090e-01
      vertex 2.678953e-02 -3.791363e-01 2.180720e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -7.529154e-01 6.581173e-01
    outer loop
      vertex 1.566853e-01 -3.394202e-01 2.635090e-01
      vertex 2.678953e-02 -3.791363e-01 2.180720e-01
      vertex 1.590481e-01 -3.791363e-01 2.180720e-01
    endloop
  endfacet
  facet normal 9.999780e-01 3.804444e-03 5.433310e-03
    outer loop
      vertex 2.639155e-02 -3.394202e-01 2.635090e-01
      vertex 2.639155e-02 -6.188860e-01 4.591930e-01
      vertex 2.678953e-02 -6.628164e-01 4.167069e-01
    endloop
  endfacet
  facet normal 9.999780e-01 3.804444e-03 5.433310e-03
    outer loop
      vertex 2.639155e-02 -3.394202e-01 2.635090e-01
      vertex 2.678953e-02 -6.628164e-01 4.167069e-01
      vertex 2.678953e-02 -3.791363e-01 2.180720e-01
    endloop
  endfacet
  facet normal 6.125047e-16 6.951917e-01 -7.188244e-01
    outer loop
      vertex 2.639155e-02 -6.188860e-01 4.591930e-01
      vertex 1.566853e-01 -6.188860e-01 4.591930e-01
      vertex 1.590481e-01 -6.628164e-01 4.167069e-01
    endloop
  endfacet
  facet normal 6.170241e-16 6.951917e-01 -7.188244e-01
    outer loop
      vertex 2.639155e-02 -6.188860e-01 4.591930e-01
      vertex 1.590481e-01 -6.628164e-01 4.167069e-01
      vertex 2.678953e-02 -6.628164e-01 4.167069e-01
    endloop
  endfacet
  facet normal 6.848300e-01 4.179668e-01 5.969184e-01
    outer loop
      vertex 1.708543e-01 -5.891616e-01 -8.606412e-04
      vertex 1.708543e-01 -2.920470e-01 -2.089025e-01
      vertex 9.824634e-02 -3.975906e-01 -5.169874e-02
    endloop
  endfacet
  facet normal 0.000000e+00 8.302394e-01 5.574069e-01
    outer loop
      vertex 1.708543e-01 -2.920470e-01 -2.089025e-01
      vertex 2.877813e-02 -2.920470e-01 -2.089025e-01
      vertex 9.824634e-02 -3.975906e-01 -5.169874e-02
    endloop
  endfacet
  facet normal -7.007538e-01 4.091913e-01 5.843857e-01
    outer loop
      vertex 2.877813e-02 -2.920470e-01 -2.089025e-01
      vertex 2.877813e-02 -5.891616e-01 -8.606412e-04
      vertex 9.824634e-02 -3.975906e-01 -5.169874e-02
    endloop
  endfacet
  facet normal -0.000000e+00 2.564966e-01 9.665451e-01
    outer loop
      vertex 2.877813e-02 -5.891616e-01 -8.606412e-04
      vertex 1.708543e-01 -5.891616e-01 -8.606412e-04
      vertex 9.824634e-02 -3.975906e-01 -5.169874e-02
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 1.732171e-01 -6.290377e-01 -4.618553e-02
      vertex 2.917611e-02 -3.278142e-01 -2.571045e-01
      vertex 1.732171e-01 -3.278142e-01 -2.571045e-01
    endloop
  endfacet
  facet normal -0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 1.732171e-01 -6.290377e-01 -4.618553e-02
      vertex 2.917611e-02 -6.290377e-01 -4.618553e-02
      vertex 2.917611e-02 -3.278142e-01 -2.571045e-01
    endloop
  endfacet
  facet normal -9.992255e-01 -2.256980e-02 -3.223302e-02
    outer loop
      vertex 1.708543e-01 -5.891616e-01 -8.606412e-04
      vertex 1.708543e-01 -2.920470e-01 -2.089025e-01
      vertex 1.732171e-01 -3.278142e-01 -2.571045e-01
    endloop
  endfacet
  facet normal -9.992255e-01 -2.256980e-02 -3.223302e-02
    outer loop
      vertex 1.708543e-01 -5.891616e-01 -8.606412e-04
      vertex 1.732171e-01 -3.278142e-01 -2.571045e-01
      vertex 1.732171e-01 -6.290377e-01 -4.618553e-02
    endloop
  endfacet
  facet normal 0.000000e+00 -8.030618e-01 5.958958e-01
    outer loop
      vertex 1.708543e-01 -2.920470e-01 -2.089025e-01
      vertex 2.877813e-02 -2.920470e-01 -2.089025e-01
      vertex 2.917611e-02 -3.278142e-01 -2.571045e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -8.030618e-01 5.958958e-01
    outer loop
      vertex 1.708543e-01 -2.920470e-01 -2.089025e-01
      vertex 2.917611e-02 -3.278142e-01 -2.571045e-01
      vertex 1.732171e-01 -3.278142e-01 -2.571045e-01
    endloop
  endfacet
  facet normal 9.999780e-01 3.804444e-03 5.433310e-03
    outer loop
      vertex 2.877813e-02 -2.920470e-01 -2.089025e-01
      vertex 2.877813e-02 -5.891616e-01 -8.606412e-04
      vertex 2.917611e-02 -6.290377e-01 -4.618553e-02
    endloop
  endfacet
  facet normal 9.999780e-01 3.804444e-03 5.433310e-03
    outer loop
      vertex 2.877813e-02 -2.920470e-01 -2.089025e-01
      vertex 2.917611e-02 -6.290377e-01 -4.618553e-02
      vertex 2.917611e-02 -3.278142e-01 -2.571045e-01
    endloop
  endfacet
  facet normal 0.000000e+00 7.507936e-01 -6.605368e-01
    outer loop
      vertex 2.877813e-02 -5.891616e-01 -8.606412e-04
      vertex 1.708543e-01 -5.891616e-01 -8.606412e-04
      vertex 1.732171e-01 -6.290377e-01 -4.618553e-02
    endloop
  endfacet
  facet normal 0.000000e+00 7.507936e-01 -6.605368e-01
    outer loop
      vertex 2.877813e-02 -5.891616e-01 -8.606412e-04
      vertex 1.732171e-01 -6.290377e-01 -4.618553e-02
      vertex 2.917611e-02 -6.290377e-01 -4.618553e-02
    endloop
  endfacet
  facet normal 7.648963e-01 3.694713e-01 5.276596e-01
    outer loop
      vertex 1.510382e-01 -2.890284e-03 2.029300e-01
      vertex 1.510382e-01 2.968725e-01 -6.966203e-03
      vertex 8.647548e-02 1.899128e-01 1.615179e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.442453e-01 5.359569e-01
    outer loop
      vertex 1.510382e-01 2.968725e-01 -6.966203e-03
      vertex 2.544036e-02 2.968725e-01 -6.966203e-03
      vertex 8.647548e-02 1.899128e-01 1.615179e-01
    endloop
  endfacet
  facet normal -7.823427e-01 3.572510e-01 5.102074e-01
    outer loop
      vertex 2.544036e-02 2.968725e-01 -6.966203e-03
      vertex 2.544036e-02 -2.890284e-03 2.029300e-01
      vertex 8.647548e-02 1.899128e-01 1.615179e-01
    endloop
  endfacet
  facet normal 6.961103e-17 2.099997e-01 9.777015e-01
    outer loop
      vertex 2.544036e-02 -2.890284e-03 2.029300e-01
      vertex 1.510382e-01 -2.890284e-03 2.029300e-01
      vertex 8.647548e-02 1.899128e-01 1.615179e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 1.534009e-01 -3.882677e-02 1.548465e-01
      vertex 2.583834e-02 2.656254e-01 -5.833322e-02
      vertex 1.534009e-01 2.656254e-01 -5.833322e-02
    endloop
  endfacet
  facet normal -8.967203e-18 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 1.534009e-01 -3.882677e-02 1.548465e-01
      vertex 2.583834e-02 -3.882677e-02 1.548465e-01
      vertex 2.583834e-02 2.656254e-01 -5.833322e-02
    endloop
  endfacet
  facet normal -9.992255e-01 -2.256980e-02 -3.223302e-02
    outer loop
      vertex 1.510382e-01 -2.890284e-03 2.029300e-01
      vertex 1.510382e-01 2.968725e-01 -6.966203e-03
      vertex 1.534009e-01 2.656254e-01 -5.833322e-02
    endloop
  endfacet
  facet normal -9.992255e-01 -2.256980e-02 -3.223302e-02
    outer loop
      vertex 1.510382e-01 -2.890284e-03 2.029300e-01
      vertex 1.534009e-01 2.656254e-01 -5.833322e-02
      vertex 1.534009e-01 -3.882677e-02 1.548465e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -8.543446e-01 5.197069e-01
    outer loop
      vertex 1.510382e-01 2.968725e-01 -6.966203e-03
      vertex 2.544036e-02 2.968725e-01 -6.966203e-03
      vertex 2.583834e-02 2.656254e-01 -5.833322e-02
    endloop
  endfacet
  facet normal 0.000000e+00 -8.543446e-01 5.197069e-01
    outer loop
      vertex 1.510382e-01 2.968725e-01 -6.966203e-03
      vertex 2.583834e-02 2.656254e-01 -5.833322e-02
      vertex 1.534009e-01 2.656254e-01 -5.833322e-02
    endloop
  endfacet
  facet normal 9.999780e-01 3.804444e-03 5.433310e-03
    outer loop
      vertex 2.544036e-02 2.968725e-01 -6.966203e-03
      vertex 2.544036e-02 -2.890284e-03 2.029300e-01
      vertex 2.583834e-02 -3.882677e-02 1.548465e-01
    endloop
  endfacet
  facet normal 9.999780e-01 3.804444e-03 5.433310e-03
    outer loop
      vertex 2.544036e-02 2.968725e-01 -6.966203e-03
      vertex 2.583834e-02 -3.882677e-02 1.548465e-01
      vertex 2.583834e-02 2.656254e-01 -5.833322e-02
    endloop
  endfacet
  facet normal 2.655193e-16 8.010074e-01 -5.986544e-01
    outer loop
      vertex 2.544036e-02 -2.890284e-03 2.029300e-01
      vertex 1.510382e-01 -2.890284e-03 2.029300e-01
      vertex 1.534009e-01 -3.882677e-02 1.548465e-01
    endloop
  endfacet
  facet normal 3.681298e-16 8.010074e-01 -5.986544e-01
    outer loop
      vertex 2.544036e-02 -2.890284e-03 2.029300e-01
      vertex 1.534009e-01 -3.882677e-02 1.548465e-01
      vertex 2.583834e-02 -3.882677e-02 1.548465e-01
    endloop
  endfacet
  facet normal 4.048890e-01 5.244587e-01 7.490046e-01
    outer loop
      vertex 1.480026e-01 3.304511e-01 6.362396e-02
      vertex 1.480026e-01 3.781210e-01 3.024514e-02
      vertex 8.583248e-02 3.684965e-01 7.059157e-02
    endloop
  endfacet
  facet normal 0.000000e+00 9.727072e-01 2.320362e-01
    outer loop
      vertex 1.480026e-01 3.781210e-01 3.024514e-02
      vertex 2.492906e-02 3.781210e-01 3.024514e-02
      vertex 8.583248e-02 3.684965e-01 7.059157e-02
    endloop
  endfacet
  facet normal -4.118936e-01 5.226612e-01 7.464375e-01
    outer loop
      vertex 2.492906e-02 3.781210e-01 3.024514e-02
      vertex 2.492906e-02 3.304511e-01 6.362396e-02
      vertex 8.583248e-02 3.684965e-01 7.059157e-02
    endloop
  endfacet
  facet normal -3.843346e-16 -1.801432e-01 9.836404e-01
    outer loop
      vertex 2.492906e-02 3.304511e-01 6.362396e-02
      vertex 1.480026e-01 3.304511e-01 6.362396e-02
      vertex 8.583248e-02 3.684965e-01 7.059157e-02
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 1.503654e-01 2.990992e-01 1.233034e-02
      vertex 2.532704e-02 3.475302e-01 -2.158136e-02
      vertex 1.503654e-01 3.475302e-01 -2.158136e-02
    endloop
  endfacet
  facet normal -7.280848e-17 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 1.503654e-01 2.990992e-01 1.233034e-02
      vertex 2.532704e-02 2.990992e-01 1.233034e-02
      vertex 2.532704e-02 3.475302e-01 -2.158136e-02
    endloop
  endfacet
  facet normal -9.992255e-01 -2.256980e-02 -3.223302e-02
    outer loop
      vertex 1.480026e-01 3.304511e-01 6.362396e-02
      vertex 1.480026e-01 3.781210e-01 3.024514e-02
      vertex 1.503654e-01 3.475302e-01 -2.158136e-02
    endloop
  endfacet
  facet normal -9.992255e-01 -2.256980e-02 -3.223302e-02
    outer loop
      vertex 1.480026e-01 3.304511e-01 6.362396e-02
      vertex 1.503654e-01 3.475302e-01 -2.158136e-02
      vertex 1.503654e-01 2.990992e-01 1.233034e-02
    endloop
  endfacet
  facet normal 0.000000e+00 -8.611728e-01 5.083123e-01
    outer loop
      vertex 1.480026e-01 3.781210e-01 3.024514e-02
      vertex 2.492906e-02 3.781210e-01 3.024514e-02
      vertex 2.532704e-02 3.475302e-01 -2.158136e-02
    endloop
  endfacet
  facet normal 0.000000e+00 -8.611728e-01 5.083123e-01
    outer loop
      vertex 1.480026e-01 3.781210e-01 3.024514e-02
      vertex 2.532704e-02 3.475302e-01 -2.158136e-02
      vertex 1.503654e-01 3.475302e-01 -2.158136e-02
    endloop
  endfacet
  facet normal 9.999780e-01 3.804444e-03 5.433310e-03
    outer loop
      vertex 2.492906e-02 3.781210e-01 3.024514e-02
      vertex 2.492906e-02 3.304511e-01 6.362396e-02
      vertex 2.532704e-02 2.990992e-01 1.233034e-02
    endloop
  endfacet
  facet normal 9.999780e-01 3.804444e-03 5.433310e-03
    outer loop
      vertex 2.492906e-02 3.781210e-01 3.024514e-02
      vertex 2.532704e-02 2.990992e-01 1.233034e-02
      vertex 2.532704e-02 3.475302e-01 -2.158136e-02
    endloop
  endfacet
  facet normal 8.873039e-16 8.532388e-01 -5.215204e-01
    outer loop
      vertex 2.492906e-02 3.304511e-01 6.362396e-02
      vertex 1.480026e-01 3.304511e-01 6.362396e-02
      vertex 1.503654e-01 2.990992e-01 1.233034e-02
    endloop
  endfacet
  facet normal 4.904031e-16 8.532388e-01 -5.215204e-01
    outer loop
      vertex 2.492906e-02 3.304511e-01 6.362396e-02
      vertex 1.503654e-01 2.990992e-01 1.233034e-02
      vertex 2.532704e-02 2.990992e-01 1.233034e-02
    endloop
  endfacet
  facet normal 3.641870e-01 5.341866e-01 7.628975e-01
    outer loop
      vertex 3.443390e-02 2.480719e-01 -6.576001e-02
      vertex 3.443390e-02 3.976558e-01 -1.704998e-01
      vertex -1.203284e-01 3.632475e-01 -7.252742e-02
    endloop
  endfacet
  facet normal 0.000000e+00 9.435038e-01 3.313618e-01
    outer loop
      vertex 3.443390e-02 3.976558e-01 -1.704998e-01
      vertex -2.601137e-01 3.976558e-01 -1.704998e-01
      vertex -1.203284e-01 3.632475e-01 -7.252742e-02
    endloop
  endfacet
  facet normal -3.973027e-01 5.263640e-01 7.517257e-01
    outer loop
      vertex -2.601137e-01 3.976558e-01 -1.704998e-01
      vertex -2.601137e-01 3.730518e-01 -1.532719e-01
      vertex -1.203284e-01 3.632475e-01 -7.252742e-02
    endloop
  endfacet
  facet normal -4.773907e-01 2.134286e-01 8.523769e-01
    outer loop
      vertex -2.601137e-01 3.730518e-01 -1.532719e-01
      vertex -1.597372e-01 2.480719e-01 -6.576001e-02
      vertex -1.203284e-01 3.632475e-01 -7.252742e-02
    endloop
  endfacet
  facet normal -0.000000e+00 5.865612e-02 9.982782e-01
    outer loop
      vertex -1.597372e-01 2.480719e-01 -6.576001e-02
      vertex 3.443390e-02 2.480719e-01 -6.576001e-02
      vertex -1.203284e-01 3.632475e-01 -7.252742e-02
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 3.496208e-02 2.166846e-01 -1.170288e-01
      vertex -2.641036e-01 3.685629e-01 -2.233752e-01
      vertex 3.496208e-02 3.685629e-01 -2.233752e-01
    endloop
  endfacet
  facet normal 3.804008e-16 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 3.496208e-02 2.166846e-01 -1.170288e-01
      vertex -2.641036e-01 3.435815e-01 -2.058830e-01
      vertex -2.641036e-01 3.685629e-01 -2.233752e-01
    endloop
  endfacet
  facet normal -0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 3.496208e-02 2.166846e-01 -1.170288e-01
      vertex -1.621875e-01 2.166846e-01 -1.170288e-01
      vertex -2.641036e-01 3.435815e-01 -2.058830e-01
    endloop
  endfacet
  facet normal -9.999613e-01 -5.049037e-03 -7.210772e-03
    outer loop
      vertex 3.443390e-02 2.480719e-01 -6.576001e-02
      vertex 3.443390e-02 3.976558e-01 -1.704998e-01
      vertex 3.496208e-02 3.685629e-01 -2.233752e-01
    endloop
  endfacet
  facet normal -9.999613e-01 -5.049037e-03 -7.210772e-03
    outer loop
      vertex 3.443390e-02 2.480719e-01 -6.576001e-02
      vertex 3.496208e-02 3.685629e-01 -2.233752e-01
      vertex 3.496208e-02 2.166846e-01 -1.170288e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -8.761364e-01 4.820633e-01
    outer loop
      vertex 3.443390e-02 3.976558e-01 -1.704998e-01
      vertex -2.601137e-01 3.976558e-01 -1.704998e-01
      vertex -2.641036e-01 3.685629e-01 -2.233752e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -8.761364e-01 4.820633e-01
    outer loop
      vertex 3.443390e-02 3.976558e-01 -1.704998e-01
      vertex -2.641036e-01 3.685629e-01 -2.233752e-01
      vertex 3.496208e-02 3.685629e-01 -2.233752e-01
    endloop
  endfacet
  facet normal 9.977963e-01 -3.805785e-02 -5.435225e-02
    outer loop
      vertex -2.601137e-01 3.976558e-01 -1.704998e-01
      vertex -2.601137e-01 3.730518e-01 -1.532719e-01
      vertex -2.641036e-01 3.435815e-01 -2.058830e-01
    endloop
  endfacet
  facet normal 9.977963e-01 -3.805785e-02 -5.435225e-02
    outer loop
      vertex -2.601137e-01 3.976558e-01 -1.704998e-01
      vertex -2.641036e-01 3.435815e-01 -2.058830e-01
      vertex -2.641036e-01 3.685629e-01 -2.233752e-01
    endloop
  endfacet
  facet normal 8.354171e-01 4.500685e-01 -3.154627e-01
    outer loop
      vertex -2.601137e-01 3.730518e-01 -1.532719e-01
      vertex -1.597372e-01 2.480719e-01 -6.576001e-02
      vertex -1.621875e-01 2.166846e-01 -1.170288e-01
    endloop
  endfacet
  facet normal 8.354171e-01 4.500685e-01 -3.154627e-01
    outer loop
      vertex -2.601137e-01 3.730518e-01 -1.532719e-01
      vertex -1.621875e-01 2.166846e-01 -1.170288e-01
      vertex -2.641036e-01 3.435815e-01 -2.058830e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.528643e-01 -5.221327e-01
    outer loop
      vertex -1.597372e-01 2.480719e-01 -6.576001e-02
      vertex 3.443390e-02 2.480719e-01 -6.576001e-02
      vertex 3.496208e-02 2.166846e-01 -1.170288e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.528643e-01 -5.221327e-01
    outer loop
      vertex -1.597372e-01 2.480719e-01 -6.576001e-02
      vertex 3.496208e-02 2.166846e-01 -1.170288e-01
      vertex -1.621875e-01 2.166846e-01 -1.170288e-01
    endloop
  endfacet
  facet normal 4.820472e-01 2.086767e-01 8.509316e-01
    outer loop
      vertex 1.498558e-01 3.750095e-01 1.407378e-01
      vertex 2.625614e-01 5.153404e-01 4.247699e-02
      vertex 1.130057e-01 4.720082e-01 1.378258e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.103959e-01 4.137383e-01
    outer loop
      vertex 2.625614e-01 5.153404e-01 4.247699e-02
      vertex 2.313074e-02 5.153404e-01 4.247699e-02
      vertex 1.130057e-01 4.720082e-01 1.378258e-01
    endloop
  endfacet
  facet normal -5.097432e-01 4.934631e-01 7.047383e-01
    outer loop
      vertex 2.313074e-02 5.153404e-01 4.247699e-02
      vertex 2.313074e-02 3.750095e-01 1.407378e-01
      vertex 1.130057e-01 4.720082e-01 1.378258e-01
    endloop
  endfacet
  facet normal -0.000000e+00 3.000687e-02 9.995497e-01
    outer loop
      vertex 2.313074e-02 3.750095e-01 1.407378e-01
      vertex 1.498558e-01 3.750095e-01 1.407378e-01
      vertex 1.130057e-01 4.720082e-01 1.378258e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 1.523060e-01 3.436281e-01 8.946480e-02
      vertex 2.350894e-02 4.862535e-01 -1.040260e-02
      vertex 2.668544e-01 4.862535e-01 -1.040260e-02
    endloop
  endfacet
  facet normal -0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 1.523060e-01 3.436281e-01 8.946480e-02
      vertex 2.350894e-02 3.436281e-01 8.946480e-02
      vertex 2.350894e-02 4.862535e-01 -1.040260e-02
    endloop
  endfacet
  facet normal -8.354171e-01 4.501065e-01 -3.154084e-01
    outer loop
      vertex 1.498558e-01 3.750095e-01 1.407378e-01
      vertex 2.625614e-01 5.153404e-01 4.247699e-02
      vertex 2.668544e-01 4.862535e-01 -1.040260e-02
    endloop
  endfacet
  facet normal -8.354171e-01 4.501065e-01 -3.154084e-01
    outer loop
      vertex 1.498558e-01 3.750095e-01 1.407378e-01
      vertex 2.668544e-01 4.862535e-01 -1.040260e-02
      vertex 1.523060e-01 3.436281e-01 8.946480e-02
    endloop
  endfacet
  facet normal 0.000000e+00 -8.761938e-01 4.819589e-01
    outer loop
      vertex 2.625614e-01 5.153404e-01 4.247699e-02
      vertex 2.313074e-02 5.153404e-01 4.247699e-02
      vertex 2.350894e-02 4.862535e-01 -1.040260e-02
    endloop
  endfacet
  facet normal 0.000000e+00 -8.761938e-01 4.819589e-01
    outer loop
      vertex 2.625614e-01 5.153404e-01 4.247699e-02
      vertex 2.350894e-02 4.862535e-01 -1.040260e-02
      vertex 2.668544e-01 4.862535e-01 -1.040260e-02
    endloop
  endfacet
  facet normal 9.999801e-01 3.615359e-03 5.163268e-03
    outer loop
      vertex 2.313074e-02 5.153404e-01 4.247699e-02
      vertex 2.313074e-02 3.750095e-01 1.407378e-01
      vertex 2.350894e-02 3.436281e-01 8.946480e-02
    endloop
  endfacet
  facet normal 9.999801e-01 3.615359e-03 5.163268e-03
    outer loop
      vertex 2.313074e-02 5.153404e-01 4.247699e-02
      vertex 2.350894e-02 3.436281e-01 8.946480e-02
      vertex 2.350894e-02 4.862535e-01 -1.040260e-02
    endloop
  endfacet
  facet normal 0.000000e+00 8.529269e-01 -5.220303e-01
    outer loop
      vertex 2.313074e-02 3.750095e-01 1.407378e-01
      vertex 1.498558e-01 3.750095e-01 1.407378e-01
      vertex 1.523060e-01 3.436281e-01 8.946480e-02
    endloop
  endfacet
  facet normal 0.000000e+00 8.529269e-01 -5.220303e-01
    outer loop
      vertex 2.313074e-02 3.750095e-01 1.407378e-01
      vertex 1.523060e-01 3.436281e-01 8.946480e-02
      vertex 2.350894e-02 3.436281e-01 8.946480e-02
    endloop
  endfacet
  facet normal -0.000000e+00 9.227722e-02 9.957334e-01
    outer loop
      vertex -1.467199e-01 -8.552630e-01 4.535870e-01
      vertex 3.432361e-02 -8.552630e-01 4.535870e-01
      vertex -7.927697e-02 -7.503965e-01 4.438687e-01
    endloop
  endfacet
  facet normal 4.174564e-01 5.212072e-01 7.443610e-01
    outer loop
      vertex 3.432361e-02 -8.552630e-01 4.535870e-01
      vertex 3.432361e-02 -7.236735e-01 3.614470e-01
      vertex -7.927697e-02 -7.503965e-01 4.438687e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.512512e-01 3.084170e-01
    outer loop
      vertex 3.432361e-02 -7.236735e-01 3.614470e-01
      vertex -2.431045e-01 -7.236735e-01 3.614470e-01
      vertex -7.927697e-02 -7.503965e-01 4.438687e-01
    endloop
  endfacet
  facet normal -3.819615e-01 3.257991e-01 8.648470e-01
    outer loop
      vertex -2.431045e-01 -7.236735e-01 3.614470e-01
      vertex -1.467199e-01 -8.552630e-01 4.535870e-01
      vertex -7.927697e-02 -7.503965e-01 4.438687e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -1.488571e-01 -9.011416e-01 4.124651e-01
      vertex 3.482359e-02 -7.676353e-01 3.189829e-01
      vertex 3.482359e-02 -9.011416e-01 4.124651e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -1.488571e-01 -9.011416e-01 4.124651e-01
      vertex -2.466458e-01 -7.676353e-01 3.189829e-01
      vertex 3.482359e-02 -7.676353e-01 3.189829e-01
    endloop
  endfacet
  facet normal 0.000000e+00 6.674493e-01 -7.446552e-01
    outer loop
      vertex -1.467199e-01 -8.552630e-01 4.535870e-01
      vertex 3.432361e-02 -8.552630e-01 4.535870e-01
      vertex 3.482359e-02 -9.011416e-01 4.124651e-01
    endloop
  endfacet
  facet normal 0.000000e+00 6.674493e-01 -7.446552e-01
    outer loop
      vertex -1.467199e-01 -8.552630e-01 4.535870e-01
      vertex 3.482359e-02 -9.011416e-01 4.124651e-01
      vertex -1.488571e-01 -9.011416e-01 4.124651e-01
    endloop
  endfacet
  facet normal -9.999653e-01 -4.779442e-03 -6.825751e-03
    outer loop
      vertex 3.432361e-02 -8.552630e-01 4.535870e-01
      vertex 3.432361e-02 -7.236735e-01 3.614470e-01
      vertex 3.482359e-02 -7.676353e-01 3.189829e-01
    endloop
  endfacet
  facet normal -9.999653e-01 -4.779442e-03 -6.825751e-03
    outer loop
      vertex 3.432361e-02 -8.552630e-01 4.535870e-01
      vertex 3.482359e-02 -7.676353e-01 3.189829e-01
      vertex 3.482359e-02 -9.011416e-01 4.124651e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -6.947487e-01 7.192526e-01
    outer loop
      vertex 3.432361e-02 -7.236735e-01 3.614470e-01
      vertex -2.431045e-01 -7.236735e-01 3.614470e-01
      vertex -2.466458e-01 -7.676353e-01 3.189829e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -6.947487e-01 7.192526e-01
    outer loop
      vertex 3.432361e-02 -7.236735e-01 3.614470e-01
      vertex -2.466458e-01 -7.676353e-01 3.189829e-01
      vertex 3.482359e-02 -7.676353e-01 3.189829e-01
    endloop
  endfacet
  facet normal 8.479374e-01 3.313640e-01 -4.137634e-01
    outer loop
      vertex -2.431045e-01 -7.236735e-01 3.614470e-01
      vertex -1.467199e-01 -8.552630e-01 4.535870e-01
      vertex -1.488571e-01 -9.011416e-01 4.124651e-01
    endloop
  endfacet
  facet normal 8.479374e-01 3.313640e-01 -4.137634e-01
    outer loop
      vertex -2.431045e-01 -7.236735e-01 3.614470e-01
      vertex -1.488571e-01 -9.011416e-01 4.124651e-01
      vertex -2.466458e-01 -7.676353e-01 3.189829e-01
    endloop
  endfacet
  facet normal -0.000000e+00 1.293402e-01 9.916003e-01
    outer loop
      vertex 2.472460e-02 -6.218645e-01 6.627867e-01
      vertex 1.347393e-01 -6.218645e-01 6.627867e-01
      vertex 1.008731e-01 -5.282255e-01 6.505728e-01
    endloop
  endfacet
  facet normal 4.444545e-01 2.720700e-01 8.534859e-01
    outer loop
      vertex 1.347393e-01 -6.218645e-01 6.627867e-01
      vertex 2.239814e-01 -5.000264e-01 5.774748e-01
      vertex 1.008731e-01 -5.282255e-01 6.505728e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.329840e-01 3.599178e-01
    outer loop
      vertex 2.239814e-01 -5.000264e-01 5.774748e-01
      vertex 2.472460e-02 -5.000264e-01 5.774748e-01
      vertex 1.008731e-01 -5.282255e-01 6.505728e-01
    endloop
  endfacet
  facet normal -4.977750e-01 4.974664e-01 7.104556e-01
    outer loop
      vertex 2.472460e-02 -5.000264e-01 5.774748e-01
      vertex 2.472460e-02 -6.218645e-01 6.627867e-01
      vertex 1.008731e-01 -5.282255e-01 6.505728e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 2.511358e-02 -6.677431e-01 6.216648e-01
      vertex 2.275052e-01 -5.439882e-01 5.350107e-01
      vertex 1.368591e-01 -6.677431e-01 6.216648e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 2.511358e-02 -6.677431e-01 6.216648e-01
      vertex 2.511358e-02 -5.439882e-01 5.350107e-01
      vertex 2.275052e-01 -5.439882e-01 5.350107e-01
    endloop
  endfacet
  facet normal 0.000000e+00 6.674493e-01 -7.446552e-01
    outer loop
      vertex 2.472460e-02 -6.218645e-01 6.627867e-01
      vertex 1.347393e-01 -6.218645e-01 6.627867e-01
      vertex 1.368591e-01 -6.677431e-01 6.216648e-01
    endloop
  endfacet
  facet normal 0.000000e+00 6.674493e-01 -7.446552e-01
    outer loop
      vertex 2.472460e-02 -6.218645e-01 6.627867e-01
      vertex 1.368591e-01 -6.677431e-01 6.216648e-01
      vertex 2.511358e-02 -6.677431e-01 6.216648e-01
    endloop
  endfacet
  facet normal -8.479684e-01 3.315174e-01 -4.135768e-01
    outer loop
      vertex 1.347393e-01 -6.218645e-01 6.627867e-01
      vertex 2.239814e-01 -5.000264e-01 5.774748e-01
      vertex 2.275052e-01 -5.439882e-01 5.350107e-01
    endloop
  endfacet
  facet normal -8.479684e-01 3.315174e-01 -4.135768e-01
    outer loop
      vertex 1.347393e-01 -6.218645e-01 6.627867e-01
      vertex 2.275052e-01 -5.439882e-01 5.350107e-01
      vertex 1.368591e-01 -6.677431e-01 6.216648e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -6.947487e-01 7.192526e-01
    outer loop
      vertex 2.239814e-01 -5.000264e-01 5.774748e-01
      vertex 2.472460e-02 -5.000264e-01 5.774748e-01
      vertex 2.511358e-02 -5.439882e-01 5.350107e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -6.947487e-01 7.192526e-01
    outer loop
      vertex 2.239814e-01 -5.000264e-01 5.774748e-01
      vertex 2.511358e-02 -5.439882e-01 5.350107e-01
      vertex 2.275052e-01 -5.439882e-01 5.350107e-01
    endloop
  endfacet
  facet normal 9.999790e-01 3.718414e-03 5.310445e-03
    outer loop
      vertex 2.472460e-02 -5.000264e-01 5.774748e-01
      vertex 2.472460e-02 -6.218645e-01 6.627867e-01
      vertex 2.511358e-02 -6.677431e-01 6.216648e-01
    endloop
  endfacet
  facet normal 9.999790e-01 3.718414e-03 5.310445e-03
    outer loop
      vertex 2.472460e-02 -5.000264e-01 5.774748e-01
      vertex 2.511358e-02 -6.677431e-01 6.216648e-01
      vertex 2.511358e-02 -5.439882e-01 5.350107e-01
    endloop
  endfacet
  facet normal 4.307696e-01 5.831648e-01 6.887353e-01
    outer loop
      vertex 3.526903e-01 -7.549481e-01 6.574071e-01
      vertex 3.411776e-01 -7.058006e-01 6.229936e-01
      vertex 2.691759e-01 -7.338829e-01 6.918049e-01
    endloop
  endfacet
  facet normal -2.305231e-01 9.612657e-01 1.510875e-01
    outer loop
      vertex 3.411776e-01 -7.058006e-01 6.229936e-01
      vertex 1.314657e-01 -7.623114e-01 6.625629e-01
      vertex 2.691759e-01 -7.338829e-01 6.918049e-01
    endloop
  endfacet
  facet normal -2.586828e-01 3.131340e-01 9.137999e-01
    outer loop
      vertex 1.314657e-01 -7.623114e-01 6.625629e-01
      vertex 1.819140e-01 -8.022547e-01 6.905315e-01
      vertex 2.691759e-01 -7.338829e-01 6.918049e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -1.862122e-02 9.998266e-01
    outer loop
      vertex 1.819140e-01 -8.022547e-01 6.905315e-01
      vertex 3.526903e-01 -8.022547e-01 6.905315e-01
      vertex 2.691759e-01 -7.338829e-01 6.918049e-01
    endloop
  endfacet
  facet normal 4.342438e-01 5.166750e-01 7.378884e-01
    outer loop
      vertex 3.526903e-01 -8.022547e-01 6.905315e-01
      vertex 3.526903e-01 -7.549481e-01 6.574071e-01
      vertex 2.691759e-01 -7.338829e-01 6.918049e-01
    endloop
  endfacet
  facet normal 1.768765e-16 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 3.581239e-01 -8.019259e-01 6.170548e-01
      vertex 1.334911e-01 -8.094026e-01 6.222901e-01
      vertex 3.464338e-01 -7.520212e-01 5.821112e-01
    endloop
  endfacet
  facet normal 1.543540e-16 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 3.581239e-01 -8.019259e-01 6.170548e-01
      vertex 1.847167e-01 -8.499613e-01 6.506896e-01
      vertex 1.334911e-01 -8.094026e-01 6.222901e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 3.581239e-01 -8.019259e-01 6.170548e-01
      vertex 3.581239e-01 -8.499613e-01 6.506896e-01
      vertex 1.847167e-01 -8.499613e-01 6.506896e-01
    endloop
  endfacet
  facet normal -9.812682e-01 -1.776034e-01 7.463119e-02
    outer loop
      vertex 3.526903e-01 -7.549481e-01 6.574071e-01
      vertex 3.411776e-01 -7.058006e-01 6.229936e-01
      vertex 3.464338e-01 -7.520212e-01 5.821112e-01
    endloop
  endfacet
  facet normal -9.812682e-01 -1.776034e-01 7.463119e-02
    outer loop
      vertex 3.526903e-01 -7.549481e-01 6.574071e-01
      vertex 3.464338e-01 -7.520212e-01 5.821112e-01
      vertex 3.581239e-01 -8.019259e-01 6.170548e-01
    endloop
  endfacet
  facet normal 3.027569e-01 -6.118860e-01 7.307078e-01
    outer loop
      vertex 3.411776e-01 -7.058006e-01 6.229936e-01
      vertex 1.314657e-01 -7.623114e-01 6.625629e-01
      vertex 1.334911e-01 -8.094026e-01 6.222901e-01
    endloop
  endfacet
  facet normal 3.027569e-01 -6.118860e-01 7.307078e-01
    outer loop
      vertex 3.411776e-01 -7.058006e-01 6.229936e-01
      vertex 1.334911e-01 -8.094026e-01 6.222901e-01
      vertex 3.464338e-01 -7.520212e-01 5.821112e-01
    endloop
  endfacet
  facet normal 6.860431e-01 4.896912e-01 -5.380960e-01
    outer loop
      vertex 1.314657e-01 -7.623114e-01 6.625629e-01
      vertex 1.819140e-01 -8.022547e-01 6.905315e-01
      vertex 1.847167e-01 -8.499613e-01 6.506896e-01
    endloop
  endfacet
  facet normal 6.860431e-01 4.896912e-01 -5.380960e-01
    outer loop
      vertex 1.314657e-01 -7.623114e-01 6.625629e-01
      vertex 1.847167e-01 -8.499613e-01 6.506896e-01
      vertex 1.334911e-01 -8.094026e-01 6.222901e-01
    endloop
  endfacet
  facet normal 0.000000e+00 6.410046e-01 -7.675370e-01
    outer loop
      vertex 1.819140e-01 -8.022547e-01 6.905315e-01
      vertex 3.526903e-01 -8.022547e-01 6.905315e-01
      vertex 3.581239e-01 -8.499613e-01 6.506896e-01
    endloop
  endfacet
  facet normal 0.000000e+00 6.410046e-01 -7.675370e-01
    outer loop
      vertex 1.819140e-01 -8.022547e-01 6.905315e-01
      vertex 3.581239e-01 -8.499613e-01 6.506896e-01
      vertex 1.847167e-01 -8.499613e-01 6.506896e-01
    endloop
  endfacet
  facet normal -9.959244e-01 -5.173197e-02 -7.388091e-02
    outer loop
      vertex 3.526903e-01 -8.022547e-01 6.905315e-01
      vertex 3.526903e-01 -7.549481e-01 6.574071e-01
      vertex 3.581239e-01 -8.019259e-01 6.170548e-01
    endloop
  endfacet
  facet normal -9.959244e-01 -5.173197e-02 -7.388091e-02
    outer loop
      vertex 3.526903e-01 -8.022547e-01 6.905315e-01
      vertex 3.581239e-01 -8.019259e-01 6.170548e-01
      vertex 3.581239e-01 -8.499613e-01 6.506896e-01
    endloop
  endfacet
  facet normal 3.476977e-01 7.019369e-01 6.216034e-01
    outer loop
      vertex 3.441437e-01 -7.172887e-01 6.169014e-01
      vertex 2.788928e-01 -6.322162e-01 5.573330e-01
      vertex 2.215768e-01 -6.778739e-01 6.409513e-01
    endloop
  endfacet
  facet normal -4.691610e-01 8.697059e-01 1.532957e-01
    outer loop
      vertex 2.788928e-01 -6.322162e-01 5.573330e-01
      vertex 1.391674e-01 -7.182033e-01 6.175418e-01
      vertex 2.215768e-01 -6.778739e-01 6.409513e-01
    endloop
  endfacet
  facet normal -4.632659e-01 5.377579e-01 7.044154e-01
    outer loop
      vertex 1.391674e-01 -7.182033e-01 6.175418e-01
      vertex 1.338084e-01 -7.739675e-01 6.565883e-01
      vertex 2.215768e-01 -6.778739e-01 6.409513e-01
    endloop
  endfacet
  facet normal 1.886539e-01 -1.251771e-02 9.819638e-01
    outer loop
      vertex 1.338084e-01 -7.739675e-01 6.565883e-01
      vertex 3.441437e-01 -7.172887e-01 6.169014e-01
      vertex 2.215768e-01 -6.778739e-01 6.409513e-01
    endloop
  endfacet
  facet normal -4.800232e-17 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 3.494300e-01 -7.635488e-01 5.760466e-01
      vertex 1.413051e-01 -7.644774e-01 5.766968e-01
      vertex 2.831767e-01 -6.771695e-01 5.155632e-01
    endloop
  endfacet
  facet normal -5.089378e-17 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 3.494300e-01 -7.635488e-01 5.760466e-01
      vertex 1.358637e-01 -8.210982e-01 6.163431e-01
      vertex 1.413051e-01 -7.644774e-01 5.766968e-01
    endloop
  endfacet
  facet normal -8.455283e-01 -4.044568e-01 3.485635e-01
    outer loop
      vertex 3.441437e-01 -7.172887e-01 6.169014e-01
      vertex 2.788928e-01 -6.322162e-01 5.573330e-01
      vertex 2.831767e-01 -6.771695e-01 5.155632e-01
    endloop
  endfacet
  facet normal -8.455283e-01 -4.044568e-01 3.485635e-01
    outer loop
      vertex 3.441437e-01 -7.172887e-01 6.169014e-01
      vertex 2.831767e-01 -6.771695e-01 5.155632e-01
      vertex 3.494300e-01 -7.635488e-01 5.760466e-01
    endloop
  endfacet
  facet normal 5.873101e-01 -5.201820e-01 6.200625e-01
    outer loop
      vertex 2.788928e-01 -6.322162e-01 5.573330e-01
      vertex 1.391674e-01 -7.182033e-01 6.175418e-01
      vertex 1.413051e-01 -7.644774e-01 5.766968e-01
    endloop
  endfacet
  facet normal 5.873101e-01 -5.201820e-01 6.200625e-01
    outer loop
      vertex 2.788928e-01 -6.322162e-01 5.573330e-01
      vertex 1.413051e-01 -7.644774e-01 5.766968e-01
      vertex 2.831767e-01 -6.771695e-01 5.155632e-01
    endloop
  endfacet
  facet normal 9.954409e-01 -3.300348e-02 8.948864e-02
    outer loop
      vertex 1.391674e-01 -7.182033e-01 6.175418e-01
      vertex 1.338084e-01 -7.739675e-01 6.565883e-01
      vertex 1.358637e-01 -8.210982e-01 6.163431e-01
    endloop
  endfacet
  facet normal 9.954409e-01 -3.300348e-02 8.948864e-02
    outer loop
      vertex 1.391674e-01 -7.182033e-01 6.175418e-01
      vertex 1.358637e-01 -8.210982e-01 6.163431e-01
      vertex 1.413051e-01 -7.644774e-01 5.766968e-01
    endloop
  endfacet
  facet normal -3.026901e-01 6.112407e-01 -7.312753e-01
    outer loop
      vertex 1.338084e-01 -7.739675e-01 6.565883e-01
      vertex 3.441437e-01 -7.172887e-01 6.169014e-01
      vertex 3.494300e-01 -7.635488e-01 5.760466e-01
    endloop
  endfacet
  facet normal -3.026901e-01 6.112407e-01 -7.312753e-01
    outer loop
      vertex 1.338084e-01 -7.739675e-01 6.565883e-01
      vertex 3.494300e-01 -7.635488e-01 5.760466e-01
      vertex 1.358637e-01 -8.210982e-01 6.163431e-01
    endloop
  endfacet
  facet normal 2.543255e-01 7.916449e-01 5.555330e-01
    outer loop
      vertex 2.882454e-01 -7.084195e-01 4.898932e-01
      vertex 1.857426e-01 -6.436768e-01 4.445598e-01
      vertex 1.707128e-01 -7.036724e-01 5.369354e-01
    endloop
  endfacet
  facet normal -5.883228e-01 7.185251e-01 3.709419e-01
    outer loop
      vertex 1.857426e-01 -6.436768e-01 4.445598e-01
      vertex 7.099035e-02 -7.908281e-01 5.475963e-01
      vertex 1.707128e-01 -7.036724e-01 5.369354e-01
    endloop
  endfacet
  facet normal -4.067166e-02 1.670349e-01 9.851117e-01
    outer loop
      vertex 7.099035e-02 -7.908281e-01 5.475963e-01
      vertex 1.449804e-01 -7.965848e-01 5.516272e-01
      vertex 1.707128e-01 -7.036724e-01 5.369354e-01
    endloop
  endfacet
  facet normal 3.727486e-01 4.333529e-02 9.269199e-01
    outer loop
      vertex 1.449804e-01 -7.965848e-01 5.516272e-01
      vertex 2.882454e-01 -7.084195e-01 4.898932e-01
      vertex 1.707128e-01 -7.036724e-01 5.369354e-01
    endloop
  endfacet
  facet normal 1.531755e-16 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 2.925637e-01 -7.534037e-01 4.481450e-01
      vertex 7.205386e-02 -8.370469e-01 5.067126e-01
      vertex 1.885253e-01 -6.876911e-01 4.021325e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 2.925637e-01 -7.534037e-01 4.481450e-01
      vertex 1.471524e-01 -8.428899e-01 5.108039e-01
      vertex 7.205386e-02 -8.370469e-01 5.067126e-01
    endloop
  endfacet
  facet normal -6.058056e-01 -5.716825e-01 5.533342e-01
    outer loop
      vertex 2.882454e-01 -7.084195e-01 4.898932e-01
      vertex 1.857426e-01 -6.436768e-01 4.445598e-01
      vertex 1.885253e-01 -6.876911e-01 4.021325e-01
    endloop
  endfacet
  facet normal -6.058056e-01 -5.716825e-01 5.533342e-01
    outer loop
      vertex 2.882454e-01 -7.084195e-01 4.898932e-01
      vertex 1.885253e-01 -6.876911e-01 4.021325e-01
      vertex 2.925637e-01 -7.534037e-01 4.481450e-01
    endloop
  endfacet
  facet normal 8.341011e-01 -3.545807e-01 4.225493e-01
    outer loop
      vertex 1.857426e-01 -6.436768e-01 4.445598e-01
      vertex 7.099035e-02 -7.908281e-01 5.475963e-01
      vertex 7.205386e-02 -8.370469e-01 5.067126e-01
    endloop
  endfacet
  facet normal 8.341011e-01 -3.545807e-01 4.225493e-01
    outer loop
      vertex 1.857426e-01 -6.436768e-01 4.445598e-01
      vertex 7.205386e-02 -8.370469e-01 5.067126e-01
      vertex 1.885253e-01 -6.876911e-01 4.021325e-01
    endloop
  endfacet
  facet normal 9.199778e-02 6.609312e-01 -7.447861e-01
    outer loop
      vertex 7.099035e-02 -7.908281e-01 5.475963e-01
      vertex 1.449804e-01 -7.965848e-01 5.516272e-01
      vertex 1.471524e-01 -8.428899e-01 5.108039e-01
    endloop
  endfacet
  facet normal 9.199778e-02 6.609312e-01 -7.447861e-01
    outer loop
      vertex 7.099035e-02 -7.908281e-01 5.475963e-01
      vertex 1.471524e-01 -8.428899e-01 5.108039e-01
      vertex 7.205386e-02 -8.370469e-01 5.067126e-01
    endloop
  endfacet
  facet normal -5.872080e-01 5.196169e-01 -6.206328e-01
    outer loop
      vertex 1.449804e-01 -7.965848e-01 5.516272e-01
      vertex 2.882454e-01 -7.084195e-01 4.898932e-01
      vertex 2.925637e-01 -7.534037e-01 4.481450e-01
    endloop
  endfacet
  facet normal -5.872080e-01 5.196169e-01 -6.206328e-01
    outer loop
      vertex 1.449804e-01 -7.965848e-01 5.516272e-01
      vertex 2.925637e-01 -7.534037e-01 4.481450e-01
      vertex 1.471524e-01 -8.428899e-01 5.108039e-01
    endloop
  endfacet
  facet normal 1.559244e-01 8.813757e-01 4.459422e-01
    outer loop
      vertex 1.742901e-01 -4.201563e-01 6.628391e-01
      vertex 1.233947e-01 -4.062123e-01 6.530754e-01
      vertex 8.871749e-02 -4.324811e-01 7.171189e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.251963e-01 3.794888e-01
    outer loop
      vertex 1.233947e-01 -4.062123e-01 6.530754e-01
      vertex 5.389545e-02 -4.062123e-01 6.530754e-01
      vertex 8.871749e-02 -4.324811e-01 7.171189e-01
    endloop
  endfacet
  facet normal -6.236069e-01 5.434223e-01 5.619668e-01
    outer loop
      vertex 5.389545e-02 -4.062123e-01 6.530754e-01
      vertex 2.820431e-02 -5.130708e-01 7.278985e-01
      vertex 8.871749e-02 -4.324811e-01 7.171189e-01
    endloop
  endfacet
  facet normal -2.992193e-01 3.437394e-01 8.901186e-01
    outer loop
      vertex 2.820431e-02 -5.130708e-01 7.278985e-01
      vertex 6.833425e-02 -5.560276e-01 7.579772e-01
      vertex 8.871749e-02 -4.324811e-01 7.171189e-01
    endloop
  endfacet
  facet normal 5.052459e-01 1.946816e-01 8.407292e-01
    outer loop
      vertex 6.833425e-02 -5.560276e-01 7.579772e-01
      vertex 1.742901e-01 -4.201563e-01 6.628391e-01
      vertex 8.871749e-02 -4.324811e-01 7.171189e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 1.771179e-01 -4.641981e-01 6.204310e-01
      vertex 5.476990e-02 -4.500279e-01 6.105089e-01
      vertex 1.253967e-01 -4.500279e-01 6.105089e-01
    endloop
  endfacet
  facet normal 5.723136e-16 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 1.771179e-01 -4.641981e-01 6.204310e-01
      vertex 2.866192e-02 -5.586201e-01 6.865460e-01
      vertex 5.476990e-02 -4.500279e-01 6.105089e-01
    endloop
  endfacet
  facet normal 4.126304e-16 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 1.771179e-01 -4.641981e-01 6.204310e-01
      vertex 6.944297e-02 -6.022739e-01 7.171127e-01
      vertex 2.866192e-02 -5.586201e-01 6.865460e-01
    endloop
  endfacet
  facet normal -3.126600e-01 -6.691860e-01 6.741171e-01
    outer loop
      vertex 1.742901e-01 -4.201563e-01 6.628391e-01
      vertex 1.233947e-01 -4.062123e-01 6.530754e-01
      vertex 1.253967e-01 -4.500279e-01 6.105089e-01
    endloop
  endfacet
  facet normal -3.126600e-01 -6.691860e-01 6.741171e-01
    outer loop
      vertex 1.742901e-01 -4.201563e-01 6.628391e-01
      vertex 1.253967e-01 -4.500279e-01 6.105089e-01
      vertex 1.771179e-01 -4.641981e-01 6.204310e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -6.968092e-01 7.172565e-01
    outer loop
      vertex 1.233947e-01 -4.062123e-01 6.530754e-01
      vertex 5.389545e-02 -4.062123e-01 6.530754e-01
      vertex 5.476990e-02 -4.500279e-01 6.105089e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -6.968092e-01 7.172565e-01
    outer loop
      vertex 1.233947e-01 -4.062123e-01 6.530754e-01
      vertex 5.476990e-02 -4.500279e-01 6.105089e-01
      vertex 1.253967e-01 -4.500279e-01 6.105089e-01
    endloop
  endfacet
  facet normal 9.798669e-01 -1.287150e-01 1.526215e-01
    outer loop
      vertex 5.389545e-02 -4.062123e-01 6.530754e-01
      vertex 2.820431e-02 -5.130708e-01 7.278985e-01
      vertex 2.866192e-02 -5.586201e-01 6.865460e-01
    endloop
  endfacet
  facet normal 9.798669e-01 -1.287150e-01 1.526215e-01
    outer loop
      vertex 5.389545e-02 -4.062123e-01 6.530754e-01
      vertex 2.866192e-02 -5.586201e-01 6.865460e-01
      vertex 5.476990e-02 -4.500279e-01 6.105089e-01
    endloop
  endfacet
  facet normal 7.873600e-01 4.187087e-01 -4.524901e-01
    outer loop
      vertex 2.820431e-02 -5.130708e-01 7.278985e-01
      vertex 6.833425e-02 -5.560276e-01 7.579772e-01
      vertex 6.944297e-02 -6.022739e-01 7.171127e-01
    endloop
  endfacet
  facet normal 7.873600e-01 4.187087e-01 -4.524901e-01
    outer loop
      vertex 2.820431e-02 -5.130708e-01 7.278985e-01
      vertex 6.944297e-02 -6.022739e-01 7.171127e-01
      vertex 2.866192e-02 -5.586201e-01 6.865460e-01
    endloop
  endfacet
  facet normal -8.339905e-01 3.540025e-01 -4.232518e-01
    outer loop
      vertex 6.833425e-02 -5.560276e-01 7.579772e-01
      vertex 1.742901e-01 -4.201563e-01 6.628391e-01
      vertex 1.771179e-01 -4.641981e-01 6.204310e-01
    endloop
  endfacet
  facet normal -8.339905e-01 3.540025e-01 -4.232518e-01
    outer loop
      vertex 6.833425e-02 -5.560276e-01 7.579772e-01
      vertex 1.771179e-01 -4.641981e-01 6.204310e-01
      vertex 6.944297e-02 -6.022739e-01 7.171127e-01
    endloop
  endfacet
  facet normal -6.754540e-01 3.082035e-01 6.699049e-01
    outer loop
      vertex -5.596744e-02 -3.447652e-01 7.123147e-01
      vertex -2.416118e-02 -4.783128e-01 8.058258e-01
      vertex -6.197854e-03 -3.791025e-01 7.782942e-01
    endloop
  endfacet
  facet normal 2.321452e-01 2.208441e-01 9.472785e-01
    outer loop
      vertex -2.416118e-02 -4.783128e-01 8.058258e-01
      vertex 2.754966e-02 -4.511809e-01 7.868278e-01
      vertex -6.197854e-03 -3.791025e-01 7.782942e-01
    endloop
  endfacet
  facet normal 7.133566e-01 4.019631e-01 5.740628e-01
    outer loop
      vertex 2.754966e-02 -4.511809e-01 7.868278e-01
      vertex 2.754966e-02 -3.447652e-01 7.123147e-01
      vertex -6.197854e-03 -3.791025e-01 7.782942e-01
    endloop
  endfacet
  facet normal 0.000000e+00 8.870628e-01 4.616489e-01
    outer loop
      vertex 2.754966e-02 -3.447652e-01 7.123147e-01
      vertex -5.596744e-02 -3.447652e-01 7.123147e-01
      vertex -6.197854e-03 -3.791025e-01 7.782942e-01
    endloop
  endfacet
  facet normal -5.309577e-16 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -5.689655e-02 -3.885762e-01 6.697451e-01
      vertex 2.800701e-02 -4.967586e-01 7.454952e-01
      vertex -2.456228e-02 -5.243409e-01 7.648085e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -5.689655e-02 -3.885762e-01 6.697451e-01
      vertex 2.800701e-02 -3.885762e-01 6.697451e-01
      vertex 2.800701e-02 -4.967586e-01 7.454952e-01
    endloop
  endfacet
  facet normal 9.801815e-01 1.269680e-01 -1.520637e-01
    outer loop
      vertex -5.596744e-02 -3.447652e-01 7.123147e-01
      vertex -2.416118e-02 -4.783128e-01 8.058258e-01
      vertex -2.456228e-02 -5.243409e-01 7.648085e-01
    endloop
  endfacet
  facet normal 9.801815e-01 1.269680e-01 -1.520637e-01
    outer loop
      vertex -5.596744e-02 -3.447652e-01 7.123147e-01
      vertex -2.456228e-02 -5.243409e-01 7.648085e-01
      vertex -5.689655e-02 -3.885762e-01 6.697451e-01
    endloop
  endfacet
  facet normal -5.293572e-01 5.670070e-01 -6.310974e-01
    outer loop
      vertex -2.416118e-02 -4.783128e-01 8.058258e-01
      vertex 2.754966e-02 -4.511809e-01 7.868278e-01
      vertex 2.800701e-02 -4.967586e-01 7.454952e-01
    endloop
  endfacet
  facet normal -5.293572e-01 5.670070e-01 -6.310974e-01
    outer loop
      vertex -2.416118e-02 -4.783128e-01 8.058258e-01
      vertex 2.800701e-02 -4.967586e-01 7.454952e-01
      vertex -2.456228e-02 -5.243409e-01 7.648085e-01
    endloop
  endfacet
  facet normal -9.999710e-01 -4.371959e-03 -6.243804e-03
    outer loop
      vertex 2.754966e-02 -4.511809e-01 7.868278e-01
      vertex 2.754966e-02 -3.447652e-01 7.123147e-01
      vertex 2.800701e-02 -3.885762e-01 6.697451e-01
    endloop
  endfacet
  facet normal -9.999710e-01 -4.371959e-03 -6.243804e-03
    outer loop
      vertex 2.754966e-02 -4.511809e-01 7.868278e-01
      vertex 2.800701e-02 -3.885762e-01 6.697451e-01
      vertex 2.800701e-02 -4.967586e-01 7.454952e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -6.968730e-01 7.171946e-01
    outer loop
      vertex 2.754966e-02 -3.447652e-01 7.123147e-01
      vertex -5.596744e-02 -3.447652e-01 7.123147e-01
      vertex -5.689655e-02 -3.885762e-01 6.697451e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -6.968730e-01 7.171946e-01
    outer loop
      vertex 2.754966e-02 -3.447652e-01 7.123147e-01
      vertex -5.689655e-02 -3.885762e-01 6.697451e-01
      vertex 2.800701e-02 -3.885762e-01 6.697451e-01
    endloop
  endfacet
  facet normal -1.457125e-01 8.663479e-01 4.777124e-01
    outer loop
      vertex -1.330547e-01 -6.199262e-01 4.454042e-01
      vertex -1.879784e-01 -6.349738e-01 4.559406e-01
      vertex -9.845412e-02 -6.513291e-01 5.129083e-01
    endloop
  endfacet
  facet normal -5.006556e-01 1.962284e-01 8.431123e-01
    outer loop
      vertex -1.879784e-01 -6.349738e-01 4.559406e-01
      vertex -9.480303e-02 -7.533341e-01 5.388174e-01
      vertex -9.845412e-02 -6.513291e-01 5.129083e-01
    endloop
  endfacet
  facet normal -8.495320e-02 2.424330e-01 9.664415e-01
    outer loop
      vertex -9.480303e-02 -7.533341e-01 5.388174e-01
      vertex -2.297890e-02 -7.673843e-01 5.486554e-01
      vertex -9.845412e-02 -6.513291e-01 5.129083e-01
    endloop
  endfacet
  facet normal 5.722895e-01 5.574404e-01 6.014524e-01
    outer loop
      vertex -2.297890e-02 -7.673843e-01 5.486554e-01
      vertex -5.809815e-02 -6.199262e-01 4.454042e-01
      vertex -9.845412e-02 -6.513291e-01 5.129083e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.066922e-01 4.217928e-01
    outer loop
      vertex -5.809815e-02 -6.199262e-01 4.454042e-01
      vertex -1.330547e-01 -6.199262e-01 4.454042e-01
      vertex -9.845412e-02 -6.513291e-01 5.129083e-01
    endloop
  endfacet
  facet normal -1.963367e-16 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -1.350551e-01 -6.637413e-01 4.028374e-01
      vertex -9.622838e-02 -7.991550e-01 4.976550e-01
      vertex -1.908046e-01 -6.790152e-01 4.135322e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -1.350551e-01 -6.637413e-01 4.028374e-01
      vertex -2.332439e-02 -8.134164e-01 5.076410e-01
      vertex -9.622838e-02 -7.991550e-01 4.976550e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -1.350551e-01 -6.637413e-01 4.028374e-01
      vertex -5.897165e-02 -6.637413e-01 4.028374e-01
      vertex -2.332439e-02 -8.134164e-01 5.076410e-01
    endloop
  endfacet
  facet normal 3.126600e-01 -6.691861e-01 6.741170e-01
    outer loop
      vertex -1.330547e-01 -6.199262e-01 4.454042e-01
      vertex -1.879784e-01 -6.349738e-01 4.559406e-01
      vertex -1.908046e-01 -6.790152e-01 4.135322e-01
    endloop
  endfacet
  facet normal 3.126600e-01 -6.691861e-01 6.741170e-01
    outer loop
      vertex -1.330547e-01 -6.199262e-01 4.454042e-01
      vertex -1.908046e-01 -6.790152e-01 4.135322e-01
      vertex -1.350551e-01 -6.637413e-01 4.028374e-01
    endloop
  endfacet
  facet normal 8.316301e-01 3.565760e-01 -4.257287e-01
    outer loop
      vertex -1.879784e-01 -6.349738e-01 4.559406e-01
      vertex -9.480303e-02 -7.533341e-01 5.388174e-01
      vertex -9.622838e-02 -7.991550e-01 4.976550e-01
    endloop
  endfacet
  facet normal 8.316301e-01 3.565760e-01 -4.257287e-01
    outer loop
      vertex -1.879784e-01 -6.349738e-01 4.559406e-01
      vertex -9.622838e-02 -7.991550e-01 4.976550e-01
      vertex -1.908046e-01 -6.790152e-01 4.135322e-01
    endloop
  endfacet
  facet normal 2.263045e-01 6.470361e-01 -7.281007e-01
    outer loop
      vertex -9.480303e-02 -7.533341e-01 5.388174e-01
      vertex -2.297890e-02 -7.673843e-01 5.486554e-01
      vertex -2.332439e-02 -8.134164e-01 5.076410e-01
    endloop
  endfacet
  facet normal 2.263045e-01 6.470361e-01 -7.281007e-01
    outer loop
      vertex -9.480303e-02 -7.533341e-01 5.388174e-01
      vertex -2.332439e-02 -8.134164e-01 5.076410e-01
      vertex -9.622838e-02 -7.991550e-01 4.976550e-01
    endloop
  endfacet
  facet normal -9.802264e-01 -1.274859e-01 1.513394e-01
    outer loop
      vertex -2.297890e-02 -7.673843e-01 5.486554e-01
      vertex -5.809815e-02 -6.199262e-01 4.454042e-01
      vertex -5.897165e-02 -6.637413e-01 4.028374e-01
    endloop
  endfacet
  facet normal -9.802264e-01 -1.274859e-01 1.513394e-01
    outer loop
      vertex -2.297890e-02 -7.673843e-01 5.486554e-01
      vertex -5.897165e-02 -6.637413e-01 4.028374e-01
      vertex -2.332439e-02 -8.134164e-01 5.076410e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -6.968155e-01 7.172504e-01
    outer loop
      vertex -5.809815e-02 -6.199262e-01 4.454042e-01
      vertex -1.330547e-01 -6.199262e-01 4.454042e-01
      vertex -1.350551e-01 -6.637413e-01 4.028374e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -6.968155e-01 7.172504e-01
    outer loop
      vertex -5.809815e-02 -6.199262e-01 4.454042e-01
      vertex -1.350551e-01 -6.637413e-01 4.028374e-01
      vertex -5.897165e-02 -6.637413e-01 4.028374e-01
    endloop
  endfacet
  facet normal -2.824523e-01 8.085921e-01 5.161390e-01
    outer loop
      vertex -1.776084e-01 -5.218924e-01 5.623705e-01
      vertex -2.530316e-01 -5.695311e-01 5.957275e-01
      vertex -1.740402e-01 -5.737825e-01 6.456152e-01
    endloop
  endfacet
  facet normal -4.374550e-01 5.157831e-01 7.366145e-01
    outer loop
      vertex -2.530316e-01 -5.695311e-01 5.957275e-01
      vertex -2.530316e-01 -5.981236e-01 6.157482e-01
      vertex -1.740402e-01 -5.737825e-01 6.456152e-01
    endloop
  endfacet
  facet normal -3.683631e-01 5.680120e-02 9.279452e-01
    outer loop
      vertex -2.530316e-01 -5.981236e-01 6.157482e-01
      vertex -1.073455e-01 -6.886289e-01 6.791207e-01
      vertex -1.740402e-01 -5.737825e-01 6.456152e-01
    endloop
  endfacet
  facet normal 3.545858e-01 4.457162e-01 8.219525e-01
    outer loop
      vertex -1.073455e-01 -6.886289e-01 6.791207e-01
      vertex -8.798296e-02 -6.357432e-01 6.420897e-01
      vertex -1.740402e-01 -5.737825e-01 6.456152e-01
    endloop
  endfacet
  facet normal 5.393952e-01 7.247757e-01 4.286642e-01
    outer loop
      vertex -8.798296e-02 -6.357432e-01 6.420897e-01
      vertex -1.776084e-01 -5.218924e-01 5.623705e-01
      vertex -1.740402e-01 -5.737825e-01 6.456152e-01
    endloop
  endfacet
  facet normal -1.597001e-15 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -1.803845e-01 -5.659106e-01 5.199459e-01
      vertex -2.569866e-01 -6.433334e-01 5.741579e-01
      vertex -2.569866e-01 -6.142939e-01 5.538243e-01
    endloop
  endfacet
  facet normal 7.682348e-17 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -1.803845e-01 -5.659106e-01 5.199459e-01
      vertex -1.090234e-01 -7.352533e-01 6.385209e-01
      vertex -2.569866e-01 -6.433334e-01 5.741579e-01
    endloop
  endfacet
  facet normal -3.967546e-16 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -1.803845e-01 -5.659106e-01 5.199459e-01
      vertex -8.935817e-02 -6.815410e-01 6.009112e-01
      vertex -1.090234e-01 -7.352533e-01 6.385209e-01
    endloop
  endfacet
  facet normal 6.057958e-01 -5.715994e-01 5.534308e-01
    outer loop
      vertex -1.776084e-01 -5.218924e-01 5.623705e-01
      vertex -2.530316e-01 -5.695311e-01 5.957275e-01
      vertex -2.569866e-01 -6.142939e-01 5.538243e-01
    endloop
  endfacet
  facet normal 6.057958e-01 -5.715994e-01 5.534308e-01
    outer loop
      vertex -1.776084e-01 -5.218924e-01 5.623705e-01
      vertex -2.569866e-01 -6.142939e-01 5.538243e-01
      vertex -1.803845e-01 -5.659106e-01 5.199459e-01
    endloop
  endfacet
  facet normal 9.978346e-01 -3.772618e-02 -5.387857e-02
    outer loop
      vertex -2.530316e-01 -5.695311e-01 5.957275e-01
      vertex -2.530316e-01 -5.981236e-01 6.157482e-01
      vertex -2.569866e-01 -6.433334e-01 5.741579e-01
    endloop
  endfacet
  facet normal 9.978346e-01 -3.772618e-02 -5.387857e-02
    outer loop
      vertex -2.530316e-01 -5.695311e-01 5.957275e-01
      vertex -2.569866e-01 -6.433334e-01 5.741579e-01
      vertex -2.569866e-01 -6.142939e-01 5.538243e-01
    endloop
  endfacet
  facet normal 5.907885e-01 5.176477e-01 -6.188779e-01
    outer loop
      vertex -2.530316e-01 -5.981236e-01 6.157482e-01
      vertex -1.073455e-01 -6.886289e-01 6.791207e-01
      vertex -1.090234e-01 -7.352533e-01 6.385209e-01
    endloop
  endfacet
  facet normal 5.907885e-01 5.176477e-01 -6.188779e-01
    outer loop
      vertex -2.530316e-01 -5.981236e-01 6.157482e-01
      vertex -1.090234e-01 -7.352533e-01 6.385209e-01
      vertex -2.569866e-01 -6.433334e-01 5.741579e-01
    endloop
  endfacet
  facet normal -9.569001e-01 2.095383e-01 -2.010867e-01
    outer loop
      vertex -1.073455e-01 -6.886289e-01 6.791207e-01
      vertex -8.798296e-02 -6.357432e-01 6.420897e-01
      vertex -8.935817e-02 -6.815410e-01 6.009112e-01
    endloop
  endfacet
  facet normal -9.569001e-01 2.095383e-01 -2.010867e-01
    outer loop
      vertex -1.073455e-01 -6.886289e-01 6.791207e-01
      vertex -8.935817e-02 -6.815410e-01 6.009112e-01
      vertex -1.090234e-01 -7.352533e-01 6.385209e-01
    endloop
  endfacet
  facet normal -8.317434e-01 -3.571679e-01 4.250107e-01
    outer loop
      vertex -8.798296e-02 -6.357432e-01 6.420897e-01
      vertex -1.776084e-01 -5.218924e-01 5.623705e-01
      vertex -1.803845e-01 -5.659106e-01 5.199459e-01
    endloop
  endfacet
  facet normal -8.317434e-01 -3.571679e-01 4.250107e-01
    outer loop
      vertex -8.798296e-02 -6.357432e-01 6.420897e-01
      vertex -1.803845e-01 -5.659106e-01 5.199459e-01
      vertex -8.935817e-02 -6.815410e-01 6.009112e-01
    endloop
  endfacet
  facet normal -5.370568e-01 7.198480e-01 4.397600e-01
    outer loop
      vertex -3.060151e-01 -9.445413e-01 2.689393e-01
      vertex -3.782049e-01 -1.038661e+00 3.348423e-01
      vertex -3.093614e-01 -9.824745e-01 3.269459e-01
    endloop
  endfacet
  facet normal -1.078170e-01 2.667055e-01 9.577284e-01
    outer loop
      vertex -3.782049e-01 -1.038661e+00 3.348423e-01
      vertex -2.803228e-01 -1.064789e+00 3.531376e-01
      vertex -3.093614e-01 -9.824745e-01 3.269459e-01
    endloop
  endfacet
  facet normal 6.635950e-01 4.290880e-01 6.128011e-01
    outer loop
      vertex -2.803228e-01 -1.064789e+00 3.531376e-01
      vertex -2.803228e-01 -9.605022e-01 2.801152e-01
      vertex -3.093614e-01 -9.824745e-01 3.269459e-01
    endloop
  endfacet
  facet normal 2.629724e-01 8.004553e-01 5.386250e-01
    outer loop
      vertex -2.803228e-01 -9.605022e-01 2.801152e-01
      vertex -3.060151e-01 -9.445413e-01 2.689393e-01
      vertex -3.093614e-01 -9.824745e-01 3.269459e-01
    endloop
  endfacet
  facet normal -1.619143e-15 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -3.102638e-01 -9.895100e-01 2.271803e-01
      vertex -2.842149e-01 -1.111427e+00 3.125476e-01
      vertex -3.834560e-01 -1.084936e+00 2.939983e-01
    endloop
  endfacet
  facet normal -1.870228e-15 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -3.102638e-01 -9.895100e-01 2.271803e-01
      vertex -2.842149e-01 -1.005693e+00 2.385114e-01
      vertex -2.842149e-01 -1.111427e+00 3.125476e-01
    endloop
  endfacet
  facet normal 8.454981e-01 -4.040620e-01 3.490943e-01
    outer loop
      vertex -3.060151e-01 -9.445413e-01 2.689393e-01
      vertex -3.782049e-01 -1.038661e+00 3.348423e-01
      vertex -3.834560e-01 -1.084936e+00 2.939983e-01
    endloop
  endfacet
  facet normal 8.454981e-01 -4.040620e-01 3.490943e-01
    outer loop
      vertex -3.060151e-01 -9.445413e-01 2.689393e-01
      vertex -3.834560e-01 -1.084936e+00 2.939983e-01
      vertex -3.102638e-01 -9.895100e-01 2.271803e-01
    endloop
  endfacet
  facet normal 3.001147e-01 6.118644e-01 -7.318150e-01
    outer loop
      vertex -3.782049e-01 -1.038661e+00 3.348423e-01
      vertex -2.803228e-01 -1.064789e+00 3.531376e-01
      vertex -2.842149e-01 -1.111427e+00 3.125476e-01
    endloop
  endfacet
  facet normal 3.001147e-01 6.118644e-01 -7.318150e-01
    outer loop
      vertex -3.782049e-01 -1.038661e+00 3.348423e-01
      vertex -2.842149e-01 -1.111427e+00 3.125476e-01
      vertex -3.834560e-01 -1.084936e+00 2.939983e-01
    endloop
  endfacet
  facet normal -9.979027e-01 3.712847e-02 5.302495e-02
    outer loop
      vertex -2.803228e-01 -1.064789e+00 3.531376e-01
      vertex -2.803228e-01 -9.605022e-01 2.801152e-01
      vertex -2.842149e-01 -1.005693e+00 2.385114e-01
    endloop
  endfacet
  facet normal -9.979027e-01 3.712847e-02 5.302495e-02
    outer loop
      vertex -2.803228e-01 -1.064789e+00 3.531376e-01
      vertex -2.842149e-01 -1.005693e+00 2.385114e-01
      vertex -2.842149e-01 -1.111427e+00 3.125476e-01
    endloop
  endfacet
  facet normal -5.909034e-01 -5.182804e-01 6.182383e-01
    outer loop
      vertex -2.803228e-01 -9.605022e-01 2.801152e-01
      vertex -3.060151e-01 -9.445413e-01 2.689393e-01
      vertex -3.102638e-01 -9.895100e-01 2.271803e-01
    endloop
  endfacet
  facet normal -5.909034e-01 -5.182804e-01 6.182383e-01
    outer loop
      vertex -2.803228e-01 -9.605022e-01 2.801152e-01
      vertex -3.102638e-01 -9.895100e-01 2.271803e-01
      vertex -2.842149e-01 -1.005693e+00 2.385114e-01
    endloop
  endfacet
  facet normal -1.730822e-01 4.065288e-02 9.840680e-01
    outer loop
      vertex -2.502826e-01 -6.648697e-01 6.989511e-01
      vertex -1.694229e-01 -6.864542e-01 7.140647e-01
      vertex -1.923475e-01 -6.227652e-01 7.074016e-01
    endloop
  endfacet
  facet normal 1.890367e-01 1.692391e-01 9.672762e-01
    outer loop
      vertex -1.694229e-01 -6.864542e-01 7.140647e-01
      vertex -1.057303e-01 -6.627555e-01 6.974707e-01
      vertex -1.923475e-01 -6.227652e-01 7.074016e-01
    endloop
  endfacet
  facet normal 4.293145e-01 8.673542e-01 2.517651e-01
    outer loop
      vertex -1.057303e-01 -6.627555e-01 6.974707e-01
      vertex -2.502826e-01 -5.729545e-01 6.345914e-01
      vertex -1.923475e-01 -6.227652e-01 7.074016e-01
    endloop
  endfacet
  facet normal -4.726441e-01 5.054662e-01 7.218805e-01
    outer loop
      vertex -2.502826e-01 -5.729545e-01 6.345914e-01
      vertex -2.502826e-01 -6.648697e-01 6.989511e-01
      vertex -1.923475e-01 -6.227652e-01 7.074016e-01
    endloop
  endfacet
  facet normal -5.623452e-16 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -2.542253e-01 -7.114855e-01 6.583454e-01
      vertex -1.073958e-01 -7.093380e-01 6.568417e-01
      vertex -1.720919e-01 -7.334101e-01 6.736971e-01
    endloop
  endfacet
  facet normal -5.847003e-16 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -2.542253e-01 -7.114855e-01 6.583454e-01
      vertex -2.542253e-01 -6.181224e-01 5.929718e-01
      vertex -1.073958e-01 -7.093380e-01 6.568417e-01
    endloop
  endfacet
  facet normal 3.001272e-01 6.119864e-01 -7.317078e-01
    outer loop
      vertex -2.502826e-01 -6.648697e-01 6.989511e-01
      vertex -1.694229e-01 -6.864542e-01 7.140647e-01
      vertex -1.720919e-01 -7.334101e-01 6.736971e-01
    endloop
  endfacet
  facet normal 3.001272e-01 6.119864e-01 -7.317078e-01
    outer loop
      vertex -2.502826e-01 -6.648697e-01 6.989511e-01
      vertex -1.720919e-01 -7.334101e-01 6.736971e-01
      vertex -2.542253e-01 -7.114855e-01 6.583454e-01
    endloop
  endfacet
  facet normal -4.044107e-01 6.093279e-01 -6.820348e-01
    outer loop
      vertex -1.694229e-01 -6.864542e-01 7.140647e-01
      vertex -1.057303e-01 -6.627555e-01 6.974707e-01
      vertex -1.073958e-01 -7.093380e-01 6.568417e-01
    endloop
  endfacet
  facet normal -4.044107e-01 6.093279e-01 -6.820348e-01
    outer loop
      vertex -1.694229e-01 -6.864542e-01 7.140647e-01
      vertex -1.073958e-01 -7.093380e-01 6.568417e-01
      vertex -1.720919e-01 -7.334101e-01 6.736971e-01
    endloop
  endfacet
  facet normal -5.908858e-01 -5.181834e-01 6.183364e-01
    outer loop
      vertex -1.057303e-01 -6.627555e-01 6.974707e-01
      vertex -2.502826e-01 -5.729545e-01 6.345914e-01
      vertex -2.542253e-01 -6.181224e-01 5.929718e-01
    endloop
  endfacet
  facet normal -5.908858e-01 -5.181834e-01 6.183364e-01
    outer loop
      vertex -1.057303e-01 -6.627555e-01 6.974707e-01
      vertex -2.542253e-01 -6.181224e-01 5.929718e-01
      vertex -1.073958e-01 -7.093380e-01 6.568417e-01
    endloop
  endfacet
  facet normal 9.978480e-01 -3.760949e-02 -5.371192e-02
    outer loop
      vertex -2.502826e-01 -5.729545e-01 6.345914e-01
      vertex -2.502826e-01 -6.648697e-01 6.989511e-01
      vertex -2.542253e-01 -7.114855e-01 6.583454e-01
    endloop
  endfacet
  facet normal 9.978480e-01 -3.760949e-02 -5.371192e-02
    outer loop
      vertex -2.502826e-01 -5.729545e-01 6.345914e-01
      vertex -2.542253e-01 -7.114855e-01 6.583454e-01
      vertex -2.542253e-01 -6.181224e-01 5.929718e-01
    endloop
  endfacet
  facet normal -4.808584e-01 5.757012e-01 6.613194e-01
    outer loop
      vertex -3.363108e-01 -6.734996e-01 6.519017e-01
      vertex -3.586601e-01 -7.689084e-01 7.187076e-01
      vertex -2.960768e-01 -7.048061e-01 7.084100e-01
    endloop
  endfacet
  facet normal -0.000000e+00 1.586096e-01 9.873414e-01
    outer loop
      vertex -3.586601e-01 -7.689084e-01 7.187076e-01
      vertex -2.490554e-01 -7.689084e-01 7.187076e-01
      vertex -2.960768e-01 -7.048061e-01 7.084100e-01
    endloop
  endfacet
  facet normal 5.160946e-01 4.912864e-01 7.016296e-01
    outer loop
      vertex -2.490554e-01 -7.689084e-01 7.187076e-01
      vertex -2.490554e-01 -6.967914e-01 6.682108e-01
      vertex -2.960768e-01 -7.048061e-01 7.084100e-01
    endloop
  endfacet
  facet normal 1.712083e-01 9.084251e-01 3.813812e-01
    outer loop
      vertex -2.490554e-01 -6.967914e-01 6.682108e-01
      vertex -3.363108e-01 -6.734996e-01 6.519017e-01
      vertex -2.960768e-01 -7.048061e-01 7.084100e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -3.415489e-01 -7.197236e-01 6.110216e-01
      vertex -2.529345e-01 -8.166183e-01 6.788680e-01
      vertex -3.642463e-01 -8.166183e-01 6.788680e-01
    endloop
  endfacet
  facet normal -2.189479e-16 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -3.415489e-01 -7.197236e-01 6.110216e-01
      vertex -2.529345e-01 -7.433781e-01 6.275846e-01
      vertex -2.529345e-01 -8.166183e-01 6.788680e-01
    endloop
  endfacet
  facet normal 9.812805e-01 -1.774275e-01 7.488651e-02
    outer loop
      vertex -3.363108e-01 -6.734996e-01 6.519017e-01
      vertex -3.586601e-01 -7.689084e-01 7.187076e-01
      vertex -3.642463e-01 -8.166183e-01 6.788680e-01
    endloop
  endfacet
  facet normal 9.812805e-01 -1.774275e-01 7.488651e-02
    outer loop
      vertex -3.363108e-01 -6.734996e-01 6.519017e-01
      vertex -3.642463e-01 -8.166183e-01 6.788680e-01
      vertex -3.415489e-01 -7.197236e-01 6.110216e-01
    endloop
  endfacet
  facet normal 0.000000e+00 6.409563e-01 -7.675773e-01
    outer loop
      vertex -3.586601e-01 -7.689084e-01 7.187076e-01
      vertex -2.490554e-01 -7.689084e-01 7.187076e-01
      vertex -2.529345e-01 -8.166183e-01 6.788680e-01
    endloop
  endfacet
  facet normal 0.000000e+00 6.409563e-01 -7.675773e-01
    outer loop
      vertex -3.586601e-01 -7.689084e-01 7.187076e-01
      vertex -2.529345e-01 -8.166183e-01 6.788680e-01
      vertex -3.642463e-01 -8.166183e-01 6.788680e-01
    endloop
  endfacet
  facet normal -9.979166e-01 3.700512e-02 5.284878e-02
    outer loop
      vertex -2.490554e-01 -7.689084e-01 7.187076e-01
      vertex -2.490554e-01 -6.967914e-01 6.682108e-01
      vertex -2.529345e-01 -7.433781e-01 6.275846e-01
    endloop
  endfacet
  facet normal -9.979166e-01 3.700512e-02 5.284878e-02
    outer loop
      vertex -2.490554e-01 -7.689084e-01 7.187076e-01
      vertex -2.529345e-01 -7.433781e-01 6.275846e-01
      vertex -2.529345e-01 -8.166183e-01 6.788680e-01
    endloop
  endfacet
  facet normal -3.001914e-01 -6.126127e-01 7.311571e-01
    outer loop
      vertex -2.490554e-01 -6.967914e-01 6.682108e-01
      vertex -3.363108e-01 -6.734996e-01 6.519017e-01
      vertex -3.415489e-01 -7.197236e-01 6.110216e-01
    endloop
  endfacet
  facet normal -3.001914e-01 -6.126127e-01 7.311571e-01
    outer loop
      vertex -2.490554e-01 -6.967914e-01 6.682108e-01
      vertex -3.415489e-01 -7.197236e-01 6.110216e-01
      vertex -2.529345e-01 -7.433781e-01 6.275846e-01
    endloop
  endfacet
  facet normal -0.000000e+00 7.724990e-02 9.970118e-01
    outer loop
      vertex -2.346404e-01 -5.484248e-01 9.022016e-01
      vertex -1.314786e-01 -5.484248e-01 9.022016e-01
      vertex -1.885876e-01 -5.009683e-01 8.985246e-01
    endloop
  endfacet
  facet normal 5.249275e-01 6.721548e-01 5.221676e-01
    outer loop
      vertex -1.314786e-01 -5.484248e-01 9.022016e-01
      vertex -1.587332e-01 -5.017516e-01 8.695207e-01
      vertex -1.885876e-01 -5.009683e-01 8.985246e-01
    endloop
  endfacet
  facet normal 2.179613e-01 9.555481e-01 1.985463e-01
    outer loop
      vertex -1.587332e-01 -5.017516e-01 8.695207e-01
      vertex -2.346404e-01 -4.814891e-01 8.553327e-01
      vertex -1.885876e-01 -5.009683e-01 8.985246e-01
    endloop
  endfacet
  facet normal -4.652888e-01 5.077063e-01 7.250797e-01
    outer loop
      vertex -2.346404e-01 -4.814891e-01 8.553327e-01
      vertex -2.346404e-01 -5.484248e-01 9.022016e-01
      vertex -1.885876e-01 -5.009683e-01 8.985246e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -2.385778e-01 -5.961279e-01 8.623572e-01
      vertex -1.613969e-01 -5.486716e-01 8.291279e-01
      vertex -1.336849e-01 -5.961279e-01 8.623572e-01
    endloop
  endfacet
  facet normal -8.115610e-16 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -2.385778e-01 -5.961279e-01 8.623572e-01
      vertex -2.385778e-01 -5.280691e-01 8.147019e-01
      vertex -1.613969e-01 -5.486716e-01 8.291279e-01
    endloop
  endfacet
  facet normal 0.000000e+00 6.410547e-01 -7.674952e-01
    outer loop
      vertex -2.346404e-01 -5.484248e-01 9.022016e-01
      vertex -1.314786e-01 -5.484248e-01 9.022016e-01
      vertex -1.336849e-01 -5.961279e-01 8.623572e-01
    endloop
  endfacet
  facet normal 0.000000e+00 6.410547e-01 -7.674952e-01
    outer loop
      vertex -2.346404e-01 -5.484248e-01 9.022016e-01
      vertex -1.336849e-01 -5.961279e-01 8.623572e-01
      vertex -2.385778e-01 -5.961279e-01 8.623572e-01
    endloop
  endfacet
  facet normal -8.921465e-01 -2.645759e-01 3.661615e-01
    outer loop
      vertex -1.314786e-01 -5.484248e-01 9.022016e-01
      vertex -1.587332e-01 -5.017516e-01 8.695207e-01
      vertex -1.613969e-01 -5.486716e-01 8.291279e-01
    endloop
  endfacet
  facet normal -8.921465e-01 -2.645759e-01 3.661615e-01
    outer loop
      vertex -1.314786e-01 -5.484248e-01 9.022016e-01
      vertex -1.613969e-01 -5.486716e-01 8.291279e-01
      vertex -1.336849e-01 -5.961279e-01 8.623572e-01
    endloop
  endfacet
  facet normal -3.001792e-01 -6.124927e-01 7.312627e-01
    outer loop
      vertex -1.587332e-01 -5.017516e-01 8.695207e-01
      vertex -2.346404e-01 -4.814891e-01 8.553327e-01
      vertex -2.385778e-01 -5.280691e-01 8.147019e-01
    endloop
  endfacet
  facet normal -3.001792e-01 -6.124927e-01 7.312627e-01
    outer loop
      vertex -1.587332e-01 -5.017516e-01 8.695207e-01
      vertex -2.385778e-01 -5.280691e-01 8.147019e-01
      vertex -1.613969e-01 -5.486716e-01 8.291279e-01
    endloop
  endfacet
  facet normal 9.978537e-01 -3.755963e-02 -5.364071e-02
    outer loop
      vertex -2.346404e-01 -4.814891e-01 8.553327e-01
      vertex -2.346404e-01 -5.484248e-01 9.022016e-01
      vertex -2.385778e-01 -5.961279e-01 8.623572e-01
    endloop
  endfacet
  facet normal 9.978537e-01 -3.755963e-02 -5.364071e-02
    outer loop
      vertex -2.346404e-01 -4.814891e-01 8.553327e-01
      vertex -2.385778e-01 -5.961279e-01 8.623572e-01
      vertex -2.385778e-01 -5.280691e-01 8.147019e-01
    endloop
  endfacet
  facet normal -3.919697e-01 4.643003e-01 7.942197e-01
    outer loop
      vertex -3.354321e-01 -6.977683e-01 8.396040e-01
      vertex -3.242020e-01 -7.457095e-01 8.731727e-01
      vertex -2.833597e-01 -6.991638e-01 8.661190e-01
    endloop
  endfacet
  facet normal 1.878275e-01 -1.598352e-02 9.820720e-01
    outer loop
      vertex -3.242020e-01 -7.457095e-01 8.731727e-01
      vertex -2.401139e-01 -7.232632e-01 8.574557e-01
      vertex -2.833597e-01 -6.991638e-01 8.661190e-01
    endloop
  endfacet
  facet normal 4.354596e-01 5.163382e-01 7.374074e-01
    outer loop
      vertex -2.401139e-01 -7.232632e-01 8.574557e-01
      vertex -2.401139e-01 -6.977683e-01 8.396040e-01
      vertex -2.833597e-01 -6.991638e-01 8.661190e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.986179e-01 5.255808e-02
    outer loop
      vertex -2.401139e-01 -6.977683e-01 8.396040e-01
      vertex -3.354321e-01 -6.977683e-01 8.396040e-01
      vertex -2.833597e-01 -6.991638e-01 8.661190e-01
    endloop
  endfacet
  facet normal -1.204803e-16 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -3.408533e-01 -7.461256e-01 8.002176e-01
      vertex -2.439946e-01 -7.720326e-01 8.183579e-01
      vertex -3.294416e-01 -7.948416e-01 8.343289e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -3.408533e-01 -7.461256e-01 8.002176e-01
      vertex -2.439946e-01 -7.461256e-01 8.002176e-01
      vertex -2.439946e-01 -7.720326e-01 8.183579e-01
    endloop
  endfacet
  facet normal 9.723030e-01 7.208325e-02 -2.223304e-01
    outer loop
      vertex -3.354321e-01 -6.977683e-01 8.396040e-01
      vertex -3.242020e-01 -7.457095e-01 8.731727e-01
      vertex -3.294416e-01 -7.948416e-01 8.343289e-01
    endloop
  endfacet
  facet normal 9.723030e-01 7.208325e-02 -2.223304e-01
    outer loop
      vertex -3.354321e-01 -6.977683e-01 8.396040e-01
      vertex -3.294416e-01 -7.948416e-01 8.343289e-01
      vertex -3.408533e-01 -7.461256e-01 8.002176e-01
    endloop
  endfacet
  facet normal -3.000360e-01 6.111002e-01 -7.324855e-01
    outer loop
      vertex -3.242020e-01 -7.457095e-01 8.731727e-01
      vertex -2.401139e-01 -7.232632e-01 8.574557e-01
      vertex -2.439946e-01 -7.720326e-01 8.183579e-01
    endloop
  endfacet
  facet normal -3.000360e-01 6.111002e-01 -7.324855e-01
    outer loop
      vertex -3.242020e-01 -7.457095e-01 8.731727e-01
      vertex -2.439946e-01 -7.720326e-01 8.183579e-01
      vertex -3.294416e-01 -7.948416e-01 8.343289e-01
    endloop
  endfacet
  facet normal -9.979149e-01 3.702033e-02 5.287052e-02
    outer loop
      vertex -2.401139e-01 -7.232632e-01 8.574557e-01
      vertex -2.401139e-01 -6.977683e-01 8.396040e-01
      vertex -2.439946e-01 -7.461256e-01 8.002176e-01
    endloop
  endfacet
  facet normal -9.979149e-01 3.702033e-02 5.287052e-02
    outer loop
      vertex -2.401139e-01 -7.232632e-01 8.574557e-01
      vertex -2.439946e-01 -7.461256e-01 8.002176e-01
      vertex -2.439946e-01 -7.720326e-01 8.183579e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -6.315200e-01 7.753596e-01
    outer loop
      vertex -2.401139e-01 -6.977683e-01 8.396040e-01
      vertex -3.354321e-01 -6.977683e-01 8.396040e-01
      vertex -3.408533e-01 -7.461256e-01 8.002176e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -6.315200e-01 7.753596e-01
    outer loop
      vertex -2.401139e-01 -6.977683e-01 8.396040e-01
      vertex -3.408533e-01 -7.461256e-01 8.002176e-01
      vertex -2.439946e-01 -7.461256e-01 8.002176e-01
    endloop
  endfacet
  facet normal -3.662423e-01 4.746326e-01 8.003689e-01
    outer loop
      vertex -3.855420e-01 -9.968513e-01 5.242578e-01
      vertex -3.740405e-01 -1.045951e+00 5.586376e-01
      vertex -3.219147e-01 -1.002723e+00 5.568552e-01
    endloop
  endfacet
  facet normal -0.000000e+00 4.119702e-02 9.991510e-01
    outer loop
      vertex -3.740405e-01 -1.045951e+00 5.586376e-01
      vertex -2.676855e-01 -1.045951e+00 5.586376e-01
      vertex -3.219147e-01 -1.002723e+00 5.568552e-01
    endloop
  endfacet
  facet normal 3.952527e-01 5.268715e-01 7.524505e-01
    outer loop
      vertex -2.676855e-01 -1.045951e+00 5.586376e-01
      vertex -2.676855e-01 -9.968513e-01 5.242578e-01
      vertex -3.219147e-01 -1.002723e+00 5.568552e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.841605e-01 1.772800e-01
    outer loop
      vertex -2.676855e-01 -9.968513e-01 5.242578e-01
      vertex -3.855420e-01 -9.968513e-01 5.242578e-01
      vertex -3.219147e-01 -1.002723e+00 5.568552e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -3.911264e-01 -1.044522e+00 4.843910e-01
      vertex -2.715628e-01 -1.094333e+00 5.192688e-01
      vertex -3.794583e-01 -1.094333e+00 5.192688e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -3.911264e-01 -1.044522e+00 4.843910e-01
      vertex -2.715628e-01 -1.044522e+00 4.843910e-01
      vertex -2.715628e-01 -1.094333e+00 5.192688e-01
    endloop
  endfacet
  facet normal 9.722974e-01 7.205932e-02 -2.223627e-01
    outer loop
      vertex -3.855420e-01 -9.968513e-01 5.242578e-01
      vertex -3.740405e-01 -1.045951e+00 5.586376e-01
      vertex -3.794583e-01 -1.094333e+00 5.192688e-01
    endloop
  endfacet
  facet normal 9.722974e-01 7.205932e-02 -2.223627e-01
    outer loop
      vertex -3.855420e-01 -9.968513e-01 5.242578e-01
      vertex -3.794583e-01 -1.094333e+00 5.192688e-01
      vertex -3.911264e-01 -1.044522e+00 4.843910e-01
    endloop
  endfacet
  facet normal 0.000000e+00 6.311537e-01 -7.756578e-01
    outer loop
      vertex -3.740405e-01 -1.045951e+00 5.586376e-01
      vertex -2.676855e-01 -1.045951e+00 5.586376e-01
      vertex -2.715628e-01 -1.094333e+00 5.192688e-01
    endloop
  endfacet
  facet normal 0.000000e+00 6.311537e-01 -7.756578e-01
    outer loop
      vertex -3.740405e-01 -1.045951e+00 5.586376e-01
      vertex -2.715628e-01 -1.094333e+00 5.192688e-01
      vertex -3.794583e-01 -1.094333e+00 5.192688e-01
    endloop
  endfacet
  facet normal -9.979185e-01 3.698854e-02 5.282511e-02
    outer loop
      vertex -2.676855e-01 -1.045951e+00 5.586376e-01
      vertex -2.676855e-01 -9.968513e-01 5.242578e-01
      vertex -2.715628e-01 -1.044522e+00 4.843910e-01
    endloop
  endfacet
  facet normal -9.979185e-01 3.698854e-02 5.282511e-02
    outer loop
      vertex -2.676855e-01 -1.045951e+00 5.586376e-01
      vertex -2.715628e-01 -1.044522e+00 4.843910e-01
      vertex -2.715628e-01 -1.094333e+00 5.192688e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -6.415204e-01 7.671060e-01
    outer loop
      vertex -2.676855e-01 -9.968513e-01 5.242578e-01
      vertex -3.855420e-01 -9.968513e-01 5.242578e-01
      vertex -3.911264e-01 -1.044522e+00 4.843910e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -6.415204e-01 7.671060e-01
    outer loop
      vertex -2.676855e-01 -9.968513e-01 5.242578e-01
      vertex -3.911264e-01 -1.044522e+00 4.843910e-01
      vertex -2.715628e-01 -1.044522e+00 4.843910e-01
    endloop
  endfacet
  facet normal 3.792135e-01 3.718491e-01 8.473047e-01
    outer loop
      vertex -1.774824e-01 -9.806695e-01 6.117571e-01
      vertex -1.493714e-01 -9.325296e-01 5.780492e-01
      vertex -2.138089e-01 -9.387572e-01 6.096214e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.810960e-01 1.935215e-01
    outer loop
      vertex -1.493714e-01 -9.325296e-01 5.780492e-01
      vertex -2.665508e-01 -9.325296e-01 5.780492e-01
      vertex -2.138089e-01 -9.387572e-01 6.096214e-01
    endloop
  endfacet
  facet normal -3.892930e-01 5.283293e-01 7.545324e-01
    outer loop
      vertex -2.665508e-01 -9.325296e-01 5.780492e-01
      vertex -2.665508e-01 -9.806695e-01 6.117571e-01
      vertex -2.138089e-01 -9.387572e-01 6.096214e-01
    endloop
  endfacet
  facet normal -0.000000e+00 5.088939e-02 9.987043e-01
    outer loop
      vertex -2.665508e-01 -9.806695e-01 6.117571e-01
      vertex -1.774824e-01 -9.806695e-01 6.117571e-01
      vertex -2.138089e-01 -9.387572e-01 6.096214e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -1.801045e-01 -1.029052e+00 5.723883e-01
      vertex -2.704886e-01 -9.802008e-01 5.381824e-01
      vertex -1.515781e-01 -9.802008e-01 5.381824e-01
    endloop
  endfacet
  facet normal -0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -1.801045e-01 -1.029052e+00 5.723883e-01
      vertex -2.704886e-01 -1.029052e+00 5.723883e-01
      vertex -2.704886e-01 -9.802008e-01 5.381824e-01
    endloop
  endfacet
  facet normal -8.989994e-01 3.046948e-01 -3.145809e-01
    outer loop
      vertex -1.774824e-01 -9.806695e-01 6.117571e-01
      vertex -1.493714e-01 -9.325296e-01 5.780492e-01
      vertex -1.515781e-01 -9.802008e-01 5.381824e-01
    endloop
  endfacet
  facet normal -8.989994e-01 3.046948e-01 -3.145809e-01
    outer loop
      vertex -1.774824e-01 -9.806695e-01 6.117571e-01
      vertex -1.515781e-01 -9.802008e-01 5.381824e-01
      vertex -1.801045e-01 -1.029052e+00 5.723883e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -6.415204e-01 7.671060e-01
    outer loop
      vertex -1.493714e-01 -9.325296e-01 5.780492e-01
      vertex -2.665508e-01 -9.325296e-01 5.780492e-01
      vertex -2.704886e-01 -9.802008e-01 5.381824e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -6.415204e-01 7.671060e-01
    outer loop
      vertex -1.493714e-01 -9.325296e-01 5.780492e-01
      vertex -2.704886e-01 -9.802008e-01 5.381824e-01
      vertex -1.515781e-01 -9.802008e-01 5.381824e-01
    endloop
  endfacet
  facet normal 9.978532e-01 -3.756347e-02 -5.364619e-02
    outer loop
      vertex -2.665508e-01 -9.325296e-01 5.780492e-01
      vertex -2.665508e-01 -9.806695e-01 6.117571e-01
      vertex -2.704886e-01 -1.029052e+00 5.723883e-01
    endloop
  endfacet
  facet normal 9.978532e-01 -3.756347e-02 -5.364619e-02
    outer loop
      vertex -2.665508e-01 -9.325296e-01 5.780492e-01
      vertex -2.704886e-01 -1.029052e+00 5.723883e-01
      vertex -2.704886e-01 -9.802008e-01 5.381824e-01
    endloop
  endfacet
  facet normal 0.000000e+00 6.311537e-01 -7.756578e-01
    outer loop
      vertex -2.665508e-01 -9.806695e-01 6.117571e-01
      vertex -1.774824e-01 -9.806695e-01 6.117571e-01
      vertex -1.801045e-01 -1.029052e+00 5.723883e-01
    endloop
  endfacet
  facet normal 0.000000e+00 6.311537e-01 -7.756578e-01
    outer loop
      vertex -2.665508e-01 -9.806695e-01 6.117571e-01
      vertex -1.801045e-01 -1.029052e+00 5.723883e-01
      vertex -2.704886e-01 -1.029052e+00 5.723883e-01
    endloop
  endfacet
  facet normal -5.011128e-01 2.044397e-01 8.408867e-01
    outer loop
      vertex -3.356375e-01 -8.436947e-01 7.920942e-01
      vertex -2.715727e-01 -9.272208e-01 8.505798e-01
      vertex -2.743335e-01 -8.548253e-01 8.313334e-01
    endloop
  endfacet
  facet normal 2.462728e-01 2.577739e-01 9.342924e-01
    outer loop
      vertex -2.715727e-01 -9.272208e-01 8.505798e-01
      vertex -2.487721e-01 -9.130563e-01 8.406617e-01
      vertex -2.743335e-01 -8.548253e-01 8.313334e-01
    endloop
  endfacet
  facet normal 7.098187e-01 4.040183e-01 5.769979e-01
    outer loop
      vertex -2.487721e-01 -9.130563e-01 8.406617e-01
      vertex -2.487721e-01 -8.205071e-01 7.758580e-01
      vertex -2.743335e-01 -8.548253e-01 8.313334e-01
    endloop
  endfacet
  facet normal -1.440262e-01 8.698824e-01 4.717638e-01
    outer loop
      vertex -2.487721e-01 -8.205071e-01 7.758580e-01
      vertex -3.356375e-01 -8.436947e-01 7.920942e-01
      vertex -2.743335e-01 -8.548253e-01 8.313334e-01
    endloop
  endfacet
  facet normal -1.469719e-15 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -3.408885e-01 -8.927889e-01 7.532239e-01
      vertex -2.526642e-01 -9.632356e-01 8.025512e-01
      vertex -2.758214e-01 -9.776217e-01 8.126244e-01
    endloop
  endfacet
  facet normal 1.477920e-15 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -3.408885e-01 -8.927889e-01 7.532239e-01
      vertex -2.526642e-01 -8.692385e-01 7.367337e-01
      vertex -2.526642e-01 -9.632356e-01 8.025512e-01
    endloop
  endfacet
  facet normal 8.246537e-01 2.942650e-01 -4.830677e-01
    outer loop
      vertex -3.356375e-01 -8.436947e-01 7.920942e-01
      vertex -2.715727e-01 -9.272208e-01 8.505798e-01
      vertex -2.758214e-01 -9.776217e-01 8.126244e-01
    endloop
  endfacet
  facet normal 8.246537e-01 2.942650e-01 -4.830677e-01
    outer loop
      vertex -3.356375e-01 -8.436947e-01 7.920942e-01
      vertex -2.758214e-01 -9.776217e-01 8.126244e-01
      vertex -3.408885e-01 -8.927889e-01 7.532239e-01
    endloop
  endfacet
  facet normal -5.906016e-01 5.166230e-01 -6.199117e-01
    outer loop
      vertex -2.715727e-01 -9.272208e-01 8.505798e-01
      vertex -2.487721e-01 -9.130563e-01 8.406617e-01
      vertex -2.526642e-01 -9.632356e-01 8.025512e-01
    endloop
  endfacet
  facet normal -5.906016e-01 5.166230e-01 -6.199117e-01
    outer loop
      vertex -2.715727e-01 -9.272208e-01 8.505798e-01
      vertex -2.526642e-01 -9.632356e-01 8.025512e-01
      vertex -2.758214e-01 -9.776217e-01 8.126244e-01
    endloop
  endfacet
  facet normal -9.979027e-01 3.712847e-02 5.302495e-02
    outer loop
      vertex -2.487721e-01 -9.130563e-01 8.406617e-01
      vertex -2.487721e-01 -8.205071e-01 7.758580e-01
      vertex -2.526642e-01 -8.692385e-01 7.367337e-01
    endloop
  endfacet
  facet normal -9.979027e-01 3.712847e-02 5.302495e-02
    outer loop
      vertex -2.487721e-01 -9.130563e-01 8.406617e-01
      vertex -2.526642e-01 -8.692385e-01 7.367337e-01
      vertex -2.526642e-01 -9.632356e-01 8.025512e-01
    endloop
  endfacet
  facet normal 3.000933e-01 -6.116569e-01 7.319971e-01
    outer loop
      vertex -2.487721e-01 -8.205071e-01 7.758580e-01
      vertex -3.356375e-01 -8.436947e-01 7.920942e-01
      vertex -3.408885e-01 -8.927889e-01 7.532239e-01
    endloop
  endfacet
  facet normal 3.000933e-01 -6.116569e-01 7.319971e-01
    outer loop
      vertex -2.487721e-01 -8.205071e-01 7.758580e-01
      vertex -3.408885e-01 -8.927889e-01 7.532239e-01
      vertex -2.526642e-01 -8.692385e-01 7.367337e-01
    endloop
  endfacet
  facet normal 3.211337e-01 1.390097e-01 9.367761e-01
    outer loop
      vertex -2.859734e-01 -1.346959e+00 5.134997e-01
      vertex -1.208076e-01 -1.244352e+00 4.416537e-01
      vertex -2.200023e-01 -1.237234e+00 4.746021e-01
    endloop
  endfacet
  facet normal 2.093956e-01 8.722454e-01 4.419745e-01
    outer loop
      vertex -1.208076e-01 -1.244352e+00 4.416537e-01
      vertex -1.935830e-01 -1.217274e+00 4.226933e-01
      vertex -2.200023e-01 -1.237234e+00 4.746021e-01
    endloop
  endfacet
  facet normal -2.035162e-01 9.440721e-01 2.594398e-01
    outer loop
      vertex -1.935830e-01 -1.217274e+00 4.226933e-01
      vertex -2.859734e-01 -1.241937e+00 4.399622e-01
      vertex -2.200023e-01 -1.237234e+00 4.746021e-01
    endloop
  endfacet
  facet normal -4.261022e-01 5.189003e-01 7.410664e-01
    outer loop
      vertex -2.859734e-01 -1.241937e+00 4.399622e-01
      vertex -2.859734e-01 -1.346959e+00 5.134997e-01
      vertex -2.200023e-01 -1.237234e+00 4.746021e-01
    endloop
  endfacet
  facet normal 1.042204e-15 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -2.899161e-01 -1.397161e+00 4.754050e-01
      vertex -1.962519e-01 -1.265688e+00 3.833466e-01
      vertex -1.224732e-01 -1.293140e+00 4.025684e-01
    endloop
  endfacet
  facet normal -1.424926e-16 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -2.899161e-01 -1.397161e+00 4.754050e-01
      vertex -2.899161e-01 -1.290691e+00 4.008536e-01
      vertex -1.962519e-01 -1.265688e+00 3.833466e-01
    endloop
  endfacet
  facet normal -5.906193e-01 5.167200e-01 -6.198139e-01
    outer loop
      vertex -2.859734e-01 -1.346959e+00 5.134997e-01
      vertex -1.208076e-01 -1.244352e+00 4.416537e-01
      vertex -1.224732e-01 -1.293140e+00 4.025684e-01
    endloop
  endfacet
  facet normal -5.906193e-01 5.167200e-01 -6.198139e-01
    outer loop
      vertex -2.859734e-01 -1.346959e+00 5.134997e-01
      vertex -1.224732e-01 -1.293140e+00 4.025684e-01
      vertex -2.899161e-01 -1.397161e+00 4.754050e-01
    endloop
  endfacet
  facet normal -3.984784e-01 -5.651288e-01 7.223880e-01
    outer loop
      vertex -1.208076e-01 -1.244352e+00 4.416537e-01
      vertex -1.935830e-01 -1.217274e+00 4.226933e-01
      vertex -1.962519e-01 -1.265688e+00 3.833466e-01
    endloop
  endfacet
  facet normal -3.984784e-01 -5.651288e-01 7.223880e-01
    outer loop
      vertex -1.208076e-01 -1.244352e+00 4.416537e-01
      vertex -1.962519e-01 -1.265688e+00 3.833466e-01
      vertex -1.224732e-01 -1.293140e+00 4.025684e-01
    endloop
  endfacet
  facet normal 3.000808e-01 -6.115349e-01 7.321042e-01
    outer loop
      vertex -1.935830e-01 -1.217274e+00 4.226933e-01
      vertex -2.859734e-01 -1.241937e+00 4.399622e-01
      vertex -2.899161e-01 -1.290691e+00 4.008536e-01
    endloop
  endfacet
  facet normal 3.000808e-01 -6.115349e-01 7.321042e-01
    outer loop
      vertex -1.935830e-01 -1.217274e+00 4.226933e-01
      vertex -2.899161e-01 -1.290691e+00 4.008536e-01
      vertex -1.962519e-01 -1.265688e+00 3.833466e-01
    endloop
  endfacet
  facet normal 9.978480e-01 -3.760949e-02 -5.371192e-02
    outer loop
      vertex -2.859734e-01 -1.241937e+00 4.399622e-01
      vertex -2.859734e-01 -1.346959e+00 5.134997e-01
      vertex -2.899161e-01 -1.397161e+00 4.754050e-01
    endloop
  endfacet
  facet normal 9.978480e-01 -3.760949e-02 -5.371192e-02
    outer loop
      vertex -2.859734e-01 -1.241937e+00 4.399622e-01
      vertex -2.899161e-01 -1.397161e+00 4.754050e-01
      vertex -2.899161e-01 -1.290691e+00 4.008536e-01
    endloop
  endfacet
  facet normal -2.322638e-01 2.837138e-01 9.303548e-01
    outer loop
      vertex -2.637077e-01 -1.080027e+00 7.554569e-01
      vertex -1.851023e-01 -1.129675e+00 7.902213e-01
      vertex -1.814577e-01 -1.013292e+00 7.556399e-01
    endloop
  endfacet
  facet normal 4.567438e-01 2.402086e-01 8.565541e-01
    outer loop
      vertex -1.851023e-01 -1.129675e+00 7.902213e-01
      vertex -9.169523e-02 -1.011021e+00 7.071385e-01
      vertex -1.814577e-01 -1.013292e+00 7.556399e-01
    endloop
  endfacet
  facet normal 3.607899e-01 6.199674e-01 6.967575e-01
    outer loop
      vertex -9.169523e-02 -1.011021e+00 7.071385e-01
      vertex -1.118747e-01 -9.559037e-01 6.685451e-01
      vertex -1.814577e-01 -1.013292e+00 7.556399e-01
    endloop
  endfacet
  facet normal -4.455040e-01 8.687117e-01 2.164861e-01
    outer loop
      vertex -1.118747e-01 -9.559037e-01 6.685451e-01
      vertex -2.637077e-01 -1.050228e+00 7.345914e-01
      vertex -1.814577e-01 -1.013292e+00 7.556399e-01
    endloop
  endfacet
  facet normal -4.232810e-01 5.196594e-01 7.421505e-01
    outer loop
      vertex -2.637077e-01 -1.050228e+00 7.345914e-01
      vertex -2.637077e-01 -1.080027e+00 7.554569e-01
      vertex -1.814577e-01 -1.013292e+00 7.556399e-01
    endloop
  endfacet
  facet normal 7.901895e-16 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -2.676627e-01 -1.130633e+00 7.176457e-01
      vertex -9.307044e-02 -1.060593e+00 6.686026e-01
      vertex -1.878784e-01 -1.181027e+00 7.529315e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -2.676627e-01 -1.130633e+00 7.176457e-01
      vertex -1.135526e-01 -1.004649e+00 6.294304e-01
      vertex -9.307044e-02 -1.060593e+00 6.686026e-01
    endloop
  endfacet
  facet normal -1.981574e-15 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -2.676627e-01 -1.130633e+00 7.176457e-01
      vertex -2.676627e-01 -1.100388e+00 6.964673e-01
      vertex -1.135526e-01 -1.004649e+00 6.294304e-01
    endloop
  endfacet
  facet normal 5.846851e-01 4.557538e-01 -6.711421e-01
    outer loop
      vertex -2.637077e-01 -1.080027e+00 7.554569e-01
      vertex -1.851023e-01 -1.129675e+00 7.902213e-01
      vertex -1.878784e-01 -1.181027e+00 7.529315e-01
    endloop
  endfacet
  facet normal 5.846851e-01 4.557538e-01 -6.711421e-01
    outer loop
      vertex -2.637077e-01 -1.080027e+00 7.554569e-01
      vertex -1.878784e-01 -1.181027e+00 7.529315e-01
      vertex -2.676627e-01 -1.130633e+00 7.176457e-01
    endloop
  endfacet
  facet normal -8.313752e-01 3.552560e-01 -4.273271e-01
    outer loop
      vertex -1.851023e-01 -1.129675e+00 7.902213e-01
      vertex -9.169523e-02 -1.011021e+00 7.071385e-01
      vertex -9.307044e-02 -1.060593e+00 6.686026e-01
    endloop
  endfacet
  facet normal -8.313752e-01 3.552560e-01 -4.273271e-01
    outer loop
      vertex -1.851023e-01 -1.129675e+00 7.902213e-01
      vertex -9.307044e-02 -1.060593e+00 6.686026e-01
      vertex -1.878784e-01 -1.181027e+00 7.529315e-01
    endloop
  endfacet
  facet normal -9.520509e-01 -1.708683e-01 2.537777e-01
    outer loop
      vertex -9.169523e-02 -1.011021e+00 7.071385e-01
      vertex -1.118747e-01 -9.559037e-01 6.685451e-01
      vertex -1.135526e-01 -1.004649e+00 6.294304e-01
    endloop
  endfacet
  facet normal -9.520509e-01 -1.708683e-01 2.537777e-01
    outer loop
      vertex -9.169523e-02 -1.011021e+00 7.071385e-01
      vertex -1.135526e-01 -1.004649e+00 6.294304e-01
      vertex -9.307044e-02 -1.060593e+00 6.686026e-01
    endloop
  endfacet
  facet normal 5.907172e-01 -5.172560e-01 6.192733e-01
    outer loop
      vertex -1.118747e-01 -9.559037e-01 6.685451e-01
      vertex -2.637077e-01 -1.050228e+00 7.345914e-01
      vertex -2.676627e-01 -1.100388e+00 6.964673e-01
    endloop
  endfacet
  facet normal 5.907172e-01 -5.172560e-01 6.192733e-01
    outer loop
      vertex -1.118747e-01 -9.559037e-01 6.685451e-01
      vertex -2.676627e-01 -1.100388e+00 6.964673e-01
      vertex -1.135526e-01 -1.004649e+00 6.294304e-01
    endloop
  endfacet
  facet normal 9.978346e-01 -3.772618e-02 -5.387857e-02
    outer loop
      vertex -2.637077e-01 -1.050228e+00 7.345914e-01
      vertex -2.637077e-01 -1.080027e+00 7.554569e-01
      vertex -2.676627e-01 -1.130633e+00 7.176457e-01
    endloop
  endfacet
  facet normal 9.978346e-01 -3.772618e-02 -5.387857e-02
    outer loop
      vertex -2.637077e-01 -1.050228e+00 7.345914e-01
      vertex -2.676627e-01 -1.130633e+00 7.176457e-01
      vertex -2.676627e-01 -1.100388e+00 6.964673e-01
    endloop
  endfacet
  facet normal -1.080522e-01 2.746300e-01 9.554596e-01
    outer loop
      vertex -1.998081e-01 -1.329507e+00 6.433638e-01
      vertex -6.683244e-02 -1.365939e+00 6.688735e-01
      vertex -9.712414e-02 -1.238020e+00 6.286797e-01
    endloop
  endfacet
  facet normal 5.869357e-01 3.659202e-01 7.222249e-01
    outer loop
      vertex -6.683244e-02 -1.365939e+00 6.688735e-01
      vertex -2.468549e-02 -1.188973e+00 5.449607e-01
      vertex -9.712414e-02 -1.238020e+00 6.286797e-01
    endloop
  endfacet
  facet normal -1.175165e-01 8.978529e-01 4.243231e-01
    outer loop
      vertex -2.468549e-02 -1.188973e+00 5.449607e-01
      vertex -1.009162e-01 -1.203885e+00 5.554023e-01
      vertex -9.712414e-02 -1.238020e+00 6.286797e-01
    endloop
  endfacet
  facet normal -5.893500e-01 7.202187e-01 3.659939e-01
    outer loop
      vertex -1.009162e-01 -1.203885e+00 5.554023e-01
      vertex -1.998081e-01 -1.329507e+00 6.433638e-01
      vertex -9.712414e-02 -1.238020e+00 6.286797e-01
    endloop
  endfacet
  facet normal 4.271349e-16 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -2.026385e-01 -1.380841e+00 6.060618e-01
      vertex -2.503518e-02 -1.238316e+00 5.062648e-01
      vertex -6.777917e-02 -1.417789e+00 6.319330e-01
    endloop
  endfacet
  facet normal 1.534798e-15 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -2.026385e-01 -1.380841e+00 6.060618e-01
      vertex -1.023457e-01 -1.253440e+00 5.168544e-01
      vertex -2.503518e-02 -1.238316e+00 5.062648e-01
    endloop
  endfacet
  facet normal 3.001738e-01 5.498468e-01 -7.794640e-01
    outer loop
      vertex -1.998081e-01 -1.329507e+00 6.433638e-01
      vertex -6.683244e-02 -1.365939e+00 6.688735e-01
      vertex -6.777917e-02 -1.417789e+00 6.319330e-01
    endloop
  endfacet
  facet normal 3.001738e-01 5.498468e-01 -7.794640e-01
    outer loop
      vertex -1.998081e-01 -1.329507e+00 6.433638e-01
      vertex -6.777917e-02 -1.417789e+00 6.319330e-01
      vertex -2.026385e-01 -1.380841e+00 6.060618e-01
    endloop
  endfacet
  facet normal -9.801492e-01 1.266003e-01 -1.525778e-01
    outer loop
      vertex -6.683244e-02 -1.365939e+00 6.688735e-01
      vertex -2.468549e-02 -1.188973e+00 5.449607e-01
      vertex -2.503518e-02 -1.238316e+00 5.062648e-01
    endloop
  endfacet
  facet normal -9.801492e-01 1.266003e-01 -1.525778e-01
    outer loop
      vertex -6.683244e-02 -1.365939e+00 6.688735e-01
      vertex -2.503518e-02 -1.238316e+00 5.062648e-01
      vertex -6.777917e-02 -1.417789e+00 6.319330e-01
    endloop
  endfacet
  facet normal 2.228402e-01 -6.025535e-01 7.663364e-01
    outer loop
      vertex -2.468549e-02 -1.188973e+00 5.449607e-01
      vertex -1.009162e-01 -1.203885e+00 5.554023e-01
      vertex -1.023457e-01 -1.253440e+00 5.168544e-01
    endloop
  endfacet
  facet normal 2.228402e-01 -6.025535e-01 7.663364e-01
    outer loop
      vertex -2.468549e-02 -1.188973e+00 5.449607e-01
      vertex -1.023457e-01 -1.253440e+00 5.168544e-01
      vertex -2.503518e-02 -1.238316e+00 5.062648e-01
    endloop
  endfacet
  facet normal 8.314894e-01 -3.558453e-01 4.266139e-01
    outer loop
      vertex -1.009162e-01 -1.203885e+00 5.554023e-01
      vertex -1.998081e-01 -1.329507e+00 6.433638e-01
      vertex -2.026385e-01 -1.380841e+00 6.060618e-01
    endloop
  endfacet
  facet normal 8.314894e-01 -3.558453e-01 4.266139e-01
    outer loop
      vertex -1.009162e-01 -1.203885e+00 5.554023e-01
      vertex -2.026385e-01 -1.380841e+00 6.060618e-01
      vertex -1.023457e-01 -1.253440e+00 5.168544e-01
    endloop
  endfacet
  facet normal -0.000000e+00 2.751293e-01 9.614072e-01
    outer loop
      vertex -7.109234e-02 -1.400647e+00 6.434149e-01
      vertex 3.264358e-02 -1.400647e+00 6.434149e-01
      vertex -8.508627e-03 -1.286673e+00 6.107986e-01
    endloop
  endfacet
  facet normal 6.846460e-01 4.180659e-01 5.970600e-01
    outer loop
      vertex 3.264358e-02 -1.400647e+00 6.434149e-01
      vertex 3.264358e-02 -1.254080e+00 5.407875e-01
      vertex -8.508627e-03 -1.286673e+00 6.107986e-01
    endloop
  endfacet
  facet normal 2.382895e-01 8.193087e-01 5.214896e-01
    outer loop
      vertex 3.264358e-02 -1.254080e+00 5.407875e-01
      vertex -2.853978e-02 -1.221978e+00 5.183095e-01
      vertex -8.508627e-03 -1.286673e+00 6.107986e-01
    endloop
  endfacet
  facet normal -6.823529e-01 5.213338e-01 5.124506e-01
    outer loop
      vertex -2.853978e-02 -1.221978e+00 5.183095e-01
      vertex -7.109234e-02 -1.400647e+00 6.434149e-01
      vertex -8.508627e-03 -1.286673e+00 6.107986e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -7.208982e-02 -1.452490e+00 6.064692e-01
      vertex 3.310159e-02 -1.303866e+00 5.024019e-01
      vertex 3.310159e-02 -1.452490e+00 6.064692e-01
    endloop
  endfacet
  facet normal -8.990059e-16 -5.735764e-01 -8.191520e-01
    outer loop
      vertex -7.208982e-02 -1.452490e+00 6.064692e-01
      vertex -2.894021e-02 -1.271314e+00 4.796085e-01
      vertex 3.310159e-02 -1.303866e+00 5.024019e-01
    endloop
  endfacet
  facet normal 0.000000e+00 5.803537e-01 -8.143645e-01
    outer loop
      vertex -7.109234e-02 -1.400647e+00 6.434149e-01
      vertex 3.264358e-02 -1.400647e+00 6.434149e-01
      vertex 3.310159e-02 -1.452490e+00 6.064692e-01
    endloop
  endfacet
  facet normal 0.000000e+00 5.803537e-01 -8.143645e-01
    outer loop
      vertex -7.109234e-02 -1.400647e+00 6.434149e-01
      vertex 3.310159e-02 -1.452490e+00 6.064692e-01
      vertex -7.208982e-02 -1.452490e+00 6.064692e-01
    endloop
  endfacet
  facet normal -9.999709e-01 -4.378303e-03 -6.252865e-03
    outer loop
      vertex 3.264358e-02 -1.400647e+00 6.434149e-01
      vertex 3.264358e-02 -1.254080e+00 5.407875e-01
      vertex 3.310159e-02 -1.303866e+00 5.024019e-01
    endloop
  endfacet
  facet normal -9.999709e-01 -4.378303e-03 -6.252865e-03
    outer loop
      vertex 3.264358e-02 -1.400647e+00 6.434149e-01
      vertex 3.310159e-02 -1.303866e+00 5.024019e-01
      vertex 3.310159e-02 -1.452490e+00 6.064692e-01
    endloop
  endfacet
  facet normal -5.221049e-01 -5.237704e-01 6.731055e-01
    outer loop
      vertex 3.264358e-02 -1.254080e+00 5.407875e-01
      vertex -2.853978e-02 -1.221978e+00 5.183095e-01
      vertex -2.894021e-02 -1.271314e+00 4.796085e-01
    endloop
  endfacet
  facet normal -5.221049e-01 -5.237704e-01 6.731055e-01
    outer loop
      vertex 3.264358e-02 -1.254080e+00 5.407875e-01
      vertex -2.894021e-02 -1.271314e+00 4.796085e-01
      vertex 3.310159e-02 -1.303866e+00 5.024019e-01
    endloop
  endfacet
  facet normal 9.801928e-01 -1.270977e-01 1.518824e-01
    outer loop
      vertex -2.853978e-02 -1.221978e+00 5.183095e-01
      vertex -7.109234e-02 -1.400647e+00 6.434149e-01
      vertex -7.208982e-02 -1.452490e+00 6.064692e-01
    endloop
  endfacet
  facet normal 9.801928e-01 -1.270977e-01 1.518824e-01
    outer loop
      vertex -2.853978e-02 -1.221978e+00 5.183095e-01
      vertex -7.208982e-02 -1.452490e+00 6.064692e-01
      vertex -2.894021e-02 -1.271314e+00 4.796085e-01
    endloop
  endfacet
  facet normal 1.065157e-01 2.793917e-01 9.542508e-01
    outer loop
      vertex 6.835344e-02 -1.441319e+00 6.151120e-01
      vertex 2.040691e-01 -1.404137e+00 5.890766e-01
      vertex 9.557924e-02 -1.312443e+00 5.743398e-01
    endloop
  endfacet
  facet normal 5.540466e-01 7.221095e-01 4.142345e-01
    outer loop
      vertex 2.040691e-01 -1.404137e+00 5.890766e-01
      vertex 8.021118e-02 -1.245309e+00 4.778642e-01
      vertex 9.557924e-02 -1.312443e+00 5.743398e-01
    endloop
  endfacet
  facet normal -3.615270e-01 7.373195e-01 5.706647e-01
    outer loop
      vertex 8.021118e-02 -1.245309e+00 4.778642e-01
      vertex 3.330096e-02 -1.295524e+00 5.130249e-01
      vertex 9.557924e-02 -1.312443e+00 5.743398e-01
    endloop
  endfacet
  facet normal -6.057585e-01 3.534817e-01 7.128165e-01
    outer loop
      vertex 3.330096e-02 -1.295524e+00 5.130249e-01
      vertex 6.835344e-02 -1.441319e+00 6.151120e-01
      vertex 9.557924e-02 -1.312443e+00 5.743398e-01
    endloop
  endfacet
  facet normal 3.963079e-16 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 6.930217e-02 -1.493169e+00 5.781711e-01
      vertex 8.132449e-02 -1.294438e+00 4.390182e-01
      vertex 2.069015e-01 -1.455470e+00 5.517743e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 6.930217e-02 -1.493169e+00 5.781711e-01
      vertex 3.376317e-02 -1.345350e+00 4.746670e-01
      vertex 8.132449e-02 -1.294438e+00 4.390182e-01
    endloop
  endfacet
  facet normal -3.001739e-01 5.498470e-01 -7.794639e-01
    outer loop
      vertex 6.835344e-02 -1.441319e+00 6.151120e-01
      vertex 2.040691e-01 -1.404137e+00 5.890766e-01
      vertex 2.069015e-01 -1.455470e+00 5.517743e-01
    endloop
  endfacet
  facet normal -3.001739e-01 5.498470e-01 -7.794639e-01
    outer loop
      vertex 6.835344e-02 -1.441319e+00 6.151120e-01
      vertex 2.069015e-01 -1.455470e+00 5.517743e-01
      vertex 6.930217e-02 -1.493169e+00 5.781711e-01
    endloop
  endfacet
  facet normal -8.339471e-01 -3.537766e-01 4.235261e-01
    outer loop
      vertex 2.040691e-01 -1.404137e+00 5.890766e-01
      vertex 8.021118e-02 -1.245309e+00 4.778642e-01
      vertex 8.132449e-02 -1.294438e+00 4.390182e-01
    endloop
  endfacet
  facet normal -8.339471e-01 -3.537766e-01 4.235261e-01
    outer loop
      vertex 2.040691e-01 -1.404137e+00 5.890766e-01
      vertex 8.132449e-02 -1.294438e+00 4.390182e-01
      vertex 2.069015e-01 -1.455470e+00 5.517743e-01
    endloop
  endfacet
  facet normal 7.792230e-01 -3.777687e-01 5.001023e-01
    outer loop
      vertex 8.021118e-02 -1.245309e+00 4.778642e-01
      vertex 3.330096e-02 -1.295524e+00 5.130249e-01
      vertex 3.376317e-02 -1.345350e+00 4.746670e-01
    endloop
  endfacet
  facet normal 7.792230e-01 -3.777687e-01 5.001023e-01
    outer loop
      vertex 8.021118e-02 -1.245309e+00 4.778642e-01
      vertex 3.376317e-02 -1.345350e+00 4.746670e-01
      vertex 8.132449e-02 -1.294438e+00 4.390182e-01
    endloop
  endfacet
  facet normal 9.797766e-01 1.276879e-01 -1.540573e-01
    outer loop
      vertex 3.330096e-02 -1.295524e+00 5.130249e-01
      vertex 6.835344e-02 -1.441319e+00 6.151120e-01
      vertex 6.930217e-02 -1.493169e+00 5.781711e-01
    endloop
  endfacet
  facet normal 9.797766e-01 1.276879e-01 -1.540573e-01
    outer loop
      vertex 3.330096e-02 -1.295524e+00 5.130249e-01
      vertex 6.930217e-02 -1.493169e+00 5.781711e-01
      vertex 3.376317e-02 -1.345350e+00 4.746670e-01
    endloop
  endfacet
  facet normal 2.295469e-01 2.876426e-01 9.298225e-01
    outer loop
      vertex 1.741658e-01 -9.200386e-01 9.428028e-01
      vertex 2.702799e-01 -8.593311e-01 9.002950e-01
      vertex 1.599620e-01 -8.001486e-01 9.092211e-01
    endloop
  endfacet
  facet normal 4.768749e-01 8.687028e-01 1.339616e-01
    outer loop
      vertex 2.702799e-01 -8.593311e-01 9.002950e-01
      vertex 1.359442e-01 -7.766609e-01 8.424087e-01
      vertex 1.599620e-01 -8.001486e-01 9.092211e-01
    endloop
  endfacet
  facet normal -5.383341e-02 9.358223e-01 3.483369e-01
    outer loop
      vertex 1.359442e-01 -7.766609e-01 8.424087e-01
      vertex 6.656573e-02 -7.820588e-01 8.461883e-01
      vertex 1.599620e-01 -8.001486e-01 9.092211e-01
    endloop
  endfacet
  facet normal -5.283476e-01 1.703833e-01 8.317562e-01
    outer loop
      vertex 6.656573e-02 -7.820588e-01 8.461883e-01
      vertex 1.741658e-01 -9.200386e-01 9.428028e-01
      vertex 1.599620e-01 -8.001486e-01 9.092211e-01
    endloop
  endfacet
  facet normal 1.026022e-15 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 1.769485e-01 -9.713940e-01 9.055158e-01
      vertex 1.381162e-01 -8.257255e-01 8.035176e-01
      vertex 2.745982e-01 -9.097166e-01 8.623288e-01
    endloop
  endfacet
  facet normal -1.355829e-16 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 1.769485e-01 -9.713940e-01 9.055158e-01
      vertex 6.762924e-02 -8.312097e-01 8.073577e-01
      vertex 1.381162e-01 -8.257255e-01 8.035176e-01
    endloop
  endfacet
  facet normal -5.846642e-01 4.556662e-01 -6.712199e-01
    outer loop
      vertex 1.741658e-01 -9.200386e-01 9.428028e-01
      vertex 2.702799e-01 -8.593311e-01 9.002950e-01
      vertex 2.745982e-01 -9.097166e-01 8.623288e-01
    endloop
  endfacet
  facet normal -5.846642e-01 4.556662e-01 -6.712199e-01
    outer loop
      vertex 1.741658e-01 -9.200386e-01 9.428028e-01
      vertex 2.745982e-01 -9.097166e-01 8.623288e-01
      vertex 1.769485e-01 -9.713940e-01 9.055158e-01
    endloop
  endfacet
  facet normal -5.870380e-01 -5.186794e-01 6.215771e-01
    outer loop
      vertex 2.702799e-01 -8.593311e-01 9.002950e-01
      vertex 1.359442e-01 -7.766609e-01 8.424087e-01
      vertex 1.381162e-01 -8.257255e-01 8.035176e-01
    endloop
  endfacet
  facet normal -5.870380e-01 -5.186794e-01 6.215771e-01
    outer loop
      vertex 2.702799e-01 -8.593311e-01 9.002950e-01
      vertex 1.381162e-01 -8.257255e-01 8.035176e-01
      vertex 2.745982e-01 -9.097166e-01 8.623288e-01
    endloop
  endfacet
  facet normal 9.056335e-02 -6.161584e-01 7.823983e-01
    outer loop
      vertex 1.359442e-01 -7.766609e-01 8.424087e-01
      vertex 6.656573e-02 -7.820588e-01 8.461883e-01
      vertex 6.762924e-02 -8.312097e-01 8.073577e-01
    endloop
  endfacet
  facet normal 9.056335e-02 -6.161584e-01 7.823983e-01
    outer loop
      vertex 1.359442e-01 -7.766609e-01 8.424087e-01
      vertex 6.762924e-02 -8.312097e-01 8.073577e-01
      vertex 1.381162e-01 -8.257255e-01 8.035176e-01
    endloop
  endfacet
  facet normal 8.338353e-01 3.531966e-01 -4.242298e-01
    outer loop
      vertex 6.656573e-02 -7.820588e-01 8.461883e-01
      vertex 1.741658e-01 -9.200386e-01 9.428028e-01
      vertex 1.769485e-01 -9.713940e-01 9.055158e-01
    endloop
  endfacet
  facet normal 8.338353e-01 3.531966e-01 -4.242298e-01
    outer loop
      vertex 6.656573e-02 -7.820588e-01 8.461883e-01
      vertex 1.769485e-01 -9.713940e-01 9.055158e-01
      vertex 6.762924e-02 -8.312097e-01 8.073577e-01
    endloop
  endfacet
  facet normal 2.394485e-01 4.269281e-01 8.720073e-01
    outer loop
      vertex 3.051866e-01 -1.291174e+00 5.787191e-01
      vertex 3.764588e-01 -1.198251e+00 5.136538e-01
      vertex 2.285819e-01 -1.162329e+00 5.366731e-01
    endloop
  endfacet
  facet normal 2.463330e-01 9.663168e-01 7.451115e-02
    outer loop
      vertex 3.764588e-01 -1.198251e+00 5.136538e-01
      vertex 1.719963e-01 -1.143155e+00 4.750751e-01
      vertex 2.285819e-01 -1.162329e+00 5.366731e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.548099e-01 2.972171e-01
    outer loop
      vertex 1.719963e-01 -1.143155e+00 4.750751e-01
      vertex 1.473689e-01 -1.143155e+00 4.750751e-01
      vertex 2.285819e-01 -1.162329e+00 5.366731e-01
    endloop
  endfacet
  facet normal -4.548631e-01 4.810598e-01 7.494538e-01
    outer loop
      vertex 1.473689e-01 -1.143155e+00 4.750751e-01
      vertex 1.525678e-01 -1.197252e+00 5.129544e-01
      vertex 2.285819e-01 -1.162329e+00 5.366731e-01
    endloop
  endfacet
  facet normal -3.392559e-01 1.034123e-01 9.349927e-01
    outer loop
      vertex 1.525678e-01 -1.197252e+00 5.129544e-01
      vertex 3.051866e-01 -1.291174e+00 5.787191e-01
      vertex 2.285819e-01 -1.162329e+00 5.366731e-01
    endloop
  endfacet
  facet normal 1.205496e-16 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 3.094785e-01 -1.341596e+00 5.407788e-01
      vertex 1.744151e-01 -1.191495e+00 4.356772e-01
      vertex 3.817529e-01 -1.247366e+00 4.747985e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 3.094785e-01 -1.341596e+00 5.407788e-01
      vertex 1.494413e-01 -1.191495e+00 4.356772e-01
      vertex 1.744151e-01 -1.191495e+00 4.356772e-01
    endloop
  endfacet
  facet normal 1.601030e-15 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 3.094785e-01 -1.341596e+00 5.407788e-01
      vertex 1.547133e-01 -1.246353e+00 4.740892e-01
      vertex 1.494413e-01 -1.191495e+00 4.356772e-01
    endloop
  endfacet
  facet normal -8.245003e-01 2.937410e-01 -4.836481e-01
    outer loop
      vertex 3.051866e-01 -1.291174e+00 5.787191e-01
      vertex 3.764588e-01 -1.198251e+00 5.136538e-01
      vertex 3.817529e-01 -1.247366e+00 4.747985e-01
    endloop
  endfacet
  facet normal -8.245003e-01 2.937410e-01 -4.836481e-01
    outer loop
      vertex 3.051866e-01 -1.291174e+00 5.787191e-01
      vertex 3.817529e-01 -1.247366e+00 4.747985e-01
      vertex 3.094785e-01 -1.341596e+00 5.407788e-01
    endloop
  endfacet
  facet normal -3.026837e-01 -6.111791e-01 7.313294e-01
    outer loop
      vertex 3.764588e-01 -1.198251e+00 5.136538e-01
      vertex 1.719963e-01 -1.143155e+00 4.750751e-01
      vertex 1.744151e-01 -1.191495e+00 4.356772e-01
    endloop
  endfacet
  facet normal -3.026837e-01 -6.111791e-01 7.313294e-01
    outer loop
      vertex 3.764588e-01 -1.198251e+00 5.136538e-01
      vertex 1.744151e-01 -1.191495e+00 4.356772e-01
      vertex 3.817529e-01 -1.247366e+00 4.747985e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -6.317596e-01 7.751644e-01
    outer loop
      vertex 1.719963e-01 -1.143155e+00 4.750751e-01
      vertex 1.473689e-01 -1.143155e+00 4.750751e-01
      vertex 1.494413e-01 -1.191495e+00 4.356772e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -6.317596e-01 7.751644e-01
    outer loop
      vertex 1.719963e-01 -1.143155e+00 4.750751e-01
      vertex 1.494413e-01 -1.191495e+00 4.356772e-01
      vertex 1.744151e-01 -1.191495e+00 4.356772e-01
    endloop
  endfacet
  facet normal 9.968416e-01 7.127741e-02 -3.502005e-02
    outer loop
      vertex 1.473689e-01 -1.143155e+00 4.750751e-01
      vertex 1.525678e-01 -1.197252e+00 5.129544e-01
      vertex 1.547133e-01 -1.246353e+00 4.740892e-01
    endloop
  endfacet
  facet normal 9.968416e-01 7.127741e-02 -3.502005e-02
    outer loop
      vertex 1.473689e-01 -1.143155e+00 4.750751e-01
      vertex 1.547133e-01 -1.246353e+00 4.740892e-01
      vertex 1.494413e-01 -1.191495e+00 4.356772e-01
    endloop
  endfacet
  facet normal 5.869326e-01 5.181008e-01 -6.221589e-01
    outer loop
      vertex 1.525678e-01 -1.197252e+00 5.129544e-01
      vertex 3.051866e-01 -1.291174e+00 5.787191e-01
      vertex 3.094785e-01 -1.341596e+00 5.407788e-01
    endloop
  endfacet
  facet normal 5.869326e-01 5.181008e-01 -6.221589e-01
    outer loop
      vertex 1.525678e-01 -1.197252e+00 5.129544e-01
      vertex 3.094785e-01 -1.341596e+00 5.407788e-01
      vertex 1.547133e-01 -1.246353e+00 4.740892e-01
    endloop
  endfacet
  facet normal 4.730448e-01 4.282990e-01 7.699276e-01
    outer loop
      vertex 3.643140e-01 -1.122200e+00 5.759122e-01
      vertex 3.766468e-01 -1.069552e+00 5.390475e-01
      vertex 3.181226e-01 -1.057072e+00 5.680625e-01
    endloop
  endfacet
  facet normal 4.672086e-01 5.071259e-01 7.242509e-01
    outer loop
      vertex 3.766468e-01 -1.069552e+00 5.390475e-01
      vertex 3.766468e-01 -1.068326e+00 5.381890e-01
      vertex 3.181226e-01 -1.057072e+00 5.680625e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.358004e-01 -3.525303e-01
    outer loop
      vertex 3.766468e-01 -1.068326e+00 5.381890e-01
      vertex 1.643860e-01 -1.068326e+00 5.381890e-01
      vertex 3.181226e-01 -1.057072e+00 5.680625e-01
    endloop
  endfacet
  facet normal -1.895852e-01 -1.613617e-02 9.817317e-01
    outer loop
      vertex 1.643860e-01 -1.068326e+00 5.381890e-01
      vertex 3.643140e-01 -1.122200e+00 5.759122e-01
      vertex 3.181226e-01 -1.057072e+00 5.680625e-01
    endloop
  endfacet
  facet normal -6.849660e-14 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 3.695535e-01 -1.171336e+00 5.370710e-01
      vertex 3.820637e-01 -1.116687e+00 4.988053e-01
      vertex 3.820637e-01 -1.117931e+00 4.996761e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 3.695535e-01 -1.171336e+00 5.370710e-01
      vertex 1.667502e-01 -1.116687e+00 4.988053e-01
      vertex 3.820637e-01 -1.116687e+00 4.988053e-01
    endloop
  endfacet
  facet normal -9.723014e-01 7.207629e-02 -2.223398e-01
    outer loop
      vertex 3.643140e-01 -1.122200e+00 5.759122e-01
      vertex 3.766468e-01 -1.069552e+00 5.390475e-01
      vertex 3.820637e-01 -1.117931e+00 4.996761e-01
    endloop
  endfacet
  facet normal -9.723014e-01 7.207629e-02 -2.223398e-01
    outer loop
      vertex 3.643140e-01 -1.122200e+00 5.759122e-01
      vertex 3.820637e-01 -1.117931e+00 4.996761e-01
      vertex 3.695535e-01 -1.171336e+00 5.370710e-01
    endloop
  endfacet
  facet normal -9.959494e-01 -5.157368e-02 -7.365484e-02
    outer loop
      vertex 3.766468e-01 -1.069552e+00 5.390475e-01
      vertex 3.766468e-01 -1.068326e+00 5.381890e-01
      vertex 3.820637e-01 -1.116687e+00 4.988053e-01
    endloop
  endfacet
  facet normal -9.959494e-01 -5.157368e-02 -7.365484e-02
    outer loop
      vertex 3.766468e-01 -1.069552e+00 5.390475e-01
      vertex 3.820637e-01 -1.116687e+00 4.988053e-01
      vertex 3.820637e-01 -1.117931e+00 4.996761e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -6.314646e-01 7.754047e-01
    outer loop
      vertex 3.766468e-01 -1.068326e+00 5.381890e-01
      vertex 1.643860e-01 -1.068326e+00 5.381890e-01
      vertex 1.667502e-01 -1.116687e+00 4.988053e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -6.314646e-01 7.754047e-01
    outer loop
      vertex 3.766468e-01 -1.068326e+00 5.381890e-01
      vertex 1.667502e-01 -1.116687e+00 4.988053e-01
      vertex 3.820637e-01 -1.116687e+00 4.988053e-01
    endloop
  endfacet
  facet normal 3.026345e-01 6.107049e-01 -7.317458e-01
    outer loop
      vertex 1.643860e-01 -1.068326e+00 5.381890e-01
      vertex 3.643140e-01 -1.122200e+00 5.759122e-01
      vertex 3.695535e-01 -1.171336e+00 5.370710e-01
    endloop
  endfacet
  facet normal 3.026345e-01 6.107049e-01 -7.317458e-01
    outer loop
      vertex 1.643860e-01 -1.068326e+00 5.381890e-01
      vertex 3.695535e-01 -1.171336e+00 5.370710e-01
      vertex 1.667502e-01 -1.116687e+00 4.988053e-01
    endloop
  endfacet
  facet normal 2.935099e-01 5.483139e-01 7.830733e-01
    outer loop
      vertex 3.689235e-01 -9.772068e-01 6.143701e-01
      vertex 3.689235e-01 -9.291158e-01 5.806964e-01
      vertex 2.436298e-01 -9.258501e-01 6.253721e-01
    endloop
  endfacet
  facet normal 0.000000e+00 9.973389e-01 -7.290422e-02
    outer loop
      vertex 3.689235e-01 -9.291158e-01 5.806964e-01
      vertex 1.910111e-01 -9.291158e-01 5.806964e-01
      vertex 2.436298e-01 -9.258501e-01 6.253721e-01
    endloop
  endfacet
  facet normal -4.078860e-01 8.100790e-01 4.211900e-01
    outer loop
      vertex 1.910111e-01 -9.291158e-01 5.806964e-01
      vertex 1.384548e-01 -9.707282e-01 6.098338e-01
      vertex 2.436298e-01 -9.258501e-01 6.253721e-01
    endloop
  endfacet
  facet normal -1.700243e-01 5.786060e-02 9.837398e-01
    outer loop
      vertex 1.384548e-01 -9.707282e-01 6.098338e-01
      vertex 1.624968e-01 -9.772068e-01 6.143701e-01
      vertex 2.436298e-01 -9.258501e-01 6.253721e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -2.094734e-01 9.778144e-01
    outer loop
      vertex 1.624968e-01 -9.772068e-01 6.143701e-01
      vertex 3.689235e-01 -9.772068e-01 6.143701e-01
      vertex 2.436298e-01 -9.258501e-01 6.253721e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 3.743793e-01 -1.025587e+00 5.749999e-01
      vertex 1.938359e-01 -9.767850e-01 5.408283e-01
      vertex 3.743793e-01 -9.767850e-01 5.408283e-01
    endloop
  endfacet
  facet normal -1.867136e-16 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 3.743793e-01 -1.025587e+00 5.749999e-01
      vertex 1.405023e-01 -1.019013e+00 5.703965e-01
      vertex 1.938359e-01 -9.767850e-01 5.408283e-01
    endloop
  endfacet
  facet normal -0.000000e+00 -5.735764e-01 -8.191520e-01
    outer loop
      vertex 3.743793e-01 -1.025587e+00 5.749999e-01
      vertex 1.648999e-01 -1.025587e+00 5.749999e-01
      vertex 1.405023e-01 -1.019013e+00 5.703965e-01
    endloop
  endfacet
  facet normal -9.958914e-01 -5.194082e-02 -7.417918e-02
    outer loop
      vertex 3.689235e-01 -9.772068e-01 6.143701e-01
      vertex 3.689235e-01 -9.291158e-01 5.806964e-01
      vertex 3.743793e-01 -9.767850e-01 5.408283e-01
    endloop
  endfacet
  facet normal -9.958914e-01 -5.194082e-02 -7.417918e-02
    outer loop
      vertex 3.689235e-01 -9.772068e-01 6.143701e-01
      vertex 3.743793e-01 -9.767850e-01 5.408283e-01
      vertex 3.743793e-01 -1.025587e+00 5.749999e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -6.415495e-01 7.670817e-01
    outer loop
      vertex 3.689235e-01 -9.291158e-01 5.806964e-01
      vertex 1.910111e-01 -9.291158e-01 5.806964e-01
      vertex 1.938359e-01 -9.767850e-01 5.408283e-01
    endloop
  endfacet
  facet normal 0.000000e+00 -6.415495e-01 7.670817e-01
    outer loop
      vertex 3.689235e-01 -9.291158e-01 5.806964e-01
      vertex 1.938359e-01 -9.767850e-01 5.408283e-01
      vertex 3.743793e-01 -9.767850e-01 5.408283e-01
    endloop
  endfacet
  facet normal 6.777984e-01 -4.476502e-01 5.832655e-01
    outer loop
      vertex 1.910111e-01 -9.291158e-01 5.806964e-01
      vertex 1.384548e-01 -9.707282e-01 6.098338e-01
      vertex 1.405023e-01 -1.019013e+00 5.703965e-01
    endloop
  endfacet
  facet normal 6.777984e-01 -4.476502e-01 5.832655e-01
    outer loop
      vertex 1.910111e-01 -9.291158e-01 5.806964e-01
      vertex 1.405023e-01 -1.019013e+00 5.703965e-01
      vertex 1.938359e-01 -9.767850e-01 5.408283e-01
    endloop
  endfacet
  facet normal 3.026220e-01 6.105850e-01 -7.318510e-01
    outer loop
      vertex 1.384548e-01 -9.707282e-01 6.098338e-01
      vertex 1.624968e-01 -9.772068e-01 6.143701e-01
      vertex 1.648999e-01 -1.025587e+00 5.749999e-01
    endloop
  endfacet
  facet normal 3.026220e-01 6.105850e-01 -7.318510e-01
    outer loop
      vertex 1.384548e-01 -9.707282e-01 6.098338e-01
      vertex 1.648999e-01 -1.025587e+00 5.749999e-01
      vertex 1.405023e-01 -1.019013e+00 5.703965e-01
    endloop
  endfacet
  facet normal 0.000000e+00 6.311828e-01 -7.756341e-01
    outer loop
      vertex 1.624968e-01 -9.772068e-01 6.143701e-01
      vertex 3.689235e-01 -9.772068e-01 6.143701e-01
      vertex 3.743793e-01 -1.025587e+00 5.749999e-01
    endloop
  endfacet
  facet normal 0.000000e+00 6.311828e-01 -7.756341e-01
    outer loop
      vertex 1.624968e-01 -9.772068e-01 6.143701e-01
      vertex 3.743793e-01 -1.025587e+00 5.749999e-01
      vertex 1.648999e-01 -1.025587e+00 5.749999e-01
    endloop
  endfacet
endsolid shards
```

<!-- optional proof anchor (uncomment to enable):
<p align="center"><sub>MPC signing architecture audited to 0 Critical/High · threshold-BLS air-gapped signing presented at NBC-2025, NTU Singapore</sub></p>
-->

---

<p align="center">
  <sub>📍 Bangalore · open to Singapore · ✉️ <a href="mailto:rana.iiitb@gmail.com">rana.iiitb@gmail.com</a> · ✍️ writeups soon</sub>
</p>
