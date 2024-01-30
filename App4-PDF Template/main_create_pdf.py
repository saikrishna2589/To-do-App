# third party library fpdf (to be installed)

# this creates pdf object instance
from fpdf import FPDF

import pandas as pd

# orientation="p" is portrait. you can goto the implemetation to check documentation.
# 'mm' unit is not for font but for other purpose
pdf = FPDF(orientation="P", unit="mm", format="A4")

# type of pdf is a python object. we need to convert it to an actual document.
print(type(pdf))

#reading the file that contains csv data
df=pd.read_csv("topics.csv")


#looping over dataset
for index,row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times",style="B",size=24)

    #setting font to gray
    pdf.set_text_color(100,100,100)

#width =0 will stretch the cell to complete page. height =12 is heigh of cell
    pdf.cell(w=0,h=12,txt=row["Topic"])

    #adding a line below .x1,y1 cordinates will be starting point and x2,y2 ending point
    pdf.line(x1=10,y1=21,x2=200,y2=21)


pdf.output("output.pdf")
