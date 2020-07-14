# Tamil Words Database Generator

This script aims to find unique words in tamil wikipedia database

### Usage
- Download [dataset](https://dumps.wikimedia.org/tawiki/20200701/). Use for example tawiki-20200701-pages-meta-current.xml
- Run: `python3 parse_tamil.py -f tawiki-20200701-pages-meta-current.xml -o output`

### Running
```
┌─[ganesh@ganesh-ubuntu] - [~/Documents/tamil] - [Tue Jul 14, 20:20]
└─[$] <git:(master*)> python3 parse_tamil.py -f tawiki-20200701-pages-meta-current.xml -o output
Parsing tawiki-20200701-pages-meta-current.xml. This may take 10 to 30 seconds depending on your machine...
Parsing: 100%|██████████████████████████████████████████████| 409398/409398 [00:17<00:00, 23005.58it/s]
Parsing done!
dumping: 100%|██████████████████████████████████████████████| 1937274/1937274 [00:01<00:00, 1724118.30it/s]
```

### Output
```
wc -l output
1937274 output
```

## Authors

* **Ganesh K.** - [LinkedIn](https://www.linkedin.com/in/ganesh-kathiresan/)
