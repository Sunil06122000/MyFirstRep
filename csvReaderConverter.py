import pandas as pd

class cvcReader():
    def __init__(self,filename):
        self.filename=filename

    def csvReader(self):
        csvdf=pd.read_csv(self.filename)
        return csvdf

class csvToJsonConvert(cvcReader):
    def __init__(self,filename,Outputfile):
        self.filename=filename
        self.Outputfile=Outputfile

    def csvToJson(self):
        csvdfobj=cvcReader(self.filename)
        csvdf=csvdfobj.csvReader()
        jsondf=csvdf.to_json(self.Outputfile)
        readjsondf=pd.read_json(self.Outputfile)
        print (readjsondf)
        return jsondf

if __name__=='__main__':
    filename='country_full.csv'
    #callcsvReader=cvcReader(filename)
    #csvfiledf=callcsvReader.csvReader()
    #print (csvfiledf)
    outputfile='country_full.json'
    callcsvToJsonConvert=csvToJsonConvert(filename,outputfile)
    jsondf=callcsvToJsonConvert.csvToJson()
    print (jsondf)

