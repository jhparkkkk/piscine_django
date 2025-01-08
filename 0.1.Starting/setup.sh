
url="https://cdn.intra.42.fr/document/document/22294/d01.tar.gz"

filename="${url##*/}"

wget "$url" -O "$filename"

tar -xzf "$filename"

