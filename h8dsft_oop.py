'''
=================================================
Non Graded Challenge 03 

Nama  : Diko Alfatha Ikhram
Batch : RMT-29

Program ini dibuat untuk melakukan input,show,search, and remove book from catalog.
=================================================
'''

class CatalogItem():
    def __init__(self):
        self.listBookCatalog = []
        self.message = ""

    def addItem(self, title, author):
        key = f"key{len(self.listBookCatalog)}"

        if(self.listBookCatalog):
            for item in self.listBookCatalog:
                while key == item['key']:
                    key = f"key{len(self.listBookCatalog) + 1}"

        item = {
            "key": key,
            "title": title,
            "author": author,
        }

        self.listBookCatalog.append(item)
        self.message = "Buku berhasil disimpan"
        
        return self.message

    def showItems(self):

        if(self.listBookCatalog):
            self.message = "No.|Judul|Penulis|Key"

        else:
            self.message = "Tidak ada buku yang tersedia saat ini"
        
        result = {
                "message": self.message,
                "result": self.listBookCatalog
            }

        return result
    
    def searchItem(self, title, author):

        if(title != "" or author != ""):
            if(self.listBookCatalog):
                self.message = "ini hasil pencarianmu: \n"
                self.message += "No.|Judul|Penulis|Key \n"
                for item in self.listBookCatalog:
                    if(title == item['title'] or author == item['author']):
                        self.message += f"1|{item['title']}|{item['author']}|{item['key']}"

                    else:
                        if(self.message == ""):
                            self.message = "Judul atau Penulis tidak ada"
            else:
                self.message = "Tidak ada buku yang tersedia saat ini"

        else:
            self.message = "Masukan Judul atau Penulis dengan benar"

        return self.message

    def removeItem(self, key):
        if(self.listBookCatalog):
            for item in self.listBookCatalog:
                if key == item['key']:
                    self.listBookCatalog.remove(item)
                    self.message = "Buku berhasil dihapus"
                    
        else:
            self.message = "Tidak ada buku yang tersedia saat ini"

        return self.message

if __name__ == "__main__":
    # Error Handling
    try:
        catalog =  CatalogItem()
        userInput = ""

        # digunakan untuk melooping indefinitely
        while userInput != "exit":
            print("=============================")
            print("Library Catalog System")
            print("=============================")
            print()
            print("Menu:")
            print("1. Input Buku")
            print("2. Cari Buku")
            print("3. Hapus Buku")
            print("4. Tampilkan Semua Buku")
            print()
            userInput = input("Masukan pilihan menu(1-4) atau ketik exit untuk keluar :")

            # digunakan untuk menentukan pilihan user
            if(userInput == "1"):
                print("Masukan Informasi Buku")

                inputTitle = input("Masukan judul buku: ")
                inputAuthor = input("Masukan penulis buku: ")

                print()
                print(catalog.addItem(inputTitle, inputAuthor))
            elif(userInput == "2"):
                print("Masukan Informasi Buku")

                inputTitle = input("Masukan judul buku: ")
                inputAuthor = input("Masukan penulis buku: ")

                print()
                print(catalog.searchItem(inputTitle, inputAuthor))

            elif(userInput == "3"):
                print("Masukan Informasi Buku")

                inputKey = input("Masukan key buku:")

                print()
                print(catalog.removeItem(inputKey))

            elif(userInput == "4"):

                result = (catalog.showItems())

                print()
                print(result['message'])
                if(result['result']):
                    n = 1
                    for item in result['result']:
                        print(f"{n}|{item['title']}|{item['author']}|{item['key']}")
                        n+=1   
            
            elif(userInput == "exit"):
                break
            else:
                print("Menu tidak tersedia, silahkan pilih dari menu yang ada.")

            print()
    except Exception as e:
        print(f"Error : {e}")