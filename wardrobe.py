

class wardrobe():

    def __init__(self, data):
        self.data = data
        self.weather = {}
        self.temp_min = {}
        self.temp_max = {}
    
    def get_stuff (self):
        for date, date_data_list in self.data.items():
            # print (j)
            for day_data in date_data_list:
                if(self.weather.get(date)==None):
                    list = []
                    print (day_data["weather"][0]['description'])
                    list.append(day_data["weather"][0]['description'])
                    self.weather[date]= list
                elif(self.weather.get(date)!=None):
                    self.weather[date].append(day_data["weather"][0]['description'])
        
        print (self.weather)