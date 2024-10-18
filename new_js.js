const products = [
    {
        id: 1,
        name: " Jordan",
        Image: "https://res.cloudinary.com/dzwspepvg/image/upload/v1708052266/products/hcfe2ltm38xf3hozthf7.png",
        description: "Description 1",
        color: "red",
        category: "sketcher",
        price: 1000,
    },
    {
        id: 2,
        name: "Nike",
        Image: "https://res.cloudinary.com/dzwspepvg/image/upload/v1708055564/products/tlklunsunrn2kwodl5qx.png",
        description: "Description 2",
        color: "blue",
        category: "sketcher",
        price: 2000,
    },
    {
        id: 3,
        name: "Adidas",
        Image: "https://res.cloudinary.com/dzwspepvg/image/upload/v1708052266/products/hcfe2ltm38xf3hozthf7.png",
        description: "Description 3",
        color: "green",
        category: "paety",
        price: 3000,
    },
    {
        id: 4,
        name: "Spike",
        Image: "https://res.cloudinary.com/dzwspepvg/image/upload/v1708055564/products/tlklunsunrn2kwodl5qx.png",
        description: "Description 4",
        color: "red",
        category: "traditional",
        price: 4000,
    },
    {
        id: 5,
        name: "Balenciaga",
        Image: "https://res.cloudinary.com/dzwspepvg/image/upload/v1708052266/products/hcfe2ltm38xf3hozthf7.png",
        description: "Description 5",
        color: "blue",
        category: "running",
        price: 5000,
    },
    {
        id: 6,
        name: "Bata",
        Image: "https://res.cloudinary.com/dzwspepvg/image/upload/v1708055564/products/tlklunsunrn2kwodl5qx.png",
        description: "Description 6",
        color: "green",
        category: "shoes",
        price: 6000,
    },
    {
        id: 7,
        name: "Everlast",
        Image: "https://res.cloudinary.com/dzwspepvg/image/upload/v1708052266/products/hcfe2ltm38xf3hozthf7.png",
        description: "Description 7",
        color: "black",
        category: "shoes",
        price: 7000,
    },
    {
        id: 8,
        name: "Hush Puppies",
        Image: "https://res.cloudinary.com/dzwspepvg/image/upload/v1708055564/products/tlklunsunrn2kwodl5qx.png",
        description: "Description 8",
        color: "white",
        category: "shoes",
        price: 8000,
    },
    {
        id: 9,
        name: "Hrx",
        Image: "https://res.cloudinary.com/dzwspepvg/image/upload/v1708052266/products/hcfe2ltm38xf3hozthf7.png",
        description: "Description 9",
        color: "black",
        category: "shoes",
        price: 9000,
    },
    {
        id: 10,
        name: "Skechers",
        Image: "https://res.cloudinary.com/dzwspepvg/image/upload/v1708055564/products/tlklunsunrn2kwodl5qx.png",
        description: "Description 10",
        color: "white",
        category: "shoes",
        price: 10000,
    },
    {
        id: 10,
        name: "Skechers",
        Image: "https://res.cloudinary.com/dzwspepvg/image/upload/v1708055564/products/tlklunsunrn2kwodl5qx.png",
        description: "Description 10",
        color: "white",
        category: "shoes",
        price: 10000,
    },
    {
        id: 10,
        name: "Skechers",
        Image: "https://res.cloudinary.com/dzwspepvg/image/upload/v1708055564/products/tlklunsunrn2kwodl5qx.png",
        description: "Description 10",
        color: "white",
        category: "shoes",
        price: 10000,
    },
    {
        id: 10,
        name: "Skechers",
        Image: "https://res.cloudinary.com/dzwspepvg/image/upload/v1708055564/products/tlklunsunrn2kwodl5qx.png",
        description: "Description 10",
        color: "white",
        category: "shoes",
        price: 10000,
    },
    {
        id: 10,
        name: "Skechers",
        Image: "https://res.cloudinary.com/dzwspepvg/image/upload/v1708055564/products/tlklunsunrn2kwodl5qx.png",
        description: "Description 10",
        color: "white",
        category: "shoes",
        price: 10000,
    },
]
// --------Render Products-------------
function renderProducts(data){
    const cards = document.querySelector(".cards");
    cards.innerHTML = '';
    data.forEach(element => {
        // console.log(element);
        const card = document.createElement("div")
        card.classList.add("card");
        card.innerHTML = `
          <img src="${element.Image}" alt="Shoes" class="card_img">
                <p class="p_name">${element.name}</p>
                
                <input type="number" class="p_quantity" min="0"  step="1" placeholder="Qty">
                <p class="p_price">$ ${element.price}</p>
                <button class="add_chart">Add to Chart</button>`
        cards.append(card)
    });


}
renderProducts(products);

