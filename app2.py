import glob, os
import PyPDF2
import re

class Extraction:
    def __init__(self):
        self.path = "assets2/*.pdf"
        self.files = glob.glob(self.path)
        self.countpages = 9
        self.count = 0
        
        self.k_countpages = 9
        self.k_count = 0
        self.KennethRows = []
        self.kenneth_sales_numbers = []
        self.kenneth_sales_extract_numbers = []
        self.int_kenneth_sales_numbers = []
        
        self.st_countpages = 9
        self.st_count = 0
        self.stephrows = []
        self.steph_sales_numbers = []
        self.steph_sales_extract_numbers = []
        self.int_steph_sales_numbers = []
        
        self.ad_countpages = 9
        self.ad_count = 0
        self.andresRows = []
        self.andre_sales_numbers = []
        self.andre_sales_extract_numbers = []
        self.int_andre_sales_numbers = []
        
        self.jk_countpages = 9
        self.jk_count = 0
        self.jackrows = []
        self.jack_sales_numbers = []
        self.jack_sales_extract_numbers = []
        self.int_jack_sales_numbers = []
        
        self.lm_countpages = 9
        self.lm_count = 0
        self.luismimiRows = []
        self.luismimi_sales_extract_numbers = []
        self.luis_sales_numbers = []
        self.int_luis_sales_numbers = []
        
        self.cl_countpages = 9
        self.cl_count = 0
        self.carlosRows = []
        self.carlos_sales_numbers_extract = []
        self.carlos_sales_numbers = []
        self.int_carlos_sales_numbers = []
        
        
        self.total = []
        
