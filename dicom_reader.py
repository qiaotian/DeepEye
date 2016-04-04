import vtk
import numpy as np
import os

from vtk.util import numpy_support
from matplotlib import pyplot, cm

data_path = "./data/"
reader = vtk.vtkDICOMImageReader()
reader.SetDirectoryName(data_path)
reader.Update()

# Load dimentions using 'GetDataExtent'
_extent = reader.GetDataExtent()
const_pixel_dims = [_extent[1]-_extent[0]+1, _extent[3]-_extent[2]+1, _extent[5]-_extent[4]+1]

#Load spacing values
const_pixel_spacing = reader.GetPixelSpacing()

# Get the 'vtkImageData' object from the reader
image_data = reader.GetOutput()

# Get the 'vtkPointData' object from the 'vtkPointData' object
point_data = image_data.GetPointData()

# Ensure that only one array exists within the 'vtkPointData' object
assert(point_data.GetNumberOfArrays()==1)

# Get the 'vtkArray' (or whatever derived type) which is needed for the 'numpy_support.vtk_to_numpy' function
array_data = point_data.GetArray(0)

# Convert the 'vtkarray' to a numpy array
array_dicom = numpy_support.vtk_to_numpy(array_data)

# Reshape the numpy array to 3D using 'const pixel dims' as a 'shape'
array_dicom = array_dicom.reshape(const_pixel_dims, order='F')

print(array_dicom.shape)


# = dicom.read_file(dicom_list[0])
#const_pixel_dims = (int(array_dicom[0]), array_dicom[1], array_dicom[2])
#const_pixel_spacing = (float(refds.PixelSpacing[0]), float(refds.PixelSpacing[1]), float(refds.SliceThickness))

x = np.arange(0.0, (const_pixel_dims[0]+1)*const_pixel_spacing[0], const_pixel_spacing[0])
y = np.arange(0.0, (const_pixel_dims[1]+1)*const_pixel_spacing[1], const_pixel_spacing[1])
z = np.arange(0.0, (const_pixel_dims[2]+1)*const_pixel_spacing[2], const_pixel_spacing[2])


dicom_cube = np.zeros(const_pixel_dims, array_dicom.dtype)

#for filename in dicom_list:
#    ds = dicom.read_file(filename)
#    dicom_cube[:,:,dicom_list.index(filename)] = ds.pixel_array


pyplot.figure(dpi=300)
pyplot.axes().set_aspect('equal', 'datalim')
pyplot.set_cmap(pyplot.gray())
pyplot.pcolormesh(x, y, np.flipud(array_dicom[:,:,80]))
pyplot.show()


"""
# source/reader --> filter --> mapper --> actor --> renderer --> renderWindow --> interactor
# 1. Source
# Generate polygon data for a cube
cube = vtk.vtkCubeSource()
# 2. Mapper
# Create a mapper for the cube data
cube_mapper = vtk.vtkPolyDataMapper()
cube_mapper.SetInputData(cube.GetOutput())
# 3. Actor
# Connect the mapper to an actor
cube_actor = vtk.vtkActor()
cube_actor.SetMapper(cube_mapper)
cube_actor.GetProperty().SetColor(1.0, 0.0, 0.0)
# 4. Renderer
# Create
# a renderer and add the cube actor to it
renderer = vtk.vtkRenderer()
renderer.SetBackground(0.0, 0.0, 0.0)
renderer.AddActor(cube_actor)
# 5. Render window
# Create a render window
render_window = vtk.vtkRenderWindow()
render_window.SetWindowName("Simple VTK scene")
render_window.SetSize(400,400)
render_window.AddRenderer(renderer)
# 6. Interactor
# Create an interactor
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

# Initialize the interactor and start the rendering loop
interactor.Initialize()
render_window.Render()
interactor.Start()
"""
