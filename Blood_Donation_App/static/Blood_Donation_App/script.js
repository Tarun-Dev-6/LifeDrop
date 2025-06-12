// Main JavaScript functionality for Blood Donation App

// Global variables
// let donors = [];

// State to Cities mapping
const stateCityMapping = {
  "Andhra Pradesh": [
    "Bhimavaram",
    "Visakhapatnam",
    "Vijayawada",
    "Guntur",
    "Nellore",
    "Kurnool",
    "Tirupati",
    "Rajahmundry",
    "Kadapa",
  ],
  Bihar: [
    "Patna",
    "Gaya",
    "Bhagalpur",
    "Muzaffarpur",
    "Purnia",
    "Darbhanga",
    "Bihar Sharif",
    "Arrah",
  ],
  Delhi: [
    "New Delhi",
    "Central Delhi",
    "North Delhi",
    "South Delhi",
    "East Delhi",
    "West Delhi",
    "North East Delhi",
    "North West Delhi",
    "South East Delhi",
    "South West Delhi",
    "Shahdara",
  ],
  Gujarat: [
    "Ahmedabad",
    "Surat",
    "Vadodara",
    "Rajkot",
    "Bhavnagar",
    "Jamnagar",
    "Gandhinagar",
    "Anand",
  ],
  Karnataka: [
    "Bangalore",
    "Mysore",
    "Hubli",
    "Mangalore",
    "Belgaum",
    "Gulbarga",
    "Shimoga",
    "Tumkur",
  ],
  Kerala: [
    "Thiruvananthapuram",
    "Kochi",
    "Kozhikode",
    "Thrissur",
    "Kollam",
    "Palakkad",
    "Alappuzha",
    "Kannur",
  ],
  Maharashtra: [
    "Mumbai",
    "Pune",
    "Nagpur",
    "Nashik",
    "Aurangabad",
    "Solapur",
    "Kolhapur",
    "Sangli",
  ],
  Punjab: [
    "Ludhiana",
    "Amritsar",
    "Jalandhar",
    "Patiala",
    "Bathinda",
    "Mohali",
    "Firozpur",
    "Hoshiarpur",
  ],
  "Tamil Nadu": [
    "Chennai",
    "Coimbatore",
    "Madurai",
    "Tiruchirappalli",
    "Salem",
    "Erode",
    "Tirunelveli",
    "Vellore",
  ],
  "Uttar Pradesh": [
    "Lucknow",
    "Kanpur",
    "Ghaziabad",
    "Agra",
    "Meerut",
    "Varanasi",
    "Allahabad",
    "Bareilly",
  ],
};

// Initialize app
document.addEventListener("DOMContentLoaded", function () {
  // loadDonors();
  // setupEventListeners();
  setupStateCityHandlers();
});


// Load mock donor data
// function loadDonors() {
//   const mockDonors = [
//     {
//       id: "1",
//       name: "Rahul Sharma",
//       bloodGroup: "A+",
//       age: 28,
//       phone: "+91 9876543210",
//       email: "rahul@example.com",
//       city: "Mumbai",
//       state: "Maharashtra",
//       lastDonated: "2024-01-15",
//       available: true,
//     },
//     {
//       id: "2",
//       name: "Priya Patel",
//       bloodGroup: "O+",
//       age: 32,
//       phone: "+91 8765432109",
//       email: "priya@example.com",
//       city: "New Delhi",
//       state: "Delhi",
//       lastDonated: "2023-12-20",
//       available: true,
//     },
//     {
//       id: "3",
//       name: "Amit Kumar",
//       bloodGroup: "B+",
//       age: 35,
//       phone: "+91 7654321098",
//       email: "amit@example.com",
//       city: "Bangalore",
//       state: "Karnataka",
//       lastDonated: "2024-02-10",
//       available: false,
//     },
//     {
//       id: "4",
//       name: "Sunita Singh",
//       bloodGroup: "AB+",
//       age: 29,
//       phone: "+91 8765432100",
//       email: "sunita@example.com",
//       city: "Chennai",
//       state: "Tamil Nadu",
//       lastDonated: "2024-01-20",
//       available: true,
//     },
//     {
//       id: "5",
//       name: "Raj Gupta",
//       bloodGroup: "O-",
//       age: 33,
//       phone: "+91 9876543211",
//       email: "raj@example.com",
//       city: "Pune",
//       state: "Maharashtra",
//       lastDonated: "2023-11-15",
//       available: true,
//     },
//   ];

//   // Store in localStorage if not already present
//   if (!localStorage.getItem("donors")) {
//     localStorage.setItem("donors", JSON.stringify(mockDonors));
//   }

