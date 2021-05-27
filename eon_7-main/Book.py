class Book: 
    def __init__(self,year,title,gn,author,publisher): 
        self.year = year 
        self.title = title 
        self.gn = gn 
        self.author = author 
        self.publisher = publisher 
    def Write(self,fs): 
        fs.write(self.year+",") 
        fs.write(self.title+",") 
        fs.write(str(self.gn)+",") 
        fs.write(self.author+",") 
        fs.write(self.publisher+",") 
    @staticmethod 
    def LoadBook(fs): 
        data = fs.readline() 
        elems = data.split(",") 
        if len(elems)<6: 
            return None 
        year = elems[0] 
        title = elems[1] 
        gn = int(elems[2]) 
        author = elems[3] 
        publisher = elems[4] 
        return Book(year,title,gn,author,publisher)
