from Memory import Memory

A = Memory("2000", 2, True)
A.setBrand("Acer")
A.setModel("2A")
A.setPrice("5.000.000")
A.setIdProduct(27)

print("Brand        : " + A.getBrand())
print("Model        : " + A.getModel())
print("Price        : " + A.getPrice())
print("Id Product   : " + str(A.getIdProduct()))
print("Frequency    : " + A.getFrequency())
print("Size Memory  : " + str(A.getMemorySize()))
print("Support Cuda : " + str(A.getSupportCuda()))