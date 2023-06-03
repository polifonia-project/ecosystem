function toggleMetaData(el) {
  var x = document.getElementById("schema");
  if (x.style.display === "none") {
    x.style.display = "block";
    el.innerHTML = 'Hide Metadata';
  } else {
    x.style.display = "none";
    el.innerHTML = 'Show Metadata';
  }
} 
