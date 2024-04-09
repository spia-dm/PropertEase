import random
import json
house_url="https://i.ibb.co/4Y25cWk/ai-generative-exterior-of-modern-luxury-house-with-garden-and-beautiful-sky-photo.jpg"
city={
  "Maharashtra": [
    "Mumbai",
    "Pune",
    "Nagpur",
    "Nashik",
    "Thane",
    "Aurangabad",
    "Navi Mumbai",
    "Solapur",
    "Kalyan-Dombivali",
    "Vasai-Virar"
  ],
  "Uttar Pradesh": [
    "Lucknow",
    "Kanpur",
    "Varanasi",
    "Agra",
    "Meerut",
    "Allahabad",
    "Ghaziabad",
    "Noida",
    "Moradabad",
    "Aligarh"
  ],
  "Tamil Nadu": [
    "Chennai",
    "Coimbatore",
    "Madurai",
    "Tiruchirappalli",
    "Salem",
    "Tirunelveli",
    "Tiruppur",
    "Ambattur",
    "Thanjavur",
    "Dindigul"
  ],
  "Karnataka": [
    "Bangalore",
    "Mysore",
    "Hubli-Dharwad",
    "Mangalore",
    "Belgaum",
    "Gulbarga",
    "Davanagere",
    "Bellary",
    "Vijayapura",
    "Shimoga"
  ],
  "Gujarat": [
    "Ahmedabad",
    "Surat",
    "Vadodara",
    "Rajkot",
    "Bhavnagar",
    "Jamnagar",
    "Junagadh",
    "Gandhinagar",
    "Nadiad",
    "Anand"
  ],
  "West Bengal": [
    "Kolkata",
    "Howrah",
    "Asansol",
    "Siliguri",
    "Durgapur",
    "Bardhaman",
    "Malda",
    "Baharampur",
    "Kharagpur",
    "Raiganj"
  ],
  "Rajasthan": [
    "Jaipur",
    "Jodhpur",
    "Kota",
    "Bikaner",
    "Ajmer",
    "Udaipur",
    "Bhilwara",
    "Alwar",
    "Bharatpur",
    "Sikar"
  ],
  "Andhra Pradesh": [
    "Visakhapatnam",
    "Vijayawada",
    "Guntur",
    "Nellore",
    "Kurnool",
    "Kakinada",
    "Rajahmundry",
    "Tirupati",
    "Anantapur",
    "Vizianagaram"
  ],
  "Telangana": [
    "Hyderabad",
    "Warangal",
    "Nizamabad",
    "Karimnagar",
    "Ramagundam",
    "Khammam",
    "Mahbubnagar",
    "Nalgonda",
    "Adilabad",
    "Suryapet"
  ],
  "Madhya Pradesh": [
    "Indore",
    "Bhopal",
    "Jabalpur",
    "Gwalior",
    "Ujjain",
    "Sagar",
    "Dewas",
    "Satna",
    "Ratlam",
    "Rewa"
  ]
}
states = list(city.keys())
adjectives = [
    "Luxurious",
    "Modern",
    "Cozy",
    "Spacious",
    "Traditional",
    "Elegant",
    "Charming",
    "Luxury",
    "Seaside",
    "Contemporary",
    "Rustic",
    "Colonial",
    "Classic",
    "Grand",
    "Eco-Friendly",
    "Riverside",
    "Majestic",
    "Serenity",
    "Chic",
    "Serene",
    "Majestic",
    "3BHK",
    "2BHK",
    "1BHK",
    "4BHK",
    "Beautiful",
    "Stylish",
    "Comfortable",
    "Inviting",
    "Enchanting",
    "Sleek",
    "Gorgeous",
    "Tranquil",
    "Picturesque",
    "Exquisite",
    "Bright",
    "Airy",
    "Peaceful",
    "Whimsical",
    "Quaint",
    "Dreamy",
    "Unique",
    "Sunny",
    "Cosy",
    "Welcoming",
    "Romantic",
    "Spectacular",
    "Idyllic",
    "Modernistic",
    "Artistic",
    "Sustainable",
    "Exclusive",
    "Opulent",
    "Glamorous",
    "Meticulous",
    "Soothing",
    "Refined",
    "Calming",
    "Trendy",
    "Polished",
    "Harmonious",
    "Elevated",
    "Chic",
    "Impeccable",
    "Fresh",
    "Upscale",
    "Timeless",
    "Lavish",
    "Enthralling",
    "Regal",
    "Ethereal",
    "Sculptural",
    "Epic",
    "Lush",
    "Gleaming",
    "Radiant",
    "Plush",
    "Modernistic",
    "Smart",
    "Zen",
    "Palatial",
    "Breathtaking",
    "Sprawling",
    "Luxuriant",
    "Zenith",
    "Intriguing",
    "Sumptuous",
    "Extravagant",
    "Remarkable",
    "Enigmatic",
    "Refined",
    "Enriching",
    "Magnificent",
    "Transcendent",
    "Stunning",
    "Timeless",
    "Unforgettable",
    "Euphoric",
    "Visionary",
    "Panoramic",
    "Verdant"
]
house_types = [
    "Villa",
    "Apartment",
    "House",
    "Bungalow",
    "Penthouse",
    "Cottage",
    "Duplex",
    "Townhouse",
    "Mansion",
    "Flat"
]
data=[]
for i in range(1000):
    state = states[random.randint(0, len(states) - 1)]
    city_list = city[state]
    selected_city = city_list[random.randint(0, len(city_list) - 1)]
    adjective = adjectives[random.randint(0, len(adjectives) - 1)]
    house_type = house_types[random.randint(0, len(house_types) - 1)]
    price = "Rs." + str(random.randint(2000000, 100000000))
    size = str(random.randint(1000, 10000)) + " sqft"

    d = {
        "id": i + 1,
        "house_url": house_url,
        "house_name": f"{adjective} {house_type} in {selected_city}",
        "price": price,
        "location":selected_city+", "+state,
        "size": size,
        "likes": 0,
        "comments": [],
        "uploaded_by": "test",
        "description": ""
    }
    data.append(d)
with open("dataset.json", "w") as json_file:
    json.dump(data, json_file, indent=4)