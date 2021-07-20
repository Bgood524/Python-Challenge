import os
import csv

csvpath = os.path.join('Resources','election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #Total Votes Cast
    election_df = list(csvreader)
    row_count =  len(election_df)

     
    


    #Create a list of candidates to loop through data and count each candidate's votes
    candidates = []


    
    for row in election_df:
        candidate = row[2]
        candidates.append(candidate)

    Khan_count = candidates.count("Khan")
    Correy_count = candidates.count("Correy")
    Li_count = candidates.count("Li")
    OTooley_count = candidates.count("O'Tooley")

    print(OTooley_count)

    #get individual percentages
    Khan_percentage = Khan_count / row_count * 100
    Correy_percentage = Correy_count / row_count * 100
    Li_percentage = Li_count / row_count * 100
    OTooley_percentage = OTooley_count / row_count * 100

    candidates = ["Khan", "Correy", "Li", "O'Tooley"]
    votes = [Khan_count, Correy_count, Li_count, OTooley_count]

    candidates_and_votes = dict(zip(candidates,votes))
    winner = max(candidates_and_votes, key = candidates_and_votes.get)


#output
    print("---------------------------------------------------------")
print("Election Results")
print("----------------------------------------------------------")
print("Total Votes: " + str(row_count))
print("Khan: " + str(Khan_percentage) + "% ("  + str(Khan_count) + ")")
print("Correy: " + str(Correy_percentage) + "% ("  + str(Correy_count) + ")")
print("Li: " + str(Li_percentage) + "% ("  + str(Li_count) + ")")
print("O'Tooley: " + str(OTooley_percentage) + "% ("  + str(OTooley_count) + ")")
print("----------------------------------------------------------")
print("Winner:" + str(winner))
print("----------------------------------------------------------")

#txt output

with open('election_analysis.txt', 'w') as analysis:
     analysis.write("---------------------------------------------------------\n")
     analysis.write("Election Results\n")
     analysis.write("----------------------------------------------------------\n")
     analysis.write("Total Votes: " + str(row_count))
     analysis.write("Khan: " + str(Khan_percentage) + "% ("  + str(Khan_count) + ")\n")
     analysis.write("Correy: " + str(Correy_percentage) + "% ("  + str(Correy_count) + ")\n")
     analysis.write("Li: " + str(Li_percentage) + "% ("  + str(Li_count) + ")\n")
     analysis.write("O'Tooley: " + str(OTooley_percentage) + "% ("  + str(OTooley_count) + ")\n")
     analysis.write("----------------------------------------------------------\n")
     analysis.write("Winner:" + str(winner) + "\n")
     analysis.write("----------------------------------------------------------\n")