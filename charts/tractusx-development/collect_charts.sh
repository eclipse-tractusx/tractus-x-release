#!/user/bin/sh

if [ ! -d charts ]
then
    mkdir charts
fi 

for product_index_file in $(cat product-chart-index.yaml | yq eval '.product-charts[].chart-url' -)
do  
    echo "getting product chart index file at: $product_index_file"
    curl -L -o act-product.yaml $product_index_file

    for chart in $(cat act-product.yaml | yq e ".entries | keys" - | sed 's/- //g')
    do 
        echo "processing chart: $chart"
        if [ ! -d charts/$chart ]
        then
            mkdir charts/$chart
        fi 

        for url in $(cat act-product.yaml | yq e ".entries.$chart[].urls[]" -)
        do
            echo "processing $url"

            filename=$(basename $url)
            if [ ! -f charts/$chart/$filename ]
            then
                echo "getting file: $filename"
                curl -L -o charts/$chart/$filename $url
            fi
        done 
    done
done

rm act-product.yaml

#add if needed --url string
helm repo index --merge charts/index.yaml charts

rm index.yaml