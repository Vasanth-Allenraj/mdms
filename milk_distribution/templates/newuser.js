const submitBtn = document.querySelector("#submit");

submitBtn.addEventListener("click", (event) => {
    event.preventDefault();

    const firstname = document.querySelector("#firstname").value;
    const lastname = document.querySelector("#lastname").value;
    const email = document.querySelector("#inputEmail4").value;
    const password = document.querySelector("#inputPassword4").value;
    const address1 = document.querySelector("#inputAddress").value;
    const address2 = document.querySelector("#inputAddress2").value;
    const city = document.querySelector("#inputCity").value;
    const states = document.querySelector("#inputState").value;
    const zip = document.querySelector("#inputZip").value;

    console.log(firstname,lastname,email,password,address1,address2,city,states,zip);  
    
});


