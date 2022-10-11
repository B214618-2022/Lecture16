IFS="/><"

echo "Type your organism...: e.g. cosmoscarta"
read beast
echo "Type your database...: e.g. nucleotide"
read db

efetchstuff=$(wget -qO- "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=${db}&term=${beast}&usehistory=y" | egrep "QueryKey|WebEnv")

QueryKey=$(echo $efetchstuff | awk '{print $(NF-5)}')

WebEnv=$(echo $efetchstuff | awk '{print $(NF-2)}')

wget -qO ${beast}_sequences.fasta "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=${db}&query_key=${QueryKey}&WebEnv=${WebEnv}&rettype=fasta&retmode=text"
echo "${beast}_sequences.fasta file retrieved"
unset IFS
