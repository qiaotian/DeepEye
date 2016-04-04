import dicom
import os
import numpy as np
from matplotlib import pyplot, cm

"""
Use os.path.walk to traverse data directory
to collect all .dcm files into a list
"""

dicom_path = "./data/"
dicom_list = [] # create an empty list
for directory, subdir, filelist in os.walk(dicom_path):
    for filename in filelist:
        if ".dcm" in filename.lower():
            dicom_list.append(os.path.join(directory, filename))


"""
Load the 1st DICOM file for calculating the
dimentions, pixel spacing and slice thickness
"""

refds = dicom.read_file(dicom_list[0])
const_pixel_dims = (int(refds.Rows), int(refds.Columns), len(dicom_list))
const_pixel_spacing = (float(refds.PixelSpacing[0]), float(refds.PixelSpacing[1]), float(refds.SliceThickness))

x = np.arange(0.0, (const_pixel_dims[0]+1)*const_pixel_spacing[0], const_pixel_spacing[0])
y = np.arange(0.0, (const_pixel_dims[1]+1)*const_pixel_spacing[1], const_pixel_spacing[1])
z = np.arange(0.0, (const_pixel_dims[2]+1)*const_pixel_spacing[2], const_pixel_spacing[2])


dicom_cube = np.zeros(const_pixel_dims, dtype=refds.pixel_array.dtype)

for filename in dicom_list:
    ds = dicom.read_file(filename)
    dicom_cube[:,:,dicom_list.index(filename)] = ds.pixel_array


pyplot.figure(dpi=300)
pyplot.axes().set_aspect('equal', 'datalim')
pyplot.set_cmap(pyplot.gray())
pyplot.pcolormesh(x, y, np.flipud(dicom_cube[:,:,80]))
pyplot.show()
