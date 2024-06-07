# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector as mysql
from QuoteHarvester.data import *
from QuoteHarvester.settings import enableDatabaseStorage, mySQLServerPassword, mySQLServerUsername 
class QuoteharvesterPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get('book_title') is None: 
            adapter['book_title'] = 'None'
        for field in adapter.field_names():
            value = adapter.get(field)
            adapter[field] = value.strip()
        value  = adapter.get("likes")
        adapter['likes'] = int(value.split()[0])

        return item
class SaveToMySQLPipeline:
    def __init__(self):
        if enableDatabaseStorage:
            self.db  = mysql.connect(
                host = 'localhost',
                user = mySQLServerUsername,
                password = mySQLServerPassword
            )
            self.cu = self.db.cursor()
            self.cu.execute('CREATE DATABASE IF NOT EXISTS quotes;')
            self.cu.execute('USE quotes;')
            self.cu.execute("CREATE TABLE IF NOT EXISTS quotes(id INT PRIMARY KEY AUTO_INCREMENT, quote TEXT NOT NULL, book_title VARCHAR(150) NOT NULL, author VARCHAR(100) NOT NULL, likes INT NOT NULL);")
    def process_item(self, item, spider):
            if enableDatabaseStorage:
                adapter = ItemAdapter(item)
                self.cu.execute("INSERT INTO quotes (quote, book_title, author, likes) VALUES ('{}', '{}','{}', {});".format(adapter['quote'][0],adapter['book_title'], adapter['author'], adapter['likes']))
                self.db.commit()
            return item
    def close_spider(self, spider):
        if enableDatabaseStorage:
            self.cu.close()
            self.db.close()