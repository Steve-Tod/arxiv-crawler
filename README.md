# arxiv filter

This is a simple keyword based filter of newest arxiv papers. This repo is based on [arxiv-sanity-preserver](https://github.com/karpathy/arxiv-sanity-preserver).

## Installation

```bash
pip install -r requirements.txt
```

## Usage

First modify the text files under `info` directory, fill in your own interested authors and keywords. For keywords, you can use `+` if you want a combination of multiple keywords.

Then fetch the data new papers by running `python fetch_papers.py`. Please run `python fetch_papers.py -h` 

Finally run `python filter_newest.py` to filter the newest papers based on the selected keywords. It will create a simple html file of the results in `daily_results` and copy it to `~\Desktop`.