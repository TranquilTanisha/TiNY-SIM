let k = 0;
function toggle() {
  if (k == 0) {
    document.documentElement.classList.add("afterupload");
    const test = document.getElementById("uploadedimgcontainer");
    test.innerHTML = '<img id="uploadedimg" src="test2.png">';
    test.style.display = "unset";
    k++;
  } else {
    document.documentElement.classList.add("afterupload");
    const test = document.getElementById("uploadedimgcontainer");
    test.innerHTML = '<img id="uploadedimg" src="test3.png">';
    test.style.display = "unset";
    k--;
  }
}

function switchE() {
  document.getElementById("encode-form").style.display = "unset";
  document.getElementById("decode-form").style.display = "none";
}

function switchD() {
  document.getElementById("encode-form").style.display = "none";
  document.getElementById("decode-form").style.display = "unset";
}

const button = document.getElementById("uploadedimgcontainer");
