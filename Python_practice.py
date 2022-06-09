#counties = ["Arapahoe","Denver","Jefferson"]

#if "Arapahoe" in counties or "El Paso" in counties:

    #print("Arapahoe or El Paso are in the list of counties.")

#else:

    #print("Arapahoe and El Paso is not in the list of counties.")


counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jeffereson": 432438}

#for county in counties_dict:

    #print(counties_dict[county])

#for county in counties_dict.keys():
    #print(county)

#for voters in counties_dict.values():

    #print(voters)

#for county in counties_dict:

    #print (counties_dict.get(county))

#for county, voters in counties_dict.items():

    #print(county + " county has " + str(voters) + " registered voters.")

#for county, voters in counties_dict.items():
    #print(f"{county} county has {voters:,} registered voters.")

voting_data = [{''"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

#for i in range(len(voting_data)):

    #print(voting_data[i]['county'])

#for county_dict in voting_data:
    #for value in county_dict.values():

        #print(value)

#for county_dict in voting_data:
    #for value in county_dict.items():
        #print(f"{county_dict} county has {value} registered voters.")

#for i in range(len(voting_data)):
    #for value in voting_data.values():

       # print(voting_data[i]['county'])

#for county, voters in voting_data.():
    #print(f"{county} county has {voters:,} registered voters.")

for data in voting_data:
    print(f'{data["county"]} has {data["registered_voters"]:,} registered voter')
