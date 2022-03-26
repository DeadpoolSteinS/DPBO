from Pc import Pc
from Processor import Processor
from Disk import Disk
from Ram import Ram

processor = Processor("Ryzen 3 5300U", 3000000)
disk = Disk("SSD", "512GB", 1000000)
ram = Ram("8GB", 500000)

pc = Pc(processor, disk, ram)
pc.showPc()

print("")

pc.getProcessor().setName("Intel I3 Gen11")
pc.getProcessor().setPrice(1000000)
pc.showPc()