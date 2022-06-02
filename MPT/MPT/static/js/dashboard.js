let btns = document.getElementsByName("btn-show");
let cbs = document.getElementsByName("cb-choose");
let btn_select = document.getElementById("btn-select");

let btn_sel_all = document.getElementById("sel-all-btn");
let btn_cancel = document.getElementById("cancel-btn");
let btn_schedule = document.getElementById("schedule-btn");

const btn_status = (status) => {
//   console.log("Hello");
  btns.forEach((btn) => {
    btn.style.opacity = status ? "0" : "1";
  });
  cbs.forEach((cb) => {
    cb.style.opacity = status ? "0" : "1";
  });
  btn_sel_all.disabled = status;
  btn_cancel.disabled = status;
  btn_schedule.disabled = status;
};
// console.log('hey');
btn_status(true);
btn_select.addEventListener("click", () => {
  btn_status(false);
});

btn_sel_all.addEventListener("click", () => {
  cbs.forEach((cb) => {
    cb.checked = true;
  });
});

btn_cancel.addEventListener("click", () => {
  btn_status(true);
  cbs.forEach((cb) => {
    cb.checked = false;
  });
});

btn_schedule.addEventListener("click", () => {
  alert("Get some stuff done!!!");
  btn_status(true);
  cbs.forEach((cb) => {
    cb.checked = false;
  });
});
