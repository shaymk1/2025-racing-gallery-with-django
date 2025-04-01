

document.addEventListener("DOMContentLoaded", function () {
    const loadMoreButton = document.getElementById("load-more");
    const photoContainer = document.getElementById("photo-container");
    const categoryFilter = document.getElementById("category-filter");

    // Handle category filter change
    categoryFilter.addEventListener("change", function () {
        const selectedCategory = categoryFilter.value;
        if (selectedCategory === "all") {
            // Redirect to the home page without any category filter
            window.location.href = "/";
        } else {
            // Redirect with the selected category filter
            window.location.href = `?category=${selectedCategory}`;
        }
    });

    // Handle Load More button click
    if (loadMoreButton) {
        loadMoreButton.addEventListener("click", function () {
            const nextPage = loadMoreButton.getAttribute("data-next-page");
            const category = loadMoreButton.getAttribute("data-category");

            fetch(`?page=${nextPage}&category=${category}`, {
                headers: {
                    "X-Requested-With": "XMLHttpRequest",
                },
            })
                .then((response) => response.json())
                .then((data) => {
                    // Append new photos to the container
                    data.photos.forEach((photo) => {
                        const photoHTML = `
                            <div class="col-md-4 mb-4">
                                <div class="card">
                                    <img src="${photo.pic_url}" class="card-img-top" alt="Photo">
                                    <div class="card-body">
                                        <p class="card-text fw-bold">${photo.title}</p>
                                        <p class="card-text">Category: ${photo.category}</p>
                                        <div class="btn-toolbar" style="padding-left: 15px">
                                            <a class="btn btn-outline-dark btn-sm m-1" href="/detailed_view/${photo.id}">View</a>
                                            <a class="btn btn-warning btn-sm m-1" href="/photo/${photo.id}/edit/">Edit</a>
                                            <a class="btn btn-danger btn-sm m-1" href="/delete_photo/${photo.id}">Delete</a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        `;
                        photoContainer.insertAdjacentHTML("beforeend", photoHTML);
                    });

                    // Update or remove the "Load More" button
                    if (data.has_next) {
                        loadMoreButton.setAttribute("data-next-page", parseInt(nextPage) + 1);
                    } else {
                        loadMoreButton.remove();
                    }
                })
                .catch((error) => console.error("Error loading more photos:", error));
        });
    }
});