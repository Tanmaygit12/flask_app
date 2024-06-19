function addToCart(productName, price, imgpath) {
    // Get or create the cart array in localStorage
    let cart = JSON.parse(localStorage.getItem('cart')) || [];

    // Check if the product is already in the cart
    let existingProduct = cart.find(item => item.name === productName);

    if (existingProduct) {
        // If product is already in the cart, update quantity
        existingProduct.quantity += 1;
    } else {
        // If product is not in the cart, add it
        cart.push({
            name: productName,
            price: price,
            quantity: 1,
            image:``    // Add image path to cart item
        });
    }

    // Save the updated cart back to localStorage
    localStorage.setItem('cart', JSON.stringify(cart));
    cartjsonadd()
    // Optionally, you can redirect to the cart page or show a success message
    alert('Product added to cart!');
    console.log(JSON.stringify(cart))
}
function cartjsonadd(productName, price, imgpath) {
  let cart = JSON.parse(localStorage.getItem("cart"));

  const jsonData = JSON.stringify(cart, null, 2); // null and 2 are for indentation

  // Step 3: Make an HTTP POST request to the Flask server
  fetch("/create_json", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: jsonData,
  })
    .then((response) => {
      if (response.ok) {
        console.log("JSON file created successfully");
        console.log(jsonData)
      } else {
        console.error("Failed to create JSON file");
      }
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}
