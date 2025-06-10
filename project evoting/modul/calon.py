ListCalon = []

def tambah_calon():
    idCal = input("Masukan ID Calon: ")
    if any(c['id'] == idCal for c in ListCalon):
        print("ID sudah terdaftar ")
        return
    namaCal = input("Masukan Nama Calon: ")
    visiCal = input("Masukan Nama Visi Misi: ")

    ListCalon.append({"id": idCal, "nama": namaCal,"visi": visiCal, "jumlah suara":0})
    print ("calon berhasil didaftarkan")

def get_data():
    return ListCalon

def cari_calon(id):
    for c in ListCalon:
        if c['id'] == id:
            return c
    return None
