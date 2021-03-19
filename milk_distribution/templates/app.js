const submitBtn = document.querySelector("#submit");

submitBtn.addEventListener("click", (event) => {
    event.preventDefault();
    const username = document.querySelector("#username").value;
  
    const password = document.querySelector("#Password").value;
   
    const loginDetails = {
      username,
      password,
    };

    
  for (const el of userList) {
    if (
      el.password === loginDetails.password &&
      el.username === loginDetails.username
    ) {
      console.log("verfied");
      window.location.assign("./customer1.html")
      

      
    }
  }
});



const userList = [
  {
    username: "siva",
    password: "siva",
  },
  {
    username: "saranyan",
    password: "saranyan",
  },
];