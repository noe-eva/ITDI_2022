# Get the TRAINING set for the ITDI shared task 2022
# this script downloads and extracts the 
# nap, vec, pms, lmo, scn, eml, lld, lij, sc, fur, roa_tara and it
# wikipedias from 01.03.2022


# NOTE: dumps from 01.03.2022 are not available anymore
# 		get the ones from 01.03.2022 from zenodo 
#		or download the newer ones (in which case change name for wikiextractor)

#wget https://dumps.wikimedia.org/napwiki/20220301/napwiki-20220301-pages-articles-multistream.xml.bz2
#wget https://dumps.wikimedia.org/vecwiki/20220301/vecwiki-20220301-pages-articles-multistream.xml.bz2
#wget https://dumps.wikimedia.org/pmswiki/20220301/pmswiki-20220301-pages-articles-multistream.xml.bz2
#wget https://dumps.wikimedia.org/lmowiki/20220301/lmowiki-20220301-pages-articles-multistream.xml.bz2
#wget https://dumps.wikimedia.org/scnwiki/20220301/scnwiki-20220301-pages-articles-multistream.xml.bz2
#wget https://dumps.wikimedia.org/emlwiki/20220301/emlwiki-20220301-pages-articles-multistream.xml.bz2
#wget https://dumps.wikimedia.org/lldwiki/20220301/lldwiki-20220301-pages-articles-multistream.xml.bz2
#wget https://dumps.wikimedia.org/lijwiki/20220301/lijwiki-20220301-pages-articles-multistream.xml.bz2
#wget https://dumps.wikimedia.org/scwiki/20220301/scwiki-20220301-pages-articles-multistream.xml.bz2
#wget https://dumps.wikimedia.org/furwiki/20220301/furwiki-20220301-pages-articles-multistream.xml.bz2
#wget https://dumps.wikimedia.org/roa_tarawiki/20220301/roa_tarawiki-20220301-pages-articles-multistream.xml.bz2
#wget https://dumps.wikimedia.org/itwiki/20220301/itwiki-20220301-pages-articles-multistream.xml.bz2


# wikiextractor: https://github.com/attardi/wikiextractor
python -m wikiextractor.WikiExtractor napwiki-20220301-pages-articles-multistream.xml.bz2 -o nap_texts --json
python -m wikiextractor.WikiExtractor vecwiki-20220301-pages-articles-multistream.xml.bz2 -o vec_texts --json
python -m wikiextractor.WikiExtractor pmswiki-20220301-pages-articles-multistream.xml.bz2 -o pms_texts --json
python -m wikiextractor.WikiExtractor lmowiki-20220301-pages-articles-multistream.xml.bz2 -o lmo_texts --json
python -m wikiextractor.WikiExtractor scnwiki-20220301-pages-articles-multistream.xml.bz2 -o scn_texts --json
python -m wikiextractor.WikiExtractor emlwiki-20220301-pages-articles-multistream.xml.bz2 -o eml_texts --json
python -m wikiextractor.WikiExtractor lldwiki-20220301-pages-articles-multistream.xml.bz2 -o lld_texts --json
python -m wikiextractor.WikiExtractor lijwiki-20220301-pages-articles-multistream.xml.bz2 -o lij_texts --json
python -m wikiextractor.WikiExtractor scwiki-20220301-pages-articles-multistream.xml.bz2 -o sc_texts --json
python -m wikiextractor.WikiExtractor furwiki-20220301-pages-articles-multistream.xml.bz2 -o fur_texts --json
python -m wikiextractor.WikiExtractor roa_tarawiki-20220301-pages-articles-multistream.xml.bz2 -o roa_tara_texts --json
#python -m wikiextractor.WikiExtractor itwiki-20220301-pages-articles-multistream.xml.bz2 -o it_texts --json
