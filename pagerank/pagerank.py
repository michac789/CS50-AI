import os
import random
import re
import sys
import numpy
import copy

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    result_dict = {}
    for webpage in corpus:
        prob = 0
        if webpage in corpus.get(page):
            prob = 1 / len(corpus.get(page))
        probability = (1 - damping_factor) / len(corpus) + (damping_factor * prob)
        result_dict[webpage] = probability
        if len(corpus.get(page)) == 0:
            result_dict[webpage] = 1 / len(corpus)
    return result_dict


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pagerank_dict = {}
    for webpage in corpus:
        pagerank_dict[webpage] = 0
    current_page = numpy.random.choice([webpage for webpage in corpus], 1, p = [1 / len(corpus) for webpage in corpus])[0]
    for i in range(n):
        pagerank_dict[current_page] += 1 / n
        model = transition_model(corpus, current_page, damping_factor)
        current_page = numpy.random.choice([webpage for webpage in model], 1, p = [webpage for webpage in model.values()])[0]
    return pagerank_dict


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pagerank_dict = {}
    for webpage in corpus:
        pagerank_dict[webpage] = 1 / len(corpus)
    accurate3dp = False
    while not accurate3dp:
        accurate3dp = True
        dict_copy = copy.deepcopy(pagerank_dict)
        for webpage in corpus:
            new_value = 0
            for webpage2 in corpus:
                model = transition_model(corpus, webpage2, damping_factor)
                new_value = new_value + dict_copy[webpage2] * model.get(webpage)
            pagerank_dict[webpage] = new_value
        for webpage in pagerank_dict:
            if abs(pagerank_dict[webpage] - dict_copy[webpage]) > 0.001:
                accurate3dp = False
    return pagerank_dict


if __name__ == "__main__":
    main()