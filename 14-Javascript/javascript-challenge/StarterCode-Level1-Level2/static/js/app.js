// from data.js
var tableData = data;
console.log(tableData);

// table display
var tbody = d3.select("tbody");
tableData.forEach((UFOSighting) => {
  var row = tbody.append("tr");
  Object.entries(UFOSighting).forEach(([key, value]) => {
    var cell = tbody.append("td");
    cell.text(value);
  });
});

// drop down city select
var cityList = d3.select("#city");
cityList.append("option").text("-Select City-");
var cityGroup = [];
tableData.forEach((UFOSighting) => {
  if (cityGroup.includes(UFOSighting.city) === false) {
    cityGroup.push(UFOSighting.city);
    cityList.append("option").text(UFOSighting.city);
  }
});

// drop down state select
var stateList = d3.select("#state");
stateList.append("option").text("-Select State-");
var stateGroup = [];
tableData.forEach((UFOSighting) => {
  if (stateGroup.includes(UFOSighting.state) === false) {
    stateGroup.push(UFOSighting.state);
    stateList.append("option").text(UFOSighting.state);
  }
});

// drop down country select
var countryList = d3.select("#country");
countryList.append("option").text("-Select Country-");
var countryGroup = [];
tableData.forEach((UFOSighting) => {
  if (countryGroup.includes(UFOSighting.country) === false) {
    countryGroup.push(UFOSighting.country);
    countryList.append("option").text(UFOSighting.country);
  }
});

// drop down shape select
var shapeList = d3.select("#shape");
shapeList.append("option").text("-Select Shape-");
var shapeGroup = [];
tableData.forEach((UFOSighting) => {
  if (shapeGroup.includes(UFOSighting.shape) === false) {
    shapeGroup.push(UFOSighting.shape);
    shapeList.append("option").text(UFOSighting.shape);
  }
});

// date filter
var filterButton = d3.select("#filter-btn");

// filter btn
filterButton.on("click", function () {
  d3.event.preventDefault();
  tbody.html("");

  // date input
  var inputElementDate = d3.select("#datetime");
  var inputValueDate = inputElementDate.property("value");
  console.log(inputValueDate);

  // city input
  var inputElementCity = d3.select("#city");
  var inputValueCity = inputElementCity.property("value");

  // statue input
  var inputElementState = d3.select("#state");
  var inputValueState = inputElementState.property("value");

  // country input
  var inputElementCountry = d3.select("#country");
  var inputValueCountry = inputElementCountry.property("value");

  // shape input
  var inputElementShape = d3.select("#shape");
  var inputValueShape = inputElementShape.property("value");

  // date filter

  if (inputValueDate) {
    var filteredDate = tableData.filter(
      (UFOSighting) => UFOSighting.datetime === inputValueDate
    );
  } else {
    filteredDate = tableData;
  }

  // Filter City
  if (inputValueCity != "-Select City-") {
    var filteredLocation = filteredDate.filter(
      (UFOSighting) => UFOSighting.city === inputValueCity
    );
  } else if (inputValueState != "-Select State-") {
    var filteredLocation = filteredDate.filter(
      (UFOSighting) => UFOSighting.state === inputValueState
    );
  } else if (inputValueCountry != "-Select Country-") {
    var filteredLocation = filteredDate.filter(
      (UFOSighting) => UFOSighting.country === inputValueCountry
    );
  } else {
    filteredLocation = filteredDate;
  }

  //Filter Shape
  if (inputValueShape != "-Select Shape-") {
    var filteredData = filteredLocation.filter(
      (UFOSighting) => UFOSighting.shape === inputValueShape
    );
  } else {
    filteredData = filteredLocation;
  }

  // Display filtered results
  filteredData.forEach((UFOSighting) => {
    var row = tbody.append("tr");
    Object.entries(UFOSighting).forEach(([key, value]) => {
      var cell = tbody.append("td");
      cell.text(value);
    });
  });
});
