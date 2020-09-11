import schedule, time

def job():
    print("Something's up")



#Time
# schedule.day(1).seconds.do(job)

schedule.every().thursday.at("22:10").do(job)
while True:
    schedule.run_pending()
    print("Working")
    time.sleep(1)