//   donors = JSON.parse(localStorage.getItem("donors") || "[]");
// }

// Setup event listeners
// function setupEventListeners() {
//   // Search form on homepage
//   const searchForm = document.getElementById("searchForm");
//   if (searchForm) {
//     searchForm.addEventListener("submit", handleSearch);
//   }

// }


document.getElementById('logout-link').addEventListener('click', function (e) {
  e.preventDefault(); // prevent immediate navigation
  localStorage.removeItem('blood_donation_dashboard_state');

  // Then manually redirect or do logout logic
  window.location.href = '/Logout';
});

// Setup state-city handlers
function setupStateCityHandlers() {
  const stateSelects = document.querySelectorAll(
    'select[name="state"], #state',
  );
  stateSelects.forEach((stateSelect) => {
    stateSelect.addEventListener("change", function () {
      const selectedState = this.value;
      const citySelect = findCorrespondingCitySelect(this);

      if (citySelect) {
        populateCities(citySelect, selectedState);
      }
    });

    // Initialize cities if state is already selected
    if (stateSelect.value) {
      const citySelect = findCorrespondingCitySelect(stateSelect);
      if (citySelect) {
        populateCities(citySelect, stateSelect.value);
      }
    }
  });
}

// Find corresponding city select for a state select
function findCorrespondingCitySelect(stateSelect) {
  const form =
    stateSelect.closest("form") ||
    stateSelect.closest(".search-form") ||
    document;
  return (
    form.querySelector('select[name="city"], #city') ||
    form.querySelector('input[name="city"], #city')
  );
}

// Populate cities based on selected state
function populateCities(cityElement, selectedState) {
  const cities = stateCityMapping[selectedState] || [];

  if (cityElement.tagName.toLowerCase() === "select") {
    // Store current value
    const currentValue = cityElement.value;

    // For select elements
    cityElement.innerHTML = '<option value="">Select city</option>';
    cities.forEach((city) => {
      const option = document.createElement("option");
      option.value = city;
      option.textContent = city;
      cityElement.appendChild(option);
    });

    // Restore value if it exists in new list
    if (currentValue && cities.includes(currentValue)) {
      cityElement.value = currentValue;
    }
  } else {
    // For input elements, we can add a datalist for suggestions
    let datalist = document.getElementById("cityDatalist");
    if (!datalist) {
      datalist = document.createElement("datalist");
      datalist.id = "cityDatalist";
      cityElement.setAttribute("list", "cityDatalist");
      cityElement.parentNode.appendChild(datalist);
    }

    datalist.innerHTML = "";
    cities.forEach((city) => {
      const option = document.createElement("option");
      option.value = city;
      datalist.appendChild(option);
    });

    cityElement.placeholder = `Enter city in ${selectedState}`;
  }
}

// Handle search functionality
// function handleSearch(e) {
//   e.preventDeāfault();

//   const bloodGroup = document.getElementById("blood_group").value;
//   const state = document.getElementById("state").value;
//   const city = document.getElementById("city").value;

//   if (!bloodGroup && !state && !city) {
//     alert("Please select at least one search criterion");
//     return;
//   }

//   // Store search parameters
//   const searchParams = { bloodGroup, state, city };
//   localStorage.setItem("searchParams", JSON.stringify(searchParams));

//   // Redirect to dashboard with search parameters
//   const urlParams = new URLSearchParams(searchParams);
//   window.location.href = `/Dashboard/?${urlParams.toString()}`;

// }


// Filter donors based on search criteria
// function filterDonors(bloodGroup, state, city) {
//   return donors.filter((donor) => {
//     const bloodGroupMatch = !bloodGroup || donor.bloodGroup === bloodGroup;
//     const stateMatch = !state || donor.state === state;
//     const cityMatch =
//       !city || donor.city.toLowerCase().includes(city.toLowerCase());

//     return bloodGroupMatch && stateMatch && cityMatch;
//   });
// }

// Format date
function formatDate(dateString) {
  const date = new Date(dateString);
  return date.toLocaleDateString("en-IN", {
    year: "numeric",
    month: "long",
    day: "numeric",
  });
}

// Contact donor
function contactDonor(donorId) {
  const donor = donors.find((d) => d.id === donorId);
  if (donor && donor.available) {
    alert(
      `Contacting ${donor.name}...\nPhone: ${donor.phone}\nEmail: ${donor.email}`,
    );
  } else {
    alert("This donor is currently unavailable");
  }
}

// Utility functions
function showLoading(element) {
  element.innerHTML = '<div class="loading">Loading...</div>';
}

function hideLoading() {
  const loadingElements = document.querySelectorAll(".loading");
  loadingElements.forEach((el) => el.remove());
}