# -----------------guide to know how the list are working--


        self.gus_countpages = 9
        self.gus_count = 0
        # list for the rows that have gustavo's name on it 
        self.gustavorows = [] 
        
        # this list is to add the numbers that are going to extract from the document
        self.gustavo_sales_numbers = []
        
        # list to put the numbers separately that gustavo row have 
        self.sales_numbers = []
        
        # list to convert the list that (sales_numbers) have into a int list
        self.gus_int_sales_numbers = []
        
    def totall(self):
        print(self.files)
        self.total = [self.int_kenneth_sales_numbers, self.int_steph_sales_numbers, self.int_andre_sales_numbers, self.int_jack_sales_numbers, self.int_luis_sales_numbers, self.int_carlos_sales_numbers, self.gus_int_sales_numbers]
        
        print("This is what Kenneth sell the last day: ", self.int_kenneth_sales_numbers)
        print("This is what Stephanie sell the last day: ", self.int_steph_sales_numbers)
        print("This is what Andres sell the last day: ", self.int_andre_sales_numbers)
        print("This is what Jack sell the last day: ", self.int_jack_sales_numbers)
        print("This is what Luis Mimi sell the last day: ", self.int_luis_sales_numbers)
        print("This is what Carlos sell the last day: ", self.int_carlos_sales_numbers)
        print("This is what Gustavo sell the last day: ", self.gus_int_sales_numbers)
        print("And this is the total: ", sum(self.total))
        
    def kennt_extract_sale_number(self, line):
        match = re.search(r'(\d+)(\s*(Tarjeta|Efectivo))', line, re.IGNORECASE)
        if match:
            return match.group(1)
        return 0
    
    def steph_extract_sale_number(self, line):
        match = re.search(r'(\d+)(\s*(Tarjeta|Efectivo))', line, re.IGNORECASE)
        if match:
            return match.group(1)
        return 0
    
    def andre_extract_sale_number(self, line):
        match = re.search(r'(\d+)(\s*(Tarjeta|Efectivo))', line, re.IGNORECASE)
        if match:
            return match.group(1)
        return 0
    def jack_extract_sale_number(self, line):
        match = re.search(r'(\d+)(\s*(Tarjeta|Efectivo))', line, re.IGNORECASE)
        if match:
            return match.group(1)
        return 0
    def mimi_extract_sale_number(self, line):
        match = re.search(r'(\d+)(\s*(Tarjeta|Efectivo))', line, re.IGNORECASE)
        if match:
            return match.group(1)
        return 0
    def carlos_extract_sale_number(self, line):
        match = re.search(r'(\d+)(\s*(Tarjeta|Efectivo))', line, re.IGNORECASE)
        if match:
            return match.group(1)
        return 0
    def gus_extract_sale_number(self, line):
        match = re.search(r'(\d+)(\s*(Tarjeta|Efectivo))', line, re.IGNORECASE)
        if match:
            return match.group(1)
        return 0
    
    
        
    def extract_sale_number_card(self, line):
        match = re.search(r'(\d+)(\s*Tarjeta)', line, re.IGNORECASE)
        if match:
            return match.group(1)
        return 0    

        
    def data_extraction(self):
        for filename in self.files:
            print(filename)
            pdf_reader = PyPDF2.PdfReader(filename)
            while self.count <= len(pdf_reader.pages):            
                if len(pdf_reader.pages) > self.countpages:
                    page = pdf_reader.pages[self.countpages]
                    text = page.extract_text() 
                    
                    if text:
                        lines = text.strip().split('\n')
                        
                                            
                        for line in lines:
                            if "KENNETH G" in line:
                                self.kenneth_sales_numbers = self.kennt_extract_sale_number(line)
                                self.KennethRows.append((self.kenneth_sales_numbers, "KENNETH G"))
                                
                                
                        for line in lines:
                            if "STEPHANIE" in line:
                                self.steph_sales_numbers = self.steph_extract_sale_number(line)                            
                                self.stephrows.append((self.steph_sales_numbers, 'STEPHANIE'))
                                
                                
                        for line in lines:
                            if "ANDRES G" in line:
                                self.andre_sales_numbers = self.  andre_extract_sale_number(line)                             
                                self.andresRows.append((self.andre_sales_numbers, "ANDRES G"))
                                
                                
                        for line in lines:
                            self.jack_sales_numbers = self.jack_extract_sale_number(line)
                            if "JACK" in line:
                                self.jackrows.append((self.jack_sales_numbers, 'JACK'))
                                
                                
                        for line in lines:
                            self.luis_sales_numbers = self.mimi_extract_sale_number(line)
                            if "LUIS MIMI" in line:
                                self.luismimiRows.append((self.luis_sales_numbers, "LUIS MIMI"))
                                
                                
                        for line in lines:
                            self.carlos_sales_number = self.carlos_extract_sale_number(line)
                            if "CARLOS S" in line:
                                self.carlosRows.append((self.carlos_sales_number, "CARLOS"))
                                
                                
                        for line in lines:
                            if "GUSTAVO" in line:
                                self.gustavo_sales_numbers = self.gus_extract_sale_number(line)
                                self.gustavorows.append((self.gustavo_sales_numbers, "GUSTAVO"))

                        
                self.countpages += 1
                self.count += 1     
                
        for row in self.KennethRows:
            numbers = row[0]
            print(row)
            self.kenneth_sales_extract_numbers.append(numbers)
        
        self.int_kenneth_sales_numbers = sum(list(map(int, self.kenneth_sales_extract_numbers)))
        print("this is the number for kenneth in the last day: ", self.int_kenneth_sales_numbers)
        
        for row in self.stephrows: 
            numbers = row[0]
            print(row)
            self.steph_sales_extract_numbers.append(numbers)
            
        self.int_steph_sales_numbers = sum(list(map(int, self.steph_sales_extract_numbers)))
        print("this is what steph sells the last day: ", self.int_steph_sales_numbers)
        
        
        for row in self.andresRows:
            numbers = row[0]
            print(row)
            self.andre_sales_extract_numbers.append(numbers)
            
        
        self.int_andre_sales_numbers = sum(list(map(int, self.andre_sales_extract_numbers)))
        print("This is what andres sels the last day: ", self.int_andre_sales_numbers)
        
        for row in self.jackrows:
            numbers = row[0]
            print(row)
            self.jack_sales_extract_numbers.append(numbers)
        
        self.int_jack_sales_numbers = sum(list(map(int, self.jack_sales_extract_numbers)))
        print("this is the numbers of sales for jack in the last day: ", self.int_jack_sales_numbers)
        
        
        for row in self.luismimiRows:
            numbers = row[0]
            print(row)
            self.luismimi_sales_extract_numbers.append(numbers)
        
        self.int_luis_sales_numbers = sum(list(map(int, self.luismimi_sales_extract_numbers)))
        
        print("this is what luis sell this past day: ", self.int_luis_sales_numbers)
        
        
        for row in self.carlosRows:
            numbers = row[0]
            print(row)
            self.carlos_sales_numbers_extract.append(numbers)

        self.int_carlos_sales_numbers = sum(list(map(int, self.carlos_sales_numbers_extract)))
        print("this is what Carlos sell the last day: ", self.int_carlos_sales_numbers)
        
        
        for row in self.gustavorows:
            numbers = row[0]
            print(row)
            self.sales_numbers.append(numbers)

        self.gus_int_sales_numbers = sum(list(map(int, self.sales_numbers)))
        print("this is what Gustavo sell the last day: ", self.gus_int_sales_numbers)
            
    def kennethExtraction(self):                            
        for filename in self.files:
            # print(filename)
            pdf_reader = PyPDF2.PdfReader(filename)
            while self.k_count <= len(pdf_reader.pages):            
                if len(pdf_reader.pages) > self.k_countpages:
                    page = pdf_reader.pages[self.k_countpages]
                    text = page.extract_text() 
                    
                    if text:
                        lines = text.strip().split('\n')
                        
                                            
                        for line in lines:
                            if "KENNETH G" in line:
                                self.kenneth_sales_numbers = self.kennt_extract_sale_number(line)
                                self.KennethRows.append((self.kenneth_sales_numbers, "KENNETH G"))
                
                self.k_countpages += 1
                self.k_count += 1 
        
        for row in self.KennethRows:
            numbers = row[0]
            print(numbers)
            self.kenneth_sales_extract_numbers.append(numbers)
        
        self.int_kenneth_sales_numbers = sum(list(map(int, self.kenneth_sales_extract_numbers)))
        print("this is the number for kenneth in the last day: ", self.int_kenneth_sales_numbers)


    def stephExtraction(self):                            
        for filename in self.files:
            # print(filename)
            pdf_reader = PyPDF2.PdfReader(filename)
            while self.st_count <= len(pdf_reader.pages):            
                if len(pdf_reader.pages) > self.st_countpages:
                    page = pdf_reader.pages[self.st_countpages]
                    text = page.extract_text() 
                    
                    if text:
                        lines = text.strip().split('\n')
                        
                                            
                        for line in lines:
                            if "STEPHANIE" in line:
                                self.steph_sales_numbers = self.steph_extract_sale_number(line)                            
                                self.stephrows.append((self.steph_sales_numbers, 'STEPHANIE'))
                
                self.st_countpages += 1
                self.st_count += 1 
        
        for row in self.stephrows: 
            numbers = row[0]
            print(row)
            self.steph_sales_extract_numbers.append(numbers)
            
        self.int_steph_sales_numbers = sum(list(map(int, self.steph_sales_extract_numbers)))
        print("this is what steph sells the last day: ", self.int_steph_sales_numbers)
            
    def andresExtraction(self):                            
        for filename in self.files:
            # print(filename)
            pdf_reader = PyPDF2.PdfReader(filename)
            while self.ad_count <= len(pdf_reader.pages):            
                if len(pdf_reader.pages) > self.ad_countpages:
                    page = pdf_reader.pages[self.ad_countpages]
                    text = page.extract_text() 
                    
                    if text:
                        lines = text.strip().split('\n')
                        
                                            
                        for line in lines:
                            if "ANDRES G" in line:
                                self.andre_sales_numbers = self.  andre_extract_sale_number(line)                             
                                self.andresRows.append((self.andre_sales_numbers, "ANDRES G"))
                
                self.countpages += 1
                self.count += 1 
        
        for row in self.andresRows:
            numbers = row[0]
            print(numbers)
            self.andre_sales_extract_numbers.append(numbers)
            
        
        self.int_andre_sales_numbers = sum(list(map(int, self.andre_sales_extract_numbers)))
        print("This is what andres sels the last day: ", self.int_andre_sales_numbers)
            
    def jackExtraction(self):                            
        for filename in self.files:
            # print(filename)
            pdf_reader = PyPDF2.PdfReader(filename)
            while self.count <= len(pdf_reader.pages):            
                if len(pdf_reader.pages) > self.countpages:
                    page = pdf_reader.pages[self.countpages]
                    text = page.extract_text() 
                    
                    if text:
                        lines = text.strip().split('\n')
                        
                                            
                        for line in lines:
                            self.jack_sales_numbers = self.jack_extract_sale_number(line)
                            if "JACK" in line:
                                self.jackrows.append((self.jack_sales_numbers, 'JACK'))
                
                self.countpages += 1
                self.count += 1 
        
        
        for row in self.jackrows:
            numbers = row[0]
            print(numbers)
            self.jack_sales_extract_numbers.append(numbers)
        
        self.int_jack_sales_numbers = sum(list(map(int, self.jack_sales_extract_numbers)))
        print("this is the numbers of sales for jack in the last day: ", self.int_jack_sales_numbers)
            
    def luismimiExtraction(self):                            
        for filename in self.files:
            # print(filename)
            pdf_reader = PyPDF2.PdfReader(filename)
            while self.count <= len(pdf_reader.pages):            
                if len(pdf_reader.pages) > self.countpages:
                    page = pdf_reader.pages[self.countpages]
                    text = page.extract_text() 
                    
                    if text:
                        lines = text.strip().split('\n')
                        
                                            
                        for line in lines:
                            self.luis_sales_numbers = self.mimi_extract_sale_number(line)
                            if "LUIS MIMI" in line:
                                self.luismimiRows.append((self.luis_sales_numbers, "LUIS MIMI"))
                
                self.countpages += 1
                self.count += 1 
        
        for i in self.luismimiRows:
            numbers = i[0]
            print(numbers)
            self.luismimi_sales_extract_numbers.append(numbers)
        
        self.int_luis_sales_numbers = sum(list(map(int, self.luismimi_sales_extract_numbers)))
        
        print("this is what luis sell this past day: ", self.int_luis_sales_numbers)
            
            
    def carlosExtraction(self):                           
        for filename in self.files:
            # print(filename)
            pdf_reader = PyPDF2.PdfReader(filename)
            while self.count <= len(pdf_reader.pages):            
                if len(pdf_reader.pages) > self.countpages:
                    page = pdf_reader.pages[self.countpages]
                    text = page.extract_text() 
                    
                    if text:
                        lines = text.strip().split('\n')
                        
                                            
                        for line in lines:
                            self.carlos_sales_number = self.carlos_extract_sale_number(line)
                            if "CARLOS S" in line:
                                self.carlosRows.append((self.carlos_sales_number, "CARLOS"))
                
                self.countpages += 1
                self.count += 1 
        
        print(self.carlosRows)
        for i in self.carlosRows:
            numbers = i[0]
            print(numbers)
            self.carlos_sales_numbers_extract.append(numbers)

        self.int_carlos_sales_numbers = sum(list(map(int, self.carlos_sales_numbers_extract)))
        print("this is what Carlos sell the last day: ", self.int_carlos_sales_numbers)
            
            
    
    def gustavoExtraction(self): 
        for filename in self.files:
            # print(filename)
            pdf_reader = PyPDF2.PdfReader(filename)
            while self.count <= len(pdf_reader.pages):            
                if len(pdf_reader.pages) > self.countpages:
                    page = pdf_reader.pages[self.countpages]
                    text = page.extract_text() 
                    
                    if text:
                        lines = text.strip().split('\n')
                        
                                            
                        for line in lines:
                            self.gustavo_sales_numbers = self.gus_extract_sale_number(line)
                            if "GUSTAVO" in line:
                                self.gustavorows.append((self.gustavo_sales_numbers, "GUSTAVO"))
                
                self.countpages += 1
                self.count += 1 
        
        print(self.gustavorows)
        for i in self.gustavorows:
            numbers = i[0]
            print(numbers)
            self.sales_numbers.append(numbers)

        self.gus_int_sales_numbers = sum(list(map(int, self.sales_numbers)))
        print("this is what Gustavo sell the last day: ", self.gus_int_sales_numbers)
        
        
        # for sales, name in self.gustavorows:
        #     print(f"{name}: {sales}")
        
extraction = Extraction()
extraction.data_extraction()
# extraction.kennethExtraction()
# extraction.gustavoExtraction()
# extraction.carlosExtraction()
# extraction.luismimiExtraction()
# extraction.jackExtraction()
# extraction.andresExtraction()
# extraction.stephExtraction()

extraction.totall()