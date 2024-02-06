function toggleMetaData(el) {
  var x = document.getElementById("metadata");
  if (x.style.display === "none") {
    document.getElementById("bibtex").style.display = "none"
    document.getElementById("apa").style.display = "none"
    x.style.display = "block";
    //el.innerHTML = 'Hide Metadata';
  } else {
    x.style.display = "none";
    //el.innerHTML = 'Show Metadata';
  }
} 

function toggleBibtex(el) {
  var x = document.getElementById("bibtex");
  if (x.style.display === "none") {
    document.getElementById("metadata").style.display = "none"
    document.getElementById("apa").style.display = "none"
    x.style.display = "block";
    //el.innerHTML = 'Hide Metadata';
  } else {
    x.style.display = "none";
    //el.innerHTML = 'Show Metadata';
  }
}

function toggleApa(el) {
  var x = document.getElementById("apa");
  if (x.style.display === "none") {
    document.getElementById("bibtex").style.display = "none"
    document.getElementById("metadata").style.display = "none"
    x.style.display = "block";
    //el.innerHTML = 'Hide Metadata';
  } else {
    x.style.display = "none";
    //el.innerHTML = 'Show Metadata';
  }
}
