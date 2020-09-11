import schedule, time, webbrowser

def open2406():
    print("Lecture is about to begin...")
    webbrowser.open('http://google.com')

def open3005():
    print("Lecture is about to begin...")
    webbrowser.open('http://google.com')

def open3008():
    print("Lecture is about to begin...")
    webbrowser.open('http://google.com')

def open3203():
    print("Lecture is about to begin...")
    webbrowser.open('http://google.com')

def open4001():
    print("Lecture is about to begin...")
    webbrowser.open('http://google.com')    

#Time

schedule.every().thursday.at("22:10").do(job)
schedule.every().thursday.at("22:10").do(job)
schedule.every().thursday.at("22:10").do(job)
schedule.every().thursday.at("22:10").do(job)
schedule.every().thursday.at("22:10").do(job)


while True:
    schedule.run_pending()
    print("online-class CONNECT")
    time.sleep(1)



