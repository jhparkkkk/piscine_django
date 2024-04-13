
url="https://cdn.intra.42.fr/document/document/10784/d00.tar.gz"

filename="${url##*/}"

wget "$url" -O "$filename"

tar -xzf "$filename"

