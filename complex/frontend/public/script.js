 
let myRequest = new Request('/api/cats');

fetch(myRequest)
    .then(function (response) {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        response.json().then(function (body) {
            cats = document.getElementById('cats')
            body.forEach(cat => {
                let cat_image = document.createElement("img");
                let cat_title = document.createElement("p");
                cat_title.innerText = cat['name']
                cat_image.setAttribute("src", cat['image'])
                let cat_block = document.createElement("div");
                cat_block.appendChild(cat_title)
                cat_block.appendChild(cat_image)
                cats.appendChild(cat_block)
            });
         })
    })