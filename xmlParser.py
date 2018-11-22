import sys
import re

def readTI(ti,TIs):
        tiTerms = []
        ti = ti.split()
        for ch in ti:
                sch = re.search('(.*)&#(\d*);',ch)
                if sch:  
                        ch = sch.group(1)                   
                if (len(ch) > 2) and (re.match('\w',ch) or re.match('-',ch)):
                        tiTerms.append(ch)
        TIs.append(tiTerms)

def readDESC(desc,DESCs):
        descTerms = []
        desc = desc.split()
        for ch in desc:
                sch = re.search('&#(\d*);',ch)
                if sch:  
                        ch = sch.group(1)  
                if (len(ch) > 2) and (re.match('\w',ch) or re.match('-',ch)):
                        descTerms.append(ch)               
        DESCs.append(descTerms)

def parse(line,IDs,Dates,LOCs,CATs,TIs,DESCs,Prices):
        searchObj = re.search( '(.*)<aid>(.*)</aid>', line)
        if searchObj:
                IDs.append(searchObj.group(2))
        searchObj = re.search( '(.*)<date>(.*)</date>', line)
        if searchObj:
                Dates.append(searchObj.group(2))
        searchObj = re.search( '(.*)<loc>(.*)</loc>', line)
        if searchObj:
                LOCs.append(searchObj.group(2))
        searchObj = re.search( '(.*)<cat>(.*)</cat>', line)
        if searchObj:
                CATs.append(searchObj.group(2))
        searchObj = re.search( '(.*)<ti>(.*)</ti>', line)
        if searchObj:
                readTI(searchObj.group(2),TIs)
        searchObj = re.search( '(.*)<desc>(.*)</desc>', line)
        if searchObj:
                readDESC(searchObj.group(2),DESCs)
        searchObj = re.search( '(.*)<price>(.*)</price>', line)
        if searchObj:
                Prices.append(searchObj.group(2))

def writeTerms(terms,IDs,TIs,DESCs):
        allTerms = []
        for j in range(len(TIs)):
                allTerms.append(TIs[j] + DESCs[j])
        for i in range(len(IDs)):
                for trm in allTerms[i]:
                        terms.write(trm.lower() + ":" +IDs[i] + "\n")

def writePDates(pdates,IDs,Dates,CATs,LOCs):
        for i in range(len(IDs)):
                pdates.write(Dates[i] + ":" +IDs[i] + "," + CATs[i] + "," + LOCs[i] + "\n")

def writePrices(prices,IDs,Prices,CATs,LOCs):
        for i in range(len(IDs)):
                prices.write(Prices[i] + ":" +IDs[i] + "," + CATs[i] + "," + LOCs[i] + "\n")

def writeAds(ads,IDs,xmlAds):
        for i in range(len(IDs)):
                ads.write(IDs[i]+ ":" + xmlAds[i] + "\n")

def main():
        file = open(sys.argv[1],"r")
        contents = file.read()
        file.close()
        contents = contents.split("\n")
        terms = open("terms.txt", "w")
        pdates = open("pdates.txt", "w")
        prices = open("prices.txt","w")
        ads = open("ads.txt","w")
        xmlAds = []
        IDs = []
        Dates = []
        LOCs = []
        CATs = []
        TIs = []
        DESCs = []
        Prices = []
        for line in contents:
                if re.findall(r'^<ad>',line, flags=0):
                        xmlAds.append(line)
                        parse(line,IDs,Dates,LOCs,CATs,TIs,DESCs,Prices) 
        writeTerms(terms,IDs,TIs,DESCs)
        writePDates(pdates,IDs,Dates,CATs,LOCs)
        writePrices(prices,IDs,Prices,CATs,LOCs)
        writeAds(ads,IDs,xmlAds)
        terms.close()
        pdates.close()
        prices.close()
        ads.close()

if __name__ == "__main__":
        main()
