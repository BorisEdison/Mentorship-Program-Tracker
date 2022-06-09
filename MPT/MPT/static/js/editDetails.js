//  ------------------- Edit profile in student dash ---------------------- //
let editLink = document.getElementsByName("edit-link");
let editBody = document.getElementsByName("edit-body");
let options = {
  threshold: 0.6,
};
const observer = new IntersectionObserver((entries, observer) => {
  entries.forEach((entry) => {
    if (!entry.isIntersecting) {
      return;
    }
    editLink.forEach((e) => {
        e.classList.add("active");
      if (e.getAttribute("href") != "#" + entry.target.id) {
        e.classList.remove("active");
      }
    });

  });
}, options);
editBody.forEach((elem) => {
  observer.observe(elem);
});
