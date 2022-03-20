let count_log = document.querySelector("#activity-list>tbody").childElementCount-1;
let count_user = document.querySelector("#user-list>tbody").childElementCount-1;
let numberOfItemsPerPage = 3;
let pageno=3;
console.log(count_log);
console.log(count_user);
console.log(numberOfItemsPerPage);
console.log(getPaginationText(count_log,numberOfItemsPerPage,pageno));
function getPaginationText(totalItemsCount, numberOfItemsPerPage, page) {
    // var pageCount = (totalItemsCount - 1) / numberOfItemsPerPage + 1;
    let start = (page - 1) * numberOfItemsPerPage + 1;
    let end = Math.min(start + numberOfItemsPerPage - 1, totalItemsCount);
  
    return `${start}-${end} of ${totalItemsCount}`;
  }

const modal = document.querySelector("#modal");
const openModal = document.querySelector(".open-button");
const closeModal = document.querySelector(".close-button");

openModal.addEventListener("click", () => {
  modal.showModal();
});

closeModal.addEventListener("click", () => {
  modal.close();
});
