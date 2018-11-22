import sys
import re

def readTI(ti,TIs):
        tiTerms = []
        ti = ti.split()
        for ch in ti:
                if ((len(ch) > 2) and (re.match('\w',ch) or ch == "_" or ch == "-")):
                        tiTerms.append(ch)
        TIs.append(tiTerms)
 
def readDESC(desc,DESCs):
        descTerms = []
        desc = desc.split()
        for ch in desc:
                if ((len(ch) > 2) and (ch.isalnum() or ch == "_" or ch == "-")):
                        descTerms.append(ch)
        DESCs.append(descTerms)

def parse(line,terms,IDs,Dates,LOCs,CATs,TIs,DESCs,Prices):
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


def main():
        file = open(sys.argv[1],"r")
        contents = file.read()
        file.close()
        contents = contents.split("\n")
        terms = open("terms.txt", "w")
        ads = []
        IDs = []
        Dates = []
        LOCs = []
        CATs = []
        TIs = []
        DESCs = []
        Prices = []
        for line in contents:
                if re.findall(r'^<ad>',line, flags=0):
                        ads.append(line)
                        parse(line,terms,IDs,Dates,LOCs,CATs,TIs,DESCs,Prices) 
        writeTerms(terms,IDs,TIs,DESCs)
        terms.close()

if __name__ == "__main__":
        main()
