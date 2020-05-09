""" File includes the world class and how worlds are created. """

import random
import names

class world:
    def __init__(self):
        """ All initiating variables on worlds. """
        
        # Name of planet
        name = random.choice(names.world_name)
        self.name = name 

        percent_1 = random.randint(4,8) * 10
        percent_2 = 100 - percent_1

        # Percentage of land and ocean on planet
        percentage = {'Ocean': percent_1, 'Land': percent_2}
        self.percentage = percentage

        # Year the player starts at
        while True:
            try:
                current_year = int(input('What year do you want to start at? '))
                break
            except:
                print('Please choose a year.')
                continue 

        self.current_year = current_year
        
        # The year the player starts at
        starting_year = 0
        self.starting_year = starting_year
        
        # The planet's starting population (at year 0)
        start_population = percentage['Land'] * random.randint(100,10000)
        self.start_population = start_population

        # The population at the current year
        current_population = start_population
        self.current_population = current_population

        """ All initiating variables on factions. """
        
        # Number of starting factions
        num_start_factions = random.randint(4,10)

        self.num_start_factions = num_start_factions

        # Number of current factions
        num_current_factions = self.num_start_factions
        self.num_current_factions = num_current_factions

        # Percent of world population starting in each faction 
        start_pop_factions = []

        # max_faction_percent is the max starting percent
        max_faction_percent = 0.9

        # Limit for how much of a population a faction can get
        faction_limit = 0.35

        # Seperates the first instance from the rest
        faction_tick = 0

        # Number of people in each faction at very start
        for factions in range(self.num_start_factions):
            if faction_tick == 0:
                percent = round(random.uniform(0.01, faction_limit), 2)
                start_pop_factions.append(int(self.start_population * percent))
                max_faction_percent = max_faction_percent - percent
                faction_tick = 1
            else:
                percent = round(random.uniform(0.01, max_faction_percent - ((num_start_factions - factions) * 0.01)), 2)
                start_pop_factions.append(int(self.start_population * percent))
                max_faction_percent = max_faction_percent - percent

        self.start_pop_factions = start_pop_factions

        # Number of people in each faction currently
        current_pop_factions = self.start_pop_factions
        self.current_pop_factions = current_pop_factions
        
        # Name of every faction in a list
        faction_names = []

        for factions in range(self.num_start_factions):
            name = f"{names.faction_first} {random.choice(names.faction_second)} {random.choice(names.faction_third)}"
            faction_names.append(name)

        self.faction_names = faction_names

        # Dictionary of name and population of each faction
        name_pop_factions = {}

        for factions in range(self.num_start_factions):
            name_pop_faction = {self.faction_names[factions]: self.start_pop_factions[factions]}
            name_pop_factions.update(name_pop_faction)
            

        self.name_pop_factions = name_pop_factions


    # Prints planet's stats
    def stats(self):
        print('Planet Name: ' + self.name)
        print('Current Year: ' + str(self.current_year))
        print('Population: ' + str(self.current_population))
        print('Percent of Land: ' + str(self.percentage['Land']))
        print('Percent of Ocean: ' + str(self.percentage['Ocean']))
        print('Number of Factions: ' + str(self.num_current_factions))
        for factions in range(self.num_start_factions):
            print(f"Faction: {self.faction_names[factions]}, Population: {self.current_pop_factions[factions]}")


        
            

        
        
        

        

