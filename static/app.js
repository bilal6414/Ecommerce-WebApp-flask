$(document).ready(function () {
    // Load product data and display in the content area
    $('#show-data-link, #show-data-link-sidebar').click(function () {
        $.get('/products', function (data) {
            let content = `
                <h2>Product List</h2>
                <table class="table table-striped table-hover">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Name</th>
                            <th>Description</th>
                            <th>Price</th>
                            <th>Rating</th>
                        </tr>
                    </thead>
                    <tbody>`;
            data = JSON.parse(data);
            data.forEach(product => {
                content += `
                    <tr>
                        <td>${product.pid}</td>
                        <td>${product.name}</td>
                        <td>${product.description}</td>
                        <td>${product.price}</td>
                        <td>${product.rating}</td>
                    </tr>`;
            });
            content += `</tbody></table>`;
            $('#content').html(content);
        });
    });

    // Show the add product modal
    $('#add-product-link, #add-product-link-sidebar').click(function () {
        $('#addProductModal').modal('show');
    });

    // Handle Add Product form submission
    $('#addProductForm').submit(function (e) {
        e.preventDefault();
        const product = {
            pid: $('#pid').val(),
            name: $('#name').val(),
            description: $('#description').val(),
            price: $('#price').val(),
            rating: $('#rating').val()
        };

        $.ajax({
            url: '/products',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(product),
            success: function () {
                alert('Product added successfully!');
                $('#addProductModal').modal('hide');
                $('#show-data-link').trigger('click');
            },
            error: function () {
                alert('Error adding product.');
            }
        });
    });

    // Show the update rating modal
    $('#update-rating-link, #update-rating-link-sidebar').click(function () {
        let updateForm = `
            <h2>Update Product Rating</h2>
            <form id="updateRatingForm">
                <div class="form-group mb-3">
                    <label for="updatePid">Product ID</label>
                    <input type="text" class="form-control" id="updatePid" required>
                </div>
                <div class="form-group mb-3">
                    <label for="newRating">New Rating</label>
                    <input type="number" class="form-control" id="newRating" max="5" required>
                </div>
                <button type="submit" class="btn btn-primary">Update Rating</button>
            </form>`;
        $('#content').html(updateForm);
    });

    // Handle Update Rating form submission
    $(document).on('submit', '#updateRatingForm', function (e) {
        e.preventDefault();
        const product = {
            pid: $('#updatePid').val(),
            rating: $('#newRating').val()
        };

        $.ajax({
            url: '/products',
            type: 'PATCH',
            contentType: 'application/json',
            data: JSON.stringify(product),
            success: function () {
                alert('Rating updated successfully!');
                $('#show-data-link').trigger('click');
            },
            error: function () {
                alert('Error updating rating.');
            }
        });
    });

    // Show the delete product modal
    $('#delete-record-link, #delete-record-link-sidebar').click(function () {
        let deleteForm = `
            <h2>Delete Product</h2>
            <form id="deleteProductForm">
                <div class="form-group mb-3">
                    <label for="deletePid">Product ID</label>
                    <input type="text" class="form-control" id="deletePid" required>
                </div>
                <button type="submit" class="btn btn-danger">Delete Product</button>
            </form>`;
        $('#content').html(deleteForm);
    });

    // Handle Delete Product form submission
    $(document).on('submit', '#deleteProductForm', function (e) {
        e.preventDefault();
        const product = {
            pid: $('#deletePid').val()
        };

        $.ajax({
            url: '/products',
            type: 'DELETE',
            contentType: 'application/json',
            data: JSON.stringify(product),
            success: function () {
                alert('Product deleted successfully!');
                $('#show-data-link').trigger('click');
            },
            error: function () {
                alert('Error deleting product.');
            }
        });
    });

    // Navigate back to home page when Home link is clicked
    $('#home-link, #home-link-sidebar').click(function () {
        $('#content').html(`
            <h1 class="mt-4">Welcome to E-commerce Web Application</h1>
            <p class="lead">
                This is a class project developed using Flask and Pandas. The goal is to create an e-commerce application where users can manage products.
                The project includes:
            </p>
            <ul>
                <li>Displaying product data</li>
                <li>Adding new products</li>
                <li>Updating product ratings</li>
                <li>Deleting products</li>
            </ul>

        `);
    });

    // Initially load home page content
    $('#home-link').trigger('click');
});
