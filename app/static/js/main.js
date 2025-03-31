document.addEventListener("DOMContentLoaded", function () {
    const loadMoreButton = document.getElementById("load-more");
    const photoContainer = document.getElementById("photo-container");

    if (loadMoreButton) {
        loadMoreButton.addEventListener("click", function () {
            const nextPage = loadMoreButton.getAttribute("data-next-page");

            fetch(`?page=${nextPage}`, {
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
                                        <p class="card-text">${photo.description}</p>
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
