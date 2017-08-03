import re

def normalizemac(mac):
    if (len(re.findall('\w',mac))) == 12:
            
        result = re.sub(':','',mac)
        result = re.sub('\.','',result)

        print(result)  #clean
        print(':'.join(re.findall('\d\d',result)))   #colons
        print('.'.join(re.findall('\d\d\d\d',result)))   #dots

   
    else:
        print('Invalid MAC')
  
normalizemac('1223.4343.4531')
