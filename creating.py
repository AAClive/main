from flask import Flask
from selenium import webdriver
from flask import render_template
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.chrome.service import Service
import time
from flask import request
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(service=Service(executable_path=os.environ.get("CHROMEDRIVER_PATH")), options=chrome_options)
sp=1
blank=3
p=3
pricevalues={}
rt=[]
ars=[]
arpssacm=0
driver.get('https://opensea.io/explore-collections')

app=Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    global variable
    if request.method == "POST":
        variable = request.form.get("variable")
        print(variable)
        search=driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/nav/div[2]/div/div/div/input')
        search.send_keys(variable)
        time.sleep(3)
        searchres=driver.find_element(By.XPATH,'//*[@id="NavSearch--results"]/li[2]/a').click()
        time.sleep(5)
        floorprices=driver.find_element(By.XPATH,'//*[@id="main"]/div/div/div[1]/div[2]/div[5]/div/div[3]/a/div/div[1]/div/span').text
        print(floorprices)
        xyz=driver.find_element(By.XPATH,'//*[@id="main"]/div/div/div[3]/div/div/div/div[3]/div[3]/div[2]')
        xyz=xyz.text.split('\n')
        nrt=driver.find_element(By.XPATH,'//*[@id="main"]/div/div/div[3]/div/div/div/div[3]/div[3]/div[2]/div/div').text
        print(nrt)
        for line in range(len(xyz)):
            executalble=f"var{line}nftnamepage=xyz[{line}]"
            exec(executalble)
            mana=f"var{line}nftnamepage=var{line}nftnamepage.lower()"
            exec(mana)
        print(xyz)
        for lane in range(len(xyz)):
            if blank==3:
                global dsa
                dsa=f"pricevalues['{xyz[1]}']=var{blank}nftnamepage"
                exec(dsa)
                blank=0
                wda=f"name{lane}nft=pricevalues['{xyz[1]}']"
                exec(wda)
            if lane==p+8:
                print(lane)
                dsa=f"pricevalues['{xyz[sp]}']=var{lane}nftnamepage"
                exec(dsa)
                p=p+8
                # if len(ars)==0:
                #     for y in pricevalues.keys():
                #         ars.append(y) 
                # for line in ars:
                #     name
            # rats=lane+1
            # wda=f"name{rats}nft=pricevalues['{xyz[rats]}']"
            # exec(wda)
            # print(rats)
            if lane==sp+8:
                sp=sp+8
            
    return render_template('main.html')

@app.route('/nft')
def nft():
    return render_template('t.html',ma=pricevalues)

@app.route('/clivestext')
def tesing():
    rqdwdwa=driver.find_element(By.XPATH,'/html/body').text
    return render_template('tesing.html',m=rqdwdwa)

@app.route('/Discover')
def dis():
    time.sleep(3)
    namepage=driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]').text
    namepage=namepage.split('\n')
    print(namepage)
    var0ntfname=namepage[0]
    var4ntfname=namepage[4]
    var12ntfname=namepage[12]
    var8ntfname=namepage[8]
    #executeable=f"var{line}ntfname=namepage[{line}]"
    #exec(executeable)
    return render_template('dis.html',data0=var0ntfname,data1=var4ntfname,data2=var8ntfname,data3=var12ntfname)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

@app.errorhandler(500)
def error_server(e):
    return render_template("500.html"),500
if __name__ == '__main__':
    app.run(debug=True)
