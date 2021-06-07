def exchangeData() :
    file1Data = open('File1.txt', 'r') 
    file2Data = open('File2.txt', 'r') 
    file1Data = file1Data.read()
    file2Data = file2Data.read()
    open("File1.txt", "w").write(file2Data)
    open("File2.txt", "w").write(file1Data)

exchangeData()
