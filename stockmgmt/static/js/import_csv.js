import Papa from 'papaparse';
// Add event listener for file input button
document.getElementById("file-input").addEventListener("change", function() {
    // Get the selected file
    var file = this.files[0];
    // Create a new FileReader object
    var reader = new FileReader();
    // Read the file as text
    reader.readAsText(file);
    // Handle the onload event
    reader.onload = function() {
        // Get the CSV data as a string
        var csvData = reader.result;
        // Parse the CSV data
        var data = Papa.parse(csvData, {
            header: true,
            dynamicTyping: true
        });
        // Iterate over the rows of data
        data.data.forEach(function(row) {
            // Create an object to store the data
            var item = {
                category: row.category,
                subcategory: row.subcategory,
                product_brand: row.product_brand,
                item_name: row.item_name,
                barcode: row.barcode,
                quantity: row.quantity,
                unit_price: row.unit_price,
                buying_price: row.buying_price
            };
            // Send the data to the server to be saved
            fetch("/api/save-item", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(item)
            })
            .then(function(response) {
                console.log("Item saved: ", item);
            })
            .catch(function(error) {
                console.error("Error saving item: ", error);
            });
        });
    };
});
