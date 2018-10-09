import csv 

# Reading the CSV file which has all the extracted tweets
with open("C:/SQL_Node/Achu/tweets.csv","r",newline='', encoding='utf-8') as csv_file:
    tweets = []
    tweet= csv.reader(csv_file, delimiter=",")
    for tw in tweet:    
        tweets.append(tw)

lexicon = dict()
# Creating a dictonary with word list
with open("C:/SQL_Node/Achu/Complete_Lexicon.csv","r") as filen:
    reader = csv.reader(filen)
    for row in reader:
        lexicon[row[0]] = float(row[1])

for t in tweets:
    score = 0
    final_score = 0
    counts = 0

    for word1 in t:
        lower_case = word1.lower()
        for word in lower_case.split():
            counts = counts + 1
            if word in lexicon:
                # Comparing each word with lexicon and assigning scores
                score = lexicon[word]
                final_score =  final_score + score
        # Getting the average for each tweet
        if counts > 0:
            avg = final_score/counts
        # Catogrize the tweets with its Score
        if final_score > 0:
            result = 'Positive'
        elif final_score < 0:
            result = 'Negative'
        else:
            result = 'Neutral'
        # Writing the tweet, sentiment and scores to a CSV file    
        with open ("analysis_senti.csv", "a", newline="", encoding='utf-8') as new_file:
                writer = csv.writer(new_file,delimiter=",")
                writer.writerow([word1,result,avg])

