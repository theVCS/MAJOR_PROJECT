from icrawler.builtin import GoogleImageCrawler

limit = 150
# lst = ["Sachin Tendulkar","Virat Kohli","MS Dhoni","Rohit Sharma","Ravindra Jadeja","Suresh Raina","Akshay Kumar","Amitabh Bachchan","Irrfan Khan","Ajay Devgn","Anupam Kher","Rajnikant","Allu Arjun","Narendra Modi","Amit Shah", "Nirmala Sitharaman","Nitin Gadkari","Subrahmanyam Jaishankar","Rajnath Singh"," Mansukh L. Mandaviya"]
lst = ["Sachin Tendulkar"]

for folder in lst:
    google_Crawler = GoogleImageCrawler(storage = {'root_dir': f"E:\MAJOR_PROJECT\software\moduleFaceRecon\images\{folder}"})
    google_Crawler.crawl(keyword = folder, max_num = limit)
