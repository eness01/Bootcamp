
class library:
    def __init__(self,file_name="books.txt"):
        self.file_name=file_name
        with open(self.file_name,"a+"):
            pass
    def add_books(self):
        name =input("Kitabın Adı: ")
        writer =input("Kitabın Yazarı: ")
        date =input("Yayınlanma Tarihi: ")
        page =input("Sayfa Sayısı: ")
        with open(self.file_name,"a+") as dosya:
            dosya.write(f"{name},{writer},{date},{page}\n")
        print("Kitabınız başarıyla kaydedildi.")
    def list_books(self):
        with open(self.file_name) as dosya:
            dosya.seek(0)
            for satır in dosya.readlines():
                books_about = satır.strip().split(',')
                print(f"Kitabın Adı:{books_about[0]},Kitabın yazarı:{books_about[1]}")
    def remove_books(self):
        remove_name = input("Silmek istediğiniz kitabın adı nedir? ")
        with open(self.file_name, "r") as dosya:
            lines = dosya.readlines()

        with open(self.file_name, "w") as dosya:
            for line in lines:
                if remove_name not in line:
                    dosya.write(line)

        print(f"{remove_name} adlı kitap silinmiştir.")

if __name__ =="__main__":
    kutuphane=library()
    while True :
        print("\n1.Add Books\n2.List Books\n3.Remove Books\n4.Exit(q)")
        choose=input("Ne yapmak istersiniz? ")
        if choose=="1":
            kutuphane.add_books()
        elif choose=="2":
            kutuphane.list_books()
        elif choose=="3":
            kutuphane.remove_books()
        elif choose=="q":
            print("Programdan Çıkılıyor.")
            break
        else:
            print("Lütfen bir seçim yapın.")





