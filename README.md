# scraping-threading
Implemented multithreading on a regular selenium web scraping script with 3 different variants 

* Normal scraper
```py
main()
```

* Applied threading to scraper
```py
for i in range(threads):
    t = threading.Thread(target=main)
    t.start()
    
```

* Applied threading and OOP
```py
    def __init__(self, threads):
        self.threads = threads
        for _ in range(self.threads):
            t1 = threading.Thread(target=self.main)
            t1.start()
```

```py
Scraper()
```

