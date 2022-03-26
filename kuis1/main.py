# Saya Novaldi Sandi Ago mengerjakan Kuis 1 dalam mata DPBO untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

from Komoditas import Komoditas
from Lahan import Lahan
from Petani import Petani

from Tengkulak import Tengkulak
from Marketplace import Marketplace

lahan1 = Lahan("2003941", "Sawah", "Gerlong", "Sukasari", "Bandung", "Jawa Barat", "100 Hektar")
lahan2 = Lahan("2710202", "Gembur", "Padang Manis", "Padang Guci", "Kaur", "Bengkulu", "50 Hektar")

petani1 = Petani("62852", "2723", "Kazuma", "Jepang", "Pemilik Lahan", lahan1)
petani1.setIdKomoditas("93846312")
petani1.setNamaKomoditas("Isekai")
petani1.setJenisLahan("Sawah")
petani1.setSistemTanam("Campur Sari")

petani2 = Petani("52231", "8474", "Eren Yaeger", "Eldia", "Buruh", lahan2)
petani2.setIdKomoditas("98421712")
petani2.setNamaKomoditas("YMIR")
petani2.setJenisLahan("Gembur")
petani2.setSistemTanam("Tunggal Tanam")

petani1.showPetani()
print("")
petani2.showPetani()
print("")

tengkulak1 = Tengkulak("94319143", "67282", "Levi Ackerman", "Eldia", "31431")
tengkulak2 = Tengkulak("53234144", "53141", "Araragi Koyomi", "Bakemonogatari", "41984")

tengkulak1.showTengkulak()
print("")
tengkulak2.showTengkulak()
print("")

marketplace1 = Marketplace("7465729", "TokoLapak", "Online", "BusinessToCustomer")
marketplace2 = Marketplace("5892358", "ManggaTiga", "Offline", "BusinessToBusiness")

marketplace1.showMarketplace()
print("")
marketplace2.showMarketplace()