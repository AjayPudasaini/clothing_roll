document.addEventListener("DOMContentLoaded", function () {
    window.addEventListener("scroll", function () {
      if (window.scrollY > 50) {
        document.getElementById("navbar_top").classList.add("fixed-top");
        // add padding top to show content behind navbar
        navbar_height = document.querySelector(".navbars").offsetHeight;
        document.body.style.paddingTop = navbar_height + "px";
      } else {
        document.getElementById("navbar_top").classList.remove("fixed-top");
        // remove padding top from body
        document.body.style.paddingTop = "0";
      }
    });
  });
  
  const searchIcon = document.querySelector(".search-icon");
  const searchForm = document.querySelector(".search-form-small");
  
  searchIcon.addEventListener("click", () => {
    // searchIcon.innerHTML = '<i class="fas fa-times-circle"></i>'
    searchForm.classList.toggle("change");
  });
  
  // category slider
  
  let prev = document.getElementById('left');
  
  let product_prev = document.getElementById('product_left');
  
  let next = document.getElementById('right');
  
  let product_next = document.getElementById('product_right');
  
  const slider = document.getElementById('slider');
  const product_slider = document.getElementById('product_slider');
  
  prev.addEventListener("click", () => {
    slider.scrollLeft -= 195
  });
  
  next.addEventListener("click", () => {
    slider.scrollLeft += 195
  });
  
  
  product_prev.addEventListener("click", () => {
    product_slider.scrollLeft -= 280
  });
  
  product_next.addEventListener("click", () => {
    product_slider.scrollLeft += 280
  });
  
  