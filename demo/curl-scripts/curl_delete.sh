if [ -z "$1" ]; then
	echo "usage curl_delete.sh <product_num>"
	exit 1
fi
curl -X DELETE http://localhost:8000/api/v1/products/${1}/destroy
echo "Deleted ${1}"
