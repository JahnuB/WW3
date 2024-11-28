class Country():
    def __init__(self, name, pop, currency, cash):
        self.name = name
        self.pop = pop
        self.currency = currency
        #True currency value: the ratio of the country's currency against the true value
        #Given inflation or deflation, costs should rise in number to match inflation rate
        #However, bank balances and overall wealth should not increase
        #Therefore, everything tied to the tcv should be stored in true currency.
        #Stuff you can buy: True Value currency
        #Stuff you already have: Country's currency
        self.tcv = 10 
        
        self.budget = {
            "resource_mining":100000 * self.tcv,
            "military": 20000 * self.tcv,
            "social_programs":100000 * self.tcv,
            "maintenance": 10000 * self.tcv
        }
        #self.researchTree = []
        self.otherCountries = [
            "United States", "Canada", "Mexico", "India", "China"
        ]
        self.relations = self.calcRelations()
        #self.tasks = {}
        self.taxrates = {
            "income_tax": 15,
            "sales_tax": 5
        }
        self.popStats = {
            "avg_income" : 10000 * self.tcv,
            "taxed_sales": 5000 * self.tcv,
            #If any of these stats reaches below a certain threshold, highly negative effects
            #can risk you losing your leadership (a.k.a. losing the game)
            "avg_h": {          #Average happiness
                "financial": 25,  #Income, tax rates, GDP, and inflation affect this statistic
                "safety": 75,     #Military power, infrastructure, and GDP affects this statistic
                "education": 50,  #Research and GDP affects this statistic
                "health": 25,     #Research, infrastructure, and GDP affects this statistic
                "leadership": 50  #Every decision you make can influence this statistic
            }
        }
        self.income = {
            "income_tax": ((self.taxrates["income_tax"] / 100) * self.popStats["avg_income"]) * self.pop,
            "sales_tax": ((self.taxrates["sales_tax"] / 100) * self.popStats["taxed_sales"]) * self.pop,
            "mint": sum(self.budget.values()) * 0.01
        }
        self.treasury = {
            "cash": [cash, self.income["income_tax"] + self.income["sales_tax"]],
            "oil": [24246,462462],
            "coal": [0,0],
            "wood": [0,0],
            "gold": [0,0],
            "steel": [0,0],
            "iron": [0,0],
            "food": [0,0],
            "stone": [0,0],
            "clay": [0,0]
        }
        self.recruits = {
            "infantry": int(self.pop * .03),
            "cavalry": int(self.pop * .025),
            "artillery":int(self.pop * .02),
            "navy":int(self.pop * .025)
        }
        self.arsenal = {
            "trebuchets": 100, 
            "ships": 0, 
            "cannons": 1500
        }
    
    def calcRelations(self):
        cr = {}
        for country in self.otherCountries:
            cr[country] = 40
        return cr
    
    def updateStats(self, days):
        #Number values are generally kept track of on a yearly basis.
        #Adjust country stats by a percentage, equal to days/365.
        percent = days / 365
        for t in self.treasury.keys(): 
            if t == "cash": self.treasury[t][0] += round((percent * self.treasury[t][1]), 2)
            self.treasury[t][0] += round(percent * self.treasury[t][1])
    
class Russia(Country):
    def __init__(self):
        super().__init__("Russia", 10000000, "₽", 500035903)