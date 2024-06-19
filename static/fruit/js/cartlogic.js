function addToCart(productName, price, imagePath) {
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
            image:` `    // Add image path to cart item
        });
    }

    // Save the updated cart back to localStorage
    localStorage.setItem('cart', JSON.stringify(cart));

    // Optionally, you can redirect to the cart page or show a success message
    alert('Product added to cart!');
}