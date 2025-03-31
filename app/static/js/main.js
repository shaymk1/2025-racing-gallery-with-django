








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
                                <div class="card my-2">
                                    <img src="${photo.pic_url}" class="card-img-top" alt="Photo">
                                    <div class="card-body">
                                        <p class="card-text fw-bold">${photo.title}</p>
                                        <p class="card-text">Category: ${photo.category}</p>
                                        <div class="btn-toolbar" style="padding-left: 15px">
                                            <a class="btn btn-outline-dark btn-sm m-1" href="/detailed_view/${photo.id}">View</a>
                                            <a class="btn btn-warning btn-sm m-1" href="/photo/${photo.id}/edit/">Edit</a>
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










