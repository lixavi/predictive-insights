$(document).ready(function() {
    const API_KEY = 'e1eefa54';
    const API_URL = 'https://www.omdbapi.com/';
    let currentPage = 1;

    $('#search-form').submit(function(e) {
        e.preventDefault();
        searchMovies();
    });

    $('#load-more-btn').on('click', function() {
        currentPage++;
        searchMovies();
    });

    function searchMovies() {
        const searchQuery = $('#search-input').val().trim();
        const requestURL = `${API_URL}?apikey=${API_KEY}&s=${encodeURIComponent(searchQuery)}&page=${currentPage}`;

        $.ajax({
            url: requestURL,
            method: 'GET',
            dataType: 'json',
            success: function(data) {
                if (data.Response === 'True') {
                    displayMovieResults(data.Search);
                } else {
                    displayErrorMessage(data.Error);
                }
            },
            error: function(xhr, status, error) {
                console.log(error);
                displayErrorMessage('An error occurred while fetching movie data.');
            }
        });
    }

    function displayMovieResults(movies) {
        console.log(movies);
        // Clear previous results if it's the first page
        if (currentPage === 1) {
            $('#movie-results').empty();
        }
    
        // Loop through the movies array and display movie information
        movies.forEach(function(movie) {
            const movieHTML = `
                <div class="movie">
                    <img src="${movie.Poster}" alt="${movie.Title}">
                    <h3>${movie.Title}</h3>
                    <p>Year: ${movie.Year}</p>
                    ${movie.imdbRating ? `<p>IMDb Rating: ${movie.imdbRating}</p>` : ''}
                </div>
            `;
            $('#movie-results').append(movieHTML);
        });
    
        // Show the Load More button if there are more results
        if (movies.length >= 8) {
            $('#load-more-btn').show();
        } else {
            $('#load-more-btn').hide();
        }
    }

    function displayErrorMessage(message) {
        // Display an error message to the user
        $('#movie-results').html(`<p class="error-message">${message}</p>`);
    }
});
