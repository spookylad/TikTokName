from selenium import webdriver

driver = webdriver.Chrome('/Users/baxbarlow/TikTokName/chromedriver')
with open("usernames.txt", 'r') as f:
	for line in f:
		url = "https://www.tiktok.com/@" + line.strip()
		driver.get(url)
		#print(url)
		if (len(driver.title) == None):
			print(line)
