#creating a class called BrowserStack
class BrowserStack:
#creating a function called __init__
    def __init__(self):
        self.data = []
        self.current = -1
#creating a function called navigation which adds data
    def navigation(self, data):
        self.data.append(data)
        self.current += 1
#creating a function called backward which takes us to the back page in a browser
    def backward(self):
        if self.current > 0:
            self.current -= 1
#creating a function called forwardward which takes us to the back page in a browser
    def forward(self):
        if self.current < len(self.data) - 1:
            self.current += 1
#creating a function called browser
    def browser(self):
        self.data = []
        self.current = -1
#creating a function append to add in new data
    def append(self, data):
        self.data.append(data)
        self.current += 1

    def __str__(self):
        return str(self.data)

browser = BrowserStack()
browser.append('www.google.com')
browser.append('www.github.com')
browser.append('www.yahoo.com')
browser.append('www.ucu.com')
browser.append('www.microsoft.com')
browser.append('www.skype.com')
print(browser)
browser.backward()
browser.backward()
browser.forward()
browser.navigation('www.3wshools.com')
browser.forward()

        

