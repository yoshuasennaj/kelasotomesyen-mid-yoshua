from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHROME_BINARY_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-minimized") #set minimize website
chrome_options.binary_location = CHROME_BINARY_PATH


with webdriver.Chrome(options=chrome_options) as driver: # setelah 'with' selesai dieksekusi, otomatis akan memanggil metode quit() 
# driver = webdriver.Chrome(options=chrome_options) (jika tidak pakai with)

    urls = [
            "https://www.tiket.com",
            "https://www.tokopedia.com",
            "https://www.orangsiber.com",
            "https://demoqa.com",
            "https://automatetheboringstuff.com"
            ]
    try:
            for url in urls:
                driver.get(url)
                domain_name = url.replace("http://", "").replace("https://", "").replace("www.", "") #untuk menghilangkan https://www pada output biar sesuai tugas
                title = driver.title
                WebDriverWait(driver, 10).until(EC.title_is(driver.title)) 
                #coba pakai explicit wait dibanding implicity wait dan sleep, karena ada kondisi tertentu menunggu hingga judul halaman sesuai dengan judul sebenarnya
                print(f"{domain_name} - {title}")
    except:
            print(f"Error guys")
# else:
#     # digunakan jika tidak pakai with, tapi kalau ga pakai quit() tetap ketutup ga sih bang setelah selesai execute hehe
#     driver.quit()
