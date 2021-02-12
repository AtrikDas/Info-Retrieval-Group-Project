import twint
import pandas

countries = ["India", "China", "Singapore", "United States", "Russia"]
keywords = ["#Trump2020", "#Vote", "#vote", "#Election2020", "#Biden", "#VoteBlueToSaveAmerica", "#trump2020", "#VoteTrumpOut", "#election2020", "#trump", "#biden", "#2020election", "#November3rd", "#NovemberIsComing", "#donaldtrump", "#MyPresident", "#Elections_2020", "#2020elections", "#USElections", "#bluewave2020", "ballot", "mailin", "mail-in", "mail in", "donaldtrump", "donaldjtrump",
            "donald j trump", "donald trump", "don trump", "joe biden", "joebiden", "biden", "mike pence", "michael pence", "mikepence", "michaelpence", "kamala harris", "kamala", "kamalaharris", "trump", "PresidentTrump", "MAGA", "trump2020", "Sleepy Joe", "Sleepyjoe", "HidenBiden", "CreepyJoeBiden", "NeverBiden", "BidenUkraineScandal", "DumpTrump", "NeverTrump", "VoteRed", "VoteBlue"]


def scrape_by_country(outfile):
    for country in countries:
        print(country)
        for keyword in keywords:
            print(keyword)
            c = twint.Config()
            c.Search = keyword
            c.Since = '2020-11-15'
            c.Store_csv = True
            c.Output = "./" + outfile
            c.Near = country
            c.Hide_output = True
            c.Count = True
            c.Stats = True
            c.Resume = 'resume.txt'
            c.Location = True
            c.Limit = 1000
            twint.run.Search(c)


scrape_by_country('Elections_Tweets_Dataset3.csv')
