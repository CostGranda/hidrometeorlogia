from netCDF4 import Dataset

my_example_nc_file = 'D:\avhrr-only-v2.19810901.nc'
fh = Dataset(my_example_nc_file, mode='r')

print(fh.variables) #ver variables en el archivo

sst = fh.variaIbles['interpolated_sst'][:] # copiarnop
