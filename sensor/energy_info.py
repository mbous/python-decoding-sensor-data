from house_info import HouseInfo
from datetime import date, datetime

#ENERGY_PER_BULB = 0.2
#ENERGY_BITS = 0x0F0
class EnergyData(HouseInfo): #child class (inherits from class HouseInfo)

    def _get_energy(self, rec): #private method to convert energy record

        self.ENERGY_PER_BULB = 0.2
        self.ENERGY_BITS = 0x0F0
        energy = int(rec, base=16)
        energy = energy & self.ENERGY_BITS 
        energy = energy >> 4
        return energy
    
    def _convert_data(self, data):
        recs = []
        for rec in data:
            recs.append(self._get_energy(rec))
        return recs
    
    def get_data_by_area(self, rec_area=0):
        recs = super().get_data_by_area("energy_usage", rec_area)
        return self._convert_data(recs)

    def get_data_by_date(self, rec_date=date.today()):
        recs = super().get_data_by_date("energy_usage", rec_date)
        return self._convert_data(recs)
    
    def calculate_energy_usage(self, data): # store the sum of all converted values in the data list 
        #for testing purpose
        total_energy = sum([self.ENERGY_PER_BULB * field for field in data])
        return total_energy
    


    

    
        

        
