import tabula
  
# Read PDF File
# this contain a list
df = tabula.read_pdf("stores.pdf", pages = 1)[0]
  
# Convert into Excel File
df.to_excel('converted_to_excel.xlsx')
