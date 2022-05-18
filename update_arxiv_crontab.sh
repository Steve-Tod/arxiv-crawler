cd ~/projects/arxiv-crawler
date >> ./log.txt
/home/zhenyu/miniconda3/envs/arxiv/bin/python fetch_papers.py >> ./log.txt
/home/zhenyu/miniconda3/envs/arxiv/bin/python filter_newest.py >> ./log.txt
echo "---------------------------------" >> ./log.txt
