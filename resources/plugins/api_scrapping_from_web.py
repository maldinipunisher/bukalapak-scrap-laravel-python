import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
import sys


def main():
    # print("Bukalapak scrapper")
    q = sys.argv[1]
    URL = (
        "https://www.bukalapak.com/products?from=omnisearch&from_keyword_history=false&search[keywords]="
        + q
        + "&search_source=omnisearch_keyword&source=navbar"
    )
    response = requests.get(URL + q)
    # print(URL)
    soup = BeautifulSoup(response.content, "html.parser")
    products = soup.find_all("div", {"class": "te-product-card"})
    data = []
    result = {"data": data}

    for res in products:
        try :
            rating = float(0)
            rating_temp = res.find("div", {"class" : "bl-product-card__description-rating-and-sold"}).find("a",  {"class" : "bl-link"}, href=True)
            terjual = "0"
            terjual_temp = res.find("div", {"class" : "bl-product-card__description-rating-and-sold"})
            product_image = res.find("img", {"class" : "bl-thumbnail--img"})['src']
            try :
                rating = float(rating_temp.string)
                terjual =terjual_temp.find_all("p", {"class" : "bl-text--body-14"})[1].string
            except AttributeError :
                pass
        except TypeError :
            pass

        seller = {
            "link": res.find("span", {"class": "bl-product-card__store"}).find(
                "a", {"class": "bl-link"}, href=True
            )["href"],
            "name": res.find("span", {"class": "bl-product-card__store"})
            .find("a", {"class": "bl-link"}, href=True)
            .string,
        }
        sold_split = terjual.strip().split(" ")
        data.append({
            "title" : res.find("a", {"class" : "bl-link"}, href = True).string.strip(),
            "link" : res.find("a", {"class" : "bl-link"}, href = True)['href'],
            "price" : res.find("p", {"class" : "bl-text--subheading-20"}).string.strip(),
            "location" : res.find("span", {"class" : "bl-product-card__location"}).string.strip(),
            "rating" : rating,
            "image" : product_image ,
            "sold" : int(sold_split[len(sold_split)-1] if len(sold_split) > 1 else sold_split[0]),
            "seller" : seller,
            })
    # with open("data.json", "w") as f:
    #     json.dump(result, f)
    print(json.dumps(result))


if __name__ == "__main__":
    main()
