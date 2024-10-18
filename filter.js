
const root = document.querySelector(".root")
// const mode_btn = document.querySelector(".mode_icon");
const n = document.querySelector(".nav");
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
// mode_btn.addEventListener("click", function () {
    

//     if (!dark) {
//         root.style.background = '';
//         n.style.background = '#000';
//         side_bar.style.background = '#000';
//         dark_mode.style.background = '#000';
//         light_mode.style.background ='transparent';
//         add_product_btn.style.background='#000';
//         chart_footer.style.backgroud='#000';
//         // search.style.background = '#000';
//         card.forEach(function (card) {
//             card.style.background = '';
//         });
//         // dark_i.style.visibility = 'hidden';
//         // light_i.style.visibility = 'visible';
        
        
//         dark = true;
        
//     } 
//     if(dark == true){
//         console.log("dark mode of");
        
//         root.style.background = '#f6f7fa';
//         n.style.background = '#3a5061';
//         side_bar.style.background = '#3a5061';
//         search.style.background = '';
//         dark_mode.style.background = 'transparent';
//         light_mode.style.background = '#3a5061';
//         card.forEach(function (card) {
//             card.style.background = '';
//         });
//         add_product_btn.style.background='#3a5061';
//         chart_footer.style.background='#3a5061';
//         // dark_i.style.visibility = 'visible';
//         // light_i.style.visibility = 'hidden';
//         dark = false;
//     }
// });
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
  
     if(add){
        
        
        add_product_page.style.display='none';
        main_root.style.display='flex';
        add_img_box.src="https://res.cloudinary.com/dzwspepvg/image/upload/v1708055564/products/tlklunsunrn2kwodl5qx.png   ";
        
        add=false;

    }
})
