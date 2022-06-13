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

// ------------------------  Marks Dynamic Fields ------------------------- //
let addSemDetail = document.getElementById("add-marks-btn");
let marksTab = document.getElementById("marks").childNodes[3];
//  newtab goes into event listener
let newtab =
  '<div class="marks-detail">\
                <div class="row pt-2">\
                  <div class="col-6">\
                    <div class="form-group col-md-10">\
                      <label for="sem">Semester</label> <br>\
                      <select id="sem" style="height: 36px;" name="Semester">\
                        <option value="-">--</option>\
                        <option value="1">1</option>\
                        <option value="2">2</option>\
                        <option value="3">3</option>\
                        <option value="4">4</option>\
                        <option value="5">5</option>\
                        <option value="6">6</option>\
                        <option value="7">7</option>\
                        <option value="8">8</option>\
                      </select>\
                    </div>\
                  </div>\
                  <div class="col-6">\
                    <div class="form-group col-md-10">\
                      <label for="gpa">GPA</label>\
                      <input type="number" step="any" name="gpa" class="form-control" id="gpa" placeholder="GPA" value="0.0">\
                    </div>\
                  </div>\
                </div>\
                <!--  Add logic to detect number of subjects -->\
                <div class="row pt-2">\
                  <div class="col-12">\
                    <div class="form-group col-md-10">\
                      <label for="subject">Subject</label> <br>\
                      <select id="subject" style="height: 36px;" name="Subject">\
                        <option value="-">--</option>\
                        <option value="1">Sub name 1</option>\
                        <option value="2">Sub name 2</option>\
                        <option value="...">...</option>\
                      </select>\
                    </div>\
                  </div>\
                </div>\
                <div class="row pt-2 pb-4">\
                  <div class="col-4">\
                    <div class="form-group col-md-10">\
                      <input type="number" name="IA1" class="form-control" id="IA1" placeholder="IA1 marks" value="0">\
                    </div>\
                  </div>\
                  <div class="col-4">\
                    <div class="form-group col-md-10">\
                      <input type="number" name="IA2" class="form-control" id="IA2" placeholder="IA2 marks" value="0">\
                    </div>\
                  </div>\
                  <div class="col-4">\
                    <div class="form-group col-md-10">\
                      <input type="number" name="ESE" class="form-control" id="ESE" placeholder="ESE marks" value="0">\
                    </div>\
                  </div>\
                </div> \
              </div>';

addSemDetail.addEventListener("click", () => {
  // alert("You unlocked an easter egg");
  marksTab.innerHTML += newtab;
});
