var page = 1;
var isLoading = false;

function fetchItems() {
  isLoading = true;

  // Simulamos una llamada a una API para obtener nuevos elementos
  setTimeout(function() {
    var itemsContainer = document.getElementById("content");

    for (var i = 1; i <= 10; i++) {
      var newItem = document.createElement("div");
      newItem.classList.add("item");
      newItem.innerHTML = "Elemento " + ((page - 1) * 10 + i);
      itemsContainer.appendChild(newItem);
    }

    isLoading = false;
  }, 1000);
}

function handleScroll() {
  var scrollPosition = window.innerHeight + window.scrollY;
  var contentHeight = document.body.offsetHeight;

  if (scrollPosition >= contentHeight && !isLoading) {
    page++;
    fetchItems();
  }
}

window.addEventListener("scroll", handleScroll);

// Cargar elementos iniciales
fetchItems();
