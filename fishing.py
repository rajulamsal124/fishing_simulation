import pickle
import fish_species  #imported the module in the same folder
import random
import time
from matplotlib import pyplot as plt
#calling AustralianBass object, contstrutor(__init__(weight)) and __str__
#__str__ return the string to AustrailianBass

def start_fishing():
    #print(fish)
    #f_list=[]
    basket=[]
    all_fish=[]
    b_w=0
    while b_w < 25:
        time.sleep(0.1)
        fish = random.randint(0,5)
        if fish ==0:
            try:
                w = random.randint(500,4000)
                AustrailianBass=fish_species.AustrailianBass(w) 
                #print(AustrailianBass)
                fs=str(AustrailianBass)
                x = fs.split(', ')
                xx=x[1]
                s=xx.split(' ')
                ww=float(s[0])
                weight=float(ww)/1000
                #print(weight)
                if s[1]=='True':
                    
                    st=x[0]+" wights "+str(weight)+" kg - added to the basket."
                    st1=x[0]+" wights "+str(weight)+" kg."
                    all_fish.append(st)
                    basket.append(st1)   
                    b_w+=weight
                else:
                    
                    st=x[0]+" wights "+str(weight)+" kg - released."
                    all_fish.append(st)
            except:
                pass
            #print(st)
        elif fish ==1:
            try:
                w = random.randint(500,4000)
                ShortFinnedEel=fish_species.ShortFinnedEel(w) 
                #print(ShortFinnedEel)
                fs=str(ShortFinnedEel)
                x = fs.split(', ')
                xx=x[1]
                s=xx.split(' ')
                ww=float(s[0])
                weight=float(ww)/1000
                #print(weight)
                if s[1]=='True':
                    
                    st=x[0]+" wights "+str(weight)+" kg - added to the basket."
                    st1=x[0]+" wights "+str(weight)+" kg."
                    all_fish.append(st)
                    basket.append(st1)   
                    b_w+=weight
                else:
                    
                    st=x[0]+" wights "+str(weight)+" kg - released."
                    all_fish.append(st)
                #print(st)
            except:
                pass
        elif fish ==2:
            try:
                w = random.randint(500,4000)
                EelTailedCatfish=fish_species.EelTailedCatfish(w) 
                #print(ShortFinnedEel)
                fs=str(EelTailedCatfish)
                x = fs.split(', ')
                xx=x[1]
                s=xx.split(' ')
                ww=float(s[0])
                weight=float(ww)/1000
                #print(weight)
                if s[1]=='True':
                    
                    st=x[0]+" wights "+str(weight)+" kg - added to the basket."
                    st1=x[0]+" wights "+str(weight)+" kg."
                    all_fish.append(st)
                    basket.append(st1)   
                    b_w+=weight
                else:
                    
                    st=x[0]+" wights "+str(weight)+" kg - released."
                    all_fish.append(st)
                #print(st)
            except:
                pass
        elif fish ==3:
            try:
                w = random.randint(500,4000)
                GippslandPerch=fish_species.GippslandPerch(w) 
                #print(ShortFinnedEel)
                fs=str(GippslandPerch)
                x = fs.split(', ')
                xx=x[1]
                s=xx.split(' ')
                ww=float(s[0])
                weight=float(ww)/1000
                #print(weight)
                if s[1]=='True':
                    
                   st=x[0]+" wights "+str(weight)+" kg - added to the basket."
                   st1=x[0]+" wights "+str(weight)+" kg."
                   all_fish.append(st)
                   basket.append(st1)   
                   b_w+=weight
                else:
                   
                   st=x[0]+" wights "+str(weight)+" kg - released."
                   all_fish.append(st)
                #print(st)
            except:
                pass
        elif fish ==4:
            try:
        
                w = random.randint(500,4000)
                Branzino=fish_species.Branzino(w) 
                #print(ShortFinnedEel)
                fs=str(Branzino)
                x = fs.split(', ')
                xx=x[1]
                s=xx.split(' ')
                ww=float(s[0])
                weight=float(ww)/1000
                #print(weight)
                if s[1]=='True':
                    
                    st=x[0]+" wights "+str(weight)+" kg - added to the basket."
                    st1=x[0]+" wights "+str(weight)+" kg."
                    all_fish.append(st)
                    basket.append(st1)   
                    b_w+=weight
                else:
                    
                    st=x[0]+" wights "+str(weight)+" kg - released."
                    all_fish.append(st)
                #print(st)
            except:
                pass
        elif fish ==5:
            try:
                w = random.randint(500,4000)
                Tilapia=fish_species.Tilapia(w) 
                #print(ShortFinnedEel)
                fs=str(Tilapia)
                x = fs.split(', ')
                xx=x[1]
                s=xx.split(' ')
                ww=float(s[0])
                weight=float(ww)/1000
                #print(weight)
                if s[1]=='True':
                    
                    st=x[0]+" wights "+str(weight)+" kg - added to the basket."
                    st1=x[0]+" wights "+str(weight)+" kg."
                    all_fish.append(st)
                    basket.append(st1)   
                    b_w+=weight
                else:
                    
                    st=x[0]+" wights "+str(weight)+" kg - released."
                    all_fish.append(st)
                #print(st)
            except:
                pass
    print("Fishing Started!")
    for item in all_fish:
        print(item)
    print("Basket is full. End of fishing session.")
    return basket
def print_basket(basket):
    print("Content of the basket:")
    for item in basket:
        print("\t\t",item)
def plot_basket(basket):
    label=["Australian ","Finned","EelTailed", "Gippsland","Branzino","Tilapia"]
    wt=[0,0,0,0,0,0]
    for j in basket:
        if "Australian" in j:
            x = j.split(' ')
            wt[0]+=float(x[4])
        if "Short" in j:
            x = j.split(' ')
            #print(x)
            wt[1]+=float(x[3])
        if "Catfish" in j:
            x = j.split(' ')
            wt[2]+=float(x[3])
        if "Gippsland" in j:
            x = j.split(' ')
            wt[3]+=float(x[2])
        if "Branzino" in j:
            x = j.split(' ')
            wt[4]+=float(x[3])

        if "Tilapia" in j:
            x = j.split(' ')
            wt[5]+=float(x[3]) 
    plt.figure()
    plt.bar(label,wt)
    plt.ylabel("Weights in kg")
    plt.show
            
def save_basket(basket, file_name):
    basketfile = open(file_name, 'basket')
      
    # source, destination
    pickle.dump(basket, basketfile)                     
    basketfile.close()
def load_basket(file_name):
    basketfile = open(file_name,'basket')     
    db = pickle.load(basketfile)
    for i in db:
        print(i)
    basketfile.close()
    
#calling a function start_fishing
basket=start_fishing()
bar=plot_basket(basket)
        