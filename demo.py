from ner_exchange.market import NERExchange
from ner_exchange.sample_data import entities, listings

if __name__ == "__main__":
    book = NERExchange(entities(), listings())
    print(book.render())
