import os
import threading
import concurrent.futures 
from concurrent.futures import ThreadPoolExecutor
spider_list = ["cgtn","engmgc","enpcn","allglobal_spider","cmilt"]
cwd = os.getcwd()
spider_path = os.path.join(cwd,"news_scrapper/news_scrapper")
os.chdir(spider_path)
def run_spiders(spider):
    os.system(f"scrapy crawl {spider}")
        
with ThreadPoolExecutor(max_workers=5) as exe:
    result = exe.map(lambda p: run_spiders(p), spider_list)