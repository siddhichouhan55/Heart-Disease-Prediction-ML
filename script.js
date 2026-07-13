const inputs=document.querySelectorAll("input");

inputs.forEach(input=>{

input.addEventListener("focus",()=>{

input.style.background="#eef7ff";

});

input.addEventListener("blur",()=>{

input.style.background="white";

});

});