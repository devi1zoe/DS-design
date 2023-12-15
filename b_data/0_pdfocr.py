import pdfplumber
file_path = r'.\class_data\pyfa\xinxixuebu2021jipeiyangfangan202112.pdf'
with pdfplumber.open(file_path) as pdf:
    for page in pdf.pages:#page = pdf.pages[1]  #提取第十一页的代码   for page in pdf.pages: #提取所有的代码
        print(page.extract_images()) #extract_text可以换成extract_table(s)提取表单


# 暂时没有用到--都是docx文件