// ----------color------------
function colorRender(uniqueColors){
    console.log(uniqueColors);
    const colorList = document.getElementById("color");
    // colorList.innerHTML = '';
    uniqueColors.forEach(color => {
        const colorOption = document.createElement("option");
        colorOption.classList.add("color_option");
        colorOption.value = color;
        colorOption.textContent = color;
        colorList.append(colorOption);
        
    })
    colorList.addEventListener('change',(opt)=>{
        const selectedColor = opt.target.value;
        console.log(selectedColor);  
        if(selectedColor === "All"){
            renderProducts(products);
            return;
        }
        const filteredProducts = products.filter((item)=>{
            return item.color === selectedColor;
        })
        renderProducts(filteredProducts);

    })
    
}
const colors = products.map((item)=>{
    return item.color;
    
})
const uniqueColors = [... new Set(colors)]


// -----------------------category---------------
function categoryRender(uniqueCategory){
    console.log(uniqueCategory);
    const categoryList = document.getElementById("categories");
    uniqueCategory.forEach((cate)=>{
        const categoryOption = document.createElement("option");
        categoryOption.classList.add("category_option");
        categoryOption.value = cate;
        categoryOption.textContent = cate;
        categoryList.append(categoryOption);
        // categoryList.append(categoryOption);
    })
    categoryList.addEventListener("change",(opt)=>{
        const selectedCategory = opt.target.value;
        if(selectedCategory === "All"){
            renderProducts(products);
            return;
        }
        const filteredProducts = products.filter((items)=>{
            return items.category === selectedCategory;
        })
        renderProducts(filteredProducts);
    })
}
const categorys = products.map((item)=>{
    return item.category;
})
// console.log(categorys);
const uniqueCategory = [...new Set(categorys)];
// console.log(uniqueCategory);



// ------------sort--------------

const sortList = document.getElementById("sort");
const sortArray = [
    {
        id: 1,
        price: "Low to High"
    },
    {
        id: 2,
        price: "High to Low"
    }
]
sortArray.forEach((item)=>{
    const sortOption = document.createElement("option")
    sortOption.classList.add("sort_option");
    sortOption.value=item.price;
    sortOption.textContent=item.price;
    sortList.append(sortOption);

})
sortList.addEventListener("change",(opt)=>{
    console.log(opt);
    
    const selectedSort = opt.target.value;
    if(selectedSort === "All"){
        renderProducts(products);
        return;
    }
    const filteredProducts = products.sort((a,b)=>{
        if(selectedSort == "Low to High"){
            return a.price - b.price;

        }
        else if(selectedSort == "High to Low"){
            return b.price - a.price;
        }
    })
    renderProducts(filteredProducts);

})

// -----------------------search input------------------ 
const searchInput = document.querySelector(".search_inp");
searchInput.addEventListener("keyup",(event)=>{
    const searchValue = event.target.value;
    console.log(searchValue);
    const filteredProducts = products.filter((product)=>{
        return product.name.toLowerCase().includes(searchValue.toLowerCase());
    })
    renderProducts(filteredProducts);
    
    
})
// price-filter
// const priceFilter = document.getElementsByClassName("filter_max_price_ul")
const priceFilter = document.querySelector(".filter_max_price_ul")

function renderPriceFilter(priceRanges) {
    console.log(priceRanges);
    
 priceFilter.innerHTML = "";
 
 priceRanges.forEach((range) => {
     const button = document.createElement("li")
     button.classList.add("filter_max_price_ul_li");
     button.textContent = range.range
     // button.classList.add("filter-button")
     button.addEventListener("click", (e) => {
         const selectedPrice = e.target.textContent
         let price1 = 0
         let price2 = 0
        if(selectedPrice.includes("and")){
            price1 = Number(selectedPrice.split("and")[0])
            price2 = maxPrice         
        }
        else{
            price1 = Number(selectedPrice.split("-")[0])
            price2 = Number(selectedPrice.split("-")[1])
        }
        console.log(price1 ,price2)
        const filteredProducts = products.filter((product) => {
            return product.price <= price2 && product.price >= price1
        })
        renderProducts(filteredProducts)
    })
    priceFilter.append(button);
    // console.log("yes");
})
}

const maxPrice = products.reduce((max, product) => Math.max(max, product.price), 0);
console.log(maxPrice);

const priceRanges = [
    { id: 1, range: `0 - ${Math.floor(maxPrice / 4)}` },
    { id: 2, range: `${Math.floor(maxPrice / 4)} - ${Math.floor(maxPrice / 2)}` },
    { id: 3, range: `${Math.floor(maxPrice / 2)} - ${Math.floor((3 * maxPrice) / 4)}` },
    { id: 4, range: `${Math.floor((3 * maxPrice) / 4)} and above` }
];



