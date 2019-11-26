try:
    import json
    import requests
except ImportError as error:
        print(error.__class__.__name__ + ": " + str(error))


class weather:

    def __init__(self, city_name, country_name="CA"):
        self.city_name = city_name
        self.country_name = country_name
        self.base_url = "https://api.openweathermap.org/data/2.5/forecast?q="
        self.api_key = "677335c0781adffdff76cac4b7d8c160"
        self.mode = "json"
    
    def request(self,api_key):
        URL =  "{}{},{}&mode={}&appid={}".format(self.base_url , self.city_name , self.country_name , self.mode , self.api_key)
        self.resp = requests.get( URL )

        if self.resp.status_code != 200:
            print (self.resp.content)
            exit()


    def parse_data(self):

        self.request(self.api_key)
        
        re = json.loads(self.resp.content)

        self.temp_lists = {}

        for r in re['list']:
            # print (r['dt_txt'])
            if(r['dt_txt'][11:13]=="06" or r['dt_txt'][11:13]=="12"):
                if (self.temp_lists.get(r['dt_txt'][8:10])==None):
                    list =[]
                    list.append(r)
                    self.temp_lists[r['dt_txt'][8:10]] = list
                    
                elif(self.temp_lists.get(r['dt_txt'][8:10])!=None):
                    self.temp_lists[r['dt_txt'][8:10]].append(r)

        return self.temp_lists