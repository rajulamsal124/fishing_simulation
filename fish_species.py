#class Austrailan Bass
class AustrailianBass:
        #constant variables
    MAX_WEIGHT = 4000
    MAX_EATING_WEIGHT = 2500
    NAME = 'Australian Bass'
    LATIN_NAME = 'Macquaria Novemaculeata'
        
        #construtor with one arguments
    def __init__(self,weight): 
        if weight > self.MAX_WEIGHT:  #weight is greater than max weight
            pass   #return false
        else:
            self.weight=weight   #weight is initialised
    def is_good_eating(self):
        if self.weight>500 and self.weight<self.MAX_EATING_WEIGHT:  #if wieight is between 500 and Max eating weight
            return True   #return true
        else:
            return False   #return false
        
    def __str__(self):

            #return string
        msg=self.NAME+"("+self.LATIN_NAME+"), "+str(self.weight)+" "+str(self.is_good_eating())
        return msg


#class ShortFinnedEel
class ShortFinnedEel:
        #constant variables
    MAX_WEIGHT = 3000
    MAX_EATING_WEIGHT = 1500
    NAME = 'ShortFinnedEel'
    LATIN_NAME = 'Anguilla australis'
        
        #construtor with one arguments
    def __init__(self,weight): 
        if weight > self.MAX_WEIGHT:  #weight is greater than max weight
            pass   #return false
        else:
            self.weight=weight   #weight is initialised
    
    def is_good_eating(self):
        if self.weight>500 and self.weight<self.MAX_EATING_WEIGHT:  #if wieight is between 500 and Max eating weight
            return True   #return true
        else:
            return False   #return false
        
    def __str__(self):

            #return string
        msg=self.NAME+"("+self.LATIN_NAME+"), "+str(self.weight)+" "+str(self.is_good_eating())
        return msg

#class EelTailedCatfish
class EelTailedCatfish:
        #constant variables
    MAX_WEIGHT = 5000
    MAX_EATING_WEIGHT = 3500
    NAME = 'EelTailedCatfish'
    LATIN_NAME = 'Tandanus tandanus'
        
        #construtor with one arguments
    def __init__(self,weight): 
        if weight > self.MAX_WEIGHT:  #weight is greater than max weight
            pass   #return false
        else:
            self.weight=weight   #weight is initialised
    
    def is_good_eating(self):
        if self.weight>500 and self.weight<self.MAX_EATING_WEIGHT:  #if wieight is between 500 and Max eating weight
            return True   #return true
        else:
            return False   #return false
        
    def __str__(self):

            #return string
        msg=self.NAME+"("+self.LATIN_NAME+"), "+str(self.weight)+" "+str(self.is_good_eating())
        return msg

#class GippslandPerch
class GippslandPerch:
        #constant variables
    MAX_WEIGHT = 4000
    MAX_EATING_WEIGHT = 2000
    NAME = 'GippslandPerch'
    LATIN_NAME = 'Percichthyidae'
        
       #construtor with one arguments
    def __init__(self,weight): 
       if weight > self.MAX_WEIGHT:  #weight is greater than max weight
           pass   #return false
       else:
           self.weight=weight   #weight is initialised
   
    def is_good_eating(self):
       if self.weight>500 and self.weight<self.MAX_EATING_WEIGHT:  #if wieight is between 500 and Max eating weight
           return True   #return true
       else:
           return False   #return false
       
    def __str__(self):

           #return string
       msg=self.NAME+"("+self.LATIN_NAME+"), "+str(self.weight)+" "+str(self.is_good_eating())
       return msg

#class Branzino
class Branzino:
        #constant variables
    MAX_WEIGHT = 2000
    MAX_EATING_WEIGHT = 1000
    NAME = 'Branzino'
    LATIN_NAME = 'Dicentrarchus labrax'
        
        #construtor with one arguments
        #construtor with one arguments
    def __init__(self,weight): 
        if weight > self.MAX_WEIGHT:  #weight is greater than max weight
            pass   #return false
        else:
            self.weight=weight   #weight is initialised
    
    def is_good_eating(self):
        if self.weight>500 and self.weight<self.MAX_EATING_WEIGHT:  #if wieight is between 500 and Max eating weight
            return True   #return true
        else:
            return False   #return false
        
    def __str__(self):
    
            #return string
        msg=self.NAME+"("+self.LATIN_NAME+"), "+str(self.weight)+" "+str(self.is_good_eating())
        return msg

#class Tilapia
class Tilapia:
        #constant variables
    MAX_WEIGHT = 4000
    MAX_EATING_WEIGHT = 2000
    NAME = 'Tilapia'
    LATIN_NAME = 'Oreochromis niloticus'
        
        #construtor with one arguments
    def __init__(self,weight): 
        if weight > self.MAX_WEIGHT:  #weight is greater than max weight
            pass   #return false
        else:
            self.weight=weight   #weight is initialised
    
    def is_good_eating(self):
        if self.weight>500 and self.weight<self.MAX_EATING_WEIGHT:  #if wieight is between 500 and Max eating weight
            return True   #return true
        else:
            return False   #return false
        
    def __str__(self):

        #return string
        msg=self.NAME+"("+self.LATIN_NAME+"), "+str(self.weight)+" "+str(self.is_good_eating())
        return msg