// ---------------------recive img - post at box-----------------

const add_img =document.querySelector(".add_img")
const add_img_box =document.querySelector(".add_img_box")

add_img.addEventListener('change', (event) => {
    const file = event.target.files[0];
    console.dir(event.target.value);

    if (file) {
        const reader = new FileReader();

        reader.onload = (e) => {
            add_img_box.src = e.target.result;
            console.dir(e.target)
            console.log(e.target.value);
            console.log(e.target.src);
            console.log(e.target.result);

            // imagePreview.style.display = 'block'; // Show the image
        };

        reader.readAsDataURL(file); // Read the file as a data URL
    }
});


// add_img.addEventListener('change',(btn)=>{
//     console.log(btn.target.value);
//     add_img_box.src = '';
//     add_img_box.src = btn.target.value;

//     console.log('yes');
    
// })

// --------------Function Call----------    
colorRender(uniqueColors);
categoryRender(uniqueCategory);
renderPriceFilter(priceRanges)




const root = document.querySelector(".root")
const mode_btn = document.querySelector(".mode_icon");
const nav = document.querySelector("nav");
const side_bar = document.querySelector(".side_bar");
const search = document.querySelector(".search");
const card = document.querySelectorAll(".card");
const cards = document.querySelector(".cards");
const dark_mode = document.querySelector(".dark_mode");
const light_mode = document.querySelector(".light_mode");
const color_option = document.querySelectorAll(".color_option");
const color_select = document.getElementById("color")
const categories_select = document.getElementById("categories")
const filter_tgl = document.querySelector(".li0")
const add_product_btn = document.querySelector(".add_product")
const add_product_page = document.querySelector(".add_pro_page")
const close_add_product_page = document.querySelector(".close_add_product_page")
const close_chart = document.querySelector(".close_chart")
const main_root =document.querySelector(".main_root")
const chart_page =document.querySelector(".chart_page")
const chart_btn =document.querySelector(".li2")
const chart_footer =document.querySelector(".chart_footer")
// const light_i = document.querySelector(".light_i")
// const dark_i = document.querySelector(".dark_i")
let dark = false;
let tgl = false;
let chart = false;
let add = false;
// --main-bg-color:#f6f7fa;
// --main2-bg-color:#3a5061;
// --main-font-color:#ffffff;
mode_btn.addEventListener("click", function () {
    console.log(root);

    if (!dark) {
        root.style.background = '';
        nav.style.background = '#000';
        side_bar.style.background = '#000';
        dark_mode.style.background = '#000';
        light_mode.style.background ='transparent';
        add_product_btn.style.background='#000';
        chart_footer.style.background='#000';
        // search.style.background = '#000';
        card.forEach(function (card) {
            card.style.background = '';
        });
        // dark_i.style.visibility = 'hidden';
        // light_i.style.visibility = 'visible';
        
        
        dark = true;
        
    } else if(dark){
        root.style.background = '#f6f7fa';
        nav.style.background = '#3a5061';
        side_bar.style.background = '#3a5061';
        search.style.background = '';
        dark_mode.style.background = 'transparent';
        light_mode.style.background = '#3a5061';
        card.forEach(function (card) {
            card.style.background = '';
        });
        add_product_btn.style.background='#3a5061';
        chart_footer.style.background='#3a5061';
        // dark_i.style.visibility = 'visible';
        // light_i.style.visibility = 'hidden';
        dark = false;
    }
});
filter_tgl.addEventListener('click',()=>{
    if(!tgl){
        side_bar.style.visibility='visible';
        tgl=true;
    }
    else if(tgl){

       
        side_bar.style.visibility='hidden';
        tgl=false;

    }
})
chart_btn.addEventListener('click',()=>{
    if(!chart){
        chart_page.style.display='block';
        main_root.style.display='none';
        add_product_page.style.display='none';
        add=false
        chart=true;
    }
    else if(chart){
        
        
        chart_page.style.display='none';
        main_root.style.display='flex';
        
        chart=false;

    }
})
close_chart.addEventListener('click',()=>{
  
    if(chart){
       
       
       chart_page.style.display='none';
       main_root.style.display='flex';
       
       chart=false;

   }
})



// ----------------------------------add product--------------------
add_product_btn.addEventListener('click',()=>{
    if(!add){
        main_root.style.display='none';
        chart_page.style.display='none';
        add_product_page.style.display='flex';
        add=true;
    }
   
})

close_add_product_page.addEventListener('click',()=>{
  d
     if(add){
        
        
        add_product_page.style.display='none';
        main_root.style.display='flex';
        add_img_box.src="https://res.cloudinary.com/dzwspepvg/image/upload/v1708055564/products/tlklunsunrn2kwodl5qx.png   ";
        
        add=false;

    }
})
