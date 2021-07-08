fetch("js/fullData.json")
    .then(response => response.json())
    .then(json => dataIteration(json)); //console.log(json));


async function dataIteration (jsonData){
    //console.log(jsonData.length);
    let len = jsonData.length;
    for(let i=0;i<len; i++){
        //TODO: manage async calls
        // Add code here

        // demo:
        // Accessing elements
        console.log(jsonData[i]);
        // Accessing a single field of the i-th element
        console.log(jsonData[i]['Postcode']);
        // await sendTransactionToBigChainDB(jsonData[i]);

    }

}
