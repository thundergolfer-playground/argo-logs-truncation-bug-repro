from loguru import logger
import random
import requests
import time

from bs4 import BeautifulSoup

TOTAL_RUNTIME_IN_SECS = 60 * 60 * 2


def page_text(soup):
    text = soup.find_all(text=True)
    output = ''
    blacklist = [
	    '[document]',
	    'noscript',
	    'header',
	    'html',
	    'meta',
	    'head',
	    'input',
	    'script',
	    # there may be more elements you don't want, such as "style", etc.
    ]

    for t in text:
	    if t.parent.name not in blacklist:
		    output += '{} '.format(t)

    return output.replace("\n", "")


def run():
    total_iterations = 1000
    iteration_len = TOTAL_RUNTIME_IN_SECS / total_iterations
    for iter in range(1, total_iterations + 1):
        logger.info(f"Running iteration {iter} / {total_iterations}")

        wiki_page_id = iter * random.randrange(10000)
        resp = requests.get(f"https://en.wikipedia.org/?curid={wiki_page_id}")

        soup = BeautifulSoup(resp.text, 'html.parser')

        some_page_text = page_text(soup)[250:750]
        logger.info(f"Start of wiki page body with id: {wiki_page_id}\n{some_page_text}")
        logger.info(f"Page title: {soup.title}")
        time.sleep(iteration_len)

    logger.info("demo run finished!")


if __name__ == '__main__':
    run()
